from models import db, Pet
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    pet_1 = Pet(name="Arthur", species="Cat", available=True)
    pet_2 = Pet(name="Missile", species="Dog", age=50, notes="good dog", photo_url='https://upload.wikimedia.org/wikipedia/en/b/be/Missile_Ghost_Trick.jpg', available=False)

    db.session.add(pet_1)
    db.session.add(pet_2)
    db.session.commit()
    