from flask import Flask, render_template, jsonify  
  
app = Flask(__name__)  
  
# 模拟的数据采集函数（实际中，这里应该是从数据库或外部API获取数据）  
def fetch_data():  
    # 这里我们简单地返回一个静态列表  
    return ["数据项1", "数据项2", "数据项3"]  
  
@app.route('/')  
def index():  
    # 调用数据采集函数  
    data = fetch_data()  
    # 渲染模板并传递数据  
    return render_template('index.html', data=data)  
  
if __name__ == '__main__':  
    app.run(debug=True)