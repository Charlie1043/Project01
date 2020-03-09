import struct

st = struct.Struct("12s3si")

data = st.pack("Charlie".encode(), "男".encode(), 180)
print(data)

data = st.unpack(data)
print(data)
print(data[0].decode().strip("\x00"))
print(data[1].strip(b"\x00").decode())