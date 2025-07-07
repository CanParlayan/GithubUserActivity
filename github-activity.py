#!/usr/bin/env python3

import json
import http.client
import argparse
import sys
from datetime import datetime


def get_github_events(username):
    connection = None
    try:
        connection = http.client.HTTPSConnection("api.github.com")
        headers = {
            'User-Agent': 'GitHub-Activity-CLI/1.0',
            'Accept': 'application/vnd.github.v3+json',
            'X-Poll-Interval': '60',
            'ETag': '"a18c3bded88eb5dbb5c849a489412bf3"'
        }

        print(f"Fetching events for user: {username}")
        connection.request("GET", f"/users/{username}/events", headers=headers)
        response = connection.getresponse()

        if response.status == 200:
            data = response.read().decode('utf-8')
            return json.loads(data)
        elif response.status == 404:
            print(f"Error: User '{username}' not found.")
            return None
        elif response.status == 403:
            print("Error: API rate limit exceeded. Please try again later.")
            return None
        elif response.status == 500:
            print("Error: GitHub API server error. Please try again later.")
            return None
        elif response.status == 503:
            print("Error: GitHub API service unavailable. Please try again later.")
            return None
        else:
            print(f"Error: {response.status} - {response.reason}")
            return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON response from GitHub API.")
        return None
    except Exception as e:
        print(f"Error: Failed to connect to GitHub API - {str(e)}")
        return None
    finally:
        connection.close()


def format_event(event):
    event_type = event.get('type', 'Unknown')
    repo_name = event.get('repo', {}).get('name', 'Unknown')
    created_at = event.get('created_at', '')

    if created_at:
        try:
            dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            time_str = dt.strftime('%Y-%m-%d %H:%M')
        except ValueError:
            time_str = created_at[:16]
    else:
        time_str = 'Unknown time'

    if event_type == 'PushEvent':
        commits = event.get('payload', {}).get('commits', [])
        commit_count = len(commits)
        return f"- [{time_str}] Pushed {commit_count} commit{'s' if commit_count != 1 else ''} to {repo_name}"

    elif event_type == 'IssuesEvent':
        action = event.get('payload', {}).get('action', 'unknown')
        return f"- [{time_str}] {action.capitalize()} an issue in {repo_name}"

    elif event_type == 'WatchEvent':
        return f"- [{time_str}] Starred {repo_name}"

    elif event_type == 'CreateEvent':
        ref_type = event.get('payload', {}).get('ref_type', 'repository')
        return f"- [{time_str}] Created {ref_type} in {repo_name}"

    elif event_type == 'ForkEvent':
        return f"- [{time_str}] Forked {repo_name}"

    elif event_type == 'PullRequestEvent':
        action = event.get('payload', {}).get('action', 'unknown')
        return f"- [{time_str}] {action.capitalize()} a pull request in {repo_name}"

    elif event_type == 'ReleaseEvent':
        action = event.get('payload', {}).get('action', 'unknown')
        return f"- [{time_str}] {action.capitalize()} a release in {repo_name}"

    elif event_type == 'DeleteEvent':
        ref_type = event.get('payload', {}).get('ref_type', 'branch')
        return f"- [{time_str}] Deleted {ref_type} in {repo_name}"
    elif event_type == 'MemberEvent':
        action = event.get('payload', {}).get('action', 'unknown')
        return f"- [{time_str}] {action.capitalize()} a member in {repo_name}"
    elif event_type == 'PublicEvent':
        return f"- [{time_str}] Made {repo_name} public"
    elif event_type == 'IssuesCommentEvent':
        action = event.get('payload', {}).get('action', 'unknown')
        return f"- [{time_str}] {action.capitalize()} a comment on an issue in {repo_name}"
    elif event_type == 'CommitCommentEvent':
        return f"- [{time_str}] Commented on a commit in {repo_name}"
    else:
        return f"- [{time_str}] {event_type.replace('Event', '')} in {repo_name}"


def display_events(events, limit):
    if not events:
        print("No recent activity found.")
        return

    print(f"\nRecent Activity (showing up to {limit} events):")
    print("-" * 50)

    displayed_count = 0
    for event in events:
        if displayed_count >= limit:
            break

        formatted_event = format_event(event)
        print(formatted_event)
        displayed_count += 1

    if len(events) > limit:
        print(f"\n... and {len(events) - limit} more events")


def main():
    parser = argparse.ArgumentParser(
        prog="github-activity",
        description="A CLI tool to fetch and display GitHub user's recent activity."
    )
    parser.add_argument(
        "username",
        help="GitHub username to fetch events for"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Number of events to display (default: 10)"
    )

    args = parser.parse_args()

    if not args.username.strip():
        print("Error: Username cannot be empty.")
        sys.exit(1)

    if args.limit <= 0:
        print("Error: Limit must be a positive integer.")
        sys.exit(1)

    events = get_github_events(args.username.strip())

    if events is None:
        sys.exit(1)

    display_events(events, args.limit)


if __name__ == "__main__":
    main()
