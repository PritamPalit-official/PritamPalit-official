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
    svg_content = """<svg viewBox="0 0 800 120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 900;
      font-size: 54px;
      fill: url(#gradient-fill);
      letter-spacing: 5px;
      text-shadow: 0px 0px 20px rgba(0, 240, 255, 0.4);
    }
    .subtitle {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 600;
      font-size: 16px;
      fill: #8b949e;
      letter-spacing: 4px;
      opacity: 0.8;
    }
  </style>
  <defs>
    <linearGradient id="gradient-fill" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%">
        <animate attributeName="stop-color" values="#ff007f;#7f00ff;#00f0ff;#ff007f" dur="8s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%">
        <animate attributeName="stop-color" values="#00f0ff;#ff007f;#7f00ff;#00f0ff" dur="8s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
  </defs>
  <text x="50%" y="65" text-anchor="middle" class="title">PRITAM PALIT</text>
  <text x="50%" y="100" text-anchor="middle" class="subtitle">DATA SCIENTIST • AI ENGINEER • VIBE CODER</text>
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
        "python": {"x": 400, "y": 200, "r": 45, "color": "#3776AB", "glow": "rgba(55,118,171,0.8)", "label": "Python"},
        "vibe": {"x": 400, "y": 50, "r": 32, "color": "#FF007F", "glow": "rgba(255,0,127,0.8)", "label": "Vibe Coding"},
        "sql": {"x": 550, "y": 100, "r": 32, "color": "#F39C12", "glow": "rgba(243,156,18,0.8)", "label": "SQL & DB"},
        "feature": {"x": 560, "y": 280, "r": 32, "color": "#2ECC71", "glow": "rgba(46,204,113,0.8)", "label": "Feature Eng"},
        "prompting": {"x": 450, "y": 350, "r": 32, "color": "#00F0FF", "glow": "rgba(0,240,255,0.8)", "label": "AI Prompting"},
        "stats": {"x": 350, "y": 350, "r": 32, "color": "#1abc9c", "glow": "rgba(26,188,156,0.8)", "label": "Statistics"},
        "data_viz": {"x": 240, "y": 280, "r": 32, "color": "#E74C3C", "glow": "rgba(231,76,60,0.8)", "label": "Data Viz"},
        "ml": {"x": 250, "y": 100, "r": 32, "color": "#9B59B6", "glow": "rgba(155,89,182,0.8)", "label": "Machine Learning"}
    }

    svg_content = """<svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <style>
    .background {
      fill: none;
    }
    .connection {
      stroke-dasharray: 6, 6;
      stroke-width: 2;
      opacity: 0.6;
      animation: dashflow 4s linear infinite;
    }
    @keyframes dashflow {
      to {
        stroke-dashoffset: -40;
      }
    }
    .node-group {
      cursor: pointer;
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .node-glow {
      transition: opacity 0.3s ease;
      opacity: 0.3;
    }
    .node-group:hover {
      transform: scale(1.12);
    }
    .node-group:hover .node-glow {
      opacity: 0.9;
    }
    .node-circle {
      stroke-width: 2;
      stroke: #fff;
    }
    .label-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: bold;
      font-size: 13px;
      fill: #adbac7;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      pointer-events: none;
    }
    .center-text {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-weight: 900;
      font-size: 15px;
      fill: #ffffff;
      pointer-events: none;
    }
    
    /* Transform origins specified in style block to keep tag structure clean */
    .node-python { transform-origin: 400px 200px; }
    .node-vibe { transform-origin: 400px 50px; }
    .node-sql { transform-origin: 550px 100px; }
    .node-feature { transform-origin: 560px 280px; }
    .node-prompting { transform-origin: 450px 350px; }
    .node-stats { transform-origin: 350px 350px; }
    .node-data_viz { transform-origin: 240px 280px; }
    .node-ml { transform-origin: 250px 100px; }
  </style>

  <defs>
    <filter id="blur-effect" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="8" />
    </filter>
  </defs>

  <rect width="800" height="400" class="background" />
  
  <!-- Connections -->
  <g>
"""

    cx, cy = nodes["python"]["x"], nodes["python"]["y"]
    for key, val in nodes.items():
        if key == "python":
            continue
        svg_content += f'    <line x1="{cx}" y1="{cy}" x2="{val["x"]}" y2="{val["y"]}" stroke="{val["color"]}" class="connection" />\n'

    svg_content += "  </g>\n\n  <!-- Nodes -->\n"

    for key, val in nodes.items():
        x, y, r, color, glow, label = val["x"], val["y"], val["r"], val["color"], val["glow"], val["label"]
        
        svg_content += f"""  <g class="node-group node-{key}">
    <!-- Outer Glow -->
    <circle cx="{x}" cy="{y}" r="{r + 12}" fill="{color}" filter="url(#blur-effect)" class="node-glow" />
    <!-- Node Body -->
    <circle cx="{x}" cy="{y}" r="{r}" fill="#161b22" stroke="{color}" class="node-circle" />
    <circle cx="{x}" cy="{y}" r="{r - 5}" fill="{color}" opacity="0.15" />
    <!-- Text Label -->
"""
        if key == "python":
            svg_content += f'    <text x="{x}" y="{y + 5}" text-anchor="middle" class="center-text">{label.upper()}</text>\n  </g>\n'
        else:
            text_y = y + r + 20 if y >= 200 else y - r - 10
            svg_content += f'    <text x="{x}" y="{text_y}" text-anchor="middle" class="label-text">{label}</text>\n  </g>\n'

    svg_content += "</svg>"

    with open(os.path.join(REPO_PATH, "skills-chart.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Created skills-chart.svg")

def create_soft_skills():
    skills = [
        {"key": "adaptiveness", "name": "Adaptiveness", "color": "#2ECC71", "desc": "Quick learner & resilient", "icon": "⚡"},
        {"key": "prompting", "name": "Prompting", "color": "#00F0FF", "desc": "AI system orchestration", "icon": "🤖"},
        {"key": "vibe", "name": "Vibe Coding", "color": "#FF007F", "desc": "Coding in flow state", "icon": "🎵"},
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
    
    /* Hover stroke colors and transform origins in stylesheet */
    .card-group.card-adaptiveness:hover .card-main { stroke: #2ECC71; }
    .card-group.card-prompting:hover .card-main { stroke: #00F0FF; }
    .card-group.card-vibe:hover .card-main { stroke: #FF007F; }
    .card-group.card-communication:hover .card-main { stroke: #F39C12; }
    .card-group.card-problem:hover .card-main { stroke: #E74C3C; }

    .card-adaptiveness { transform-origin: 90px 57.5px; }
    .card-prompting { transform-origin: 245px 57.5px; }
    .card-vibe { transform-origin: 400px 57.5px; }
    .card-communication { transform-origin: 555px 57.5px; }
    .card-problem { transform-origin: 710px 57.5px; }
  </style>

  <defs>
    <filter id="soft-blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="6" />
    </filter>
  </defs>
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
    <rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="10" ry="10" fill="{s["color"]}" filter="url(#soft-blur)" class="card-glow" />
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

if __name__ == "__main__":
    create_header()
    create_skills()
    create_skills_chart()
    create_soft_skills()
