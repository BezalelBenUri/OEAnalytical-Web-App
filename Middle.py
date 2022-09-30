import math

import pandas as pd
import numpy as np
import plotly.express as px

from Backend import DataRepository as repo

from dash import dcc

class GraphBuilder:
    
    """Methods for building Graphs."""
    
    def __init__(self):
        
        """init

        Parameters
        ----------
        repo : DataRepository, optional
            Data source, by default DataRepository()
        """
        
        self.repo = repo
        
    
    def what_is_your_gender(data):
        
        data = pd.DataFrame(data)
        
        gender = data[['What is your gender?', 'Who are you interviewing?']].sort_values(
            by = ['What is your gender?'], ascending = False)
        gender_fig = px.pie(gender, names = 'What is your gender?')
        return  gender_fig
    
    
    def residents_duration(data):
        residents_duration = data[['How long have you been living in this community?', 'Who are you interviewing?']].sort_values(
            by = ['How long have you been living in this community?'], ascending = False)
        residents_duration = residents_duration.value_counts(normalize = True)
        residents_duration = residents_duration.mul(100).rename('Percent').reset_index()
        residents_duration['Percent'] = residents_duration['Percent'].round(decimals = 1)
        
        residents_duration_fig = px.bar(residents_duration,  x =  'How long have you been living in this community?' , y = 'Percent', text = 'Percent')
        return residents_duration_fig
    
    
    def occupation_n_income(data):
        occ_n_inc = data[["What is your occupation?", "What is your monthly income range?"]].value_counts(normalize = True)
        occ_n_inc = occ_n_inc.mul(100).rename('Percent').reset_index()
        occ_n_inc['Percent'] = occ_n_inc['Percent'].round(decimals = 1)

        occ_n_inc_fig = px.bar(occ_n_inc, x = occ_n_inc["What is your monthly income range?"], y = "Percent", barmode = 'group', 
                     color = occ_n_inc["What is your occupation?"], text = 'Percent')
        occ_n_inc_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return occ_n_inc_fig
    
    
    def jetty_use(data):
        jetty_use = data[['Do you use the Jetty?', 'Who are you interviewing?']].sort_values(
            by = ['Do you use the Jetty?'], ascending = False)
        jetty_use_fig = px.pie(jetty_use, names = 'Do you use the Jetty?')
        return jetty_use_fig
    
    
    def jetty_usage(data):
        jetty_usage = data["How often do you use the Jetty?"].value_counts(normalize = True)
        jetty_usage = jetty_usage.mul(100).rename('Percent').reset_index()
        jetty_usage['Percent'] = jetty_usage['Percent'].round(decimals = 1)
        jetty_usage = px.bar(jetty_usage , x = "index", y = 'Percent', text = 'Percent')
        jetty_usage.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return jetty_usage
    
    def mode_of_transportation(data):
        trans_mode = data[['What is your most preferred mode of transportation?', 'Who are you interviewing?']].sort_values(
            by = ['What is your most preferred mode of transportation?'], ascending = False)
        trans_mode_fig = px.pie(trans_mode, names = 'What is your most preferred mode of transportation?')
        return trans_mode_fig
    
    def jetty_inc(data):
        jetty_incen = data[['Which of the following will make you use the jetty frequently?', 'Who are you interviewing?']].sort_values(
            by = ['Which of the following will make you use the jetty frequently?'], ascending = False).value_counts(normalize = True)
        jetty_incen = jetty_incen.mul(100).rename('Percent').reset_index()
        jetty_incen['Percent'] = jetty_incen['Percent'].round(decimals = 1)
        jetty_incen_fig = px.bar(jetty_incen , x = "Which of the following will make you use the jetty frequently?", y = 'Percent', text = 'Percent')
        jetty_incen_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return jetty_incen_fig
    
    def jetty_impact(data):
        jetty_impact = data[['How has the Jetty impacted the neighbourhood?', 'Who are you interviewing?']].sort_values(
            by = ['How has the Jetty impacted the neighbourhood?'], ascending = False)
        jetty_impact_fig = px.pie(jetty_impact, names = 'How has the Jetty impacted the neighbourhood?')
        return jetty_impact_fig
    
    def impact_as(data):
        impact_fact = data[['Positive impacts such as', 'Who are you interviewing?']].sort_values(
            by = ['Positive impacts such as'], ascending = False).value_counts(normalize = True)
        impact_fact = impact_fact.mul(100).rename('Percent').reset_index()
        impact_fact['Percent'] = impact_fact['Percent'].round(decimals = 1)

        impact_fact_fig = px.bar(impact_fact , x = "Positive impacts such as", y = 'Percent', text = 'Percent')
        impact_fact_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return impact_fact_fig
    
    def improvement(data):
        improvement_fact = data[['Kindly suggest ways in which the jetty can be improved', 'Who are you interviewing?']].sort_values(
            by = ['Kindly suggest ways in which the jetty can be improved'], ascending = False).value_counts(normalize = True)
        improvement_fact = improvement_fact.mul(100).rename('Percent').reset_index()
        improvement_fact['Percent'] = improvement_fact['Percent'].round(decimals = 1)

        improvement_fact_fig = px.bar(residents_improvement_fact , x = "Kindly suggest ways in which the jetty can be improved", y = 'Percent', text = 'Percent')
        improvement_fact_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return improvement_fact_fig
    
    
    
    
    def residency(data):
        residency = data[['Are you a resident?', 'Who are you interviewing?']].sort_values(by = ['Are you a resident?'], ascending = False)
        residency_fig = px.pie(residency, names = 'Are you a resident?')
        return residency_fig
    
    def fare_view(data):
        view_tfare = data[['What is your view on the fare rates?', 'Who are you interviewing?']].sort_values(
            by = ['What is your view on the fare rates?'], ascending = False)
        view_tfare = view_tfare.value_counts(normalize = True)
        view_tfare = view_tfare.mul(100).rename('Percent').reset_index()
        view_tfare['Percent'] = view_tfare['Percent'].round(decimals = 1)
        
        view_tfare_fig = px.bar(view_tfare , x = "What is your view on the fare rates?", y = 'Percent', text = 'Percent')
        view_tfare_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return view_tfare_fig
    
    def problems(data):
        prob = data[['Have you ever experience any problem during the ride?', 'Who are you interviewing?']].sort_values(
            by = ['Have you ever experience any problem during the ride?'], ascending = False)
        prob = px.pie(prob, names = 'Have you ever experience any problem during the ride?')
        return prob
    
    def experience(data):
        problems_exp = data[['If yes, what kind of problem?', 'Who are you interviewing?']].sort_values(
            by = ['If yes, what kind of problem?'], ascending = False).value_counts(normalize = True)
        problems_exp = problems_exp.mul(100).rename('Percent').reset_index()
        problems_exp['Percent'] = problems_exp['Percent'].round(decimals = 1)

        problems_exp_fig = px.bar(problems_exp , x = "If yes, what kind of problem?", y = 'Percent', text = 'Percent')
        problems_exp_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return problems_exp_fig
    
    def purpose(data):
        purpose = data[['What is your purpose for traveling on water?', 'Who are you interviewing?']].sort_values(
            by = ['What is your purpose for traveling on water?'], ascending = False).value_counts(normalize = True)
        purpose = purpose.mul(100).rename('Percent').reset_index()
        purpose['Percent'] = purpose['Percent'].round(decimals = 1)

        purpose_fig = px.bar(purpose , x = "What is your purpose for traveling on water?", y = 'Percent', text = 'Percent')
        purpose_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return purpose_fig
    
#     def jetty_usage1(data):
#         jetty_usage = data[['How often do you use the jetty?', 'Who are you interviewing?']].sort_values(
#             by = ['How often do you use the jetty?'], ascending = False).value_counts(normalize = True)
#         jetty_usage = jetty_usage.mul(100).rename('Percent').reset_index()
#         jetty_usage['Percent'] = jetty_usage['Percent'].round(decimals = 1)

#         jetty_usage_fig = px.bar(jetty_usage , x = 'How often do you use the jetty?', y = 'Percent', text = 'Percent')
#         jetty_usage_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
#         return jetty_usage_fig
        
    
    def delay_ride(data):
        delayed = data[['Do you experience any form of delay before boarding a boat?', 'Who are you interviewing?']].sort_values(
            by = ['Do you experience any form of delay before boarding a boat?'], ascending = False).value_counts(normalize = True)
        delayed = delayed.mul(100).rename('Percent').reset_index()
        delayed['Percent'] = delayed['Percent'].round(decimals = 1)

        delayed_fig = px.bar(delayed , x = 'Do you experience any form of delay before boarding a boat?', y = 'Percent', text = 'Percent')
        delayed_fig.update_layout(yaxis = {'visible' : False, 'showticklabels' : False})
        return delayed_fig
    
    def anti_delay(data):
        anti = data[['If yes, how can it be improved?', 'Who are you interviewing?']].sort_values(
            by = ['If yes, how can it be improved?'], ascending = False).value_counts(normalize = True)
        anti = anti.mul(100).rename('Percent').reset_index()
        anti['Percent'] = anti['Percent'].round(decimals = 1)
        
        anti_fig = px.pie(anti, names = 'If yes, how can it be improved?')
        return anti_fig
    
    def rating(data):
        sec_rating = data['How would you rate the security at the Jetty?'].value_counts()
        dri_rating = data['How would you rate the boat drivers in terms of how coordinated they are while on water and their attitude to passengers?'].value_counts()
        staf_rating = data['How would you rate the services rendered by the staff working at the jetty?'].value_counts()

        passengers_rating = pd.DataFrame([sec_rating, dri_rating, staf_rating]).fillna(0).reset_index()
        return passengers_rating