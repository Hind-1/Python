x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Bryant', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 15, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0]=15
# print(x)
# # Change the last_name of the first student from 'Jordan' to 'Bryant'.
# students[0]['last_name']='Bryant'
# print(students)
# # In the sports_directory, change 'Messi' to 'Andres'.
# sports_directory['soccer'][0]= 'Andres'
# print(sports_directory)
# # Change the value 20 in z to 30.
# z[0]['y']=30
# print(z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for i in range (len(students)):
        for key, val in students[i].items():
            print(key,"-", val)
iterateDictionary(students)


def iterateDictionary2(first_name, some_list):
    for i in range (len(students)):
        print(students[i]['first_name'])
iterateDictionary2('first_name', students)


def iterateDictionary2(key_name, some_list):
    for i in range (len(students)):
        print(students[i][key_name])
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dec):
    for k in dec:
        print(str(len(dojo[k])) +" "+ k.upper())
        for i in range (len(dojo[k])):
            print(dojo[k][i])
printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon