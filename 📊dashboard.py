import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import data #data to run the formulas
import calc_ans #functions to calculate the answers
import calc_ans_new
from google.oauth2 import service_account
from google.cloud import bigquery


st.set_page_config(layout = "wide",
                   page_title = "SMR Dashboard",
                   page_icon = "📊")

df = pd.read_csv('answers.csv', sep=';')
df = df.replace(np.nan,0)
pd.options.display.float_format = '{:,.0f}'.format
qnt_answers = len(df.index)


# Create API client, Google Cloud Big Query
credentials = service_account.Credentials.from_service_account_info( st.secrets["gcp_service_account"] )
client = bigquery.Client(credentials=credentials)
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows
rows = run_query("SELECT * FROM `answers.answers`")
# Print results.

df_bigquery = pd.DataFrame(rows)

def collecting_results (city, dataframe):

    # df_donostia = df_bigquery.loc[df_bigquery['city'] == 'Donostia']
    dataframe = dataframe.loc[dataframe['city'] == city]
    # df_sevilla = df_bigquery.loc[df_bigquery['city'] == 'Sevilla']

    dataframe['revaluation_period'] = dataframe['revaluation_period'].astype(str).astype(int)
    dataframe = dataframe.sort_values(by='revaluation_period', ascending=False).reset_index()

    dataframe = dataframe[ ['L1Q1', 'L1Q2', 'L1Q3', 'L1Q4', 'L1Q5', 'L2Q1', 'L2Q2', 'L3Q1', 'L3Q2', 'L3Q3', 'L3Q4', 'L3Q5', 'L4Q1', 'L4Q2', 'L4Q3', 'L4Q4', 'L4Q5', 'L4Q6', 'L4Q7',
                                'U1Q1', 'U1Q2', 'U1Q3', 'U1Q4', 'U1Q5', 'U1Q6', 'U1Q7', 'U1Q8', 'U1Q9', 'U1Q10', 'U1Q11', 
                                'E1Q1', 'E1Q2', 'E1Q3', 'E1Q4', 'E1Q5', 'E1Q6', 'E1Q7', 'E1Q8', 'E1Q9', 'E1Q10', 'E1Q11',
                                'revaluation_period'] ]
    dataframe = dataframe.fillna(0)
    return(dataframe)




# df_donostia = df_donostia[ ['L1Q1', 'L1Q2', 'L1Q3', 'L1Q4', 'L1Q5', 'L2Q1', 'L2Q2', 'L3Q1', 'L3Q2', 'L3Q3', 'L3Q4', 'L3Q5', 'L4Q1', 'L4Q2', 'L4Q3', 'L4Q4', 'L4Q5', 'L4Q6', 'L4Q7',
#                             'U1Q1', 'U1Q2', 'U1Q3', 'U1Q4', 'U1Q5', 'U1Q6', 'U1Q7', 'U1Q8', 'U1Q9', 'U1Q10', 'U1Q11', 
#                             'E1Q1', 'E1Q2', 'E1Q3', 'E1Q4', 'E1Q5', 'E1Q6', 'E1Q7', 'E1Q8', 'E1Q9', 'E1Q10', 'E1Q11', 
#                             'revaluation_period'] ]

# df_sevilla = df_sevilla[ ['L1Q1', 'L1Q2', 'L1Q3', 'L1Q4', 'L1Q5', 'L2Q1', 'L2Q2', 'L3Q1', 'L3Q2', 'L3Q3', 'L3Q4', 'L3Q5', 'L4Q1', 'L4Q2', 'L4Q3', 'L4Q4', 'L4Q5', 'L4Q6', 'L4Q7',
#                             'U1Q1', 'U1Q2', 'U1Q3', 'U1Q4', 'U1Q5', 'U1Q6', 'U1Q7', 'U1Q8', 'U1Q9', 'U1Q10', 'U1Q11', 
#                             'E1Q1', 'E1Q2', 'E1Q3', 'E1Q4', 'E1Q5', 'E1Q6', 'E1Q7', 'E1Q8', 'E1Q9', 'E1Q10', 'E1Q11',
#                             'revaluation_period'] ]

# df_donostia += 1
# df_valencia += 1
# df_sevilla += 1

# df_donostia = df_donostia.fillna(0)

# df_sevilla = df_sevilla.fillna(0)



###
###    GENERATING THE CHARTS
###
# GAUGE CHARTS
def gauge_charts (completeness, text, reference):
    match text:
            case "Leadership & Governance":
                starting = [0, 5]
                moderate = [5, 10]
                advanced = [10, 15]
                robust = [15, 20]
                vertebrate = [20, 25]
            case "Preparedness <br> Synthetic data":
                starting = [0, 5]
                moderate = [5, 10]
                advanced = [10, 15]
                robust = [15, 20]
                vertebrate = [20, 25]
            case "Infrastructure & Resources <br> Synthetic data":
                starting = [0, 5]
                moderate = [5, 10]
                advanced = [10, 15]
                robust = [15, 20]
                vertebrate = [20, 25]
            case "Cooperation <br> Synthetic data":
                starting = [0, 5]
                moderate = [5, 10]
                advanced = [10, 15]
                robust = [15, 20]
                vertebrate = [20, 25]
            case "Urban Development <br>& Environmental":
                starting = [0, 5]
                moderate = [5, 10]
                advanced = [10, 15]
                robust = [15, 20]
                vertebrate = [20, 25]
            case _:
                print("error")
    fig = go.Figure(go.Indicator(
        domain = {'x': [0, 1], 'y': [0, 1]},
        value = completeness,
        mode = "gauge",
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


# RADAR CHARTS
def transform_radar_leadership(dataframe):
    df_radar_previous_L1 = [dataframe[0]['L1Q1'].mean(),dataframe[0]['L1Q2'].mean(),dataframe[0]['L1Q3'].mean(),
                            dataframe[0]['L1Q4'].mean(),dataframe[0]['L1Q5'].mean()]
    df_radar_previous_L2 = [dataframe[0]['L2Q1'].mean(),dataframe[0]['L2Q2'].mean()] 
    df_radar_previous_L3 = [dataframe[0]['L3Q1'].mean(),dataframe[0]['L3Q2'].mean(),dataframe[0]['L3Q3'].mean(),
                            dataframe[0]['L3Q4'].mean(),dataframe[0]['L3Q5'].mean()]
    df_radar_previous_L4 = [dataframe[0]['L4Q1'].mean(),dataframe[0]['L4Q2'].mean(),dataframe[0]['L4Q3'].mean(),
                            dataframe[0]['L4Q4'].mean(),dataframe[0]['L4Q5'].mean(),dataframe[0]['L4Q6'].mean(),
                            dataframe[0]['L4Q7'].mean()]
    return df_radar_previous_L1, df_radar_previous_L2, df_radar_previous_L3, df_radar_previous_L4

def transform_radar_urban(dataframe):
    df_radar_previous_U1 = [dataframe[0]['U1Q1'].mean(), dataframe[0]['U1Q2'].mean(), dataframe[0]['U1Q3'].mean(), 
                            dataframe[0]['U1Q4'].mean(), dataframe[0]['U1Q5'].mean(), dataframe[0]['U1Q6'].mean(), 
                            dataframe[0]['U1Q7'].mean(), dataframe[0]['U1Q8'].mean(), dataframe[0]['U1Q9'].mean(),
                            dataframe[0]['U1Q10'].mean(), dataframe[0]['U1Q11'].mean()]
    df_radar_previous_E1 = [dataframe[0]['E1Q1'].mean(), dataframe[0]['E1Q2'].mean(), dataframe[0]['E1Q3'].mean(), 
                            dataframe[0]['E1Q4'].mean(), dataframe[0]['E1Q5'].mean(), dataframe[0]['E1Q6'].mean(), 
                            ((dataframe[0]['E1Q7'].mean() + dataframe[0]['E1Q8'].mean() + dataframe[0]['E1Q9'].mean() + dataframe[0]['E1Q10'].mean())/4),
                            dataframe[0]['E1Q11'].mean()]
    return df_radar_previous_U1, df_radar_previous_E1

def returningbest(best, categories, bestname, linecolor):
    test = go.Scatterpolar(r=best, theta=categories, fill='toself', name=bestname, line_color = linecolor)
    return test

def checking_quantity_of_layers (size, best, score, categories, df_radar_previous):
    if size == 2:
            data = [            
                returningbest(best,categories,'best','#2C3639'),
                returningbest(score,categories,'score','#D04848')]
    elif size == 3: 
            data = [            
                returningbest(best,categories,'best','#2C3639'),
                returningbest(df_radar_previous,categories,'previous result','#ffb400'),
                returningbest(score,categories,'score','#D04848'),]
    return data

def radar_charts (categories, best, score, text, df_radar_previous, trigger_new_cities):
    categories = [*categories, categories[0]]
    best = [*best, best[0]]
    score = [*score, score[0]]
    if trigger_new_cities == True:
        size = 3
    else:
        size = 2
        df_radar_previous = None
    fig = go.Figure(
            checking_quantity_of_layers(size, best, score, categories, df_radar_previous),
        layout=go.Layout(
            title=go.layout.Title(text=text),
            polar={'radialaxis': {'visible': True}},
            showlegend=True))

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", title_x=0, margin= dict(l=30,r=30,b=50,t=50))
    return fig

# LINE CHARTS
def line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prev, trigger_new_cities):
    fig = go.Figure()
    fig.add_trace(go.Bar(y=dimension, x=valueBestDimension, name='Best Accomplishment', orientation='h',
                             marker=dict(color='#e2e2e2', line=dict(color='rgba(58, 71, 80, 1.0)', width=1))))
        
    fig.add_trace(go.Bar(y=dimension, x=valueCapturedCompleteness, name='Captured Completeness', orientation='h',
                             marker=dict(color='#ffb400', line=dict(color='#4C3A51', width=1))))

    if trigger_new_cities == True:
        fig.add_trace(go.Bar(y=dimension, x=valueCapturedCompleteness_prev, name='Captured Completeness Previous', orientation='h',
                             marker=dict(color='#D04848', line=dict(color='#D04848', width=1))))

    fig.update_layout(title = title, barmode='overlay', title_x=0,
                          legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                          margin= dict(l=30,r=30,b=50,t=50))
    return fig

###
###    STREAMLIT LEFT PANNEL
###
# SELECTION CITY AND DIMENSION
with st.sidebar:
    # city = st.selectbox(
    #     'Select city',
    #     ("Donostia", "Sevilla", "Valencia"))
    trigger = False  
    trigger_new_cities = False  
    questionnaire = st.selectbox(
        'Select the option',
        ('Donostia (16/03/23)',
         'Donostia',
         'Sevilla',
         'Valencia'
         ))

    match questionnaire:
        case "Donostia (16/03/23)":
            df_pol = df.iloc[0]
        case "Donostia":
            trigger_new_cities = True
            df_pol = collecting_results("Donostia", df_bigquery)
            if len(df_pol) > 1:
                df_pol_actualmonth = (df_pol.iloc[[0]]).astype(int)
                df_pol_previousmonth = (df_pol.iloc[[1]]).astype(int)
                trigger = True
        case "Sevilla":
            trigger_new_cities = True
            df_pol = collecting_results("Sevilla", df_bigquery)
            if len(df_pol) > 1:
                df_pol_actualmonth = (df_pol.iloc[[0]]).astype(int)
                df_pol_previousmonth = (df_pol.iloc[[1]]).astype(int)
                trigger = True
        case "Valencia":
            trigger_new_cities = True
            df_pol = collecting_results("Valencia", df_bigquery)
            if len(df_pol) > 1:
                df_pol_actualmonth = (df_pol.iloc[[0]]).astype(int).reset_index(drop=True)
                df_pol_actualmonth = df_pol_actualmonth.T
                df_pol_previousmonth = (df_pol.iloc[[1]]).astype(int).reset_index(drop=True)
                df_pol_previousmonth = df_pol_previousmonth.T
                trigger = True
        case _:
            print("error")
    
    

    if trigger == False:
        leadershipResults, leadershipCompleteness = calc_ans.Leadership(df_pol, data.dfL1Best, data.dfL2Best, data.dfL3Best, data.dfL4Best)
        preparednessResults, preparednessCompleteness = calc_ans.Preparedness(df_pol, data.dfP1Best, data.dfP2Best)
        infraResults, infraCompleteness = calc_ans.Infra(df_pol, data.dfI1Best, data.dfI2Best)
        cooperationResults, cooperationCompleteness = calc_ans.Cooperation(df_pol, data.dfC1Best, data.dfC2Best)
        urbanResults, urbanCompleteness = calc_ans.Urban(df_pol, data.dfU1Best, data.dfE1Best)
    else:
        # df_pol_previousmonth
        print(df_pol_previousmonth)
        leadershipResults_prev, leadershipCompleteness_prev = calc_ans_new.Leadership(df_pol_previousmonth, data.dfL1Best, data.dfL2Best, data.dfL3Best, data.dfL4Best)
        preparednessResults_prev, preparednessCompleteness_prev = calc_ans_new.Preparedness(df_pol_previousmonth, data.dfP1Best, data.dfP2Best)
        infraResults_prev, infraCompleteness_prev = calc_ans_new.Infra(df_pol_previousmonth, data.dfI1Best, data.dfI2Best)
        cooperationResults_prev, cooperationCompleteness_prev = calc_ans_new.Cooperation(df_pol_previousmonth, data.dfC1Best, data.dfC2Best)
        urbanResults_prev, urbanCompleteness_prev = calc_ans_new.Urban(df_pol_previousmonth, data.dfU1Best, data.dfE1Best)
        # df_pol_actualmonth
        leadershipResults, leadershipCompleteness = calc_ans_new.Leadership(df_pol_actualmonth, data.dfL1Best, data.dfL2Best, data.dfL3Best, data.dfL4Best)
        preparednessResults, preparednessCompleteness = calc_ans_new.Preparedness(df_pol_actualmonth, data.dfP1Best, data.dfP2Best)
        infraResults, infraCompleteness = calc_ans_new.Infra(df_pol_actualmonth, data.dfI1Best, data.dfI2Best)
        cooperationResults, cooperationCompleteness = calc_ans_new.Cooperation(df_pol_actualmonth, data.dfC1Best, data.dfC2Best)
        urbanResults, urbanCompleteness = calc_ans_new.Urban(df_pol_actualmonth, data.dfU1Best, data.dfE1Best)

###
###    DASHBOARD GENERATION
###
title1, title2 = st.columns((0.11,1)) 
with title1:
    st.image('logo_smr.png', width = 120)
with title2:
    st.title('SMR Dashboard - ' + questionnaire)

st.write("test")
st.write("test")
st.write("test")
st.write("test")
st.write("test")
###
###    POLICIES COMPLETENESS IN GENERAL - GAUGE CHARTS
###
st.subheader("SMR Completeness")
sec5_col1, sec5_col2, sec5_col3, sec5_col4, sec5_col5 = st.columns([1,1,1,1,1])

#GAUGE 1 - Leadership & Governance
completenessLeadership = sum(leadershipCompleteness)
if leadershipCompleteness[0] < 5:
    valueLeadership = leadershipCompleteness[0]
elif leadershipCompleteness[1] < 8:
    valueLeadership = leadershipCompleteness[1] + leadershipCompleteness[0]
elif leadershipCompleteness[2] < 7:
    valueLeadership = leadershipCompleteness[2] + leadershipCompleteness[1] + leadershipCompleteness[0]
elif leadershipCompleteness[3] < 4:
    valueLeadership = leadershipCompleteness[3] + leadershipCompleteness[2] + leadershipCompleteness[1] + leadershipCompleteness[0]
elif leadershipCompleteness[4] <= 5:
    valueLeadership = leadershipCompleteness[4] + leadershipCompleteness[3] + leadershipCompleteness[2] + leadershipCompleteness[1] + leadershipCompleteness[0]
text = 'Leadership & Governance'
reference = 25
fig1 = gauge_charts(valueLeadership, text, reference)
sec5_col1.plotly_chart(fig1, use_container_width=True)

#GAUGE 2 - Preparedness
completenessPreparedness = preparednessCompleteness
text = 'Preparedness <br> Synthetic data'
reference = 25
fig2 = gauge_charts(completenessPreparedness, text, reference)
sec5_col2.plotly_chart(fig2, use_container_width=True)

#GAUGE 3 - Infrastructure & Resources
completenessInfra = infraCompleteness
text = 'Infrastructure & Resources <br> Synthetic data'
reference = 25
fig3 = gauge_charts(completenessInfra, text, reference)
sec5_col3.plotly_chart(fig3, use_container_width=True)

#GAUGE 4 - Cooperation
completenessCooperation = cooperationCompleteness
text = 'Cooperation <br> Synthetic data'
reference = 25
fig4 = gauge_charts(completenessCooperation, text, reference)
sec5_col4.plotly_chart(fig4, use_container_width=True)

#GAUGE 5 - Urban Development & Environmental
completenessUrban = sum(urbanCompleteness)
valueUrban = 0
if urbanCompleteness[0] < 5:
    valueUrban = urbanCompleteness[0]
elif urbanCompleteness[1] < 8:
    valueUrban = urbanCompleteness[1] + urbanCompleteness[0]
elif urbanCompleteness[2] < 6:
    valueUrban = urbanCompleteness[2] + urbanCompleteness[1] + urbanCompleteness[0]
elif urbanCompleteness[3] < 3:
    valueUrban = urbanCompleteness[3] + urbanCompleteness[2] + urbanCompleteness[1] + urbanCompleteness[0]
elif urbanCompleteness[4] <= 1:
    valueUrban = urbanCompleteness[4] + urbanCompleteness[3] + urbanCompleteness[2] + urbanCompleteness[1] + urbanCompleteness[0]
text = 'Urban Development <br>& Environmental'
reference = 25
fig5 = gauge_charts(valueUrban, text, reference)
sec5_col5.plotly_chart(fig5, use_container_width=True)

## Line with the maturity levels range
fig = go.Figure()
# Create scatter trace of text labels
config = {'staticPlot': True}
fig.add_trace(go.Scatter(
    x=[0.5, 1.5, 2.5, 3.5, 4.5],
    y=[1.4, 1.4, 1.4, 1.4, 1.4],
    text=["STARTING",
          "MODERATE",
          "ADVANCED",
          "ROBUST",
          "VERTEBRATE"],
    mode="text",
))
# Set axes properties
fig.update_xaxes(range=[0, 5])
fig.update_yaxes(range=[0, 2])
# Add shapes
fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=0, y0=0,
    x1=1, y1=1,
    fillcolor="#ef476f",)

fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=1, y0=0,
    x1=2, y1=1,
    fillcolor="#ffd166",)

fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=2, y0=0,
    x1=3, y1=1,
    fillcolor="#06d6a0",)

fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=3, y0=0,
    x1=4, y1=1,
    fillcolor="#118ab2",)

fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=4, y0=0,
    x1=5, y1=1,
    fillcolor="#073b4c",)

fig.update_layout(
    autosize=False,
    width=70,
    height=70,
    font=dict(size=18),
    yaxis_visible=False, yaxis_showticklabels=False,
    margin= dict(l=0,r=0,b=0,t=0),
    plot_bgcolor =  'rgba(0,0,0,0)',
    paper_bgcolor =  'rgba(0,0,0,0)'
)
st.plotly_chart(fig, use_container_width=True, config=config)


# tab1, tab2, tab3, tab4, tab5 = st.tabs(['Leadership & Governance', 'Preparedness', 'Cooperation','Infrastructure & Resources', 'Urban Development & Environmental'])
tab1, tab2, = st.tabs(['Leadership & Governance', 'Urban Development & Environmental'])
###
###    LEADERSHIP & GOVERNANCE DASHBOARD
###
with tab1:
    ##
    # RADAR CHARTS
    ##
    with st.expander('Questions Performance Analysis', expanded=True):
        st.subheader('Questions Performance Analysis - Leadership & Governance')
        col1, col2 = st.columns([1,1])
        # RADAR L1

        if trigger_new_cities == True:
            score_L1, score_L2, score_L3, score_L4 = transform_radar_leadership(df_pol_actualmonth)
            df_radar_previous_L1, df_radar_previous_L2, df_radar_previous_L3, df_radar_previous_L4 = transform_radar_leadership(df_pol_previousmonth)
            score = 0
        
        else:
            df_radar = df_pol
            df_radar_previous_L1= df_radar_previous_L2= df_radar_previous_L3= df_radar_previous_L4 = 0
            score_L1 = [df_radar['L1Q1'].mean(),df_radar['L1Q2'].mean(),df_radar['L1Q3'].mean(),df_radar['L1Q4'].mean(),df_radar['L1Q5'].mean()]
            score_L2 = [df_radar['L2Q1'].mean(), df_radar['L2Q2'].mean()]
            score_L3 = [df_radar['L3Q1'].mean(), df_radar['L3Q2'].mean(), df_radar['L3Q3'].mean(), df_radar['L3Q4'].mean(), df_radar['L3Q5'].mean()]
            score_L4 = [df_radar['L4Q1'].mean(), df_radar['L4Q2'].mean(), df_radar['L4Q3'].mean(), df_radar['L4Q4'].mean(), df_pol['L4Q5'].mean(), df_radar['L4Q6'].mean(), df_radar['L4Q7'].mean()]

        categories = ['Resilience<br>Governance', 'Development<br>of<br>RAP', 'RAP<br>Integration', 'Access to basic services', 'Support to other cities']
        best = [4, 4, 4, 4, 4]
        text='Leadership & Governance (L1)'
        fig1 = radar_charts(categories, best, score_L1, text, df_radar_previous_L1, trigger_new_cities)
        col1.plotly_chart(fig1, use_container_width=True)

        # RADAR L2
        categories = ['Standards<br>Alignment', 'Certification<br>Processes']
        best = [4, 4] 
        text='Leadership & Governance (L2)'
        fig2 = radar_charts(categories, best, score_L2, text, df_radar_previous_L2, trigger_new_cities)
        col2.plotly_chart(fig2, use_container_width=True)

        col3, col4 = st.columns([1,1])
        # RADAR L3
        categories = ['Resilience<br>Culture', 'Lessons<br>Past Events', 'Knowledge<br>Sharing', 'Learning<br>Process', 'Learning Process<br>Assessment']
        best = [4, 4, 4, 4, 4]
        text='Leadership & Governance (L3)'
        fig3 = radar_charts(categories, best, score_L3, text, df_radar_previous_L3, trigger_new_cities)
        col3.plotly_chart(fig3, use_container_width=True)

        # RADAR L4
        categories = ['Disaster Response<br>Plan', 'RAP Plan<br>Development', 'Stakeholders<br>Collaboration', 'Disaster<br>Focus', 'Climate Change<br>Perspective', 'Resilience Adoption<br>and Integration', 'Collaboration and Networking with<br>Cities and External Bodies']
        best = [4, 4, 4, 4, 4, 4, 4]
        text='Leadership & Governance (L4)'
        fig4 = radar_charts(categories, best, score_L4, text, df_radar_previous_L4, trigger_new_cities)
        col4.plotly_chart(fig4, use_container_width=True)

    ###
    ###    POLICIES
    ###
    with st.expander('Completeness', expanded=True):
        st.subheader('Completeness - Leadership & Governance')

        linegraphView = st.selectbox('Select the view - To see the recommendations select "SMART Completeness (All subdimensions) + Policies Recommendations"',
        ('Policies Completeness','SMART Completeness (Each subdimension)','SMART Completeness (All subdimensions) + Policies Recommendations'))
        
        if linegraphView == 'Policies Completeness':
            sec4_col1,sec4_col2 = st.columns([1,1])
            if trigger_new_cities == True:
                valueCapturedCompleteness_prevL1 = [leadershipResults_prev['L1S1'][0], leadershipResults_prev['L1S2'][0],
                                                    leadershipResults_prev['L1M1'][0], leadershipResults_prev['L1M2'][0], leadershipResults_prev['L1M3'][0],
                                                    leadershipResults_prev['L1A1'][0], leadershipResults_prev['L1A2'][0],
                                                    leadershipResults_prev['L1R2'][0], leadershipResults_prev['L1T2'][0]]
                valueCapturedCompleteness_prevL2 = [leadershipResults_prev['L2M1'][0], leadershipResults_prev['L2A1'][0], leadershipResults_prev['L2R1'][0], leadershipResults_prev['L2T1'][0]]
                valueCapturedCompleteness_prevL3 = [leadershipResults_prev['L3S1'][0],
                                                    leadershipResults_prev['L3M1'][0], leadershipResults_prev['L3M2'][0],
                                                    leadershipResults_prev['L3A2'][0],
                                                    leadershipResults_prev['L3R2'][0],
                                                    leadershipResults_prev['L3T1'][0], leadershipResults_prev['L3T2'][0]]
                valueCapturedCompleteness_prevL4 = [leadershipResults_prev['L4S1'][0], leadershipResults_prev['L4S2'][0],
                                                    leadershipResults_prev['L4M2'][0], leadershipResults_prev['L4M3'][0],
                                                    leadershipResults_prev['L4A1'][0], leadershipResults_prev['L4A2'][0], leadershipResults_prev['L4A4'][0],
                                                    leadershipResults_prev['L4T3'][0]]
            else:
                valueCapturedCompleteness_prevL1 = valueCapturedCompleteness_prevL2 = valueCapturedCompleteness_prevL3 = valueCapturedCompleteness_prevL4 = 0

            ## LINE CHART L1
            dimension = ['L1S1','L1S2','L1M1','L1M2','L1M3','L1A1','L1A2','L1R2','L1T2']
            valueBestDimension = [1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L1S1'][0], leadershipResults['L1S2'][0], 
                                        leadershipResults['L1M1'][0], leadershipResults['L1M2'][0], leadershipResults['L1M3'][0], 
                                        leadershipResults['L1A1'][0], leadershipResults['L1A2'][0], 
                                        leadershipResults['L1R2'][0], leadershipResults['L1T2'][0]]
            title = 'All Policies - L1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL1, trigger_new_cities)
            sec4_col1.plotly_chart(fig1, use_container_width=True)
            
            ## LINE CHART L2
            dimension = ['L2M1','L2A1','L2R1','L2T1']
            valueBestDimension = [1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L2M1'][0], leadershipResults['L2A1'][0], leadershipResults['L2R1'][0], leadershipResults['L2T1'][0]]
            title = 'All Policies - L2'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL2, trigger_new_cities)
            sec4_col2.plotly_chart(fig2, use_container_width=True)

            sec4_col3, sec4_col4 = st.columns([1,1])
            ## LINE CHART L3
            dimension = ['L3S1','L3M1','L3M2','L3A2','L3R2','L3T1','L3T2']
            valueBestDimension = [1,1,1,1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L3S1'][0],
                                        leadershipResults['L3M1'][0], leadershipResults['L3M2'][0],
                                        leadershipResults['L3A2'][0],
                                        leadershipResults['L3R2'][0],
                                        leadershipResults['L3T1'][0], leadershipResults['L3T2'][0]]
            title = 'All Policies - L3'
            fig3 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL3, trigger_new_cities)
            sec4_col3.plotly_chart(fig3, use_container_width=True)

            # LINE CHART L4
            dimension = ['L4S1','L4S2','L4M2','L4M3','L4A1','L4A2','L4A4','L4R2','L4T3']
            valueBestDimension = [1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L4S1'][0], leadershipResults['L4S2'][0],
                                        leadershipResults['L4M2'][0], leadershipResults['L4M3'][0],
                                        leadershipResults['L4A1'][0], leadershipResults['L4A2'][0], leadershipResults['L4A4'][0],
                                        leadershipResults['L4R2'][0],
                                        leadershipResults['L4T3'][0]]
            title = 'All Policies - L4'
            fig4 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL4, trigger_new_cities)
            sec4_col4.plotly_chart(fig4, use_container_width=True)
        

        ###
        ###    SMART COMPLETENESS (EACH SUBDIMENSION)
        ###
        elif linegraphView == 'SMART Completeness (Each subdimension)':
            if trigger_new_cities == True:
                valueCapturedCompleteness_prevL1 = [(leadershipResults_prev['L1S1'][0] + leadershipResults_prev['L1S2'][0])/2,
                                                    (leadershipResults_prev['L1M1'][0] + leadershipResults_prev['L1M2'][0] + leadershipResults_prev['L1M3'][0])/3,
                                                    (leadershipResults_prev['L1A1'][0] + leadershipResults_prev['L1A2'][0])/2,
                                                    leadershipResults_prev['L1R2'][0],
                                                    leadershipResults_prev['L1T2'][0]]
                valueCapturedCompleteness_prevL2 = [leadershipResults_prev['L2M1'][0], leadershipResults_prev['L2A1'][0], leadershipResults_prev['L2R1'][0], leadershipResults_prev['L2T1'][0]]
                valueCapturedCompleteness_prevL3 = [leadershipResults_prev['L3S1'][0],
                                                    (leadershipResults_prev['L3M1'][0] + leadershipResults_prev['L3M2'][0])/2,
                                                    leadershipResults_prev['L3A2'][0],
                                                    leadershipResults_prev['L3R2'][0],
                                                    (leadershipResults_prev['L3T1'][0] + leadershipResults_prev['L3T2'][0])/2]
                valueCapturedCompleteness_prevL4 = [(leadershipResults_prev['L4S1'][0] + leadershipResults_prev['L4S2'][0])/2,
                                                    (leadershipResults_prev['L4M2'][0] + leadershipResults_prev['L4M3'][0])/2,
                                                    (leadershipResults_prev['L4A1'][0] + leadershipResults_prev['L4A2'][0] + leadershipResults_prev['L4A4'][0])/3,
                                                    leadershipResults_prev['L4R2'][0],
                                                    leadershipResults_prev['L4T3'][0], ]
            else:
                valueCapturedCompleteness_prevL1 = valueCapturedCompleteness_prevL2 = valueCapturedCompleteness_prevL3 = valueCapturedCompleteness_prevL4 = 0

            sec4_col1,sec4_col2 = st.columns([1,1])

            ## LINE GRAPH L1
            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(leadershipResults['L1S1'][0] + leadershipResults['L1S2'][0])/2, 
                                        (leadershipResults['L1M1'][0] + leadershipResults['L1M2'][0] + leadershipResults['L1M3'][0])/3, 
                                        (leadershipResults['L1A1'][0] + leadershipResults['L1A2'][0])/2, 
                                        leadershipResults['L1R2'][0],
                                        leadershipResults['L1T2'][0]]
            title = 'All Policies - L1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL1, trigger_new_cities)
            sec4_col1.plotly_chart(fig1, use_container_width=True)

            ## LINE CHART L2
            dimension = ['Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L2M1'][0], leadershipResults['L2A1'][0], leadershipResults['L2R1'][0], leadershipResults['L2T1'][0]]
            title = 'All Policies - L2'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL2, trigger_new_cities)
            sec4_col2.plotly_chart(fig2, use_container_width=True)

            sec4_col3, sec4_col4 = st.columns([1,1])
            ## LINE CHART L3
            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L3S1'][0],
                                        (leadershipResults['L3M1'][0] + leadershipResults['L3M2'][0])/2,
                                        leadershipResults['L3A2'][0],
                                        leadershipResults['L3R2'][0],
                                        (leadershipResults['L3T1'][0] + leadershipResults['L3T2'][0])/2]
            title = 'All Policies - L3'
            fig3 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL3, trigger_new_cities)
            sec4_col3.plotly_chart(fig3, use_container_width=True)

            # LINE CHART L4
            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(leadershipResults['L4S1'][0] + leadershipResults['L4S2'][0])/2,
                                        (leadershipResults['L4M2'][0] + leadershipResults['L4M3'][0])/2,
                                        (leadershipResults['L4A1'][0] + leadershipResults['L4A2'][0] + leadershipResults['L4A4'][0])/3,
                                        leadershipResults['L4R2'][0],
                                        leadershipResults['L4T3'][0], ]
            title = 'All Policies - L4'
            fig4 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL4, trigger_new_cities)
            sec4_col4.plotly_chart(fig4, use_container_width=True)

        ###
        ###    SMART COMPLETENESS (ALL SUBDIMENSIONS) + POLICIES RECOMMENDATIONS
        ###
        elif linegraphView == 'SMART Completeness (All subdimensions) + Policies Recommendations':
            if trigger_new_cities == True:
                valueCapturedCompleteness_prevL = [(leadershipResults_prev['L1S1'][0] + leadershipResults_prev['L1S2'][0] + leadershipResults_prev['L3S1'][0] + leadershipResults_prev['L4S1'][0] + leadershipResults_prev['L4S2'][0])/5,
                                             (leadershipResults_prev['L1M1'][0] + leadershipResults_prev['L1M2'][0] + leadershipResults_prev['L1M3'][0] + leadershipResults_prev['L2M1'][0] + leadershipResults_prev['L3M1'][0] + leadershipResults_prev['L3M2'][0] + leadershipResults_prev['L4M2'][0] + leadershipResults_prev['L4M3'][0])/8,
                                             (leadershipResults_prev['L1A1'][0] + leadershipResults_prev['L1A2'][0] + leadershipResults_prev['L2A1'][0] + leadershipResults_prev['L3A2'][0] + leadershipResults_prev['L4A1'][0] + leadershipResults_prev['L4A2'][0] + leadershipResults_prev['L4A4'][0])/7,
                                             (leadershipResults_prev['L1R2'][0] + leadershipResults_prev['L2R1'][0] + leadershipResults_prev['L3R2'][0] + leadershipResults_prev['L4R2'][0])/4,
                                             (leadershipResults_prev['L1T2'][0] + leadershipResults_prev['L2T1'][0] + leadershipResults_prev['L3T1'][0] + leadershipResults_prev['L3T2'][0] + leadershipResults_prev['L4T3'][0])/5]


            else:
                valueCapturedCompleteness_prevL = 0

            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(leadershipResults['L1S1'][0] + leadershipResults['L1S2'][0] + leadershipResults['L3S1'][0] + leadershipResults['L4S1'][0] + leadershipResults['L4S2'][0])/5,
                                        (leadershipResults['L1M1'][0] + leadershipResults['L1M2'][0] + leadershipResults['L1M3'][0] + leadershipResults['L2M1'][0] + leadershipResults['L3M1'][0] + leadershipResults['L3M2'][0] + leadershipResults['L4M2'][0] + leadershipResults['L4M3'][0])/8,
                                        (leadershipResults['L1A1'][0] + leadershipResults['L1A2'][0] + leadershipResults['L2A1'][0] + leadershipResults['L3A2'][0] + leadershipResults['L4A1'][0] + leadershipResults['L4A2'][0] + leadershipResults['L4A4'][0])/7,
                                        (leadershipResults['L1R2'][0] + leadershipResults['L2R1'][0] + leadershipResults['L3R2'][0] + leadershipResults['L4R2'][0])/4,
                                        (leadershipResults['L1T2'][0] + leadershipResults['L2T1'][0] + leadershipResults['L3T1'][0] + leadershipResults['L3T2'][0] + leadershipResults['L4T3'][0])/5]
            title = 'All Policies'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevL, trigger_new_cities)
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
                actual_policy = ""
                st.markdown(f'''##### ➜ Policies to be prioritised to achieve {dimension[dimension_value]} maximum level''', unsafe_allow_html=True)
                # st.markdown("**➜ Policies to be prioritised to achieve **" + dimension[dimension_value] + "** maximum level**")
                for key, value in leadershipResults.items():
                    if improve_dimension in key:
                        if leadershipResults[key][0] < 1:
                            st.write("🔴" + key + " - " + data.leadershipPoliciesText[key][0])
                            actual_policy = key
                st.markdown(f'''##### ➜ Additional policies to achieve {dimension[dimension_value+1]} maximum level''', unsafe_allow_html=True)
                # st.write("**➜ Additional policies to achieve **" + dimension[dimension_value+1] + "** maximum level**")

                for key, value in leadershipResults.items():
                    if "S" in actual_policy:
                        if "M" in key:
                            if leadershipResults[key][0] < 1:
                                st.write("🟠" + key + " - " + data.leadershipPoliciesText[key][0])
                    if "M" in actual_policy:
                        if "A" in key:
                            if leadershipResults[key][0] < 1:
                                st.write("🟠" + key + " - " + data.leadershipPoliciesText[key][0])
                    if "A" in actual_policy:
                        if "R" in key:
                            if leadershipResults[key][0] < 1:
                                st.write("🟠" + key + " - " + data.leadershipPoliciesText[key][0])
                    if "T" in actual_policy:
                        st.write("No policies to achieve")
            else:
                st.markdown(f'''##### There is no policies to be achieved''', unsafe_allow_html=True)

    ##
    # Overview of Policies by years
    ##
    with st.expander("SMR Completeness", expanded=True):
        st.subheader("Cities and SMR Completeness - Urban Development & Environmental")

        x = [
            ["2022", "2022", "2022",
            "2023", "2023", "2023"],
            ["Donostia - Synthetic data", "Sevilla - Synthetic data", "Valencia - Synthetic data",
            "Donostia", "  Sevilla - Synthetic data", "  Valencia - Synthetic data"]
        ]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=[3, 4, 3, urbanCompleteness[0], 5, 4], name='Starting', marker_color = "#ef476f"))
        fig.add_trace(go.Bar(x=x, y=[1, 3, 2, urbanCompleteness[1], 4, 3], name='Robust', marker_color = "#ffd166"))
        fig.add_trace(go.Bar(x=x, y=[0, 2, 1, urbanCompleteness[2], 3, 2], name='Advanced', marker_color = "#06d6a0"))
        fig.add_trace(go.Bar(x=x, y=[0, 1, 0, urbanCompleteness[3], 2, 1], name='Moderate', marker_color = "#118ab2"))
        fig.add_trace(go.Bar(x=x, y=[0, 0, 0, urbanCompleteness[4], 1, 0], name='Vertebrate', marker_color = "#073b4c"))
        fig.update_layout(barmode="relative")
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

with tab2:
    ##
    # RADAR GRAPHS
    ##

    with st.expander('Questions Performance Analysis', expanded=True):

        if trigger_new_cities == True:
            score_U1, score_E1= transform_radar_urban(df_pol_actualmonth)
            df_radar_previous_U1, df_radar_previous_E1 = transform_radar_urban(df_pol_previousmonth)
            score = 0
        
        else:
            df_radar = df_pol
            df_radar_previous_U1 = df_radar_previous_E1 = 0
            score_U1 = [df_radar['U1Q1'].mean(), df_radar['U1Q2'].mean(), df_radar['U1Q3'].mean(), 
                        df_radar['U1Q4'].mean(), df_radar['U1Q5'].mean(), df_radar['U1Q6'].mean(), 
                        df_radar['U1Q7'].mean(), df_radar['U1Q8'].mean(), df_radar['U1Q9'].mean(),
                        df_radar['U1Q10'].mean(), df_radar['U1Q11'].mean()]
            score_E1 = [df_radar['E1Q1'].mean(), df_radar['E1Q2'].mean(), df_radar['E1Q3'].mean(),
                         df_radar['E1Q4'].mean(), df_radar['E1Q5'].mean(), df_radar['E1Q6'].mean(), 
                         ((df_radar['E1Q7'].mean() + df_radar['E1Q8'].mean() + df_radar['E1Q9'].mean() + df_radar['E1Q10'].mean())/4),
                         df_radar['E1Q11'].mean()]
        
        st.subheader('Questions Performance Analysis - Urban Development & Environmental')
        col1, col2 = st.columns([1,1])
        # RADAR U1
        categories = ['Adaptation Measures in Urban Planning', 
                      'Adaptation Measures in Urban Development',
                      'Plans to Implement CC Adaptation Measures', 
                      'Monitoring and Evaluation of the CC Adaptation Measures',
                      'NBSs Identification',
                      'NBSs Implementation',
                      'Climate Information to Support Decision Making',
                      'Building Regulations and Standards',
                      'Guideline for Sustainable and Resilient Urban Planning',
                      'Sustainable Design and Risk Reduction Measures in Buildings',
                      'Sustainable Design and Development of Urban Mobility and Public Services',]
        best = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        text='Urban Development & Environmental (U1)'
        fig1 = radar_charts(categories, best, score_U1, text, df_radar_previous_U1, trigger_new_cities)
        col1.plotly_chart(fig1, use_container_width=True)
    
        # RADAR E1
        categories = ['Assessment of the ecosystem and biodiversity', 
                      'Awareness', 
                      'Promotion and establishment of transboundary agreements and collaborations',
                      'Protection and restoration of important ecosystems',
                      'Definition of Targets for GHG reduction till 2050',
                      'Establish plans to favor the implementation of climate change mitigation actions',
                      'Climate change mitigation',
                      'Monitoring and evaluation of the climate change mitigation measures']
        best = [4, 4, 4, 4, 4, 4, 4, 4]
        text='Urban Development & Environmental (E1)'
        fig2 = radar_charts(categories, best, score_E1, text, df_radar_previous_E1, trigger_new_cities)
        col2.plotly_chart(fig2, use_container_width=True)
    ##
    # Policies
    ##
    with st.expander('Completeness', expanded=True):
        st.subheader('Completeness - Urban Development & Environmental')

        linegraphView = st.selectbox('Select the view - To see the recommendations select "SMART Completeness (All subdimensions) + Policies Recommendations"',
        ('Policies Completeness ','SMART Completeness (Each subdimension) ','SMART Completeness (All subdimensions) + Policies Recommendations'))

        if linegraphView == 'Policies Completeness ':
            if trigger_new_cities == True:
                valueCapturedCompleteness_prevU1 = [urbanResults_prev['U1S1'][0], urbanResults_prev['U1S3'][0], urbanResults_prev['U1S4'][0],
                                                    urbanResults_prev['U1M1'][0], urbanResults_prev['U1M2'][0], urbanResults_prev['U1M3'][0], urbanResults_prev['U1M4'][0], urbanResults_prev['U1M5'][0], urbanResults_prev['U1M6'][0],
                                                    urbanResults_prev['U1A1'][0], urbanResults_prev['U1A2'][0], 
                                                    urbanResults_prev['U1R1'][0]]
                valueCapturedCompleteness_prevE1 = [urbanResults_prev['E1S1'][0], urbanResults_prev['E1S3'][0],
                                                    urbanResults_prev['E1M2'][0], urbanResults_prev['E1M3'][0],
                                                    urbanResults_prev['E1A1'][0], urbanResults_prev['E1A2'][0], urbanResults_prev['E1A3'][0],
                                                    urbanResults_prev['E1R2'][0], urbanResults_prev['E1R3'][0], urbanResults_prev['E1A4'][0],
                                                    urbanResults_prev['E1T1'][0]]
            else:
                valueCapturedCompleteness_prevU1 = valueCapturedCompleteness_prevE1 = 0
            sec4_col1,sec4_col2 = st.columns([1,1])

            ## LINE GRAPH U1
            dimension = ['U1S1', 'U1S3', 'U1S4', 'U1M1', 'U1M2', 'U1M3', 'U1M4', 'U1M5', 'U1M6', 'U1A1', 'U1A2', 'U1R1']
            valueBestDimension = [1,1,1,1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [urbanResults['U1S1'][0], urbanResults['U1S3'][0], urbanResults['U1S4'][0],
                                        urbanResults['U1M1'][0], urbanResults['U1M2'][0], urbanResults['U1M3'][0], urbanResults['U1M4'][0], urbanResults['U1M5'][0], urbanResults['U1M6'][0],
                                        urbanResults['U1A1'][0], urbanResults['U1A2'][0], 
                                        urbanResults['U1R1'][0]]
            title = 'All Policies - U1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevU1, trigger_new_cities)
            sec4_col1.plotly_chart(fig1, use_container_width=True)

            ## LINE GRAPH E1
            dimension = ['E1S1', 'E1S3', 'E1M2', 'E1M3', 'E1A1', 'E1A2', 'E1A3', 'E1R2', 'E1R3', 'E1A4', 'E1T1']
            valueBestDimension = [1,1,1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [urbanResults['E1S1'][0], urbanResults['E1S3'][0],
                                         urbanResults['E1M2'][0], urbanResults['E1M3'][0],
                                         urbanResults['E1A1'][0], urbanResults['E1A2'][0], urbanResults['E1A3'][0],
                                         urbanResults['E1R2'][0], urbanResults['E1R3'][0], urbanResults['E1A4'][0],
                                         urbanResults['E1T1'][0]]
            title = 'All Policies - E1'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevE1, trigger_new_cities)
            sec4_col2.plotly_chart(fig2, use_container_width=True)
        #
        ## SMART Completeness (Each subdimension)
        #
        elif linegraphView == 'SMART Completeness (Each subdimension) ':
            if trigger_new_cities == True:
                valueCapturedCompleteness_prevU1 = [(urbanResults_prev['U1S1'][0] + urbanResults_prev['U1S3'][0])/2, 
                                                    (urbanResults_prev['U1M1'][0] + urbanResults_prev['U1M2'][0] + urbanResults_prev['U1M4'][0] + urbanResults_prev['U1M5'][0])/4,
                                                    (urbanResults_prev['U1A1'][0] + urbanResults_prev['U1A2'][0])/2,
                                                    (urbanResults_prev['U1R1'][0])]
                valueCapturedCompleteness_prevE1 = [(urbanResults_prev['E1S1'][0] + urbanResults_prev['E1S3'][0])/2,
                                                    (urbanResults_prev['E1M2'][0] + urbanResults_prev['E1M3'][0])/2,
                                                    (urbanResults_prev['E1A1'][0] + urbanResults_prev['E1A2'][0] + urbanResults_prev['E1A3'][0])/3,
                                                    (urbanResults_prev['E1R2'][0] + urbanResults_prev['E1R3'][0] + urbanResults_prev['E1A4'][0])/3,
                                                    urbanResults_prev['E1T1'][0]]

            else:
                valueCapturedCompleteness_prevU1 = valueCapturedCompleteness_prevE1  = 0

            sec4_col1,sec4_col2 = st.columns([1,1])
            ## LINE GRAPH U1
            dimension = ['Starting','Moderate','Advanced','Robust']
            valueBestDimension = [1,1,1,1]
            valueCapturedCompleteness = [(urbanResults['U1S1'][0] + urbanResults['U1S3'][0])/2, 
                                        (urbanResults['U1M1'][0] + urbanResults['U1M2'][0] + urbanResults['U1M4'][0] + urbanResults['U1M5'][0])/4,
                                        (urbanResults['U1A1'][0] + urbanResults['U1A2'][0])/2,
                                        (urbanResults['U1R1'][0])]
            title = 'All Policies - U1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevU1, trigger_new_cities)
            sec4_col1.plotly_chart(fig1, use_container_width=True)

            ## LINE GRAPH E1
            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(urbanResults['E1S1'][0] + urbanResults['E1S3'][0])/2,
                                         (urbanResults['E1M2'][0] + urbanResults['E1M3'][0])/2,
                                         (urbanResults['E1A1'][0] + urbanResults['E1A2'][0] + urbanResults['E1A3'][0])/3,
                                         (urbanResults['E1R2'][0] + urbanResults['E1R3'][0] + urbanResults['E1A4'][0])/3,
                                         urbanResults['E1T1'][0]]
            title = 'All Policies - E1'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prevE1, trigger_new_cities)
            sec4_col2.plotly_chart(fig2, use_container_width=True)
        
        elif linegraphView == 'SMART Completeness (All subdimensions) + Policies Recommendations':

            if trigger_new_cities == True:
                valueCapturedCompleteness_prev = [(urbanResults_prev['U1S1'][0] + urbanResults_prev['U1S3'][0] + urbanResults_prev['E1S1'][0] + urbanResults_prev['E1S3'][0])/4,
                                                  (urbanResults_prev['U1M1'][0] + urbanResults_prev['U1M2'][0] + urbanResults_prev['U1M4'][0] + urbanResults_prev['U1M5'][0] + urbanResults_prev['E1M2'][0] + urbanResults_prev['E1M3'][0])/6,
                                                  (urbanResults_prev['U1A1'][0] + urbanResults_prev['U1A2'][0] + urbanResults_prev['E1A1'][0] + urbanResults_prev['E1A2'][0] + urbanResults_prev['E1A3'][0])/5,
                                                  (urbanResults_prev['U1R1'][0] + urbanResults_prev['E1R2'][0] + urbanResults_prev['E1R3'][0] + urbanResults_prev['E1A4'][0])/4,
                                                  urbanResults_prev['E1T1'][0]]
            else:
                valueCapturedCompleteness_prev = 0

            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(urbanResults['U1S1'][0] + urbanResults['U1S3'][0] + urbanResults['E1S1'][0] + urbanResults['E1S3'][0])/4,
                                         (urbanResults['U1M1'][0] + urbanResults['U1M2'][0] + urbanResults['U1M4'][0] + urbanResults['U1M5'][0] + urbanResults['E1M2'][0] + urbanResults['E1M3'][0])/6,
                                         (urbanResults['U1A1'][0] + urbanResults['U1A2'][0] + urbanResults['E1A1'][0] + urbanResults['E1A2'][0] + urbanResults['E1A3'][0])/5,
                                         (urbanResults['U1R1'][0] + urbanResults['E1R2'][0] + urbanResults['E1R3'][0] + urbanResults['E1A4'][0])/4,
                                         urbanResults['E1T1'][0]]
            title = 'All Policies'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title, valueCapturedCompleteness_prev, trigger_new_cities)
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
                actual_policy = ""
                st.markdown(f'''##### ➜ Policies to be prioritised to achieve {dimension[dimension_value]} maximum level''', unsafe_allow_html=True)
                # st.markdown("**➜ Policies to be prioritised to achieve **" + dimension[dimension_value] + "** maximum level**")
                for key, value in urbanResults.items():
                    if improve_dimension in key:
                        if urbanResults[key][0] < 1:
                            st.write("🔴" + key + " - " + data.urbanPoliciesText[key][0])
                            actual_policy = key
                st.markdown(f'''##### ➜ Additional policies to achieve {dimension[dimension_value+1]} maximum level''', unsafe_allow_html=True)
                # st.write("**➜ Additional policies to achieve **" + dimension[dimension_value+1] + "** maximum level**")
                for key, value in urbanResults.items():
                    if "S" in actual_policy:
                        if "M" in key:
                            if urbanResults[key][0] < 1:
                                st.write("🟠" + key + " - " + data.urbanPoliciesText[key][0])
                    if "M" in actual_policy:
                        if "A" in key:
                            if urbanResults[key][0] < 1:
                                st.write("🟠" + key + " - " + data.urbanPoliciesText[key][0])
                    if "A" in actual_policy:
                        if "R" in key:
                            if urbanResults[key][0] < 1:
                                st.write("🟠" + key + " - " + data.urbanPoliciesText[key][0])
                    if "T" in actual_policy:
                        st.write("No policies to achieve")
            else:
                st.markdown(f'''##### There is no policies to be achieved''', unsafe_allow_html=True)

    ##
    # Overview of Policies by years
    ##
    with st.expander("SMR Completeness", expanded=True):
        st.subheader("Cities and SMR Completeness - Urban Development & Environmental")

        x = [
            ["2022", "2022", "2022",
            "2023", "2023", "2023"],
            ["Donostia - Synthetic data", "Sevilla - Synthetic data", "Valencia - Synthetic data",
            "Donostia", "  Sevilla - Synthetic data", "  Valencia - Synthetic data"]
        ]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=[3, 4, 3, urbanCompleteness[0], 5, 4], name='Starting', marker_color = "#ef476f"))
        fig.add_trace(go.Bar(x=x, y=[1, 3, 2, urbanCompleteness[1], 4, 3], name='Robust', marker_color = "#ffd166"))
        fig.add_trace(go.Bar(x=x, y=[0, 2, 1, urbanCompleteness[2], 3, 2], name='Advanced', marker_color = "#06d6a0"))
        fig.add_trace(go.Bar(x=x, y=[0, 1, 0, urbanCompleteness[3], 2, 1], name='Moderate', marker_color = "#118ab2"))
        fig.add_trace(go.Bar(x=x, y=[0, 0, 0, urbanCompleteness[4], 1, 0], name='Vertebrate', marker_color = "#073b4c"))
        fig.update_layout(barmode="relative")
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)