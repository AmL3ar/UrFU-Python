from flask import Flask, url_for

app = Flask(__name__)


@app.route('/test1')
def test1():
    return 'test1'


@app.route('/test2')
def test2():
    return 'test2'


@app.errorhandler(404)
def undefined_page(error):
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.defaults or ()) >= len(rule.arguments or ()):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(f'http://127.0.0.1:5000{url}')
    return "Cписок ссылок, по которым можно перейти:" + "".join(f'</br><a href="{link}">{link}<a>' for link in links)


if __name__ == '__main__':
    app.run(debug=True)
