#!/usr/bin/env python3

from app import app
from models import db, Pet

with app.app_context():

    # 1. Clear existing data to prevent duplicates
    print("Deleting existing pets...")
    Pet.query.delete()

    # 2. Create a list of specific Pet instances
    print("Creating new pet records...")
    pets = [
        Pet(name="Fido", species="Dog"),
        Pet(name="Whiskers", species="Cat"),
        Pet(name="Hermie", species="Hamster"),
        Pet(name="Slither", species="Snake"),
        Pet(name="Bubbles", species="Fish"),
        Pet(name="Rex", species="Dog"),
        Pet(name="Goldie", species="Fish"),
        Pet(name="Mittens", species="Cat"),
        Pet(name="Polly", species="Bird"),
        Pet(name="Speedy", species="Turtle")
    ]

    # 3. Add all pets to the session
    db.session.add_all(pets)

    # 4. Commit the transaction to the database
    db.session.commit()

    print("Successfully seeded 10 pets!")