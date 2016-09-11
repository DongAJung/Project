import serial
import pymysql
from flask import Flask , render_template

app = Flask(__name__)
serialWithArduino= serial.Serial("/dev/ttyACM0" , 9600)


@app.route("/index")
def func2():
    serialWithArduino.write('1')
    obj = serialWithArduino.readline()
    input = obj[:-2].decode()
    
    serialWithArduino.write('2')
    obj_2 = serialWithArduino.readline()
    input_2 = obj_2[:-2].decode()
    
    viewData = {
        'state' : 'OFF' ,
        'data' : input ,
        'data2' : input_2
    }

    return render_template('index.html' , **viewData)
    
@app.route("/index/On")
def func3():
    serialWithArduino.write('1')
    obj = serialWithArduino.readline()
    input = obj[:-2].decode()
    
    serialWithArduino.write('2')
    obj_2 = serialWithArduino.readline()
    input_2 = obj_2[:-2].decode()

    serialWithArduino.write('3')
    
    viewData = {
        'state' : 'ON' ,
        'data' : input ,
        'data2' : input_2
    }

    return render_template('index.html' , **viewData)
@app.route("/index/OFF")
def func4():
    serialWithArduino.write('1')
    obj = serialWithArduino.readline()
    input = obj[:-2].decode()
    
    serialWithArduino.write('2')
    obj_2 = serialWithArduino.readline()
    input_2 = obj_2[:-2].decode()

    serialWithArduino.write('4')
    
    viewData = {
        'state' : 'OFF' ,
        'data' : input ,
        'data2' : input_2
    }

    return render_template('index.html' , **viewData)

@app.route("/index/db")
def func5():
    con = pymysql.connect(host='222.233.48.21' , user='root' , password='admin' , db='sensordata' , charset='utf8')
    cur = con.cursor()
    
    serialWithArduino.write('1')
    obj = serialWithArduino.readline()
    input = obj[:-2].decode()
    
    serialWithArduino.write('2')
    obj_2 = serialWithArduino.readline()
    input_2 = obj_2[:-2].decode()

    serialWithArduino.write('4')
    
    viewData = {
        'state' : 'OFF' ,
        'data' : input ,
        'data2' : input_2
    }

    sql = """insert into arduino(humidity , temperature) value (%s , %s)"""

    cur.execute(sql , (input , input_2))
    con.commit()

    con.close()
    
    return render_template('index.html' , **viewData)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

    
