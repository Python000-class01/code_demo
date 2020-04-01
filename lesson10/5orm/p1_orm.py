# pip install pymysql
# pip install SQLAlchemy


########### 连接数据库
from sqlalchemy import create_engine

engine = create_engine(
        "mysql+pymysql://root:rootroot@localhost:3306/test?charset=utf8", 
        echo=True)
# echo=True：用于显示SQLAlchemy在操作数据库时所执行的SQL语句情况，
# 相当于一个监视器，可以清楚知道执行情况。

############ 创建数据表
from sqlalchemy import Column, Integer, String, DateTime 
# 常用数据类型

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Mytable(Base):
    # 表名
    __tablename__ ="mytable"
    # 字段，属性
    id = Column(Integer, primary_key=True)
    name = Column(String(10), unique=True)
    age = Column(Integer)

Base.metadata.create_all(engine)

############## 删除表
Base.metadata.drop_all(engine)

# 添加数据，创建一个会话对象，用于执行SQL语句
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind = engine)
session = DBSession()
new_data = Mytable(name='John', age=10)
session.add(new_data)
session.commit()
session.close()

# 更新数据
# 使用update更新
session.query(Mytable).filter_by(id=1).update({Mytable.age:12})
session.commit()
session.close()

# 使用赋值方式更新
get_data = session.query(Mytable).filter_by(id=1).first()
get_data.age = 14
session.commit()
session.close()

# 查询所有数据
# select * from mytable;
get_data = session.query(Mytable).all()
for i in get_data:
    print(f'我的名字:{i.name}')
    print(f'我的年龄:{i.age}')
session.close()

# 设置筛选条件
get_data = session.query(Mytable.name, Mytable.age).filter_by(id=1).all()
for i in get_data:
    print(f'我的名字:{i.name}')
    print(f'我的年龄:{i.age}')
session.close()

# 多条件查询
# and
get_data = session.query(Mytable.name, Mytable.name).filter(Mytable.id>2, Mytable.name=='Tango').first()

# or
from sqlalchemy import or_
session.query(Mytable).filter(or_(Mytable.id>2, Mytable.name=='Tango')).all()

# 多表 join
# join为内连，如果需要使用外连把join换成outerjoin就好
get_data = session.query(Mytable).join(Mytable2).filter(Mytable.id>=2).all()

# 直接执行SQL语句
sql = "select * from mytable "
session.excute(sql)
session.commit()
