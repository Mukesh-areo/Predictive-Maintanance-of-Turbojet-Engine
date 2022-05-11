from flask import Flask ,request
app=Flask(__name__)
@app.route('/',methods=['GET'])
def hello():
    return 'hello guys'
@app.route('/get',methods=['POST'])
def name():
      return 'THIS IS THE POST'


if __name__ == '__main__':
    app.run()