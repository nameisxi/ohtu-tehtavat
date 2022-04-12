from query import Query
from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or


class QueryBuilder:
    def __init__(self, query=All()):
        self.query = query

    def playsIn(self, team):
        return QueryBuilder(And(self.query, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query, HasFewerThan(value, attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1, query2))

    def build(self):
        return self.query
