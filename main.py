from spy_details import spy_name,spy_salutaion,spy_age,spy_rating
from start_chat import spy
print "Let's get started"
question="Do you want to continue as" + spy['salutaion'] + " " + spy['name'] + "(Y/N):"
existing=raw_input(question)
if existing=='Y' or existing=='y':
    start_chat(spy_name,spy_age,spy_rating)
elif existing=='N' or existing=='n':
    spy_name = raw_input("Provide your name here:")
    if len(spy_name) > 0:
        spy_age = 0
        spy_rating = 0.0
        spy_status = True
        spy_salutation = raw_input("What should we call you:")
        spy_age = raw_input("Enter your age?")
        print type(spy_age)
        spy_age = int(spy_age)
        print type(spy_age)
        if spy_age > 12 and spy_age < 50:
            spy_rating = raw_input("What is your spy rating?")
        else:
            print "Not eligible for spy right now."
        print type(spy_rating)
        spy_rating = float(spy_rating)
        print type(spy_rating)
        if spy_rating > 4.5:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'Gud'
        else:
            print 'bad'
        spy_name = spy_salutation + ' ' + spy_name
        print "Welcome" + " " + spy_name + " " + "Glad to meet you."
        print "Alright" + " " + spy_name + " " + "I would like to know more aout you."
    else:
        print 'Invalid name. Try again.'

else:
    print 'Wrong choice. Try again.'
