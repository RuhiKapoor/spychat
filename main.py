print "Let's get started"
spy_name=raw_input("Provide your name here:")

if len(spy_name)> 0:
     spy_salutation = raw_input("What should we call you:")
     spy_name = spy_salutation + ' ' + spy_name
     print "Welcome" +" " + spy_name + " " + "Glad to meet you."
     print "Alright"+ " " + spy_name + "i would like to know more aout you."
else:
    print 'Invalid name. Try again.'
