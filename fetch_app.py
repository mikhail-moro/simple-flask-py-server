import json
import dateutil.parser
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def getJsonData():
    with open("data.json", "r", encoding="utf8") as file:
        return json.load(file)


def getMeetings(req_start_time, req_end_time):
    data = getJsonData()
    res = {}

    req_start_time = dateutil.parser.isoparse(req_start_time)
    req_end_time = dateutil.parser.isoparse(req_end_time)

    for i in data:
        meeting_start_time = dateutil.parser.isoparse(i["start"][0:-6])
        meeting_end_time = dateutil.parser.isoparse(i["end"][0:-6])

        if req_start_time < meeting_start_time and req_end_time > meeting_end_time:
            res_item = {}
            date = i["start"][0: 10]

            if date not in res.keys():
                res[date] = []

            res_item["module"] = i["info"]["moduleName"]
            res_item["name"] = i["name"]
            res_item["theme"] = i["info"]["theme"]
            res_item["type"] = i["info"]["type"]
            res_item["aud"] = i["info"]["aud"]
            res_item["link"] = i["info"]["link"]
            res_item["teachers"] = i["info"]["teachersNames"]
            res_item["groups"] = i["info"]["groupName"]
            res_item["startTime"] = i["start"][11: 16]
            res_item["endTime"] = i["end"][11: 16]
            res_item["color"] = i["color"]

            res[date].append(res_item)

    return json.dumps(res)


@app.route('/', methods = ['GET', 'POST'])
@cross_origin()
def index():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    if request.method == 'GET':
        if (start_time and len(start_time) == 19) and (end_time and len(end_time) == 19):
            return getMeetings(start_time, end_time)


if __name__ == '__main__':
    app.run()
