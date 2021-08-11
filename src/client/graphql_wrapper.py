'''
This file exposes a `query` function for convenient GraphQL querying.

This is nothing but a wrapper around the gql library.  The point is merely to hide-away the configuration stuff in this file, so that the actual usage in all other files is minimal.
'''
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# The URL for the GraphQL server
SERVER_URL = "http://localhost:8000"

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url=SERVER_URL)
# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

def query(query_name):
    # get query string from file
    file_path = f'queries/{query_name}.graphql'
    query_string = open(file_path).read()
    # turn it into a GraphQL query
    gql_query = gql(query_string)
    # Execute the query on the transport
    result = client.execute(gql_query)
    return result
