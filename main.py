import numpy as np
from data import get_data

def pattern_solution(arr):
    arr_len = len(arr)
    edge_dict = {}
    min_val = np.min(arr)

    min_pos = np.where(arr == min_val)[0][0]
    print(f'Min Pos: {min_pos}, val: {arr[min_pos]}')
    edge_dict['Min'] = [min_pos, arr[min_pos]]
    
    # top pos
    top_edge_pos = -1
    for i in range(min_pos, -1, -1):
        if arr[i] < 100:
            pass
        else:
            if i!=0:
                if arr[i-1] - arr[i] >= 10:
                    pass
                else:
                    top_edge_pos = i
                    break
            else:
                top_edge_pos = 0
    edge_dict['Top'] = [top_edge_pos, arr[top_edge_pos]]
    print(f'Top Pos: {top_edge_pos}, val: {arr[top_edge_pos]}')
    
    # first peak
    peak_dict = {}
    cur_val = 0
    slop = 1
    peak_cnt = 0
    for i in range(min_pos, arr_len):
        if peak_cnt == 4:
            break
        else:
            if slop == 1:
                if i != arr_len-1:
                    if arr[i+1] >= arr[i]:
                        pass
                    else:
                        if peak_cnt == 0:
                            if arr[i] < 200:
                                pass
                            else:
                                peak_dict['first_peak'] = [i, arr[i]]
                                slop = -1
                                peak_cnt += 1
                        elif peak_cnt == 2:
                            if arr[i] < 200:
                                pass
                            else:
                                peak_dict['second_peak'] = [i, arr[i]]
                                slop = -1
                                peak_cnt += 1
            else:
                if i != arr_len-1:
                    if arr[i+1] <= arr[i]:
                        pass
                    else:
                        if peak_cnt == 1:
                            if arr[i] > 200:
                                pass
                            else:
                                peak_dict['first_valley'] = [i, arr[i]]
                                slop = 1
                                peak_cnt += 1
                        elif peak_cnt == 3:
                            if arr[i] > 200:
                                pass
                            else:
                                peak_dict['second_valley'] = [i, arr[i]]
                                slop = 1
                                peak_cnt += 1
                        
        
            
    print(peak_dict)
    edge_dict['peak'] = peak_dict
    print(edge_dict)

test_a, test_b = get_data()

pattern_solution(test_a)
pattern_solution(test_b)