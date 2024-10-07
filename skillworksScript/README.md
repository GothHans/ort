### Description
To parse the scan result from the scanner and generate a new scan yaml result file with the following requirements:
- remove "*/test/*" or "*/tests/*" from the path

### Environment setup
- Python 3.9.6
- pip 24.2


### Install dependencies
Depend on the version of Python you are using, you can use `pip` or `pip3` to install dependencies.
```bash
pip install -r /path/to/requirements.txt # Install dependencies
pip3 install -r /path/to/requirements.txt # Install dependencies
```


### Usage
```bash
python locationScript.py --i scan-result.yml --o scan-result2.yml
```
