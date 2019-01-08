# gamedomizer.py
# Author : Amanda Ciampa
# Usage  : Selects a random game within Steam library or emulated games
import random
import os

class ROM:
	def __init__(self, rom_dir, rom_core, rom_ext):
		self.rom_list = {}
		self.rom_dir = rom_dir
		self.rom_core = rom_core
		#self.rom_ext = rom_ext
		self.rom_ext = {}

	def random_number(self):	# Returns a random number from the beginning to end of the rom_list dictionary
		return random.randint(0, (len(self.rom_list) - 1))

	def set_roms(self):		# Adds all game titles within that system's ROM folder to rom_list dictionary
		self.rom_list = os.listdir(self.rom_dir)

	def get_rom(self, num):	# Returns a game title using the passed in int variable
		return self.rom_list[num]

	def play_rom(self, num):
		os.system("D:\\EMULATORS\\RetroArch\\retroarch.exe -fullscreen -L" + self.rom_core + " \"" + 
			self.rom_dir + self.get_rom(num) + "\"")

	def play_iso(self, num):
		os.system("D:\\EMULATORS\\Dolphin\\Dolphin.exe -b" + " \"" + self.rom_dir + self.get_rom(num) + "\"")

	#def play_steam(self, num):
		#def playgame(game):
		#    webbrowser.open('steam://rungameid/{}'.format(game['appid']))
		#pass

#    _____ _______________       _____________   _____________ _________
#   / ___// ____/ ____/   |     / ____/ ____/ | / / ____/ ___//  _/ ___/
#   \__ \/ __/ / / __/ /| |    / / __/ __/ /  |/ / __/  \__ \ / / \__ \
#  ___/ / /___/ /_/ / ___ |   / /_/ / /___/ /|  / /___ ___/ // / ___/ /
# /____/_____/\____/_/  |_|   \____/_____/_/ |_/_____//____/___//____/
genesis_games = 'D:\\GAMES\\Genesis\\'
genesis_core = "D:\\EMULATORS\\RetroArch\\cores\\genesis_plus_gx_libretro.dll"
genesis_extension = '.md'

genesis = ROM(genesis_games, genesis_core, genesis_extension)
genesis.set_roms()

#genesis.play_rom(genesis.random_number())
# ---------------------------------------------------------------------------------

#     _____ __  ______  __________     _   _______   _______________   ______  ____
#   / ___// / / / __ \/ ____/ __ \   / | / /  _/ | / /_  __/ ____/ | / / __ \/ __ \
#   \__ \/ / / / /_/ / __/ / /_/ /  /  |/ // //  |/ / / / / __/ /  |/ / / / / / / /
#  ___/ / /_/ / ____/ /___/ _, _/  / /|  // // /|  / / / / /___/ /|  / /_/ / /_/ /
# /____/\____/_/   /_____/_/ |_|  /_/ |_/___/_/ |_/ /_/ /_____/_/ |_/_____/\____/
snes_games = 'D:\\GAMES\\SNES\\'
snes_core = "D:\\EMULATORS\\RetroArch\\cores\\bsnes_mercury_balanced_libretro.dll"
snes_extension = '.sfc'

snes = ROM(snes_games, snes_core, snes_extension)
snes.set_roms()
# snes.play_rom(snes.random_number())
# ---------------------------------------------------------------------------------

#     _   _______   _______________   ______  ____     _____ __ __
#    / | / /  _/ | / /_  __/ ____/ | / / __ \/ __ \   / ___// // /
#   /  |/ // //  |/ / / / / __/ /  |/ / / / / / / /  / __ \/ // /_
#  / /|  // // /|  / / / / /___/ /|  / /_/ / /_/ /  / /_/ /__  __/
# /_/ |_/___/_/ |_/ /_/ /_____/_/ |_/_____/\____/   \____/  /_/
n64_games = 'D:\\GAMES\\N64\\'
n64_core = "D:\\EMULATORS\\RetroArch\\cores\\mupen64plus_libretro.dll"
n64_extension = '.z64'

n64 = ROM(n64_games, n64_core, n64_extension)
n64.set_roms()
#n64.play_rom(n64.random_number())
# ---------------------------------------------------------------------------------

#     ____  __    _____  ________________  ______________  _   __
#    / __ \/ /   /   \ \/ / ___/_  __/   |/_  __/  _/ __ \/ | / /
#   / /_/ / /   / /| |\  /\__ \ / / / /| | / /  / // / / /  |/ /
#  / ____/ /___/ ___ |/ /___/ // / / ___ |/ / _/ // /_/ / /|  /
# /_/   /_____/_/  |_/_//____//_/ /_/  |_/_/ /___/\____/_/ |_/
psx_games = 'D:\\GAMES\\Playstation\\'
psx_core = "D:\\EMULATORS\\RetroArch\\cores\\pcsx_rearmed_libretro.dll"
psx_extension = '.PBP'

psx = ROM(psx_games, psx_core, psx_extension)
psx.set_roms()
#psx.play_rom(psx.random_number())
# ---------------------------------------------------------------------------------

#    _________    __  _____________  ______  __   ___    ____ _    _____    _   __________________
#   / ____/   |  /  |/  / ____/ __ )/ __ \ \/ /  /   |  / __ \ |  / /   |  / | / / ____/ ____/ __ \
#  / / __/ /| | / /|_/ / __/ / __  / / / /\  /  / /| | / / / / | / / /| | /  |/ / /   / __/ / / / /
# / /_/ / ___ |/ /  / / /___/ /_/ / /_/ / / /  / ___ |/ /_/ /| |/ / ___ |/ /|  / /___/ /___/ /_/ /
# \____/_/  |_/_/  /_/_____/_____/\____/ /_/  /_/  |_/_____/ |___/_/  |_/_/ |_/\____/_____/_____/
gba_games = 'D:\\GAMES\\GBA\\'
gba_core = "D:\\EMULATORS\\RetroArch\\cores\\mgba_libretro.dll"
gba_extension = '.gba'

gba = ROM(gba_games, gba_core, gba_extension)
gba.set_roms()
#gba.play_rom(gba.random_number())
# ---------------------------------------------------------------------------------

#    _________    __  _________________  ______  ______
#   / ____/   |  /  |/  / ____/ ____/ / / / __ )/ ____/
#  / / __/ /| | / /|_/ / __/ / /   / / / / __  / __/
# / /_/ / ___ |/ /  / / /___/ /___/ /_/ / /_/ / /___
# \____/_/  |_/_/  /_/_____/\____/\____/_____/_____/
gc_games = 'D:\\GAMES\\Gamecube\\'
gc_core = ""
gc_extension = '.iso'
gc2_extension = '.gcm'

gc = ROM(gc_games, gc_core, gc_extension)
gc2 = ROM(gc_games, gc_core, gc2_extension)
gc.set_roms()
gc2.set_roms()
#gc.play_iso(gc.random_number())
# ---------------------------------------------------------------------------------

#  _       __________
# | |     / /  _/  _/
# | | /| / // / / /
# | |/ |/ // /_/ /
# |__/|__/___/___/
wii_games = 'D:\\GAMES\\Wii\\'
wii_core = ""
wii_extension = '.iso'

wii = ROM(wii_games, wii_core, wii_extension)
wii.set_roms()
#wii.play_iso(wii.random_number())



system_hash = {0:genesis, 1:snes, 2:n64, 3:psx, 4:gba, 5:gc, 6:gc2, 7:wii}

randint = random.randint(0, 7)

if randint != 5 and randint != 6 and randint !=7:
	system_hash[randint].play_rom(system_hash[randint].random_number())
else:
	system_hash[randint].play_iso(system_hash[randint].random_number())