const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: {
    // Content
    'content/opt-out-ext.js': './src/content/opt-out-ext.js',
    // Popup
    'popup/popup-main.js': './src/popup/popup-main.js'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name]'
  },
  module: {
    rules: []
  },
  optimization: {
    minimize: false
  },
  // Copies static assets to correct places
  plugins: [
    new CopyPlugin([
      // Extension Static Assests
      { from: './src/index-1.html', to: './index-1.html' },
      { from: './src/manifest.json', to: './manifest.json' },
      { from: './src/README.md', to: './README.md' },
      { from: './src/icons', to: './icons' },
      // Content Static Assets
      { from: './src/content/opt-out.css', to: './content/opt-out.css' },
      // Popup Static Assets
      { from: './src/popup/assets', to: './popup/assets' },
      { from: './src/popup/popup.html', to: './popup/popup.html' }
    ])
  ],
  devtool: 'inline-source-map'
};
