import loadouts.loadout as loadout
import loadouts.selector as selector
from flask import Flask
from flask import render_template

app = Flask(__name__)

loadout = loadout.Loadout()
loadout_selector = selector.LoadoutSelector()
loadout_selector.filepath = 'loadouts'
loadout_selector.get_data_from_csv()

@app.route("/")
def index():
    bf_class = loadout_selector.choose_class()
    loadout.primary_weapon = loadout_selector.choose_loadout(equipment_filter=bf_class)
    loadout.primary_weapon_attachments = loadout_selector.choose_weapon_attachments(loadout.primary_weapon, unlock_filter=None)
    loadout.secondary_weapon = loadout_selector.choose_loadout(equipment_filter='Handgun')
    loadout.secondary_weapon_attachments = loadout_selector.choose_weapon_attachments(loadout.secondary_weapon, unlock_filter=None)
    loadout.granade = loadout_selector.choose_loadout(equipment_filter='Granade')
    loadout.gadgets = loadout_selector.choose_gadgets()
    return render_template('index.html',
                           titel="Bf4LoadoutRandomizer",
                           description="Returns a randomized loadout option for battlefield 4", 
                           bf_class=bf_class, primary_weapon=loadout.primary_weapon, primary_weapon_attachments=loadout.primary_weapon_attachments,
                           secondary_weapon=loadout.secondary_weapon, secondary_weapon_attachments=loadout.secondary_weapon_attachments,
                           granade=loadout.granade, gadgets=loadout.gadgets)
