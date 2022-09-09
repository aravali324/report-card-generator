import csv

class CSVReader:
    # csv file reader class
    @staticmethod
    def students_file_reader(stud_file):
        # reading the student file and converting to dict 
        #  :params stu_file: student file path
        #  :return: student dict
        student_dict ={}
        with open(stud_file) as f: 
            student = csv.reader(f)
            firstrow= True
            for row in student:
                if firstrow:
                    firstrow=False
                    continue
                else:
                    student_dict[int(row[0])]= row[1]
        return student_dict
    
    @staticmethod
    def courses_file_reader(courses_file):
        # Reading the course csv file and converting to dict 
        # : params courses_file : course file path
        #  return: course dict
        courses_dict = {}
        with open(courses_file) as f:
            courses = csv.reader(f)
            firstrow = True
            for row in courses:
                if firstrow:
                    firstrow= False
                    continue
                else:
                    courses_dict[int(row[0])] = [row[1], row[2], {}]
        return courses_dict



    @staticmethod
    def test_file_reader(tests_file, courses_file):
        """
        reading the test and course file and converting to respective dict
        :param tests_file: test csv file path
        :param courses_file: course csv file path
        :return: tuple of dict
        """
        courses_dict = CSVReader.courses_file_reader(courses_file)
        tests_dict = {}
        with open(tests_file) as f:
            tests = csv.reader(f)
            firstrow = True
            for row in tests:
                if firstrow:
                    firstrow = False
                    continue
                else:
                    courses_dict[int(row[1])][2][int(row[0])] = int(row[2])
                    tests_dict[int(row[0])] = [int(row[1]), int(row[2])]
        return courses_dict, tests_dict

    @staticmethod
    def marks_file_reader(marks_file):
        """
        reading the marks csv file and converting to dict
        :param marks_file: marks csv file path
        :return: marks dict
        """
        with open(marks_file) as f:
            marks = csv.reader(f, delimiter=',')
            marks_dict = {}
            firstrow = True
            for row in marks:
                if firstrow:
                    firstrow = False
                    continue
                else:
                    if int(row[1]) in marks_dict.keys():
                        marks_dict[int(row[1])].extend([int(row[0]), int(row[2])])
                    else:
                        marks_dict[int(row[1])] = [int(row[0]), int(row[2])]
        return marks_dict