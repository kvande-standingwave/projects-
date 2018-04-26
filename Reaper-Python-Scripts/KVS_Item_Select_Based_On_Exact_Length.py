from Functions import *

"""

Notes:

Need to figure out how to make Dialog Box bigger

Need to understand what size_of_user_input means

Why does sys.getsizeof always return 24?

What does named argument mean? Why can't i put *default_value?  Can I make this box show up with no value in Box?

"""
# Constants for pop-up dialogs
TITLE = 'Find Item Length Between Two Values'
DEFAULT_INPUT_SIZE = 255





#------------------------script start

#Set Up Dialog Box

# caption = "Deselect Items Less Than (sec)"
# default_value = '0' 
# size_of_user_input = 1024
# user_input = RPR_GetUserInputs('Deselect Items Less Entered Value', 1 , caption, default_value, size_of_user_input)








# User entered value in seconds

# user_seconds = float(user_input[4])
# log(user_seconds)


#byte_size = sys.getsizeof(user_seconds)




def main():

	(greater_than, less_than) = get_item_length_between_values()

	float(greater_than)
	float(less_than)
	log(greater_than)
	log(less_than)

	shouldContinue = True
	while shouldContinue == True:
		shouldContinue = False
		for i in range(RPR_CountSelectedMediaItems(0)):
			current_item = RPR_GetSelectedMediaItem(0, i)
			current_item_length = RPR_GetMediaItemInfo_Value(current_item, 'D_LENGTH')
			log(current_item_length)
			if greater_than >= current_item_length and less_than < current_item_length:
			#if greater_than < current_item_length < less_than:
			#if current_item_length == greater_than:
				RPR_SetMediaItemInfo_Value(current_item, 'B_UISEL', True)
				log("YES!") 
				shouldContinue = True 
			else:
				RPR_SetMediaItemInfo_Value(current_item, 'B_UISEL', False) 
				log("FACK") 
				#break

	



def get_item_length_between_values():
    num_inputs = 2
    captions_csv = 'Item Length Greater or Equal To:,But Less Than:'
    default_value = '0,0'
    user_inputs = RPR_GetUserInputs(TITLE, num_inputs, captions_csv, default_value, DEFAULT_INPUT_SIZE)

    if user_inputs[0] is 0:
        log('User hit cancel.')
        return (0, 0)

# Assumption: there are 2 values
    user_input_values = user_inputs[4].split(',')
    return (user_input_values[0], user_input_values[1])



if __name__ == "__main__":
    main()
    RPR_UpdateArrange()

# 40118 = Move selected Items down one track
#RPR_Main_OnCommand(40118, 0)




#RPR_ShowConsoleMsg("Size of user entered value in bytes is: " + str(byte_size))
