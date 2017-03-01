# creating a mapping of state to abbreviation

states = {
    'Texas': 'TX',
    'Illinois': 'IL',
    'Arizona': 'AZ',
    'California': 'CA',
    'Washington': 'WA',
    'New York': 'NY'
}

# creating a basic set of states and some cities in them

cities = {
    'TX': 'Austin',
    'IL': 'Chicago',
    'AZ': 'Phoenix',
    'CA': 'San Francisco'
}

# adding some more cities
cities['WA'] = 'Seattle'
cities['NY'] = 'New York City'

# print out some cities
print '-' * 10
print "Texas has:", cities['TX']
print "Illinois has:", cities['IL']

# print out some cities
print '-' * 10
print "Texas' abbreviation is:", states['Texas']
print "California's abbreviation is:", states['California']

# do the same but use the state and then the cities dictionary
print '-' * 10
print "Arizona has:", cities[states["Arizona"]]
print "California has:", cities[states["California"]]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for state, city in cities.items():
    print "%s is located in the great state of %s" % (city, state)

# now add state abbreviation, adding detail to the previous printout
print '-' * 10
for state, abbrev in states.items():
    print "The state of %s is abbreviated %s and has a city called %s in the great state" % \
          (state, abbrev, cities[abbrev])

print '-' * 10
# Now try to get a state abbreviation for something that is not in *your* dictionary... yet
state = states.get("Hawaii")

if not state:
    print "Sorry, no Hawaii"

# get a city with a default value
city = cities.get('HI', 'Does Not Exist')
print "The city for the state 'HI' is: %s" % city