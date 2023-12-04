const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/myendpoint', (req, res) => {
  const receivedString = req.body.data;
  console.log('Received String:', receivedString);

  // Process the received string as needed
    

  res.json({ message: 'String received successfully' });
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});