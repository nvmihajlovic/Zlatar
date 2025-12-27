-- Supabase SQL Schema for Blog Statistics
-- Run this in Supabase SQL Editor after creating your project

-- 1. Create blog_stats table
CREATE TABLE IF NOT EXISTS blog_stats (
    id BIGSERIAL PRIMARY KEY,
    post_id TEXT UNIQUE NOT NULL,
    likes INTEGER DEFAULT 0,
    views INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Create blog_likes table (tracks who liked what)
CREATE TABLE IF NOT EXISTS blog_likes (
    id BIGSERIAL PRIMARY KEY,
    post_id TEXT NOT NULL,
    user_fingerprint TEXT NOT NULL,
    liked_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(post_id, user_fingerprint)
);

-- 3. Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_blog_stats_post_id ON blog_stats(post_id);
CREATE INDEX IF NOT EXISTS idx_blog_likes_post_id ON blog_likes(post_id);
CREATE INDEX IF NOT EXISTS idx_blog_likes_fingerprint ON blog_likes(user_fingerprint);

-- 4. Enable Row Level Security (RLS)
ALTER TABLE blog_stats ENABLE ROW LEVEL SECURITY;
ALTER TABLE blog_likes ENABLE ROW LEVEL SECURITY;

-- 5. Create policies - Allow everyone to read
CREATE POLICY "Enable read access for all users" ON blog_stats
    FOR SELECT USING (true);

CREATE POLICY "Enable read access for all users" ON blog_likes
    FOR SELECT USING (true);

-- 6. Create policies - Allow anonymous inserts/updates
CREATE POLICY "Enable insert for all users" ON blog_stats
    FOR INSERT WITH CHECK (true);

CREATE POLICY "Enable update for all users" ON blog_stats
    FOR UPDATE USING (true);

CREATE POLICY "Enable insert for all users" ON blog_likes
    FOR INSERT WITH CHECK (true);

CREATE POLICY "Enable delete for all users" ON blog_likes
    FOR DELETE USING (true);

-- 7. Insert initial data for all blog posts
INSERT INTO blog_stats (post_id, likes, views) VALUES
    ('blog-post-1', 42, 1250),
    ('blog-post-2', 38, 980),
    ('blog-post-3', 45, 1100),
    ('blog-post-4', 36, 870),
    ('blog-post-5', 41, 1050),
    ('blog-post-6', 39, 920),
    ('blog-post-7', 43, 1180),
    ('blog-post-8', 37, 890),
    ('blog-post-9', 44, 1200),
    ('blog-post-10', 40, 1020),
    ('blog-post-11', 46, 1300),
    ('blog-post-12', 52, 1420)
ON CONFLICT (post_id) DO NOTHING;

-- 8. Create function to automatically update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- 9. Create trigger for auto-updating timestamp
CREATE TRIGGER update_blog_stats_updated_at 
    BEFORE UPDATE ON blog_stats
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Done! Your tables are ready to use.
