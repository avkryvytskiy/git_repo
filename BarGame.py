#BarGame.py - Рабочий листинг
import math, random, sys
""" Вспомогательные функции """
""" Помещен в Git repo """
"""
 Релизы:
     18.06.2017 - Первая робочая версия "прогон" v.0.0.1
 Планы:
     Пользовательское меню - пуск в анонимном режиме, представление пользователей, выход и т.д.
	 Запись результатов в файл
"""


# Вспомогательная Функция "Формирование Простого Листа (из 0 - нулей)
def create_simpleList(num): 
    simpleList = []
    for i in range(num):
            simpleList.append(0)
    return simpleList                    # Test Pass

# Вспомогательная Функция "Простой Рандом Простого Листа"
def random_simpleList(simpleList,low = 1, high = 6): 
    import random
    if simpleList != []:
        for i in range(len(simpleList)):
            simpleList[i] = random.randint(low,high)  
    else:
        print("Отсутствует объект")
    return simpleList                     # Test Pass

# Вспомогательная Функция "Получение целого"
def get_int(msg):
    print("Введите число %s ... " % (msg), end = "")
    while 1:
        count = input()
        try:
            count = int(count)
            break
        except ValueError:
            print("Введите число %s ... " % (msg), end = "")
    
    return count                          # Test Pass

# Вспомогательная Функция "Удаление лишнего числа из листа"
def remove_num_from_simple_list(simpleList, num): 
    while num in simpleList:
        simpleList.remove(num)
    return simpleList                      # Test Pass



def count_num_in_simple_list(simpleList, num): 
    countNum = [] 
    for i in range(len(simpleList)):
        if simpleList[i] == num:
            countNum.append(0)
    return(countNum)

def num_go_to_next_list(twoLevelList, num): 
    len_two_level_list = len(twoLevelList)
    for i in range(len_two_level_list):
        if i < len_two_level_list-1:
            num_to_go = count_num_in_simple_list(twoLevelList[i], num) #Вызов функции
            twoLevelList[i+1].extend(num_to_go)
            #print(num_to_go)
        else:
            num_to_go = count_num_in_simple_list(twoLevelList[i], num)
            twoLevelList[0].extend(num_to_go)
            #print(num_to_go)
            #print("END") 
    return(twoLevelList)

""" Основные функции """
# Функция "На Старт" - формирование игровых КОНСТАНТ (игроки, кости)    
def go_on_start(numOfPlayers = 2,numOfDices = 6):
    listOfDice = []
    listOfPlayers = []
    for i in range(numOfPlayers):
        listOfDice.append(create_simpleList(numOfDices))
        listOfPlayers.append("Player " + str(i+1))
    return listOfPlayers, listOfDice

# Функция "Первый расклад"  num - количество костей, list2L - двухуровневый  
def first_layout(list2L, num):
    for i in range(len(list2L)):
        list2L[i] = create_simpleList(num)
    return list2L

# Функция "Бросок"    
def throw(dices):
    if dices != []:
        for i in range(len(dices)):
            dices[i] = random_simpleList(dices[i])
    else:
         print("Список пуст")
    return (dices)

# Функция "Расклад" - отображение после броска    
def layout(players, dices):
    for i in range(len(players)):
        print ("\n", players[i] + "...", end = " ")
        for j in range(len(dices[i])):
            print (dices[i][j], end = " ")
    print ("\n")

      
""" НАЧАЛО РАБОТЫ """

""" Константы """
players_str = 'ИГРОКОВ'
dices_str = 'КОСТЕЙ для ИГРОКА'

""" Основные переменные """
numPlayers = get_int(players_str) # Ввод "Количество игроков"
numDices = get_int(dices_str)     # Ввод "Количество костей у игрока"
""" """
winners = []                      # Список Победителей
players = []                      # Список Игроков
dices = []                        # Наборы Костей
delList = []

""" ИГРА """
print ("START")
print("-" * 20)
print ("Количество ИГРОКОВ - ", numPlayers)
print ("Количество Костей на Игрока - ", numDices)
print("-" * 20)
""" Формирование игрового пула """
print ("Предсталяем игровой пул")
players, dices = go_on_start(numPlayers,numDices)
layout(players, dices) # Расклад
print("-" * 20)

""" БРОСКИ """
print (len(winners))
while len(winners) <= (numPlayers - 2):
    # while [] not in dices:
    
    #input("Проводим бросок")
    throw(dices) # Первый бросок
    layout(players, dices) # Расклад
    #input("Убираем 1-цы")
    for i in range(len(dices)):   # Убираем 1-цы
        remove_num_from_simple_list(dices[i], 1)
    layout(players, dices) # Расклад
    #input("Переносим 6-ки")
    num_go_to_next_list(dices, 6)
    for i in range(len(dices)):   # Убираем 6-ки
        remove_num_from_simple_list(dices[i], 6)

    layout(players, dices) # Расклад

    for i in range(len(dices)):
        if dices[i] == []:
            delList.append(i)
                
    print ("delList = ", delList)   # глючит!!!!!
    for i in range(len(delList)):
        # print ("delList[i] = ", delList[i])
        # print ("players[delList[i]] = ", players[delList[i]])
        winners.append(players[delList[i]])
        players.pop(delList[i])  
        players.insert(delList[i], 22)
        dices.pop(delList[i])
        dices.insert(delList[i], 22)
    remove_num_from_simple_list(players, 22)
    remove_num_from_simple_list(dices, 22) 

    # print("delList = ", delList)
    print ("winners = ", winners)
    # print ("players = ", players) 
    # print ("dices = ", dices)             
    delList.clear()
    # print("delList = ", delList)
    # print (len(winners))
    # input ("Ищем дальше")
                    
print ("players = ", players)
""" Прерывание """
sys.exit(0)



