def find_matches(people):
    for (i,p1) in enumerate(people):
        for p2 in people[i+1:]:
            if p1['spouse'] and p2['spouse']:
                if p1['spouse'] == p2['name']:
                    print "Match1: {p1} {p2}".format(p1=p1['name'],p2=p2['name'])
                    yield(p1,p2)
                elif p1['spouse'] in p2['name'] and p2['spouse'] in p1['name']:
                    print "Match2: {p1} {p2}".format(p1=p1['name'],p2=p2['name'])
                    yield(p1,p2)
                elif p2['spouse'] == p1['name']:
                    print "Match3: {p1} {p2}".format(p1=p1['name'],p2=p2['name'])
                    yield(p1,p2)
                elif p2['spouse'] in p1['name'] and p1['spouse'] in p2['name']:
                    print "Match4: {p1} {p2}".format(p1=p1['name'],p2=p2['name'])
                    yield(p1,p2)
            else:
                p1last = p1['name'].split()[-1]
                p2last = p2['name'].split()[-1]
                if p1['spouse']:
                    if p1['spouse'] in p2['name'] and p1last == p2last:
                        print "Match5: {p1} {p2}".format(p1=p1['name'],p2=p2['name'])
                        yield(p1,p2)
                if p2['spouse']:
                    if p2['spouse'] in p1['name'] and p2last == p1last:
                        print "Match6: {p1} {p2}".format(p1=p1['name'],p2=p2['name'])
                        yield(p1,p2)
