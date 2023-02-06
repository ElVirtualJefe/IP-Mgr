print('__name__ = %s' % (__name__))
_ONE_DAY_IN_SECONDS = 24 * 60 * 60

from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from urllib.parse import quote_plus as urlquote

if __name__ == 'app':
    from app.models import db
elif __name__ == '__main__':
    from models import db

# our database uri
username = config.get("postgres","DB_USERNAME")
password = urlquote(config.get("postgres","DB_PASSWORD"))
dbname = config.get("postgres","DB_NAME")
dbserver = config.get("postgres","DB_SERVER")
dbport = config.getint("postgres","DB_PORT")

SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{username}:{password}@{dbserver}:{dbport}/{dbname}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

engine = create_engine(SQLALCHEMY_DATABASE_URI)
db.create_all(engine)

Session = scoped_session(sessionmaker(bind=engine))
sess = Session()


import grpc,time
from concurrent import futures
from app.implementations import IpAddressServiceServicer
from app.stubs import ipAddress_pb2_grpc as ip_grpc


"""Start grpc server servicing FMS RPCs."""
print("Starting gRPC Server...")
# create grpc server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

ipAddressServicer = IpAddressServiceServicer()
ip_grpc.add_IpAddressServiceServicer_to_server(ipAddressServicer,server)

# start server
server_port = config.get("server","PORT")
server_address = config.get("server","ADDRESS")
address = '%s:%s' % (server_address, server_port)
#logging.info('Starting grpc server at %s', address)

server.add_insecure_port(address)
server.start()
print('gRPC Server running at %s' % address)

# start() does not block so sleep-loop
try:
    server.wait_for_termination()
    #while True:
        #time.sleep(_ONE_DAY_IN_SECONDS)
except KeyboardInterrupt:
    print("Stopping gRPC Server...")
    server.stop(0)





