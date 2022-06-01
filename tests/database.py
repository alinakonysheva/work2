from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# needed for declaring tables
Base = declarative_base()

def create_database(engine_, do_erase=False):
    from myapp.bp_books.modal_books import PaperBook, EBook, AudioBook, Wishlist, WishlistBook, Book
    from myapp.bp_users.model_users import User

    """
    create the database
    """
    if do_erase:
        PaperBook.__table__.drop(bind=engine_)
        EBook.__table__.drop(bind=engine_)
        AudioBook.__table__.drop(bind=engine_)
        Wishlist.__table__.drop(bind=engine_)
        WishlistBook.__table__.drop(bind=engine_)
        User.__table__.drop(bind=engine_)
        Book.__table__.drop(bind=engine_)

        # Base.metadata.drop_all(bind=engine, tables=[ObjectName.__table__])

    # create tables
    Base.metadata.create_all(engine_)
engine = create_engine('sqlite://')
create_database(engine)