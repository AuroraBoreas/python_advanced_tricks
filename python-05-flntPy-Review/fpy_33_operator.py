### start functional programming using operator module
import operator
import itertools
fmt = "\n{:-^50}"
# some iterable. fractal essences calculation
a = range(10, 1, -1)
print(fmt.format("simple usage"))
# get sum
ttl = itertools.accumulate(a, lambda x, y: x + y)
print(list(ttl))
# or alternative
ttl = itertools.accumulate(a, operator.add)
print(list(ttl))

# operator.itemgetter(), operator.attrgetter()
# more examples
metro_areas = [
('Tokyo','JP',36.933,(35.689722,139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
# operator.itemgetter(index) returns iterable[index] 
# it's similar with lambda: seq: seq[index]
print(fmt.format("sorting based on population(index2)"))
for city in sorted(metro_areas, key=operator.itemgetter(2)):
    print(city)
# if passing more paramters to operator.itemgetter() ...
print(fmt.format("passing multiple indexes(i.e 2 indexes)"))
city_name = operator.itemgetter(1, 0)
for city in sorted(metro_areas):
    print(city_name(city))

# operator.attrgetter(fields) ...
import collections
Latlong = collections.namedtuple('Latlong', 'Lat Lng')
# you can't do nested tuple inside a namedtuple...
# City = collections.namedtuple('City', 'Name short pop (lat., lng.)') # ValueError
City = collections.namedtuple('City', 'name short pop latlong')
redim_metro_areas = [City(name, cc, pop, Latlong(lat, lng))
            for name, cc, pop, (lat, lng) in metro_areas
]
print(fmt.format("operator.attrgetter()..."))
# for city in redim_metro_areas:
#     print(city)
name_lat = operator.attrgetter('name', 'latlong.Lat')
for city in sorted(redim_metro_areas, key=operator.attrgetter('latlong.Lng')):
    print(name_lat(city))