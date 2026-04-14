from endee import Endee

# Step 1: connect to Endee
client = Endee()

# Step 2: connect to same index
index = client.create_index(name="hospital", dimension=3)

# Step 3: query similar data
results = index.query(vector=[5, 10, 1], top_k=1)

print("Best match:", results)