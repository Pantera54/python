import numpy as np
def get_det(m):
    if len(m) ==2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        D = 0
        for i in range(len(m)):
            M = m[0,i]
            new_m = []
            for j in range(len(m)):
                for k in range(len(m)):
                    if(j !=0 and k !=i):
                        new_m.append(m[j, k])
            new_m = np.array(new_m).reshape((len(m) - 1, len(m) - 1))
            if (i + 1) % 2 == 0:
                D += M * get_det(new_m)
            else:
                D-= M * get_det(new_m)
            return D
def cramer(A,b):
                    D = get_det(A)
                    if (D == 0):
                        print('Ошибка, не крамер это, епта!')
                    else:
                            dets =[]
                            for i in range(len(A)):
                                copied_A = np.array(A)
                                copied_A[:,i] = b
                                dets.append(get_det(copied_A))
                                x = []
                                for curr_det in dets:
                                    x.append(float(curr_det) / D)
                                    return x
                 
