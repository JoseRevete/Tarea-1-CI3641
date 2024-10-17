class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_traductor(self, lenguajeBase, lenguajeOrigen, lenguajeDestino):
        if not lenguajeBase or not lenguajeOrigen or not lenguajeDestino: return False
        if lenguajeOrigen not in self.grafo:
            self.grafo[lenguajeOrigen] = {'traductores': {}, 'interpretes': {}}
        if lenguajeBase not in self.grafo[lenguajeOrigen]['traductores']:
            self.grafo[lenguajeOrigen]['traductores'][lenguajeBase] = []
        self.grafo[lenguajeOrigen]['traductores'][lenguajeBase].append(lenguajeDestino)
        return True

    def agregar_interprete(self, lenguajeBase, lenguajeOrigen):
        if not lenguajeBase or not lenguajeOrigen: return False
        if lenguajeOrigen not in self.grafo:
            self.grafo[lenguajeOrigen] = {'traductores': {}, 'interpretes': {}}
        self.grafo[lenguajeOrigen]['interpretes'][lenguajeBase] = True
        return True

    def buscar(self, lenguaje):
        return self.grafo.get(lenguaje, None)

    def buscar_interprete(self, lenguaje):
        esLOCAL = False
        if not lenguaje: return False
        if lenguaje in self.grafo:
            if str(self.grafo[lenguaje]['interpretes']):
                claves_interpretes = list(self.grafo[lenguaje]['interpretes'].keys())
                if str(claves_interpretes):
                    for i in range(len(claves_interpretes)):
                        if str(claves_interpretes[i]) == "LOCAL":
                            esLOCAL = True
                            return esLOCAL
                        else:
                            esLOCAL = self.buscar_interprete(claves_interpretes[i])
                            if esLOCAL:
                                return esLOCAL
        return esLOCAL

    def buscar_traductor(self, lenguaje):
        esLOCAL = False
        if not lenguaje: return False
        if lenguaje in self.grafo:
            if str(self.grafo[lenguaje]['traductores']):
                claves_traductores = list(self.grafo[lenguaje]['traductores'].keys())
                if str(claves_traductores):
                    for i in range(len(claves_traductores)):
                        if str(claves_traductores[i]) == "LOCAL":
                            for j in range(len(self.grafo[lenguaje]['traductores']['LOCAL'])):
                                if str(self.grafo[lenguaje]['traductores']['LOCAL'][j]) == "LOCAL":
                                    esLOCAL = True
                                    break
                                else:
                                    if str(self.grafo[lenguaje]['interpretes'][claves_traductores[j]]) == "LOCAL":
                                        esLOCAL = True
                                        break
                                    elif str(self.grafo[lenguaje]['interpretes'][claves_traductores[j]]) == "LOCAL":
                                        esLOCAL = self.buscar_interprete(claves_traductores[j])
                                        if esLOCAL:
                                            break
                                    else:
                                        esLOCAL = self.buscar_traductor(claves_traductores[j])
                                        if esLOCAL:
                                            break
                        else:
                            esLOCAL = self.buscar_interprete(claves_traductores[i])
                            if esLOCAL:
                                for j in range(len(self.grafo[lenguaje]['traductores'][claves_traductores[i]])):
                                    if str(self.grafo[lenguaje]['traductores'][claves_traductores[i]][j]) == "LOCAL":
                                        esLOCAL = True
                                        break
                                    else:
                                        esLOCAL = self.buscar_interprete(self.grafo[lenguaje]['traductores'][claves_traductores[i]][j])
                                        if esLOCAL:
                                            break
                                        else:
                                            esLOCAL = self.buscar_traductor(self.grafo[lenguaje]['traductores'][claves_traductores[i]][j])
                                            if esLOCAL:
                                                break
                            else:
                                break
        return esLOCAL

    def busqueda(self, lenguaje):
        esLOCAL = False
        if not lenguaje: return None
        if lenguaje == "LOCAL":
            return True
        
        try:
            if str(self.grafo[str(lenguaje)]):
                if  str(self.grafo[str(lenguaje)]['interpretes']):
                    claves_interpretes = list(self.grafo[lenguaje]['interpretes'].keys())
                    if str(claves_interpretes):
                        for i in range(len(claves_interpretes)):
                            if str(claves_interpretes[i]) == "LOCAL": esLOCAL = True; break
                            else:
                                esLOCAL = self.buscar_interprete(claves_interpretes[i])
                                if esLOCAL: break
                if str(self.grafo[str(lenguaje)]['traductores']):
                    claves_traductores = list(self.grafo[lenguaje]['traductores'].keys())
                    if str(claves_traductores):
                        for i in range(len(claves_traductores)):
                            if str(claves_traductores[i]) == "LOCAL":
                                for j in range(len(self.grafo[lenguaje]['traductores']['LOCAL'])):
                                    if str(self.grafo[lenguaje]['traductores']['LOCAL'][j]) == "LOCAL": esLOCAL = True; break
                                    else:
                                        if str(self.grafo[self.grafo[lenguaje]['traductores']['LOCAL'][j]]['interpretes']) == "LOCAL": esLOCAL = True;break
                                        else:
                                            esLOCAL = self.buscar_interprete(self.grafo[lenguaje]['traductores']['LOCAL'][j])
                                            if esLOCAL:break
                                            else:
                                                esLOCAL = self.buscar_traductor(self.grafo[lenguaje]['traductores']['LOCAL'][j])
                                                if esLOCAL: break
                            else:
                                esLOCAL = self.buscar_interprete(claves_traductores[i])
                                if esLOCAL:
                                    for j in range(len(self.grafo[lenguaje]['traductores'][claves_traductores[i]])):
                                        if str(self.grafo[lenguaje]['traductores'][claves_traductores[i]][j]) == "LOCAL": esLOCAL = True;break
                                        else:
                                            esLOCAL = self.buscar_interprete(self.grafo[lenguaje]['traductores'][claves_traductores[i]][j])
                                            if esLOCAL:break
                                            else:
                                                esLOCAL = self.buscar_traductor(self.grafo[lenguaje]['traductores'][claves_traductores[i]][j])
                                                if esLOCAL: break
                                else:
                                    nuevoTraductor = self.grafo[claves_traductores[i]]
                                    if str(nuevoTraductor['traductores']):
                                        claves_traductores_nuevo = list(nuevoTraductor['traductores'].keys())
                                        if str(claves_traductores_nuevo):
                                            for k in range(len(claves_traductores_nuevo)):
                                                if str(claves_traductores_nuevo[k]) == "LOCAL":
                                                    for l in range(len(nuevoTraductor['traductores']['LOCAL'])):
                                                        if str(nuevoTraductor['traductores']['LOCAL'][l]) == "LOCAL":
                                                            esLOCAL = True
                                                            for m in range(len(self.grafo[claves_traductores[i]]['traductores']['LOCAL'])):
                                                                self.agregar_traductor("LOCAL", lenguaje, self.grafo[lenguaje]['traductores'][claves_traductores[i]][m])
                                                                esLOCAL = self.busqueda(self.grafo[lenguaje]['traductores'][claves_traductores[i]][m]); break
                                                        else:
                                                            try:
                                                                if str(self.grafo[nuevoTraductor['traductores']['LOCAL'][l]]['interpretes']['LOCAL']) or False:
                                                                    for m in range(len(self.grafo[lenguaje]['traductores'][claves_traductores[i]])):
                                                                        self.agregar_traductor("LOCAL", lenguaje, self.grafo[lenguaje]['traductores'][claves_traductores[i]][m])
                                                                        esLOCAL = self.busqueda(self.grafo[lenguaje]['traductores'][claves_traductores[i]][m])               
                                                                    break
                                                            except Exception as e:
                                                                esLOCAL = self.buscar_interprete(nuevoTraductor['traductores']['LOCAL'][l])
                                                                if esLOCAL:
                                                                    for m in range(len(self.grafo[lenguaje]['traductores']['LOCAL'])):
                                                                        self.agregar_traductor("LOCAL", lenguaje, self.grafo[lenguaje]['traductores']['LOCAL'][m])
                                                                        esLOCAL = self.busqueda(self.grafo[lenguaje]['traductores']['LOCAL'][m])
                                                                    break
                                                                else:
                                                                    esLOCAL = self.buscar_traductor(self.grafo[claves_traductores[i]]['traductores']['LOCAL'][l])
                                                                    if esLOCAL:
                                                                        for m in range(len(self.grafo[lenguaje]['traductores'][claves_traductores[i]])):
                                                                            self.agregar_traductor("LOCAL", lenguaje, self.grafo[lenguaje]['traductores'][claves_traductores[i]][m])
                                                                            esLOCAL = self.busqueda(lenguaje)
                                                                        break
                                                else:
                                                    esLOCAL = self.buscar_interprete(claves_traductores_nuevo[k])
                                                    if esLOCAL:
                                                        for l in range(len(nuevoTraductor['traductores'][claves_traductores_nuevo[k]])):
                                                            if str(nuevoTraductor['traductores'][claves_traductores_nuevo[k]][l]) == "LOCAL":
                                                                esLOCAL = True
                                                                for m in range(len(self.grafo[lenguaje]['traductores']['LOCAL'])):
                                                                    self.agregar_traductor("LOCAL", lenguaje, self.grafo[lenguaje]['traductores']['LOCAL'][m])
                                                                    esLOCAL = self.busqueda(self.grafo[lenguaje]['traductores']['LOCAL'][m])
                                                                break
                                                            else:
                                                                esLOCAL = self.buscar_interprete(nuevoTraductor['traductores'][claves_traductores_nuevo[k]][l])
                                                                if esLOCAL:
                                                                    for m in range(len(self.grafo[lenguaje]['traductores'][claves_traductores[i]])):
                                                                        self.agregar_traductor(self.grafo[lenguaje]['traductores'][claves_traductores[i]][m], lenguaje, "LOCAL")
                                                                        esLOCAL = self.busqueda(self.grafo[lenguaje]['traductores'][claves_traductores[i]][m])
                                                                    break
                                                                else:
                                                                    esLOCAL = self.buscar_traductor(nuevoTraductor['traductores'][claves_traductores_nuevo[k]][l])
                                                                    if esLOCAL:
                                                                        for m in range(len(self.grafo[lenguaje]['traductores']['LOCAL'])):
                                                                            self.agregar_traductor("LOCAL", lenguaje, self.grafo[lenguaje]['traductores']['LOCAL'][m])
                                                                            esLOCAL = self.busqueda(self.grafo[lenguaje]['traductores']['LOCAL'][m])
                                                                        break
                                                    else:
                                                        break
                                    if esLOCAL:
                                        break
        except Exception as e:
            return False
        return esLOCAL

datos_programas = {}

G = Grafo()

def main():
    print("Simulador iniciado.")
    while True:
        entrada = input("$> ")
        if entrada.upper() == "SALIR":
            break
        entradas(entrada.split(" ")[0], entrada.split(" ")[1:])
    print("Simulador finalizado.")

def entradas(primera_entrada, resto_entrada=None):
    if primera_entrada:
        primera_entrada = primera_entrada.upper()
    if primera_entrada == "DEFINIR":
        definir(resto_entrada)
    elif primera_entrada == "EJECUTABLE":
        ejecutable(resto_entrada)
    else: ayuda()
    return True

def definir(entrada):
    if not entrada or len(entrada) < 2: print("Error: Faltan argumentos."); return False
    
    comando = entrada[0].upper()
    if comando == "PROGRAMA":
        programa(entrada[1:])
    elif comando == "INTERPRETE":
        interprete(entrada[1:])
    elif comando == "TRADUCTOR":
        traductor(entrada[1:])
    else: ayuda() 
    return True

def programa(entrada):
    if not entrada or len(entrada) != 2: print("Error: Demasiados o pocos argumentos."); return False
    try:
        nombre = entrada[0]
        lenguaje = entrada[1]
        respuesta_datos = datos_programas.get(nombre)
        
        if respuesta_datos is not None:
            if lenguaje in respuesta_datos:raise Exception("El programa ya existe.")
            datos_programas[nombre].append(lenguaje)
        else:
            datos_programas[nombre] = [lenguaje]
        print(f"Programa {nombre} definido.")
    except Exception as e: print(f"Error: {e}")
    return True

def interprete(entrada):
    if not entrada or len(entrada) != 2: print("Error: Demasiados o pocos argumentos."); return False
    try:
        lenguajeBase = entrada[0]
        lenguaje = entrada[1]
        respuesta_datos = G.buscar(lenguaje)
        
        if respuesta_datos is not None:
            if lenguajeBase in respuesta_datos['interpretes']: raise Exception("El interprete ya existe.")
            G.agregar_interprete(lenguajeBase, lenguaje)
        else:
            G.agregar_interprete(lenguajeBase, lenguaje)
        print(f"Interprete {lenguaje} definido.")
    except Exception as e: print(f"Error: {e}")
    return True

def traductor(entrada):
    if not entrada or len(entrada) != 3: print("Error: Demasiados o pocos argumentos."); return False
    
    try:
        lenguajeBase = entrada[0]
        lenguajeOrigen = entrada[1]
        lenguajeDestino = entrada[2]
        traductores = G.buscar(lenguajeOrigen)
        if traductores is not None:
            if lenguajeBase in traductores['traductores']:
                if lenguajeDestino in traductores['traductores'][lenguajeBase]: raise Exception("El traductor ya existe.")
            G.agregar_traductor(lenguajeBase, lenguajeOrigen, lenguajeDestino)
        else:
            G.agregar_traductor(lenguajeBase, lenguajeOrigen, lenguajeDestino)
        print(f"Traductor {lenguajeOrigen} a {lenguajeDestino} definido.")
    except Exception as e: print(f"Error: {e}")

    return True

def ejecutable(entrada):
    if not entrada or len(entrada) != 1: print("Error: Demasiados o pocos argumentos."); return False
    esLOCAL = False
    try:
        nombre = entrada[0]
        respuesta_datos = datos_programas.get(nombre)
        if respuesta_datos is not None:
            for lenguaje in respuesta_datos:
                esLOCAL = G.busqueda(str(lenguaje))
                if esLOCAL:
                    print(f"Programa {nombre} ejecutable en {lenguaje}.")
                else:
                    print(f"Programa {nombre} no ejecutable en {lenguaje}.")
                
        else: print(f"Programa {nombre} no definido.")
    except Exception as e: print(f"Error: {e}")
    return esLOCAL

def ayuda():
    print("Comandos disponibles:")
    print("DEFINIR PROGRAMA <nombre> <lenguaje>")
    print("DEFINIR INTERPRETE <lenguajeBase> <lenguaje>")
    print("DEFINIR TRADUCTOR <lenguajeBase> <lenguajeOrigen> <lenguajeDestino>")
    print("EJECUTABLE <nombre>")
    print("SALIR")
    return True

if __name__ == "__main__":
    main()