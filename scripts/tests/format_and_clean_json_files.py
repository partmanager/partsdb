import json
from common import load_files


def cleanup_json_data(data):
    if isinstance(data, dict):
        return {k: cleanup_json_data(v) for k, v in data.items() if v != ""}
    elif isinstance(data, list):
        return [cleanup_json_data(e) for e in data]
    else:
        return data


def cleanup_and_sort_json_files(files):
    for f in files:
        try:
            with open(str(f)) as jsonfile:
                content = json.load(jsonfile)
                cleanup_json = cleanup_json_data(content)
                sorted_json = sorted(cleanup_json, key=lambda x: x['manufacturer'] + x['partNumber'])
                fixed_content = json.dumps(sorted_json, indent='\t')
                jsonfile.close()
                if content != fixed_content:
                    with open(str(f), 'w') as jsonfile:
                        jsonfile.write(fixed_content)
        except ValueError as e:
            print(f"Invalid JSON file {f}: {e}")


cleanup_and_sort_json_files(load_files('./components/IC/texas instruments'))
