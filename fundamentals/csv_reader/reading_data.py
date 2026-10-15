import csv
from csv import QUOTE_MINIMAL

def age_seperator(reader):
    person = (support for role,support in reader if role == 'support')
    yield  next(person)


with open('MOCK_DATA.csv', newline='') as file:
    reader = csv.reader(
        file,
        delimiter=',',
        quotechar='"',
        escapechar=None,
        doublequote=True,
        skipinitialspace=False,
        lineterminator='\r\n',
        quoting=QUOTE_MINIMAL
    )

print(next(age_seperator(reader)))



