gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)

kimberly = {'name': "Kimberly Warner", 'availability': ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)
print(gamers)

gamers_data = [
    {'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]},
    {'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]},
    {'name': 'Michelle Reyes', 'availability': ["Wednesday", "Thursday", "Sunday"]},
    {'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]},
    {'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]},
    {'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]},
    {'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]},
    {'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]},
    {'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}
]

for gamer in gamers_data:
    add_gamer(gamer, gamers)

def build_daily_frequency_table():
    return {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }
count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

def find_best_night(availability_table):
    best_night = max(availability_table, key=availability_table.get)
    return best_night

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    return [gamer for gamer in gamers_list if day in gamer['availability']]

attending_game_night = available_on_night(gamers, game_night)

form_email = """
Dear {name},

The Sorcery Society is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

the Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")

unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer['availability']]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")