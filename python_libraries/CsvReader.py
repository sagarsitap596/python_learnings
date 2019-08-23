import csv

countryCodeMap = {}


class CountryCode:
    def __init__(self, countryCode, head, tail):
        self.countryCode = countryCode
        self.head = head
        self.tail = tail


def loadCountryCodeMapping():
    with open('/Users/sitapsha/my_git/code_clones/python_learnings/resource/country_phone.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for line in csv_reader:
            if line_count > 0:
                countryCodeMap[line[0]] = CountryCode(line[0], line[1], line[2])
            line_count += 1


def generate_msiddn(country):
    if len(countryCodeMap) == 0:
        loadCountryCodeMapping()
        return countryCodeMap.get(country)
    else:
        return countryCodeMap.get(country)


print(generate_msiddn("india").countryCode)
print(generate_msiddn("india").head)
print(generate_msiddn("india").tail)
