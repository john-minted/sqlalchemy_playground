from sqlalchemy import \
  create_engine, \
  Column, \
  Integer, \
  String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  fullname = Column(String)
  password = Column(String)

  def __repr__(self):
     return "<User(name='%s', fullname='%s', password='%s')>" % (
                          self.name, self.fullname, self.password)


# create db engine
engine = create_engine('sqlite:///tutorial.db', echo=True)
# create all db tables
Base.metadata.create_all(engine)

# grab a session
Session = sessionmaker(bind=engine)
session = Session()

# create a user object
ed_user = User(name='ed', fullname='Ed Jones', password='password')
session.add(ed_user)
john_user = User(name='john', fullname='John Jones', password='password')
session.add(john_user)

session.commit()

q = session.query(User).filter(User.password == 'password')
print '>> making call'
item = q.first()
print item.name
print '>> making call'
item = q.first()
print item.name
