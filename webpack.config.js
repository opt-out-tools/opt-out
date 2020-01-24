const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: {
    // Bundles entry points for js for each part of web ext
    'content/opt-out-ext.js': './src/content/opt-out-ext.js',
    'popup/popup-main.js': './src/popup/popup-main.js'
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name]'
  },
  // Copies static assets to correct place
  plugins: [
    new CopyPlugin([
      { from: './src/index-1.html', to: './index-1.html' },
      { from: './src/manifest.json', to: './manifest.json' },
      { from: './src/README.md', to: './README.md' },
      { from: './src/icons', to: './icons' },
      { from: './src/content/opt-out.css', to: './content/opt-out.css' },
      { from: './src/popup/assets', to: './popup/assets' },
      { from: './src/popup/popup.html', to: './popup/popup.html' }
    ])
  ],
  devtool: 'inline-source-map'
};
