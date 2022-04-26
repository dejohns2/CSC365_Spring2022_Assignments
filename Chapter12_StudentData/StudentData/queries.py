import student_data as data


###########################################################################################
# Display a list of students ids & names
###########################################################################################
def list_students(student_ids):
    for student_id in student_ids:
        print(student_id, data.students.get(student_id).get('firstName'),
              data.students.get(student_id).get('lastName'))


###########################################################################################
# Display the student information
###########################################################################################
def student_information():

    print('=' * 80)
    print("Student Information")
    print('=' * 80)

    for student_id, student_data in data.students.items():
        print('ID:', student_id, student_data.get('firstName'), student_data.get('lastName'))

        print('\tGroups:', end=' ')
        print(*student_data.get('groups'), sep=', ')

        for class_name, class_grades in data.grades.items():
            if student_id in class_grades:
                print('\t' + class_name, class_grades.get(student_id))


###########################################################################################
# All Sports List
###########################################################################################
def all_sports_list():
    print('=' * 80)
    print("All Sports")
    print('=' * 80)

    sports = list()

    for season_sports in data.sports.values():
        sports.extend(list(season_sports))

    sports.sort()

    for sport in sports:
        print(sport)


###########################################################################################
# Each Class Genders

# Create a nested subjectGender dict, example:
# 'math': {'Female': 3, 'Male': 1}
# 'english': {'Female': 3, 'Male': 2}
# 'science': {'Female': 3, 'Male': 2}
###########################################################################################
def each_class_genders():
    print('=' * 80)
    print("Each Class Genders")
    print('=' * 80)

    class_genders = dict()

    for class_name, class_grades in data.grades.items():
        male_count = 0
        female_count = 0

        for student_id, student_grades in class_grades.items():
            student_gender = data.students.get(student_id).get('gender')

            if student_gender == 'M':
                male_count += 1
            else:
                female_count += 1

        class_genders[class_name] = {'male': male_count, 'female': female_count}

    for class_name, genders in class_genders.items():
        print(class_name + ':', 'Male =', genders.get('male'), 'Female =', genders.get('female'))


###########################################################################################
# Sue Smith Class LIst
###########################################################################################
def sue_smith_class_list():
    print('=' * 80)
    print("Sue Smith Class List")
    print('=' * 80)

    sue_smith_classes = list()

    for student_id, student_info in data.students.items():
        first_name = student_info.get('firstName')
        last_name = student_info.get('lastName')

        if first_name == 'Sue' and last_name == 'Smith':
            for class_name, class_grades in data.grades.items():
                if student_id in class_grades:
                    sue_smith_classes.append(class_name)

    sue_smith_classes.sort()

    for class_name in sue_smith_classes:
        print(class_name)


###########################################################################################
# Students in Science not Math
###########################################################################################
def students_in_science_not_math():
    print('=' * 80)
    print("Students in Science but not in Math")
    print('=' * 80)

    science_not_math = list()

    for student_id in data.students.keys():
        if student_id in data.grades.get('Science') and student_id not in data.grades.get('Math'):
            science_not_math.append(student_id)

    science_not_math.sort()

    list_students(science_not_math)


###########################################################################################
# NonSports groups
###########################################################################################
def non_sports_groups():
    print('=' * 80)
    print("NonSports Groups")
    print('=' * 80)

    sports = set()
    non_sports = list()

    for season, season_sports in data.sports.items():
        sports.update(season_sports)

    for student_id, student_info in data.students.items():

        student_groups = student_info.get('groups')

        whats_left = student_groups - sports

        if len(whats_left):
            non_sports.append(*whats_left)

    non_sports.sort()

    for group in non_sports:
        print(group)


###########################################################################################
# All Season Sports Students
###########################################################################################
def all_seasons_sports_students():
    print('=' * 80)
    print("All Seasons Sports Students")
    print('=' * 80)

    all_seasons = list()

    for student_id, student_info in data.students.items():

        student_groups = student_info.get('groups')

        if student_groups & data.sports.get('fall') \
                and student_groups & data.sports.get('winter') \
                and student_groups & data.sports.get('spring') \
                and student_groups & data.sports.get('summer'):
            all_seasons.append(student_id)

    all_seasons.sort()

    list_students(all_seasons)


###########################################################################################
# Students classes same as Sue Smith
###########################################################################################
def student_classes_same_as_sue_smith():
    print('=' * 80)
    print("Students Classes same as Sue Smith")
    print('=' * 80)

    sue_smith_classes = set()
    same_as_sue_smith = list()
    students_classes = dict()

    for student_id, student_info in data.students.items():
        student_classes = set()

        first_name = student_info.get('firstName')
        last_name = student_info.get('lastName')

        for class_name, class_grades in data.grades.items():
            if student_id in class_grades:
                student_classes.add(class_name)

        if (first_name + last_name) == 'SueSmith':
            sue_smith_classes = student_classes
        else:
            students_classes[student_id] = student_classes

    for student_id, classes in students_classes.items():
        if classes == sue_smith_classes:
            same_as_sue_smith.append(student_id)

    same_as_sue_smith.sort()

    list_students(same_as_sue_smith)


###########################################################################################
# Students with low grades
###########################################################################################
def students_with_low_grades():
    print('=' * 80)
    print("Students with Low Grades")
    print('=' * 80)

    low_grades = set()

    for student_id, student_info in data.students.items():

        for class_name, student_grades in data.grades.items():

            if student_id in student_grades:
                grade_total = sum(student_grades.get(student_id))
                grade_count = len(student_grades.get(student_id))
                avg_grade = grade_total / grade_count

                if avg_grade < 70:
                    low_grades.add(student_id)

    low_grades_list = list(low_grades)
    low_grades_list.sort()
    list_students(low_grades_list)
