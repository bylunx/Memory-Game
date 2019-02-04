def gen_toast():
  yield "toto"
  yield "toto2"
  yield "toto3"

for y in gen_toast():
  print y
