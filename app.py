import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import data #data to run the formulas
import calc_ans #functions to calculate the answers

st.set_page_config(layout = "wide")

df = pd.read_csv('answers.csv', sep=',')
df = df.replace(np.nan,0)
pd.options.display.float_format = '{:,.0f}'.format
qnt_answers = len(df.index)

###
###    GENERATING THE CHARTS
###
# GAUGE CHARTS
def gauge_charts (completeness, text, reference):
    match text:
            case "Leadership & Governance":
                starting = [0, 6] #5
                moderate = [6, 12] # 13
                advanced = [12, 17] # 20
                robust = [17, 23] # 24
                vertebrate = [23, 29] # 29
            case "Preparedness <br> Synthetic data":
                starting = [0, 5] # 6
                moderate = [5, 10]#10
                advanced = [10, 15]#17
                robust = [15, 20]#20
                vertebrate = [20, 25]#23
            case "Infrastructure & Resources <br> Synthetic data":
                starting = [0, 5]#6
                moderate = [5, 10]#14
                advanced = [10, 15]#21
                robust = [15, 20]#24
                vertebrate = [20, 25]#28
            case "Cooperation <br> Synthetic data":
                starting = [0, 5]#2
                moderate = [5, 10]#7
                advanced = [10, 15]#13
                robust = [15, 20]#17
                vertebrate = [20, 25]#21
            case "Urban Development <br>& Environmental":
                starting = [0, 4]#4
                moderate = [4, 9]#10
                advanced = [9, 13]#17
                robust = [13, 17]#21
                vertebrate = [17, 22]#22
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

# RADAR CHARTS
def radar_charts (categories, best, mean, text):
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

# LINE CHARTS
def line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(y=dimension, x=valueBestDimension, name='Best Accomplishment', orientation='h',
                             marker=dict(color='#e2e2e2', line=dict(color='rgba(58, 71, 80, 1.0)', width=1))))
        
    fig.add_trace(go.Bar(y=dimension, x=valueCapturedCompleteness, name='Captured Completeness', orientation='h',
                             marker=dict(color='#ffb400', line=dict(color='#4C3A51', width=1))))

    fig.update_layout(title = title, barmode='overlay', title_x=0,
                          legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                          margin= dict(l=30,r=30,b=50,t=50))
    return fig

###
###    STREAMLIT LEFT PANNEL
###
# SELECTION CITY AND DIMENSION
with st.sidebar:
    city = st.selectbox(
        'Select city',
        ('Donostia', 'Pamplona', 'Bilbao'))
    
    questionnaire = st.selectbox(
        'Select the questionnaire',
        ('answer 1 - 27/03 (Leadership)',
        #  'answer 2 - 27/03 (Leadership)', 
        #  'answer 3',# 'answer 4', 'answer 5', 'answer 6', 'answer 7', 'answer 8', 'answer 9', 'answer 10', 'answer 11', 
         'mean'))

    match questionnaire:
        case "answer 1 - 27/03 (Leadership)":
            df_pol = df.iloc[0]
        #case "answer 2 - 27/03 (Leadership)":
        #    df_pol = df.iloc[1]
        # case "answer 3":
        #     df_pol = df.iloc[2]
        # case "answer 4":
        #     df_pol = df.iloc[3]
        # case "answer 5":
        #     df_pol = df.iloc[4]
        # case "answer 6":
        #     df_pol = df.iloc[5]
        # case "answer 7":
        #     df_pol = df.iloc[6]
        # case "answer 8":
        #     df_pol = df.iloc[7]
        # case "answer 9":
        #     df_pol = df.iloc[8]
        # case "answer 10":
        #     df_pol = df.iloc[9]
        # case "answer 11":
        #     df_pol = df.iloc[10]
        case "mean":
            df_pol = df.mean(axis=0)
        case _:
            print("error")

    leadershipResults, leadershipCompleteness = calc_ans.Leadership(df_pol, data.dfL1Best, data.dfL2Best, data.dfL3Best, data.dfL4Best)
    preparednessResults, preparednessCompleteness = calc_ans.Preparedness(df_pol, data.dfP1Best, data.dfP2Best)
    infraResults, infraCompleteness = calc_ans.Infra(df_pol, data.dfI1Best, data.dfI2Best)
    cooperationResults, cooperationCompleteness = calc_ans.Cooperation(df_pol, data.dfC1Best, data.dfC2Best)
    urbanResults, urbanCompleteness = calc_ans.Urban(df_pol, data.dfU1Best, data.dfE1Best)

###
###    DASHBOARD GENERATION
###
title1, title2 = st.columns((0.11,1)) 
with title1:
    st.image('logo_smr.png', width = 120)
with title2:
    st.title('SMR DashboardasdasdAS - ' + city)

###
###    POLICIES COMPLETENESS IN GENERAL
###
st.subheader("SMR Completeness")
sec5_col1, sec5_col2, sec5_col3, sec5_col4, sec5_col5 = st.columns([1,1,1,1,1])

#GAUGE 1 - Leadership & Governance
completenessLeadership = sum(leadershipCompleteness)
text = 'Leadership & Governance'
reference = 29
fig1 = gauge_charts(completenessLeadership, text, reference)
sec5_col1.plotly_chart(fig1, use_container_width=True)

#GAUGE 2 - Preparedness
completenessPreparedness = preparednessCompleteness
text = 'Preparedness <br> Synthetic data'
reference = 25#23
fig2 = gauge_charts(completenessPreparedness, text, reference)
sec5_col2.plotly_chart(fig2, use_container_width=True)

#GAUGE 3 - Infrastructure & Resources
completenessInfra = infraCompleteness
text = 'Infrastructure & Resources <br> Synthetic data'
reference = 25#28
fig3 = gauge_charts(completenessInfra, text, reference)
sec5_col3.plotly_chart(fig3, use_container_width=True)

#GAUGE 4 - Cooperation
completenessCooperation = cooperationCompleteness
text = 'Cooperation <br> Synthetic data'
reference = 25#21
fig4 = gauge_charts(completenessCooperation, text, reference)
sec5_col4.plotly_chart(fig4, use_container_width=True)

#GAUGE 5 - Urban Development & Environmental
completenessUrban = sum(urbanCompleteness)
text = 'Urban Development <br>& Environmental'
reference = 22
fig5 = gauge_charts(completenessUrban, text, reference)
sec5_col5.plotly_chart(fig5, use_container_width=True)




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
    with st.expander('Questions Performance Analysis (Mean between all answers)', expanded=True):
        st.subheader('Questions Performance Analysis - Leadership & Governance (Mean between all answers)')
        
        col1, col2 = st.columns([1,1])
        # RADAR L1
        categories = ['Resilience<br>Governance', 'Plans<br>Integration', 'Access to<br>Basic Services', 'Support to<br>other cities']
        best = [4, 5, 3, 4]
        mean = [df['L1Q1'].mean(),df['L1Q2'].mean(),df['L1Q3'].mean(),df['L1Q4'].mean()]
        text='Leadership & Governance (L1)'
        fig1 = radar_charts(categories, best, mean, text)
        col1.plotly_chart(fig1, use_container_width=True)

        # RADAR L2
        categories = ['Standards<br>Alignment', 'Certification<br>Processes', 'Risk Reduction and<br>Prevention Policies']
        best = [5, 5, 4]
        mean = [df['L2Q1'].mean(), df['L2Q2'].mean(), df['L2Q3'].mean()]
        text='Leadership & Governance (L2)'
        fig2 = radar_charts(categories, best, mean, text)
        col2.plotly_chart(fig2, use_container_width=True)

        col3, col4 = st.columns([1,1])
        # RADAR L3
        categories = ['Resilience<br>Culture', 'Lessons<br>Past Events', 'Knowledge<br>Transfer', 'Learning<br>Process', 'Learning Process<br>Assessment']
        best = [3, 4, 5, 5, 3]
        mean = [df['L3Q1'].mean(), df['L3Q2'].mean(), df['L3Q3'].mean(), df['L3Q4'].mean(), df['L3Q5'].mean()]
        text='Leadership & Governance (L3)'
        fig3 = radar_charts(categories, best, mean, text)
        col3.plotly_chart(fig3, use_container_width=True)

        # RADAR L4
        categories = ['Disaster Response<br>Plan', 'RAP Plan<br>Development', 'Stakeholders<br>Collaboration', 'Disaster<br>Focus', 'Climate Change<br>Perspective', 'Resilience Adoption<br>and Integration', 'Collaboration and Networking with<br>Cities and External Bodies']
        best = [3, 5, 5, 3, 3, 4, 5]
        mean = [df['L4Q1'].mean(), df['L4Q2'].mean(), df['L4Q3'].mean(), df['L4Q4'].mean(), df['L4Q5'].mean(), df['L4Q6'].mean(), df['L4Q7'].mean()]
        text='Leadership & Governance (L4)'
        fig4 = radar_charts(categories, best, mean, text)
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
            ## LINE CHART L1
            dimension = ['L1S1','L1S2','L1M1','L1M2','L1M3','L1A1','L1A2','L1R2','L1T2']
            valueBestDimension = [1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L1S1'][0], leadershipResults['L1S2'][0], 
                                        leadershipResults['L1M1'][0], leadershipResults['L1M2'][0], leadershipResults['L1M3'][0], 
                                        leadershipResults['L1A1'][0], leadershipResults['L1A2'][0], 
                                        leadershipResults['L1R2'][0], leadershipResults['L1T2'][0]]
            title = 'All Policies - L1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col1.plotly_chart(fig1, use_container_width=True)

            ## LINE CHART L2
            dimension = ['L2M1','L2A1','L2R1','L2T1']
            valueBestDimension = [1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L2M1'][0], leadershipResults['L2A1'][0], leadershipResults['L2R1'][0], leadershipResults['L2T1'][0]]
            title = 'All Policies - L2'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
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
            fig3 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col3.plotly_chart(fig3, use_container_width=True)

            # LINE CHART L4
            dimension = ['L4S1','L4S2','L4M2','L4M3','L4A1','L4A2','L4A4','L4R2','L4T3']
            valueBestDimension = [1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L4S1'][0], leadershipResults['L4S2'][0],
                                        leadershipResults['L4M2'][0], leadershipResults['L4M3'][0],
                                        leadershipResults['L4A1'][0], leadershipResults['L4A2'][0], leadershipResults['L4A4'][0],
                                        leadershipResults['L4R2'][0],
                                        leadershipResults['L4T3'][0], ]
            title = 'All Policies - L4'
            fig4 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col4.plotly_chart(fig4, use_container_width=True)
        

        ###
        ###    SMART COMPLETENESS (EACH SUBDIMENSION)
        ###
        elif linegraphView == 'SMART Completeness (Each subdimension)':
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
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col1.plotly_chart(fig1, use_container_width=True)

            ## LINE CHART L2
            dimension = ['Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1]
            valueCapturedCompleteness = [leadershipResults['L2M1'][0], leadershipResults['L2A1'][0], leadershipResults['L2R1'][0], leadershipResults['L2T1'][0]]
            title = 'All Policies - L2'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
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
            fig3 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
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
            fig4 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col4.plotly_chart(fig4, use_container_width=True)

        ###
        ###    SMART COMPLETENESS (ALL SUBDIMENSIONS) + POLICIES RECOMMENDATIONS
        ###
        elif linegraphView == 'SMART Completeness (All subdimensions) + Policies Recommendations':
            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(leadershipResults['L1S1'][0] + leadershipResults['L1S2'][0] + leadershipResults['L3S1'][0] + leadershipResults['L4S1'][0] + leadershipResults['L4S2'][0])/5,
                                        (leadershipResults['L1M1'][0] + leadershipResults['L1M2'][0] + leadershipResults['L1M3'][0] + leadershipResults['L2M1'][0] + leadershipResults['L3M1'][0] + leadershipResults['L3M2'][0] + leadershipResults['L4M2'][0] + leadershipResults['L4M3'][0])/8,
                                        (leadershipResults['L1A1'][0] + leadershipResults['L1A2'][0] + leadershipResults['L2A1'][0] + leadershipResults['L3A2'][0] + leadershipResults['L4A1'][0] + leadershipResults['L4A2'][0] + leadershipResults['L4A4'][0])/7,
                                        (leadershipResults['L1R2'][0] + leadershipResults['L2R1'][0] + leadershipResults['L3R2'][0] + leadershipResults['L4R2'][0])/4,
                                        (leadershipResults['L1T2'][0] + leadershipResults['L2T1'][0] + leadershipResults['L3T1'][0] + leadershipResults['L3T2'][0] + leadershipResults['L4T3'][0])/5]
            title = 'All Policies'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
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

with tab2:
    ##
    # RADAR GRAPHS
    ##

    with st.expander('Questions Performance Analysis', expanded=True):
        st.subheader('Questions Performance Analysis - Urban Development & Environmental')
        col1, col2 = st.columns([1,1])
        # RADAR U1
        categories = ['Evaluate and identify the adaptation measures', 
                      'CC adaptation', 
                      'Integration of CC adaptation and mitigation strategies',
                      'Municipal CC resilience plans and programs ',
                      'NBSs evaluation ',
                      'Nature-Based Solutions',
                      'Climate information to support decision making',
                      'Building regulations and standards ',
                      'Guideline for sustainable and resilient urban planning  ',
                      'Contributions to increase resilience, CC adaptation and risk management in urban areas',]
        best = [3, 3, 3, 3, 3, 4, 4, 4, 3, 3]
        mean = [df['U1Q1'].mean(), 
                df['U1Q2'].mean(), 
                df['U1Q3'].mean(), 
                df['U1Q4'].mean(), 
                df['U1Q5'].mean(), 
                df['U1Q6'].mean(), 
                df['U1Q7'].mean(), 
                df['U1Q8'].mean(), 
                df['U1Q9'].mean(), 
                (df['U1Q10'].mean()+df['U1Q11'].mean()+df['U1Q12'].mean())/3]
        text='Urban Development & Environmental (U1)'
        fig1 = radar_charts(categories, best, mean, text)
        col1.plotly_chart(fig1, use_container_width=True)
    
        # RADAR E1
        categories = ['Development of an ecosystem services assessment', 
                      'Awareness', 
                      'Promotion and establishment of transboundary agreements and collaborations',
                      'Protection and restoration of important ecosystems',
                      'Definition of Targets for GHG reduction till 2050',
                      'Establish the legal context and the financial and technical resources to favour the implementation of climate change actions',
                      'Climate change mitigation',
                      'Periodic monitoring and evaluation of mitigation measures performance and effectiveness']
        best = [4, 3, 3, 4, 3, 3, 3, 3]
        mean = [df['E1Q1'].mean(), 
                df['E1Q2'].mean(), 
                df['E1Q3'].mean(), 
                (df['E1Q4'].mean() + df['E1Q5'].mean())/2,
                df['E1Q6'].mean(), 
                (df['E1Q7'].mean() + df['E1Q8'].mean())/2,
                (df['E1Q9'].mean() + df['E1Q10'].mean() + df['E1Q11'].mean() + df['E1Q12'].mean())/4,
                df['E1Q13'].mean()]
        text='Urban Development & Environmental (E1)'
        fig2 = radar_charts(categories, best, mean, text)
        col2.plotly_chart(fig2, use_container_width=True)
    ##
    # Policies
    ##
    with st.expander('Completeness', expanded=True):
        st.subheader('Completeness - Urban Development & Environmental')

        linegraphView = st.selectbox('Select the view - To see the recommendations select "SMART Completeness (All subdimensions)"',
        ('Policies Completeness ','SMART Completeness (Each subdimension) ','SMART Completeness (All subdimensions) '))

        if linegraphView == 'Policies Completeness ':
            sec4_col1,sec4_col2 = st.columns([1,1])
            ## LINE GRAPH U1
            dimension = ['U1S1', 'U1M1', 'U1A1', 'U1R1', 'U1M2', 'U1A2', 'U1R2', 'U1S3', 'U1M4', 'U1A4', 'U1M5']
            valueBestDimension = [1,1,1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [urbanResults['U1S1'][0], urbanResults['U1S3'][0], 
                                        urbanResults['U1M1'][0], urbanResults['U1M2'][0], urbanResults['U1M4'][0], urbanResults['U1M5'][0],
                                        urbanResults['U1A1'][0], urbanResults['U1A2'][0], urbanResults['U1A4'][0], 
                                        urbanResults['U1R1'][0], urbanResults['U1R2'][0]]
            title = 'All Policies - U1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col1.plotly_chart(fig1, use_container_width=True)

            ## LINE GRAPH E1
            dimension = ['E1S1', 'E1A1', 'E1T1', 'E1M2', 'E1A2', 'E1R2', 'E1S3', 'E1M3', 'E1A3', 'E1R3', 'E1A4']
            valueBestDimension = [1,1,1,1,1,1,1,1,1,1,1]
            valueCapturedCompleteness = [urbanResults['E1S1'][0], urbanResults['E1S3'][0],
                                         urbanResults['E1M2'][0], urbanResults['E1M3'][0],
                                         urbanResults['E1A1'][0], urbanResults['E1A2'][0], urbanResults['E1A3'][0],
                                         urbanResults['E1R2'][0], urbanResults['E1R3'][0], urbanResults['E1A4'][0],
                                         urbanResults['E1T1'][0]]
            title = 'All Policies - E1'
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col2.plotly_chart(fig2, use_container_width=True)

        #
        ## SMART Completeness (Each subdimension)
        #
        elif linegraphView == 'SMART Completeness (Each subdimension) ':
            sec4_col1,sec4_col2 = st.columns([1,1])
            ## LINE GRAPH U1
            dimension = ['Starting','Moderate','Advanced','Robust']
            valueBestDimension = [1,1,1,1]
            valueCapturedCompleteness = [(urbanResults['U1S1'][0] + urbanResults['U1S3'][0])/2, 
                                        (urbanResults['U1M1'][0] + urbanResults['U1M2'][0] + urbanResults['U1M4'][0] + urbanResults['U1M5'][0])/4,
                                        (urbanResults['U1A1'][0] + urbanResults['U1A2'][0] + urbanResults['U1A4'][0])/3,
                                        (urbanResults['U1R1'][0] + urbanResults['U1R2'][0])/2]
            title = 'All Policies - U1'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
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
            fig2 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
            sec4_col2.plotly_chart(fig2, use_container_width=True)
        
        elif linegraphView == 'SMART Completeness (All subdimensions) ':
            dimension = ['Starting','Moderate','Advanced','Robust','Vertebrate']
            valueBestDimension = [1,1,1,1,1]
            valueCapturedCompleteness = [(urbanResults['U1S1'][0] + urbanResults['U1S3'][0] + urbanResults['E1S1'][0] + urbanResults['E1S3'][0])/4,
                                         (urbanResults['U1M1'][0] + urbanResults['U1M2'][0] + urbanResults['U1M4'][0] + urbanResults['U1M5'][0] + urbanResults['E1M2'][0] + urbanResults['E1M3'][0])/6,
                                         (urbanResults['U1A1'][0] + urbanResults['U1A2'][0] + urbanResults['U1A4'][0] + urbanResults['E1A1'][0] + urbanResults['E1A2'][0] + urbanResults['E1A3'][0])/6,
                                         (urbanResults['U1R1'][0] + urbanResults['U1R2'][0] + urbanResults['E1R2'][0] + urbanResults['E1R3'][0] + urbanResults['E1A4'][0])/5,
                                         urbanResults['E1T1'][0]]
            title = 'All Policies'
            fig1 = line_charts(dimension, valueBestDimension, valueCapturedCompleteness, title)
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
            ["Donostia - Synthetic data", "Bilbao - Synthetic data", "Pamplona - Synthetic data",
            "Donostia", " Bilbao - Synthetic data", "  Pamplona - Synthetic data"]
        ]
        fig = go.Figure()
        fig.add_trace(go.Bar(x=x, y=[3, 4, 3, urbanCompleteness[0], 5, 4], name='Starting', marker_color = "#ef476f"))
        fig.add_trace(go.Bar(x=x, y=[1, 3, 2, urbanCompleteness[1], 4, 3], name='Robust', marker_color = "#ffd166"))
        fig.add_trace(go.Bar(x=x, y=[0, 2, 1, urbanCompleteness[2], 3, 2], name='Advanced', marker_color = "#06d6a0"))
        fig.add_trace(go.Bar(x=x, y=[0, 1, 0, urbanCompleteness[3], 2, 1], name='Moderate', marker_color = "#118ab2"))
        fig.add_trace(go.Bar(x=x, y=[0, 0, 0, urbanCompleteness[4], 1, 0], name='Vertebrate', marker_color = "#073b4c"))
        fig.update_layout(barmode="relative")
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)