import time
from sharkdash import db, SharkSign, SharkSignHistory


db.create_all()
sign1 = SharkSign('Scarborough', True)
sign2 = SharkSign('Fremantle', True)

db.session.add(sign1)
db.session.add(sign2)
db.session.commit()

sign1history1 = SharkSignHistory(1, 1)
time.sleep(1)
sign1history2 = SharkSignHistory(2, 1)

db.session.add(sign1history1)
db.session.add(sign1history2)
db.session.commit()
