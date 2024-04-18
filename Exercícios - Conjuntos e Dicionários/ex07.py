#7. Crie uma lista chamada sandwich_orders e a preencha com os nomes devários sanduíches. 
#Em seguida, crie uma lista vazia chamada finished_sandwiches . Percorra a lista de pedidos 
#de sanduíches com um laço e mostre uma mensagem para cada pedido, por exemplo, Preparei seu
#sanduíche de atum. À medida que cada sanduíche for preparado, transfirao para a lista 
#de sanduíches prontos. Depois que todos os sanduíches estiverem prontos, 
#mostre uma mensagem que liste cada sanduíche preparado.

sandwich_orders = ["Bomba", "Vegetariano", "Tasty", "BigMac", "Podrão"]
finished_sandwiches = []

while sandwich_orders:
    pedido = sandwich_orders.pop(0)  
    print(f"Pedido está pronto: {pedido}.")
    finished_sandwiches.append(pedido)

print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print(sanduiche)
