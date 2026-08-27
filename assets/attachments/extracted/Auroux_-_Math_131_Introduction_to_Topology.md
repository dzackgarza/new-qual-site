Math 131: Introduction to Topology 1
Professor Denis Auroux
Fall, 2019
Contents
9/4/2019 - Introduction, Metric Spaces, Basic Notions 3
9/9/2019 - Topological Spaces, Bases 9
9/11/2019 - Subspaces, Products, Continuity 15
9/16/2019 - Continuity, Homeomorphisms, Limit Points 21
9/18/2019 - Sequences, Limits, Products 26
9/23/2019 - More Product Topologies, Connectedness 32
9/25/2019 - Connectedness, Path Connectedness 37
9/30/2019 - Compactness 42
10/2/2019 - Compactness, Uncountability, Metric Spaces 45
10/7/2019 - Compactness, Limit Points, Sequences 49
10/9/2019 - Compactiﬁcations and Local Compactness 53
10/16/2019 - Countability, Separability, and Normal Spaces 57
10/21/2019 - Urysohn’s Lemma and the Metrization Theorem 61
1 Please email Beckham Myers at bmyers@college.harvard.edu with any corrections, questions, or comments. Any
mistakes or errors are mine.

10/23/2019 - Category Theory, Paths, Homotopy 64
10/28/2019 - The Fundamental Group(oid) 70
10/30/2019 - Covering Spaces, Path Lifting 75
11/4/2019 - Fundamental Group of the Circle, Quotients and Gluing 80
11/6/2019 - The Brouwer Fixed Point Theorem 85
11/11/2019 - Antipodes and the Borsuk-Ulam Theorem 88
11/13/2019 - Deformation Retracts and Homotopy Equivalence 91
11/18/2019 - Computing the Fundamental Group 95
11/20/2019 - Equivalence of Covering Spaces and the Universal Cover 99
11/25/2019 - Universal Covering Spaces, Free Groups 104
12/2/2019 - Seifert-Van Kampen Theorem, Final Examples 109
2

9/4/2019 - Introduction, Metric Spaces, Basic Notions
The instructor for this course is Professor Denis Auroux. His email is auroux@math.harvard.edu
and his oﬃce is SC539. He will be hosting oﬃce hours Monday 12:30-2 and Tuesday 9-10:30. The
course website is http://math.harvard.edu/ auroux/131f19/. All information will be posted on the
course webpage, although we will use Canvas to record grades.
There will be homework due every week on Wednesday, along with a take-home midterm and
an in class ﬁnal. We will loosely follow Munkres’ Topology. The only prerequisites are some famil-
iarity with the notion of a group and some comfort with metric spaces/the ability to manipulate
open and closed sets.
Introduction
Broadly, geometry is the study of measuring quantities. Mathematicians then use these measure-
ments to make conclusions about properties of the spaces being studied. Topology, on the other
hand, studies spaces by asking questions from a qualitative perspective. For example, some topo-
logical questions include:
• Is a space connected?
• Is a space simply connected? This question provides a technique for distinguishing between
a sphere and a torus. For on the torus, there exist closed curves which cannot be ‘shrunk’ to
a point.
• Is a space oriented? For example, the regular cylinder is oriented (as it has two sides), while
the M¨ obius space is not (it has only one side). Note that there are easier ways to distinguish
these two, namely by examining their boundaries.
Algebraic topology is the ﬁeld that studies invariants of topological spaces that measure these above
properties. For example, the fundamental group measures how far a space is from being simply
connected. Before this, however, we will develop the language of point set topology, which extends
the theory to a much more abstract setting than simply metric spaces.
Today we will remain informal, but a topological space is an abstraction of metric spaces. In
short, a topological space is a set equipped with the additional data necessary to make sense of
what it means for points to be ‘close’ to each other. This will allow us to develop notions of limits
and continuity.
3

The Power of Abstraction - Example from Analysis
We have the following classical theorem:
Theorem (The Extreme Value Theorem) . Given a continuous function f : [a,b ]→ R, f
achieves is maximum and minimum in the interval [a,b ].
This theorem can be generalized to the following:
Theorem. Given a continuous function f : C → R from a compact set C, f achieves its
maximum and minimum in C.
And this is itself a special case of an even more general theorem:
Theorem. Given a continuous function f : C→ X from a compact set C to a topological
spaceX, the image of f is compact.
This is one excellent example of the power of abstraction, as we can take existing results and
expand them to vastly more generalize situations.
We will introduce metric spaces in order to motivate the deﬁnition of topological spaces (otherwise,
the deﬁnition seems a bit arbitrary).
Metric spaces and open sets
Deﬁnition. A metric space is a pair (X,d ), where X is a set and d : X×X → R≥0 is the
distance function. d should satisfy
1. d(x,x ) = 0 and d(x,y )> 0 when x⁄=y, for all x,y∈X.
2. d(x,y ) =d(y,x ), namely d is symmetric.
3. d(x,z )≤ d(x,y ) +d(y,z ) for all x,y,z ∈ X. This is the triangle inequality , which says
that the shortest path between two points is the ‘straight line’ between them.
Examples
• The vector space Rn with the Euclidean distance
d(x,y ) =
vuu√
n∑
i=0
(yi−xi)2
where x = (x1,...,x n),y = (y1,...,y n) ∈ Rn, is a metric space. This is the usual
distance in space. It’s easy to check that this indeed deﬁnes a metric on the space Rn.
• LetY ⊂ Rn. Then Y becomes a metric space under the induced metric. In particular,
we deﬁne a metric on Y by simply restricting the metric d|Y×Y on X.
4

Note that this is not always the appropriate metric to use on a subspace. For exam-
ple, the surface of the earth is a subset of space, but we don’t usually measure the
distance between two points on the earth by simply drawing a straight line between them
in space.
• We can deﬁne another metric on Rn by taking
d∞(x,y ) = max
i
|yi−xi|
You will check this a metric on the ﬁrst homework.
• We can deﬁne another metric on Rn by taking
d1(x,y ) =
n∑
i=1
|yi−xi|
Once we have a notion of distance, we can discuss open sets. The idea of topological spaces will be
to bypass the notion of distance and simply consider these open sets.
Deﬁnition. Given a metric space (X,d ) and a point p∈ X, the open ball of radius r∈ R>0
aroundp is
Br(p) ={q∈X :d(p,q )<r}
Such an open ball is sometimes referred to as the open neighborhood of p of radius r.
Open balls are instances of open sets.
Deﬁnition. A subset U ⊂ X is open if, for every point x∈ U, there exists ϵ > 0 such that
Bϵ(x)⊂U.
The idea is that, in a open set, there exists a ‘safety margin’ around every point. Given a point p,
one can move around in the set a certain distance and remain in the sense.
Some basic properties of open sets are
1. Open balls are open. This is a basic consequence of the triangle inequality. It is on the ﬁrst
homework.
5

2. ∅ is open (vacuously).
3. X is open (as all open balls are contained in X).
4. The arbitrary union of open sets is open (even inﬁnitely many). This follows easily from the
deﬁnition.
5. The intersection of ﬁnitely many open sets is open.
It is important to note that we can only expect that the intersection of ﬁnitely many open sets is
still open. For example, open intervals are open in R, but the intersection
⋂
n∈N
(
− 1
n, 1
n
)
={0}
is not open (as there are no open balls around 0 contained in {0}).
Limits and closed sets
One very important notion in the theory of metric spaces is that of a sequence. Let ( X,d ) be a
metric space.
Deﬁnition. A sequence p1,p 2,... ∈X converges to a limit p∈X if, for all ϵ >0, there exists
some N∈ N such that for all n≥N we have d(pn,p )<ϵ .
Lemma. If a sequence in a metric space converges to a limit, this limit is unique.
This is false in a general topological space. We will discuss the properties of a topological space
that will guarantee a sequence has a unique limit.
We can formulate the notion of the convergence of a sequence without mentioning the limit point.
In this case, we want that the points of a sequence become arbitrarily close to each other (whereas
above, we demanded that the points become arbitrarily close to a given point p).
Deﬁnition. A sequence p1,p 2,... ∈ X is Cauchy if, for all ϵ >0, there exists N∈ N such that
for all n,m≥N we have d(pn,pm)<ϵ .
It is easy to prove that a converging sequence is Cauchy using the triangle inequality. The idea is
that, if all the points are becoming arbitrarily close to a given point p, then they are also becoming
close to each other. The converse is not always true, however.
Deﬁnition. A metric space is complete if every Cauchy sequence also converges to a point.
In fact, every metric space X is sitting inside a larger, complete metric space X.
Remark. Given a metric space X, one can construct the completion of a metric space by consid-
ering the space of all Cauchy sequences in X up to an appropriate equivalence relation. Then this
space of Cauchy sequences is itself a metric space which restricts to the original metric space X.
Deﬁnition. A set Z⊂X is closed if the complement X\Z is open.
6

Remark. A subset does not need to be open or closed. Subsets can be open, closed, open and closed,
or neither open nor closed.
For example, ∅ and X are always both open and closed. We also have an alternative deﬁnition of
closedness that applies in particular to metric spaces (whereas the above deﬁnition is the same for
topological spaces).
Proposition. In a metric space X, a subset Z⊂ X is closed if and only if for every sequence
p1,p 2,... ∈Z that converges to a point p∈X, we have p∈Z.
So in a metric space, these two deﬁnitions are equivalent. In a topological space, the second
deﬁnition does not necessarily imply the ﬁrst.
Proof. We will prove the forward implication by contradiction. Suppose there exists a sequence
{pn : n∈ N} with pn∈ Z that converges to a point p∈ X\Z. Then for all r >0, there exists
N∈ N such that for all n≥N,d(pn,p )<r . Thus Br(p)∩Z⁄= ∅ for all r> 0, and Br(p)⁄⊂X\Z,
which means that X\Z is not open, and hence Z is not closed.
Conversely, suppose for contradiction that Z is not closed. Then X\Z is not open, so take
p∈X\Z such that Br(p)∩Z⁄= ∅ for all r >0. For each n∈ N, let pn∈B1/n(p)∩Z. Then the
sequence p1,p 2,... converges to p∈X\Z.
Continuity
We’ll now introduce the notion of continuity for maps between metric spaces.
Deﬁnition. A function f : X→ Y between metric spaces (X,dX) and (Y,dY ) is continuous if
for all x∈ X and all ϵ >0, there exists δ >0 such that for all p∈ X with d(p,x ) < δ, we have
d(f(p),f (x))<ϵ . In other words, we have
f(Bδ(x))⊂Bϵ(f(x))
The idea is that, as points in the domain X become close together, their images under f become
close together as well. There is in fact another characterization of continuity that doesn’t involve
as many quantiﬁers. This is how we will ultimately characterize continuity in arbitrary topological
spaces.
Theorem. A functionf :X→Y is continuous if and only if for all open sets U⊂Y , the preimage
f−1(U)⊂X is open.
Proof. Assume thatf :X→Y is continuous. Let U⊂Y be an open set. We want to showf−1(U)
is open, so let p∈f−1(U). Since U is open and f(p)∈U, we can take ϵ> 0 small enough so that
Bϵ(f(p))⊂U. By continuity, there exists δ >0 such that f(Bδ(p))⊂Bϵ(f(p))⊂U, which means
Bδ(p)⊂f−1(U). Hence f−1(U) is open.
7

Conversely, assume for all open U⊂Y we have that f−1(U) is open. We want to show f is con-
tinuous. Let p∈X and let ϵ> 0. The set Bϵ(f(p)) is open, so f−1(Bϵ(f(p))) is open and contains
p. Then by deﬁnition of an open set, there exists a radius δ >0 such that Bδ(p)⊂f−1(Bϵ(f(p))).
This implies f(Bδ(p))⊂Bϵ(f(p)), so f is continuous as desired.
This lays the groundwork for deﬁning a topological space, which is a space in which one can extend
all of these ideas of open/closed sets, limits and continuity without a distance function.
Deﬁnition. A topologyT on a set X is a set of subsets of X (which are the open sets) that satisfy
1. ∅,X ∈T .
2. Arbitrary unions of elements of T are inT .
3. Finite intersections of elements of T are inT .
Note that these are exactly the properties we noted above for metric spaces. Next time we will give
many examples of spaces that illustrate how pathological these can become.
One reason why we consider such an abstract deﬁnition is because there are topological spaces
which are not metric spaces. For example, the space of continuous functions from [ a,b ] to R can
be given a topology that does not arise from a metric.
8

9/9/2019 - Topological Spaces, Bases
Today we will begin to discuss topological spaces.2
Deﬁnition. A topological space is a set X with a topology T . A topology is a collection T ⊂
P(X).3 These are the open sets of X.T must satisfy
1. ∅,X ∈T
2. If Ui∈T for i∈I, then ⋃
iUi∈T (arbitrary unions of open sets are open)
3. If U1,...,U n∈T , then U1∩... ∩Un∈T (ﬁnite intersections of open sets are open)
This deﬁnition formalizes the properties we saw for metric spaces and generalizes the notion of
being open in the abstract. As before, we deﬁne the following.
Deﬁnition. A subset Z⊂X is closed if X\Z is open.
It is easy to prove the following proposition with basic set theory.
Proposition. We have
1. ∅,X are closed
2. Arbitrary intersections of closed sets are closed
3. Finite unions of closed sets are closed
We will see that such spaces can be in fact quite pathological, but we will ﬁrst start with some
basic examples.
Basic Examples
• Let (X,d ) be a metric space. Then the set
T ={U⊂X : for all x∈U there exists r> 0 such that Br(x)⊂U}
deﬁnes a topology on X.
• Let X ={a,b}. A topology T must contain ∅ and X. It may or may not contain
{a} or{b}. If they are both in T , this means that the two points are distinct and
separate. If neither of them are in T , then the points are as close together as they could
be (topologically indistinguishable). Finally, one could even declare {a} to be open and
not{b}.
• Let X ={a,b,c}. We begin to see the conditions that the axioms place on valid topolo-
gies. For example, if {a} and{b} are open then {a,b} must be open. The possible
2Munkres, sections 12-13.
3P(X) is the power setP(X) ={A⊂X}.
9

topologies range from T ={∅,X} (the coarsest topology) to T =P(X) (the ﬁnest
topology).
Deﬁnition. The discrete topology on a set X is given by T =P(X).
In the discrete topology, every subset is both open and closed.
Deﬁnition. We say a topology T′ is ﬁner thanT if it contains more open sets than T , namely
T ⊂T′. We say T′ is coarser thenT ifT′⊂T .
We use the terms ﬁne and coarse because a ﬁner topology distinguishes more between points. A
ﬁner topology also places more conditions on convergence. For example, a sequence in a topological
space equipped with the discrete topology T =P(X) converges if and only if it becomes constant
at some point.
Note that two topologies need not be comparable. Sometimes neither one is a subset of the other.
We can also consider more interesting examples.
The Coﬁnite Topology
• Let X be an inﬁnite set and take
T ={S⊂X :X\S is ﬁnite or S = ∅}
This is the ﬁnite complement topology , also called the coﬁnite topology. Although
it seems contrived, when this topology is placed on a ﬁeld it has a special place in alge-
braic geometry.
T is a topology. It contains ∅,X by deﬁnition (in particular, it contains ∅ because
of the additional condition we included). If S =⋃
iUi forUi∈S , eitherS = ∅ orUi⊂S
where Ui has ﬁnite complement. Then
X\S⊂X\Ui
So X\S is ﬁnite, and S∈T . If we let U1,...,U n be open, then
X\ (
n⋂
i=1
Ui) =
n⋃
i=1
X\Ui
which is the ﬁnite union of ﬁnitely many points, and hence ﬁnite. Thus ⋂n
i=1∈T . So
this is indeed a topology.
Counterexample
• Let X be an inﬁnite set and take
T ={S⊂X :S ﬁnite or S =X}
T is not a topology, even though ∅,X ∈T . Any inﬁnite proper subset Y ⊊ X can be
10

written as the union
Y =
⋃
y∈Y
{y}
Each{y} is inT , but their union Y is not contained inT .
In these simple examples, we can aﬀord to keep track of the open sets of a topology. But this is in
general too much information for a space. For example, we don’t keep in mind all of the open sets
in Rn we working with its topology. In practice, it suﬃces to only consider a smaller subset of the
open sets called a basis, which generates the topology. 4
Deﬁnition. A basis is a collection of subsets B⊂P (X) such that
1. B coversX, namely ⋃
B∈BB =X.
2. If B1,B 2∈B and x∈B1∩B2, then there exists B3∈B such that x∈B3⊂B1∩B2
A basis is not usually a topology, but we can generate a topology from a basis.
Deﬁnition. The topologyT generated by a basis B is deﬁned as follows. U∈T if and only if for
all x∈U, there exists B∈B such that x∈B⊂U.
This is analogous to a deﬁnition of what it means for a set to be open in a metric space. We can
now interpret the second condition in the deﬁnition of a basis as saying that the intersection of two
basis elements is open.
Proposition. The topology generated by a basis B is indeed a topology.
Proof. ∅∈T vacuously. Similarly,X∈T because of condition 1 above.
Let Ui∈T . If x∈ ⋃
iUi, then there exists i such that x∈ Ui. Since Ui is open, there exists
a basis element B∈B with
x∈B⊂Ui⊂
⋃
i
Ui
4Despite the name, a topological basis is not very similar to the basis of a vector space. For example, the entire
topology is a basis for itself. There is no notion of independence.
11

Therefore arbitrary unions of open sets are open.
We will show ﬁnite intersections of open sets is open by showing U1∩U2 is open (as we can
get to ﬁnite intersections by successively taking intersections of two open sets). Let x∈ U1∩U2.
Since both of these sets are open, there exist B1,B 2∈B with x∈B1⊂U1 and x∈B2⊂U2. By
condition 2, there exists a basis element B3∈B withx∈B3⊂B1∩B2⊂U1∩U2. Therefore ﬁnite
intersections of open sets is open, and T is indeed a topology.
Example
• LetB ={Br(x) :x∈ Rn,r> 0}. ThenB is a basis for the usual metric topology on Rn.
B clearly covers all of Rn and satisﬁes condition 2 in the deﬁnition above.
However, we can deﬁne another basis for Rn as well given by the sets of open rectangles
(a1,b 1)× (a2,b 2)×... × (an,bn) ={(x1,x 2,...,x n) :ai<x i<b i for all i}
It is easy to check that this is indeed a basis.
Furthermore, this basis also generates the standard metric topology on Rn, illustrat-
ing the important idea that there are many bases that generate a single topology. We
will prove using tools developed below. In short, the idea will be that open rectangles
are open in the metric ball sense. Similarly, open balls are open in the open-rectangle
sense.
Right now, we don’t have a very concrete description of the topology generated by a basis B. The
following proposition gives a more explicit way to understand open sets.
Proposition. LetB be a basis. The topology T generated byB is given by
T =
{⋃
i
Ui :Ui∈B
}
In words, the open sets of T are all unions of sets in B.
Proof. If U∈T , for all x∈U there exists Bx∈B such that x∈B⊂U. Then
⋃
B∈B
B⊂U
B =U
We have⋃
B⊂U⊂U by deﬁnition. For any point x∈U, the set Bx containsx and is contained in
U. Hence U⊂⋃
B⊂UB, so we have equality.
Remark.T is the smallest collection of subsets of X that containsB and is a topology.
It is in this sense that a basis generates a topology. However, it is important to note that a basis,
as well as the way to write an open set as the union of basis elements, is far from unique.
12

Examples
• There is a basis for the usual topology on R given by all open intervals of the form (a,b ),
where a<b and a,b∈ R. Then the proposition says that every open subset of R is the
union of intervals. This union may not even be ﬁnite. For example, the set R\ Z is open,
as it is the union
R\ Z =
⋃
n∈Z
(n,n + 1)
• Consider the complement of the Cantor set, given by
X ={x∈ (0, 1) : at least one 1 appears in the base 3 expansion of x}
There is no linear ordering of the countably many open intervals that appear in the union
for X.
• There is no open set in R that requires uncountably many disjoint open intervals to write
as a union. This is because every open interval contains a rational (in fact inﬁnitely may
rationals), and if there were uncountably many disjoint open intervals, there would be
uncountably many rationals.
• The lower limit topology on R is the topologyT𝓁 generated by the basis
B ={[a,b ) :a<b and a,b∈ R}
These sets cover R and satisfy the intersection condition (in fact the nonempty intersec-
tion of two such half-open intervals is again a half-open interval). So B is a basis.
T𝓁 is distinct from the usual topology T on R, as [ a,b ) ∈ T𝓁 but [a,b ) /∈ T. How-
ever, (a,b )∈T 𝓁. This is because for all x∈ (a,b ), we have x∈ [x,b )⊂ (a,b ). Therefore
T ⊊T𝓁, namelyT𝓁 is ﬁner thanT (orT is coarser thanT𝓁).
Lemma. LetB,B′ be bases for topologies T,T′, respectively. Then T′ is ﬁner than T (meaning
T ⊂T′) if and only if B⊂T ′. Equivalently, T ⊂T′ if and only if for all B∈B and x∈B, there
exists B′∈B′ such that x∈B′⊂B.
This provides a way to compare topologies. Namely, to show one topology is ﬁner than another we
must ﬁnd such basis elements.
13

The French train distance
• The French train distance on R2 is the metric
d(p,q ) =
{
d(p,q ) p and q lie on the same line through the origin
d(p, 0) +d(0,q ) otherwise
This is indeed a metric. What are the open balls in this metric? They are the radial lines
union an open ball around the origin, when r is large enough.
These balls are not open in the usual topology, as the radial portion of these balls lack thickness
in one direction. However, every ball in the usual topology on R2 is open in the French train
metric. So TT (the train metric) is ﬁner than T (the usual topology).
14

9/11/2019 - Subspaces, Products, Continuity
Recall that we were discussing bases for topological spaces. A basis is a smaller collection of open
sets that generates a topology. Then in the topology generated by a basis B, a set U⊂X is open
if for every point x∈ U there exists an element B∈B such that x∈ B⊂ U. In a metric space,
the open balls are a basis for the metric space topology.
We also saw there is a more concrete description of the topology generated by a basis:
T ={unions of elements ofB}
In other words,T is the coarsest topology which contains B.
We will continue today with some examples. 5 The ﬁrst two will be very useful techniques by
which we can build topologies on sets.
Let X be a topological space and A⊂ X any subset. Recall that, if X is a metric space, then A
inherits the metric space topology via the induced metric obtained from restricting the metric on
X. Namely, the open balls in A are of the form
BA
r (p) =BX
r (p)∩A ={x∈A :d(x,p )<r}
Then we ﬁnd that open subsets of A are precisely the open sets of X intersectA. This is because
for an open U⊂A we have
U =
⋃
p∈U
BA
rp(p) =
⋃
p∈U
BX
rp(p)∩A =
(⋃
p∈U
BX
r (p)
)
∩A
where rp> 0 is chosen such that BA
rp(p)⊂U. This motivates the following deﬁnition.
Deﬁnition. LetX be a topological space andA⊂X be a subset. The subspace topology on A is
TA ={U∩A :u∈T x}
Lemma.TA is indeed a topology on A. Furthermore, if B is a basis for TX then{B∩A :B∈B}
is a basis for TA.
Proof. Clearly ∅,A∈T A, as ∅,X ∈T X. We also have
⋃
i
(Ui∩A) =
(⋃
i
Ui
)
∩A
n⋂
i=1
(Ui∩A) =
( n⋂
i=1
Ui
)
∩A
5Munkres, sections 14-16.
15

soTA is closed under arbitrary unions and ﬁnite intersections, as T is.
Also, using the above characterization of a basis, for an open set U⊂X we can write
U∩A =
(⋃
i
Ui
)
∩A =
⋃
i
Ui∩A
So any open set in TA can be expressed as the union of elements of {B∩A : B ∈B} , which
completes the proof.
Remark. The closed sets in the subset topology on A⊂X are of the form Y∩A, where Y ⊂X
is closed.
This is an easy set-theoretic veriﬁcation.
Examples
• The subspace topology on R⊂ R2 is the usual topology on the real line.
• Consider the subspace topology on [0, 1]⊂ R. The open intervals that are proper subsets
of [0, 1] are open as usual. But the half-interval [0 , 1/2) is also open in [0, 1] as it can be
obtained via the intersection [0, 1]∩ (−1/2, 1/2).
• With the subspace topology on Q⊂ R some sets now can be both open and closed. For
example, (
√
2,
√
3)∩ Q is open, but it is also closed, as (
√
2,
√
3)∩ Q = [
√
2,
√
3]∩ Q.
The product topology
We will begin by discussing topologies on ﬁnite products. For inﬁnite products, however, the
obvious generalization breaks down. We will see this a bit later.
Deﬁnition. Given topologiesT onX andT′ onY , the product topologyonX×Y is the topology
generated by the basis B ={U×V :U∈T ,V ∈T ′}.
Note that the set B is itself not a topology, as the union of two rectangles U1×V1 and U2×V2 is
not necessarily another rectangle.
Lemma. This setB ={U×V :U∈T ,V ∈T ′} is indeed a basis.
16

Proof. The sets of the form U×V cover, as the whole space X×Y is the product of X∈T and
Y ∈T ′. If U1×V1,U 2×V2∈B , then
(U1×V1)∩ (U2×V2) = (U1∩U2)× (V1∩V2)
Thus their intersection it itself an open rectangle, as U1∩U2∈T and V1∩V2∈T ′. Therefore B
is indeed a basis.
Intuitively, the idea is that a point is close to ( x,y ) if it is both close to x and close to y.
There is in fact a better basis that generates the product topology.
Proposition. IfB,B′ are bases for T,T′, respectively, then the product topology is generated by
the basis
D ={B×B′ :B∈B,B′∈B′}
Proof. This is because everything inD is indeed open, as these are products of open sets. Further-
more, every open set of Z⊂X×Y can be written
Z =
⋃
i
Ui×Vi =
⋃
i
(⋃
j
Bj
)
×
(⋃
k
B′
k
)
=
⋃
i
⋃
j
⋃
k
Bj×B′
k
Example
• We have that the product topology on R× R is the usual topology on R2.
By the previous proposition a basis for R× R is given by
{(a1,b 1)× (a2,b 2) :a1<b 1,a 2<b 2}
These are also open in the standard topology on R2, because for any point ( x,y ) ∈
(a1,b 1)× (a2,b 2), the ball of radius min{|x−a1|,|x−a2|,|x−b1|,|x−b2|} is contained
in (a1,b 1)× (a2,b 2).
Conversely, given an open ball B in R2 and x∈ B we can choose a small enough open
rectangle R = (a1,b 1)× (a2,b 2) with x∈R⊂B.
One can also show this easily using the metric
d∞((x,y ), (x′,y′)) = max{|x−x′|,|y−y′|}
The ball of radius r centered at p in this metric is the cube of side length 2 r centered at
p, namely the product (x−r,x +r)× (y−r,y +r), which is already a basis element of
the product topology. Thus the topology induced by d∞, which is the standard topology
on R2, is the product topology.
17

Deﬁnition. Let X be a set with a total order. 6 The order topology on X is generated by the
basis that contains the elements
• (a,b ) ={x∈X :a<x<b }
• If X has a smallest element a0, then also the element [a0,b ) ={x∈X :a≤x<b }
• If X has a largest element b0, then also the element (a,b 0] ={x∈X :a<x ≤b}
Examples
• On R with the usual order, the order topology is the usual topology on R.
• On subsets of R with the usual order, the order topology is the subspace topology.
• We can consider stranger examples as well. During this example, we will denote the point
(a,b )∈ [0, 1]× [0, 1] bya×b to eliminate confusion. Consider the lexigraphic/dictionary
order deﬁned on [0, 1]× [0, 1]. This is deﬁned by
a×b<a ′×b′ ⇐⇒ a<a ′ or (a =a′ and b<b ′)
Then the open sets are of the form
The open sets in the order topology are not open in the standard topology (obtained via
the subspace topology inherited from R2), since there are no open neighborhoods of the
edge points contained in (a,b )⊂ [0, 1]× [0, 1].
Open sets in the standard topology are not necessarily open in the order topology either.
An open ball in the interior of [0 , 1]× [0, 1] is open in the order topology, as it is the
union of vertical line segments. But if we examine the point 1 /2× 0 in the open set
[0, 1]× [0, 1/2), it does not sit in any basis element of the order topology (open interval)
that is contained in [0, 1]× [0, 1/2). This is because any open interval containing 1 /2× 0
must have starting point a with a <1/2. Then the interval contains all points on the
vertical line with ﬁrst coordinate x for any a < x <1/2, and these points are not all
contained in [0, 1]× [0, 1/2).
6A total order is a relation < on X×X such that
1. Either a<b , b<a , or a =b (precisely one of these must hold).
2. If a<b and b<c , then a<c , namely < is transitive.
18

The above example illustrates a situation in which two topologies, namely the usual topology and
dictionary order topology on [0, 1]× [0, 1] are not comparable.
Continuity
Deﬁnition. Let X,Y be topological spaces. A function f :X→Y is continuous if for all open
U⊂Y , the preimage f−1(U)⊂X is open.
Remark. For metric spaces, this deﬁnition agrees with the delta-epsilon formulation of continuity.
Note that the continuity of a function depends entirely on the topology of the spaces involved.
Examples
• Deﬁne the function f : R→ R by
f(x) =
{
1 x≥ 0
−1 x< 0
Consider an open set around f(0) = 1. The inverse image of the open set (1 /2, 1/3)⊂ R
is [0,∞)⊂ R, which is not open in the usual topology. Thus f is not continuous.
• Equip R with the lower limit topology and denote this space by R𝓁. Recall that the lower
limit topology is ﬁner than the usual topology. Then the function f : R𝓁→ R𝓁 deﬁned
as above is in fact continuous. This is because the set f−1((1/2, 3/2) = [0,∞)⊂ R𝓁 is
now open. In fact, for every open U⊂ R𝓁 the set f−1(U) is open. There aren’t many
choices, so we can explicitly compute
f−1(U) =



∅ {−1, 1}∩ U = ∅
[0,∞) 1 ∈U and − 1⁄∈u
(−∞, 0) −1∈U and 1⁄∈U
R −1, 1∈U
All of these are open in the lower limit topology, which proves that f : R𝓁 → R𝓁 is
continuous.a
• The identity function f : R→ R𝓁, deﬁned by f(x) = x, is not continuous. This is
because the preimage of [0, 1)⊂ R𝓁 is [0, 1)⊂ R, which is not open. The identity function
f : R𝓁→ R is continuous, as any open set U⊂ R is open in R𝓁. This demonstrates that
we can gauge the ﬁneness of a topology relative to another topology on the same set by
the continuity of the identity map.
• LetX,Y be topological spaces. The projection π1 :X×Y →X deﬁned byπ(x,y ) =x is
continuous. This is because any open set U⊂X has preimage π−1
1 (U) = U×Y , which
is open on the product space.
aIn fact, the topology on the codomain here is irrelevant. As long as the domain is R𝓁, this f will be
continuous.
19

Next class we will speak further about continuity and show that it suﬃces to check continuity on
a basis. We will also deﬁne the notion of a homeomorphism, which captures when two spaces are
topologically the same.
20

9/16/2019 - Continuity, Homeomorphisms, Limit Points
Today we will continue discussing continuity and then begin speaking about limit points.
Continuity
Recall the following deﬁnition.
Deﬁnition. A function f :X→Y is continuous if for all open U⊂Y , f−1(U)⊂X is open.
It in fact suﬃces to check continuity on a basis. This provides a criterion that is often more
convenient that looking at all open sets.
Proposition. A function f :X→Y is continuous if and only if for all basis elements B⊂Y for
the topology on Y , f−1(B)⊂X is open.
Proof. This condition is certainly necessary, as every basis element for the topology on Y is open
in Y . It is also suﬃcient, as an open set U⊂Y can be written U =⋃
iBi, in which case we have
that
f−1(U) =f−1
(⋃
i
Bi
)
=
⋃
i
f−1(Bi)⊂X
is open.
Example
• If X is a topological space and Y is a metric space, then it suﬃces to check that
f−1(Bϵ(y))⊂X is open for all y∈Y and ϵ> 0. If we expand this to the case when X
is also a metric space, we will ﬁnd that this deﬁnition is a bit stronger than the usual
deﬁnition of continuity for metric spaces (as we demand that every point in Bϵ(y) has a
neighborhood around its preimage contained in the preimage of Bϵ(y), rather than just
considering the center y. Ultimately, however, these deﬁnitions are equivalent).
Since topological spaces can be quite pathological, it is worthwhile to conﬁrm some basic, desirable
properties of continuity.
Proposition. We have the following:
1. A constant function f : X → Y given by f(x) = y0 for all x∈ X and some y0 ∈ Y is
continuous.
2. Let A⊂ X be a subspace with the subspace topology. Then the inclusion i : A ↪→ X is
continuous.7
3. If f : X → Y and g : Y → Z are continuous, then the composition g◦f : X → Z is
continuous.
7We can describe the subspace topology as the coarsest topology for A such that this inclusion map is continuous.
21

Note that we are not considering the sum or products of continuous functions for two reasons.
The ﬁrst is that these topological spaces may not have any addition or multiplication operations.
The second is that, even if we are working with a space like R, there are topologies for which the
algebraic operations are not continuous. 8
Proof. Constant functions are continuous, since open sets U⊂ Y either contain y0 or do not. If
y0∈U, then the preimage of U is all of X, which is open. Otherwise, the preimage of U is empty,
which is also open. Note that these are the only functions between two spaces that are always
guaranteed to be continuous regardless of the topologies on X and Y .
Let U⊂.
Let U ⊂ Z be open. Then g−1(U) is open by continuity of g. And f−1(g−1(U)) is open by
continuity off. Thus (g◦f)−1(U) =f−1(g−1(U)) is open.
It will be useful in algebraic topology to be able to say something about the continuity of a function
given information about its behavior on certain pieces of a space.
Proposition. Let X =⋃
iUi with Ui⊂ X open, and let f : X→ Y be a function such that the
restrictionf|Ui :Ui→Y is continuous9 for all i, then f is continuous.
One can also recast this proposition to say that a function f : X→ Y is continuous if, for every
point in X, there is an open set of X on which f is continuous.
Also note that the converse of this proposition holds, since if f is continuous then the restric-
tion f|Ui :Ui→Y is given as the composition of the inclusion i :Ui→X and f, which are both
continuous.
Proof. For allV ⊂Y open, (f|Ui)−1(V ) =f−1(V )∩Ui, which is open in Ui by assumption. Hence
(f|Ui)−1(V ) =Ui∩ (open set in X)
is open in X. In general, an open subset of an open subspace of X is also open in X. Thus
f−1(V ) =f−1(V )∩
(⋃
i
Ui
)
=
⋃
i
f−1(V )∩Ui =
⋃
i
f|−1
Ui (V )
and the sets f|−1
Ui (V ) are open.
Homeomorphism
What makes two topological spaces the same? We usually don’t want to demand that two topo-
logical spaces are the same only if their underlying sets and topologies are precisely equal. Every
branch of math has a notion of sameness 10, and in topology this notion is homeomorphism.
8Topological spaces with a continuous operation deﬁned on them are called topological groups.
9Where Ui is of course given the subspace topology.
10For example, two vector spaces are the same if they are isomorphic.
22

Deﬁnition. A homeomorphism is a bijection f :X→Y such that f :X→Y andf−1 :Y →X
are both continuous.
Intuitively, the continuity of both f and f−1 means we have bijections
X Y
f
f−1
So a set U⊂ X is open if and only if f(U)⊂ Y is open. In other words, points in X are close
together if and only if their images are close together in Y .
Deﬁnition. SpacesX and Y are homeomorphic if there exists a homeomorphism f :X→Y .
Remark. A continuous bijection need not be a homeomorphism.
Nonexamples
• The identity id: R𝓁→ R is a continuous bijection, but it is not a homeomorphism. It is
continuous because R𝓁 is ﬁner than the standard topology R. But [a,b )⊂ R𝓁 is open in
R𝓁 but not in R.
• Let X ={0}∪{ 1/n : n∈ N} as a subspace of R and consider N with the discrete
topology (which is also the subspace topology inherited from R). Consider the bijection
f : N→X deﬁned by f(0) = 0 and f(n) = 1/n. f is continuous, as any function from a
space with the discrete topology is continuous. a The inverse bijection is not continuous.
{0} is open, but the image f({0}) ={0}⊂ X is not open. This is because any open ball
around 0 in R contains some 1/n.
aThis is because any subset of N is open, so the preimage of every subset of the codomain is open.
Recall the following deﬁnition.
Deﬁnition. A metric space X is bounded if sup{d(x,y ) :x,y∈X} is ﬁnite.
In turns out that this is not a topological property.
Boundedness is not topological
• Consider the function f : (−π/2,π/ 2)→ R deﬁned by f(x) = tan x. f is a contin-
uous bijection from ( −π/2,π/ 2) to R with a continuous inverse arctan. Thus f is a
homeomorphism from (−π/2,π/ 2) to R.
So two topological spaces can be homeomorphic despite the fact that one is bounded and the other
is not. Intuitively, topologies do not detect how far points are from each other, but rather only if
points are close to each other.
Homeomorphism is what makes the sameness of topological spaces precise. There is a related
notion that describes when one space looks like a subspace of another.
23

Deﬁnition. An embedding is a continuous injective map f :Y →X such that the induced map
f :Y →f(Y )⊂X is a homeomorphism, where f(Y )⊂Y is equipped with the subspace topology.
Note that in this class, we are not considering the smoothness of an embedding. 11
Closed sets and limit points 12
Recall that a subset A⊂X is closed if its complement X\A is open. Subsets can be both open
and closed. They can also be neither open nor closed. We can approximate subsets with open and
closed sets.
Deﬁnition. LetA⊂X be any subset. The closure of A, denoted by A, is the smallest closed set
containingA. It is given by
A =
⋂
Y⊃A closed
Y
Note that if A is already closed, then A = A. If A = A then A is closed. We will see that A is
obtained from A by adding points.
Deﬁnition. A subset A⊂X is dense if A =X.
Deﬁnition. Let A⊂X be any subset. The interior of A, denoted by int (A), is the largest open
closed containing A. It is given by
int(A) =
⋃
U⊂A open
U
The interior of A consists of all the interior points of A, which are points in A that have an open
neighborhood contained in A.
Note that if A is already open, then int(A) =A. If int(A) =A then A is open.
Deﬁnition. LetA⊂X be any subset. The boundary ofA, denoted by ∂A = bd(A), is A\ int(A).
Example
• Let X = [0, 1). Then X = [0, 1]. [0 , 1] is closed and contains [0 , 1), and certainly
[0, 1)⊂X, so we only have to prove that 1∈X. Suppose for contradiction 1 ⁄∈X. Then
X = [0, 1), which is not closed.
We have int(X) = (0, 1) for similar reasons, and then ∂X ={0, 1}.
It will be very useful to remember that if A⊂F and F is closed, then A⊂F . Similarly, if U⊂A
and U is open, then U⊂ int(A). We also have
(X\A) =X− int(A)
11In diﬀerential geometry/topology, the cuspidal cubic cannot be obtained as an embedding of the line R, as there
is a lack of smoothness at the origin.
24

Example
• Q⊂ R is dense, namely Q = R. Suppose the open set R\ Q is nonempty with x∈ R\ Q.
Then there is some ϵ >0 such that (x−ϵ,x +ϵ)⊂ R\ Q. But every open interval of
reals contains a rational number.
By the same argument and the density of the irrationals, int( Q) = ∅.
Thus∂(Q) = R.
We will next introduce limit points, which are an important way of describing closedness.
Deﬁnition. A neighborhood of a point x∈X is an open set U⊂X with x∈U.
Deﬁnition. A point x∈X is a limit point of a subset A⊂X if for every neighborhood U⊂X
of x there exists a point a∈A with a⁄=x and a∈U.
Note that the condition that a⁄= x means that an isolated point of A is not a limit point. Intu-
itively, limit points of A are points for which there exist points of A arbitrarily close to x.
It is an immediate consequence of the deﬁnition that all interior points and boundary points are
limit points of A.
Examples
• 1 is a limit point of the subset (0, 1) or of [0, 1]. There are points arbitrarily close to 1 in
these sets that are not equal to 1 itself.
• 1 is not a limit point of the set {0}∪{ 1/n : n∈ N}, as small neighborhoods of 1 will
contain only the element 1 from this set. However, 0 is indeed a limit point of this set.
This allows us to formulate the following characterization of the closure.
Theorem. We have
A =A∪{ limit points of A}
Proof. Suppose x /∈ A and x is not a limit point of A. Then there exists an open neighborhood
U⊂ X of x which doesn’t contain anything from A. Thus X\U is a closed set that contains A
and A⊂X\U⊂X\{x}. So x⁄∈A.
Suppose x⁄∈ A. Then x∈ X\A, which is an open set. Let U ⊂ X\A be an open neigh-
borhood of x. U is disjoint from A, so x is not in A and is not a limit point of A either.
Deﬁnition. x∈A if and only if, for every neighborhood U⊂X of x we have A∩U⁄= ∅.
This follows easily from the above theorem. Next time we will discuss the limit of a sequence and
its relation to limit points.
25

9/18/2019 - Sequences, Limits, Products
Today we will begin by discussing sequences and limits. 13 Recall that we had the following deﬁni-
tion:
Deﬁnition. A point x∈ X is a limit point of A⊂ X if for all open neighborhoods U of x, we
have U∩ (A\{x})⁄= ∅.
We also proved the following theorem:
Theorem. We have
A =
⋂
F⊃A
F closed
=A∪{ limit points of A}
Corollary. x∈A if and only if for every neighborhood U of x, we have U∩A⁄= ∅.
Deﬁnition. A sequence x1,x 2,... in a topological space X converges to a limit x if for all neigh-
borhoodsU of x, there exists N∈ N such that n≥N implies xn∈U.
The limit of a sequence is not necessarily unique. We will see later what conditions need to be
placed on X in order to guarantee that limits are unique.
Deﬁnition. A basis of neighborhoods for x is a family of neighborhoods B ={Bi} of x such
that if U is a neighborhood of X, there exists some i with Bi⊂U.
We can sharpen the criterion for convergenging to a limit.
Remark. A sequence converges to a limit x if there exists such an N∈ N for every element in a
basis of neighborhoods for x.
Example
• In a metric space, the family {Bϵ(x) :ϵ> 0} forms a basis of neighborhoods for x.
The family{B1/n(x) :n∈ N} also forms a basis of neighborhoods for x.
We can now see how the usual notion of convergence in a metric space is a special case of convergence
in general topological spaces.
Convergence in metric spaces
• In a metric space, a sequence x1,x 2,... converges to a limit x if and only if for all r> 0,
there exists N such that n≥N implies xn∈Br(x).
13Munkres, section 17
26

Lemma. If there exists a sequence x1,x 2,... in A that converges to x such that xn⁄=x for all n,
then x is a limit point of A.
Conversely, in a metric space, if x is a limit point of A, then for all n≥ 1, then there exists
a sequence x1,x 2,... that converges to x with xn⁄=x.
To prove the converse in a metric space, we take xn∈B1/n(x)∩ (A\{x}), which is nonempty by
assumption.
In general, the disjointness assumption is to guarantee that x1,x 2,... is not the constant sequence
(without this assumption isolated points of A would be declared limit points).
The converse also holds more generally in spaces whose points have countable bases of neigh-
borhoods (these are called ﬁrst-countable spaces14). So to ﬁnd a counterexample to the converse
in general, it will be necessary to ﬁnd a case in which there is a point with no countable basis of
neighborhoods.
A limit point without a converging sequence
• Consider the set R with the topology
T ={∅}∪{ U : R\U is countable}
T is modeled after the ﬁnite-complement topology, and it is indeed a topology for similar
reasons.
Let A = (0, 1). We will show A is dense. This is because if F is a closed set that
contains A, it must be countable. But there are no countable sets that contain A, so
F = R. Thus any real number is a limit point of A.
However, no sequence in A converges to 2. Given any sequence x1,x 2,... in A, the
set U = R\{x1,x 2,... } is an open set containing 2 that contains none of the points
of the sequence. In fact, this same argument demonstrates that any sequence does not
converge to any number. Thus the only sequences that converge are the sequences that
eventually stabilize.
This is an example of a topology which has many limit points and for which it is very
diﬃcult for sequences to converge.
Intuitively, the notion of sequences indexed by the integers is suitable for capturing the idea of
limit points in spaces that admit a countable description. To describe larger spaces like the above
example using sequences would require a generalization of sequences indexed by (uncountable) sets.
14A space is ﬁrst-countable if for all x, there exit neighborhoods U1,U 2,... such that for any neighborhood V of
x, there is some n with x∈Un⊂V . This is a way of making precise the complexity of a topology, and there is an
entire classiﬁcation system which extends this project.
27

Uniqueness of limits
In a metric space, the limit of a sequence, if it exists, is necessarily unique. This is not true in a
general topological space.
Limits are not unique
• Consider the set R with the ﬁnite complement topology
T ={∅}∪{ U : R\U is ﬁnite}
Let a1,a 2,... be a sequence in X with all ai distinct.a The claim is that this sequence
converges to any element of R.
Let x ∈ R, and consider a neighborhood U. Then U contains all but ﬁnitely many
of the ai points, so there exists N large enough so that n≥N implies an∈U.
aWe actually only require that a point is hit by the sequence ﬁnitely many times.
At this point, the right thing to do is to introduce a notion that forces topological spaces to be
better behaved.
Separation axioms
Deﬁnition. A topological space is Hausdorﬀ, also called separable, if for distinct points x1,x 2∈
X there exist neighborhoods U1 of x1 and U2 of x2 such that U1∩U2 = ∅.
Examples
• Metric spaces are Hausdorﬀ. For points x,x 2∈ X, let 0 < ϵ < d(x1,x 2)/2 and deﬁne
U1 =Bϵ(x1) and U2 =Bϵ(x2). Then U1∩U2 = ∅.
• The ﬁnite complement topology on R is not Hausdorﬀ. This is because any two nonempty
open sets must intersect, as they both have ﬁnite complements.
• The discrete topology on any set is Hausdorﬀ.
The following theorem motivates this deﬁnition.
28

Theorem. If X is Hausdorﬀ, then every sequence converges to at most one limit.
Proof. Assume there is a sequence x1,x 2,... that converges to x in X. Let y⁄= x. We will show
that this sequence does not converge to y. Since X is Hausdorﬀ, there exist open neighborhoods U
ofx andV ofy such thatU∩V = ∅. By deﬁnition of convergence, there exists N such thatn≥N
implies xn∈ U. Thus V contains only ﬁnitely many points, so the sequence cannot converge to
y.
The Hausdorﬀ condition is one of many separation axioms, which are conditions that describe
how well a topological space distinguishes between points. Most of the time in this course will
be concerned with Hausdorﬀ spaces, although non-Hausdorﬀ topologies play an important role in
many parts of math. 15 We have the following separation axioms:
1. A space X is T0 if, for distinct x,y ∈X, there exists an open neighborhood of one that
does not contain the other. This means that the open sets are enough to determine the
points of X.
2. A space X isT1 if, for distinct x,y∈X, there exists an open neighborhood of x not con-
tainingy and an open neighborhood of y not containing x. Equivalently, every singleton
{x} is closed.
3. A space X is T2 if it is Hausdorﬀ, namely for distinct points x,y ∈ X, there exists an
open neighborhood U of x and V of y such that U∩V = ∅.
4. A space X isT3, also called regular, if it is T1 and given a pointx∈X and closedA⊂X
that are disjoint, there exist neighborhoods U of x and V of A with U∩V = ∅.a
5. A space X isT4, also called normal, if for A,B⊂X disjoint closed sets there exist open
neighborhoods U of A and V of B with U∩V = ∅.
aBeing Hausdorﬀ is a weaker version of this condition when A is taken to be the singleton. Munkres, section
31 contains examples of spaces that are T2 but not T3.
We see that R with the ﬁnite complement topology is T1 (as singletons are closed) but not T2. And
R𝓁 (R with the lower limit topology) is normal, while R𝓁× R𝓁 is regular but not normal.
These axioms are important, for it is useful to know when a topological space arises from a met-
ric space. A topological space that comes from a metric space is called metrizable. One way
to approach this question is to determine where metric spaces lie in the hierarchy of separation
axioms.
Theorem. Every metric space is normal.
The proof is not diﬃcult but also not presently relevant to the course.
Conversely, we have the following theorem.
15For example, in algebraic geometry the Zariski topology is a useful topology deﬁned on space (or on the prime
ideals of a commutative ring) that is not Hausdorﬀ.
29

Theorem (Urysohn Metrization theorem). Every regular space with a countable 16 basis is metriz-
able.
Product topologies 17
We will see that when considering an inﬁnite collection {Xi :i∈I} of spaces, the question of the
appropriate topology on their product
∏
i∈I
Xi ={(xi)i∈I :xi∈X,i∈I}
=
{
functions f :I→
⋃
Xi with f(i)∈Xi for all i∈I
}
becomes more complex. A ﬁrst attempt might be the following:
Theorem. The box topology on a product ∏
i∈IXi is generated by the basis
B =
{∏
i∈I
Ui :Ui⊂Xi is open
}
B is indeed a basis, as the intersection of two elements (open boxes) of B is another element ofB.
(∏
i∈I
Ui
)
∩
(∏
i∈I
Vi
)
=
∏
i∈I
Ui∩Vi
However, this will ultimately turn out to be an inappropriate topology for the general product
space.
Example
• Consider the product
RN = Rω = R0× R1× R2×...
Consider the diagonal map
∆ : R→ Rω
x↦→ (x,x,x,... )
In the ﬁnite case R2, the map ∆ is the inclusion of R into the diagonal of the plane R2.
However, the diagonal map is not continuous in the box topology. For consider the
open set
U = (−1, 1)× (−1/2, 1/2)× (−1/3, 1/3)×...
U is open in the box topology, as it is in fact a basis element. However, the preimage of
U under d is precisely{0}, as we require
∆−1(U) = (−1, 1)∩ (−1/2, 1/2)∩ (−1/3, 1/3)∩...
16There are stronger versions of the theorem that drop this countability condition, as sometimes it is useful to
deﬁne metrics on large function spaces. However, this is at the cost of introducing much complexity.
30

This is a good indication that the box topology is not the right one to take on the inﬁnite product.
We thus introduce the following topology.
Deﬁnition. The product topology on a product ∏
i∈XXi is generated by the basis
B =
{∏
i∈I
Ui :Ui⊂Xi is open and Ui =Xi for all but ﬁnitely many i
}
When I is ﬁnite, the box topology and the product topology are equal. When I is inﬁnite, the
product topology is strictly coarser than the box topology. With the product topology, we obtain
the following important result:
Theorem. A map f :Z→∏
i∈IXi, where ∏
i∈IXi has the product topology, is continuous if and
only if the component fi :Z→Xi is continuous for all i.
This justiﬁes the choice of the product topology as the desired choice for an inﬁnite product. We
will prove one direction today.
Proof. Assume f : Z→∏
i∈IXi is continuous. The component maps are fi = pi◦f, where pi is
the projection to the ith factor. Each pi is continuous, as the preimage of U⊂Xi is
p−1
i (U) ={(xj)j∈I :xi∈U} =
∏
j∈I
Uj where Uj =
{
Xj j⁄=i
U j =i
The composition of continuous functions is continuous, so fi is continuous.
This argument did not require the product topology and would have worked equally well with the
box topology. We will require the ﬁniteness condition for the converse, which we will prove next
time.
31

9/23/2019 - More Product Topologies, Connectedness
We’ve been discussing lots of terminology and notation so far, and this will continue for a few more
lectures. However, over the coming weeks, with connectedness and compactness, the material will
involve more content.
Recall that we introduced two possible topologies on inﬁnite product spaces.
X =
∏
i∈I
Xi ={(xi)i∈I :xi∈Xi} ={functions f :I→
⋃
i∈I
Xi with f(i)∈Xi}
I can be any set (whether or not it is uncountable is irrelevant, and the theory becomes interesting
only when I is inﬁnite of any cardinality). We deﬁned the box topology as the topology generated
by the basis
BBox =
{∏
i∈I
Ui :Ui⊂Xi open
}
The problem is that the box topology is too ﬁne. So we instead introduced the product topology,
which is generated by the basis
BProd =
{∏
i∈I
Ui :Ui =Xi for all but ﬁnitely many i
}
The following characterization of continuity for maps into product spaces conﬁrmed that the prod-
uct topology is the right one to take on the product.
Theorem. A function f : Z→ X = ∏
i∈IXi is continuous if and only if its components fi =
πi◦f :Z→Zi, where πi :X→Xi is the usual projection, are continuous.
For example, we considered the diagonal map
∆ : R→ Rω = RN
x↦→ (x,x,... )
and saw that it is not continuous over the box topology, while by the theorem ∆ is continuous when
considered as a map into the product topology. Last time we proved one direction of the theorem,
but we will review the result here.
Proof. Each projection π :X→Xi is continuous regardless of the topology on X, as for an open
set U⊂Xi we have
π−1
i (U) ={(xj)j∈I :xi∈U} =
∏
j∈I
Uj
whereUj =U ifj =i andUj =Xj otherwise. This is indeed open, so fi =πi◦f is the composition
of continuous functions and hence continuous.
Conversely, suppose all fi component maps are continuous. We want to show f is continuous,
32

and it suﬃces to show that the inverse image of any basis element is open. Let ∏
i∈IUi⊂X be a
basis element. Recall Ui =Xi for all but ﬁnitely many i. We have
f−1
(∏
i∈I
Ui
)
={z∈Z :fi(z)∈Ui} =
⋂
i∈I
f−1
i (Ui)
Each f−1
i (Ui) is open in Z by the continuity of fi. Furthermore, f−1
i (Ui) = Z whenever Ui =Xi,
which happens for all but ﬁnitely many i. We thus have
f−1
(∏
i∈I
Ui
)
=
n⋂
j=1
f−1
ij (Uij)
which is the ﬁnite intersecrtion of open sets. Therefore f is continuous.
The box and product topologies are likely the only natural/reasonable topologies to place on an
arbitrary product of topological spaces. If our spaces are metric spaces, however, we can use their
metrics to deﬁne another natural topology.
Motivating example
• We deﬁned a metric on Rn by
d∞(x,y ) = sup
i∈{1,...,n}
|yi−xi|
Recall that d∞ deﬁnes the same topology on Rn as the product topology.
The above example does not work immediately for inﬁnite products, as the supremum of the indi-
vidual distances may not exist (if the distances become arbitrarily large, for example).
One solution would be to restrict to sequences in the product with bounded distances, but this is
not ideal, as we would like to consider the entire product space. Recalling that the only thing that
matters in a topology is the relative distance between points, another solution is to replace every
metric with a bounded metric that induces the same topology.
Let (xi,di), for i∈I, be a collection of metric spaces. For each i, deﬁne a new metric
di(x,y ) = min{d(x,y ), 1}
This is still a metric. The only property to check is the triangle inequality, but this is not too
diﬃcult.
Lemma. di induces the same topology on Xi as di.
Proof. A basis for the topology induced by di consists of balls of radius less than 1 in the di metric
as well as all of Xi. The key observation is that it doesn’t hurt us to throw away the larger balls
in the di metric.
If U is open in the di metric, for each x∈ U there exists a radius r ball around x. If r≥ 1,
then we can just take a ball in the di metric of radius less than 1. Therefore U is open in the di
metric as well. The other direction is similar.
33

Deﬁnition. Let (Xi,di) be a collection of metric spaces. The uniform topology on the product∏
i∈IXi is the topology induced by the uniform metric, deﬁned by
d∞(x,y ) = sup
i∈I
di(xi,yi)
Example
• The uniform topology on RI ={functions I→ R} is deﬁned by
d∞(f,g ) = min
{
sup
i∈I
|f(i)−g(i)|, 1
}
Then a sequence of functions fn converge to f if and only if d∞(fn,f ) converges to 0.
This is the deﬁnition of uniform convergence.
To understand the topology that the uniform metric deﬁnes, we must ﬁrst understand the open
balls. If I is ﬁnite, then the open balls of radius r≤ 1 for d∞ are products of balls of radius r.
Bd∞
r (x) =
∏
i∈I
Bdi
r (xi)
This is simply because the supremum of the individual distances is less than r if and only if all of
the individual distances are less than r.
This situation becomes a bit more complex with an inﬁnite product. For example, the set
U = (−1, 1)× (−1, 1)×... ⊂ Rω
is not the unit ball around in the origin with the uniform metric. The unit ball is indeed in U, but
the point (0, 1/2, 2/3, 3/4,... ) is contained in U but not the unit ball, as
d∞(0, 1/2, 2/3, 3/4,... ) = sup{0, 1/2, 2/3, 3/4,... } = 1
which is not strictly less than 1.
In fact, U is not even open. For any ϵ-ball around the above point contains points outside of
U (we can choose some coordinate suﬃciently close to 1 such that adding ϵ moves outside of U).
Despite this setback, we can indeed formulate a description of open balls. If r≤ 1, then for r′<r
deﬁne
Ur′(x) =
∏
i∈I
Bdi
r′ (x)
Ur′ is contained in Bd∞
r (x). The idea is that we bound each element of the tuple by some safety
margin from 1. In other words, if every coordinate is less than 1 −ϵ, then their supremum will be
no more than 1−ϵ< 1.
Conversely, if d∞(x,y ) < r, then there exists r′ < r such that d∞(x,y ) < r′ < r. Therefore
di(x,y )<r′ for all i, and thus y∈Ur′(x). This proves that x∈Bd∞
r if and only if x∈Ur′(x) for
some r′<r . Thus
Bd∞
r (x) =
⋃
r′<r
Ur′(x)
34

In other words, we need that all components of a point are less than r−ϵ for some ϵ > 0, not
merely that they are all less than just r. We can now state the following theorem.
Theorem. The uniform topology on a product of metric spaces is ﬁner than the product topology
and coarser than the box topology.
Remark. For a ﬁnite product, Tprod⊂T unif ⊂T box. It’s obvious that Tprod =Tbox in this case,
which implies that the three topologies are in fact equal.
Proof. First we show that the uniform topology is ﬁner than the product topology. Let ∏
i∈IUi
be a basis element of the product topology. Let x = (xi)i∈I∈∏
i∈IUi. Since xi∈Ui, there exists
ri∈ (0, 1] such that Bdi
ri (xi)⊂Ui.
The ri may all be diﬀerent, so we take the smallest of all radii. Only ﬁnitely many ri are strictly
less than 1 (explicitly, when Ui =Xi takeri = 1). If we take
r = inf{ri :i∈I}
then r> 0 and
Bd∞
r ⊂Ur(x) =
∏
i∈I
Bdi
r (xi)⊂
∏
i∈I
Bdi
ri (xi)⊂
∏
i∈I
Ui
Therefore every open set in the product topology is open in the uniform topology.
Next we show that every ball in the metric d∞ is open in the box topology. Balls with radius
r≥ 1 are all of X and hence open in the box topology. If r< 1 then
Bd∞
r (x) =
⋃
r′<r
Ur′(x)
where
Ur′(x) =
∏
i∈I
Bdi
ri (xi)
This expresses Bd∞
r as the union of open sets in the box topology, so it is also open in the box
topology.
We could also ask whether or not the box and product topologies come from a metric when they
are endowed on a product of metric spaces. In general, the box topology does not arise from a
metric, while one can deﬁne a metric that induces the product topology on a set. We will not delve
much further into this matter.
Connectness
We will introduce the notion of connectedness today and continue with it next lecture.18 Intuitively,
the idea of connectedness should be quite clear: a space is connected if it does not consist of two
disjoint components. The trick will be to make this precise.
18Munkres, sections 23 and 24.
35

Deﬁnition. A space X is connected if it cannot be written X =U∪V , where U,V are disjoint,
nonempty, open subsets. Such a decomposition is a separation of X.
Note that if X =U∪V is a separation, then U =X\V and V =X\U are both closed as well.
We can then equivalently characterize connectedness as follows.
Deﬁnition. A space X is connected if A⊂X is open and closed implies A = ∅ or A =X.
When writing proofs, it is a useful strategy that if one can express a connected space X =U∪V
with U,V disjoint and open, then one of these sets is empty and the other is the whole space.
Examples
• The subspace [0, 1]⊂ R is connected. It’s not completely obvious why, however, as on
the other hand the subset [0, 1]∩ Q is not connected (one can cut the interval in half at
any irrational number).
Suppose for contradiction we have a separation [0 , 1] = U∪V . We can assume 0 ∈ U.
Since U is open, in fact [0,ϵ )⊂U for some ϵ> 0. Deﬁne
a = sup{x> 0 : [0,x )⊂U}
We have seen a >0, as a≥ϵ. The ﬁrst claim is that a /∈V . Indeed, if a∈V and V is
open, there exists ϵ> 0 such that (a−ϵ,a ]⊂V . But then [0,x )⁄⊂U wheneverx>a −ϵ,
which contradicts the fact that a is the supremum of all such x.
Thus a∈ U. The second claim is that a⁄< 1. Indeed, if a < 1 since U is open there
exists ϵ> 0 such that (a−ϵ,a +ϵ)⊂U. Thus [0,a +ϵ)⊂U, which contradicts the fact
that a is the supremum of all such x. Thus a = 1, which implies [0, 1)⊂U and 1∈U.
Therefore V = ∅, so [0, 1] is connected.
• The subspace [0, 1)∪ (1, 2]⊂ R is not connected. In general, if A⊂ R where x<y <z
with x,z ∈ A and y⁄∈ A, then A is not connected. So connected subsets of R must be
‘interval-like.’
The above proof that [0, 1] is connected seems more complex than it should be, but the underlying
idea behind it is quite simple. We show that given a single point in U, it must follow that all points
are in U from the properties of the set in question (here, we use that nonempty bounded subsets
of R have a least upper bound).
36

9/25/2019 - Connectedness, Path Connectedness
We will return to the topic of connectness, which intuitively captures the idea when a space consists
of a single piece. Recall the following deﬁnition.
Deﬁnition. A topological spaceX is connected if it doesn’t have a separation X =U∪V , where
U,V are nonempty, disjoint, open subsets.
Equivalently,X is connected if its only subsets that are both open and closed are ∅ and X. To
prove that a space is not connected, it suﬃces to ﬁnd a separation. It can be trickier to prove that
a space is connected, but the typical strategy is to show why one of the subsets must in fact be the
entire space. We will see examples of this today. 19
We also saw last time that connected subsets of R cannot have gaps (missing points).
Examples
• R𝓁, which is R with the lower limit topology, a is not connected. For example, ( −∞, 0)
and [0,∞) are both open, disjoint, and cover R𝓁.
In fact, any subset of R𝓁 with more than one point is disconnected by this same ar-
gument. Such a topological space is called totally disconnected.
• R with the ﬁnite complement topology is connected. If we write R =U∪V with both U
andV open, necessarily U∩V ⁄= ∅ (as each of them does not contain only ﬁnitely many
points).
Note that this example has a diﬀerent ﬂavor. Usually it is diﬃcult to ﬁnd open sets
that exactly tile a space, but here it is impossible to ﬁnd nonempty open sets that are
even disjoint.
aIntuitively, one should imagine R𝓁 as the real line with a gap to the left of each point (as there are open
neighborhoods which do not contain any points less than a particular point) but with points to the right of that
point.
The idea of connectedness will be important later, when we study algebraic topology. Generaliza-
tions of connectedness are an important tool that topologists use to distinguish between spaces.
Let A,B ⊂ X be connected. It is not necessarily true that A∩B is connected. It is easy to
ﬁnd a counterexample in R2.
The union of connected spaces is also not necessarily connected. However, we can come up with a
condition to guarantee that the union of such spaces is in fact connected.
Proposition. LetA,B⊂X be connected and suppose A∩B⁄= ∅. Then A∪B is connected.
We can generalize this to inﬁnite unions.
19Recall the proof from last time that [0 , 1] is connected (which proceeded in this manner).
37

Theorem. LetAi⊂X be a collection of connected subsets indexed by I that all contain a point p.
Then Y =⋃
i∈IAi is connected.
Proof. Let Y = U∪V , with U,V open sets. Either U or V contains p, so assume p∈ U. Write
Ai = (U∩Ai)∪ (V∩Ai). Necessarily U∩Ai is not empty, so by connectedness of Ai we have
Ai = U∩Ai and Ai⊂ U (and Ai∩V = ∅). This holds for all i so ⋃
i∈IAi⊂ U and Y = U,
Y∩V = ∅. Therefore Y is connected.
Corollary. R is connected. [a,b ], [a,b ), (a,b )⊂ R are connected.
Proof. Write
R =
⋃
n∈N
[−n,n ]
Each [−n,n ] is connected by the argument from last time (as it is homeomorphic to [0 , 1]). Thus
R is connected. A similar argument shows these other intervals are also connected.
Note that we used the fact that if X is homeomorphic to Y and X is connected, then Y is also
connected. For we can take the image of any separation of one of the sets under the homeomorphism
to obtain a separation of the other set. In general, we can examine the behavior of connectedness
under continuous functions.
Theorem. Let f : X → Y be a continuous function. If X is connected, then f(X) ⊂ Y is
connected.
Proof. Note that what is outside the image of f is irrelevant, so we can assume f is surjective (as
the corestriction f :X→f(X), where f(X)⊂Y is given the subspace topology, is continuous).
Iff(X) =U∪V withU,V open, disjoint, and nonempty, then we can writeX =f−1(U)∪f−1(V ).
These two sets are open, as f is continuous. They are disjoint, as a single point cannot map to
both U and V (which are disjoint). They are nonempty, as we assumed f is surjective. Thus a
separation of f(X) implies there exists a separation of X. So if X is connected, then f(X) is
connected as well.
The key idea of the proof is that the inverse image of a separation along a surjective continuous
map is a separation of the domain. This observation implies the intermediate value theorem.
Theorem. Let X be a connected topological space and f : X → R a continuous function. Let
a,b∈X and r∈ R be such that f(a)<r<f (b). Then there exists c∈X such that f(c) =r.
Proof. Suppose for contradictionf(c)⁄=r for allc∈X. Then f(X)∩(−∞,r ) andf(X)∩(r,∞) is a
separation of f(X). But X is connected, so f(X) is connected, which is a contradiction. Therefore
there exists some c∈X with f(c) =r.
38

It turns out that if we have any path in X between two points, then along the path f obtains all
intermediate values.
We will continue by exploring how to build connected spaces from other connected spaces.
Theorem. If X and Y is connected, then X×Y is connected.
Proof. Let X×Y =U∪V , where U,V are open and disjoint. Let ( a,b )∈U. We will show that
U contains everything.
First, note that if we move along the slice X×{b}⊂ X×Y , this space is connected. This is
because the subspace topology on X×{b}⊂ X×Y is the same as the topology on X (these spaces
are homeomorphic). We have
X×{b} = ((X×{b})∩U)∪ ((X×{b})∩V )
where these sets are open and disjoint. Since ( a,b )∈ (X×{b})∩U, we have that X×{b}⊂ U.
The same argument implies that{a}×Y is inU. In fact, since {x}×{b} is inU, any slice{x}×Y
is in U by the same argument. This holds for all x∈X, so X×Y ⊂U.20
Corollary. If X1,...,X n are connected, then their product X1×... ×Xn is connected.
It is true, but not obvious, that the inﬁnite product of connected spaces is connected.
Theorem. Let (Xi)i∈I be a collection of connected spaces, then their product ∏
i∈IXi (equipped
with the product topology) is connected.
We will see in a moment that this is not true in the box topology or the uniform topology. We
won’t use this result, so the proof is left as an exercise.
Nonconnectedness of the inﬁnite product
• Consider the product space
Rω ={(a1,a 2,... ) :ai∈ R}
with the box topology. Let U be the set of bounded sequences, such that for ( ai)i∈ U
there exists M with|ai|<M for all i. Let V be the set of unbounded sequences.
Clearly U and V are nonempty, disjoint, and cover Rω. Then the only claim is that
U and V are open in the box and uniform topologies. Since the box topology is ﬁner
than the uniform topology, it in fact suﬃces to check the uniform topology. But for the
sake of completeness we will present both veriﬁcations.
20Munkres supplies another proof. He argues to take the union of ( X×{b}∪{ x}× Y ) for all x. All of these are
connected, as they are individually the union of two slices (which are connected) that intersect at (a,b ). Furthermore,
they all contain (a,b ), and hence their union is connected.
39

Given a sequence (ai)i∈ Rω, the basis element
Ba =
∏
i
(ai− 1,ai + 1)
contains (ai)i. If ( ai)i∈ U and M is a bound for ( ai)i, then M + 1 is a bound for any
sequence inBa. Thus (ai)i∈Ba⊂U. If (ai)i is unbounded, then every sequence is Ba is
also unbounded (as modifying the sequence coordinatewise by at most 1 does not aﬀect
boundedness). Therefore U and V are both open.
For the uniform topology, simply observe that the ball Ba contains the open ball in
the uniform topology of radius 1 centered at ( ai)i (since the open balls of the uniform
topology are a bit smaller than those of the box topology).
Path connectedness
Path connectedness is another way of precisely formulating the intuition that a space is made of
one piece. We require the following deﬁnition.
Deﬁnition. If x,y ∈X, a path in X is a continuous map f : [0, 1]→X such that f(0) = x and
f(1) =y.
The only requirement on a path is that it be continuous (they do not need to be injective). Later
in the course we will consider spaces of paths as an invariant for distinguishing topological spaces.
Deﬁnition. A space X is path-connectedif any two points x,y∈X can be joined by a path.
Remark. The relation∼ deﬁned by x∼y if and only if there exists a path from x to y in X is an
equivalence relation.21 The equivalence classes of this relation are called the path components of
X.
It is now natural to ask about the relationship between connectedness and path-connectedness.
Theorem. If X is path connected, then X is connected.
Proof. Suppose X is path connected. Write X =U∪V , with U,V open and disjoint, with at least
U nonempty. Let x∈U. For any y∈X, there exists a path f : [0, 1]→X fromx toy. Since [0, 1]
is connected, f([0, 1]) is connected. Writing
f([0, 1]) = (f([0, 1])∩U)∪ (f([0, 1])∩V )
implies f([0, 1])⊂U, and in particular y∈U for all y∈X.
21A relation that is reﬂexive, symmetric, and transitive. Such relations provide a notion of equality on a collection.
The constant path demonstrates∼ is reﬂexive. To show∼ is symmetric, run a path from x toy backwards to obtain
a path from y to x. Given paths from x to y and y to z, concatenate them to obtain a path from x to z.
40

However, the converse is false. The famous counterexample is the topologist’s sine curve, which is
the subset of R2 deﬁned by
S ={(x,y ) :y = sin(1/x),x> 0}| {z }
S0
∪{(0, 0)}
S0 is connected, as it is the image of (0 ,∞) under a continuous function. We must conﬁrm that
adding (0, 0) doesn’t disconnect the space S.
Note that (0, 0) is a limit point of S, as the sequence {(1/(nπ), 0) : n∈ N} converges to (0, 0).
Now write S =U∪V , with U,V open, nonempty, and disjoint. S0 is either entirely in U or V by
connectedness. Suppose S0⊂U. But since U is closed, it contains its limit points. In particular,
it contains (0, 0), so S =U and V = ∅.
However, S is not path connected. The idea of the proof is as follows. Suppose for contradic-
tion there exists a path f : [0, 1]→ S with f(0) = (0 , 0) and f(1, sin 1). Composing with the
projection to the x-axis yields a continuous function πx◦f. The intermediate value theorem im-
plies that πx◦f passes through all points of the form pn = 1/(2nπ +π/2). There exist tn∈ [0, 1]
such that f(tn) =pn for all n. Then the pn converge to 0, while for all tn we have that f(tn) = 1.
However, the situation is not entirely hopeless. For well-behaved subsets of Rn, these notions
coincide.
Theorem. If A⊂ Rn is open, then A is path-connected if and only if A is connected.
41

9/30/2019 - Compactness
Today we will begin discussing what is perhaps one of the least intuitive notions in point set
topology. Recall from real analysis that the closed interval [a,b ]⊂ R is compact. In fact, any closed
and bounded set in Rn is compact. These sets enjoy nice properties, such as the fact that any
continuous function f : K→ R from compact K achieves its maximum and minimum. But in a
general topological space, there is no notion of boundedness without a metric, so another deﬁnition
will be necessary. Intuitively, compactness will be a generalization of a ‘ﬁniteness’ for a space.
Deﬁnition. Let X be a topological space. A collection of open sets {Ui}i∈I is an open cover if
X =⋃
i∈IUi.
Note that the index set I can be anything, even uncountable.
Deﬁnition. X is compact if every open cover contains a ﬁnite subcollection that also covers X.
Such a ﬁnite subcollection is a ﬁnite subcover.
This can be a tricky deﬁnition. In order to show a space is compact, it is necessary to prove that
every open cover has a ﬁnite subcover. Whereas to show a space is not compact, it is only necessary
to exhibit a single open cover without a ﬁnite subcover.
Examples
• R is not compact, as the cover
R =
⋃
n∈Z
(n,n + 2)
contains no ﬁnite subcover. Every open set is necessary, as removing any of them exludes
the integer n + 1.
This is a good sign, as it indicates that the general deﬁnition of compactness we have
given agrees with the usual one from analysis.
• The half-open interval (0, 1] is not compact, The cover
(0, 1] =
⋃
n∈N
(1/n, 1]
has no ﬁnite subcover.
• Let X ={0}∪{ 1/n :n∈ N}. X is compact. This is because some element of any open
cover must contain 0, and thus contains all but ﬁnitely many of the points{1/n :n∈ N}.
For each of the excluded points, take an open set that contains it. Then combining these
we obtain a ﬁnite subcollection that covers X, so X is compact.
Theorem. If A is compact and f :A→X is continuous, then f(A) is compact.
Note that if we take X = R, then this recovers the result that continuous functions from compact
spaces to R obtain their global extrema.
42

Proof. Let{Ui}i∈I be an open cover off(A). The preimages{f−1(Ui)}i∈I form an open cover ofA.
By compactness of A, there is a ﬁnite subcover f−1(U1),...,f −1(Un) ofA, where we are relabeling
indices for the purposes of notation. Then U1,...,U n cover f(A), since their preimages cover A.
Therefore f(A) is compact.
The following is an important example that will allow us to greatly expand the theory of compact
spaces.
Proof. Let{Ui}i∈I be an open cover of [0, 1]. Let
A ={x∈ [0, 1] : there exists a ﬁnite subcover of [0 ,x ]}
A is nonempty, as it contains 0. We will showA is both open and closed. Then by the connectedness
of [0, 1], this will prove A = [0, 1].
• Suppose x∈A, namely [0,x ] admits a ﬁnite subcover. Then x∈Ui for some i in this ﬁnite
subcover. Ui is open, so there exists ϵ so that Bϵ(x)⊂Ui. Then (x−ϵ,x +ϵ)⊂A as well, as
the same ﬁnite subcollection is a ﬁnite subcover for any [0,y ] withy∈ (x−ϵ,x +ϵ). Therefore
A is open.
• To show A is closed, let x be a limit point of A. Then x∈ Ui for some i in the cover, so
x∈Bϵ(x)⊂Ui for suﬃciently small ϵ> 0. There exists a point y∈A with|x−y|<ϵ , as x
is a limit point. Then the ﬁnite subcover of [0,y ] along with the setUi yields a ﬁnite subcover
for [0,x ], so x∈A and A contains its limit points.
Therefore A = [0, 1], which completes the proof.
In the usual topology on Rn, compact sets are closed and bounded. Although there is no notion
of boundedness in a general topological space, we can still ask how compactness is related to
closedness.
Theorem. If X is compact, then any closed subspace A⊂X is compact.
Proof. LetA be an open cover of A by sets open in X. Then A∪{ X\A} is an open cover of X,
which by compactness of X admits a ﬁnite subcover. This yields a ﬁnite subcover of A.
So in a compact space, closed subsets are also compact. What about the converse? In Rn, the
answer is yes, but this fails more generally.
Compact does not imply closed
• Let X⊂ R, where R is given the coﬁnite topology. X is always compact, as any open
set contains all but ﬁnitely many points. So once we have one open set in a cover, it
suﬃces to ﬁnd ﬁnitely many remaining sets that cover the points missing from the ﬁrst set.
43

However,X may not be closed. For example, any inﬁnite set is not closed in the coﬁnite
topology, although they are all compact.
However, we can salvage this by imposing conditions that ensure our topological spaces are not too
pathological.
Theorem. LetX be Hausdorﬀ. If K⊂X is compact, then K is closed.
Proof. We will show that X\K is open. Let x∈ X\K. For every y∈ K there exists disjoint
neighborhoods y∈Uy and x∈Vy by Hausdorﬀness. Then the collection {Uy}y∈K is a cover of K.
By compactness, there exists a ﬁnite subcoverUy1,...,U yn. The ﬁnite intersectionV =Vy1∩...∩Vyn
is open and does not meet anyUyi, and henceV∩K = ∅. V is an open neighborhood of x∈X\K,
so X\K is open.
Theorem. Let X,Y be compact and Hausdorﬀ. Then a continuous bijection f : X → Y is a
homeomorphism.
Proof. It suﬃces to show that f is closed, namely the images of closed sets are closed. Let A⊂X
be closed. A is compact, so f(A)⊂ Y is compact. But Y is Hausdorﬀ, so this implies f(A) is
closed, as desired.
Remark. The above theorem only requires that X is compact and Y is Hausdorﬀ. However, the
conclusion then immediately implies that X and Y are both compact and Hausdorﬀ.
Example
• The compactness assumption is really necessary. Consider the bijection
f : [0, 1)→S1
x↦→e2πix = (cos(2πx), sin(2πx))
f is a continuous bijection, but not a homeomorphism. One way to see this is that S1 is
compact while [0, 1) is not. Alternatively, removing most points from [0 , 1) disconnects
the space, while removing any point from S1 does not.
Next lecture we will prove the following important result.
Theorem. LetX and Y be compact. Then X×Y is compact.22
22This holds for inﬁnitely, and even uncountably, many compact spaces. This is Tychonoﬀ’s theorem, and it is
equivalent to the axiom of choice.
44

10/2/2019 - Compactness, Uncountability, Metric Spaces
We will begin by proving the following theorem introduced last lecture.
Theorem. LetX and Y be compact. Then X×Y is compact.
By induction we have the following corollary.
Corollary. LetX1,...,X n be compact. Then X1×...X n is compact.
Proof. LetA be an open cover of X×Y . We want to ﬁnd a ﬁnite subcover of A. A basis element
of X×Y is of the form U×V , where U⊂X and V ⊂Y is open. Thus each element of A is the
union of such subsets U×V .
The strategy will be to deﬁne a new cover that consists of only basis elements and demonstrate
that these have a ﬁnite subcover. Then by replacing each basis element U×V with the open set of
A in which it is contained, we obtain a ﬁnite subcover of A. This reduces the problem to ﬁnding a
subcover of a cover that consists of only basis elements, so we can assume that all sets in A are of
the form Ui×Vi, with Ui⊂X and Vi⊂Y open.
Consider a point x∈ X. {x}× Y is homeomorphic to Y and hence compact. Then it has a
ﬁnite subcover of the form ⋃n
i=1Ui×Vi and x∈ Ui for all i. If we take the ﬁnite intersection
W =⋂n
i=1Ui, then W is an open neighborhood of x in X. Also, ⋃n
i=1Ui×Vi is a ﬁnite cover of
W×Y .
For every x, similarly deﬁne an open set Wx to obtain a strip Wx×Y and a ﬁnite subcover of
this strip. The sets Wx for all x cover X, so by compactness of X there is a ﬁnite subcover
Wx1,...,W xm. Finitely many sets from A cover each Wxi×Y , so collecting these all together
yields a ﬁnite subcover of A for all of X×Y .
Recall that we proved compact Hausdorﬀ spaces have some nice properties. Namely, if X is
Hausdorﬀ and A⊂ X is compact, then A is closed. Also, if f : X→ Y is a continuous bijection
between compact, Hausdorﬀ spaces X and Y then f is a homeomorphism. We have the following
neat application of these ideas.
45

Uncountability of R
We ﬁrst introduce the following deﬁnition.
Deﬁnition. LetX be a topological space. An isolated point of X is a point x∈X such that
the singleton{x} is open.
Theorem. If X is a nonempty, compact Hausdorﬀ space with no isolated points, then X is
uncountable.a
We ﬁrst need the following lemma.
Lemma. If U⊂ X is open and x∈ X, there exists a nonempty open set V with x⁄∈ V and
V ⊂U.
Proof. Choose y∈U such that x⁄=y. This is possible because U is a neighborhood of x and
x is not an isolated point. By Hausdorﬀness, there are disjoint neighborhoods Wx ofx andWy
of y. Take V = Wy∩U, which is nonempty as it contains y. Then Wx is open and disjoint
from V , so V ⊂X\Wx and x⁄∈V .
We now prove the theorem.
Proof. Let f : N→ X be any function. We will show that f is not a surjection. This will
imply that X is not countable. b We will deﬁne a sequence of sets by induction. By the claim,
set U = X and ﬁnd V1⊂ X such that f(1)⁄∈ V1. For n >1, apply the claim to the point
f(n) andU =Vn−1. Then V1⊃V2⊃... is a sequence of nonempty, closed sets withf(n)⁄∈Vn.
We claim ⋃
i(X\Vi) ⁄= X. Suppose for contradiction that we have equality. Then since
X is compact, there is a ﬁnite subcover X\Vi1,...,X \Vin. But any point in Vj withj larger
than i1,...,i n is not covered by these sets, so this is not actually a cover. Thus ⋂
iVi⁄= ∅.
If we take x∈⋂
iVi, then by deﬁnition x⁄=f(n) for any n, and f is not surjective.
Corollary. Every closed interval of R is uncountable.
aThis is a special case of general result in topology and functional analysis called the Baire category theorem.
Challenge: look up the Baire category theorem on Wikipedia and show that our result follows as a corollary.
bA countable set is one that admits a surjection from N by deﬁnition.
Compactness in metric spaces
Recall that A⊂ Rn is compact if A is closed in bounded. 23 This agrees with the topological
deﬁnition.
Theorem. A⊂ Rn is compact if and only if A is closed and bounded in the Euclidean metric.
23This is the Heine-Borel characterization of compactness in Rn.
46

Proof. Suppose A⊂ Rn is compact. Then A is closed, since Rn is Hausdorﬀ. Cover A with the
open balls {Br(0) : r∈ N}. Then by compactness, there is a ﬁnite subcover Br1(0),...,B rm(0).
Then there is some r with A⊂Br(0), so A is bounded.
Suppose A⊂ Rn is closed and bounded. Since A is bounded, it is contained in some suitably
large rectangle [−r,r ]n. This closed rectange is the product of intervals and thus compact. A is a
closed subspace of a compact space, so A is compact.
Remark. The theorem depends on the Euclidean metric in an important way. We can deﬁne other
metrics on Rn that induce the standard topology, but for which this theorem is not true.
For example, the uniform metric on Rn induces the same topology as the Euclidean metric, but all
of Rn is bounded in this metric (while Rn is not compact).
We can use compactness to generalize two of the most important theorems in calculus to com-
pact spaces.
Theorem (Extreme value theorem) . If X is compact and f : X→ R is a continuous function,
then f achieves its maximum. Namely, there exists c∈X such that f(x)≤f(c) for all x∈X.
Proof. f(X)⊂ R is compact, so it is bounded and closed (and hence contains its limit points). If
m = sup(X) is in f(X), then we are done. Otherwise, ( m−ϵ,m )∩f(X)⁄= ∅ for all ϵ >0 by
deﬁnition of the supremum, so m is a limit point of f(X) and therefore m∈f(X).
For the next theorem, 24 we introduce a few deﬁnitions.
Deﬁnition. If (X,d ) is a metric space and A⊂X is nonempty, the distance fromx∈X to A is
deﬁned to be d(x,A ) = inf{d(x,y ) :y∈A}.
If A is compact, then there exists a point y∈ A with d(x,y ) = d(x,A ). This is because d(x,·) :
A→ R is a continuous function from a compact set A and achieves its minimum at some point
y∈A.
Deﬁnition. If A is bounded, the diameter of A is deﬁned to be sup{d(x,y ) :x,y∈A}.
Intuitively, the diameter ofA is the largest distance between two points inA. If A is compact, then
there exist points x,y∈A with d(x,y ) equal to the diameter of A. This is because d :A×A→ R
is a continuous function 25 from the compact set A×A to R and achieves its maximum at some
pair (x,y )∈A×A.
The following useful lemma will be essential for the proof.
24Recall that the uniform continuity theorem says that iff : [a,b ]→ R is continuous, thenf is uniformly continuous.
This means that for any ϵ> 0, there exists δ >0 such that|x−y|<δ implies|f(x)−f(y)|<ϵ . In other words, δ
does not depend on the point x.
25Veriﬁcation: d :A×A→ R is a continuous function.
47

Lemma. LetA be an open cover of a metric space (X,d ). If X is compact, then there exists some
δ >0 such that all subsets of X of diameter less than δ are contained in an element of A. δ is the
Lebesgue number ofA.
Proof. Choose a ﬁnite subcover {A1,...,A n}⊂A . Deﬁne the function
f :X→ R
x↦→ 1
n
n∑
i=1
d(x,X\Ai)
If x⁄∈Ai, then d(x,X\Ai) = 0. Intuitively summand measures how far the exterior of Ai is from
the point x.
f is the sum of continuous functions and is hence continuous. Since each Ai is open, if x∈Ai there
is some ϵ> 0 with x∈Bϵ(x)⊂Ai. Then in such a case, d(x,X\Ai)>ϵ . Any x∈X is contained
in some Ai, so f(x)> 0 for all x∈X.
X is compact, so f achieves its minimum δ > 0 with f(x)≥ δ for all x∈ X. Then for any
x, there exists some Ai such that d(x,X \Ai)≥ δ by deﬁnition of f (as f is the average of all
d(x,X\Ai)). This δ is the Lebesgue number of A.
We now conﬁrm the result. Suppose B has diameter less than δ. If x0∈B then
x0∈B⊂Bδ(x0)⊂Ai
We now deﬁne uniform continuity.
Deﬁnition. Let (X,dX) and (Y,dY ) be metric spaces. A function f : X → Y is uniformly
continuous if for all ϵ> 0, there exists δ >0 such that dX(x,y )<δ implies dY (f(x),f (y))<ϵ .
We will prove the following theorem next lecture.
Theorem (Uniform continuity theorem). If X and Y are metric spaces and X is compact, then
any continuous function f :X→Y is uniformly continuous.
48

10/7/2019 - Compactness, Limit Points, Sequences
Recall that a space X is compact if every open coverX =⋃
i∈IUi has a ﬁnite subcover. In Rn with
the usual distance, a subset is comapct if and only if it is closed and bounded.
Another useful result is that if f : X → Y is continuous at X is compact, then f(X)⊂ Y is
compact. This implies the extreme value theorem for continuous functions f : X→ R, with X
compact.
Recall the following useful lemma from last lecture.
Lemma. Let (X,d ) be a compact metric space andA an open cover of X. There exists δ >0 such
that any subset of diameter less than δ is entirely contained in one set of A.
The Lebesgue number lemma is false in noncompact spaces.
Failure of the Lebesgue lemma for noncompact spaces
• For example, we can cover the noncompact space R by
⋃
n∈Z
(
n− (1 + 1/n),n + (1 + 1/n)
)
Then for any δ, we can ﬁnd a set of radius less than δ containing some integer that does
not lie in a single
• This fails even when we have a ﬁnite cover of a noncompact space. For example, R2 is
covered by the two sets
A1 ={(x,y ) :xy <1}∪{ (x,y ) :x≤ 0 or y≤ 0}
A2 ={(x,y ) :y >0}
We can ﬁnd arbitrarily small balls near thex-axis far away that do not sit entirely in one
of the two open sets.
Uniform continuity expresses the idea that the neighborhoods of points in the preimages of open
sets are ‘uniformly sized.’ To compare the sizes of neighborhoods, we require a metric on the space.
Deﬁnition. A function of metric spaces f : (X,dX)→ (Y,dY ) is uniformly continuous if for all
ϵ> 0, there exists δ >0 such that for x0,x 1∈X we have d(x0,x 1)<δ impliesd(f(x0),f (x1))<ϵ .
Theorem. LetX,Y be metric spaces and f :X→Y a continuous function. If X is compact, then
f is uniformly continuous.
We will prove this easily with the Lebesgue number lemma, but there are more complicated proofs
that rely directly on the ﬁniteness condition from the deﬁnition of compactness.
49

Proof. Given ϵ >0, consider the cover of Y given by taking all balls of radius ϵ/2. The idea will
be that if we gaurantee f(x0) and f(x1) are in the same ball, then the distance between them is
less than ϵ by the triangle inequality.
Take the open cover
X =
⋃
y∈Y
f−1(
Bϵ/2(y)
)
By the Lebesgue number lemma, there exists some δ >0 such that if dX(x0,x 1)< δimplies that
x0,x 1∈ f−1(
Bϵ/2(y)
)
for some y∈ Y . Therefore f(x0),f (x1)∈ Bϵ/2(y) and dY (f(x0),f (x1)) <
ϵ.
Limit point and sequential compactness
There are two other deﬁnitions of compactness. In a metric space, these notions coincide, but
they diﬀer in a general topological space. The reason for this is that sequences do not capture the
topological information of a general space very well.
Deﬁnition. A space X is limit point compact if every inﬁnite subset of X has a limit point.
[Examples]
• (0, 1]⊂ R is not limit point compact, as the inﬁnite collection {1/n :n∈ N} has no limit
point in (0, 1].
• R is not limit point compact, as Z⊂ R is an inﬁnite subset with no limit point.
• {1/n : n∈ N}∪{ 0} is limit point compact. Any inﬁnite subset has 0 as a limit point
necessarily.
So far limit point compactness seems to agree with the usual deﬁnition.
Theorem. LetX be compact. Then X is limit point compact.
Proof. We will show the contrapositive. Suppose X is not limit point compact, and let A⊂X be
an inﬁnite subset with no limit point. For each a∈A, a is not a limit point of A, and thus there
exists a neighborhood Ua of a such that Ua∩A ={a}.
We have constructed a cover of A, so it remains to cover the rest of X. A has no limit points, so
it is closed. Thus X\A is open, which yields an open cover
X = (X\A)∪
⋃
a∈A
Ua
This is an open cover with no ﬁnite subcover, as a∈Ua and no other sets in this cover. Therefore
X is not compact.
50

The easiest counterexamples to the converse are non-Hausdorﬀ, but it is possible to deﬁne a Haus-
dorﬀ counterexample as well (although it may be a bit more complicated).
Failure of the converse
• Consider Z with the topology generated by the sets of the form {−n,n} for all n∈ Z
along with{0}. Z is not Hausdorﬀ, as it is not possible to separate the points −n andn.
Given an inﬁnite subset S ⊂ Z, let n ∈ S\{ 0}. The claim is that −n is a limit
point, as every neighborhood of −n containsn, an element of S distinct from−n.
There is another notion of compactness as well.
Deﬁnition. X is sequentially compact if every sequence of points in X has a convergent sub-
sequence.
Example
• In R, every bounded sequence in [−R,R ] has a convergent subsequence.
For example, 1, 0, 1, 0,... has a convergent subsequence 1, 1,... .
• The sequence 1, 2, 3,... in R has no convergent subsequence, even though the sequence
1, 1/2, 2, 1/3, 3,... has a convergent subsequence 1, 1/2, 1/3,... .
It is natural to ask how sequential compactness relates to limit point compactness and usual com-
pactness. In spaces with a countable basis of neighborhoods (for example metric spaces), the notion
of a limit of a sequence is closely related to that of the limit point of a set. In such a case, sequen-
tially compactness is equivalent to limit point compactness.
In general, however, sequentially compactness only implies limit point compactness. This should
be understood as a failure for sequences to detect the topology of a space rather than a reﬂection of
the strength of these competing notions. 26 We will prove the following important characterization
of these notions.
Theorem. If (X,d ) is a metric space, then compactness, limit point compactness, and sequential
compactness are equivalent.
Proof. We showed compactness implies limit point compactness already. LetX be limit point com-
pact, and let x1,x 2,... be a sequence in X. If this sequence consists of only ﬁnitely many distinct
terms, then there exists some a =xi that reappears inﬁnitely many times in the sequence. Namely,
xn =a for inﬁnitely many n. These indices form a convergent subsequence.
Otherwise, the inﬁnite set {x1,x 2,... } has a limit point a∈ X by assumption. Let n1 be such
26There is a generalization of a sequence called a net that is designed to capture the topology of a space that
doesn’t admit such a countable description.
51

that xn1∈B1(a). Then inductively take ni >n i−1 with xni∈B1/i(a). This yields a subsequence
converging to a.
Let X be sequentially compact. We introduce the following lemma.
Lemma. If X is sequentially compact, then for all ϵ> 0, X can be covered by ﬁnitely many open
balls of radius ϵ.
Proof. Suppose for contradiction there exists ϵ> 0 such that no ﬁnite collection of balls of radius
ϵ cover X. Take x1∈ X, and inductively take xn∈ X\⋃n
i=1Bϵ(xi). Thus we have a sequence
x1,x 2,...,x n with distance between any distinct points at least ϵ. This yields a sequence with no
convergent subsequence, which is a contradiction.
We will also need the next lemma.
Lemma. LetX be sequentially compact. Then every open cover of X has a Lebesgue number.
Proof. Suppose for contradiction 27 there is a cover A ={Ai}i∈I. For all n, there exists Cn⊂ X
with diameter less than 1/n such that Cn is not contained in any single Ai.
Choose xn∈Cn for all n. By sequential compactness, there exists a convergent subsequence that
converges to some a. We know a∈Ai for some i, and thus there exists ϵ> 0 with a∈Bϵ(a)⊂Ai.
Pick k large enough so that d(xnk,a ) < ϵ/2. Then the diameter of Cnk is less than 1 /nk < ϵ/2.
This implies
Cnk⊂Bϵ/2(xnk)⊂Bϵ(a)⊂Ai
which is a contradiction.
It is now easy to prove the last part of the theorem. For sequentially compact X, given an open
coverX =⋃
i∈IUi, by the second lemma there exists δ >0 such that every subset of diameter less
thanδ is contained entirely in some Ui. Let ϵ<δ/ 2. Then by the ﬁrst lemma X can be covered by
ﬁnitely many ballsBϵ(x1),...,B ϵ(xn), whereBϵ(xi)⊂Uji. Thus Uj1,...,U jn are a ﬁnite subcover,
and X is compact.
27In general it is easier to contradict sequential compactness by building a sequence with no convergent subsequence
than to try leverage this condition to prove the claim directly.
52

10/9/2019 - Compactiﬁcations and Local Compactness
We saw on the homework assignment that although Rn is not compact, Rn∪{∞} with a basis
given by the usual open balls along with
Ur ={x∈ Rn :|x|>r}∪{∞}
forr> 0 is compact. This is a case of a more general construction, the compactiﬁcation of a space.
Deﬁnition. LetY be compact and Hausdorﬀ. If X ↪→Y is an embedding 28 such that X is dense
in Y , then Y is a compactiﬁcation of X. If Y\X is a single point, then Y is the one-point
compactiﬁcation of X.
Examples
• The circle S1 is a compactiﬁcation of the open interval (0 , 1). However, [0 , 1] is also a
compactiﬁcation of (0, 1), which shows that compactiﬁcations are not necessarily unique.
• The open square (0, 1)× (0, 1) has many compactiﬁcations:
– The closed square [0, 1]× [0, 1] is a compactiﬁcation.
– The sphereS2 is a compactiﬁcation (the one-point compactiﬁcation, as (0, 1)×(0, 1)
is homeomorphic to R2).
– The torus S1×S1 is a compactiﬁcation.
• Real or complex projective space ( RPn or CPn) is a compactiﬁcation of Rn or Cn.
• Let Z be endowed with the discrete topology and take X = Z∪{∞} , given the subspace
topology in R∪{∞} . Then X is the one-point compactiﬁcation of Z.
Compactiﬁcations are very useful. For example, in algebraic geometry compact varieties are much
easier to work with. It is thus worth investigation when they exist, and what sort of properties
they exhibit. To answer this question, we introduce local compactness.
Deﬁnition. A space X is locally compact at x if there exists a compact subset K⊂ X which
contains a neighborhood of x. X is locally compact if it is locally compact at all x∈X.
Examples
• Any compact space is locally compact.
• Rn is locally compact. For all points x∈ Rn, the closed ball Br(x) is a closed and
bounded subset of Rn (thus compact) that contains the open neighborhood Br(x).
• Rω with the product topology is not locally compact, as none of its basis elements are
contained in compact subspaces (otherwise their closures would be a closed subset of a
compact space and hence compact). More explicitly, local compactness at 0 would require
28An embedding is a homeomorphism onto its image. Intuitively, an embedding allows us to view the abstract
topological space X as a subspace of Y .
53

some neighborhood
(−ϵ,ϵ )×... × (−ϵ,ϵ )× R× R×...
to lie in a compact neighborhood, which implies
[−ϵ,ϵ ]×... × [−ϵ,ϵ ]× R× R×...
is compact. But this is easily seen to be a contradiction.
Constructing compactiﬁcations
Local compactness turns out to be precisely the assumption both necessary and suﬃcient to ensure
that a Hausdorﬀ space X has a Hausdorﬀ one-point compactiﬁcation.
Theorem. X is a locally compact Hausdorﬀ space if and only if there exists a one-point compact-
iﬁcationY of X. Moreover, if such a compactiﬁcation Y exists, then it is unique up to homeomor-
phism.
Proof. Suppose Y = X∪{∞} is a one-point compactiﬁcation, namely that it is compact and
Hausdorﬀ. The subspace X⊂Y is Hausdorﬀ, and if x∈X choose disjoint neighborhoods x∈U
and∞∈ V . Let C =Y\V . C is compact, as it is a closed subspace of Y . And
x∈U⊂C =Y\V ⊂Y\{∞} =X
Therefore Y is locally compact at x.
Suppose X is locally compact Hausdorﬀ. Deﬁne Y as the set Y = X∪{∞} , where the element
∞⁄∈ X is a distinct symbol. Deﬁne a topology on Y by
T ={U :U⊂X open}| {z }
(1)
∪{Y\C :C⊂X compact}| {z }
(2)
The ﬁrst sets (1) are those that are already open in X. The second sets (2) are those containing
∞ whose complements are compact subsets of X.
1. We ﬁrst conﬁrm that this indeed deﬁnes a topology. The empty set ∅ is in the ﬁrst summand
(1). The space Y =Y\ ∅ is in the second summand (2).
Arbitrary unions and ﬁnite intersections of type (1) are of type (1), and the unions and
intersections of type (2) are type (2). This is because if Ci⊂ X is a collection of compact
subspaces for i∈I, then⋂
i∈I is compact and C1∪... ∪Cn is compact.29
If U⊂X is open and C⊂X is compact (and hence closed), then
U∩ (Y\C) =U∩ (X\C)
is open of type (1) and
U∪ (Y\C) =Y\ (C∩ (X\U))
29These claims are not too diﬃcult to prove.
54

is open of type (2), as C∩ (X\U) is closed in C and hence compact.
Moreover, since X is open in Y , as it is of type (1), the subspace topology on X induced by
T is the original topology on X.
2. Y is Hausdorﬀ. If two points x,y ∈ Y lie in X, then they can be separated by the corre-
sponding open neighborhoods that arise from the Hausdorﬀ X⊂Y . To separate x∈X and
∞, local compactness implies there exists a compact C containing an open neighborhood U
of x. Then U and Y\C separate x and∞.
3. Y is compact. Let {Ui}i∈I be an open cover. ∞ lies in some U0 = Y\C, for C compact.
Now{Ui∩C}i∈I are an open cover of C, so by compactness there exists a ﬁnite subcover
C = (U1∩C)∪... ∪ (Un∩C). Thus C⊂U1∪... ∪Un, and Y =U0∪U1∪... ∪Un.
4. Finally, Y is unique up to homeomorphism. Suppose there is another Y′ = X∪{p} that is
comapct and Hausdorﬀ such that subspace topology on X agrees with our original topology
on X. We will show that the map Y → Y′ deﬁned by the identity on X and∞↦→ p is a
homeomorphism, so that the only diﬀerence between Y and Y′ is the naming of the added
point.
• {p} is closed, as Y′ is Hausdorﬀ. Therefore X⊂Y′ is open. So the subspace topology
on X consists exactly of open subsets of Y′ which contain X. Then the type (1) open
sets in Y′ are exactly the open sets of X.
• If V ⊂Y′ is open and p∈V , then C =Y′\V is closed in Y′, and hence C is compact.
But in fact C⊂Y′\{p} =X, so V =Y′\C, where C⊂X, is compact. Conversely, if
C⊂X is compact, then it is closed in Y′ by Hausdorﬀness, and so Y′\C must be open
in Y′.
Note that the deﬁnition we have given for local compactness doesn’t seem very local. 30 We can
provide a better formulation when X is Hausdorﬀ.
Proposition. Assume X is Hausdorﬀ. Then X is locally compact if and only if for all x∈X and
neighborhoodsU of x, there exists a neighborhood V of x such that V ⊂U and V is compact.
Proof. Suppose for all x∈X and neighborhoods U of x, there exists a neighborhood V of x such
that V ⊂U and V is compact. Take U =X, at which points there exists compact V containingx
that contains the open neighborhood V of x.
Now suppose X is locally compact. Let x∈ X and U be a neighborhood of x. Let Y be the
one-point compactiﬁcation of X. Recall that Y is compact Hausdorﬀ and C =Y\U is closed in
Y and thus compact. We require the following lemma.
Lemma. Let Y be Hausdorﬀ. If C⊂ Y is compact and disjoint from x, then there exist disjoint
open neighborhoodsV of x and V′ of C.
30The term local in topology usually means something like examining arbitrarily small neighborhoods.
55

Proof. The proof of this lemma just like proof that compact sets in a Hausdorﬀ space are closed.
Since x⁄∈C, for each y∈C we can choose disjoint open neighborhoods Vy of x and V′
y of y. The
collection{V′
y}y∈C is a cover of C, and by compactness thus admits a ﬁnite subcover V′
y1,...,V ′
yn.
Then takeV =Vy1∩...∩Vyn andV′ =V′
y1∪...∪V′
yn. V does not intersect anyV′
yi, soV∩V′ = ∅.
And x∈V and C⊂V′, as desired.
Apply the lemma to conclude that there exists disjoint neighborhoods V around x and V′ around
Y\U. Thus we have
x∈V ⊂V ⊂ (Y\V′)⊂ (Y\C =U)
Next time we will introduce separation axioms, which are a similar way of describe to what extend
points and subsets of a topological space can be separated by open sets. We will focus on normal
spaces and metrizability.
56

10/16/2019 - Countability, Separability, and Normal Spaces
We will speak a bit about separation axioms and metrizability. One could discuss point set topology
for a long time, but we will limit ourselves to a brief overview of the subject. 31
Countability
There are diﬀerent ways in which a topological space can be ‘countably complicated’. We are
of course not demanding that the underlying set be countable or the topology of open sets be
countable.
Deﬁnition. A topological space X has a countable basis of neighborhoods at x∈ X if there
exists a countable collection U1,U 2,... of neighborhoods of x such that every neighborhood V of x
contains some Ui.
This captures the idea that a topological space could have countable complexity locally.
Deﬁnition. A space with a countable basis of neighborhoods at all x∈X is ﬁrst countable.
Examples
• Any metric space is ﬁrst countable. For each x∈X, takeUn =B1/n(x). Then U1,U 2,...
is a countable basis of neighborhoods at x.
• R𝓁 is ﬁrst countable. Take Un = [x,x + 1/n).
First countability is a way of characterizing when sequences are capable of detecting topological
phenomena.
Theorem. Let A⊂X be a subspace, and let x∈X. If there exists a sequence (an) with an∈A
that converges to x, then x∈A. If X is ﬁrst countable, then the converse also holds.
We can assume that the basis of neighborhoods satisﬁes a descending chain U1⊃U2⊃... . Then
takean∈Un to obtain a sequence that converges to a.
There is a stronger notion of countability on a topological space as well.
Deﬁnition. A topological spaceX is second countable if its topology admits a countable basis.
Example
• R with the usual topology is second countable, as the basis {(a,b ) : a,b∈ Q} generates
the Euclidean topology.
• Rn with the usual topology is second countable, as the basis {(a1,b 1)×... × (an,bn) :
ai,bi∈ Q} generates the Euclidean topology.
• Rω with the product topology is second countable, as it is generated by products of R
31Lots of additional point set topology comes up in functional analysis.
57

with ﬁnitely many open intervals with rational endpoints. This is because the set of all
ﬁnite subsets of a countable set is itself countable.
• Rω with the uniform topology is not second countable, even though it is a metric space.
Indeed,{0, 1}ω⊂ Rω is an uncountable subset that is discrete in the uniform topology.
Thus there exist basis elements Brx(x) around each x∈{ 0, 1}ω that does not intersect
any other points of{0, 1}ω. This implies that any basis of Rω with the uniform topology
is uncountable.a
aNote that Rω with the uniform topology is still ﬁrst countable.
Proposition. If X is second countable, then X contains a countable, dense subset.
Proof. Given a countable basis, choose a point from each nonempty element of the basis. Every
open set must contain a basis element and hence one of these points.
The converse of this proposition is not true. R𝓁 has a dense, countable subset Q. The idea is that we
must include half-open intervals that begin at every irrational number, and there are uncountably
many such irrationals.
Regular and normal spaces
Recall that a spaceX is Hausdorﬀ if distinct points have disjoint, open neighborhoods. This implies
the weaker property that single points are closed.
Deﬁnition. Suppose the singletons {x}⊂ X are closed for all x∈X.
X is regular if, for all x∈ X and closed subsets B⊂ X disjoint from x, there exist disjoint,
openU,V ⊂X with x∈U and B⊂V .
X is normal if for all disjoint, closed A,B ⊂X there exist disjoint, open U,V ⊂X with A⊂U
and B⊂V .
If a space is normal, it is regular (we can take the closed set A simply to be {x}). If a space is
regular, it is Hausdorﬀ (we can take the closet set B simply to be{y}).
Many common spaces are normal, but it is useful to examine carefully the boundaries between
them.
Example
• R𝓁 is normal. Let A,B ⊂ R𝓁 be disjoint and closed. Given a point a∈A, there exists a
neighborhood of a disjoint from the closed set B. Namely, [a,a +ϵa)∩B = ∅ for some
ϵa> 0. Similarly, there is an open neighborhood [ b,b +ϵa) of b that is disjoint from A.
Let U = ⋃
a∈A[a,a +ϵa) and V = ⋃
b∈B[b,b +ϵb). U and V are open. They remain
disjoint, as we expand both sets to right (and they will not intersect, as we do not
increase them to the left).
58

• Normality is not necessarily preserved over products. R2
𝓁 is regular, as the product of
regular spaces is regular. However, the product is not normal (this is one of the simplest
examples of the failure of normality over products). a
• R and Rn are normal. In fact, Rω with the product or the uniform topology is also
normal. If I is uncountable, then RI is regular but not normal.
aThe proof is quite involved.
Theorem. If X is a regular space with a countable basis, then X is normal.
The idea of the proof is that given two closed sets, we use the countable basis to provide an order
by which we build up the two open neighborhoods. We have the following consequential theorem.
Theorem. Every metric space is normal.
Proof. Let A,B be disjoint, closed sets in X. For all a ∈ A, there exists ϵa > 0 such that
B(a,ϵa)∩B = ∅. Similarly, for all b∈B there exists ϵb> 0 such that B(b,ϵb)∩A = ∅. Let
U =
⋃
a∈A
B
(
a,ϵa
2
)
V =
⋃
b∈B
B
(
b,ϵb
2
)
The claim is that U∩V = ∅. Indeed, if z∈ U∩V there exists a∈ A and b∈ B such that
d(a,z )<ϵ a/2 and d(b,z )<ϵ b/2. By the triangle inequality
d(a,b )≤d(a,z ) +d(z,b )< ϵa
2 + ϵb
2 ≤ max{ϵa,ϵb}
which implies z∈B(a,ϵa) or z∈B(b,ϵb).
Theorem. Every compact Hausdorﬀ space is normal.
Proof. Letx∈X andB⊂X be closed (and thus compact). If x⁄∈B, given any point y∈B there
exist disjoint, open Uy,Vy with x∈Uy and y∈Vy by Hausdorﬀness. By compactness, there exist
y1,...,y n with B⊂⋃n
i=1Vyi. Take U =⋂n
i=1Uyi. U,V are open and disjoint, so X is regular.
Given closed (and thus compact), disjoint A,B ⊂ X, for all y ∈ B there exist disjoint, open
Uy,Vy with A⊂Uy and y∈Vy. B is compact, so there exist y1,...,y n with B⊂⋃n
i=1Vy1. Take
U =⋂n
i=1Uy1 and V =⋃n
i=1Vyi. Then U∩V = ∅, so X is normal.
We know a metric space is regular and normal. The Urysohn metrization theorem provides a
converse.
Theorem. LetX be regular with a countable basis. Then X is metrizable.
The ﬁrst condition is necessary, but the second one is not optimal. TheNagata-Smirnov metrization
theorem weakens this assumption.
59

Theorem. X is metrizable if and only if X is regular and admits a countable, locally-ﬁnite basis. 32
We will not both to prove this stronger version, but the proof of the Urysohn metrization lemma has
an elegant proof. The key idea will be to build continuous functions that separate closed subsets.
32This is a basis that is a union of countably many components, each of which is locally ﬁnite (this means there
exists a neighborhood of every point in the space that intersects only ﬁnitely many of these components).
60

10/21/2019 - Urysohn’s Lemma and the Metrization Theorem
The following result is the Urysohn metrization theorem.
Theorem. If X is regular33 and has a countable basis, then X is metrizable.
The key ingredient in this theorem is Urysohn’s lemma.
Theorem. Let X be a normal space and A,B be disjoint closed subsets. Then there exists a
continuous function f :X→ [0, 1] such that f(x) = 0 for all x∈A and f(x) = 1 for all x∈B.
The idea of the proof will ﬁrst be to construct open sets Uq for all q∈ [0, 1]∩ Q such that
A⊂U0⊂... ⊂U1 =X\B
and p<q implies Up⊂Uq, suing normality of X. The second step will be to deﬁne
f(x) = inf{q∈ Q :x∈Uq}
and show that f is continuous.
The ﬁrst step will use the following formulation of normality.
Lemma. If X is normal, then for all closed A⊂X and open U⊃A, there exists an open V ⊂X
such that A⊂V and V ⊂U.
Intuitively, this says that in a normal space every neighborhood of a closed subset contains another
smaller open neighborhood and its closure.
Proof. A and B =X\U are disjoint closed sets, so by normality there exist disjoint open V ⊃A
and V′⊃B. X\V′ is closed, so V ⊂X\V′ implies V ⊂X\V′. We have
A⊂V ⊂V ⊂ (X\V′)⊂ (X\B =U)
as desired.
We now present a proof of Urysohn’s lemma.
Proof. We begin with the ﬁrst step outlined above. Let A,B be disjoint and closed. Take U1 =
X\B, and by the previous lemma let U0 be open such that A⊂U0⊂U0⊂U1. Next, we construct
Uq for q∈ (0, 1)∩ Q such that p<q implies Up⊂Uq. This proceeds by induction. Choose a well
33Recall that this means it is possible to separate points from closed sets. Namely, if x is disjoint from a closed set
A then there exists disjoint open neighborhoods U ofx andV ofA. However, a regular space that admits a countable
basis is normal, which means that it is possible to separate disjoint closed sets from each other.
61

ordering34{q0,q 1,q 2,... } of [0, 1]∩ Q such that q0 = 0 and q1 = 1. Assuming Uq0,...,U qn have
already been chosen we construct Uqn+1 using the above lemma. Namely, take
qk = max
(
{q0,...,q n}∩ [0,qn+1)
)
q𝓁 = min
(
{q0,...,q n}∩ (qn+1, 1]
)
so that qk < qn+1 < q𝓁 and none of the rationals already consider lie in between these. By
the inductive hypothesis, Uqk⊂ Uq𝓁, so by using normality there exists an open set V such that
Uqk⊂V ⊂V ⊂Vq𝓁. Let Uqn+1 =V . Also set Uq = ∅ for q <0 and Vq =X for q >1, and observe
that we have a collection{Uq}q∈Q such that p<q implies Up⊂Uq.
Next, deﬁne the function
f(x) = infQx
where
Qx ={q∈ Q :x∈Uq}
We have thatf satisﬁes the following properties.
• f(x)≤ 1 for all x∈X since x∈Uq for all q >1.
• If x∈B then x⁄∈U1 =X\B, so Qx = Q∩ (1,∞) and f(x) = 1.
• f(x)≥ 0 for all x∈X since Qx⊂ [0,∞) because Uq = ∅ when q <0.
• If x∈A⊂U0, then 0∈Qx and f(x) = 0.
So the function f satisﬁes the desired properties, and it only remains to show that f is continuous.
• x∈Uq implies f(x)≤q. If x∈Uq then x∈Uq′ for all q′>q , so Qx⊃ Q∩ (q,∞).
• x⁄∈Uq implies f(x)≥q. If x⁄∈Uq then Qx⊂ Q∩ (q,∞).
Now we can prove thatf−1((c,d )) is open inX for all open intervals (c,d ). Assume x0∈f−1((c,d )),
and letp,q∈ Q such thatc<p<f (x0)<q <d . Then by the above remarks,x0∈Uq andx0⁄∈Up.
The set V =Uq∩ (X\Up) is open and a neighborhood of x0. Moreover, x∈V implies x⁄∈Up so
f(x)≥p and x∈Uq so f(x)≤q. Therefore V ⊂f−1((c,d )), which completes the proof.
Now we can prove the metrization theorem. We will do this by embedding X into a metric space,
namely [0, 1]ω with either the product topology or the uniform topology. The uniform topology
comes from the metric
d∞((xn), (yn)) = sup{|yn−xn|}
and the product topology comes from the metric
d′
∞((xn), (yn)) = sup
{ 1
n|yn−xn|
}
34A well ordering is a total ordering < on (0, 1)∩ Q, namely an irreﬂexive, antisymmetric, transitive, total relation
that is wellfounded, which means every nonempty subset contains a least element. This allows us to induct over the
rationals, and the existence of such a well-ordering on any set is equivalent to the axiom of choice.
62

The balls in the metric d′
∞ are
Bd′
∞
ϵ ((xn)) =
∏
n
(xn−nϵ,xn +nϵ)
The key point is that for n>ϵ −1 the multiplicand (xn−nϵ,xn +nϵ) is all of [0, 1]. We require the
following lemma.
Lemma. There exists a countable collection of continuous functions fn :X→ [0, 1] such that for
all x0∈X and neighborhoodsU of x0, there exists n for which fn(x0)> 0 and fn = 0 on X\U.
Proof. This follows from Urysohn’s lemma, but we need to be careful to ensure that countably
many functions suﬃces. Let B ={Bn} be a countable basis forX. If U is an open neighborhood of
x0 then there exists some Bn such that x0∈Bn⊂U. By normality of X, there exists open V for
whichx∈V ⊂V ⊂Bn and there existsBm such thatx∈Bm⊂V . This yields x∈Bm⊂Bn⊂U.
For every (m,n ) ∈ N× N such that Bm ⊂ Bn, apply Urysohn’s lemma to obtain a function
gm,n : X→ [0, 1] such that gm,n = 1 on Bm and gm,n = 0 on X\Bn. This yields a countable
collection of functions{gm,n :m,n∈ N} with the desired property.
We can now prove the theorem.
Proof. Let{fn :n∈ N} be a countable collection of functions as in the lemma. The claim is that
F :X→ [0, 1]ω
x↦→ (f1(x),f 2(x),... )
is an embedding, which shows that the topology on X can be obtained by restricting the d′
∞ metric
from [0, 1]ω.
• F is continuous in the product topology because each component fn is continuous by con-
struction.
• F is injective, since x⁄= y implies there exists disjoint neighborhoods U of x and V of y.
Thus there existsm,n∈ N such thatfn(x)> 0 andfn = 0 outisde of U (aty) andfm(y)> 0
and fm = 0 outside of V (hence at x).
• F deﬁnes a continuous bijection onto its image Z = F (X), it only remains to show that if
U⊂X is open then F (U)⊂Z is open. For this, let U⊂X be open and x0∈U. Then there
exists n such that fn(x0)> 0 and fn = 0 outside of U. Let
Vn =π−1
n ((0,∞))∩Z ={(z1,z 2,... )∈Z :zn> 0}⊂ Z
Vn is open. Then x0 ∈ F−1(Vn)⊂ U, since fn(x0) > 0 and fn(x) > 0 implies x∈ U.
Therefore F (x0)∈Vn⊂F (U), with Vn open in Z. This holds for all x0∈U, so we conclude
F (U) is open.
Therefore F :X→Z is a homeomorphism, and X is in fact a metric space.
Remark. When X does not admit a countable basis this procedure still produces embeddings of X
into [0, 1]I. However, [0, 1]I is not metrizable when I is uncountable.
63

10/23/2019 - Category Theory, Paths, Homotopy
Today we will begin the second part of the course, which is an introduction to algebraic topology.
Categories
Category theory is a language that provides a precise way to formulate patterns that appear in
diﬀerent areas of mathematics.
Deﬁnition. A category consists of a collection 35 of objects and, for each pair of objects A and
B, a collection of morphisms Mor(A,B ) from A to B. There is an operation of composition
◦ :Mor(A,B )× Mor(B,C )→ Mor(A,C ) that takes (f,g ) to g◦f. This operation must satisfy two
axioms:
1. Every object A has an identity morphism idA∈ Mor(A,A ) such that for all morphisms f∈
Mor(A,B ), we have f◦ idA = idB◦f =f.
2. Composition of morphisms is associative, namely (f◦g)◦h =f◦ (g◦h).
Examples
• The category Set has objects that are sets, and its morphisms are functions between sets.
• The category Vectk has objects that are ﬁnite-dimensional vector spaces over a ﬁeld k,
and its morphisms are linear maps between vector spaces.
• The category Group has objects that are groups, and its morphisms are group homomor-
phisms between groups.
• The category Top has objects that are topological spaces, and its morphisms are contin-
uous functions between spaces.
The above example illustrates that a category often consists of a collection of sets endowed with ad-
ditional structure, with morphisms the functions on the underlying set that respect this structure.
Then the composition law is usually given by the composition of the functions on these underlying
sets. However, not all categories arise as collections of objects with additional structure.
It is an easy exercise to see that the identity morphism is unique, as
idA = idA◦ id′
A = id′
A
Deﬁnition. A morphism f∈ Mor(A,B ) is an isomorphism if there exists g∈ Mor(B,A ) such
that f◦g = idB and g◦f = idA. In such a case, g =f−1 is the inverse of f.
It is easy to see that the identity is an isomorphism. Also, if f is an isomorphism, then f−1 is an
isomorphism. If f and g are isomorphisms, then f◦g is an isomorphism.
35To be precise, a category consists of a class of objects, as sometimes there may be too many objects to be a set.
64

At this point, you should notice that the properties of the collection of isomorphisms are simi-
lar to those of a group. There is an identity element, a composition law, and inverses. However,
the collection of isomorphisms of a category diﬀers from a group, as it is not always possible to
compose two isomorphisms. If we eliminate the problem, however, we indeed obtain a group.
Deﬁnition. The automorphism group of A is the collection
Aut(A) ={f∈ Mor(A,A ) :f is an isomorphism}
under composition of morphisms.
Examples
• In Set, the isomorphisms are precisely the bijective functions on sets. Then given a ﬁnite
set A with n elements, we have Aut(A)≃Sn.
• In Vectk, the isomorphisms are the linear isomorphisms between vector spaces. If V is
an n-dimensional vector space R, then Aut(V )≃GL(n, R).
Note that in both of these examples, if A andB are isomorphic, then Aut(A)≃ Aut(B) as groups.
However, this isomorphism often depends on a choice of an isomorphism between A and B to
identify the two objects. We can then recast the deﬁnition of a group in terms of category theory.
Deﬁnition. A group is a category with a single object in which all morphisms are isomorphisms.
One strength of category theory is that it easily allows one to generalize deﬁnitions far beyond their
original scope.
Deﬁnition. A groupoid is a category in which all morphisms are isomorphic.
Since morphisms may map from/to diﬀerent objects, the composition of two morphisms is not
always deﬁned.
Examples
• The category that consists of sets as objects and bijections as morphisms is a groupoid.
• The category that consists of topological spaces as objects and homeomorphisms as mor-
phisms is a groupoid.
Both of these examples are not particularly interesting, as they are simply obtained from an existing
category by restricting attention to only isomorphisms. We will soon construct a more interesting
groupoid from a topological space by letting the objects be points in the space and taking the
morphisms to be homotopy classes of paths between two points.
Just like a category often consists of objects with structure-preserving maps between them, there
is a notion of a structure-preserving map between categories. In algebraic topology, we will often
65

associate a topological space X to an algebraic invariantA(X) such as groups or vector spaces. We
would further like this association to behave with the continuous maps on X. Namely, we would
like a continuous mapX→Y to induce a morphism A(X)→A(Y ). This associaton of morphisms
should satisfy some nice properties, namely that it should respect composition and isomorphisms.
This will provide a way to construct algebraic invariants of topological spaces.
Deﬁnition. Let C and D be categories. A functor F : C→ D is an assignment of each object
X∈ C to an object F (X)∈ D as well as an assignment of each morphism f∈ MorC(X,Y ) to a
morphism F (f)∈ MorD(F (X),F (Y )). This should satisfy
1. F (idX) = idF (X), namely F respects the zero-fold composition of morphisms.
2. F (f◦g) =F (f)◦F (g)
Examples
• The forgetful functor takes an object of Group, Top, or Vectk to the underlying set and
a morphism to the underlying function on sets.
• Given a vector space V ∈ Vectk, there is a functor F : Vectk→ Vectk given by F (W ) =
Hom(V,W ). A linear map f : W→ U induces a linear map Hom( V,W )→ Hom(V,U )
given by taking ϕ∈ Hom(V,W ) to f◦ϕ∈ Hom(V,U ).
Homotopy
One goal of algebraic topology is to study spaces up to continuous deformation, often parameterized
by the interval I = [0, 1]. This is homotopy.
Deﬁnition. Letf,g :X→Y be continuous maps. A homotopy betweenf and g is a continuous
map F :X× [0, 1]→Y such that F (x, 0) =f(x) and F (x, 1) =g(x) for all x∈X. In such a case,
f and g are homotopic and we write f≃g.
It is often convenient to view the parameter in I as describing a deformation of the map f to g
over time.
Deﬁnition. If f is homotopic to a constant map, then f is nullhomotopic.
If Y is path-connected, any two nullhomotopic paths are homotopic. 36
Deﬁnition. A path in a spaceX fromx0 tox1 is a continuous map f :I→X such that f(0) =x0
and f(1) =x1.
In turns out the studying general paths in a space is not too interesting, as any map from a
contractible space is always nullhomotopic. If we ﬁx endpoints, however, the picture becomes much
more interesting.
36Take one path along a homotopy to a point, move the point along a path to the other point, and the apply the
homotopy for the other map in reverse.
66

Deﬁnition. A homotopy of paths is a homotopy between f,g :I→X wheref(0) = g(0) = x0
and f(1) =g(1) =x1 that ﬁxes the endpoints at all time. More explicitly, there exists a homotopy
F :I×I→X such that F (s, 0) =f(s), F (s, 1) =g(s),F (0,t ) =x0,F (1,t ) =x1. In such a case,
we write f≃pg.
Lemma. Homotopy≃ and path homotopy ≃p are equivalence relations.
Proof. A map f is homotopic to itself by taking the constant homootpy F (x,t ) =f(x).
If f≃g under a homotopy F (x,t ), then g≃f via reversing the homotopy G(x,t ) =F (x, 1−t).
If f ≃ g under the homotopy F and g ≃ h under the homotopy G. We compose these two
homotopies, reparameterizing each appropriately.
H(x,t ) =
{
F (x, 2t) t∈ [0, 1/2]
G(x, 2t− 1) t∈ [1/2, 1]
H is continuous because F and G are and they agree on the intersection of their domains.
None of the proof involved adjusting endpoints, so this also shows ≃p is an equivalence relation as
well.
We denote the (path) homotopy equivalence class of f by [f].
67

The straight line homotopy
Lemma. Letf,g be any paths in Rn fromx0 to x1. Then f≃pg.
Proof. Deﬁne the straight line homotopy between f and g by
F (s,t ) = (1−t)f(s) +tg(s)
This is a parameterization of the line segment between f(s) and g(s).
Remark. This result holds more generally in any convex subset of Rn, as the line segment
between any two points in a convex subset is contained in the subset.
This also holds for any maps, not just paths, into Rn. This means that Rn, and convex sets
more generally, are homotopically trivial. a
aThere are many other homotopically trivial/contractible spaces, but one must be more clever about inter-
polation.
Example
• In R2\{ 0}, the two paths from ( −1, 0) to (1, 0) that pass above and below the miss-
ing origin are not homotopic. We don’t yet have the tools to prove that formally, however.
This idea will provide a proof that R2\{ 0} is not homeomorphic to R2, and also that R2
is not homeomorphic to R.
Homotopy classes of paths in a given space X form a category, and this category is a groupoid.
The key operation will be the compostion/concatenation of paths.
Deﬁnition. Given a path f fromx to y and a path g fromy to z, we deﬁne the path f∗g fromx
to z by
(f∗g)(t) =
{
f(2t) t∈ [0, 1/2]
g(2t− 1) t∈ [1/2, 1]
Note that path homotopy is not associative, but only associative up to path homotopy due to
path parameterization details. One could equally well parameterize by all intervals, but this also
ultimately has its own disadvantages.
Lemma. Path concatenation is well-deﬁned on homotopy classes of paths. Namely, provided that
f(1) =g(0) and f≃pf′ and g≃pg′ then f∗g≃pf′∗g′.
Proof. We deﬁne the homotopy
(F∗G)(s,t ) =
{
F (2s,t ) s∈ [0, 1/2]
G(2s− 1,t ) s∈ [1/2, 1]
68

Then we deﬁne∗ on homotopy classes of paths by [f]∗[g] = [f∗g]. The main claim will be that this
operation∗ is associative, has an identity, as has inverses. Thus path homotopy classes inX form a
groupoid with objects points ofX and morphisms the homotopy classes of paths between two points.
This operation is not always interesting, though. The space Z is totally disconnected, so there
are only morphisms on each point in the space.
Given a point x∈ X, the identity of x in this groupoid will be the homotopy class [ ex], where
ex :I→X is the constant path ex(s) =x.
Given a path f : I → X, the homotopy inverse of f is the path f : I → X given by running
f backwards forf(s) =f(1−s). We will show that this is indeed a homotopy inverse next lecture
and show that∗ is associative.
We then ﬁx all paths at one point to obtain a group associated to the topological space X.
69

10/28/2019 - The Fundamental Group(oid)
Today we will dive deeper into algebraic topology. Recall that we were looking at paths in a space
X, which are continuous maps I→X. We deﬁned the following notion of ‘sameness’ for paths.
Deﬁnition. A path-homotopy between paths f,g : I → X from x to y is a continuous map
F :I×I→X such that F (s, 0) =f(s),F (s, 1) =g(s),F (0,t ) =x,F (1,t ) =y.
In general, we will restrict out attention to individual path-components and take it for granted that
we can understand these individual pieces of a space by probing them with maps from the interval.
We deﬁned a concatenation operation on paths f,g : I → X by declaring f∗g to be the path
obtained by ﬁrst running f and then running g. In formulas, this is
(f∗g)(s) =
{
f(2s) s∈ [0, 1/2]
g(2s− 1) s∈ [1/2, 1]
We proved last lecture that this is well-deﬁned on paths up to homotopy equivalence, and thus
deﬁnes an operation on equivalence classes [ f]∗ [g]. When we pass to path homotopy, we obtain
the following desirable property.
Lemma.∗ on homotopy classes of paths is associative, has an identity, and has inverses. Then the
collection of all homotopy classes of paths along with ∗ is the fundamental groupoid ofX, where
the objects of this groupoid are the points of X and the morphisms from x to y are the homotopy
classes of maps from x to y.
Proof. The identity morphism at a pointx∈X will be given by idx = [ex], whereex is the constant
path ex(s) =x. We need to check that the identity behaves as expected under composition.
The homotopy
F (s,t ) =
{
f
( s
1−t/2
)
s∈ [0, 1−t/2]
y s ∈ [1−t/2, 1]
is a path homotopy from f to f∗ey. A similar computation shows that id x◦ [f] = [f] as well.
Given a pathf, deﬁnef(s) =f(1−s). f runs the pathf backwards. The claim is that [f]∗[f] = idx
70

and [f]∗ [f] = idy. The diagram
suggests that we should consider a family of paths that travel partially along f and then return.
Explicitly, the homotopy
F (s,t ) =
{
f(2ts) s∈ [0, 1/2]
f(2t(1−s)) s∈ [1/2, 1]
is a path homotopy from ex to f∗f.
Finally, we check associativity. The reason ( f∗g)∗h⁄= f∗ (g∗h) literally is that, in the ﬁrst
expression, we spend 1/4 of the time on f and g and 1/2 of the time on h, whereas in the second
expression we spend 1/2 of the time on f and 1/4 of the time on g and h. Then the diagram
shows we can rescale the time parameter as desired.
Although groupoids capture much information about a space, they can be diﬃcult to deal with.
For that reason, we will restrict our attention to a single point to obtain a group. We choose a
base point x0∈X and consider only loops at x0, namely paths that begin and end at x0.
Deﬁnition. The set of path homotopy classes of loops based at x0, with operation ∗, is the fun-
damental group of X at x0, denoted π1(X,x 0).37
37The notation is suggestive, as there are higher homotopy groups deﬁned as homotopy classes of maps from
higher-dimensional spheres into X.
71

The fundamental group is of great importance in topology. The fact that it is a group follows
immediately from the previous lemma, as π1(X) is given as the automorphism group of a point
x0∈ X. We will see that this group is often nontrivial and examine its behavior under maps. 38
Today we will introduce some basic notions.
Example
• In Rn, or a convex subspace of Rn, every loop at x0 is homotopic to the constant loop
via the straight line homotopy. Explicitly, the path homotopy
F (t,s ) = (1−t)f(s) +tx0
does the trick. Therefore π1(Rn,x 0) ={id} = 1.
Deﬁnition. A space X is simply connected if X is nonempty, path-connected, and for some x0
we have π(X,x 0) = 1.
Then the above example should then be interpreted as saying that Rn, and any convex subset of
Rn, is simply-connected. Sn is simply-connected whenn≥ 2. However, S1 is not simply-connected,
and we will study π1(S1,x 0) in great detail.
It turns out that, when restricting to the same path component, π1(X,x 0) is independent of the
base point x0.
Proposition. Letx0 and x1 be points in a path-connected space X. Then π1(X,x 0)≃π1(X,x 1).
Proof. We must determine how to relate loops at x0 to those at x1.
For a loopf atx0 and a pathα fromx0 tox1, we obtain a loop atx1 by the concatenationα∗f∗α.
This yields a map
ˆα :π1(X,x 0)→π1(X,x 1)
[f]↦→ [α∗f∗α] = [α]−1∗ [f]∗ [α]
38This will require the technology of covering spaces, which are a way of unrolling a topological space in a discrete
way.
72

We will show that ˆα is a group isomorphism, namely that it is a homomorphism with an inverse.
If a,b∈π1(X,x 0) then we have
ˆα(a∗b) = [α]−1∗a∗b∗ [α]
= [α]−1∗a∗ [α]∗ [α]−1∗b∗ [α]
=ˆα(a)∗ˆα(b)
by associativity and identity. Let β = α be the path α run in reverse. The claim is that ˆβ is an
inverse to ˆα. Indeed, for a∈π1(X,x 0) we have
ˆβ◦ˆα(a) =ˆβ([α]−1∗a∗ [α])
= [β]−1∗ [α]−1∗a∗ [α]∗ [β]
=a
Thereforeˆβ◦ˆα = id, and the same argument provesˆα◦ˆβ = id. Therefore π1(X,x 0)≃π1(X,x 1).
This result can be stated categorically as well. Ifx0,x 1 are isomorphic in the fundamental groupoid,
namely there exists a path from x0 tox1, then Aut(x0)≃ Aut(x1). This proposition should not be
too surprising, as it says that studying continuous loops at a point does not depend on continuous
moving the base point around the space.
Corollary. If X is path-connected, then up to isomorphism π1(X,x 0) is independent of the base
pointx0.
Corollary. A loop f at x0 induces an automorphism ˆf : π1(X,x 0)→ π1(X,x 0). This yields a
group action of π1(X,x 0) on itself via conjugation:
a↦→ [f]−1∗a∗ [f]
Such a map is an inner automorphism of π1(X,x 0).
An obvious next question would be the extend to which the fundamental group is a natural con-
struction on a space. In other words, how does changing the spaceX aﬀect the fundamental group?
The key idea will be thatπ1 can be understood as a functor from the category of pointed topological
spaces to the category of groups.
Deﬁnition. The category of pointed topological spaces is the category Top∗, whose objects
consist of pairs (X,x 0), where X is a space and x0 ∈ X a point. The morphisms of Top∗ are
continuous maps that respect the points, namely a map f :X→Y such that f(x0) =y0.
Proposition. A morphism h : (X,x 0)→ (Y,y 0) induces a group homomorphism h∗ :π1(X,x 0)→
π1(Y,y 0) deﬁned by
h∗([f]) = [h◦f]
We must check that this homomorphism is well-deﬁned, namely that if [f] = [f′] then [h◦f] = [h◦f′].
This is simple, though, as ifF :I×I→X is a homotopy betweenf andf′ thenh◦F is a homotopy
betweenh◦f and h◦f′. It is also easy to see that h◦ (f∗g) = (h◦f)∗ (h◦g), so together these
facts imply we have a well-deﬁned homomorphism
h∗([f]∗ [g]) =h∗([f])∗h∗([g])
73

Corollary. π1 : Top∗→ Group is a functor. It sends an object (X,x 0)∈ Top∗ to π1(X,x 0) and a
morphism h : (X,x 0)→ (Y,y 0) to the induced map h∗ :π1(X,x 0)→π1(Y,y 0).
Note that it still remains to check that π1 respects composition of morphisms, namely that if
h : (X,x 0)→ (Y,y 0) and k : (Y,y 0)→ (Z,z 0) are morphisms then (k◦h)∗ =k∗◦h∗.
π1(X,x 0) π1(Y,y 0) π1(Z,z 0)
(k◦h)∗
h∗ k∗
But this follows immediately from the associativity of function composition, as
(k◦h)∗([f]) = [(k◦h)◦f]
= [k◦ (h◦f)]
=k∗([h◦f])
=k∗◦h∗([f])
Since functors map isomorphisms to isomorphisms (as inverses are sent to inverses), we obtain the
following result for free.
Corollary. If h : (X,x 0)→ (Y,y 0) is a homeomorphism, then h∗ : π1(X,x 0)→ π1(Y,y 0) is an
isomorphism.
This is good, because we would like to view homeomorphic spaces as the same, so they should have
the same fundamental group. Homeomorphism is a very strong idea of sameness for topological
spaces, however, and we will see later than π1 is invariant under a much weaker notion, homotopy
equivalence.
74

10/30/2019 - Covering Spaces, Path Lifting
Given a pointed topological space ( X,x 0), we associate to it the fundamental group π1(X,x 0).
This group consists of homotopy classes of loops based at x0, with product given by concatenat-
ing two loops. Up to isomorphism, π1(X,x 0) is independent of basepoint, and a continuous map
(X,x 0)→ (Y,y 0) induces a homomorphism π1(X,x 0)→π1(Y,y 0).
To compute π1(X,x 0), we will introduce covering spaces. These are topological spaces that ‘sit
above’X in some discrete way.
Deﬁnition. Letp :E→B be a continuous, surjective map. p evenly covers an open set U⊂B
if
p−1(U) =
⨆
α∈A
Vα
whereVα⊂E are disjoint open subsets and p|Vα :Vα→U is a homeomorphism.
Equivalently, we can say that there is a homeomorphismp−1(U)→U×A, whereA has the discrete
topology, such that
p−1(U) U×A
U
∼
p
commutes.
Deﬁnition. If p :E→B is continuous and surjective such that every point b∈B has a neighbor-
hood evenly covered by p, then E is a covering space of B with covering map p.
The equivalent deﬁnition above means that we can alternatively characterize covering spaces as
ﬁber bundles with discrete ﬁber.
75

Examples
• Let X be any topological space and A be discrete. Then p : X×A→ X is a covering
map. This is the trivial |A|-fold cover of X, and the entire space X is evenly covered by
p.
• Deﬁne p : R→S1 byp(t) = (cost, sint).
To show an arbitrary point has a neighborhood that is evenly covered, consider the point
(1, 0). Let U ={(x,y )∈S1 :x> 0}. U⊂S1 is open in the subspace topology. Then we
have
p−1(U) =
⨆
n∈Z
(2πn−π/2, 2πn +π/2)
p restricted to each (2πn−π/2, 2πn +π/2) is a homeomorphism onto U.
In other words, above each point a covering space is a collection of sheets, but these may be
connected together nontrivially globally. These covering spaces are intimately related to homotopy,
as they allow us to unroll paths of X in interesting ways.
Proposition. Letp :E→B and q :E′→B′ be covering maps. Then (p×q) :E×E′→B×B′
is a covering map.
Example
• The mapp×p : R2→S1×S1, where p : R→S1 is the above covering map of the circle,
is a cover of the torus.
Proof. Given (b,b′)∈ B×B′, there exists open U⊂ B,U′⊂ U′ containing b,b′ that are evenly
76

covered byp,p′, respectively. The claim is that U×U′ is evenly covered by p×p′. For if
p−1(U) =
⨆
α∈A
Vα⊂E
p′−1(U′) =
⨆
β∈B
V′
β⊂E′
then
(p×p′)−1(U×U′) =p−1(U)×p−1(U′) =
⨆
(α,β)∈A×B
Vα×Vβ⊂E×E′
Proposition. If p : E→ B is a covering map and B0⊂ B a subset, then E0 = p−1(B0) is a
covering space of B0 with covering map p|E0.
For example, restricting one’s attention to the meridian and the longitude of the torusS1×S1 yields
a covering space of S1∨S1 (the ﬁgure-eight space) that is the inﬁnite grid, where the horizontal
and vertical lines are 2π apart.
The following important fact is an exercise on the homework assignment.
Proposition. Suppose B is connected and p : E→ B is a covering map. Then for all x,y ∈ B,
the ﬁbers p−1(x) and p−1(y) have the same cardinality.
Deﬁnition. Let B be connected and p : E → B be a covering map. If p−1(x) is ﬁnite, then
d =f−1(x) is the degree of p.
Example
• The covering map p : R→S1 has inﬁnite degree.
• View S1⊂ C as the complex numbers of norm 1. Then the map
p :S1→S1
eiθ↦→eniθ
can be seen to have degree n.
Lifting
It will be extremely useful to develop criteria for when it is possible to lift a map f : Y → X to
another map ~f :Y →E such that
E
Y B
p~f
f
commutes. This lifting will eventually allow us to determine homotopy classes of maps into X.
77

The ﬁrst observation is that if p : E → B is a covering map, then there exists a local lift of
any map f :X→B. Namely, if f(X)⊂U, where U is evenly covered, then if Vα is a sheet over
U we can deﬁne ~f = (p|Vα)−1◦f. We will next show that it is always possible to lift paths, and
homotopies of paths, even if they leave a single evenly covered subspace of B.
Example
• Consider the usual covering mapp : R→S1 given byp(x) = (cosx, sinx). Let f :I→S1
be the path f(s) = (cosπs, sinπs). This path has inﬁnitely many lifts to R, speciﬁed by
choosing an initial point.
Theorem. Let p : E→ B be a covering map and f : [0, 1]→ B a path with f(0) = b. Given
e∈p−1(b), there exists a unique lift ~f : [0, 1]→E such that ~f(0) =e and p◦ ~f =f.
The key idea of the proof is that, as long as the path remains in an evenly covered subspace, there
is a unique choice of the a lift for the path.
Proof. CoverB by open subsets Uα that are themselves evenly covered by p. Then the inverse im-
agesf−1(Uα) cover the interval [0, 1]. By the Lebesgue number lemma, there exists δ >0 such that
(s,s +δ) lies in a single set f−1(Uα), and equivalently f(s,s +δ) lies in a single Uα. Thus we can
subdivide the path 0 =s0≤s1≤... ≤sn = 1 such thatf(si,si+1)⊂Uα for someα depending oni.
Deﬁne ~f(0) = e. Assume that ~f is deﬁned on [0 ,si]. By construction, f(si,si+1) lies in a sin-
gle evenly coveredU. f(si) is deﬁned, so let V ⊂p−1(U) be the slice above U containing thisf(si).
Fors∈ [si,si+1], deﬁne f(s) = (p|V )−1◦f(s). This agrees with the deﬁnition of f|[0,si], and it is
continuous on [si,si+1] since it is the composition of continuous maps.
This choice of ~f is unique, as at each step the deﬁnition of ~f on [si,si+1] is forced.
The next theorem says that we can also lift homotopies.
Theorem. Let p : E→ B be a covering map and F : I×I→ B a homotopy with F (0, 0) = b.
Given e∈p−1(b), there exists a unique lift ~F :I×I→E such that ~F (0, 0) =e and p◦ ~F =F .
The proof is analogous to the previous one, where we now use the Lebesgue number lemma to
conclude that there is a small enough subdivision of I×I such that the image of each subrectangle
lies in an evenly covered subset of B.39
Remark. If F is a path homotopy from f to g in B, then ~F is a path homotopy from ~f to~g in E.
In particular, if f and g are path homotopic then the lifts ~f and ~g beginning at e also end at the
same point e′ = ~f(1) =~g(1).
This is an important observation that relates homotopy to path lifting.
39In general, any map from a simply connected space can be lifted to a covering space. We will give a more complete
characterization of lifting and covering spaces later.
78

Loops don’t always lift to loops, however, For example, lifting the loop that goes around the
circle S1 yields a path in R. This will be precisely how we show that such a loop on S1 is not
homotopic to a constant loop.
Given a starting point e0 ∈ p−1(b0), the endpoint of the lift of a loop at b0 is uniquely deter-
mined. Furthermore, path homotopic loops has lifts with the same endpoint. This means there is
a well-deﬁned lifting correspondence ϕ : π1(B,b 0)→ p−1(b0) that sends a homotopy class [ f] to
ϕ([f]) = ~f(1).
The fundamental group of the circle is nontrivial
• Let p : R→S1 be the usual covering map and b0 = (1, 0). If f loops around the circle k
times, then ~f(1) = 2πk. Thus ϕ([f]) = 2πk. We have a map ϕ :π1(S1,b 0)→ 2πZ that
is a surjection. Therefore π1(S1,b 0) is at least as large as Z as a set. We will show that
this is in fact a group homomorphism.
Next time we will show additional properties of the lifting correspondence, namely why it is often
surjective and sometimes injective. We will consider more examples of spaces in algebraic topology
generated via quotients and gluing.
79

11/4/2019 - Fundamental Group of the Circle, Quotients and
Gluing
Recall that given a covering map p : E→ B, any path f : I→ B beginning at f(0) = b can be
lifted uniquely to a path ~f : I→ E beginning at e∈ p−1(b). We also saw that homotopies lift,
which means homotopic paths have homotopic lifts, and in particular the lifts end at the same point.
This implies there is a lifting correspondence ϕ : π1(B,b 0)→ p−1(b0) deﬁned by ϕ([f]) = ~f(1)
well-deﬁned on homotopy classes of loops.
Example
• Consider the usual covering map
p : R→S1
x↦→ (cos 2πx, sin 2πx)
The loop f that goes once clockwise around the circle lifts to a path in R from 0 to 1.
Thus ϕ([f]) = 1. In general, ϕ takes the loop that travels k times around the circle to
k∈ Z.
Lemma. If E is path-connected, then the lifting correspondence ϕ is surjective.
Proof. Letf :I→E be a path frome0∈p−1(b0) to anye∈p−1(b0). Then the projection g =p◦f
is a loop in B based at b0. f is a lift of this loop g, which implies ϕ([g]) =e.
Usually, the lifting correspondence need not be injective. However, given certain conditions on the
covering space E we can guarantee that this correspondence is a bijection.
Proposition. If p : E → B is a covering map and E is simply connected, 40, then the lifting
correspondenceϕ is a bijection.
Proof. ϕ is surjective by the previous lemma. To showϕ is injective, supposeϕ([f]) =ϕ([g]). Then
the lifts ~f and~g has the same endpoint e.
The claim is that ~f and ~g are path-homotopic. ~f∗~g−1 is a loop based at e0, homotopic to
the constant loop. Then
~f≃ ~f∗e≃ ~f∗~g−1∗~g≃e∗~g≃~g
where we are using that ~g−1∗~g≃ e and ~f∗~g−1≃ e0. Let ~F be a homotopy between ~f and ~g.
Then F =p◦ ~F is a path homotopy between f and g, which implies [f] = [g]. So ϕ is injective, as
desired.
Theorem. We have π1(S1)≃ Z as groups.
40This is the universal cover of B.
80

This tells us the group structure on π1(S1) (rather than merely the cardinality).
Proof. Consider the lifting correspondence ϕ :π1(S1, (1, 0))→ R on the covering space R→S1. ϕ
is a bijection by the previous theorem, so it remains to conﬁrm that this map respects composition
in π1(S1, (1, 0)).
Let [f], [g]∈ π1(S1, (1, 0)) with ϕ([f]) = n and ϕ([g]) = m. Then the lifts ~f and ~g beginning
at 0 end at n andm, respectively. Deﬁne h :I→ R byh(s) =n +~g(s). This is the lift of g starting
at n. Since n = ~f(1), we know that ~f∗h is a path in R that is the lift of f∗g beginning at 0 and
ending at n +m. Therefore ϕ([f]∗ [g]) =n +m.
Remark. The same method yields π1(S1×S1)≃ Z× Z.
Gluing and quotients
We will return to some point set topology, 41 as gluing and quotients will be an important source
of examples in algebraic topology.
Examples
• The quotient of the interval [0 , 1] by the equivalence relation 0 ∼ 1 that identiﬁes the
endpoints yields the circle S1.
• The quotient of the square [0, 1]2 by the equivalence relation that identiﬁes (0,t )≃ (1,t )
yields the cylinder [0, 1]×S1. Also gluing along ( s, 0)≃ (s, 1) yields the torus S1×S1.
These constructions are usually best illustrated with a gluing diagram.
The construction that underlies these examples is the quotient topology.
Deﬁnition. Let X be a topological space, A a set, and f : X→ A be a surjective map. 42 The
quotient topology on A is deﬁned by declaring U⊂A open if and only if f−1(U)⊂X is open.
This indeed deﬁnes a topology on A, as unions and intersections behave well with preimages. The
quotient topology is alternatively characterized as the ﬁnest topology on A such that the quotient
map f :X→A is continuous.
Deﬁnition. A map f : X→ Y is a quotient map if f is surjective and U⊂ Y is open if and
only if f−1(U)⊂X is open.
Remark. If f :X→Y is surjective, continuous, and open, then f is a quotient map.
Note that there are quotient maps that are not necessarily open. The deﬁnition only demands
that open sets that are the preimage of sets in Y map to open sets, and it does not constrain the
41‘We are going back in time here and must only be careful not to meet the parents of of the fundamental group.’
(D. Auroux)
42We can also frame this as an equivalence relation ∼ on X by deﬁning f : X → X/∼= A. Conversely, if
f :X→A is surjective, we obtain an equivalence relation on X by declaring x∼x′ if they lie in the same ﬁber.
81

behavior of f on the other open sets of X that do not arise as such a preimage.
Homeomorphisms are another trivial example of quotient maps (in which case the equivalence
relation∼ only identiﬁes x∼x and nothing else).
Example
• We can obtainS1 as [0, 1] with 0 identiﬁed with 1. Explicitly, the equivalence relation is
0∼ 1 with no other distinct points identiﬁed. The equivalence classes of [0 , 1] are{0, 1}
along with{x} for all x∈ (0, 1).
The quotient map f : [0, 1]→ S1 is given by f(t) = (cos 2πt, sin 2πt). f is a quotient
map, but it is not open, as the image of the open set [0 ,ϵ ) is not open in S1.a
a[0,ϵ ) is not a subset that arises as the preimage of any set in S1.
We can use quotients to attach topological spaces together.
Attaching topological spaces
• Let (X1,x 1),..., (Xn,xn) be pointed topological spaces, with each Xi≃ S1. Let A be
the quotient space of the disjoint union ⨆Xi, where the equivalence relation identiﬁes
xi∼xj for all i,j and no other distinct points. Then A is the wedge of n circles .
If A = X/∼ and f : X→ Y is compatible with the equivalence relation, in that x∼ x′ implies
f(x) = f(x′), then f induces a map f :A→Y deﬁned by f([x]) = f(x). Compatibility with the
equivalence relation guarantees this is well-deﬁned. In such a case, we say that f factors through
the quotient.
X Y
A =X/∼
f
f
Although this makes sense from a set-theoretic perspective, we would like our maps in topology to
be continuous as well. Let q :X→X/∼ be the quotient map.
Theorem. If f : X→ Y is continuous and x∼ x′ implies f(x) = f(x′), then the induced map
f : X/∼→ Y is continuous. Conversely, if f is continuous, then the composition f = f◦q is
continuous.
82

Proof. For U ⊂ Y open, we have that f−1(U) = q−1(f
−1
(U))⊂ Y is open. By deﬁnition of
the quotient topology, f
−1
(U) is open, as the inverse image q−1(f−1(U)) is open. Therefore f is
continuous.
Example
• On X = Rn\{ 0}, deﬁne x∼y if and only if x and y lie on the same line through 0. In
other words, x∼ y if and only if x = αy for some nonzero α∈ R. It is not diﬃcult to
see that this is an equivalence relation.
The quotient space X/∼= RPn−1 is real projective space of dimension n− 1.a A contin-
uous map f : RPn−1→Y is the same as a continuous map f : Rn\{ 0}→ Y such that
f(αx) =f(x) for all α∈ R\{ 0}.
• Let X = [0, 1]× [0, 1]. Let
A ={0}× [0, 1] ={(0,y ) :y∈ [0, 1]}
A′ ={1}× [0, 1] ={(1,y ) :y∈ [0, 1]}
B = [0, 1]×{ 0} ={(x, 0) :x∈ [0, 1]}
B′ = [0, 1]×{ 1} ={(x, 1) :x∈ [0, 1]}
– Glue A to A′ by the equivalence relation (0,t )∼ (1,t ) to obtain the cylinder S1×
[0, 1].
– We can also glue A to A′ by the equivalence relation (0,t )∼ (1, 1−t). This yields
the M¨ obius strip.
– Glue A to A′ by (0,t )∼ (1,t ) and B to B′ by (s, 0)∼ (s, 1) to obtain the torus.
– GlueA toA′ by (0,t )∼ (1,t ) and B toB′ by (s, 0)∼ (1−s, 1) to obtain the Klein
83

bottle.
– Glue A to A′ by (0,t )∼ (1, 1−t) and B to B′ by (s, 0)∼ (1−s, 1) to obtain the
real projective plane RP2.
aThere is an important connection between the sphere and real projective space. One can construct the
sphere as a quotient of Rn\{ 0} by the same equivalence relation, except restricting scalar multiplication to
positive real numbers.
84

11/6/2019 - The Brouwer Fixed Point Theorem
Today we will discuss two applications of the resultπ1(S1) = Z. Both of these are, in some sense, 2-
dimensional generalizations of the intermediate value theorem. For example, consider the following
two results.
Theorem. Every continuous map f :I→I has a ﬁxed point, namely there exists x∈I such that
f(x) =x.
This follows from the intermediate value theorem applied to the function g(x) = f(x)−x. This
generalizes to the Brouwer ﬁxed point theorem.
Theorem. Every continuous map f :S1→ R has a point x∈S1 such that f(x) =f(−x).
This follows from the intermediate value theorem applied to the function g(x) = f(x)−f(−x).
This generalizes to the Borsuk-Ulam theorem.
Brouwer ﬁxed point theorem
Let Bn be the closed ball of radius 1 in Rn. Then ∂Bn =Sn−1. The Brouwer ﬁxed point theorem
is the following result.
Theorem. Let f :Bn→Bn be a continuous map. Then f has a ﬁxed point, namely there exists
x∈Bn with f(x) =x.
This general result requires techniques of higher homotopy or homology. We will be able to prove
the result in dimension 2.
Theorem. Let f : B2→ B2 be a continuous map. Then f has a ﬁxed point, namely there exists
x∈B2 with f(x) =x.
Recall the notion of a retraction.
Deﬁnition. LetA⊂X be a subset. A continuous map r :X→A is a retraction if r|A :A→A
is the identity.
The theorem that provides the bridge to the Brouwer ﬁxed point theorem is the following result.
Theorem. There does not exist a retraction r :B2→S1.
In general, a retraction induces a surjective map on fundamental groups, but we can present a more
concrete proof as well.
Proof. Let r : B2→ S1 be a retraction. If f is a loop in S1, then f is a loop in B2. B2⊂ R2 is
convex, so f is homotopy equivalent to a constant loop. Let F :I×I→B2 be such a homotopy.
Then the composition r◦F : I×I → S1 is a homotopy from f to the constant loop. This is
impossible whenever [f] is nontrivial in π1(S1) = Z.
85

The higher dimensional analogue of this intermediate theorem is the nonexistence of a retraction
Bn→Sn−1. We can use this to prove the ﬁxed point theorem.
Proof. Suppose for contradiction there exists f : B2→ B2 with f(x)⁄= x for all x∈ B2. Then
deﬁne F :B2→S1 by letting F (x) be the intersection of the line through f(x) and x and S1.
More explicitly, we have that
F (x) =x +t(x−f(x))
where t is the positive root of the quadratic equation
1 =‖x +t(x−f(x))‖2
which depends onx continuously by the quadratic formula. Thus we have a retractionF :B2→S1,
which is a contradiction.
Given the intermediary theorem, the same argument implies that any map Bn→ Bn has a ﬁxed
point.
We will develop a bit more theory that will help us understand why this argument worked. The
following is a characterization of topologically trivial maps S1→X.
Theorem. Leth :S1→X be continuous. The following are equivalent.
1. h is nullhomotopic, namely h is homotopic to a constant map.
2. h extends to a continuous map ~k :B2→X such that k|S1 =h.
3. The induced h∗ :π1(S1)→π1(X) is trivial.
Proof. Let H :S1×I→X be a homotopy between h and a constant map. π :S1×I→B2 given
byπ(x,t ) = (1−t)x is a quotient map and yields a homeomorphism
(
S1×I/(x, 1)∼ (x′, 1)
)
≃B2.
H|S1×{1} is constant, and thus H factors though the quotient H : B2→ X with H|S1×{0} = h.
Then k =H is the desired extension.
86

Let h : k|S1 → X be a map, where k : B2→ X. We can write h = k◦i and use the functo-
riality of π1 for
S1 B2 X
π1(S1) π1(B2) = 0 π1(X)
h
i k
h∗
i∗ k∗
which implies h∗ is trivial.
Finally, assume the induced h∗ : π1(S1,b 0)→ π1(X,x 0) is trivial. Let f : I → S1 be the loop
f(s) = (cos 2πs, sin 2πs), whose homotopy class generates π1(S1). f is also a quotient map and
yields and homeomorphism
(
[0, 1]/0∼ 1
)
≃ S1. Deﬁne g = h◦f : I→ X. g is a loop in ( X,x 0)
representing the image h∗(f). There exists a path homotopy G :I×I→X fromg to the constant
path atx0. There is a quotient map F :I×I→S1×I given byF (s,t ) = (f(s),t ), and it identiﬁes
(0,t )∼ (1,t ). G respects this relation and descends to a map G :S1×I→X. This is the desired
homotopy.
Corollary. The identity S1→S1 is not nullhomotopic, as the induced map of fundamental groups
is the identity π1(S1)→π1(S1). In other words, S1 is not contractible.
Corollary. There are no retractionsB2→S1, as a retraction is merely the extension of the identity
on S1 to all of B2.
Corollary. The inclusion i : S1 ↪→ R2\{ 0} is not nullhomotopic, as there is a retraction r :
R2\{ 0}→ S1 given by r(x) = x/‖x‖. Since id π1(S1) = r∗◦i∗ implies i∗ is injective, the lemma
implies i is not nullhomotopic.
The lemma packages the relationship between homotopy and extension into one result.
We are now poised to oﬀer a diﬀerent, perhaps more intuitive proof of the ﬁxed point theorem.
Proof. Suppose for contradiction f : B2 → B2 has no ﬁxed points. Deﬁne g : B2 → R\{ 0}
by g(x) = x−f(x). The restriction g|S1 is a continuous map that extends to B2, and is hence
nullhomotopic by the lemma. On the other hand, we also claim it is homotopic to the inclusion
i :S1↪→ R2\{ 0}.
Forx∈S1, we have that x−f(x)∈B1(x)\{ 0}, which is a convex subset of R2. The straight line
homotopyG(x,t ) =x− (1−t)f(x) doesn’t intersect the origin. This is a contradiction, so f has a
ﬁxed point.
We will state the Borsuk-Ulam theorem in dimension 2.
Theorem. Letf :S2→ R2 be a continuous map. Then there exists x∈S2 such thatf(x) =f(−x).
87

11/11/2019 - Antipodes and the Borsuk-Ulam Theorem
We spent some time last lecture proving the following result.
Theorem. The following are equivalent.
1. The map h :S1→X is nullhomotopic.
2. h :S1→X extends to a map h :B2→X.
3. The induced homomorphism h∗ :π1(S1,b 0)→π1(X,x 0) is trivial.
We saw that this result implies there is no retraction fromB2 toS1. Brouwer’s ﬁxed point theorem,
which says that every map f : B2→ B2 admits a ﬁxed point f(x) = x, then follows from this
corollary.
The Borsuk-Ulam theorem is a result of a similar ﬂavor.
Theorem. Letf :S2→ R2 be continuous. Then there exists x∈S2 such that f(x) =f(−x).
An analogous result holds for maps on the n-sphere Sn→ Rn, but this requires more homotopy
theory to prove. The case when n = 1 can be proven with the intermediate value theorem.
Deﬁnition. The antipode of x∈Sn is−x∈Sn. A map h :Sn→Sn is antipode-preserving
if h(−x) =−h(x).
Example
• The rotation of S1 by an angle θ is antipode-preserving.
The follow result says something about the homotopy class of an antipode preserving map on the
sphere.43
Theorem. If h :S1→S1 is continuous and antipode-preserving, then h is not nullhomotopic.
Proof. We will show that the induced h∗ : π1(S1)→ π1(S1) is nontrivial. If [ g]∈ π1(S1) is a
generator, h∗ takes [g] to an odd multiple of [ g].
Let α : S1→ S1 be the antipodal map α(x) = −x. The semicircle path f : I → S1 given by
f(s) = (cosπs, sinπs) goes from b0 to−b0. Then g = f∗ (α◦f). Now, h◦f : I→ S1 is a path
fromh(b0) to h(−b0) =−h(b0) and h◦ (α◦f) =α◦h◦f is a path from−h(b0) to h(b0) (as h and
α commute by assumption). The goal will then be to show h∗(g) = (h◦f)∗ (α◦h◦f).
Letp : R→S1 be the usual covering map of the circle. Choose a lift t0 ofh(b0). The lift k ofh◦f
starting at t0 ends at a point of p−1(−h(b0)) =t0 + 1/2 +Z. Let t0 + 1/2 +n be the endpoint. The
43We present a concrete proof for the case n = 1. There is a more abstract proof in Munkres that generalizes this
to other dimensions, using the fact that Sn is the two-fold cover of projective space RPn.
88

lift ofα◦h◦f starting att0 + 1/2 +n is then𝓁 :I→ R deﬁned by𝓁(s) =k(s) + 1/2 +n. This ends
at (t0 + 1/2 +n) + 1/2 +n =t0 + (2n + 1). Then k∗𝓁 :I→ R is the lift of h◦g =h◦f∗ (α◦h◦f).
It begins at t0 and ends at t0 + 2n + 1, which implies h∗([g]) is nontrivial.
Corollary. There is no continuous antipode-preserving map g :S2→S1.
Proof. Suppose for contradiction there exists such a g : S2→ S1. By embedding S1⊂ S2 as the
equator, we can view g as a map S2→S2. Since g is not surjective (its image lies on the equator),
g is nullhomotopic.
More explicitly, we can consider the restriction g|S1 → S2. g|S1 extends to a map of the disc
B2 by embedding the disc as the upper hemisphere of Sn.
We can now prove the Borsuk-Ulam theorem in dimension 2.
Theorem. Letf :S2→ R2 be continuous. Then there exists x∈S2 such that f(x) =f(−x).
Proof. Suppose for contradiction there exists a f : S2 → R2 such that f(x)⁄=−f(−x) for all
x∈S2. Deﬁne g :S2→S1 by
g(x) = f(x)−f(−x)
‖f(x)−f(−x)‖
g is clearly antipode-preserving, which is a contradiction.
A corollary is the invariance of domain when n = 2.
Corollary. An open set in R2 is not homeomorphic to an open set of Rn, where n≥ 3.
Invariance of domain in dimension 1 is easy, as an open set of R1 can be separated removing a
point, while open sets of Rn with n≥ 2 cannot be disconnected by removing a single point. 44
Proof. Let U ⊂ Rn be open, with n≥ 3. Suppose for contradiction there is a homeomorphism
f : U → V ⊂ R2. There is a closed ball Br(x)⊂ U for small r > 0, on which the boundary
f :S2→ R2 is continuous and injective, which contradicts Borsuk-Ulam theorem.
There is another amusing application of the Borsuk-Ulam. Given a suﬃciently nice bounded subset
A⊂ R2, there exists a straight line in R2 that bisectsA into two pieces of equal area. The following
theorem generalizes this.
Theorem. Given suﬃciently nice 45 bounded subsetsA1,A 2⊂ R2, there exists a straight line in R2
that simultaneously bisects both A1 to A2 into two pieces of equal area.
44The general result can be proven using homology.
45These subsets should be measurable.
89

Proof. View A1 and A2 as lying in the plane R2×{ 1}⊂ R3. Given a point u∈ S2⊂ R3, let
P⊂ R3 be a plane through the origin with normal vector u. P dividesS3 into two half-spaces. For
all but the two vertical choices for u, P divides the plane R2×{ 1} into two pieces.46 Deﬁne fi(u)
to be the area of the part of Ai that lies on the side of the normal vector u.
The functions f1,f 2 : S2→ R, are continuous and yield a continuous map ( f1,f 2) : S2→ R2.
Furthermore, we clearly have fi(u) +fi(−u) = Area(Ai). The Borsuk-Ulam implies there exists
u∈S2 such that fi(−u) =fi(u) = Area(Ai)/2.
Again, there is a generalization of this result ton bounded, measurable regions in Rn. There exists a
hyperplane cut that simultaneously bisects all these regions. When n = 3, this is the ham-sandwich
theorem, as it says that two pieces of bread and a slice of ham can be simultaneously bisected by
a single hyperplane. 47
46Here we are cleverly parameterizing the possible cuts of the plane R2×{ 1} via the sphere. If a line is of the form
ax +by +c = 0, we can normalize the vector ( a,b,c ) to obtain a parameterized family of lines in the plane. This is
the above construction.
47A physicist’s proof of this would be to consider the centers of mass of each of the three objects and then take the
hyperplane that intersects these three points.
90

11/13/2019 - Deformation Retracts and Homotopy Equivalence
Today we will discuss deformation retracts and homotopy equivalence. We have seen that spaces
that are homeomorphic share many topological properties, but it turns out that often spaces look
very much alike without being precisely homeomorphic.
Recall that given a subspace A ⊂ X, a retraction is a continuous r : X → A such that the
restriction r|A acts as the identity on A. In other words, if i : A ↪→ X is the inclusion that
r◦i = idA.
Example
• The constant map S1→p to a point p∈S1 is a retraction.
• Consider the unit sphere Sn. Then Sn admits a retraction Sn → H onto the upper
hemisphere H ={xn+1≥ 0} given by (x1,...,x n+1)↦→ (x1,..., |xn+1|).
• There is a retraction R2\{ 0}→ S1 given by x↦→x/‖x‖.
• There is a retraction from the M¨ obius band onto its core circleS1 obtained by projecting
I×I/∼ to the ﬁrst coordinate.
The second two examples are diﬀerent from the ﬁrst two, as one would like to argue that R2\{ 0}
and S1 are the same in a way more fundamental then S1 and p are. Namely, all of the homotopy
information of R2\{ 0} is the same as that of S1.
The idea is that it is possible to continuously deform the identity map on R2\{ 0} to the retraction
r : R2\{ 0}→ S1. In other words, the identity map is homotopic to the retraction.
Example
• Consider again the M¨ obius bandX = I×I/(0,y )∼ (1, 1−y) and the subspace A =
I×{ 1/2}/(0, 1/2)∼ (1, 1/2). Deﬁne the homotopy
H :X×I→X
([x,y ],t )↦→ [x,t 1
2 + (1−t)y]
The deﬁnition ((x,y ),t )↦→ (x,t/ 2 + (1−t)y) is compatible with the equivalence relation
∼, so H descends to a homotopy of the quotient.
Deﬁnition. A subspace A⊂ X is a deformation retract of X if idX is homotopic to a map
X → A such that the points of A are ﬁxed throughout the homotopy. Explicitly, there exists a
continuousH×I→X such that
• H(x, 0) =x for all x∈X
• H(x, 1)∈A for all x∈X
• H(a,t ) =a for all a∈A and all t
91

H is a deformation retraction.
Given a deformation retractionH, there is a retractionr :X→A given by deﬁningr(x) =H(x, 1).
So being a deformation retract is a stronger condition than being merely a retract.
A deformation retract can also be stated as a retraction r : X→ A along with a homotopy H
between idX and r that ﬁxes points of A.
Example
• The retraction r : Rn\{ 0}→ Sn−1 given by x↦→x/‖x‖ is homotopic to the identity on
Rn\{ 0} via the straight line homotopy. Deﬁne
H :X×I→X
(x,t )↦→t x
‖x‖ + (1−t)x
The straight line segment from x to x/‖x‖ does not pass through the origin, so this is
well-deﬁned. H also ﬁxes Sn−1 throughout the homotopy.
The existence of a deformation retract allows us to say something about the homotopy of a space
relative to its subspace. We’ve seen that ifA is a retract ofX, then the inducedi∗ :π1(A)→π1(X)
is injective and the induced r∗ :π1(X)→π1(A) is surjective. 48 When A is a deformation retract,
this will become isomorphisms.
Proposition. Supposeh,k : (X,x 0)→ (Y,y 0) are homotopic with the property that the homotopy
preserves the base point. Then h∗ =k∗.
Proof. Let f be a loop in (X,x 0). Then
I×I (X,x 0)×I (Y,y 0)
f×id H
is a path homotopy between h◦f andk◦f. Since the homotopy H holds the base point constant,
we know that this composition indeed deﬁnes a path homotopy that ﬁxes endpoints.
What happens in the base point during the homotopy does not stay ﬁxed? If h,k : X→ Y are
homotopic with homotopy H but yt =H(x0,t ) is not constant, let α(t) =yt be a path from y0 to
y1. We cannot say that h∗ and k∗ are equal, as they are maps to diﬀerent groups:
h∗ :π1(X,x 0)→π1(Y,y 0)
k∗ :π1(X,x 0)→π1(Y,y 1)
There is an isomorphism between the two codomains induced by the path α deﬁned by
ˆα :π1(Y,y 0)→π1(Y,y 1)
[g]↦→ [α−1∗g∗α]
Then the correct conclusion is the following.
48As if r◦i =idA, then r∗◦i∗ =id∗
π1(A), which implies i∗ is injective and r∗ is surjective.
92

Theorem. Given the above conditions, we have a commutative diagram
π1(X,x 0) π1(Y,y 0)
π1(Y,y 1)
h∗
k∗
ˆα
Proof. Let F :I×I→X×I be a path homotopy of loops based at ( x0, 1) obtained by
• (x0, 1)↦→ (x0,t )
• f in X×{t}
• (x0,t )↦→ (x0, 1)
Now we can prove the following theorem.
Theorem. If A⊂X is a deformation retract, then the inclusion i : (A,x 0)→ (X,x 0) induces an
isomorphism on fundamental groups.
Proof. Let r : X→ A be a retraction and H be a homotopy between id X and i◦r. As usual,
the induced i∗ is injective. And since i◦r is homotopic to the identity, by the above proposition
i∗◦r∗ =idπ1(X), so i∗ is also surjective.
In conclusion, we don’t need that two maps compose to the identity in order to induce an isomor-
phism on homotopy. It suﬃces that their composition is homotopic to the identity.
Example
• S1 has the same fundamental group as the cylinder S1×I, the M¨ obius bandI×I/∼,
the punctured plane R2\{ 0}, the solid torus S1×B2.
• The ﬁgure eight space (wedge of two circlesS1∨S1) is a deformation retract ofR2\{1,−1}.
Theθ-grapha is also a deformation retract of R2\{1,−1}. All three spaces have the same
fundamental group, although the θ-graph and S1∨S1 are not deformation retracts of
each other.
aIt looks like a θ in the plane.
The second example illustrates that there is a more general relation between spaces than deforma-
tion retract. In fact, since we noticed that it suﬃces for i◦r to be homotopic to the identity, we
might as well also allowr◦i to be homotopic to the identity, rather than demanding strict equality.
Deﬁnition. Letf :X→Y andg :Y →X be continuous maps. If g◦f :X→X andf◦g :Y →Y
are both homotopic to the identity, then f and g are homotopy equivalences. In such a case, X
and Y are homotopy equivalent. We say X and Y have the same homotopy type.
93

Spaces of the same homotopy type are indistinguishable in algebraic topology.
Example
• If A is a deformation retract of X, then A and X have the same homotopy type and
i :A↪→X and r :X→A are homotopy equivalences.
• The inclusion of the θ-graph into R2\{ 1,−1} and then the retraction onto S1∨S1 is a
homotopy equivalence between the θ-graph and S1∨S1. This is a particular case of the
following proposition.
Proposition. If f : X→ Y and g : Y → Z are homotopy equivalences, then g◦f : X→ Z is a
homotopy equivalence.
A homotopy inverse of g◦f is obtained by composing inverses for f and g in the opposite order.
Theorem. Let f : (X,x 0)→ (Y,y 0) be a homotopy equivalence. The induced f∗ : π1(X,x 0)→
π1(Y,y 0) is an isomorphism.
The proof is similar to the case of deformation retracts with some additional details.
Proof. Let g :Y →X be a homotopy inverse to f with g(y0) =x1∈X. There is a composition
π1(X,x 0) π1(Y,y 0) π1(X,x 1) π1(Y,y 1)
f∗ g∗ f′
∗
We know g◦f is homotopic to id X, so g∗◦f∗ = ˆα◦idπ1(X,x0) where α is the path from x0 to x1
that arises from the homotopy from id X to g◦f. This implies f∗ is injective and g∗ is surjective.
f◦g is homotopic to the identity, so f′
∗◦g∗ i an isomorphism π1(Y,y 0)→π1(Y,y 1). This implies
g∗ is injective and f′
∗ is surjective. Thus g∗ is an isomorphism, which completes the proof. 49
49This means that π1 : Top→ Grp descends to a functor HoTop→ Grp.
94

11/18/2019 - Computing the Fundamental Group
Broadly, we are attempting to develop tools to understand homotopy theory , which studies the
space of maps between two spaces. We are focusing on the maps between the circle and and space,
which is fundamental group.
Last lecture we introduced homotopy equivalence, which gives a more general notion of ‘same-
ness’ for topological spaces. Homotopy equivalence is one way of determining when two spaces
have the same fundamental group. Last group we proved the following result.
Lemma. Let f : X → Y be a homotopy equivalence. Then the induced map f∗ : π1(X,x 0)→
π1(Y,y 0) is an isomorphism.
So homotopy classes of maps from S1 to X and to Y behave the same way. In fact, homotopy
classes of maps from any spaces into X and Y behave the same way. We will present a simpliﬁed,
shorter proof of this result in a special case.
Proof. Supposef :X→Y is a homotopy equivalence that takesf(x0) =y0. Assume the homotopy
inverseg :Y →X takesg(y0) =x0 and the homotopies preserve basepoints. 50 Then we have
π1(X,x 0) π1(Y,y 0) π1(X,x 0)
(g◦f )∗=id∗
Then a homotopy betweeng◦f and id yields, for all loopsh :I→X, a homotopy between (g◦f)◦h
and h.
This result gives access to many examples of spaces and their fundamental groups.
Example
• Let A⊂ X be a deformation retract. Then the inclusion i : A ↪→ X and retraction
r :X→A are homotopy equivalences, so π1(X)≃π(A).
Thus the cylinder S1×I, the M¨ obius bandI×I/(0,y )∼ (0, 1−y), and the punc-
tured plane R2\{ 0}.
Note that if two spaces have the same fundamental group, they are not necessarily homotopy-
equivalent. An easy example is the sphere S2 and the point, although we don’t have a way to show
this.
The rest of the course will consist of studying ways to compute fundamental groups as well as
what these have to tell us about homotopy theory.
50The lack of these assumptions is what makes the proof trickier in the general case.
95

Given a decomposition X = U∪V into open subsets for which we know π1(U) and π1(V ), what
can we say about π1(X)? For example, we can split Sn into two hemispheres for which we know
their fundamental groups. Can this tell us anything about the fundamental group of Sn?
Another example is the ﬁgure-eight spaceS1∨S1. There are open subsets that consist of each copy
ofS1 and a bit of extra material. We know each of these is homotopy equivalent toS1. So we know
the fundamental group of the pieces. Do we know anything about the fundamental group ofS1∨S1?
There is a general answer to this question, the Seifert van Kampen theorem. For simplicity, we will
ﬁrst present a simpler version of the result.
Theorem. SupposeX =U∪V , with U,V open and U∩V path-connected. Letx0∈U∩V be the
basepoint, and leti :U ↪→X andj :V ↪→X be the inclusion maps. Then the images of the induced
homomorphisms i∗ :π1(U,x 0)→π1(X,x 0) and j∗ :π1(V,x 0)→π1(X,x 0) generateπ1(X,x 0).
When we say that a collection of elements generates a group, this means that the smallest subgroup
that contains these elements is in fact the entire group. More concretely, every element ofπ1(X,x 0)
can be expressed as the product of elements of the subgroups im i∗ and imj∗. This doesn’t mean
that every loop in X lies in either U or V , but instead that we can express any such loop as the
product of loops that lie in either U or V .
Proof. Let f : I → X be a loop based at x0. We can pullback the open cover for a cover
[0, 1] = f−1(U)∪f−1(V ). By the Lebesgue number lemma, there exists δ > 0 such that for
any subinterval of [0 , 1] of length less than δ, this subinterval lies completely in either f−1(U)
or f−1(V ). Then we can consider a ﬁnite subdivision 0 = a0 < a1 < ... < an = 1 such that
f([ai,ai+1]) lies in either U or V . Without loss of generality, by combining subintervals if neces-
sary, we can take these subintervals such that f([ai,ai+1]) alternates between lying in U and V .
Let fi = f|[ai−1,ai]. Since the image of the subintervals [ ai−1,ai] alternates between lying in U
and V , we know f(ai)∈U∩V for all i. Choose a path αi in U∩V from x0 to f(ai), and let α0
and αn be constant paths at x0. Then
f≃ (α0∗f1∗α−1
1 )∗ (α1∗f2∗α−1
2 )∗... ∗ (αn−1∗fn∗α−1
n )
where each αi−1∗fi∗α−1
i is a loop at x0 contained in either U or V .
Corollary. SupposeX =U∪V , with U,V open and simply connected and U∩V path connected.
Then X is simply connected.
Proof. π1(X) is generated by the images of trivial groups, so π1(X) is itself trivial.
Corollary. When n≥ 2, π1(Sn) ={1}.
Proof. Let Sn = U∪V , where U = Sn\{ (0, 0,..., 1)} and V = Sn\{ (0, 0,..., −1)}. The claim
is that U and V are both homeomorphic to Rn. We can use stereographic projection. Place Sn in
Rn+1 such that Rn×{ 0}⊂ Rn+1 intersects Sn along the equator. Then for a point Z∈ U, take
96

the unique line through N and Z. Then deﬁne f :U→ Rn by taking z =f(Z) to be the unique
intersection of this line and Rn×{ 0}⊂ Rn+1.
The formula is
f(z1,...,z n+1) =
( z1
1−zn+1
,..., zn
1−zn+1
)
Hence U and V are simply connected. Since U∩V ≃ Rn\{ 0} by the same technique 51 if n≥ 2,
the theorem implies π1(Sn) ={1}.
Computing the fundamental group of projective space
• The quotient of Sn by the relation∼ deﬁned by x∼−x is homeomorphic to RPn. The
map p :Sn→Sn/∼≃ RP 2 is a covering map of degree 2.
SinceSn is path connected and simply connected, the lifting correspondenceϕ :π1(RPn)→
p−1(b0) is a bijection. The ﬁbers of p have cardinality 2, which implies that π1(RP 2)≃
Z/2Z is the unique group of order 2.
• Consider the ﬁgure-eight space S1∨S1 with the cover S1∨S1 =U∪V , where U andV
each consist of a circle and a bit extra to make U and V open.
Then π1(S1∨S1) is generated by images of the two maps Z→π1(X), so every element
ofπ1(X) can be expressed as the product of a loops and b loops. However, we do not yet
know whether or not there are relations between the homotopy classes of [ a] and [b]. In
turns out the there will be no such relations, which implies that π1(X) is the free group
on two generators .
However, we can prove thatπ1(X) is not abelian, namely ab⁄=ba. We can cover S1∨S1
51In fact, U∩V is homotopy equivalent toSn−1, which can be used to construct an induction number to compute
the higher homotopy and homology of spheres in algebraic topology.
97

by the following construction
Beginning at the origin, the lift of the loop a∗b ends at 1× 0. The lift of b∗a ends at
0× 1. Since a∗b and b∗a lift to diﬀerent points and are not path homotopic, they are
not homotopic in S1∨S1.
Note that this cover cannot distinguish between a∗b∗a−1 and b∗a∗b−1.
The above example illustrates that a deeper understanding of covering spaces could shed light on
the fundamental group.
98

11/20/2019 - Equivalence of Covering Spaces and the Universal
Cover
We will next explore a classiﬁcation of covering spaces of a space. This will help us understand the
fundamental group.
Classiﬁcation of covering spaces
Let p : (E,e 0)→ (B,b 0) be a covering map. Assume E and B are path connected. What is the
relationship between π1(E,e 0) and π1(B,b 0)? Given this answer, we can develop a theory as to
whether or not a space E coversB.
Proposition. The homomorphismp∗ :π1(E,e 0)→π1(B,b 0) induced by a covering mapp :E→B
is injective.
Proof. Since p∗ is a group homomorphism, it suﬃces to check that the preimage of the identity is
the identity. Suppose p∗([f]) = eb0 for [f]∈ π1(E,e 0). Then [ f◦p] is homotopic to the constant
loop. f is a lift of f◦p, and we can lift this homotopy to a homotopy from f to the constant loop
in E.
Therefore every covering p : E→B with a choice of base points ( E,e 0) and (B,b 0) yields a sub-
group H =p∗(π1(E,e 0))⊂π1(B,b 0) that is isomorphic to π1(E,e 0).
This will lead to two key results.
1. The subgroup H⊂π1(B,b 0) determines the covering space up to equivalence. In other words,
all the information about a covering space is encoded in this subgroup.
2. Given a suﬃciently nice 52 space B, for every subgroup H⊂π1(B,b 0) there exists a covering
space p :E→B with H =p∗(π1(E,e 0)).
Deﬁnition. Let p : E→ B and p′ : E′→ B be covering spaces. E and E′ are equivalent as
covering spaces of B if there exists a homeomorphism h :E→E′ such that p =p′◦h.
E E
B
h
p p′
The condition p =p′◦h says that h should map E to E′ in a way that respects their structure as
covering spaces ofB. For all b∈B,h gives a bijectionp−1(b)→p′−1(b) that varies continuously as
b changes. In other words, h takes sheets of one covering to another covering in a consistent way.
52B should be path connected, locally path connected, and semi-locally simply connected (this means that every
neighborhood of any point contains a neighborhood for which the inclusion into B induces the trivail homomorphism
of fundamental groups.
99

Example
• There are two coverings of S1 given by
p : R→S1
x↦→ (cosx, sinx)
p′ : R→S1
x↦→ (cos(2πx), sin(2πx))
Then these coverings are equivalent by the homomorphism h : R→ R deﬁned by h(x) =
2πx.
The goal today will be to prove the following result.
Theorem. If E→B and E′→B are two coverings of B that correspond to the same subgroup of
π1(B,b 0), then E and E′ are equivalent.
To prove this, we will need to be able to lifts maps to a covering space more generally.
Deﬁnition. A spaceX is locally path connected if for all x∈X and all open U⊂X containing
x, there exists an open V ⊂X containingx such that U∩V is path connected.
Example
• The union of two disjoint discs is locally path connected, but it is not path connected.
• The collection of points {1/n :n∈ N}∪{ 0} is not path connected and not locally path
connected, as no neighborhood of 0 does not contain another point in the set.
• The space (⋃
n∈N
{1/n}× R
)
∪ (0× R)∪ (R× 0)
is path connected, but it is not locally path connected.
Lemma. Letp :E→B be a covering. A loop f in (B,b 0) lifts to a loop in (E,e 0) if and only if
[f]∈p∗(π1(E,e 0))⊂π1(B,b 0).
Proof. Let f be such a loop in ( B,b 0), and let ~f be its lift in ( E,e 0) that is a loop. By deﬁnition
p◦ ~f =f, so p∗([~f]) = [f].
Now suppose [ f] = p∗([~g]) for some loop ~g in (E,e 0). Then f and g = p◦~g are path homo-
topic. Lifting this path homotopy yields a path homotopy between ~f and~g. Since ~g is a loop, ~f is
a loop as well.
We can now prove a lifting lemma that will be very useful in the theory of covering spaces.
100

Theorem. Let p : E → B be a covering map with p(e0) = b0. Let Y be path connected and
locally path connected. Let f : (Y,y 0)→ (B,b 0) be a continuous map. Then f can be lifted to
~f : Y → E such that ~f(y0) = e0 if and only if f∗(π1(Y,y 0)) ⊂ p∗(π1(E,e 0)) as subgroups of
π1(B,b 0). Furthermore, such a lift of f, if it exists, is unique.
(E,e 0)
(Y,y 0) (B,b 0)
p
f
~f
This theorem is a complete characterization of obstructions to lifting maps to the covering space.
Proof. Suppose f admits a lift to ~f :Y →E. Then f =p◦ ~f, and by functoriality of π1 we have
the diagram
π1(E,e 0)
π1(Y,y 0) π1(B,b 0)
p∗
f∗
~f∗
which immediately implies that the image of f∗ lies in the image of p∗.
Conversely, suppose f∗(π1(Y,y 0))⊂ p∗(π1(E,e 0)). Let y1∈ Y and let α be a path from y0 to
y1. Lift f◦α :I→B to a path in E starting at e0. Then deﬁne ~f(y1) to be the endpoint of this
path. We must show that the resulting function ~f is both well-deﬁned and continuous. Note that
if a lift ~f exists, then it is unique. For any y1∈Y , a path from f(y0) to f(y1) lifts uniquely to E
and hence determines ~f(y1).
We ﬁrst show that this is well-deﬁned. Let β be another path from y0 to y1. Then α∗β−1 is
a loop in ( Y,y 0), and f◦ (α∗β−1) = ( f◦α)∗ (f◦β−1) is a loop in ( B,b 0). By assumption
f∗([α∗β−1])∈p∗(π1(E,e 0)), so the lemma implies that f∗([α∗β−1]) lifts to a loop in ( E,e 0).
f◦α lifts to a path beginning at e0 at ending at ~f(y1), and ( f◦β)−1 lifts to a path begin-
ning at ~f(y1) and ending at e0. Therefore f◦β lifts to a path beginning at e0 and ending at ~f(y10,
which shows that ~f(y1) is independent of the choice of path.
Finally, we show that ~f is continuous. It is enough to check ~f is continuous on a neighborhood of
each y1∈ Y . Let U be a neighborhood of f(y1)∈ B. Since Y is locally path connected, there is
a neighborhood W of y1 with W ⊂ f−1(U). Let V denote the slice of E containing ~f(y1). The
restriction p|V :V →U is a homeomorphism. Any point of f(W ) is connected to f(y1) via a path
in U. Lifting this path to V starting at ~f(y1) is obtained by the inverse (p|V )−1. So
~f|W = (p|V )−1◦f
101

which is the composition of continuous functions.
Theorem. Let p :E→B and p′ :E′→B be covering spaces, with p(e0) = p′(e′
0) = b0. Suppose
E,E′, and B are all path connected and locally path connected. Then there is an equivalence of
covering spaces h : E→ E′ such that h(e0) = e′
0 if and only if the subgroups H = p∗(π1(E,e 0))
and H′ = p′
∗(π1(E′,e′
0)) of π1(B,b 0) are equal. Furthermore, if such an equivalence exists then it
is unique.
Proof. If such an equivalence exists, by functoriality of h we have
π1(E,e 0) π1(E′,e′
0)
π1(B,b 0)
h∗
p∗ p′
∗
Now suppose H =H′. By the lifting lemma, there exist basepoint-preserving lifts
E
E′
E B
p
p′
k
h
p
So k◦h is a lift of p : E→ B. However, the identity map id: E→ E is also a lift of p, so by
uniqueness of lifts k◦h = id. A similar argument shows h◦k = id, which proves that h :E→E′
is indeed a homeomorphism.
Classifying covering spaces of the circle
• There is the k-sheeted coveringpk :S1→S1 given bypk(z) =zk, viewing S1⊂ C as the
102

subset of complex numbers with norm 1. Then the map
(pk)∗ :π1(S1,e 0)≃ Z→ Z≃π1(S1,b 0)
is multiplication by k, and the subgroup corresponding to pk is kZ.
• The usual covering map p0 : R→S1 corresponds to the trivial subgroup {0}⊂ Z.
• These are all of the subgroups of Z, so every connected covering space of S1 is equivalent
to either S1 under pk or R.
Next time we will discuss how allowing the basepoint of the covering space to change aﬀects this
theorem. We will also deﬁne the universal cover, which is the covering space corresponding to the
trivial subgroup.
103

11/25/2019 - Universal Covering Spaces, Free Groups
Let p :E→B be a covering map. Recall that we obtain a subgroup
H =p∗(π1(E,e 0))⊂π1(B,b 0)
that consists of loops in ( B,b 0) that lift to loops in ( E,e 0). We proved the following classiﬁcation
of covering spaces using the lifting lemma.
Theorem. Let p : E→ B and p′ : E′→ B be covering maps with E,E′,B path connected and
p(e0) =p′(e′
0) =b0. There is an equivalence
E E′
B
p
h
p′
such that h(e0) =e′
0 if and only if the induced subgroups H and H′ are equal.
What if we do not require h(e0) = e′
0? In general, adjusting the basepoint of the cover changes
the induced subgroup of π1(B,b 0). This is because choosing a new basepoint in the covering space
adjusts the fundamental group by conjugation.
Let e0,e 1∈ p−1(b0). Given a path ~α in E from e0 to e1, α = p◦~α is a loop in ( B,b 0). The
induced isomorphism is
~α∗ :π1(E,e 0)→π1(E,e 1)
[h]↦→ [~α−1∗h∗~α]
Then the corresponding subgroups of π1(B,b 0) are related by
p∗◦~α∗ :p∗(π1(E,e 0)) =H−→H′ =p∗(π1(E,e 1))
[h]↦−→p∗([~α−1∗h∗~α]) = [α]−1∗ [p◦h]∗ [α]
This shows thatH andH′ are related by conjugation by [α], so H andH′ are conjugate subgroups.
Conversely, given two conjugate subgroups H0 = p∗(π1(E,e 0)) and H1 of π1(B,b 0) related by
H1 = [α]−1H0[α], then lift α to a path ~α in E starting at e0 and ending at e1. Then we have
H1 =p∗(π1(E,e 1)). This leads to the following more general classiﬁcation result.
Theorem. Let p : E→ B and p′ : E′→ B be path connected covering spaces. E and E′ are
equivalent if and only if the subgroups H =p∗(π1(E,e 0)) and H =p′
∗(π1(E′,e′
0)) are conjugate in
π1(B,b 0)
At this point we have produced some classiﬁcation results for covering spaces. We will brieﬂy
discuss construction of covering spaces. Every fundamental group has a subgroup that is equal
to the entire group. This corresponds to the trivial cover of a space by itself. However, every
fundamental group also has the trivial group as a subgroup, which corresponds to the universal
covering space.
104

Deﬁnition. A universal covering space is a covering space p : E→ B such that E is simply
connected.
The corresponding subgroup of a universal covering space is trivial.
Remark. By the previous theorem, universal covering spaces are unique up to equivalence.
Examples
• The usual map R→S1 is the universal cover.
• The product p×p :R×R→S1×S1 is the universal cover.
• The universal cover of the ﬁgure-eight spaceS1∨S1 is the Cayley graph on two generators:
Since the universal covering space is simply connected, we have seen that the lifting correspondence
π1(B,b 0)→ p−1(b0) is a bijection. The following theorem explains why such a cover is called
universal.
Theorem. Let p : E → B be a universal covering space and p′ : E′ → B any path connected
covering space. Then there exists a covering map q : E→ E′ such that p′◦q = p, and E is the
universal covering space of E′.
E E′
B
q
p p′
Then we have the following result, which follows from the fact that covering maps are also quotient
maps.
Corollary. Any path connected covering of B can be realized as the quotient of the universal
covering space.
Not all spaces admit a universal covering spaces
• The Hawaiian earring space is given by the union
H =
⋃
n≥1
Cn⊂ R2
105

where Cn is the circle of radius 1/n centered at (1/n, 0).
Any covering map must evenly cover some neighborhood of the origin 0. This means for
large enough n, the loop around Cn lifts to a loop in the covering space, so no covering
space of H is simply connected.
Ruling out some pathological spaces yields the following existence result.
Proposition. SupposeB is locally simply-connected.53 Then B admits a universal covering space.
Proof. Homotopy classes of loops should correspond to distinct sheets of the covering spaces, so
that no loops in ( B,b 0) lift to a loop in ( E,e 0). So the ﬁber above a point b∈B must consist of
all possible paths from b0 to b1 up to homotopy. Then the idea is to build a universal cover of B
out of pairs (b, [γ]) for b∈B and [γ] a homotopy class of paths from b0 to b.
At this point, {(b, [γ])} is merely a set. There is a natural topology on {(b, [γ])} obtained by
using local simply connectedness. It is then straightforward to conﬁrm that this is a covering
space.
To obtain other covering spaces, one then simply restricts attention to certain homotopy classes of
paths in this construction.
Free groups
The other main tool to compute the fundamental group is Van Kampen’s theorem. Today we will
discuss free groups and free products and relate them to this theorem next week.
Let G be a group, and let G1,...,G n be a collection of subgroups that generate G.54 In general,
the expressions for g∈G are far from being unique. Further assume that Gi∩Gj is trivial for all
i⁄=j.
If x = x1...x m, then (x1,...,x m) is a word that represents x. There can be many words that
representx, as adding identity elements has no bearing on the product.
53In fact, it suﬃces to assumeB is semi-locally simply connected, which means that every point has a neighborhood
for which the inclusion into the whole space induces the trivial homomorphism on fundamental groups.
54This means any g∈G can be written as a product of elements in G1,...,G n.
106

A word is reduced if no Gj contains consecutive xi and xi+1. This implies that the identity
is not present in the word, and that every xi is in a distinct subgroup Gj.
Deﬁnition. G is the (internal) free product of its subgroups G1,...,G n, denoted G1∗...∗Gn, if
1. G1,...,G n generateG
2. Gi∩Gj ={1} for all i⁄=j
3. For all x∈G, there is a unique reduced word that represents x.
The third condition is saying that there are no relations between elements in diﬀerent subgroups.
Example
• Z2 is not the free product of Z and Z. a +b =b +a, as Z2 is abelian, so this element is
represented by (a,b ) and (b,a ) (and (a2,b,a−1) along with many others).
Deﬁnition. The (external) free product of a collection of groups G1,...,G n is a group G along
with injective homomorphisms ij :Gj→G such that G =i1(G1)∗... ∗in(Gn).
The free product of groups always exists. It can be constructed as the set of reduced words in
G1,...,G n. The product is given by composition/concatenation of words.
Remark. The free product of groups is unique up to isomorphism, as since every element has a
unique reduced word, this yields an isomorphism with the above concrete construction.
The free product of groups satisﬁes a universal property.
Lemma. LetG =G1∗...∗Gn. For every group H and collection of homomorphisms hj :Gj→H,
there exists a unique homomorphism h :G→H such that h =hj◦ij.
Gj G
H
hj
ij
h
Proof. For an element x = x1...x n, let h(x) = h(x1)...h (xn). If xi∈ Gj, then deﬁne h(xi) =
hj(xi).55
Deﬁnition. The free group on elements{aj} is deﬁned to be the free product of Gj ={an
j :n∈
Z}≃ Z.
55This can always be written for a collection of groups that generate G, but it is not well-deﬁned unless we have
that G is the free product. Uniqueness of the reduced word allows us to choose a preferred representative on which
to deﬁne h.
107

The free group on elements {aj} is thus the collection of all words with all possible exponents on
each letter.
Returning to topology, we have seen that if X = U∪V with U,V ⊂ X open and U∩V path
connected, then π1(X,x 0) is generated by the subgroups i∗(π1(U,x 0)) and j∗(π1(V,x 0)), where i
andj are the inclusions ofU andV , respectively. By the above universal property, there is a unique
homomorphism
h :π1(U,x 0)∗π1(V,x 0)
that agrees with i∗ and j∗. The weak version of Van Kampen’s theorem implies that this homo-
morphism is a surjection. We adduce an additional result.
Theorem. If U∩V is simply connected then the above map h is an isomorphism.
Example
• The fundamental group of the ﬁgure-eight space S1∨S1 is the free group Z∗ Z.
108

12/2/2019 - Seifert-Van Kampen Theorem, Final Examples
Today we will state the Seifert-Van Kampen theorem. This theorem provides a way to understand
the fundamental group of a space X =U∪V in terms of the fundamental group of two open sets
U,V .
First, we proved that in such a case the fundamental group of X is generated by the images
of the fundamental groups of U and V under the induced homomorphisms that arise from the
inclusions U ↪→X and V ↪→X.
Second, we stated that if U∩V is in fact simply connected then the fundamental group of X
is the free product of the fundamental groups of U and V .
The Seifert-Van Kampen theorem addresses this question in its greatest generality. There is a
diagram of inclusions of topological spaces
U
U∩V X
V
j1i1
i2 j2
By the functoriality of π1 we have a diagram
π1(U,x 0)
π1(U,x 0)∗π1(V,x 0) π1(X,x 0)
π1(V,x 0)
(j1)∗
h
(j2)∗
where∗ indicates the free product56 and the map h is induced by the universal property of the free
product.57 Then from this perspective, the ﬁrst statement above implies thath is surjective. When
U∩V is simply connected, the second statement above implies that h is injective. The Seifert-Van
Kampen theorem says something about the kernel of h in the general case.
Theorem. Let X = U∪V , where U,V ⊂ X are open and U∩V is path connected. Then the
natural homomorphism
h :π1(U,x 0)∗π1(V,x 0)→π1(X,x 0)
extending (j1)∗ and (j2)∗ is surjective, and its kernel N is the smallest normal subgroup 58 of
π1(U,x 0)∗π1(V,x 0) which contains all elements of the form (i1)∗(g)−1(i2)∗(g) for all g∈ π1(U∩
56The free product of G and H can be explicitly constructed as the set of all words in G and H, which are ﬁnite
sequences of elements in G and H, where no successive elements lie in the same group. The multiplication law in
G∗H is given by composition of these words.
57See the notes from last lecture.
58We cannot simply consider the subgroup of elements of this form, as the quotient of a group by an arbitrary
subgroup is only in general a set. To obtain another group, we must consider the normal closure, namely the smallest
normal subgroup containing it, to obtain a quotient group.
109

V,x 0). In other words, we have
π1(X,x 0)≃ (π1(U,x 0)∗π1(V,x 0))/N
Taking the quotient byN serves to identify the loops in X that in fact arise from the same loops in
U andV . So π1(X) is the ‘free-est’ group that comes fromπ1(U) andπ1(V ) once we have identiﬁed
the loops that lie in U∩V .
Corollary. If U∩V is simply connected, then N ={1} and π1(X,x 0)≃π1(U,x 0)∗π1(V,x 0).
Corollary. IfV is simply connected, thenπ1(X,x 0)≃π1(U,x 0)/N, whereN is the smallest normal
subgroup containing the image of (i1)∗ :π1(U∩V,x 0)→π1(U,x 0).59
Examples
• Consider the ﬁgure-eight space X, which is the wedge of two circles .
Let U be the left circle, along with a bit of the right circle so that it is open. Similarly
letV be the right circle. Both U andV deformation retract ontoS1, andU∩V is simply
connected (it is contractible). The corollary then implies
π1(X)≃π1(S1)∗π1(S1)≃ Z∗ Z
• Similarly, an easy inductive argument implies that the wedge of n circles X =⋁nS1 has
fundamental group
π1(X)≃ Z∗... ∗ Z| {z }
n times
For example, the case when n = 4 is below.
59We cannot sayπ1(U∩V,x 0) is a subgroup of π1(U,x 0), as it is possible that the homomorphism (i1)∗ is not even
injective. Furthermore, there is no reason that the image should be normal.
110

Remark. Any connected ﬁnite grapha has the homotopy type of a wedge of ﬁnitely many circles.
Although we won’t prove this formally, the idea is simply that taking the quotient by an edge
that connects two distinct vertices is a homotopy equivalence, so we can reduce the graph to
having one vertex and many edges from that vertex to itself. Thus the fundamental group of
any ﬁnite graph is a free group.
This implies that any subgroup of a free group is free, as such a subgroup corresponds to
a covering space, and a covering space of a ﬁnite graph is also a graph.
aIn topology, a graph is a union of intervals glued at their endpoints.
Fundamental groups of surfaces
• Consider the torusT =S1×S1. We can obtain the torus as the quotient I×I/∼, where
(x, 0)∼ (x, 1) and (0,y )∼ (1,y ).
Let p = (1/2, 1/2) be the center of this square. Take U = T\{p} and V a small disc
centered at p.
U deformation retracts to onto the ﬁgure-eight space via a radial deformation retract
onto the the boundary of the square, and then applying the identiﬁcations indeed yields
the wedge of two circles (the ﬁgure-eight space). So π1(U,x 0)≃ Z∗ Z. V is contractible,
so π1(V,x 0).
The theorem implies π1(T )≃ π1(U)/N, where N is the smallest normal subgroup con-
taining (i1)′
∗(π1(U∩V )). U∩V is the punctured disc, and it is homotopy equivalent to
S1 with fundamental group π1(U∩V )≃ Z. We must examine the image of a generator
f∈π1(U∩V ) under (i1)∗.
Following f along the radial projection to the boundary and the identiﬁcation of the
edges illustrates that the image of f under (i1)∗ is aba−1b−1. Thus
π1(T ) = (Z∗ Z)/N
=⟨a,b :ab =ba⟩
= Z× Z
as expected.
• We can similarly compute the fundamental group of the projective plane RP 2. Recall
111

that RP 2≃S2/∼, where∼ identiﬁes antipodes x∼−x.
Then by restricting our attention to the upper hemisphere, we can also construct the
projective plane as a quotient of the disc RP 2≃ B2/∼, where∼ identiﬁes x∼− x for
x∈S1 and leaves points alone otherwise.
Let U = RP 2\{p} and V be a small disc centered at p. As in the previous exam-
ple,π1(V ) is trivial. U deformation retracts ontoS1/∼, which is itself homeomorphic to
S1. So π1(U)≃ Z. It remains to examine the image of π1(U∩V ). U∩V is homotopy-
equivalent to S1, so π1(U∩V ). The generator of this group is sent along the radial
retraction to the boundary, which is the loop that passes around the S1/∼ twice. Thus
π1(RP 2)≃ Z/2Z
• The Klein bottle can be constructed as the quotient I×I/∼, where (x, 0)∼ (x, 1) and
(0,y )∼ (1, 1−y).
TakingU =K\{p} and V a small disc around p again yields π1(U)∼ Z∗ Z and π1(V )
trivial by the same argument as the torus. U∩V is homotopy equivalent to S1, so let
f be a generator of π1(U∩V ). Taking f along the radial retraction and examining its
image after the identiﬁcation yields aba−1b. So
π1(K)≃⟨a,b :aba−1b = 1⟩
The relation can equivalently be given by ab =b−1a, or aba−1 =b−1. So b is conjugate
to b−1. This group contains an index 2 subgroup H generated by a2 and b. Then
a2ba−2 =a(aba−1)a−1 =ab−1a−1 =b
So a2 and b commute. Thus H≃ Z× Z.
112

An index 2 subgroup corresponds to a degree 2 covering space. The claim is that the
subgroup H⊂π1(K) corresponds to a covering map T→K, where T is the torus and
K is the Klein bottle. a
a‘If you paint a Klein bottle, the paint forms a torus.’ -D. Auroux
113

