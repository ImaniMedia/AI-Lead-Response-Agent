
// webhook_listener.js
// This script listens for incoming webhooks and processes them.

const express = require('express');
const app = express();
app.use(express.json());

app.post('/lead-inquiry', (req, res) => {
    const inquiry = req.body;
    console.log('New Inquiry Received:', inquiry);
    // Forward to AI processing logic here
    res.send({status: 'Received', inquiry});
});

app.listen(3000, () => {
    console.log('Webhook listener running on port 3000');
});
