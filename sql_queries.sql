-- Total claims cost
SELECT SUM(claim_amount) AS total_claim_cost
FROM claims_data;

-- Average claim amount by plan type
SELECT plan_type, AVG(claim_amount) AS avg_claim_cost
FROM claims_data
GROUP BY plan_type;

-- High cost procedures
SELECT procedure_category, SUM(claim_amount) AS total_cost
FROM claims_data
GROUP BY procedure_category
ORDER BY total_cost DESC;

-- In-network vs Out-of-network cost comparison
SELECT network_status, SUM(claim_amount) AS total_cost
FROM claims_data
GROUP BY network_status;
