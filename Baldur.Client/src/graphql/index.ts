import gql from "graphql-tag";

export const getUserEmail = (id: number) => gql`
    query {
        user(q: "${id}") {
            email
        }
    }
`;

