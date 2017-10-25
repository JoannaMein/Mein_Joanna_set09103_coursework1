import json
from flask import Flask, url_for, render_template, json, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html'), 200
  
@app.route('/about/')
def about():
  return render_template('about.html'), 200

@app.route('/recipes/')
def recipes():
  return render_template('recipes.html'), 200

@app.route('/recipes/halloween/')
def halloween():
  return render_template('halloween.html'), 200
  
@app.route('/recipes/bonfire/')
def bonfire():
  return render_template('bonfire.html'), 200
  
@app.route('/recipes/christmas/')
def christmas():
  return render_template('christmas.html'), 200

@app.route('/recipes/10_mins/')
def ten_mins():
  return render_template('10_mins.html'), 200
  
@app.route('/recipes/10_20mins/')
def ten_twenty_mins():
  return render_template('10_20mins.html'), 200
  
@app.route('/recipes/20_30mins/')
def twenty_thirthy_mins():
  return render_template('20_30mins.html'), 200
  
@app.route('/recipes/30_40mins/')
def thirty_fourty_mins():
  return render_template('30_40mins.html'), 200
  
@app.route('/recipes/pumpkin_pie/')
@app.route('/recipes/halloween/pumpkin_pie/')
@app.route('/recipes/30_40mins/pumpkin_pie/')
def pumpkin_pie():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Pumpkin Pie":
       print item
       p = item

  return render_template('pumpkin_pie.html', pumpkin=p), 200
  
@app.route('/recipes/cobweb_cake/')
@app.route('/recipes/halloween/cobweb_cake/')
@app.route('/recipes/20_30mins/cobweb_cake/')
def cobweb_cake():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Marshmallow Cobweb Cake":
       print item
       p = item

  return render_template('cobweb_cake.html', cobweb=p), 200
	
@app.route('/recipes/rocky_road/')
@app.route('/recipes/halloween/rocky_road/')
@app.route('/recipes/bonfire/rocky_road/')
@app.route('/recipes/10_mins/rocky_road')
def rocky():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Rocky Road Crunch Bars":
       print item
       p = item

  return render_template('rocky_road.html', rocky=p), 200
  
@app.route('/recipes/peanut_squares/')
@app.route('/recipes/bonfire/peanut_squares/')
@app.route('/recipes/20_30mins/peanut_squares/')
def peanut_squares():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Peanut Butter Squares":
       print item
       p = item

  return render_template('peanut_squares.html', peanut=p), 200
  
@app.route('/recipes/toffee_muffins/')
@app.route('/recipes/bonfire/toffee_muffins/')
@app.route('/recipes/30_40mins/toffee_muffins/')
def toffee_muffins():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Toffee Apple Muffins":
       print item
       p = item

  return render_template('toffee_muffins.html', toffee=p), 200
  
@app.route('/recipes/christmas_wreaths/')
@app.route('/recipes/christmas/christmas_wreaths/')
@app.route('/recipes/10_20mins/christmas_wreaths/')
def christmas_wreaths():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Christmas Wreath Biscuits":
       print item
       p = item

  return render_template('christmas_wreaths.html', wreaths=p), 200

@app.route('/recipes/gingerbread_baubles/')
@app.route('/recipes/christmas/gingerbread_baubles/')
@app.route('/recipes/10_mins/gingerbread_baubles')
def gingerbread_baubles():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Gingerbread Baubles":
       print item
       p = item

  return render_template('gingerbread_baubles.html', baubles=p), 200
  
@app.route('/recipes/mince_pies/')
@app.route('/recipes/christmas/mince_pies/')
@app.route('/recipes/10_20mins/mince_pies/')
def mince_pies():
  recipes = []
  with open('recipes.json', 'r') as f:
     recipes = json.load(f)
     f.close()

  p = {}
  for item in recipes:
     if item['name'] == "Easy Mince Pies":
       print item
       p = item

  return render_template('mince_pies.html', mince=p), 200
  
@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404

if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)

