
PIECE_COUNT = 128 # Edit this value. 128 for default S-Layer(Reaktor) sample maps - 512 for 4 full sample maps for Whoosh

RPR_ClearConsole()


if (RPR_CountSelectedMediaItems(0)) == 0:
	RPR_ShowConsoleMsg("There are zero items selected")

else:

	RPR_ShowConsoleMsg("There are " + str(RPR_CountSelectedMediaItems(0)) + " items selected" '\n\n') 

	RPR_ShowConsoleMsg("Divided by 2: " + str(float(RPR_CountSelectedMediaItems(0) / 2)) + " pieces" '\n\n') 

	RPR_ShowConsoleMsg("Divided by 4: " + str(float(RPR_CountSelectedMediaItems(0) / 4)) + " pieces" '\n\n')	

	RPR_ShowConsoleMsg("Subtracted by 128: " + str(float(RPR_CountSelectedMediaItems(0) - PIECE_COUNT)) + " pieces" '\n\n')  

	RPR_ShowConsoleMsg("Negative number = # of under 128, Positive Number = # of pieces over 128")  








