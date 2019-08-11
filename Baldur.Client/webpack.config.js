const path = require("path")
const HtmlWebPackPlugin = require("html-webpack-plugin")
//const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;


module.exports = {
    entry: './src/index.js',
    resolve: {
        extensions: [ '.tsx', '.ts', '.js', '.jsx' ],
        alias: {
            shared: path.resolve(__dirname, "./src/shared"),
            components: path.resolve(__dirname, "./src/components"),
            views: path.resolve(__dirname, "./src/views")
        }
    },
    devServer: {
        historyApiFallback: true
    },
    output: {
        publicPath: '/'
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: "babel-loader"
            },
            {
                test: /\.tsx?$/,
                exclude: /node_modules/,
                use: 'ts-loader',
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
    plugins: [
        new HtmlWebPackPlugin({
            template: "./src/index.html",
            filename: "./index.html"
        }),
        //new BundleAnalyzerPlugin()
    ]
}
