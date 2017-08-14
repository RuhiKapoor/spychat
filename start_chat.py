def start_chat(name,age,rating):
    show_menu=True
    while show_menu:
        menu_choices='What do you want to do? \n 1.Add status. \n 2.Close application'
        result=int(raw_input(menu_choices))
        if result==1:
            print 'ok'
        elif result==2:
            show_menu=False
        else:
            print 'Wrong input. Try again.'