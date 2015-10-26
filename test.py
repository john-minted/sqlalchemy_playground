from sqlalchemy import \
  create_engine, \
  Column, \
  Integer, \
  String, \
  ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()


class Product(Base):
  __tablename__ = 'product'

  id = Column(Integer, primary_key=True)
  sku = Column(String)

  project_id = Column(
    Integer,
    ForeignKey('product_project.id'),
    nullable=True)

  project = relationship(
    'ProductProject',
    backref=backref('products'))

  def __repr__(self):
     return "<Product(sku='{0}')>".format(self.sku)


class ProductProject(Base):
  __tablename__ = 'product_project'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(String)

  def __repr__(self):
    return "<ProductProject(name='{0}', description='{1}')>".format(
        self.name, self.description)


# create db engine
engine = create_engine('sqlite:///tutorial.db', echo=True)
# create all db tables
Base.metadata.create_all(engine)

# grab a session
Session = sessionmaker(bind=engine)
session = Session()

# create product project
project = ProductProject(name='snow', description='lalala')
# commit names so we have ids
session.add(project)
session.commit()

# create a user object
product1 = Product(sku='sku1', project_id=project.id)
product2 = Product(sku='sku2', project_id=project.id)
product3 = Product(sku='sku3', project_id=project.id)
session.add(product1)
session.add(product2)
session.add(product3)
session.commit()

q = session.query(ProductProject).filter(ProductProject.id==project.id)
res_project = q.first()

print '========'
print 'project'
print '========'

print 'check 1 -----------'
print 'project.products'
for product in project.products:
  print 'product.sku: ' + str(product.sku)
print 'check 2 -----------'
print 'project.products'
for product in project.products:
  print 'product.sku: ' + str(product.sku)

print 'check 3 -----------'
print ' > delete products'
q = session.query(Product)
q = q.join(ProductProject, ProductProject.id == Product.project_id)
q = q.filter(ProductProject.id == project.id)
products = q.all()
print ' > len products: ' + str(len(products))
for product in products:
  session.delete(product)

session.commit()

print 'check 4 -----------'
print ' > delete products?'
q = session.query(Product)
q = q.join(ProductProject, ProductProject.id == Product.project_id)
q = q.filter(ProductProject.id == project.id)
products = q.all()
print ' > len products: ' + str(len(products))
