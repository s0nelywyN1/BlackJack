import random
import time
import webbrowser

count = 0
print('\n'*50)
'''Menu główne'''
print('Witam, oto gra - Black Jack.')
time.sleep(1)
file = open('money.txt', 'r', )
money = file.read()
total_money=money
total_money = int(total_money) + 0
if total_money == 0:
    total_money = int(total_money) + 1
file.close()
def take_first_kart():
    file = open('money.txt', 'r', )
    money = file.read()
    total_money=money
    total_money = int(total_money) + 0
    choise1 = input('chcesz wziąć kolejną kartę? t/n   ')
    print('\n'*5)
    if choise1 == 't':
        print('┌-----┐      ┌-----┐\n'
              '|?    |      |%d    |\n'
              '|  ?  |      |  %s  |\n'
              '|    ?|      |    %d|\n'
              '└-----┘      └-----┘' % (dealer1,kolor_for_dealer, dealer1))
        time.sleep(1)
        print('┌-----┐      ┌-----┐      ┌-----┐\n'
              '|%d    |      |%d    |      |%d    |\n'
              '| %s   |      |  %s  |      |  %s  |\n'
              '|   %d |      |    %d|      |    %d|\n'
              '└-----┘      └-----┘      └-----┘' % (
              player1, player2, player3, kolor1,kolor2,kolor3, player1, player2, player3))
        print('Ty: %d\n' % (player1 + player2 + player3))
        if player1+player2+player3 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' %int(player1 + player2 + player3))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %s$' %(total_money-bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
                file1.close()
            time.sleep(1)
            return choise
        elif player1+player2+player3 == 21 and player1+player2+player3 > dealer:
            print('Krupier: %d' %dealer)
            print('Ty: %d' %int(player1+player2+player3))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' %pot)
            print('Twoje saldo jest teraz: %s$' %(total_money+pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money+pot))
            time.sleep(1)
            return choise
        take_second_cart()

    elif choise1 == 'n':
        if player1 + player2 > dealer and player1 + player2 <= 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' %int(player1 + player2))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money+pot))
            time.sleep(1)
            return choise
        elif player1 + player2 < 21 and player1 + player2 < dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' %int(player1 + player2))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %d$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
            return choise
        elif player1+player2 == dealer and player1+player2 <= 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' %int(player1 + player2))
            print('Remis! Pieniądze zostają z Tobą!\n')
            print('Twoje saldo jest teraz: %d$\n' %total_money)
            time.sleep(1)
            return choise
        elif player1 + player2  < 21 and dealer1 + dealer2 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
    else:
        take_first_kart()


    file.close()

def take_second_cart():
    file = open('money.txt', 'r', )
    money = file.read()
    total_money = money
    total_money = int(total_money) + 0
    choise2 = input('Chcesz wziąć kolejną kartę? t/n   ')

    if choise2 == 't':
        print('┌-----┐      ┌-----┐\n'
              '|?    |      |%d    |\n'
              '|  ?  |      |  %s  |\n'
              '|    ?|      |    %d|\n'
              '└-----┘      └-----┘' % (dealer1,kolor_for_dealer, dealer1))
        time.sleep(1)
        print('┌-----┐      ┌-----┐      ┌-----┐       ┌-----┐\n'
              '|%d    |      |%d    |      |%d    |       |%d    |\n'
              '| %s   |      |  %s  |      |  %s  |       |  %s  |\n'
              '|   %d |      |    %d|      |    %d|       |    %d|\n'
              '└-----┘      └-----┘      └-----┘       └-----┘' % (
              player1, player2, player3, player4,kolor1,kolor2,kolor3,kolor4, player1, player2, player3, player4))
        print('Ty: %d\n' % (player1 + player2 + player3 + player4))
        if player1 + player2 + player3 + player4 == 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 < 21 and player1 + player2 + player3 + player4 > dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %s$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
            return choise
        return take_third_cart()
    elif choise2 == 'n':
        if player1 + player2 + player3 > dealer and player1 + player2 + player3 <= 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 <= 21 and player1 + player2 + player3 == dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3))
            print('Remis! Pieniądze zostają z Tobą!\n')
            print('Twoje saldo jest teraz: %s$\n' % total_money)
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %s$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
        elif player1 + player2 + player3 < 21 and dealer1 + dealer2 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
    else:
        return take_second_cart()

    file.close()

def take_third_cart():
    file = open('money.txt', 'r', )
    money = file.read()
    total_money = money
    total_money = int(total_money) + 0
    choise3 = input('Chcesz wziąć kolejną kartę? t/n  ')
    if choise3 == 't':
        print('┌-----┐      ┌-----┐\n'
              '|?    |      |%d    |\n'
              '|  ?  |      |  %s  |\n'
              '|    ?|      |    %d|\n'
              '└-----┘      └-----┘' % (dealer1,kolor_for_dealer, dealer1))
        time.sleep(1)
        print('┌-----┐      ┌-----┐      ┌-----┐       ┌-----┐       ┌-----┐\n'
              '|%d    |      |%d    |      |%d    |       |%d    |       |%d    |\n'
              '| %s   |      |  %s  |      |  %s  |       |  %s  |       |  %s  |\n'
              '|   %d |      |    %d|      |    %d|       |    %d|       |    %d|\n'
              '└-----┘      └-----┘      └-----┘       └-----┘       └-----┘' % (
                  player1, player2, player3, player4, player5,kolor1,kolor2,kolor3,kolor4,kolor5, player1, player2, player3,
                  player4, player5))
        print('Ty: %d\n' % (player1 + player2 + player3 + player4 + player5))
        if player1 + player2 + player3 + player4 + player5 == 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 < 21 and player1 + player2 + player3 + player4 + player5 > dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %d$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
            return choise
        return take_fourth_cart()
    elif choise3 == 'n':
        if player1 + player2 + player3 + player4 == 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 > dealer and player1 + player2 + player3 + player4 <= 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4<= 21 and player1 + player2 + player3 + player4 == dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('Remis! Pieniądze zostają z Tobą!\n')
            print('Twoje saldo jest teraz: %d$\n' % total_money)
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4> 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(+ player2 + player3 + player4))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %d$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4< 21 and dealer1 + dealer2 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        else:
            take_third_cart()

    file.close()

def take_fourth_cart():
    file = open('money.txt', 'r', )
    money = file.read()
    total_money = money
    total_money = int(total_money) + 0
    choise4 = input('Chcesz wziąć kolejną kartę? t/n   ')
    if choise4 == 't':
        print('┌-----┐      ┌-----┐\n'
              '|?    |      |%d    |\n'
              '|  ?  |      |  %s  |\n'
              '|    ?|      |    %d|\n'
              '└-----┘      └-----┘' % (dealer1, random.randint(kolor1,kolor2,kolor3,kolor4,kolor5), dealer1))
        time.sleep(1)
        print('┌-----┐      ┌-----┐      ┌-----┐       ┌-----┐       ┌-----┐       ┌-----┐\n'
              '|%d    |      |%d    |      |%d    |       |%d    |       |%d    |       |%d    |\n'
              '| %s   |      |  %s  |      |  %s  |       |  %s  |       |  %s  |       |  %s  |\n'
              '|   %d |      |    %d|      |    %d|       |    %d|       |    %d|       |    %d|\n'
              '└-----┘      └-----┘      └-----┘       └-----┘       └-----┘       └-----┘' % (
                  player1, player2, player3, player4, player5,player6,kolor1,kolor2,kolor3,kolor4,kolor5,kolor6, player1, player2, player3,
                  player4, player5,player6))
        print('Ty: %d\n' % (player1 + player2 + player3 + player4 + player5 + player6))
        if player1 + player2 + player3 + player4 + player5 + player6 == 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5 + player6))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 + player6 < 21 and player1 + player2 + player3 + player4 + player5 + player6 > dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5 + player6))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 + player6 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5 + player6))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %d$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
            return choise
    elif choise4 == 'n':
        if player1 + player2 + player3 + player4 + player5== 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 > dealer and player1 + player2 + player3 + player4 + player5 <= 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5 + player6))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 <= 21 and player1 + player2 + player3 + player4 + player5 == dealer:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5))
            print('Remis! Pieniądze zostają z Tobą!\n')
            print('Twoje saldo jest teraz: %d$\n' % total_money)
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5  > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(+ player2 + player3 + player4 + player5))
            print('Przegrałeś!\n')
            print('Twoje saldo jest teraz: %d$' % (total_money - bet))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money - bet))
            time.sleep(1)
            return choise
        elif player1 + player2 + player3 + player4 + player5 < 21 and dealer1 + dealer2 > 21:
            print('Krupier: %d' % dealer)
            print('Ty: %d' % int(player1 + player2 + player3 + player4 + player5 ))
            print('\nWygrałeś i otrzymałeś %s$ na swoje konto!\n' % pot)
            print('Twoje saldo jest teraz: %s$' % (total_money + pot))
            with open('money.txt', 'w') as file1:
                file1.write(str(total_money + pot))
            time.sleep(1)
            return choise
        else:
            take_fourth_cart()

    file.close()



while True:
    file = open('money.txt', 'r', )
    money = file.read()
    total_money=money
    total_money = int(total_money) + 0
    choise = str(input('-> Grać <-\n'
                       '-> Zasady gry <-\n'
                       '-> Wyjście <-\n'
                       '-> Pieniądze <-\n'
                       'Twój wybór --> '))
# '''Start    Start       Start       Start       Start       Start       Start       Start       Start       Start       Start       Start   '''
    if choise == 'Grać' or choise == 'GRAĆ' or choise == 'grać' or choise == 'g' or choise == 'G' or choise == 'Grac' or choise == 'GRAC' or choise == 'grac':
        print('\n' * 50)
        print('Wybrałeś: Grać\n')
        print('\n' * 3)
        time.sleep(0.7)
        print('Pieniądze: %s$' %total_money)
        if total_money == 0:
            file.close()
            with open('money.txt', 'w') as file:
                file.write(str(total_money + 1))
            total_money = int(total_money) + 1
            print('Masz 0$ i nie będziesz mógł grać z powodu braku środków\nSpokojnie, dodałem już 1$ do twojego konta!')
            print('Pieniądze: %s$' %total_money)
            file.close()

        bet = input('Ile stawiasz? (1-%d lub „0” dla wyjścia)\n' % total_money)
        if bet.isdigit() is True:
            pass
        else:
            while bet.isdigit() is False:
                bet = input('Ile stawiasz? (1-%d lub „0” dla wyjścia)\n' % total_money)

        bet = int(bet) + 0
        if bet > total_money or bet < 0:
            print('Nie masz wystarczających środków!\n')
            time.sleep(1)
            choise
        elif bet != 0:
            pot = int((bet / 100) * 150)
            print('Możliwa wygrana kwota: %s\n' %pot)
            money = total_money - bet
            time.sleep(2)
            for i in range(1):
                suit1 = random.randint(1, 4)
                if suit1 == 1:
                    suit1 = '♥'
                elif suit1 == 2:
                    suit1 = '♦'
                elif suit1 == 3:
                    suit1 = '♣'
                elif suit1 == 4:
                    suit1 = '♠'
                suit2 = random.randint(1, 4)
                if suit2 == 1:
                    suit2 = '♥'
                elif suit2 == 2:
                    suit2 = '♦'
                elif suit2 == 3:
                    suit2 = '♣'
                elif suit2 == 4:
                    suit2 = '♠'
                suit3 = random.randint(1, 4)
                if suit3 == 1:
                    suit3 = '♥'
                elif suit3 == 2:
                    suit3 = '♦'
                elif suit3 == 3:
                    suit3 = '♣'
                elif suit3 == 4:
                    suit3 = '♠'
                suit4 = random.randint(1, 4)
                if suit4 == 1:
                    suit4 = '♥'
                elif suit4 == 2:
                    suit4 = '♦'
                elif suit4 == 3:
                    suit4 = '♣'
                elif suit4 == 4:
                    suit4 = '♠'
                suit5 = random.randint(1, 4)
                if suit5 == 1:
                    suit5 = '♥'
                elif suit5 == 2:
                    suit5 = '♦'
                elif suit5 == 3:
                    suit5 = '♣'
                elif suit5 == 4:
                    suit5 = '♠'
                suit6 = random.randint(1, 4)
                if suit6 == 1:
                    suit6 = '♥'
                elif suit6 == 2:
                    suit6 = '♦'
                elif suit6 == 3:
                    suit6 = '♣'
                elif suit6 == 4:
                    suit6 = '♠'
                suit = [suit1, suit2, suit3, suit4, suit5, suit6]
                kolor_for_dealer = random.choice(suit)
                random.shuffle(suit)
                kolor1 = suit.pop()
                kolor2 = suit.pop()
                kolor3 = suit.pop()
                kolor4 = suit.pop()
                kolor5 = suit.pop()
                kolor6 = suit.pop()



                talia = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4
                talia1 = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4
                talia2 = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4
                talia3 = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4
                talia4 = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4
                talia5 = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4
                talia6 = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10, 11] * 4


                random.shuffle(talia)
                random.shuffle(talia1)
                random.shuffle(talia2)
                random.shuffle(talia3)
                random.shuffle(talia4)
                random.shuffle(talia5)
                random.shuffle(talia6)


                dealer1 = talia.pop() #Карты дилера
                dealer2 = talia1.pop()#Карты дилера

                dealersum=dealer1+dealer2
                if dealersum > 21:
                    random.shuffle(talia)
                    random.shuffle(talia1)
                    dealer1 = talia.pop()
                    dealer1 = talia1.pop()

                player1 = talia2.pop() #Карты игрока
                player2 = talia3.pop() #Карты игрока
                player3 = talia4.pop()  # Карты игрока
                player4 = talia5.pop()  # Карты игрока
                player5 = talia6.pop()  # Карты игрока
                player6 = talia6.pop()  # Карты игрока
                player7 = talia6.pop()  # Карты игрока

                playerssum=player1+player2
                if playerssum >21:
                    random.shuffle(talia2)
                    random.shuffle(talia3)
                    player1 = talia2.pop()
                    player2 = talia3.pop()

                print('Krupier ???')
                dealer = dealer1 + dealer2
                print('┌-----┐      ┌-----┐\n'
                      '|?    |      |%d    |\n'
                      '|  ?  |      |  %s  |\n'
                      '|    ?|      |    %d|\n'
                      '└-----┘      └-----┘' %(dealer1,kolor_for_dealer, dealer1))
                time.sleep(1)
                print('┌-----┐      ┌-----┐\n'
                      '|%d    |      |%d    |\n'
                      '| %s   |      |  %s  |\n'
                      '|   %d |      |    %d|\n'
                      '└-----┘      └-----┘' % (player1,player2,kolor1,kolor2,player1,player2))
                print('Ty: %d\n' % (player1 + player2))
                take_first_kart()

        elif bet == 0:
            print('wyszedłeś\n')
            time.sleep(1)
            print('\n' * 50)
            choise

        else:
            choise


# '''Rools    Rools       Rools       Rools       Rools       Rools       Rools       Rools       Rools       Rools       Rools       Rools   '''
    elif choise == 'Zasady' or choise == 'Zasady gry' or choise == 'ZASADY' or choise == 'zasady' or choise == 'z' or choise == 'Z' or choise == 'zasady gry':
        print('\n' * 50)
        print('Wybrałeś: Zasady gry')
        open_link = input('chcesz otworzyć stronę Wikipedii z zasadami gry? t/n\n')
        if open_link == 't':
            webbrowser.open('https://pl.wikipedia.org/wiki/Blackjack#Zasady_gry')
            input('Naciśnij Enter, aby kontynuować..')
            print('\n' * 50)
        elif open_link == 'n':
            print('\n' * 50)
        else:
            while open_link != 't' or open_link != 'n':
                open_link = input('chcesz otworzyć stronę Wikipedii z zasadami gry? t/n\n')
                if open_link == 't':
                    webbrowser.open('https://pl.wikipedia.org/wiki/Blackjack#Zasady_gry')
                    input('Naciśnij Enter, aby kontynuować')
                    print('\n' * 50)
                    choise
                elif open_link == 'n':
                    print('\n' * 50)
                    choise
            choise
# '''Quit     Quit         Quit         Quit         Quit         Quit         Quit         Quit         Quit         Quit         Quit    '''
    elif choise == 'Wyjście' or choise == 'wyjście' or choise == 'WYJŚCIE' or choise == 'w' or choise == 'W' or choise == 'WYJSCIE' or choise == 'wyjscie' or choise == 'Wyjscie' :
        time.sleep(0.5)
        print('Do zobaczenia następnym razem!')
        time.sleep(1)
        break
#Money        Money        Money        Money        Money        Money        Money        Money
    elif choise == 'Pieniądze' or choise == 'p' or choise == 'pieniądze' or choise == 'Pieniądze' or choise == 'PIENIADZE' or choise == 'Pieniadze' or choise == 'pieniadze' :
        print('\nPieniądze: %d$\n' %total_money)
        time.sleep(1)
    else:
        print('Nie ma takiego przycisku. Wybierz z listy: \n')
        choise
file.close()

