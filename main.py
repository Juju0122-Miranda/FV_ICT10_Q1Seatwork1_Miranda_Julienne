# Seatwork 1
from pyscript import display, document


fullname = 'Julienne Iliana T. Miranda'  # string
ag3_s = 15  # integer
Hei8th = 152  # integer
Dream_countries =  ["Switzerland", "China", "Norway"]   # list
student_type = False  # boolean
dictionary = {"color": "royal blue", "car_brand": "Honda", "shoe_size": 7, "best_friend": "Mary"} #  dict
fav_fruits = ["mango", "sugar apple", "banana", "strawberry", "melon"]  # list
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")  #tuple


display(f'Hi! I am {fullname} and I am {ag3_s} years old.', target="result") #display fullname and age
display(f'My height in cm is {Hei8th}.', target="result") #display height
display(f'My dream destinations are {Dream_countries}.', target="result") #display dream countries
display(f'I am an old student: {student_type}.', target="result") #display student
display(f'My favorite color is {dictionary["color"]}, a car brand that I like is {dictionary["car_brand"]}, my shoe size is {dictionary["shoe_size"]}, and my best friend is {dictionary["best_friend"]}.', target="result") #display dictionary
display(f'My favorite fruits are {fav_fruits}.', target="result") #display fav_fruits
display(f'The days of the week are {days}.', target="result") #display days 