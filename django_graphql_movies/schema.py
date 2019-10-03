import graphene
import graphql_jwt
import django_graphql_movies.movies.schema

class Query(django_graphql_movies.movies.schema.Query, graphene.ObjectType):
    pass

class Mutation(django_graphql_movies.movies.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
