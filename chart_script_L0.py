import plotly.graph_objects as go

fig = go.Figure()

# Define node positions for entities and process
node_x = [0, 1, 2, 1]
node_y = [1.5, 0, 1.5, 3]
names = ['User', 'Student\nTracker\nSystem', 'Database', 'Admin']

# Map colors for:
# User: #1FB8CD
# Admin: #DB4545
# Database: #2E8B57
# System: #D2BA4C
node_colors = ['#1FB8CD', '#D2BA4C', '#2E8B57', '#DB4545']

# Plot nodes
for i, (x, y, name) in enumerate(zip(node_x, node_y, names)):
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(size=80, color=node_colors[i], line=dict(color='black', width=2)),
        text=[name],
        textposition='middle center',
        textfont=dict(size=14, color='white'),
        hovertemplate='%{text}',
        showlegend=False,
        cliponaxis=False
    ))

# Data flow edges/arrows (drawn with lines and arrowheads)
arrows = [
    # User -> System
    dict(x0=0, y0=1.5, x1=1, y1=0, label='reg/login', color='#5D878F'),
    dict(x0=0, y0=1.5, x1=1, y1=0, label='task/update', color='#5D878F'),
    # Admin -> System
    dict(x0=1, y0=3, x1=1, y1=0, label='admin mgmt', color='#DB4545'),
    # System <-> Database
    dict(x0=1, y0=0, x1=2, y1=1.5, label='store/retr', color='#2E8B57'),
    dict(x0=2, y0=1.5, x1=1, y1=0, label='results', color='#2E8B57'),
    # System -> User
    dict(x0=1, y0=0, x1=0, y1=1.5, label='view result', color='#5D878F')
]

for arr in arrows:
    fig.add_annotation(
        x=arr['x1'], y=arr['y1'],
        ax=arr['x0'], ay=arr['y0'],
        xref='x', yref='y', axref='x', ayref='y',
        text='',
        showarrow=True, arrowhead=3, arrowsize=1.5, arrowcolor=arr['color'],
        standoff=10
    )

# Add edge labels as invisible scatters with short text
edge_labels = [
    ((0.5, 0.75), 'reg/login'),
    ((0.5, 0.75), 'task/update'),
    ((1, 1.5), 'admin mgmt'),
    ((1.5, 0.75), 'store/retr'),
    ((1.5, 0.75), 'results'),
    ((0.5, 0.75), 'view result')
]
edge_text_styles = [
    dict(color='#5D878F'), dict(color='#5D878F'), dict(color='#DB4545'), dict(color='#2E8B57'), dict(color='#2E8B57'), dict(color='#5D878F')
]
for (pos, label), style in zip(edge_labels, edge_text_styles):
    fig.add_trace(go.Scatter(
        x=[pos[0]], y=[pos[1]],
        mode='text', text=[label],
        textfont=dict(size=13, color=style['color']),
        showlegend=False, cliponaxis=False
    ))

fig.update_layout(
    title_text='Level 0 DFD Student Tracker',
    xaxis=dict(visible=False, range=[-0.7, 2.7]),
    yaxis=dict(visible=False, range=[-0.5, 3.7])
)

fig.update_layout(hovermode=False)

fig.write_image('level0dfd.png')
