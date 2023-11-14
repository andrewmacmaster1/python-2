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

def ex4():
    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

    def get_people(people):
        return [person['name'] for person in people if person['age'] >= 15]
    
    print(get_people(people_list))

def ex5():
    class WordCounter:
        def __init__(self, sentence):
            self.sentence = sentence

        def count_words(self):
            self.word_count = len(self.sentence.split())
        
        def get_word_count(self):
            return self.word_count
        
        def get_shortest_word(self):
            shortest = None
            for word in self.sentence.split():
                if not shortest: shortest = word
                if len(word) < len(shortest): shortest = word

            return len(shortest)
        
        def get_longest_word(self):
            longest = None
            for word in self.sentence.split():
                if not longest: longest = word
                if len(word) > len(longest): longest = word

            return len(longest)
        
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.

def ex6():
    class TaxMan:
        def __init__(self, items, tax):
            self.items = items
            self.tax = float(tax[:-1])/100
            self.total = 0

        def calc_total(self):
            total = 0
            for item in self.items:
                total += item['price'] + item['price']*self.tax
            
            self.total = total

        def get_total(self):
            return self.total
        
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())