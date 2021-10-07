from hashlib import sha256

data = "<data here>"

h = sha256()
h.update(data.encode())

print(h.hexdigest())