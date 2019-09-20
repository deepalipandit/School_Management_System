import DAO

def show_my_courses(student, attending_dao, course_dao):
    print('\nMy Courses:')
    print('#\tCOURSE NAME\tINSTRUCTOR NAME')
#     attending_dao = DAO.AttendingDAO(student.email)
#     course_dao  = DAO.CourseDAO()
    my_courses = attending_dao.get_student_courses(student.email)
    i = 1
    courseName = ''
    instructor = ''
    for course in my_courses:
        courseName, instructor = course_dao.get_couse_name_And_Instructor_from_Course_ID(course)
        print(f'{course}\t{courseName}\t{instructor}')
        i+=1

def show_all_courses(course_list):
    print('\nAll Courses:')
    print('ID\tCOURSE NAME\tINSTRUCTOR NAME')
    for course in course_list:
        
        print('{}\t{}\t{}'.format(course.get_id(),course.get_name(),course.get_instructor()))
        
def main():
    print('Welcome!')
   
    entry=None
    while entry!='2':
        entry = input('\n1. Student\n2. Quit\nPlease, enter 1 or 2: ')
         
        if entry=='1':
            student_dao = DAO.StudentDAO()
            email = input('\nEnter Your Email: ')
            pw = input('Enter Your Password: ')
             
            if student_dao.validate_user(email, pw):
                course_dao = DAO.CourseDAO()
                attending_dao = DAO.AttendingDAO(email)
                student = student_dao.get_student_by_email(email)
                course_list = course_dao.get_courses()
                 
                show_my_courses(student, attending_dao, course_dao)
                print('\nWhat Would You Like To Do?')
                 
                while entry!='2':
                    entry = input('\n1. Register To Course\n2. Logout\nPlease, enter 1 or 2: ')
                     
                    if entry=='1':
                        show_all_courses(course_list)
                        course_id = input('\nSelect Course By ID Number: ')
                        print("\nAttempting to Register...")
                        if attending_dao.register_student_to_course(course_id, email):
                            print(f"\nCongratulations You've Just Registered For: {course_id}")
                            show_my_courses(student, attending_dao, course_dao)
                        else:
                            print(f"\nYou Are Already Registered For This Course : {course_id}")
                    elif entry=='2':
                        print('\nYou Have Been Logged Out.')
                    else:
                        print('\nInvalid Option...')
            else:
                print('\nWrong Credentials!')
        elif entry!='2':
            print('\nInvalid Option...')
    print('\nClosing Program. Goodbye.')
    
if __name__=='__main__':
    main()