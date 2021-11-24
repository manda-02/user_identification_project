from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class Properties:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class Users:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
s = Properties("soccer")
t = Properties("soocer_int")   
b = Properties("music")
g = Properties("guitar")
d = Properties("student")
q = Properties("queens_student")
c = Properties("school_club")
f = Properties("specialization")
p = Properties("in_person")
a = Properties("first_year")
r = Properties("on_res")

# At least one of these will be true
nick = Users("nick")
amanda = Users("amanda")
vanshita = Users("vanshita")
adam = Users("adam")
jimmy = Users("jimmy")
moira = Users("moira")
gary = Users("gary")

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    
    #USER CONSTRAINTS
    E.add_contraint(nick >> (s & d & q & f & p))
    E.add_contraint(amanda >> (s & t & d & q & c & f & p))
    E.add_contraint(vanshita >> (b & d & q & c & f & p))
    E.add_contraint(adam >> (s & t & d & q & f & p))
    E.add_contraint(jimmy >> (s & g & b &d & c & a & r))
    E.add_contraint(moira >> (s & t & b & p & d & c))
    E.add_contraint(gary >> (g & b & s))
    
    #PROPERTY CONTRAINTS
    E.add_constraint((t | q | c | f | p | a | r)>>d)
    E.add_constraint((q & a) >> r)
    E.add_constraint(t >> (s & d))
    E.add_constraint(f >> (a).negate())
    E.add_constraint((b).negate() >> (g).negate())
    E.add_constraint(g >> b)
    E.add_constraint(c >> d)
    
    #PROPERTY-TO-USER CONTRAINTS
    E.add_constraint(s >> (nick | amanda | adam | jimmy | moira))
    E.add_constraint(t >> (amanda | adam | jimmy | moira))
    E.add_constraint(b >> (vanshita |  jimmy | moira | gary))
    E.add_constraint(g >> (jimmy | gary))
    E.add_constraint(d >> (nick | amanda | vanshita | adam | jimmy | moira))
    E.add_constraint(q >> (nick | amanda | vanshita | adam))
    E.add_constraint(c >> (amanda | vanshita | jimmy | moira))
    E.add_constraint(f >> (nick | amanda | vanshita | adam))
    E.add_constraint(p >> (nick | amanda | vanshita | adam | moira))
    E.add_constraint(a >> (jimmy))
    E.add_constraint(r >> (jimmy))
    
    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
