import random

# Constants for pop-up dialogs
TITLE = 'FX Permutator'
DEFAULT_INPUT_SIZE = 255

DEFAULT_PROJECT = 0

NEW_TRACK_TIME_BUFFER = 10 # seconds
MEDIA_ITEM_SEPARATION = 5  # seconds
REGION_TAIL_BUFFER    = 20 # seconds

PRESET_SELECT_FROM_ALL = 0
PRESET_SELECT_FROM_LIST = 1

BASE_NAME = 'FXPerm'
NEW_TRACK_COUNT = 0

LIST_OF_FX = [
    {
        'name': 'Absynth 5 FX',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    # {
    #     'name': 'Hadron',
    #     'separation_count': -1,
    #     'presets': [],
    #     'preset_selection_mode': PRESET_SELECT_FROM_ALL
    # },
    {
        'name': 'Doppler Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Fracture',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Driver',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': ['INIT - Driver'],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Acon Digital Multiply',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    # {
    #     'name': 'EchoBoy',
    #  #   'short_name': '',
    #     'separation_count': -1,
    #     'presets': [],
    #     'presets_exclusion': [],
    #     'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    # },
    {
        'name': 'Doubler4 Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Hysteresis',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    # {
    #     'name': 'Crystallizer',
    #  #   'short_name': '',
    #     'separation_count': -1,
    #     'presets': [],
    #     'presets_exclusion': [],
    #     'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    # },
    {
        'name': 'UltraPitch 3 Voices Mono/Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'BC Chorus 4 (Stereo)',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
 
    {
        'name': 'MondoMod Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Enigma Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'GTR Tool Rack Stereo FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'MetaFlanger Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'ValhallaRoom',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'ValhallaShimmer',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'ValhallaSpaceModulator',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-A_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-D_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-F_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-G_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-P_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-Q_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-S_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Uhbik-T_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Guitar Rig 5',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Morphoder Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'C4 Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'H-Delay Stereo',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'PSP 608 MultiDelay',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Reaktor 6_FXPERM',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Krush',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Spaceship Delay',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Regressif',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'Camel Phat 3',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },
    {
        'name': 'CamelSpace',
     #   'short_name': '',
        'separation_count': -1,
        'presets': [],
        'presets_exclusion': [],
        'preset_selection_mode': PRESET_SELECT_FROM_ALL, # 0 = All, 1 = From List
    },







]

def main():
    log('~~Starting FXPermutator~~')

    (plugin_count, iteration_count) = get_plugin_and_permutation_counts()
    # plugin_count = 1
    # iteration_count = 20
    plugin_count = int(plugin_count)
    iteration_count = int(iteration_count)
    if plugin_count is 0 or iteration_count is 0:
        log('Plugin Count ({}) and Iteration Count ({}) must both be greater than zero.'.format(plugin_count, iteration_count))
        return

    start_track = get_starting_track() # TODO: Validate the start track
    RPR_Undo_BeginBlock()
    new_track = create_new_track()     # TODO: Validate the new track
    for i in range(iteration_count):
        if i > 0:
            start_track = new_track
            RPR_Undo_BeginBlock()
            new_track = create_new_track() # TODO: Validate the new track
        set_track_fx_enabled(new_track, False)

        copy_and_paste_media_items(start_track, new_track)
        create_separation_between_media_items(new_track)
        # set_color_for_media_items(new_track)

        list_of_added_fx = add_multiple_fx_to_track(new_track, plugin_count)
        region_name = '{}_{}'.format(BASE_NAME, list_of_added_fx)
        create_region_around_media_items_on_track(new_track, region_name)
        RPR_Undo_EndBlock('Create {}'.format(region_name), 0)

    RPR_UpdateArrange() # Updates the UI

    log('~~Finsihed Permutating')

def get_plugin_and_permutation_counts():
    num_inputs = 2
    captions_csv = 'Number of Plugins per FX Chain:,Number of FX Chain iterations:'
    default_value = '3,2'
    user_inputs = RPR_GetUserInputs(TITLE, num_inputs, captions_csv, default_value, DEFAULT_INPUT_SIZE)

    if user_inputs[0] is 0:
        log('User hit cancel.')
        return (0, 0)

    # Assumption: there are 2 values
    user_input_values = user_inputs[4].split(',')
    return (user_input_values[0], user_input_values[1])

def get_starting_track():
    # Assumption: There is only one track
    original_track_index = 0
    original_track = RPR_GetTrack(DEFAULT_PROJECT, original_track_index)
    # Assumption: There is media on the track already
    # media_items_count = RPR_CountTrackMediaItems(original_track)
    return original_track

def create_new_track():
    # Create our new track
    #  Assumption: Creating a new track always succeeds
    RPR_Main_OnCommand(40702, 0) # Insert the new track at the end of the track list
    new_track_index = RPR_GetNumTracks() - 1
    new_track = RPR_GetTrack(DEFAULT_PROJECT, new_track_index)

    # Name the track with our prefix
    global NEW_TRACK_COUNT
    NEW_TRACK_COUNT += 1
    track_name = '{}_{}'.format(BASE_NAME, NEW_TRACK_COUNT)
    log('New track name: {}'.format(track_name))
    response = RPR_GetSetMediaTrackInfo_String(new_track, 'P_NAME', track_name, True)
    (succeeded, track, param_name, track_name, set_new_value) = response
    if not succeeded:
        log('Failed to update the track name to the new name: {}'.format(response))

    return new_track

def toggle_track_fx_enabled(track):
    param = 'I_FXEN'
    previous_value = RPR_GetMediaTrackInfo_Value(track, param)
    results = RPR_SetMediaTrackInfo_Value(track, param, not previous_value)

def set_track_fx_enabled(track, value):
    param = 'I_FXEN'
    results = RPR_SetMediaTrackInfo_Value(track, param, value)

def copy_and_paste_media_items(source_track, dest_track):
    select_only_media_items_on_track(source_track)
    move_cursor_to_right_edge_of_selected()
    move_cursor(NEW_TRACK_TIME_BUFFER + REGION_TAIL_BUFFER)
    copy()
    select_only_track(dest_track)
    paste()

def create_separation_between_media_items(track):
    select_only_media_items_on_track(track)
    next_start_position = 0
    for i in range(RPR_CountSelectedMediaItems(DEFAULT_PROJECT)):
        media_item = RPR_GetSelectedMediaItem(DEFAULT_PROJECT, i)
        media_item_pos = RPR_GetMediaItemInfo_Value(media_item, 'D_POSITION')
        media_item_length = RPR_GetMediaItemInfo_Value(media_item, 'D_LENGTH')
        if next_start_position is 0:
            next_start_position = media_item_pos + media_item_length + MEDIA_ITEM_SEPARATION
        else:
            RPR_SetMediaItemPosition(media_item, next_start_position, True)
            media_item_pos = next_start_position
            next_start_position += media_item_length + MEDIA_ITEM_SEPARATION

# def set_color_for_media_items(track):
#     color_range = range(255)
#     select_only_media_items_on_track(track)
#     for i in range(RPR_CountSelectedMediaItems(DEFAULT_PROJECT)):
#         r = random.choice(color_range)
#         g = random.choice(color_range)
#         b = random.choice(color_range)
#         media_item = RPR_GetSelectedMediaItem(DEFAULT_PROJECT, i)
#         log('(r={},g={},b={})'.format(r, g, b))
#         color = RPR_ColorToNative(r,g,b)
#         log('color={}'.format(color))
#         color_hex = color | 0x100000
#         log('color_hex={}'.format(color_hex))
#         RPR_SetMediaItemInfo_Value(media_item, 'I_CUSTOMCOLOR', color_hex)

def add_multiple_fx_to_track(track, fx_count):
    already_added_fx = []
    fullname = ''
    for i in range(fx_count):
        # Pick a random FX
        new_fx = random.choice(LIST_OF_FX)
        while new_fx['name'] in already_added_fx:
            if len(already_added_fx) >= len(LIST_OF_FX):
                break
            new_fx = random.choice(LIST_OF_FX)

        # Add the FX to the track
        fx_index = add_fx_to_track(track, new_fx['name'])
        fx_name = new_fx['name'] if 'short_name' not in new_fx or len(new_fx['short_name']) is 0 else new_fx['short_name']
        already_added_fx.append(new_fx['name'])

        preset_name = set_fx_preset(track, new_fx, fx_index)

        # Add to the full name
        if len(fullname) > 0:
            fullname += '-'
        fullname += '{}_{}'.format(fx_name, preset_name)

    return fullname

def set_fx_preset(track, fx, fx_index):
    # Get the preset count
    preset_selection_mode = get_preset_selection_mode(fx)
    preset_count = 0
    if preset_selection_mode == PRESET_SELECT_FROM_ALL:
        response = RPR_TrackFX_GetPresetIndex(track, fx_index, 0)
        (current_preset_index, track, fx_index_returned, preset_count) = response
    elif preset_selection_mode == PRESET_SELECT_FROM_LIST:
        # if len(new_fx['presets']):
        #     preset_name = random.choice(new_fx['presets'])
        #     RPR_TrackFX_SetPreset(track, fx_index, preset_name)
        pass

    # Keep trying to set preset until we have a valid selection
    if preset_count > 0:
        attempt_index = 0
        index_range = range(preset_count)
        log(index_range)
        preset_index_list = random.sample(index_range, len(index_range))
        log(preset_index_list)
        while attempt_index < len(preset_index_list):
            preset_index = preset_index_list[attempt_index]
            RPR_TrackFX_SetPresetByIndex(track, fx_index, preset_index)
            response = RPR_TrackFX_GetPreset(track, fx_index, '', 255)
            preset_name = response[3].strip()
            if len(preset_name) > 0 and preset_name != 'Default' and preset_name != 'disabled' and preset_name != 'Untitled Sound':
                return preset_name
            attempt_index += 1
    return ''

def get_preset_selection_mode(fx):
    if 'preset_selection_mode' not in fx:
        return PRESET_SELECT_FROM_ALL
    if fx['preset_selection_mode'] == PRESET_SELECT_FROM_ALL or fx['preset_selection_mode'] == PRESET_SELECT_FROM_LIST:
        return fx['preset_selection_mode']
    log('Warning: Encountered unknown preset selection mode "{}". Using "PRESET_SELECT_FROM_ALL" instead.'.format(fx['preset_selection_mode']))
    return  PRESET_SELECT_FROM_ALL

def add_fx_to_track(track, fxName):
    return RPR_TrackFX_AddByName(track, fxName, False, -1) # 4th arg is instantiate: -1 always add, 0 get existing, 1 only one

def select_only_media_items_on_track(track):
    for x in range(RPR_CountMediaItems(DEFAULT_PROJECT)):
        media_item = RPR_GetMediaItem(DEFAULT_PROJECT, x)
        RPR_SetMediaItemSelected(media_item, RPR_MediaItemDescendsFromTrack(media_item, track))

def create_region_around_media_items_on_track(track, name):
    select_only_media_items_on_track(track)
    set_time_selection_to_items()
    (start_time, end_time) = get_start_and_end_of_selected()
    end_time += REGION_TAIL_BUFFER
    RPR_AddProjectMarker(DEFAULT_PROJECT, True, start_time, end_time, name, -1)

def get_start_and_end_of_selected():
    lowest_start = 0
    highest_end = 0
    for i in range(RPR_CountSelectedMediaItems(DEFAULT_PROJECT)):
        media_item = RPR_GetSelectedMediaItem(DEFAULT_PROJECT, i)

        # Compare start times
        start_time = RPR_GetMediaItemInfo_Value(media_item, 'D_POSITION')
        if lowest_start is 0 or start_time < lowest_start:
            lowest_start = start_time

        # Compare end times
        end_time = start_time + RPR_GetMediaItemInfo_Value(media_item, 'D_LENGTH')
        if highest_end is 0 or end_time > highest_end:
            highest_end = end_time

    return (lowest_start, highest_end)

def move_cursor_to_right_edge_of_selected():
    set_time_selection_to_items()
    go_to_end_of_time_selection()

def select_only_track(track):
    for x in range(0, RPR_GetNumTracks()):
        each_track = RPR_GetTrack(DEFAULT_PROJECT, x)
        RPR_SetTrackSelected(each_track, each_track == track)

def copy():
    RPR_Main_OnCommand(40698, 0) # Insert the new track at the end of the track list

def paste():
    RPR_Main_OnCommand(40058, 0) # Insert the new track at the end of the track list

def set_time_selection_to_items():
    RPR_Main_OnCommand(40290, 0) # Time selection: Set time selection to items

def go_to_end_of_time_selection():
    RPR_Main_OnCommand(40631, 0) # Go to end of time selection

def move_cursor(seconds_to_move):
    RPR_MoveEditCursor(seconds_to_move, False)

def log(string):
    RPR_ShowConsoleMsg('{}{}'.format(string,'\n'))


# def set_colors():
#     color_range = range(255)
#     for i in range(RPR_CountSelectedMediaItems(DEFAULT_PROJECT)):
#         media_item = RPR_GetSelectedMediaItem(DEFAULT_PROJECT, i)
#         r = 154#random.choice(color_range)
#         g = 223#random.choice(color_range)
#         b = 133#random.choice(color_range)
#         log('(r={},g={},b={})'.format(r, g, b))
#         color = RPR_ColorToNative(r,g,b)
#         log('color={}'.format(color))
#         color_hex = color | 0x100000
#         log('color_hex={},should_be={}'.format(color_hex, 26926981))
#         RPR_SetMediaItemInfo_Value(media_item, 'I_CUSTOMCOLOR', color_hex)
#
# def set_track_color(track):
#     log('\n\n')
#     # printed int 23859107
#     # hex color:  #6C0FA3
#     # rgb: (108, 15, 163)
#     rgb = RPR_ColorToNative(108, 15, 163)
#     log('color={}'.format(rgb))
#     color_hex = rgb | 0x100000
#     log('color_hex={},should_be={}'.format(color_hex, 23859107))
#     log('track color: {}'.format(RPR_GetTrackColor(track)))
# rgb(154, 223, 133), value=26926981

# Create Chain
# Create regions around items
# Name regions to chaininfo ({DATE}_{PLUGIN NAME AND PRESET IN APPLIED ORDER})
# Create new project for each permutation

if __name__ == "__main__":
    main()
