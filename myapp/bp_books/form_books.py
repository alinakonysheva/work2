from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, RadioField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed


class EbookForm(FlaskForm):
    title = StringField('EBook title', id='ebook_title', validators=[DataRequired()])
    author_first_name = StringField('Author first name', id='ebook_author_first_name')
    author_last_name = StringField('Author last name', id='ebook_author_last_name', validators=[DataRequired()])
    # TODO: this field is allowed to be empty, redo
    author_middle_name = StringField('Author middle name', id='ebook_author_middle_name')
    release_year = IntegerField('Release year', id='ebook_release_year', validators=[DataRequired()])
    rating = FloatField('Rating', id='ebook_rating')
    pic = FileField('Picture', id='ebook_pic', validators=[FileAllowed(['jpg', 'png', 'svg', 'jpeg'], 'Images only!')])
    category = IntegerField('Category', id='ebook_category', validators=[DataRequired()])
    language = RadioField('Language', choices=[('ru', 'Russian'), ('nl', 'Nederlands'), ('en', 'English')],
                          id='ebook_language', validators=[DataRequired()])
    annotation = TextAreaField('Annotation', id='ebook_annotation')
    publisher = StringField('Publisher', id='ebook_publisher')
    size = FloatField('Size in Mb', id='ebook_size', validators=[DataRequired()])

    submit = SubmitField('Save', id='ebook_submit')


class AudiobookForm(FlaskForm):
    title = StringField('Audiobook title', id='audiobook_title', validators=[DataRequired()])
    author_first_name = StringField('Author first name', id='audiobook_author_first_name')
    author_last_name = StringField('Author last name', id='audiobook_author_last_name', validators=[DataRequired()])
    # TODO: this field is allowed to be empty, redo
    author_middle_name = StringField('Author middle name', id='audiobook_author_middle_name')
    release_year = IntegerField('Release year', id='audiobook_release_year', validators=[DataRequired()])
    rating = FloatField('Rating', id='audiobook_rating')
    pic = FileField('Picture', id='ebook_pic', validators=[FileAllowed(['jpg', 'png', 'svg', 'jpeg'], 'Images only!')])
    category = IntegerField('Category, number', id='audiobook_category', validators=[DataRequired()])
    language = RadioField('Language', choices=[('ru', 'Russian'), ('nl', 'Nederlands'), ('en', 'English')],
                          id='audiobook_language', validators=[DataRequired()])
    annotation = TextAreaField('Annotation', id='audiobook_annotation')
    publisher = StringField('Publisher', id='audiobook_publisher')
    reader_first_name = StringField('Reader, first name', id='audiobook_reader_first_name')
    reader_last_name = StringField('Reader, last name', id='audiobook_reader_last_name', validators=[DataRequired()])
    reader_middle_name = StringField('Reader, middle name', id='audiobook_reader_middle_name')
    duration_hours = IntegerField('Duration, hours', id='audiobook_duration_hours')
    duration_minutes = IntegerField('Duration, minutes', id='audiobook_duration_minutes')
    duration_seconds = IntegerField('Duration, seconds', id='audiobook_duration_seconds')

    submit = SubmitField('Save', id='audiobook_submit')


class PaperbookForm(FlaskForm):
    title = StringField('Paper book title', id='paperbook_title', validators=[DataRequired()])
    author_first_name = StringField('Author first name', id='paperbook_author_first_name')
    author_last_name = StringField('Author last name', id='paperbook_author_last_name', validators=[DataRequired()])
    # TODO: this field is allowed to be empty, redo
    author_middle_name = StringField('Author middle name', id='paperbook_author_middle_name')
    release_year = IntegerField('Release year', id='paperbook_release_year', validators=[DataRequired()])
    rating = FloatField('Rating', id='paperbook_rating')
    pic = FileField('Picture', id='ebook_pic', validators=[FileAllowed(['jpg', 'png', 'svg', 'jpeg'], 'Images only!')])
    category = IntegerField('Category, number', id='paperbook_category', validators=[DataRequired()])
    language = RadioField('Language', choices=[('ru', 'Russian'), ('nl', 'Nederlands'), ('en', 'English')],
                          id='paperbook_language', validators=[DataRequired()])
    annotation = TextAreaField('Annotation', id='paperbook_annotation')
    publisher = StringField('Publisher', id='paperbook_publisher')

    cover = RadioField('Cover', choices=[(1, 'Soft'), (2, 'Hard')], id='paperbook_cover')
    length = IntegerField('Length in cm, int', id='paperbook_length')
    width = IntegerField('Width in cm, int', id='paperbook_width')
    weight = IntegerField('Weight in gr, int', id='paperbook_weight')
    pages = IntegerField('Number of pages', id='paperbook_pages', validators=[DataRequired()])
    isbn = StringField('ISBN, 13 digits', id='paperbook_isbn', validators=[DataRequired()])
    submit = SubmitField('Save', id='paperbook_submit')


class SearchForm(FlaskForm):
    title = StringField('by title:', id='title')
    author_last_name = StringField('by author, last name', id='author_last_name')
    author_first_name = StringField('by author, first name', id='author_first_name')
    publisher = StringField('by publisher', id='publisher')
    submit = SubmitField('Find!', id='find')
