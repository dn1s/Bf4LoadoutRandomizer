from Bf4LoadoutRandomizer import Loadouts
from flask import Flask
from flask import render_template

app = Flask(__name__)

loadout = Loadouts()
loadout.get_data_from_csv()

@app.route("/")
def index():
    bf_class = loadout.choose_class()
    primary_weapon = loadout.choose_loadout(equipment_filter=bf_class)
    primary_weapon_attachments = loadout.choose_weapon_attachments(primary_weapon)
    secondary_weapon = loadout.choose_loadout(equipment_filter='Handgun')
    secondary_weapon_attachments = loadout.choose_weapon_attachments(secondary_weapon)
    granade = loadout.choose_loadout(equipment_filter='Granade')
    gadget = loadout.choose_loadout(equipment_filter=f'{bf_class}_gadgets')
    return render_template('index.html',
                           titel="Bf4LoadoutRandomizer",
                           description="Returns a randomized loadout option for battlefield 4", 
                           bf_class=bf_class, primary_weapon=primary_weapon, primary_weapon_attachments=primary_weapon_attachments,
                           secondary_weapon=secondary_weapon, secondary_weapon_attachments=secondary_weapon_attachments,
                           granade=granade, gadget=gadget)
