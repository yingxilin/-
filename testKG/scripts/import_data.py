import pandas as pd
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

class Neo4jImporter:
    def __init__(self):
        self.uri = os.getenv('NEO4J_URI')
        self.user = os.getenv('NEO4J_USER')
        self.password = os.getenv('NEO4J_PASSWORD')
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

    def clear_database(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def create_constraints(self):
        with self.driver.session() as session:
            # 创建唯一约束
            session.run("CREATE CONSTRAINT car_name IF NOT EXISTS FOR (c:Car) REQUIRE c.name IS UNIQUE")
            session.run("CREATE CONSTRAINT brand_name IF NOT EXISTS FOR (b:Brand) REQUIRE b.name IS UNIQUE")

    def import_car_data(self, file_path):
        df = pd.read_csv(file_path)
        
        with self.driver.session() as session:
            for _, row in df.iterrows():
                # 创建汽车节点
                session.run("""
                    MERGE (c:Car {name: $name})
                    SET c.price = $price,
                        c.engine = $engine,
                        c.transmission = $transmission,
                        c.fuel_type = $fuel_type,
                        c.body_type = $body_type,
                        c.power = $power,
                        c.torque = $torque
                """, {
                    'name': row['name'],
                    'price': row['price'],
                    'engine': row['engine'],
                    'transmission': row['transmission'],
                    'fuel_type': row['fuel_type'],
                    'body_type': row['body_type'],
                    'power': row['power'],
                    'torque': row['torque']
                })

                # 创建品牌节点并建立关系
                session.run("""
                    MERGE (b:Brand {name: $brand})
                    WITH b
                    MATCH (c:Car {name: $car_name})
                    MERGE (c)-[:属于]->(b)
                """, {
                    'brand': row['brand'],
                    'car_name': row['name']
                })

def main():
    importer = Neo4jImporter()
    try:
        print("清空数据库...")
        importer.clear_database()
        
        print("创建约束...")
        importer.create_constraints()
        
        print("导入数据...")
        importer.import_car_data('data/car_kg_data.csv')
        
        print("数据导入完成！")
    finally:
        importer.close()

if __name__ == "__main__":
    main() 