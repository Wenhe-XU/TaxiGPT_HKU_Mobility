from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# 连接到数据库
engine = create_engine('postgresql://postgres:Xxh135792468@localhost/OPENITS')
metadata = MetaData()
idf_files = Table('idf_files', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('content', String))

metadata.create_all(engine)  # 确保表存在

# 读取 IDF 文件
with open(r'E:\dissertation\ENERGYPLUS\9021005053130.idf', 'r') as file:  # 确保路径正确
    idf_content = file.read()

# 将 IDF 内容存储到数据库
ins = idf_files.insert().values(content=idf_content)

# 使用上下文管理器来确保事务提交
with engine.connect() as conn:
    conn.execute(ins)
    conn.commit()  # 确保事务提交