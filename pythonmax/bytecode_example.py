import dis

def funcion_ejemplo():
    a = 10
    b = 5
    c = a + b

    mes = "hello world"
    print(mes)
    return c

print(dis.dis(funcion_ejemplo)) 
# dis me deja ver la traduccion a bytecode de la funcion

"""
  3           0 RESUME                   0

  4           2 LOAD_CONST               1 (10)
              4 STORE_FAST               0 (a)

  5           6 LOAD_CONST               2 (5)
              8 STORE_FAST               1 (b)

  6          10 LOAD_FAST                0 (a)
             12 LOAD_FAST                1 (b)
             14 BINARY_OP                0 (+)
             18 STORE_FAST               2 (c)

  8          20 LOAD_CONST               3 ('hello world')
             22 STORE_FAST               3 (mes)

  9          24 LOAD_GLOBAL              1 (NULL + print)
             36 LOAD_FAST                3 (mes)
             38 PRECALL                  1
             42 CALL                     1
             52 POP_TOP

 10          54 LOAD_FAST                2 (c)
             56 RETURN_VALUE
None
"""