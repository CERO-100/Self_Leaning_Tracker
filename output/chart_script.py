import plotly.graph_objects as go

# Shapes for entities and process (boxes or circles)
shapes = [
    # User (Student)
    dict(type='rect', x0=0.10, y0=0.6, x1=0.28, y1=0.82, line=dict(color='#2E8B57', width=2), fillcolor='#2E8B57', opacity=0.2),
    # Admin
    dict(type='rect', x0=0.10, y0=0.18, x1=0.28, y1=0.40, line=dict(color='#DB4545', width=2), fillcolor='#DB4545', opacity=0.2),
    # Student Progress Tracker (main system)
    dict(type='circle', x0=0.35, y0=0.27, x1=0.71, y1=0.75, line=dict(color='#1FB8CD', width=3), fillcolor='#1FB8CD', opacity=0.18),
    # Database
    dict(type='rect', x0=0.80, y0=0.35, x1=0.96, y1=0.65, line=dict(color='#D2BA4C', width=2), fillcolor='#D2BA4C', opacity=0.2)
]

# Entity positions for arrow connections and texts
entities = {
    'User (Student)': {'x': 0.19, 'y': 0.71},
    'Admin': {'x': 0.19, 'y': 0.29},
    'Student Progress Tracker': {'x': 0.53, 'y': 0.51},
    'Database': {'x': 0.88, 'y': 0.50}
}

# Arrows (data flows)
arrows = [
    # User <-> Main System
    {'x0': entities['User (Student)']['x'] + 0.09, 'y0': entities['User (Student)']['y'], 'x1': 0.38, 'y1': 0.65, 'label': 'Login/Data', 'color':'#2E8B57'},
    {'x0': 0.38, 'y0': 0.57, 'x1': entities['User (Student)']['x'] + 0.09, 'y1': entities['User (Student)']['y'], 'label': 'View Prog.', 'color':'#1FB8CD'},

    # Admin <-> Main System
    {'x0': entities['Admin']['x'] + 0.09, 'y0': entities['Admin']['y'], 'x1': 0.38, 'y1': 0.37, 'label': 'Manage', 'color':'#DB4545'},
    {'x0': 0.38, 'y0': 0.43, 'x1': entities['Admin']['x'] + 0.09, 'y1': entities['Admin']['y'], 'label': 'Report', 'color':'#2E8B57'},

    # Main System <-> Database
    {'x0': 0.71, 'y0': 0.55, 'x1': entities['Database']['x'] - 0.04, 'y1': 0.55, 'label': 'Stores', 'color':'#D2BA4C'},
    {'x0': entities['Database']['x'] - 0.04, 'y0': 0.45, 'x1': 0.71, 'y1': 0.45, 'label': 'Fetch', 'color':'#5D878F'}
]

fig = go.Figure()

# Draw shapes
fig.update_layout(shapes=shapes)

# Draw entity/process names
fig.add_trace(go.Scatter(
    x=[entities['User (Student)']['x']],
    y=[entities['User (Student)']['y']],
    text=["User (Student)"],
    mode="text",
    textfont=dict(size=18, color="#2E8B57"),
    showlegend=False
))
fig.add_trace(go.Scatter(
    x=[entities['Admin']['x']],
    y=[entities['Admin']['y']],
    text=["Admin"],
    mode="text",
    textfont=dict(size=18, color="#DB4545"),
    showlegend=False
))
fig.add_trace(go.Scatter(
    x=[entities['Student Progress Tracker']['x']],
    y=[entities['Student Progress Tracker']['y']],
    text=["Student Prog. Tracker"],
    mode="text",
    textfont=dict(size=20, color="#1FB8CD"),
    showlegend=False
))
fig.add_trace(go.Scatter(
    x=[entities['Database']['x']],
    y=[entities['Database']['y']],
    text=["Database"],
    mode="text",
    textfont=dict(size=18, color="#D2BA4C"),
    showlegend=False
))

# Draw arrows with labels
for arr in arrows:
    fig.add_annotation(x=arr['x1'], y=arr['y1'], ax=arr['x0'], ay=arr['y0'],
                      xref="x", yref="y", axref="x", ayref="y",
                      text="", showarrow=True, arrowhead=3, arrowsize=1.2, arrowwidth=2, arrowcolor=arr['color'])
    mx = (arr['x0'] + arr['x1']) / 2
    my = (arr['y0'] + arr['y1']) / 2
    fig.add_trace(go.Scatter(
        x=[mx],
        y=[my],
        text=[arr['label'][:15]],
        mode="text",
        textfont=dict(size=14, color=arr['color']),
        showlegend=False
    ))

# Set axis limits and hide axes
fig.update_xaxes(visible=False, range=[0, 1])
fig.update_yaxes(visible=False, range=[0, 1])

fig.update_layout(
    title_text="Level 0 DFD: Student Prog. Tracker"
)

# Save as PNG
fig.write_image("level0_dfd.png")
