def generate_L1_prn(prn_num):
    prn_num = prn_num - 1   # Account for Python's zero indexing

    import numpy as np

    g1 = np.array([1,1,1,1,1,1,1,1,1,1])
    g2 = np.array([1,1,1,1,1,1,1,1,1,1])

    g1_feedback = np.array([0,0,1,0,0,0,0,0,0,1])
    g2_feedback = np.array([0,1,1,0,0,1,0,1,1,1])

    phs_sel = np.zeros((32, 2), dtype=int)

    phs_sel[0][:] = [2,6]
    phs_sel[1][:] = [3,7]
    phs_sel[2][:] = [4,8]
    phs_sel[3][:] = [5,9]
    phs_sel[4][:] = [1,9]
    phs_sel[5][:] = [2,10]
    phs_sel[6][:] = [1,8]
    phs_sel[7][:] = [2,9]
    phs_sel[8][:] = [3,10]
    phs_sel[9][:] = [2,3]
    phs_sel[10][:] = [3,4]
    phs_sel[11][:] = [5,6]
    phs_sel[12][:] = [6,7]
    phs_sel[13][:] = [7,8]
    phs_sel[14][:] = [8,9]
    phs_sel[15][:] = [9,10]
    phs_sel[16][:] = [1,4]
    phs_sel[17][:] = [2,5]
    phs_sel[18][:] = [3,6]
    phs_sel[19][:] = [4,7]
    phs_sel[20][:] = [5,8]
    phs_sel[21][:] = [6,9]
    phs_sel[22][:] = [1,3]
    phs_sel[23][:] = [4,6]
    phs_sel[24][:] = [5,7]
    phs_sel[25][:] = [6,8]
    phs_sel[26][:] = [7,9]
    phs_sel[27][:] = [8,10]
    phs_sel[28][:] = [1,6]
    phs_sel[29][:] = [2,7]
    phs_sel[30][:] = [3,8]
    phs_sel[31][:] = [4,9]

    phs_sel = phs_sel - 1   # Account for Python's zero indexing

    # Hardcoding the phase selector
    phs_sel_logic = np.array([0,0,0,0,0,0,0,0,0,0])
    print(phs_sel_logic)

    phs_sel_logic[phs_sel[prn_num]] = 1
    #phs_sel_logic[phs_sel[1]] = 1

    num_chips = 1023
    prn = np.empty(num_chips)

    # Advance g2 ahead of g1



    for ii in range(num_chips):
        phs_sel_out = np.bitwise_and(g2, phs_sel_logic)
        phs_sel_out = np.sum(phs_sel_out)
        phs_sel_out = np.mod(phs_sel_out, 2)
        prn[ii] = np.bitwise_xor(phs_sel_out, g1[9])

        g1_fb_val = np.bitwise_and(g1, g1_feedback)
        g1_fb_val = np.sum(g1_fb_val)
        g1_fb_val = np.mod(g1_fb_val, 2)
        g1 = np.roll(g1, 1)
        g1[0] = g1_fb_val
        

        g2_fb_val = np.bitwise_and(g2, g2_feedback)
        g2_fb_val = np.sum(g2_fb_val)
        g2_fb_val = np.mod(g2_fb_val, 2)
        g2 = np.roll(g2, 1)
        g2[0] = g2_fb_val

    return prn


