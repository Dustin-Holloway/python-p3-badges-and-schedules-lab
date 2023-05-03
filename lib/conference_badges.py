def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    badge =  [f"Hello, my name is {name}." for name in names]
    return badge

def assign_rooms(names):
    numbers = range(1,9)
    room_assignment = [f"Hello, {name}! You'll be assigned to room {n}!" for name, n in zip(names, numbers)]
    return room_assignment

def printer(names):
    badges = batch_badge_creator(names)
    room_numbers = assign_rooms(names)
    for badge in (badges):
        print(badge)
    for num in room_numbers:
        print(num)
    

