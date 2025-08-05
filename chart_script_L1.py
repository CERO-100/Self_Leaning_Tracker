import plotly.graph_objects as go

# Define nodes (processes, external entities, and data stores)
labels = [
    'User',                     # 0
    'Admin',                    # 1
    'Student Tracker System',   # 2 (Main system)
    'User Mgmt',                # 3
    'Task Mgmt',                # 4
    'Skill/Progress',           # 5
    'Analytics',                # 6
    'User Data',                # 7
    'Task Data',                # 8
    'Skill Data',               # 9
    'Database'                  #10
]

colors = [
    '#1FB8CD', # User
    '#DB4545', # Admin
    '#2E8B57', # Main System
    '#5D878F', # Process 1
    '#D2BA4C', # Process 2
    '#B4413C', # Process 3
    '#964325', # Process 4
    '#944454', # User Data
    '#13343B', # Task Data
    '#DB4545', # Skill Data
    '#1FB8CD', # Database
]

# Arrows (links): Each tuple is (source, target, value)
links = [
    # User/Admin to system:
    (0, 2, 1), # User → Main System
    (1, 2, 1), # Admin → Main System

    # Main system decomposes into subprocesses (L1 DFD):
    (2, 3, 1), # Main → User Mgmt
    (2, 4, 1), # Main → Task Mgmt
    (2, 5, 1), # Main → Skill/Progress
    (2, 6, 1), # Main → Analytics

    # Processes exchange with data stores:
    (3, 7, 1), # User Mgmt → User Data
    (7, 3, 1), # User Data → User Mgmt
    (4, 8, 1), # Task Mgmt → Task Data
    (8, 4, 1), # Task Data → Task Mgmt
    (5, 9, 1), # Skill/Progress → Skill Data
    (9, 5, 1), # Skill Data → Skill/Progress
    (6, 7, 1), # Analytics → User Data
    (6, 8, 1), # Analytics → Task Data
    (6, 9, 1), # Analytics → Skill Data

    # Processes to external data store (Database):
    (7,10, 1), # User Data → Database
    (8,10, 1), # Task Data → Database
    (9,10, 1), # Skill Data → Database
    (10,7, 1), # Database → User Data
    (10,8, 1), # Database → Task Data
    (10,9, 1), # Database → Skill Data

    # Users & Admins interact with certain processes:
    (0,3, 1),  # User → User Mgmt
    (1,3, 1),  # Admin → User Mgmt
    (0,4, 1),  # User → Task Mgmt
    (0,5, 1),  # User → Skill/Progress
    (0,6, 1),  # User → Analytics
    (1,6, 1),  # Admin → Analytics
]

# Prepare sources and targets for Sankey
sources = [s for (s,t,v) in links]
targets = [t for (s,t,v) in links]
values =  [v for (s,t,v) in links]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=25,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color=colors,
        hovertemplate='%{label}',
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        color="rgba(150,200,250,0.2)",
    )
))

fig.update_layout(title_text="L1 DFD: Student Tracker Sys")
fig.write_image("dfd_student_tracker.png")
