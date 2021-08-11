from graphql_wrapper import query

# This demonstrates the usage
# Yes!  It's that simple!  Just put the name of your query.  Create the file queries/myqueryname.graphql and put the query there.
result = query('authors')

print(result)
