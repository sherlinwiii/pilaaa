class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

def esta_balanceado(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}
    
    for caracter in cadena:
        if caracter in '({[':
            pila.apilar(caracter)
        elif caracter in ')}]':
            if pila.esta_vacia() or pila.desapilar() != pares[caracter]:
                return False
    
    return pila.esta_vacia()


cadena = "{[()]}"
print(esta_balanceado(cadena))  
