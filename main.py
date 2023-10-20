from Person import Person

p1 = Person("Mike", 27,90)
p1.print_info()
p1.get_older(3)
p1.save_to_json("Mike.json")

p2 = Person(None, None, None)
p2.load_from_json("Mike.json")
p2.print_info()