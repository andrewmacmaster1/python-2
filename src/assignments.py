# define your methods here.
# ex1() - ex10()

def ex1():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def sort_people(people, field, direction):
        people.sort(reverse=(direction=='desc'),key=lambda p: p[field])

    sort_people(people_list, 'weight', 'asc')
    print(people_list)

def ex2():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def filter_males(people):
        return list(filter(lambda p: p['sex'] == 'male', people))
    
    filtered_list = filter_males(people_list)
    print(filtered_list)

def ex3():
    people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]

    def calc_bmi(people):
        for person in people:
            person['bmi'] = round(person['weight_kg'] / person['height_meters'] ** 2, 1)

        return people
    
    new_people_list = calc_bmi(people_list)
    print(new_people_list)