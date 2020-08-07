import enum, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

class BugStatus(enum.Enum):
    new           = 7
    incomplete    = 6
    invalid       = 5
    wont_fix      = 4
    in_progress   = 3
    fix_committed = 2
    fix_released  = 1

class intBugStatus(enum.IntEnum):
    """enum.IntEnum class supports its members to behave more like numbers -- aka to support comparisons
    """
    new           = 7
    incomplete    = 6
    invalid       = 5
    wont_fix      = 4
    in_progress   = 3
    fix_committed = 2
    fix_released  = 1   


@addBreaker
def enum_create(e: enum):
    print('\nMember name : {}'.format(BugStatus.wont_fix.name))
    print('Member value: {}'.format(BugStatus.wont_fix.value))

@addBreaker
def enum_vs_dict():
    BugStatus = dict(
        new           = 7,
        incomplete    = 6,
        invalid       = 5,
        wont_fix      = 4,
        in_progress   = 3,
        fix_committed = 2,
        fix_released  = 1,
    )
    
    print('\nMember name : {}'.format(BugStatus.keys()))
    print('Member value: {}'.format(BugStatus['wont_fix'])) 

@addBreaker
def enum_iterate(e: enum):
    for status in e:
        print('{:15} = {}'.format(status.name, status.value))

@addBreaker
def enum_comp(e: enum):
    actual_state = e.wont_fix
    desire_state = e.fix_released

    print('Equality:', actual_state == desire_state, actual_state == e.wont_fix)
    print('Identity:', actual_state is desire_state, actual_state is e.wont_fix)

    print('Ordered by value:')
    try:
        print('\n'.join('  ' + s.name for s in sorted(e)))
    except TypeError as err:
        print('  cannot sort: {}'.format(err))

# TODOS: P107









def main():
    # create enum
    enum_create(BugStatus)
    # i can't figure out what fuck merit from enum though. Dict() produces the same output with less lines of code, doesn't it?
    # tries to find out merit ..
    enum_vs_dict()
    # iterates an enum
    enum_iterate(BugStatus)
    # enum inner element comparison
    enum_comp(BugStatus)
    # enum.IntEnum
    enum_comp(intBugStatus)

if __name__ == "__main__":
    main()