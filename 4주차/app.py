from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
client = MongoClient('mongodb+srv://taesikyoon97:louis17467@cluster0.ncjxm.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/homework", methods=["POST"])
def homework_post():
    user_name = request.form['name_give']
    user_comment = request.form['commnet_give']
    doc = { 
        "name": user_name,
        "comment": user_comment
    }
    db.users.insert_one(doc)
    print(user_name,user_comment)
    return jsonify({'msg': 'DB 저장 완료'})


@app.route("/homework", methods=["GET"])
def homework_get():
    comment_user = list(db.users.find({},{'_id':False}))
    return jsonify({'comments':comment_user})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


#check
