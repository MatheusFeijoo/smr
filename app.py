import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

## TO DO
# Add the excel formulas for each dimension
# Update the charts based on the new dimensions tabs (create the new tabs based on leadership)

st.set_page_config(layout = "wide")

dfL1Best = [4,5,3,4]
dfL2Best = [5,5,4]
dfL3Best = [3,4,5,5,3]
dfL4Best = [3,5,5,3,3,4,5]
dfP1Best = [5,4,3,4,5,4,4,4]
dfP2Best = [4,3,3,3,3,3,3,4,5,3,3,3]
dfI1Best = [4,4,4,4,5,3,4,4,4,3,4,4]
dfI2Best = [3,3,4,3,4,3,3,3,4,3,3,3,3,3]
dfC1Best = [4,3,3,4,4,5,3,3,4,4]
dfC2Best = [4,4,4,4,4,4,4,5]
dfU1Best = [3,3,3,3,3,4,4,4,3,3,3,3]
dfE1Best = [4,3,3,4,4,3,3,3,3,3,3,3,3]

leadershipPoliciesText = ({'L1S1': ['Establish a working team responsible for resilience issues in the city'], 
                    'L1M1': ['Establish a single point of coordination in the city (i.e. resilience department or committee) that facilitates cross-departmental coordination board and procedures'], 
                    'L1A1': ['Implement the multi-level governance approach to establish an organisational structure with strong leadership and clarity of coordination between municipal, regional and national levels of governance'], 
                    'L1S2': ['Integrate resilience into visions, policies and strategies for city development plans'], 
                    'L1M2': ['Align, integrate and connect the resilience action plan with regional plans'], 
                    'L1A2': ['Align, integrate and connect the resilience action plan with national plans'], 
                    'L1R2': ['Align, integrate and connect the city resilience plan with regional, national and international resilience management guidelines'], 
                    'L1T2': ['Support the development of other city resilience plans aligned, integrated and connected with regional, national and international resilience management guidelines'], 
                    'L1M3': ['Promote equality of access to services and basic infrastructure to vulnerable sectors of society'],
                    'L2M1': ['Integrate resilience approach into existing risk reduction and prevention policies by establishing new strategies, acts, laws and codes'], 
                    'L2A1': ['Conduct certification processes to achieve the conformity with national standards'], 
                    'L2R1': ['Conduct certification processes to achieve the conformity with international standards'], 
                    'L2T1': ['Contribute to the development of standards on resilience guidelines and policies'],
                    'L3S1': ['Develop a strategy to create a resilience culture'], 
                    'L3M1': ['Promote a culture of resilience among citizens, institutions and organisations by investing and promoting social and institutional cohesion'], 
                    'L3T1': ['Promote leadership for knowledge transferring and sharing among global cities, regions and nations'], 
                    'L3M2': ['Review existing strategies, practices, and actions to capture lessons from past events'], 
                    'L3A2': ['Formalize the learning process and institutionalise regular debriefing meetings'], 
                    'L3R2': ['Create a ´Learning City` by establishing active networks of stakeholders to exchange lessons learned and knowledge'], 
                    'L3T2': ['Develop formal procedures to assess the effectiveness of the learning process'],
                    'L4S1': ['Identify the requirements needed to boost the process of integrating the resilience approach into development policies'], 
                    'L4A1': ['Properly integrate the resilience strategy with other key city functions (planning, sustainability, emergency management, infrastructure management)'], 
                    'L4S2': ['Develop disaster management, response and recovery plan '], 
                    'L4M2': ['Develop a resilience action plan to respond to shocks and long-term stresses by taking as a starting point those city elements and resources already available'], 
                    'L4A2': ['Develop leading indicators for assessing the performance of the resilience action plan'], 
                    'L4R2': ['Perform periodic monitoring and assessment of the resilience action plan effectiveness to continuously update and improve the plan with new data and planning strategies'], 
                    'L4M3': ['Adopt a bottom-up approach that facilitates transparent and inclusive participatory and multi-stakeholder consultation processes to develop resilience planning, policies and strategies'], 
                    'L4T3': ["Share the CITY's expertise in resilience action plan development with other cities about to start the process"], 
                    'L4A4': ['Integrate climate change perspective in developing the resilience action plan by incorporating climate risk information at every phase of policy planning']})


df = pd.read_csv('Demo SMR Self-Assessment Tool.csv', sep=';')

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
  leadershipResults = ({'L1S1': [L1S1], 'L1M1': [L1M1], 'L1A1': [L1A1], 'L1S2': [L1S2], 'L1M2': [L1M2], 'L1A2': [L1A2], 'L1R2': [L1R2], 'L1T2': [L1T2], 'L1M3': [L1M3],
                        'L2M1': [L2M1], 'L2A1': [L2A1], 'L2R1': [L2R1], 'L2T1': [L2T1],
                        'L3S1': [L3S1], 'L3M1': [L3M1], 'L3T1': [L3T1], 'L3M2': [L3M2], 'L3A2': [L3A2], 'L3R2': [L3R2], 'L3T2': [L3T2],
                        'L4S1': [L4S1], 'L4A1': [L4A1], 'L4S2': [L4S2], 'L4M2': [L4M2], 'L4A2': [L4A2], 'L4R2': [L4R2], 'L4M3': [L4M3], 'L4T3': [L4T3], 'L4A4': [L4A4]})

  #Classifying by achieved policy by completeness
  starting = moderate = advanced = robust = vertebrate = 0
  for i in leadershipResults:
    if "S" in i and leadershipResults[i][0] == 1:
        starting = starting + 1
    elif "M" in i and leadershipResults[i][0] == 1:
        moderate = moderate + 1
    elif "A" in i and leadershipResults[i][0] == 1:
        advanced = advanced + 1 
    elif "R" in i and leadershipResults[i][0] == 1:
        robust = robust + 1
    elif "T" in i and leadershipResults[i][0] == 1:
        vertebrate = vertebrate + 1
  completeness = [starting, moderate, advanced, robust, vertebrate]

  return leadershipResults, completeness

def Preparedness (df_pol, dfP1Best, dfP2Best):
    preparednessResults = preparednessCompleteness = 14
    return preparednessResults, preparednessCompleteness

def Infra (df_pol, dfI1Best, dfI2Best):
    infraResults = infraCompleteness = 16
    return infraResults, infraCompleteness

def Cooperation (df_pol, dfC1Best, dfC2Best):
    cooperationResults = cooperationCompleteness = 13
    return cooperationResults, cooperationCompleteness

def Urban (df_pol, dfU1Best, dfE1Best):
    urbanResults = urbanCompleteness = 10
    return urbanResults, urbanCompleteness
      
# GAUGE GRAPHS

def gauge_graphs (completeness, text, reference):
    match text:
            case "Leadership & Governance":
                starting = [0, 5] #5
                moderate = [5, 10] # 13
                advanced = [10, 15] # 20
                robust = [15, 20] # 24
                vertebrate = [20, 25] # 29
            case "Preparedness":
                starting = [0, 5] # 6
                moderate = [5, 10]#10
                advanced = [10, 15]#17
                robust = [15, 20]#20
                vertebrate = [20, 25]#23
            case "Infrastructure & Resources":
                starting = [0, 5]#6
                moderate = [5, 10]#14
                advanced = [10, 15]#21
                robust = [15, 20]#24
                vertebrate = [20, 25]#28
            case "Cooperation":
                starting = [0, 5]#2
                moderate = [5, 10]#7
                advanced = [10, 15]#13
                robust = [15, 20]#17
                vertebrate = [20, 25]#21
            case "Urban Development <br>& Environmental":
                starting = [0, 5]#4
                moderate = [5, 10]#10
                advanced = [10, 15]#17
                robust = [15, 20]#21
                vertebrate = [20, 25]#22
            case _:
                print("error")
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = completeness,
        mode = "gauge+number+delta",
        title = {'text': text},
        delta = {'reference': reference},
        gauge = {'axis': {'range': [None, reference]},
                'bar': {'color': "gray"},
                'steps' : [
                    {'range': starting, 'color': "#ef476f",},
                    {'range': moderate, 'color': "#ffd166"},
                    {'range': advanced, 'color': "#06d6a0"},
                    {'range': robust, 'color': "#118ab2"},
                    {'range': vertebrate, 'color': "#073b4c"},]}))
    fig.update_layout(
        height=270,
        margin= dict(l=0,r=0,b=0,t=0)
        )
    return fig

# RADAR GRAPHS
def radar_graphs (categories, best, mean, text):
    categories = [*categories, categories[0]]
    best = [*best, best[0]]
    mean = [*mean, mean[0]]

    fig = go.Figure(
        data=[
            go.Scatterpolar(r=best, theta=categories, fill='toself', name='best', line_color = '#2C3639'),
            go.Scatterpolar(r=mean, theta=categories, fill='toself', name='mean', line_color = '#ffb400')],
        layout=go.Layout(
            title=go.layout.Title(text=text),
            polar={'radialaxis': {'visible': True}},
            showlegend=True))

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", title_x=0, margin= dict(l=30,r=30,b=50,t=50))
    return fig

# LINE GRAPHS
def line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(y=dimension, x=valueBestDimension, name='Best Accomplishment', orientation='h',
                             marker=dict(color='#e2e2e2', line=dict(color='rgba(58, 71, 80, 1.0)', width=1))))
        
    fig.add_trace(go.Bar(y=dimension, x=valueCapturedCompleteness, name='Captured Completeness', orientation='h',
                             marker=dict(color='#ffb400', line=dict(color='#4C3A51', width=1))))

    fig.update_layout(title = title, barmode='overlay', title_x=0,
                          legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                          margin= dict(l=30,r=30,b=50,t=50))
    return fig

####
####
#### PLOTING THE DATA
####
####

##
# SELECTION CITY AND DIMENSION
##
with st.sidebar:
    city = st.selectbox(
        'Select city',
        ('Donostia', 'Pamplona', 'Bilbao'))
    
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
        case "mean":
            df_pol = df.mean(axis=0)
        case _:
            print("error")

    leadershipResults, leadershipCompleteness = Leadership(df_pol, dfL1Best, dfL2Best, dfL3Best, dfL4Best)
    preparednessResults, preparednessCompleteness = Preparedness(df_pol, dfP1Best, dfP2Best)
    infraResults, infraCompleteness = Infra(df_pol, dfI1Best, dfI2Best)
    cooperationResults, cooperationCompleteness = Cooperation(df_pol, dfC1Best, dfC2Best)
    urbanResults, urbanCompleteness = Urban(df_pol, dfU1Best, dfE1Best)


title1, title2 = st.columns((0.11,1)) 
with title1:
    st.image('logo_smr.png', width = 120)
with title2:
    st.title('SMR Dashboard - ' + city)

##
# Policies completeness in general
##
st.subheader("SMR Completeness")
sec5_col1, sec5_col2, sec5_col3, sec5_col4, sec5_col5 = st.columns([1,1,1,1,1])

#Gauge 1 - Leadership & Governance
completenessLeadership = sum(leadershipCompleteness)
text = 'Leadership & Governance'
reference = 25#29
fig1 = gauge_graphs(completenessLeadership, text, reference)
sec5_col1.plotly_chart(fig1, use_container_width=True)

#Gauge 2 - Preparedness
completenessPreparedness = preparednessCompleteness
text = 'Preparedness'
reference = 25#23
fig2 = gauge_graphs(completenessPreparedness, text, reference)
sec5_col2.plotly_chart(fig2, use_container_width=True)

#Gauge 3 - Infrastructure & Resources
completenessInfra = infraCompleteness
text = 'Infrastructure & Resources'
reference = 25#28
fig3 = gauge_graphs(completenessInfra, text, reference)
sec5_col3.plotly_chart(fig3, use_container_width=True)

#Gauge 4 - Cooperation
completenessCooperation = cooperationCompleteness
text = 'Cooperation'
reference = 25#21
fig4 = gauge_graphs(completenessCooperation, text, reference)
sec5_col4.plotly_chart(fig4, use_container_width=True)

#Gauge 5 - Urban Development & Environmental
completenessUrban = urbanCompleteness
text = 'Urban Development <br>& Environmental'
reference = 25#22
fig5 = gauge_graphs(completenessUrban, text, reference)
sec5_col5.plotly_chart(fig5, use_container_width=True)

# tab1, tab2, tab3, tab4, tab5 = st.tabs(['Leadership & Governance', 'Preparedness', 'Cooperation','Infrastructure & Resources', 'Urban Development & Environmental'])

# with tab1:
    ##
    # RADAR GRAPHS
    ##
with st.expander('Questions Performance Analysis', expanded=True):
    st.subheader('Questions Performance Analysis - Leadership & Governance')
    
    col1, col2 = st.columns([1,1])
    # RADAR L1
    categories = ['Resilience<br>Governance', 'Plans<br>Integration', 'Access to<br>Basic Services', 'Support to<br>other cities']
    best = [4, 5, 3, 4]
    mean = [df['L1Q1'].mean(),df['L1Q2'].mean(),df['L1Q3'].mean(),df['L1Q4'].mean()]
    text='Leadership & Governance (L1)'
    fig1 = radar_graphs(categories, best, mean, text)
    col1.plotly_chart(fig1, use_container_width=True)

    # RADAR L2
    categories = ['Standards<br>Alignment', 'Certification<br>Processes', 'Risk Reduction and<br>Prevention Policies']
    best = [5, 5, 4]
    mean = [df['L2Q1'].mean(), df['L2Q2'].mean(), df['L2Q3'].mean()]
    text='Leadership & Governance (L2)'
    fig2 = radar_graphs(categories, best, mean, text)
    col2.plotly_chart(fig2, use_container_width=True)

    col3, col4 = st.columns([1,1])
    # RADAR L3
    categories = ['Resilience<br>Culture', 'Lessons<br>Past Events', 'Knowledge<br>Transfer', 'Learning<br>Process', 'Learning Process<br>Assessment']
    best = [3, 4, 5, 5, 3]
    mean = [df['L3Q1'].mean(), df['L3Q2'].mean(), df['L3Q3'].mean(), df['L3Q4'].mean(), df['L3Q5'].mean()]
    text='Leadership & Governance (L3)'
    fig3 = radar_graphs(categories, best, mean, text)
    col3.plotly_chart(fig3, use_container_width=True)

    # RADAR L4
    categories = ['Disaster Response<br>Plan', 'RAP Plan<br>Development', 'Stakeholders<br>Collaboration', 'Disaster<br>Focus', 'Climate Change<br>Perspective', 'Resilience Adoption<br>and Integration', 'Collaboration and Networking with<br>Cities and External Bodies']
    best = [3, 5, 5, 3, 3, 4, 5]
    mean = [df['L4Q1'].mean(), df['L4Q2'].mean(), df['L4Q3'].mean(), df['L4Q4'].mean(), df['L4Q5'].mean(), df['L4Q6'].mean(), df['L4Q7'].mean()]
    text='Leadership & Governance (L4)'
    fig4 = radar_graphs(categories, best, mean, text)
    col4.plotly_chart(fig4, use_container_width=True)

##
# Policies
##
with st.expander('Completeness', expanded=True):
    st.subheader('Completeness - Leadership & Governance')

    linegraphView = st.selectbox('Select the view - To see the recommendations select "SMART Completeness (All subdimensions)"',
    ('Policies Completeness','SMART Completeness (Each subdimension)','SMART Completeness (All subdimensions)'))

    if linegraphView == 'Policies Completeness':
        sec4_col1,sec4_col2 = st.columns([1,1])
        ## LINE GRAPH L1
        dimension = ['L1S1','L1S2','L1M1','L1M2','L1M3','L1A1','L1A2','L1R2','L1T2']
        valueBestDimension = [1,1,1,1,1,1,1,1,1]
        valueCapturedCompleteness = [leadershipResults['L1S1'][0], leadershipResults['L1S2'][0], 
                                    leadershipResults['L1M1'][0], leadershipResults['L1M2'][0], leadershipResults['L1M3'][0], 
                                    leadershipResults['L1A1'][0], leadershipResults['L1A2'][0], 
                                    leadershipResults['L1R2'][0], leadershipResults['L1T2'][0]]
        title = 'All Policies - L1'
        fig1 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col1.plotly_chart(fig1, use_container_width=True)

        ## LINE GRAPH L2
        dimension = ['L2M1','L2A1','L2R1','L2T1']
        valueBestDimension = [1,1,1,1]
        valueCapturedCompleteness = [leadershipResults['L2M1'][0], leadershipResults['L2A1'][0], leadershipResults['L2R1'][0], leadershipResults['L2T1'][0]]
        title = 'All Policies - L2'
        fig2 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col2.plotly_chart(fig2, use_container_width=True)

        sec4_col3, sec4_col4 = st.columns([1,1])
        ## LINE GRAPH L3
        dimension = ['L3S1','L3M1','L3M2','L3A2','L3R2','L3T1','L3T2']
        valueBestDimension = [1,1,1,1,1,1,1]
        valueCapturedCompleteness = [leadershipResults['L3S1'][0],
                                    leadershipResults['L3M1'][0], leadershipResults['L3M2'][0],
                                    leadershipResults['L3A2'][0],
                                    leadershipResults['L3R2'][0],
                                    leadershipResults['L3T1'][0], leadershipResults['L3T2'][0]]
        title = 'All Policies - L3'
        fig3 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col3.plotly_chart(fig3, use_container_width=True)

        # LINE GRAPH L4
        dimension = ['L4S1','L4S2','L4M2','L4M3','L4A1','L4A2','L4A4','L4R2','L4T3']
        valueBestDimension = [1,1,1,1,1,1,1,1,1]
        valueCapturedCompleteness = [leadershipResults['L4S1'][0], leadershipResults['L4S2'][0],
                                    leadershipResults['L4M2'][0], leadershipResults['L4M3'][0],
                                    leadershipResults['L4A1'][0], leadershipResults['L4A2'][0], leadershipResults['L4A4'][0],
                                    leadershipResults['L4R2'][0],
                                    leadershipResults['L4T3'][0], ]
        title = 'All Policies - L4'
        fig4 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col4.plotly_chart(fig4, use_container_width=True)
    
    #
    ## SMART Completeness (Each subdimension)
    #
    elif linegraphView == 'SMART Completeness (Each subdimension)':
        sec4_col1,sec4_col2 = st.columns([1,1])
        ## LINE GRAPH L1
        dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
        valueBestDimension = [1,1,1,1,1]
        valueCapturedCompleteness = [(leadershipResults['L1S1'][0] + leadershipResults['L1S2'][0])/2, 
                                    (leadershipResults['L1M1'][0] + leadershipResults['L1M2'][0] + leadershipResults['L1M3'][0])/3, 
                                    (leadershipResults['L1A1'][0] + leadershipResults['L1A2'][0])/2, 
                                    (leadershipResults['L1R2'][0] + leadershipResults['L1T2'][0])/2]
        title = 'All Policies - L1'
        fig1 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col1.plotly_chart(fig1, use_container_width=True)

        ## LINE GRAPH L2
        dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
        valueBestDimension = [1,1,1,1,1]
        valueCapturedCompleteness = [leadershipResults['L2M1'][0], leadershipResults['L2A1'][0], leadershipResults['L2R1'][0], leadershipResults['L2T1'][0]]
        title = 'All Policies - L2'
        fig2 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col2.plotly_chart(fig2, use_container_width=True)

        sec4_col3, sec4_col4 = st.columns([1,1])
        ## LINE GRAPH L3
        dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
        valueBestDimension = [1,1,1,1,1]
        valueCapturedCompleteness = [leadershipResults['L3S1'][0],
                                    (leadershipResults['L3M1'][0] + leadershipResults['L3M2'][0])/2,
                                    leadershipResults['L3A2'][0],
                                    leadershipResults['L3R2'][0],
                                    (leadershipResults['L3T1'][0] + leadershipResults['L3T2'][0])/2]
        title = 'All Policies - L3'
        fig3 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col3.plotly_chart(fig3, use_container_width=True)

        # LINE GRAPH L4
        dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
        valueBestDimension = [1,1,1,1,1]
        valueCapturedCompleteness = [(leadershipResults['L4S1'][0] + leadershipResults['L4S2'][0])/2,
                                    (leadershipResults['L4M2'][0] + leadershipResults['L4M3'][0])/2,
                                    (leadershipResults['L4A1'][0] + leadershipResults['L4A2'][0] + leadershipResults['L4A4'][0])/3,
                                    leadershipResults['L4R2'][0],
                                    leadershipResults['L4T3'][0], ]
        title = 'All Policies - L4'
        fig4 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        sec4_col4.plotly_chart(fig4, use_container_width=True)
    
    elif linegraphView == 'SMART Completeness (All subdimensions)':
        dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
        valueBestDimension = [1,1,1,1,1]
        valueCapturedCompleteness = [(leadershipResults['L1S1'][0] + leadershipResults['L1S2'][0] + leadershipResults['L3S1'][0] + leadershipResults['L4S1'][0] + leadershipResults['L4S2'][0])/5,
                                    (leadershipResults['L1M1'][0] + leadershipResults['L1M2'][0] + leadershipResults['L1M3'][0] + leadershipResults['L2M1'][0] + leadershipResults['L3M1'][0] + leadershipResults['L3M2'][0] + leadershipResults['L4M2'][0] + leadershipResults['L4M3'][0])/8,
                                    (leadershipResults['L1A1'][0] + leadershipResults['L1A2'][0] + leadershipResults['L2A1'][0] + leadershipResults['L3A2'][0] + leadershipResults['L4A1'][0] + leadershipResults['L4A2'][0] + leadershipResults['L4A4'][0])/7,
                                    (leadershipResults['L1R2'][0] + leadershipResults['L2R1'][0] + leadershipResults['L3R2'][0] + leadershipResults['L4R2'][0])/4,
                                    (leadershipResults['L1T2'][0] + leadershipResults['L2T1'][0] + leadershipResults['L3T1'][0] + leadershipResults['L3T2'][0] + leadershipResults['L4T3'][0])/5]
        title = 'All Policies'
        fig1 = line_graphs(dimension, valueBestDimension, valueCapturedCompleteness, title)
        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

        improve_dimension = 0
        dimension_value = 0

        if valueCapturedCompleteness[0] < 1:
            improve_dimension = "S"
            dimension_value = 0
        elif valueCapturedCompleteness[1] < 1:
            improve_dimension = "M"
            dimension_value = 1
        elif valueCapturedCompleteness[2] < 1:
            improve_dimension = "A"
            dimension_value = 2
        elif valueCapturedCompleteness[3] < 1:
            improve_dimension = "R"
            dimension_value = 3
        elif valueCapturedCompleteness[4] < 1:
            improve_dimension = "T"
            dimension_value = 4

        if valueCapturedCompleteness[dimension_value]<1:




            st.subheader("Recommendations")
            st.markdown(f'''##### ➜ Policies to be prioritised to achieve {dimension[dimension_value]} maximum level''', unsafe_allow_html=True)
            # st.markdown("**➜ Policies to be prioritised to achieve **" + dimension[dimension_value] + "** maximum level**")
            # st.write(leadershipResults['L1S1'][0])
            for key, value in leadershipResults.items():
                if improve_dimension in key:
                    if leadershipResults[key][0] < 1:
                        st.write("🔴" + key + " - " + leadershipPoliciesText[key][0])
                        # st.write(key)
            st.markdown(f'''##### ➜ Additional policies to achieve {dimension[dimension_value+1]} maximum level''', unsafe_allow_html=True)
            # st.write("**➜ Additional policies to achieve **" + dimension[dimension_value+1] + "** maximum level**")
            for key, value in leadershipResults.items():
                if "M" in key:
                    if leadershipResults[key][0] < 1:
                        # st.write(key)
                        st.write("🟠" + key + " - " + leadershipPoliciesText[key][0])

##
# Overview of Policies by years
##
with st.expander("SMR Completeness", expanded=True):
    st.subheader("Cities and SMR Completeness - Leadership & Governance")

    x = [
        ["2022", "2022", "2022",
        "2023", "2023", "2023"],
        ["Donostia - Synthetic data", "Bilbao - Synthetic data", "Pamplona - Synthetic data",
        "Donostia", " Bilbao - Synthetic data", "  Pamplona - Synthetic data"]
    ]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=[3, 4, 3, leadershipCompleteness[0], 5, 4], name='Starting', marker_color = "#ef476f"))
    fig.add_trace(go.Bar(x=x, y=[1, 3, 2, leadershipCompleteness[1], 4, 3], name='Robust', marker_color = "#ffd166"))
    fig.add_trace(go.Bar(x=x, y=[0, 2, 1, leadershipCompleteness[2], 3, 2], name='Advanced', marker_color = "#06d6a0"))
    fig.add_trace(go.Bar(x=x, y=[0, 1, 0, leadershipCompleteness[3], 2, 1], name='Moderate', marker_color = "#118ab2"))
    fig.add_trace(go.Bar(x=x, y=[0, 0, 0, leadershipCompleteness[4], 1, 0], name='Vertebrate', marker_color = "#073b4c"))
    fig.update_layout(barmode="relative")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

# with tab2:
#     st.write('Test')

# with tab3:
#     st.write('Test')

# with tab4:
#     st.write('Test')

# with tab5:
#     st.write('Test')