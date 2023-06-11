from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    from group import group
else:
    from .group import group

@app.route("/")
def main():
	return group().f()


if __name__ == "__main__":
	app.run(debug=True)
