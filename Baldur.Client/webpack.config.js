const path = require("path");

module.exports = {
    resolve: {
        extensions: ['.ts', '.tsx', '.js', '.graphql'],
    },
    module: {
        rules: [
            {
                test: /\.(graphql)|(gql)$/,
                use: "graphql-tag/loader",
                exclude: path.resolve(__dirname, "node_modules")
            }
        ]
    }
};

