import requests

BASE_USAJOBS_URL = "https://data.usajobs.gov/api/jobs"
COMPJOUR_URL = "http://stash.compjour.org/data/usajobs/us-statecodes.json"
resp = requests.get(COMPJOUR_URL)
state_code = resp.json()
names = ['California', 'Florida', 'Maryland', 'New York']
thelist = []
thelist.append(["State", "Job Count"])
for n in names:
    atts = {'CountrySubdivision': n, 'NumberOfJobs': 1}
    resp = requests.get(BASE_USAJOBS_URL, params = atts)
    jobcount = int(resp.json()['TotalJobs'])
    geocode = 'US-'+state_code[n]
    thelist.append([geocode, jobcount])



chartcode = """
<html>
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
  </head>
  <body>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["geochart"]});
      google.setOnLoadCallback(drawRegionsMap);

      function drawRegionsMap() {

        var data = %s
        var datatable = google.visualization.arrayToDataTable(data);
        var options = {'region': 'US', 'width': 600, 'height': 400, 'resolution': 'provinces'};

        var chart = new google.visualization.GeoChart(document.getElementById('mychart'));

        chart.draw(datatable, options);
      }
    </script>


      <div class="container">
        <h1 style="text-align:center">Hello chart</h1>
        <div id="mychart"></div>
      </div>
  </body>
</html>
"""


htmlfile = open("1-8.html", "w")
htmlfile.write(chartcode % thelist)
htmlfile.close()