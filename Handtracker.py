#first import the necessary libraries
#import opencv 
#import mediapipe


#most of this is from the mediapipe and opencv documentation

import cv2
import mediapipe as mp

#initialize the mediapipe hands module

#right here we are going to be drawing the hand
#these are the landmark points from our hands
mp_drawing = mp.solutions.drawing_utils

#this is for basically styling the lines we dont need it but we are just customizning the lines
mp_drawing_styles = mp.solutions.drawing_styles

#now we need to track the hand in real time
mphands = mp.solutions.hands

#now we need to access our webcame
cap = cv2.VideoCapture(0)
hands = mphands.Hands()

#this while loop is for the entail logic
while True:
    #this is for reading the image from the webcam
    data, image = cap.read()
    #now we are going to be flipping the image so the camera is flippped yk what i mean (selfie view)
    #after we flip the image we are going to be converting the image to RGB
    image = cv2.cvtColor(cv2.flip(image,1), cv2.COLOR_BGR2RGB)
    #now we are going to printing the image
    results = hands.process(image)
    #now we need to find the landmarks on our hand
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        #here we are going to be checking if there are any landmark features on teh hand which will activate the for loop and then start drawing the lines
        for hand_landmarks in results.multi_hand_landmarks:
            #it will draw the line
            mp_drawing.draw_landmarks(
                #it will make the connections
                image, hand_landmarks, mphands.HAND_CONNECTIONS,)
    cv2.imshow('Hand Tracking', image)
    cv2.waitKey(1)

















