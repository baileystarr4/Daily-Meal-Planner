from flask import Flask
import os
from dotenv import load_dotenv
from views import views

app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.register_blueprint(views, url_prefix='/')
  

if __name__ == "__main__":
    app.run(debug=True)