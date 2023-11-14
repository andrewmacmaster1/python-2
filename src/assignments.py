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