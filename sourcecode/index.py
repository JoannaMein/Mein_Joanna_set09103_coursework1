from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/recipes/')
def recipes():
  return render_template('recipes.html')

@app.route('/recipes/halloween/')
def halloween():
  return render_template('halloween.html')
  
@app.route('/recipes/bonfire/')
def bonfire():
  return render_template('bonfire.html')
  
@app.route('/recipes/christmas/')
def christmas():
  return render_template('christmas.html')
  


@app.route('/recipes/halloween/cobweb_cake/')
def cobweb_cake():
  return render_template('cobweb_cake.html')

@app.route('/recipes/halloween/rocky_road/')
def rocky_road():
  return render_template('rocky_road.html')
  
@app.route('/recipes/halloween/pumpkin_pie/')
def pumpkin_pie():
	with open("test.json") as pumpkinpie:
		json.load(pumpkinpie
		)
  	return render_template('pumpkin_pie2.html')
  
if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

