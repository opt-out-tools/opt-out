# Let's Stop It - Sexual Cyber Harassment and Sexist Hate Speech

A tool to help people avoid online sexual harassment by filtering out unwanted comments from Facebook or Twitter.

## Contribute

To install or mofify the extension you'll need to run it locally.

```sh
git clone https://github.com/malteserteresa/stop-it
cd stop-it
npm install    # Install all dependencies
npm run build  # Build the extension so it's ready for the browser
npm run watch  # Listen for file changes and auto-rebuild
```

After building the extension:
- Open `about:debugging#addons`
- Click on the `Load Temporary Add-on` button
- Select the file stop-it/extension/manifest.json
