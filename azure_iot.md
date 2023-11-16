### View message from json file
`cat file.json | jq -r`  

### Decode json file Body
`cat file.json | jq -r ".Body" | base64 --decode`  
