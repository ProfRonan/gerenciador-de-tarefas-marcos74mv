"""
Modulo que implementa um gerenciador de tarefas
"""


lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    """
    Adiciona uma tarefa na lista de tarefas
    Lança exceções caso a prioridade seja inválida ou a tarefa já exista

    Args:
        prioridade (bool): True se a tarefa tem prioridade alta, False caso contrário
        tarefa (str): string que representa a tarefa
    """
    # TODO: coloque o código aqui para adicionar um tarefa na lista
    # Caso a prioridade não seja True ou False, levante uma exceção
    # do tipo ValueError com a mensagem "Prioridade inválida"
    # Caso a tarefa já exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa já existe"
    if prioridade != True and prioridade != False:
        raise ValueError("A prioridade é inválida")
    for j in lista_de_tarefas:
        if j["tarefa"] == tarefa:
            raise ValueError("A tarefa já existe")
    lista_de_tarefas.append({"prioridade": prioridade, "tarefa": tarefa})
   # raise NotImplementedError("Adicionar tarefas não implementado")


def remove_tarefas(índices: tuple[int]):
    """
    Remove várias tarefas da lista de tarefas de uma vez, dado uma tupla de índices
    Lança exceções caso a tarefa não exista

    Args:
        índices (tuple[int]): tupla de inteiros que representam os índices das tarefas
                             que devem ser removidas da lista.
    """
    # TODO: coloque o código aqui para remover um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"
    if len(lista_de_tarefas) == 0:
        raise ValueError("A lista está vazia")
    for j in índices:
        if j < 0 or j >= len(lista_de_tarefas):
            raise ValueError("A tarefa não existe")
    for ind in range(len(índices)-1, -1, -1):
        lista_de_tarefas.pop(índices[ind])
    #raise NotImplementedError("Remover tarefas não implementado")


def encontra_tarefa(tarefa: str) -> int:
    """
    Encontra o índice de uma tarefa na lista de tarefas
    Lança exceções caso a tarefa não exista

    Args:
        tarefa (str): string que representa a tarefa
    """
    # TODO: coloque o código aqui para encontrar um tarefa na lista
    # Caso a tarefa não exista na lista, levante uma exceção do tipo ValueError
    # com a mensagem "Tarefa não existe"
    for dic in range(0,len(lista_de_tarefas)):
        if tarefa == lista_de_tarefas[dic]["tarefa"]:
            return dic
    raise ValueError("A tarefa não existe")
    #raise NotImplementedError("Encontrar tarefas não implementado")


def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    # TODO: coloque o código aqui para ordenar a lista de tarefas por prioridade
    # com as tarefas prioritárias no início da lista, seguidas pelas tarefas
    # não prioritárias.
    # As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    # tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    ordenar = []
    global lista_de_tarefas
    for j in range(len(lista_de_tarefas)-1,-1,-1):
        if lista_de_tarefas[j]["prioridade"] == False:
            ordenar.append(lista_de_tarefas[j])
            lista_de_tarefas.pop(j)
    lista_de_tarefas = sorted(lista_de_tarefas, key=lambda dicionario: dicionario["tarefa"].upper())
    ordenar = sorted(ordenar, key=lambda dicionario: dicionario["tarefa"].upper())
    for j in range(0, len(ordenar)):
        lista_de_tarefas.append(ordenar[j])
    #raise NotImplementedError("Ordenar tarefas não implementado")


def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)