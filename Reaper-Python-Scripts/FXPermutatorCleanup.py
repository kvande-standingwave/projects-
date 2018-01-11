BASE_NAME = 'FXPerm'
BUFFER_SIZE = 255

PERMUTATOR_COLOR = 33521664

def main():
    # TODO: Show dialog to ask if we should do this or not
    log('\n')
    proj_index = 0

    # Clean up the tracks first
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

    # Clean up regions
    region_index = 0
    should_continue = True
    while should_continue:
        is_region = False
        pos = False
        region_end = 0
        name = ""
        mark_region_index_number = True
        color = 0
        response = RPR_EnumProjectMarkers3(proj_index, region_index, is_region, pos, region_end, name, mark_region_index_number, color)
        (return_val, returned_proj, returned_index, is_region, pos, region_end, name, mark_region_index_number, color) = response
        log(response)

        if return_val:
            if color == PERMUTATOR_COLOR:
                if RPR_DeleteProjectMarker(proj_index, mark_region_index_number, True) == False:
                    region_index += 1
            else:
                region_index += 1
        else:
            should_continue = False

        if region_index > 100:
            log('Safe guarded the while loop to delete regions')
            should_continue = False



    log('Success!')

def log(string):
    RPR_ShowConsoleMsg('{}{}'.format(string,'\n'))

if __name__ == "__main__":
    main()
