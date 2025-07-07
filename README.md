# GitHub Activity CLI[https://roadmap.sh/projects/github-user-activity]

A simple command-line tool to fetch and display a GitHub user's recent activity.  

## 📝 Description  

This project is a CLI application that retrieves a GitHub user's recent activity using the GitHub API and displays it in the terminal. It helps you practice working with APIs, handling JSON data, and building CLI tools.  

## 🚀 Features  

- Fetch a GitHub user's recent activity via the GitHub API.  
- Display the activity in a clean, readable format.  
- Gracefully handle errors (e.g., invalid usernames, API failures).  

## 🔧 Requirements  

- A GitHub username (to fetch activity for).  
- No external libraries needed—uses native HTTP requests.  

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
[https://api.github.com/users/kamranahmedse/events](https://api.github.com/users/kamranahmedse/events)  

## 🛠️ Built With  

- Any programming language of your choice (Python, JavaScript, Go, etc.).  
- Native HTTP requests (no external libraries).  

## 🔍 Possible Extensions  

For a more advanced version, consider:  
- Filtering activity by event type (pushes, issues, stars, etc.).  
- Structured output (e.g., tables, JSON).  
- Caching to improve performance.  
- Exploring other GitHub API endpoints for richer data.  

## 📚 Resources  

- [GitHub API Documentation](https://docs.github.com/en/rest)  

---

This version improves readability with proper Markdown formatting, clear sections, and consistent styling. Let me know if you'd like any modifications! 🚀
