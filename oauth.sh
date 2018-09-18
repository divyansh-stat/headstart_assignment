github_token_code=$(curl -X POST -u "divyansh-stat":"" -H 'Content-Type: application/json' -d '{"scopes": ["user:email"],"note": "Head Start Assignment"}' https://api.github.com/authorizations)

echo $github_token_code >> token.txt
