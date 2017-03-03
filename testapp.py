from os.path import dirname, join
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition

#// Armor Attack
AASounds = [
	[ 'Tank En.',    'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Beep En.',    'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Chopper En.', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Tank Fire',      'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 7],
	[ 'Hi Explosion',   'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 6],
	[ 'Jeep Fire',      'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 5],
	[ 'Lo Explosion',   'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 4],
	[ 'Tank Speed',     'ACT_SET', 0, 'ST_AAS', 0x000F, 0x0000, 0]
]

#// Rip Off
ROSounds = [
	[ 'Explsn',         'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 7],
	[ 'Laser',             'ACT_PLS', 4, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Torpedo',           'ACT_PLS', 3, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'BG Speed',  'ACT_SET', 0, 'ST_ROS', 0x0007, 0x0000, 3],
	[ 'BG En.', 'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 2],
	[ 'Beep',              'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 1],
	[ 'Motor',             'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 0]
]

#// Solar Quest
SQSounds = [
	[ 'Loud Explsn', 'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  7],
	[ 'Soft Explsn', 'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  6],
	[ 'Thrust',         'ACT_TGL', 0, 'ST_SQ1', 0x0001, 0x0001,  5],
	[ 'Fire',           'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  4],
	[ 'Capture',        'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  3],
	[ 'Nuke',           'ACT_TGL', 0, 'ST_SQ1', 0x0001, 0x0000,  2],
	[ 'Photon',         'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  1],
	[ 'Music En.',   'ACT_TGL', 0, 'ST_SQ2', 0x0001, 0x0000, 15],
	[ 'Music Vol',   'ACT_SET', 0, 'ST_SQ2', 0x0007, 0x0007, 12],
	[ 'Music Pitch',    'ACT_SET', 0, 'ST_SQ2', 0x0FFF, 0x0000,  0]
]

#// Space War
SWSounds = [
	[ 'Explosion',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Fire',         'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Thrust 1',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Thrust 2',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Sound En.', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4]
]

#// Star Castle
SCSounds = [
	[ 'Loud Explsn',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Soft Explsn',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Laser En.',      'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Fire Ball En.',  'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 7],
	[ 'Shield En.',     'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 6],
	[ 'Star En.',       'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0000, 5],
	[ 'Thrust En.',     'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 4],
	[ 'BG En.', 'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 3],
	[ 'BG Speed',  'ACT_SET', 0, 'ST_AAS', 0x0007, 0x0000, 0]
]

#// Star Hawk
SHSounds = [
	[ 'Explosion',     'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Laser 1',       'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Laser 2',       'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0000, 2],
	[ 'K On/Off',      'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Master On/Off', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'K Exit',        'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0000, 7]
]

#// Sundance
SDSounds = [
	[ 'Bong',      'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 0],
	[ 'Whoosh',    'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Explsn', 'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Ping 1',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Ping 2',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Hatch',     'ACT_PLS', 6, 'ST_OUT', 0x0001, 0x0001, 7]
];

#// Tailgunner
TGSounds = [
	[ 'Explsn',     'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 0],
	[ 'Rumble',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 1],
	[ 'Laser',         'ACT_TGR',  4, 'ST_TGS', 0x0001, 0x0001, 2],
	[ 'Shield',        'ACT_TGL',  0, 'ST_TGS', 0x0001, 0x0001, 3],
	[ 'Shield Bounce', 'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 4],
	[ 'Hyperspace',    'ACT_PLS', 34, 'ST_TGS', 0x0001, 0x0001, 5],
]

SoundBoard = [
	[ 'Armor Attack', len(AASounds), AASounds],
	[ 'Rip Off',      len(ROSounds), ROSounds],
	[ 'Solar Quest',  len(SQSounds), SQSounds],
	[ 'Space War(s)', len(SWSounds), SWSounds],
	[ 'Star Castle',  len(SCSounds), SCSounds],
	[ 'Star Hawk',    len(SHSounds), SHSounds],
	[ 'Sundance',     len(SDSounds), SDSounds],
	[ 'Tailgunner',   len(TGSounds), TGSounds]
]

GameBoards = {
	'Armor Attack': AASounds,
	'Rip Off': ROSounds,
	'Solar Quest': SQSounds,
	'Space Wars': SWSounds,
	'Star Castle': SCSounds,
	'Star Hawk': SHSounds,
	'Sundance': SDSounds,
	'Tailgunner': TGSounds
}

blue = [0.33, 0.5, 1, 1]
#'dkblue': [0.15, 0.33, 0.5, 1]

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')

class GameButton(Button):
	pass

class SoundButton(Button):
	pass

class MainMenu(Screen):
	pass

class Sounds(Screen):
	game = None

	def on_pre_enter(self):
		self.ids.btnstack.clear_widgets()
		id = 0

		for sound in GameBoards[self.game]:
			btn = SoundButton()
			btn.text = sound[0]
			btn.id = str(id)
			self.ids.btnstack.add_widget(btn)
			id += 1

	def set_gamename(self, gamename):
		self.game = gamename

	def play_sound(self):
		print sound

class AdvSounds(Screen):
	pass

class Games(Screen):
	game = StringProperty('')

	def on_pre_enter(self):
		self.ids.btnstack.clear_widgets()
		id = 0
		for game in SoundBoard:
			btn = GameButton()
			btn.text = game[0]
			btn.id = str(id)
			self.ids.btnstack.add_widget(btn)
			id += 1

cat = Builder.load_file('cat.kv')

sm = ScreenManager()
sm.add_widget(MainMenu(name='MainMenu'))
sm.add_widget(Games(name='Games'))
sm.add_widget(Sounds(name='Sounds'))
sm.add_widget(AdvSounds(name='AdvSounds'))

cat.add_widget(sm)

class CATApp(App):

	def build(self):
		return cat

	def go_screen(self, screen, dir):
		if dir == 'None':
			sm.transition = NoTransition()
		else:
			sm.transition = SlideTransition()
			sm.transition.direction = dir
		sm.current = screen

	def set_selected_game(self, gamename):
		sm.screens[2].game = gamename

	def play_sound(self, soundname):
		print soundname

if __name__ == '__main__':
	CATApp().run()
