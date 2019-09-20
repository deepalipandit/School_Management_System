import Models
import email

class StudentDAO:
    
    #Read the students.csv file & append each student to the list 
    def __init__(self):
        self.studentsDataList = []
        with open('students.csv') as f:
            for line in f.read().split('\n'):
                email, s_name, s_password = line.split(',') 
                s = Models.Student(email, s_name, s_password)
                self.studentsDataList.append(s)
    
    #This method returns the list of students        
    def get_students(self):
        return self.studentsDataList
    
    #This method takes an email and a password from the user input. 
    #Returns, whether or not a Student with the given information is found.
    def validate_user(self, email, pw):
        found = False
        for s in self.studentsDataList:
            if (s.email == email) & (s.s_password == pw):
                found = True
                break
        return found

    #   This method takes a Student’s email as a String & searches the List of Students
    #   for a Student with that email and returns a Student Object.
    def get_student_by_email(self, email):
        s = Models.Student
        for s in self.studentsDataList:
            if s.email == email:
                return s
    
class CourseDAO:
    def __init__(self):
        self.coursesDataList = []
        with open('courses.csv') as f:
            for line in f.read().split('\n'):
                course_id, course_name, instructor = line.split(',') 
                c = Models.Course(course_id, course_name, instructor)
                self.coursesDataList.append(c)
        
    #This method takes no parameters and returns every Course in the system.    
    def get_courses(self):
        return self.coursesDataList
    
    def get_couse_name_And_Instructor_from_Course_ID(self, course_ID):
        for c in self.coursesDataList:
            if c.c_id == course_ID:
                return c.c_name, c.instructor
            
    
   
class AttendingDAO:
    def __init__(self, email):
        self.attendingDataList = []
        self.coursesStudentIsAttending = []
        with open('attending.csv') as f:
            for line in f.read().split('\n'):
                course_id, email = line.split(',') 
                a = Models.Attending(course_id, email)
                self.attendingDataList.append(a)
        self.get_student_courses(email)
    
    #This method returns a list of Attending Objects.    
    def get_attending(self):
        return self.attendingDataList

    #This method takes a Student’s Email as a parameter and searches the Attending List 
    #for all the courses that student is registered to.
    #This list of courses the Student is attending is returned.
    def get_student_courses(self, email):
        self.coursesStudentIsAttending = []
        for a in self.attendingDataList:
            if a.student_email == email:
                self.coursesStudentIsAttending.append(a.course_id)
        return self.coursesStudentIsAttending

    #This method takes a Student’s email, a Course ID. It checks if a Student with that Email 
    #is currently attending a Course with that ID.
    #If the Student is not attending that Course and the Course ID is valid, 
    #then add a new Attending object with the Student’s Email and Course ID to the List & save the list on a file and return True.
    #Otherwise, return False.
    def register_student_to_course(self, course_id, email):
        try:            
            i = self.coursesStudentIsAttending.index(course_id)
            return False
        except ValueError as valerr:
                a = Models.Attending(course_id, email)
                self.attendingDataList.append(a)
                self.coursesStudentIsAttending.append(course_id)
                self.save_attending()
        return True
        
        
        
    #This method overwrites the original Attending.csv file with the new data.
    def save_attending(self):
        with open('attending.csv', mode = 'w', encoding = 'utf-8') as f:
            a = Models.Attending
            for a in self.attendingDataList:
                stringToWrite = a.course_id + ',' + a.student_email
                f.write(f'{stringToWrite}\n')
            
