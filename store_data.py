from endee import Endee

client = Endee()

index = client.create_index(name="hospital", dimension=3)

index.upsert([
    {"id": "1", "vector": [5, 10, 1], "meta": {"doctor": "Dr.A"}},
    {"id": "2", "vector": [3, 8, 1], "meta": {"doctor": "Dr.A"}},
])

print("Data stored successfully ✅")