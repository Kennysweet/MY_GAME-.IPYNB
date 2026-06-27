const { exec } = require('child_process');
const path = require('path');

const url = 'http://127.0.0.1:8000/index.html';

const command = process.platform === 'win32'
  ? `start "" "${url}"`
  : process.platform === 'darwin'
    ? `open "${url}"`
    : `xdg-open "${url}"`;

exec(command, (error) => {
  if (error) {
    console.error('Could not open browser automatically:', error.message);
    console.log('Please open this URL manually: ' + url);
  } else {
    console.log('Opened game in browser: ' + url);
  }
});
