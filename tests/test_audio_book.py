from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from myapp.bp_books.modal_books import AudioBook
from myapp.bp_books.constants import categories

C_TITLE = 'Staring at the Sun'
C_TITLE_2 = 'Staring at the Sun2'
C_INCORRECT_TITLE = str('[i for i in ...]')
C_AUTHOR_LAST_NAME = 'Yalom'
C_AUTHOR_LAST_NAME_2 = 'Yalom2'
C_AUTHOR_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_LAST_NAME_SHORT = ''
C_AUTHOR_FIRST_NAME = 'Irvin'
C_AUTHOR_FIRST_NAME_2 = 'Irvin2'
C_AUTHOR_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_FIRST_NAME_SHORT = ''
C_AUTHOR_MIDDLE_NAME = 'David'
C_AUTHOR_MIDDLE_NAME_2 = 'David_2'
C_AUTHOR_INCORRECT_MIDDLE_NAME_LONG = str('[i for i in ...]')
C_AUTHOR_INCORRECT_MIDDLE_NAME_SHORT = ''
C_RELEASE_YEAR = 2008
C_RELEASE_YEAR_2 = 2010
C_INCORRECT_RELEASE_YEAR_TO_SMALL = 1234
C_INCORRECT_RELEASE_YEAR_TO_BIG = 4321
C_RATING = 9.9
C_RATING_3 = 8.9
C_RATING_2 = 10.0
C_INCORRECT_RATING_TO_BIG = 11
C_INCORRECT_RATING_TO_SMALL = -1
C_CATEGORY = 3
C_CATEGORY_2 = 5
C_INCORRECT_CATEGORY = max(categories.keys()) + 1
C_LANGUAGE = "nl"
C_LANGUAGE_2 = "ru"
C_INCORRECT_LANGUAGE = "ne"
C_ANNOTATION = "Written in Irv Yalom's inimitable story-telling style, Staring at the Sun is a profoundly encouraging" \
               "approach to the universal issue of mortality. In this magisterial opus, capping a lifetime of work and" \
               "personal experience, Dr. Yalom helps us recognize that the fear of death is at the heart of much of " \
               "our anxiety. Such recognition is often catalyzed by an \"awakening experience\"—a dream, \" \
               \"or loss (the death of a loved one, divorce, loss of a job or home), illness, trauma, or aging."
C_ANNOTATION_2 = "Written in Irv Yalom's inimitable story-telling style, Staring at the Sun is a profoundly encouraging" \
                 "approach to the universal issue of mortality. In this magisterial opus, capping a lifetime of work and" \
                 "personal experience, Dr. Yalom helps us recognize that the fear of death is at the heart of much of " \
                 "our anxiety. Such recognition is often catalyzed by an \"awakening experience\"—a dream, \" \
                 \"or loss (the death of a loved one, divorce, loss of a job or home), illness, trauma, or aging.2"
C_INCORRECT_ANNOTATION = str('[i for i in ...]')
C_PUBLISHER = "Wiley"
C_PUBLISHER_2 = "Wiley2"
C_INCORRECT_PUBLISHER = str([1 for i in range(70)])
C_READER_LAST_NAME = 'Smith'
C_READER_LAST_NAME_2 = 'Smith2'
C_READER_INCORRECT_LAST_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_LAST_NAME_SHORT = ''
C_READER_FIRST_NAME = 'Black'
C_READER_FIRST_NAME_2 = 'Black2'
C_READER_INCORRECT_FIRST_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_FIRST_NAME_SHORT = ''
C_READER_MIDDLE_NAME = 'Nil'
C_READER_MIDDLE_NAME_2 = 'Nil2'
C_READER_INCORRECT_MIDDLE_NAME_LONG = str('[i for i in ...]')
C_READER_INCORRECT_MIDDLE_NAME_SHORT = ''
C_DURATION_HOURS = 2
C_DURATION_HOURS_2 = 4
C_DURATION_MINUTES = 50
C_DURATION_MINUTES_2 = 52
C_DURATION_SECONDS = 34
C_DURATION_SECONDS_2 = 36


class BaseDbTest(TestCase):
    engine = create_engine('sqlite://')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class AudioBookTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_audio_book(self):
        audio_book = AudioBook()
        audio_book.book_title = C_TITLE
        audio_book.author_last_name = C_AUTHOR_LAST_NAME
        audio_book.author_first_name = C_AUTHOR_FIRST_NAME
        audio_book.author_middle_name = C_AUTHOR_MIDDLE_NAME
        audio_book.release_year = C_RELEASE_YEAR
        audio_book.rating = C_RATING
        audio_book.category = C_CATEGORY
        audio_book.language = C_LANGUAGE
        audio_book.annotation = C_ANNOTATION
        audio_book.publisher = C_PUBLISHER
        audio_book.reader_first_name = C_READER_FIRST_NAME
        audio_book.reader_middle_name = C_READER_MIDDLE_NAME
        audio_book.reader_last_name = C_READER_LAST_NAME
        audio_book.duration_hours = C_DURATION_HOURS
        audio_book.duration_minutes = C_DURATION_MINUTES
        audio_book.duration_seconds = C_DURATION_SECONDS

        self.session.add(audio_book)
        self.session.commit()

        ab_from_query = self.session.query(AudioBook).get(1)
        self.assertEqual(ab_from_query.book_title, C_TITLE)
        self.assertEqual(ab_from_query.author_last_name, C_AUTHOR_LAST_NAME)
        self.assertEqual(ab_from_query.author_first_name, C_AUTHOR_FIRST_NAME)
        self.assertEqual(ab_from_query.author_middle_name, C_AUTHOR_MIDDLE_NAME)
        self.assertEqual(ab_from_query.release_year, C_RELEASE_YEAR)
        self.assertEqual(ab_from_query.rating, C_RATING)
        self.assertEqual(ab_from_query.category, C_CATEGORY)
        self.assertEqual(ab_from_query.language, C_LANGUAGE)
        self.assertEqual(ab_from_query.annotation, C_ANNOTATION)
        self.assertEqual(ab_from_query.publisher, C_PUBLISHER)
        self.assertEqual(ab_from_query.reader_first_name, C_READER_FIRST_NAME)
        self.assertEqual(ab_from_query.reader_middle_name, C_READER_MIDDLE_NAME)
        self.assertEqual(ab_from_query.reader_last_name, C_READER_LAST_NAME)
        self.assertEqual(ab_from_query.duration_hours, C_DURATION_HOURS)
        self.assertEqual(ab_from_query.duration_minutes, C_DURATION_MINUTES)
        self.assertEqual(ab_from_query.duration_seconds, C_DURATION_SECONDS)