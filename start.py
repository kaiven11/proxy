#coding=utf-8
from logic.Schedule import Schedule
from logic.api import app
from gevent.wsgi import WSGIServer

def main():
    schedule = Schedule(100)
    schedule.start()
    http_server = WSGIServer(('0.0.0.0', int(3456)), app)
    http_server.serve_forever()
if __name__=="__main__":
    main()
