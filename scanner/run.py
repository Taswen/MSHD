from app.app import app
from scanner.scanner import Scanner

if __name__ == '__main__':
    Scanner(app).run()
