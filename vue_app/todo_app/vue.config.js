module.exports = {
    devServer: {
      proxy: {
        '/api/v1': {
          target: 'http://127.0.0.1:8000',
          ws: true,
          changeOrigin: true
        }
      }
    }
  }