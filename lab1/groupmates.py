#coding:utf-8
groupmates = [
	{
		"name": u"Полина",
		"group": "1702",
		"age": 19,
		"marks": [5,4,4,5,5]
	},
	{
		"name": u"Татьяна",
		"group": "1703",
		"age": 18,
		"marks": [5,4,4,5,3]
	},
	{
		"name": u"Анастасия",
		"group": "1701",
		"age": 19,
		"marks": [5,5,5,5,5]
	},
	{
		"name": u"Екатерина",
		"group": "1702",
		"age": 19,
		"marks": [5,5,4,5,5]
	}
]

def print_students(students):
	print u"Имя студента".ljust(15), \
		u"Группа".ljust(8), \
		u"Возраст".ljust(8), \
		u"Оценки".ljust(20)
	for student in students:
		print \
			student["name"].ljust(15), \
			student["group"].ljust(8), \
			str(student["age"]).ljust(8), \
			str(student["marks"]).ljust(20)
		print "\n"

print_students(groupmates)

def filtration(students,p):
	print u"Студенты, средняя оценка которых выше заданного параметра"
	b=[]
	for i in students:
		a=len(i["marks"])
		m=sum(i["marks"])
		if (m/a)>=p:
			b.append(i)
	print_students(b)
	
filtration(groupmates,4.5)