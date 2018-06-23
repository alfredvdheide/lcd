from pyspeedtest import pyspeedtest
st = pyspeedtest.SpeedTest()
ping = st.ping()
download = st.download()
upload = st.upload()
print("ping: "+str(round(ping,2))+" Ms")
print("down: "+str(download)[0:2]+" MB/s")
print("up: "+str(upload)[0:2]+" MB/s")

