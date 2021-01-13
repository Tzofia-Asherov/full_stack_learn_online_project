def validate_teacher(last_name , phone, aviable_after_lesson):
    if last_name == '':
        last_name = 'null'
    
    if phone =='':
        phone ='null'

    aviable_flag = False
    if aviable_after_lesson == 'on':
        aviable_flag = True

    return last_name, phone, aviable_flag