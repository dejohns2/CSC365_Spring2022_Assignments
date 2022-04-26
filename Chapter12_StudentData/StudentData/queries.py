import student_data as data

"""
This module contains the functions for querying the student data containers
"""

__author__ = "Debbie Johnson"
__version__ = "1.0"
_date__ = "2022.04.01"


def list_students(student_ids):
    """
    Display a list of students ids & names used by other functions.  Example:

    13 Amy Hans
    41 Joe Jones

    :param student_ids: a list of all students to display
    :return: n/a
    """

    for student_id in student_ids:
        print(student_id,
              data.students.get(student_id).get('first_name'),
              data.students.get(student_id).get('last_name')
              )


def student_information():
    """
    Display the student information. Report Example:

    ================================================================================
    Student Information
    ================================================================================
    ID: 31 Bob Smith
       Groups: track, basketball, student council,
       english [80, 100]
       science [100, 80]

    :return: n/a
    """

    print('=' * 80)
    print("Student Information")
    print('=' * 80)

    # loop through all students
    for student_id, student_data in data.students.items():
        print('ID:', student_id, student_data.get('first_name'), student_data.get('last_name'))

        print('\tGroups:', end=' ')
        print(*student_data.get('groups'), sep=', ')

        # loop through all the courses
        # and if the student is in the course
        # then display the course name and grades list
        for course_name, course_grades in data.grades.items():
            if student_id in course_grades:
                print('\t' + course_name, course_grades.get(student_id))


def all_sports_list():
    """
    List all sports. Report example:

    ================================================================================
    All Sports
    ================================================================================
    baseball
    basketball
    cross country
    football
    softball
    track
    volleyball
    wrestling

    :return: n/a
    """

    print('=' * 80)
    print("All Sports")
    print('=' * 80)

    # create an empty list that will store all sports
    all_sports = list()

    # loop through each season one at a time
    # convert the current season's set to a list
    # add the current season's list to the full list using the extend method to add more than one item
    for season_sports in data.sports.values():
        all_sports.extend(list(season_sports))

    all_sports.sort()

    # use the iterator unpack operator to list all sport on it's own line
    print(*all_sports, sep='\n')


def each_course_genders():
    """
    Lists each course's genders

    This functions will create a nested subjectGender dict used to produce the report:
        'math': {'Female': 3, 'Male': 1}
        'english': {'Female': 3, 'Male': 2}
        'science': {'Female': 3, 'Male': 2}

    Report Example:

    ================================================================================
    Each Class Genders
    ================================================================================
    math: Male = 1 Female = 3
    english: Male = 2 Female = 3
    science: Male = 2 Female = 3

    :return: n/a
    """

    print('=' * 80)
    print("Each Class Genders")
    print('=' * 80)

    # create a temporary dictionary that store the course's gender counts
    # example: 'math': {'Female': 3, 'Male': 1}
    course_genders = dict()

    # loop through each course one at a time
    for course_name, course_grades in data.grades.items():
        # reset the counter for each season
        male_count = 0
        female_count = 0

        # loop through each student in the course
        for student_id, student_grades in course_grades.items():

            student_gender = data.students.get(student_id).get('gender')

            if student_gender == 'M':
                male_count += 1
            else:
                female_count += 1

        # after counting the gender for one course, add the course info to the temp reporting dictionary
        course_genders[course_name] = {'male': male_count, 'female': female_count}

    # print the report by looping through the temporary reporting dictionary that was just created
    for course_name, genders in course_genders.items():
        print(course_name + ':', 'Male =', genders.get('male'), 'Female =', genders.get('female'))


def sue_smith_course_list():
    """
    Sue Smith Class List. Report Example:

    ================================================================================
    Sue Smith Class List
    ================================================================================
    math, english, science

    :return: n/a
    """

    print('=' * 80)
    print("Sue Smith Class List")
    print('=' * 80)

    # create a temporary list that will store sue's courses
    sue_smith_courses = list()

    # loop through all students to locate Sue Smith
    for student_id, student_info in data.students.items():
        first_name = student_info.get('first_name')
        last_name = student_info.get('last_name')

        if first_name == 'Sue' and last_name == 'Smith':
            # loop through all courses to find Sue Smith
            # if Sue Smith is in the course then append the course name to the temporary list
            for course_name, course_grades in data.grades.items():
                if student_id in course_grades:
                    sue_smith_courses.append(course_name)

    sue_smith_courses.sort()

    # use the iterator unpack operator to list eaach course on it's own line
    print(*sue_smith_courses, sep='\n')


def students_in_science_not_math():
    """
    Students in science not math.  Report Example:

    ================================================================================
    Students in science not math:
    ================================================================================
    31# Bob Smith
    55# Sue Johnson

    :return: n/a
    """

    print('=' * 80)
    print("Students in science but not in math")
    print('=' * 80)

    # create an temporary list that will store student ids that are in science but not math
    science_not_math = list()

    # loop through each student id key (don't need the values too)
    # if the student is in science but not math then append the student_id to the temporary list
    for student_id in data.students.keys():
        if student_id in data.grades.get('science') and student_id not in data.grades.get('math'):
            science_not_math.append(student_id)

    science_not_math.sort()
    list_students(science_not_math) # common function for displaying a list of students


def non_sports_groups():
    """
    List NonSports groups.  Report Example:

    ================================================================================
    Non-Sports Groups
    ================================================================================
    student council
    national honor society

    :return: n/a
    """

    print('=' * 80)
    print("NonSports Groups")
    print('=' * 80)

    # create a temporary set for storing all sports
    all_sports = set()
    # create a temporary list for storing all non sports related group
    non_sports = list()

    # loop through each season
    # use the update method to append a set to a set
    for season, season_sports in data.sports.items():
        all_sports.update(season_sports)

    # loop through each student
    for student_id, student_info in data.students.items():

        student_groups = student_info.get('groups')

        # use the - operator to get the differences between the current student's groups and all sports
        whats_left = student_groups - all_sports

        # if there are any non-sports related groups then append them to the temporary list
        if len(whats_left):
            non_sports.append(*whats_left)

    non_sports.sort()

    # use the iterator unpack operator to list all sport on it's own line
    print(*non_sports, sep='\n')

def all_seasons_sports_students():
    """
    All Season Sports Students.  Report Example:

    ================================================================================
    Students in All Four Seasons of Sports
    ================================================================================
    22 Sue Smith
    41 Joe Jones

    :return: n/a
    """

    print('=' * 80)
    print("All Seasons Sports Students")
    print('=' * 80)

    # create an temporary list to store student ids that are in all sports
    all_seasons = list()

    # loop through students one at a time
    for student_id, student_info in data.students.items():

        student_groups = student_info.get('groups')

        # if the student_groups isn't empty and student's groups intersect (&) with each season
        # then append to the temporary list
        if student_groups & data.sports.get('fall') \
                and student_groups & data.sports.get('winter') \
                and student_groups & data.sports.get('spring') \
                and student_groups & data.sports.get('summer'):
            all_seasons.append(student_id)

    all_seasons.sort()
    list_students(all_seasons) # common function for displaying a list of students


def student_courses_same_as_sue_smith():
    """
    Students coursees same as Sue Smith.  Report Example:

    ================================================================================
    Students in Same Classes as Sue Smith
    ================================================================================
    13 Amy Hans
    41 Joe Jones

    :return: n/a
    """

    print('=' * 80)
    print("Students Classes same as Sue Smith")
    print('=' * 80)

    # create a temporary set to store all sue smith's courses
    sue_smith_courses = set()
    # create a temporary list to store student ids of students in the same courses as Sue Smith
    same_as_sue_smith = list()
    # create a temporary dictionary to store
    students_courses = dict()

    # loop through each student one at a time
    for student_id, student_info in data.students.items():
        # create an empty set for each student that will store the courses they are in
        student_courses = set()

        first_name = student_info.get('first_name')
        last_name = student_info.get('last_name')

        # loop through each course grades and if the current student is in the course
        # then add the course to the student's temporary set of courses
        for course_name, course_grades in data.grades.items():
            if student_id in course_grades:
                student_courses.add(course_name)

        # after building the current student's course set see if the student is Sue Smith
        # if so, update Sue Smith's set
        # else store the current student's course set into a dictionary that will be used for the final report
        if (first_name + last_name) == 'SueSmith':
            sue_smith_courses = student_courses
        else:
            students_courses[student_id] = student_courses

    # loop through the temporary dictionary of all student besides Sue Smith
    # if the current student's course set matches Sue Smith's courses
    # then append the student id to the temporary list
    for student_id, courses in students_courses.items():
        if courses == sue_smith_courses:
            same_as_sue_smith.append(student_id)

    same_as_sue_smith.sort()
    list_students(same_as_sue_smith) # common function for displaying a list of students


###########################################################################################
# Students with low grades
###########################################################################################
def students_with_low_grades():
    """
    Students with low grades.  Report Example:

    ================================================================================
    Students with Low Grades
    ================================================================================
    41 Joe Jones
    45 Sue Johnson

    :return: n/a
    """

    print('=' * 80)
    print("Students with Low Grades")
    print('=' * 80)

    # create a temporary set that will store all student ids with low grades
    # we are using a set because a set doesn't store duplicates and it's possible
    # that a student has a low grade in more than one course
    low_grades = set()

    # loop through each student one at a time
    for student_id, student_info in data.students.items():

        # loop through all courses one at a time
        # if the student is in the course then calculate their grade average
        # if it's below 70 add the student id to the temporary set
        for course_name, student_grades in data.grades.items():
            if student_id in student_grades:
                grade_total = sum(student_grades.get(student_id))
                grade_count = len(student_grades.get(student_id))
                avg_grade = grade_total / grade_count

                if avg_grade < 70:
                    low_grades.add(student_id)

    # convert the set to a list so we can sort it
    low_grades_list = list(low_grades)
    low_grades_list.sort()
    list_students(low_grades_list) # common function for displaying a list of students
