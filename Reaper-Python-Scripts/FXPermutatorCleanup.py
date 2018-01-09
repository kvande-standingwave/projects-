BASE_NAME = 'FXPerm'
BUFFER_SIZE = 255

def main():
    log('\n')
    proj_index = 0
    track_count = RPR_GetNumTracks()
    track_index = 0
    while track_index < track_count:
        log('Current index:{} Track count:{}'.format(track_index, track_count))
        track = RPR_GetTrack(proj_index, track_index)
        response = RPR_GetSetMediaTrackInfo_String(track, 'P_NAME', '', False)
        (succeeded, track, param_name, track_name, set_new_value) = response
        if not succeeded:
            log('Failed to get the name for track {}/{}: {}'.format(track_index, track_count, response))
            return

        log('Current track name: {}'.format(track_name))

        # Check if the track name already has the base name
        if track_name.startswith(BASE_NAME):
            RPR_DeleteTrack(track)
            log('Deleted track!')
            track_count = RPR_GetNumTracks()
        else:
            track_index += 1

    log('Success!')

def log(string):
    RPR_ShowConsoleMsg('{}{}'.format(string,'\n'))

if __name__ == "__main__":
    main()
