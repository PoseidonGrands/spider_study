from peewee import *

db = MySQLDatabase('csdn', host='127.0.0.1', port=3306, user='root', password='2280139492')


class BaseModel(Model):
    class Meta:
        database = db


class Post(BaseModel):
    _id = IntegerField(primary_key=True)
    author_name = CharField()
    author_id = CharField()
    title = CharField()
    content = TextField()
    create_at = DateField()
    view_num = IntegerField()
    comment_num = IntegerField()
    rating = IntegerField()
    status = IntegerField()


class Answer(BaseModel):
    post_id = IntegerField()
    author_name = CharField()
    author_id = CharField()
    content = TextField()
    comment_time = DateField()

    like_num = IntegerField()
    comment_num = IntegerField()
    rating = IntegerField()
    status = IntegerField()


class Author(BaseModel):
    user_id = IntegerField(primary_key=True)

    view_num = IntegerField()
    follow_num = IntegerField()
    fans_num = IntegerField()
    original_num = IntegerField()

    rank = IntegerField()
    ip = CharField()
    desc = TextField()
    join_time = DateField()


if __name__ == '__main__':
    db.create_tables([Post, Answer, Author])
