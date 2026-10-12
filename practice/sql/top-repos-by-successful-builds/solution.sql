SELECT repo_name, COUNT(status) AS success_count 
FROM ci_builds
WHERE status = 'success' 
GROUP BY repo_name
ORDER BY success_count DESC, repo_name 
