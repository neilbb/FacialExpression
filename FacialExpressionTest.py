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



happy = np.array([3.4469,2.9125,0.2438])
sad = np.array([-2.3793,-1.3414,-1.8759])

fear = np.array([-2.4077,-0.7577,-0.6808])
disgust = np.array([-2.5706,0.2676,0.4265])

surprise = np.array([1.4796,1.3151,2.3139])
anger = np.array([-2.0267,1.0667,1.7967])



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



if __name__ == '__main__':
	main(appreciative)
	main(evil)





