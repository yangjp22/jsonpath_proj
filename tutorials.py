import jsonpath_ng
import jsonpath
import json


with open("./champions.json", "r") as fp:
    data = json.load(fp)

reg = "$.champions[*].[tags,name]"

print(jsonpath.jsonpath(data, reg))
