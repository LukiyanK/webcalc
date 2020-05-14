#!/usr/bin/env python
from flask import (Flask, request)
import math
import redis
from datetime import datetime
app = Flask(__name__)
r = redis.Redis()
def addition(num1, num2):
  result =num1+num2
  now = datetime.now()
  tored={"arg1":num1,"op":"plus","arg2":num2,"res":result}
  r.hmset(now.strftime("%m/%d/%Y, %H:%M:%S"),tored)
  return str(result)
def subtraction(num1, num2):
  result = num1 - num2
  now = datetime.now()
  tored={"arg1":num1,"op":"sub","arg2":num2,"res":result}
  r.hmset(now.strftime("%m/%d/%Y, %H:%M:%S"),tored)
  return str(result)
def mul(num1, num2):
  result = num1*num2
  now = datetime.now()
  tored={"arg1":num1,"op":"mul","arg2":num2,"res":result}
  r.hmset(now.strftime("%m/%d/%Y, %H:%M:%S"),tored)
  return str(result)
def division(num1, num2):
  result1 = num1/num2
  result2 = num1 % num2
  #result = str(result1)+","+str(result2)
  result = float(num1)/float(num2)
  now = datetime.now()
  tored={"arg1":num1,"op":"div","arg2":num2,"res":result}
  r.hmset(now.strftime("%m/%d/%Y, %H:%M:%S"),tored)
  return str(result)
def default(num1, num2):
  return "### op = plus | sub | mul | div"
switcher = {
    "plus": addition,
    "sub": subtraction,
    "mul": mul,
    "div": division
}

#r = redis.Redis()

def switch(operation, num1, num2):
  return str(switcher.get(operation, default)(num1, num2))
@app.route('/calc', methods=['POST','GET'])
def dadd_args():
    try:
        arg1 = int(request.args['arg1'])
        arg2 = int(request.args['arg2'])
        arg3 = str(request.args['op'])
        #return (jsonify({'answer':answer}), 200)
        return (switch(arg3,arg1, arg2))
    except KeyError:
        abort(400)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
