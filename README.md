I followed the [docs](https://strawberry.rocks/docs) and it worked.

The installation command `pip install strawberry-graphql[debug-server]` must use python 3 and preferably a newer one, and must be run in bash.  So for me I had to run `bash` and then `pip3 install strawberry-graphql[debug-server]`.



## Install
in `bash` (NOT zsh), run

    pip3 install strawberry-graphql[debug-server]



## Run GraphQL Server

    cd src
    strawberry server schema
