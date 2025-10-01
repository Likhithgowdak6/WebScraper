# Install pymilvus first if not installed:
# pip install pymilvus

from pymilvus import connections, utility, Collection

# 1️⃣ Connect to Milvus
connections.connect(
    alias="default",
    host="localhost",
    port="19530"
)

# 2️⃣ List all collections
collections = utility.list_collections()
print("Collections in Milvus:", collections)

# 3️⃣ For each collection, drop it safely
for coll_name in collections:
    # Drop the collection
    if utility.has_collection(coll_name):
        utility.drop_collection(coll_name)
        print(f"Collection '{coll_name}' has been dropped.")
    else:
        print(f"Collection '{coll_name}' does not exist.")
