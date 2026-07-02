import urllib.request
import urllib.error
import base64
import os

# Define output path
REPO_PATH = r"C:\Users\prita\.gemini\antigravity\scratch\PritamPalit-official"

def download_and_encode(name, url):
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            content = response.read()
            encoded = base64.b64encode(content).decode('utf-8')
            return f"data:image/svg+xml;base64,{encoded}"
    except Exception as e:
        print(f"Error downloading {name}: {e}")
        return ""

def create_header():
    svg_content = """<svg viewBox="0 0 800 160" xmlns="http://www.w3.org/2000/svg">
  <style>
    .background { fill: #080d16; rx: 12px; }
    .border { stroke: #30363d; stroke-width: 1.5; fill: none; rx: 12px; }
    .title {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 900;
      font-size: 38px;
      fill: #ffffff;
      letter-spacing: 6px;
      text-shadow: 0px 0px 15px rgba(0, 240, 255, 0.5);
    }
    .subtitle {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 700;
      font-size: 11px;
      fill: #8b949e;
      letter-spacing: 3px;
      opacity: 0.8;
    }
    .hud-text {
      font-family: monospace;
      font-size: 10px;
      fill: #58a6ff;
    }
    .pulse-dot {
      fill: #238636;
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0% { opacity: 0.3; }
      50% { opacity: 1; }
      100% { opacity: 0.3; }
    }
  </style>

  <rect width="800" height="160" class="background" />
  
  <!-- Network Nodes Emblem (Replacing Radar) -->
  <g transform="translate(60, 80)">
    <circle r="30" fill="none" stroke="#30363d" stroke-width="1.5" />
    <circle r="15" fill="none" stroke="#30363d" stroke-width="1" />
    <line x1="-30" y1="0" x2="30" y2="0" stroke="#30363d" stroke-width="1" />
    <line x1="0" y1="-30" x2="0" y2="30" stroke="#30363d" stroke-width="1" />
    <circle cx="0" cy="0" r="5" fill="#58a6ff" />
    <circle cx="21" cy="-21" r="3" fill="#238636" />
    <circle cx="-21" cy="21" r="3" fill="#ffbd2e" />
  </g>
  <text x="60" y="142" class="hud-text" text-anchor="middle">[ SYS_ONLINE ]</text>

  <!-- Telemetry Info (Left Panel) -->
  <text x="130" y="50" class="hud-text">ROLE: DATA &amp; BI ENGINEER</text>
  <text x="130" y="70" class="hud-text">LOC : KOLKATA, IN</text>
  <text x="130" y="90" class="hud-text">STAT: ACTIVELY HIRING</text>

  <!-- Center Title & Subtitle -->
  <text x="400" y="75" text-anchor="middle" class="title">PRITAM PALIT</text>
  <text x="400" y="105" text-anchor="middle" class="subtitle">DATA SCIENTIST • BI ENGINEER • ML DEVELOPER</text>

  <!-- Status indicators (Right Panel) -->
  <g transform="translate(620, 40)">
    <!-- Resource bars -->
    <text x="0" y="10" class="hud-text">DATA_ENGINEERING: 90%</text>
    <rect x="0" y="15" width="120" height="4" fill="#30363d" rx="2" />
    <rect x="0" y="15" width="108" height="4" fill="#58a6ff" rx="2" />
    
    <text x="0" y="32" class="hud-text">STATISTICAL_MODEL: 85%</text>
    <rect x="0" y="37" width="120" height="4" fill="#30363d" rx="2" />
    <rect x="0" y="37" width="102" height="4" fill="#58a6ff" rx="2" />

    <text x="0" y="54" class="hud-text">BI_ARCHITECTURE : 95%</text>
    <rect x="0" y="59" width="120" height="4" fill="#30363d" rx="2" />
    <rect x="0" y="59" width="114" height="4" fill="#ffbd2e" rx="2" />
  </g>
  
  <!-- Glowing Pulse dot and Status -->
  <g transform="translate(755, 30)">
    <circle cx="0" cy="0" r="5" class="pulse-dot" />
    <circle cx="0" cy="0" r="8" fill="none" stroke="#238636" stroke-width="1" opacity="0.5">
      <animate attributeName="r" from="5" to="12" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" from="0.5" to="0" dur="2s" repeatCount="indefinite" />
    </circle>
  </g>
  <text x="740" y="33" class="hud-text" text-anchor="end">SYS_ONLINE</text>
  
  <!-- HUD Corner Brackets -->
  <path d="M 10 20 L 20 20 M 10 20 L 10 30" stroke="#30363d" stroke-width="1.5" fill="none" />
  <path d="M 790 20 L 780 20 M 790 20 L 790 30" stroke="#30363d" stroke-width="1.5" fill="none" />
  <path d="M 10 140 L 20 140 M 10 140 L 10 130" stroke="#30363d" stroke-width="1.5" fill="none" />
  <path d="M 790 140 L 780 140 M 790 140 L 790 130" stroke="#30363d" stroke-width="1.5" fill="none" />

  <!-- Stripe-Style Reflection Sweep -->
  <defs>
    <linearGradient id="header-sweep" x1="0%" y1="0%" x2="30%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.08" />
      <stop offset="70%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
  </defs>
  <rect width="800" height="160" fill="url(#header-sweep)" pointer-events="none" rx="12">
    <animate attributeName="x" from="-800" to="800" dur="8s" repeatCount="indefinite" />
  </rect>

  <rect width="800" height="160" class="border" />
</svg>"""
    
    with open(os.path.join(REPO_PATH, "header.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created header.svg")

def create_skills():
    urls = {
        "python": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
        "pandas": "https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg",
        "numpy": "https://raw.githubusercontent.com/devicons/devicon/master/icons/numpy/numpy-original.svg",
        "scikitlearn": "https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg",
        "tensorflow": "https://raw.githubusercontent.com/devicons/devicon/master/icons/tensorflow/tensorflow-original.svg",
        "jupyter": "https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg",
        "mysql": "https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg",
        "git": "https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg"
    }

    base64_data = {}
    for name, url in urls.items():
        print(f"Downloading {name} icon...")
        base64_data[name] = download_and_encode(name, url)

    svg_content = """<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg">
  <style>
    @keyframes fadeInUp {
      from {
        opacity: 0;
        transform: translateY(20px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
    .animate-group {
      opacity: 0;
      animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    .animate-group-0 { animation-delay: 0.1s; }
    .animate-group-1 { animation-delay: 0.2s; }
    .animate-group-2 { animation-delay: 0.3s; }
    .animate-group-3 { animation-delay: 0.4s; }
    .animate-group-4 { animation-delay: 0.5s; }
    .animate-group-5 { animation-delay: 0.6s; }
    .animate-group-6 { animation-delay: 0.7s; }
    .animate-group-7 { animation-delay: 0.8s; }

    .hover-group {
      transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.3s ease;
      cursor: pointer;
    }
    .hover-group:hover {
      transform: translateY(-8px) scale(1.2);
    }
    
    .hover-group.python:hover { filter: drop-shadow(0px 8px 12px rgba(55, 118, 171, 0.8)); }
    .hover-group.pandas:hover { filter: drop-shadow(0px 8px 12px rgba(231, 4, 136, 0.8)); }
    .hover-group.numpy:hover { filter: drop-shadow(0px 8px 12px rgba(77, 119, 207, 0.8)); }
    .hover-group.scikitlearn:hover { filter: drop-shadow(0px 8px 12px rgba(247, 147, 30, 0.8)); }
    .hover-group.tensorflow:hover { filter: drop-shadow(0px 8px 12px rgba(255, 111, 0, 0.8)); }
    .hover-group.jupyter:hover { filter: drop-shadow(0px 8px 12px rgba(243, 118, 38, 0.8)); }
    .hover-group.mysql:hover { filter: drop-shadow(0px 8px 12px rgba(0, 117, 143, 0.8)); }
    .hover-group.git:hover { filter: drop-shadow(0px 8px 12px rgba(240, 80, 50, 0.8)); }

    /* Centered transform-origin for smooth scale from center */
    .python { transform-origin: 65.5px 50px; }
    .pandas { transform-origin: 161.0px 50px; }
    .numpy { transform-origin: 256.5px 50px; }
    .scikitlearn { transform-origin: 352.0px 50px; }
    .tensorflow { transform-origin: 447.5px 50px; }
    .jupyter { transform-origin: 543.0px 50px; }
    .mysql { transform-origin: 638.5px 50px; }
    .git { transform-origin: 734.0px 50px; }
  </style>
"""

    names = ["python", "pandas", "numpy", "scikitlearn", "tensorflow", "jupyter", "mysql", "git"]
    for i, name in enumerate(names):
        x = 35.5 + i * 95.5
        b64 = base64_data[name]
        svg_content += f"""
  <g class="animate-group animate-group-{i}">
    <g class="hover-group {name}">
      <image href="{b64}" x="{x}" y="20" width="60" height="60" />
    </g>
  </g>"""

    svg_content += "\n</svg>"
    
    with open(os.path.join(REPO_PATH, "skills.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created skills.svg")

def create_skills_chart():
    nodes = {
        "python": {"x": 400, "y": 210, "r": 48, "color": "#3776AB", "label": "Python", "icon": "🐍"},
        "data_eng": {"x": 400, "y": 60, "r": 30, "color": "#E67E22", "label": "Data Pipelines", "icon": "☁️"},
        "sql": {"x": 560, "y": 110, "r": 30, "color": "#F39C12", "label": "SQL &amp; DB", "icon": "💾"},
        "feature": {"x": 570, "y": 280, "r": 30, "color": "#2ECC71", "label": "Feature Eng", "icon": "⚙️"},
        "ai_eng": {"x": 450, "y": 350, "r": 30, "color": "#00F0FF", "label": "Generative AI", "icon": "🤖"},
        "stats": {"x": 350, "y": 350, "r": 30, "color": "#1abc9c", "label": "Statistics", "icon": "📊"},
        "data_viz": {"x": 230, "y": 280, "r": 30, "color": "#E74C3C", "label": "BI &amp; Viz", "icon": "🎨"},
        "ml": {"x": 240, "y": 110, "r": 30, "color": "#9B59B6", "label": "Machine Learning", "icon": "🧠"}
    }

    svg_content = """<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg">
  <style>
    .background {
      fill: #080d16;
      rx: 12px;
    }
    .connection {
      stroke-width: 1.5;
      opacity: 0.25;
    }
    .radar-ring {
      fill: none;
      stroke: #30363d;
      stroke-width: 1;
      opacity: 0.3;
    }
    .radar-axis {
      stroke: #30363d;
      stroke-width: 1;
      stroke-dasharray: 4, 8;
      opacity: 0.2;
    }
    .label-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 800;
      font-size: 12px;
      fill: #adbac7;
      letter-spacing: 0.5px;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      pointer-events: none;
    }
    .center-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 900;
      font-size: 14px;
      fill: #ffffff;
      letter-spacing: 1px;
      pointer-events: none;
    }
    .node-group {
      cursor: pointer;
    }
    .glow-python { filter: drop-shadow(0px 0px 8px #3776AB); }
    .glow-data_eng { filter: drop-shadow(0px 0px 8px #E67E22); }
    .glow-sql { filter: drop-shadow(0px 0px 8px #F39C12); }
    .glow-feature { filter: drop-shadow(0px 0px 8px #2ECC71); }
    .glow-ai_eng { filter: drop-shadow(0px 0px 8px #00F0FF); }
    .glow-stats { filter: drop-shadow(0px 0px 8px #1abc9c); }
    .glow-data_viz { filter: drop-shadow(0px 0px 8px #E74C3C); }
    .glow-ml { filter: drop-shadow(0px 0px 8px #9B59B6); }
  </style>

  <!-- Background Card -->
  <rect width="800" height="420" class="background" stroke="#30363d" stroke-width="1.5" />

  <!-- Radar Grid Background -->
  <g>
    <circle cx="400" cy="210" r="90" class="radar-ring" />
    <circle cx="400" cy="210" r="170" class="radar-ring" stroke-dasharray="4, 4" />
    <circle cx="400" cy="210" r="250" class="radar-ring" opacity="0.15" />
    <line x1="80" y1="210" x2="720" y2="210" class="radar-axis" />
    <line x1="400" y1="40" x2="400" y2="380" class="radar-axis" />
  </g>

  <!-- Connection Lines -->
  <g>
"""

    cx, cy = nodes["python"]["x"], nodes["python"]["y"]
    # Write connection lines
    for key, val in nodes.items():
        if key == "python":
            continue
        svg_content += f'    <line x1="{cx}" y1="{cy}" x2="{val["x"]}" y2="{val["y"]}" stroke="{val["color"]}" class="connection" />\n'

    svg_content += "  </g>\n\n  <!-- Animated Data Packets -->\n  <g>\n"
    # Write animated data packets
    for key, val in nodes.items():
        if key == "python":
            continue
        x, y, color = val["x"], val["y"], val["color"]
        # Packet 1
        svg_content += f"""    <circle r="3" fill="{color}" opacity="0.8">
      <animate attributeName="cx" from="{cx}" to="{x}" dur="2.5s" begin="0s" repeatCount="indefinite" />
      <animate attributeName="cy" from="{cy}" to="{y}" dur="2.5s" begin="0s" repeatCount="indefinite" />
    </circle>"""
        # Packet 2
        svg_content += f"""
    <circle r="3" fill="{color}" opacity="0.8">
      <animate attributeName="cx" from="{cx}" to="{x}" dur="2.5s" begin="1.25s" repeatCount="indefinite" />
      <animate attributeName="cy" from="{cy}" to="{y}" dur="2.5s" begin="1.25s" repeatCount="indefinite" />
    </circle>\n"""

    svg_content += "  </g>\n\n  <!-- Skill Nodes -->\n"

    # Write nodes
    satellites = {
        "data_eng": 4.0,
        "sql": 5.5,
        "feature": 3.2,
        "ai_eng": 6.8,
        "stats": 4.5,
        "data_viz": 5.0,
        "ml": 3.8
    }

    for key, val in nodes.items():
        x, y, r, color, label, icon = val["x"], val["y"], val["r"], val["color"], val["label"], val.get("icon", "")
        
        svg_content += f"""  <!-- Node: {label} -->
  <g class="node-group">
"""
        if key == "python":
            svg_content += f"""    <!-- Node Body -->
    <circle cx="{x}" cy="{y}" r="{r + 5}" fill="{color}" opacity="0.2" class="glow-python" />
    <circle cx="{x}" cy="{y}" r="{r}" fill="#0d1117" stroke="{color}" stroke-width="2.5" />
    <text x="{x}" y="{y + 5}" text-anchor="middle" class="center-text">{label.upper()}</text>
  </g>
"""
        else:
            svg_content += f"""    <!-- Outer Ring border -->
    <circle cx="{x}" cy="{y}" r="35" fill="none" stroke="{color}" stroke-width="1" opacity="0.25" />
    <!-- Node Body -->
    <circle cx="{x}" cy="{y}" r="{r + 3}" fill="{color}" opacity="0.1" class="glow-{key}" />
    <circle cx="{x}" cy="{y}" r="{r}" fill="#0d1117" stroke="{color}" stroke-width="1.5" />
    <circle cx="{x}" cy="{y}" r="{r - 4}" fill="{color}" opacity="0.05" />
    <!-- Icon Inside circle -->
    <text x="{x}" y="{y + 7}" text-anchor="middle" font-size="18" font-family="-apple-system, BlinkMacSystemFont, sans-serif">{icon}</text>
    <!-- Label -->
"""
            text_y = y + r + 22 if y >= 210 else y - r - 12
            svg_content += f'    <text x="{x}" y="{text_y}" text-anchor="middle" class="label-text">{label}</text>\n  </g>\n'

    svg_content += """
  <!-- Stripe-Style Reflection Sweep -->
  <defs>
    <linearGradient id="radar-sweep" x1="0%" y1="0%" x2="30%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.06" />
      <stop offset="70%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
  </defs>
  <rect width="800" height="420" fill="url(#radar-sweep)" pointer-events="none" rx="12">
    <animate attributeName="x" from="-800" to="800" dur="10s" repeatCount="indefinite" />
  </rect>
</svg>"""

    with open(os.path.join(REPO_PATH, "skills-chart.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created skills-chart.svg")

def create_soft_skills():
    skills = [
        {"key": "adaptiveness", "name": "Adaptiveness", "color": "#2ECC71", "desc": "Quick learner &amp; resilient", "icon": "⚡"},
        {"key": "strategy", "name": "Data Strategy", "color": "#00F0FF", "desc": "Business value alignment", "icon": "📈"},
        {"key": "analytical", "name": "Analytical", "color": "#9B59B6", "desc": "Root cause data extraction", "icon": "🧠"},
        {"key": "communication", "name": "Communication", "color": "#F39C12", "desc": "Clear team collaboration", "icon": "💬"},
        {"key": "problem", "name": "Problem Solving", "color": "#E74C3C", "desc": "Analytical debug mindset", "icon": "🔍"}
    ]

    svg_content = """<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .card-group {
      cursor: pointer;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .card-glow {
      transition: opacity 0.3s ease;
      opacity: 0;
    }
    .card-main {
      transition: stroke 0.3s ease, fill 0.3s ease;
    }
    .card-group:hover {
      transform: translateY(-6px);
    }
    .card-group:hover .card-glow {
      opacity: 0.65;
    }
    .card-title {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 800;
      font-size: 13px;
      fill: #ffffff;
    }
    .card-desc {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 500;
      font-size: 9px;
      fill: #8b949e;
    }
    .card-icon {
      font-size: 20px;
    }
    
    .card-group.card-adaptiveness:hover .card-main { stroke: #2ECC71; }
    .card-group.card-strategy:hover .card-main { stroke: #00F0FF; }
    .card-group.card-analytical:hover .card-main { stroke: #9B59B6; }
    .card-group.card-communication:hover .card-main { stroke: #F39C12; }
    .card-group.card-problem:hover .card-main { stroke: #E74C3C; }

    .card-adaptiveness { transform-origin: 90px 57.5px; }
    .card-strategy { transform-origin: 245px 57.5px; }
    .card-analytical { transform-origin: 400px 57.5px; }
    .card-communication { transform-origin: 555px 57.5px; }
    .card-problem { transform-origin: 710px 57.5px; }

    /* CSS drop-shadow instead of SVG filter elements */
    .glow-adaptiveness { filter: drop-shadow(0px 0px 8px #2ECC71); }
    .glow-strategy { filter: drop-shadow(0px 0px 8px #00F0FF); }
    .glow-analytical { filter: drop-shadow(0px 0px 8px #9B59B6); }
    .glow-communication { filter: drop-shadow(0px 0px 8px #F39C12); }
    .glow-problem { filter: drop-shadow(0px 0px 8px #E74C3C); }
  </style>
"""

    card_w = 135
    card_h = 75
    gap = 20
    start_x = 22.5
    y = 20

    for i, s in enumerate(skills):
        x = start_x + i * (card_w + gap)
        
        svg_content += f"""
  <g class="card-group card-{s["key"]}">
    <!-- Glow layer -->
    <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="10" ry="10" fill="{s["color"]}" class="card-glow glow-{s["key"]}" />
    <!-- Card Body -->
    <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="10" ry="10" fill="#0d1117" stroke="#30363d" stroke-width="1.5" class="card-main" />
    <!-- Icon -->
    <text x="{x + 15}" y="{y + 35}" class="card-icon">{s["icon"]}</text>
    <!-- Title -->
    <text x="{x + 15}" y="{y + 52}" class="card-title">{s["name"]}</text>
    <!-- Description -->
    <text x="{x + 15}" y="{y + 64}" class="card-desc">{s["desc"]}</text>
  </g>"""

    svg_content += "\n</svg>"

    with open(os.path.join(REPO_PATH, "soft-skills.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created soft-skills.svg")

def create_about_me():
    svg_content = """<svg viewBox="0 0 800 360" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg { fill: #0d1117; stroke: #30363d; stroke-width: 1.5; rx: 12px; }
    .dot { stroke-width: 0; }
    .dot-red { fill: #ff5f56; }
    .dot-yellow { fill: #ffbd2e; }
    .dot-green { fill: #27c93f; }
    .text {
      font-family: 'Fira Code', Consolas, Monaco, 'Courier New', monospace;
      font-size: 13px;
      fill: #adbac7;
    }
    .ln { fill: #57606a; text-anchor: end; user-select: none; }
    .keyword { fill: #ff7b72; font-weight: bold; }
    .class-name { fill: #d2a8ff; }
    .function-name { fill: #79c0ff; }
    .string { fill: #a5d6ff; }
    .comment { fill: #8b949e; font-style: italic; }
    .self { fill: #ff7b72; }
    .variable { fill: #79c0ff; }
  </style>
  
  <rect width="800" height="360" class="bg" />
  
  <circle cx="25" cy="20" r="6" class="dot dot-red" />
  <circle cx="45" cy="20" r="6" class="dot dot-yellow" />
  <circle cx="65" cy="20" r="6" class="dot dot-green" />
  
  <text x="35" y="60" class="text ln">1</text>
  <text x="35" y="80" class="text ln">2</text>
  <text x="35" y="100" class="text ln">3</text>
  <text x="35" y="120" class="text ln">4</text>
  <text x="35" y="140" class="text ln">5</text>
  <text x="35" y="160" class="text ln">6</text>
  <text x="35" y="180" class="text ln">7</text>
  <text x="35" y="200" class="text ln">8</text>
  <text x="35" y="220" class="text ln">9</text>
  <text x="35" y="240" class="text ln">10</text>
  <text x="35" y="260" class="text ln">11</text>
  <text x="35" y="280" class="text ln">12</text>
  <text x="35" y="300" class="text ln">13</text>
  <text x="35" y="320" class="text ln">14</text>
  
  <text x="60" y="60" class="text"><tspan class="keyword">class</tspan> <tspan class="class-name">PritamPalit</tspan>:</text>
  <text x="60" y="80" class="text">    <tspan class="keyword">def</tspan> <tspan class="function-name">__init__</tspan>(<tspan class="self">self</tspan>):</text>
  <text x="60" y="100" class="text">        <tspan class="self">self</tspan>.<tspan class="variable">name</tspan> = <tspan class="string">"Pritam Palit"</tspan></text>
  <text x="60" y="120" class="text">        <tspan class="self">self</tspan>.<tspan class="variable">role</tspan> = <tspan class="string">"Data Analyst &amp; Business Analyst"</tspan></text>
  <text x="60" y="140" class="text">        <tspan class="self">self</tspan>.<tspan class="variable">location</tspan> = <tspan class="string">"Kolkata, India"</tspan></text>
  <text x="60" y="160" class="text">        <tspan class="self">self</tspan>.<tspan class="variable">experience</tspan> = {</text>
  <text x="60" y="180" class="text">            <tspan class="string">"HDFC Life"</tspan>: <tspan class="string">"Sales &amp; Data Analyst Intern (Jan 24 - Aug 24)"</tspan>,</text>
  <text x="60" y="200" class="text">            <tspan class="string">"Coding Ninjas"</tspan>: <tspan class="string">"Social Media &amp; Data Analyst Intern (Jun 22 - Dec 22)"</tspan></text>
  <text x="60" y="220" class="text">        }</text>
  <text x="60" y="240" class="text">        <tspan class="self">self</tspan>.<tspan class="variable">education</tspan> = <tspan class="string">"B.Tech in Electronics &amp; Communication Eng (2020-2024)"</tspan></text>
  <text x="60" y="260" class="text">        <tspan class="self">self</tspan>.<tspan class="variable">certifications</tspan> = [</text>
  <text x="60" y="280" class="text">            <tspan class="string">"Google Data Analytics"</tspan>, <tspan class="string">"Microsoft Power BI (PL-300)"</tspan>, <tspan class="string">"Scaler DSML (In Progress)"</tspan></text>
  <text x="60" y="300" class="text">        ]</text>
  <text x="60" y="320" class="text">        <tspan class="comment"># Turning data noise into actionable strategic signals...</tspan></text>
  <defs>
    <linearGradient id="about-sweep" x1="0%" y1="0%" x2="30%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.05" />
      <stop offset="70%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
  </defs>
  <rect width="800" height="360" fill="url(#about-sweep)" pointer-events="none" rx="12">
    <animate attributeName="x" from="-800" to="800" dur="9s" repeatCount="indefinite" />
  </rect>
</svg>"""
    
    with open(os.path.join(REPO_PATH, "about_me.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created about_me.svg")

def create_experience():
    svg_content = """<svg viewBox="0 0 800 320" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg { fill: #080d16; rx: 12px; }
    .border { stroke: #30363d; stroke-width: 1.5; fill: none; rx: 12px; }
    .card { fill: #0d1117; stroke: #30363d; stroke-width: 1; rx: 10px; }
    .card-title {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 800;
      font-size: 15px;
      fill: #ffffff;
    }
    .card-sub {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 600;
      font-size: 12px;
    }
    .card-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: 11px;
      fill: #adbac7;
    }
    .metric {
      font-weight: 800;
    }
    .badge {
      font-family: monospace;
      font-size: 9px;
      font-weight: bold;
    }
  </style>

  <!-- Background Card -->
  <rect width="800" height="320" class="bg" />

  <!-- Left Card: HDFC Life -->
  <g>
    <rect x="25" y="30" width="360" height="260" fill="none" stroke="#58a6ff" stroke-width="2" rx="10" opacity="0.15" />
    <rect x="25" y="30" width="360" height="260" class="card" />
    
    <text x="45" y="60" class="card-title">Sales &amp; Data Analyst Intern</text>
    <text x="45" y="78" class="card-sub" fill="#58a6ff">HDFC Life Insurance • Jan - Aug 2024</text>
    
    <rect x="45" y="90" width="110" height="18" rx="4" fill="#238636" opacity="0.2" />
    <rect x="45" y="90" width="110" height="18" rx="4" fill="none" stroke="#238636" stroke-width="0.8" />
    <text x="100" y="102" class="badge" fill="#39d353" text-anchor="middle">⏱️ SAVED 5+ HRS/WK</text>
    
    <circle cx="50" cy="132" r="2.5" fill="#58a6ff" />
    <text x="60" y="135" class="card-text">Automated Excel dashboards via Power Query, reducing</text>
    <text x="60" y="150" class="card-text">reporting cycles by <tspan fill="#58a6ff" class="metric">30%</tspan> and saving <tspan fill="#39d353" class="metric">5+ hours/week</tspan>.</text>
    
    <circle cx="50" cy="182" r="2.5" fill="#58a6ff" />
    <text x="60" y="185" class="card-text">Segmented <tspan fill="#58a6ff" class="metric">10,000+</tspan> customer transaction records using SQL,</text>
    <text x="60" y="200" class="card-text">increasing lead qualification rates by <tspan fill="#58a6ff" class="metric">12%</tspan>.</text>
    
    <circle cx="50" cy="232" r="2.5" fill="#58a6ff" />
    <text x="60" y="235" class="card-text">Developed self-service dashboards, cutting ad-hoc</text>
    <text x="60" y="250" class="card-text">reporting requests by <tspan fill="#58a6ff" class="metric">40%</tspan> for <tspan fill="#58a6ff" class="metric">20+</tspan> stakeholders.</text>
  </g>

  <!-- Right Card: Coding Ninjas -->
  <g>
    <rect x="415" y="30" width="360" height="260" fill="none" stroke="#ff7b72" stroke-width="2" rx="10" opacity="0.15" />
    <rect x="415" y="30" width="360" height="260" class="card" />
    
    <text x="435" y="60" class="card-title">Social Media &amp; Data Analyst Intern</text>
    <text x="435" y="78" class="card-sub" fill="#ff7b72">Coding Ninjas • Jun - Dec 2022</text>
    
    <rect x="435" y="90" width="110" height="18" rx="4" fill="#da3633" opacity="0.2" />
    <rect x="435" y="90" width="110" height="18" rx="4" fill="none" stroke="#da3633" stroke-width="0.8" />
    <text x="490" y="102" class="badge" fill="#f85149" text-anchor="middle">📈 ENGAGEMENT +20%</text>
    
    <circle cx="440" cy="132" r="2.5" fill="#ff7b72" />
    <text x="450" y="135" class="card-text">Boosted audience engagement by <tspan fill="#ff7b72" class="metric">20%</tspan> via analytics-driven</text>
    <text x="450" y="150" class="card-text">content optimization and metrics analysis.</text>
    
    <circle cx="440" cy="182" r="2.5" fill="#ff7b72" />
    <text x="450" y="185" class="card-text">Executed A/B test campaigns, raising click-through rates</text>
    <text x="450" y="200" class="card-text">(<tspan fill="#ff7b72" class="metric">CTR</tspan>) by <tspan fill="#ff7b72" class="metric">15%</tspan> and reducing CPA by <tspan fill="#ff7b72" class="metric">10%</tspan>.</text>
    
    <circle cx="440" cy="232" r="2.5" fill="#ff7b72" />
    <text x="450" y="235" class="card-text">Built weekly tracker reports covering <tspan fill="#ff7b72" class="metric">8 key KPIs</tspan></text>
    <text x="450" y="250" class="card-text">to optimize 5 concurrent digital campaigns.</text>
  </g>

  <!-- Stripe-Style Reflection Sweep -->
  <defs>
    <linearGradient id="exp-sweep" x1="0%" y1="0%" x2="30%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.06" />
      <stop offset="70%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
  </defs>
  <rect width="800" height="320" fill="url(#exp-sweep)" pointer-events="none" rx="12">
    <animate attributeName="x" from="-800" to="800" dur="8s" repeatCount="indefinite" />
  </rect>

  <rect width="800" height="320" class="border" />
</svg>"""
    
    os.makedirs(os.path.join(REPO_PATH, "assets"), exist_ok=True)
    with open(os.path.join(REPO_PATH, "assets", "experience.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created experience.svg")

if __name__ == "__main__":
    create_header()
    create_skills()
    create_skills_chart()
    create_soft_skills()
    create_about_me()
    create_experience()
