import helpers, algorithms
predicates = [
    ['loc', '=', 'montreal'],
    ['loc', '=', 'new york'],
    ['loc', '=', 'addis ababa'],
    ['budget', '<', 2000],
    ['budget', '>=', 2000],
    ['pname', '=', 'test']
]

queries = [
    "select * from projects where budget < 2000",
    "select * from projects where budget >= 2000",
    "select * from projects where loc = 'montreal'",
    "select * from projects where loc = 'new york'",
    "select * from projects where loc = 'paris'",
]

application_need = helpers.get_application_needs(queries)

algorithms.com_min('test_db', predicates, application_need)