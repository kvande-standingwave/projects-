import random

def main():
    log('Starting Shuffler')

    if RPR_CountSelectedTracks(0) == 0:
        log('Please select a track to run this script.')
        return

    track = RPR_GetSelectedTrack(0, 0)

    # Shuffle the FX
    fx_count = RPR_TrackFX_GetCount(track)
    fx_range = range(fx_count)
    for i in fx_range:
        select_first_fx_chain()
        for j in range(random.choice(fx_range)):
            move_selected_fx_down()

    log('Finished')

def log(string):
    RPR_ShowConsoleMsg('{}{}'.format(string,'\n'))

# _S&M_SELFX1
# ...
# _S&M_SELFX8

def select_first_fx_chain():
    RPR_Main_OnCommand(RPR_NamedCommandLookup('_S&M_SELFX1'), 0) # Select FX 1 for selected tracks

def move_selected_fx_down():
    RPR_Main_OnCommand(RPR_NamedCommandLookup('_S&M_MOVE_FX_DOWN'), 0)

def move_selected_fx_up():
    RPR_Main_OnCommand(RPR_NamedCommandLookup('_S&M_MOVE_FX_UP'), 0)

if __name__ == "__main__":
    main()