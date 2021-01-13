def validate_teacher(phone, aviable_after_lesson):

    if phone =='':
        phone ='null'

    aviable_flag = False
    if aviable_after_lesson == 'on':
        aviable_flag = True

    return phone, aviable_flag


                
