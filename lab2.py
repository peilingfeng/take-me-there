a = {"79":1,"80":2,"81":3,"75":4,"76":5,"77":6,"71":7,"72":8,"73":9}
dev = evdev.InputDevice('/dev/input/event2')
for event in dev.read_loop():
	if(event.value ==1):
		print(event.code)
                dictionary = {}
                flag = 'a'
                pape = 'a'
                off = 'a'
                while flag == 'a' or 'c' :
                    flag = raw_input("input or search? (a/c)")
                    if flag == "a" :                    
                        word = raw_input("name(key):")
                        defintion = raw_input("number(value):")
                          dictionary[str(word)] = str(defintion)  
                        print "success!"
                        pape = raw_input("search numeber ?(a/0)")  
                        if pape == 'a':
                            print dictionary
                        else :
                            continue
                    elif flag == 'c':
                        check_word = event.code  
                        for key in sorted(dictionary.keys()):            # yes
                            if str(check_word) == key:
                                print  dictionary[key]
                                break
                            else:                                       # no
                                off = 'b'
                       # if off == 'b':
                       #    print "sorry!"
                    else:                            
                        print "error type"
                        break
