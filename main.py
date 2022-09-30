import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

mpg_data = sns.load_dataset("mpg")
pd.set_option('display.max_columns', None)
dts = mpg_data.head(12)

print(mpg_data)
print(mpg_data.info())
print(mpg_data.isna().sum())

name = dts['name'].tolist()
horsepower = dts['horsepower'].tolist()
fig = go.Figure(px.bar(x=name, y=horsepower, color=horsepower, text=horsepower))
fig.update_traces(textfont_size = 14, textangle = 0, textposition = 'outside',
                  marker=dict(color=horsepower, coloraxis = 'coloraxis', line=dict(color='black', width=2)))
fig.update_layout(
            title = 'Сomparative statistics of car capacities', title_font_size = 20, title_x = 0.5, title_xanchor = 'center',
            xaxis_title = 'Car model', xaxis_title_font_size = 16, xaxis_tickangle = 315, xaxis_tickfont_size = 14,
            yaxis_title = 'hp', yaxis_title_font_size = 16, yaxis_tickfont_size = 14,
            height = 700,
            margin = dict(l=0,r=0,t=50,b=0)
)
fig.show()

fig2 = go.Figure(px.pie(values=horsepower, names=name, color=name))
fig2.update_traces(marker=dict(line=dict(color='black', width=2)))
fig2.update_layout(
            title = 'Сomparative statistics of car capacities', title_font_size = 20, title_x = 0.5, title_xanchor = 'center',
            xaxis_title = 'Car model', xaxis_title_font_size = 16, xaxis_tickangle = 315, xaxis_tickfont_size = 14,
            yaxis_title = 'hp', yaxis_title_font_size = 16, yaxis_tickfont_size = 14,
            margin = dict(l=0,r=0,t=50,b=0),
            height = 700
)
fig2.show()

fig3 = go.Figure(px.bar(x=name, y=horsepower, color=horsepower, text=horsepower))
fig3.update_traces(textfont_size=14, textangle=0, textposition="outside",
                   marker=dict(color=horsepower, coloraxis="coloraxis", line=dict(color='black', width=2)))
fig3.update_layout(
                title = 'Сomparative statistics of car capacities', title_font_size = 20, title_x=0.5, title_xanchor='center',
                xaxis_title='Car model', xaxis_tickangle=315, xaxis_title_font_size=16, xaxis_tickfont_size=14,
                yaxis_title='hp', yaxis_title_font_size=16, yaxis_tickfont_size=14,
                margin = dict(l = 0, r = 0, t = 40, b = 0),
                height = 700
)
fig3.update_xaxes(showgrid=True, gridwidth=2, gridcolor='ivory')
fig3.update_yaxes(showgrid=True, gridwidth=2, gridcolor='ivory')
sum=0
for i in range(len(horsepower)):
    horsepower[i]+=sum
    sum=horsepower[i]
fig3.add_trace(go.Scatter(x=name, y=horsepower, name = 'hp cumulative', mode = 'lines+markers',
                         line_color='crimson', marker=dict(color='white', line = dict(color='black', width=2))))
fig3.show()

