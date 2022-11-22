import graphene
import ipdb

class Query(graphene.ObjectType):
  hello = graphene.String(name=graphene.String(default_value="World"))

  hi = graphene.String(name=graphene.String(default_value="World"))

  def resolve_hello(self, info, name):
    return 'Hello ' + name

  def resolve_hi(self, info, name):
    return 'Hi ' + name

schema = graphene.Schema(query=Query)

query = '''
query {
  hello(name: "Earth")
  hi(name: "Moon")
}
'''

result = schema.execute(query)
print(result)

query = '''
query {
  hello
  hi
}
'''
result = schema.execute(query)
print(result)
# print()
# print(result.data['hello']) # "Hello World"
