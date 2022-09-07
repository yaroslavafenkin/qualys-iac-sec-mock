from flask import Flask

app = Flask(__name__)

@app.route('/cloudview-api/rest/v1/iac/getScanList')
def scanlist():
    return '{"content": [{"status": "FINISHED"}]}'

@app.route('/cloudview-api/rest/v1/iac/scanResult')
def result():
    return '''{"result": [
        {
            "results": {
                "passedChecks": [{
                    "checkResult": {"result": "SUCCESS"},
                    "checkId": "<img/src/onerror=alert('checkId')>",
                    "checkName": "<img/src/onerror=alert('checkName')>",
                    "criticality": "<img/src/onerror=alert('criticality')>",
                    "filePath": "<img/src/onerror=alert('filePath')>",
                    "resource": "<img/src/onerror=alert('resource')>"
                }],
                "failedChecks": [],
                "parsingErrors": []
            },
            "checkType": "checktype",
            "summary": {
                "failedStats": {
                    "high": 3,
                    "medium": 2,
                    "low": 1
                },
                "passed": 4,
                "failed": 6,
                "skipped": 8,
                "parsingErrors": 111
            }
        }
    ]}'''

@app.route('/cloudview-api/rest/v1/iac/scan', methods = ['POST'])
def test():
    return '{"scanUuid": "5eef275e-dbb8-4f8d-8541-9b4c18460983"}'