## **QUICK START:**

This is a loadout randomizer for battlefield 4 written in python

This script can be run as flask site or just from loadout.py directly

Example output from standalone:

```
Class: Support, Weapon: RPK-12 - Attachments: ['M145 (3.4X)', 'Vertical Grip', 'Magnifier (2X)', 'Flash Hider'], Handgun: SW40 - Attachments: ['Delta (RDS)', 'Laser Sight', 'Compensator'], Granade: M34 Incendiary, Gadget_one: M224 Mortar, Gadget_two: Ammo Pack
```

Run as standalone:
```
cd Bf4LoadoutRandomizer
python3 ./loadout.py
```

Python Flask module has to be installed to run as website:
```
pip install Flask
```

Run as website:
```
cd bf4LoadoutRandomizer
flask --app loadouts/website run
```