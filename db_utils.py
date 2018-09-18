import logging
from sqlalchemy.exc import IntegrityError, DatabaseError, ProgrammingError, OperationalError
from helper import get_unique_id
from db_settings import session
from models import Storage
from collections import defaultdict

logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def get_details(model, id):
    try:
        data = session.query(model).filter(model.id == id).all()
    except ProgrammingError as e:
        logging.error(
            'Programming Exception {} occurred while updating {}'.format(e, id))
        return None
    except OperationalError as e:
        logging.error(
            'Operational Exception {} occurred while updating {}'.format(e, id))
        return None
    except DatabaseError as e:
        logging.error(
            'Database Exception {} occurred while inserting {}'.format(e, data))
        return None
    if not data:
        return None
    data = data[0]
    data = data.__dict__
    data.pop('_sa_instance_state', None)
    data['modified_date'] = data['modified_date'].strftime('%Y-%m-%d')
    if data:
        return data
    return None


def post_details(model, data):
    data['id'] = get_unique_id()
    try:
        session.add(model(**data))
        session.commit()
        return True
    except IntegrityError as e:
        session.rollback()
        logging.error(
            'Integrity Exception {} occurred while inserting {}'.format(e, data))
        return False
    except DatabaseError as e:
        session.rollback()
        logging.error(
            'Database Exception {} occurred while inserting {}'.format(e, data))
        # log it in sentry
        return False
    except ProgrammingError as e:
        session.rollback()
        logging.error(
            'Programming Exception {} occurred while inserting {}'.format(e, data))
        return False
    except OperationalError as e:
        session.rollback()
        logging.error(
            'Operational Exception {} occurred while updating {}'.format(e, id))
        return False


def put_details(model, id, data):
    try:
        session.query(model).filter(model.id == id).update(
            data, synchronize_session=False)
        session.commit()
        return True
    except IntegrityError as e:
        logging.error('Exception {} occurred while updating {}'.format(e, id))
        return False
    except ProgrammingError as e:
        logging.error('Exception {} occurred while updating {}'.format(e, id))
        return False
    except OperationalError as e:
        session.rollback()
        logging.error(
            'Operational Exception {} occurred while updating {}'.format(e, id))
        return False
    except DatabaseError as e:
        session.rollback()
        logging.error(
            'Database Exception {} occurred while inserting {}'.format(e, data))
        return False


def delete_details(model, id):
    to_be_deleted = session.query(model).get(id)
    if to_be_deleted:
        try:
            session.delete(to_be_deleted)
            session.commit()
        except IntegrityError as e:
            logging.error(
                'Exception {} occurred while updating {}'.format(e, id))
            return False
        except ProgrammingError as e:
            session.rollback()
            logging.error(
                'Exception {} occurred while updating {}'.format(e, id))
            return False
        except OperationalError as e:
            session.rollback()
            logging.error(
                'Operational Exception {} occurred while updating {}'.format(e, id))
            return False
        except DatabaseError as e:
            session.rollback()
            logging.error(
                'Database Exception {} occurred while inserting {}'.format(e, id))
            return False

    return False


def get_all(model):
    res = []
    for u in session.query(model).all():
        d = u.__dict__
        d['modified_date'] = d['modified_date'].strftime('%Y-%m-%d')
        d.pop('_sa_instance_state', None)
        res.append(d)
    return res


def get_storage_data(list_skuids):
    print(list_skuids)
    storage_records = session.query(Storage).filter(
        Storage.sku_id.in_(list_skuids)).order_by(Storage.stock.asc()).all()
    res = defaultdict(list)
    for record in storage_records:
        d = record.__dict__
        res[d['sku_id']].append((d['stock'], d['id']),)
    return dict(res)
