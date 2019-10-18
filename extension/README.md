
## Development

- start Mozilla Firefox
- set url to: 
```
about:debugging#/runtime/this-firefox
```
- click 
```
Load Teporary Add-ons
```
- open manifest.json of this extension
- when adding new changes to files click "reload" (left of "remove" button) to apply new changes to script 


## Tweeter Edge Cases

- ##### Logged User
  - tweet (text + media)
  - re-tweet (same as above)
  - quote (re-tweet with a comment above)
  - reply
  
- ##### Non-logged user
  - regular text tweet - contains text + media content (image, video, link) (optional)
  - quote
  - re-tweet
  
Tweeter tweet lists
  - home
  - explore
  - notifications
  - lists
