# Script that queries the GraphQL server
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="http://localhost:8000")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# get query string
query_string = open('queries/books.graphql').read()

# Provide a GraphQL query
query = gql(query_string)

# Execute the query on the transport
result = client.execute(query)
print(result)
