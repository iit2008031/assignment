import datetime

from sqlalchemy import (Text, Column, DateTime, orm,
                        Index, Integer, UniqueConstraint,
                        ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base

from db_settings import DB_STRING

base = declarative_base()


class SKU(base):
    __tablename__ = 'sku_details'
    id = Column(Text, nullable=False, primary_key=True)
    product_name = Column(Text, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)
    UniqueConstraint('product_name', name='sku_product_name_sku_const')
    __table_args__ = (Index('sku_product_idx', "product_name"),)


class Storage(base):
    __tablename__ = 'storage'
    id = Column(Text, nullable=False, primary_key=True)
    stock = Column(Integer, nullable=False)
    sku_id = Column(Text, ForeignKey('sku_details.id'),
                    nullable=False, primary_key=True)
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)


class Order(base):
    __tablename__ = 'order'
    id = Column(Text, nullable=False, primary_key=True)
    customer_name = Column(Text, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (Index('name_idx', "customer_name"),)


class OrderLine(base):
    __tablename__ = 'order_line'
    id = Column(Text, nullable=False, primary_key=True)
    sku_id = Column(Text, ForeignKey('sku_details.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    modified_date = Column(DateTime, default=datetime.datetime.utcnow)
    __table_args__ = (Index('order_line_sku_id', "sku_id"),)

if __name__ == '__main__':
    orm.configure_mappers()
    db_engine = create_engine(DB_STRING)
    base.metadata.create_all(db_engine)
