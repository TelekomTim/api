const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

const cors = require('cors');

app.use(cors()); // This will enable all CORS requests

app.use((req, res, next) => {
  res.setHeader('Content-Security-Policy', "default-src 'self'; script-src 'self' https://airtable.com; connect-src 'self' https://airtable.com;");
  next();
});
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