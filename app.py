import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

dfL1Best = [4,5,3,4]
dfL2Best = [5,5,4]
dfL3Best = [3,4,5,5,3]
dfL4Best = [3,5,5,3,3,4,5]
def Leadership(df_pol, dfL1Best, dfL2Best, dfL3Best, dfL4Best):
  #L1
  L1S1 = (((df_pol['L1Q1'])/(dfL1Best[0]-2)>=1 and (1,) or (0,))[0])
  L1M1 = (((df_pol['L1Q1'])/(dfL1Best[0]-2)>=1 and (((df_pol['L1Q1']-1)/(dfL1Best[0]-2)<1 and ((df_pol['L1Q1']-1)/(dfL1Best[0]-2),) or (1,))[0],) or (0,))[0])
  L1A1 = (((df_pol['L1Q1'])/(dfL1Best[0]-2)>=1 and ((df_pol['L1Q1']-1)/(dfL1Best[0]-1),) or (0,))[0])
  L1S2 = (((df_pol['L1Q2'])/(dfL1Best[1]-3)>=1 and (1,) or (0,))[0])
  L1M2 = (((df_pol['L1Q2'])/(dfL1Best[1]-3)>=1 and (((df_pol['L1Q2']-1)/(dfL1Best[1]-3)>1 and (1,) or ((df_pol['L1Q2']-1)/(dfL1Best[1]-3),))[0],) or (0,))[0])
  L1A2 = (((df_pol['L1Q2'])/(dfL1Best[1]-3)>=1 and (((df_pol['L1Q2']-1)/(dfL1Best[1]-2)>1 and (1,) or ((df_pol['L1Q2']-1)/(dfL1Best[1]-2),))[0],) or (0,))[0])
  L1R2 = (((df_pol['L1Q2'])/(dfL1Best[1]-3)>=1 and (((df_pol['L1Q2']-1)/(dfL1Best[1]-1)>1 and (1,) or ((df_pol['L1Q2']-1)/(dfL1Best[1]-1),))[0],) or (0,))[0])
  L1T2 = ((L1R2>=0.75 and (((df_pol['L1Q4']>1 and ((df_pol['L1Q4']-1)/(dfL1Best[3]-1),) or (0,))[0]),) or (0,))[0])
  L1M3 = ((df_pol['L1Q3']==0 and (0,) or ((df_pol['L1Q3']-1)/(dfL1Best[2]-1),))[0])
  #L2
  L2M1 = (((((df_pol['L2Q1'])/(dfL2Best[0]-3)>=1 and (1,) or (0,))[0])+(((df_pol['L2Q2'])/(dfL2Best[1]-3)>=1 and (1,) or (0,))[0])+((df_pol['L2Q3']==0 and (0,) or ((df_pol['L2Q3']-1)/(dfL2Best[2]-1),))[0]))/3)
  L2A1 = (((((df_pol['L2Q1'])/(dfL2Best[0]-3)>=1 and (((df_pol['L2Q1']-1)/(dfL2Best[0]-3)>1 and (1,) or ((df_pol['L2Q1']-1)/(dfL2Best[0]-3),))[0],) or (0,))[0])+(((df_pol['L2Q2'])/(dfL2Best[1]-3)>=1 and (((df_pol['L2Q2']-1)/(dfL2Best[1]-3)>1 and (1,) or ((df_pol['L2Q2']-1)/(dfL2Best[1]-3),))[0],) or (0,))[0]))/2)
  L2R1 = (((((df_pol['L2Q1'])/(dfL2Best[0]-3)>=1 and (((df_pol['L2Q1']-1)/(dfL2Best[0]-2)>1 and (1,) or ((df_pol['L2Q1']-1)/(dfL2Best[0]-2),))[0],) or (0,))[0])+(((df_pol['L2Q2'])/(dfL2Best[1]-3)>=1 and (((df_pol['L2Q2']-1)/(dfL2Best[1]-2)>1 and (1,) or ((df_pol['L2Q2']-1)/(dfL2Best[1]-2),))[0],) or (0,))[0]))/2)
  L2T1 = (((((df_pol['L2Q1'])/(dfL2Best[0]-3)>=1 and (((df_pol['L2Q1']-1)/(dfL2Best[0]-1)>1 and (1,) or ((df_pol['L2Q1']-1)/(dfL2Best[0]-1),))[0],) or (0,))[0])+(((df_pol['L2Q2'])/(dfL2Best[1]-3)>=1 and (((df_pol['L2Q2']-1)/(dfL2Best[1]-1)>1 and (1,) or ((df_pol['L2Q2']-1)/(dfL2Best[1]-1),))[0],) or (0,))[0]))/2)
  #L3
  L3S1 = (((df_pol['L3Q1'])/(dfL3Best[0]-1)>=1 and (1,) or (0,))[0])
  L3M1 = (((df_pol['L3Q1'])/(dfL3Best[0]-1)>=1 and (((df_pol['L3Q1']-1)/(dfL3Best[0]-1)),) or (0,))[0])
  L3T1 = ((L3M1>=0.75 and ((df_pol['L3Q1']>=3 and (((df_pol['L3Q3']>1 and (((df_pol['L3Q3']-1)/(dfL3Best[2]-1)),) or (0,))[0]),) or (0,))[0],) or (0,))[0])
  L3M2 = ((df_pol['L3Q2']>1 and ((((df_pol['L3Q2'])/(dfL3Best[1]-1)>=1 and (1,) or ((df_pol['L3Q2'])/(dfL3Best[1]),))[0]),) or (0,))[0])
  L3A2 = ((((df_pol['L3Q2']>1 and ((((df_pol['L3Q2']-1)/(dfL3Best[1]-1)>=1 and (1,) or ((df_pol['L3Q2'])/dfL3Best[1],))[0]),) or (0,))[0])+((df_pol['L3Q4']>1 and ((((df_pol['L3Q4'])/(dfL3Best[3]-1)>=1 and (1,) or ((df_pol['L3Q4'])/(dfL3Best[3]-1),))[0]),) or (0,))[0]))/2)
  L3R2 = ((df_pol['L3Q4']>1 and ((df_pol['L3Q4']-1)/(dfL3Best[3]-1),) or (0,))[0])
  L3T2 = ((L3R2>=0.75 and (((df_pol['L3Q5']>1 and ((df_pol['L3Q5']/dfL3Best[4]),) or (0,))[0]),) or (0,))[0])
  #L4
  L4S1 = ((df_pol['L4Q6']>1 and ((((df_pol['L4Q6'])/(dfL4Best[5]-2)>1 and (1,) or ((df_pol['L4Q6'])/(dfL4Best[5]-2),))[0]),) or (0,))[0])
  L4A1 = ((df_pol['L4Q6']>1 and (((df_pol['L4Q6']-1)/(dfL4Best[5]-1)),) or (0,))[0])
  L4S2 = ((df_pol['L4Q1']>1 and (((df_pol['L4Q1']-1)/(dfL4Best[0]-1)),) or (0,))[0])
  L4M2 = ((((L4S2>=0.75 and (((df_pol['L4Q2']>1 and (((df_pol['L4Q2']/(dfL4Best[1]-2)<1 and ((df_pol['L4Q2']/(dfL4Best[1]-2)),) or (1,))[0]),) or (0,))[0]),) or (0,))[0])+(((df_pol['L4Q4'])/(dfL4Best[3]-1)>=1 and (1,) or ((df_pol['L4Q4'])/(dfL4Best[3]-1),))[0]))/2)
  L4A2 = (((L4S2>=0.75 and ((((df_pol['L4Q2']-1)/(dfL4Best[1]-2)>1 and (1,) or ((df_pol['L4Q2']-1)/(dfL4Best[1]-2),))[0]),) or (0,))[0]+(df_pol['L4Q4']/dfL4Best[3]))/2)
  L4R2 = ((L4A2>=0.75 and (((df_pol['L4Q2']>1 and ((df_pol['L4Q2']-1)/(dfL4Best[1]-1),) or (0,))[0]),) or (0,))[0])
  L4M3 = ((df_pol['L4Q3'])/(dfL4Best[2]))
  L4T3 = ((L4M3>=0.75 and (((df_pol['L4Q7']>1 and (((df_pol['L4Q7']-1)/(dfL4Best[6]-1)),) or (0,))[0]),) or (0,))[0])
  L4A4 = ((df_pol['L4Q5']>1 and (((df_pol['L4Q5']-1)/(dfL4Best[4]-1)),) or (0,))[0])
  leadershipResults = [L1S1, L1M1, L1A1, L1S2, L1M2, L1A2, L1R2, L1T2, L1M3, L2M1, L2A1, L2R1, L2T1, L3S1, L3M1, L3T1, L3M2, L3A2, L3R2, L3T2, L4S1, L4A1, L4S2, L4M2, L4A2, L4R2, L4M3, L4T3, L4A4]

  return leadershipResults#, completenessLeadership
  

def check_completeness(leadershipResults):
    
    completenessLeadership = 0
    for i in range(len(leadershipResults)):
        if leadershipResults[i] == 1:
            completenessLeadership = completenessLeadership+1
    return completenessLeadership        

####
####
#### CLEANING THE DATA
####
####
df = pd.read_csv('Demo SMR Self-Assessment Tool.csv', sep=';')

####
####
#### PLOTING THE DATA
####
####

st.set_page_config(layout = "wide")
title1, title2, title3 = st.columns([1,1,1])
with title2:
  st.title('SMR DASHBOARD')
##
# SELECTION CITY AND DIMENSION
##
with st.sidebar:
  city = st.selectbox(
      'Select city',
      ('Donostia', 'Pamplona', 'Bilbao'))
  dimension = st.selectbox(
      'Select dimension',
      ('Leadership & Governance', 'Preparedness', 'Cooperation','Infrastructure & Resources', 'Urban Development & Environmental'))

##
# RADAR GRAPHS
##
st.subheader('Questions Performance Analysis')
col1,col2 = st.columns([1,1])

#Radar L1
categories = ['Resilience<br>Governance', 'Plans<br>Integration', 'Access to<br>Basic Services', 'Support to<br>other cities']
categories = [*categories, categories[0]]
best = [4, 5, 3, 4]
mean = [df['L1Q1'].mean(),df['L1Q2'].mean(),df['L1Q3'].mean(),df['L1Q4'].mean()]
best = [*best, best[0]]
mean = [*mean, mean[0]]

fig = go.Figure(
    data=[
        go.Scatterpolar(r=best, theta=categories, fill='toself', name='best', line_color = '#2C3639'),
        go.Scatterpolar(r=mean, theta=categories, fill='toself', name='mean', line_color = '#ffb400')],
    layout=go.Layout(
        title=go.layout.Title(text='Leadership & Governance (L1)'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True)
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
col1.plotly_chart(fig, use_container_width=True)

#Radar L2
categories = ['Standards<br>Alignment', 'Certification<br>Processes', 'Risk Reduction and<br>Prevention Policies']
categories = [*categories, categories[0]]
best = [5, 5, 4]
mean = [df['L2Q1'].mean(), df['L2Q2'].mean(), df['L2Q3'].mean()]
best = [*best, best[0]]
mean = [*mean, mean[0]]
fig = go.Figure(
    data=[
        go.Scatterpolar(r=best, theta=categories, fill='toself', name='best', line_color = '#2C3639'),
        go.Scatterpolar(r=mean, theta=categories, fill='toself', name='mean', line_color = '#ffb400')],
    layout=go.Layout(
        title=go.layout.Title(text='Leadership & Governance (L2)'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True)
)
col2.plotly_chart(fig, use_container_width=True)

col3,col4 = st.columns([1,1])

#Radar L3
categories = ['Resilience<br>Culture', 'Lessons<br>Past Events', 'Knowledge<br>Transfer', 'Learning<br>Process', 'Learning Process<br>Assessment']
categories = [*categories, categories[0]]
best = [3, 4, 5, 5, 3]
mean = [df['L3Q1'].mean(), df['L3Q2'].mean(), df['L3Q3'].mean(), df['L3Q4'].mean(), df['L3Q5'].mean()]
best = [*best, best[0]]
mean = [*mean, mean[0]]
fig = go.Figure(
    data=[
        go.Scatterpolar(r=best, theta=categories, fill='toself', name='best', line_color = '#2C3639'),
        go.Scatterpolar(r=mean, theta=categories, fill='toself', name='mean', line_color = '#ffb400')],
    layout=go.Layout(
        title=go.layout.Title(text='Leadership & Governance (L3)'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True)
)
col3.plotly_chart(fig, use_container_width=True)

#Radar L4
categories = ['Disaster Response<br>Plan', 'RAP Plan<br>Development', 'Stakeholders<br>Collaboration', 'Disaster<br>Focus', 'Climate Change<br>Perspective', 'Resilience Adoption<br>and Integration', 'Collaboration and Networking with<br>Cities and External Bodies']
categories = [*categories, categories[0]]
best = [3, 5, 5, 3, 3, 4, 5]
mean = [df['L4Q1'].mean(), df['L4Q2'].mean(), df['L4Q3'].mean(), df['L4Q4'].mean(), df['L4Q5'].mean(), df['L4Q6'].mean(), df['L4Q7'].mean()]
best = [*best, best[0]]
mean = [*mean, mean[0]]
fig = go.Figure(
    data=[
        go.Scatterpolar(r=best, theta=categories, fill='toself', name='best', line_color = '#2C3639'),
        go.Scatterpolar(r=mean, theta=categories, fill='toself', name='mean', line_color = '#ffb400')],
    layout=go.Layout(
        title=go.layout.Title(text='Leadership & Governance (L4)'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True)
)
col4.plotly_chart(fig, use_container_width=True)

##
# Policies
##
st.subheader('Policies Completeness')
secQuestionnaire_col1,secQuestionnaire_col2 = st.columns([1,4])
with secQuestionnaire_col1:
  questionnaire = st.selectbox(
    'Select the questionnaire',
      ('answer 1', 'answer 2', 'answer 3', 'answer 4', 'answer 5', 'answer 6', 'mean'))

match questionnaire:
    case "answer 1":
        df_pol = df.iloc[0]
    case "answer 2":
        df_pol = df.iloc[1]
    case "answer 3":
        df_pol = df.iloc[2]
    case "answer 4":
        df_pol = df.iloc[3]
    case "answer 5":
        df_pol = df.iloc[4]
    case "answer 6":
        df_pol = df.iloc[5]
    case _:
        print("error")

leadershipResults = Leadership(df_pol, dfL1Best, dfL2Best, dfL3Best, dfL4Best)

sec4_col1,sec4_col2 = st.columns([1,1])

## Line graph L1
fig = go.Figure()
fig.add_trace(go.Bar(
    y=['L1S1','L1M1','L1A1','L1S2','L1M2','L1A2','L1R2','L1T2','L1M3'],
    x=[1,1,1,1,1,1,1,1,1],
    name='Best Accomplishment',
    orientation='h',
    marker=dict(
        color='#e2e2e2',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )
))
fig.add_trace(go.Bar(
    y=['L1S1','L1M1','L1A1','L1S2','L1M2','L1A2','L1R2','L1T2','L1M3'],
    x=[leadershipResults[0],
       leadershipResults[1],
       leadershipResults[2],
       leadershipResults[3],
       leadershipResults[4],
       leadershipResults[5],
       leadershipResults[6],
       leadershipResults[7],
       leadershipResults[8]],
    name='Captured Completeness',
    orientation='h',
    marker=dict(
        color='#ffb400',
        line=dict(color='#4C3A51', width=1)
    )
))

fig.update_layout(
  title = 'All Policies - L1',
  barmode='overlay',
  legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),
)
sec4_col1.plotly_chart(fig, use_container_width=True)

## Line graph 2
fig = go.Figure()
fig.add_trace(go.Bar(
    y=['L2M1','L2A1','L2R1','L2T1'],
    x=[1,1,1,1],
    name='Best Accomplishment',
    orientation='h',
    marker=dict(
        color='#e2e2e2',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )
))
fig.add_trace(go.Bar(
    y=['L2M1','L2A1','L2R1','L2T1'],
    x=[leadershipResults[9],
       leadershipResults[10],
       leadershipResults[11],
       leadershipResults[12]],
    name='Captured Completeness',
    orientation='h',
    marker=dict(
        color='#ffb400',
        line=dict(color='#4C3A51', width=1)
    )
))

fig.update_layout(
  title = 'All Policies - L2',
  barmode='overlay',
  legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),
)
sec4_col2.plotly_chart(fig, use_container_width=True)

sec4_col3, sec4_col4 = st.columns([1,1])

## Line graph 3
fig = go.Figure()
fig.add_trace(go.Bar(
    y=['L3S1','L3M1','L3T1','L3M2','L3A2','L3R2','L3T2'],
    x=[1,1,1,1,1,1,1],
    name='Best Accomplishment',
    orientation='h',
    marker=dict(
        color='#e2e2e2',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )
))
fig.add_trace(go.Bar(
    y=['L3S1','L3M1','L3T1','L3M2','L3A2','L3R2','L3T2'],
    x=[leadershipResults[13],
       leadershipResults[14],
       leadershipResults[15],
       leadershipResults[16],
       leadershipResults[17],
       leadershipResults[18],
       leadershipResults[19]],
    name='Captured Completeness',
    orientation='h',
    marker=dict(
        color='#ffb400',
        line=dict(color='#4C3A51', width=1)
    )
))

fig.update_layout(
  title = 'All Policies - L3',
  barmode='overlay',
  legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),
)
sec4_col3.plotly_chart(fig, use_container_width=True)

# Line graph 4
fig = go.Figure()
fig.add_trace(go.Bar(
    y=['L4S1','L4A1','L4S2','L4M2','L4A2','L4R2','L4M3','L4T3','L4A4'],
    x=[1,1,1,1,1,1,1,1,1],
    name='Best Accomplishment',
    orientation='h',
    marker=dict(
        color='#e2e2e2',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    )
))
fig.add_trace(go.Bar(
    y=['L4S1','L4A1','L4S2','L4M2','L4A2','L4R2','L4M3','L4T3','L4A4'],
    x=[leadershipResults[20],
       leadershipResults[21],
       leadershipResults[22],
       leadershipResults[23],
       leadershipResults[24],
       leadershipResults[25],
       leadershipResults[26],
       leadershipResults[27],
       leadershipResults[28]],
    name='Captured Completeness',
    orientation='h',
    marker=dict(
        color='#ffb400',
        line=dict(color='#4C3A51', width=1)
    )
))

fig.update_layout(
  title = 'All Policies - L4',
  barmode='overlay',
  legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),
)
sec4_col4.plotly_chart(fig, use_container_width=True) 

##
# Policies completeness in general
##
st.subheader("SMR Completeness")
sec5_col1, sec5_col2, sec5_col3, sec5_col4, sec5_col5 = st.columns([1,1,1,1,1])

completenessLeadership = check_completeness(leadershipResults)

#Gauge 1 - Leadership & Governance
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = completenessLeadership,
    mode = "gauge+number+delta",
    title = {'text': "Leadership & Governance"},
    delta = {'reference': 29},
    gauge = {'axis': {'range': [None, 29]},
              'bar': {'color': "gray"},
              'steps' : [
                {'range': [0, 9.6], 'color': "#FF6961"},
                {'range': [9.6, 19.3], 'color': "#F8D66D"},
                {'range': [19.3, 29], 'color': "#7ABD7E"}]}))
fig.update_layout(
  margin=dict(l=20, r=20, t=10, b=10),
)
sec5_col1.plotly_chart(fig, use_container_width=True)

#Gauge 2 - Preparedness
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 0,
    mode = "gauge+number+delta",
    title = {'text': "Preparedness"},
    delta = {'reference': 23},
    gauge = {'axis': {'range': [None, 23]},
              'bar': {'color': "gray"},
              'steps' : [
                {'range': [0, 7.6], 'color': "#FF6961"},
                {'range': [7.6, 15.3], 'color': "#F8D66D"},
                {'range': [15.3, 23], 'color': "#7ABD7E"}]}))
fig.update_layout(
  margin=dict(l=20, r=20, t=10, b=10),
)
sec5_col2.plotly_chart(fig, use_container_width=True)

#Gauge 3 - Infrastructure & Resources
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 0,
    mode = "gauge+number+delta",
    title = {'text': "Infrastructure & Resources"},
    delta = {'reference': 28},
    gauge = {'axis': {'range': [None, 28]},
              'bar': {'color': "gray"},
              'steps' : [
                {'range': [0, 9.3], 'color': "#FF6961"},
                {'range': [9.3, 18.6], 'color': "#F8D66D"},
                {'range': [18.6, 28], 'color': "#7ABD7E"}]}))
fig.update_layout(
  margin=dict(l=20, r=20, t=10, b=10),
)
sec5_col3.plotly_chart(fig, use_container_width=True)

#Gauge 4 - Cooperation
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 0,
    mode = "gauge+number+delta",
    title = {'text': "Cooperation"},
    delta = {'reference': 21},
    gauge = {'axis': {'range': [None, 21]},
              'bar': {'color': "gray"},
              'steps' : [
                {'range': [0, 7], 'color': "#FF6961"},
                {'range': [7, 14], 'color': "#F8D66D"},
                {'range': [14, 21], 'color': "#7ABD7E"}]}))
fig.update_layout(
  margin=dict(l=20, r=20, t=10, b=10),
)
sec5_col4.plotly_chart(fig, use_container_width=True)

#Gauge 5 - Urban Development & Environmental
fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = 0,
    mode = "gauge+number+delta",
    title = {'text': "Urban Development & Environmental"},
    delta = {'reference': 22},
    gauge = {'axis': {'range': [None, 22]},
              'bar': {'color': "gray"},
              'steps' : [
                {'range': [0, 7.3], 'color': "#FF6961"},
                {'range': [7.3, 14.6], 'color': "#F8D66D"},
                {'range': [14.6, 22], 'color': "#7ABD7E"}]}))
fig.update_layout(
  margin=dict(l=20, r=20, t=10, b=10),
)
sec5_col5.plotly_chart(fig, use_container_width=True)

##
# Overview of Policies by years
##
st.subheader("Cities and SMR Completeness")
df = pd.DataFrame(np.array([['Donostia', 15, 2021], ['Donostia', 16, 2022], ['Donostia', 17, 2023], ['Pamplona', 20, 2021], ['Pamplona', 21, 2022], ['Pamplona', 21, 2023], ['Bilbao', 14, 2021], ['Bilbao', 15, 2022], ['Bilbao', 15, 2023]]),
                   columns=['city', 'policy', 'year'])
fig = px.line(df, x="year", y="policy", color="city", symbol="city", text="policy", markers=True, title="Cities X Years (Leadership & Governance)")

fig.update_traces(line=dict(width=5),
                  marker_size=25)
st.plotly_chart(fig, theme="streamlit", use_container_width=True)