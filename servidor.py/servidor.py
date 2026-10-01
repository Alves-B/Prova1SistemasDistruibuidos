Servidor.py
from xmlrpc.server import SimplesXMLRPCServer

def calcular_pontos(valor_compra,pontos_por_real):

  Servidor = SimpleXMLRPCServer(("localhost",8004))

servidor.register_function(
  calcular_pontos
  "calcular_pontos"
)
 print("Servidor RPC aguardando solicitações...")
servidor.serve_forever()

