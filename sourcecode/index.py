from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
  
@app.route('/about/')
def about():
  return render_template('about.html')

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
  
@app.route('/recipes/10_mins/')
def ten_mins():
  return render_template('10_mins.html')
  
@app.route('/recipes/10_20mins/')
def ten_twenty_mins():
  return render_template('10_20mins.html')
  
@app.route('/recipes/20_30mins/')
def twenty_thirthy_mins():
  return render_template('20_30mins.html')
  
@app.route('/recipes/30_40mins/')
def thirty_fourty_mins():
  return render_template('30_40mins.html')
  
@app.route('/recipes/halloween/pumpkin_pie/')
@app.route('/recipes/halloween/pumpkin_pie/')
def pumpkin_pie():
  return render_template('pumpkin_pie.html')
  
@app.route('/recipes/cobweb_cake/')
@app.route('/recipes/halloween/cobweb_cake/')
def cobweb_cake():
  return render_template('cobweb_cake.html')

@app.route('/recipes/rocky_road/')
@app.route('/recipes/halloween/rocky_road/')
@app.route('/recipes/bonfire/rocky_road/')
def rocky_road():
  return render_template('rocky_road.html')
  
if __name__ == ("__main__"):
  app.run(host='0.0.0.0', debug=True)