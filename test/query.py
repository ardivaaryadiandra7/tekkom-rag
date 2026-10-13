from qdrant_client import QdrantClient, models

client = QdrantClient(url="http://localhost:6333")

response = client.query_points(
    collection_name="hello",
    query=[2,3,4,2],
    limit=2,
    with_payload=True
)
print(response)