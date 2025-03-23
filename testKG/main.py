from py2neo import Graph, Node, Relationship

# 连接到本地的 Neo4j 数据库（默认地址是 localhost:7687）
graph = Graph("bolt://localhost:7687", auth=("neo4j", "YXLyingxilin715"))

# 创建一些节点
alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
charlie = Node("Person", name="Charlie")

# 将节点添加到图中
graph.create(alice)
graph.create(bob)
graph.create(charlie)

# 创建关系
knows_alice_bob = Relationship(alice, "KNOWS", bob)
knows_bob_charlie = Relationship(bob, "KNOWS", charlie)

# 将关系添加到图中
graph.create(knows_alice_bob)
graph.create(knows_bob_charlie)

# 查询并打印图中的节点
print("Nodes in the graph:")
for node in graph.nodes:
    print(node)

# 查询并打印 Alice 的朋友
print("\nAlice's friends:")
for friend in graph.match(nodes=[alice], r_type="KNOWS"):
    print(friend.end_node["name"])
