from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.util import b64encode

from myapp.bp_books.constants import categories, languages, covers
from myapp import db
from sqlalchemy import Column, String, Integer, Float, Text, ForeignKey, LargeBinary

from myapp.bp_users.model_users import User


class Book(db.Model):
    __tablename__ = 'T_Book'
    id = Column(Integer, primary_key=True)
    _title = Column('F_TITLE', String(200))
    _author_first_name = Column('F_AUTHOR_FIRST_NAME', String(100))
    _author_last_name = Column('F_AUTHOR_LAST_NAME', String(100))
    _author_middle_name = Column('F_AUTHOR_MIDDLE_NAME', String(100))
    _release_year = Column('F_RELEASE_YEAR', Integer)
    _rating = Column('F_RATING', Float)
    pic = Column('F_PIC', LargeBinary(4294967295))
    _category = Column('F_CATEGORY', Integer)
    _language = Column('F_LANGUAGE', String(2))
    _annotation = Column('F_ANNOTATION', Text)
    _publisher = Column('F_PUBLISHER', String(200))
    __table_args__ = {'extend_existing': True}

    @declared_attr
    def wishlists(cls):
        return relationship('WishlistBook', back_populates='book')

    # wishlists = relationship('WishlistBook', back_populates='book')

    @hybrid_property
    def book_title(self) -> str:
        return str(self._title)

    @book_title.setter
    def book_title(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Title is too small')
        if len(v) > 200:
            raise ValueError('Title should be less than 200 symbols')
        self._title = v

    @hybrid_property
    def author_first_name(self) -> str:
        return str(self._author_first_name).capitalize()

    @author_first_name.setter
    def author_first_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('First name is too small')
        if len(v) > 100:
            raise ValueError('First name should be less than 100 symbols')
        self._author_first_name = v

    @hybrid_property
    def author_last_name(self) -> str:
        return str(self._author_last_name).capitalize()

    @author_last_name.setter
    def author_last_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Last name is too small')
        if len(v) > 100:
            raise ValueError('Last name should be less than 100 symbols')
        self._author_last_name = v

    @hybrid_property
    def author_middle_name(self) -> str:
        return str(self._author_middle_name).capitalize()

    @author_middle_name.setter
    def author_middle_name(self, value) -> None:
        v = value.strip()
        if len(v) > 100:
            raise ValueError('Middle name should be less than 100 symbols')
        self._author_middle_name = v

    @property
    def author_full_name(self) -> str:
        return f'{self._author_first_name} {self._author_middle_name} {self._author_last_name}'

    @hybrid_property
    def release_year(self) -> int:
        return int(self._release_year)

    @release_year.setter
    def release_year(self, value: int) -> None:
        v = value
        if v <= 1457:
            raise ValueError('First printed book appeared in 1457 year')
        today_year = datetime.today().year
        if v > today_year:
            raise ValueError(f'Year should be less than {today_year}')
        self._release_year = v

    @hybrid_property
    def rating(self) -> float:
        return float(self._rating)

    @rating.setter
    def rating(self, value) -> None:
        v = value
        if v < 0:
            raise ValueError('Rating should be positive number')
        if v > 10:
            raise ValueError(f'Rating should be less than 10')
        self._rating = v

    @hybrid_property
    def category(self) -> int:
        return int(self._category)

    @category.setter
    def category(self, value: int) -> None:
        category_options = categories.keys()
        if value in category_options:
            self._category = value
        else:
            raise ValueError(f'category should be in between {min(category_options)} and {max(category_options)}')

    @hybrid_property
    def language(self) -> str:
        return str(self._language)

    @language.setter
    def language(self, value) -> None:
        v = value
        if len(v) != 2:
            raise ValueError('Language should be set with 2 letters')
        if v in languages.keys():
            self._language = v
        else:
            raise ValueError('Language should be set with 2 existing abbreviation letters')

    @hybrid_property
    def annotation(self) -> str:
        return str(self._annotation)

    @annotation.setter
    def annotation(self, value) -> None:
        self._annotation = value

    @hybrid_property
    def publisher(self) -> str:
        return str(self._publisher)

    @publisher.setter
    def publisher(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('the name of the publisher is too small')
        if len(v) > 200:
            raise ValueError('the name of the publisher should be less than 200 symbols')
        self._publisher = v

    def pic_encoded(self):
        if self.pic:
            return b64encode(self.pic)
        else:
            return None

    @property
    def __str__(self) -> str:
        return f'{self._book_title} - {self.author_full_name}'


class AudioBook(Book):
    __tablename__ = "T_AUDIOBOOK"

    _reader_first_name = Column('F_READER_FIRST_NAME', String(100))
    _reader_last_name = Column('F_READER_LAST_NAME', String(100))
    _reader_middle_name = Column('F_READER_MIDDLE_NAME', String(100))
    _duration_hours = Column('F_DURATION_HOURS', Integer)
    _duration_minutes = Column('F_DURATION_MINUTES', Integer)
    _duration_seconds = Column('F_DURATION_SECONDS', Integer)
    __mapper_args__ = {'polymorphic_identity': 'T_AUDIOBOOK'}
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, ForeignKey('T_Book.id'), primary_key=True)

    @hybrid_property
    def reader_first_name(self) -> str:
        return str(self._reader_first_name).capitalize()

    @reader_first_name.setter
    def reader_first_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('First name is too small')
        if len(v) > 100:
            raise ValueError('First name should be less than 100 symbols')
        self._reader_first_name = v

    @hybrid_property
    def reader_last_name(self) -> str:
        return str(self._reader_last_name).capitalize()

    @reader_last_name.setter
    def reader_last_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('Last name is too small')
        if len(v) > 100:
            raise ValueError('Last name should be less than 100 symbols')
        self._reader_last_name = v

    @hybrid_property
    def reader_middle_name(self) -> str:
        return str(self._reader_middle_name).capitalize()

    @reader_middle_name.setter
    def reader_middle_name(self, value) -> None:
        v = value.strip()
        if len(v) > 100:
            raise ValueError('Middle name should be less than 100 symbols')
        self._reader_middle_name = v

    @hybrid_property
    def duration_hours(self) -> int:
        return self._duration_hours

    @duration_hours.setter
    def duration_hours(self, value) -> None:
        if value < 0:
            raise ValueError('duration hours have to be positive or 0')
        self._duration_hours = value

    @hybrid_property
    def duration_minutes(self) -> int:
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value) -> None:
        if value < 0:
            raise ValueError('duration minutes have to be positive or 0')
        if value >= 59:
            raise ValueError('duration minutes have to be less than 60')
        self._duration_minutes = value

    @hybrid_property
    def duration_seconds(self) -> int:
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, value) -> None:
        if value < 0:
            raise ValueError('duration seconds have to be positive or 0')
        if value >= 59:
            raise ValueError('duration seconds have to be less than 60')

        self._duration_seconds = value


class EBook(Book):
    __tablename__ = "T_EBOOK"

    # in MB
    size = Column('F_SIZE', Float)
    id = Column(Integer, ForeignKey('T_Book.id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'T_EBOOK'}
    __table_args__ = {'extend_existing': True}


class PaperBook(Book):
    __tablename__ = "T_PAPER_BOOK"
    # 1 or 2
    _cover = Column('F_COVER', String(1))
    # in cm
    _length = Column('F_LENGTH', Integer)
    # in cm
    _width = Column('F_WIDTH', Integer)
    # in g
    _weight = Column('F_WEIGHT', Integer)
    _pages = Column('F_PAGES', Integer)
    _isbn = Column('F_ISBN', String(15))
    __mapper_args__ = {'polymorphic_identity': 'T_PAPER_BOOK'}
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, ForeignKey('T_Book.id'), primary_key=True)

    @hybrid_property
    def cover(self):
        return self._cover

    @cover.setter
    def cover(self, value) -> None:
        if value in covers.keys():
            self._cover = value
        else:
            raise ValueError(f'Cover has to be one of values {covers.keys()}')

    @hybrid_property
    def length(self) -> int:
        return int(self._length)

    @length.setter
    def length(self, value: int) -> None:
        # the longest existing book
        if value > 300:
            raise ValueError('the length of the book can not be longer than 3m')

        if value <= 0:
            raise ValueError('the length of the book can not be 0 of negative')

        self._length = value

    @hybrid_property
    def width(self) -> int:
        return int(self._width)

    @width.setter
    def width(self, value: int) -> None:
        # the widest existing book
        if value > 300:
            raise ValueError('the width of the book can not be longer than 3m')

        if value <= 0:
            raise ValueError('the width of the book can not be 0 of negative')

        self._width = value

    @hybrid_property
    def weight(self) -> int:
        return int(self._weight)

    @weight.setter
    def weight(self, value: int) -> None:
        if value > 10000:
            raise ValueError('the weight of the book can not be bigger than 10kg')

        if value <= 0:
            raise ValueError('the weight of the book can not be 0 of negative')

        self._weight = value

    # pages
    @hybrid_property
    def pages(self) -> int:
        return int(self._pages)

    @pages.setter
    def pages(self, value: int) -> None:
        # the widest existing book
        if value > 23675:
            raise ValueError('the pages of the book can not be more than 23675')

        if value <= 0:
            raise ValueError('the pages of the book can not be 0 of negative')

        self._pages = value

    # isbn
    @hybrid_property
    def isbn(self) -> str:
        return self._isbn

    @isbn.setter
    def isbn(self, value: str) -> None:
        if len(value) != 13:
            raise ValueError('the isbn of the book can not be longer than 13 digit')

        self._isbn = value


class Wishlist(db.Model):
    __tablename__ = "T_WISHLIST"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    id_user = Column('F_USER_ID', ForeignKey(User.id), index=True)
    user = relationship('User', foreign_keys='Wishlist.id_user', back_populates="wishlist")

    @declared_attr
    def books(cls):
        return relationship('WishlistBook', back_populates='wishlist')


class WishlistBook(db.Model):

    __tablename__ = 'T_WISHLISTBOOK'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)

    id_wishlist = Column('id_wishlist', ForeignKey(Wishlist.id))

    book = relationship(Book, back_populates='wishlists')
    wishlist = relationship(Wishlist, back_populates='books')

    id_book = Column('Book_id', ForeignKey('T_Book.id'))

    __mapper_args__ = {'polymorphic_identity': 'T_WISHLISTBOOK', 'concrete': True}

    def __str__(self) -> str:
        return f'{self.id} - {self.id_book} - {self.id_wishlist} '
