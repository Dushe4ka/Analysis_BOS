import json
import re


def analysis(file_path, pattern):
    with open('log_analysics.json', 'w'):
        pass

    with open(file_path, 'r', encoding='utf8') as f:
        last_read = 0
        print(last_read)
        f.seek(last_read)
        while True:
            line = f.readline()

            if line == "":
                last_read = f.tell()
                print(last_read)
                return last_read

            if not line:
                break

            match = re.search(pattern, line)

            if match:

                printer_1 = re.split(';|,|\n|]', line)

                date = str(printer_1[1])
                date_to_json = date.replace('[', '')

                info = str(printer_1[2])
                info_to_json = info.replace('[', '')

                application = str(printer_1[3])
                application_to_json = application.replace('[', '')

                action = str(printer_1[4])
                action_to_json = action.replace('[', '')

                to_json = {'Date': date_to_json,
                           'Info': info_to_json,
                           'Application': application_to_json,
                           'Action': action_to_json}

                with open('log_analysics.json', 'a') as file:
                    json.dump(to_json, file)

                print(f'Date: {date_to_json}, Info: {info_to_json}, Application: {application_to_json}, Action: {action}')

