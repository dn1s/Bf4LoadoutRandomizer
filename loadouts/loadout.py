# Loadout
import loadouts.selector as selector

class Loadout:
    def __init__(self):
        self.primary_weapon = None
        self.primary_weapon_attachments = []
        self.secondary_weapon = None
        self.secondary_weapon_attachments = []
        self.granade = None
        self.gadgets = None


if __name__ == '__main__':
    gear = {}
    # This can be set to absolute path to bf4_attachments.csv file for convenience
    filepath = 'loadouts'

    loadout = Loadout()
    loadout_selector = selector.LoadoutSelector()
    loadout_selector.filepath = filepath
    loadout_selector.get_data_from_csv()
    bf_class = loadout_selector.choose_class()
    loadout.primary_weapon = loadout_selector.choose_loadout(equipment_filter=bf_class)
    loadout.primary_weapon_attachments = loadout_selector.choose_weapon_attachments(loadout.primary_weapon, unlock_filter=None)
    loadout.secondary_weapon = loadout_selector.choose_loadout(equipment_filter='Handgun')
    loadout.secondary_weapon_attachments = loadout_selector.choose_weapon_attachments(loadout.secondary_weapon, unlock_filter=None)
    loadout.granade = loadout_selector.choose_loadout(equipment_filter='Granade')
    loadout.gadgets = loadout_selector.choose_gadgets()

    print(f'Class: {bf_class}, Weapon: {loadout.primary_weapon} - Attachments: {loadout.primary_weapon_attachments}, \
            Handgun: {loadout.secondary_weapon} - Attachments: {loadout.secondary_weapon_attachments}, \
            Granade: {loadout.granade}, Gadget_one: {loadout.gadgets[0][0]}, Gadget_two: {loadout.gadgets[1][0]}')
