issues_code=$(curl -X GET -u $GITHUB_TOKEN:x-oauth-basic 'https://api.github.com/repos/vmg/redcarpet/issues?sort="comments"+per_page=100' -H "Accept: application/vnd.github.squirrel-girl-preview")

echo $issues_code >> fetched_issues.txt
