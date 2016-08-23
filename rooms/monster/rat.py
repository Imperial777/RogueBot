from constants import *

name = 'Крыса'

hp = 20
element = NONE
damage_range =  ( 2, 4 )

coins = 7

loot = [ 'rat_tooth' ]

def enter(user, reply):
	if user.has_aura(BUDDHA):
		reply('Крысы не трогают буддистов. Иди с миром')
		user.won(reply)
	else:
		reply('ААААААААА! ТУТ КРЫСА. УБЕЙ ЕЕ.')
