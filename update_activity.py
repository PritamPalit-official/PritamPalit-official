import urllib.request
import json
import re
import os

username = "PritamPalit-official"
url = f"https://api.github.com/users/{username}/events/public"

try:
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    with urllib.request.urlopen(req) as response:
        events = json.loads(response.read().decode('utf-8'))
except Exception as e:
    print(f"Error fetching events: {e}")
    events = []

formatted_lines = []
seen_activities = set() # To prevent duplicate activities in the feed

for e in events:
    if len(formatted_lines) >= 5:
        break
        
    repo_name = e['repo']['name']
    repo_url = f"https://github.com/{repo_name}"
    # Filter out profile repo to prevent infinite loop of commits
    if repo_name.lower() == f"{username}/{username}".lower():
        continue
        
    type_ = e['type']
    payload = e.get('payload', {})
    
    line = ""
    activity_key = ""
    
    if type_ == "PushEvent":
        commits = payload.get('commits', [])
        if not commits:
            continue
        msg = commits[0].get('message', '').split('\n')[0]
        # truncate if message is too long
        if len(msg) > 60:
            msg = msg[:57] + "..."
        count = len(commits)
        if count == 1:
            line = f"📝 Pushed: *\"{msg}\"* to [{repo_name}]({repo_url})"
        else:
            line = f"📝 Pushed {count} commits to [{repo_name}]({repo_url}) (latest: *\"{msg}\"*)"
        activity_key = f"push-{repo_name}-{msg}"
            
    elif type_ == "CreateEvent":
        ref_type = payload.get('ref_type', '')
        ref = payload.get('ref', '')
        if ref_type == "repository":
            line = f"🚀 Created repository [{repo_name}]({repo_url})"
        elif ref_type == "branch":
            line = f"🌿 Created branch `{ref}` in [{repo_name}]({repo_url})"
        activity_key = f"create-{ref_type}-{repo_name}-{ref}"
            
    elif type_ == "WatchEvent":
        action = payload.get('action', '')
        if action == "started":
            line = f"⭐ Starred repository [{repo_name}]({repo_url})"
        activity_key = f"star-{repo_name}"
            
    elif type_ == "PullRequestEvent":
        action = payload.get('action', '')
        pr = payload.get('pull_request', {})
        pr_title = pr.get('title', '')
        pr_url = pr.get('html_url', '')
        if len(pr_title) > 50:
            pr_title = pr_title[:47] + "..."
        line = f"🔀 {action.capitalize()} PR [#{pr.get('number', '')} {pr_title}]({pr_url}) in [{repo_name}]({repo_url})"
        activity_key = f"pr-{action}-{repo_name}-{pr.get('number', '')}"
        
    elif type_ == "IssuesEvent":
        action = payload.get('action', '')
        issue = payload.get('issue', {})
        issue_title = issue.get('title', '')
        issue_url = issue.get('html_url', '')
        if len(issue_title) > 50:
            issue_title = issue_title[:47] + "..."
        line = f"🐛 {action.capitalize()} issue [#{issue.get('number', '')} {issue_title}]({issue_url}) in [{repo_name}]({repo_url})"
        activity_key = f"issue-{action}-{repo_name}-{issue.get('number', '')}"

    if line and activity_key not in seen_activities:
        formatted_lines.append(f"- {line}")
        seen_activities.add(activity_key)

# Fallback if no activity is found
if not formatted_lines:
    formatted_lines.append("- No recent activity found.")

activity_text = "\n".join(formatted_lines)

# Now replace the activity section in README.md
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace content between tags
    pattern = r"(<!--START_SECTION:activity-->)(.*?)(<!--END_SECTION:activity-->)"
    replacement = f"\\1\n{activity_text}\n\\3"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully updated README.md with recent activity!")
else:
    print("README.md not found!")
