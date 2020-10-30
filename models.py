import datetime

from peewee import *

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    entry_id = AutoField()
    title = TextField()
    date = DateTimeField(default=datetime.datetime.now().strftime('%B %d, %Y'))
    time_spent = TextField()
    what_you_learned = TextField()
    resources_to_remember = TextField()
    tags = TextField()
    
    class Meta:
        database = DATABASE
        order_by = ('-date',)
        
    @classmethod
    def create_entry(cls, title, date, time_spent, what_you_learned, resources_to_remember, tags):
        cls.create(
            title=title,
            time_spent=time_spent,
            what_you_learned=what_you_learned,
            resources_to_remember=resources_to_remember,
            tags=tags
        )
            
            
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)
    DATABASE.close()
