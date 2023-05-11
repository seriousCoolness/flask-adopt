from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

app.config['SECRET_KEY'] = 'secret_key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
with app.app_context():
    db.create_all()

@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet addition form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template(
            "pet_add_form.html", form=form)
    

@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet_details(id):
    """Shows pet stats and displays form to edit them."""

    pet = Pet.query.get_or_404(id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        
        db.session.commit()
        return redirect('/')
    else:
        return render_template(
            "pet_details.html", pet=pet, form=form)
