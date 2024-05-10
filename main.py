import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

##### DATA PROCESSING for the box plots and histograms #####

### Load data subset
# length (box)
source4_1 = pd.read_csv('data/subdata/CC388_len_1.csv', encoding='utf-8')
source5_1 = pd.read_csv('data/subdata/CC389_len_1.csv', encoding='utf-8')
source6_1 = pd.read_csv('data/subdata/CC390_len_1.csv', encoding='utf-8')
source7_1 = pd.read_csv('data/subdata/CC391_len_1.csv', encoding='utf-8')
source8_1 = pd.read_csv('data/subdata/CC392_len_1.csv', encoding='utf-8')
source4_2 = pd.read_csv('data/subdata/CC388_len_2.csv', encoding='utf-8')
source5_2 = pd.read_csv('data/subdata/CC389_len_2.csv', encoding='utf-8')
source6_2 = pd.read_csv('data/subdata/CC390_len_2.csv', encoding='utf-8')
source7_2 = pd.read_csv('data/subdata/CC391_len_2.csv', encoding='utf-8')
source8_2 = pd.read_csv('data/subdata/CC392_len_2.csv', encoding='utf-8')
source4_3 = pd.read_csv('data/subdata/CC141_len_3.csv', encoding='utf-8')
source5_3 = pd.read_csv('data/subdata/CC142_len_3.csv', encoding='utf-8')
source6_3 = pd.read_csv('data/subdata/CC143_len_3.csv', encoding='utf-8')
source7_3 = pd.read_csv('data/subdata/CC144_len_3.csv', encoding='utf-8')
source8_3 = pd.read_csv('data/subdata/CC145_len_3.csv', encoding='utf-8')
# weight (box)
source4_1w = pd.read_csv('data/subdata/CC388_wei_1.csv', encoding='utf-8')
source5_1w = pd.read_csv('data/subdata/CC389_wei_1.csv', encoding='utf-8')
source6_1w = pd.read_csv('data/subdata/CC390_wei_1.csv', encoding='utf-8')
source7_1w = pd.read_csv('data/subdata/CC391_wei_1.csv', encoding='utf-8')
source8_1w = pd.read_csv('data/subdata/CC392_wei_1.csv', encoding='utf-8')
source4_2w = pd.read_csv('data/subdata/CC388_wei_2.csv', encoding='utf-8')
source5_2w = pd.read_csv('data/subdata/CC389_wei_2.csv', encoding='utf-8')
source6_2w = pd.read_csv('data/subdata/CC390_wei_2.csv', encoding='utf-8')
source7_2w = pd.read_csv('data/subdata/CC391_wei_2.csv', encoding='utf-8')
source8_2w = pd.read_csv('data/subdata/CC392_wei_2.csv', encoding='utf-8')
source4_3w = pd.read_csv('data/subdata/CC141_wei_3.csv', encoding='utf-8')
source5_3w = pd.read_csv('data/subdata/CC142_wei_3.csv', encoding='utf-8')
source6_3w = pd.read_csv('data/subdata/CC143_wei_3.csv', encoding='utf-8')
source7_3w = pd.read_csv('data/subdata/CC144_wei_3.csv', encoding='utf-8')
source8_3w = pd.read_csv('data/subdata/CC145_wei_3.csv', encoding='utf-8')
# length (histo)
source4_1h = pd.read_csv('data/subdata/CC388_len_1h.csv', encoding='utf-8')
source5_1h = pd.read_csv('data/subdata/CC389_len_1h.csv', encoding='utf-8')
source6_1h = pd.read_csv('data/subdata/CC390_len_1h.csv', encoding='utf-8')
source7_1h = pd.read_csv('data/subdata/CC391_len_1h.csv', encoding='utf-8')
source8_1h = pd.read_csv('data/subdata/CC392_len_1h.csv', encoding='utf-8')
source4_2h = pd.read_csv('data/subdata/CC388_len_2h.csv', encoding='utf-8')
source5_2h = pd.read_csv('data/subdata/CC389_len_2h.csv', encoding='utf-8')
source6_2h = pd.read_csv('data/subdata/CC390_len_2h.csv', encoding='utf-8')
source7_2h = pd.read_csv('data/subdata/CC391_len_2h.csv', encoding='utf-8')
source8_2h = pd.read_csv('data/subdata/CC392_len_2h.csv', encoding='utf-8')
source4_3h = pd.read_csv('data/subdata/CC141_len_3h.csv', encoding='utf-8')
source5_3h = pd.read_csv('data/subdata/CC142_len_3h.csv', encoding='utf-8')
source6_3h = pd.read_csv('data/subdata/CC143_len_3h.csv', encoding='utf-8')
source7_3h = pd.read_csv('data/subdata/CC144_len_3h.csv', encoding='utf-8')
source8_3h = pd.read_csv('data/subdata/CC145_len_3h.csv', encoding='utf-8')
# weigth (histo)
source4_1wh = pd.read_csv('data/subdata/CC388_wei_1h.csv', encoding='utf-8')
source5_1wh = pd.read_csv('data/subdata/CC389_wei_1h.csv', encoding='utf-8')
source6_1wh = pd.read_csv('data/subdata/CC390_wei_1h.csv', encoding='utf-8')
source7_1wh = pd.read_csv('data/subdata/CC391_wei_1h.csv', encoding='utf-8')
source8_1wh = pd.read_csv('data/subdata/CC392_wei_1h.csv', encoding='utf-8')
source4_2wh = pd.read_csv('data/subdata/CC388_wei_2h.csv', encoding='utf-8')
source5_2wh = pd.read_csv('data/subdata/CC389_wei_2h.csv', encoding='utf-8')
source6_2wh = pd.read_csv('data/subdata/CC390_wei_2h.csv', encoding='utf-8')
source7_2wh = pd.read_csv('data/subdata/CC391_wei_2h.csv', encoding='utf-8')
source8_2wh = pd.read_csv('data/subdata/CC392_wei_2h.csv', encoding='utf-8')
source4_3wh = pd.read_csv('data/subdata/CC141_wei_3h.csv', encoding='utf-8')
source5_3wh = pd.read_csv('data/subdata/CC142_wei_3h.csv', encoding='utf-8')
source6_3wh = pd.read_csv('data/subdata/CC143_wei_3h.csv', encoding='utf-8')
source7_3wh = pd.read_csv('data/subdata/CC144_wei_3h.csv', encoding='utf-8')
source8_3wh = pd.read_csv('data/subdata/CC145_wei_3h.csv', encoding='utf-8')


##### DATA PROCESSING FOR BAR CHARTS #####
source_sex = pd.read_csv('data/subdata/girls_boys.csv', encoding='utf-8')


##### DATA PROCESSING FOR LINE CHARTS #####

# Load raw data file used for line charts
df = pd.read_csv('data/sumstats.csv')

# Filter for 'pregnancy_duration_term' group
df_filtered = df[df['term'] == 'pregnancy_duration_term']

# Filter for 'nvp', 'no_nvp', and 'hospitalized_Pnvp' conditions (filters out month bins per group)
conditions = ['nvp', 'no_nvp', 'hospitalized_Pnvp']
df_filtered = df_filtered[df_filtered['condition'].isin(conditions)]

# Convert age time points to common denominator (year)
## this will be changed to correspond to the child development chart clinicians use, i.e. where the first 1-1.5y is stretched out to see more detail

age_mapping = {
    'birth': 0,
    '6w': 0.115,  # 6 weeks = 6/52 years
    '3m': 0.25,   # 3 months = 0.25 years
    '6m': 0.5,    # 6 months = 0.5 years
    '8m': 0.667,  # 8 months = 8/12 years
    '1y': 1,
    '16m': 1.333, # 16 months = 16/12 years
    '2y': 2,
    '3y': 3,
    '5y': 5,
    '7y': 7,
    '8y': 8
}

# Create a new column 'age_years' by mapping the age variables to their corresponding ages in years
df_filtered['age_years'] = df_filtered['age'].map(age_mapping)

# Define variables
condition = 'no_nvp'
term = 'pregnancy_duration_term'
phenotype = 'length'
age = 'birth'

# Filter data to only include the variables of interest above
filtered_data = df[(df['condition'] == condition) & (df['term'] == term) & (df['phenotype'] == phenotype) & (df['age'] == age)]

# Define a function to calculate the 95% confidence interval
def calculate_ci(group):
    mean = group['mean'].mean()
    std = group['mean'].std()
    n = len(group)
    ci_lower = mean - 1.96 * (std / np.sqrt(n))
    ci_upper = mean + 1.96 * (std / np.sqrt(n))
    return pd.DataFrame({'ci_lower': [ci_lower], 'ci_upper': [ci_upper]})

# Calculate 95% confidence interval for each group for both length and weight
ci_data_length = df_filtered[df_filtered['phenotype'] == 'length'].groupby(['condition', 'age_years']).apply(calculate_ci).reset_index()
ci_data_weight = df_filtered[df_filtered['phenotype'] == 'weight'].groupby(['condition', 'age_years']).apply(calculate_ci).reset_index()

# Merge confidence interval data with the original DataFrame for both length and weight
df_grouped_length = df_filtered[df_filtered['phenotype'] == 'length'].groupby(['condition', 'term', 'age_years']).agg({'mean': 'mean', 'sd': 'std', 'n': 'sum'}).reset_index()
df_grouped_weight = df_filtered[df_filtered['phenotype'] == 'weight'].groupby(['condition', 'term', 'age_years']).agg({'mean': 'mean', 'sd': 'std', 'n': 'sum'}).reset_index()

df_grouped_length = pd.merge(df_grouped_length, ci_data_length, on=['condition', 'age_years'])
df_grouped_weight = pd.merge(df_grouped_weight, ci_data_weight, on=['condition', 'age_years'])

# Display DataFrame after grouping and calculating statistics
# print("DataFrame after grouping and calculating statistics:")
# print(df_grouped_length)
# print(df_grouped_weight)


##### STREAMLIT APP LAYOUT AND INTERACTIONS #####

# Set layout details: title and width of page
st.set_page_config(
    page_title="MoBa Pregnancy and Child Growth Dashboard",
    layout="wide"
)

# Create sidebar with brief descriptions of project dashboard, and for sidebar menus
st.sidebar.header("MoBa Pregnancy and Child Development Dashboard")
st.sidebar.write("The charts displayed in this dashboard are interactive (zoom and scroll to view details).")
st.sidebar.write(" ")

# Selection menu for phenotype
selected_phenotype = st.sidebar.selectbox("**Select a phenotype**", ["Length", "Weight"], index=0)

# Selection menu for month
selected_month = st.sidebar.selectbox("**Select a month**", ["Month 4", "Month 5", "Month 6", "Month 7", "Month 8+"], index=0)

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.subheader("Definition of terms")
st.sidebar.write("**No NVP** = No Nausea and Vomiting in Pregnancy")
st.sidebar.write("**NVP** = Nausea and Vomiting in Pregnancy")
st.sidebar.write("**Hospitalized** = due to NVP")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.subheader("About this project")
st.sidebar.write("This dashboard is using data from the [Norwegian Mother, Father, and Child (MoBa) cohort study](https://www.niehs.nih.gov/research/atniehs/labs/epi/studies/moba). It was developed as a data exploration tool for various expert groups in research and clinic (genetic epidemilogists, paediatricians) who are investigating factors impacting women's health during pregnancy and child development outcomes, with a focus on hyperemesis gravidarum (HG). HG is a rare but devastating condition that affects 1-3 percent of all pregnancies. More information about HG can be found [here](https://pubmed.ncbi.nlm.nih.gov/31515515/).")

# Define dictionaries to create the data subsets for boxplots and histograms

# Length
month_data = {
    "Month 4": {"no_nvp": source4_1, "nvp": source4_2, "hospitalized": source4_3},
    "Month 5": {"no_nvp": source5_1, "nvp": source5_2, "hospitalized": source5_3},
    "Month 6": {"no_nvp": source6_1, "nvp": source6_2, "hospitalized": source6_3},
    "Month 7": {"no_nvp": source7_1, "nvp": source7_2, "hospitalized": source7_3},
    "Month 8+": {"no_nvp": source8_1, "nvp": source8_2, "hospitalized": source8_3}
}

# Weight
month_data_weight = {
    "Month 4": {"no_nvp": source4_1w, "nvp": source4_2w, "hospitalized": source4_3w},
    "Month 5": {"no_nvp": source5_1w, "nvp": source5_2w, "hospitalized": source5_3w},
    "Month 6": {"no_nvp": source6_1w, "nvp": source6_2w, "hospitalized": source6_3w},
    "Month 7": {"no_nvp": source7_1w, "nvp": source7_2w, "hospitalized": source7_3w},
    "Month 8+": {"no_nvp": source8_1w, "nvp": source8_2w, "hospitalized": source8_3w}
}


##### FUNCTIONS TO CREATE BOXPLOTS AND HISTOGRAMS #####

# Boxplot length
def create_boxplot(source, color_code, title_txt):
    boxplot = alt.Chart(source).mark_boxplot(color= color_code).encode(
        alt.Y('outcome_level:Q', scale=alt.Scale(domain=[5, 75]), title='length [cm]')
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).properties(
    height=250
    ).configure_axis(
    labelFontSize=13,
    titleFontSize=15
    ).interactive()
    return boxplot

# Boxplot Weight
def create_boxplot_w(source, color_code, title_txt):
    #title = alt.TitleParams(text="No NVP (n=33040)")
    boxplot = alt.Chart(source).mark_boxplot(color= color_code).encode(
    alt.Y('outcome_level:Q', scale=alt.Scale(domain=[0, 10000]), title='weight [g]')
    ).properties(
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).properties(
    height=250
    ).configure_axis(
    labelFontSize=13,
    titleFontSize=15
    ).interactive() 
    return boxplot

## Histogram Length
def create_histo(source, color_code, title_txt):
    histo = alt.Chart(source).mark_bar(color= color_code).encode( 
        alt.X('outcome_level:Q', bin=alt.Bin(extent=[0, 70], step=2), title='length [cm]'),
        alt.Y('n:Q'),  
    ).properties(
    height=250,
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17
    }
    ).configure_axis( 
    labelFontSize=13,
    titleFontSize=15
    ).interactive(bind_y=False)
    return histo  
    # horizontal layout:
    # .configure_axisX(
    # orient = "top"
    # )

## Histogram Weight

def create_histo_w(source, color_code, title_txt):
    histo = alt.Chart(source).mark_bar(color= color_code).encode(  
        alt.X('outcome_level:Q', bin=alt.Bin(extent=[0, 10000], step=400), title='weight [g]'),
        alt.Y('n:Q'),   
    ).properties(
    height=250,
    title={ 
      "text": [title_txt], 
      "dy" : -10,
      "fontSize": 17,
    }
    ).configure_axis(
    labelFontSize=13,
    titleFontSize=15
    ).interactive(bind_y=False)  
    return histo

## Bar charts genetic sex differences

def create_barchart_sex(source, color_code, title_txt):
    barchart = alt.Chart(source).mark_bar(color=color_code).encode(
        alt.X('outcome_level:N', title='Sex'),
        alt.Y('n:Q', title='n'),
        
    ).properties(
    # title={ 
    #   "text": [title_txt], 
    #   "dy" : -10,
    #   "fontSize": 17
    # }
    ).properties(
    height=200,
    ).configure_axis( 
    labelFontSize=13,
    titleFontSize=15
    )
    # (1 = Girls, 2 = Boys, 3 = Missing)
    return barchart 

# def create_barchart_sex(source, color_code):
#     barchart = alt.Chart(source).mark_bar(color=color_code, size=22).encode(
#         alt.X('outcome_level:N', title='Sex'),
#         alt.Y('n:Q', title='n'),
#     ).properties(
#         height=350
#     ).configure_axis(    
#         labelFontSize=13,
#         titleFontSize=15
#     ).interactive()
#     # (1 = Girls, 2 = Boys, 3 = Missing)
#     return barchart

# Define data subsets for genetic sex bar charts
sub_sex_any = source_sex.loc[(source_sex.category == 'any').reset_index(drop=True)]
# No NVP
sub_sex_4_1 = source_sex.loc[(source_sex.category == 'CC388').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_5_1 = source_sex.loc[(source_sex.category == 'CC389').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_6_1 = source_sex.loc[(source_sex.category == 'CC390').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_7_1 = source_sex.loc[(source_sex.category == 'CC391').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_8_1 = source_sex.loc[(source_sex.category == 'CC392').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
# NVP
sub_sex_4_2 = source_sex.loc[(source_sex.category == 'CC388').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_5_2 = source_sex.loc[(source_sex.category == 'CC389').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_6_2 = source_sex.loc[(source_sex.category == 'CC390').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_7_2 = source_sex.loc[(source_sex.category == 'CC391').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_8_2 = source_sex.loc[(source_sex.category == 'CC392').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
# Hospital
sub_sex_4_3 = source_sex.loc[(source_sex.category == 'CC141').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_5_3 = source_sex.loc[(source_sex.category == 'CC142').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_6_3 = source_sex.loc[(source_sex.category == 'CC143').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_7_3 = source_sex.loc[(source_sex.category == 'CC144').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_8_3 = source_sex.loc[(source_sex.category == 'CC145').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]

sub_sex_any = source_sex.loc[(source_sex.category == 'any').reset_index(drop=True)]
# No NVP
sub_sex_4_1 = source_sex.loc[(source_sex.category == 'CC388').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_5_1 = source_sex.loc[(source_sex.category == 'CC389').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_6_1 = source_sex.loc[(source_sex.category == 'CC390').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_7_1 = source_sex.loc[(source_sex.category == 'CC391').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
sub_sex_8_1 = source_sex.loc[(source_sex.category == 'CC392').reset_index(drop=True) & (source_sex.level == '0').reset_index(drop=True)]
# NVP
sub_sex_4_2 = source_sex.loc[(source_sex.category == 'CC388').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_5_2 = source_sex.loc[(source_sex.category == 'CC389').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_6_2 = source_sex.loc[(source_sex.category == 'CC390').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_7_2 = source_sex.loc[(source_sex.category == 'CC391').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_8_2 = source_sex.loc[(source_sex.category == 'CC392').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
# Hospital
sub_sex_4_3 = source_sex.loc[(source_sex.category == 'CC141').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_5_3 = source_sex.loc[(source_sex.category == 'CC142').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_6_3 = source_sex.loc[(source_sex.category == 'CC143').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_7_3 = source_sex.loc[(source_sex.category == 'CC144').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]
sub_sex_8_3 = source_sex.loc[(source_sex.category == 'CC145').reset_index(drop=True) & (source_sex.level == '1').reset_index(drop=True)]

# calculate sums for n
sum_any = source_sex.loc[(source_sex['category'] == 'any').reset_index(drop=True) & (source_sex['level'] == 'any').reset_index(drop=True), 'n'].sum()
sum4_1 = source_sex.loc[(source_sex['category'] == 'CC388').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() # 80960 
sum4_2 = source_sex.loc[(source_sex['category'] == 'CC388').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum5_1 = source_sex.loc[(source_sex['category'] == 'CC389').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum5_2 = source_sex.loc[(source_sex['category'] == 'CC389').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum6_1 = source_sex.loc[(source_sex['category'] == 'CC390').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum6_2 = source_sex.loc[(source_sex['category'] == 'CC390').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum7_1 = source_sex.loc[(source_sex['category'] == 'CC391').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum7_2 = source_sex.loc[(source_sex['category'] == 'CC391').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum8_1 = source_sex.loc[(source_sex['category'] == 'CC392').reset_index(drop=True) & (source_sex['level'] == '0').reset_index(drop=True), 'n'].sum() 
sum8_2 = source_sex.loc[(source_sex['category'] == 'CC392').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 

sum4_3 = source_sex.loc[(source_sex['category'] == 'CC141').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum() 
sum5_3 = source_sex.loc[(source_sex['category'] == 'CC142').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()
sum6_3 = source_sex.loc[(source_sex['category'] == 'CC143').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()
sum7_3 = source_sex.loc[(source_sex['category'] == 'CC144').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()
sum8_3 = source_sex.loc[(source_sex['category'] == 'CC145').reset_index(drop=True) & (source_sex['level'] == '1').reset_index(drop=True), 'n'].sum()

### Define colors for each condition group ###

## colorblind-safe scheme, for patient groups
color1="#038d93"    # turquoise "#0097a7"
color2="#5443aa"    # violet
color3="#882255"    # dark red
color4="#88ccee"    # light blue

## old color scheme
# color1="#416396" 
# color2="#0097a7"
# color3="#b06fc6"
# color4="#669"


##### SET STREAMLIT LAYOUT & RENDER VISUALIZATIONS #####

tab1, tab2 = st.tabs(["View: Single time point", "View: All time points"])

with tab1:
    # Define first setion with titles
    col13, col14 = st.columns(2)

    with st.container():
        with col13:
            st.write(f"<h6>Child <b>{selected_phenotype}</b>, given each patient group during <b>{selected_month}</b> of pregnancy.</h6>", unsafe_allow_html=True)

        with col14:
            phenotype_title = []

            if selected_phenotype == 'Weight':
                phenotype_title = 'Weight'
            elif selected_phenotype == 'Length':
                phenotype_title = 'Length'
            st.write(f"<h6>Child {phenotype_title} Growth Development Chart</h6>", unsafe_allow_html=True)

    # Create 5 columns for charts        
    col1, col2, col3, col4, col5 = st.columns([15, 15, 15, 5, 50])

    ## For all the following sections, an if loop runs through to display correct boxplots based on user selection of phenotype and month
    ## This code can definitely be streamlined, done 'smarter' rather than so long (but at least it works!)

    # Boxplots (No NVP)
    with st.container():
        with col1:
            # st.markdown("<h5 style='text-align: center;'> No NVP </h5>", unsafe_allow_html=True)

            #### No NVP
            if selected_phenotype == "Weight":
                if selected_month == "Month 4":
                    boks4_1 = create_boxplot_w(source4_1w, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(boks4_1, use_container_width=True)
                    histo4_1 = create_histo_w(source4_1wh, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(histo4_1, use_container_width=True)
                elif selected_month == "Month 5":
                    boks5_1w = create_boxplot_w(source5_1w, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(boks5_1w, use_container_width=True)
                    histo5_1 = create_histo_w(source5_1wh, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(histo5_1, use_container_width=True)
                elif selected_month == "Month 6":
                    boks6_1 = create_boxplot_w(source6_1w, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(boks6_1, use_container_width=True)
                    histo6_1 = create_histo_w(source6_1wh, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(histo6_1, use_container_width=True)
                elif selected_month == "Month 7":
                    boks7_1 = create_boxplot_w(source7_1w, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(boks7_1, use_container_width=True)
                    histo7_1 = create_histo_w(source7_1wh, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(histo7_1, use_container_width=True)
                elif selected_month == "Month 8+":
                    boks8_1 = create_boxplot_w(source8_1w, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(boks8_1, use_container_width=True)
                    histo8_1 = create_histo_w(source8_1wh, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(histo8_1, use_container_width=True)

            elif selected_phenotype == "Length": ### BIRTH LENGTH
                if selected_month == "Month 4":
                    boks4_1 = create_boxplot(source4_1, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(boks4_1, use_container_width=True)
                    histo4_1 = create_histo(source4_1h, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(histo4_1, use_container_width=True)      
                elif selected_month == "Month 5":
                    boks5_1 = create_boxplot(source5_1, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(boks5_1, use_container_width=True)
                    histo5_1 = create_histo(source5_1h, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(histo5_1, use_container_width=True)   
                elif selected_month == "Month 6":
                    boks6_1 = create_boxplot(source6_1, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(boks6_1, use_container_width=True)
                    histo6_1 = create_histo(source6_1h, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(histo6_1, use_container_width=True)
                elif selected_month == "Month 7":
                    boks7_1 = create_boxplot(source7_1, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(boks7_1, use_container_width=True)
                    histo7_1 = create_histo(source7_1h, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(histo7_1, use_container_width=True)
                elif selected_month == "Month 8+":
                    boks8_1 = create_boxplot(source8_1, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(boks8_1, use_container_width=True)
                    histo8_1 = create_histo(source8_1h, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(histo8_1, use_container_width=True)

    # Boxplots (NVP)      
        with col2:
            # st.markdown("<h5 style='text-align: center;'>NVP </h5>", unsafe_allow_html=True)
            
            #### NVP
            if selected_phenotype == "Weight":
                if selected_month == "Month 4":
                    boks4_2 = create_boxplot_w(source4_2w, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(boks4_2, use_container_width=True)
                    histo4_2 = create_histo_w(source4_2wh, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(histo4_2, use_container_width=True)
                elif selected_month == "Month 5":
                    boks5_2 = create_boxplot_w(source5_2w, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(boks5_2, use_container_width=True)
                    histo5_2 = create_histo_w(source5_2wh, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(histo5_2, use_container_width=True)
                elif selected_month == "Month 6":
                    boks6_2 = create_boxplot_w(source6_2w, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(boks6_2, use_container_width=True)
                    histo6_2 = create_histo_w(source6_2wh, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(histo6_2, use_container_width=True)
                elif selected_month == "Month 7":
                    boks7_2 = create_boxplot_w(source7_2w, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(boks7_2, use_container_width=True)
                    histo7_2 = create_histo_w(source7_2wh, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(histo7_2, use_container_width=True)
                elif selected_month == "Month 8+":
                    boks8_2 = create_boxplot_w(source8_2w, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(boks8_2, use_container_width=True)
                    histo8_2 = create_histo_w(source8_2wh, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(histo8_2, use_container_width=True)


            ### BIRTH LENGTH
            elif selected_phenotype == "Length": ### BIRTH LENGTH
                if selected_month == "Month 4":
                    boks4_2 = create_boxplot(source4_2, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(boks4_2, use_container_width=True)
                    histo4_2 = create_histo(source4_2h, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(histo4_2, use_container_width=True)
                elif selected_month == "Month 5":
                    boks5_2 = create_boxplot(source5_2, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(boks5_2, use_container_width=True)
                    histo5_2 = create_histo(source5_2h, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(histo5_2, use_container_width=True)
                elif selected_month == "Month 6":
                    boks6_2 = create_boxplot(source6_2, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(boks6_2, use_container_width=True)
                    histo6_2 = create_histo(source6_2h, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(histo6_2, use_container_width=True)
                elif selected_month == "Month 7":
                    boks7_2 = create_boxplot(source7_2, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(boks7_2, use_container_width=True)
                    histo7_2 = create_histo(source7_2h, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(histo7_2, use_container_width=True)
                elif selected_month == "Month 8+":
                    boks8_2 = create_boxplot(source8_2, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(boks8_2, use_container_width=True)
                    histo8_2 = create_histo(source8_2h, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(histo8_2, use_container_width=True)

    # Boxplots (Hospitalized)
        with col3:
            # st.markdown("<h5 style='text-align: center;'>Hospitalized </h5>", unsafe_allow_html=True)
            
            if selected_phenotype == "Weight":
                if selected_month == "Month 4":
                    boks4_3 = create_boxplot_w(source4_3w, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(boks4_3, use_container_width=True)
                    histo4_3 = create_histo_w(source4_3wh, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(histo4_3, use_container_width=True)
                elif selected_month == "Month 5":   
                    boks5_3 = create_boxplot_w(source5_3w, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(boks5_3, use_container_width=True)
                    histo5_3 = create_histo_w(source5_3wh, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(histo5_3, use_container_width=True)
                elif selected_month == "Month 6":
                    boks6_3 = create_boxplot_w(source6_3w, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(boks6_3, use_container_width=True)
                    histo6_3 = create_histo_w(source6_3wh, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(histo6_3, use_container_width=True)
                elif selected_month == "Month 7":
                    boks7_3 = create_boxplot_w(source7_3w, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(boks7_3, use_container_width=True)
                    histo7_3 = create_histo_w(source7_3wh, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(histo7_3, use_container_width=True)
                elif selected_month == "Month 8+":
                    boks8_3 = create_boxplot_w(source8_3w, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(boks8_3, use_container_width=True)
                    histo8_3 = create_histo_w(source8_3wh, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(histo8_3, use_container_width=True)

            ### BIRTH LENGTH
            elif selected_phenotype == "Length": ### BIRTH LENGTH
                if selected_month == "Month 4":
                    boks4_3 = create_boxplot(source4_3, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(boks4_3, use_container_width=True)
                    histo4_3 = create_histo(source4_3h, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(histo4_3, use_container_width=True)
                elif selected_month == "Month 5":
                    boks5_3 = create_boxplot(source5_3, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(boks5_3, use_container_width=True)
                    histo5_3 = create_histo(source5_3h, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(histo5_3, use_container_width=True)
                elif selected_month == "Month 6":
                    boks6_3 = create_boxplot(source6_3, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(boks6_3, use_container_width=True)
                    histo6_3 = create_histo(source6_3h, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(histo6_3, use_container_width=True)
                elif selected_month == "Month 7":
                    boks7_3 = create_boxplot(source7_3, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(boks7_3, use_container_width=True)
                    histo7_3 = create_histo(source7_3h, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(histo7_3, use_container_width=True)
                elif selected_month == "Month 8+":
                    boks8_3 = create_boxplot(source8_3, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(boks8_3, use_container_width=True)
                    histo8_3 = create_histo(source8_3h, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(histo8_3, use_container_width=True)

        # with col4:
            # This column intentionally left blank

        ##### COL5 LINE CHART VISUALIZATION #####

        # Create line chart with 95% CI error band

        # Define custom colors for each patient group
        custom_colors = {
            'no_nvp': "#038d93",  # turquoise
            'nvp': "#5443aa",     # violet
            'hospitalized_Pnvp': "#882255"  # dark red
        }

        # Define length line chart with CI
        line_with_ci_length = alt.Chart(df_grouped_length).mark_line().encode(
            x='age_years:Q',
            y=alt.Y('mean:Q', title='Mean Length [cm]'),
            color=alt.Color('condition', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=list(custom_colors.values())), legend=alt.Legend(title='Condition', orient='bottom', labelExpr="datum.label == 'no_nvp' ? 'No NVP' : (datum.label == 'nvp' ? 'NVP' : 'Hospitalized')")),
            strokeDash=alt.StrokeDash('condition', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=[[10], [0], [5]]))  
        )

        band_with_ci_length = alt.Chart(df_grouped_length).mark_errorband(extent='ci', opacity=0.1).encode(
            x='age_years:Q',
            y='ci_lower:Q',
            y2='ci_upper:Q',
            color=alt.Color('condition:N', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=list(custom_colors.values())), legend=alt.Legend(title='Condition', orient='bottom')) 
        )

        chart_with_ci_band_length = (band_with_ci_length + line_with_ci_length).properties(
            width="container", 
            height=500  
        ).interactive()  

        # Define weight line chart with CI
        line_with_ci_weight = alt.Chart(df_grouped_weight).mark_line().encode(
            x='age_years:Q',
            y=alt.Y('mean:Q', title='Mean Weight [kg]'),
            color=alt.Color('condition', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=list(custom_colors.values())), legend=alt.Legend(title='Condition', orient='bottom', labelExpr="datum.label == 'no_nvp' ? 'No NVP' : (datum.label == 'nvp' ? 'NVP' : 'Hospitalized')")),
            strokeDash=alt.StrokeDash('condition', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=[[10], [0], [5]]))  
        )

        band_with_ci_weight = alt.Chart(df_grouped_weight).mark_errorband(extent='ci', opacity=0.1).encode(
            x='age_years:Q',
            y='ci_lower:Q',
            y2='ci_upper:Q',
            color=alt.Color('condition:N', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=list(custom_colors.values())), legend=alt.Legend(title='Condition', orient='bottom')) 
        )

        chart_with_ci_band_weight = (band_with_ci_weight + line_with_ci_weight).properties(
            width="container",  
            height=450  
        ).interactive() 

        # Function to create the chart without the CI band
        def create_chart_no_ci(df_grouped, phenotype):
            custom_colors = {
                'no_nvp': color1,  # no NVP
                'nvp': color2,     # NVP
                'hospitalized_Pnvp': color3  # Hosp.
            }

            # Create line chart
            line = alt.Chart(df_grouped).mark_line().encode(
                x='age_years:Q',
                y=alt.Y('mean:Q', title=f'Mean {phenotype.capitalize()}'),
                color=alt.Color('condition', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=list(custom_colors.values())), legend=alt.Legend(title='Condition', orient='bottom', labelExpr="datum.label == 'no_nvp' ? 'No NVP' : (datum.label == 'nvp' ? 'NVP' : 'Hospitalized')")),
                strokeDash=alt.StrokeDash('condition', scale=alt.Scale(domain=['no_nvp', 'nvp', 'hospitalized_Pnvp'], range=[[10], [0], [5]])) 
            )

            chart_no_ci = line.properties(
                width="container",
                height=450
            ).interactive()

            return chart_no_ci

        # Create charts for each phenotype
        chart_length_no_ci = create_chart_no_ci(df_grouped_length, 'length')
        chart_weight_no_ci = create_chart_no_ci(df_grouped_weight, 'weight')

        with col5:
            # Radio button options for viewing different stats
            stats_view = st.radio(
                "Select an additional view:",
                ["Off", "95% CI", "Percentiles", "Mean Estimate"],
                index=0,
                horizontal=True,
            )
            
            # original checkbox option for just one stat type
            # User input options for viewing different stats # change to 95% CI (from SD)
            # show_ci = st.checkbox("Show 95% Confidence Interval")
            # show_mean_est = st.checkbox("Show mean estimate")
        
            if selected_phenotype == 'Length':
                if stats_view == "95% CI":
                    st.altair_chart(chart_with_ci_band_length, use_container_width=True)  # Length chart with CI band
                else:
                    st.altair_chart(chart_length_no_ci, use_container_width=True)  # Length chart without CI band

            elif selected_phenotype == 'Weight':
                if stats_view == "95% CI":
                    st.altair_chart(chart_with_ci_band_weight, use_container_width=True)  # Weight chart with CI band
                else:
                    st.altair_chart(chart_weight_no_ci, use_container_width=True) # Weight chart without CI band

    ##### BAR CHARTS FOR DIFF BETWEEN BOYS AND GIRLS #####

    col11, col12 = st.columns(2)

    with st.container():
        with col11:
            st.write(f"<h6><b>Genetic sex</b> at birth, given each patient group during <b>{selected_month}</b> of pregnancy.</h6>", unsafe_allow_html=True)

        with col12:
            st.write("<h6>Raw data tables for displayed charts.</h6>", unsafe_allow_html=True)

    col6, col7, col8, col9, col10 = st.columns([15,15,15,5,50])

    with st.container():
        with col6:
            if selected_month == "Month 4":
                bar4_1 = create_barchart_sex(sub_sex_4_1, color1, "No NVP (n=" + str(sum4_1) + ")")
                st.altair_chart(bar4_1, use_container_width=True)
            elif selected_month == "Month 5":
                bar5_1 = create_barchart_sex(sub_sex_5_1, color1, "No NVP (n=" + str(sum5_1) + ")")
                st.altair_chart(bar5_1, use_container_width=True)
            elif selected_month == "Month 6":
                bar6_1 = create_barchart_sex(sub_sex_6_1, color1, "No NVP (n=" + str(sum6_1) + ")")
                st.altair_chart(bar6_1, use_container_width=True)
            elif selected_month == "Month 7":
                bar7_1 = create_barchart_sex(sub_sex_7_1, color1, "No NVP (n=" + str(sum7_1) + ")")
                st.altair_chart(bar7_1, use_container_width=True)
            elif selected_month == "Month 8+":        
                bar8_1 = create_barchart_sex(sub_sex_8_1, color1, "No NVP (n=" + str(sum8_1) + ")")
                st.altair_chart(bar8_1, use_container_width=True)

        with col7:
            if selected_month == "Month 4":
                bar4_2 = create_barchart_sex(sub_sex_4_2, color2, "NVP (n=" + str(sum4_2) + ")")
                st.altair_chart(bar4_2, use_container_width=True)
            elif selected_month == "Month 5":
                bar5_2 = create_barchart_sex(sub_sex_5_2, color2, "NVP (n=" + str(sum5_2) + ")")
                st.altair_chart(bar5_2, use_container_width=True)
            elif selected_month == "Month 6":
                bar6_2 = create_barchart_sex(sub_sex_6_2, color2, "NVP (n=" + str(sum6_2) + ")")
                st.altair_chart(bar6_2, use_container_width=True)
            elif selected_month == "Month 7":
                bar7_2 = create_barchart_sex(sub_sex_7_2, color2, "NVP (n=" + str(sum7_2) + ")")
                st.altair_chart(bar7_2, use_container_width=True)
            elif selected_month == "Month 8+":
                bar8_2 = create_barchart_sex(sub_sex_8_2, color2, "NVP (n=" + str(sum8_2) + ")")
                st.altair_chart(bar8_2, use_container_width=True)
        
        with col8:
            if selected_month == "Month 4":
                bar4_3 = create_barchart_sex(sub_sex_4_3, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                st.altair_chart(bar4_3, use_container_width=True)
            elif selected_month == "Month 5":
                bar5_3 = create_barchart_sex(sub_sex_5_3, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                st.altair_chart(bar5_3, use_container_width=True)
            elif selected_month == "Month 6":
                bar6_3 = create_barchart_sex(sub_sex_6_3, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                st.altair_chart(bar6_3, use_container_width=True)
            elif selected_month == "Month 7":
                bar7_3 = create_barchart_sex(sub_sex_7_3, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                st.altair_chart(bar7_3, use_container_width=True)
            elif selected_month == "Month 8+":
                bar8_3 = create_barchart_sex(sub_sex_8_3, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                st.altair_chart(bar8_3, use_container_width=True)
        

        # with col9:
            # This column intentionally left blank
            
        # Raw data table based on user input in sidebar menus. User can select which table to display.
        with col10:

            # Filter the DataFrame based on the selected phenotype
            if selected_phenotype == "Weight":
                filtered_df = df[df['phenotype'] == 'weight']
            elif selected_phenotype == "Length":
                filtered_df = df[df['phenotype'] == 'length']

            # Display the filtered DataFrame as a table
            st.write(filtered_df)

with tab2:

    with st.container():
        chart_view = st.radio(
                "Select a chart type:",
                ["Boxplots", "Histograms"],
                index=0,
                horizontal=True,
            )

    with st.container():
        ## All time steps:
        col20, col21, col22, col23, col24, = st.columns([1, 1, 1, 1, 1])
    
        if selected_phenotype == "Length":        
            with col20:
                #### No NVP
                if chart_view == "Histograms":
                    histo4_1 = create_histo(source4_1h, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(histo4_1, use_container_width=True)      
                    histo4_2 = create_histo(source4_2h, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(histo4_2, use_container_width=True)
                    histo4_3 = create_histo(source4_3h, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(histo4_3, use_container_width=True)
                else:
                    boks4_1 = create_boxplot(source4_1, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(boks4_1, use_container_width=True)
                    boks4_2 = create_boxplot(source4_2, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(boks4_2, use_container_width=True)
                    boks4_3 = create_boxplot(source4_3, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(boks4_3, use_container_width=True)    
                        
            with col21:
                #### No NVP
                if chart_view == "Histograms":
                    histo5_1 = create_histo(source5_1h, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(histo5_1, use_container_width=True)   
                    histo5_2 = create_histo(source5_2h, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(histo5_2, use_container_width=True)
                    histo5_3 = create_histo(source5_3h, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(histo5_3, use_container_width=True)
                else:
                    boks5_1 = create_boxplot(source5_1, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(boks5_1, use_container_width=True)
                    boks5_2 = create_boxplot(source5_2, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(boks5_2, use_container_width=True)
                    boks5_3 = create_boxplot(source5_3, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(boks5_3, use_container_width=True)
    
        
            with col22:
                #### No NVP
                if chart_view == "Histograms":
                    histo6_1 = create_histo(source6_1h, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(histo6_1, use_container_width=True)
                    histo6_2 = create_histo(source6_2h, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(histo6_2, use_container_width=True)
                    histo6_3 = create_histo(source6_3h, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(histo6_3, use_container_width=True)
                else:
                    boks6_1 = create_boxplot(source6_1, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(boks6_1, use_container_width=True)
                    boks6_2 = create_boxplot(source6_2, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(boks6_2, use_container_width=True)
                    boks6_3 = create_boxplot(source6_3, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(boks6_3, use_container_width=True)

            with col23:
                #### No NVP
                if chart_view == "Histograms":
                    histo7_1 = create_histo(source7_1h, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(histo7_1, use_container_width=True)
                    histo7_2 = create_histo(source7_2h, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(histo7_2, use_container_width=True)
                    histo7_3 = create_histo(source7_3h, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(histo7_3, use_container_width=True)
                else:
                    boks7_1 = create_boxplot(source7_1, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(boks7_1, use_container_width=True)
                    boks7_2 = create_boxplot(source7_2, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(boks7_2, use_container_width=True)
                    boks7_3 = create_boxplot(source7_3, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(boks7_3, use_container_width=True)

            with col24:
                #### No NVP
                if chart_view == "Histograms":
                    histo8_1 = create_histo(source8_1h, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(histo8_1, use_container_width=True)
                    histo8_2 = create_histo(source8_2h, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(histo8_2, use_container_width=True)
                    histo8_3 = create_histo(source8_3h, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(histo8_3, use_container_width=True)
                else:
                    boks8_1 = create_boxplot(source8_1, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(boks8_1, use_container_width=True)
                    boks8_2 = create_boxplot(source8_2, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(boks8_2, use_container_width=True)
                    boks8_3 = create_boxplot(source8_3, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(boks8_3, use_container_width=True)
        
        elif selected_phenotype == "Weight":
            if chart_view == "Histograms":
                with col20:
                    histo4_1 = create_histo_w(source4_1wh, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(histo4_1, use_container_width=True)
                    histo4_2 = create_histo_w(source4_2wh, color2, "NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(histo4_2, use_container_width=True)
                    histo4_3 = create_histo_w(source4_3wh, color3, "Hospitalized (n=" + str(sum4_3) + ")")
                    st.altair_chart(histo4_3, use_container_width=True)

                with col21:
                    histo5_1 = create_histo_w(source5_1wh, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(histo5_1, use_container_width=True)
                    histo5_2 = create_histo_w(source5_2wh, color2, "NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(histo5_2, use_container_width=True)
                    histo5_3 = create_histo_w(source5_3wh, color3, "Hospitalized (n=" + str(sum5_3) + ")")
                    st.altair_chart(histo5_3, use_container_width=True)

                with col22:
                    histo6_1 = create_histo_w(source6_1wh, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(histo6_1, use_container_width=True)
                    histo6_2 = create_histo_w(source6_2wh, color2, "NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(histo6_2, use_container_width=True)
                    histo6_3 = create_histo_w(source6_3wh, color3, "Hospitalized (n=" + str(sum6_3) + ")")
                    st.altair_chart(histo6_3, use_container_width=True)

                with col23:
                    histo7_1 = create_histo_w(source7_1wh, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(histo7_1, use_container_width=True)
                    histo7_2 = create_histo_w(source7_2wh, color2, "NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(histo7_2, use_container_width=True)
                    histo7_3 = create_histo_w(source7_3wh, color3, "Hospitalized (n=" + str(sum7_3) + ")")
                    st.altair_chart(histo7_3, use_container_width=True)
                
                with col24:
                    histo8_1 = create_histo_w(source8_1wh, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(histo8_1, use_container_width=True)
                    histo8_2 = create_histo_w(source8_2wh, color2, "NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(histo8_2, use_container_width=True)
                    histo8_3 = create_histo_w(source8_3wh, color3, "Hospitalized (n=" + str(sum8_3) + ")")
                    st.altair_chart(histo8_3, use_container_width=True)   
            
            elif chart_view == "Boxplots":
                with col20:
                    boks4_1 = create_boxplot_w(source4_1w, color1, "No NVP (n=" + str(sum4_1) + ")")
                    st.altair_chart(boks4_1, use_container_width=True)
                    boks4_2 = create_boxplot_w(source4_2w, color2, "No NVP (n=" + str(sum4_2) + ")")
                    st.altair_chart(boks4_2, use_container_width=True)
                    boks4_3 = create_boxplot_w(source4_3w, color3, "No NVP (n=" + str(sum4_3) + ")")
                    st.altair_chart(boks4_3, use_container_width=True)
                with col21: 
                    boks5_1w = create_boxplot_w(source5_1w, color1, "No NVP (n=" + str(sum5_1) + ")")
                    st.altair_chart(boks5_1w, use_container_width=True)
                    boks5_2 = create_boxplot_w(source5_2w, color2, "No NVP (n=" + str(sum5_2) + ")")
                    st.altair_chart(boks5_2, use_container_width=True)
                    boks5_3 = create_boxplot_w(source5_3w, color3, "No NVP (n=" + str(sum5_3) + ")")
                    st.altair_chart(boks5_3, use_container_width=True)
                with col22:
                    boks6_1 = create_boxplot_w(source6_1w, color1, "No NVP (n=" + str(sum6_1) + ")")
                    st.altair_chart(boks6_1, use_container_width=True)
                    boks6_2 = create_boxplot_w(source6_2w, color2, "No NVP (n=" + str(sum6_2) + ")")
                    st.altair_chart(boks6_2, use_container_width=True)
                    boks6_3 = create_boxplot_w(source6_3w, color3, "No NVP (n=" + str(sum6_3) + ")")
                    st.altair_chart(boks6_3, use_container_width=True)
                with col23:   
                    boks7_1 = create_boxplot_w(source7_1w, color1, "No NVP (n=" + str(sum7_1) + ")")
                    st.altair_chart(boks7_1, use_container_width=True)
                    boks7_2 = create_boxplot_w(source7_2w, color3, "No NVP (n=" + str(sum7_2) + ")")
                    st.altair_chart(boks7_2, use_container_width=True)
                    boks7_3 = create_boxplot_w(source7_3w, color3, "No NVP (n=" + str(sum7_3) + ")")
                    st.altair_chart(boks7_3, use_container_width=True)
                with col24:
                    boks8_1 = create_boxplot_w(source8_1w, color1, "No NVP (n=" + str(sum8_1) + ")")
                    st.altair_chart(boks8_1, use_container_width=True)
                    boks8_2 = create_boxplot_w(source8_2w, color2, "No NVP (n=" + str(sum8_2) + ")")
                    st.altair_chart(boks8_2, use_container_width=True)
                    boks8_3 = create_boxplot_w(source8_3w, color3, "No NVP (n=" + str(sum8_3) + ")")
                    st.altair_chart(boks8_3, use_container_width=True)

    # ##### FILTER DATA (DATA SUBSETS) FOR BOXPLOTS #####
    # # Load data set
    # data = pd.read_csv('data/data-5-box.csv', encoding='utf-8')

    # ### BIRTH LENGTH (DD14) ###
    # # No NVP
    # sub_CC388_len_1 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC388_len_1.to_csv('data/subdata/CC388_len_1.csv', index=False, encoding='utf-8') 
    # sub_CC389_len_1 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC389_len_1.to_csv('data/subdata/CC389_len_1.csv', index=False, encoding='utf-8') 
    # sub_CC390_len_1 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC390_len_1.to_csv('data/subdata/CC390_len_1.csv', index=False, encoding='utf-8') 
    # sub_CC391_len_1 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC391_len_1.to_csv('data/subdata/CC391_len_1.csv', index=False, encoding='utf-8') 
    # sub_CC392_len_1 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC392_len_1.to_csv('data/subdata/CC392_len_1.csv', index=False, encoding='utf-8')
    # # PNVP
    # sub_CC388_len_2 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC388_len_2.to_csv('data/subdata/CC388_len_2.csv', index=False, encoding='utf-8') 
    # sub_CC389_len_2 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC389_len_2.to_csv('data/subdata/CC389_len_2.csv', index=False, encoding='utf-8') 
    # sub_CC390_len_2 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC390_len_2.to_csv('data/subdata/CC390_len_2.csv', index=False, encoding='utf-8') 
    # sub_CC391_len_2 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC391_len_2.to_csv('data/subdata/CC391_len_2.csv', index=False, encoding='utf-8') 
    # sub_CC392_len_2 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC392_len_2.to_csv('data/subdata/CC392_len_2.csv', index=False, encoding='utf-8')
    # # hospitalized due to PNVP 
    # sub_CC141_len_3 = data.loc[(data.category == 'CC141').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC141_len_3.to_csv('data/subdata/CC141_len_3.csv', index=False, encoding='utf-8') 
    # sub_CC142_len_3 = data.loc[(data.category == 'CC142').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)] 
    # sub_CC142_len_3.to_csv('data/subdata/CC142_len_3.csv', index=False, encoding='utf-8') 
    # sub_CC143_len_3 = data.loc[(data.category == 'CC143').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC143_len_3.to_csv('data/subdata/CC143_len_3.csv', index=False, encoding='utf-8') 
    # sub_CC144_len_3 = data.loc[(data.category == 'CC144').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC144_len_3.to_csv('data/subdata/CC144_len_3.csv', index=False, encoding='utf-8') 
    # sub_CC145_len_3 = data.loc[(data.category == 'CC145').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC145_len_3.to_csv('data/subdata/CC145_len_3.csv', index=False, encoding='utf-8')

    # ### BIRTH WEIGHT (DD13) ###
    # # No NVP
    # sub_CC388_wei_1 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC388_wei_1.to_csv('data/subdata/CC388_wei_1.csv', index=False, encoding='utf-8') 
    # sub_CC389_wei_1 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC389_wei_1.to_csv('data/subdata/CC389_wei_1.csv', index=False, encoding='utf-8') 
    # sub_CC390_wei_1 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC390_wei_1.to_csv('data/subdata/CC390_wei_1.csv', index=False, encoding='utf-8') 
    # sub_CC391_wei_1 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC391_wei_1.to_csv('data/subdata/CC391_wei_1.csv', index=False, encoding='utf-8') 
    # sub_CC392_wei_1 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC392_wei_1.to_csv('data/subdata/CC392_wei_1.csv', index=False, encoding='utf-8') 
    # # NVP
    # sub_CC388_wei_2 = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC388_wei_2.to_csv('data/subdata/CC388_wei_2.csv', index=False, encoding='utf-8') 
    # sub_CC389_wei_2 = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC389_wei_2.to_csv('data/subdata/CC389_wei_2.csv', index=False, encoding='utf-8') 
    # sub_CC390_wei_2 = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC390_wei_2.to_csv('data/subdata/CC390_wei_2.csv', index=False, encoding='utf-8') 
    # sub_CC391_wei_2 = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC391_wei_2.to_csv('data/subdata/CC391_wei_2.csv', index=False, encoding='utf-8') 
    # sub_CC392_wei_2 = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC392_wei_2.to_csv('data/subdata/CC392_wei_2.csv', index=False, encoding='utf-8') 
    # # hospitalized due to PNVP
    # sub_CC141_wei_3 = data.loc[(data.category == 'CC141').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC141_wei_3.to_csv('data/subdata/CC141_wei_3.csv', index=False, encoding='utf-8') 
    # sub_CC142_wei_3 = data.loc[(data.category == 'CC142').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC142_wei_3.to_csv('data/subdata/CC142_wei_3.csv', index=False, encoding='utf-8') 
    # sub_CC143_wei_3 = data.loc[(data.category == 'CC143').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC143_wei_3.to_csv('data/subdata/CC143_wei_3.csv', index=False, encoding='utf-8') 
    # sub_CC144_wei_3 = data.loc[(data.category == 'CC144').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC144_wei_3.to_csv('data/subdata/CC144_wei_3.csv', index=False, encoding='utf-8') 
    # sub_CC145_wei_3 = data.loc[(data.category == 'CC145').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC145_wei_3.to_csv('data/subdata/CC145_wei_3.csv', index=False, encoding='utf-8')


    # ##### FILTER DATA (DATA SUBSETS) FOR HISTOGRAM #####

    # # Read data file for histograms
    # data = pd.read_csv('data/data-5-histo.csv', encoding='utf-8')

    # ### BIRTH LENGTH (DD14) ###
    # # No NVP
    # sub_CC388_len_1h = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC388_len_1h.to_csv('data/subdata/CC388_len_1h.csv', index=False, encoding='utf-8') 
    # sub_CC389_len_1h = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC389_len_1h.to_csv('data/subdata/CC389_len_1h.csv', index=False, encoding='utf-8') 
    # sub_CC390_len_1h = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC390_len_1h.to_csv('data/subdata/CC390_len_1h.csv', index=False, encoding='utf-8') 
    # sub_CC391_len_1h = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC391_len_1h.to_csv('data/subdata/CC391_len_1h.csv', index=False, encoding='utf-8') 
    # sub_CC392_len_1h = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC392_len_1h.to_csv('data/subdata/CC392_len_1h.csv', index=False, encoding='utf-8')
    # # PNVP
    # sub_CC388_len_2h = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC388_len_2h.to_csv('data/subdata/CC388_len_2h.csv', index=False, encoding='utf-8') 
    # sub_CC389_len_2h = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC389_len_2h.to_csv('data/subdata/CC389_len_2h.csv', index=False, encoding='utf-8') 
    # sub_CC390_len_2h = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC390_len_2h.to_csv('data/subdata/CC390_len_2h.csv', index=False, encoding='utf-8') 
    # sub_CC391_len_2h = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC391_len_2h.to_csv('data/subdata/CC391_len_2h.csv', index=False, encoding='utf-8') 
    # sub_CC392_len_2h = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC392_len_2h.to_csv('data/subdata/CC392_len_2h.csv', index=False, encoding='utf-8')
    # # hospitalized due to PNVP 
    # sub_CC141_len_3h = data.loc[(data.category == 'CC141').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC141_len_3h.to_csv('data/subdata/CC141_len_3h.csv', index=False, encoding='utf-8') 
    # sub_CC142_len_3h = data.loc[(data.category == 'CC142').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)] 
    # sub_CC142_len_3h.to_csv('data/subdata/CC142_len_3h.csv', index=False, encoding='utf-8') 
    # sub_CC143_len_3h = data.loc[(data.category == 'CC143').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC143_len_3h.to_csv('data/subdata/CC143_len_3h.csv', index=False, encoding='utf-8') 
    # sub_CC144_len_3h = data.loc[(data.category == 'CC144').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC144_len_3h.to_csv('data/subdata/CC144_len_3h.csv', index=False, encoding='utf-8') 
    # sub_CC145_len_3h = data.loc[(data.category == 'CC145').reset_index(drop=True) & (data.outcome == 'DD14').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC145_len_3h.to_csv('data/subdata/CC145_len_3h.csv', index=False, encoding='utf-8')

    # ### BIRTH WEIGHT (DD13) ###
    # # No NVP
    # sub_CC388_wei_1h = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC388_wei_1h.to_csv('data/subdata/CC388_wei_1h.csv', index=False, encoding='utf-8') 
    # sub_CC389_wei_1h = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC389_wei_1h.to_csv('data/subdata/CC389_wei_1h.csv', index=False, encoding='utf-8') 
    # sub_CC390_wei_1h = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC390_wei_1h.to_csv('data/subdata/CC390_wei_1h.csv', index=False, encoding='utf-8') 
    # sub_CC391_wei_1h = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC391_wei_1h.to_csv('data/subdata/CC391_wei_1h.csv', index=False, encoding='utf-8') 
    # sub_CC392_wei_1h = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '0').reset_index(drop=True)]
    # sub_CC392_wei_1h.to_csv('data/subdata/CC392_wei_1h.csv', index=False, encoding='utf-8') 
    # # NVP
    # sub_CC388_wei_2h = data.loc[(data.category == 'CC388').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC388_wei_2h.to_csv('data/subdata/CC388_wei_2h.csv', index=False, encoding='utf-8') 
    # sub_CC389_wei_2h = data.loc[(data.category == 'CC389').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC389_wei_2h.to_csv('data/subdata/CC389_wei_2h.csv', index=False, encoding='utf-8') 
    # sub_CC390_wei_2h = data.loc[(data.category == 'CC390').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC390_wei_2h.to_csv('data/subdata/CC390_wei_2h.csv', index=False, encoding='utf-8') 
    # sub_CC391_wei_2h = data.loc[(data.category == 'CC391').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC391_wei_2h.to_csv('data/subdata/CC391_wei_2h.csv', index=False, encoding='utf-8') 
    # sub_CC392_wei_2h = data.loc[(data.category == 'CC392').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == '1').reset_index(drop=True)]
    # sub_CC392_wei_2h.to_csv('data/subdata/CC392_wei_2h.csv', index=False, encoding='utf-8') 
    # # hospitalized due to PNVP
    # sub_CC141_wei_3h = data.loc[(data.category == 'CC141').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC141_wei_3h.to_csv('data/subdata/CC141_wei_3h.csv', index=False, encoding='utf-8') 
    # sub_CC142_wei_3h = data.loc[(data.category == 'CC142').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC142_wei_3h.to_csv('data/subdata/CC142_wei_3h.csv', index=False, encoding='utf-8') 
    # sub_CC143_wei_3h = data.loc[(data.category == 'CC143').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC143_wei_3h.to_csv('data/subdata/CC143_wei_3h.csv', index=False, encoding='utf-8') 
    # sub_CC144_wei_3h = data.loc[(data.category == 'CC144').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC144_wei_3h.to_csv('data/subdata/CC144_wei_3h.csv', index=False, encoding='utf-8') 
    # sub_CC145_wei_3h = data.loc[(data.category == 'CC145').reset_index(drop=True) & (data.outcome == 'DD13').reset_index(drop=True) & (data.level == 1).reset_index(drop=True)]
    # sub_CC145_wei_3h.to_csv('data/subdata/CC145_wei_3h.csv', index=False, encoding='utf-8') 