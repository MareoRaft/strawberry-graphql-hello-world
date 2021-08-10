I followed the [docs](https://strawberry.rocks/docs) and it worked.

The installation command `pip install strawberry-graphql[debug-server]` must use python 3 and preferably a newer one, and must be run in bash.  So for me I had to run `bash` and then `pip3 install strawberry-graphql[debug-server]`.



## Install
in `bash` (NOT zsh), run

    # for the server
    pip3 install strawberry-graphql[debug-server]
    # for the client
    pip3 install --pre gql[all]



## Run GraphQL Server

    cd src/server
    strawberry server schema


## Query the server

sample query:

    {
      books {
        author
      }
    }

To run the client script to perform a query, run:

    cd src/client
    python3 query.py
