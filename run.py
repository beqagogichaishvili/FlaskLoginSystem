from flask import render_template
from flaskapp import app, login_required
from flaskapp.user.routes import *
from flaskapp.user.models import *

def run():
  @app.route('/')
  def home():
    return render_template('home.html')

  @app.route('/Homepage')
  @login_required
  def loggedhome():
    return render_template('loggedhome.html')

  @app.route('/about')
  def about():
    return render_template('about.html')

  @app.route('/contact')
  def contact():
    return render_template('contact.html')

  @app.route('/register')
  def register():
    return render_template('register.html')

  @app.route('/loginuser')
  def loginuser():
    return render_template('login.html')

  @app.route('/dashboard/')
  @login_required
  def dashboard():
    return render_template('dashboard.html')

  if __name__ == '__main__':
    app.run(debug=False)

  return app
