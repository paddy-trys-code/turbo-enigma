#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: paddy o'brien 
# DATE CREATED:april 7th, 2020                     
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#      def calculates_results_stats(results_dic):

def calculates_results_stats(results_dic):
    
    results_stats_dic=dict()
    results_stats_dic['n_dogs_img']=0
    results_stats_dic['n_match']=0
    results_stats_dic['n_correct_dogs']=0
    results_stats_dic['n_correct_notdogs']=0
    results_stats_dic['n_correct_breed']=0

    for key in results_dic:
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
            
        if sum(results_dic[key][2:]) == 3:
                results_stats_dic['n_correct_breed'] += 1
        
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        else:
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
                
        results_stats_dic['n_images'] = len(results_dic)


        results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                          results_stats_dic['n_dogs_img']) 

    #############################################################################
        #percent match statistic
        pct_crct_match = 100.0*(int(results_stats_dic['n_match'])/int(results_stats_dic['n_images']))

        results_stats_dic['pct_match'] = pct_crct_match

        #percentage for correctly labelling dogs 
        if results_stats_dic['n_dogs_img'] >0: 
            pct_crct_dogs = 100.0*(int(results_stats_dic['n_correct_dogs'])/int(results_stats_dic['n_dogs_img']))
            results_stats_dic['pct_correct_dogs'] = pct_crct_dogs
        else: 
            results_stats_dic['pct_correct_dogs'] = 0.0

        #percent for correctly labelling breeds
        if results_stats_dic['n_dogs_img'] >0:
            pct_crct_breed = 100.0*(int(results_stats_dic['n_correct_breed'])/int(results_stats_dic['n_dogs_img']))
            results_stats_dic['pct_correct_breed'] = pct_crct_breed
        else:
            results_stats_dic['pct_correct_breed'] = 0.0

        #percent for correctly labelling not-dogs
        if results_stats_dic['n_notdogs_img'] > 0:
            pct_correct_notdogs = (int(results_stats_dic['n_correct_notdogs']) /int(results_stats_dic['n_notdogs_img']))*100.0
            results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs
        else:
            results_stats_dic['pct_correct_notdogs'] = 0.0

        return results_stats_dic

