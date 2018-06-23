from pyspeedtest import pyspeedtest




st = pyspeedtest.SpeedTest()
ping = st.ping()
download = st.download()
upload = st.upload()
print("ping: "+str(round(ping,2))+" Ms")
short = ("ping: "+str(round(ping,2))+" Ms")
long = ("down: "+str(download)[0:2]+" MB/s"+". up: "+str(upload)[0:2]+" MB/s")
