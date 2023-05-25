import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('new_updated_ipd5.csv')
df2=pd.read_csv('IPL_Matches_2008_2022 (1).csv')
new_df=pd.read_csv('split1.csv',low_memory=False,index_col=False)
new_df1=pd.read_csv('split2.csv',low_memory=False,index_col=False)
new_df2=pd.read_csv('split3.csv',low_memory=False,index_col=False)
new_df3=pd.read_csv('split4.csv',low_memory=False,index_col=False)
new_df4=pd.read_csv('batter_runs_vs_team.csv')
new_df5=pd.read_csv('batter_6_vs_team.csv')
new_df6=pd.read_csv('batter_4_vs_team.csv')
new_df7=pd.read_csv('played_for_team.csv')
avg_df=pd.read_csv('batter (1).csv')
a = df[df['WonBy'].isna()].shape[0]


st.markdown('<h1 style="color:yellow;">IPL Analytics Dashboard(2008-2022)</h1>', unsafe_allow_html=True)
st.markdown('##### Discover the Thrill of Cricket Analysis')





teams=['Select Team','Chennai Super Kings','Deccan Chargers','Delhi Capitals','Delhi Daredevils','Gujarat Lions','Gujarat Titans','Kings XI Punjab',
       'Kochi Tuskers Kerala','Kolkata Knight Riders','Lucknow Super Giants', 'Mumbai Indians','Pune Warriors','Punjab Kings','Rajasthan Royals',
       'Rising Pune Supergiants','Royal Challengers Bangalore','Sunrisers Hyderabad']

players=['Select Player','A Ashish Reddy','A Badoni', 'A Chandila', 'A Chopra', 'A Choudhary', 'A Dananjaya',
 'A Flintoff', 'A Kumble', 'A Manohar', 'A Mishra', 'A Mithun', 'A Mukund', 'A Nehra', 'A Nel', 'A Nortje', 'A Singh' 'A Symonds', 'A Tomar', 'A Uniyal', 'A Zampa',
 'AA Bilakhia', 'AA Chavan', 'AA Jhunjhunwala', 'AA Kazi', 'AA Noffke', 'AB Agarkar', 'AB Barath', 'AB Dinda', 'AB McDonald', 'AB de Villiers', 'AC Blizzard',
 'AC Gilchrist', 'AC Thomas', 'AC Voges', 'AD Hales', 'AD Mascarenhas', 'AD Mathews', 'AD Nath', 'AD Russell', 'AF Milne', 'AG Murtaza', 'AG Paunikar', 'AJ Finch',
 'AJ Turner', 'AJ Tye', 'AK Markram', 'AL Menaria', 'AM Nayar', 'AM Rahane', 'AM Salvi', 'AN Ahmed', 'AN Ghosh', 'AP Dole', 'AP Majumdar', 'AP Tare', 'AR Bawne',
 'AR Patel', 'AS Joseph', 'AS Rajpoot', 'AS Raut', 'AS Roy', 'AS Yadav', 'AT Carey', 'AT Rayudu', 'AU Rashid', 'AUK Pathan', 'Abdul Samad', 'Abdur Razzak', 'Abhishek Sharma',
 'Akash Deep', 'Akash Singh', 'Aman Hakim Khan', 'Anand Rajan', 'Anirudh Singh', 'Ankit Sharma', 'Ankit Soni', 'Anmolpreet Singh', 'Anuj Rawat', 'Anureet Singh', 'Arshdeep Singh',
 'Avesh Khan', 'Azhar Mahmood', 'B Akhil', 'B Chipli', 'B Geeves','B Indrajith', 'B Kumar', 'B Laughlin', 'B Lee', 'B Sai Sudharsan', 'B Stanlake', 'B Sumanth',
 'BA Bhatt', 'BA Stokes', 'BAW Mendis', 'BB McCullum', 'BB Samantray', 'BB Sran', 'BCJ Cutting', 'BE Hendricks', 'BJ Haddin', 'BJ Hodge', 'BJ Rohrer', 'BMAJ Mendis',
 'BR Dunk', 'BW Hilfenhaus', 'Basil Thampi', 'Bipul Sharma', 'C Ganapathy', 'C Madan', 'C Munro', 'C Nanda', 'C Sakariya', 'C de Grandhomme', 'CA Ingram',
 'CA Lynn', 'CA Pujara', 'CH Gayle', 'CH Morris', 'CJ Anderson', 'CJ Dala', 'CJ Ferguson', 'CJ Green', 'CJ Jordan', 'CJ McKay', 'CK Kapugedera', 'CK Langeveldt', 'CL White',
 'CM Gautam', 'CR Brathwaite', 'CR Woakes', 'CRD Fernando', 'CV Varun','D Brevis','D Kalyankrishna', 'D Padikkal', 'D Pretorius', 'D Salunkhe', 'D Wiese',
 'D du Preez', 'DA Miller', 'DA Warner', 'DAJ Bracewell', 'DB Das', 'DB Ravi Teja', 'DE Bollinger', 'DG Nalkande', 'DH Yagnik', 'DJ Bravo', 'DJ Harris', 'DJ Hooda',
 'DJ Hussey', 'DJ Jacobs', 'DJ Malan', 'DJ Mitchell', 'DJ Muthuswami', 'DJ Thornely', 'DJ Willey', 'DJG Sammy', 'DJM Short', 'DL Chahar', 'DL Vettori', 'DM Bravo', 'DNT Zoysa',
 'DP Conway', 'DP Nannes', 'DP Vijaykumar', 'DPMD Jayawardene', 'DR Martyn', 'DR Sams',
 'DR Shorey', 'DR Smith', 'DS Kulkarni', 'DS Lehmann', 'DT Christian', 'DT Patil', 'DW Steyn', 'E Lewis', 'EJG Morgan', 'ER Dwivedi', 'F Behardien', 'F du Plessis',
 'FA Allen', 'FH Edwards', 'FY Fazal', 'Fazalhaq Farooqi', 'G Gambhir','GB Hogg', 'GC Smith', 'GC Viljoen', 'GD McGrath', 'GD Phillips', 'GH Vihari', 'GHS Garton',
 'GJ Bailey', 'GJ Maxwell', 'GR Napier', 'GS Sandhu', 'Gagandeep Singh', 'Gurkeerat Singh', 'H Das', 'H Klaasen', 'HE van der Dussen', 'HF Gurney', 'HH Gibbs','HH Pandya',
 'HM Amla', 'HR Shokeen','HV Patel', 'Harbhajan Singh', 'Harmeet Singh', 'Harpreet Brar','Harpreet Singh', 'Harshit Rana', 'I Malhotra', 'I Sharma', 'I Udana',
 'IC Pandey', 'IC Porel', 'IK Pathan', 'IR Jaggi', 'IS Sodhi', 'Imran Tahir', 'Iqbal Abdulla', 'Ishan Kishan', 'J Arunkumar', 'J Botha', 'J Suchith', 'J Syed Mohammad',
 'J Theron', 'J Yadav', 'JA Morkel', 'JA Richardson', 'JC Archer', 'JC Buttler', 'JD Ryder', 'JD Unadkat', 'JDP Oram', 'JDS Neesham', 'JE Taylor',
 'JEC Franklin' 'JH Kallis', 'JJ Bumrah', 'JJ Roy', 'JJ van der Wath', 'JL Denly', 'JL Pattinson', 'JM Bairstow', 'JM Kemp', 'JM Sharma', 'JO Holder', 'JP Behrendorff',
 'JP Duminy', 'JP Faulkner', 'JPR Scantlebury-Searles', 'JR Hazlewood', 'JR Hopes', 'JR Philippe', 'JW Hastings', 'Jalaj S Saxena', 'Jaskaran Singh',
 'Joginder Sharma', 'K Goel', 'K Gowtham', 'K Kartikeya', 'K Khejroliya', 'K Rabada', 'K Santokie', 'K Upadhyay', 'K Yadav', 'KA Jamieson', 'KA Pollard',
 'KAJ Roach', 'KB Arun Karthik', 'KC Cariappa', 'KC Sangakkara', 'KD Karthik', 'KH Pandya', 'KJ Abbott', 'KK Ahmed','KK Cooper',
 'KK Nair', 'KL Nagarkoti', 'KL Rahul', 'KM Asif', 'KM Jadhav', 'KMA Paul', 'KMDN Kulasekara','KP Appanna','KP Pietersen', 'KR Sen', 'KS Bharat', 'KS Sharma',
 'KS Williamson', 'KV Sharma', 'KW Richardson', 'Kamran Akmal', 'Kamran Khan', 'Karanveer Singh', 'Kartik Tyagi', 'Kuldeep Yadav',
 'L Ablish', 'L Balaji', 'L Ngidi', 'L Ronchi', 'LA Carseldine', 'LA Pomersbach', 'LE Plunkett',
 'LH Ferguson', 'LI Meriwala','LJ Wright', 'LMP Simmons', 'LPC Silva', 'LR Shukla', 'LRPL Taylor', 'LS Livingstone', 'Lalit Yadav', 'M Ashwin', 'M Jansen', 'M Kaif', 'M Kartik',
 'M Klinger', 'M Manhas', 'M Markande', 'M Morkel', 'M Muralitharan', 'M Ntini', 'M Pathirana', 'M Prasidh Krishna', 'M Rawat', 'M Shahrukh Khan', 'M Theekshana',
 'M Vijay', 'M Vohra', 'M de Lange', 'MA Agarwal', 'MA Khote', 'MA Starc', 'MA Wood', 'MB Parmar', 'MC Henriques', 'MC Juneja', 'MD Mishra',
 'MDKJ Perera','MEK Hussey', 'MF Maharoof', 'MG Johnson','MG Neser', 'MJ Clarke', 'MJ Guptill', 'MJ Henry', 'MJ Lumb', 'MJ McClenaghan', 'MJ Santner', 'MK Lomror',
 'MK Pandey', 'MK Tiwary', 'ML Hayden', 'MM Ali', 'MM Patel', 'MM Sharma', 'MN Samuels', 'MN van Wyk', 'MP Stoinis', 'MR Marsh', 'MS Bisla',
 'MS Dhoni','MS Gony', 'MS Wade','MV Boucher','Mandeep Singh','Mashrafe Mortaza','Misbah-ul-Haq', 'Mohammad Ashraful','Mohammad Asif','Mohammad Hafeez',
 'Mohammad Nabi', 'Mohammed Shami', 'Mohammed Siraj', 'Mohsin Khan', 'Monu Kumar', 'Mujeeb Ur Rahman', 'Mukesh Choudhary', 'Mustafizur Rahman', 'N Jagadeesan',
 'N Pooran', 'N Rana', 'N Saini', 'NB Singh', 'ND Doshi','NJ Maddinson','NJ Rimmington', 'NK Patel', 'NL McCullum', 'NLTC Perera', 'NM Coulter-Nile', 'NS Naik', 'NT Ellis',
 'NV Ojha', 'Navdeep Saini', 'O Thomas', 'OA Shah', 'OC McCoy', 'OF Smith', 'P Amarnath',
 'P Awana', 'P Chopra', 'P Dogra', 'P Dubey', 'P Kumar', 'P Negi', 'P Parameswaran', 'P Prasanth', 'P Ray Barman', 'P Sahu', 'P Simran Singh', 'P Suyal',
 'PA Patel', 'PA Reddy', 'PBB Rajapaksa', 'PC Valthaty','PD Collingwood', 'PH Solanki', 'PJ Cummins', 'PJ Sangwan', 'PK Garg', 'PM Sarvesh Kumar', 'PN Mankad', 'PP Chawla',
 'PP Ojha', 'PP Shaw', 'PR Shah', 'PSP Handscomb', 'PV Tambe', 'PVD Chameera', 'PWH de Silva', 'Pankaj Singh',
 'Parvez Rasool', 'Q de Kock', 'R Ashwin', 'R Bhatia', 'R Bishnoi', 'R Dhawan', 'R Dravid', 'R McLaren','R Ninan', 'R Parag','R Powell', 'R Rampaul',
 'R Sai Kishore', 'R Sanjay Yadav', 'R Sathish', 'R Sharma', 'R Shepherd', 'R Shukla', 'R Tewatia', 'R Vinay Kumar','RA Bawa', 'RA Jadeja',
 'RA Shaikh', 'RA Tripathi', 'RD Chahar', 'RD Gaikwad', 'RE Levi', 'RE van der Merwe', 'RG More','RG Sharma', 'RJ Harris', 'RJ Peterson', 'RJ Quiney', 'RK Bhui',
 'RK Singh', 'RM Patidar', 'RN ten Doeschate','RP Meredith', 'RP Singh', 'RR Bhatkal', 'RR Bose', 'RR Pant', 'RR Powar', 'RR Raje', 'RR Rossouw',
 'RR Sarwan', 'RS Bopara', 'RS Gavaskar', 'RS Sodhi', 'RT Ponting','RV Gomez', 'RV Patel','RV Uthappa', 'RW Price', 'Ramandeep Singh', 'Rashid Khan',
 'Rasikh Salam', 'Ravi Bishnoi', 'S Anirudha', 'S Aravind', 'S Badree', 'S Badrinath', 'S Chanderpaul', 'S Dhawan', 'S Dube','S Gopal', 'S Kaul','S Kaushik',
 'S Ladda', 'S Lamichhane','S Midhun','S Nadeem', 'S Narwal', 'S Rana','S Randiv', 'S Sandeep Warrier','S Sohal', 'S Sreesanth','S Sriram','S Tyagi',
 'S Vidyut', 'SA Abbott', 'SA Asnodkar', 'SA Yadav','SB Bangar','SB Jakati','SB Joshi', 'SB Styris','SB Wagh', 'SC Ganguly','SC Kuggeleijn', 'SD Chitnis','SD Lad',
 'SE Bond','SE Marsh', 'SE Rutherford','SJ Srivastava','SK Raina','SK Trivedi','SK Warne','SL Malinga','SM Boland','SM Curran', 'SM Harwood',
 'SM Katich','SM Pollock', 'SMSM Senanayake', 'SN Khan', 'SN Thakur','SO Hetmyer', 'SP Fleming','SP Goswami','SP Jackson','SP Narine',
 'SPD Smith', 'SR Tendulkar','SR Watson','SS Agarwal','SS Cottrell', 'SS Iyer','SS Mundhe','SS Prabhudessai','SS Sarkar','SS Shaikh',
 'SS Tiwary','ST Jayasuriya','STR Binny', 'SV Samson','SW Billings', 'SW Tait','Sachin Baby','Salman Butt','Sandeep Sharma','Shahbaz Ahmed',
 'Shahid Afridi','Shakib Al Hasan','Shashank Singh','Shivam Mavi','Shivam Sharma','Shoaib Ahmed','Shoaib Akhtar','Shoaib Malik','Shubman Gill',
 'Simarjeet Singh','Sohail Tanvir','Sunny Gupta','Sunny Singh','Swapnil Singh','T Banton','T Henderson','T Kohli','T Natarajan',
 'T Shamsi','T Stubbs','T Taibu','T Thushara','TA Boult','TD Paine','TG Southee','TH David','TK Curran','TL Seifert',
 'TL Suman','TM Dilshan', 'TM Head','TM Srivastava','TP Sudhindra','TR Birt','TS Mills','TU Deshpande','Tejas Baroka','Tilak Varma','U Kaul',
 'UA Birla','UBT Chand','UT Khawaja','UT Yadav','Umar Gul','Umran Malik','V Kohli','V Pratap Singh','V Sehwag','V Shankar','VG Arora',
 'VH Zol','VR Aaron','VR Iyer','VRV Singh','VS Malik','VS Yeligati','VVS Laxman','VY Mahesh','Virat Singh','Vishnu Vinod',
 'W Jaffer','WA Mota','WD Parnell','WP Saha','WPUJC Vaas','Washington Sundar','X Thalaivan Sargunam','Y Gnaneswara Rao','Y Nagar','Y Prithvi Raj','Y Venugopal Rao',
 'YA Abdulla', 'YBK Jaiswal','YK Pathan','YS Chahal','YV Takawale','Yash Dayal','Yashpal Singh','Younis Khan','Yuvraj Singh','Z Khan']

stadiums=['Select Stadium','Arun Jaitley Stadium, Delhi', 'Barabati Stadium, Cuttack',  'Brabourne Stadium, Mumbai', 'Buffalo Park, East London',
       'De Beers Diamond Oval, Kimberley', 'Dr DY Patil Sports Academy, Mumbai',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam','Dubai International Cricket Stadium, Dubai',
       'Eden Gardens, Kolkata', 'Green Park, Kanpur','Himachal Pradesh Cricket Association Stadium, Dharamsala',
       'Holkar Cricket Stadium, Indore','JSCA International Stadium Complex, Ranchi', 'Kingsmead, Durban',
       'M.Chinnaswamy Stadium, Bengaluru','MA Chidambaram Stadium, Chennai','Maharashtra Cricket Association Stadium, Pune',
       'Narendra Modi Stadium, Ahmedabad', 'Nehru Stadium, Kochi', 'New Wanderers Stadium, Johannesburg', 'Newlands,Cape Town',
       'OUTsurance Oval,Bloemfontein','Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Rajiv Gandhi International Stadium, Hyderabad','Saurashtra Cricket Association Stadium, Rajkot','Sawai Mansingh Stadium,Jaipur',
       'Shaheed Veer Narayan Singh International Stadium, Raipur', 'Sharjah Cricket Stadium, Sharjah',
       'Sheikh Zayed Stadium, Abu Dhabi',"St George's Park, Port Elizabeth", 'SuperSport Park, Centurion', 'Vidarbha Cricket Association Stadium, Nagpur',
       'Wankhede Stadium, Mumbai', 'Zayed Cricket Stadium, Abu Dhabi']



# Main Code Start


st.sidebar.markdown('<h1 style="color:yellow;">IPL Encyclopedia</h1>', unsafe_allow_html=True)
st.sidebar.markdown('##### Thrilling Highlights and Memorable Performances')
analysis = st.sidebar.selectbox('Select Analysis Type',['Overall','Teamwise Analysis','Playerwise Analysis','Stadiumwise Analysis'])

if analysis=='Teamwise Analysis':
    selected_option=st.sidebar.selectbox('Please Select Team',teams)

elif analysis=='Playerwise Analysis':
    selected_option=st.sidebar.selectbox('Please Select Player',players)

elif analysis=='Stadiumwise Analysis':
    selected_option=st.sidebar.selectbox('Please Select Stadium',stadiums)


# 1. Teamwise Analysis Start

if (analysis=='Teamwise Analysis' and selected_option!='Select Team'):
 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### Matches Played\t')
  st.title(df[(df['Team1']==selected_option)| (df['Team2']==selected_option)].shape[0])

 with col2:
  st.markdown(' ### Matches Won\t')
  st.title(df['WinningTeam'].value_counts()[selected_option])

 with col3:
  st.markdown(' ### Matches lose\t')
  st.title(df[(df['Team1']==selected_option)| (df['Team2']==selected_option)][df['WinningTeam']!=selected_option].shape[0])

 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### Winning Percent %\t')
  won=df['WinningTeam'].value_counts()[selected_option]
  total=df[(df['Team1']==selected_option)| (df['Team2']==selected_option)].shape[0]
  st.title(round((won/total)*100,2))

 with col2:
  st.markdown(' ### Final Played\t')
  st.title(df[df['MatchNumber']=='Final'][(df['Team1']==selected_option) | (df['Team2']==selected_option)].shape[0])

 with col3:
  st.markdown(' ### Final Won\t')
  df1 = df[df['MatchNumber'] == 'Final'][(df['Team1'] == selected_option) | (df['Team2'] == selected_option)]
  st.title(df1[df1['WinningTeam'] == selected_option].shape[0])

 st.markdown('<h2 style="color:yellow;">Seasonwise Team Performance </h2>', unsafe_allow_html=True)
 wons = df[(df['Team1'] == selected_option) | (df['Team2'] == selected_option)]
 wons=wons[(wons['WinningTeam'] == selected_option) & (wons['MatchNumber'].str.isdigit())].groupby('Season')[
  'WinningTeam'].count().reset_index()

 fig = make_subplots(rows=1, cols=2, subplot_titles=(
  "Seasonwise Matches won Line graph", "Seasonwise Matches won Bar graph"))
 fig.add_trace(go.Scatter(x=wons['Season'], y=wons['WinningTeam'], name='Matches won'), row=1, col=1)

 # Add bar graph trace
 fig.add_trace(go.Bar(x=wons['Season'], y=wons['WinningTeam'], name='Matches won', marker_color='orange'), row=1,
               col=2)
 fig.update_xaxes(tickmode='array', tickvals=wons['Season'], dtick=1)

 fig.update_xaxes(title_text='Season', row=1, col=1)
 fig.update_xaxes(title_text='Season', row=1, col=2)
 fig.update_yaxes(title_text='Matches Won', row=1, col=1)
 fig.update_yaxes(title_text='Matches Won', row=1, col=2)
 # Update layout
 fig.update_layout(height=400, width=800, showlegend=False)


 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Seasonwise Top Run Scorer </h2>', unsafe_allow_html=True)
 team_df = new_df[(new_df['Team1'] == selected_option) | (new_df['Team2'] == selected_option)]
 player_run = team_df.groupby(['Season', 'batter'])['batsman_run'].sum().sort_values(
  ascending=False).reset_index().drop_duplicates(subset='Season', keep='first')
 player_run = player_run.sort_values(by='Season')
 fig = go.Figure(data=go.Bar(x=player_run['Season'], y=player_run['batsman_run'],text=player_run['batter'], textposition='auto', marker_color='orange'))
 fig.update_layout(title=selected_option + ' Top Run Scorer', xaxis_title='Season', yaxis_title='Runs Scored')
 st.plotly_chart(fig)





 st.markdown('<h2 style="color:yellow;">Seasonwise Top Wicket Taker </h2>', unsafe_allow_html=True)
 team_df = new_df[(new_df['Team1'] == selected_option) | (new_df['Team2'] == selected_option)]
 player_run = team_df.groupby(['Season', 'bowler'])['isWicketDelivery'].sum().sort_values(
  ascending=False).reset_index().drop_duplicates(subset='Season', keep='first')
 player_run = player_run.sort_values(by='Season')
 fig = go.Figure(
  data=go.Bar(x=player_run['Season'], y=player_run['isWicketDelivery'], text=player_run['bowler'], textposition='auto',
              marker_color='orange'))
 fig.update_layout(title=selected_option + ' Top Wicket Taker', xaxis_title='Season', yaxis_title='Wicket Taken')
 st.plotly_chart(fig)


 st.markdown('<h2 style="color:yellow;">Seasonwise Highest Run </h2>', unsafe_allow_html=True)
 team_df = new_df[(new_df['Team1'] == selected_option) | (new_df['Team2'] == selected_option)]
 player_run=team_df.groupby(['Season','ID','innings'])[['batsman_run','isWicketDelivery','extras_run']].sum().sort_values(by='batsman_run',ascending=False).reset_index().drop_duplicates(subset='Season',keep='first')
 player_run=player_run.sort_values(by='Season')
 player_run['total_run'] = player_run['batsman_run'] + player_run['extras_run']
 player_run['run_wicket'] = player_run['total_run'].astype(str) + '-' + player_run['isWicketDelivery'].astype(str)

 fig = go.Figure(
  data=go.Bar(x=player_run['Season'], y=player_run['total_run'], text=player_run['run_wicket'], textposition='auto',
              marker_color='orange'))
 fig.update_layout(title=selected_option + ' Seasonwise Highest Runs', xaxis_title='Season', yaxis_title='Runs')
 st.plotly_chart(fig)



 st.markdown('<h2 style="color:yellow;">Seasonwise Lowest Run </h2>', unsafe_allow_html=True)
 team_df = new_df[(new_df['Team1'] == selected_option) | (new_df['Team2'] == selected_option)]
 player_run = team_df.groupby(['Season', 'ID', 'innings'])[
  ['batsman_run', 'isWicketDelivery', 'extras_run']].sum().sort_values(by='batsman_run',
                                                                       ).reset_index().drop_duplicates(
  subset='Season', keep='first')
 player_run = player_run.sort_values(by='Season')
 player_run['total_run'] = player_run['batsman_run'] + player_run['extras_run']
 player_run['run_wicket'] = player_run['total_run'].astype(str) + '-' + player_run['isWicketDelivery'].astype(str)

 fig = go.Figure(
  data=go.Bar(x=player_run['Season'], y=player_run['total_run'], text=player_run['run_wicket'], textposition='auto',
              marker_color='orange'))
 fig.update_layout(title=selected_option + ' Seasonwise Lowest Runs', xaxis_title='Season', yaxis_title='Runs')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Team Runs Distribution  </h2>', unsafe_allow_html=True)
 batsman_stat = new_df[new_df['battingteam'] == selected_option]['batsman_run'].value_counts()
 labels = batsman_stat.index.astype(str)
 values = batsman_stat.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option + ' runs distribution')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Team Dismissals Distribution </h2>', unsafe_allow_html=True)
 out = new_df[new_df['battingteam'] == selected_option]['kind'].value_counts()
 labels = out.index.astype(str)
 values = out.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option + ' dismissals distribution')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Team Wickets Taken Distribution </h2>', unsafe_allow_html=True)
 out = new_df1[new_df1['bowlingteam'] == selected_option]['kind'].value_counts()
 labels = out.index.astype(str)
 values = out.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option + ' wickets taken distribution')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Head to Head Matches </h2>', unsafe_allow_html=True)
 col1,col2=st.columns(2)
 with col1:
  st.selectbox('Please Select Team1',[selected_option])
 with col2:

  team2=st.selectbox('Please Select Team2',teams)

 if ((team2!=selected_option) and (team2!='Select Team')):
  btnh=st.button('Show Analysis')

  if btnh:
   col1, col2,col3,col4 = st.columns(4)
   with col1:
    st.markdown(' ### Matches \t')
    t1 = df[(df['Team1'] == selected_option) | (df['Team2'] == selected_option)]
    matches_palyed = t1[(t1['Team1'] == team2) | (t1['Team2'] == team2)].shape[0]
    st.title(matches_palyed)

   with col2:
    st.markdown(' ### Team1 Won\t')
    team1_win = t1[(t1['Team1'] == team2) | (t1['Team2'] == team2)]
    team1_win_num = team1_win[team1_win['WinningTeam'] == selected_option].shape[0]
    st.title(team1_win_num)


   with col3:
    st.markdown(' ### Team2 Won')
    team2_win_num = t1[t1['WinningTeam'] == team2].shape[0]
    st.title(team2_win_num)
   with col4:
    st.markdown(' ### No Result')
    st.title(matches_palyed-team1_win_num-team2_win_num)
   q=pd.DataFrame({'Team_Name':[selected_option,team2],'Matches_won':[team1_win_num,team2_win_num]})
   fig = go.Figure(
   data = go.Bar(x=q['Team_Name'], y=q['Matches_won'], text=q['Team_Name'], textposition='auto',
                 marker_color='orange'))
   fig.update_layout(title=selected_option + ' vs '+team2, xaxis_title='Team Name', yaxis_title='No. of Matches Win')
   st.plotly_chart(fig)




# 2. Playerwise Analysis

elif (analysis=='Playerwise Analysis' and selected_option!='Select Player'):
 col1, col2, col3,col4,col5 = st.columns(5)

 with col1:
  st.markdown(' ### Matches Played\t')
  player_matches=df2[df2['Team1Players'].str.contains(selected_option)].shape[0]+df2[df2['Team2Players'].str.contains(selected_option)].shape[0]
  st.title(player_matches)
 with col2:
  st.markdown(' ### Total Runs in IPL\t')
  batter = new_df.groupby('batter')['batsman_run'].sum().reset_index()
  batter1 = batter.set_index('batter')
  if (new_df[new_df['batter'].str.contains(selected_option)].shape[0]==0):
   st.title(0)
  else:
   st.title(batter1.loc[selected_option, 'batsman_run'])
 with col3:
  st.markdown(' ### No. of Sixes\t')
  st.title(new_df[(new_df['batter'] == selected_option) & (new_df['batsman_run'] == 6)].shape[0])


  with col4:
   st.markdown(' ### No. of Fours\t')
   st.title(new_df[(new_df['batter'] == selected_option) & (new_df['batsman_run'] == 4)].shape[0])

  with col5:
   st.markdown(' ### Half-Century\t')
   halfc = new_df[new_df['batter'] == selected_option].groupby('ID')['batsman_run'].sum().sort_values(
    ascending=False).reset_index()
   st.title(halfc[(halfc['batsman_run']>=50) & (halfc['batsman_run']<100) ].shape[0])

 col1, col2, col3,col4,col5 = st.columns(5)

 with col1:
  st.markdown(' ### No. of Century\t')
  st.title(halfc[halfc['batsman_run']>=100].shape[0])

 with col2:
  st.markdown(' ### Highest  Score\t')
  st.title(new_df[new_df['batter']==selected_option].groupby('ID')['batsman_run'].sum().sort_values(ascending=False).reset_index().loc[0,'batsman_run'])


 with col3:
  st.markdown(' ### No. of Notouts')
  out = new_df1[(new_df1['batter'] == selected_option) & (new_df1['isWicketDelivery'] == 1) & (new_df1['player_out'] == selected_option)].shape[0] + new_df1[(new_df1['non-striker'] == selected_option) & (new_df1['isWicketDelivery'] == 1) & (new_df1['player_out'] == selected_option)].shape[0]
  st.title(player_matches - out)

 with col4:
  st.markdown(' ### No. of Wickets\t')
  bowler = new_df.groupby('bowler')['isWicketDelivery'].sum().reset_index()
  bowler1 = bowler.set_index('bowler')
  if (new_df[new_df['bowler'].str.contains(selected_option)].shape[0] == 0):
   st.title('NA')
  else:
   st.title(bowler1.loc[selected_option, 'isWicketDelivery'])

 with col5:
  st.markdown(' ### Best Bowling')
  if (new_df[new_df['bowler'].str.contains(selected_option)].shape[0] == 0):
   st.title('NA')
  else:
   wickets = new_df[new_df['bowler'] == selected_option].groupby('ID')['isWicketDelivery'].sum().sort_values(ascending=False).reset_index().loc[0, 'isWicketDelivery']
   run = new_df[new_df['bowler'] == selected_option].groupby('ID')['isWicketDelivery'].sum().sort_values(ascending=False).reset_index().loc[0, 'ID']
   runs = new_df[(new_df["ID"] == run) & (new_df['bowler'] == selected_option)]['total_run'].sum()
   best_bowling = f"{runs}-{wickets}"
   st.title(best_bowling)

 st.markdown('<h2 style="color:yellow;">Player Seasonwise Performance</h2>', unsafe_allow_html=True)
 s = new_df[new_df['batter'] == selected_option]
 s = s.groupby('Season')['batsman_run'].sum().reset_index()
 s = s.sort_values('Season')

 fig = make_subplots(rows=1, cols=2, subplot_titles=(
 "Player Performance Seasonwise Line Graph", "Player Performance Seasonwise Bar Graph"))
 fig.add_trace(go.Scatter(x=s['Season'], y=s['batsman_run'], name='Line Graph'), row=1, col=1)

 # Add bar graph trace
 fig.add_trace(go.Bar(x=s['Season'], y=s['batsman_run'], name='Bar Graph', marker_color='orange'), row=1, col=2)
 fig.update_xaxes(tickmode='array', tickvals=s['Season'], dtick=1)

 fig.update_xaxes(title_text='Season', row=1, col=1)
 fig.update_xaxes(title_text='Season', row=1, col=2)
 fig.update_yaxes(title_text='Runs Scored', row=1, col=1)
 fig.update_yaxes(title_text='Runs Scored', row=1, col=2)
 # Update layout
 fig.update_layout(height=400, width=800, showlegend=False)

 # Display the graph in Streamlit
 st.plotly_chart(fig)



 st.markdown('<h2 style="color:yellow;">Player vs Other Teams </h2>', unsafe_allow_html=True)
 s = new_df4[new_df4['batter'] == selected_option]
 # s['againstTeam'] = ''
 # # Iterate over each row in the DataFrame
 # for index, row in s.iterrows():
 #  # Check if the toss decision is 'batting' or 'fielding'
 #  if selected_option in row['Team1Players']:
 #   s.at[index, 'againstTeam'] = row['Team2']
 #  elif selected_option in row['Team2Players']:
 #   s.at[index, 'againstTeam'] = row['Team1']
 # s = s.groupby('againstTeam')['batsman_run'].sum().sort_values(ascending=False).reset_index()
 fig = go.Figure(data=go.Bar(x=s['againstTeam'], y=s['batsman_run'], marker_color='orange'))
 fig.update_layout(title=selected_option+' vs Other Teams',xaxis_title='Teams Name', yaxis_title='Runs Scored')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Player Runs Distribution </h2>', unsafe_allow_html=True)
 batsman_stat=new_df[new_df['batter']==selected_option]['batsman_run'].value_counts()
 labels=batsman_stat.index.astype(str)
 values=batsman_stat.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option+' runs distribution')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Player Dismissals Distribution </h2>', unsafe_allow_html=True)
 out= new_df[new_df['batter'] == selected_option]['kind'].value_counts()
 labels=out.index.astype(str)
 values=out.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option + ' dismissals distribution')
 st.plotly_chart(fig)


 st.markdown('<h2 style="color:yellow;">Player Sixes vs Other Teams </h2>', unsafe_allow_html=True)
 s = new_df5[new_df5['batter'] == selected_option]
 # s['againstTeam'] = ''
 # # Iterate over each row in the DataFrame
 # for index, row in s.iterrows():
 #  # Check if the toss decision is 'batting' or 'fielding'
 #  if selected_option in row['Team1Players']:
 #   s.at[index, 'againstTeam'] = row['Team2']
 #  elif selected_option in row['Team2Players']:
 #   s.at[index, 'againstTeam'] = row['Team1']
 # s = s.groupby('againstTeam')['batsman_run'].count().sort_values().reset_index()
 fig = go.Figure(data=go.Bar(x=s['batsman_run'], y=s['againstTeam'], marker_color='orange',orientation='h'))
 fig.update_layout(title=selected_option +' sixes' +' vs Other Teams', xaxis_title='No. of Sixes', yaxis_title='Teams Name')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Player Fours vs Other Teams </h2>', unsafe_allow_html=True)
 s = new_df6[new_df6['batter'] == selected_option]
 # s['againstTeam'] = ''
 # # Iterate over each row in the DataFrame
 # for index, row in s.iterrows():
 #  # Check if the toss decision is 'batting' or 'fielding'
 #  if selected_option in row['Team1Players']:
 #   s.at[index, 'againstTeam'] = row['Team2']
 #  elif selected_option in row['Team2Players']:
 #   s.at[index, 'againstTeam'] = row['Team1']
 # s = s.groupby('againstTeam')['batsman_run'].count().sort_values().reset_index()
 fig = go.Figure(data=go.Bar(x=s['batsman_run'], y=s['againstTeam'], marker_color='orange', orientation='h'))
 fig.update_layout(title=selected_option + ' fours' + ' vs Other Teams', xaxis_title='No. of fours',
                   yaxis_title='Teams Name')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Last 5 innings player performance</h2>', unsafe_allow_html=True)
 runs = new_df[new_df['batter'] == selected_option].groupby('ID')['batsman_run'].sum()
 result = pd.DataFrame({
  'ID': runs.index,
  'runs': runs.values
 })
 result.set_index('ID', inplace=True)
 result['Team'] = new_df1.groupby('ID')['bowlingteam'].first() + ' vs ' + new_df1.groupby('ID')['battingteam'].first()
 result=result.tail(5)

 fig = go.Figure(data=go.Bar(x=result['Team'], y=result['runs'],marker_color='orange'))
 fig.update_layout(yaxis_title='Runs Scored')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Seasonwise Player of the Match Award</h2>', unsafe_allow_html=True)
 st.markdown(' ### Total Player of Match Award\t')
 s = df[df['Player_of_Match'] == selected_option].groupby('Season')['Player_of_Match'].count().reset_index()
 st.title(s['Player_of_Match'].sum())
 fig = go.Figure(data=go.Scatter(x=s["Season"], y=s['Player_of_Match'], mode='markers'))

 # Update layout
 fig = go.Figure(data=go.Pie(labels=s['Season'], values=s['Player_of_Match']))

 # Update layout
 fig.update_layout(title='Pie Chart')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Most dismissals of Player against Top 5 bowlers </h2>', unsafe_allow_html=True)
 s = new_df[(new_df['batter'] == selected_option) & (new_df['player_out'] == selected_option) & (new_df['kind'] != 'run out')]
 s=s.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending=False).reset_index().head(5)
 fig = go.Figure(data=go.Bar(x=s['bowler'], y=s['isWicketDelivery'], marker_color='orange'))
 fig.update_layout(title='Most Number of Dismissals of '+selected_option, xaxis_title='Bowler Name', yaxis_title='No. of  Wickets')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Player as a Fielder Record  </h2>', unsafe_allow_html=True)
 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### No. of Catches\t')
  st.title(new_df[(new_df['fielders_involved']==selected_option)& (new_df['kind']=='caught')].shape[0])

 with col2:
  st.markdown(' ### No. of Runouts\t')
  st.title(new_df[(new_df['fielders_involved']==selected_option)& (new_df['kind']=='run out')].shape[0])

 with col3:
  st.markdown(' ### No. of Stumpings')
  st.title(new_df[(new_df['fielders_involved']==selected_option)& (new_df['kind']=='stumped')].shape[0])

 st.markdown('<h2 style="color:yellow;">Interesting Facts about the Player </h2>', unsafe_allow_html=True)
 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### No. of Ducks\t')
  s = new_df[(new_df['batter'] == selected_option)].groupby('ID')['batsman_run'].sum().sort_values().reset_index()
  st.title(s[s['batsman_run']==0].shape[0])

 with col2:
  st.markdown(' ### Orange Cap Won\t')
  s = new_df.groupby(['Season', 'batter'])['batsman_run'].sum().reset_index().sort_values('batsman_run',
                                                                                          ascending=False).drop_duplicates(
   subset=['Season'], keep='first').sort_values('Season').reset_index().drop('index', axis=1).set_index('Season')
  if s[s['batter'] == selected_option].shape[0] != 0:
   num= s[s['batter'] == selected_option].index
   year=''
   for i in num:
    year=year+str(i)+','
   st.title(year[:-1])
  else:
   st.title(0)

 with col3:
  st.markdown(' ### Purple Cap Won')
  s = new_df[(new_df['kind'] == 'caught') | (new_df['kind'] == 'caught') | (new_df['kind'] == 'bowled') | (
          new_df['kind'] == 'stumped') | (new_df['kind'] == 'caught and bowled') | (new_df['kind'] == 'hit wicket') | (
                      new_df['kind'] == 'lbw')]
  s=s.groupby(['Season', 'bowler'])['isWicketDelivery'].sum().reset_index().sort_values('isWicketDelivery',
                                                                                       ascending=False).drop_duplicates(
   subset=['Season'], keep='first').sort_values('Season').reset_index().drop('index', axis=1).set_index('Season')
  if s[s['bowler'] == selected_option].shape[0] != 0:
   num= s[s['bowler'] == selected_option].index
   year=''
   for i in num:
    year=year+str(i)+','
   st.title(year[:-1])

  else:
   st.title(0)

 col1, col2, col3 = st.columns(3)
 with col1:
   st.markdown(' ### Batting Average\t')
   avg_df=avg_df.set_index('batter')
   st.title(round(avg_df.loc[selected_option,'avg'],2))

 with col2:
   st.markdown(' ### Strike Rate\t')
   st.title(round(avg_df.loc[selected_option,'strike_rate'],2))

 with col3:
   st.markdown(' ### Played For Teams')
   s = new_df7[(new_df7['batter'] == selected_option)]
   # s['againstTeam'] = ''
   # # Iterate over each row in the DataFrame
   # for index, row in s.iterrows():
   #  # Check if the toss decision is 'batting' or 'fielding'
   #  if selected_option in row['Team1Players']:
   #   s.at[index, 'againstTeam'] = row['Team1']
   #  elif selected_option in row['Team2Players']:
   #   s.at[index, 'againstTeam'] = row['Team2']
   sachin=s['againstTeam'].unique()
   team=''
   for i in sachin:
    team = team + str(i) + ', '
   st.title(team[:-2])

 st.markdown('<h2 style="color:yellow;">Head to Head Player vs Bowler Battle </h2>', unsafe_allow_html=True)
 col1, col2 = st.columns(2)
 with col1:
  st.selectbox('Please Select Player', [selected_option])
 with col2:
  bow = list(new_df['bowler'].unique())
  bow.sort()
  bow.insert(0,'Select Bowler')
  bowler = st.selectbox('Please Select Bowler', bow)

 if ((bowler != selected_option) and (bowler != 'Select Bowler')):
  btnh = st.button('Show Analysis')
  if btnh:
   batsman_scored = new_df[(new_df['batter'] == selected_option) & (new_df['bowler'] == bowler)].groupby('batter').sum()['total_run'][0]
   bowler_wickets = new_df[
    (new_df['batter'] == selected_option) & (new_df['bowler'] == bowler) & (new_df['isWicketDelivery'] == 1)].shape[0]
   ball_faced = new_df[(new_df['batter'] == selected_option) & (new_df['bowler'] == bowler)].count()[0]
   NoOfFours = new_df[(new_df['batter'] == selected_option) & (new_df['bowler'] == bowler) & (new_df['batsman_run'] == 4)].count()[
    0]
   NoOfSixes = new_df[(new_df['batter'] == selected_option) & (new_df['bowler'] == bowler) & (new_df['batsman_run'] == 6)].count()[
    0]
   StrikeRate = (batsman_scored / ball_faced) * 100
   if bowler_wickets == 0:
    average = batsman_scored
   else:
    average = batsman_scored / bowler_wickets
   d = {'Rivalary': (selected_option + " vs " + bowler), 'Balls': (ball_faced), 'Run Scored': (batsman_scored),
        'Dismissals': (bowler_wickets), 'Fours': (NoOfFours), 'Sixes': (NoOfSixes), 'Strike Rate': (StrikeRate),
        'Average': (average)}
   FinalStat = pd.DataFrame(data=d, index=[1])
   st.dataframe(FinalStat)






elif (analysis=='Stadiumwise Analysis' and selected_option!='Select Stadium'):
 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### Total Matches\t')
  total_matches=df[df['Venue']==selected_option].shape[0]
  st.title(total_matches)

 with col2:
  st.markdown(' ### Batting 1st Won\t')
  stadium = df[df['Venue'] ==selected_option]
  bat1=stadium[(stadium['TossDecision']=='bat')&(stadium['TossWinner']==stadium['WinningTeam'])].shape[0]+stadium[(stadium['TossDecision']=='field')&(stadium['TossWinner']!=stadium['WinningTeam'])].shape[0]
  st.title(bat1)
 with col3:
  st.markdown(' ### Batting 2nd Won\t')
  bat2=stadium[(stadium['TossDecision']=='field')&(stadium['TossWinner']==stadium['WinningTeam'])].shape[0]+stadium[(stadium['TossDecision']=='bat')&(stadium['TossWinner']!=stadium['WinningTeam'])].shape[0]
  st.title(bat2)
 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### Winning % Bat 1st\t')
  st.title(round((bat1/total_matches)*100,2))

 with col2:
  st.markdown(' ### Winning %Bat 2nd\t')
  st.title(round((bat2 / total_matches) * 100, 2))
 with col3:
  st.markdown(' ### Sixes/Matches')
  sixs = new_df2[new_df2['batsman_run'] == 6].groupby(['Venue'])['batsman_run'].count().reset_index()
  sixs = sixs.set_index('Venue')
  sixes=sixs.loc[selected_option, 'batsman_run']
  st.title(round(sixes/total_matches))

 st.markdown('<h2 style="color:yellow;">Seasonwise bat 1st Average Score </h2>', unsafe_allow_html=True)
 bat1 = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 1)].groupby(['Season', 'ID'])[
  'batsman_run'].sum().reset_index()
 bat11 = bat1.groupby('Season')['batsman_run'].mean().reset_index()
 bat11['batsman_run'] = bat11['batsman_run'].astype('int64')
 fig = go.Figure(data=go.Line(x=bat11['Season'], y=bat11['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Seasonwise average Batting Ist Score in  ' + selected_option, xaxis_title='Season',
                   yaxis_title='Average Score')
 fig.update_xaxes(tickmode='array', tickvals=bat11['Season'], dtick=1)
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Seasonwise bat 2nd Average Score </h2>', unsafe_allow_html=True)
 bat2 = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 2)].groupby(['Season', 'ID'])[
  'batsman_run'].sum().reset_index()
 bat22 = bat2.groupby('Season')['batsman_run'].mean().reset_index()
 bat22['batsman_run'] = bat22['batsman_run'].astype('int64')
 fig = go.Figure(data=go.Line(x=bat22['Season'], y=bat22['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Seasonwise average Batting IInd Score in  ' + selected_option, xaxis_title='Season',
                   yaxis_title='Average Score')
 fig.update_xaxes(tickmode='array', tickvals=bat22['Season'], dtick=1)
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Seasonwise Comparison between Highest and lowest Scores in Stadium Bat 1st </h2>', unsafe_allow_html=True)
 highest = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 1)].groupby(['Season', 'ID'])[
  'batsman_run'].sum().reset_index().sort_values(['Season', 'batsman_run'], ascending=False).drop_duplicates(
  subset='Season', keep='first')

 lowest = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 1)].groupby(['Season', 'ID'])[
  'batsman_run'].sum().reset_index().sort_values(['Season', 'batsman_run'], ascending=False).drop_duplicates(
  subset='Season', keep='last')


 fig = make_subplots(rows=1, cols=2, subplot_titles=(
  "Highest Score in Bat 1st", "Lowest Score in Bat 1st"))
 fig.add_trace(go.Scatter(x=highest['Season'], y=highest['batsman_run'], name='Highest Score'), row=1, col=1)

 # Add bar graph trace
 fig.add_trace(go.Line(x=lowest['Season'], y=lowest['batsman_run'], name='Lowest Score', marker_color='orange'), row=1, col=2)
 fig.update_xaxes(tickmode='array', tickvals=highest['Season'], dtick=1)

 fig.update_xaxes(title_text='Season', row=1, col=1)
 fig.update_xaxes(title_text='Season', row=1, col=2)
 fig.update_yaxes(title_text='Highest Scores', row=1, col=1)
 fig.update_yaxes(title_text='Lowest  Scores', row=1, col=2)
 # Update layout
 fig.update_layout(height=400, width=800, showlegend=False)


 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Seasonwise Comparison between Highest and lowest Scores in Stadium Bat 2nd </h2>',unsafe_allow_html=True)
 highest = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 2)].groupby(['Season', 'ID'])[
  'batsman_run'].sum().reset_index().sort_values(['Season', 'batsman_run'], ascending=False).drop_duplicates(
  subset='Season', keep='first')

 lowest = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 2)].groupby(['Season', 'ID'])[
  'batsman_run'].sum().reset_index().sort_values(['Season', 'batsman_run'], ascending=False).drop_duplicates(
  subset='Season', keep='last')

 fig = make_subplots(rows=1, cols=2, subplot_titles=(
  "Highest Score in Bat 1st", "Lowest Score in Bat 1st"))
 fig.add_trace(go.Scatter(x=highest['Season'], y=highest['batsman_run'], name='Highest Score'), row=1, col=1)

 # Add bar graph trace
 fig.add_trace(go.Line(x=lowest['Season'], y=lowest['batsman_run'], name='Lowest Score', marker_color='orange'), row=1,
               col=2)
 fig.update_xaxes(tickmode='array', tickvals=highest['Season'], dtick=1)

 fig.update_xaxes(title_text='Season', row=1, col=1)
 fig.update_xaxes(title_text='Season', row=1, col=2)
 fig.update_yaxes(title_text='Highest Scores', row=1, col=1)
 fig.update_yaxes(title_text='Lowest  Scores', row=1, col=2)
 # Update layout
 fig.update_layout(height=400, width=800, showlegend=False)

 # Display the graph in Streamlit
 st.plotly_chart(fig)



 st.markdown('<h2 style="color:yellow;">Seasonwise Sixes in Stadium </h2>', unsafe_allow_html=True)
 s=new_df2[(new_df2['Venue'] == selected_option) & (new_df2['batsman_run'] == 6)].groupby('Season')[
  'batsman_run'].count().reset_index()
 fig = go.Figure(data=go.Bar(x=s['Season'], y=s['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Seasonwise sixes in ' + selected_option, xaxis_title='Season',
                   yaxis_title='No. of  Sixes')
 fig.update_xaxes(tickmode='array', tickvals=s['Season'], dtick=1)
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Seasonwise Fours in Stadium </h2>', unsafe_allow_html=True)
 s = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['batsman_run'] == 4)].groupby('Season')[
  'batsman_run'].count().reset_index()
 fig = go.Figure(data=go.Bar(x=s['Season'], y=s['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Seasonwise fours in ' + selected_option, xaxis_title='Season',
                   yaxis_title='No. of  Fours')
 fig.update_xaxes(tickmode='array', tickvals=s['Season'], dtick=1)
 st.plotly_chart(fig)




 st.markdown('<h2 style="color:yellow;">Runs Distribution in Stadium </h2>', unsafe_allow_html=True)
 batsman_stat = new_df2[new_df2['Venue'] == selected_option]['batsman_run'].value_counts()
 labels = batsman_stat.index.astype(str)
 values = batsman_stat.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option + ' runs distribution')
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Dismissals Distribution in Stadium </h2>', unsafe_allow_html=True)
 out = new_df2[new_df2['Venue'] == selected_option]['kind'].value_counts()
 labels = out.index.astype(str)
 values = out.values
 fig = go.Figure(data=go.Pie(labels=labels, values=values))

 # Update layout
 fig.update_layout(title=selected_option + ' dismissals distribution')
 st.plotly_chart(fig)




 st.markdown('<h2 style="color:yellow;">Top 5 batsman in Stadium </h2>', unsafe_allow_html=True)
 s=new_df2[(new_df2['Venue'] == selected_option)].groupby('batter')['batsman_run'].sum().sort_values(
  ascending=False).reset_index().head(5)
 fig = go.Figure(data=go.Bar(x=s['batter'], y=s['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Top 5 batsman in ' + selected_option, xaxis_title='Batsman Name',
                   yaxis_title='Runs Scored')
 #fig.update_xaxes(tickmode='array', tickvals=s['Season'], dtick=1)
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Top 5 bowlers in Stadium </h2>', unsafe_allow_html=True)
 s = new_df2[(new_df2['Venue'] == selected_option)].groupby('bowler')['isWicketDelivery'].sum().sort_values(
  ascending=False).reset_index().head(5)
 fig = go.Figure(data=go.Bar(x=s['bowler'], y=s['isWicketDelivery'], marker_color='orange'))
 fig.update_layout(title='Top 5 bowlers in ' + selected_option, xaxis_title='Bowler Name',
                   yaxis_title='Wickets Taken')
 # fig.update_xaxes(tickmode='array', tickvals=s['Season'], dtick=1)
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Interesting Facts about the Stadium</h2>', unsafe_allow_html=True)
 col1, col2, col3 = st.columns(3)


 with col1:
  st.markdown(' ### Highest score\t')
  bat1 =new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 1)].groupby(['Season', 'ID'])[
   'batsman_run'].sum().reset_index().sort_values(['Season', 'batsman_run'], ascending=False).drop_duplicates(
   subset='Season', keep='first')
  st.title(bat1['batsman_run'].max())

 with col2:
  st.markdown(' ### Lowest Score\t')
  bat1 = new_df2[(new_df2['Venue'] == selected_option) & (new_df2['innings'] == 1)].groupby(['Season', 'ID'])[
   'batsman_run'].sum().reset_index().sort_values(['Season', 'batsman_run'], ascending=False).drop_duplicates(
   subset='Season', keep='last')
  st.title(bat1['batsman_run'].min())

 with col3:
  st.markdown(' ### No.of Final Matches')
  final=df[(df['Venue'] == selected_option) & (df['MatchNumber'] == 'Final')].shape[0]
  st.title(final)

 col1, col2, col3 = st.columns(3)

 with col1:
  st.markdown(' ### No. of Catches\t')
  st.title(new_df2[(new_df2['Venue'] == selected_option) & ((new_df2['kind'] == 'caught') | (new_df2['kind'] == 'caught and bowled'))].shape[0])

 with col2:
  st.markdown(' ### No. of Runouts\t')
  st.title(new_df2[(new_df2['Venue']==selected_option)&(new_df2['kind']=='run out')].shape[0])
 with col3:
  st.markdown(' ### No.of Stumpings')
  st.title(new_df2[(new_df2['Venue'] == selected_option) & (new_df2['kind'] == 'stumped')].shape[0])

 st.markdown('<h2 style="color:yellow;">Head to Head Stadium vs Batsman/Bowler Analysis </h2>', unsafe_allow_html=True)
 analysis_type=st.selectbox('Select Analysis Type',['Stadium vs Batsman','Stadium vs Bowler'])
 if analysis_type=='Stadium vs Batsman':
  col1, col2 = st.columns(2)
  with col1:
   st.selectbox('Please Select Stadium', [selected_option])
  with col2:
   batsm = list(new_df['batter'].unique())
   batsm.sort()
   batsm.insert(0, 'Select Batsman')

   batsman = st.selectbox('Please Select Batsman', batsm)

  if (batsman != 'Select Batsman'):
   btnh = st.button('Show Analysis')
   if btnh:
    col1, col2, col3 = st.columns(3)
    with col1:
     st.markdown(' ### Matches Played\t')
     stadium1 = new_df2[new_df2['Venue'] == selected_option]
     matches_played_batsman = stadium1[stadium1['batter'] == batsman]['ID'].nunique()
     st.title(matches_played_batsman)

    with col2:
     st.markdown(' ### Runs Scored\t')
     stadium1_batsman_runs = stadium1[stadium1['batter'] == batsman]['batsman_run'].sum()
     st.title(stadium1_batsman_runs)
    with col3:
     stadium1_batsman = stadium1[stadium1['batter'] == batsman]
     st.markdown(' ### Out\t')
     total_outs = stadium1_batsman[stadium1_batsman['isWicketDelivery'] == 1].shape[0]
     st.title(total_outs)

    col1, col2, col3 = st.columns(3)
    with col1:
     st.markdown(' ### No. of Sixes\t')
     st.title(stadium1_batsman[stadium1_batsman['batsman_run'] == 6].shape[0])

    with col2:
     st.markdown(' ### No. of Fours\t')
     st.title(stadium1_batsman[stadium1_batsman['batsman_run'] == 4].shape[0])
    with col3:
     st.markdown(' ### Average\t')
     st.title(round(stadium1_batsman_runs / total_outs, 2))



 else:
  col1, col2 = st.columns(2)
  with col1:
   st.selectbox('Select Stadium', [selected_option])
  with col2:
   bowle = list(new_df['bowler'].unique())
   bowle.sort()
   bowle.insert(0, 'Select Bowler')

   bowler = st.selectbox('Please Select Bowler', bowle)

  if (bowler != 'Select Bowler'):
   btnh = st.button('Show Analysis')
   if btnh:
    col1, col2, col3 = st.columns(3)
    with col1:
     st.markdown(' ### Matches Played\t')
     stadium1 = new_df2[new_df2['Venue'] == selected_option]
     matches_played_bowler = stadium1[stadium1['bowler'] == bowler]['ID'].nunique()
     st.title(matches_played_bowler)

    with col2:
     st.markdown(' ### Wickets Taken\t')
     matches_played_bowler = stadium1[stadium1['bowler'] == bowler]
     bwic = matches_played_bowler[matches_played_bowler['isWicketDelivery'] == 1].shape[0]
     st.title(bwic)
    with col3:
     st.markdown(' ### Best Bowling\t')
     best_bowling = matches_played_bowler.groupby('ID')[['batsman_run', 'isWicketDelivery']].sum()
     best_bowling['best'] = best_bowling['batsman_run'].apply(str) + '-' + best_bowling['isWicketDelivery'].apply(str)
     eco = list(best_bowling[best_bowling['isWicketDelivery'] == best_bowling['isWicketDelivery'].max()]['best'])
     st.title(eco[0])




# 3. Overall Analysis
else:
 col1, col2, col3, col4 = st.columns(4)

 with col1:
  st.markdown(' ### Matches Played\t')
  st.title(df.shape[0])
 with col2:
  st.markdown(' ### Batting Ist Team won\t')
  st.title(df[(df['TossDecision'] == 'bat') & (df['TossWinner'] == df['WinningTeam'])].shape[0] +
           df[(df['TossDecision'] == 'field') & (df['TossWinner'] != df['WinningTeam'])].shape[0]
           )
 with col3:
  st.markdown(' ### Bowling Ist Team won\t')
  st.title(df.shape[0] - a - df[(df['TossDecision'] == 'bat') & (df['TossWinner'] == df['WinningTeam'])].shape[0] -
           df[(df['TossDecision'] == 'field') & (df['TossWinner'] != df['WinningTeam'])].shape[0]
           )
 with col4:
  st.markdown(' ### No Result (Rain)')
  st.title(a)
  st.title('\n')

 st.markdown('<h2 style="color:yellow;">Seasonwise Winner List</h2>', unsafe_allow_html=True)
 st.dataframe(df[df['MatchNumber'] == 'Final'][
               ['Season', 'WinningTeam', 'Team1', 'Team2', 'Venue', 'TossWinner', 'TossDecision',
                'Player_of_Match']].set_index('Season'))

 st.markdown('<h2 style="color:yellow;">IPL Winners List (No. of Trophy)</h2>', unsafe_allow_html=True)
 col1,col2=st.columns(2)
 with col2:
  st.write("")
  st.write("")
  iplw=df[df['MatchNumber'] == 'Final']['WinningTeam'].value_counts().reset_index()
  st.dataframe(iplw)
 with col1:
  fig = go.Figure(data=go.Bar(x=iplw['WinningTeam'], y=iplw['count'], marker_color='orange'))
  fig.update_layout(title='IPL Winners List', xaxis_title='Teams Name',
                    yaxis_title='No. of  trophies Won',width=450,height=400)

  st.plotly_chart(fig)


 st.markdown('<h2 style="color:yellow;">Seasonwise Orange cap Winner List</h2>', unsafe_allow_html=True)
 orangecap = new_df.groupby(['Season', 'batter'])['batsman_run'].sum().reset_index().sort_values('batsman_run',
                                                                                                 ascending=False).drop_duplicates(
  subset=['Season'], keep='first').sort_values('Season').reset_index().drop('index', axis=1).set_index('Season')
 col1,col2=st.columns(2)
 with col1:
  fig = go.Figure(data=go.Line(x=orangecap['batter'], y=orangecap['batsman_run'], marker_color='orange'))
  fig.update_layout(title='Orange Cap Winners', xaxis_title='Player Name',
                    yaxis_title='Runs Scored', width=450, height=400)

  st.plotly_chart(fig)
 with col2:
  st.dataframe(orangecap)


 st.markdown('<h2 style="color:yellow;">Seasonwise Purple cap Winner List</h2>', unsafe_allow_html=True)
 ni = new_df[(new_df['kind'] == 'caught') | (new_df['kind'] == 'caught') | (new_df['kind'] == 'bowled') | (
          new_df['kind'] == 'stumped') | (new_df['kind'] == 'caught and bowled') | (new_df['kind'] == 'hit wicket') | (
                      new_df['kind'] == 'lbw')]
 purplecap=ni.groupby(['Season', 'bowler'])['isWicketDelivery'].sum().reset_index().sort_values('isWicketDelivery',
                                                                                                   ascending=False).drop_duplicates(
  subset=['Season'], keep='first').sort_values('Season').reset_index().drop('index', axis=1).set_index('Season')
 col1,col2=st.columns(2)
 with col1:
  fig = go.Figure(data=go.Line(x=purplecap['bowler'], y=purplecap['isWicketDelivery'], marker_color='orange'))
  fig.update_layout(title='Purple Cap Winners', xaxis_title='Player Name',
                    yaxis_title='Wickets Taken', width=450, height=400)

  st.plotly_chart(fig)

 with col2:
  st.dataframe(purplecap)

 st.markdown('<h2 style="color:yellow;">Top 10 Batsman</h2>', unsafe_allow_html=True)
 runs=new_df.groupby('batter')['batsman_run'].sum().sort_values(ascending=False).reset_index().head(10)

 col1,col2=st.columns(2)
 with col2:
  st.dataframe(runs)
 with col1:
  fig = go.Figure(data=go.Bar(x=runs['batter'], y=runs['batsman_run'], marker_color='orange'))
  fig.update_layout(title='Top 10 Batsman', xaxis_title='Player Name',
                    yaxis_title='Runs Scored', width=450, height=400)

  st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Top 10 Bowler</h2>', unsafe_allow_html=True)
 wickets=new_df.groupby('bowler')['isWicketDelivery'].sum().sort_values(ascending=False).reset_index().head(10)


 col1,col2=st.columns(2)
 with col1:
  fig = go.Figure(data=go.Bar(x=wickets['bowler'], y=wickets['isWicketDelivery'], marker_color='orange'))
  fig.update_layout(title='Top 10 Bowlers', xaxis_title='Player Name',
                    yaxis_title='Wickets Taken', width=450, height=400)

  st.plotly_chart(fig)

 with col2:
  st.dataframe(wickets)



 st.markdown('<h2 style="color:yellow;">Top 10 Six hitter batsman</h2>', unsafe_allow_html=True)
 sixhitter=new_df[new_df['batsman_run'] == 6].groupby('batter')['batsman_run'].count().sort_values(
  ascending=False).reset_index().head(10)


 col1,col2=st.columns(2)
 with col1:
  fig = go.Figure(data=go.Line(x=sixhitter['batter'], y=sixhitter['batsman_run'], marker_color='orange'))
  fig.update_layout(title='Top 10 Six Hitters', xaxis_title='Player Name',
                    yaxis_title='No. of Sixes', width=450, height=400)

  st.plotly_chart(fig)

 with col2:
  st.dataframe(sixhitter)


 st.markdown('<h2 style="color:yellow;">Top 10 boundary(fours) hitter batsman</h2>', unsafe_allow_html=True)
 fourhitter=new_df[new_df['batsman_run'] == 4].groupby('batter')['batsman_run'].count().sort_values(
  ascending=False).reset_index().head(10)


 col1,col2=st.columns(2)
 with col1:
  fig = go.Figure(data=go.Line(x=fourhitter['batter'], y=fourhitter['batsman_run'], marker_color='orange'))
  fig.update_layout(title='Top 10 Four Hitters', xaxis_title='Player Name',
                    yaxis_title='No. of Fours', width=450, height=400)

  st.plotly_chart(fig)

 with col2:
  st.dataframe(fourhitter)

 st.markdown('<h2 style="color:yellow;">Number of Sixes each team hit</h2>', unsafe_allow_html=True)
 bat6team=new_df[new_df['batsman_run'] == 6].groupby('battingteam')['batsman_run'].count().sort_values(ascending=False).reset_index()
 fig = go.Figure(data=go.Bar(x=bat6team['battingteam'], y=bat6team['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Number of Sixes hit by each team', xaxis_title='Team Names',
                   yaxis_title='No. of Sixes')

 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Number of Fours each team hit</h2>', unsafe_allow_html=True)
 bat6team = new_df[new_df['batsman_run'] == 4].groupby('battingteam')['batsman_run'].count().sort_values(
  ascending=False).reset_index()
 fig = go.Figure(data=go.Bar(x=bat6team['battingteam'], y=bat6team['batsman_run'], marker_color='orange'))
 fig.update_layout(title='Number of Fours hit by each team', xaxis_title='Team Names',
                   yaxis_title='No. of Fours')

 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Top 10 batsman Facing most number of balls </h2>', unsafe_allow_html=True)
 d = {'Batsman': (list(new_df['batter'].value_counts().index)), 'Balls': (new_df['batter'].value_counts())}
 ballsfaced = pd.DataFrame(data=d)
 ballsfaced.reset_index(inplace=True, drop=True)
 ballfaced = ballsfaced.head(10)

 fig = go.Figure(data=go.Bar(x=ballfaced['Batsman'], y=ballfaced['Balls'], marker_color='orange'))
 fig.update_layout(title='Top 10 Batsman vs Number of Balls', xaxis_title='Batsman Name',
                   yaxis_title='No. of Balls')

 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Most Player of the Match Award </h2>', unsafe_allow_html=True)
 d = {'Batsman': (list(df['Player_of_Match'].value_counts().index)), 'no_of_award': (df['Player_of_Match'].value_counts())}
 p = pd.DataFrame(data=d)
 p.reset_index(inplace=True, drop=True)
 p = p.head(10)
 fig = go.Figure(data=go.Bar(x=p['Batsman'], y=p['no_of_award'], marker_color='orange'))
 fig.update_layout(title='Top 10 Batsman winning most number of times Player of the Match Award', xaxis_title='Batsman Name',
                   yaxis_title='No. of Award')

 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Overall Winning </h2>', unsafe_allow_html=True)
 win_counts = df.groupby(['WinningTeam', 'WonBy']).size().reset_index(name='Count')

 # Create the bar graph
 fig = go.Figure()

 # Add the bar traces for each win type
 for win_type in win_counts['WonBy'].unique():
  subset_df = win_counts[win_counts['WonBy'] == win_type]
  fig.add_trace(go.Bar(x=subset_df['WinningTeam'], y=subset_df['Count'], name=win_type))

 # Set the axis labels and title
 fig.update_layout(xaxis=dict(title='Winning Team'), yaxis=dict(title='Count'), title='Number of matches winning by teams by runs and wickets')

 # Display the graph in Streamlit
 st.plotly_chart(fig)

 st.markdown('<h2 style="color:yellow;">Number of Sixes hitted by a Team in 1 to 20 overs </h2>', unsafe_allow_html=True)
 sixt = new_df3[new_df3['batsman_run'] == 6]
 pt=sixt.pivot_table(index='overs', columns='battingteam', values='batsman_run', aggfunc='count')

 plt.figure(figsize=(10, 6))
 sns.heatmap(data=pt, annot=True, cmap='Blues', fmt='g')

 # Set the axis labels and title
 plt.xlabel('Teams Name')
 plt.ylabel('Overs')
 plt.title('Number of Sixes by Teams in Each Over')

 # Display the heatmap in Streamlit
 st.pyplot(plt)

 st.markdown('<h2 style="color:yellow;">Top 20 batsman according to Average and Strike rate </h2>',unsafe_allow_html=True)
 stat_batsman=avg_df.head(20)
 fig = px.scatter(stat_batsman, x='avg', y='strike_rate', text='batter', title='Top 20 batsman according to avg and strike rate')
 fig.update_traces(textposition='top center')

 # Set the axis labels
 fig.update_layout(xaxis_title='Average', yaxis_title='Strike Rate')

 # Set the figure size
 fig.update_layout(height=600, width=800)

 # Display the scatter plot in Streamlit
 st.plotly_chart(fig)




