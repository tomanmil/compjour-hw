import csv
from flask import Flask
from flask import render_template
from flask import request
import math
app = Flask(__name__)

def get_csv():
    csv_path = 'VegasRestaurants.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    for row in csv_list:
        if not isinstance(row['current_grade'],str) or not isinstance(row['current_demerits'],int):
            csv_list.remove(row)
    return csv_list

@app.route("/")
def index():
    template = 'front-end.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)
    
@app.route('/search', methods=['GET','POST'])
def res():
    template = 'front-end.html'
    object_list = get_csv()
    result_list = []
    grade = request.form['current_grade']
    demerits = request.form['current_demerits']
    stars = request.form['yelp_stars']
    for row in object_list:
        add = True
        if row['current_grade'] != grade and grade != "any":
            add = False
        if isinstance(stars,int) and math.ceil(float(row['yelp_stars'])) != int(stars):
            add = False
        dems = int(row['current_demerits'])
        if dems != 0 and demerits == "0":
            add = False
        if (dems < 1 or dems > 5) and demerits == "1-5":
            add = False
        if (dems < 6 or dems > 10) and demerits == "6-10":
            add = False
        if (dems < 11 or dems > 15) and demerits == "11-15":
            add = False
        if (dems < 16 or dems > 20) and demerits == "16-20":
            add = False
        if dems < 21 and demerits == "21+":
            add = False
        if add:
            result_list.append(row)
    return render_template(template, object_list=result_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)