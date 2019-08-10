const HtmlWebPackPlugin = require("html-webpack-plugin")
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    entry: './src/index.js',
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: "babel-loader"
            },
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
                exclude: /node_modules/
            },
            {
                test: /\.(graphql|gql)$/,
                exclude: /node_modules/,
                use: "graphql-tag/loader"
            },
            {
                test: /\.html$/,
                use: "html-loader"
            },
            {
                test: /\.scss$/,
                use: [
                    "style-loader",
                    "css-loader",
                    "sass-loader"
                ]
            }
        ],
    },
    resolve: {
        extensions: [ '.tsx', '.ts', '.js', '.jsx' ]
    },
    plugins: [
        new HtmlWebPackPlugin({
            template: "./src/index.html",
            filename: "./index.html"
        }),
        //new BundleAnalyzerPlugin()
    ],
    devServer: {
        historyApiFallback: true
    },
    output: {
        publicPath: '/'
    }
}
