 var path = require('path');
 var webpack = require('webpack');

 module.exports = {
     entry: path.join(__dirname,'start.js'),
     output: {
         path: path.resolve(__dirname, '../static/js'),
         filename: 'main.bundle.js'
     },
     module: {
         loaders: [
             {
                 test: /\.js$/,
                 loader: 'babel-loader',
                 query: {
                     presets: ['es2015']
                 }
             }
         ]
     },
     stats: {
         colors: true
     },
     devtool: 'source-map',
	 watch: true,
	 watchOptions:{
		aggregateTimeout:300,
		ignored: /node_modules/
	 }
 };
