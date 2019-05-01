# Stop It <img src='logo_stopit.png' align="right" height="165" />

[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com)

## Contribute

To install or mofify the extension you'll need to run it locally.

```sh
git clone https://github.com/malteserteresa/stop-it # Clone it locally
cd stop-it/extension # Go to the extension directory
npm install    # Install all dependencies
npm run build  # Build the extension so it's ready for the browser
npm run watch  # Listen for file changes and auto-rebuild
```

After building the extension:
- Open `about:debugging#addons` in Firefox
- Click on the `Load Temporary Add-on` button
- Select the file `stop-it/extension/dist/manifest.json`
