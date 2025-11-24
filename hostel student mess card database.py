STUDENT={'25bce10001':{'Name':'Shrijay Shrivastava','Room':'B-312'},
         '25bce10002':{'Name':'Shuchi Shubhra','Room':'A-510'},
         '25bce10003':{'Name':'Rajeev Kumar','Room':'A-701'},
         '25bce10004':{'Name':'Krish Sharma','Room':'D-107'}
         }
meal_log=[]
import datetime
def log_attendance(student_id, meal_type):
    student_name=None
    for student in STUDENT:
        if student[0]==student_id:
            student_name=student[1]
            break
    if student_name is None:
        print(f"record failed:student id{student_id} is not found in the system")
        return
    timestamp=datetime.datetime.now().strftime("%H:%M:%S")
    record=(student_id,student_name,meal_type.upper(),timestamp)
    meal_log.append(record)
    print(f"recorded:{student_name}({student_id}) checked in for{meal_type.upper()} at {timestamp}")
    if __name__=='__main__':
        print("___mess attendance system started___")
        log_attendance('25bce10001','breakfast')
        log_attendance('25bce10002','lunch')
        log_attendance('25bce10003','dinner')
        log_attendance('25bce10004','dinner')
        log_attendance('25bce10002','dinner')
        log_attendance('25bce10674','breakfast')
        print("\n---final attendance log---")
        if meal_log:
            print(f"{'id':<6} {'name':<20} {'meal':<10} {'time':<10}")
            print("-"*50)
            for id ,name , meal, time in meal_log:
                print(f"{id:<6} {name:<20} {meal:<10}")
        else:
            print("log is empmy")