import yaml
import time
import argparse


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.load(file, Loader=yaml.CLoader)


def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, Dumper=yaml.CDumper)


def parse_location(ls):
    """
    Filter licenses without locations with */test/* or '/tests/'
    Since "location" field exists in both data class LicenseFinding and CopyrightFinding in ORT,
    this function can be used for both cases.
    :param ls: list of licenses or copyrights
    :return: list of licenses or copyrights without locations with */test/* or '/tests/'
    """
    result = []
    for object in ls:
        location = object.get('location', {})
        if len(location) == 0:
            continue
        path = location.get('path', '').lower()
        # skip licenses with path containing 'test/' or 'tests/'
        if 'test/' in path or 'tests/' in path:
            continue
        result.append(object)
    return result


def parse_yaml(data):
    """
    Parse location of scan-result.yml from ORT.
    :param data: scan-result.yml
    :return: scan-result.yml with licenses and copyrights without locations with */test/* or '/tests/'
    """
    scanner = data.get('scanner', {})
    if len(scanner) == 0:
        return data

    scan_results = scanner.get('scan_results', {})
    if len(scan_results) == 0:
        return data

    for scan_result in scan_results:
        # Refer to data class ScanSummary in ORT
        summary = scan_result.get('summary', {})
        if len(summary) == 0:
            continue

        # Refer to data class LicenseFinding in ORT
        licenses = summary.get('licenses', {})
        if len(licenses) != 0:
            scan_result['summary']['licenses'] = parse_location(licenses)

        # Refer to data class CopyrightFinding in ORT
        copyrights = summary.get('copyrights', {})
        if len(copyrights) != 0:
            scan_result['summary']['copyrights'] = parse_location(copyrights)
    return data


def main(args):
    yaml_data = read_yaml(args.i)
    parsed_yaml = parse_yaml(yaml_data)
    write_yaml(parsed_yaml, args.o)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple script to parse location of scan-result.yml from ORT.")
    parser.add_argument('--i', type=str, required=True, help='input path of scan-result.yml')
    parser.add_argument('--o', type=str, required=True, help='output path for  this script')

    args = parser.parse_args()

    start_time = time.time()
    main(args)
    end_time = time.time()
    print(f"Processing time: {end_time - start_time} seconds")

