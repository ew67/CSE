states = {
    "CA": "California",
    "VA": "Virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada",

}
print(states["CA"])
print(states["NV"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045  # 39,557,045
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8517685  # 8,517,685
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718  # 6,042,718
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315  # 1,057,315

    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392  # 3,034,392
    },
}


print(nested_dictionary["NV"]["POPULATION"])

print(nested_dictionary["RI"]["NAME"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39557045,  # 39,557,045
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles",
        ]  # WATCH THE SQUARE BRACKETS
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8517685,  # 8,517,685
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexandria",
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6042718,  # 6,042,718
        "CITIES": [
            "Bethesda",
            "Baltimore",
            "Annapolis",
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,  # 1,057,315
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick",
        ]

    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3034392,  # 3,034,392
        "CITIES": [
            "Carson City",
            "Reno",
            "Las Vegas",
        ]
    },
}


print(complex_dictionary["RI"]["CITIES"][2])

# Open your notes, and get it to say "Virginia",
# Then get it to say "Bethesda"

print(complex_dictionary["MD"]["CITIES"][0])

print(complex_dictionary.keys())  # Lists all Keys available

print(nested_dictionary.items())  # Lists all Items in Keys

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

# We're going to make this look great...
for state, facts in complex_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)

        print("-" * 20)
    print('=' * 20)


# Other Notes


# Adding to a Dictionary

states['AL'] = "Alaska?"  # It isn't Alaska
print(states['AL'])

# Changing a dictionary value
states['AL'] = "Alabama"  # It's actually Alabama
print(states['AL'])
