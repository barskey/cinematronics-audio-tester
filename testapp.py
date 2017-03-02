from os.path import dirname, join
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ListProperty
from kivy.uix.screenmanager import Screen

#// Armor Attack
AASounds = [
	[ 'Tank Enable',    'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Beep Enable',    'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Chopper Enable', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Tank Fire',      'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 7],
	[ 'Hi Explosion',   'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 6],
	[ 'Jeep Fire',      'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 5],
	[ 'Lo Explosion',   'ACT_PLS', 1, 'ST_AAS', 0x0001, 0x0001, 4],
	[ 'Tank Speed',     'ACT_SET', 0, 'ST_AAS', 0x000F, 0x0000, 0]
]

#// Rip Off
ROSounds = [
	[ 'Explosion',         'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 7],
	[ 'Laser',             'ACT_PLS', 4, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Torpedo',           'ACT_PLS', 3, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Background Speed',  'ACT_SET', 0, 'ST_ROS', 0x0007, 0x0000, 3],
	[ 'Background Enable', 'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 2],
	[ 'Beep',              'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 1],
	[ 'Motor',             'ACT_TGL', 0, 'ST_ROS', 0x0001, 0x0001, 0]
]

#// Solar Quest
SQSounds = [
	[ 'Loud Explosion', 'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  7],
	[ 'Soft Explosion', 'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  6],
	[ 'Thrust',         'ACT_TGL', 0, 'ST_SQ1', 0x0001, 0x0001,  5],
	[ 'Fire',           'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  4],
	[ 'Capture',        'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  3],
	[ 'Nuke',           'ACT_TGL', 0, 'ST_SQ1', 0x0001, 0x0000,  2],
	[ 'Photon',         'ACT_PLS', 1, 'ST_SQ1', 0x0001, 0x0001,  1],
	[ 'Music Enable',   'ACT_TGL', 0, 'ST_SQ2', 0x0001, 0x0000, 15],
	[ 'Music Volume',   'ACT_SET', 0, 'ST_SQ2', 0x0007, 0x0007, 12],
	[ 'Music Pitch',    'ACT_SET', 0, 'ST_SQ2', 0x0FFF, 0x0000,  0]
]

#// Space War
SWSounds = [
	[ 'Explosion',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 0],
	[ 'Fire',         'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0000, 1],
	[ 'Thrust 1',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Thrust 2',     'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Sound Enable', 'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 4]
]

#// Star Castle
SCSounds = [
	[ 'Loud Explosion',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 1],
	[ 'Soft Explosion',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Laser Enable',      'ACT_TGL', 0, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Fire Ball Enable',  'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 7],
	[ 'Shield Enable',     'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 6],
	[ 'Star Enable',       'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0000, 5],
	[ 'Thrust Enable',     'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 4],
	[ 'Background Enable', 'ACT_TGL', 0, 'ST_AAS', 0x0001, 0x0001, 3],
	[ 'Background Speed',  'ACT_SET', 0, 'ST_AAS', 0x0007, 0x0000, 0]
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
	[ 'Explosion', 'ACT_PLS', 0, 'ST_OUT', 0x0001, 0x0001, 2],
	[ 'Ping 1',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 3],
	[ 'Ping 2',    'ACT_PLS', 1, 'ST_OUT', 0x0001, 0x0001, 4],
	[ 'Hatch',     'ACT_PLS', 6, 'ST_OUT', 0x0001, 0x0001, 7]
];

#// Tailgunner
TGSounds = [
	[ 'Explosion',     'ACT_PLS',  0, 'ST_TGS', 0x0001, 0x0001, 0],
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

blue = [0.33, 0.5, 1, 1]
#'dkblue': [0.15, 0.33, 0.5, 1]

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')

class GameButton(Button):
	pass

class MainScreen(Screen):
	pass
	
class SoundsScreen(Screen):
	pass

	def on_enter(self):
		self.ids.btnstack.clear_widgets()
		id = 0
		for sound in SoundBoard[0][2]:
			btn = GameButton()
			btn.text = sound[0]
			btn.id = str(id)
			self.ids.btnstack.add_widget(btn)
			id += 1
	
	def play_sound(soundid):
		print soundid

class AdvSoundsScreen(Screen):
	pass

class GamesScreen(Screen):
	pass

	def on_enter(self):
		self.ids.btnstack.clear_widgets()
		id = 0
		for game in SoundBoard:
			btn = GameButton()
			btn.text = game[0]
			btn.id = str(id)
			self.ids.btnstack.add_widget(btn)
			id += 1

class MyScreen(Screen):
	#fullscreen = BooleanProperty(False)

	def add_widget(self, *args):
		if 'btnstack' in self.ids:
			return self.ids.btnstack.add_widget(*args)
		return super(MyScreen, self).add_widget(*args)
			
class CATApp(App):

	index = NumericProperty(-1)
	current_title = StringProperty()
	sourcecode = StringProperty()
	screen_names = ListProperty([])
	hierarchy = ListProperty([])

	def build(self):
		self.title = 'hello world'
		self.screens = {}
		self.available_screens = [
			'Main', 'Games', 'Sounds', 'AdvSounds'
		]
		self.screen_names = self.available_screens
		curdir = dirname(__file__)
		self.available_screens = [join(curdir, 'data', 'screens',
			'{}.kv'.format(fn)) for fn in self.available_screens]
		self.go_next_screen()

	def go_previous_screen(self):
		self.index = (self.index - 1) % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction='right')
		self.current_title = screen.name

	def go_next_screen(self):
		self.index = (self.index + 1) % len(self.available_screens)
		screen = self.load_screen(self.index)
		sm = self.root.ids.sm
		sm.switch_to(screen, direction='left')
		self.current_title = screen.name

	def go_screen(self, idx):
		self.index = idx
		self.root.ids.sm.switch_to(self.load_screen(idx), direction='left')

	def load_screen(self, index):
		if index in self.screens:
			return self.screens[index]
		screen = Builder.load_file(self.available_screens[index].lower())
		self.screens[index] = screen
		return screen

if __name__ == '__main__':
	CATApp().run()
