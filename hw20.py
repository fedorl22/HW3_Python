# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

lst1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S','T', 'R']
lst2 = ['D', 'G']
lst3 = ['B', 'C', 'M', 'P']
lst4 = ['F', 'H', 'V', 'W', 'Y']
lst5 = ['K']
lst8 = ['J', 'X']
lst10 = ['Q', 'Z']
lstr1 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
lstr2 = ['Д', 'К', 'Л', 'М', 'П', 'У']
lstr3 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
lstr4 = ['Й', 'Ы']
lstr5 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
lstr8 = ['Ш', 'Э', 'Ю']
lstr10 = ['Ф', 'Щ', 'Ъ']
world = list(input('Введите слово заглавными буквами: '))
cost_eng = 0
cost_rus = 0
for i in world:
    if i in lst1:
        cost_eng+=1    
    elif i in lst2:
        cost_eng+=2
    elif i in lst3:
        cost_eng+=3
    elif i in lst4:
        cost_eng+=4
    elif i in lst5:
        cost_eng+=5
    elif i in lst8:
        cost_eng+=8
    elif i in lst10:
        cost_eng+=10
if cost_eng!=0:
        print(' Английское слово стоит: ', cost_eng) 
for i in world:
    if i in lstr1:
        cost_rus+=1    
    elif i in lstr2:
        cost_rus+=2
    elif i in lstr3:
        cost_rus+=3
    elif i in lstr4:
        cost_rus+=4
    elif i in lstr5:
        cost_rus+=5
    elif i in lstr8:
        cost_rus+=8
    elif i in lstr10:
        cost_rus+=10  
if cost_rus!=0:
    print(' Русское слово стоит: ', cost_rus) 
 




