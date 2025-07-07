# [Github User Activity CLI](https://roadmap.sh/projects/github-user-activity)

A simple command-line tool to fetch and display a GitHub user's recent activity.  

## 📝 Description  

This project is a CLI application that retrieves a GitHub user's recent activity using the GitHub API and displays it in the terminald  

## 🚀 Features  

- Fetches a GitHub user's recent activity via the GitHub API.  
- Displays the activity in a clean, readable format.  
- Gracefully handles errors (e.g., invalid usernames, API failures).
  
## 📌 Usage  

Run the CLI with a GitHub username as an argument:  

```sh
github-activity <username>
```  

Example:  
```sh
github-activity kamranahmedse
```  

### Example Output  

```
- Pushed 3 commits to kamranahmedse/developer-roadmap  
- Opened a new issue in kamranahmedse/developer-roadmap  
- Starred kamranahmedse/developer-roadmap  
- ...  
```  

## 🌐 API Endpoint  

The tool uses the GitHub Events API:  

```
GET https://api.github.com/users/<username>/events
```  
Example:  
[https://api.github.com/users/CanParlayan/events](https://api.github.com/users/CanParlayan/events)  

