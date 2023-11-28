# MathHelper

**MathHelper** es un módulo en Python que te permite realizar operaciones matemáticas escritas en letras o números y también convertir números escritos en letras a su equivalente en formato de dígitos.

## Características

- Realiza operaciones matemáticas básicas (suma, resta, multiplicación, división, exponentes, raíces).
- Convierte números escritos en letras (en español) a su representación numérica.
- No utiliza librerías ni consume API's.

## Uso

### Ejemplo de Operación Matemática

```python
# Importa la clase MathHelper
from math_helper import MathHelper

# Crea una instancia de MathHelper
calculadora = MathHelper()

# Ejemplo de operación
operacion = "raiz cubica de veinte mil doscientos mas cinco multiplicado por diez mil menos un millon" # 20200**(1/3)+5*10000-1000000
resultado = calculadora.solve_operation(operacion)
print("Resultado:", resultado) # -949972.77

# Ejemplo de conversión de número escrito en letras a dígitos
numero_escrito = "novecientos millones cuatrocientos veinte mil dos"
numero = calculadora.text2num(numero_escrito)
print(f"{numero_escrito.capitalize()} en dígitos: {numero}") # 900420002
