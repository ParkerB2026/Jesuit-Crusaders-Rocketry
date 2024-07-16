import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#Hohmann Transfer ∆v Calculator by Parker Bailey
#Message
print("""Hohmann Transfer ∆v Calculator by Parker Bailey

""")
#_________________________________________________Dictionaries_________________________________________________

#Spacecraft data (dictionary)
spacecraft_data = {

    #Mars spacecraft
    "Mars Reconnaissance Orbiter": {"total_mass": 2180, "dry_mass": 1031, "wet_mass": 1149, "isp": 311},
    "MAVEN (Mars Atmosphere and Volatile EvolutioN)": {"total_mass": 2454, "dry_mass": 1902, "wet_mass": 552, "isp": 320},
    "Mars Global Surveyor (MGS)": {"total_mass": 1060, "dry_mass": 533, "wet_mass": 527, "isp": 310},
    "Mars Global Surveyor (MGS)": {"total_mass": 1060, "dry_mass": 533, "wet_mass": 527, "isp": 310},
    #Jupiter spacecraft
    "Juno": {"total_mass": 3625, "dry_mass": 1593, "wet_mass": 2032, "isp": 317},
    "Galileo": {"total_mass": 2223, "dry_mass": 1391, "wet_mass": 832, "isp": 316},
    "Europa Clipper": {"total_mass": 6000, "dry_mass": 2900, "wet_mass": 3100, "isp": 557}, 
    #Saturn spacecraft
    "Cassini": {"total_mass": 5712, "dry_mass": 2523, "wet_mass": 2189, "isp": 308},
}

#Planet data (dictionary)
planet_data = {
    "Sun": {"mass": 1.9891e30, "radius": 696340, "color": "yellow"},
    "Mercury": {"mass": 3.3011e23, "radius": 2439.7, "color": "gray"},
    "Venus": {"mass": 4.8675e24, "radius": 6051.8, "color": "navajowhite"},
    "Earth": {"mass": 5.97237e24, "radius": 6371.0, "color": "dodgerblue"},
    "Mars": {"mass": 6.4171e23, "radius": 3389.5, "color": "tomato"},
    "Jupiter": {
        "mass": 1.8982e27,
        "radius": 69911.0,
        "color": "orange",
        "ring_color": "lightcoral",
        "rings": [
            [92000000, 122500000, "Halo Ring"],
            [122500000, 129000000, "Main Ring"],
            [129000000, 160000000, "Gossamer Rings"],
        ]
    },
    "Saturn": {
        "mass": 5.6834e26,
        "radius": 58232.0,
        "color": "gold",
        "ring_color": "wheat",
        "rings": [
            [66000000, 74500000, "D Ring"],
            [74500000, 91700000, "C Ring"],
            [91700000, 117600000, "B Ring"],
            [136700000, 180600000, "A Ring"],
            [140200000, 165500000, "F Ring"],
            [167000000, 174000000, "G Ring"],
            [180000000, 300000000, "E Ring"]
        ]
    },
    "Uranus": {
        "mass": 8.6810e25,
        "radius": 25362.0,
        "color": "paleturquoise",
        "ring_color": "silver",
        "rings": [
            [46000000, 49600000, "Epsilon Ring"],
            [51000000, 55000000, "Delta Ring"],
            [54000000, 57000000, "Gamma Ring"],
            [58000000, 60000000, "Beta Ring"],
            [61000000, 62500000, "Alpha Ring"]
        ]
    },
    "Neptune": {
        "mass": 1.02413e26,
        "radius": 24622.0,
        "color": "dodgerblue",
        "ring_color": "tomato",
        "rings": [
            [29300000, 29700000, "Adams Ring"],
            [29100000, 29600000, "Le Verrier Ring"],
            [32000000, 34000000, "Arago Ring"],
            [34800000, 35400000, "Galle Ring"],
            [35400000, 35700000, "Lassell Ring"]
        ]
    }
}

#_________________________________________________Planet Data_________________________________________________

#Message
print("""Input Values

Planetary Information
""")

#Planet Input
planet_name = input("Primary Body: ").capitalize()

#Fetch planet mass and radius
if planet_name in planet_data:
    #Assign mass, radius, and color to variables
    m = planet_data[planet_name] ["mass"] 
    r = planet_data[planet_name] ["radius"] * 1000
    color_planet = planet_data[planet_name]["color"]
    rings = planet_data[planet_name]["rings"]
    ring_color = planet_data[planet_name] ["ring_color"]
    print(f"The mass of {planet_name} is {m} kg.")
    print(f"The radius of {planet_name} is {r} m.")
    print(f"Rings data for {planet_name}:")
    for ring in rings:
        print(f"  - {ring[2]}: Inner radius {ring[0]} km, Outer radius {ring[1]} km")
    
else:
    print("""
Planet not found. Please enter a valid planet name (Mercury, Venus, Earth, etc.).
""")
    planet_name = input("Primary Body: ").capitalize()

#_________________________________________________Spacecraft Data_________________________________________________

#Spacecraft Input
print("""
Spacecraft Information
""")
spacecraft_name = str(input("Spacecraft name (if not applicable, input 'none'): ")).capitalize()

if spacecraft_name in spacecraft_data:
    t_m = spacecraft_data[spacecraft_name] ["total_mass"]
    d_m = spacecraft_data[spacecraft_name] ["dry_mass"]
    w_m = spacecraft_data[spacecraft_name] ["wet_mass"]
    i_s_p = spacecraft_data[spacecraft_name] ["isp"]
    spacecraft_delta_v = i_s_p * 9.81 * np.log(t_m / d_m)
    print(f"Total mass is {t_m} kg")
    print(f"Dry mass is {d_m} kg")
    print(f"Wet mass is {w_m} kg")
    print(f"Propulsion Isp is {i_s_p} seconds")
else:
    print("Spacecraft not found, please input another spacecraft name")
    spacecraft_name = str(input("Spacecraft name (if not applicable, input 'none'): ")).capitalize()
if spacecraft_name.upper() == "NONE":
    spacecraft_total_mass = float(input("Total mass of spacecraft (kg): "))
    spacecraft_dry_mass = float(input("Dry mass of spacecraft (kg): "))
    spacecraft_i_s_p = float(input("Propulsion Isp (seconds) (if unknown, input '0'): "))
    spacecraft_delta_v = i_s_p * 9.81 * np.log(t_m / d_m)
    if spacecraft_i_s_p == 0:
        spacecraft_delta_v = float(input("Spacecraft ∆v (ms^s-1): "))

#_________________________________________________Orbital Information_________________________________________________

#orbital Values
G = 6.67e-11
µ = G * m #Gravitational Parameter for Earth

#Message
print("""
Hohmann Transfer Orbit Information
""")

#Orbital Inputs
r_p_a = float(input("Periapsis of orbit A: "))
r_a_a = float(input("Apoapsis of Orbit A: "))
r_p_b = float(input("Semi-major axis of Orbit B (circular orbit): "))

#_________________________________________________Calculated Values_________________________________________________

a_a = round((r_p_a + r_a_a) / 2, 4)#Semi-major axis of orbit A

a_t = round((r_p_a + r_p_b) / 2, 4) #Semi-major axis of transfer orbit

a_b = round(r_p_b, 4) #Semi-major axis of orbit B (target orbit)

e_a = round((r_a_a - r_p_a) / (r_a_a + r_p_a), 4)

e_t = round((r_p_b - r_p_a) / (r_p_b + r_p_a), 4)

e_b = 0

v_a_i = (µ * ((2 / r_p_a) - (1 / a_a))) ** 0.5 #Velocity at burn position of orbit A

v_a_t = (µ * ((2 / r_p_a) - (1 / a_t))) ** 0.5 #Velocity at burn point of transfer orbit

delta_v_t = round(v_a_t - v_a_i, 4) #Difference of orbit A and transfer orbit velocity at burn point: ∆v required

v_p_b = (µ * ((2 / r_p_b) - (1 / a_t))) ** 0.5 #Velocity at orbit B semi-major distance

v_b = (µ / a_b) ** 0.5 #Circular velocity of orbit B

delta_v_c = round(v_b - v_p_b, 4) #Difference of transfer orbit and target orbit (circular): ∆v required

delta_t_t = (2 * np.pi * np.sqrt((a_t ** 3)/ µ)) / 3600

delta_t_t_half = round(((2 * np.pi * np.sqrt((a_t ** 3)/ µ)) / 3600) / 2, 4)

#_________________________________________________Graphing_________________________________________________

#Subplot 1: Trajectory
theta = np.linspace(0, 2 * np.pi, 1000) # Defining theta input

fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'polar': True})

#Orbit A
o_a = (a_a * (1 - e_a**2)) / (1 + e_a * np.cos(theta))
ax.plot(theta, o_a, color='black', linestyle='-', label=f'Orbit A (Initial Orbit): a={a_a}, e={e_a}')

#Transfer Orbit
o_t = (a_t * (1 - e_t**2)) / (1 + e_t * np.cos(theta))
ax.plot(theta, o_t, color='red', linestyle='--', label=f'Transfer Orbit: a={a_t}, e={e_t}')

#Orbit B
o_b = (a_b * (1 - e_b**2)) / (1 + e_b * np.cos(theta))
ax.plot(theta, o_b, color='black', linestyle='-', label=f'Orbit B (Target Orbit): a={a_b}, e={e_b}')

#Primary body
r_circle = np.ones_like(theta) * r

ax.fill(theta, r_circle, color=color_planet, linestyle='-', linewidth=1, label=f'{planet_name}: r={r} meters')

#Ringed bodies
for inner, outer, ring_name in rings:
    ring_inner_radius = np.ones_like(theta) * inner
    ring_outer_radius = np.ones_like(theta) * outer
    ax.fill_between(theta, ring_inner_radius, ring_outer_radius, color=ring_color, alpha=0.32, edgecolor='black', linewidth=0.5)

#Adding ring names to the legend
for inner, outer, ring_name in rings:
    r_inner = np.ones_like(theta) * inner  
    r_outer = np.ones_like(theta) * outer
    ax.plot([], [], color=ring_color, alpha=0.75, label=ring_name)  # Add empty plot for legend

#∆v Text box
ax.set_title(f'{spacecraft_name} Hohmann Transfer Orbit Visual Centralized Around {planet_name}')
ax.legend(loc ='upper left')

textstr = '\n'.join([
    f'Apoapsis Raise ∆v: {delta_v_t} ms^-1',
    f'Circularization ∆v: {delta_v_c} ms^-1',
    f'Transfer period between Orbit A & B: {delta_t_t_half} hrs',
])
ax.text(0.95, 0.95, textstr, ha='right', va='top', transform=ax.transAxes, 
        bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 10}, fontsize=7, color='black')

#Subplot 2: Gravitational Acceleration vs. time

# Show the plot
plt.show()

#_________________________________________________Printed Values_________________________________________________

#Print
print(e_a)
print(e_b)
print(e_t)
print(v_a_i)
print(v_a_t)
print(v_p_b)
print(v_b)
print(delta_v_t)
print(delta_v_c)
print(delta_t_t)










