# quick python overview

# ##############################
# string
# ##############################
my_name = "Python"
# s = f"I'm learning {my_name}"
# print(s)


# ##############################
# list
# ##############################
# defining a list named: departments
# and initializing it with three elements
# a list is an array, indexed beginning with '0'

departments = ["T98700", "T96800", "T91000"]

# print(departments[0])
# print(departments[1])
# print()
# print(departments[:2])
# print()
# print(departments[::-1])

# # append a str
# departments.append("BSS1000")
# print(departments)
# print(type(departments[3]))
#
# # append an int
# departments.append(777777)
# print(departments)
# print(type(departments[4]))

# for dept in departments:
#     print(dept)


# ##############################
# dictionary
# ##############################
# we can define it using dept id's as keys
# and some descr as the value for each key
departments_dict = {
    "T98700": "descr for T98700",
    "T96800": "descr for T96800",
    "T91000": "descr for T91000",
}

# print(departments_dict)
# print()
# print(departments_dict['T96800'])
# print()
# for x in departments_dict:
#     print(x)
# for key, val in departments_dict.items():
#     print(key, " --->", val)


# ##############################
# list of dicts
# ##############################

my_list_of_dicts = [
    {'id': 100},
    {'id': 101},
    {'id': 1000},
    {'id': 2000}
]

# print(my_list_of_dicts)
# print()
# print(my_list_of_dicts[2]['id'])
# print()
# print(my_list_of_dicts[2].get('id'))
# print()
# # by default, when using .get(), if the key doesn't exist, it returns None
# print(my_list_of_dicts[2].get('id_number'))
# print()
# # or we can specify what to return if key doesn't exist
# print(my_list_of_dicts[2].get('id_number', 'Key Error!'))


# ##############################
# ##############################
# here, we are defining a dictionary named: teams
# this dictionary has two keys: ppmd, bss
# each key has a corresponding value
# in this case, the value for each key is a list (a list of dictionaries)

teams = {
    "ppmd": [
        {
            "name": "joe",
            "id": 199
        },
        {
            "name": "john",
            "id": 100
        }
    ],
    "bss": [{"name": "jane", "id": 125},
            {"name": "tom", "id": 114}
            ]
}

# print(teams)
# print()
# print(teams.get('ppmd'))
# print()
# print(teams.get('ppmd')[0])
# print(teams.get('ppmd')[1])
# print()
# print(teams.get('ppmd')[1].get('name'))
# print()
# for team in teams:
#     print(f"looking at {team}.")
#     print(teams.get(team))
#     for user in teams.get(team):
#         print(user)
#         print(f"{user.get('name')} has this id: {user.get('id')}")
