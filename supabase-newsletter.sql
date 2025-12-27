-- Supabase SQL Schema for Newsletter System
-- Add this to your existing Supabase project (same database as blog stats)

-- 1. Create newsletter_subscribers table
CREATE TABLE IF NOT EXISTS newsletter_subscribers (
    id BIGSERIAL PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    subscribed_at TIMESTAMPTZ DEFAULT NOW(),
    is_active BOOLEAN DEFAULT true,
    source TEXT DEFAULT 'website',
    user_fingerprint TEXT,
    ip_address TEXT,
    user_agent TEXT
);

-- 2. Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_newsletter_email ON newsletter_subscribers(email);
CREATE INDEX IF NOT EXISTS idx_newsletter_active ON newsletter_subscribers(is_active);
CREATE INDEX IF NOT EXISTS idx_newsletter_date ON newsletter_subscribers(subscribed_at DESC);

-- 3. Enable Row Level Security
ALTER TABLE newsletter_subscribers ENABLE ROW LEVEL SECURITY;

-- 4. Create policies - Allow everyone to subscribe (insert)
CREATE POLICY "Enable insert for all users" ON newsletter_subscribers
    FOR INSERT WITH CHECK (true);

-- 5. Create policies - Only allow reading active subscribers (for admin)
CREATE POLICY "Enable read access for all users" ON newsletter_subscribers
    FOR SELECT USING (is_active = true);

-- 6. Create function to prevent duplicate subscriptions
CREATE OR REPLACE FUNCTION subscribe_newsletter(
    p_email TEXT,
    p_name TEXT DEFAULT NULL,
    p_fingerprint TEXT DEFAULT NULL,
    p_ip TEXT DEFAULT NULL,
    p_user_agent TEXT DEFAULT NULL
)
RETURNS JSON AS $$
DECLARE
    v_result JSON;
    v_subscriber_id BIGINT;
    v_is_new BOOLEAN;
BEGIN
    -- Check if email already exists
    SELECT id INTO v_subscriber_id
    FROM newsletter_subscribers
    WHERE email = p_email;
    
    IF v_subscriber_id IS NOT NULL THEN
        -- Email exists, check if active
        SELECT is_active INTO v_is_new
        FROM newsletter_subscribers
        WHERE id = v_subscriber_id;
        
        IF v_is_new THEN
            -- Already subscribed
            v_result := json_build_object(
                'success', false,
                'message', 'Ова email адреса је већ пријављена',
                'already_subscribed', true
            );
        ELSE
            -- Reactivate subscription
            UPDATE newsletter_subscribers
            SET is_active = true,
                subscribed_at = NOW()
            WHERE id = v_subscriber_id;
            
            v_result := json_build_object(
                'success', true,
                'message', 'Добродошли назад! Ваша претплата је поново активирана',
                'reactivated', true
            );
        END IF;
    ELSE
        -- New subscription
        INSERT INTO newsletter_subscribers (
            email, name, user_fingerprint, ip_address, user_agent
        ) VALUES (
            p_email, p_name, p_fingerprint, p_ip, p_user_agent
        )
        RETURNING id INTO v_subscriber_id;
        
        v_result := json_build_object(
            'success', true,
            'message', 'Успешно сте се пријавили за newsletter!',
            'subscriber_id', v_subscriber_id,
            'is_new', true
        );
    END IF;
    
    RETURN v_result;
END;
$$ LANGUAGE plpgsql;

-- 7. Create function to unsubscribe
CREATE OR REPLACE FUNCTION unsubscribe_newsletter(p_email TEXT)
RETURNS JSON AS $$
DECLARE
    v_result JSON;
    v_rows_affected INTEGER;
BEGIN
    UPDATE newsletter_subscribers
    SET is_active = false
    WHERE email = p_email AND is_active = true;
    
    GET DIAGNOSTICS v_rows_affected = ROW_COUNT;
    
    IF v_rows_affected > 0 THEN
        v_result := json_build_object(
            'success', true,
            'message', 'Успешно сте одјављени са newsletter-а'
        );
    ELSE
        v_result := json_build_object(
            'success', false,
            'message', 'Email адреса није пронађена'
        );
    END IF;
    
    RETURN v_result;
END;
$$ LANGUAGE plpgsql;

-- 8. Create view for active subscribers (useful for exports)
CREATE OR REPLACE VIEW active_subscribers AS
SELECT 
    id,
    email,
    name,
    subscribed_at,
    source
FROM newsletter_subscribers
WHERE is_active = true
ORDER BY subscribed_at DESC;

-- 9. Grant access to view
GRANT SELECT ON active_subscribers TO anon, authenticated;

-- Done! Newsletter system is ready.

-- USEFUL QUERIES:
-- =================

-- Count active subscribers
-- SELECT COUNT(*) FROM newsletter_subscribers WHERE is_active = true;

-- Get all subscribers (for export to Mailchimp/SendGrid)
-- SELECT email, name, subscribed_at FROM active_subscribers;

-- Get subscriber stats by date
-- SELECT DATE(subscribed_at) as date, COUNT(*) as new_subscribers
-- FROM newsletter_subscribers
-- WHERE is_active = true
-- GROUP BY DATE(subscribed_at)
-- ORDER BY date DESC;

-- Recent signups (last 7 days)
-- SELECT email, name, subscribed_at
-- FROM newsletter_subscribers
-- WHERE subscribed_at > NOW() - INTERVAL '7 days'
-- AND is_active = true
-- ORDER BY subscribed_at DESC;
