const http = require('http');
const handler = require('serve-handler');

const port = process.env.PORT || 3000;

const server = http.createServer((request, response) => {
  return handler(request, response, {
    public: 'dist',
    cleanUrls: false,
    trailingSlash: false
  });
});

server.listen(port, () => {
  console.log(`SHARK website server running on port ${port}`);
});
