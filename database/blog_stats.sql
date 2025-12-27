-- Blog Statistics Database Schema
-- Креирај ову табелу у твојој MySQL бази података

CREATE TABLE IF NOT EXISTS blog_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id VARCHAR(50) NOT NULL UNIQUE,
    likes INT DEFAULT 0,
    views INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_post_id (post_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Табела за праћење ко је лајковао (за превенцију дупликата)
CREATE TABLE IF NOT EXISTS blog_likes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id VARCHAR(50) NOT NULL,
    user_identifier VARCHAR(255) NOT NULL,
    liked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_like (post_id, user_identifier),
    INDEX idx_post_user (post_id, user_identifier)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Иницијализација података за постојеће постове
INSERT INTO blog_stats (post_id, likes, views) VALUES
    ('blog-post-1', 42, 1250),
    ('blog-post-2', 38, 980),
    ('blog-post-3', 45, 1100),
    ('blog-post-4', 52, 1420),
    ('blog-post-5', 36, 890),
    ('blog-post-6', 41, 1050),
    ('blog-post-7', 48, 1180),
    ('blog-post-8', 39, 920),
    ('blog-post-9', 44, 1090),
    ('blog-post-10', 50, 1310),
    ('blog-post-11', 37, 870),
    ('blog-post-12', 43, 1020)
ON DUPLICATE KEY UPDATE post_id=post_id;
