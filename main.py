import sys
from myapp import create_app

sys.dont_write_bytecode = True

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)