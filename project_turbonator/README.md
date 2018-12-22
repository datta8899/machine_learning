Open Anaconda CMD prompt and run below.

>> set FLASK_APP=app.py

>> flask run
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [23/Dec/2018 00:23:18] "POST /predict HTTP/1.1" 200 -


Then run below CURL command from another window.

>> curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/predict -d "[{\"house_id\":1001,\"age\":50},{\"house_id\":1002,\"age\":75},{\"house_id\":1003,\"age\":100}]"
   age  house_id  predicted_price
0   50      1001        24.901049
1   75      1002        22.065760
2  100      1003        19.230470
