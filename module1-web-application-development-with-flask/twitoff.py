from TWITOFF.models import *

DB.create_all()

u1 = User(name = 'austen', id=5453)
t1=Tweet(text='whee', id=3)

DB.session.add(u1)
DB.session.add(t1)
DB.session.commit()

quit()





