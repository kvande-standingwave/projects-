
'''
0.1 Count Number of FX
0.2 Get Open FX - iterate through the FX Chain count - return True to FX that is open or floating - and then get the preset count on that index

1. Get total number of presets from an FX on a track
2. Iterate through total number of presets on preset name length:
	2a. If len is == 0 then don't add to list
	2b. If len is > 0 then append to list of preset names

3. Pick a random preset string name from list of eligible presets
4. Apply preset to FX




Select a Random Preset from a list of presets that is built only with presets that have strings for names - at least a length of 1 AND is not <disabled>

'''



# GLOBALS

first_fx_index = 0 # first plugin in FX chain

track = RPR_GetSelectedTrack(0,0) # get selected track

#num_of_fx = RPR_TrackFX_GetCount(track)

list_of_preset_names = []

#----------------------------------------------------------------------------------------------------------- function


def main():
	open_fx = get_open_fx()
	for i in open_fx:
		presets = get_preset_count(i)
	log(presets[2])

	for i in range(presets[0]):
		preset_string = RPR_TrackFX_GetPreset(track, open_fx, '', 512)
		log(preset_string[3])

		



def get_open_fx():
	list_of_open_fx = []
	fx_count = RPR_TrackFX_GetCount(track)
	log('Number of FX in Chain {}{}' .format (fx_count, '\n'))
	for i in range(fx_count):

		open_fx = RPR_TrackFX_GetOpen(track, i)
		fx_name = RPR_TrackFX_GetFXName(track, i, '', 512)
		if open_fx == True and len(list_of_open_fx) < 2:
			#log(str(i) + '\n')
			list_of_open_fx.append(i)
			log('FX index: {} ({}) was ++++++ to the list {}' .format(i, fx_name[3], '\n'))
			

		else:
			log('FX index: {} ({}) was NOT added to the list {}' .format(i, fx_name[3], '\n'))

	return list_of_open_fx
	#return open_fx		




def get_preset_count(open_fx):
	
	preset_count = RPR_TrackFX_GetPresetIndex(track, open_fx, 0) # track, fx, numberOfPresetsOut
	fx_name = RPR_TrackFX_GetFXName(track, open_fx, '', 512)
	log('{}  has {} presets {}' .format(fx_name[3],preset_count[3], '\n'))
	#(Boolean retval, MediaTrack track, Int fx, String presetname, Int presetname_sz) 
	#current_preset = RPR_TrackFX_GetPreset(track, open_fx, '', 512)
	#log('{} is the currently selected preset {}' .format(current_preset[3], '\n'))

	return preset_count[3], fx_name[3], open_fx





def log(string): # print
	RPR_ShowConsoleMsg(string)




#------------------------------------------------------------run----------------------------------------------


main()
log('\n\n')

