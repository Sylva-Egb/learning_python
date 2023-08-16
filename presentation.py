about_me = {
    'firstName' : 'Sylvanus',
    'lastName' : 'EGBEWOLE', 
    'age' : 21,
    'skills' : [('HTML','CSS','PHP','Java','C'),'Laravel']
}

about_me['skills'].append('ReactJs')

about_me['skills'].append('Python')

print(f"Hello! I'm {about_me['firstName']} {about_me['lastName']}. \n "+
f"I'm {about_me['age']} years old. I specialised myself in Web and Mobile Development for the moment(maybe in future surely I will switch to another universe)"+
f"So to deal with my work field, I reached this primary necessary skills such as: {about_me['skills']}")