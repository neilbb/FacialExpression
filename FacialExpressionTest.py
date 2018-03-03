######################################################
# FacialExpressionTest.py
# Used for testing facial expressions
# Input: EPA vector
# Output: Emotions to apply + Value to assign
# Value can be used on the Demo Site
#
######################################################





import numpy as np
from numpy import interp
import pickle


with open('newemotionEPAset+.pickle', 'rb') as handle:
    emotion_data = pickle.load(handle)



happy = np.array([3.4469,2.9125,0.2438])
sad = np.array([-2.3793,-1.3414,-1.8759])

fear = np.array([-2.4077,-0.7577,-0.6808])
disgust = np.array([-2.5706,0.2676,0.4265])

surprise = np.array([1.4796,1.3151,2.3139])
anger = np.array([-2.0267,1.0667,1.7967])
'''

happy = np.array([3.4469,2.9125])
sad = np.array([-2.3793,-1.3414])

fear = np.array([-2.4077,-0.7577])
disgust = np.array([-2.5706,0.2676])

surprise = np.array([1.4796,1.3151])
anger = np.array([-2.0267,1.0667])
'''

evil = np.array([-3.1129,1.4194,0.2645])

bad = np.array([-3.3205,0.5103,1.3538])

appreciative = np.array([3.1824, 2.4227, -0.0721])



def main(emot):
    #first dimension
    happyDist = np.linalg.norm(emot-happy)
    sadDist = np.linalg.norm(emot-sad)

    #second dimension
    fearDist = np.linalg.norm(emot-fear)
    disgustDist = np.linalg.norm(emot-disgust)

    #third dimension
    surpriseDist = np.linalg.norm(emot-surprise)
    angerDist = np.linalg.norm(emot-anger)

    print("HappyDist: ", happyDist,"SadDist: ", sadDist)

    print("FearDist: ", fearDist,"DisgustDist: ", disgustDist)
 
    print("SurpriseDist: ",surpriseDist,"AngerDist: ",angerDist)


    #1 - interp(7,[0,13.8564064606],[0,1])
    if happyDist < sadDist:
        val = 1 - interp(happyDist,[0,10],[0,1])
        print("Happy: ", val)

    elif sadDist < happyDist:
        val = 1 - interp(sadDist,[0,10],[0,1])
        print("Sad: ", val)

    if fearDist < disgustDist:
        val = 1 - interp(fearDist,[0,10],[0,1])
        print("Fear: ", val)

    elif disgustDist < fearDist:
        val = 1 - interp(disgustDist,[0,10],[0,1])
        print("Disgust: ", val)

    if surpriseDist < angerDist:
        val = 1 - interp(surpriseDist,[0,10],[0,1])
        print("Surprise: ", val)

    elif angerDist < surpriseDist:
        val = 1 - interp(angerDist,[0,10],[0,1])
        print("Anger: ", val)

    print("Evaluation: ",emot[0])
    print("Potency: ",emot[1])
    print("Activity: ",emot[2])

if __name__ == '__main__':
   # main(appreciative)
    print(50*'*')
    #main(evil)

    for ind,(key,value) in enumerate(emotion_data.items()):
        if key == "repentant":
            print(ind+1,key,np.array(value))
            evalpot = np.array([value[0],value[1]])
            #print (evalpot)
            main(value)
            print(50*'*')


'''
14 shocked [-0.2529  0.8411  1.0177]
[-0.2529  0.8411]
HappyDist:  4.2401907975939
SadDist:  3.047110633042391
FearDist:  2.683155694327111
DisgustDist:  2.3876003727592274
SurpriseDist:  1.796171553610623
AngerDist:  1.7880888680376041
Sad:  0.6952889366957609
Disgust:  0.7612399627240772
Anger:  0.8211911131962396
Evaluation:  -0.2529
Potency:  0.8411
**************************************************


14 shocked [-0.2529  0.8411  1.0177]
HappyDist:  4.310236560793387
SadDist:  4.20211900949985
FearDist:  3.175567150919659
DisgustDist:  2.459705872660388
SurpriseDist:  2.2150319839677257
AngerDist:  1.9504109310604265
Sad:  0.5797880990500149
Disgust:  0.7540294127339612
Anger:  0.8049589068939573
Evaluation:  -0.2529
Potency:  0.8411
Activity:  1.0177

'''
