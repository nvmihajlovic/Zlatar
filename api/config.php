<?php

/**
 * Database Configuration
 * Унеси своје податке за MySQL базу
 */

// MySQL connection parameters
define('DB_HOST', 'localhost');           // Обично 'localhost' на shared hosting-у
define('DB_NAME', 'your_database_name');  // Име твоје базе података
define('DB_USER', 'your_username');       // MySQL username
define('DB_PASS', 'your_password');       // MySQL password
define('DB_CHARSET', 'utf8mb4');

// Security settings
define('ALLOWED_ORIGINS', [
    'https://tvojdomen.com',
    'https://www.tvojdomen.com',
    'http://localhost',
    'http://127.0.0.1'
]);

// Rate limiting (опционално - број захтева по минути)
define('RATE_LIMIT_LIKES', 10);    // Максимум лајкова по минути
define('RATE_LIMIT_VIEWS', 100);   // Максимум прегледа по минути

/**
 * Get database connection
 */
function getDbConnection()
{
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
        $options = [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ];

        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        error_log("Database connection failed: " . $e->getMessage());
        http_response_code(500);
        echo json_encode(['error' => 'Database connection failed']);
        exit;
    }
}

/**
 * Validate CORS origin
 */
function validateOrigin()
{
    $origin = $_SERVER['HTTP_ORIGIN'] ?? '';

    if (in_array($origin, ALLOWED_ORIGINS)) {
        header("Access-Control-Allow-Origin: $origin");
        return true;
    }

    // Ако је локалан развој, дозволи
    if (strpos($origin, 'localhost') !== false || strpos($origin, '127.0.0.1') !== false) {
        header("Access-Control-Allow-Origin: $origin");
        return true;
    }

    return false;
}

/**
 * Get user identifier (за праћење лајкова)
 */
function getUserIdentifier()
{
    // Комбинација IP адресе и User Agent-а
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
    $userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'unknown';

    // Hash за приватност
    return hash('sha256', $ip . $userAgent);
}
