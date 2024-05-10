####################
DATA FILES INCLUDED:

The data folder includes three csv files that are preprocessed in the following manner:
1. data-5-box.csv: missing values are deleted to not influence the mean and standard deviation of the boxplots, values with <10 are transfered to 5
2. data-5-histo.csv: includes missing data encoded as "0", values with <10 are transfered to 5
3. A third data file, sumstats.csv, is used for the child development line chart visualization and statistics. (This was the original data file provided by our data/content expert, Marc Vaudel).


##########################
INSTALLATION REQUIREMENTS:

1. Safe the folder "Streamlit"

2. Virtual Environment
Change directory:           cd .\Streamlit> 
Create virtual environment: python3 -m venv venv
Activate environment:       .\venv\Scripts\activate

3. Install libaries in the environment
python3 pip install streamlit, altair, pandas, numpy

4. Choose the environment Kernel 

5. Choose Python Version in the bottom right, e.g., 3.12

6. Run streamlit in browser via Terminal: 
streamlit run d:\_UniBergen\INF252_Vis\PROJECT-HG-children-development\Streamlit\main.py
*If using VS Code, open main.py and execute the streamlit app in the Terminal with the following line: python3 -m streamlit run main.py

###################
ABOUT THIS PROJECT:

Version: 2.0
Last updated: 2024-05-10

About:
This data dashboard was developed for the course INF252, Visualization, Spring semester 2024 at the University of Bergen. We collaborated with Marc Vaudel, a genetic epidemiologist, to develop visualizations that allow experts to explore possible correlations between pregnancy health (specifically the condition hyperemesis gravidarum, HG) and child phenotypic outcomes, namely height and weight. We plan to expand this dashboard with other visualization types and additional variables of interest for conducting this research.

Libraries and tools used:
Pandas, NumPy, Vega-Altair, Streamlit app development
plus all relevant documentation. ChatGPT for occasional debugging.

Current issues/bugs to be fixed:
1. Statistical views for child development line chart still not functional. Code is partly there but not loading, yet.
2. Slow loading for some pages on front-end. Need to work with Streamlit's features for managing large data sets.
3. Annotation to designate missing values in histograms not working (attempted multiple ways to implement in the altair visualizations, e.g. changing label for '0' on x-axis, adding a symbol above the value, changing color, but we have not gotten these to work, yet.)
4. Optimize layout by removing redundant headers above charts in each column (if #s are the same).

Future work:
1. Fix issues/bugs listed above.
2. Adapt child development chart to match clinical charts more closely.
3. Figure out how to further customize Streamlit layout to minimize white space and add more data views for experts.
4. Update boys/girls data (raw data and visualizations) to enable brushing interaction between histograms and boy/girl detailed view.
5. Add aria-labels for enhanced accessibility.
6. Add new variables for further exploration.

About uncertainty:
Follow-on work related to this project will involve an exploration of the issue of uncertainty. This includes how uncertainty is introduced at all stages of data collection, analysis/processing, and visualization, with consequences for clinical research of rare diseases as well as broader societal/cultural implications. DUE: June 14th.


################
ACKNOWLEDGMENTS:
Supervisor: Laura Garrison, PhD, Associate Professor, Depart. of Informatics, University of Bergen
Content expert: Marc Vaudel, PhD, Associate Professor, Dept. of Clinical Science, University of Bergen
Special thanks: David Grellscheid (tech/data processing help), Eduard Gröller (design input), INF252 classmates (ongoing feedback)