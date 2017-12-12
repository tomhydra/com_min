operator_negations = {
    '<': '>=',
    '>': '<=',
    '>=': '<',
    '<=': '>',
    '=': '!=',
    '!=': '='
}

def com_min(R, Pr, application):
    '''
        @params
        R: string
        Pr: list of lists
        application: list of lists
    '''
    _Pr = []  # set of simple predicates
    complete_predicates = generate_complete_predicates(Pr, application)
    _Pr.append(complete_predicates.pop())

    while len(complete_predicates):
        _Pr.append(complete_predicates.pop())
        if not relevant(_Pr):
            _Pr.pop()
    print(_Pr)
    return _Pr


def generate_complete_predicates(Pr, application):
    cp = []
    for pr in Pr:
        if pr[0] in [x[0] for x in application]:
            cp.append(pr)
    return cp


def relevant(Pr):
    last_item = Pr[len(Pr) - 1]
    for item in Pr:
        if item == negation(last_item):
            return False
    return True


def negation(item):
    return [item[0], operator_negations[item[1]], item[2]]

