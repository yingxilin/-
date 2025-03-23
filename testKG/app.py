from flask import Flask, render_template, request, jsonify
from neo4j import GraphDatabase
from config import Config
import re

app = Flask(__name__)

class Neo4jDatabase:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            Config.NEO4J_URI,
            auth=(Config.NEO4J_USER, Config.NEO4J_PASSWORD)
        )

    def close(self):
        self.driver.close()

    def query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters or {})
            return [record for record in result]

    def get_all_cars(self):
        query = "MATCH (c:Car) RETURN c.name as name ORDER BY c.name"
        return self.query(query)

db = Neo4jDatabase()

def parse_question(question):
    # 简单的问题解析逻辑
    for key in Config.QA_PATTERNS:
        if key in question:
            # 使用正则表达式提取车名
            match = re.search(r'(.+)的' + key, question)
            if match:
                return key, match.group(1)
    return None, None

@app.route('/')
def index():
    cars = db.get_all_cars()
    return render_template('index.html', cars=[record['name'] for record in cars])

@app.route('/query', methods=['POST'])
def query():
    question = request.json.get('question', '')
    
    # 解析问题
    attribute, entity = parse_question(question)
    
    if not attribute or not entity:
        return jsonify({
            'status': 'error',
            'message': '抱歉，我无法理解您的问题。请使用"XX的品牌/价格/发动机/变速箱"的形式提问。'
        })
    
    # 获取查询模板
    query_template = Config.QA_PATTERNS.get(attribute)
    if not query_template:
        return jsonify({
            'status': 'error',
            'message': '抱歉，我暂时无法回答这类问题。'
        })
    
    # 执行查询
    query = query_template.format(entity=entity)
    try:
        result = db.query(query)
        if result:
            return jsonify({
                'status': 'success',
                'answer': f"{entity}的{attribute}是：{result[0][0]}"
            })
        else:
            return jsonify({
                'status': 'error',
                'message': f'抱歉，没有找到{entity}的相关信息。'
            })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'查询出错：{str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True) 