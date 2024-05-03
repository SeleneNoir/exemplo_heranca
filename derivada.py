from somaMultiplica import ClasseSomaMultiplica

class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b;
    def dividir(self):
        return self.a / self.b;

d = Derivada(10, 20);
print(f'A soma de 10 e 20 é: {d.somar}');
print(issubclass(Derivada, ClasseSomaMultiplica));