class MathHelper:
    def __init__(self):
        self.numbers = []
        self.operadores = []
        self.others = ["y", "mil", "millon", "millones"]
        self.operaciones = {
            "mas": "+",
            "sumado": "+",
            "sumame": "+",
            "sumar": "+",
            "sumas": "+",
            "suma": "+",
            "+": "+",
            "menos": "-",
            "restado": "-",
            "restame": "-",
            "restar": "-",
            "restas": "-",
            "resta": "-",
            "-": "-",
            "multiplicado": "*",
            "por": "*",
            "*": "*",
            "x": "*",
            "dividido": "/",
            "entre": "/",
            "/": "/",
            "**": "**",
            "^": "**",
            "elevado": "**",
            "cuadrado": "**2",
            "cubo": "**3",
            "cuarta": "**4",
            "quinta": "**5",
            "sexta": "**6",
            "cuadrada": "**(1/2)",
            "cubica": "**(1/3)"
        }

    def solve_operation(self, operacion):
        try:
            resultado = eval(operacion)
        except:       
            operacion = self._fix_operation(operacion)
            self._find_numbers(0, operacion)
            self._find_operators(operacion)
            self._converter(self.numbers)
            resultado = self._resolve(self.numbers, self.operadores)
        finally:
            return resultado
        
    def text2num(self, str):
        if str.isdigit():
            return int(str)

        unidades = ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        diez = ["once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
        veinte = ["veintiuno", "veintidos", "veintitres", "veinticuatro", "veinticinco", "veintiseis", "veintisiete",   "veintiocho", "veintinueve"]
        decenas = ["diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
        centenas = ["ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]

        numero = 0
        millones = 0

        tokens = str.split()

        for token in tokens:
            if token != "y":
                if token == "cero":
                    numero = 0
                elif token == "cien":
                    numero = 100
                elif token == "mil":
                    if numero == 0:
                        numero = 1000
                    else:
                        numero = numero * 1000
                elif token == "millon" or token == "millones":
                    if numero == 0:
                        millones = 1000000
                    else:
                        millones += numero * 1000000
                        numero = 0
                else:
                    for i in range(9):
                        if unidades[i] == token:
                            numero = numero + i + 1
                            break
                        elif diez[i] == token:
                            numero = numero + (i + 1) + 10
                            break
                        elif veinte[i] == token:
                            numero = numero + (i + 1) + 20
                            break
                        elif decenas[i] == token:
                            numero = numero + ((i + 1) * 10)
                            break
                        elif centenas[i] == token:
                            numero = numero + ((i + 1) * 100)
                            break

        numero += millones                   

        if tokens[0] != "cero" and numero == 0 and tokens[0] != "y":
            raise ValueError("Error. Valores inválidos.")
        else:
            return numero

    def _fix_operation(self, operation):
        operation = operation.lower()
        operation += " "
        tildes = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', '?': '', "¿": '', '¡': '', "!": '', 'multiplicado por': 'por', 'elevado al cuadrado': 'cuadrado', 'elevado al cubo': 'cubo', 'elevado a la cuarta': 'cuarta', 'elevado a la quinta': 'quinta', 'elevado a la sexta': 'sexta'}

        for tilde, sin_tilde in tildes.items():
            operation = operation.replace(tilde, sin_tilde)

        return operation.split(" ")
    
    def _find_numbers(self, start, operacion):
        curr_num = ""
        for i in range(start, len(operacion)):
            if operacion[i].isdigit():
                self.numbers.append(operacion[i])
                self._find_numbers(i+1, operacion)
                break
            try:
                num = self.text2num(operacion[i])
                curr_num = curr_num + operacion[i] + " "
                if i == len(operacion)-1:
                    self.numbers.append(curr_num)
            except:
                num = operacion[i]
                if num in self.others:
                    curr_num = curr_num + num + " "
                else:
                    if curr_num != '':
                        self.numbers.append(curr_num)
                    self._find_numbers(i+1, operacion)
                    break

    def _find_operators(self, operacion):
        for w in operacion:
            if w in self.operaciones.keys():
                self.operadores.append(self.operaciones[w])   

    def _converter(self, nums):
        for i in range(len(nums)):
            if not nums[i].isdigit():
                nums[i] = self.text2num(nums[i])
            else:
                nums[i] = nums[i]

    def _resolve(self, nums, operators):
        try:
            lenght = max(len(operators), len(nums))
            operation = ''
            for i in range(lenght):
                if i == 0:
                    operation += str(nums[i])
                    operation += operators[i]
                else:
                    if (operation[-1].isdigit()) or (operation[-1] == ")"):
                        if i < len(operators): operation += operators[i]
                        try:
                            if (operation[-3] == "*" and operation[-2] == "*") or (operation[-1] == ")"):
                                operation += operators[i+1]
                                operation += str(nums[i])
                                operators.pop(i+1)
                            else:
                                operation += str(nums[i])
                        except:
                            pass
                    else:
                        if i < len(nums): operation += str(nums[i])
                        if i < len(operators): operation += operators[i]

            print("Operacion:", operation)
            return round(eval(operation), 2)
        except:
            raise ValueError("Error. No fue posible resolver la operación.")