from flask import Flask
from helper import manual_testing, output_lable

app = Flask(__name__)

str = """WASHINGTON (AP) — With little time left to prevent a government shutdown, the House is in a familiar position: effectively paralyzed as conservatives feud with Speaker Kevin McCarthy over matters large and small. McCarthy has pushed the Republican conference to embrace a short-term funding plan that would also include a sweeping Republican proposal for the southern border. But a small group of hardline conservatives has defied the speaker in a quest to get rid of stopgap funding plans, known as continuing resolutions, even if opposing them means forcing a government shutdown. It’s left McCarthy at an impasse. He will likely be left with the political damage of a shutdown unless he turns to Democrats for help in passing a bipartisan bill. But working with Democrats would give hard-right Republicans reason to remove him as speaker."""

@app.route('/')
def ex():
    res = manual_testing(str)
    re = output_lable(int(res))
    print('fafff',re)
    return re

@app.route('/my_post_route', methods=['POST'])
def my_post_route():
    # data = request.body.form['key']
    res = manual_testing(str)
    return res
# @app.route('/recognize', methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)
