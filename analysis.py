import json
import re
from utils import get_data, save_data_to_database


def analysis(file_path, PATH_JSON, pattern, read_positions, params):
    with open('log_analysics.json', 'w'):
        pass

    last_read = read_positions

    with open(file_path, 'r', encoding='utf8') as f:
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

                to_json = {}
                to_json['message'] = []
                to_json['message'].append({
                    'Date': date_to_json,
                    'Info': info_to_json,
                    'Application': application_to_json,
                    'Action': action_to_json,
                })

                with open('log_analysics.json', 'w') as file:
                    json.dump(to_json, file)
                message_list = get_data(PATH_JSON)
                save_data_to_database('bosik', message_list, params)
                print(
                    f'Date: {date_to_json}, Info: {info_to_json}, Application: {application_to_json}, Action: {action_to_json}')
