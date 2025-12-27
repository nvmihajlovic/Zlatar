<?php

/**
 * Blog Stats API
 * Endpoint за добијање и ажурирање статистике блог постова
 */

require_once 'config.php';

// CORS headers
validateOrigin();
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json');

// Handle preflight OPTIONS request
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$db = getDbConnection();

/**
 * GET /api/blog-stats.php?action=get&post_id=blog-post-1
 * Добија статистику за пост
 */
if ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['action']) && $_GET['action'] === 'get') {
    $postId = $_GET['post_id'] ?? '';

    if (empty($postId)) {
        http_response_code(400);
        echo json_encode(['error' => 'Missing post_id']);
        exit;
    }

    try {
        $stmt = $db->prepare("
            SELECT likes, views 
            FROM blog_stats 
            WHERE post_id = :post_id
        ");
        $stmt->execute(['post_id' => $postId]);
        $stats = $stmt->fetch();

        if (!$stats) {
            // Ако пост не постоји, креирај га са 0 лајкова и прегледа
            $stmt = $db->prepare("
                INSERT INTO blog_stats (post_id, likes, views) 
                VALUES (:post_id, 0, 0)
            ");
            $stmt->execute(['post_id' => $postId]);

            $stats = ['likes' => 0, 'views' => 0];
        }

        // Провери да ли је корисник лајковао
        $userIdentifier = getUserIdentifier();
        $stmt = $db->prepare("
            SELECT COUNT(*) as has_liked 
            FROM blog_likes 
            WHERE post_id = :post_id AND user_identifier = :user_id
        ");
        $stmt->execute([
            'post_id' => $postId,
            'user_id' => $userIdentifier
        ]);
        $likeStatus = $stmt->fetch();

        echo json_encode([
            'success' => true,
            'likes' => (int)$stats['likes'],
            'views' => (int)$stats['views'],
            'hasLiked' => (bool)$likeStatus['has_liked']
        ]);
    } catch (PDOException $e) {
        error_log("Error getting stats: " . $e->getMessage());
        http_response_code(500);
        echo json_encode(['error' => 'Failed to get stats']);
    }

    exit;
}

/**
 * POST /api/blog-stats.php
 * Body: {"action": "like", "post_id": "blog-post-1"}
 * Тогглује лајк за пост
 */
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = json_decode(file_get_contents('php://input'), true);
    $action = $input['action'] ?? '';
    $postId = $input['post_id'] ?? '';

    if (empty($postId)) {
        http_response_code(400);
        echo json_encode(['error' => 'Missing post_id']);
        exit;
    }

    try {
        $db->beginTransaction();
        $userIdentifier = getUserIdentifier();

        // LIKE ACTION
        if ($action === 'like') {
            // Провери да ли корисник већ лајковао
            $stmt = $db->prepare("
                SELECT COUNT(*) as count 
                FROM blog_likes 
                WHERE post_id = :post_id AND user_identifier = :user_id
            ");
            $stmt->execute([
                'post_id' => $postId,
                'user_id' => $userIdentifier
            ]);
            $exists = $stmt->fetch();

            if ($exists['count'] > 0) {
                // UNLIKE - уклони лајк
                $stmt = $db->prepare("
                    DELETE FROM blog_likes 
                    WHERE post_id = :post_id AND user_identifier = :user_id
                ");
                $stmt->execute([
                    'post_id' => $postId,
                    'user_id' => $userIdentifier
                ]);

                // Смањи бројач
                $stmt = $db->prepare("
                    UPDATE blog_stats 
                    SET likes = GREATEST(0, likes - 1)
                    WHERE post_id = :post_id
                ");
                $stmt->execute(['post_id' => $postId]);

                $action_result = 'unliked';
            } else {
                // LIKE - додај лајк
                $stmt = $db->prepare("
                    INSERT INTO blog_likes (post_id, user_identifier) 
                    VALUES (:post_id, :user_id)
                ");
                $stmt->execute([
                    'post_id' => $postId,
                    'user_id' => $userIdentifier
                ]);

                // Повећај бројач
                $stmt = $db->prepare("
                    UPDATE blog_stats 
                    SET likes = likes + 1 
                    WHERE post_id = :post_id
                ");
                $stmt->execute(['post_id' => $postId]);

                $action_result = 'liked';
            }

            $db->commit();

            // Врати нову статистику
            $stmt = $db->prepare("
                SELECT likes, views 
                FROM blog_stats 
                WHERE post_id = :post_id
            ");
            $stmt->execute(['post_id' => $postId]);
            $stats = $stmt->fetch();

            echo json_encode([
                'success' => true,
                'action' => $action_result,
                'likes' => (int)$stats['likes'],
                'views' => (int)$stats['views']
            ]);
        }

        // INCREMENT VIEW
        elseif ($action === 'view') {
            $stmt = $db->prepare("
                INSERT INTO blog_stats (post_id, views) 
                VALUES (:post_id, 1)
                ON DUPLICATE KEY UPDATE views = views + 1
            ");
            $stmt->execute(['post_id' => $postId]);

            $db->commit();

            // Врати нову статистику
            $stmt = $db->prepare("
                SELECT likes, views 
                FROM blog_stats 
                WHERE post_id = :post_id
            ");
            $stmt->execute(['post_id' => $postId]);
            $stats = $stmt->fetch();

            echo json_encode([
                'success' => true,
                'action' => 'view_incremented',
                'views' => (int)$stats['views']
            ]);
        } else {
            $db->rollBack();
            http_response_code(400);
            echo json_encode(['error' => 'Invalid action']);
        }
    } catch (PDOException $e) {
        if ($db->inTransaction()) {
            $db->rollBack();
        }
        error_log("Error processing action: " . $e->getMessage());
        http_response_code(500);
        echo json_encode(['error' => 'Failed to process action']);
    }

    exit;
}

// Invalid method
http_response_code(405);
echo json_encode(['error' => 'Method not allowed']);
