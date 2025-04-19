const express = require('express');

const PORT = 8080;

function main() {
  const app = express();

  app.get('/', (req, res) => {
    res.send('I hate javascript!');
  });

  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
}

main();
