import sys
from flask import Flask, abort, request, make_response
import json
import main as umls





app = Flask(__name__)



def proccesing_response(input_dicc,return_type):
    finalResponse = {}
    text=input_dicc["data"]
    if return_type=="label":
        finalResponse["label"]= umls.get_cui_label(text)
    elif return_type=="cui":
        finalResponse["cui"]= umls.get_cui_id(text)
    return finalResponse



@app.route('/umlsmatching', methods=['POST'])
def main_api():
    if (not request.json):
        abort(400)
    input_list = request.json
    if 'type' in request.args:
        return_type = request.args['type']
    else:
        abort(400)
    if len(input_list) == 0:
        r = "{results: 'Error in the input format'}"
    else:
        response = proccesing_response(input_list,return_type)
        r = json.dumps(response, indent=4)            
    response = make_response(r, 200)
    response.mimetype = "application/json"
    return response

def main(*args):
    if len(args) == 1:
        myhost = args[0]
    else:
        myhost = "0.0.0.0"
    app.run(debug=False, host=myhost)
    
if __name__ == '__main__':
     main(*sys.argv[1:])