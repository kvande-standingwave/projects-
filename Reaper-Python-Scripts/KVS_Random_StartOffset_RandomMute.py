from random import uniform


""" Aaron - this is a simple script that will choose a random offset of the selected items. The media item stays in place but the position
of the waveform changes. Throw any audio file into a track and run the script and you'll see the media item stay in it's location on the 
timeline - but the waveform will jump around. the random_startoffset function works but we need to take into account the length of the SOURCE
file - not the length of the item which i have here. A media item container can be longer than the actual source file itself which can cause 
some complications

The second function - random_mute - should be very simple and I can't get it to work. What I'd like it to do is - count how many items there
and then mute a percentage of the total items every time.

This script will yield a ton of different variations. Let's say I stack 8 audio files of different forest ambiences on top of each other - 
each one being 5 minutes long. When you play them back - they all start at the beginning of the file. The random offset will provide variation
by starting the file at different locations. So once you run random_startoffset, file 1 will start at 1:20, file 2 will start at 4:18, etc.

Then the idea is the random_mute function will mute a couple of these files to thin out the mix and provide different variations. So when i run
the script Files 2 and 4 will be muted, and then when i run it again Files 1 and 7 will be muted. 

Does that make sense? Anyways - would love for us to work on this to ease back into cranking out some sweet scripts!


"""
def log(string):
    RPR_ShowConsoleMsg('{}{}'.format(string,'\n'))

def random_startoffset(items):
	selected_item = RPR_GetSelectedMediaItem(0, items)
	item_length = RPR_GetMediaItemInfo_Value(selected_item, 'D_LENGTH')
	active_take = RPR_GetActiveTake(selected_item)
	random_start_offset = uniform(0, item_length)
	new_offset = RPR_SetMediaItemTakeInfo_Value (active_take, 'D_STARTOFFS', random_start_offset)
	RPR_UpdateArrange()	

def random_mute(items):
	selected_item = RPR_GetSelectedMediaItem(0, items)
	active_take = RPR_GetActiveTake(selected_item)
	RPR_SetMediaItemTakeInfo_Value (active_take, 'B_MUTE', 1.0)
	RPR_UpdateArrange()	



for i in range(RPR_CountSelectedMediaItems(0)):
	random_startoffset(i)
	random_mute(i)
# 	#log('New Offset Value: {}' .format(str(random_start_offset)))


# item = RPR_GetSelectedMediaItem(0, 0)
# RPR_SetMediaItemTakeInfo_Value(item, 'B_MUTE', False)
# RPR_UpdateArrange()