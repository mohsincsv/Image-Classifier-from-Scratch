#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:   Mohsin Iqbal
# DATE CREATED: 1-12-2022                     
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    
    # Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)

    pet_image = filename_list
    pet_name  = []
        
    for image in pet_image:
        
        image = image.lower()
        image = image.split('_')
        
        label = ""

        # Loops to check if word in pet name is only
        # alphabetic characters - if true append word
        # to pet_name separated by trailing space 
        for word in image:
            if word.isalpha():
                label += word + " "
               
        label = label[:-1]
        label.strip()
        pet_name.append(label)
    
    # Creates empty dictionary named results_dic
    results_dic = dict()
    
    # Determines number of items in dictionary
    items_in_dic = len(results_dic)
    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
    # a List that contains only one item - the pet image label
    if pet_image[0] != '.':
        for idx in range(0, len(pet_image), 1):
            if pet_image[idx] not in results_dic:
                 results_dic[pet_image[idx]] = [pet_name[idx]]
            else:
                 print("** Warning: Key=", pet_image[idx], 
                       "already exists in results_dic with value =", 
                       results_dic[pet_image[idx]])

    return results_dic
