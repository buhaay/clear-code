import csv
import re
import operator
import sys


invalid_logs = {"number": 0}
dict = {}

with open("logs.log") as log_report:
    for line in log_report:
        correct_log = re.findall(r'([(\d\.)]+) \[(.*?)\] "(.*?)" (\d+) (\d+)', line)

        if not correct_log:
            invalid_logs["number"] += 1
        else:
            stripped_url = re.findall(r'(?P<url>[a-z]*[a-z]+\.[a-z]+/*[a-z]*\.*[a-z]+)', str(correct_log))
            dict.setdefault(stripped_url[0], 0)
            dict[stripped_url[0]] += 1


csv_writer = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

csv_writer.writerows(sorted(dict.items(),
                            key=operator.itemgetter(1), reverse=True))

sys.stderr.write("Invalid log lines: {}\n".format(invalid_logs["number"]))
