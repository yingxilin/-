# 汽车知识图谱问答系统

这是一个基于Neo4j的汽车领域知识图谱问答系统。

## 项目结构
```
.
├── app/
│   ├── static/
│   ├── templates/
│   └── __init__.py
├── data/
│   └── car_kg_data.csv
├── scripts/
│   └── import_data.py
├── config.py
├── app.py
└── requirements.txt
```

## 环境要求
- Python 3.7+
- Neo4j 4.4+

## 安装步骤

1. 安装Neo4j数据库
   - 从[Neo4j官网](https://neo4j.com/download/)下载并安装Neo4j Desktop
   - 创建一个新的数据库实例
   - 设置数据库密码

2. 安装Python依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
   - 复制`.env.example`文件为`.env`
   - 填写Neo4j数据库连接信息

4. 导入数据
```bash
python scripts/import_data.py
```

5. 运行应用
```bash
python app.py
```

访问 http://localhost:5000 即可使用系统。

## 功能特点
- 支持汽车相关知识的自然语言查询
- 可视化知识图谱关系
- 基于Neo4j的高效查询
- 友好的Web界面

## 数据来源
使用开源的汽车知识图谱数据集，包含车型、品牌、性能参数等信息。
 