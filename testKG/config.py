import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7687')
    NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
    NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'password')
    
    # 知识图谱配置
    RELATIONSHIPS = [
        '品牌',
        '车型',
        '价格',
        '发动机',
        '变速箱',
        '燃料类型',
        '车身结构',
        '最大功率',
        '最大扭矩'
    ]
    
    # 问答模板
    QA_PATTERNS = {
        '品牌': 'MATCH (n:Car)-[:属于]->(b:Brand) WHERE n.name = "{entity}" RETURN b.name',
        '价格': 'MATCH (n:Car) WHERE n.name = "{entity}" RETURN n.price',
        '发动机': 'MATCH (n:Car) WHERE n.name = "{entity}" RETURN n.engine',
        '变速箱': 'MATCH (n:Car) WHERE n.name = "{entity}" RETURN n.transmission',
    } 