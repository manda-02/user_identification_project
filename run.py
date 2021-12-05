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

    def __init__(self, data, arr):
        self.data = data
        self.arr = {}

    def __repr__(self):
        return f"A.{self.data}"
        
    def array():
        return self.arr

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

properties = [s,t,b,g,d,q,c,f,p,a,r]


# At least one of these will be true
nick = Users("nick", {s, ~t, ~b, ~g, d, q, ~c, f, p, ~a, ~r})
amanda = Users("amanda", {s, t, ~b, ~g, d, q, c, f, p, ~a, ~r})
vanshita = Users("vanshita", {~s, ~t, b, ~g, d, q, c, f, p, ~a, ~r})
adam = Users("adam", {s, t, ~b, ~g, d, q, ~c, f, p, ~a, ~r})
jimmy = Users("jimmy", {s, ~t, b, g, d, ~q, c, ~f, ~p, a, r})
moira = Users("moira", {s, t, b, ~g, d, ~q, c, ~f, p, ~a, ~r})
gary = Users("gary", {s, ~t, b, g, ~d, ~q, ~c, ~f, ~p, ~a, ~r})

def getInput():

    inputs = []
    questions = ["Plays Soccer? T/F\n","Plays Soccer Intramurals? T/F\n","Plays Music? T/F\n","Plays Guitar? T/F\n","Is a Student? T/F\n","Is a Queen's Student? T/F\n","Is In a School Club? T/F\n","Is In a Specialization? T/F\n","Is Taking School in Person? T/F\n","Is a First Year Student? T/F\n","Is Living on Residence? T/F\n"]

    print("Choose True (' T ') or False (' F ') for the following characteristics and we'll return who most likely sent the message out of the following users:\n Nick, \n Amanda, \n Vanshita, \n Adam, \n Jimmy, \n Moira, \n Gary\n")
    
    for v in questions:
        temp = input(v)
        inputs.append(temp)
        
        
    return inputs
    


def checkInputs(inputs):

    for input in inputs:
        if "T" != input:
            if "F" != input:
                print("Please enter valid response")
                return False
    
    
def initializingInputs(inputs):
        
    for i in range(0, len(inputs)):
        if inputs[i] == "T":
            E.add_constraint(properties[i])
        elif inputs[i] == "F":
            E.add_constraint(~properties[i])
            
def findWinners(T):

    solutions = []
    count = 0
    for v in [nick,amanda,vanshita,adam,jimmy,moira,gary]:
        temp = likelihood(T, v)
        if temp > count:
            count = temp
            solutions.append(v.data)
    
    for v in [nick,amanda,vanshita,adam,jimmy,moira,gary]:
        temp = likelihood(T, v)
        if temp == count:
            if v.data != solutions[0]:
                solutions.append(v.data)
    
    print("the highest probablity user(s):\n")
    for i in solutions:
        print(i, "\n")
        
    print("With a likelihood of: \n", (100 * count), "%")
        


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():

    #USER CONSTRAINTS
    E.add_constraint((s & ~t & ~b & ~g & d & q & ~c & f & p & ~a & ~r) >> nick)
    E.add_constraint((s & t & ~b & ~g & d & q & c & f & p & ~a & ~r) >> amanda)
    E.add_constraint((~s & ~t & b & ~g & d & q & c & f & p & ~a & ~r) >> vanshita)
    E.add_constraint((s & t & ~b & ~g & d & q & ~c & f & p & ~a & ~r) >> adam)
    E.add_constraint((s & ~t & b & g & d & ~q & c & ~f & ~p & a & r) >> jimmy)
    E.add_constraint((s & t & b & ~g & d & ~q & c & ~f & p & ~a & ~r) >> moira)
    E.add_constraint((s & ~t & b & g & ~d & ~q & ~c & ~f & ~p & ~a & ~r) >> gary)
    
    #PROPERTY CONTRAINTS
    E.add_constraint((t | q | c | f | p | a | r)>>d)
    E.add_constraint((q & a) >> r)
    E.add_constraint(t >> (s & d))
    E.add_constraint(f >> ~(a))
    E.add_constraint(~(b) >> ~(g))
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
    
    inputs = getInput()
    check = checkInputs(inputs)
    while check is False:
        inputs = getInput()
        check = checkInputs(inputs)
    
    initializingInputs(inputs)
        
    return E
    


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    try:
        print("\nSatisfiable: %s" % T.satisfiable())
        print("# Solutions: %d" % count_solutions(T))
        print("   Solution: %s" % T.solve())
    
        findWinners(T)
    
        print("\nVariable likelihoods:")
        for v,vn in zip([nick, amanda, vanshita, adam, jimmy, moira, gary], ['Nick','Amanda','Vanshita','Adam','Jimmy','Moira','Gary',]):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
            print(" %s: %.2f" % (vn, likelihood(T, v)))
    except:
            print("Error Calculating Solution (Make sure to adhere to logical constraints: i.e. if you play guitar then you play music, etc.)")
    finally:
            print("Program Concluded.")
    print()
