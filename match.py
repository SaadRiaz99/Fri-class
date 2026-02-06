print("enter 404 , 201 , 302 ,504")
chose = int(input("enter the code : "))
match chose :
        case  404:
            print("not found")
        case  201:
            print("created")    
        case  302:
            print("Internet problem")    
        case  504:
            print("Return timeout")    

            