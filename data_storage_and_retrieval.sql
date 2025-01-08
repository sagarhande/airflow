-- Data Storage
CREATE TABLE interactions (
    interaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER,
    action TEXT,
    timestamp TIMESTAMP,
    interaction_count INTEGER
);

-- Total number of interactions per day
SELECT DATE(timestamp) AS interaction_date, COUNT(*) AS total_interactions
FROM interactions
GROUP BY interaction_date;

-- Top 5 users by the number of interactions
SELECT user_id, COUNT(*) AS total_interactions
FROM interactions
GROUP BY user_id
ORDER BY total_interactions DESC
LIMIT 5;

-- Most interacted products based on the number of interactions
SELECT product_id, COUNT(*) AS interaction_count
FROM interactions
GROUP BY product_id
ORDER BY interaction_count DESC
LIMIT 1;


-- Optimization Techniques
-- Indexes: Creating indexes on user_id, product_id, and timestamp can significantly speed up the queries that involve these columns.

CREATE INDEX idx_user_id ON interactions(user_id);
CREATE INDEX idx_product_id ON interactions(product_id);
CREATE INDEX idx_timestamp ON interactions(timestamp);

