BASE_NAME = "GTR Tool Rack Stereo"
BUFFER_SIZE = 255

def main():
    log('\n')
    # Get the track name
    proj_index = 0
    track_index = 0
    track = RPR_GetTrack(proj_index, track_index)
    response = RPR_GetSetMediaTrackInfo_String(track, 'P_NAME', '', False)
    (succeeded, track, param_name, track_name, set_new_value) = response
    if not succeeded:
        log('Failed to get the name for the default track in the default project: {}'.format(response))
        return

    log('Current track name: {}'.format(track_name))

    current_preset_index = 1
    # Check if the track name already has the base name
    if track_name.startswith(BASE_NAME):
        # Get the current index and increment it
        track_name_parts = track_name.split('_')
        if len(track_name_parts) != 2:
            log('Track name does not match the expected format: {}'.format(track_name))
        else:
            current_preset_index = int(track_name_parts[1])
            log('Current preset index: {}'.format(current_preset_index))
            if current_preset_index < 1:
                log('Could not reliably parse the current preset index: {}'.format(current_preset_index))
                current_preset_index = 1
            else:
                current_preset_index += 1

    # Now set the name
    track_name = '{}_{}'.format(BASE_NAME, current_preset_index)
    log('New track name: {}'.format(track_name))
    response = RPR_GetSetMediaTrackInfo_String(track, 'P_NAME', track_name, True)
    (succeeded, track, param_name, track_name, set_new_value) = response
    if not succeeded:
        log('Failed to update the track name to the new name: {}'.format(response))
        return

    log('Success!')

def log(string):
    RPR_ShowConsoleMsg('{}{}'.format(string,'\n'))

if __name__ == "__main__":
    main()
