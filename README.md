# GitHub User Activity CLI

A lightweight Python command-line tool that shows a user's recent **public GitHub events** in your terminal. Built as a [roadmap.sh project](https://roadmap.sh/projects/github-user-activity).

## Features

- Retrieves public activity from the GitHub Events API.
- Formats pushes, issues, pull requests, stars, and other events.
- Lets you limit how many events are displayed.
- Reports common API/network errors.

## Requirements

- Python 3
- Internet access

No third-party Python packages are required.

## Getting started

```bash
git clone https://github.com/CanParlayan/GithubUserActivity.git
cd GithubUserActivity
python github-activity.py CanParlayan
```

To display up to five events:

```bash
python github-activity.py CanParlayan --limit 5
```

Replace `CanParlayan` with any public GitHub username.

## Example output

```text
Recent Activity (showing up to 5 events):
--------------------------------------------------
- [2025-07-08 14:00] Pushed 3 commits to owner/repository
- [2025-07-08 13:00] Opened an issue in owner/repository
```

*Illustrative output; actual events and timestamps will differ.*

## Data source and limitations

The script calls:

```text
GET https://api.github.com/users/<username>/events
```

Only public events exposed by GitHub are available. The API can be rate-limited, and the list of recent events is not a complete history.

The executable file in this repository is **`github-activity.py`**. Run it with `python`; the command `github-activity` is not installed globally by this project.
