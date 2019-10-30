from basic_model_app import db, Puppy

###########################
###### CREATE ############
#########################
my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

###########################
###### READ ##############
#########################
all_puppies = Puppy.query.all()
print(all_puppies)
print('\n')

puppy_one = Puppy.query.get(1)
print(puppy_one)
print(puppy_one.age)
print('\n')

puppy_sam = Puppy.query.filter_by(name='Sammy') # Returns list
print(puppy_sam)
print('\n')

###########################
###### UPDATE ############
#########################
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

###########################
###### DELETE ############
#########################
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

all_puppies = Puppy.query.all() # list of all puppies in table
print(all_puppies)
