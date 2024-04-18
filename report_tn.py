# Importing Libraries

import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import Dash, dcc, html, Input, Output, dash_table

# Importing data

dt_df = pd.read_excel('Report_TN.xlsx', sheet_name='AC_DT')

ae_stat_df = pd.read_excel('Report_TN.xlsx', sheet_name='ae_stat')
pe_stat_df = pd.read_excel('Report_TN.xlsx', sheet_name='pe_stat')

ae_pos_df = pd.read_excel('Report_TN.xlsx', sheet_name='ae_pos')
pe_pos_df = pd.read_excel('Report_TN.xlsx', sheet_name='ls_pos')

party_bar_df = pd.read_excel('Report_TN.xlsx', sheet_name='ae')

district_list = list(dt_df['District'].unique())
district_list = sorted(district_list)

party_cmap = {'ADMK': '#408627', 'AGP': '#99CCFF',
              'AIFB': '#D70000', 'AIMIM': '#136B4B',
              'AINRC': '#FFC000', 'AITC': '#20C646',
              'BJD': '#006400', 'BJP': '#FF9933',
              'BSP': '#22409A', 'CPI': '#FF0000',
              'CPI(M)': '#FF1D15', 'DMDK': '#FFEA19',
              'DMK': '#DD1100', 'HSPDP': '#0000FF',
              'INC': '#19AAED', 'INLD': '#336600',
              'IPFT': '#008000', 'IUML': '#228B22',
              'JCC': '#FFC0DB', 'JD(S)': '#138808',
              'JKNPP': '#000180', 'JKPDP': '#058532',
              'JMM': '#215B30', 'LJP': '#0093DD',
              'MNF': '#2E5694', 'MNS': '#5F2301',
              'NCP': '#00B2B2', 'NDPP': '#ED1B24',
              'NPF': '#990066', 'NPP': '#DB7093',
              'PDA': '#FF0000', 'PMK': '#FFFF00',
              'PPA': '#008000', 'RJD': '#008000',
              'RLD': '#006400', 'RLTP': '#DBE934',
              'RSP': '#FF4A4A', 'SAD': '#0F204A',
              'SDF': '#FFFC06', 'SKM': '#ED1E26',
              'SP': '#FF2222', 'SHS': '#F26F21',
              'TDP': '#FCEE23', 'TRS': '#FF0274',
              'UDP': '#CEF2E0', 'UPPL': '#F3ED13',
              'Others': '#696969',
              'YSRCP': '#1569C7', 'ST': '#228B22', 'SC': '#00008B', 'GEN': '#f4c2c2'}

# App code

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([

    # Header
    html.Div([
        html.H1("Tamil Nadu Assembly Constituency Report",
                style={'text-align': 'center', 'fontweight': 'bold'})
    ], className='header'),

    # Dropdowns
    html.Div([
        html.Label("Select District", style={'colour': '#000000',
                                             'fontsize': '16px', 'fontWeight': 'bold'}),
        dcc.Dropdown(id="District",
                     options=[{"label": i, "value": i} for i in district_list],
                     placeholder="Select District",
                     multi=False,
                     searchable=True,
                     value='Ariyalur',
                     clearable=False,
                     style={'width': '100%', 'verticalAlign': 'middle',
                            'color': 'black'})
    ], className='dropdown1'),

    html.Div([
        html.Label("Select Assembly Constituency", style={'colour': '#000000',
                                                          'fontsize': '16px', 'fontWeight': 'bold'}),
        dcc.Dropdown(id='AC',
                     options=[],
                     placeholder="Select Assembly Constituency",
                     multi=False,
                     searchable=True,
                     clearable=True,
                     style={'width': '100%', 'verticalAlign': 'middle',
                            'color': 'black'})
    ], className='dropdown2'),

    html.Div(children=[
        html.Label("Assembly Election Stats", style={'fontWeight': 'bold'}),
        dash_table.DataTable(id='ac_stat_table', style_cell={'text-align': 'left',
                                                             'height': 'auto',
                                                             'fontSize': 11.5,
                                                             'maxWidth': '35%',
                                                             'font-family': 'HelveticaNeue'
                                                             },
                             style_header={'fontWeight': 'bold',
                                           'color': '#ffffff',
                                           'backgroundColor': '#052F5F'},
                             style_data={'fontWeight': 'bold',
                                         'whiteSpace': 'normal',
                                         'height': 'auto',
                                         'backgroundColor': 'transparent'
                                         },
                             style_cell_conditional=[
                                 {'if': {'column_id': 'Turnout'}, 'width': '22.5%'},
                                 {'if': {'column_id': 'Electors'}, 'width': '22.5%'},
                                 {'if': {'column_id': 'Valid Votes'}, 'width': '22.5%'},
                                 {'if': {'column_id': 'Constituency Type'}, 'width': '22.5%'}
                             ],
                             style_as_list_view=True, )
    ], className='ac_stat'),

    html.Div(children=[
        html.Label("Lok Sabha Election Stats", style={'fontWeight': 'bold'}),
        dash_table.DataTable(id='pc_stat_table', style_cell={'text-align': 'left',
                                                             'height': 'auto',
                                                             'fontSize': 11.5,
                                                             'maxWidth': '35%',
                                                             'font-family': 'HelveticaNeue'
                                                             },
                             style_header={'fontWeight': 'bold',
                                           'color': '#ffffff',
                                           'backgroundColor': '#052F5F'},
                             style_data={'fontWeight': 'bold',
                                         'whiteSpace': 'normal',
                                         'height': 'auto',
                                         'backgroundColor': 'transparent'
                                         },
                             style_cell_conditional=[
                                 {'if': {'column_id': 'Year'}, 'width': '10%'},
                                 {'if': {'column_id': 'Turnout'}, 'width': '22.5%'},
                                 {'if': {'column_id': 'Valid Votes'}, 'width': '22.5%'}
                             ],
                             style_as_list_view=True, )
    ], className='pc_stat'),

    html.Div(children=[
        html.Label("Assembly Election Summary", style={'fontWeight': 'bold'}),
        dash_table.DataTable(id='ac_sum_table',
                             style_cell={'text-align': 'left',
                                         'height': 'auto',
                                         'fontSize': 11.5,
                                         'maxWidth': '35%',
                                         'font-family': 'HelveticaNeue'
                                         },
                             style_header={'fontWeight': 'bold',
                                           'color': '#ffffff',
                                           'height': 'auto',
                                           'backgroundColor': '#052F5F'},
                             style_data={'fontWeight': 'bold',
                                         'whiteSpace': 'normal',
                                         'height': 'auto',
                                         'backgroundColor': 'transparent'
                                         },
                             style_cell_conditional=[
                                 {'if': {'column_id': '1st'}, 'width': '15%'},
                                 {'if': {'column_id': '1st Party'}, 'width': '5%'},
                                 {'if': {'column_id': '1st Votes'}, 'width': '5%'},
                                 {'if': {'column_id': '1st Vote %'}, 'width': '5%'},
                                 {'if': {'column_id': '2nd'}, 'width': '15%'},
                                 {'if': {'column_id': '2nd Party'}, 'width': '5%'},
                                 {'if': {'column_id': '2nd Votes'}, 'width': '5%'},
                                 {'if': {'column_id': '2nd Vote %'}, 'width': '5%'},
                                 {'if': {'column_id': '3rd'}, 'width': '15%'},
                                 {'if': {'column_id': '3rd Party'}, 'width': '5%'},
                                 {'if': {'column_id': '3rd Votes'}, 'width': '5%'},
                                 {'if': {'column_id': '3rd Vote %'}, 'width': '5%'}
                             ],
                             style_as_list_view=True, )
    ], className='ac_sum_tab'),

    html.Div(children=[
        html.Label("Lok Sabha Election Summary", style={'fontWeight': 'bold'}),
        dash_table.DataTable(id='pc_sum_table',
                             style_cell={'text-align': 'left',
                                         'height': 'auto',
                                         'fontSize': 11.5,
                                         'maxWidth': '35%',
                                         'font-family': 'HelveticaNeue'
                                         },
                             style_header={'fontWeight': 'bold',
                                           'color': '#ffffff',
                                           'backgroundColor': '#052F5F'},
                             style_data={'fontWeight': 'bold',
                                         'whiteSpace': 'normal',
                                         'height': 'auto',
                                         'backgroundColor': 'transparent'
                                         },
                             style_cell_conditional=[
                                 {'if': {'column_id': '1st'}, 'width': '15%'},
                                 {'if': {'column_id': '1st Party'}, 'width': '5%'},
                                 {'if': {'column_id': '1st Votes'}, 'width': '5%'},
                                 {'if': {'column_id': '1st Vote %'}, 'width': '5%'},
                                 {'if': {'column_id': '2nd'}, 'width': '15%'},
                                 {'if': {'column_id': '2nd Party'}, 'width': '5%'},
                                 {'if': {'column_id': '2nd Votes'}, 'width': '5%'},
                                 {'if': {'column_id': '2nd Vote %'}, 'width': '5%'},
                                 {'if': {'column_id': '3rd'}, 'width': '15%'},
                                 {'if': {'column_id': '3rd Party'}, 'width': '5%'},
                                 {'if': {'column_id': '3rd Votes'}, 'width': '5%'},
                                 {'if': {'column_id': '3rd Vote %'}, 'width': '5%'}
                             ],
                             style_as_list_view=True, )
    ], className='pc_sum_tab'),

    # html.Div([
    #     html.Label('Party Votes 2011',style={'fontWeight':'bold'}),
    #     dcc.Graph(id='bar1')
    #     ],className='bar1'),

    html.Div([
        html.Label('Party Votes 2016', style={'fontWeight': 'bold'}),
        dcc.Graph(id='bar2')
    ], className='bar2'),

    html.Div([
        html.Label('Party Votes 2021', style={'fontWeight': 'bold'}),
        dcc.Graph(id='bar3')
    ], className='bar3'),

    html.Div([
        html.Label('Party Votes 2011', style={'fontWeight': 'bold'}),
        dcc.Graph(id='bar1')
    ], className='bar1'),

    # html.Div([
    #     dcc.Graph(id='pie')
    #     ],className='pie'),

], className='report')


@app.callback(
    Output('AC', 'options'),
    Output('AC', 'value'),
    [Input('District', 'value')]
)
def update_ac(District):
    df = dt_df[dt_df['District'] == District]
    k = df["AC"].unique()
    return [{'label': i, 'value': i} for i in df['AC'].unique()], k[0]


@app.callback(
    [
        Output('ac_stat_table', 'data'),
        Output('ac_stat_table', 'columns'),
        Output('pc_stat_table', 'data'),
        Output('pc_stat_table', 'columns'),
        Output('ac_sum_table', 'data'),
        Output('ac_sum_table', 'columns'),
        Output('pc_sum_table', 'data'),
        Output('pc_sum_table', 'columns')
    ],
    [Input('AC', 'value')]
)
def update_table(Constituency):
    # Data table for ac stats
    df_ac = ae_stat_df[ae_stat_df['AC'] == Constituency]
    df_ac = df_ac.drop(columns=['AC', 'Constituency_No', 'Constituency_Name'])
    df_ac = df_ac.drop_duplicates(subset=['Year'])
    df_ac = df_ac[['Year', 'Turnout', 'Electors', 'Valid Votes', 'Constituency Type']]
    df_ac = df_ac.sort_values(by='Year', ascending=False)
    columns_df_ac = [{'name': col, 'id': col} for col in df_ac.columns]
    data_df_ac = df_ac.to_dict(orient='records')

    # Data table for pc stats
    df_pc = pe_stat_df[pe_stat_df['AC'] == Constituency]
    df_pc = df_pc.drop(columns=['AC'])
    df_pc = df_pc.drop_duplicates(subset=['Year'])
    df_pc = df_pc[['Year', 'Valid Votes', '1st Vote Share Percentage']]
    df_pc = df_pc.sort_values(by='Year', ascending=False)
    columns_df_pc = [{'name': col, 'id': col} for col in df_pc.columns]
    data_df_pc = df_pc.to_dict(orient='records')

    # Data table for ac top 3
    df_ac_sum = ae_pos_df[ae_pos_df['AC'] == Constituency]
    df_ac_sum = df_ac_sum.drop(columns=['AC'])
    columns_df_ac_sum = [{'name': col, 'id': col} for col in df_ac_sum.columns]
    data_df_ac_sum = df_ac_sum.to_dict(orient='records')

    # Data table for pc top 3
    df_pc_sum = pe_pos_df[pe_pos_df['AC'] == Constituency]
    df_pc_sum = df_pc_sum.drop(columns=['AC'])
    columns_df_pc_sum = [{'name': col, 'id': col} for col in df_pc_sum.columns]
    data_df_pc_sum = df_pc_sum.to_dict(orient='records')

    return data_df_ac, columns_df_ac, data_df_pc, columns_df_pc, data_df_ac_sum, columns_df_ac_sum, data_df_pc_sum, columns_df_pc_sum


@app.callback(
    Output('bar1', 'figure'),
    [Input('AC', 'value')]
)
def update_support(Cons):
    df_supp = party_bar_df[party_bar_df['AC'] == Cons]
    df_supp = df_supp[df_supp['Year'] == 2011]

    barchart = px.bar(
        data_frame=df_supp,
        x='Party',
        y='Vote Share',
        color='Party',
        text='Votes',
        opacity=0.9,
        color_discrete_map=party_cmap,
        orientation='v',
        barmode='relative',
        # width=400
    )
    barchart.update(layout_yaxis_range=[0, 50])
    return (barchart)


@app.callback(
    Output('bar2', 'figure'),
    [Input('AC', 'value')]
)
def update_support(Cons):
    df_supp = party_bar_df[party_bar_df['AC'] == Cons]
    df_supp = df_supp[df_supp['Year'] == 2016]

    barchart = px.bar(
        data_frame=df_supp,
        x='Party',
        y='Vote Share',
        color='Party',
        text='Votes',
        opacity=0.9,
        orientation='v',
        color_discrete_map=party_cmap,
        barmode='relative',
        # width=400
    )
    barchart.update(layout_yaxis_range=[0, 50])
    return (barchart)


@app.callback(
    Output('bar3', 'figure'),
    [Input('AC', 'value')]
)
def update_support(Cons):
    df_supp = party_bar_df[party_bar_df['AC'] == Cons]
    df_supp = df_supp[df_supp['Year'] == 2021]

    barchart = px.bar(
        data_frame=df_supp,
        x='Party',
        y='Vote Share',
        color='Party',
        text='Votes',
        opacity=0.9,
        orientation='v',
        color_discrete_map=party_cmap,
        barmode='relative',
        # xaxis=
        # width=400
    )
    barchart.update(layout_yaxis_range=[0, 50])
    return (barchart)


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)