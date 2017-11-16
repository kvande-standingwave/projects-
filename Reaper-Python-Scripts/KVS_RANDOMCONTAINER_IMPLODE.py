# \\\\\\\\\\\\\\\\\\\ Implode selected items and adjust imploded item's length to length of longest take - color it, then zoom



"""
# TURN THIS INTO AVERAGE LENGTH 


#A list of the lengths of each element in a list:

lengths = [len(i) for i in my_list]


#For the average:

def averageLen(lst):
    lengths = [len(i) for i in lst]
    return 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths)) 


#If it's a list of lists:

lengths = [averageLen(i) for i in my_list]


# AND ADD RANDOMIZE PANS

"""



# --------- | variables, defined.


item_lengths = []

implode_items = 40543 # implodes selected items on same track

set_time_selection = 40290 # sets time selection to selected items

random_take_color = RPR_NamedCommandLookup('_SWS_TAKESRANDCOLS') # color all takes in an item to a random custom color

hor_zoom_to_time_selection = RPR_NamedCommandLookup('_SWS_TOGZOOMHORIZ_TSEL') # Horizontal Zoom to time selection or selected items


# --------- script, start.



# get the item length from all selected items and put their length into a list while marking Loop Source = False

for i in range(RPR_CountSelectedMediaItems(0)): # Count the number of selected items

	current_item = RPR_GetSelectedMediaItem(0, i) # Get each item

	RPR_SetMediaItemInfo_Value(current_item, 'B_LOOPSRC', False) # set each items Loop Source to False

	current_item_length = RPR_GetMediaItemInfo_Value(current_item, 'D_LENGTH') # get each items length



	item_lengths.append(current_item_length) # --------- building list.




# get the longest length in seconds from list

longest_length_seconds = max(item_lengths)

# get the list index of item that has the longest length

longest_length_index = item_lengths.index(max(item_lengths)) #no longer needed, used for debugging



# IMPLODE, ADJUST LENGTH, COLOR, ZOOM!

RPR_Main_OnCommand(implode_items, 0) # imploding

imploded_item = RPR_GetSelectedMediaItem(0, 0) # getting imploded item

RPR_SetMediaItemInfo_Value(imploded_item, 'D_LENGTH', longest_length_seconds) # setting imploded item to length of longest take

RPR_SetToggleCommandState(0, hor_zoom_to_time_selection, 0) # attempting to set this command to OFF - not sure if it works

#RPR_ShowConsoleMsg(hor_zoom_to_time_selection)


# --------- make it puurty.

RPR_Main_OnCommand(random_take_color, 0) # random color to each take in item
RPR_Main_OnCommand(set_time_selection, 0) # create time selection around imploded item
RPR_Main_OnCommand(hor_zoom_to_time_selection, 0) # horizontal zoom to time selected imploded item
RPR_UpdateArrange()








