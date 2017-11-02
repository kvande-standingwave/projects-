from random import uniform
from random import getrandbits


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
	RPR_SetMediaItemInfo_Value (selected_item, 'B_MUTE', bool(getrandbits(1)))
	RPR_UpdateArrange()	



for i in range(RPR_CountSelectedMediaItems(0)):
	random_startoffset(i)
	random_mute(i)
