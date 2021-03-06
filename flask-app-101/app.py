import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)

def get_csv():
    csv_path = './static/sf311.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = []
    for row in csv_obj:
        mypoint = row['point'].replace('(','').replace(')','')
        pointlist = mypoint.split(',')
        row['y'] = float(pointlist[0])
        row['x'] = float(pointlist[1])
        csv_list.append(row)
    print(csv_list)
    return csv_list

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)


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