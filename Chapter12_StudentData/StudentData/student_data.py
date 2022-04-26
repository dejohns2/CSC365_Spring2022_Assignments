"""
This module contains the student data containers
"""

__author__ = "Debbie Johnson"
__version__ = "1.0"
_date__ = "2022.04.01"

sports = {
    'fall': {'football', 'volleyball', 'cross country'},
    'winter': {'basketball', 'wrestling'},
    'spring': {'track'},
    'summer': {'baseball', 'softball'}
}

students = {
    31: {
        'first_name': 'Bob',
        'last_name': 'Smith',
        'gender': 'M',
        'groups': {'basketball', 'track', 'student council'}
    },
    22: {
        'first_name': 'Sue',
        'last_name': 'Smith',
        'gender': 'F',
        'groups': {'volleyball', 'basketball', 'track', 'softball', 'national honor society'}
    },
    13: {
        'first_name': 'Amy',
        'last_name': 'Hans',
        'gender': 'F',
        'groups': {'basketball', 'volleyball'}
    },
    41: {
        'first_name': 'Joe',
        'last_name': 'Jones',
        'gender': 'M',
        'groups': {'track', 'baseball', 'cross country', 'wrestling'}
    },
    55: {
        'first_name': 'Sue',
        'last_name': 'Johnson',
        'gender': 'F',
        'groups': {'basketball', 'volleyball'}
    },
    45: {
        'first_name': 'Sue',
        'last_name': 'Johnson',
        'gender': 'F',
        'groups': {'track', 'volleyball', 'basketball'}
    }
}

grades = {
    'math': {
        22: [90, 100, 100],
        13: [80, 75, 80, 80],
        41: [70, 55, 70, 75],
        45: [70, 75, 55]
    },
    'english': {
        31: [80, 100],
        22: [100, 100],
        13: [90, 100],
        41: [70, 65, 70],
        55: [90, 95]
    },
    'science': {
        31: [100, 80],
        22: [90, 80],
        13: [100],
        55: [100, 80, 85],
        41: [70]
    }
}

