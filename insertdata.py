#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import db,Category,Book,Chapter,Chunk,Audio

db.create_all()

hci=Category('HCI')
db.session.add(hci)

e=Book('The Design of Everyday Things','Donald A. Norman','Basic Books',1225,9780465050659,hci)
c=Book(u'設計的心理學 : 人性化的產品設計如何改變世界','Donald A. Norman',u'遠流出版社',4215,'9789573274582',hci)
db.session.add(e)
db.session.add(c)

e1=Chapter(1,e)
c1=Chapter(1,c)
db.session.add(e1)
db.session.add(c1)

for i in range(44):
	ch = Chunk('enc1_'+str(i+1)+'.png',e1)
	au = Audio('enc1_'+str(i+1)+'.wmv',ch)
	db.session.add(ch)
	db.session.add(au)

for i in range(35):
	ch = Chunk('cnc1_'+str(i+1)+'.png',c1)
	au = Audio('cnc1_'+str(i+1)+'.wmv',ch)
	db.session.add(ch)
	db.session.add(au)

db.session.commit()