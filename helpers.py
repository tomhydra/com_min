def parse_query(query, relation):
    '''
        Simple query parser
        This function works for queries of the following format

        format => "select * from projects where budget < 2000"

        NB: It only accepts queries with one predicate
    '''
    q, p = query.split('where')
    relation_name = q.split('from')[1].strip()
    predicate = p.strip().replace("'" ,"").split(' ')
    if relation == relation_name: # check if its the correct relation
        return predicate

def get_application_needs(queries):
    application_needs = []
    for q in queries:
        application_needs.append(parse_query(q, 'projects'))
    return application_needs

