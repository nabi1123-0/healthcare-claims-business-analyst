import pandas as pd

# Load claims data
df = pd.read_csv("claims_data.csv")

# Total claims cost
total_claim_cost = df["claim_amount"].sum()

# Average claim cost by plan type
avg_by_plan = df.groupby("plan_type")["claim_amount"].mean()

# Total cost by procedure category
cost_by_procedure = df.groupby("procedure_category")["claim_amount"].sum()

# Network cost comparison
network_cost = df.groupby("network_status")["claim_amount"].sum()

print("Total Claims Cost:")
print(total_claim_cost)

print("\nAverage Claim Cost by Plan Type:")
print(avg_by_plan)

print("\nTotal Cost by Procedure Category:")
print(cost_by_procedure)

print("\nNetwork Cost Comparison:")
print(network_cost)
