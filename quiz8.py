def booleanF(i):
    wtsb = []
    for a in i:
        prediction = ( (a[1] or (not a[3])) and ((not a[1]) or a[2]) )
        if (prediction == False):
            wtsb.append(0)
        else: 
            wtsb.append(1)
    return wtsb

def doPrediction(w, i):
    wta = []
    for a in range(len(i)):
        prediction = ( (w[0]*i[a][0]) + (w[1]*i[a][1]) + (w[2]*i[a][2]) + (w[3]*i[a][3]) )
        if (prediction <= 0):
            wta.append(0)
        else:
            wta.append(1)
    print(wta)
    return wta 

        

def train(w, i, wta, wtsb):
    #still_wrong = True
    #while (still_wrong):
    for a in range(len(i)):
        if (wta[a] != wtsb[a]):
            print(w)
            print(i[a])
            #print (str(wta[a]) + " " + str(wtsb[a]))
            w0 = w[0] - 0.1*(wta[a] - wtsb[a]) * i[a][0]
            w1 = w[1] - 0.1*(wta[a] - wtsb[a]) * i[a][1]
            w2 = w[2] - 0.1*(wta[a] - wtsb[a]) * i[a][2]
            w3 = w[3] - 0.1*(wta[a] - wtsb[a]) * i[a][3]
            w = [w0, w1, w2, w3]
            wta = doPrediction(w, i)
    #    if (wta == wtsb):
     #       still_wrong = False
    print(w)
    return w

if __name__=='__main__':
    inputs = [[-1,0,0,0],[-1,0,0,1],[-1,0,1,0],[-1,0,1,1],[-1,1,0,0],[-1,1,0,1],[-1,1,1,0],[-1,1,1,1]]
    weights = [0.1, -0.15, -0.1, 0.05]
    
    what_they_are = doPrediction(weights, inputs)
    what_they_should_b = booleanF(inputs)
    weights = train(weights, inputs, what_they_are, what_they_should_b)
    print()
    print(what_they_should_b)
    doPrediction(weights, inputs)