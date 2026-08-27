An Introduction to Lie Groups
and Symplectic Geometry
A series of nine lectures on Lie groups and symplectic
geometry delivered at the Regional Geometry Institute in
Park City, Utah, 24 June–20 July 1991.
by
Robert L. Bryant
Duke University
Durham, NC
bryant@math.duke.edu
This is an unoﬃcial version of the notes and was last modiﬁed o n
23 July 2018.

Introduction
These are the lecture notes for a short course entitled “Intr oduction to Lie groups and
symplectic geometry” that I gave at the 1991 Regional Geomet ry Institute at Park City,
Utah starting on 24 June and ending on 11 July.
The course really was designed to be an introduction, aimed a t an audience of stu-
dents who were familiar with basic constructions in diﬀeren tial topology and rudimentary
diﬀerential geometry, who wanted to get a feel for Lie groups and symplectic geometry.
My purpose was not to provide an exhaustive treatment of eith er Lie groups, which would
have been impossible even if I had had an entire year, or of sym plectic manifolds, which
has lately undergone something of a revolution. Instead, I t ried to provide an introduction
to what I regard as the basic concepts of the two subjects, wit h an emphasis on examples
that drove the development of the theory.
I deliberately tried to include a few topics that are not part of the mainstream subject,
such as Lie’s reduction of order for diﬀerential equations a nd its relation with the notion
of a solvable group on the one hand and integration of ODE by qu adrature on the other.
I also tried, in the later lectures to introduce the reader to some of the global methods
that are now becoming so important in symplectic geometry. H owever, a full treatment of
these topics in the space of nine lectures beginning at the el ementary level was beyond my
abilities.
After the lectures were over, I contemplated reworking thes e notes into a comprehen-
sive introduction to modern symplectic geometry and, after some soul-searching, ﬁnally
decided against this. Thus, I have contented myself with mak ing only minor modiﬁcations
and corrections, with the hope that an interested person cou ld read these notes in a few
weeks and get some sense of what the subject was about.
An essential feature of the course was the exercise sets. Eac h set begins with elemen-
tary material and works up to more involved and delicate prob lems. My object was to
provide a path to understanding of the material that could be entered at several diﬀerent
levels and so the exercises vary greatly in diﬃculty. Many of these exercise sets are obvi-
ously too long for any person to do them during the three weeks the course, so I provided
extensive hints to aid the student in completing the exercis es after the course was over.
I want to take this opportunity to thank the many people who ma de helpful sugges-
tions for these notes both during and after the course. Parti cular thanks goes to Karen
Uhlenbeck and Dan Freed, who invited me to give an introducto ry set of lectures at the
RGI, and to my course assistant, Tom Ivey, who provided inval uable help and criticism in
the early stages of the notes and tirelessly helped the stude nts with the exercises. While
the faults of the presentation are entirely my own, without t he help, encouragement, and
proofreading contributed by these folks and others, neithe r these notes nor the course
would never have come to pass.
I.1 2

Background Material and Basic T erminology . In these lectures, I assume that
the reader is familiar with the basic notions of manifolds, v ector ﬁelds, and diﬀerential
forms. All manifolds will be assumed to be both second counta ble and Hausdorﬀ. Also,
unless I say otherwise, I generally assume that all maps and m anifolds are C∞.
Since it came up several times in the course of the course of th e lectures, it is probably
worth emphasizing the following point: A submanifold of a smooth manifold X is, by
deﬁnition, a pair ( S,f ) where S is a smooth manifold and f :S → X is a one-to-one
immersion. In particular, f need not be an embedding.
The notation I use for smooth manifolds and mappings is fairl y standard, but with a
few slight variations:
If f :X →Y is a smooth mapping, then f ′:TX →TY denotes the induced mapping
on tangent bundles, with f ′(x) denoting its restriction to TxX. (However, I follow tradition
when X = R and let f ′(t) stand for f ′(t)(∂/∂t ) for all t ∈ R. I trust that this abuse of
notation will not cause confusion.)
For any vector space V , I generally use Ap(V ) (instead of, say, Λ p(V ∗)) to denote
the space of alternating (or exterior) p-forms on V . For a smooth manifold M , I denote
the space of smooth, alternating p-forms on M by Ap(M ). The algebra of all (smooth)
diﬀerential forms on M is denoted by A∗(M ).
I generally reserve the letter d for the exterior derivative d: Ap(M ) → Ap+1(M ).
For any vector ﬁeld X on M , I will denote left-hook with X (often called interior
product with X) by the symbol X . This is the graded derivation of degree −1 of A∗(M )
that satisﬁes X (df) = Xf for all smooth functions f on M . For example, the Cartan
formula for the Lie derivative of diﬀerential forms is writt en in the form
LXφ =X dφ +d(X φ).
Jets. Occasionally, it will be convenient to use the language of je ts in describing
certain constructions. Jets provide a coordinate free way t o talk about the Taylor expansion
of some mapping up to a speciﬁed order. No detailed knowledge about these objects will
be needed in these lectures, so the following comments shoul d suﬃce:
If f and g are two smooth maps from a manifold Xm to a manifold Yn, we say that
f and g agree to order k at x ∈ X if, ﬁrst, f (x) = g(x) = y ∈ Y and, second, when
u:U → Rm and v:V → Rn are local coordinate systems centered on x and y respectively,
the functions F =v ◦f ◦u−1 andG =v ◦g ◦u−1 have the same Taylor series at 0 ∈ Rm up
to and including order k. Using the Chain Rule, it is not hard to show that this conditi on
is independent of the choice of local coordinates u and v centered at x and y respectively.
The notation f ≡x,k g will mean that f and g agree to order k at x. This is easily
seen to deﬁne an equivalence relation. Denote the ≡x,k-equivalence class of f byjk(f )(x),
and call it the k-jet of f at x.
For example, knowing the 1-jet at x of a map f :X →Y is equivalent to knowing both
f (x) and the linear map f ′(x):Tx →Tf (x)Y .
I.2 3

The set of k-jets of maps from X toY is usually denoted by Jk(X,Y ). It is not hard
to show that Jk(X,Y ) can be given a unique smooth manifold structure in such a way
that, for any smooth f :X →Y , the obvious map jk(f ):X →Jk(X,Y ) is also smooth.
These jet spaces have various functorial properties that we shall not need at all. The
main reason for introducing this notion is to give meaning to concise statements like “The
critical points of f are determined by its 1-jet”, “The curvature at x of a Riemannian
metric g is determined by its 2-jet at x”, or, from Lecture 8, “The integrability of an
almost complex structure J:TX → TX is determined by its 1-jet”. Should the reader
wish to learn more about jets, I recommend the ﬁrst two chapte rs of [GG].
Basic and Semi-Basic. Finally, I use the following terminology: If π:V → X is
a smooth submersion, a p-form φ ∈ Ap(V ) is said to be π-basic if it can be written in
the form φ = π∗(ϕ) for some ϕ ∈ Ap(X) and π-semi-basic if, for any π-vertical*vector
ﬁeld X, we have X φ = 0. When the map π is clear from context, the terms “basic” or
“semi-basic” are used.
It is an elementary result that if the ﬁbers of π are connected and φ is a p-form on V
with the property that both φ and dφ are π-semi-basic, then φ is actually π-basic.
At least in the early lectures, we will need very little in the way of major theorems,
but we will make extensive use of the following results:
• The Implicit F unction Theorem: If f :X → Y is a smooth map of manifolds
and y ∈ Y is a regular value of f , then f −1(y) ⊂ X is a smooth embedded submanifold
of X, with
Txf −1(y) = ker(f ′(x):TxX →TyY )
• Existence and Uniqueness of Solutions of ODE: If X is a vector ﬁeld on a
smooth manifold M , then there exists an open neighborhood U of {0} ×M in R ×M and
a smooth mapping F :U →M with the following properties:
i. F (0,m ) = m for all m ∈M .
ii. For each m ∈ M , the slice Um = {t ∈ R | (t,m ) ∈ U } is an open interval in R
(containing 0) and the smooth mapping φm:Um →M deﬁned by φm(t) = F (t,m ) is
an integral curve of X.
iii. ( Maximality ) If φ:I → M is any integral curve of X where I ⊂ R is an interval
containing 0, then I ⊂Uφ(0) and φ(t) = φφ(0)(t) for all t ∈I.
The mapping F is called the (local) ﬂow ofX and the open set U is called the domain
of the ﬂow of X. If U = R ×M , then we say that X is complete.
Two useful properties of this ﬂow are easy consequences of th is existence and unique-
ness theorem. First, the interval UF (t,m) ⊂ R is simply the interval Um translated by −t.
Second, F (s +t,m ) = F (s,F (t,m )) whenever t and s +t lie in Um.
* A vector ﬁeld X isπ-vertical with respect to a map π:V →X if and only if π′(
X(v)
)
=
0 for all v ∈V
I.3 4

• The Simultaneous Flow-Box Theorem: If X1, X2, ... , Xr are smooth vector
ﬁelds on M that satisfy the Lie bracket identities
[Xi,Xj] = 0
for all i and j, and if p ∈ M is a point where the r vectors X1(p),X 2(p),...,X r(p) are
linearly independent in TpM , then there exists a local coordinate system x1,x 2,...,x n on
an open neighborhood U of p so that, on U ,
X1 = ∂
∂x1, X 2 = ∂
∂x2, ..., X r = ∂
∂xr.
The Simultaneous Flow-Box Theorem has two particularly use ful consequences. Be-
fore describing them, we introduce an important concept.
Let M be a smooth manifold and let E ⊂TM be a smooth subbundle of rank p. We
say that E is integrable if, for any two vector ﬁelds X andY onM that are sections of E,
their Lie bracket [ X,Y ] is also a section of E.
• The Local F robenius Theorem: If Mn is a smooth manifold and E ⊂ TM is
a smooth, integrable sub-bundle of rank r, then every p in M has a neighborhood U on
which there exist local coordinates x1,...,x r,y 1,...,y n−r so that the sections of E over
U are spanned by the vector ﬁelds
∂
∂x1, ∂
∂x2, ..., ∂
∂xr.
Associated to this local theorem is the following global ver sion:
• The Global F robenius Theorem: LetM be a smooth manifold and let E ⊂TM
be a smooth, integrable subbundle of rank r. Then for any p ∈M , there exists a connected
r-dimensional submanifold L ⊂ M that contains p, that satisﬁes TqL = Eq for all q ∈S,
and that is maximal in the sense that any connected r′-dimensional submanifold L′ ⊂M
that contains p and satisﬁes TqL′ ⊂Eq for all q ∈L′ is a submanifold of L.
The submanifolds L provided by this theorem are called the leaves of the sub-bundle
E. (Some books call a sub-bundle E ⊂ TM a distribution on M , but I avoid this since
“distribution” already has a well-established meaning in a nalysis.)
I.4 5

Contents
1. Introduction: Symmetry and Diﬀerential Equations 7
First notions of diﬀerential equations with symmetry, clas sical “integration methods.”
Examples: Motion in a central force ﬁeld, linear equations, the Riccati equation, and
equations for space curves.
2. Lie Groups 12
Lie groups. Examples: Matrix Lie groups. Left-invariant ve ctor ﬁelds. The exponen-
tial mapping. The Lie bracket. Lie algebras. Subgroups and s ubalgebras. Classiﬁca-
tion of the two and three dimensional Lie groups and algebras .
3. Group Actions on Manifolds 38
Actions of Lie groups on manifolds. Orbit and stabilizers. E xamples. Lie algebras
of vector ﬁelds. Equations of Lie type. Solution by quadratu re. Appendix: Lie’s
Transformation Groups, I. Appendix: Connections and Curva ture.
4. Symmetries and Conservation Laws 61
Particle Lagrangians and Euler-Lagrange equations. Symme tries and conservation
laws: Noether’s Theorem. Hamiltonian formalism. Examples : Geodesics on Rie-
mannian Manifolds, Left-invariant metrics on Lie groups, R igid Bodies. Poincar´ e
Recurrence.
5. Symplectic Manifolds, I 80
Symplectic Algebra. The structure theorem of Darboux. Exam ples: Complex Mani-
folds, Cotangent Bundles, Coadjoint orbits. Symplectic an d Hamiltonian vector ﬁelds.
Involutivity and complete integrability.
6. Symplectic Manifolds, II 100
Obstructions to the existence of a symplectic structure. Ri gidity of symplectic struc-
tures. Symplectic and Lagrangian submanifolds. Fixed Poin ts of Symplectomor-
phisms. Appendix: Lie’s Transformation Groups, II
7. Classical Reduction 116
Symplectic manifolds with symmetries. Hamiltonian and Poi sson actions. The mo-
ment map. Reduction.
8. Recent Applications of Reduction 128
Riemannian holonomy. K¨ ahler Structures. K¨ ahler Reduction. Examples: Projective
Space, Moduli of Flat Connections on Riemann Surfaces. Hype rK¨ ahler structures and
reduction. Examples: Calabi’s Examples.
9. The Gromov School of Symplectic Geometry 147
The Soft Theory: The h-Principle. Gromov’s Immersion and Embedding Theorems.
Almost-complex structures on symplectic manifolds. The Ha rd Theory: Area esti-
mates, pseudo-holomorphic curves, and Gromov’s compactne ss theorem. A sample of
the new results.
I.1 6

Lecture 1:
Introduction: Symmetry and Diﬀerential Equations
Consider the classical equations of motion for a particle in a conservative force ﬁeld
¨x = −grad V (x),
where V : Rn → R is some function on Rn. If V is proper (i.e. the inverse image under V
of a compact set is compact, as when V (x) = |x|2), then, to a ﬁrst approximation, V is the
potential for the motion of a ball of unit mass rolling around in a cup, moving only under
the inﬂuence of gravity. For a general function V we have only the grossest knowledge of
how the solutions to this equation ought to behave.
Nevertheless, we can say a few things. The total energy (= kin etic plus potential)
is given by the formula E = 1
2 | ˙x|2 +V (x) and is easily shown to be constant on any
solution (just diﬀerentiate E
(
x(t)
)
and use the equation). Since, V is proper, it follows
that x must stay inside a compact set V −1(
[0,E (x(0))]
)
, and so the orbits are bounded.
Without knowing any more about V , one can show (see Lecture 4 for a precise statement)
that the motion has a certain ‘recurrent’ behaviour: The tra jectory resulting from ‘most’
initial positions and velocities tends to return, inﬁnitel y often, to a small neighborhood
of the initial position and velocity. Beyond this, very litt le is known is known about the
behaviour of the trajectories for generic V .
Suppose now that the potential function V is rotationally symmetric, i.e., that V
depends only on the distance from the origin and, for the sake of simplicity, let us take
n = 3 as well. This is classically called the case of a central fo rce ﬁeld in space. If we let
V (x) = 1
2v(|x|2), then the equations of motion become
¨x = −v′(
|x|2)
x.
As conserved quantities, i.e., functions of the position an d velocity that stay constant on
any solution of the equation, we still have the energy E = 1
2
(
| ˙x|2 +v(|x|2)
)
, but is it also
easy to see that the vector-valued function x × ˙x is conserved, since
d
dt (x × ˙x) = ˙x × ˙x −x ×v′(|x|2) x = 0 − 0 = 0.
Call this vector-valued function µ. We can think of E and µ as functions on the phase
space R6. For generic values of E0 and µ0, the simultaneous level set
ΣE0,µ0 = { (x, ˙x) |E(x, ˙x) = E0, µ(x, ˙x) = µ0 }
of these functions is a surface Σ E0,µ0 ⊂ R6, and any integral of the equations of motion
must lie in one of these surfaces. Since we know a great deal ab out integrals of ODEs on
L.1.1 7

surfaces, this problem is very tractable. (See Lecture 4 and its exercises for more details
on this.)
The function µ, known as the angular momentum , is called a ﬁrst integral of the
second-order ODE for x(t) and seems to somehow correspond to the rotational symmetry
of the original ODE. This vague relationship will be conside rably sharpened and made
precise in the upcoming lectures.
The relationship between symmetry and solvability in diﬀer ential equations is pro-
found and far reaching. The subjects that are now known as ‘Li e groups’ and ‘symplectic
geometry’ got their beginnings from the study of symmetries of systems of ordinary diﬀer-
ential equations and of integration techniques for them.
By the middle of the nineteenth century, Galois theory had cl ariﬁed the relationship
between the solvability of polynomial equations by radical s and the group of ‘symmetries’
of the equations. Sophus Lie set out to do the same thing for di ﬀerential equations and
their symmetries.
Here is a ‘dictionary’ showing the (rough) correspondence t hat Lie developed between
these two achievements of nineteenth century mathematics.
Galois theory inﬁnitesimal symmetries
ﬁnite groups continuous groups
polynomial equations diﬀerential equations
solvable by radicals solvable by quadrature
Although the full explanation of these correspondances mus t await the later lectures, we
can at least begin the story in the simplest examples as motiv ation for developing the
general theory. This is what I shall do for the rest of today’s lecture.
Classical Integration T echniques. The very simplest ordinary diﬀerential equation
that we ever encounter is the equation
(1) ˙ x(t) = α(t)
where α is a known function of t. The solution of this diﬀerential equation is simply
x(t) = x0 +
∫ x
0
α(τ )dτ.
The process of computing an integral was known as ‘quadratur e’ in the classical literature
(a reference to expressing the area under a curve as the area o f a quadrilateral), so it was
said that (1) was ‘solvable by quadrature’. Note that, once o ne ﬁnds a particular solution,
all of the others are got by simply translating the particula r solution by a constant, in this
case, by x0. Alternatively, one could say that the equation (1) itself w as invariant under
‘translation inx’.
The next most trivial case is the homogeneous linear equatio n
(2) ˙ x =β(t)x.
L.1.2 8

This equation is invariant under scale transformations x ↦→rx. Since the mapping
log: R+ → R converts scaling to translation, it should not be surprisin g that the diﬀerential
equation (2) is also solvable by a quadrature:
x(t) = x0e
∫ t
0
β(τ )dτ.
Note that, again, the symmetries of the equation suﬃce to all ow us to deduce the general
solution from a particular one.
Next, consider an equation where the right hand side is an aﬃn e function of x,
(3) ˙ x =α(t) +β(t)x.
This equation is still solvable in full generality, using tw o quadratures. For, if we set
x(t) = u(t)e
∫ t
0
β(τ )dτ,
thenu satisﬁes ˙u =α(t)e−
∫ t
0
β(τ )dτ , which can be solved for u by another quadrature. It is
not at all clear why one can somehow ‘combine’ equations (1) a nd (2) and get an equation
that is still solvable by quadrature, but this will become cl ear in Lecture 3.
Now consider an equation with a quadratic right-hand side, t he so-called Riccati equa-
tion:
(4) ˙ x =α(t) + 2β(t)x +γ(t)x2.
It can be shown that there is no method for solving this by quad ratures and algebraic
manipulations alone. However, there is a way of obtaining th e general solution from a
particular solution: If s(t) is a particular solution of (4), try the ansatz x(t) = s(t) +
1/u(t). The resulting diﬀerential equation for u has the form (3) and hence is solvable by
quadratures.
The Riccati equation (4) has an extensive history, and we wil l return to it often. Its
remarkable property, that given one solution we can obtain t he general solution, should be
contrasted with the case of
(5) ˙ x =α(t) +β(t)x +γ(t)x2 +δ(t)x3.
For equation (5), knowing one solution does not help give the rest of the solutions. There
is in fact a world of diﬀerence between this and the Riccati eq uation, although this is far
from evident looking at them.
Before leaving these simple ODE, we note the following curio us progression: If x1 and
x2 are solutions of an equation of type (1), then clearly the diﬀ erencex1 −x2 is constant.
Similarly, if x1 and x2 ⁄= 0 are solutions of an equation of type (2), then the ratio x1/x2
is constant. Furthermore, if x1, x2, and x3 ⁄=x1 are solutions of an equation of type (3),
L.1.3 9

then the expression (x1 −x2)/(x1 −x3) is constant. Finally, if x1,x2,x3 ⁄=x1, and x4 ⁄=x2
are solutions of an equation of type (4), then the cross-ratio
(x1 −x2)(x4 −x3)
(x1 −x3)(x4 −x2)
is constant. There is no such corresponding expression (for any number of particular
solutions) for equations of type (5). The reason for this wil l be made clear in Lecture 3.
For right now, we just want to remark on the fact that the linea r fractional transformations
of the real line, a group isomorphic to SL(2 , R), are exactly the transformations that leave
ﬁxed the cross-ratio of any four points. As we shall see, the g roup SL(2, R) is closely
connected with the Riccati equation and it is this connectio n that accounts for many of
the special features of this equation.
We will conclude this lecture by discussing the group of rigi d motions in Euclidean
3-space. These are transformations of the form
T (x) = R x + t,
where R is a rotation in E3 and t ∈ E3 is any vector. It is easy to check that the set of
rigid motions form a group under composition that is, in fact , isomorphic to the group of
4-by-4 matrices {(
R t
0 1
)
tR R = I3, t ∈ R3
}
.
(Topologically, the group of rigid motions is just the produ ct O(3) × R3.)
Now, suppose that we are asked to solve for a curve x: R → R3 with a prescribed
curvature κ(t) and torsion τ (t). If x were such a curve, then we could calculate the
curvature and torsion by deﬁning an oriented orthonormal ba sis (e1,e2,e3) along the curve,
satisfying ˙x = e1, ˙e1 =κe2, ˙e2 = −κe1 +τ e3. (Think of the torsion as measuring how e2
falls away from the e1e2-plane.) Form the 4-by-4 matrix
X =
(
e1 e2 e3 x
0 0 0 1
)
,
(where we always think of vectors in R3 as columns). Then we can express the ODE for
prescribed curvature and torsion as
˙X =X



0 −κ 0 1
κ 0 −τ 0
0 τ 0 0
0 0 0 0


.
We can think of this as a linear system of equations for a curve X(t) in the group of rigid
motions.
L.1.4 10

It is going to turn out that, just as in the case of the Riccati e quation, the prescribed
curvature and torsion equations cannot be solved by algebra ic manipulations and quadra-
ture alone. However, once we know one solution, all other sol utions for that particular(
κ(t),τ (t)
)
can be obtained by rigid motions. In fact, though, we are goin g to see that one
does not have to know a solution to the full set of equations be fore ﬁnding the rest of the
solutions by quadrature, but only a solution to an equation c onnected to SO(3), just in the
same way that the Riccati equation is connected to SL(2 , R), the group of transformations
of the line that ﬁx the cross-ratio of four points.
L.1.5 11

Lecture 2:
Lie Groups and Lie Algebras
Lie Groups. In this lecture, I deﬁne and develop some of the basic propert ies of the
central objects of interest in these lectures: Lie groups an d Lie algebras.
Deﬁnition 1: A Lie group is a pair (G,µ ) whereG is a smooth manifold and µ :G×G →G
is a smooth mapping that gives G the structure of a group.
When the multiplication µ is clear from context, one usually just says “ G is a Lie
group.” Also, for the sake of notational sanity, I will follo w the practice of writing µ(a,b )
simply asab whenever this will not cause confusion. I will usually denot e the multiplicative
identity by e ∈G and the multiplicative inverse of a ∈G bya−1 ∈G.
Most of the algebraic constructions in the theory of abstrac t groups have straightfor-
ward analogues for Lie groups:
Deﬁnition 2: A Lie subgroup of a Lie group G is a subgroup H ⊂ G that is also a
submanifold of G. A Lie group homomorphism is a group homomorphism φ :H →G that
is also a smooth mapping of the underlying manifolds.
Here is the prototypical example of a Lie group:
Example : The General Linear Group. The (real) general linear group in dimen-
sionn, denoted GL(n, R), is the set of invertible n-by-n real matrices regarded as an open
submanifold of the n2-dimensional vector space of all n-by-n real matrices with multipli-
cation map µ given by matrix multiplication: µ(a,b ) = ab. Since the matrix product ab
is deﬁned by a formula that is polynomial in the matrix entrie s of a and b, it is clear
that GL(n, R) is a Lie group.
Actually, if V is any ﬁnite dimensional real vector space, then GL( V ), the set of
bijective linear maps φ :V →V , is an open subset of the vector space End( V ) = V ⊗V ∗
and becomes a Lie group with multiplication µ : GL(V ) × GL(V ) → GL(V ) given by
composition of maps: µ(φ1,φ 2) = φ1◦φ2. If dim( V ) = n, then GL(V ) is isomorphic (as a
Lie group) to GL( n, R), though not canonically.
The advantage of considering abstract vector spaces V rather than just Rn is mainly
conceptual, but, as will be seen, this conceptual advantage is great. In fact, Lie groups of
linear transformations are so fundamental that a special te rminology is reserved for them:
Deﬁnition 3: A ( linear) representation of a Lie group G is a Lie group homomor-
phism ρ : G → GL(V ) for some vector space V (called the representation space). Such
a representation is said to be faithful (resp., almost faithful ) if ρ is one-to-one (resp., has
0-dimensional kernel).
L.2.1 12

It is a consequence of a theorem of Ado and Iwasawa that every c onnected Lie group
has an almost faithful, ﬁnite-dimensional representation . (One of the later exercises con-
structs a connected Lie group that has no faithful, ﬁnite-dimensional representation, so
almost faithful is the best one can hope for.)
Example: V ector Spaces. Any vector space over R becomes a Lie group when the
group “multiplication” is taken to be addition.
Example: Matrix Lie Groups. The Lie subgroups of GL( n, R) are called matrix Lie
groups and play an important role in the theory. Not only are they the most frequently
encountered, but, because of the theorem of Ado and Iwasawa, practically anything that is
true for matrix Lie groups has an analog for a general Lie grou p. In fact, for the ﬁrst pass
through, the reader can simply imagine that all of the Lie gro ups mentioned are matrix
Lie groups. Here are a few simple examples:
1. Let An be the set of diagonal n-by-n matrices with positive entries on the diagonal.
2. Let Nn be the set of upper triangular n-by-n matrices with all diagonal entries all
equal to 1.
3. (n = 2 only) Let C• =
{(a −b
b a
)
|a2 +b2> 0
}
. Then C• is a matrix Lie group diﬀeo-
morphic to S1 × R. (You should check that this is actually a subgroup of GL(2 , R)!)
4. Let GL +(n, R) = {a ∈ GL(n, R) | det(a)> 0}
There are more interesting examples, of course. A few of thes e are
SL(n, R) = {a ∈ GL(n, R) | det(a) = 1 }
O(n) = {a ∈ GL(n, R) |taa =In}
SO(n, R) = {a ∈ O(n) | det(a) = 1 },
which are known respectively as the special linear group , the orthogonal group , and the
special orthogonal group in dimension n. In each case, one must check that the given
subset is actually a subgroup and submanifold of GL( n, R). These are exercises for the
reader. (See the problems at the end of this lecture for hints .)
A Lie group can have ‘wild’ subgroups that cannot be given the structure of a Lie
group. For example, ( R, +) is a Lie group that contains totally disconnected, uncoun table
subgroups. Since all manifolds in these notes are second cou ntable, such subgroups (by
deﬁnition) cannot be given the structure of a (0-dimensiona l) Lie group.
However, it can be shown [see Warner, pg. 110] that any closed subgroup of a Lie
group G is an embedded submanifold of G and hence is a Lie subgroup. However, for
reasons that will soon become apparent, it is disadvantageo us to consider only closed
subgroups.
L.2.2 13

Example: A non-closed subgroup. For example, even GL( n, R) can have Lie
subgroups that are not closed. Here is a simple example: Let λ be any irrational real
number and deﬁne a homomorphism φλ : R → GL(4, R) by the formula
φλ(t) =



cost − sint 0 0
sint cost 0 0
0 0 cos λt − sinλt
0 0 sin λt cosλt



Then φλ is easily seen to be a one-to-one immersion so its image is a su bmanifold Gλ ⊂
GL(4, R), which is therefore a Lie subgroup. It is not hard to see that
Gλ =








cost − sint 0 0
sint cost 0 0
0 0 cos s − sins
0 0 sin s coss



s,t ∈ R





.
Note thatGλ is diﬀeomorphic to R while its closure in GL(4, R) is diﬀeomorphic to S1×S1 !
It is also useful to consider matrix Lie groups with complex c oeﬃcients. However,
complex matrix Lie groups are really no more general than rea l matrix Lie groups (though
they may be more convenient to work with). To see why, note tha t one can write a
complex n-by-n matrix A +Bi (where A and B are real n-by-n matrices) as the 2 n-by-
2n matrix
(A −B
B A
)
. In this way, one can embed GL( n, C), the space of n-by-n invertible
complex matrices, as a closed submanifold of GL(2 n, R). The reader should check that
this mapping is actually a group homomorphism.
Among the more commonly encountered complex matrix Lie grou ps are the complex
special linear group , denoted by SL( n, C), and the unitary and special unitary groups ,
denoted, respectively, as
U(n) = {a ∈ GL(n, C) | ∗aa =In }
SU(n) = {a ∈ U(n) | detC(a) = 1 }
where ∗a = t¯a is the Hermitian adjoint of a. These groups will play an important role in
what follows. One may want to familiarize oneself with these groups by doing some of the
exercises for this section.
Basic General Properties. If G is a Lie group with a ∈ G, let La,Ra : G → G
denote the smooth mappings deﬁned by
La(b) = ab and Ra(b) = ba.
Proposition 1: For any Lie group G, the maps La andRa are diﬀeomorphisms, the map
µ :G ×G →G is a submersion, and the inverse mapping ι :G →G deﬁned by ι(a) = a−1
is smooth.
L.2.3 14

Proof: By the axioms of group multiplication, La−1 is both a left and right inverse to
La. Since ( La)−1 exists and is smooth, La is a diﬀeomorphism. The argument for Ra is
similar.
In particular, L′
a :TG →TG induces an isomorphism of tangent spaces TbG ˜→TabG
for all b ∈ G and R′
a :TG →TG induces an isomorphism of tangent spaces TbG ˜→TbaG
for all b ∈ G. Using the natural identiﬁcation T(a,b)G ×G ≃TaG ⊕TbG, the formula for
µ′(a,b ) : T(a,b)G ×G →TabG is readily seen to be
µ′(a,b )(v,w ) = L′
a(w) +R′
b(v)
for all v ∈TaG and w ∈TbG. In particular µ′(a,b ) is surjective for all ( a,b ) ∈G ×G, so
µ :G ×G →G is a submersion.
Now, by the Implicit Function Theorem, µ−1(e) is a closed, embedded submanifold of
G ×G whose tangent space at ( a,b ), by the above formula, is
T(a,b)µ−1(e) = {(v,w ) ∈TaG ×TbG
L′
a(w) +R′
b(v) = 0 }.
Meanwhile, the group axioms imply that
µ−1(e) =
{
(a,a −1) |a ∈G
}
,
which is precisely the graph of ι :G →G. Since L′
a andR′
b are isomorphisms, the tangent
space T(a,b)µ−1(e) intersects each of the subspaces T(a,b)
(
{a}×G
)
and T(a,b)
(
G×{b}
)
in
the trivial subspace. It then follows that the projection on the ﬁrst factor π1 :G ×G →G
restricts to µ−1(e) to be a smooth, one-to-one map of µ−1(e) onto G that is a local
diﬀeomorphism. The inverse of this diﬀeomorphism is theref ore also smooth and is simply
the graph of ι. It follows that ι is smooth, as desired. □
The Identity Component. For any Lie group G, let G◦ ⊂G denote the connected
component of G that contains e. This is usually called the identity component of G.
Proposition 2: For any Lie group G, the set G◦ is an open, normal subgroup of G.
Moreover, if U is any open neighborhood of e inG◦, then G◦ is the union of the “powers”
Un deﬁned inductively by U 1 =U and Uk+1 =µ(Uk,U ) for k >0.
Proof: Since G is a manifold, its connected components are open and path-co nnected,
so G◦ is open and path-connected. If α,β : [0, 1] → G are two continuous maps with
α(0) = β(0) = e, then γ : [0, 1] → G deﬁned by γ(t) = α(t)β(t)−1 is a continuous path
from e to α(1)β(1)−1, so G◦ is closed under multiplication and inverse, and hence is a
subgroup. It is a normal subgroup since, for any a ∈G, the map
Ca =La ◦ (Ra)−1 :G →G
(conjugation by a) is a diﬀeomorphism that clearly ﬁxes e and hence ﬁxes its connected
component G◦ also.
L.2.4 15

Finally, let U ⊂G◦ be any open neighborhood of e and, setting U 1 =U , inductively
deﬁne the powers Uk =µ(Uk−1,U ) ⊂G◦. Since e ∈U , note that Uk−1 ⊂Uk and, since µ
is a submersion, each of the sets Uk is open, as is their union U ∞ ⊂G◦.
It remains to show that U ∞ = G◦. For any a ∈ G◦, let γ : [0 , 1] → G◦ be a
continuous path with γ(0) = e and γ(1) = a. If a ⁄∈U ∞, then by the openness of U ∞
and the continuity of γ there will be a t0 ∈ (0, 1] such that γ(t0) ⁄∈U ∞, while γ(t) ∈U ∞
for all 0 ≤ t < t0. By continuity, there will exist a t ∈ [0,t 0) such that γ(t) lies in
the open set Lγ(t0)
(
ι(U )
)
(since ι(U ) is an open neighborhood of e). However, since
γ(t) = a0a1 · · ·ak for some ai ∈U and since γ(t) = γ(t0)b−1 for some b ∈U , it now follows
thatγ(t0) = a0a1 · · ·akb, i.e., that γ(t0) lies in Uk+1 ⊂U ∞. This contradiction establishes
that a ∈U ∞. Thus, U ∞ =G◦. □
An immediate consequence of Proposition 2 is that, for a conn ected Lie group H,
any Lie group homomorphism φ : H → G is determined by its behavior on any open
neighborhood of e ∈H. We are soon going to show an even more striking fact, namely t hat,
for connected H, any homomorphism φ :H →G is determined by φ′(e) : TeH →TeG.
The Adjoint Representation. It is conventional to denote the tangent space at
the identity of a Lie group by an appropriate lower case gothi c letter. Thus, the vector
space TeG is denoted g, the vector space TeGL(n, R) is denoted gl(n, R), etc.
For example, one can easily compute the tangent spaces at e of the Lie groups deﬁned
so far. Here is a sample:
sl(n, R) = {a ∈ gl(n, R) | tr(a) = 0 }
so(n, R) = {a ∈ gl(n, R) |a +ta = 0}
u(n, R) = {a ∈ gl(n, C) |a +t¯a = 0}
Deﬁnition 4: For any Lie groupG, the adjoint mapping is the mapping Ad : G → End(g)
deﬁned by
Ad(a) =
(
La ◦ (Ra)−1
)′
(e) : TeG →TeG.
As an example, for G = GL(n, R) it is easy to see that
Ad(a)(x) = axa−1
for all a ∈ GL(n, R) and x ∈ gl(n, R). Of course, this formula is valid for any matrix Lie
group.
The following proposition explains why the adjoint mapping is also called the adjoint
representation.
Proposition 3: The adjoint mapping is a linear representation Ad : G → GL(g).
L.2.5 16

Proof: For any a ∈G, let Ca =La ◦Ra−1 . Then Ca :G →G is a diﬀeomorphism that
satisﬁes Ca(e) = e. In particular, Ad( a) = C′
a(e) : g → g is an isomorphism and hence
belongs to GL( g).
The associative property of group multiplication implies Ca ◦Cb =Cab, so the Chain
Rule implies that C′
a(e) ◦C′
b(e) = C′
ab(e). Hence, Ad( a)Ad(b) = Ad( ab), so Ad is a
homomorphism.
It remains to show that Ad is smooth. However, if C : G ×G → G is deﬁned by
C(a,b ) = aba−1, then, by Proposition 1, C is a composition of smooth maps and hence
is smooth. It follows easily that the map c : G × g → g given by c(a,v ) = C′
a(e)(v) =
Ad(a)(v) is a composition of smooth maps. The smoothness of the map c clearly implies
the smoothness of Ad : G → g ⊗ g∗. □
Left-invariant vector ﬁelds. Because L′
a induces an isomorphism from g to TaG
for all a ∈G, it is easy to show that the map Ψ : G × g →TG given by
Ψ(a,v ) = L′
a(v)
is actually an isomorphism of vector bundles that makes the f ollowing diagram commute.
G × g
Ψ
− → TG
π1


↓


↓π
G
id
− → G
Note that, in particular, G is a parallelizable manifold. This implies, for example, th at the
only compact surface that can be given the structure of a Lie g roup is the torus S1 ×S1.
For eachv ∈ g, one uses Ψ to deﬁne a vector ﬁeld Xv onG by the rule Xv(a) = L′
a(v).
Note that, by the Chain Rule and the deﬁnition of Xv, one has
L′
a(Xv(b)) = L′
a(L′
b(v)) = L′
ab(v) = Xv(ab).
Thus, the vector ﬁeld Xv is invariant under left translation by any element of G. Such
vector ﬁelds turn out to be extremely useful in understandin g the geometry of Lie groups,
and are accorded a special name:
Deﬁnition 5: IfG is a Lie group, a left-invariant vector ﬁeld onG is a vector ﬁeld X on
G that satisﬁes L′
a(X(b)) = X(ab).
For example, consider GL( n, R) as an open subset of the vector space of n-by-n ma-
trices with real entries. Here, gl(n, R) is just the vector space of n-by-n matrices with real
entries itself and one easily sees that
Xv(a) = (a,av ).
L.2.6 17

(Since GL(n, R) is an open subset of a vector space, namely, gl(n, R), one can use the
standard identiﬁcation of the tangent bundle of GL( n, R) with GL(n, R) × gl(n, R).)
The following proposition determines all of the left-invar iant vector ﬁelds on a Lie
group.
Proposition 4: Every left-invariant vector ﬁeld X on G is of the form X = Xv where
v =X(e) and hence is smooth. Moreover, such an X is complete, i.e., the ﬂow Φ associated
to X has domain R ×G. Finally, for all s,t ∈ R, one has
Φ(s +t,e ) = Φ( s,e )Φ(t,e ).
Proof: That every left-invariant vector ﬁeld on G has the stated form is an easy exercise
for the reader.
Let Φ : D → G be the ﬂow of X, where D ⊂ R × G is an open neighborhood
of {0} ×G with the property that, for all a ∈ G, there is an open interval Ia ⊂ R such
thatD ∩
(
R × {a}
)
=Ia × {a} and the curve γa :Ia →G deﬁned by γa(t) = Φ( t,a ) is the
maximally extended integral curve of X (i.e.,γ′
a(t) = X (γa(t)) for all t ∈Ia) that satisﬁes
the initial condition γa(0) = a.
Note that, for any a ∈G, the curve
δa(t) = aγe(t)
satisﬁes δa(0) = a and
δ′
a(t) = L′
a (γ′
e(t)) = L′
a (X (γe(t))) = X (aγe(t)) = X (δa(t)).
Thus, it follows that Ie ⊂Ia and that
γa(t) = aγe(t)
for all t ∈Ie.
Since the domain D of the ﬂow Φ of X contains the product open set Ie ×G ⊂ R ×G,
it follows by standard arguments that D = R ×G, i.e., that X is complete.
Finally, because Φ( s +t,e ) = Φ
(
t, Φ(s,e )
)
by the properties of ﬂows, one has, by the
above formula for γa in terms of γe that
Φ(s +t,e ) = Φ
(
t, Φ(s,e )
)
=γΦ(s,e)(t) = Φ( s,e )γe(t) = Φ( s,e )Φ(t,e ).
□
As an example, consider the ﬂow of the left-invariant vector ﬁelds on GL( n, R) (or
any matrix Lie group, for that matter): For any v ∈ gl(n, R), the diﬀerential equation that
γe satisﬁes is simply
γ′
e(t) = γe(t)v.
L.2.7 18

This is a matrix diﬀerential equation and, in elementary ode courses, one learns that the
‘fundamental solution’ is
γe(t) = etv =In +
∞∑
k=1
vk
k!tk
and that this series converges uniformly on compact sets in R to a smooth matrix-valued
function of t.
Matrix Lie groups are by far the most commonly encountered an d, for this reason,
one often uses the notation exp( tv) or even etv for the integral curve γe(t) associated to
Xv in a general Lie group G. (Actually, in order for this notation to be unambiguous, it
has to be checked that if tv =uw for t,u ∈ R and v,w ∈ g, then γe(t) = δe(u) where γe is
the integral curve of Xv with initial condition e and δe is the integral curve of Xw initial
condition e. However, this is an easy exercise in the use of the Chain Rule .)
It is worth remarking explicitly that for any v ∈ g the formula for the ﬂow of the left
invariant vector ﬁeld Xv on G is simply
Φ(t,a ) = a exp(tv) = aetv.
(Warning: many beginners make the mistake of thinking that t he formula for the ﬂow of
the left invariant vector ﬁeld Xv should be Φ( t,a ) = exp(tv)a instead. It is worth pausing
for a moment to think why this is not so.)
It is now possible to describe all of the homomorphisms from t he Lie group ( R, +)
into any given Lie group:
Proposition 5: Every Lie group homomorphism φ : R → G is of the form φ(t) = etv
where v =φ′(0) ∈ g.
Proof: Let v =φ′(0) ∈ g, and let Xv be the associated left-invariant vector ﬁeld on G.
Since φ(0) = e, by ode uniqueness, it suﬃces to show that φ is an integral curve of Xv.
However,φ(s +t) = φ(s)φ(t) implies φ′(s) = L′
φ(s)
(
φ′(0)
)
=Xv
(
φ(s)
)
, as desired. □
The Exponential Map. We are now ready to introduce one of the principal tools
in the study of Lie groups.
Deﬁnition 6: For any Lie group, the exponential mapping of G is the mapping exp :
g →G deﬁned by exp(v) = γe(1) where γe is the integral curve of the vector ﬁeld Xv with
initial condition e .
It is an exercise for the reader to show that exp : g →G is smooth and that
exp′(0) : g →TeG = g
is just the identity mapping.
L.2.8 19

Example: As has been seen, for GL( n, R) (or GL( V ) in general for that matter), the
formula for the exponential mapping is just the usual power s eries:
ex =I +x + 1
2x2 + 1
6x3 + · · ·.
This formula works for all matrix Lie groups as well, and can s implify considerably in
certain special cases. For example, for the group N3 deﬁned earlier (usually called the
Heisenberg group), one has
n3 =





0 x z
0 0 y
0 0 0


⏐
⏐
⏐
⏐
⏐x,y,z ∈ R


,
and v3 = 0 for all v ∈ n3. Thus
exp




0 x z
0 0 y
0 0 0



 =


1 x z + 1
2xy
0 1 y
0 0 1

.
The Lie Bracket. Now, the mapping exp is not generally a homomorphism from
g (with its additive group structure) to G, although, in a certain sense, it comes as close
as possible, since, by construction, it is a homomorphism when restricted to any one-
dimensional linear subspace Rv ⊂ g. We now want to spend a few moments considering
what the multiplication map on G “looks like” when pulled back to g via exp.
Since exp ′(0) : g → TeG = g is the identity mapping, it follows from the Implicit
Function Theorem that there is a neighborhood U of 0 ∈ g so that exp : U → G is a
diﬀeomorphism onto its image. Moreover, there must be a smal ler open neighborhood
V ⊂ U of 0 so that µ
(
exp(V ) × exp(V )
)
⊂ exp(U ). It follows that there is a unique
smooth mapping ν :V ×V →U such that
µ (exp(x), exp(y)) = exp (ν(x,y )).
Since exp is a homomorphism restricted to each line through 0 in g, it follows that ν
satisﬁes
ν(αx,βx ) = (α +β)x
for all x ∈V and α,β ∈ R such that αx,βx ∈V .
Sinceν(0, 0) = 0, the Taylor expansion to second order of ν about (0, 0) is of the form,
ν(x,y ) = ν1(x,y ) + 1
2ν2(x,y ) +R3(x,y )
whereνi is a g-valued polynomial of degree i on the vector space g ⊕ g andR3 is a g-valued
function on V that vanishes to at least third order at (0 , 0).
L.2.9 20

Since ν(x, 0) = ν(0,x ) = x, it easily follows that ν1(x,y ) = x +y and that ν2(x, 0) =
ν2(0,y ) = 0. Thus, the quadratic polynomial ν2 is linear in each g-variable separately.
Moreover, since ν(x,x ) = 2x for all x ∈V , substituting this into the above expansion
and comparing terms of order 2 yields that ν2(x,x ) ≡ 0. Of course, this implies that ν2 is
actually skew-symmetric since
0 = ν2(x +y,x +y) −ν2(x,x ) −ν2(y,y ) = ν2(x,y ) +ν2(y,x ).
Deﬁnition 7: The skew-symmetric, bilinear multiplication [ , ] : g × g → g deﬁned by
[x,y ] = ν2(x,y )
is called the Lie bracket in g. The pair ( g, [, ]) is called the Lie algebra of G.
With this notation, one obtains a formula
exp(x) exp(y) = exp
(
x +y + 1
2 [x,y ] +R3(x,y )
)
valid for all x and y in some ﬁxed open neighborhood of 0 in g.
One might think of the term involving [ , ] as the ﬁrst deviation of the Lie group
multiplication from being just vector addition. In fact, it is clear from the above formula
that, if the group G is abelian, then [x,y ] = 0 for all x,y ∈ g. For this reason, a Lie algebra
in which all brackets vanish is called an abelian Lie algebra. (In fact, (see the Exercises)
g being abelian implies that G◦, the identity component of G, is abelian.)
Example : IfG = GL(n, R), then it is easy to see that the induced bracket operation on
gl(n, R), the vector space of n-by-n matrices, is just the matrix “commutator”
[x,y ] = xy −yx.
In fact, the reader can verify this by examining the followin g second order expansion:
exey = (In +x + 1
2x2 + · · ·)(In +y + 1
2y2 + · · ·)
= (In +x +y + 1
2 (x2 + 2xy +y2) + · · ·)
= (In + (x +y + 1
2 [x,y ]) + 1
2 (x +y + 1
2 [x,y ])2 + · · ·)
Moreover, this same formula is easily seen to hold for any x andy in gl(V ) where V is any
ﬁnite dimensional vector space.
Theorem 1: Ifφ :H →G is a Lie group homomorphism, then ϕ =φ′(e) : h → g satisﬁes
expG(ϕ(x)) = φ(expH (x))
for all x ∈ h. In other words, the diagram
h
ϕ
− → g
expH


↓


↓ expG
H
φ
− → G
commutes. Moreover, for all x and y in h,
ϕ([x,y ]H) = [ϕ(x),ϕ (y)]G.
L.2.10 21

Proof: The ﬁrst statement is an immediate consequence of Propositi on 5 and the Chain
Rule since, for every x ∈ h, the map γ : R →G given byγ(t) = φ(etx) is clearly a Lie group
homomorphism with initial velocity γ′(0) = ϕ(x) and hence must also satisfy γ(t) = etϕ(x).
To get the second statement, let x and y be elements of h that are suﬃciently close
to zero. Then, using self-explanatory notation:
φ(expH (x) expH(y)) = φ(expH (x))φ(expH (y)),
so
φ(expH (x +y + 1
2 [x,y ]H +RH
3 (x,y ))) = expG(ϕ(x)) expG(ϕ(y)),
and thus
expG(ϕ(x +y + 1
2 [x,y ]H +RH
3 (x,y ))) = expG(ϕ(x) +ϕ(y) + 1
2 [ϕ(x),ϕ (y)]G +RG
3 (ϕ(x),ϕ (y))),
ﬁnally giving
ϕ(x +y + 1
2 [x,y ]H +RH
3 (x,y )) = ϕ(x) +ϕ(y) + 1
2 [ϕ(x),ϕ (y)]G +RG
3 (ϕ(x),ϕ (y)).
Now using the fact that ϕ is linear and comparing second order terms gives the desired
result. □
On account of this theorem, it is usually not necessary to dis tinguish the map exp
or the bracket [ , ] according to the group in which it is being applied, so I will follow this
practice also. Henceforth, these symbols will be used witho ut group decorations whenever
confusion seems unlikely.
Theorem 1 has many useful corollaries. Among them is
Proposition 6: If H is a connected Lie group and φ1,φ 2 : H → G are two Lie group
homomorphisms that satisfy φ′
1(e) = φ′
2(e), then φ1 =φ2.
Proof: There is an open neighborhood U of e in H so that exp H is invertible on this
neighborhood with inverse satisfying exp −1
H (e) = 0. Then for a ∈U one has, by Theorem
1,
φi(a) = expG(ϕi(exp−1
H (a))).
Since ϕ1 = ϕ2, one has φ1 = φ2 on U . By Proposition 2, every element of H can be
written as a ﬁnite product of elements of U , so one must have φ1 =φ2 everywhere. □
We also have the following fundamental result:
Proposition 7: If Ad : G → GL(g) is the adjoint representation, then ad = Ad ′(e) : g →
gl(g) is given by the formula ad(x)(y) = [x,y ]. In particular, one has the Jacobi identity
ad([x,y ]) = [ad(x), ad(y)].
Proof: This is simply a matter of unwinding the deﬁnitions. By deﬁni tion, Ad(a) = C′
a(e)
where Ca :G →G is deﬁned by Ca(b) = aba−1. In order to compute C′
a(e)(y) for y ∈ g,
L.2.11 22

one may just compute γ′(0) where γ is the curve γ(t) = a exp(ty)a−1. Moreover, since
exp′(0) : g → g is the identity, one may as well compute β′(0) where β = exp −1 ◦γ. Now,
assuming a = exp(x), one computes
β(t) = exp −1(exp(x) exp(ty) exp(−x))
= exp −1(exp(x +ty + 1
2 [x,ty ] + · · ·) exp(−x))
= exp −1(exp((x +ty + 1
2 [x,ty ]) + (−x) + 1
2 [x +ty, −x] + · · ·)
=ty +t[x,y ] +E3(x,ty )
where the omitted terms and the function E3 vanish to order at least 3 at ( x,y ) = (0, 0).
(Note that I used the identity [ y,x ] = −[x,y ].) It follows that
Ad(exp(x))(y) = β′(0) = y + [x,y ] +E′
3(x, 0)y
where E′
3(x, 0) denotes the derivative of E3 with respect to y evaluated at ( x, 0) and is
hence a function of x that vanishes to order at least 2 at x = 0. On the other hand, by
the ﬁrst part of Theorem 1,
Ad(exp(x)) = exp(ad(x)) = I + ad(x) + 1
2 (ad(x))2 + · · ·.
Comparing the x-linear terms in the last two equations clearly gives the des ired result.
The validity of the Jacobi identity now follows by applying t he second part of Theorem 1
to Proposition 3. □
The Jacobi identity is often presented diﬀerently. The read er can verify that the
equation ad
(
[x,y ]
)
=
[
ad(x), ad(y)
]
where ad(x)(y) = [x,y ] is equivalent to the condition
that [
[x,y ],z
]
+
[
[y,z ],x
]
+
[
[z,x ],y
]
= 0 for all z ∈ g.
This is a form in which the Jacobi identity is often stated. Un fortunately, although this is
a very symmetric form of the identity, it somewhat obscures i ts importance and meaning.
The Jacobi identity is so important that the class of algebra s in which it holds is given
a name:
Deﬁnition 8: A Lie algebra is a pair ( g, [, ]) where g is a vector space and [ , ] : g×g → g is
a skew-symmetric bilinear multiplication that satisﬁes th e Jacobi identity, i.e., ad([x,y ]) =
[ad(x), ad(y)], where ad : g → gl(g) is deﬁned by ad( x)(y) = [x,y ] A Lie subalgebra of g is
a linear subspace h ⊂ g that is closed under bracket. A homomorphism of Lie algebras is
a linear mapping of vector spaces ϕ : h → g that satisﬁes
ϕ
(
[x,y ]
)
=
[
ϕ(x),ϕ (y)
]
.
The only examples of Lie algebras encountered so far are the o nes provided by Propo-
sition 6, namely, the Lie algebras of Lie groups. This is not a ccidental, for, as will be seen,
every ﬁnite dimensional Lie algebra is the Lie algebra of som e Lie group.
L.2.12 23

Lie Brackets of V ector Fields. There is another notion of Lie bracket, namely
the Lie bracket of smooth vector ﬁelds on a smooth manifold. T his bracket is also skew-
symmetric and satisﬁes the Jacobi identity, so it is reasona ble to ask how it might be
related to the notion of Lie bracket that has already been deﬁ ned. Since Lie bracket of
vector ﬁelds commutes with diﬀeomorphisms, it easily follo ws that the Lie bracket of two
left-invariant vector ﬁelds on a Lie group G is also a left-invariant vector ﬁeld on G. The
following result is, perhaps then, to be expected.
Proposition 8: For any x,y ∈ g, one has [Xx,Xy] = X[x,y].
Proof: This is a direct calculation. For simplicity, I will use the f ollowing characterization
of the Lie bracket for vector ﬁelds: If Φ x and Φ y are the ﬂows associated to the vector
ﬁelds Xx and Xy, then for any function f on G one has the formula:
([Xx,Xy]f )(a) = lim
t→0+
f (Φy(−
√
t, Φx(−
√
t, Φy(
√
t, Φx(
√
t,a ))))) −f (a)
t .
Now, as has been seen, the formulas for the ﬂows of Xx and Xy are given by Φ x(t,a ) =
a exp(tx) and Φ y(t,a ) = a exp(ty). This implies that the general formula above simpliﬁes
to
([Xx,Xy]f )(a) = lim
t→0+
f
(
a exp(
√
tx) exp(
√
ty) exp(−
√
tx) exp(−
√
ty)
)
−f (a)
t .
Now
exp(±
√
tx) exp(±
√
ty) = exp( ±
√
t(x +y) + t
2 [x,y ] + · · ·)
so exp(
√
tx) exp(
√
ty) exp(−
√
tx) exp(−
√
ty) simpliﬁes to exp(t[x,y ] +· · ·) where the omit-
ted terms vanish to higher t-order than t itself. Thus,
([Xx,Xy]f )(a) = lim
t→0+
f
(
a exp(t[x,y ] + · · ·)
)
−f (a)
t .
Since [Xx,Xy] must be a left-invariant vector ﬁeld and since
(X[x,y]f )(a) = lim
t→0+
f
(
a exp(t[x,y ])
)
−f (a)
t ,
the desired result follows. □
We can now prove the following fundamental result.
Theorem 2: For each Lie subgroup H of a Lie group G, the subspace h =TeH is a Lie
subalgebra of g. Moreover, every Lie subalgebra h ⊂ g is TeH for a unique connected Lie
subgroup H of G.
L.2.13 24

Proof: Suppose that H ⊂G is a Lie subgroup. Then the inclusion map is a Lie group
homomorphism and Theorem 1 thus implies that the inclusion m ap h֒→g is a Lie algebra
homomorphism. In particular, h, when considered as a subspace of g, is closed under the
Lie bracket in G and hence is a subalgebra.
Suppose now that h ⊂ g is a subalgebra.
First, let us show that there is at most one connected Lie subg roup of G with Lie
algebra h. Suppose that there were two, say H1 and H2. Then by Theorem 1, exp G(h) is
a subset of both H1 and H2 and contains an open neighborhood of the identity element
in each of them. However, since, by Proposition 2, each of H1 and H2 are generated by
ﬁnite products of the elements in any open neighborhood of th e identity, it follows that
H1 ⊂H2 and H2 ⊂H1, so H1 =H2, as desired.
Second, the existence of a subgroup H with TeH = h, will be proved by calling on
the Global Frobenius Theorem. Let r = dim( h) and let E ⊂ TG be the rank r sub-
bundle spanned by the vector ﬁelds Xx where x ∈ h. Note that Ea = L′
a(Ee) = L′
a(h)
for all a ∈ G, so E is left-invariant. Since h is a subalgebra of g, Proposition 8 implies
that E is an integrable distribution on G. By the Global Frobenius Theorem, there is an
r-dimensional leaf of E passing through e. Call this E-leaf H.
It remains to show that H is closed under multiplication and inverse. To do this, ﬁrst
note that, because E is left-invariant, it follows that, for any a ∈ G, the leaf of E that
passes through a is La(H) = aH. Now, if a lies in H, then aH ∩H contains a (since H
containse) and hence the two E-leavesaH andH must be equal. Since aH =H it follows
thatab lies inH if both a andb do, so that H is closed under multiplication. Since aH =H
and H passes through e, it follows that there is a b ∈H such that ab =e. Thus, b =a−1
belongs to H as well. Thus, H is closed under inverse. □
Theorem 3: IfH is a connected and simply connected Lie group, then, for any L ie group
G, each Lie algebra homorphism ϕ : h → g is of the form ϕ = φ′(e) for some unique Lie
group homorphism φ :H →G.
Proof: In light of Theorem 1 and Proposition 6, all that remains to be proved is that
for each Lie algebra homorphism ϕ : h → g there exists a Lie group homomorphism φ
satisfying φ′(e) = ϕ.
We do this as follows: Suppose that ϕ : h → g is a Lie algebra homomorphism.
Consider the product Lie group H ×G. Its Lie algebra is h ⊕ g with Lie bracket given
by [(h1,g 1), (h2,g 2)] = ([h1,h 2], [g1,g 2]), as is easily veriﬁed. Now consider the subspace
ˆh ⊂ h ⊕ g spanned by elements of the form ( x,ϕ (x)) where x ∈ h. Since ϕ is a Lie algebra
homomorphism,ˆh is a Lie subalgebra of h ⊕ g (and happens to be isomorphic to h). In
particular, by Theorem 2, it follows that there is a connecte d Lie subgroup ˆH ⊂ H ×G,
whose Lie algebra is ˆh. We are now going to show that ˆH is the graph of the desired Lie
group homomorphism φ :H →G.
Note that since ˆH is a Lie subgroup of H ×G, the projections π1 : ˆH → H and
π2 : ˆH →G are Lie group homomorphisms. The associated Lie algebra hom omorphisms
̟1 :ˆh → h and ̟2 :ˆh → g are clearly given by ̟1(x,ϕ (x)) = x and ̟2(x,ϕ (x)) = ϕ(x).
L.2.14 25

Now, I claim that π1 is actually a surjective covering map: It is surjective sinc e
̟1 :ˆh → h is an isomorphism so π1(ˆH) contains a neighborhood of the identity in H and
hence, by Proposition 2 and the connectedness of H, must contain all of H. It remains to
show that, under π1, points of H have evenly covered neighborhoods.
Let ˆZ = ker(π1). Then ˆZ is a closed discrete subgroup of ˆH. Let ˆU ⊂ ˆH be a
neighborhood of the identity to which π1 restricts to be a smooth diﬀeomorphism onto
a neighborhood U of e in H. Then the reader can easily verify that for each a ∈ ˆH the
mapσa : ˆZ ×ˆU → ˆH given by σa(z,u ) = azu is a diﬀeomorphism onto ( π1)−1(Lπ1(a)(U ))
that commutes with the appropriate projections and hence es tablishes the even covering
property.
Finally, since ˆH is connected and, by hypothesis, H is simply connected, it follows
that π1 must actually be a one-to-one and onto diﬀeomorphism. The ma pφ =π2 ◦π−1
1 is
then the desired homomorphism. □
As one ﬁnal general Theorem, I state, without proof, the foll owing existence result.
Theorem 4: For each ﬁnite dimensional Lie algebra g, there exists a Lie group G whose
Lie algebra is isomorphic to g.
Unfortunately, this theorem is surprisingly diﬃcult to pro ve. It would suﬃce, by
Theorem 2, to show that every Lie algebra g is isomorphic to a subalgebra of the Lie
algebra of a Lie group. In fact, an even stronger statement is true. A theorem of Ado
asserts that every ﬁnite dimensional Lie algebra is isomorp hic to a subalgebra of gl(n, R)
for some n. Thus, to prove Theorem 4, it would be enough to prove Ado’s th eorem.
Unfortunately, this theorem also turns out to be rather deli cate (see [Po] for a proof).
However, there are many interesting examples of g for which a proof can be given by
elementary means (see the Exercises).
On the other hand, this abstract existence theorem is not use d very often anyway.
It is rare that a (ﬁnite dimensional) Lie algebra arises in pr actice that is not readily
representable as the Lie algebra of some Lie group.
The reader may be wondering about uniqueness: How many Lie gr oups are there
whose Lie algebras are isomorphic to a given g? Since the Lie algebra of a Lie group
G only depends on the identity component G, it is reasonable to restrict to the case of
connected Lie groups. Now, as you are asked to show in the Exer cises, the universal cover
˜G of a connected Lie group G can be given a unique Lie group structure for which the
covering map ˜G → G is a homomorphism. Thus, there always exists a connected and
simply connected Lie group, say G(g), whose Lie algebra is isomorphic to g. A simple
application of Theorem 3 shows that if G′ is any other Lie group with Lie algebra g, then
there is a homomorphism φ :G(g) →G that induces an isomorphism on the Lie algebras.
It follows easily that, up to isomorphism, there is only one s imply-connected and connected
Lie group with Lie algebra g. Moreover, every other connected Lie group with Lie algebra
G is isomorphic to a quotient of G(g) by a discrete subgroup of G that lies in the center
of G(g) (see the Exercises).
L.2.15 26

The Structure Constants. Our work so far has shown that the problem of classify-
ing the connected Lie groups up to isomorphism is very nearly the same thing as classifying
the (ﬁnite dimensional) Lie algebras. (See the Exercises fo r a clariﬁcation of this point.)
This is a remarkable state of aﬀairs, since, a priori , Lie groups involve the topology of
smooth manifolds and it is rather surprising that their clas siﬁcation can be reduced to
what is essentially an algebra problem. It is worth taking a c loser look at this algebra
problem itself.
Let g be a Lie algebra of dimension n, and let x1,x 2,...,x n be a basis for g. Then
there exist constants ck
ij so that (using the summation convention)
[xi,xj] = ck
ijxk.
(These quantities c are called the structure constants of g relative to the given basis.) The
skew-symmetry of the Lie bracket is is equivalent to the skew -symmetry of c in its lower
indices:
ck
ij +ck
ji = 0.
The Jacobi identity is equivalent to the quadratic equation s:
cℓ
ijcm
kℓ +cℓ
jkcm
iℓ +cℓ
kicm
jℓ = 0.
Conversely, any set of n3 constants satisfying these relations deﬁnes an n-dimensional Lie
algebra by the above bracket formula.
Of course, because of the skew-symmetry of the bracket, only n
(n
2
)
of these constants
are independent. In fact, using the dual basis x1,...,x n of g∗, one can write the expression
for the Lie bracket as an element β ∈ g ⊗ Λ 2(g∗), in the form
β = 1
2ci
jkxi ⊗xj ∧xk.
The Jacobi identity is then equivalent to the condition J(β) = 0, where
J : g ⊗ Λ 2(g∗) → g ⊗ Λ 3(g∗)
is the quadratic polynomial map given in coordinates by
J(β) = 1
6
(
cℓ
ijcm
kℓ +cℓ
jkcm
iℓ +cℓ
kicm
jℓ
)
xm ⊗xi ∧xj ∧xk.
L.2.16 27

Left-Invariant F orms and the Structure Equations. Dual to the left-invariant
vector ﬁelds on a Lie group G, there are the left-invariant 1-forms, which are indispens able
as calculational tools.
Deﬁnition 9: For any Lie group G, the g-valued 1-form on G deﬁned by
ωG(v) = L′
a−1 (v) for v ∈TaG
is called the canonical left-invariant 1-form on G.
It is easy to see that ωG is smooth. Moreover, ωG is the unique left-invariant g-valued
1-form on G that satisﬁes ωG(v) = v for all v ∈ g =TeG.
By a calculation that is left as an exercise for the reader,
φ∗(ωG) = ϕ(ωH )
for any Lie group homomorphism φ :H →G with ϕ =φ′(e). In particular, when H is a
subgroup of G, the pull back of ωG to H via the inclusion mapping is just ωH . For this
reason, it is common to simply write ω for ωG when there is no danger of confusion.
Example: If G ⊂ GL(n, R) is a matrix Lie group, then one may regard the inclusion
g : G → GL(n, R) as a matrix-valued function on G and compute that ω is given by the
simple formula
ω =g−1dg.
From this formula, the left-invariance of ω is obvious.
In the matrix Lie group case, it is also easy to compute the ext erior derivative of ω:
Since gg −1 =In, one obtains
dgg −1 +gd
(
g−1)
= 0,
so
d
(
g−1)
= −g−1dgg −1.
This implies the formula
dω = −ω ∧ω.
(Warning: Matrix multiplication is implicit in this formul a!)
For a general Lie group, the formula for dω is only slightly more complicated. To
state the result, let me ﬁrst deﬁne some notation. I will use [ ω,ω ] to denote the g-valued
2-form on G whose value on a pair of vectors v,w ∈TaG is
[ω,ω ](v,w ) = [ω(v),ω (w)] − [ω(w),ω (v)] = 2[ω(v),ω (w)].
Proposition 9: For any Lie group G, dω = − 1
2 [ω,ω ].
L.2.17 28

Proof: First, let Xv and Xw be the left-invariant vector ﬁelds on G whose values at e
are v and w respectively. Then, by the usual formula for the exterior de rivative
dω(Xv,Xw) = Xv
(
ω(Xw)
)
−Xw
(
ω(Xv)
)
−ω
(
[Xv,Xw]
)
.
However, the g-valued functions ω(Xv) and ω(Xw) are clearly left-invariant and hence are
constants and equal to v and w respectively. Moreover, by Proposition 8, [ Xv,Xw] =
X[v,w], so the formula simpliﬁes to
dω(Xv,Xw) = −ω
(
X[v,w]
)
.
The right hand side is, again, a left-invariant function, so it must equal its value at the
identity, which is clearly −[v,w ], that equals −[ω(Xv),ω (Xw)] Thus,
dω(Xv,Xw) = − 1
2 [ω(Xv),ω (Xw)]
for any pair of left-invariant vector ﬁelds on G. Since any pair of vectors in TaG can be
written as Xv(a) and Xw(a) for some v,w ∈ g, the result follows. □
The formula proved in Proposition 9 is often called the structure equation of Maurer
and Cartan. It is also usually expressed slightly diﬀerentl y. If x1,x 2,...,x n is a basis for
g with structure constants ci
jk , then ω can be written in the form
ω =x1ω1 + · · · +xnωn
where the ωi are R-valued left-invariant 1-forms and Proposition 9 can then b e expanded
to give
dωi = − 1
2ci
jkωj ∧ωk,
which is the most common form in which the structure equation s are given. Note that the
identityd(d(ωi)) = 0 is equivalent to the Jacobi identity.
An Extended Example: 2- and 3-dimensional Lie Algebras. It is clear that
up to isomorphism, there is only one (real) Lie algebra of dim ension 1, namely g = R with
the zero bracket. This is the Lie algebra of the connected Lie groups R and S1. (You are
asked to prove in an exercise that these are, in fact, the only connected one-dimensional
Lie groups.)
The ﬁrst interesting case, therefore, is dimension 2. If g is a 2-dimensional Lie alge-
bra with basis x1,x 2, then the entire Lie algebra structure is determined by the b racket
[x1,x 2] = a1x1 +a2x2. If a1 =a2 = 0, then all brackets are zero, and the algebra is abelian.
If one of a1 or a2 is non-zero, then, by switching x1 and x2 if necessary, one may assume
thata1 ⁄= 0. Then, considering the new basis y1 =a1x1 +a2x2 andy2 = (1/a1)x2, one ob-
tains [y1,y 2] = y1. Since the Jacobi identity is easily veriﬁed for this Lie bra cket, this does
deﬁne a Lie algebra. Thus, up to isomorphism, there are only t wo distinct 2-dimensional
Lie algebras.
L.2.18 29

The abelian example is, of course, the Lie algebra of the vect or space R2 (as well as
the Lie algebra of S1 × R, and the Lie algebra of S1 ×S1).
An example of a Lie group of dimension 2 with a non-abelian Lie algebra is the matrix
Lie group
G =
{(
a b
0 1
)⏐
⏐
⏐
⏐a ∈ R+, b ∈ R
}
.
In fact, it is not hard to show that, up to isomorphism, this is the only connected non-
abelian Lie group of dimension 2 (see the Exercises).
Now, let us pass on to the classiﬁcation of the three dimensio nal Lie algebras. Here,
the story becomes much more interesting. Let g be a 3-dimensional Lie algebra, and let
x1,x 2,x 3 be a basis of g. Then, one may write the bracket relations in matrix form as
( [x2,x 3] [ x3,x 1] [ x1,x 2] ) = ( x1 x2 x3 )C
where C is the 3-by-3 matrix of structure constants. How is this matr ix aﬀected by a
change of basis? Well, let
( y1 y2 y3 ) = ( x1 x2 x3 )A
where A ∈ GL(3, R). Then it is easy to compute that
( [y2,y 3] [ y3,y 1] [ y1,y 2] ) = ( [ x2,x 3] [ x3,x 1] [ x1,x 2] ) Adj(A)
where Adj(A) is the classical adjoint matrix of A, i.e., the matrix of 2-by-2 minors. Thus,
A−1 = (det(A))−1tAdj(A).
(Do not confuse this with the adjoint mapping deﬁned earlier !) It then follows that
( [y2,y 3] [ y3,y 1] [ y1,y 2] ) = ( y1 y2 y3 )C′,
where
C′ =A−1C Adj(A) = det(A)A−1CtA−1.
It follows without too much diﬃculty that, if one writes C =S + ˆa, where S is a symmetric
3-by-3 matrix and
ˆa =


0 −a3 a2
a3 0 −a1
−a2 a1 0

 where a =


a1
a2
a3

,
then C′ =S′ +ˆa′, where
S′ = det(A)A−1StA−1 and a′ = tAa.
L.2.19 30

Now, I claim that the condition that the Jacobi identity hold for the bracket deﬁned
by the matrix C is equivalent to the condition Sa = 0. To see this, note ﬁrst that
[[x2,x 3],x 1] + [[x3,x 1],x 2] + [[x1,x 2],x 3]
= [C1
1x1 +C2
1x2 +C3
1x3,x 1]+[C1
2x1 +C2
2x2 +C3
2x3,x 2]+[C1
3x1 +C2
3x2 +C3
3x3,x 3]
= (C2
3 −C3
2 )[x2,x 3] + (C3
1 −C1
3 )[x3,x 1] + (C1
2 −C2
1 )[x1,x 2]
= 2a1[x2,x 3] + 2a2[x3,x 1] + 2a3[x1,x 2]
= 2 ( [x2,x 3] [ x3,x 1] [ x1,x 2] ) a
= 2 ( x1 x2 x3 )Ca,
and Ca = (S + ˆa)a = Sa since ˆaa = 0. Thus, the Jacobi identity applied to the basis
x1,x 2,x 3 implies that Sa = 0. However, if y1,y 2,y 3 is any other triple of elements of g,
then for some 3-by-3 matrix B, one has
( y1 y2 y3 ) = ( x1 x2 x3 )B,
and I leave it to the reader to check that
[[y2,y 3],y 1]+[[y3,y 1],y 2]+[[y1,y 2],y 3] = det(B) ([[x2,x 3],x 1] + [[x3,x 1],x 2] + [[x1,x 2],x 3])
in this case. Thus, Sa = 0 implies the full Jacobi identity.
There are now two essentially diﬀerent cases to treat.
In the ﬁrst case, if a = 0, then the Jacobi identity is automatically satisﬁed, and
S can be any symmetric matrix. However, two such choices S and S′ will clearly give
rise to isomorphic Lie algebras if and only if there is an A ∈ GL(3, R) for which S′ =
det(A)A−1StA−1. I leave as an exercise for the reader to show that every choic e of S
yields an algebra (with a = 0) that is equivalent to exactly one of the algebras made by
one of the following six choices for S:


0 0 0
0 0 0
0 0 0




0 1 0
1 0 0
0 0 0




0 1 0
1 0 0
0 0 1




1 0 0
0 0 0
0 0 0




1 0 0
0 1 0
0 0 0




1 0 0
0 1 0
0 0 1


.
In the second case, if a ⁄= 0, then by a suitable change of basis A, one can assume that
a1 =a2 = 0 and that a3 = 1. Any change of basis A that preserves this normalization is
seen to be of the form
A =


A1
1 A1
2 A1
3
A2
1 A2
2 A2
3
0 0 1

.
L.2.20 31

Since Sa = 0 and since S is symmetric, it follows that S must be of the form
S =


s11 s12 0
s12 s22 0
0 0 0

.
Moreover, a simple calculation shows that the result of appl ying a change of basis of the
above form is to change the matrix S into the matrix
S′ =


s′
11 s′
12 0
s′
12 s′
22 0
0 0 0


where
(
s′
11 s′
12
s′
12 s′
22
)
= 1
A1
1A2
2 −A1
2A2
1
(
A2
2 −A1
2
−A2
1 A1
1
)(
s11 s12
s12 s22
)(
A2
2 −A2
1
−A1
2 A1
1
)
.
It follows that s′
11s′
22 − (s′
12)2 =s11s22 − (s12)2, so there is an ‘invariant’ to be considered.
I leave it to the reader to show that the upper left-hand 2-by- 2 block of S can be brought
by a change of basis of the above form into exactly one of the fo ur forms
(
0 0
0 0
) (
1 0
0 0
) (
σ 0
0 σ
) (
σ 0
0 −σ
)
where σ >0 is a real positive number.
To summarize, every 3-dimensional Lie algebra is isomorphi c to exactly one of the
following Lie algebras: Either
so(3) :
[x2,x 3] = x1
[x3,x 1] = x2
[x1,x 2] = x3
or sl(2, R) :
[x2,x 3] = x2
[x3,x 1] = x1
[x1,x 2] = x3
or an algebra of the form
[x2,x 3] = b11x1 +b12x2
[x3,x 1] = b21x1 +b22x2
[x1,x 2] = 0
where the 2-by-2 matrix B is one of the following
(
0 0
0 0
) (
1 0
0 0
) (
1 0
0 1
) (
0 1
1 0
)
(
0 1
−1 0
) (
1 1
−1 0
) (
σ 1
−1 σ
) (
σ 1
−1 −σ
)
L.2.21 32

and, in the latter two cases, σ is a positive real number. Each of these eight latter types
can be represented as a subalgebra of gl(3, R) in the form
g =





(1 +b21)z −b11z x
b22z (1 −b12)z y
0 0 z


⏐
⏐
⏐
⏐
⏐x,y,z ∈ R



I leave as an exercise for the reader to show that the correspo nding subgroup of GL(3 , R)
is a closed, embedded, simply connected matrix Lie group who se underlying manifold is
diﬀeomorphic to R3.
L.2.22 33

Exercise Set 2:
Lie Groups
1. Show that for any real vector space of dimension n, the Lie group GL( V ) is isomorphic
to GL(n, R). (Hint: Choose a basis b of V , use b to construct a mapping φb: GL(V ) →
GL(n, R), and then show that φb is a smooth isomorphism.)
2. Let G be a Lie group and let H be an abstract subgroup. Show that if there is an open
neighborhood U ofe inG so that H ∩U is a smooth embedded submanifold of G, then H
is a Lie subgroup of G.
3. Show that SL( n, R) is an embedded Lie subgroup of GL( n, R). (Hint: SL( n, R) =
det−1(1).)
4. Show that O( n) is an compact Lie subgroup of GL( n, R). (Hint: O( n) = F −1(In),
whereF is the map from GL( n, R) to the vector space of n-by-n symmetric matrices given
by F (A) = tAA . Taking note of Exercise 2, show that the Implicit Function T heorem
applies. To show compactness, apply the Heine-Borel theore m.) Show also that SO( n) is
an open-and-closed, index 2 subgroup of O( n).
5. Carry out the analysis in Exercise 3 for the complex matrix L ie group SL(n, C) and the
analysis in Exercise 4 for the complex matrix Lie groups U( n) and SU(n). What are the
(real) dimensions of all of these groups?
6. Show that the map µ: O(n) ×An ×Nn → GL(n, R) deﬁned by matrix multiplication
is a diﬀeomorphism although it is not a group homomorphism. (Hint: The map is clearly
smooth, you must only compute an inverse. To get the ﬁrst fact orν1: GL(n, R) → O(n) of
the inverse map, think of an element b ∈ GL(n, R) as a row of column vectors in Rn and
let ν1(b) be the row of column vectors that results from b by apply the Gram-Schmidt
orthogonalization process. Why does this work and why is the resulting map ν1 smooth?)
Show, similarly that the map
µ: SO(n) ×
(
An ∩ SL(n, R)
)
×Nn → SL(n, R)
is a diﬀeomorphism. Are there similar factorizations for th e groups GL(n, C) and SL(n, C)?
(Hint: Consider unitary bases rather than orthogonal ones. )
7. Show that
SU(2) =
{(
a −
b
b a
)
aa +bb = 1
}
.
Conclude that SU(2) is diﬀeomorphic to the 3-sphere and, usi ng the previous exercise,
that, in particular, SL(2 , C) is simply connected, while π1
(
SL(2, R)
)
≃ Z.
E.2.1 34

8. Show that, for any Lie group G, the mappings La satisfy
L′
a(b) = L′
ab(e) ◦ (L′
b(e))−1.
where L′
a(b):TbG → TabG. (This shows that the eﬀect of left translation is completel y
determined by what it does at e.) State and prove a similar formula for the mappings Ra.
9. Let (G,µ ) be a Lie group. Using the canonical identiﬁcation T(a,b)(G×G) = TaG⊕TbG,
prove the formula
µ′(a,b )(v,w ) =R′
b(a)(v) +L′
a(b)(w)
for all v ∈TaG and w ∈TbG.
10. Complete the proof of Proposition 3 by explicitly exhibiti ng the mapc as a composition
of known smooth maps. (Hint: if f :X →Y is smooth, then f ′:TX →TY is also smooth.)
11. Show that, for any v ∈ g, the left-invariant vector ﬁeld Xv is indeed smooth. Also prove
the ﬁrst statement in Proposition 4. (Hint: Use Ψ to write the mapping Xv:G →TG as
a composition of smooth maps. Show that the assignment v ↦→Xv is linear. Finally, show
that if a left-invariant vector ﬁeld on G vanishes anywhere, then it vanishes identically.)
12. Show that exp: g →G is indeed smooth and that exp ′: g → g is the identity mapping.
(Hint: Write down a smooth vector ﬁeld Y on g ×G such that the integral curves of Y are
of the form γ(t) = (v0,a 0etv0 ). Now use the ﬂow of Y ,
Ψ: R × g ×G → g ×G,
to write exp as the composition of smooth maps.)
13. Show that, for the homomorphism det: GL( n, R) → R•, we have det ′(In)(x) = tr(x),
where tr denotes the trace function. Conclude, using Theore m 1 that, for any matrix a,
det(ea) = etr(a).
14. Prove that, for any g ∈G and any x ∈ g, we have the identity
g exp(x)g−1 = exp
(
Ad(g)(x)
)
.
(Hint: Replace x bytx in the above formula and consider Proposition 5.) Use this to show
that tr
(
exp(x)
)
≥ − 2 for all x ∈ sl(2, R). Conclude that exp: sl(2, R) → SL(2, R) is not
surjective. (Hint: show that every x ∈ sl(2, R) is of the form gyg −1 for some g ∈ SL(2, R)
and some y that is one of the matrices
(
0 ±1
0 0
)
,
(
λ 0
0 −λ
)
, or
(
0 −λ
λ 0
)
, (λ> 0).
Also, remember that tr
(
aba−1)
= tr(b).)
E.2.2 35

15. Using Theorem 1, show that if H1 and H2 are Lie subgroups of G, then H1 ∩H2 is
also a Lie subgroup of G. (Hint: What should the Lie algebra of this intersection be? Be
careful: H1 ∩H2 might have countably many distinct components even if H1 and H2 are
connected!)
16. For any skew-commutative algebra ( g, [, ]), we deﬁne the map ad: g → End(g) by
ad(x)(y) = [x,y ]. Verify that the validity of the Jacobi identity [ad( x), ad(y)] = ad([x,y ])
(where, as usual, the bracket on End( g) is the commutator) is equivalent to the validity of
the identity
[[x,y ],z ] + [[y,z ],x ] + [[z,x ],y ] = 0
for all x,y,z ∈ g.
17. Show that, as λ ∈ R varies, all of the groups
Gλ =
{(
a b
0 aλ
)⏐
⏐
⏐
⏐a ∈ R+, b ∈ R
}
withλ ⁄= 1 are isomorphic, but are not conjugate in GL(2 , R). What happens when λ = 1?
18. Show that a connected Lie group G is abelian if and only if its Lie algebra satisﬁes
[x,y ] = 0 for all x,y ∈ g. Conclude that a connected abelian Lie group of dimension n is
isomorphic to Rn/Zd where Zd is some discrete subgroup of rank d ≤n. (Hint: To show
‘G abelian’ implies ‘g abelian’, look at how [ , ] was deﬁned. To prove the converse, use
Theorem 3 to construct a surjective homomorphism φ: Rn →G with discrete kernel.)
19. ( Covering Spaces of Lie groups ) Let G be a connected Lie group and let π: ˜G →G be
the universal covering space of G. (Recall that the points of ˜G can be regarded as the space
of ﬁxed-endpoint homotopy classes of continuous maps γ: [0, 1] →G withγ(0) = e.) Show
that there is a unique Lie group structure ˜ µ: ˜G × ˜G → ˜G for which the homotopy class of
the constant map ˜e ∈ ˜G is the identity and so that π is a homomorphism. (Hints: Give ˜G
the (unique) smooth structure for which π is a local diﬀeomorphism. The multiplication
˜µ can then be deﬁned as follows: The map ¯ µ =µ ◦ (π ×π): ˜G × ˜G →G is a smooth map
and satisﬁes ¯µ(˜e, ˜e) = e. Since ˜G × ˜G is simply connected, the universal lifting property
of the covering map π implies that there is a unique map ˜ µ: ˜G × ˜G → ˜G that satisﬁes
π ◦ ˜µ = ¯µ and ˜µ(˜e, ˜e) = ˜e. Show that ˜µ is smooth, that it satisﬁes the axioms for a group
multiplication (associativity, existence of an identity, and existence of inverses), and that π
is a homomorphism. You will want to use the universal lifting property of covering spaces
a few times.)
The kernel of π is a discrete normal subgroup of ˜G. Show that this kernel lies in
the center of ˜G. In fact, show that, for any connected Lie group G, any discrete normal
subgroup H ⊂ G lies in the center of G. (Hint: For any z ∈ H, the connected set
{aza−1 | a ∈G} must also lie in H.)
Show that the center of the simply connected Lie group
G =
{(
a b
0 1
)⏐
⏐
⏐
⏐a ∈ R+, b ∈ R
}
E.2.3 36

is trivial, so any connected Lie group with the same Lie algeb ra is actually isomorphic
to G.
(In the next Lecture, we will show that whenever K is a closed normal subgroup of
a Lie group G, the quotient group G/K can be given the structure of a Lie group. Thus,
in many cases, one can eﬀectively list all of the connected Li e groups with a given Lie
algebra.)
20. Show that ~SL(2, R) is not a matrix group! In fact, show that any homomorphism
φ: ~SL(2, R) → GL(n, R) factors through the projections ~SL(2, R) → SL(2, R). (Hint: Re-
call, from earlier exercises, that the inclusion map SL(2 , R) → SL(2, C) induces the zero
map on π1 since SL(2, C) is simply connected. Now, any homomorphism φ: ~SL(2, R) →
GL(n, R) induces a Lie algebra homomorphism φ′(e): sl(2, R) → gl(n, R) and this may
clearly be complexiﬁed to yield a Lie algebra homomorphism φ′(e)C: sl(2, C) → gl(n, C).
Since SL(2, C) is simply connected, there must be a corresponding Lie grou p homorphism
φC: SL(2, C) → GL(n, C). Now suppose that φ does not factor through SL(2 , R), i.e.,
that φ is non-trivial on the kernel of ~SL(2, R) → SL(2, R), and show that this leads to a
contradiction.)
21. An ideal in a Lie algebra g is a linear subspace h that satisﬁes [ h, g] ⊂ h. Show that
the kernel k of a Lie algebra homomorphism ϕ: h → g is an ideal in h and that the image
ϕ(h) is a subalgebra of g. Conversely, show that if k ⊂ h is an ideal, then the quotient
vector space h/k carries a unique Lie algebra structure for which the quotien t mapping
h → h/k is a homomorphism.
Show that the subspace [ g, g] of g that is generated by all brackets of the form [ x,y ]
is an ideal in g. What can you say about the quotient g/[g, g]?
22. Show that, for a connected Lie group G, a connected Lie subgroup H is normal if and
only if h is an ideal of g. (Hint: Use Proposition 7 and the fact that H ⊂G is normal if
and only if exHe −x =H for all x ∈ g.)
23. For any Lie algebra g, let z(g) ⊂ g denote the kernel of the homomorphism ad: g →
gl(g). Use Theorem 2 and Exercise 16 to prove Theorem 4 for any Lie a lgebra g for which
z(g) = 0. (Hint: Look at the discussion after the statement of The orem 4.)
Show also that if g is the Lie algebra of the connected Lie group G, then the connected
Lie subgroupZ(g) ⊂G that corresponds to z(g) lies in the center of G. (In the next lecture,
we will be able to prove that the center of G is a closed Lie subgroup of G and that Z(g)
is actually the identity component of the center of G.)
24. For any Lie algebra g, there is a canonical bilinear pairing κ: g × g → R, called the
Killing form , deﬁned by the rule:
κ(x,y ) = tr
(
ad(x)ad(y)
)
.
E.2.4 37

(i) Show that κ is symmetric and, if g is the Lie algebra of a Lie group G, then κ is
Ad-invariant:
κ
(
Ad(g)x, Ad(g)y
)
=κ(x,y ) = κ(y,x ).
Show also that
κ
(
[z,x ],y
)
= −κ
(
x, [z,y ]
)
.
A Lie algebra g is said to be semi-simple if κ is a non-degenerate bilinear form on g.
(ii) Show that, of all the 2- and 3-dimensional Lie algebras, only so(3) and sl(2, R) are
semi-simple.
(iii) Show that if h ⊂ g is an ideal in a semi-simple Lie algebra g, then the Killing form
of h as an algebra is equal to the restriction of the Killing form o f g to h. Show also
that the subspace h⊥ = {x ∈ g |κ(x,y ) = 0 for all y ∈ h} is also an ideal in g and that
g = h ⊕ h⊥ as Lie algebras. (Hint: For the ﬁrst part, examine the eﬀect o f ad(x) on a
basis of g chosen so that the ﬁrst dim h basis elements are a basis of h.)
(iv) Finally, show that a semi-simple Lie algebra can be writ ten as a direct sum of ideals
hi, each of which has no proper ideals. (Hint: Apply (iii) as man y times as you can
ﬁnd proper ideals of the summands found so far.) A Lie algebra h of dimension greater
than 1 that has no proper ideals is said to be simple.
A more general class of Lie algebras are the reductive ones. W e say that a Lie algebra is
reductive if there is a non-degenerate symmetric bilinear form ( , ): g × g → R that satisﬁes
the identity
(
[z,x ],y
)
+
(
x, [z,y ]
)
= 0. Using the above arguments, it is easy to see that a
reductive algebra can be written as the direct sum of an abeli an algebra and some number
of simple algebras in a unique way.
25. Show that, if ω is the canonical left-invariant 1-form on G andYv is the right-invariant
vector ﬁeld on G satisfying Yv(e) = v, then
ω
(
Yv(a)
)
= Ad
(
a−1)
(v).
(Remark: For any skew-commutative algebra ( a, [, ]), the function [ [, ] ]:a × a × a → a
deﬁned by
[ [x,y,z ] ] = [[x,y ],z ] + [[y,z ],x ] + [[z,x ],y ]
is tri-linear and skew-symmetric, and hence represents an e lement of a ⊗ Λ 3(a∗).)
E.2.5 38

Lecture 3:
Group Actions on Manifolds
In this lecture, I turn from the abstract study of Lie groups t o their realizations as
‘transformation groups.’
Lie group actions.
Deﬁnition 1: If (G,µ ) is a Lie group and M is a smooth manifold, then a left action of
G on M is a smooth mapping λ:G ×M → M that satisﬁes λ(e,m ) = m for all m ∈ M
and
λ
(
a,λ (b,m )
)
=λ
(
µ(a,b ),m
)
.
Similarly, a right action of G on M is a smooth mapping ρ:M ×G → M , that satisﬁes
ρ(m,e ) = m for all m ∈M and
ρ
(
ρ(m,a ),b
)
=ρ
(
m,µ (a,b )
)
.
For notational sanity, whenever the action (left or right) c an be easily inferred from
context, we will usually write a ·m instead of λ(a,m ) or m ·a instead of ρ(m,a ). Thus,
for example, the axioms for a left action in this abbreviated notation are simply e ·m =m
and a · (b ·m) = ab ·m.
For a given a left action λ:G ×M → M , it is easy to see that for each ﬁxed a ∈ G
the map λa:M →M deﬁned by λa(m) = λ(a,m ) is a smooth diﬀeomorphism of M onto
itself. Thus, G gets represented as a group of diﬀeomorphisms, or ‘transfor mations’ of a
manifoldM . This notion of ‘transformation group’ was what motivated L ie to develop his
theory in the ﬁrst place. See the Appendix to this Lecture for a more complete discussion
of this point.
Equivalence of Left and Right Actions. Note that every right action ρ:M ×G →
M can be rewritten as a left action and vice versa. One merely de ﬁnes
˜ρ(a,m ) = ρ(m,a −1).
(The reader should check that this ˜ ρ is, in fact, a left action.) Thus, all theorems about
left actions have analogues for right actions. The distinct ion between the two is mainly
for notational and conceptual convenience. I will concentr ate on left actions and only
occasionally point out the places where right actions behav e slightly diﬀerently (mainly
changes of sign, etc.).
Stabilizers and Orbits. A left action is said to be eﬀective if g ·m = m for all
m ∈M implies that g = e. (Sometimes, the word faithful is used instead.) A left action
is said to be free if g ⁄=e implies that g ·m ⁄=m for all m ∈M .
A left action is said to be transitive if, for any x,y ∈M , there exists a g ∈G so that
g ·x =y. In this case, M is usually said to be homogeneous under the given action.
L.3.1 39

For any m ∈M , the G-orbit of m is deﬁned to be the set
G ·m = {g ·m |g ∈G}
and the stabilizer (or isotropy group ) of m is deﬁned to be the subset
Gm = {g ∈G |g ·m =m}.
Note that
Gg·m =gGmg−1.
Thus, wheneverH ⊂G is the stabilizer of a point of M , then all of the conjugate subgroups
of H are also stabilizers. These results imply that
GM = ⋂
m∈M
Gm
is a closed normal subgroup of G and consists of those g ∈G for which g ·m =m for all
m ∈M . Often in practice, GM is a discrete (in fact, usually ﬁnite) subgroup of G. When
this is so, we say that the action is almost eﬀective .
The following theorem says that orbits and stabilizers are p articularly nice objects.
Though the proof is relatively straightforward, it is a litt le long, so we will consider a few
examples before attempting it.
Theorem 1: Let λ:G ×M →M be a left action of G on M . Then, for all m ∈M , the
stabilizer Gm is a closed Lie subgroup of G. Moreover, the orbit G ·m can be given the
structure of a smooth submanifold of M in such a way that the map φ:G →G ·m deﬁned
byφ(g) = λ(g,m ) is a smooth submersion.
Example 1. Any Lie group left-acts on itself by left multiplication. I. e., we set
M =G and deﬁne λ:G ×M →M to simply be µ. This action is both free and transitive.
Example 2. Given a homomorphism of Lie groups φ:H → G, deﬁne a smooth left
actionλ:H ×G →G by the rule λ(h,g ) = φ(h)g. Then He = ker(φ) andH ·e =φ(H) ⊂G.
◮ In particular, Theorem 1 implies that the kernel of a Lie grou p homomorphism
is a (closed, normal) Lie subgroup of the domain group and the image of a Lie group
homomorphism is a Lie subgroup of the range group.
Example 3. Any Lie group acts on itself by conjugation: g ·g0 =gg0g−1. This action
is neither free nor transitive (unless G = {e}). Note that Ge = G and, in general, Gg is
the centralizer of g ∈G. This action is eﬀective (respectively, almost eﬀective) i f and only
if the center of G is trivial (respectively, discrete). The orbits are the con jugacy classes
of G.
Example 4. GL(n, R) acts on Rn as usual by A ·v =Av. This action is eﬀective but
is neither free nor transitive since GL( n, R) ﬁxes 0 ∈ Rn and acts transitively on Rn\{0}.
Thus, there are exactly two orbits of this action, one closed and the other not.
L.3.2 40

Example 5. SO(n+1) acts on Sn = {x ∈ Rn+1 |x ·x = 1 } by the usual action
A ·x = Ax. This action is transitive and eﬀective, but not free (unles s n = 1) since, for
example, the stabilizer of en+1 is clearly isomorphic to SO( n).
Example 6. Let Sn be the n(n+1)/2-dimensional vector space of n-by-n real sym-
metric matrices. Then GL( n, R) acts on Sn by A ·S = AS tA. The orbit of the identity
matrixIn is S+(n), the set of all positive-deﬁnite n-by-n real symmetric matrices (Why?).
In fact, it is known that, if we deﬁne Ip,q ∈ Sn to be the matrix
Ip,q =


Ip 0 0
0 −Iq 0
0 0 0

,
(where the ‘0’ entries have the appropriate dimensions) the n Sn is the (disjoint) union of
the orbits of the matrices Ip,q where 0 ≤p,q and p +q ≤n (see the Exercises).
The orbit of Ip,q is open in Sn iﬀ p +q =n. The stabilizer of Ip,q in this case is deﬁned
to be O(p,q ) ⊂ GL(n, R).
Note that the action is merely almost eﬀective since {±In} ⊂ GL(n, R) ﬁxes every
S ∈ Sn.
Example 7. Let J =
{
J ∈ GL(2n, R) |J 2 = −I2n
}
. Then GL(2 n, R) acts on J on
the left by the formula A ·J =AJA −1. I leave as exercises for the reader to prove that J
is a smooth manifold and that this action of GL(2 n, R) is transitive and almost eﬀective.
The stabilizer of J0 = multiplication by i in Cn ( = R2n) is simply GL( n, C) ⊂ GL(2n, R).
Example 8. Let M = RP1, denote the projective line, whose elements are the lines
through the origin in R2. We will use the notation
[
x
y
]
to denote the line in R2 spanned
by the non-zero vector
(x
y
)
.
Let G = SL(2, R) act on RP1 on the left by the formula
(
a b
c d
)
·
[
x
y
]
=
[
ax +by
cx +dy
]
.
This action is easily seen to be almost eﬀective, with only ±I2 ∈ SL(2, R) acting trivially.
Actually, it is more common to write this action more informa lly by using the iden-
tiﬁcation RP1 = R∪{∞} that identiﬁes
[
x
y
]
when y ⁄= 0 with x/y ∈ R and
[ 1
0
]
with ∞.
With this convention, the action takes on the more familiar ‘ linear fractional’ form
(
a b
c d
)
·x = ax +b
cx +d .
Note that this form of the action makes it clear that the so-ca lled ‘linear fractional’ action or
‘M¨ obius’ action on the real line is just the projectivization of the usual linear representation
of SL(2, R) on R2.
L.3.3 41

We now turn to the proof of Theorem 1.
Proof of Theorem 1: Fix m ∈ M and deﬁne φ:G → M by φ(g) = λ(g,m ) as in the
theorem. Since Gm =φ−1(m), it follows that Gm is a closed subset of G. The axioms for
a left action clearly imply that Gm is closed under multiplication and inverse, so it is a
subgroup.
I claim that Gm is a submanifold of G. To see this, let gm ⊂ g =TeG be the kernel
of the mapping φ′(e):TeG →TmM . Since φ ◦Lg = λg ◦φ for all g ∈ G, the Chain Rule
yields a commutative diagram:
g
L′
g (e)
− → TgG
φ′(e)


↓


↓φ′(g)
TmM
λ′
g(m)
− → Tg·mM
Since both L′
g(e) and λ′
g(m) are isomorphisms, it follows that ker( φ′(g)) = L′
g(e)(gm) for
all g ∈ G. In particular, the rank of φ′(g) is independent of g ∈ G. By the Implicit
Function Theorem (see Exercise 2), it follows that φ−1(m) = Gm is a smooth submanifold
of G.
It remains to show that the orbit G · m can be given the structure of a smooth
submanifold of M with the stated properties. That is, that G ·m can be given a second
countable, Hausdorﬀ, locally Euclidean topology and a smoo th structure for which the
inclusion map G ·֒→ M is a smooth immersion and for which the map φ:G →G ·m is
a submersion.
Before embarking on this task, it is useful to remark on the na ture of the ﬁbers of
the map φ. By the axioms for left actions, φ(h) = h ·m = g ·m = φ(g) if and only if
g−1h ·m =m, i.e., if and only if g−1h lies in Gm. This is equivalent to the condition that
h lie in the left Gm-coset gGm. Thus, the ﬁbers of the map φ are the left Gm-cosets in G.
In particular, the map φ establishes a bijection ¯φ:G/Gm →G ·m.
First, I specify the topology on G·m to be quotient topology induced by the surjective
mapφ:G →G ·m. Thus, a set U inG ·m is open if and only if φ−1(U ) is open in G. Since
φ:G → M is continuous, the quotient topology on the image G ·m is at least as ﬁne as
the subspace topology G ·m inherits via inclusion into M . Since the subspace topology is
Hausdorﬀ, the quotient topology must be also. Moreover, the quotient topology on G ·m
is also second countable since the topology of G is. For the rest of the proof, ‘the topology
on G ·m’ means the quotient topology.
I will both establish the locally Euclidean nature of this to pology and construct a
smooth structure on G ·m at the same time by ﬁnding the required neighborhood charts
and proving that they are smooth on overlaps. First, however , I need a lemma establishing
the existence of a ‘tubular neighborhood’ of the submanifol d Gm ⊂G. Let d = dim(G) −
dim(Gm). Then there exists a smooth mapping ψ:Bd → G (where Bd is an open ball
about 0 in Rd) so that ψ(0) = e and so that g is the direct sum of the subspaces gm and
V =ψ′(0)(Rd). By the Chain Rule and the deﬁnition of gm, it follows that (φ◦ψ)′(0): Rd →
L.3.4 42

TmM is injective. Thus, by restricting to a smaller ball in Rd if necessary, I may assume
henceforth that φ ◦ψ:Bd →M is a smooth embedding.
Consider the mapping Ψ: Bd ×Gm →G deﬁned by Ψ( x,g ) = ψ(x)g. I claim that Ψ
is a diﬀeomorphism onto its image (which is an open set), say U = Ψ( Bd ×Gm) ⊂ G.
(Thus,U forms a sort of ‘tubular neighborhood’ of the submanifold Gm in G.)
To see this, ﬁrst I show that Ψ is one-to-one: If Ψ( x1,g 1) = Ψ( x2,g 2), then
(φ ◦ψ)(x1) = ψ(x1) ·m = (ψ(x1)g1) ·m = (ψ(x2)g2) ·m =ψ(x2) ·m = (φ ◦ψ)(x2),
so the injectivity of φ ◦ψ implies x1 =x2. Since ψ(x1)g1 =ψ(x2)g2, this in turn implies
that g1 =g2.
Second, I must show that the derivative
Ψ ′(x,g ):TxRd ⊕TgGm →Tψ(x)gG
is an isomorphism for all ( x,g ) ∈ Bd ×Gm. However, from the beginning of the proof,
ker(φ′(ψ(x)g)) = L′
ψ(x)g(e)(gm) and this latter space is clearly Ψ ′(x,g )(0 ⊕TgGm). On
the other hand, since φ(Ψ(x,g )) = φ ◦ψ(x), it follows that
φ′(Ψ(x,g ))
(
Ψ ′(x,g )(TxRd ⊕ 0)
)
= (φ ◦ψ)′(x)(TxRd)
and this latter space has dimension d by construction. Hence, Ψ ′(x,g )(TxRd ⊕ 0) is
a d-dimensional subspace of Tψ(x)gG that is transverse to Ψ ′(x,g )(0 ⊕ TgGm). Thus,
Ψ ′(x,g ):TxRd ⊕TgGm →Tψ(x)gG is surjective and hence an isomorphism, as desired.
This completes the proof that Ψ is a diﬀeomorphism onto U. It f ollows that the inverse
of Ψ is smooth and can be written in the form Ψ −1 = π1 ×π2 where π1:U → Bd and
π2:U →Gm are smooth submersions.
Now, for each g ∈ G, deﬁne ρg:Bd → M by the formula ρg(x) = φ
(
gψ(x)
)
. Then
ρg = λg ◦φ ◦ψ, so ρg is a smooth embedding of Bd into M . By construction, U =
φ−1(φ ◦ψ(Bd)) = φ−1(ρe(Bd)) is an open set in G, so it follows that ρe(Bd) is an open
neighborhood of e ·m = m in G ·m. By the axioms for left actions, it follows that
φ−1(
ρg(Bd)
)
= Lg(U ) (which is open in G) for all g ∈ G. Thus, ρg(Bd) is an open
neighborhood of g ·m in G ·m (in the quotient topology). Moreover, contemplating the
commutative square
U
Lg
− → Lg(U )
π1


↓


↓φ
Bd ρg
− → ρg(Bd)
whose upper horizontal arrow is a diﬀeomorphism that identi ﬁes the ﬁbers of the vertical
arrows (each of which is a topological identiﬁcation map) im plies that ρg is, in fact, a
homeomorphism onto its image. Thus, the quotient topology i s locally Euclidean.
Finally, I show that the ‘patches’ ρg overlap smoothly. Suppose that
ρg(Bd) ∩ρh(Bd) ⁄= ∅.
L.3.5 43

Then, because the maps ρg and ρh are homeomorphisms,
ρg(Bd) ∩ρh(Bd) = ρg(W1) = ρh(W2)
where Wi ⁄= ∅ are open subsets of Bd. It follows that
Lg
(
Ψ(W1 ×Gm)
)
=Lh
(
Ψ(W2 ×Gm)
)
.
Thus, if τ :W1 →W2 is deﬁned by the rule τ =π1 ◦Lh−1 ◦Lg ◦ψ, then τ is a smooth map
with smooth inverse τ −1 =π1 ◦Lg−1 ◦Lh ◦ψ and hence is a diﬀeomorphism. Moreover, we
haveρg = ρh ◦τ , thus establishing that the patches ρg overlap smoothly and hence that
the patches deﬁne the structure of a smooth manifold on G ·m.
That the map φ:G →G ·m is a smooth submersion and that the inclusion G ·֒→M
is a smooth one-to-one immersion are now clear. □
It is worth remarking that the proof of Theorem 1 shows that th e Lie algebra of Gm
is the subspace gm. In particular, if Gm = {e}, then the map φ:G → M is a one-to-one
immersion.
The proof also brings out the fact that the orbit G ·m can be identiﬁed with the left
coset space G/Gm, which thereby inherits the structure of a smooth manifold. It is natural
to wonder which subgroups H of G have the property that the coset space G/H can be
given the structure of a smooth manifold for which the coset p rojection π:G →G/H is a
smooth map. This question is answered by the following resul t. The proof is quite similar
to that of Theorem 1, so I will only provide an outline, leavin g the details as exercises for
the reader.
Theorem 2: If H is a closed subgroup of a Lie group G, then the left coset space G/H
can be given the structure of a smooth manifold in a unique way so that the coset mapping
π:G →G/H is a smooth submersion. Moreover, with this smooth structur e, the left action
λ:G ×G/H →G/H deﬁned by λ(g,hH ) = ghH is a transitive smooth left action.
Proof: (Outline.) If the coset mapping π:G → G/H is to be a smooth submersion,
elementary linear algebra tells us that the dimension of G/H will have to be d = dim(G) −
dim(H). Moreover, for every g ∈G, there will have to exist a smooth mapping ψg:Bd →G
withψg(0) = g that is transverse to the submanifold gH atg and so that the composition
π ◦ψ:Bd → G/H is a diﬀeomorphism onto a neighborhood of gH ∈ G/H. It is not
diﬃcult to see that this is only possible if G/H is endowed with the quotient topology.
The hypothesis that H be closed implies that the quotient topology is Hausdorﬀ. It is
automatic that the quotient topology is second countable. T he proof that the quotient
topology is locally Euclidean depends on being able to const ruct the ‘tubular neighborhood’
U of H as constructed for the case of a stabilizer subgroup in the pr oof of Theorem 1.
Once this is done, the rest of the construction of charts with smooth overlaps follows the
end of the proof of Theorem 1 almost verbatim. □
L.3.6 44

Group Actions and V ector Fields. A left action λ: R ×M → M (where R has
its usual additive Lie group structure) is, of course, the sa me thing as a ﬂow. Associated
to each ﬂow on M is a vector ﬁeld that generates this ﬂow. The generalization of this
association to more general Lie group actions is the subject of this section.
Let λ:G ×M →M be a left action. Then, for each v ∈ g, there is a ﬂow Ψ λ
v on M
deﬁned by the formula
Ψ λ
v (t,m ) = etv ·m.
This ﬂow is associated to a vector ﬁeld on M that we shall denote by Yλ
v , or simply Yv if the
action λ is clear from context. This deﬁnes a mapping λ∗: g → X(M ), where λ∗(v) = Yλ
v .
Proposition 1: For each left action λ:G ×M → M , the mapping λ∗ is a linear anti-
homomorphism from g to X(M ). In other words, λ∗ is linear and
λ∗([x,y ]) = −[λ∗(x),λ ∗(y)].
Proof: For each v ∈ g, let Yv denote the right invariant vector ﬁeld on G whose value
at e is v. Then, according to Lecture 2, the ﬂow of Yv on G is given by the formula
Ψ v(t,g ) = exp(tv)g. As usual, let Φ v denote the ﬂow of the left invariant vector ﬁeld Xv.
Then the formula
Ψ v(t,g ) =
(
Φ −v(t,g −1)
)−1
is immediate. If ι∗: X(G) → X(G) is the map induced by the diﬀeomorphism ι(g) = g−1,
then the above formula implies
ι∗(X−v) = Yv.
In particular, since ι∗ commutes with Lie bracket, it follows that
[Yx,Yy] = −Y[x,y]
for all x,y ∈ g.
Now, regard Yv and Ψ v as being deﬁned on G×M in the obvious way, i.e., Ψ v(g,m ) =
(etvg,m ). Then λ intertwines this ﬂow with that of Ψ λ
v :
λ ◦ Ψ v = Ψ λ
v ◦λ.
It follows that the vector ﬁelds Yv and Yλ
v are λ-related. Thus, [ Yλ
x,Y λ
y ] is λ-related to
[Yx,Yy] = −Y[x,y] and hence must be equal to −Yλ
[x,y]. Finally, since the map v ↦→Yv is
clearly linear, it follows that λ∗ is also linear. □
◮ The appearance of the minus sign in the above formula is somet hing of an annoyance
and has led some authors (cf. [A]) to introduce a non-classic al minus sign into either the
deﬁnition of the Lie bracket of vector ﬁelds or the deﬁnition of the Lie bracket on g in
order to get rid of the minus sign in this theorem. As logical a s this revisionism is, it has
not been particularly popular. However, it turns up just oft en enough that the reader of
other sources should be wary of it.
L.3.7 45

Even with a minus sign, however, Proposition 1 implies that the subspa ce λ∗(g) ⊂
X(M ) is a (ﬁnite dimensional) Lie subalgebra of the Lie algebra o f all vector ﬁelds on M .
Example: Linear F ractional T ransformations. Consider the M¨ obius action in-
troduced earlier of SL(2 , R) on RP1:
(
a b
c d
)
·s = as +b
cs +d.
A basis for the Lie algebra sl(2, R) is
x =
(
0 1
0 0
)
, h =
(
1 0
0 −1
)
, y =
(
0 0
1 0
)
Thus, for example, the ﬂow Ψ λ
y is given by
Ψ λ
y (t,s ) = exp
(
0 0
t 0
)
·s =
(
1 0
t 1
)
·s = s
ts + 1 =s −s2t + · · ·,
so Yλ
y = −s2∂/∂s . In fact, it is easy to see that, in general,
λ∗(a0x +a1h +a2y) = (a0 + 2a1s −a2s2)∂
∂s.
The basic ODE existence theorem can be regarded as saying tha t every vector ﬁeld
X ∈ X(M ) arises as the ‘ﬂow’ of a ‘local’ R-action on M . There is a generalization of this
notion that covers ﬁnite dimensional subalgebras of X(M ).
To state it precisely, we ﬁrst deﬁne a local left action of a Lie group G on a manifold M
to be an open neighborhood U ⊂G×M of {e}×M together with a smooth map λ:U →M
satisfying λ(e,m ) = m for all m ∈M and
λ
(
a,λ (b,m )
)
=λ(ab,m )
whenever this makes sense, i.e., whenever ( b,m ), (ab,m ), and
(
a,λ (b,m )
)
all lie in U .
For example, the linear fractional transformations of the l ast example could just as
easily have been regarded as a local action of SL(2 , R) on R, where the open set U ⊂
SL(2, R) × R is just the set of pairs where cs +d ⁄= 0.
It is easy to see that even a mere local Lie group action induce s a Lie algebra anti-
homomorphism λ∗: g → X(M ) as above. There is a converse to this statement, due,
originally to Lie:
Proposition 2: Let G be a connected Lie group and let ϕ: g → X(M ) be a Lie algebra
anti-homomorphism. Then there exists a local left action (U,λ ) ofG onM so that λ∗ =ϕ.
L.3.8 46

Proof: On G×M ×M , deﬁne, for each v ∈ g, a vector ﬁeld Zv such that, for each
(g,p,q ) ∈G×M ×M ,
Zv(g,p,q ) =
(
Yv(g), 0p, φ(v)(q)
)
∈TgG ⊕TpM ⊕TqM =T(g,p,q )G×M ×M.
Then, by hypotheses, [ Zv,Zw] = −Z[v,w] for all v,w ∈ g. Moreover, Zv is nowhere vanish-
ing when v ⁄= 0 (since Yv is nowhere vanishing). Thus, the Zv span an integrable d-plane
ﬁeld (where d = dim(G)), and G×M ×M is foliated by the leaves of this plane ﬁeld. Let
F denote the foliation by these d-dimensional leaves
Letn = dimM . The union of the F -leaves that pass through the points ( e,m,m ) for
m ∈ M is a smooth submanifold S ⊂ G×M ×M of dimension d+n. The tangent space
of S at (e,m,m ) is the direct sum of the d-dimensional subspace spanned by the vector
ﬁelds Zv and the n-dimensional subspace spanned by vectors of the form (0 ,w,w ) for
w ∈ TmM . Thus, in a neighborhood of {e}×diag(M ), the submanifold S can be written
as the graph of a smooth map µ:U → M , where U is an open neighborhood of {e}×M ,
i.e., the manifold consists of triples
(
g,m,µ (g,m )
)
. This mapping satisﬁes µ(e,m ) = m
for all m ∈M , and it also satisﬁes
µ(exp(tv)g,m ) = Φ t(φ(v),µ (g,m ))
for all v ∈ g and all t andg suﬃciently small that Phit(φ(v),µ (g,m )), i.e., the time t ﬂow
ofφ(v) with initial point µ(g,m ), exists and (exp( tv)g,m ) lies in U . From this follows the
desired property that
µ(h,µ (g,m )) = µ(hg,m )
holds when it makes sense. □
Equations of Lie type. Early in the theory of Lie groups, a special family of
ordinary diﬀerential equations was singled out for study th at generalized the theory of
linear equations and the Riccati equation. These have come t o be known as equations of
Lie type . We are now going to describe this class.
Given a Lie algebra homomorphism λ∗: g → X(M ) where g is the Lie algebra of a Lie
group G, and a curve A: R → g, the ordinary diﬀerential equation for a curve γ: R →M
γ′(t) = λ∗
(
A(t)
)(
γ(t)
)
is known as an equation of Lie type .
Example: The Riccati equation. By our previous example, the classical Riccati
equation
s′(t) = a0(t) + 2a1(t)s(t) +a2(t)
(
s(t)
)2
is an equation of Lie type for the (local) linear fractional a ction of SL(2 , R) on R. The
curveA is
A(t) =
(
a1(t) a0(t)
−a2(t) −a1(t)
)
L.3.9 47

Example: Linear Equations. Every linear equation is an equation of Lie type. Let G
be the matrix Lie subgroup of GL( n+1, R),
G =
{(
A B
0 1
)⏐
⏐
⏐
⏐
⏐A ∈ GL(n, R) and B ∈ Rn
}
.
Then G acts on Rn by the standard aﬃne action:
(
A B
0 1
)
·x =Ax +B.
It is easy to verify that the inhomogeneous linear diﬀerenti al equation
x′(t) = a(t)x(t) +b(t)
is then a Lie equation, with
A(t) =
(
a(t) b(t)
0 0
)
.
The following proposition follows from the fact that a left a ctionλ:G×M →M relates
the right invariant vector ﬁeld Yv to the vector ﬁeld λ∗(v) on M . Despite its simplicity, it
has important consequences.
Proposition 3: IfA: R → g is a curve in the Lie algebra of a Lie group G andS: R →G
is the solution to the equation S′(t) = YA(t)(S(t)) with initial condition S(0) = e, then on
any manifold M endowed with a left G-action λ, the equation of Lie type
γ′(t) = λ∗
(
A(t)
)(
γ(t)
)
,
with initial condition γ(0) = m has, as its solution, γ(t) = S(t) ·m. □
The solution S of Proposition 3 is often called the fundamental solution of the Lie
equation associated to A(t). The most classical example of this is the fundamental solu tion
of a linear system of equations:
x′(t) = a(t)x(t)
wherea is an n-by-n matrix of functions of t andx is to be a column of height n. In ODE
classes, we learn that every solution of this equation is of t he form x(t) = X(t)x0 whereX
is the n-by-n matrix of functions of t that solves the equation X ′(t) = a(t)X(t) with initial
conditionX(0) = In. Of course, this is a special case of Proposition 3 where GL( n, R) acts
on Rn via the standard left action described in Example 4.
L.3.10 48

Lie’s Reduction Method. I now want to explain Lie’s method of analysing equa-
tions of Lie type. Suppose that λ:G ×M → M is a left action and that A: R → g is
a smooth curve. Suppose that we have found (by some method) a p articular solution
γ: R → M of the equation of Lie type associated to A with γ(0) = m. Select a curve
g: R →G so that γ(t) = g(t) ·m. Of course, this g will not, in general be unique, but any
other choice ˜g will be of the form ˜g(t) = g(t)h(t) where h: R →Gm.
I would like to choose h so that ˜g is the fundamental solution of the Lie equation
associated to A, i.e., so that
˜g′(t) = YA(t)
(
˜g(t)
)
=R′
˜g(t)
(
A(t)
)
Unwinding the deﬁnitions, it follows that h must satisfy
R′
g(t)h(t)
(
A(t)
)
=L′
g(t)
(
h′(t)
)
+R′
h(t)
(
g′(t)
)
so
R′
h(t)
(
R′
g(t)
(
A(t)
))
=L′
g(t)
(
h′(t)
)
+R′
h(t)
(
g′(t)
)
Solving for h′(t), we ﬁnd that h must satisfy the diﬀerential equation
h′(t) = R′
h(t)
(
L′
g(t)−1
(
R′
g(t)
(
A(t)
)
−g′(t)
))
.
If we set
B(t) = L′
g(t)−1
(
R′
g(t)
(
A(t)
)
−g′(t)
)
,
then B is clearly computable from g and A and hence may be regarded as known. Since
B(t) =
(
R′
h(t)
)−1(
h′(t)
)
and since h is a curve in Gm, it follows that B must actually be
a curve in gm.
◮ It follows that the equation
h′(t) = R′
h(t)
(
B(t)
)
is a Lie equation for h. In other words in order to ﬁnd the fundamental solution of a L ie
equation for G when the particular solution with initial condition g(0) = m ∈M is known,
it suﬃces to solve a Lie equation in Gm!
This observation is known as Lie’s method of reduction . It shows how knowledge of a
particular solution to a Lie equation simpliﬁes the search f or the general solution. (Note
that this is deﬁnitely not true of general diﬀerential equations.) Also, Lie’s method gener-
alizes to cover the case of several particular solutions. If one knows k particular solutions
with initial values m1,...,m k ∈ M , then (by letting G act on the k-fold product of M
with itself) one can reduce ﬁnding the fundamental solution to ﬁnding the fundamental
solution of a Lie equation in
Gm1,...,mk =Gm1 ∩Gm2 ∩ · · · ∩Gmk.
L.3.11 49

If it happens that this intersection is discrete, then one ca n explicitly compute a funda-
mental solution that will then yield the general solution.
Example: The Riccati equation again. Consider the Riccati equation
s′(t) = a0(t) + 2a1(t)s(t) +a2(t)
(
s(t)
)2
and suppose that we know a particular solution s0(t). Then let
g(t) =
(
1 s0(t)
0 1
)
,
so that s0(t) = g(t) · 0 (we are using the linear fractional action of SL(2 , R) on R). The
stabilizer of 0 is the subgroup G0 of matrices of the form:
(
u 0
v u −1
)
.
Thus, if we set, as usual,
A(t) =
(
a1(t) a0(t)
−a2(t) −a1(t)
)
,
then the fundamental solution of S′(t) = A(t)S(t) can be written in the form
S(t) = g(t)h(t) =
(
1 s0(t)
0 1
)(u(t) 0
v(t)
(
u(t)
)−1
)
Solving for the matrix B(t) (which we know will have values in the Lie algebra of G0), we
ﬁnd
B(t) =
(
b1(t) 0
b2(t) −b1(t)
)
=
(
a1(t) +a2(t)s0(t) 0
−a2(t) −a1(t) −a2(t)s0(t)
)
,
and the remaining equation to be solved is
h′(t) = B(t)h(t),
which is solvable by quadratures in the usual way:
u(t) = exp
(∫ t
0
b1(τ )dτ
)
,
and, once u(t) has been found,
v(t) =
(
u(t)
)−1
∫ t
0
b2(τ )
(
u(τ )
)2
dτ.
L.3.12 50

Example: Linear Equations Again. Consider the general inhomogeneous n-by-n
system
x′(t) = a(t)x(t) +b(t).
Let G be the matrix Lie subgroup of GL( n+1, R),
G =
{(
A B
0 1
)⏐
⏐
⏐
⏐
⏐A ∈ GL(n, R) and B ∈ Rn
}
.
acting on Rn by the standard aﬃne action as before. If we embed Rn into Rn+1 by the
rule
x ↦→
(
x
1
)
,
then the standard aﬃne action of G on Rn extends to the standard linear action of G
on Rn+1. Note that G leaves invariant the subspace xn+1 = 0, and solutions of the Lie
equation corresponding to
A(t) =
(
a(t) b(t)
0 0
)
that lie in this subspace are simply solutions to the homogen eous equation x′(t) = a(t)x(t).
Suppose that we knew a basis for the homogeneous solutions, i .e., the fundamental solution
to X ′(t) = a(x)X(t) with X(0) = In. This corresponds to knowing the n particular
solutions to the Lie equation on Rn+1 that have the initial conditions e1,...,e n. The
simultaneous stabilizer of all of these points in Rn+1 is the subgroup H ⊂ G of matrices
of the form (
In y
0 1
)
Thus, we choose
g(t) =
(
X(t) 0
0 1
)
as our initial guess and look for the fundamental solution in the form:
S(t) = g(t)h(t) =
(
X(t) 0
0 1
)(
In y(t)
0 1
)
.
Expanding the condition S′(t) = A(t)S(t) and using the equation X ′(t) = a(t)X(t) then
reduces us to solving the equation
y′(t) =
(
X(t)
)−1
b(t),
which is easily solved by integration. The reader will proba bly recognize that this is
precisely the classical method of ‘variation of parameters ’.
L.3.13 51

Solution by quadrature. This brings us to an interesting point: Just how hard is
it to compute the fundamental solution to a Lie equation of th e form
γ′(t) = R′
γ(t)
(
A(t)
)
?
One case where it is easy is if the Lie group is abelian. We have already seen that if T
is a connected abelian Lie group with Lie algebra t, then the exponential map exp: t →T
is a surjective homomorphism. It follows that the fundament al solution of the Lie equation
associated to A: R → t is given in the form
S(t) = exp
(∫ t
0
A(τ )dτ
)
(Exercise: Why is this true?) Thus, the Lie equation for an ab elian group is ‘solvable by
quadrature’ in the classical sense.
Another instance where one can at least reduce the problem so mewhat is when one has
a homomorphismφ:G →H and knows the fundamental solution SH to the Lie equation for
ϕ ◦A: R → h. In this case, SH is the particular solution (with initial condition SH (0) = e)
of the Lie equation on H associated to A by regarding φ as deﬁning a left action on H.
By Lie’s method of reduction, therefore, we are reduced to so lving a Lie equation for the
group ker(φ) ⊂G.
Example. Suppose that G is connected and simply connected. Let g be its Lie algebra
and let [ g, g] ⊂ g be the linear subspace generated by all brackets of the form [ x,y ] where
x and y lie in g. Then, by the Exercises of Lecture 2, we know that [ g, g] is an ideal in g
(called the commutator ideal of g). Moreover, the quotient algebra t = g/[g, g] is abelian.
Since G is connected and simply connected, Theorem 3 from Lecture 2 i mplies that
there is a Lie group homomorphism φ0:G → T0 = t whose induced Lie algebra homo-
morphism ϕ0: g → t = g/[g, g] is just the canonical quotient mapping. From our previous
remarks, it follows that any Lie equation for G can be reduced, by one quadrature, to a
Lie equation for G1 = kerφ0. It is not diﬃcult to check that the group G1 constructed in
this argument is also connected and simply connected.
The desire to iterate this process leads to the following con struction: Deﬁne the
sequence {gk} of commutator ideals of g by the rules g0 = g and and gk+1 = [ gk, gk] for
k ≥ 0. Then we have the following result:
Proposition 4: Let G be a connected and simply connected Lie group for which the
sequence {gk} of commutator ideals satisﬁes gN = (0) for some N > 0. Then any Lie
equation for G can be solved by a sequence of quadratures.
A Lie algebra with the property described in Proposition 4 is called ‘solvable’. For
example, the subalgebra of upper triangular matrices in gl(n, R) is solvable, as the reader
is invited to check.
L.3.14 52

While it may seem that solvability is a lot to ask of a Lie algeb ra, it turns out that
this property is surprisingly common. The reader can also ch eck that, of all of the two
and three dimensional Lie algebras found in Lecture 2, only sl(2, R) and so(3) fail to be
solvable.
This (partly) explains why the Riccati equation holds such a n important place in
the theory of ODE. In some sense, it is the ﬁrst Lie equation th at cannot be solved by
quadratures. (See the exercises for an interpretation and ‘ proof’ of this statement.)
In any case, the sequence of subalgebras {gk} eventually stabilizes at a subalgebra
gN whose Lie algebra satisﬁes [ gN, gN ] = gN . A Lie algebra g for which [ g, g] = g is
called ‘perfect’. Our analysis of Lie equations shows that, by Lie’s reduction method, we
can, by quadrature alone, reduce the problem of solving Lie e quations to the problem
of solving Lie equations associated to Lie groups with perfe ct algebras. Further analysis
of the relation between the structure of a Lie algebra and the solvability by quadratures
of any associated Lie equation leads to the development of th e so-called Jordan-H¨ older
decomposition theorems, see [ ?].
L.3.15 53

Appendix: Lie’s T ransformation Groups, I
When Lie began his study of symmetry groups in the nineteenth century, the modern
concepts of manifold theory were not available. Thus, the ex amples that he had to guide
him were deﬁned as ‘transformations in n variables’ that were often, like the M¨ obius
transformations on the line or like conformal transformati ons in space, only deﬁned ‘almost
everywhere’. Thus, at ﬁrst glance, it might appear that Lie’ s concept of a ‘continuous
transformation group’ should correspond to what we have deﬁ ned as a local Lie group
action.
However, it turns out that Lie had in mind a much more general c oncept. For Lie, a
set Γ of local diﬀeomorphisms in Rn formed a ‘continuous transformation group’ if it was
closed under composition and inverse and moreover, the elem ents of Γ were characterized
as the solutions of some system of diﬀerential equations.
For example, the M¨ obius group on the line could be character ized as the set Γ of
(non-constant) solutions f (x) of the diﬀerential equation
2f ′′′(x)f ′(x) − 3
(
f ′′(x)
)2
= 0.
As another example, the ‘group’ of area preserving transfor mations of the plane could be
characterized as the set of solutions
(
f (x,y ),g (x,y )
)
to the equation
fxgy −gxfy ≡ 1,
while the ‘group’ of holomorphic transformations of the pla ne
R2
(regarded as C) was the set of solutions
(
f (x,y ),g (x,y )
)
to the equations
fx −gy =fy +gx = 0.
Notice a big diﬀerence between the ﬁrst example and the other two. In the ﬁrst
example, there is only a 3-parameter family of local solutio ns and each of these solutions
patches together on RP1 = R ∪ {∞} to become an element of the global Lie group action
of SL(2, R) on RP1. In the other two examples, there are many local solutions th at cannot
be extended to the entire plane, much less any ‘completion’. Moreover in the volume
preserving example, it is clear that no ﬁnite dimensional Li e group could ever contain all
of the globally deﬁned volume preserving transformations o f the plane.
Lie regarded these latter two examples as ‘inﬁnite continuo us groups’. Nowadays, we
would call them ‘inﬁnite dimensional pseudo-groups’. I wil l say more about this point of
view in an appendix to Lecture 6.
Since Lie did not have a group manifold to work with, he did not regard his ‘inﬁnite
groups’ as pathological. Instead of trying to ﬁnd a global de scription of the groups, he
worked with what he called the ‘inﬁnitesimal transformatio ns’ of Γ. We would say that,
L.3.16 54

for each of his groups Γ, he considered the space of vector ﬁelds γ ⊂ X(Rn) whose (local)
ﬂows were 1-parameter ‘subgroups’ of Γ. For example, the inﬁnitesimal transformations
associated to the area preserving transformations are the v ector ﬁelds
X =f (x,y )∂
∂x +g(x,y )∂
∂y
that are divergence free, i.e., satisfy fx +gy = 0.
Lie ‘showed’ that for any ‘continuous transformation group ’ Γ, the associated set of
vector ﬁelds γ was actually closed under addition, scalar multiplication (by constants),
and, most signiﬁcantly, the Lie bracket. (The reason for the quotes around ‘showed’ is
that Lie was not careful to specify the nature of the diﬀerent ial equations that he was
using to deﬁne his groups. Without adding some sort of consta nt rank or non-degeneracy
hypotheses, many of his proofs are incorrect.)
For Lie, every subalgebra L of the algebra X(Rn) that could be characterized by some
system of pde was to be regarded the Lie algebra of some Lie group. Thus, rat her than
classify actual groups (that might not really be groups beca use of domain problems), Lie
classiﬁed subalgebras of the algebra of vector ﬁelds.
In the case that L was ﬁnite dimensional, Lie actually proved that there was a ‘germ’
of a Lie group (in our sense) and a local Lie group action that g enerated this algebra of
vector ﬁelds. This is Lie’s so-called Third Fundamental The orem.
The case where L was inﬁnite dimensional remained rather intractable. I wil l have
more to say about this in Lecture 6. For now, though, I want to s tress that there is a sort
of analogue of actions for these ‘inﬁnite dimensional Lie gr oups’.
For example, ifM is a manifold and Diff(M ) is the group of (global) diﬀeomorphisms,
then we can regard the natural (evaluation) map λ: Diff(M )×M →M given byλ(φ,m ) =
φ(m) as a faithful Lie group action. If M is compact, then every vector ﬁeld is complete, so,
at least formally, the induced map λ∗:TidDiff(M ) → X(M ) ought to be an isomorphism
of vector spaces. If our analogy with the ﬁnite dimensional c ase is to hold up, λ∗ must
reverse the Lie bracket.
Of course, since we have not deﬁned a smooth structure on Diff(M ), it is not im-
mediately clear how to make sense of TidDiff(M ). I will prefer to proceed formally and
simply deﬁne the Lie algebra diff(M ) of Diff(M ) to be the vector space X(M ) with the
Lie algebra bracket given by the negative of the vector ﬁeld L ie bracket.
With this deﬁnition, it follows that a left action λ:G ×M → M where G is ﬁnite
dimensional can simply be regarded as a homomorphism Λ: G → Diff(M ) inducing a
homomorphism of Lie algebras.
A modern treatment of this subject can be found in [SS].
L.3.17 55

Appendix: Connections and Curvature
In this appendix, I want brieﬂy to describe the notions of con nections and curvature
on principal bundles in the language that I will be using them in the examples in this
Lecture.
Let G be a Lie group with Lie algebra g and let ωG be the canonical g-valued, left-
invariant 1-form on G.
Principal Bundles. LetM be an n-manifold and let P be a principal right G-bundle
over M . Thus, P comes equipped with a submersion π:P → M and a free right action
ρ:P ×G →P so that the ﬁbers of π are the G-orbits of ρ.
The Gauge Group. The group Aut(P ) of automorphisms of P is, by deﬁnition, the
set of diﬀeomorphisms φ:P →P that are compatible with the two structure maps, i.e.,
π ◦φ =π and ρg ◦φ =φ ◦ρg for all g ∈G.
For reasons having to do with Physics, this group is nowadays referred to as the gauge
group of P . Of course, Aut(P ) is not a ﬁnite dimensional Lie group, but it would have
been considered by Lie himself as a perfectly reasonable ‘co ntinuous transformation group’
(although not a very interesting one for his purposes).
For any φ ∈ Aut(P ), there is a unique smooth map ϕ:P → G that satisﬁes φ(p) =
p ·ϕ(p). The identity ρg ◦φ = φ ◦ρg implies that ϕ satisﬁes ϕ(p ·g) = g−1ϕ(p)g for all
g ∈G. Conversely, any smooth map ϕ:P →G satisfying this identity deﬁnes an element
of Aut(P ). It follows that Aut(P ) is the space of sections of the bundle C(P ) = P ×C G
where C:G ×G →G is the conjugation action C(a,b ) = aba−1.
Moreover, it easily follows that the set of vector ﬁelds on P whose ﬂows generate
1-parameter subgroups of Aut(P ) is identiﬁable with the space of sections of the vector
bundle Ad(P ) = P ×Ad g.
Connections. Let A(P ) denote the space of connections on P . Thus, an element
A ∈ A(P ) is, by deﬁnition, a g-valued 1-form A on P with the following two properties:
(1) For any p ∈P , we have ι∗
p(A) = ωG where ιp:G →P is given by ιp(g) = p ·g.
(2) For all g in G, we have ρ∗
g(A) = Ad(g−1)(A) where ρg:P →P is right action by g.
It follows from Property 1 that, for any connection A on P , we have A
(
ρ∗(x)
)
= x
for all x ∈ g. It follows from Property 2 that Lρ∗(x)A = −[x,A ] for all x ∈ g.
IfA0 andA1 are connections on P , then it follows from Property 1 that the diﬀerence
α = A1 −A0 is a g-valued 1-form that is ‘semi-basic’ in the sense that α(v) = 0 for all
v ∈ kerπ′. Moreover, Property 2 implies that α satisﬁes ρ∗
g(α) = Ad(g−1)(α). Conversely,
if α is any g-valued 1-form on P satisfying these latter two properties and A ∈ A(P ) is a
connection, then A +α is also a connection. It is easy to see that a 1-form α with these
two properties can be regarded as a 1-form on M with values in Ad( P ).
◮ Thus, A(P ) is an aﬃne space modeled on the vector space A1(
Ad(P )
)
. In particular,
if we regard A(P ) as an ‘inﬁnite dimensional manifold’, the tangent space TAA(P ) at any
point A is naturally isomorphic to A1(
Ad(P )
)
.
L.3.18 56

Curvature. The curvature of a connection A is the 2-form FA =dA + 1
2 [A,A ]. From
our formulas above, it follows that
ρ∗(x) FA =ρ∗(x) dA + [x,A ] = Lρ∗(x)A + [x,A ] = 0.
Since the vector ﬁelds ρ∗(x) span the vertical tangent spaces of P , it follows that FA is
a ‘semi-basic’ 2-form (with values in g). Moreover, the Ad-equivariance of A implies that
ρ∗
g(FA) = Ad(g−1)(FA). Thus, FA may be regarded as a section of the bundle of 2-forms
on M with values in the bundle Ad( P ).
The group Aut(P ) acts naturally on the right on A(P ) via pullback: A ·φ =φ∗(A).
In terms of the corresponding map ϕ:P →G, we have
A ·φ =ϕ∗(ωG) + Ad
(
ϕ−1)
(A).
It follows by direct computation that FA·φ =φ∗(FA) = Ad
(
ϕ−1)
(FA).
We say that A is ﬂat if FA = 0. It is an elementary ode result that A is ﬂat if and
only if, for every m ∈ M , there exists an open neighborhood U of m and a smooth map
τ :π−1(U ) → G that satisﬁes τ (p ·g) = τ (p)g and τ ∗(ωG) = A|U . In other words A is
ﬂat if and only if the bundle-with-connection ( P,A ) is locally diﬀeomorphic to the trivial
bundle-with-connection (M ×G,ωG).
Covariant Diﬀerentiation. The space Ap(
Ad(P )
)
of p-forms on M with values in
Ad(P ) can be identiﬁed with the space of g-valued, p-forms β on P that are both semi-
basic and Ad-equivariant (i.e., ρ∗
g(β) = Ad( g−1)(β) for all g ∈ G). Given such a form
β, the expression dβ + [A,β ] is easily seen to be a g-valued (p+1)-form on P that is also
semi-basic and Ad-equivariant. It follows that this deﬁnes a ﬁrst-order diﬀerential operator
dA: Ap(
Ad(P )
)
→ Ap+1(
Ad(P )
)
called covariant diﬀerentiation with respect to A. It is elementary to check that
dA
(
dAβ
)
= [FA,β ] = ad(FA)(β).
Thus, for a ﬂat connection,
(
A∗(Ad(P )),dA
)
forms a complex over M .
We also have the Bianchi identity dAFA = 0.
For some, ‘covariant diﬀerentiation’ means only dA: A0(Ad(P )) → A 1(Ad(P )).
Horizontal Lifts and Holonomy . Let A be a connection on P . If γ: [0, 1] →M is
aC1 curve and p ∈π−1(
γ(0)
)
is chosen, then there exists a unique C1 curve ˜γ: [0, 1] →P
that both ‘lifts’ γ in the sense that γ = π ◦ ˜γ and also satisﬁes the diﬀerential equation
˜γ∗(A) = 0.
(To see this, ﬁrst choose any lift ¯γ: [0, 1] →P that satisﬁes ¯γ(0) = p. Then the desired
lifting will then be given by ˜γ(t) = ¯γ(t) ·g(t) where g: [0, 1] →G is the solution of the Lie
equation g′(t) = −Rg(t)
(
A(¯γ′(t))
)
satisfying the initial condition g(0) = e.)
L.3.19 57

The resulting curve ˜γ is called a horizontal lift of γ. If γ is merely piecewise C1, the
horizontal lift can still be deﬁned by piecing together hori zontal lifts of the C1-segments
in the obvious way. Also, if p′ =p ·g0, then the horizontal lift of γ with initial condition
p′ is easily seen to be ρg0 ◦ ˜γ.
Let p ∈ P be chosen and set m = π(p). For every piecewise C1-loop γ: [0, 1] → M
based at m, the horizontal lift ˜γ has the property that ˜ γ(1) = p ·h(γ) for some unique
h(γ) ∈G. The holonomy of A at p, denoted by HA(p) is, by deﬁnition, the set of all such
elementsh(γ) of G where γ ranges over all of the piecewise C1 closed loops based at m.
I leave it to the reader to show that HA(p ·g) = g−1HA(p)g and that, if p and p′ can
be joined by a horizontal curve in P , then HA(p) = HA(p′). Thus, the conjugacy class of
HA(p) in G is independent of p if M is connected.
A basic theorem due to Borel and Lichnerowitz (see [KN]) asse rts thatHA(p) is always
a Lie subgroup of G.
L.3.20 58

Exercise Set 3:
Actions of Lie Groups
1. Verify the claim made in the lecture that every right (respe ctively, left) action of a
Lie group on a manifold can be rewritten as a left (respective ly, right) action. Is the
assumption that a left action λ:G ×M → M satisfy λ(e,m ) = m for all m ∈ M really
necessary?
2. Show that if f :X →Y is a map of smooth manifolds for which the rank of f ′(x):TxX →
Tf (x)Y is independent of x, then f −1(y) is a (possibly empty) closed, smooth submanifold
ofX for ally ∈Y . Note that this properly generalizes the usual Implicit Fun ction Theorem,
which requires f ′(x) to be a surjection everywhere in order to conclude that f −1(y) is a
smooth submanifold.
(Hint: Suppose that the rank of f ′(x) is identically k. You want to show that f −1(y)
(if non-empty) is a submanifold of X of codimension k. To do this, let x ∈f −1(y) be given
and construct a map ψ:V → Rk on a neighborhood V of y so that ψ ◦f is a submersion
near x. Then show that ( ψ ◦f )−1(
ψ(y)
)
(which, by the Implicit Function Theorem, is a
closed codimension k submanifold of the open set f −1(V ) ⊂X) is actually equal to f −1(y)
on some neighborhood of x. Where do you need the constant rank hypothesis?)
3. This exercise concerns the automorphism groups of Lie alge bras and Lie groups.
(i) Show that, for any Lie algebra g, the group of automorphisms Aut( g) deﬁned by
Aut(g) = {a ∈ End(g) |
[
a(x),a (y)
]
=a
(
[x,y ]
)
for all x,y ∈ g}
is a closed Lie subgroup of GL( g). Show that its Lie algebra is
der(g) = {a ∈ End(g) |a
(
[x,y ]
)
=
[
a(x),y
]
+
[
x,a (y)
]
for all x,y ∈ g}.
(Hint: Show that Aut( g) is the stabilizer of some point in some representation of th e
Lie group GL( g).)
(ii) Show that if G is a connected and simply connected Lie group with Lie algebr a g,
then the group of (Lie) automorphisms of G is isomorphic to Aut( g).
(iii) Show that ad: g → End(g) actually has its image in der(g), and that this image is an
ideal in der(g). What is the interpretation of this fact in terms of “inner” and “outer”
automorphisms of G? (Hint: Use the Jacobi identity.)
(iv) Show that if the Killing form of g is non-degenerate, then [ g, g] = g. (Hint: Suppose
that [ g, g] lies in a proper subspace of g. Then there exists an element y ∈ g so that
κ
(
[x,z ],y
)
= 0 for all x,z ∈ g. Show that this implies that [ x,y ] = 0 for all x ∈ g,
and hence that ad( y) = 0.)
(v) Show that if the Killing form of g is non-degenerate, then der(g) = ad( g). This shows
that all of the automorphisms of a simple Lie algebra are “inn er”. (Hint: Show that
E.3.1 59

the set p =
{
a ∈ der(g) | tr
(
a ad(x)
)
= 0 for all x ∈ g
}
is also an ideal in der(g) and
hence that der(g) = p ⊕ ad(g) as algebras. Show that this forces p = 0 by considering
what it means for elements of p (which, after all, are derivations of g) to commute
with elements in ad( g).)
4. Consider the 1-parameter group that is generated by the ﬂow of the vector ﬁeld X in
the plane
X = cosy∂
∂x + sin2y∂
∂y.
Show that this vector ﬁeld is complete and hence yields a free R-action on the plane. Let
Z also act on the plane by the action
m · (x,y ) = (( −1)mx,y +mπ).
Show that these two actions commute, and hence together deﬁn e a free action of G = R×Z
on the plane. Sketch the orbits and show that, even though the G-orbits of this action are
closed, and the quotient space is Hausdorﬀ, the quotient spa ce is not a manifold. (The
point of this problem is to warn the student not to make the com mon mistake of thinking
that the quotient of a manifold by a free Lie group action is a m anifold if it is Hausdorﬀ.)
5. Show that if ρ:M ×G → M is a right action, then the induced map ρ∗: g → X(M )
satisﬁes ρ∗
(
[x,y ]
)
=
[
ρ∗(x),ρ ∗(y)
]
.
6. Prove Proposition 2. (Hint: you are trying to ﬁnd an open nei ghborhood U of {e} ×M
inG ×M and a smooth map λ:U →M with the requisite properties. To do this, look for
the graph of λ as a submanifold Γ ⊂ G ×M ×M that contains all the points ( e,m,m )
and is tangent to a certain family of vector ﬁelds on G ×M ×M constructed using the
left invariant vector ﬁelds on G and the corresponding vector ﬁelds on M determined by
the Lie algebra homomorphism φ: g → X(M ).)
7. Show that, if A: R → g is a curve in the Lie algebra of a Lie group G, then there exists
a unique solution to the ordinary diﬀerential equation S′(t) = RS(t)
(
A(t)
)
with initial
condition S(0) = e. (It is clear that a solution exists on some interval ( −ε,ε ) in R. The
problem is to show that the solution exists on all of R.)
8. Show that, under the action of GL( n, R) on the space of symmetric n-by-n matrices
deﬁned in the Lecture, every symmetric n-by-n matrix is in the orbit of an Ip,q.
9. This problem examines the geometry of the classical second order equation for one
unknown.
(i) Rewrite the second-order ODE
d2x
dt2 =F (t)x
as a system of ﬁrst-order ODEs of Lie type for an action of SL(2 , R) on R2.
E.3.2 60

(ii) Suppose in particular that F (t) is of the form
(
f (t)
)2
+f ′(t), where f (0) ⁄= 0. Use
the solution
x(t) = exp
(∫ t
0
f (τ )dτ
)
to write down the fundamental solution for this Lie equation up in SL(2, R).
(iii) Explain why the (more general) second order linear ODE
x′′ =a(t)x′ +b(t)x
is solvable by quadratures once we know a single solution wit h either x(0) ⁄= 0 or
x′(0) ⁄= 0. (Hint: all two-dimensional Lie groups are solvable.)
10*. Show that the general equation of the form y′′(x) = f (x)y(x) is not integrable by
quadratures. Speciﬁcally, show that there do not exist “uni versal” functions F0 and F1
of two and three variables respectively so that the function y deﬁned by taking the most
general solution of
u′(x) = F0
(
x,f (x)
)
y′(x) = F1
(
x,f (x),u (x)
)
is the general solution of y′′(x) = f (x)y(x). Note that this shows that the general solution
cannot be got by two quadratures, which one might expect to ne ed since the general
solution must involve two constants of integration. Howeve r, it can be shown that no
matter how many quadratures one uses, one cannot get even a pa rticular solution of
y′′(x) = f (x)y(x) (other than the trivial solution y ≡ 0) by quadrature. (If one could get
a (non-trivial) particular solution this way, then, by two m ore quadratures, one could get
the general solution.)
11. The point of this exercise is to prove Lie’s theorem (stated below) on (local) group
actions on R. This theorem “explains” the importance of the Riccati equa tion, and why
there are so few actions of Lie groups on R. Let g ⊂ X(R) be a ﬁnite dimensional Lie
algebra of vector ﬁelds on R with the property that, at every x ∈ R, there is at least one
X ∈ g so that X(x) ⁄= 0. (Thus, the (local) ﬂows of the vector ﬁelds in g do not have any
common ﬁxed point.)
(i) For each x ∈ R, let gk
x ⊂ g denote the subspace of vector ﬁelds that vanish to order
at least k + 1 at x. (Thus, g−1
x = g for all x.) Let g∞
x ⊂ g denote the intersection
of all the gk
x. Show that g∞
x = 0 for all x. (Hint: Fix a ∈ R and choose an X ∈ g
so that X(a) ⁄= 0. Make a local change of coordinates near a so that X = ∂/∂x on
a neighborhood of a. Note that [ X, g∞
a ] ⊂ g∞
a . Now choose a basis Y1,...,Y N of g∞
a
and note that, near a, we have Yi =fi∂/∂x for some functions fi. Show that the fi
must satisfy some diﬀerential equations and then apply ODE u niqueness. Now go on
from there.)
* This exercise is somewhat diﬃcult, but you should enjoy see ing what is involved in
trying to prove that an equation is not solvable by quadratur es.
E.3.3 61

(ii) Show that the dimension of g is at most 3. (Hint: First, show that [ gj
x, gk
x] =⊂ gj+k
x .
Now, by part (i), you know that there is a smallest integer N (which may depend on
x) so that gN+1
x = 0. Show that if X ∈ g does not vanish at x andYN ∈ g vanishes to
exactly order N atx, then YN−1 = [X,YN ] vanishes to order exactly N − 1. Conclude
that the vectors X,Y 0,...,Y N (whereYi−1 = [X,Yi] for i> 0) form a basis of g. Now,
what do you know about [ YN−1,YN ]?).
(iii) (Lie’s Theorem) Show that, if dim( g) = 2, then g is isomorphic to the (unique) non-
abelian Lie algebra of that dimension and that there is a loca l change of coordinates
so that
g = {(a +bx)∂/∂x |a,b ∈ R}.
Show also that, if dim( g) = 3, then g is isomorphic to sl(2, R) and that there exist
local changes of coordinates so that
g = {(a +bx +cx2)∂/∂x |a,b,c ∈ R}.
(In the second case, after you have shown that the algebra is i somorphic to sl(2, R),
show that, at each point of R, there exists a element X ∈ g that does not vanish at
the point and that satisﬁes
(
ad(X)
)2
= 0. Now put it in the form X =∂/∂x for some
local coordinate x and ask what happens to the other elements of g.)
(iv) (This is somewhat harder.) Show that if dim( g) = 3, then there is a diﬀeomorphism
of R with an open interval I ⊂ R so that g gets mapped to the algebra
g =
{
(a +b cosx +c sinx)∂
∂x a,b,c ∈ R
}
.
In particular, this shows that every local action of SL(2 , R) on R is the restriction
of the M¨ obius action on RP1 after “lifting” to its universal cover. Show that two
intervals I1 = (0,a ) and I2 = (0,b ) are diﬀeomorphic in such a way as to preserve
the Lie algebra g if and only if either a =b = 2nπ for some positive integer n or else
2nπ <a,b< (2n + 2)π for some positive integer n. (Hint: Show, by a local analysis,
that any vector ﬁeld X ∈ g that vanishes at any point of R must have κ(X,X ) ≥ 0.
Now choose an X so that κ(X,X ) = −2 and choose a global coodinate x: R → R
so that X = ∂/∂x . You must still examine the eﬀect of your choices on the image
intervalx(R) ⊂ R.)
Lie and his coworkers attempted to classify all of the ﬁnite d imensional Lie subalgebras
of the vector ﬁelds on Rk, for k ≤ 5, since (they thought) this would give a classiﬁcation
of all of the equations of Lie type for at most 5 unknowns. The c lassiﬁcation became
extremely complex and lengthy by dimension 5 and it was aband oned. On the other hand,
the project of classifying the abstract ﬁnite dimensional Lie algebras has enjoyed a great
deal of success. In fact, one of the triumphs of nineteenth ce ntury mathematics was the
classiﬁcation, by Killing and Cartan, of all of the ﬁnite dim ensional simple Lie algebras
over C and R.
E.3.4 62

Lecture 4:
Symmetries and Conservation Laws
V ariational Problems. In this Lecture, I will introduce a particular set of variati onal
problems, the so-called ‘ﬁrst-order particle Lagrangian p roblems’, that will serve as a link
to the ‘symplectic’ geometry to be developed in the next Lect ure.
Deﬁnition 1: A Lagrangian on a manifold M is a smooth function L:TM → R. For any
smooth curve γ: [a,b ] →M , deﬁne
FL(γ) =
∫ b
a
L
(
˙γ(t)
)
dt.
FL is called the functional associated to L.
(The use of the word “functional” here is classical. The read er is supposed to think
of the set of all smooth curves γ: [a,b ] →M as a sort of inﬁnite dimensional manifold and
of FL as a function on it.)
I have deliberately chosen to avoid the (mild) complication s caused by allowing less
smoothness for L andγ, though for some purposes, it is essential to do so. The geome tric
points that I want to make, however will be clearest if we do no t have to worry about
determining the optimum regularity assumptions.
Also, some sources only require L to be deﬁned on some open set in TM . Others
allow L to “depend on t”, i.e., take L to be a function on R ×TM . Though I will not
go into any of these (slight) extensions, the reader should b e aware that they exist. For
example, see [A].
Example: Suppose that L:TM → R restricts to each TxM to be a positive deﬁnite
quadratic form. Then L deﬁnes what is usually called a Riemannian metric on M . For a
curveγ in M , the functional FL(γ) is then twice what is usually called the “action” of γ.
This example is, by far, the most commonly occurring Lagrang ian in diﬀerential geometry.
We will have more to say about this below.
For a Lagrangian L, one is usually interested in ﬁnding the curves γ: [a,b ] →M with
given “endpoint conditions” γ(a) = p and γ(b) = q for which the functional FL(γ) is a
minimum. For example, in the case where L deﬁnes a Riemannian metric on M , the curves
with ﬁxed endpoints of minimum “action” turn out also to be th e shortest curves joining
those endpoints. From calculus, we know that the way to ﬁnd mi nima of a function on a
manifold is to ﬁrst ﬁnd the “critical points” of the function and then look among those
for the minima. As mentioned before, the set of curves in M can be thought of as a sort
of “inﬁnite dimensional” manifold, but I won’t go into detai ls on this point. What I will
do instead is describe what ought to be the set of “curves” in t his space (classically called
“variations”) if it were a manifold.
L.4.1 63

Given a curve γ: [a,b ] → M , a (smooth) variation of γ with ﬁxed endpoints is, by
deﬁnition, a smooth map
Γ : [a,b ] × (−ε,ε ) →M
for some ε> 0 with the property that Γ( t, 0) = γ(t) for all t ∈ [a,b ] and that Γ(a,s ) = γ(a)
and Γ(b,s ) = γ(b) for all s ∈ (−ε,ε ).
◮ In this lecture, “variation” will always mean “smooth varia tion with ﬁxed endpoints”.
If L is a Lagrangian on M and Γ is a variation of γ: [a,b ] →M , then we can deﬁne a
function FL,Γ : (−ε,ε ) → R by setting
FL,Γ (s) = FL(γs)
where γs(t) = Γ(t,s ).
Deﬁnition 2: A curve γ: [a,b ] →M is L-critical if F ′
L,Γ (0) = 0 for all variations of γ.
It is clear from calculus that a curve that minimizes FL among all curves with the
same endpoints will have to be L-critical, so the search for minimizers usually begins with
the search for the critical curves.
Canonical Coordinates. I want to examine what the problem of ﬁnding L-critical
curves “looks like” in local coordinates. If U ⊂M is an open set on which there exists a
coordinate chart x:U → Rn, then there is a canonical extension of these coordinates to a
coordinate chart (x,p ):TU → Rn × Rn with the property that, for any curve γ: [a,b ] →U ,
with coordinates y = x ◦γ, the p-coordinates of the curve ˙ γ: [a,b ] → TU are given by
p ◦ ˙γ = ˙y. We shall call the coordinates ( x,p ) on TU , the canonical coordinates associated
to the coordinate system x on U .
The Euler-Lagrange Equations. In a canonical coordinate system ( x,p ) on TU
where U is an open set in M , the function L can be expressed as a function L(x,p ) of
x and p. For a curve γ: [a,b ] → M that happens to lie in U , the functional FL becomes
simply
FL(γ) =
∫ b
a
L
(
y(t), ˙y(t)
)
dt.
I will now derive the classical conditions for such a γ to beL-critical: Let h: [a,b ] → Rn
be any smooth map that satisﬁes h(a) = h(b) = 0. Then, for suﬃciently small ε, there is
a variation Γ of γ that is expressed in ( x,p )-coordinates as
(x,p ) ◦ Γ = (y +sh, ˙y +s ˙h).
L.4.2 64

Then, by the classic integration-by-parts method,
F ′
L,Γ (0) = d
ds
⏐
⏐
⏐
s=0
(∫ b
a
L
(
y(t) +sh(t), ˙y(t) +s ˙h(t)
)
dt
)
=
∫ b
a
(∂L
∂xk
(
y(t), ˙y(t)
)
hk(t) + ∂L
∂pk
(
y(t), ˙y(t)
)˙hk(t)
)
dt
=
∫ b
a
(∂L
∂xk
(
y(t), ˙y(t)
)
− d
dt
(∂L
∂pk
(
y(t), ˙y(t)
)))
hk(t)dt.
This formula is valid for any h: [a,b ] → Rn that vanishes at the endpoints. It follows
without diﬃculty that the curve γ is L-critical if and only if y = x ◦γ satisﬁes the n
diﬀerential equations
∂L
∂xk
(
y(t), ˙y(t)
)
− d
dt
(∂L
∂pk
(
y(t), ˙y(t)
))
= 0, for 1 ≤k ≤n.
These are the famous Euler-Lagrange equations.
The main drawback of the Euler-Lagrange equations in this fo rm is that they only
give necessary and suﬃcient conditions for a curve to be L-critical if it lies in a coordinate
neighborhoodU . It is not hard to show that if γ: [a,b ] →M isL-critical, then its restriction
to any subinterval [a′,b ′] ⊂ [a,b ] is also L-critical. In particular, a necessary condition for
γ to be L-critical is that it satisfy the Euler-Lagrange equations o n any subcurve that lies
in a coordinate system. However, it is not clear that these ‘local conditions’ are suﬃcient.
Another drawback is that, as derived, the equations depend o n the choice of coordi-
nates and it is not clear that one’s success in solving them mi ght not depend on a clever
choice of coordinates.
In what follows, we want to remedy these defects. First, thou gh, here are a couple of
examples.
Example: Riemannian Metrics. Consider a Riemannian metric L:TM → R. Then,
in local canonical coordinates,
L(x,p ) = gij(x)pipj.
where g(x) is a positive deﬁnite symmetric matrix of functions. (Reme mber, the summa-
tion convention is in force.) In this case, the Euler-Lagran ge equations are
∂gij
∂xk
(
y(t)
)
˙yi(t) ˙yj(t) = d
dt
(
2gkj
(
y(t)
)
˙yj(t)
)
= 2∂gkj
∂xi
(
y(t)
)
˙yi(t) ˙yj(t) + 2gkj
(
y(t)
)
¨yj(t).
Since the matrix g(x) is invertible for all x, these equations can be put in more familiar
form by solving for the second derivatives to get
¨yi = −Γi
jk (y) ˙yj ˙yk
L.4.3 65

where the functions Γ i
jk = Γi
kj are given by the formula so familiar to geometers:
Γi
jk = 1
2giℓ
(∂gℓj
∂xk + ∂gℓk
∂xj − ∂gjk
∂xℓ
)
where the matrix
(
gij)
is the inverse of the matrix
(
gij
)
.
Example: One-Forms. Another interesting case is when L is linear on each tangent
space, i.e., L =ω where ω is a smooth 1-form on M . In local canonical coordinates,
L =ai(x)pi
for some functions ai and the Euler-Lagrange equations become:
∂ai
∂xk
(
y(t)
)
˙yi(t) = d
dt
(
ak
(
y(t)
))
= ∂ak
∂xi
(
y(t)
)
˙yi(t)
or, simply, (∂ai
∂xk (y) − ∂ak
∂xi (y)
)
˙yi = 0.
This last equation should look familiar. Recall that the ext erior derivative of ω has the
coordinate expression
dω = 1
2
(∂aj
∂xi − ∂ai
∂xj
)
dxi ∧dxj.
If γ: [a,b ] → U is Fω-critical, then for every vector ﬁeld v along γ the Euler-Lagrange
equations imply that
dω
(
˙γ(t),v (t)
)
= 1
2
(∂aj
∂xi
(
y(t)
)
− ∂ai
∂xj
(
y(t)
))
˙yi(t)vj(t) = 0.
In other words, ˙γ(t) dω = 0. Conversely, if this identity holds, then γ is clearly ω-critical.
This leads to the following global result:
Proposition 1: A curve γ: [a,b ] →M is ω-critical for a 1-form ω on M if and only if it
satisﬁes the ﬁrst order diﬀerential equation
˙γ(t)
dω = 0.
Proof: A straightforward integration-by-parts on M yields the coordinate-free formula
F ′
ω,Γ (0) =
∫ b
a
dω
(
˙γ(t), ∂Γ
∂s (t, 0)
)
dt
where Γ is any variation of γ and ∂Γ
∂s is the “variation vector ﬁeld” along γ. Since this
vector ﬁeld is arbitrary except for being required to vanish at the endpoints, we see that
“dω
(
˙γ,v
)
= 0 for all vector ﬁelds v along γ” is the desired condition for ω-criticality. □
L.4.4 66

The way is now paved for what will seem like a trivial observat ion, but, in fact, turns
out to be of fundamental importance: It is the “seed” of Noeth er’s Theorem.
Proposition 2: Suppose that ω is a 1-form on M and that X is a vector ﬁeld on M
whose (local) ﬂow leaves ω invariant. Then the function ω(X) is constant on all ω-critical
curves.
Proof: The condition that the ﬂow of X leave ω invariant is just that LX (ω) = 0.
However, by the Cartan formula,
0 = LX (ω) = d(X
ω) +X dω,
so for any curve γ in M , we have
dω
(
˙γ(t),X (γ(t))
)
= −dω
(
X(γ(t)), ˙γ(t)
)
= −(X dω)
(
˙γ(t)
)
=d(X ω)
(
˙γ(t)
)
and this last expression is clearly the derivative of the fun ction X ω = ω(X) along γ.
Now apply Proposition 1. □
It is worth pausing a moment to think about what Proposition 2 means. The condition
that the ﬂow of X leaveω invariant is essentially saying that the ﬂow of X is a “symmetry”
of ω and hence of the functional Fω. What Proposition 2 says is that a certain kind of
symmetry of the functional gives rise to a “ﬁrst integral” (s ometimes called “conservation
law”) of the equation for ω-critical curves. If the function ω(X) is not a constant function
onM , then saying that the ω-critical curves lie in its level sets is useful information about
these critical curves.
Now, this idea can be applied to the general Lagrangian with s ymmetries. The only
trick is to ﬁnd the appropriate 1-form on which to evaluate ‘s ymmetry’ vector ﬁelds.
Proposition 3: For any LagrangianL:TM → R, there exist a unique function EL onTM
and a unique 1-form ωL on TM that, relative to any local coordinate system x:U → R,
have the expressions
EL =pi∂L
∂pi −L and ωL = ∂L
∂pi dxi.
Moreover, if γ: [a,b ] →M is any curve, then γ satisﬁes the Euler-Lagrange equations for
L in every local coordinate system if and only if its canonical lift ˙γ: [a,b ] →TM satisﬁes
¨γ(t) dωL = −dEL( ˙γ(t)).
Proof: This will mainly be a sequence of applications of the Chain Ru le.
There is an invariantly deﬁned vector ﬁeld R on TM that is simply the radial vector
ﬁeld on each subspace TmM . It is expressed in canonical coordinates as R = pi∂/∂pi.
Now, using this vector ﬁeld, the quantity EL takes the form
EL = −L +dL(R).
L.4.5 67

Thus, it is clear that EL is well-deﬁned on TM .
Now we check the well-deﬁnition of ωL. If z:U → R is any other local coordinate
system, then z =F (x) for some F : Rn → Rn. The corresponding canonical coordinates on
TU are (z,q ) where q =F ′(x)p. In particular,
(
dz
dq
)
=
(
F ′(x) 0
G(x,p ) F ′(x)
)(
dx
dp
)
.
where G is some matrix function whose exact form is not relevant. The n writing Lz for(∂L
∂z 1,..., ∂L
∂z n
)
, etc., yields
dL =Lzdz +Lqdq
=
(
LzF ′(x) +LqG(x,p )
)
dx +LqF ′(x)dp
=Lxdx +Lpdp.
Comparingdp-coeﬃcients yields Lp =LqF ′(x), so Lpdx =LqF ′(x)dx =Lqdz. In partic-
ular, as we wished to show, there exists a well-deﬁned 1-form ωL onTM whose coordinate
expression in local canonical coordinates ( x,p ) is Lpdx.
The remainder of the proof is a coordinate calculation. The r eader will want to note
that I am using the expression ¨ γ to denote the velocity of the curve ˙ γ in TM . The curve
˙γ is described in U as (x,p ) = (y, ˙y) and its velocity vector ¨γ is simply ( ˙x, ˙p) = ( ˙y, ¨y).
Now, the Euler-Lagrange equations are just
∂L
∂xi (y, ˙y) = d
dt
(∂L
∂pi (y, ˙y)
)
= ∂2L
∂pi∂pj (y, ˙y)¨yj + ∂2L
∂pi∂xj (y, ˙y) ˙yj.
Meanwhile,
dωL = ∂2L
∂pi∂pjdpj ∧dxi + ∂2L
∂pi∂xjdxj ∧dxi,
so
¨γ dωL = ∂2L
∂pi∂pj (y, ˙y)
(
¨yjdxi − ˙yidpj)
+ ∂2L
∂pi∂xj (y, ˙y)
(
˙yjdxi − ˙yidxj)
.
On the other hand, an easy computation yields
−dEL( ˙γ) =
(∂L
∂xi (y, ˙y) − ∂2L
∂pj∂xi (y, ˙y) ˙yj
)
dxi − ∂2L
∂pi∂pj (y, ˙y) ˙yidpj.
Comparing these last two equations, the condition ¨ γ dωL = −dEL( ˙γ) is seen to be the
Euler-Lagrange equations, as desired. □
Conservation of Energy . One important consequence of Proposition 3 is that the
function EL is constant along the curve ˙ γ for any L-critical curve γ: [a,b ] → M . This
follows since, for such a curve,
dEL
(
¨γ(t)
)
= −dωL
(
¨γ(t), ¨γ(t)
)
= 0.
EL is generally interpreted as the “energy” of the Lagrangian L, and this constancy of EL
on L-critical curves is often called the principle of Conservat ion of Energy.
◮ Some sources deﬁne EL as L −dL(R). My choice was to have EL agree with the
classical energy in the classical problems.
L.4.6 68

Deﬁnition 3: IfL:TM → R is a Lagrangian on M , a diﬀeomorphism f :M →M is said
to be a symmetry ofL ifL is invariant under the induced diﬀeomorphism f ′:TM →TM ,
i.e., if L ◦f ′ =L. A vector ﬁeld X on M is said to be an inﬁnitesimal symmetry of L if
the (local) ﬂow Φ t of X is a symmetry of L for all t.
It is perhaps necessary to make a remark about the last part of this deﬁnition. For a
vector ﬁeld X that is not necessarily complete, and for any t ∈ R, the “time t” local ﬂow
ofX is well-deﬁned on an open set Ut ⊂M . The local ﬂow of X then gives a well-deﬁned
diﬀeomorphism Φ t:Ut →U−t. The requirement for X is that, for each t for which Ut ⁄= ∅,
the induced map Φ ′
t:TUt →TU −t should satisfy L ◦ Φ ′
t =L. (Of course, if X is complete,
then Ut =M for all t, so symmetry has its usual meaning.)
Let X be any vector ﬁeld on M with local ﬂow Φ. This induces a local ﬂow on TM
that is associated to a vector ﬁeld X ′ on TM . If, in a local coordinate chart, x:U → Rn,
the vector ﬁeld X has the expression
X =ai(x)∂
∂xi,
then the reader may check that, in the associated canonical c oordinates on TU ,
X ′ =ai ∂
∂xi +pj∂ai
∂xj
∂
∂pi.
The condition that X be an inﬁnitesimal symmetry of L is then that L be invariant
under the ﬂow of X ′, i.e., that
dL(X ′) = ai ∂L
∂xi +pj∂ai
∂xj
∂L
∂pi = 0.
The following theorem is now a simple calculation. Neverthe less, it is the foundation
of a vast theory. It usually goes by the name “Noether’s Theor em”, though, in fact,
Noether’s Theorem is more general.
Theorem 1: If X is an inﬁnitesimal symmetry of the Lagrangian L, then the function
ωL(X ′) is constant on ˙γ: [a,b ] →TM for every L-critical path γ: [a,b ] →M .
Proof: Since the ﬂow of X ′ ﬁxes L it should not be too surprising that it also ﬁxes EL
and ωL. These facts are easily checked by the reader in local coordi nates, so they are left
as exercises. In particular,
LX′ωL =d(X ′
ωL) +X ′ dωL = 0 and LX′EL =dEL(X ′) = 0.
Thus, for any L-critical curve γ in M ,
d
(
ωL(X ′)
)(
¨γ(t)
)
=d(X ′ ωL)
(
¨γ(t)
)
= −(X ′ dωL)
(
¨γ(t)
)
=dωL
(
¨γ(t),X ′( ˙γ(t))
)
=
(
¨γ(t) dωL
)(
X ′( ˙γ(t))
)
= −dEL
(
X ′( ˙γ(t))
)
= 0.
L.4.7 69

Hence, the function ωL(X ′) is constant on ˙γ, as desired. □
Of course, the formula for ωL(X ′) in local canonical coordinates is simply
ωL(X ′) = ai∂L
∂pi,
and the constancy of this function on the solution curves of t he Euler-Lagrange equations
is not diﬃcult to check directly.
The principle
Symmetry =⇒ Conservation Law
is so fundamental that whenever a new system of equations is e ncountered an enormous
eﬀort is expended to determine its symmetries. Moreover, th e intuition is often expressed
that “every conservation law ought to come from some symmetr y”, so whenever conserved
quantities are observed in Nature (or, more accurately, our models of Nature) people
nowadays look for a symmetry to explain it. Even when no symme try is readily apparent,
in many cases a sort of “hidden symmetry” can be found.
Example: Motion in a Central Force Field. Consider the Lagrangian of “kinetic
minus potential energy” for an particle (of mass m ⁄= 0) moving in a “central force ﬁeld”.
Here, we take Rn with its usual inner product and a function V (|x|2) (called the potential
energy) that depends only on distance from the origin. The La grangian is
L(x,p ) = m
2 |p|2 −V (|x|2).
The function EL is given by
EL(x,p ) = m
2 |p|2 +V (|x|2),
and ωL =mpidxi =mp ·dx.
The Lagrangian L is clearly symmetric with respect to rotations about the ori gin. For
example, the rotation in the ij-plane is generated by the vector ﬁeld
Xij =xj∂
∂xi −xi∂
∂xj.
According to Noether’s Theorem, then, the functions
µij =ωL(X ′
ij) = m
(
xjpi −xipj)
are constant on all solutions. These are usually called the “ angular momenta”. It follows
from their constancy that the bivector ξ =y(t)∧ ˙y(t) is constant on any solution x =y(t) of
the Euler-Lagrange equations and hence that y(t) moves in a ﬁxed 2-plane. Thus, we are
essentially reduced to the case n = 2. In this case, for constants E0 and µ0, the equations
m
2 |p|2 +V (|x|2) = E0 and m(x1p2 −x2p1) = µ0
L.4.8 70

will generically deﬁne a surface in T R2. The solution curves to the Euler-Lagrange equa-
tions
˙x =p and ˙ p = − 2
mV ′(|x|2)x
that lie on this surface can then be analyzed by phase portrai t methods. (In fact, they can
be integrated by quadrature.)
Example: Riemannian metrics with Symmetries. As another example, consider
the case of a Riemannian manifold with inﬁnitesimal symmetr ies. If the ﬂow of X on M
preserves a Riemannian metric L, then, in local coordinates,
L =gij(x)pipj
and
X =ai(x)∂
∂xi.
According to Conservation of Energy and Noether’s Theorem, the functions
EL =gij(x)pipj and ωL(X ′) = 2gij(x)ai(x)pj
are ﬁrst integrals of the geodesic equations.
For example, if a surface S ⊂ R3 is a surface of revolution, then the induced metric
can locally be written in the form
I =E(r)dr2 + 2F (r)drdθ +G(r)dθ2
where the rotational symmetry is generated by the vector ﬁel d X =∂/∂θ . The following
functions are then constant on solutions of the geodesic equ ations:
E(r) ˙r2 + 2F (r) ˙r ˙θ +G(r) ˙θ2 and F (r) ˙r +G(r) ˙θ.
This makes it possible to integrate by quadratures the geode sic equations on a surface of
revolution, a classical accomplishment. (See the Exercise s for details.)
Subexample: Left Invariant Metrics on Lie Groups. LetG be a Lie group and let
ω1,ω 2,...,ω n be any basis for the left-invariant 1-forms on G. Consider the Lagrangian
L =
(
ω1)2
+ · · · + (ωn)2,
which deﬁnes a left-invariant metric on G. Since left translations are symmetries of this
metric and since the ﬂows of the right-invariant vector ﬁelds Yi leave the left-invariant
1-forms ﬁxed, we see that these generate symmetries of the La grangian L. In particular,
the functions EL =L and
µi =ω1(Yi)ω1 + · · · +ωn(Yi)ωn
L.4.9 71

are functions on TG that are constant on all of the geodesics of G with the metric L. I
will return to this example several times in future lectures .
Subsubexample: The Motion of Rigid Bodies. A special case of the Lie group example
is particularly noteworthy, namely the theory of the rigid b ody.
A rigid body (in Rn) is a (ﬁnite) set of points x1,..., xN with masses m1,...,m N
such that the distances dij = |xi − xj | are ﬁxed (hence the name “rigid”). The free motion
of such a body is governed by the “kinetic energy” Lagrangian
L = m1
2 |p1|2 + · · · + mN
2 |pN |2.
where pi represents the velocity of the i’th point mass. Here is how this can be converted
into a left-invariant Lagrangian variational problem on a L ie group:
Let G be the matrix Lie group
G =
{(
A b
0 1
)⏐
⏐
⏐
⏐
⏐A ∈ O(n),b ∈ Rn
}
.
Then G acts as the space of isometries of Rn with its usual metric and thus also acts on
the N -fold product
YN = Rn × Rn × · · · × Rn
by the “diagonal” action. It is not diﬃcult to show that G acts transitively on the simul-
taneous level sets of the functions fij(x) = |xi − xj|. Thus, for each symmetric matrix
∆ = ( dij), the set
M∆ = {x ∈YN | | xi − xj | =dij }
is an orbit of G (and hence a smooth manifold) when it is not empty. The set M∆ is said to
be the “conﬁguration space” of the rigid body. (Question: Ca n you determine a necessary
and suﬃcient condition on the matrix ∆ so that M∆ is not empty? In other words, which
rigid bodies are possible?)
Let us suppose that M∆ is not empty and let ¯x ∈M∆ be a ‘reference conﬁguration’,
which, for convenience, we shall suppose has its center of ma ss at the origin:
mk ¯xk = 0.
(This can always be arranged by a simultaneous translation o f all of the point masses.)
Now let γ: [a,b ] →M∆ be a curve in the conﬁguration space. (Such curves are often c alled
“trajectories”.) Since M∆ is a G-orbit, there is a curve g: [a,b ] →G so that γ(t) = g(t) · ¯x.
Let us write
γ(t) = ( x1(t),..., xN (t))
and let
g(t) =
(
A(t) b(t)
0 1
)
.
L.4.10 72

The value of the canonical left invariant form on g is
g−1 ˙g =
(
α β
0 0
)
=
(
A−1 ˙A A −1 ˙b
0 0
)
.
The kinetic energy along the trajectory γ is then
1
2
∑
k
mk | ˙xk|2 = 1
2
∑
k
mk ( ˙xk · ˙xk) = 1
2
∑
k
mk
(
˙A¯xk + ˙b
)
·
(
˙A¯xk + ˙b
)
.
Since A is a curve in O( n), this becomes
= 1
2
∑
k
mk
(
(A−1(˙A¯xk + ˙b
))
·
(
(A−1(˙A¯xk + ˙b
))
= 1
2
∑
k
mk (α¯xk +β) · (α¯xk +β).
Using the center-of-mass normalization, this simpliﬁes to
= 1
2
∑
k
mk
(
−t¯xkα2 ¯xk + |β|2)
.
With a slight rearrangement, this takes the simple form
L
(
˙γ(t)
)
= −tr
((
α(t)
)2
µ
)
+ 1
2m |β(t)|2
wherem =m1 + · · · +mN is the total mass of the body and µ is the positive semi-deﬁnite
symmetric n-by-n matrix
µ = 1
2
∑
k
mk ¯xk
t¯xk.
It is clear that we can interpret L as a left-invariant Lagrangian on G. Actually, even the
formula we have found so far can be simpliﬁed: If we write µ =Rδ tR whereδ is diagonal
and R is an orthogonal matrix (which we can always do), then right a cting on G by the
element (
R 0
0 1
)
will reduce the Lagrangian to the form
L
(
˙g(t)
)
= −tr
((
α(t)
)2
δ
)
+ 1
2m |β(t)|2.
Thus, only the eigenvalues of the matrix µ really matter in trying to solve the equations
of motion of a rigid body. This observation is usually given a n interpretation like “the
motion of any rigid body is equivalent to the motion of its ‘el lipsoid of inertia’ ”.
Hamiltonian F orm. Let us return to the consideration of the Euler-Lagrange equ a-
tions. As we have seen, in expanded form, the equations in loc al coordinates are
∂2L
∂pi∂pj (y, ˙y)¨yj + ∂2L
∂pi∂xj (y, ˙y) ˙yj − ∂L
∂xi (y, ˙y) = 0.
L.4.11 73

In order for these equations to be solvable for the highest de rivatives at every possible set
of initial conditions, the symmetric matrix
HL(x,p ) =
( ∂2L
∂pi∂pj (x,p )
)
.
must be invertible at every point ( x,p ).
Deﬁnition 4: A Lagrangian L is said to be non-degenerate if, relative to every local
coordinate system x:U → Rn, the matrix HL is invertible at every point of TU .
For example, if L:TM → R restricts to each tangent space TmM to be a non-
degenerate quadratic form, then L is a non-degenerate Lagrangian. In particular, when L
is a Riemannian metric, L is non-degenerate.
Although Deﬁnition 4 is fairly explicit, it is certainly not coordinate free. Here is a
result that may clarify the meaning of non-degenerate.
Proposition 4: The following are equivalent for a Lagrangian L:TM → R:
(1) L is a non-degenerate Lagrangian.
(2) In local coordinates (x,p ), the functions x1,...,x n,∂L/∂p 1,...,∂L/∂p n have every-
where independent diﬀerentials.
(3) The 2-form dωL is non-degenerate at every point of TM , i.e., for any tangent vector
v ∈T (TM ),v
dωL = 0 implies that v = 0.
Proof: The equivalence of (1) and (2) follows directly from the Chai n Rule and is left
as an exercise. The equivalence of (2) and (3) can be seen as fo llows: Let v ∈ Ta(TM )
be a tangent vector based at a ∈TmM . Choose any local any canonical local coordinate
system (x,p ) with m ∈U and write qi =∂L/∂pi for 1 ≤i ≤n. Then ωL takes the form
dωL =dqi ∧dxi.
Thus,
v dωL =dqi(v)dxi −dxi(v)dqi.
Now, suppose that the diﬀerentials dx1,...,dx n,dqi,...,dq n are linearly independent
at a and hence span T ∗
a (TM ). Then, if v dωL = 0, we must have dqi(v) = dxi(v) = 0,
which, because the given 2 n diﬀerentials form a spanning set, implies that v = 0 Thus,
dωL is non-degenerate at a.
On the other hand, suppose that that the diﬀerentials dx1,...,dx n,dq 1,...,dq n are
linearly dependent ata. Then, by linear algebra, there exists a non-zero vector v ∈T ∗
a (TM )
so that dqi(v) = dxi(v) = 0. However, it is then clear that v dωL = 0 for such a v, so
that dωL will be degenerate at a. □
For physical reasons, the function qi is usually called the conjugate momentum to the
coordinate xi.
L.4.12 74

Before exploring the geometric meaning of the coordinate sy stem (x,q ), we want to
give the following description of the L-critical curves of a non-degenerate Lagrangian.
Proposition 5: IfL:TM → R is a non-degenerate Lagrangian, then there exists a unique
vector ﬁeld Y onTM so that, for every L-critical curve γ: [a,b ] →M , the associated curve
˙γ: [a,b ] →TM is an integral curve of Y . Conversely, for any integral curve ϕ: [a,b ] →TM
of Y , the composition φ =π ◦ϕ: [a,b ] →M is an L-critical curve in M .
Proof: It is clear that we should take Y to be the unique vector ﬁeld on TM that satisﬁes
Y dωL = −dEL. (There is only one since, by Proposition 4, dωL is non-degenerate.)
Proposition 3 then says that for every L-critical curve, its lift ˙γ satisﬁes ¨γ(t) = Y ( ˙γ(t)) for
all t, i.e., that ˙γ is indeed an integral curve of Y .
The details of the converse will be left to the reader. First, one must check that, with φ
deﬁned as above, we have ˙φ =ϕ. This is best done in local coordinates. Second, one must
check that φ is indeed L-critical, even though it may not lie entirely within a coord inate
neighborhood. This may be done by computing the variation of φ restricted to appropriate
subintervals and taking account of the boundary terms intro duced by integration by parts
when the endpoints are not ﬁxed. Details are in the Exercises . □
The canonical vector ﬁeld Y on TM is just the coordinate free way of expressing the
fact that, for non-degenerate Lagrangians, the Euler-Lagr angian equations are simply a
non-singular system of second order ODE for maps γ: [a,b ] →M
Unfortunately, the expression for Y in canonical (x,p )-coordinates on TM is not very
nice; it involves the inverse of the matrix HL. However, in the ( x,q )-coordinates, it is
a completely diﬀerent story. In these coordinates, everyth ing takes a remarkably simple
form, a fact that is the cornerstone on symplectic geometry a nd the calculus of variations.
Before taking up the geometric interpretation of these new c oordinates, let us do a
few calculations. We have already seen that , in these coordi nates, the canonical 1-form
ωL takes the simple form ωL =qidxi.
We can also expressEL as a function of (x,q ). It is traditional to denote this expression
byH(x,q ) and call it the Hamiltonian of the variational problem (even though, in a certain
sense, it is the same function as EL). The equation determining the vector ﬁeld Y is
expressed in these coordinates as
Y dωL =Y (dqi ∧dxi) = dqi(Y )dxi −dxi(Y )dqi
= −dH = −∂H
∂xi dxi − ∂H
∂qi
dqi,
so the expression for Y in these coordinates is
Y = ∂H
∂qi
∂
∂xi − ∂H
∂xi
∂
∂qi
.
In particular, the ﬂow of Y takes the form
˙xi = ∂H
∂qi
and ˙ qi = −∂H
∂xi.
L.4.13 75

These equations are known as Hamilton ’s Equations or, sometimes, as the Hamiltonian
form of the Euler-Lagrange equations.
Part of the reason for the importance of the ( x,q ) coordinates is the symmetric way
they treat the positions and momenta. Another reason comes f rom the form the inﬁnites-
imal symmetries take in these coordinates: If X is an inﬁnitesimal symmetry of L and
X ′ is the induced vector ﬁeld on TM with conserved quantity G = ωL(X ′), then, since
LX′ωL = 0,
X ′ dωL = −d(ωL(X ′)) = −dG.
Thus, by the same analysis as above, the ODE represented by X ′ in the (x,q ) coordinates
becomes
˙xi = ∂G
∂qi
and ˙ qi = −∂G
∂xi.
In other words, in the ( x,q ) coordinates, the ﬂow of a symmetry X ′ has the same Hamil-
tonian form as the ﬂow of the vector ﬁeld Y that gives the solutions of the Euler-Lagrange
equations! This method of putting the symmetries of a Lagran gian and the solutions of
the Lagrangian on a sort of equal footing will be seen to have p owerful consequences.
The Cotangent Bundle. Early on in this lecture, we introduced, for each coordinate
chart x:U → Rn, a canonical extension ( x,p ):TU → Rn × Rn and characterized it by a
geometric property. There is also a canonical extension ( x,ξ ):T ∗U → Rn × Rn where
ξ = (ξi):T ∗U → Rn is characterized by the condition that, if f :U → R is any smooth
function on U , then, regarding its exterior derivative df as a section df:U →T ∗U , we have
ξi ◦df = ∂f
∂xi.
I will leave to the reader the task of showing that ( x,ξ ) is indeed a coordinate system
on T ∗U .
It is a remarkable fact that the cotangent bundle π:T ∗M →M of any smooth manifold
carries a canonical 1-form ω deﬁned by the following property: For each α ∈ T ∗
xM , we
deﬁne the linear function ωα:Tα
(
T ∗M
)
→ R by the rule ωα(v) = α
(
π′(α)(v)
)
. I leave to
the reader the task of showing that, in canonical coordinate s (x,ξ
)
:T ∗U → Rn × Rn, this
canonical 1-form has the expression
ω =ξidxi.
The Legendre transformation. Now consider a smooth Lagrangian L:TM → R
as before. We can use L to construct a smooth mapping τL:TM → T ∗M as follows: At
each v ∈ TM , the 1-form ωL(v) is semi-basic, i.e., there exists a (necessarily unique) 1 -
form τL(v) ∈T ∗
π(v)M so that ωL(v) = π∗(
τL(v)
)
. This mapping is known as the Legendre
transformation associated to the Lagrangian L.
L.4.14 76

This deﬁnition is rather abstract, but, in local coordinate s, it takes a simple form.
The reader can easily check that in canonical coordinates as sociated to a coordinate chart
x:U → Rn, we have
(x,ξ ) ◦τL = (x,q ) =
(
xi, ∂L
∂pi
)
.
In other words, the ( x,q ) coordinates are just the canonical coordinates on the cota ngent
bundle composed with the Legendre transformation! It is now immediate that τL is a local
diﬀeomorphism if and only if L is a non-degenerate Lagrangian. Moreover, we clearly have
ωL = τ ∗
L(ω), so the 1-form ωL is also expressible in terms of the canonical 1-form ω and
the Legendre transform.
What about the function EL on TM ? Let us put the following condition on the
Lagrangian L: Let us assume that τL:TM → T ∗M is a (one-to-one) diﬀeomorphism
onto its image τL(TM ) ⊂T ∗M . (Note that this implies that L is non-degenerate, but is
stronger than this.) Then there clearly exists a function on τL(TM ) that pulls back to TM
to be EL. In fact, as the reader can easily verify, this is none other t han the Hamiltonian
function H constructed above.
The fact that the Hamiltonian H naturally ‘lives’ onT ∗M (or at least an open subset
thereof) rather than on TM justiﬁes it being regarded as distinct from the function EL.
There is another reason for moving over to the cotangent bund le when one can: The
vector ﬁeld Y onTM corresponds, under the Legendre transformation, to a vecto r ﬁeld Z
on τL(TM ) that is characterized by the simple rule Z dω = −dH. Thus, just knowing
the Hamiltonian H on an open set in T ∗M determines the vector ﬁeld that sweeps out the
solution curves! We will see that this is a very useful observ ation in what follows.
Poincar´ e Recurrence. To conclude this lecture, I want to give an application of
the geometry of the form ωL to understanding the global behavior of the L-critical curves
when L is a non-degenerate Lagrangian. First, I make the following observation:
Proposition 6: Let L:TM → R be a non-degenerate Lagrangian. Then 2n-form µL =
(dωL)n is a volume form on TM (i.e., it is nowhere vanishing). Moreover the (local) ﬂow
of the vector ﬁeld Y preserves this volume form.
Proof: To see that µL is a volume form, just look in local ( x,q )-coordinates:
µL = (dωL)n = (dqi ∧dxi)n
=n!dq1 ∧dx2 ∧dq2 ∧dx2 ∧ · · · ∧dqn ∧dxn.
By Proposition 4, this latter form is not zero.
Finally, since
LY (dωL) = d(Y dωL) = −d
(
dEL
)
= 0,
it follows that the (local) ﬂow of Y preservesdωL and hence preserves µL. □
Now we shall give an application of Proposition 6. This is the famous Poincar´ e
Recurrence Theorem.
L.4.15 77

Theorem 2: Let L:TM → R be a non-degenerate Lagrangian and suppose that EL is a
proper function on TM . Then the vector ﬁeld Y is complete, with ﬂow Φ: R ×TM →TM .
Moreover, this ﬂow is recurrent in the following sense: For any point v ∈ TM , any open
neighborhood U of v, and any positive time interval T >0, there exists an integer N >0
so that Φ(TN,U ) ∩U ⁄= ∅.
Proof: The completeness of the ﬂow of Y follows immediately from the fact that the
integral curve of Y that passes through v ∈TM must stay in the compact set E−1
L
(
EL(v)
)
.
(Recall thatEL is constant on all of the integral curves of Y .) Details are left to the reader.
I now turn to the proof of the recurrence property. Let E0 =EL(v). By hypothesis,
the set C = E−1
L
(
[E0 − 1,E 0 + 1]
)
is compact, so the µL-volume of the open set W =
E−1
L
(
(E0−1,E 0+1)
)
(which lies inside C) is ﬁnite. It clearly suﬃces to prove the recurrence
property for any open neighborhood U ofv that lies insideW , so let us assume that U ⊂W .
Let φ:W → W be the diﬀeomorphism φ(w) = Φ( T,w ). This diﬀeomorphism is
clearly invertible and preserves the µL-volume of open sets in W . Consider the open sets
Uk = φk(U ) for k > 0 (integers). These open sets all have the same µL-volume and
hence cannot be all disjoint since then their union (which li es in W ) would have inﬁnite
µL-volume. Let 0 <j <k be two integers so that Uj ∩Uk ⁄= ∅. Then, since
Uj ∩Uk =φj (U ) ∩φk(U ) = φj(
U ∩φk−j(U )
)
,
it follows that U ∩φk−j (U ) ⁄= ∅, as we wished to show. □
This theorem has the amazing consequence that, whenever one has a non-degenerate
Lagrangian with a proper energy function, the correspondin g mechanical system “recurs”
in the sense that “arbitrarily near any given initial condit ion, there is another initial
condition so that the evolution brings this initial conditi on back arbitrarily close to the
ﬁrst initial condition”. I realize that this statement is so mewhat vague and subject to
misinterpretation, but the precise statement has already b een given, so there seems not to
be much harm in giving the paraphrase.
L.4.16 78

Exercise Set 4:
Symmetries and Conservation Laws
1. Show that two Lagrangians L1,L 2:TM → R satisfy
EL1 =EL2 and dωL1 =dωL2
if and only if there is a smooth function f on M so that L1 =L2 +df. Such Lagrangians
are said to diﬀer by a “divergence term.” Show that such Lagra ngians share the same
critical curves and that one is non-degenerate if and only if the other is.
2. What does Conservation of Energy mean for the case where L deﬁnes a Riemannian
metric on M ?
3. Show that the equations for geodesics of a rotationally inv ariant metric of the form
I =E(r)dr2 + 2F (r)drdθ +G(r)dθ2
can be integrated by separation of variables and quadrature s. (Hint: Start with the con-
servation laws we already know:
E(r) ˙r2 + 2F (r) ˙r ˙θ +G(r) ˙θ2 =v2
0
F (r) ˙r +G(r) ˙θ =u0
where v0 and u0 are constants. Then eliminate ˙θ and go on from there.)
4. The deﬁnition of ωL given in the text might be regarded as somewhat unsatisfacto ry
since it is given in coordinates and not “invariantly”. Show that the following invariant
description of ωL is valid: The manifold TM inherits some extra structure by virtue of
being the tangent bundle of another manifold M . Let π:TM → M be the basepoint
projection. Then π is a submersion: For every a ∈TM ,
π′(a):TaTM →Tπ(a)M
is a surjection and the ﬁber at π(a) is equal to
π−1(
π(a)
)
=Tπ(a)M.
It follows that the kernel of π′(a) (i.e., the “vertical space” of the bundle π:TM → M
at a) is naturally isomorphic to Tπ(a)M . Call this isomorphism α:Tπ(a)M ˜→ ker
(
π′(a)
)
.
Then the 1-form ωL is deﬁned by
ωL(v) = dL
(
α ◦π′(v)
)
for v ∈T (TM ).
Hint: Show that, in local canonical coordinates, the map α ◦π′ satisﬁes
α ◦π′
(
ai∂
∂xi +bi∂
∂pi
)
=ai∂
∂pi.
E.4.1 79

5. For any vector ﬁeld X on M , let the associated vector ﬁeld on TM be denoted X ′.
Show that if X has the form
X =ai ∂
∂xi
in some local coordinate system, then, in the associated can onical (x,p ) coordinates, X ′
has the form
X ′ =ai ∂
∂xi +pj∂ai
∂xj
∂
∂pi.
6. Show that conservation of angular momenta in the motion of a point mass in a central
force ﬁeld implies Kepler’s Law that “equal areas are swept o ut over equal time intervals.”
Show also that, in the n = 2 case, employing the conservation of energy and angular
momentum allows one to integrate the equations of motion by q uadratures. (Hint: For
the second part of the problem, introduce polar coordinates : (x1,x 2) = (r cosθ,r sinθ).)
7. In the example of the motion of a rigid body, show that the Lag rangian on G is always
non-negative and is non-degenerate (so that L deﬁnes a left-invariant metric on G) if and
only if the matrix µ has at most one zero eigenvalue. Show that L is degenerate if and
only if the rigid body lies in a subspace of dimension at most n−2.
8. Supply the details in the proof of Proposition 5. You will wa nt to go back to the
integration-by-parts derivation of the Euler-Lagrange eq uations and show that, even if the
variation Γ induced by h does not have ﬁxed endpoints, we still get a local coordinate
formula of the form
F ′
L,Γ (0) = ∂L
∂pk
(
y(b), ˙y(b)
)
hk(b) − ∂L
∂pk
(
y(a), ˙y(a)
)
hk(a)
for any variation of a solution of the Euler-Lagrange equati ons. Give these “boundary
terms” an invariant geometric meaning and show that they can cel out when we sum over
a partition of a (ﬁxed-endpoint) variation of an L-critical curve γ into subcurves that lie
in coordinate neighborhoods.)
9. (Alternate to Exercise 8.) Here is another approach to prov ing Proposition 5. Instead of
dividing the curve up into sub-curves, show that for any vari ation Γ of a curve γ: [a,b ] →M
(not necessarily with ﬁxed endpoints), we have the formula
F ′
L,Γ (0) = ωL
(
V (b)
)
−ωL
(
V (a)
)
−
∫ b
a
dωL
(
¨γ(t),V (t)
)
+dEL
(
V (t)
)
dt
where V (t) = ˙Γ ′(t, 0)(∂/∂s) is the “variation vector ﬁeld” at s = 0 of the lifted variation
˙Γ in TM . Conclude that, whether L is non-degenerate or not, the condition ¨ γ
dωL +
dEL
(
˙γ(t)
)
= 0 is the necessary and suﬃcient condition that γ be L-critical.
E.4.2 80

10. The Two Body Problem. Consider a pair of point masses (with masses m1 and
m2) that move freely subject to a force between them that depend s only on the distance
between the two bodies and is directed along the line joining the two bodies. This is what
is classically known as the Two Body Problem. It is represent ed by a Lagrangian on the
manifold M = Rn × Rn with position coordinates x1,x 2:M → Rn of the form
L(x1,x 2,p 1,p 2) = m1
2 |p1|2 + m2
2 |p2|2 −V (|x1 −x2|2).
(Here, ( p1,p 2) are the canonical ﬁber (velocity) coordinates on TM associ ated to the
coordinate system ( x1,x 2).) Notice that L has the form “kinetic minus potential”. Show
that rotations and translations in Rn generate a group of symmetries of this Lagrangian
and compute the conserved quantities. What is the interpret ation of the conservation law
associated to the translations?
11. The Sliding Particle. Suppose that a particle of unit weight and mass (remember:
“geometric units” means never having to state your constant s) slides without friction on
a smooth hypersurface xn+1 = F (x1,...,x n) subject only to the force of gravity (which
is directed downward along the xn+1-axis). Show that the “kinetic-minus-potential” La-
grangian for this motion in the x-coordinates is
L = 1
2
(
(p1)2 + · · · + (pn)2 +
(∂F
∂xipi)2
)
−F (x1,...,x n).
Show that this is a non-degenerate Lagrangian and that its en ergy EL is proper if and
only if F −1(
(−∞,a ]
)
is compact for all a ∈ R.
Suppose that F is invariant under rotation, i.e., that
F (x1,...,x n) = f
(
(x1)2 + · · · + (xn)2)
for some smooth function f . Show that the “shadow” of the particle in Rn stays in a ﬁxed
2-plane. Show that the equations of motion can be integrated by quadrature.
Remark: This Lagrangian is also used to model a small ball of u nit mass and weight
“rolling without friction in a cup”. Of course, in this formu lation, the kinetic energy
stored in the ball by its spinning is ignored. If you want to ta ke this ‘spinning’ energy into
account, then you must study quite a diﬀerent Lagrangian, es pecially if you assume that
the ball rolls without slipping. This goes into the very inte resting theory of ‘non-holonomic
systems’, which we (unfortunately) do not have time to go int o.
12. Let L be a Lagrangian that restricts to each ﬁber TxM to be a non-degenerate
(though not necessarily positive deﬁnite) quadratic form. Show that L is non-degnerate
as a Lagrangian and that the Legendre mapping τL:TM → T ∗M is an isomorphism of
vector bundles. Show that, if L is, in addition a positive deﬁnite quadratic form on each
ﬁber, then the new Lagrangian deﬁned by
˜L =
(
L + 1
)1
2
is also a non-degenerate Lagrangian, but that the map τ ˜L:TM →T ∗M , though one-to-one,
is not onto.
E.4.3 81

Lecture 5:
Symplectic Manifolds, I
In Lecture 4, I associated a non-degenerate 2-form dωL onTM to every non-degenerate
Lagrangian L:TM → R. In this section, I want to begin a more systematic study of th e
geometry of manifolds on which there is speciﬁed a closed, no n-degenerate 2-form.
Symplectic Algebra.
First, I will develop the algebraic precursors of the manifo ld concepts that are to
follow. For simplicity, all of these constructions will be c arried out on vector spaces over
the reals, but they could equally well have been carried out o ver any ﬁeld of characteristic
not equal to 2.
Symplectic V ector Spaces. A bilinear pairing B:V ×V → R is said to be skew-
symmetric (or alternating) if B(x,y ) = −B(y,x ) for all x,y in V . The space of skew-
symmetric bilinear pairings on V will be denoted by A2(V ). The set A2(V ) is a vec-
tor space under the obvious addition and scalar multiplicat ion and is naturally identiﬁed
with Λ 2(V ∗), the space of exterior 2-forms on V . The elements of A2(V ) are often called
skew-symmetric bilinear forms on V. A pairing B ∈A2(V ) is said to be non-degenerate if,
for every non-zero v ∈V , there is a w ∈V for which B(v,w ) ⁄= 0.
Deﬁnition 1: A symplectic space is a pair ( V,B ) where V is a vector space and B is a
non-degenerate, skew-symmetric, bilinear pairing on V .
Example. Let V = R2n and let Jn be the 2n-by-2n matrix
Jn =
(
0n In
−In 0n
)
.
For vectors v,w ∈ R2n, deﬁne
B0(x,y ) = txJny.
Then it is clear that B0 is bilinear and skew-symmetric. Moreover, in components
B0(x,y ) = x1yn+1 + · · · +xny2n −xn+1y1 − · · · −x2nyn
so it is clear that if B0(x,y ) = 0 for all y ∈ R2n then x = 0. Hence, B0 is non-degenerate.
Generally, in order for B(x,y ) = txAy to deﬁne a skew-symmetric bilinear form on
Rn, it is only necessary that A be a skew-symmetric n-by-n matrix. Conversely, every
skew-symmetric bilinear form B on Rn can be written in this form for some unique skew-
symmetric n-by-n matrix A. In order that this B be non-degenerate, it is necessary and
suﬃcient that A be invertible. (See the Exercises.)
L.5.1 82

The Symplectic Group. Now, a linear transformation R: R2n → R2n preservesB0,
i.e., satisﬁes B0(Rx,Ry ) = B0(x,y ) for all x,y ∈ R2n, if and only if tRJnR = Jn. This
motivates the following deﬁnition:
Deﬁnition 2: The subgroup of GL(2 n, R) deﬁned by
Sp(n, R) =
{
R ∈ GL(2n, R) | tRJnR =Jn
}
is called the symplectic group of rank n.
It is clear that Sp( n, R) is a (closed) subgroup of GL(2 n, R). In the Exercises, you are
asked to prove that Sp( n, R) is a Lie group of dimension 2 n2 +n and to derive other of its
properties.
Symplectic Normal F orm. The following proposition shows that there is a normal
form for ﬁnite dimensional symplectic spaces.
Proposition 1: If (V,B ) is a ﬁnite dimensional symplectic space, then there exists a
basis e1,...,e n,f 1...,f n of V so that, for all 1 ≤i,j ≤n,
B(ei,ej) = 0, B (ei,f j) = δj
i, and B(fi,f j) = 0
Proof: The desired basis will be constructed in two steps. Let m = dim(V ).
Suppose that for some n ≥ 0, we have found a sequence of linearly independent vectors
e1,...,e n so that B(ei,ej) = 0 for all 1 ≤ i,j ≤ n. Consider the vector space Wn ⊂ V
that consists of all vectors w ∈ V so that B(ei,w ) = 0 for all 1 ≤ i ≤ n. Since the ei
are linearly independent and since B is non-degenerate, it follows that Wn has dimension
m −n. We must have n ≤m −n since all of the vectors e1,...,e n clearly lie in Wn.
If n < m−n, then there exists a vector en+1 ∈ Wn that is linearly independent
from e1,...,e n. It follows that the sequence e1,...,e n+1 satisﬁes B(ei,ej) = 0 for all
1 ≤ i,j ≤ n + 1. (Since B is skew-symmetric, B(en+1,en+1) = 0 is automatic.) This
extension process can be repeated until we reach a stage wher e n =m −n, i.e., m = 2n.
At that point, we will have a sequence e1,...,e n for whichB(ei,ej) = 0 for all 1 ≤i,j ≤n.
Next, we construct the sequence f 1,...,f n. For each j in the range 1 ≤ j ≤ n,
consider the set of n linear equations
B(ei,w ) = δj
i, 1 ≤i ≤n.
We know that these n equations are linearly independent, so there exists a solut ionfj
0 . Of
course, once one particular solution is found, any other sol ution is of the formfj =fj
0 +ajiei
for some n2 numbers aji. Thus, we have found the general solutions fj to the equations
B(ei,f j) = δj
i .
L.5.2 83

We now show that we can choose the aij so as to satisfy the last remaining set of
conditions, B(fi,f j) = 0. If we set bij =B(fi
0,f j
0 ) = −bji, then we can compute
B(fi,f j) = B(fi
0,f j
0 ) +B(aikek,f j
0 ) +B(fi
0,ajlel) +B(aikek,ajlel)
=bij +aij −aji + 0.
Thus, it suﬃces to set aij = −bij/2. (This is where the hypothesis that the characteristic
of R is not 2 is used.)
Finally, it remains to show that the vectors e1,...,e n,f 1...,f n form a basis of V .
Since we already know that dim( V ) = 2 n, it is enough to show that these vectors are
linearly independent. However, any linear relation of the f orm
aiei +bjfj = 0,
implies bk =B(ek,aiei +bjfj) = 0 and ak = −B(fk,aiei +bjfj) = 0. □
◮ We often say that a basis of the form found in Proposition 1 is a symplectic or standard
basis of the symplectic space ( V,B ).
Symplectic Reduction of V ector Spaces. If B:V ×V → R is a skew-symmetric
bilinear form (possibly degenerate), deﬁne the null space of B to be the subspace
NB = {v ∈V |B(v,w ) = 0 for all w ∈V }.
On the quotient vector space V =V/NB, there is a well-deﬁned skew-symmetric bilinear
form B:V ×V → R given by
B(x,y) = B(x,y )
where x and y are the cosets in V of x and y in V . It is easy to see that ( V, B) is a
symplectic space.
Deﬁnition 2: If B is a skew-symmetric bilinear form on a vector space V , then the
symplectic space (
V, B) is called the symplectic reduction of (V,B ).
Here is an application of the symplectic reduction idea: Usi ng the identiﬁcation of
A2(V ) with Λ 2(V ∗) mentioned earlier, Proposition 1 allows us to write down a n ormal
form for any alternating 2-form on any ﬁnite dimensional vec tor space.
Proposition 2: For any non-zero β ∈ Λ 2(V ∗), there exist an integer n ≤ 1
2 dim(V ) and
linearly independent 1-forms ω1,ω 2,...,ω 2n ∈V ∗ for which
β =ω1 ∧ω2 +ω3 ∧ω4... +ω2n−1 ∧ω2n.
Thus,n is the largest integer so that βn ⁄= 0.
L.5.3 84

Proof: Regard β as a skew-symmetric bilinear form B on V in the usual way. Let
(V, B) be the symplectic reduction of ( V,B ). Since B ⁄= 0, we known that V ⁄= {0}. Let
dim(V ) = 2n ≥ 2 and lete1,...,e n,f 1...,f n be elements ofV so thate1,..., en,f
1
..., f
n
forms a symplectic basis of V with respect to B. Let p = dim(V ) − 2n, and let b1,...,b p
be a basis of NB.
It is easy to see that
b =
(
e1 f 1 e2 f 2 · · · en fn b1 · · · bp
)
forms a basis of V . Let
ω1 · · · ω2n+p
denote the dual basis of V ∗. Then, as the reader can easily check, the 2-form
Ω = ω1 ∧ω2 +ω3 ∧ω4... +ω2n−1 ∧ω2n
has the same values as β does on all pairs of elements of b. Of course this implies that
β = Ω. The rest of the Proposition also follows easily since, fo r example, we have
βn =n! ω1 ∧ · · · ∧ω2n ⁄= 0,
although βn+1 clearly vanishes. □
◮ If we regard β as an element of A2(V ), then n is one-half the dimension of V . Some
sources call the integer n the half-rank of β and others call n the rank. I use ‘half-rank’.
Note that, unlike the case of symmetric bilinear forms, there is no notion of signature
type or ‘positive deﬁniteness’ for skew-symmetric forms.
◮ It follows from Proposition 2 that for β in A2(V ), where V is ﬁnite dimensional, the
pair (V,β ) is a symplectic space if and only if V has dimension 2n for some n andβn ⁄= 0.
Subspaces of Symplectic V ector Spaces. Let Ω be a symplectic form on a vector
spaceV . For any subspace W ⊂V , we deﬁne the Ω-complement to W to be the subspace
W ⊥ = {v ∈V | Ω(v,w ) = 0 for all w ∈W }.
The Ω-complement of a subspace W is sometimes called its skew-complement. It is an
exercise for the reader to check that, because Ω is non-degen erate,
(
W ⊥)⊥
=W and that,
when V is ﬁnite-dimensional,
dim W + dim W ⊥ = dim V.
However, unlike the case of an orthogonal with respect to a po sitive deﬁnite inner product,
the intersection W ∩W ⊥ does not have to be the zero subspace. For example, in an
Ω-standard basis for V , the vectors e1,...,e n obviously span a subspace L that satisﬁes
L⊥ =L.
L.5.4 85

IfV is ﬁnite dimensional, it turns out (see the Exercises) that, up to symplectic linear
transformations of V , a subspace W ⊂V is characterized by the numbers d = dim W and
ν = dim (W ∩W ⊥) ≤ d. If ν = 0 we say that W is a symplectic subspace of V . This
corresponds to the case that Ω restricts to W to deﬁne a symplectic structure on W . At
the other extreme is when ν = d, for then we have W ∩W ⊥ = W . Such a subspace is
called Lagrangian.
Symplectic Manifolds.
We are now ready to return to the study of manifolds.
Deﬁnition 3: A symplectic structure on a smooth manifold M is a non-degenerate, closed
2-form Ω ∈ A 2(M ). The pair ( M, Ω) is called a symplectic manifold . If Ω is a symplectic
structure on M and Υ is a symplectic structure on N , then a smooth map φ:M → N
satisfyingφ∗(Υ) = Ω is called a symplectic map . If, in addition, φ is a diﬀeomorphism, we
say that φ is a symplectomorphism.
Before developing any of the theory, it is helpful to see a few examples.
Surfaces with Area F orms. If S is an orientable smooth surface, then there exists
a volume form µ onS. By deﬁnition, µ is a non-degenerate closed 2-form on S and hence
deﬁnes a symplectic structure on S.
Lagrangian Structures on TM . From Lecture 4, any non-degenerate Lagrangian
L:TM → R deﬁnes the 2-form dωL, which is a symplectic structure on TM .
A ‘Standard’ Structure on R2n. Think of R2n as a smooth manifold and let Ω be
the 2-form with constant coeﬃcients
Ω = 1
2
tdxJndx =dx1 ∧dxn+1 + · · · +dxn ∧dx2n.
Symplectic Submanifolds. Let (M 2m, Ω) be a symplectic manifold. Suppose that
P 2p ⊂ M 2m be any submanifold to which the form Ω pulls back to be a non-de generate
2-form Ω P . Then ( P, ΩP ) is a symplectic manifold. We say that P is a symplectic sub-
manifold of M .
It is not obvious just how to ﬁnd symplectic submanifolds of M . Even though being
a symplectic submanifold is an ‘open’ condition on submanif olds of M , is is not ‘dense’.
One cannot hope to perturb an arbitrary even dimensional sub manifold of M slightly so
as to make it symplectic. There are even restrictions on the t opology of the submanifolds
of M on which a symplectic form restricts to be non-degenerate.
For example, no symplectic submanifold of R2n (with any symplectic structure on
R2n) could be compact for the following simple reason: Since R2n is contractible, its
second deRham cohomology group vanishes. In particular, fo r any symplectic form Ω
on R2n, there must be a 1-form ω so that Ω = dω, which implies that Ω m =d
(
ω∧Ωm−1)
.
Thus, for all m > 0, the 2 m-form Ω m is exact on R2n (and every submanifold of R2n).
L.5.5 86

By Proposition 2, if M 2m were a submanifold of R2n on which Ω restricted to be non-
degenerate, then Ω m would be a volume form on M . However, on a compact manifold the
volume form is never exact (just apply Stokes’ Theorem).
Example. Complex Submanifolds. Nevertheless, there are many symplectic subman-
ifolds of R2n. One way to construct them is to regard R2n as Cn in such a way that
the linear map J: R2n → R2n represented by Jn becomes complex multiplication. (For
example, just deﬁne the complex coordinates by zk =xk +ixk+n.) Then, for any non-zero
vectorv ∈ R2n, we have Ω( v,Jv ) = −|v|2 ⁄= 0. In particular, Ω is non-degenerate on every
complex subspace S ⊂ Cn. Thus, if M 2m ⊂ Cn is any complex submanifold (i.e., all of
its tangent spaces are m-dimensional complex subspaces of Cm), then Ω restricts to be
non-degenerate on M .
The Cotangent Bundle. Let M be any smooth manifold and let T ∗M be its
cotangent bundle. As we saw in Lecture 4, there is a canonical 2-form on T ∗M that can
be deﬁned as follows: Let π:T ∗M → M be the basepoint projection. Then, for every
v ∈Tα(T ∗M ), deﬁne
ω(v) = α
(
π′(v)
)
.
I claim that ω is a smooth 1-form on T ∗M and that Ω = dω is a symplectic form on T ∗M .
To see this, let us compute ω in local coordinates. Let x:U → Rn be a local coordinate
chart. Since the 1-forms dx1,...,dx n are linearly independent at every point of U , it follows
that there are unique functions ξi on T ∗U so that, for α ∈T ∗
aU ,
α =ξ1(α)dx1|a + · · · +ξn(α)dxn|a.
The functionsx1,...,x n,ξ 1,...,ξ n then form a smooth coordinate system on T ∗U in which
the projection mapping π is given by
π(x,p ) = x.
It is then straightforward to compute that, in this coordina te system,
ω =ξidxi.
Hence, Ω = dξi∧dxi and so is non-degenerate.
Symplectic Products. If (M, Ω) and ( N, Υ) are symplectic manifolds, then M ×N
carries a natural symplectic structure, called the product symplectic structure Ω ⊕ Υ,
deﬁned by
Ω ⊕ Υ = π∗
1(Ω) + π∗
2(Υ).
Thus, for example, n-fold products of compact surfaces endowed with area forms g ive
examples of compact symplectic 2 n-manifolds.
L.5.6 87

Coadjoint Orbits. Let Ad ∗:G → GL(g∗) denote the coadjoint representation of G.
This is the so-called ‘contragredient’ representation to t he adjoint representation. Thus,
for any a ∈G and ξ ∈ g∗, the element Ad ∗(a)(ξ) ∈ g∗ is determined by the rule
Ad∗(a)(ξ)(x) = ξ
(
Ad(a−1)(x)
)
for all x ∈ g.
◮ One must be careful not to confuse Ad∗(a) with
(
Ad(a)
)∗
. Instead, as our deﬁnition
shows,Ad∗(a) =
(
Ad(a−1)
)∗
.
Note that the induced homomorphism of Lie algebras, ad ∗: g → gl(g∗) is given by
ad∗(x)(ξ)(y) = −ξ
(
[x,y ]
)
The orbits G ·ξ in g∗ are called the coadjoint orbits . Each of them carries a natural
symplectic structure. To see how this is deﬁned, let ξ ∈ g∗ be ﬁxed, and let φ:G →G ·ξ
be the usual submersion induced by the Ad ∗-action, φ(a) = Ad ∗(a)(ξ) = a ·ξ. Now let ωξ
be the left-invariant 1-form on G whose value at e is ξ. Thus, ωξ = ξ(ω) where ω is the
canonical g-valued 1-form on G.
Proposition 3: There is a unique symplectic form Ωξ on the orbit G·ξ =G/Gξ satisfying
φ∗(Ωξ) = dωξ.
Proof: If Proposition 3 is to be true, then Ω ξ must satisfy the rule
Ωξ
(
φ′(v),φ ′(w)
)
=dωξ(v,w ) for all v,w ∈TaG.
What we must do is show that this rule actually does deﬁne a sym plectic 2-form on G ·ξ.
First, note that, for x,y ∈ g =TeG, we may compute via the structure equations that
dωξ(x,y ) = ξ
(
dω(x,y )
)
=ξ
(
−[x,y ]
)
=ad∗(x)(ξ)(y).
In particular, ad∗(x)(ξ) = 0, if and only if x lies in the null space of the 2-form dωξ(e). In
other words, the null space of dωξ(e) is gξ, the Lie algebra of Gξ. Since dωξ is left-invariant,
it follows that the null space of dωξ(a) is L′
a(gξ) ⊂ TaG. Of course, this is precisely the
tangent space at a to the left coset aGξ. Thus, for each a ∈G,
Ndωξ (a) = kerφ′(a),
It follows that, Ta·ξ(G ·ξ) = φ′(a)(TaG) is naturally isomorphic to the symplectic quotient
space (TaG)/
(
L′
a(gξ)
)
for each a ∈G. Thus, there is a unique, non-degenerate 2-form Ω a
on Ta·ξ(G ·ξ) so that
(
φ′(a)
)∗
(Ωa) = dωξ(a).
It remains to show that Ω a = Ω b if a ·ξ =b ·ξ. However, this latter case occurs only
if a =bh where h ∈Gξ. Now, for any h ∈Gξ, we have
R∗
h(ωξ) = ξ
(
R∗
h(ω)
)
=ξ
(
Ad(h−1)(ω)
)
= Ad ∗(h)(ξ)(ω) = ξ(ω) = ωξ.
L.5.7 88

Thus,R∗
h(dωξ) = dωξ. Since the following square commutes, it follows that Ω a = Ω b.
TaG
R′
h
− → TbG
φ′(a)


↓


↓φ′(b)
Ta·ξ(G ·ξ)
id
− → Tb·ξ(G ·ξ)
All this shows that there is a well-deﬁned, non-degenerate 2 -form Ω ξ onG ·ξ that satisﬁes
φ∗(Ωξ) = dωξ. Since φ is a smooth submersion, the equation
φ∗(dΩξ) = d(dωξ) = 0
implies that dΩξ = 0, as promised. □
◮ Note that a consequence of Proposition 3 is that all of the coa djoint orbits are actually
even dimensional. As we shall see when we take up the subject o f reduction, the coadjoint
orbits are particularly interesting symplectic manifolds .
Examples: Let G = O(n), with Lie algebra so(n), the space of skew-symmetric n-by-n
matrices. Now there is an O( n)-equivariant positive deﬁnite pairing of so(n) with itself ⟨, ⟩
given by
⟨x,y ⟩ = −tr(xy).
Thus, we can identify so(n)∗ with so(n) by this pairing. The reader can check that, in this
case, the coadjoint action is isomorphic to the adjoint acti on
Ad(a)(x) = axa−1.
If ξ is the rank 2 matrix
ξ =


0 −1
1 0 0
0 0

,
then it is easy to check that the stabilizer Gξ is just the set of matrices of the form
(
a 0
0 A
)
where a ∈ SO(2) and A ∈ O(n − 2). The quotient O( n)/
(
SO(2) × O(n − 2)
)
thus has a
symplectic structure. It is not diﬃcult to see that this homo geneous space can be identiﬁed
with the space of oriented 2-planes in En.
As another example, if n = 2m, then Jm lies in so(2m), and its stabilizer is U( m) ⊂
SO(2m). It follows that the quotient space SO(2 m)/U(m), which is identiﬁable as the set
of orthogonal complex structures on E2m, is a symplectic space.
Finally, if G = U(n), then, again, we can identify u(n)∗ with u(n) via the U( n)-
invariant, positive deﬁnite pairing
⟨x,y ⟩ = −Re
(
tr(xy)
)
.
L.5.8 89

Again, under this identiﬁcation, the coadjoint action agre es with the adjoint action. For
0<p<n , the stabilizer of the element
ξp =
(
iIp 0
0 −iIn−p
)
is easily seen to be U( p) × U(n −p). The orbit of ξp is identiﬁable with the space Gr p(Cn),
i.e., the Grassmannian of (complex) p-planes in Cn, and, by Proposition 3, carries a canon-
ical, U(n)-invariant symplectic structure.
Darboux’ Theorem. There is a manifold analogue of Proposition 1 that says that
symplectic manifolds of a given dimension are all locally ‘i somorphic’. This fundamental
result is known as Darboux’ Theorem. I will give the classical proof (due to Darboux) here,
deferring the more modern proof (due to Weinstein) to the nex t section.
Theorem 1: (Darboux’ Theorem) If Ω is a closed 2-form on a manifold M 2n that satisﬁes
the condition that Ωn be nowhere vanishing, then for every p ∈M , there is a neighborhood
U of p and a coordinate system x1,x 2,...,x n,y 1,y 2,...,y n on U so that
Ω |U =dx1 ∧dy1 +dx2 ∧dy2 + · · · +dxn ∧dyn.
Proof: We will proceed by induction on n. Assume that we know the theorem for
n−1 ≥ 0. We will prove it for n. Fix p, and let y1 be a smooth function on M for which
dy1 does not vanish at p. Now let X be the unique (smooth) vector ﬁeld that satisﬁes
X Ω = dy1.
This vector ﬁeld does not vanish at p, so there is a function x1 on a neighborhood U of p
that satisﬁes X(x1) = 1. Now let Y be the vector ﬁeld on U that satisﬁes
Y Ω = −dx1.
Since dΩ = 0, the Cartan formula, now gives
LX Ω = LY Ω = 0 .
We now compute
[X,Y ] Ω = LXY Ω = LX (Y Ω) −Y (LX Ω)
= LX (−dx1) = −d
(
X(x1)
)
= −d(1) = 0.
Since Ω has maximal rank, this implies [ X,Y ] = 0. By the simultaneous ﬂow-box theorem,
it follows that there exist local coordinates x1,y 1,z 1,z 2,...,z 2n−2 on some neighborhood
U1 ⊂U of p so that
X = ∂
∂x1
and Y = ∂
∂y 1.
L.5.9 90

Now consider the form Ω ′ = Ω −dx1∧dy1. Clearly dΩ ′ = 0. Moreover,
X Ω ′ = LX Ω ′ =Y Ω ′ = LY Ω ′ = 0.
It follows that Ω ′ can be expressed as a 2-form in the variables z1,z 2,...,z 2n−2 alone.
Hence, in particular, (Ω ′)n ≡ 0. On the other hand, by the binomial theorem, then
0 ⁄= Ω n =ndx 1 ∧dy1 ∧ (Ω ′)n−1.
It follows that Ω ′ may be regarded as a closed 2-form of maximal half-rank n−1 on an
open set in R2n−2. Now apply the inductive hypothesis to Ω ′. □
Darboux’ Theorem has a generalization that covers the case o f closed 2-forms of con-
stant (though not necessarily maximal) rank. It is the analo gue for manifolds of the
symplectic reduction of a vector space.
Theorem 2: (Darboux’ Reduction Theorem) Suppose that Ω is a closed 2-form of constant
half-rank n on a manifold M 2n+k. Then the ‘null bundle’
NΩ =
{
v ∈TM | Ω(v,w ) = 0 for all w ∈Tπ(v)M
}
is integrable and of constant rank k. Moreover, any point of M has a neighborhood U on
which there exist local coordinates x1,...,x n,y 1,...,y n,z 1,...z k in which
Ω |U =dx1 ∧dy1 +dx2 ∧dy2 + · · · +dxn ∧dyn.
Proof: Note that a vector ﬁeld X on M is a section of NΩ if and only if X
Ω = 0. In
particular, since Ω is closed, the Cartan formula implies th at LX Ω = 0 for all such X.
If X and Y are two sections of NΩ , then
[X,Y ] Ω = LX (Y Ω) −Y (LX Ω) = 0 − 0 = 0,
so it follows that [ X,Y ] is a section of NΩ as well. Thus, NΩ is integrable.
Now apply the Frobenius Theorem. For any point p ∈M , there exists a neighborhood
U on which there exist local coordinates z1...,z 2n+k so that NΩ restricted to U is spanned
by the vector ﬁelds Zi = ∂/∂zi for 1 ≤ i ≤ k. Since Zi Ω = LZi Ω = 0 for 1 ≤ i ≤ k,
it follows that Ω can be expressed on U in terms of the variables zk+1,...,z 2n+k alone.
In particular, Ω restricted to U may be regarded as a non-degenerate closed 2-form on an
open set in R2n. The stated result now follows from Darboux’ Theorem. □
L.5.10 91

Symplectic and Hamiltonian vector ﬁelds.
We now want to examine some of the special vector ﬁelds that ar e deﬁned on sym-
plectic manifolds. Let M 2n be manifold and let Ω be a symplectic form on M . Let
Sp(Ω) ⊂ Diff(M ) denote the subgroup of symplectomorphisms of ( M, Ω). We would like
to follow Lie in regarding Sp(Ω) as an ‘inﬁnite dimensional Lie group’. In that case, the L ie
algebra of Sp(Ω) should be the space of vector ﬁelds whose ﬂows preserve Ω. Of course, Ω
will be invariant under the ﬂow of a vector ﬁeld X if and only if LXΩ = 0. This motivates
the following deﬁnition:
Deﬁnition 4: A vector ﬁeld X on M is said to be symplectic if LX Ω = 0. The space of
symplectic vector ﬁelds on M will be denoted sp(Ω).
It turns out that there is a very simple characterization of t he symplectic vector ﬁelds
on M : Since dΩ = 0, it follows that for any vector ﬁeld X on M ,
LX Ω = d(X
Ω).
◮ Thus,X is a symplectic vector ﬁeld if and only if X Ω is closed.
Now, since Ω is non-degenerate, for any vector ﬁeld X onM , the 1-form ♭(X) = −X Ω
vanishes only where X does. Since TM and T ∗M have the same rank, it follows that the
mapping ♭: X(M ) → A 1(M ) is an isomorphism of C∞(M )-modules. In particular, ♭ has
an inverse, ♯: A1(M ) → X(M ).
With this notation, we can write sp(Ω) = ♯
(
Z 1(M )
)
where Z 1(M ) denotes the vector
space of closed 1-forms on M . Now, Z 1(M ) contains, as a subspace, B1(M ) = d
(
C∞(M )
)
,
the space of exact 1-forms on M . This subspace is of particular interest; we encountered
it already in Lecture 4.
Deﬁnition 5: For eachf ∈C∞(M ), the vector ﬁeld Xf =♯(df) is called the Hamiltonian
vector ﬁeld associated to f . The set of all Hamiltonian vector ﬁelds on M is denoted h(Ω).
Thus, by deﬁnition, h(Ω) = ♯
(
B1(M )
)
. For this reason, Hamiltonian vector ﬁelds are
often called exact. Note that a Hamiltonian vector ﬁeld is one whose equations, written in
symplectic coordinates, represent an ODE in Hamiltonian fo rm.
The following formula shows that, not only is sp(Ω) a Lie algebra of vector ﬁelds, but
that h(Ω) is an ideal in sp(Ω), i.e., that [ sp(Ω), sp(Ω)] ⊂ h(Ω).
Proposition 4: ForX,Y ∈ sp(Ω) , we have
[X,Y ] = XΩ(X,Y ).
In particular, [Xf,Xg] = X{f,g } where, by deﬁnition, {f,g } = Ω(Xf,Xg).
Proof: We use the fact that, for any vector ﬁeld X, the operator LX is a derivation with
respect to any natural pairing between tensors on M :
[X,Y ]
Ω =
(
LXY
)
Ω = LX
(
Y Ω
)
−Y
(
LX Ω
)
=d
(
X
(
Y Ω
))
+X d (Y Ω) + 0 = d
(
Ω(Y,X )
)
+ 0
= −d
(
Ω(X,Y )
)
=
(
XΩ(X,Y )
)
Ω.
This proves our ﬁrst equation. The remaining equation follo ws immediately. □
L.5.11 92

The deﬁnition {f,g } = Ω(Xf,Xg) is an important one. The bracket ( f,g ) ↦→ {f,g } is
called the Poisson bracket of the functions f andg. Proposition 4 implies that the Poisson
bracket gives the functions on M the structure of a Lie algebra. The Poisson bracket is
slightly more subtle than the pairing ( Xf,Xg) ↦→X{f,g } since the mapping f ↦→Xf has a
non-trivial kernel, namely, the locally constant function s.
Thus, if M is connected, then we get an exact sequence of Lie algebras
0 − →R − →C∞(M ) − →h(Ω) − →0
that is not, in general, split (see the Exercises). Since {1,f } = 0 for all functions f on
M , it follows that the Poisson bracket on C∞(M ) makes it into a central extension of
the algebra of Hamiltonian vector ﬁelds. The geometry of thi s central extension plays an
important role in quantization theories on symplectic mani folds (see [GS 2] or [We]).
Also of great interest is the exact sequence
0 − →h(Ω) − →sp(Ω) − →H 1
dR(M, R) − →0,
where the right hand arrow is just the map described by X ↦→[X Ω]. Since the bracket of
two elements in sp(Ω) lies in h(Ω), it follows that this linear map is actually a Lie algebra
homomorphism when H 1
dR(M, R) is given the abelian Lie algebra structure. This sequence
also may or may not split (see the Exercises), and the propert ies of this extension have a
great deal to do with the study of groups of symplectomorphis ms of M . See the Exercises
for further developments.
Involution
I now want to make some remarks about the meaning of the Poisso n bracket and its
applications.
Deﬁnition 5: Let (M, Ω) be a symplectic manifold. Two functions f and g are said to
be in involution (with respect to Ω) if they satisfy the condition {f,g } = 0.
◮ Note that, since {f,g } =dg(Xf ) = −df(Xg), it follows that two functions f andg are
in involution if and only if each is constant on the integral c urves of the other’s Hamiltonian
vector ﬁeld.
Now, if one is trying to describe the integral curves of a Hami ltonian vector ﬁeld, Xf ,
the more independent functions on M that one can ﬁnd that are constant on the integral
curves of Xf , the more accurately one can describe those integral curves . If one were able
ﬁnd, in addition to f itself, 2n−2 additional independent functions on M that are constant
on the integral curves of Xf , then one could describe the integral curves of Xf implicitly
by setting those functions equal to a constant.
It turns out, however, that this is too much to hope for in gene ral. It can happen that
a Hamiltonian vector ﬁeld Xf has no functions in involution with it except for functions
of the form F (f ).
L.5.12 93

Nevertheless, in many cases that arise in practice, we can ﬁn d several functions in
involution with a given function f = f1 and, moreover, in involution with each other.
In case one can ﬁnd n−1 such independent functions, f2,...,f n, we have the following
theorem of Liouville, which says that the remaining n−1 required functions can be found
(at least locally) by quadrature alone. In the classical lan guage, a vector ﬁeld Xf for which
such functions are known is said to be ‘completely integrabl e by quadratures’, or, more
simply as ‘completely integrable’.
Theorem 3: Let f 1,f 2,...,f n be n functions in involution on a symplectic manifold
(M 2n, Ω) . Suppose that the functions fi are independent in the sense that the diﬀerentials
df1,...,df n are linearly independent at every point of M . Then each point of M has an
open neighborhood U on which there are functions a1,...,a n on U so that
Ω = df1 ∧da1 + · · · +dfn ∧dan.
Moreover, the functions ai can be found by ‘ﬁnite’ operations and quadrature.
Proof: By hypothesis, the forms df1,...,df n are linearly independent at every point of
M , so it follows that the Hamiltonian vector ﬁelds Xf 1,...,X f n are also linearly inde-
pendent at every point of M . Also by hypothesis, the functions fi are in involution, so it
follows that dfi(Xf j ) = 0 for all i and j.
The vector ﬁelds Xf i are linearly independent on M , so by ‘ﬁnite’ operations, we can
construct 1-forms ¯β1,..., ¯βn that satisfy the conditions
¯βi(Xf j ) = δij (Kronecker delta).
Any other set of forms βi that satisfy these conditions are given by expressions:
βi = ¯βi +gijdfj
for some functions gij on M . Let us regard the functions gij as unknowns for a moment.
Let Y1,...,Y n be the vector ﬁelds that satisfy
Yi
Ω = βi,
with ¯Yi denoting the corresponding quantities when the gij are set to zero. Then it is easy
to see that
Yi = ¯Yi −gijXf j.
Now, by construction,
Ω(Xf i,Xf j ) = 0 and Ω( Yi,Xf j ) = δij.
Moreover, as is easy to compute,
Ω(Yi,Yj) = Ω( ¯Yi, ¯Yj) −gji +gij.
L.5.13 94

Thus, choosing the functions gij appropriately, saygij = − 1
2 Ω( ¯Yi, ¯Yj), we may assume that
Ω(Yi,Yj) = 0. It follows that the sequence of 1-forms df1,...,df n,β 1,...,β n is the dual
basis to the sequence of vector ﬁelds Y1,...,Y n,Xf 1,...,X f n. In particular, we see that
Ω = df1 ∧β1 + · · · +dfn ∧βn,
since the 2-forms on either side of this equation have the sam e values on all pairs of vector
ﬁelds drawn from this basis.
Now, since Ω is closed, we have
dΩ = df1 ∧dβ1 + · · · +dfn ∧dβn = 0.
If, for example, we wedge both sides of this equation with df2,...,df n, we see that
df1 ∧df2 ∧ ... ∧dfn ∧dβ1 = 0.
Hence, it follows that dβ1 lies in the ideal generated by the forms df1,...,df n. Of course,
there was nothing special about the ﬁrst term, so we clearly h ave
dβi ≡ 0 mod df1,...,df n for all 1 ≤i ≤n.
In particular, it follows that, if we pull back the 1-forms βi to any n-dimensional level set
Mc ⊂ M deﬁned by equations fi = ci where the ci are constants, then each βi becomes
closed.
Let m ∈M be ﬁxed and choose functions g1,...,g n on a neighborhood U of m inM
so that gi(m) = 0 and so that the functions g1,...,g n,f 1,...,f n form a coordinate chart
onU . By shrinking U if necessary, we may assume that the image of this coordinate chart
in Rn × Rn is an open set of the form B1 ×B2, where B1 and B2 are open balls in Rn
(with B1 centered on 0). In this coordinate chart, the βi can be expressed in the form
βi =Bj
i (g,f )dgj +Cij(g,f )dfj.
Deﬁne new functions ai on B1 ×B2 by the rule
hi(g,f ) =
∫ 1
0
Bj
i (tg,f )gjdt.
(This is just the Poincar´ e homotopy formula with the f ’s held ﬁxed. It is also the ﬁrst
place where we use ‘quadrature’.) Since setting the f ’s equals to constants makes βi a
closed 1-form, it follows easily that
βi =dhi +Aij(g,f )dfj
for some functions Aij on B1 ×B2. Thus, on U , the form Ω has the expression
Ω = dfi ∧dhi +Aijdfi ∧dfj.
L.5.14 95

It follows that the 2-form A =Aijdfi∧dfj is closed on (the contractible open set) B1 ×B2.
Thus, the functions Aij do not depend on the g-coordinates at all. Hence, by employing
quadrature once more (i.e., the second time) in the Poincar´ e homotopy formula, we can
write A = −d(sidfi) for some functions si of the f ’s alone. Setting ai =hi +si, we have
the desired local normal form Ω = dfi∧dai. □
In many useful situations, one does not need to restrict to a l ocal neighborhood U
to deﬁne the functions ai (at least up to additive constants) and the 1-forms dai can be
deﬁned globally on M (or, at least away from some small subset in M where degeneracies
occur). In this case, the construction above is often called the construction of ‘action-angle’
coordinates. We will discuss this further in Lecture 6.
L.5.15 96

Exercise Set 5:
Symplectic Manifolds, I
1. Show that the bilinear form on Rn deﬁned in the text by the rule B(x,y ) = txAy (where
A is a skew-symmetric n-by-n matrix) is non-degenerate if and only if A is invertible. Show
directly (i.e., without using Proposition 1) that a skew-sy mmetric,n-by-n matrixA cannot
be invertible if n is odd. (Hint: For the last part, compute det( A) two ways.)
2. Let ( V,B ) be a symplectic space and let b = (b1,b 2,...,b m) be a basis of B. Deﬁne
the m-by-m skew-symmetric matrix Ab whose ij-entry is B(bi,bj). Show that if b′ = bR
is any other basis of V (where R ∈ GL(m, R) ), then
Ab′ = tRA bR.
Use Proposition 1 and Exercise 1 to conclude that, if A is an invertible, skew-symmetric
2n-by-2n matrix, then there exists a matrix R ∈ GL(2n, R) so that
A = tR
(
0n In
−In 0n
)
R.
In other words, the GL(2 n, R)-orbit of the matrix Jn deﬁned in the text (under the “stan-
dard” (right) action of GL(2 n, R) on the skew-symmetric 2 n-by-2n matrices) is the open
set of all invertible skew-symmetric 2 n-by-2n matrices.
3. Show that Sp( n, R), as deﬁned in the text, is indeed a Lie subgroup of GL(2 n, R) and
has dimension 2n2 +n. Compute its Lie algebra sp(n, R). Show that Sp(1 , R) = SL(2, R).
4. In Lecture 2, we deﬁned the groups GL( n, C) = {R ∈ GL(2n, R) | JnR =RJn} and
O(2n) = {R ∈ GL(2n, R) | tRR =I2n}. Show that
GL(n, C) ∩ Sp(n, R) = O(2n) ∩ Sp(n, R) = GL(n, C) ∩ O(2n) = U(n).
5. Let Ω be a symplectic form on a vector space V of dimension 2 n. Let W ⊂ V be a
subspace that satisﬁes dim W = d and dim (W ∩W ⊥) = ν. Show that there exists an
Ω-standard basis of V so that W is spanned by the vectors
e1, ..., eν+m, f1, ..., fm
where d −ν = 2m. In this basis of V , what is a basis for W ⊥?
E.5.1 97

6. The Pfaffian. LetV be a vector space of dimension 2 n. Fix a basis b = (b1,...,b 2n).
For any skew-symmetric 2n-by-2n matrix F = (fij), deﬁne the 2-vector
ΦF = 1
2fijbi ∧bj = 1
2 b ∧F ∧tb.
Then there is a unique polynomial function Pf, homogeneous o f degree n, on the space of
skew-symmetric 2n-by-2n matrices for which
(ΦF )n =n! Pf(F )b1 ∧ ... ∧b2n.
Show that
Pf(F ) = f 12 when n = 1,
Pf(F ) = f 12f 34 +f 13f 42 +f 14f 23 when n = 2.
Show also that
Pf(AF tA) = det(A) Pf(F )
for all A ∈ GL(2n, R). (Hint: Examine the eﬀect of a change of basis b = b′A. Com-
pare Problem 2.) Use this to conclude that Sp( n, R) is a subgroup of SL(2 n, R). Finally,
show that (Pf( F ))2 = det(F ). (Hint: Show that the left and right hand sides are polyno-
mial functions that agree on a certain open set in the space of skew-symmetric 2n-by-2n
matrices.)
The polynomial function Pf is called the Pfaﬃan . It plays an important role in
diﬀerential geometry.
7. Verify that, for any B ∈ A2(V ), the symplectic reduction (
V, B) is a well-deﬁned
symplectic space.
8. Show that if there is a G-invariant non-degnerate pairing ( , ): g × g → R, then g and
g∗ are isomorphic as G-representations.
9. Compute the adjoint and coadjoint representations for
G =
{(
a b
0 1
)
a ∈ R+,b ∈ R
}
Show that g and g∗ are not isomorphic as G-spaces! (For a general G, the Ad-orbits of G
in g are not even of even dimension in general, so they can’t be sym plectic manifolds.)
10. For any Lie group G and any ξ ∈ g∗, show that the symplectic structures Ω ξ and Ω a·ξ
on G ·ξ are the same for any a ∈G.
E.5.2 98

11. This exercise concerns the splitting properties of the two Lie algebras sequences
associated to any symplectic structure Ω on a connected mani fold M :
0 − →R − →C∞(M ) − →h(Ω) − →0
and
0 − →h(Ω) − →sp(Ω) − →H 1
dR(M, R) − →0.
Deﬁne the “divided powers” of Ω by the rule Ω [k] = (1/k!) Ωk, for each 0 ≤k ≤n.
(i) Show that, for any vector ﬁelds X and Y on M ,
Ω(X,Y ) Ω [n] = −(X Ω) ∧ (Y Ω) ∧ Ω [n−1].
Conclude that the ﬁrst of the above two sequences splits if M is compact. (Hint: For
the latter statement, show that the set of functions f on M for which
∫
Mf Ω [n] = 0
forms a Poisson subalgebra of C∞(M ).)
(ii) On the other hand, show that for R2 with the symplectic structure Ω = dx∧dy, the
ﬁrst sequence does not split. (Hint: Show that every smooth function on R2 is of the
form {x,g } for some g ∈C∞(R2). Why does this help?)
(iii) Suppose that M is compact. Deﬁne a skew-symmetric pairing
βΩ :H 1
dR(M, R) ×H 1
dR(M, R) → R
by the formula
βΩ (a,b ) =
∫
M
˜a ∧ ˜b ∧ Ω [n−1],
where ˜a and ˜b are closed 1-forms representing the cohomology classes a and b respec-
tively. Show that if there is a Lie algebra splitting σ:H 1
dR(M, R) → sp(Ω) then
Ω
(
σ(a),σ (b)
)
= − βΩ (a,b )
vol(M, Ω [n])
for all a,b ∈H 1
dR(M, R). (Remember that the Lie algebra structure on H 1
dR(M, R) is
the abelian one.) Use this to conclude that the second sequen ce does split for a sym-
plectic structure on the standard 1-holed torus, but does not split for any symplectic
structure on the 2-holed torus. (Hint: To show the non-split ting result, use the fact
that any tangent vector ﬁeld on the 2-holed torus must have a z ero.)
E.5.3 99

12. The Flux Homomorphism. The object of this exercise is to try to identify the
subgroup of Sp(Ω) whose Lie algebra is h(Ω). Thus, let ( M, Ω) be a symplectic manifold.
First, I remind you how the construction of the (smooth) univ ersal cover of the identity
component of Sp(Ω) goes. Let p: [0, 1] ×M →M be a smooth map with the property that
the map pt:M →M deﬁned by pt(m) = p(t,m ) is a symplectomorphism for all 0 ≤t ≤ 1.
Such a p is called a (smooth) path in Sp(M ). We say that p is based at the identity map
e:M →M ifp0 = e. The set of smooth paths in Sp(M ) that are based at e will be denoted
by Pe
(
Sp(Ω)
)
.
Two paths p andp′ in Pe
(
Sp(Ω)
)
satisfyingp1 =p′
1 are said to be homotopic if there
is a smooth map P : [0, 1] × [0, 1] ×M →M that satisﬁes the following conditions: First,
P (s, 0,m ) = m for all s and m. Second, P (s, 1,m ) = p1(m) = p′
1(m) for all s and m.
Third, P (0,t,m ) = p(t,m ) and P (1,t,m ) = p′(t,m ) for all t and m. The set of homotopy
classes of elements of Pe
(
Sp(Ω)
)
is then denoted by ~Sp0(Ω). In any reasonable topology
on Sp(Ω), this should to be the universal covering space of the ide ntity component of
Sp(Ω). There is a natural group structure on ~Sp0(Ω) in which ˜e, the homotopy class of
the constant path at e, is the identity element (cf., the covering spaces exercise in Exercise
Set 2).
We are now going to construct a homomorphism Φ: ~Sp0(Ω) → H 1(M, R), called the
ﬂux homomorphism . Let p ∈ Pe
(
Sp(Ω)
)
be chosen, and let γ:S1 →M be a closed curve
representing an element of H1(M, Z). Then we can deﬁne
F (p,γ ) =
∫
[0,1]×S1
(p ·γ)∗(Ω)
where (p ·γ): [0, 1] ×S1 →M is deﬁned by ( p ·γ)(t,θ ) = p
(
t,γ (θ)
)
. The number F (p,γ )
is called the ﬂux of p through γ.
(i) Show that F (p,γ ) = F (p′,γ ′) if p is homotopic to p′ and γ is homologous to γ′).
(Hint: Use Stokes’ Theorem several times.)
Thus,F is actually well deﬁned as a map F :~Sp0(Ω) ×H1(M, R) → R.
(ii) Show that F :~Sp0(Ω) ×H1(M, R) → R is linear in its second variable and that, under
the obvious multiplication, we have
F (pp ′,γ ) = F (p,γ ) +F (p′,γ ).
(Hint: Use Stokes’ Theorem again.)
Thus,F may be transposed to become a homomorphism
Φ: ~Sp0(Ω) →H 1(M, R).
Show (by direct computation) that ifζ is a closed 1-form on M for which the symplectic
vector ﬁeld Z =♯ζ is complete on M , then the path p in Sp(M ) deﬁned by the ﬂow
of Z from t = 0 to t = 1 satisﬁes Φ( p) = [ ζ] ∈ H 1(M, R). Conclude that the ﬂux
homomorphism Φ is always surjective and that its derivative Φ ′(˜e): sp(Ω) →H 1(M, R)
is just the operation of taking cohomology classes. (Recall that we identify sp(Ω) with
Z 1(M ).)
E.5.4 100

(iii) Show that if M is a compact surface of genus g > 1, then the ﬂux homomorphism
is actually well deﬁned as a map from Sp(Ω) to H 1(M, R). Would the same result
be true if M were of genus 1? How could you modify the map so as to make it wel l-
deﬁned on Sp(Ω) in the case of the torus? (Hint: Show that if you have two pa ths
p and p′ with the same endpoint, then you can express the diﬀerence of their ﬂuxes
across a circle γ as an integral of the form
∫
S1×S1
Ψ ∗(Ω)
where Ψ: S1 ×S1 → M is a certain piecewise smooth map from the torus into M .
Now use the fact that, for any piecewise smooth map Ψ: S1 ×S1 →M , the induced
map Ψ ∗:H 2(M, R) →H 2(S1 ×S1, R) on cohomology is zero. (Why does this follow
from the assumption that the genus of M is greater than 1?) )
In any case, the subgroup ker Φ (or its image under the natural projection from ~Sp0(Ω)
to Sp(Ω)) is known as the group H(Ω) of exact or Hamiltonian symplectomorphisms. Note
that, at least formally, its Lie algebra is h(Ω).
13. In the case of the geodesic ﬂow on a surface of revolution (se e Lecture 4), show that
the energy f 1 =EL and the conserved quantity f 2 =F (r) ˙r +G(r) ˙θ are in involution. Use
the algorithm described in Theorem 3 to compute the function s a1 and a2, thus verifying
that the geodesic equations on a surface of revolution are in tegrable by quadrature.
E.5.5 101

Lecture 6:
Symplectic Manifolds, II
The Space of Symplectic Structures on M .
I want to turn now to the problem of describing the symplectic structures a manifoldM
can have. This is a surprisingly delicate problem and is curr ently a subject of research.
Of course, one fundamental question is whether a given manif old has any symplec-
tic structures at all. I want to begin this lecture with a disc ussion of the two known
obstructions for a manifold to have a symplectic structure.
The cohomology ring condition. If Ω ∈ A 2(M 2n) is a symplectic structure on a
compact manifold M , then the cohomology class [Ω] ∈ H 2
dR(M, R) is non-zero. In fact,
[Ω]n = [Ω n], but the class [Ω n] cannot vanish in H 2n
dR(M ) because the integral of Ω n over
M is clearly non-zero. Thus, we have
Proposition 1: If M 2n is compact and has a symplectic structure, there must exist a n
elementu ∈H 2(M, R) so that un ⁄= 0 ∈H 2n
dR(M ).
Example. This immediately rules out the existence of a symplectic str ucture on S2n for
alln> 1. One consequence of this, as you are asked to show in the Exer cises, is that there
cannot be any simple notion of connected sum in the category o f symplectic manifolds
(except in dimension 2).
The bundle obstruction. If M admits a symplectic structure Ω, then, in partic-
ular, this deﬁnes a symplectic structure on each of the tange nt spaces TmM that varies
continuously with m. In other words, TM must carry the structure of a symplectic vector
bundle. There are topological obstructions to the existenc e of such a structure on the tan-
gent bundle of a general manifold. As a simple example, if M has a symplectic structure,
then TM must be orientable.
There are more subtle obstructions than orientation. Unfor tunately, a description of
these obstructions requires some acquaintance with the the ory of characteristic classes.
However, part of the following discussion will be useful eve n to those who aren’t familiar
with characteristic class theory, so I will give it now, even though the concepts will only
reveal their importance in later Lectures.
Deﬁnition 1: An almost symplectic structure on a manifold M 2n is a smooth 2-form
Ω deﬁned on M that is non-degenerate but not necessarily closed. An almost complex
structure onM 2n is a smooth bundle map J:TM →TM that satisﬁes J 2v = −v for all v
in TM .
The reason that I have introduced both of these concepts at th e same time is that
they are intimately related. The really deep aspects of this relationship will only become
apparent in the Lecture 9, but we can, at least, give the follo wing result now.
L.6.1 102

Proposition 2: A manifold M 2n has an almost symplectic structure if and only if it has
an almost complex structure.
Proof: First, suppose that M has an almost complex structure J. Let g0 be any Rie-
mannian metric on M . (Thus, g0:TM → R is a smooth function that restricts to each
TmM to be a positive deﬁnite quadratic form.) Now deﬁne a new Riem annian metric by
the formula
g(v) = g0(v) +g0(Jv ).
Then g has the property that g(Jv ) = g(v) for all v ∈TM since
g(Jv ) = g0(Jv ) +g0(J 2v) = g0(Jv ) +g0(−v) = g(v).
Now let ⟨, ⟩ denote the (symmetric) inner product associated with g. Thus, ⟨v,v ⟩ =
g(v), so we have ⟨Jx,Jy ⟩ = ⟨x,y ⟩ when x and y are tangent vector with the same base
point. For x,y ∈TmM deﬁne Ω( x,y ) = ⟨Jx,y ⟩. I claim that Ω is a non-degenerate 2-form
on M . To see this, ﬁrst note that
Ω(x,y ) = ⟨Jx,y ⟩ = −⟨Jx,J 2y⟩ = −⟨J 2y,Jx ⟩ = −⟨Jy,x ⟩ = −Ω(y,x ),
so Ω is a 2-form. Moreover, if x is a non-zero tangent vector, then Ω( x,Jx ) = ⟨Jx,Jx ⟩ =
g(x)> 0, so it follows that x
Ω ⁄= 0. Thus Ω is non-degenerate.
To go the other way is a little more delicate. Suppose that Ω is given and ﬁx a
Riemannian metric g on M with associated inner product ⟨, ⟩. Then, by linear algebra
there exists a unique bundle mapping A:TM →TM so that Ω( x,y ) = ⟨Ax,y ⟩. Since Ω is
skew-symmetric and non-degenerate, it follows that A must be skew-symmetric relative to
⟨, ⟩ and must be invertible. It follows that −A2 must be symmetric and positive deﬁnite
relative to ⟨, ⟩ .
Now, standard results from linear algebra imply that there i s a unique smooth bundle
map B:TM → TM that is positive deﬁnite and symmetric with respect to ⟨, ⟩ and that
satisﬁes B2 = −A2. Moreover, this linear mapping B must commute with A. (See the
Exercises if you are not familiar with this fact). Thus, the m apping J = AB−1 satisﬁes
J 2 = −I, as desired. □
It is not hard to show that the mappings ( J,g 0) ↦→Ω and (Ω ,g ) ↦→J constructed in the
proof of Proposition 1 depend continuously (in fact, smooth ly) on their arguments. Since
the set of Riemannian metrics on M is contractible, it follows that the set of homotopy
classes of almost complex structures on M is in natural one-to-one correspondence with
the set of homotopy classes of almost symplectic structures .
(The reader who is familiar with the theory of principal bund les knows that at the
heart of Proposition 1 is the fact that Sp( n, R) and GL( n, C) have the same maximal
compact subgroup, namely U( n).)
L.6.2 103

Now I can describe some of the bundle obstructions. Suppose t hatM has a symplectic
structure Ω and let J be any one of the almost complex structures on M we constructed
above. Then the tangent bundle of M can be regarded as a complex bundle, which we will
denote by TJ , and hence has a total Chern class
c(TJ ) =
(
1 +c1(J) +c2(J) + · · · +cn(J)
)
whereci(J) ∈H 2i(M, Z). Now, by the properties of Chern classes, cn(J) = e(TM ), where
e(TM ) is the Euler class of the tangent bundle given the orientati on determined by the
volume form Ω n.
These classes are related to the Pontrijagin classes of TM by the Whitney sum formula
(see [MS]):
p(TM ) = 1 −p1(TM ) +p2(TM ) − · · · + (−1)[n/2]p[n/2](TM )
=c(TJ ⊕T −J )
=
(
1 +c1(J) +c2(J) + · · · +cn(J)
)(
1 −c1(J) +c2(J) − · · · + (−1)ncn(J)
)
Sincep(TM ) depends only on the diﬀeomorphism class of M , this gives quadratic equations
for the ci(J),
pk(T ) =
(
ck(J)
)2
− 2ck−1(J)ck+1(J) + · · · + (−1)k2c0(J)c2k(J),
to which any manifold with an almost complex structure must h ave solutions. Since not
every 2n-manifold has cohomology classes ci(J) satisfying these equations, it follows that
some 2n-manifolds have no almost complex structure and hence, by Pr oposition 2, no
almost symplectic structure either.
Examples. Here are two examples in dimension 4 to show that the cohomolo gy ring
condition and the bundle obstruction are independent.
•M =S1 ×S3 does not have a symplectic structure because H 2(M, R) = 0. However
the bundle obstruction vanishes because M is parallelizable (why?). Thus M does have
an almost symplectic structure.
• M = CP2 # CP2. The cohomology ring of M in this case is generated over Z by
two generators u1 and u2 in H 2(M, Z) that are subject to the relations u1u2 = 0 and
u2
1 = u2
2 = v where v generates H 4(M, Z). For any non-zero class u = n1u1 +n2u2, we
haveu2 = (n2
1 +n2
2)v ⁄= 0. Thus the cohomology ring condition is satisﬁed.
However,M has no almost symplectic structure: If it did, then T =TM would have
a complex structure J, with total Chern class c(J) and the equations above would give
p1(T ) =
(
c1(J)
)2
− 2c2(J). Moreover, we would have e(T ) = c2(J). Thus, we would have
to have (
c1(J)
)2
=p1(T ) + 2e(T ).
L.6.3 104

For any compact, simply-connected, oriented 4-manifold M with orientation class
µ ∈ H 4(M, Z), the Hirzebruch Signature Theorem (see [MS]) implies p1(T ) = 3( b+
2 −
b−
2 )µ, where b±
2 are the number of positive and negative eigenvalues respect ively of the
intersection pairing H 2(M, Z) ×H 2(M, Z) → Z. In addition, e(T ) = (2 + b+
2 +b−
2 )µ.
Substituting these into the above formula, we would have
(
c1(J)
)2
= (4 + 5b+
2 −b−
2 )µ for
any complex structure J on the tangent bundle of M .
In particular, if M = CP2 # CP2 had an almost complex structure J, then
(
c1(J)
)2
would be either 14 v (if µ = v, since then b+
2 = 2 and b−
2 = 0) or −2v (if µ = −v, since
then b+
2 = 0 and b−
2 = 2). However, by our previous calculations, neither 14 v nor −2v is
the square of a cohomology class in H 2(CP2 # CP2, Z).
◮ This example shows that, in general, one cannot hope to have a connected sum
operation for symplectic manifolds.
The actual conditions for a manifold to have an almost symple ctic structure can be
expressed in terms of characteristic classes, so, in princi ple, this can always be determined
once the manifold is given explicitly. In Lecture 9 we will de scribe more fully the following
remarkable result of Gromov:
◮ If M 2n has no compact components and has an almost symplectic struc ture Υ ,
then there exists a symplectic structure Ω on M that is homotopic to Υ through almost
symplectic structures.
Thus, the problem of determining which manifolds have sympl ectic structures is now
reduced to the compact case. In this case, no obstruction bey ond what I have already
described is known. Thus, I can state the following:
Basic Open Problem: If a compact manifold M 2n satisﬁes the cohomology ring condi-
tion and has an almost symplectic structure, does it have a sy mplectic structure?
Even (perhaps especially) for 4-manifolds, this problem is extremely interesting and
very poorly understood.
Deformations of Symplectic Structures. We will now turn to some of the features
of the space of symplectic structures on a given manifold tha t does admit symplectic
structures. First, we will examine the ‘deformation proble m’. The following theorem due
to Moser (see [We]) shows that symplectic structures determ ining a ﬁxed cohomology class
in H 2 on a compact manifold are ‘rigid’.
Theorem 1: IfM 2n is a compact manifold and Ωt fort ∈ [0, 1] is a continuous 1-parameter
family of smooth symplectic structures on M that has the property that the cohomology
classes [Ωt] in H 2
dR(M, R) are independent of t, then for each t ∈ [0, 1], there exists a
diﬀeomorphism φt so that φ∗
t (Ωt) = Ω 0.
L.6.4 105

Proof: We will start by proving a special case and then deduce the gen eral case from it.
Suppose that Ω 0 is a symplectic structure on M and that ϕ ∈ A 1(M ) is a 1-form so that,
for all s ∈ (−1, 1), the 2-form
Ωs = Ω 0 +sdϕ
is a symplectic form on M as well. (This is true for all suﬃciently “small” 1-forms on M
since M is compact.) Now consider the 2-form on ( −1, 1) ×M deﬁned by the formula
Ω = Ω 0 +sdϕ −ϕ ∧ds.
(Here, we are using s as the coordinate on the ﬁrst factor ( −1, 1) and, as usual, we write
Ω 0 and ϕ instead of π∗
2(Ω 0) and π∗
2 (ϕ) where π2: (−1, 1) ×M → M is the projection on
the second factor.)
The reader can check that Ω is closed on ( −1, 1) ×M . Moreover, since Ω pulls back
to each slice {s0} ×M to be the non-degenerate form Ω s0 it follows that Ω has half-rank
n everywhere. Thus, the kernel NΩ is 1-dimensional and is transverse to each of the slices
{t} ×M . Hence there is a unique vector ﬁeld X that spans NΩ and satisﬁes ds(X) = 1.
Now because M is compact, it is not diﬃcult to see that each integral curve o f X
projects by s = π1 diﬀeomorphically onto ( −1, 1). Moreover, it follows that there is a
smooth map φ: (−1, 1) ×M →M so that, for each m, the curve t ↦→φ(t,m ) is the integral
curve of X that passes through (0 ,m ).
It follows that the map Φ: ( −1, 1) ×M → (−1, 1) ×M deﬁned by
Φ(t,m ) =
(
t,φ (t,m )
)
carries the vector ﬁeld ∂/∂s to the vector ﬁeld X. Moreover, since Ω 0 and Ω have the
same value when pulled back to the slice {0} ×M and since
L∂/∂s Ω 0 = 0
∂/∂s Ω 0 = 0
and LX Ω = 0
X Ω = 0 ,
it follows easily that Φ ∗(Ω) = Ω 0. In particular, φ∗
t (Ωt) = Ω 0 where φt is the diﬀeomor-
phism of M given by φt(m) = φ(t,m ).
Now let us turn to the general case. If Ω t for 0 ≤ t ≤ 1 is any continuous family of
smooth closed 2-forms for which the cohomology classes [Ω t] are all equal to [Ω 0], then for
any two values t1 and t2 in the unit interval, consider the 1-parameter family of 2-f orms
Υ s = (1 −s)Ωt1 +sΩt2.
Using the compactness of M , it is not diﬃcult to show that for t2 suﬃciently close to t1,
the family Υ s is a 1-parameter family of symplectic forms on M fors in some open interval
containing [0, 1]. Moreover, by hypothesis, [Ω t2 − Ωt1 ] = 0, so there exists a 1-form ϕ on
M so that dϕ = Ω t2 − Ωt1 . Thus,
Υ s = Ω t1 +sdϕ.
L.6.5 106

By the special case already treated, there exists a diﬀeomor phism φt2,t1 of M so that
φ∗
t2,t1 (Ωt2 ) = Ω t1 .
Finally, using the compactness of the interval [0 ,t ] for any t ∈ [0, 1], we can subdivide
this interval into a ﬁnite number of intervals [ t1,t 2] on which the above argument works.
Then, by composing diﬀeomorphisms, we can construct a diﬀeo morphismφt ofM so that
φ∗
t (Ωt) = Ω 0. □
The reader may have wanted the family of diﬀeomorphisms φt to depend continuously
on t and smoothly on t if the family Ω t is smooth in t. This can, in fact, be arranged.
However, it involves showing that there is a smooth family of 1-forms ϕt on M so that
d
dt Ωt = dϕt, i.e., smoothly solving the d-equation. This can be done, but requires some
delicacy or use of elliptic machinery (e.g., Hodge-deRham t heory).
◮ Theorem 1 does not hold without the hypothesis of compactnes s. For example, if Ω
is the restriction of the standard structure on R2n to the unit ball B2n, then for the family
Ωt =etΩ there cannot be any family of diﬀeomorphisms of the ball φt so that φ∗
t (Ωt) = Ω
since the integrals over B of the volume forms (Ω t)n =entΩn are all diﬀerent.
Intuitively, Theorem 1 says that the “connected components ” of the space of symplec-
tic structures on a manifold are orbits of the group Diff0(M ) of diﬀeomorphisms isotopic
to the identity. (The reason this is only intuitive is that we have not actually deﬁned a
topology on the space of symplectic structures on M .)
It is an interesting question as to how many “connected compo nents” the space of
symplectic structures on M has. The work of Gromov has yielded methods to attack this
problem and I will have more to say about this in Lecture 9.
Submanifolds of Symplectic Manifolds
We will now pass on to the study of the geometry of submanifold s of a symplectic
manifold. The following result describes the behaviour of s ymplectic structures near closed
submanifolds. This theorem, due to Weinstein (see [Weinste in]), can be regarded as a
generalization of Darboux’ Theorem. The reader will note th at the proof is quite similar
to the proof of Theorem 1.
Theorem 2: Let P ⊂ M be a closed submanifold and let Ω 0 and Ω 1 be symplectic
structures on M that have the property that Ω 0(p) = Ω 1(p) for all p ∈ P . Then there
exist open neighborhoods U0 and U1 of P and a diﬀeomorphism φ:U0 → U1 satisfying
φ∗(Ω 1) = Ω 0 and which moreover ﬁxes P pointwise and satisﬁes φ′(p) = idp:TpM →TpM
for all p ∈P .
Proof: Consider the linear family of 2-forms
Ωt = (1 −t)Ω 0 +tΩ 1
L.6.6 107

which ‘interpolates’ between the forms Ω 0 and Ω 1. Since [0 , 1] is compact and since, by
hypothesis, Ω 0(p) = Ω 1(p) for allp ∈P , it easily follows that there is an open neighborhood
U of P in M so that Ω t is a symplectic structure on U for all t in some open interval
I = (−ε, 1 +ε) containing [0, 1].
We may even suppose that U is a ‘tubular neighborhood’ of P that has a smooth
retraction R: [0, 1] ×U →U intoP . Since Φ = Ω 1 − Ω 0 vanishes on P , it follows without
too much diﬃcultly (see the Exercises) that there is a 1-form ϕ on U that vanishes on P
and that satisﬁes dϕ = Φ.
Now, on I ×U , consider the 2-form
Ω = Ω 0 +sdϕ −ϕ ∧ds.
This is a closed 2-form of half-rank n onI ×U . Just as in the previous theorem, it follows
that there exists a unique vector ﬁeld X on I ×U so that ds(X) = 1 and X Ω = 0.
Sinceϕ and dϕ vanish on P , the vector ﬁeld X has the property that X(s,p ) = ∂/∂s
for all p ∈ P and s ∈ I. In particular, the set {0} ×P lies in the domain of the time 1
ﬂow of X. Since this domain is an open set, it follows that there is an o pen neighborhood
U0 of P in U so that {0} ×U0 lies in the domain of the time 1 ﬂow of X. The image of
{0} × U0 under the time 1 ﬂow of X is of the form {1} × U1 where U1 is another open
neighborhood of P in U .
Thus, the time 1 ﬂow of X generates a diﬀeomorphism φ:U0 →U1. By the arguments
of the previous theorem, it follows that φ∗(Ω 1) = Ω 0. I leave it to the reader to check that
φ ﬁxes P in the desired fashion. □
Theorem 2 has a useful corollary:
Corollary : Let Ω be a symplectic structure on M and letf0 andf1 be smooth embeddings
of a manifold P into M so that f ∗
0 (Ω) = f ∗
1 (Ω) and so that there exists a smooth bundle
isomorphismτ :f ∗
0 (TM ) →f ∗
1 (TM ) that extends the identity map on the subbundle TP ⊂
f ∗
i (TM ) and that identiﬁes the symplectic structures on f ∗
i (TM ). Then there exist open
neighborhoods Ui offi(P ) inM and a diﬀeomorphism φ:U0 →U1 that satisﬁes φ∗(Ω) = Ω
and, moreover, φ ◦f0 =f1.
Proof: It is an elementary result in diﬀerential topology that, und er the hypotheses of the
Corollary, there exists an open neighborhood W0 off0(P ) inM and a smooth diﬀeomorphic
embeddingψ:W0 →M so that ψ ◦f0 =f1 andψ′(
f0(p)
)
:Tf0(p)(M ) →Tf1(p)(M ) is equal
toτ (p). It follows that ψ∗(Ω) is a symplectic form on W0 that agrees with Ω along f0(P ).
By Theorem 2, it follows that there is a neighborhood U0 of f0(P ) that lies in W0 and a
smooth map ν:U0 → W0 that is a diﬀeomorphism onto its image, ﬁxes f0(P ) pointwise,
satisﬁes ν′(
f0(p)
)
=idf0(p) for all p ∈P , and also satisﬁes ν∗(
ψ∗(Ω)
)
= Ω. Now just take
φ =ψ ◦ν. □
We will now give two particularly important applications of this result:
IfP ⊂M is a symplectic submanifold, then by using Ω, we can deﬁne a no rmal bundle
for P as follows:
ν(P ) = {(p,v ) ∈P ×TM |v ∈TpM, Ω(v,w ) = 0 for all w ∈TpP }.
L.6.7 108

The bundle ν(P ) has a natural symplectic structure on each of its ﬁbers (see the Exer-
cises), and hence is a symplectic vector bundle. The followi ng proposition shows that, up
to local diﬀeomorphism, this normal bundle determines the s ymplectic structure Ω on a
neighborhood of P .
Proposition 3: Let (P, Υ) be a symplectic manifold and let f0,f 1:P → M be two
symplectic embeddings of P as submanifolds of M so that the normal bundles ν0(P ) and
ν1(P ) are isomorphic as symplectic vector bundles. Then there are open neighborhoods
Ui of fi(P ) in M and a symplectic diﬀeomorphism φ:U0 →U1 that satisﬁes f1 =φ ◦f0.
Proof: It suﬃces to construct the map τ required by the hypotheses of Theorem 2.
Now, we have a symplectic bundle decomposition f ∗
i (TM ) = TP ⊕νi(P ) for i = 1, 2. If
α:ν0(P ) → ν1(P ) is a symplectic bundle isomorphism, we then deﬁne τ = id ⊕α in the
obvious way and we are done. □
At the other extreme, we want to consider submanifolds of M to which the form Ω
pulls back to be as degenerate as possible.
Deﬁnition 2: If Ω is a symplectic structure on M 2n, an immersionf :P →M is said to be
isotropic iff ∗(Ω) = 0. If the dimension of P isn, we say that f is a Lagrangian immersion.
If in addition, f is one-to-one, then we say that f (P ) is a Lagrangian submanifold of M .
Note that the dimension of an isotropic submanifold of M 2n is at most n, so the
Lagrangian submanifolds of M have maximal dimension among all isotropic submanifolds.
Example: Graphs of Symplectic Mappings. If f :M →N is a symplectic mapping
where Ω and Υ are the symplectic forms on M and N respectively, then the graph of f
in M ×N is an isotropic submanifold of M ×N endowed with the symplectic structure
(−Ω) ⊕ Υ = π∗
1(−Ω) + π∗
2 (Υ). If M and N have the same dimension, then the graph of f
in M ×N is a Lagrangian submanifold.
Example: Closed 1-forms. If α is a 1-form on M , then the graph of α in T ∗M is a
Lagrangian submanifold of T ∗M if and only if dα = 0. This follows because Ω on T ∗M
has the “reproducing property” that α∗(Ω) = dα for any 1-form on M .
Proposition 4: Let Ω be a symplectic structure on M and let P be a closed Lagrangian
submanifold of M . Then there exists an open neighborhood U of the zero section in T ∗P
and a smooth map φ:U →M satisfying φ(0p) = p that is a diﬀeomorphism onto an open
neighborhood of P in M and that pulls back Ω to be the standard symplectic structure
on U .
Proof: From the earlier proofs, the reader probably can guess what w e will do. Let
ι:P → M be the inclusion mapping and let ζ:P → T ∗P be the zero section of T ∗P . I
leave as an exercise for the reader to show that ζ ∗(
T (T ∗P )
)
= TP ⊕T ∗P , and that the
induced symplectic structure Υ on this sum is simply the natu ral one on the sum of a
bundle and its dual:
Υ
(
(v1,ξ 1), (v2,ξ 2)
)
=ξ1(v2) −ξ2(v1)
L.6.8 109

I will show that there is a bundle isomorphism τ :TP ⊕T ∗P →ι∗(TM ) that restricts
to the subbundle TP to be ι′:TP →ι∗(TM ).
First, select an n-dimensional subbundle L ⊂ ι∗(TM ) that is complementary to
ι′(TP ) ⊂ ι∗(TM ). It is not diﬃcult to show (and it is left as an exercise for th e reader)
that it is possible to choose L so that it is a Lagrangian subbundle of ι∗(TM ) so that there
is an isomorphism α:T ∗P →L so that τ :TP ⊕T ∗P →ι′(TP ) ⊕L deﬁned by τ =ι′ ⊕α
is a symplectic bundle isomorphism.
Now apply the Corollary to Theorem 2. □
Proposition 4 shows that the symplectic structure on a manif oldM in a neighborhood
of a closed Lagrangian submanifold P is completely determined by the diﬀeomorphism type
of P . This fact has several interesting applications. We will on ly give one of them here.
Proposition 5: Let (M, Ω) be a compact symplectic manifold with H 1
dR(M, R) = 0 .
Then in Diff(M ) endowed with the C1 topology, there exists an open neighborhood U of
the identity map so that any symplectomorphism φ:M → M that lies in U has at least
two ﬁxed points.
Proof: Consider the manifold M ×M endowed with the symplectic structure Ω ⊕ (−Ω).
The diagonal ∆ ⊂ M × M is a Lagrangian submanifold. Proposition 4 implies that
there exists an open neighborhood U of the zero section in T ∗M and a symplectic map
ψ:U →M ×M that is a diﬀeomorphism onto its image so that ψ(0p) = (p,p ).
Now, there is an open neighborhood U0 of the identity map on M in Diff(M ) endowed
with the C0 topology that is characterized by the condition that φ belongs to U0 if and
only if the graph of φ in M ×M , namely id ×φ lies in the open set ψ(U ) ⊂ M ×M .
Moreover, there is an open neighborhood U ⊂ U0 of the identity map on M in Diff(M )
endowed with the C1 topology that is characterized by the condition that φ belongs to U
if and only if ψ−1 ◦ (id ×φ):M →T ∗M is the graph of a 1-form αφ.
Now suppose that φ ∈ U is a symplectomorphism. By our previous discussion, it
follows that the graph of φ in M ×M is Lagrangian. This implies that the graph of αφ
is Lagrangian in T ∗M , which, by our second example, implies that αφ is closed. Since
H 1
dR(M, R) = 0, this, in turn, implies that αφ =dfφ for some smooth function f on M .
SinceM is compact, it follows that fφ must have at least two critical points. However,
these critical points are zeros of the 1-form dfφ =αφ. It is a consequence of our construction
that these points must then be places where the graph of φ intersects the diagonal ∆. In
other words, they are ﬁxed points of φ. □
This theorem can be generalized considerably. According to a theorem of Hamilton
[Ha], if M is compact, then there is an open neighborhood U of the identity map id in
Sp(Ω) (with the C1 topology) so that every φ ∈ U is the time-one ﬂow of a symplectic
vector ﬁeld Xφ ∈ sp(Ω). If Xφ is actually Hamiltonian (which would, of course, follow if
H 1
dR(M, R) = 0), then −Xφ
Ω = dfφ, so Xφ will vanish at the critical points of fφ and
these will be ﬁxed points of φ.
L.6.9 110

Appendix: Lie’s T ransformation Groups, II
The reader who is learning symplectic geometry for the ﬁrst t ime may be astonished by
the richness of the subject and, at the same time, be wonderin g ‘Are there other geometries
like symplectic geometry that remain to be explored?’ The po int of this appendix is to
give one possible answer to this very vague question.
When Lie began his study of transformation groups in n variables, he modeled his
attack on the known study of the ﬁnite groups. Thus, his idea w as that he would ﬁnd all
of the “simple groups” ﬁrst and then assemble them (by solvin g the extension problem)
to classify the general group. Thus, if one “group” G had a homomorphism onto another
“group” H
1 − →K − →G − →H − →1
then one could regard G as a semi-direct product of H with the kernel subgroup K.
Guided by this idea, Lie decided that the ﬁrst task was to clas sify the transitive
transformation groups G, i.e., the ones that acted transitively on Rn (at least locally).
The reason for this was that, if G had an orbit S of dimension 0 < k < n, then the
restriction of the action of G to S would give a non-trivial homomorphism of G into a
transformation group in fewer variables.
Second, Lie decided that he needed to classify ﬁrst the ‘grou ps’ that, in his language,
‘did not preserve any subset of the variables.’ The example h e had in mind was the group
of diﬀeomorphisms of R2 of the form
φ(x,y ) =
(
f (x),g (x,y )
)
.
Clearly the assignment φ ↦→f provides a homomorphism of this group into the group of
diﬀeomorphisms in one variable. Lie called groups that ‘did not preserve any subset of
the variables’ primitive. In modern language, primitive is taken to mean that G does not
preserve any foliation on Rn (coordinates on the leaf space would furnish a ‘proper subse t
of the variables’ that was preserved by G).
Thus, the fundamental problem was to classify the “primitiv e transitive continuous
transformation groups”.
When the algebra of inﬁnitesimal generators of G was ﬁnite dimensional, Lie and his
coworkers made good progress. Their work culminated in the w ork of Cartan and Killing,
classifying the ﬁnite dimensional simple Lie groups. (Inte restingly enough, they did not
then go on to solve the extension problem and so classify all L ie groups. Perhaps they
regarded this as a problem of lesser order. Or, more likely, t he classiﬁcation turned out to
be messy, uninteresting, and ultimately intractable.)
They found that the simple groups fell into two types. Beside s the special linear
groups, such as SL( n, R), SL(n, C) and other complex analogs; orthogonal groups, such as
SO(p,q ) and its complex analogs; and symplectic groups, such as Sp( n, R) and its complex
analogs (which became known as the classical groups), there were ﬁve ‘exceptional’ types.
This story is quite long, but very interesting. The ‘ﬁnite di mensional Lie groups’ went on
L.6.10 111

to become an essential part of the foundation of modern diﬀer ential geometry. A complete
account of this classiﬁcation (along with very interesting historical notes) can be found in
[He].
However, when the algebra of inﬁnitesimal generators of G was inﬁnite dimensional,
the story was not so complete. Lie himself identiﬁed four cla sses of these ‘inﬁnite dimen-
sional primitive transitive transformation groups’. They were
• In every dimension n, the full diﬀeomorphism group, Diff(Rn).
• In every dimension n, the group of diﬀeomorphisms that preserve a ﬁxed volume for m
µ, denoted by SDiff(µ).
• In every even dimension 2 n, the group of diﬀeomorphisms that preserve the standard
symplectic form
Ωn =dx1 ∧dy1 + · · · +dxn ∧dyn,
denoted by Sp(Ωn).
• In every odd dimension 2 n + 1, the group of diﬀeomorphisms that preserve, up to a
scalar function multiple , the 1-form
ωn =dz +x1dy1 + · · · +xndyn.
This ‘group’ was known as the contact group and I will denote it by Ct(ωn).
However, Lie and his coworkers were never able to discover an y others, though they
searched diligently. (By the way, Lie was aware that there we re also holomorphic analogs
acting in Cn, but, at that time, the distinction between real and complex was not generally
made explicit. Apparently, an educated reader was supposed to know or be able to guess
what the generalizations to the complex category were.)
In a series of four papers spanning from 1902 to 1910, ´Elie Cartan reformulated Lie’s
problem in terms of systems of partial diﬀerential equation s and, under the hypothesis
of analyticity (real and complex were not carefully disting uished), he proved that Lie’s
classes were essentially all of the inﬁnite dimensional pri mitive transitive transformation
groups. The slight extension was that SDiff(µ) had a companion extension to R·SDiff(µ),
the diﬀeomorphisms that preserve µ up to a constant multiple and that Sp(Ωn) had a
companion extension to R · Sp(Ωn), the diﬀeomorphisms that preserve Ω n up to a constant
multiple. Of course, there were also the holomorphic analog ues of these. Notice the
remarkable fact that there are no “exceptional inﬁnite dime nsional primitive transitive
transformation groups”.
These papers are remarkable, not only for their results, but for the wealth of concepts
that Cartan introduced in order to solve his problem. In thes e papers, Cartan introduces
the notion of G-structures (of all orders), principal bundles and their co nnections, jet
bundles, prolongation (both of group actions and exterior d iﬀerential systems), and a host
of other ideas that were only appreciated much later. Perhap s because of its originality,
Cartan’s work in this area was essentially ignored for many y ears.
L.6.11 112

In the 1950’s, when algebraic varieties were being explored and developed as complex
manifolds, it began to be understood that complex manifolds were to be thought of as
manifolds with an atlas of coordinate charts whose “overlap s” were holomorphic. Gener-
alizing this example, it became clear that, for any collecti on Γ of local diﬀeomorphisms
of Rn that satisﬁed the following deﬁnition, one could deﬁne a cat egory of Γ-manifolds as
manifolds endowed with an atlas A of coordinate charts whose overlaps lay in A.
Deﬁnition 3: A local diﬀeomorphism of Rn is a pair ( U,φ ) where U ⊂ Rn is an open
set and φ:U → Rn is a one-to-one diﬀeomorphism onto its image. A set Γ of local
diﬀeomorphisms of Rn is said to form a pseudo-group on Rn if it satisﬁes the following
three properties:
(1) (Composition and Inverses) If ( U,φ ) and ( V,ψ ) are in Γ, then ( φ−1(V ),ψ ◦φ) and
(φ(U ),φ −1) also belong to Γ.
(2) (Localization and Globalization) If ( U,φ ) is in Γ, and W ⊂U is open, then ( W,φ |W )
is also in Γ. Moreover, if ( U,φ ) is a local diﬀeomorphism of Rn such that U can be
written as the union of open subsets Wα for which (Wα,φ |Wα ) is in Γ for all α, then
(U,φ ) is in Γ.
(3) (Non-triviality) ( Rn,id ) is in Γ.
As it turned out, the pseudo-groups Γ of interest in geometry were exactly the ones
that could be characterized as the (local) solutions of a sys tem of partial diﬀerential equa-
tions, i.e., they were Lie’s transformation groups. This ca used a revival of interest in
Cartan’s work. Consequently, much of Cartan’s work has now b een redone in modern
language. In particular, Cartan’s classiﬁcation was redon e according to modern standards
of rigor and a very readable account of this theory can be foun d in [SS].
In any case, symplectic geometry, seen in this light, is one o f a small handful of
“natural” geometries that one can impose on manifolds.
L.6.12 113

Exercise Set 6:
Symplectic Manifolds, II
1. Assume n > 1. Show that if Ar,R ⊂ R2n (with its standard symplectic structure) is
the annulus described by the relations r < |x| < R, then there cannot be a symplectic
diﬀeomorphism φ:Ar,R → As,S that ‘exchanges the boundaries’. (Hint: Show that if φ
existed one would be able to construct a symplectic structur e on S2n.) Conclude that one
cannot na ¨ ıvely deﬁne connected sum in the category of symplectic manifolds. (The “na ¨ ıve”
deﬁnition would be to try to take two symplectic manifolds M1 andM2 of the same dimen-
sion, choose an open ball in each one, cut out a sub-ball of eac h and identify the resulting
annuli by an appropriate diﬀeomorphism that was chosen to be a symplectomorphism.)
2. This exercise completes the proof of Proposition 1.
(i) Let S+
n denote the space of n-by-n positive deﬁnite symmetric matrices. Show that
the map σ: S+
n → S+
n deﬁned by σ(s) = s2 is a one-to-one diﬀeomorphism of S+
n onto
itself. Conclude that every element of S+
n has a unique positive deﬁnite square root
and that the map s ↦→√
s is a smooth mapping. Show also that, for any r ∈ O(n),
we have
√
trar = tr √ar , so that the square root function is O( n)-equivariant.
(ii) Let A•
n denote the space of n-by-n invertible anti-symmetric matrices. Show that, for
a ∈ A•
n, the matrix −a2 is symmetric and positive deﬁnite. Show that the matrix
b =
√
−a2 is the unique symmetric positive deﬁnite matrix that satisﬁ es b2 = −a2
and moreover that b commutes with a. Check also that the mapping a ↦→
√
−a2 is
O(n)-equivariant.
(iii) Now verify the claim made in the proof of Proposition 1 t hat, for any smooth vector
bundle E over a manifold M endowed with a smooth inner product on the ﬁbers
and any smooth, invertible skew-symmetric bundle mapping A:E → E, there exists
a unique smooth positive deﬁnite symmetric bundle mapping B:E →E that satisﬁes
B2 = −A2 and that commutes with A.
3. This exercise requires that you know something about chara cteristic classes.
(i) Show that S4n has no almost complex structure for any n. (Hint: What could the
total Chern and Pontrijagin class of the tangent bundle be?)
(Using the Bott Periodicity Theorem, it can be shown that the characteristic class
cn of any complex bundle over S2n must be an integer multiple of ( n − 1)!v where
v ∈ H 2n(S2n) is a generator. It follows that, among the spheres, only S2 and S6
could have almost complex structures and, in fact, they both do. It is a long standing
problem whether or not S6 has a complex structure.)
(ii) Using the formulas for 4-manifolds developed in the Lec ture, determine how many
possibilities there are for the ﬁrst Chern class c1(J) of an almost complex structure J
on M where M a connected sum of 3 or 4 copies of CP2.
E.6.1 114

4. Show that, if Ω 0 is a symplectic structure on a compact manifold M , then there is an
open neighborhood U in H 2(M, R) of [Ω 0], such that, for all u ∈U , there is a symplectic
structure Ω u on M with [Ω u] = u. (Hint: Since M is compact, for any closed 2-form Υ,
the 2-form Ω + tΥ is non-degenerate for all suﬃciently small t.)
5. Mimic the proof of Theorem 1 to prove another theorem of Mose r: For any compact,
connected, oriented manifold M , two volume forms µ0 and µ1 diﬀer by an oriented dif-
feomorphism (i.e., there exists an orientation preserving diﬀeomorphism φ:M → M that
satisﬁes φ∗(µ1) = µ0) if and only if
∫
M
µ0 =
∫
M
µ1.
(This theorem is also true without the hypothesis of compact ness, but the proof is slightly
more delicate.)
6. Let M be a connected, smooth oriented 4-manifold and let µ ∈ A 4(M ) be a volume
form that satisﬁes
∫
Mµ = 1. (By the previous problem, any two such forms diﬀer by an
oriented diﬀeomorphism of M .) For any (smooth) Ω ∈ A 2(M ), deﬁne ∗(Ω 2) ∈C∞(M ) by
the equation
Ω 2 = ∗(Ω 2)µ.
Now, ﬁx a cohomology class u ∈ H 2
dR(M ) satisfying u2 = r[µ] where r ⁄= 0. Deﬁne the
functional F :u → R
F (Ω) =
∫
M
∗(Ω 2) Ω 2 for Ω ∈u.
Show that any F -critical 2-form Ω ∈u is a symplectic form satisfying ∗(Ω 2) = r and that
F has no critical values other than r2. Show also that F (Ω) ≥r2 for all Ω ∈u.
This motivates deﬁning an invariant of the class u by
I(u) = inf
Ω ∈u
F (Ω).
Gromov has suggested (private communication) that perhaps I(u) = r2 for all u, even
when the inﬁmum is not attained.
7. Let P ⊂M be a closed submanifold and let U ⊂M be an open neighborhood of P in
M that can be retracted onto P , i.e., there exists a smooth map R:U × [0, 1] →U so that
R(u, 1) = u for all u ∈U , R(p,t ) = p for all p ∈P and t ∈ [0, 1], and R(u, 0) lies in P for
all u ∈U . (Every closed submanifold of M has such a neighborhood.)
Show that if Φ is a closed k-form on U that vanishes at every point of P , then there
exists a ( k − 1)-form φ on U that vanishes on P and satisﬁes dφ = Φ. (Hint: Mimic
Poincar´ e’s Homotopy Argument: Let Υ =R∗(Φ) and set υ = ∂
∂t Υ. Then, using the fact
that υ(u,t ) can be regarded as a ( k − 1)-form at u for all t, deﬁne
φ(u) =
∫ 1
0
υ(u,t )dt.
Now verify that φ has the desired properties.)
E.6.2 115

8. Show that Theorem 2 implies Darboux’ Theorem. (Hint: Take P to be a point in a
symplectic manifold M .)
9. This exercise assumes that you have done Exercise 5.10. Let (M, Ω) be a symplectic
manifold. Show that the following description of the ﬂux hom omorphism is valid. Let p be
an e-based path in Sp(Ω). Thus, p: [0, 1] ×M →M satisﬁes p∗
t (Ω) = Ω for all 0 ≤t ≤ 1.
Show that p∗(Ω) = Ω + ϕ∧dt for some 1-form ϕ on [0, 1] ×M . Let ιt:M → [0, 1] ×M be
the “t-slice inclusion”: ιt(m) = (t,m ), and set ϕt =ι∗
t (ϕ).
Show that ϕt is closed for all 0 ≤t ≤ 1. Show that if we set
˜Φ(p) =
∫ 1
0
ϕtdt,
then the cohomology class [ ˜Φ(p)] ∈ H 1
dR(M, R) depends only on the homotopy class of p
and hence deﬁnes a map Φ: ~Sp0(Ω) →H 1
dR(M, R). Verify that this map is the same as the
ﬂux homomorphism deﬁned in Exercise 5.10.
Use this description to show that if p is in the kernel of Φ, then p is homotopic to a
path p′ for which the forms ϕ′
t are all exact. This shows that the kernel of Φ is actually
connected.
10. The point of this exercise is to show that any symplectic vect or bundle over a sym-
plectic manifold (M, Ω) can occur as the symplectic normal bundle for some symplecti c
embedding M into some other symplectic manifold.
Let (M, Ω) be a symplectic manifold and let π:E →M be a symplectic vector bundle
over M of rank 2 n. (I.e., E comes equipped with a section B of Λ 2(E∗) that restricts
to each ﬁber Em to be a symplectic structure Bm.) Show that there exists a symplectic
structure Ψ on an open neighborhood in E of the zero section of E that satisﬁes the
condition that Ψ 0m = Ω m +Bm under the natural identiﬁcation T0mE =TmM ⊕Em.
(Hint: Choose a locally ﬁnite open cover U = {Uα |α ∈A} of M so that, if we deﬁne
Eα = π−1(Uα), then there exists a symplectic trivialization τα:Eα → R2n (where R2n is
given its standard symplectic structure Ω 0 =dxi∧dyi). Now let {λα |α ∈A} be a partition
of unity subordinate to the cover U. Show that the form
Ψ = π∗(Ω) +
∑
α
d
(
λατ ∗
α(xidyi)
)
has the desired properties.)
11. Show that if E is a symplectic vector bundle over M and L ⊂ E is a Lagrangian
subbundle, then E is isomorphic to L ⊕L∗ as a symplectic bundle. (The symplectic
bundle structure Υ on L ⊕L∗ is the one that, on each ﬁber satisﬁes
Υ
(
(v,α ), (w,β )
)
=α(w) −β(v). )
E.6.3 116

(Hint: First choose a complementary subbundle F ⊂E so that E =L ⊕F . Show that
F is naturally isomorphic to L∗ abstractly by using the fact that the symplectic structure
on E is non-degenerate. Then show that there exists a bundle map A:F →L so that
˜F = {v +Av | v ∈F }
is also a Lagrangian subbundle of E that is complementary to L and isomorphic to L∗ via
some bundle map α:L∗ → ˜F . Now show that id ⊕α:L ⊕L∗ →L ⊕ ˜F ≃E is a symplectic
bundle isomorphism.)
12. Action-Angle Coordinates. Proposition 4 can be used to show the existence of so-
called action angle coordinates in the neighborhood of a com pact level set of a completely
integrable Hamiltonian system. (See Lecture 5). Here is how this goes: Let ( M 2n, Ω) be
a symplectic manifold and let f = (f 1,...,f n):M → Rn be a smooth submersion with
the property that the coordinate functions fi are in involution, i.e., {fi,f j} = 0. Suppose
that, for some c ∈ Rn, the f -level set Mc =f −1(c) is compact. Replacing f byf −c, we
may assume that c = 0, which we do from now on.
Show that M0 ⊂M is a closed Lagrangian submanifold of M .
Use Proposition 4 to show that there is an open neighborhood B of 0 ∈ Rn so that(
f −1(B), Ω
)
is symplectomorphic to a neighborhood U of the zero section in T ∗M0 (en-
dowed with its standard symplectic structure) in such a way t hat, for each b ∈B, the sub-
manifoldMb =f −1(b) is identiﬁed with the graph of a closed 1-form ωb onM0. Show that
it is possible to choose b1,...,b n inB so that the corresponding closed 1-forms ω1,...,ω n
are linearly independent at every point of M0.
Conclude that M0 is diﬀeomorphic to a torus T = Rn/Λ where Λ ⊂ Rn is a lattice,
in such a way that the forms ωi become identiﬁed with dθi whereθi are the corresponding
linear coordinates on Rn.
Now prove that for any b ∈B, the 1-form ωb must be a linear combination of the ωi
with constant coeﬃcients. Thus, there are functions ai on B so that ωb =ai(b)ωi. (Hint:
Show that the coeﬃcients must be invariant under the ﬂows of t he vector ﬁelds dual to
the ωi.)
Conclude that, under the symplectic map identifying MB with U , the form Ω gets
identiﬁed with dai∧dθi. The functions ai and θi are the so-called “action-angle coordi-
nates”.
Extra Credit: Trace through the methods used to prove Proposition 4 and sho w that,
in fact, the action-angle coordinates can be constructed us ing quadrature and “ﬁnite”
operations.
E.6.4 117

Lecture 7:
Classical Reduction
In this section, we return to the study of group actions. This time, however, we
will concentrate on group actions on symplectic manifolds t hat preserve the symplectic
structure. Such actions happen to have quite interesting pr operties and moreover, turn
out to have a wide variety of applications.
Symplectic Group Actions. First, the basic deﬁnition.
Deﬁnition 1: Let (M, Ω) be a symplectic manifold and let G be a Lie group. A left
action λ:G ×M →M of G on M is a symplectic action if λ∗
a(Ω) = Ω for all a ∈G.
We have already encountered several examples:
Example: Lagrangian Symmetries. If G acts on a manifold M is such a way that
it preserves a non-degenerate Lagrangian L:TM → R, then, by construction, it preserves
the symplectic 2-form dωL.
Example: Cotangent Actions. A left G-action λ:G ×M → M , induces an action
˜λ of G on T ∗M . Namely, for each a ∈ G, the diﬀeomorphism λa:M → M induces a
diﬀeomorphism ˜λa:T ∗M → T ∗M . Since the natural symplectic structure on T ∗M is
invariant under diﬀeomorphisms, it follows that ˜λ is a symplectic action.
Example: Coadjoint Orbits. As we saw in Lecture 5, for every ξ ∈ g∗, the coadjoint
orbit G ·ξ carries a natural G-invariant symplectic structure Ω ξ. Thus, the left action of
G on G ·ξ is symplectic.
Example: Circle Actions on Cn. Let z1,...,z n be linear complex coordinates on Cn
and let this vector space be endowed with the symplectic stru cture
Ω = i
2
(
dz1 ∧d¯z1 + · · · +dzn ∧d¯zn)
=dx1 ∧dy1 + · · · +dxn ∧dyn
where zk =xk +iyk. Then for any integers ( k1,...,k n), we can deﬁne an action of S1 on
Cn by the formula
eiθ ·


z1
.
.
.
zn

 =


eik1θz1
.
.
.
eiknθzn


The reader can easily check that this deﬁnes a symplectic cir cle action on Cn.
Generally what we will be interested in is the following: Y will be a Hamiltonian
vector ﬁeld on a symplectic manifold ( M, Ω) and G will act symplectically on M as a
group of symmetries of the ﬂow of Y . We want to understand how to use the action of G
to “reduce” the problem of integrating the ﬂow of Y .
L.7.1 118

In Lecture 3, we saw that when Y was the Euler-Lagrange vector ﬁeld associated to a
non-degenerate Lagrangian L, then the inﬁnitesimal generators of symmetries of L could
be used to generate conserved quantities for the ﬂow of Y . We want to extend this process
(as far as is reasonable) to the general case.
◮ For the rest of the lecture, I will assume that G is a Lie group with a symplectic
action λ on a connected symplectic manifold (M, Ω) .
Since λ is symplectic, it follows that the mapping λ∗: g → X(M ) actually has image
in sp(Ω), the algebra of symplectic vector ﬁelds on M . As we saw in Lecture 3, λ∗ is
an anti-homomorphism, i.e., λ∗
(
[x,y ]
)
= −
[
λ∗(x),λ ∗(y)
]
. Since, as we saw in Lecture
5, [ sp(Ω), sp(Ω)] ⊂ h(Ω), it follows that λ∗
(
[g, g]
)
⊂ h(Ω). Thus, Hλ: g → H 1
dR(M, R)
deﬁned by Hλ(x) =
[
λ∗(x) Ω
]
is a homomorphism of Lie algebras with kernel containing
the commutator subalgebra [ g, g].
The map Hλ is the obstruction to ﬁnding a Hamiltonian function associa ted to each
inﬁnitesimal symmetry λ∗(x) since Hλ(x) = 0 if and only if λ∗(x) Ω = −df for some
f ∈C∞(M ).
Deﬁnition 2: A symplectic action λ:G ×M →M is said to be Hamiltonian if Hλ = 0,
i.e., if λ∗(g) ⊂ h(Ω).
There are a few particularly interesting cases where the obs truction Hλ must vanish:
• If H 1
dR(M, R) = 0. In particular, if M is simply connected.
• If g is perfect, i.e., [ g, g] = g. For example this happens whenever the Killing form
on g is non-degenerate (this is the ﬁrst Whitehead Lemma, see Exe rcise 3). However, this
is not the only case: For example, if G is the group of rigid motions in Rn for n ≥ 3, then
g has this property, even though its Killing form is degenerat e.
• If there exists a 1-form ω on M that is invariant under G and satisﬁes Ω = dω.
(This is the case of symmetries of a Lagrangian.) To see this, note that if X is a vector
ﬁeld on M that preserves ω, then
0 = LXω =d(X ω) +X Ω,
so X Ω is exact.
For a Hamiltonian action λ, every inﬁnitesimal symmetry λ∗(x) has a Hamiltonian
function fx ∈C∞. However, the choice of fx is not unique since we can add any constant
to fx without changing its Hamiltonian vector ﬁeld. This non-uni queness causes some
problems in the theory we wish to develop.
To see why, suppose that we choose a (linear) lifting ρ: g →C∞(M ) of −λ∗: g → h(Ω).
(The choice of −λ∗ instead of λ∗ was made to get rid of the annoying sign in the formula
for the bracket.)
g
ρ ↓ ց −λ∗
0 → R → C∞(M ) → h(Ω) → 0
L.7.2 119

Thus, for every x ∈ g, we have λ∗(x) Ω = d
(
ρ(x)
)
. A short calculation (see the Exercises)
now shows that {ρ(x),ρ (y)} is a Hamiltonian function for −λ∗([x,y ]), i.e., that
λ∗
(
[x,y ]
)
Ω = d
(
{ρ(x),ρ (y)}
)
.
In particular, it follows (since M is connected) that there must be a skew-symmetric
bilinear map cρ: g × g → R so that
{ρ(x),ρ (y)} =ρ
(
[x,y ]
)
+cρ(x,y ).
An application of the Jacobi identity implies that the map cρ satisﬁes the condition
cρ
(
[x,y ],z
)
+cρ
(
[y,z ],x
)
+cρ
(
[z,x ],y
)
= 0 for all x,y,z ∈ g.
This condition is known as the 2-cocycle condition forcρ regarded as an element of A2(g) =
Λ 2(g∗). (See Exercise 3 for an explanation of this terminology.)
For purposes of simplicity, it would be nice if we could choos e ρ so that cρ were
identically zero. In order to see whether this is possible, l et us choose another linear map
˜ρ: g →C∞(M ) that satisﬁes ˜ρ(x) = ρ(x) +ξ(x) where ξ: g → R is any linear map. Every
possible lifting of −λ∗ is clearly of this form for some ξ. Now we compute that
{
˜ρ(x), ˜ρ(y)
}
=
{
ρ(x),ρ (y)
}
=ρ
(
[x,y ]
)
+cρ(x,y )
= ˜ρ
(
[x,y ]
)
+cρ(x,y ) −ξ
(
[x,y ]
)
.
Thus,c˜ρ(x,y ) = cρ(x,y ) −ξ
(
[x,y ]
)
. Thus, in order to be able to choose ˜ ρ so that c˜ρ = 0,
we see that there must exist a ξ ∈ g∗ so that cρ = −δξ where δξ is the skew-symmetric
bilinear map on g that satisﬁes δξ(x,y ) = −ξ
(
[x,y ]
)
(see the Exercises for an explanation
of this notation). This is known as the 2 -coboundary condition.
There are several important cases where we can assure that cρ can be written in the
form −δξ. Among them are:
• If M is compact, then the sequence
0 → R →C∞(M ) → H(Ω) → 0
splits: If we let C∞
0 (M, Ω) ⊂C∞(M ) denote the space of functions f for which
∫
Mf Ωn =
0, then these functions are closed under Poisson bracket (se e Exercise 5.6 for a hint as to
why this is true) and we have a splitting of Lie algebras C∞(M ) = R ⊕C∞
0 (M, Ω). Now
just choose the unique ρ so that it takes values in C∞
0 (M, Ω). This will clearly have cρ = 0.
• If g has the property that every 2-cocycle for g is actually a 2-coboundary. This hap-
pens, for example, if the Killing form of g is non-degenerate (this is the second Whitehead
Lemma, see Exercise 3), though it can also happen for other Li e algebras. For example,
for the non-abelian Lie algebra of dimension 2, it is easy to s ee that every 2-cocycle is a
2-coboundary.
L.7.3 120

• If there is a 1-form ω on M that is preserved by the G action and satisﬁes dω = Ω.
(This is true in the case of symmetries of a Lagrangian.) In th is case, we can merely take
ρ(x) = −ω
(
λ∗(x)
)
. I leave as an exercise for the reader to check that this works .
Deﬁnition 3: A Hamiltonian action λ:G ×M → M is said to be a Poisson action if
there exists a lifting ρ with cρ = 0.
Henceforth in this Lecture, I am only going to consider Poiss on actions. By my
previous remarks, this case includes all of the Lagrangians with symmetries, but it also
includes many others.
I will assume that, in addition to having a Poisson action λ:G ×M → M speciﬁed,
we have chosen a lifting ρ: g → C∞(M ) of −λ∗ that satisﬁes
{
ρ(x),ρ (y)
}
= ρ
(
[x,y ]
)
for
all x,y ∈ g. Note that such a ρ is unique up to replacement by ˜ρ =ρ +ξ where ξ : g → R
satisﬁes δξ = 0. Such ξ (if any non-zero ones exist) are ﬁxed under the co-adjoint ac tion
of the identity component of G.
The Momentum Mapping. We are now ready to make one of the most important
constructions in the theory.
Deﬁnition 4: The momentum mapping associated to λ andρ is the mapping µ:M → g∗
that satisﬁes
µ(m)(y) = ρ(y)(m).
Note that, for ﬁxed m ∈ M , the assignment y ↦→ρ(y)(m) is a linear map from g to
R, so the deﬁnition makes sense.
It is worth pausing to consider why this mapping is called the momentum mapping.
The reader should calculate this mapping in the case of a free particle or a rigid body
moving in space. In either case, the Lagrangian is invariant under the action of the group
G of rigid motions of space. If y ∈ g corresponds to a translation, then ρ(y) gives the
function on T R3 that evaluates at each point (i.e., each position-plus-vel ocity) to be the
linear momentum in the direction of translation. If y corresponds to rotation about a ﬁxed
axis, then ρ(y) turns out to be the angular momentum of the body about that ax is.
One important reason for studying the momentum mapping is th e following formula-
tion of the classical conservation of momentum theorems:
Proposition 1: If f is a function on M that is invariant under the action of G, then µ
is constant on the integral curves of the Hamiltonian vector ﬁeld Xf . □
In particular, µ provides conserved quantities for any G-invariant Hamiltonian.
The main result about the momentum mapping is the following o ne.
Theorem 1: IfG is connected, then the momentum mapping µ:M → g∗ isG-equivariant.
L.7.4 121

Proof: Recall that the coadjoint action of G on g∗ is deﬁned by Ad ∗(g)(ξ)(x) =
ξ
(
Ad(g−1)x
)
. The condition that µ be G-equivariant, i.e., that µ(g ·m) = Ad ∗(g)
(
µ(m)
)
for all m ∈M and g ∈G, is thus seen to be equivalent to the condition that
ρ
(
Ad(g−1)y
)
(m) = ρ(y)(g ·m)
for all m ∈M ,g ∈G, and y ∈ g. This is the identity I shall prove.
SinceG is connected and since each side of the above equation repres ents a G-action,
if we prove that the above formula holds for g of the form g =etx for any x ∈ g and any
t ∈ R, the formula for general g will follow. Thus, we want to prove that
ρ
(
Ad(e−tx)y
)
(m) = ρ(y)(etx ·m)
for all t. Since this latter equation holds at t = 0, it is enough to show that both sides
have the same derivative with respect to t.
Now the derivative of the right hand side of the formula is
d
(
ρ(y)
)(
λ∗(x)(etx ·m)
)
= Ω
(
λ∗(y)(etx ·m),λ ∗(x)(etx ·m)
)
= Ω
(
λ∗
(
Ad(e−tx)y
)
(m),λ ∗
(
Ad(e−tx)x
)
(m)
))
= Ω
(
λ∗
(
Ad(e−tx)y
)
(m),λ ∗(x)(m)
)
where, to verify the second equality we have used the identit y
λ′
a
(
λ∗(y)(m)
)
=λ∗
(
Ad(a)y
)
(a ·m)
and the fact that Ω is G-invariant.
On the other hand, the derivative of the left hand side of the f ormula is clearly
ρ
(
[−x, Ad(e−tx)y]
)
(m) = −
{
ρ(x),ρ
(
Ad(e−tx)y
)}
(m)
= Ω
(
λ∗
(
Ad(e−tx)y
)
(m),λ ∗(x)(m)
)
so we are done. (Note that I have used my assumption that cρ = 0!) □
Example: Left-Invariant Metrics on Lie Groups. Let G be a Lie group and let
Q: g → R be a non-degenerate quadratic form with associated inner pr oduct ⟨, ⟩Q. Let
L:TG → R be the Lagrangian
L = 1
2Q
(
ω
)
where ω:TG → g is, as usual, the canonical left-invariant form on G. Then, using the
basepoint map π:TG →G, we compute that
ωL =
⟨
ω,π ∗(ω)
⟩
Q.
As we saw in Lecture 3, the assumption that Q is non-degenerate implies that dωL is
a symplectic form on TG . Now, since the ﬂow of a right-invariant vector ﬁeld Yx is
multiplication on the left by etx, it follows that, for this action, we may deﬁne
ρ(x) = −ωL(Y ′
x) = −
⟨
ω,ω (Yx)
⟩
Q = −
⟨
ω, Ad(g−1)x
⟩
Q
L.7.5 122

(where g:TG →G is merely a more descriptive name for the base point map than π).
Now, there is an isomorphism τQ: g → g∗, called transpose with respect to Q that
satisﬁes τQ(x)(y) = ⟨x,y ⟩Q for all x,y ∈ g. In terms of τQ, we can express the momentum
mapping as
µ(v) = −Ad∗(g)
(
τQ(ω(v))
)
for all v ∈TG . Note that µ is G-equivariant, as promised by the theorem.
According to the Proposition 1, the function µ is a conserved quantity for the solutions
of the Euler-Lagrange equations. In one of the Exercises, yo u are asked to show how this
information can be used to help solve the Euler-Lagrange equ ations for the L-critical
curves.
Example: Coadjoint Orbits. LetG be a Lie group and consider ξ ∈ g∗ with stabilizer
subgroup Gξ ⊂G. The orbit G ·ξ ⊂ g∗ is canonically identiﬁed with G/Gξ ( identify a ·ξ
with aGξ) and we have seen that there is a canonical G-invariant symplectic form Ω ξ
on G/Gξ that satisﬁes π∗
ξ (Ωξ) = dωξ where πξ : G → G/Gξ is the coset projection, ω is
the tautological left-invariant 1-form on G, and ωξ =ξ(ω).
Recall also that, for each x ∈ g, the right-invariant vector ﬁeld Yx on G is deﬁned so
that Yx(e) = x ∈ g. Then the vector ﬁeld λ∗(x) on G/Gξ is πξ-related to Yx, so
π∗
ξ
(
λ∗(x)
Ωξ
)
=Yx dωξ =d
(
−ωξ(Yx)
)
.
(This last equality follows because ωξ, being left-invariant, is invariant under the ﬂow
of Yx.) Now, the value of the function ωξ(Yx) at a ∈G is
ωξ(Yx)(a) = ξ
(
ω(Yx(a))
)
=ξ
(
Ad(a−1)(x)
)
= Ad ∗(a)(ξ)(x) = (a ·ξ)(x).
Thus, it follows that the natural left action of G on G·ξ is Poisson, with momentum
mapping µ :G·ξ → g∗ given by
µ(a ·ξ) = −a ·ξ.
(Note: some authors do not have a minus sign here, but that is b ecause their Ω ξ is the
negative of ours.)
Reduction. I now want to discuss a method of taking quotients by group act ions in
the symplectic category. Now, when a Lie group G acts symplectically on the left on a
symplectic manifold M , it is not generally true that the space of orbits G\M can be given
a symplectic structure, even when this orbit space can be giv en the structure of a smooth
manifold (for example, the quotient need not be even dimensi onal).
However, when the action is Poisson, there is a natural metho d of breaking the orbit
spaceG\M into a union of symplectic submanifolds provided that certa in regularity criteria
are met. The procedure I will describe is known as symplectic reduction. It is due, in its
modern form, to Marsden and Weinstein (see [GS 2]).
The idea is simple: If µ:M → g∗ is the momentum mapping, then the G-equivariance
of µ implies that there is a well-deﬁned set map
¯µ:G\M →G\g∗.
L.7.6 123

The theorem we are about to prove asserts that, provided cert ain regularity criteria are
met, the subsets Mξ = ¯µ−1( ¯ξ) ⊂G\M are symplectic manifolds in a natural way.
Deﬁnition 4: Let f :X → Y be a smooth map. A point y ∈ Y is a clean value of f if
the set f −1(y) ⊂X is a smooth submanifold of X and, moreover, if Txf −1(y) = kerf ′(x)
for each x ∈f −1(y).
Note: While every regular value of f is clean, not every clean value of f need be
regular. The concept of cleanliness is very frequently enco untered in the reduction theory
we are about to develop.
Theorem 2: Let λ:G ×M → M be a Poisson action on the symplectic manifold M .
Letµ:M → g∗ be a momentum mapping for λ. Suppose that, ξ ∈ g∗ is a clean value of µ.
ThenGξ acts smoothly on µ−1(ξ). Suppose further that the space of Gξ-orbits in µ−1(ξ),
say,Mξ = Gξ\
(
µ−1(ξ)
)
, can be given the structure of a smooth manifold in such a way
that the quotient mapping πξ:µ−1(ξ) →Mξ is a smooth submersion. Then there exists a
symplectic structure Ωξ onMξ that is deﬁned by the condition that π∗
ξ (Ωξ) be the pullback
of Ω to µ−1(ξ).
Proof: Sinceξ is a clean value of µ, we know that µ−1(ξ) is a smooth submanifold of M .
By the G-equivariance of the momentum mapping, the stabilizer subg roup Gξ ⊂ G acts
on M preserving the submanifold µ−1(ξ). The restricted action of Gξ on µ−1(ξ) is easily
seen to be smooth.
Now, I claim that, for each m ∈µ−1(ξ), the Ω-complementary subspace to Tm
(
µ−1(ξ)
)
is the space Tm
(
G ·m
)
, i.e., the tangent to the G-orbit through m. To see this, ﬁrst
note that the space Tm
(
G ·m
)
is spanned by the values at m assumed by the vector
ﬁelds λ∗(x) for x ∈ g. Thus, a vector v ∈ TmM lies in the Ω-complementary space
of Tm
(
G ·m
)
if and only if v satisﬁes Ω
(
λ∗(x)(m),v
)
= 0 for all x ∈ g. Since, by
deﬁnition, Ω
(
λ∗(x)(m),v
)
= d
(
ρ(x)
)
(v), it follows that this condition on v is equivalent
to the condition that v lie in ker µ′(m). However, since ξ is a clean value of µ, we have
kerµ′(m) = Tm
(
µ−1(ξ)
)
, as claimed.
Now, theG-equivariance ofµ implies thatµ−1(ξ)∩
(
G·m
)
=Gξ ·m for allm ∈µ−1(ξ).
In particular, Tm
(
Gξ ·m
)
⊆Tm
(
µ−1(ξ)
)
∩Tm
(
G·m
)
. To demonstrate the reverse inclusion,
suppose that v lies in both Tm
(
µ−1(ξ)
)
andTm
(
G·m
)
. Then v =λ∗(x)(m) for some x ∈ g,
and, by the G-equivariance of the momentum mapping and the assumption th atξ is clean
(so that Tm
(
µ−1(ξ)
)
= kerµ′(m)) we have
0 = µ′(m)(v) = µ′(m)
(
λ∗(x)(m)
)
=
(
Ad∗)
∗(x)(µ(m)) =
(
Ad∗)
∗(x)(ξ)
so that x must lie in gξ. Consequently, v = λ∗(x)(m) is tangent to the orbit Gξ ·m and
thus,
Tm
(
µ−1(ξ)
)
∩Tm
(
G ·m
)
= kerµ′(m) ∩Tm
(
G ·m
)
=Tm
(
Gξ ·m
)
.
As a result, since the Ω-complementary spaces Tm
(
µ−1(ξ)
)
andTm
(
G ·m
)
intersect in the
tangents to the Gξ-orbits, it follows that if ˜Ωξ denotes the pullback of Ω to µ−1(ξ), then
the null space of ˜Ωξ at m is precisely Tm
(
Gξ ·m
)
.
L.7.7 124

Finally, let us assume, as in the theorem, that there is a smoo th manifold structure
on the orbit space Mξ =Gξ\µ−1(ξ) so that the orbit space projection πξ:µ−1(ξ) →Mξ is
a smooth submersion. Since ˜Ωξ is clearly Gξ invariant and closed and moreover, since its
null space at each point of M is precisely the tangent space to the ﬁbers of πξ, it follows
that there exists a unique “push down” 2-form Ω ξ onMξ as described in the statement of
the theorem. That Ω ξ is closed and non-degenerate is now immediate. □
The point of Theorem 2 is that, even though the quotient of a sy mplectic manifold
by a symplectic group action is not, in general, a symplectic manifold, there is a way to
produce a family of symplectic quotients parametrized by th e elements of the space g∗.
The quotients Mξ often turn out to be quite interesting, even when the origina l symplectic
manifold M is very simple.
Before I pass on to the examples, let me make a few comments abo ut the hypotheses
in Theorem 2.
First, there will always be clean values ξ of µ for which µ−1(ξ) is not empty (even
when there are no such regular values). This follows because , if we look at the closed
subset Dµ ⊂ M consisting of points m where µ′(m) does not reach its maximum rank,
then µ
(
Dµ) can be shown (by a sort of Sard’s Theorem argument) to be a pro per subset
of µ(M ). Meanwhile, it is not hard to show that any element ξ ∈µ(M ) that does not lie
in µ
(
Dµ) is clean.
Second, it quite frequently does happen that the Gξ-orbit space Mξ has a manifold
structure for which πξ is a submersion. This can be guaranteed by various hypothese s that
are often met with in practice. For example, if Gξ is compact and acts freely on µ−1(ξ),
thenMξ will be a manifold. (More generally, if the orbits Gξ ·m are compact and all of the
stabilizer subgroups Gm ⊂Gξ are conjugate in Gξ, then Mξ will have a manifold structure
of the required kind.)
Weaker hypotheses also work. Basically, one needs to know th at, at every point m
of µ−1(ξ), there is a smooth slice to the action of Gξ, i.e., a smoothly embedded disk D
in µ−1(ξ) that passes through m and intersects each Gξ-orbit in Gξ ·D transversely and
in exactly one point. (Compare the construction of a smooth s tructure on each G-orbit in
Theorem 1 of Lecture 3.)
Even when there is not a slice around each point of µ−1(ξ), there is very often a near-
slice, i.e., a smoothly embedded disk D in µ−1(ξ) that passes through m and intersects
each Gξ-orbit in Gξ ·D transversely and in a ﬁnite number of points. In this case, th e
quotient space Mξ inherits the structure of a symplectic orbifold, and these ‘generalized
manifolds’ have turned out to be quite useful.
Finally, it is worth computing the dimension of Mξ when it does turn out to be a
manifold. Let Gm ⊂ G be the stabilizer of m ∈ µ−1(ξ). I leave as an exercise for the
reader to check that
dim Mξ = dim M − dim G − dim Gξ + 2 dimGm
= dim M − 2 dim G/Gm + dim G/Gξ.
L.7.8 125

Since we will see so many examples in the next Lecture, I will c ontent myself with
only mentioning two here:
• LetM =T ∗G and let G act on T ∗G on the left in the obvious way. Then the reader
can easily check that, for each x ∈ g, we have ρ(x)(α) = α
(
Yx(a)
)
for all α ∈T ∗
aG where,
as usual, Yx denotes the right invariant vector ﬁeld on G whose value at e isx ∈ g. Hence,
µ:T ∗G → g∗ is given by µ(α) = R∗
π(α)(α).
Consequently,µ−1(ξ) ⊂T ∗G is merely the graph in T ∗G of the left-invariant 1-form
ωξ (i.e., the left-invariant 1-form whose value at e is ξ ∈ g∗). Thus, we can use ωξ as a
section of T ∗G to pull back Ω (the canonical symplectic form on T ∗G, which is clearly
G-invariant) to get the 2-form dωξ on G. As we already saw in Lecture 5, and is now
borne out by Theorem 2, the null space of dωξ at any point a ∈G is TaaGξ, the quotient
byGξ is merely the coadjoint orbit G/Gξ, and the symplectic structure Ω ξ is just the one
we already constructed.
Note, by the way, that every value of µ is clean in this example (in fact, they are all
regular), even though the dimensions of the quotients G/Gξ vary with ξ.
• Let G = SO(3) act on R6 =T ∗R3 by the extension of rotation about the origin in
R3. Then, in standard coordinates ( x,y ) (where x,y ∈ R3), the action is simply g · (x,y ) =
(gx,gy ), and the symplectic form is Ω = dx ·dy = tdx∧dy.
We can identify so(3)∗ with so(3) itself by interpreting a ∈ so(3) as the linear func-
tional b ↦→ −tr(ab). It is easy to see that the co-adjoint action in this case get s identiﬁed
with the adjoint action.
We compute that ρ(a)(x,y ) = −txay, so it follows without too much diﬃculty that,
with respect to our identiﬁcation of so(3)∗ with so(3), we have µ(x,y ) = xty −ytx.
The reader can check that all of the values of µ are clean except for 0 ∈ so(3). Even
this value would be clean if, instead of taking M to be all of R6, we let M be R6 minus
the origin (x,y ) = (0, 0).
I leave it to the reader to check that the G-invariant map P : R6 → R3 deﬁned by
P (x,y ) = (x ·x, x·y, y·y)
maps the set µ−1(0) onto the “cone” consisting of those points ( a,b,c ) ∈ R3 with a,c ≥ 0
and b2 =ac and the ﬁbers of P are the G0-orbits of the points in µ−1(0).
Forξ ⁄= 0, the P -image of the set µ−1(ξ) is one nappe of the hyperboloid of two sheets
described as ac −b2 = −tr(ξ2). The reader should compute the area forms Ω ξ on these
sheets.
L.7.9 126

Exercise Set 7:
Classical Reduction
1. Let M be the torus R2/Z2 and let dx and dy be the standard 1-forms on M . Let
Ω = dx∧dy. Show that the “translation action” ( a,b ) · [x,y ] = [x +a,y +b] of R2 onM is
symplectic but not Hamiltonian.
2. Let (M, Ω) be a connected symplectic manifold and let λ:G×M →M be a Hamiltonian
group action.
(i) Prove that, if ρ: g → C∞(M ) is a linear mapping that satisﬁes λ∗(x)
Ω = d
(
ρ(x)
)
,
then λ∗
(
[x,y ]
)
Ω = d
(
{ρ(x),ρ (y)}
)
.
(ii) Show that the associated linear mapping cρ: g × g → R deﬁned in the text does indeed
satisfy cρ
(
[x,y ],z
)
+cρ
(
[y,z ],x
)
+cρ
(
[z,x ],y
)
= 0 for all x,y,z ∈ g. (Hint: Use the
fact the Poisson bracket satisﬁes the Jacobi identity and th at the Poisson bracket of
a constant function with any other function is zero.)
3. Lie Algebra Cohomology. The purpose of this exercise is to acquaint the reader
with the rudiments of Lie algebra cohomology.
The Lie bracket of a Lie algebra g can be regarded as a linear map ∂: Λ 2(g) → g.
The dual of this linear map is a map −δ: g∗ → Λ 2(g∗). (Thus, for ξ ∈ g∗, we have
δξ(x,y ) = −ξ
(
[x,y ]
)
.) This map δ can be extended uniquely to a graded, degree-one
derivationδ: Λ ∗(g∗) → Λ ∗(g∗).
(i) For any c ∈ Λ 2(g∗), show that δc(x,y,z ) = −c
(
[x,y ],z
)
−c
(
[y,z ],x
)
−c
(
[z,x ],y
)
.
(Hint: Every c ∈ Λ 2(g∗) is a sum of wedge products ξ∧η where ξ,η ∈ g∗.) Conclude
that the Jacobi identity in g is equivalent to the condition that δ2 = 0 on all of Λ ∗(g∗).
Thus, for any Lie algebra g, we can deﬁne the k’th cohomology group of g, denoted Hk(g),
as the kernel of δ in Λ k(g∗) modulo the subspace δ
(
Λk−1(g∗)
)
.
(ii) Let G be a Lie group whose Lie algebra is g. For each Φ ∈ Λk(g∗), deﬁne ωΦ to be the
left-invariantk-form on G whose value at the identity is Φ. Show that dωΦ = ωδΦ .
(Hint: the space of left-invariant forms on G is clearly closed under exterior derivative
and is generated over R by the left-invariant 1-forms. Thus, it suﬃces to prove this
formula for Φ of degree 1. Why?)
Thus, the cohomology groups Hk(g) measure “closed-mod-exact” in the space of left-
invariant forms on G. If G is compact, then these cohomology groups are isomorphic to
the corresponding deRham cohomology groups of the manifold G.
(iii) (The Whitehead Lemmas) Show that if the Killing form of g is non-degenerate,
then H 1(g) = H 2(g) = 0. (Hint: You should have already shown that if κ is non-
degenerate, then [ g, g] = g. Show that this implies that H 1(g)=0. Next show that for
Φ ∈ Λ 2(g∗), we can write Φ( x,y ) = κ(Lx,y ) where L: g → g is skew-symmetric. Then
show that if δΦ = 0, then L is a derivation of g. Now see Exercise 3.3, part (iv).)
E.7.1 127

4. Homogeneous Symplectic Manifolds. Suppose that (M, Ω) is a symplectic mani-
fold and suppose that there exists a transitive symplectic a ctionλ:G ×M →M whereG is
a group whose Lie algebra satisﬁes H 1(g) = H 2(g) = 0. Show that there is a G-equivariant
symplectic covering map π:M → G/Gξ for some ξ ∈ g∗. Thus, up to passing to covers,
the only symplectic homogeneous spaces of a Lie group satisf ying H 1(g) = H 2(g) = 0 are
the coadjoint orbits. This result is usually associated wit h the names Kostant, Souriau,
and Symes.
(Hint: Since G acts homogeneously on M , it follows that, as G-spaces,M =G/H for
some closed subgroup H ⊂G that is the stabilizer of a point m of M . Let φ:G →M be
φ(g) = g ·m. Now consider the left-invariant 2-form φ∗(Ω) on G in light of the previous
Exercise. Why do we also need the hypothesis that H 1(g) = 0?)
I warn the reader that this characterization of homogeneous symplectic spaces is some-
times misquoted. Either the covering ambiguity is overlook ed or else, instead of hypotheses
about the cohomology groups, sometimes compactness is assu med, either for M orG. The
example of S1 ×S1 acting on itself and preserving the bi-invariant area form s hows that
compactness is not generally helpful. Here is an example tha t shows that you must allow
for the covering possibility: Let H ⊂ SL(2, R) be the subgroup of diagonal matrices with
positive entries on the diagonal. Then SL(2 , R)/H has an SL(2 , R)-invariant area form,
but it double covers the associated coadjoint orbit.
5. Verify the claim made in the text that, if there exists a G-invariant 1-form ω on M so
that dω = Ω, then the formula ρ(x) = −ω
(
λ∗(x)
)
yields a lifting ρ for which cρ = 0.
6. Show that if R2 acts on itself by translation then, with respect to the stand ard area
form Ω = dx∧dy, this action is Hamiltonian but not Poisson.
7. Verify the claim made in the proof of Theorem 1 that the follo wing identity holds for
all a ∈G, all y ∈ g, and all m ∈M :
λ′
a
(
λ∗(y)(m)
)
=λ∗
(
Ad(a)y
)
(a ·m).
8. Matrix Calculations. The purpose of this exercise is to let you get some practice
in a case where everything can be written out in coordinates.
Let G = GL( n, R) and let Q: gl(n, R) → R be a non-degenerate quadratic form.
Show that if we use the inclusion mapping x: GL(n, R) → Mn×n as a coordinate chart,
then, in the associated canonical coordinates ( x,p ), the Lagrangian L takes the form
L = 1
2 ⟨x−1p,x −1p⟩Q. Show also that ωL = ⟨x−1p,x −1dx⟩Q.
Now compute the expression for the momentum mapping µ and the Euler-Lagrange
equations for motion under the Lagrangian L. Show directly that µ is constant on the
solutions of the Euler-Lagrange equations.
Suppose that Q is Ad-invariant, i.e., Q
(
Ad(g)(x)
)
= Q(x) for all g ∈ G and x ∈ g.
Show that the constancy of µ is equivalent to the assertion that px −1 is constant on the
E.7.2 128

solutions of the Euler-Lagrange equations. Show that, in th is case, the L-critical curves in
G are just the curves γ(t) = γ0etv where γ0 ∈G and v ∈ g are arbitrary.
Finally, repeat all of these constructions for the general L ie group G, translating
everything into invariant notation (as opposed to matrix no tation).
9. Euler’s Equation. Look back over the example given in the Lecture of left-invar iant
metrics on Lie groups. Suppose that γ: R → G is an L-critical curve. Deﬁne ξ(t) =
τQ
(
ω( ˙γ(t))
)
. Thus, ξ: R → g∗. Show that the image of ξ lies on a single coadjoint orbit.
Moreover, show that ξ satisﬁes Euler’s Equation:
˙ξ + ad∗(
τ −1
Q (ξ)
)
(ξ) = 0.
The reason Euler’s Equation is so remarkable is that it only i nvolves ‘half of the
variables’ of the curve ˙γ in TG .
Once a solution to Euler’s Equation is found, the equation fo r ﬁnding the original
curve γ is just ˙γ = L′
γ
(
τ −1
Q (ξ)
)
, which is a Lie equation for γ and hence is amenable to
Lie’s method of reduction.
Actually more is true. Show that, if we set ξ(0) = ξ0, then the equation Ad ∗(γ)(ξ) = ξ0
determines the solution γ of the Lie equation with initial condition γ(0) = e up to right
multiplication by a curve in the stabilizer subgroup Gξ0 . Thus, we are reduced to solving
a Lie equation for a curve in Gξ0 . (It may be of some interest to note that the stabilizer
of the generic element η ∈ g∗ is a solvable group. Of course, for such η, the corresponding
Lie equation can be solved by quadratures.)
10. Project: Analysis of the Rigid Body in R3. Go back to the example of the
motion of a rigid body in R3 presented in Lecture 4. Use the information provided in
the previous two Exercises to show that the equations of moti on for a free rigid body
are integrable by quadratures. You will want to ﬁrst compute the coadjoint action and
describe the coadjoint orbits and their stabilizers.
11. Verify that, under the hypotheses of Theorem 2, the dimensi on of the reduced space
Mξ is given by the formula
dim Mξ = dim M − dim G − dim Gξ + 2 dimGm
where Gm is the stabilizer of any m ∈µ−1(ξ).
(Hint: Show that for any m ∈µ−1(ξ), we have
dim Tmµ−1(ξ) + dim Tm
(
G ·m
)
= dim M
and then do some arithmetic.)
12. In the reduction process, what is the relationship between Mξ and MAd∗(g)(ξ)?
E.7.3 129

13. Suppose that λ:G ×M → M is a Poisson action and that Y is a symplectic vector
ﬁeld on M that is G-invariant. Then according to Proposition 1, Y is tangent to each
of the submanifolds µ−1(ξ) (when ξ is a clean value of µ). Show that, when the sym-
plectic quotient Mξ exists, then there exists a unique vector ﬁeld Yξ on Mξ that satisﬁes
Yξ
(
πξ(m)
)
= π′
ξ
(
Y (m)
)
. Show also that Yξ is symplectic. Finally show that, given an
integral curve γ: R →Mξ of Yξ, then the problem of lifting this to an integral curve of Y
is reducible by “ﬁnite” operations to solving a Lie equation for Gξ.
This procedure is extremely helpful for two reasons: First, sinceMξ is generally quite
a bit smaller than M , it should, in principle, be easier to ﬁnd integral curves of Yξ than
integral curves of Y . For example, if Mξ is two dimensional, then Yξ can be integrated
by quadratures (Why?). Second, it very frequently happens t hat Gξ is a solvable group.
As we have already seen, when this happens the “lifting probl em” can be integrated by (a
sequence of) quadratures.
E.7.4 130

Lecture 8:
Recent Applications of Reduction
In this Lecture, we will see some examples of symplectic redu ction and its generaliza-
tions in somewhat non-classical settings.
In many cases, we will be concerned with extra structure on M that can be carried
along in the reduction process to produce extra structure on Mξ. Often this extra structure
takes the form of a Riemannian metric with special holonomy, so we begin with a short
review of this topic.
Riemannian Holonomy . LetMn be a connected and simply connected n-manifold,
and let g be a Riemannian metric on M . Associated to g is the notion of parallel transport
along curves. Thus, for each (piecewise C1) curveγ: [0, 1] →M , there is associated a linear
mapping Pγ:Tγ(0)M → Tγ(1)M , called ‘parallel transport along γ’, which is an isometry
of vector spaces and which satisﬁes the conditions P¯γ =P −1
γ and Pγ2γ1 =Pγ2 ◦Pγ1 where
¯γ is the path deﬁned by ¯γ(t) = γ(1 −t) and γ2γ1 is deﬁned only when γ1(1) = γ2(0) and,
in this case, is given by the formula
γ2γ1(t) =
{ γ1(2t) for 0 ≤t ≤ 1
2 ,
γ2(2t − 1) for 1
2 ≤t ≤ 1.
These properties imply that, for any x ∈M , the set of linear transformations of the form Pγ
where γ(0) = γ(1) = x is a subgroup Hx ⊂ O(TxM ) and that, for any other point y ∈M ,
we have Hy =PγHxP¯γ where γ: [0, 1] →M satisﬁes γ(0) = x and γ(1) = y. Because we
are assuming that M is simply connected, it is easy to show that Hx is actually connected
and hence is a subgroup of SO( TxM ).
´Elie Cartan was the ﬁrst to deﬁne and study Hx. He called it the holonomy ofg atx.
He assumed that Hx was always a closed Lie subgroup of SO( TxM ), a result that was only
later proved by Borel and Lichnerowitz (see [KN]).
Georges de Rham, a student of Cartan, proved that, if there is a splitting TxM =
V1 ⊕V2 that remains invariant under all the action of Hx, then, in fact, the metric g is
locally a product metric in the following sense: The metric g can be written as a sum of the
formg =g1 +g2 in such a way that, for every point y ∈M there exists a neighborhood U
ofy, a coordinate chart ( x1,x 2):U → Rd1 × Rd2 , and metrics ¯gi on Rdi so that gi =x∗
i (¯gi).
He also showed that in this reducible case the holonomy group Hx is a direct product
of the form H 1
x ×H 2
x where Hi
x ⊂ SO(Vi). Moreover, it turns out (although this is not
obvious) that, for each of the factor groups Hi
x, there is a submanifold Mi ⊂ M so that
TxMi =Vi and so that Hi
x is the holonomy of the Riemannian metric gi on Mi.
From this discussion it follows that, in order to know which s ubgroups of SO(n) can
occur as holonomy groups of simply connected Riemannian man ifolds, it is enough to ﬁnd
the ones that, in addition, act irreducibly on Rn. Using a great deal of machinery from the
theory of representations of Lie groups, M. Berger [Ber] det ermined a relatively short list
L.8.1 131

of possibilities for irreducible Riemannian holonomy grou ps. This list was slightly reduced
a few years later, independently by Alexseevski and by Brown and Gray. The result of
their work can be stated as follows:
Theorem 1: Suppose that g is a Riemannian metric on a connected and simply connected
n-manifold M and that the holonomy Hx acts irreducibly on TxM for some (and hence
every) x ∈ M . Then either (M,g ) is locally isometric to an irreducible Riemannian
symmetric space or else there is an isometry ι:TxM → Rn so that H =ιHxι−1 is one of
the subgroups of SO(n) in the following table.
Irreducible Holonomies of Non-Symmetric Metrics
Subgroup Conditions Geometrical Type
SO(n) anyn generic metric
U(m) n = 2m> 2 K¨ ahler
SU(m) n = 2m> 2 Ricci-ﬂat K¨ ahler
Sp(m)Sp(1) n = 4m> 4 Quaternionic K¨ ahler
Sp(m) n = 4m> 4 hyperK¨ ahler
G2 n = 7 Associative
Spin(7) n = 8 Cayley
A few words of explanation and comment about Theorem 1 are in o rder.
First, a Riemannian symmetric space is a Riemannian manifol d diﬀeomorphic to a
homogeneous space G/H where H ⊂G is essentially the ﬁxed subgroup of an involutory
homomorphismσ:G →G that is endowed with a G-invariant metricg that is also invariant
under the involution ι:G/H →G/H deﬁned by ι(aH) = σ(a)H. The classiﬁcation of the
Riemannian symmetric spaces reduces to a classiﬁcation pro blem in the theory of Lie
algebras and was solved by Cartan. Thus, the Riemannian symm etric spaces may be
regarded as known.
Second, among the holonomies of non-symmetric metrics list ed in the table, the ranges
for n have been restricted so as to avoid repetition or triviality . Thus, U(1) = SO(2) and
SU(1) = {e} while Sp(1) = SU(2), and Sp(1)Sp(1) = SO(4).
Third, according to S. T. Yau’s celebrated proof of the Calab i Conjecture, any compact
complex manifold for which the canonical bundle is trivial a nd that has a K¨ ahler metric
also has a Ricci-ﬂat K¨ ahler metric (see [Bes]). For this rea son, metrics with holonomy
SU(m) are often referred to as Calabi-Yau metrics.
Finally, I will not attempt to discuss the proof of Theorem 1 i n these notes. Even
with modern methods, the proof of this result is non-trivial and, in any case, would take
us far from our present interests. Instead, I will content my self with the remark that it
is now known that every one of these groups does, in fact, occu r as the holonomy of a
Riemannian metric on a manifold of the appropriate dimensio n. I refer the reader to [Bes]
for a complete discussion.
L.8.2 132

We will be particularly interested in the K¨ ahler and hyperK ¨ ahler cases since these
cases can be characterized by the condition that the holonom y of g leaves invariant certain
closed non-degenerate 2-forms. Hence these cases represen t symplectic manifolds with
“extra structure”, namely a compatible metric.
The basic result will be that, for a manifold M that carries one of these two structures,
there is a reduction process that can be applied to suitable g roup actions onM that preserve
the structure.
K¨ ahler Manifolds and Algebraic Geometry .
In this section, we give a very brief introduction to K¨ ahler manifolds. These are
symplectic manifolds that are also complex manifolds in suc h a way that the complex
structure is “maximally compatible” with the symplectic st ructure. These manifolds arise
with great frequency in Algebraic Geometry, and it is beyond the scope of these Lectures
to do more than make an introduction to their uses here.
Hermitian Linear Algebra. As usual, we begin with some linear algebra. Let
H: Cn × Cn → C be the hermitian inner product given by
H(z,w ) = t¯zw = ¯z1w1 + · · · + ¯znwn.
Then U(n) ⊂ GL(n, C) is the group of complex linear transformations of Cn that pre-
serveH since H(Az,Aw ) = H(z,w ) for all z,w ∈ Cn if and only if t ¯AA =In.
Now,H can be split into real and imaginary parts as
H(z,w ) = ⟨z,w ⟩ +ı Ω(z,w ).
It is clear from the relation H(z,w ) =
H(w,z ) that ⟨, ⟩ is symmetric and Ω is skew-
symmetric. I leave it to the reader to show that ⟨, ⟩ is positive deﬁnite and that Ω is
non-degenerate.
Moreover, since H(z,ıw ) = ıH (z,w ), it also follows that Ω( z,w ) = ⟨ız,w ⟩ and
⟨z,w ⟩ = Ω( z,ıw ). It easily follows from these equations that, if we let J: Cn → Cn
denote multiplication by ı, then knowing any two of the three objects ⟨, ⟩, Ω, or J on R2n
determines the third.
Deﬁnition 1: Let V be a vector space over R. A non-degenerate 2-form Ω on V and
a complex structure J:V → V are said to be compatible if Ω( x,Jy ) = Ω( y,Jx ) for all
x,y ∈ V . If the pair (Ω ,J ) is compatible, then we say that the pair forms an Hermitian
structure on V if, in addition, Ω( x,Jx )> 0 for all non-zero x ∈V . The positive deﬁnite
quadratic form g(x,x ) = Ω( x,Jx ) is called the associated metric on V .
I leave as an exercise for the reader the task of showing that a ny two Hermitian
structures on V are isomorphic via some invertible endomorphism of V .
It is easy to show that, if g is the quadratic form associated to a compatible pair
(
Ω,J
)
,
then Ω( v,w ) = g(Jv,w ). It follows that any two elements of the triple
(
Ω,J,g
)
determine
the third.
L.8.3 133

In an extension of the notion of compatibility, we deﬁne a qua dratic form g on V to
be compatible with a non-degenerate 2-form Ω on V if the linear map J:V →V deﬁned
by the relation Ω( v,w ) = g(Jv,w ) satisﬁes J 2 = −1. Similarly, we deﬁne a quadratic form
g onV to be compatible with a complex structure J onV ifg(Jv,w ) = −g(Jw,v ), so that
Ω(v,w ) = g(Jv,w ) deﬁnes a 2-form on V .
Almost Hermitian Manifolds. Since our main interest is in symplectic and com-
plex structures, I will introduce the notion of an almost Her mitian structure on a manifold
in terms of its almost complex and almost symplectic structu res:
Deﬁnition 2: Let M 2n be a manifold. A 2-form Ω and an almost complex structure J
deﬁne an almost Hermitian structure on M if, for each m ∈M , the pair (Ω m,Jm) deﬁnes
a Hermitian structure on TmM .
When (Ω ,J ) deﬁnes an almost Hermitian structure on M , the Riemannian metric g
on M deﬁned by g(v) = Ω( v,Jv ) is called the associated metric.
Just as one must place conditions on an almost symplectic str ucture in order to get a
symplectic structure, there are conditions that an almost c omplex structure must satisfy
in order to be a complex structure.
Deﬁnition 3: An almost complex structure J onM 2n is integrable if each point ofM has a
neighborhoodU on which there exists a coordinate chart z:U → Cn so thatz′(Jv ) = ız ′(v)
for all v ∈TU . Such a coordinate chart is said to be J-holomorphic.
According to the Korn-Lichtenstein theorem, when n = 1 all almost complex struc-
tures are integrable. However, for n ≥ 2, one can easily write down examples of almost
complex structures J that are not integrable. (See the Exercises.)
When J is an integrable almost complex structure on M , the set
UJ = {(U,z ) | z:U → Cn is J-holomorphic}
forms an atlas of charts that are holomorphic on overlaps. Th us, UJ deﬁnes a holomorphic
structure on M .
The reader may be wondering just how one determines whether a n almost complex
structure is integrable or not. In the Exercises, you are ask ed to show that, for an integrable
almost complex structure J , the identity LJXJ −J ◦LXJ = 0 must hold for all vector ﬁelds
X on M . It is a remarkable result, due to Newlander and Nirenberg, t hat this condition
is suﬃcient for J to be integrable.
◮ The reason that I mention this condition is that it shows that integrability is deter-
mined by J and its ﬁrst derivatives in any local coordinate system. Thi s condition can be
rephrased as the condition that the vanishing of a certain te nsor NJ , called the Nijenhuis
tensor of J and constructed out of the ﬁrst-order jet of J at each point, is necessary and
suﬃcient for the integrability of J.
We are now ready to name the various integrability condition s that can be deﬁned for
an almost Hermitian manifold.
L.8.4 134

Deﬁnition 4: We call an almost Hermitian pair (Ω ,J ) on a manifold M almost K¨ ahler
if Ω is closed, Hermitian if J is integrable, and K¨ ahlerif Ω is closed and J is integrable.
We already saw in Lecture 6 that a manifold has an almost compl ex structure if and
only if it has an almost symplectic structure. However, this relationship does not, in
general, hold between complex structures and symplectic st ructures.
Example: Here is a complex manifold that has no symplectic structure. Let Z act on
M = C2\{0} byn ·z = 2nz. This free action preserves the standard complex structure on
M . Let N = Z\ ˜M , then, via the quotient mapping, N inherits the structure of a complex
manifold.
However,N is diﬀeomorphic to S1 ×S3 as a smooth manifold. Thus N is a compact
manifold satisfying H 2
dR(N, R) = 0. In particular, by the cohomology ring obstruction
discussed in Lecture 6, we see that M cannot be given a symplectic structure.
Example: Here is an example due to Thurston, of a compact 4-manifold th at has a
complex structure and has a symplectic structure, but has no K¨ ahler structure.
LetH3 ⊂ GL(3, R) be the Heisenberg group, deﬁned in Lecture 2 as the set of mat rices
of the form
g =


1 x z + 1
2xy
0 1 y
0 0 1

.
The left invariant forms and their structure equations on H3 are easily computed in these
coordinates as
ω1 =dx
ω2 =dy
ω3 =dz − 1
2 (xdy −ydx )
dω1 = 0
dω2 = 0
dω3 = −ω1 ∧ω2
Now, let Γ = H3 ∩ GL(3, Z) be the subgroup of H3 consisting of those elements of H3 all
of whose entries are integers. Let X = Γ \H3 be the space of right cosets of Γ. Since the
forms ωi are left-invariant, it follows that they are well-deﬁned on X and form a basis for
the 1-forms on X.
Now let M =X ×S1 and let ω4 =dθ be the standard 1-form on S1. Then the forms
ωi for 1 ≤ i ≤ 4 form a basis for the 1-forms on M . Since dω4 = 0, it follows that the
2-form
Ω = ω1 ∧ω3 +ω2 ∧ω4
is closed and non-degenerate on M . Thus, M has a symplectic structure.
Next, I want to construct a complex structure on M . In order to do this, I will
produce the appropriate local holomorphic coordinates on M . Let ˜M = H3 × R be the
simply connected cover of M with coordinates ( x,y,z,θ ). We regard ˜M as a Lie group.
Deﬁne the functions w1 =x +ıy and w2 =z +ı
(
θ + 1
4 (x2 +y2)
)
on ˜M . Then I leave to
the reader to check that, if g0 is the element of ˜M with coordinates (x0,y 0,z 0,θ 0), then
L∗
g0(w1) = w1 +w1
0 and L∗
g0 (w2) = w2 +
(
ı/2
)
¯w1
0w1 +w2
0.
L.8.5 135

Thus, the coordinates w1 andw2 deﬁne a left-invariant complex structure on ˜M . Since M
is obtained from ˜M by dividing by the obvious left action of Γ × Z, it follows that there is
a unique complex structure on M for which the covering projection is holomorphic.
Finally, we show that M cannot carry a K¨ ahler structure. Since Γ is a discrete
subgroup of H3, the projection H3 →X is a covering map. Since H3 = R3 as manifolds,
it follows that π1(X) = Γ. Moreover, X is compact since it is the image under the
projection of the cube in H3 consisting of those elements whose entries lie in the closed
interval [0, 1]. On the other hand, since [Γ , Γ] ≃ Z, it follows that Γ /[Γ, Γ] ≃ Z2. Thus,
H 1(M, Z) = H 1(X ×S1, Z) = Z2 ⊕ Z. From this, we get that H 1
dR(M, R) = R3. In
particular, the ﬁrst Betti number of M is 3. Now, it is a standard result in K¨ ahler
geometry that the odd degree Betti numbers of a compact K¨ ahl er manifold must be even
(for example, see [Ch]). Hence, M cannot carry any K¨ ahler metric.
Example: Because of the classiﬁcation of compact complex surfaces du e to Kodaira, we
know exactly which compact 4-manifolds can carry complex st ructures. Fernandez, Gotay,
and Gray [FGG] have constructed a compact, symplectic 4-man ifold M whose underlying
manifold is not on Kodaira’s list, thus, providing an exampl e of a compact symplectic
4-manifold that carries no complex structure.
The fundamental theorem relating the two “integrability co nditions” to the idea of
holonomy is the following one. We only give the idea of the pro of because a complete proof
would require the development of considerable machinery.
Theorem 2: An almost Hermitian structure (Ω,J ) on a manifold M is K¨ ahler if and
only if the form Ω is parallel with respect to the parallel transport of the ass ociated metric
g.
Proof: (Idea) Once the formulas are developed, it is not diﬃcult to see tha t the covariant
derivatives of Ω with respect to the Levi-Civita connection of g are expressible in terms
of the exterior derivative of Ω and the Nijenhuis tensor of J. Conversely, the exterior
derivative of Ω and the Nijenhuis tensor of J can be expressed in terms of the covariant
derivative of Ω with respect to the Levi-Civita connection o f g. Thus, Ω is covariant
constant (i.e., invariant under parallel translation with respect to g) if and only it is closed
and J is integrable. □
◮ It is worth remarking that J is invariant under parallel transport with respect to g if
and only if Ω is.
The reason for this is that J is determined from and determines Ω once g is ﬁxed.
The observation now follows, since g is invariant under parallel transport with respect to
its own Levi-Civita connection.
K¨ ahler Reduction.We are now ready to state the ﬁrst of the reduction theorems
we will discuss in this Lecture.
It turns out that it’s a good idea to discuss a special case ﬁrs t.
L.8.6 136

Theorem 3: K¨ahler Reduction at 0. Let (Ω,g ) be a K¨ ahler structure on M 2n.
Let λ:G ×M → M be a left action that is Poisson with respect to Ω and preserves the
metricg. Let µ:M → g∗ be the associated momentum mapping. Suppose that 0 ∈ g∗ is a
clean value of µ and that there is a smooth structure on the orbit space M0 =G\µ−1(0)
for which the natural projection π0 :µ−1(0) → G\µ−1(0) is a smooth submersion. Then
there is a unique K¨ ahler structure (Ω 0,g 0) on M0 deﬁned by the conditions that π∗
0(Ω 0)
be equal to the pullback of Ω toµ−1(0) ⊂M and that π0:µ−1(0) →M0 be a Riemannian
submersion.
Proof: Let ˜g0 and ˜Ω 0 be the pullbacks of g and Ω respectively to µ−1(0). By hypotheses,
˜g0 and ˜Ω 0 are invariant under the action of G.
From Theorem 2 of Lecture 7, we already know that there exists a unique symplectic
structure Ω 0 on M0 for which π∗
0(Ω 0) = ˜Ω 0.
Here is how we construct g0. For any m ∈µ−1(0), there is a well deﬁned ˜g0-orthogonal
splitting
Tmµ−1(0) = Tm
(
G ·m
)
⊕Hm
that is clearly G-invariant. Since, by hypothesis, π0:µ−1(0) → M0 is a submersion, it
easily follows that π′
0(m):Hm →Tπ0(m)M0 is an isomorphism of vector spaces. Moreover,
theG-invariance of ˜g shows that there is a well-deﬁned quadratic form g0(m) on Tπ0(m)M0
that corresponds to the restriction of ˜ g0 to Hm under this isomorphism. By the very
deﬁnition of Riemannian submersion, it follows that g0 is a Riemannian metric on M0 for
whichπ0 is a Riemannian submersion.
It remains to show that (Ω 0,g 0) deﬁnes a K¨ ahler structure on M0. First, we show
that it is an almost K¨ ahler structure, i.e., that Ω 0 and g0 are actually compatible. Since
π′
0(m):Hm → Tπ0(m)M0 is an isomorphism of vector spaces that identiﬁes (Ω 0,g 0) with
the restriction of (Ω ,g ) to Hm, it suﬃces to show that Hm is invariant under the action
of J.
Here is how we do this. Tracing back through the deﬁnitions, w e see that x ∈TmM
lies in the subspace Hm if and only if x satisﬁes both of the conditions Ω( x,y ) = 0 and
g(x,y ) = 0 for all y ∈Tm
(
G·m
)
. However, since Ω( x,y ) = g(Jx,y ) for all y, it follows that
the necessary and suﬃcient conditions that x lie in Hm can also be expressed as the two
conditionsg(Jx,y ) = 0 and Ω( Jx,y ) = 0 for all y ∈Tm
(
G·m
)
. Of course, these conditions
are exactly the conditions that Jx lie in Hm. Thus, x ∈ Hm implies that Jx ∈ Hm, as
desired.
Finally, in order to show that the almost K¨ ahler structure o n M0 is actually K¨ ahler,
it must be shown that Ω 0 is parallel with respect to the Levi-Civita connection of g0.
This is a straightforward calculation using the structure e quations and will not be done
here. (Alternatively, to prove that the structure is actual ly K¨ ahler, one could instead show
that the induced almost complex structure is integrable. Th is is somewhat easier and the
interested reader can consult the Exercises, where a proof i s outlined.) □
L.8.7 137

Now, it seems unreasonable to consider only reduction at 0 ∈ g∗. However, some
caution is in order because the na ¨ ıve attempt to generalize Theorem 3 to reduction at a
generalξ ∈ g∗ fails: Let λ :G×M →M be a Poisson action on a K¨ ahler manifold (M, Ω,g )
that preserves g and let µ : M → g∗ be a Poisson momentum mapping. Then for every
clean value ξ ∈ g∗ for which the orbit space Mξ =Gξ\µ−1(ξ) has a smooth structure that
makesπξ :µ−1(ξ) →Mξ a smooth submersion, there is a symplectic structure Ω ξ on Mξ
that is induced by reduction in the usual way. Moreover, ther e is a unique metric gξ onMξ
for which πξ is a Riemannian submersion (when µ−1(ξ) ⊂ M is given the induced sub-
manifold metric). Unfortunately, it is not, in general, true that gξ is compatible with Ω ξ.
(See the Exercises for an example.)
If you examine the proof given above in the general case, you’ ll see that the main
problem is that the ‘horizontal space’ Hm need not be stable under J. In fact, what one
knows in the general case is that Hm isg-orthogonal to both TmGξ·m and to J
(
TmG·m
)
.
However, when Gξ is a proper subgroup of G (i.e., when ξ is not a ﬁxed point of the co-
adjoint action), we won’t have TmGξ·m =TmG·m, which is what we needed in the proof
to show that Hm is stable under J.
In fact, the proof does work when Gξ =G, but this can be seen directly from the fact
that, in this case, the ‘shifted’ momentum mapping µξ =µ −ξ still satisﬁes G-equivariance
and we are simply performing reduction at 0 for the shifted mo mentum mapping µξ.
Reduction at K ¨ahler coadjoint orbits. Generalizing the case where G·ξ = {ξ},
there is a way to deﬁne K¨ ahler reduction at certain values of ξ ∈ g∗, by relying on the
‘shifting trick’ described in the Exercises of Lecture 7:
In many cases, a coadjoint orbit G·ξ ⊂ g∗ can be equipped with a G-invariant metrichξ
for which the pair (Ω ξ,hξ) deﬁnes a K¨ ahler structure on the orbit G·ξ. (For example, this
is always the case when G is compact.) In such a case, the shifting trick allows us to de ﬁne
a K¨ ahler metric onMξ =Gξ\µ−1(0) by doing K¨ ahler reduction at 0 on M ×G·ξ endowed
with the product K¨ ahler structure. In the cases in which the re is only one G-invariant
K¨ ahler metrichξ onG·ξ that is compatible with Ω ξ (and, again, this always holds when G
is compact), this deﬁnes a canonical K¨ ahler reduction proc edure for ξ ∈ g∗.
Example: K¨ahler reduction in Algebraic Geometry. By far the most com-
mon examples of K¨ ahler manifolds arise in Algebraic Geomet ry. Here is a sample of what
K¨ ahler reduction yields:
Let M = Cn+1 with complex coordinates z0,z 1,...,z n. We let zk =xk +ıyk deﬁne
real coordinates on M . Let G =S1 act on M by the rule
eıθ ·z =eıθz.
Then G clearly preserves the K¨ ahler structure deﬁned by the natur al complex structure
on M and the symplectic form
Ω = ı
2
tdz ∧d¯z =dx1 ∧dy1 + · · · +dxn ∧dyn.
The associated metric is easily seen to be just
g = tdz ◦d¯z =
(
dx1)2
+
(
dy1)2
+ · · · +
(
dxn)2
+
(
dyn)2
.
L.8.8 138

Now, setting X = ∂
∂θ , we can compute that
λ∗(X) = xk ∂
∂yk −yk ∂
∂xk.
Thus, it follows that
dρ(X) = λ∗(X) Ω = −xkdxk −ykdyk =d
(
− 1
2 |z|2)
.
Thus, identifying g∗ with R, we have that µ: Cn → R is merely µ(z) = − 1
2 |z|2.
It follows that every negative number is a non-trivial clean value for µ. For example,
S2n+1 = µ−1(− 1
2 ). Clearly G = S1 itself is the stabilizer subgroup of all of the values of
µ. Thus, M− 1
2
is the quotient of the unit sphere by the action of S1. Since each G-orbit
is merely the intersection of S2n+1 with a (unique) complex line through the origin, it is
clear that M− 1
2
is diﬀeomorphic to CPn.
Since the coadjoint action is trivial, reduction at ξ = − 1
2 will deﬁne a K¨ ahler struc-
ture on CPn. It is instructive to compute what this K¨ ahler structure lo oks like in local
coordinates. Let A0 ⊂ CPn be the subset consisting of those points [ z0,...,z n] for which
z0 ⁄= 0. Then A0 can be parametrized by φ : Cn → A0 whereφ(w) = [1,w ]. Now, over A0,
we can choose a section σ: A0 →S2n+1 by the rule
σ ◦φ(w) = (1,w )
W
where W 2 = 1 + |w1|2 + · · · + |wn|2> 0. It follows that
φ∗(Ω − 1
2
) = (σ ◦φ)∗(Ω) = ı
2
(
d
(wk
W
)
∧d
(¯wk
W
))
= ı
2
(dwk∧d ¯wk
W 2 + (wkd ¯wk − ¯wkdwk) ∧
dW
W 3
)
= ı
2
(W 2δjk − ¯wjwk
W 4
)
dwj ∧d ¯wk.
I leave it to the reader to check that the quotient metric (i.e ., the one for which the
submersion S2n+1 → CPn is Riemannian) is given by the formula
g− 1
2
=
(W 2δjk − ¯wjwk
W 4
)
dwj◦d ¯wk.
In particular, it follows that the functions wk are holomorphic functions with respect to
the induced almost complex structure, verifying directly t hat the pair (Ω − 1
2
,g − 1
2
) is indeed
a K¨ ahler structure onCPn. Up to a normalizing constant, this is the usual formula for t he
Fubini-Study K¨ ahler structure onCPn in an aﬃne chart.
L.8.9 139

Of course, the Fubini-Study metric induces a K¨ ahler struct ure on every complex sub-
manifold of CPn. However, we can just as easily see how this arises from the re duction
procedure: If P (z0,...,z n) is a non-zero homogeneous polynomial of degree d, then the
set ˜MP =P −1(0) ⊂ Cn+1 is a complex subvariety of Cn+1 that is invariant under the S1
action since, by homogeneity, we have
P (eıθ ·z) = eıdθP (z).
It is easy to show that if the variety ˜MP has no singularity other than 0 ∈ Cn+1, then the
K¨ ahler reduction of the K¨ ahler structure that it inherits from the standard structure on
Cn+1 is just the K¨ ahler structure on the corresponding projecti vized variety MP ⊂ CPn
that is induced by restriction of the Fubini-Study structur e.
“Example”: Flat Bundles over Compact Riemann Surfaces. The following
is not really an example of the theory as we have developed it s ince it will deal with
“inﬁnite dimensional manifolds”, however it is suggestive and the formal calculations yield
an interesting result. (For a review of the terminology used in this and the next example,
see the Appendix.)
LetG be a Lie group with Lie algebra g, and let ⟨, ⟩ be a positive deﬁnite, Ad-invariant
inner product on g. (For example, if G = SU(n), we could take ⟨x,y ⟩ = −tr(xy).)
Let Σ be a connected compact Riemann surface. Then there is a s tar operation
∗: A1(Σ) → A 1(Σ) that satisﬁes ∗2 = −id, and α∧∗α ≥ 0 for all 1-forms α on Σ.
Let P be a principal right G-bundle over Σ, and let Ad( P ) = P ×Ad g denote the
vector bundle over M associated to the adjoint representation Ad: G → Aut(g). Let
Aut(P ) denote the group of automorphisms of P , also known as the gauge group of P .
Let A(P ) denote the space of connections on P . Then it is well known that A(P )
is an aﬃne space modeled on the vector space A1(
Ad(P )
)
, which consists of the 1-forms
on M with values in Ad( P ). Thus, in particular, for every A ∈ A(P ), we have a natural
isomorphism
TAA(P ) = A1(
Ad(P )
)
.
I now want to deﬁne a “K¨ ahler” structure on A(P ). In order to do this, I will deﬁne
the metric g and the 2-form Ω .
First, for α ∈TAA(P ), I deﬁne
g(α) =
∫
Σ
⟨α, ∗α⟩.
(I extend the operator ∗ in the obvious way to A1(
Ad(P )
)
.) It is clear that g(α) ≥ 0 with
equality if and only if α = 0. Thus, g deﬁnes a “Riemannian metric” on A(P ). Since g is
“translation invariant”, it “follows” that g is “ﬂat”.
Second, I deﬁne Ω by the rule:
Ω (α,β ) =
∫
Σ
⟨α,β ⟩.
L.8.10 140

Since Ω (α,β ) = g(α, ∗β), it follows that Ω is actually non-degenerate. Moreover, because
Ω too is “translation invariant”, it “must” be “parallel” wit h respect to g.
Thus, ( Ω , g) is a “ﬂat K¨ ahler” structure on A(P ). Now, I claim that both Ω and g
are invariant under the natural right action of Aut(P ) on A(P ). To see this, note that an
elementφ ∈ Aut(P ) determines a map ϕ:P →G by the rule p ·ϕ(p) = φ(p) and that this
ϕ satisﬁes the identity ϕ(p ·g) = g−1ϕ(p)g. In terms of ϕ, the action of Aut(P ) on A(P )
is given by the classical formula
A ·φ =φ∗(A) = ϕ∗(ωG) + Ad
(
ϕ−1)
(A).
From this, it follows easily that Ω and g are Aut(P )-invariant.
Now, I want to compute the momentum mappping µ . The Lie algebra of Aut(P ),
namely aut(P ), can be naturally identiﬁed with A0(
Ad(P )
)
, the space of sections of the
bundle Ad(P ). I leave to the reader the task of showing that the induced ma p from
aut(P ) to vector ﬁelds on A(P ) is given by dA: A0(
Ad(P )
)
→ A 1(
Ad(P )
)
. Thus, in order
to construct the momentum mapping, we must ﬁnd, for each f ∈ A 0(
Ad(P )
)
, a function
ρ (f ) on A so that the 1-form dρ (f ) is given by
dρ (f )(α) = dAf Ω (α) =
∫
Σ
⟨dAf,α ⟩ = −
∫
Σ
⟨f,dAα⟩.
However, this is easy. We just set
ρ (f )(A) = −
∫
Σ
⟨f,FA⟩
and the reader can easily check that
d
dt
⏐
⏐
⏐
t=0
(ρ (f )(A +tα)) = −
∫
Σ
⟨f,dAα⟩
as desired. Finally, using the natural isomorphism
(
aut(P )
)∗
=
(
A0(
Ad(P )
))∗
= A2(
Ad(P )
)
,
we see that (up to sign) the formula for the momentum mapping s imply becomes
µ (A) = FA =dA + 1
2 [A,A ].
Now, can we do reduction? What we need is a clean value of µ . As a reasonable ﬁrst
guess, let’s try 0. Thus, µ −1(0) consists exactly of the ﬂat connections on P and the reduced
space M0 should be the ﬂat connections modulo gauge equivalence, i.e ., µ −1(0)/Aut(P ).
How can we tell whether 0 is a clean value? One way to know this w ould be to know
that 0 is a regular value. We have already seen that µ ′(A)(α) = dAα, so we are asking
L.8.11 141

whether the map dA: A1(
Ad(P )
)
→ A 2(
Ad(P )
)
is surjective for any ﬂat connection A.
Now, because A is ﬂat, the sequence
0 − → A0(
Ad(P )
)dA
− → A1(
Ad(P )
)dA
− → A2(
Ad(P )
)
− →0
forms a complex and the usual Hodge theory pairing shows that H 2(Σ,dA) is the dual
space of H 0(Σ,dA). Thus, µ ′(A) is surjective if and only if H 0(Σ,dA) = 0. Now, an
element f ∈ A 0(
Ad(P )
)
that satisﬁes dAf = 0 exponentiates to a 1-parameter family
of automorphisms of P that commute with the parallel transport of A. I leave to the
reader to show that H 0(Σ,dA) ⁄= 0 is equivalent to the condition that the holonomy group
HA(p) ⊂G has a centralizer of positive dimension in G for some (and hence every) point
of P . For example, for G = SU(2), this would be equivalent to saying that the holonomy
groups HA(p) were each contained in an S1 ⊂G.
Let us let ˜M
∗
⊂ µ −1(0) denote the (open) subset consisting of those ﬂat connect ions
whose holonomy groups have at most discrete centralizers in G. If G is compact, of course,
this implies that these centralizers are ﬁnite. Then it “fol lows” that M∗
0 = ˜M
∗
/Aut(P )
is a K¨ ahler manifold wherever it is a manifold. (In general, at the connections where the
centralizer of the holonomy is trivial, one expects the quot ient to be a manifold.)
Since the space of ﬂat connections on P modulo gauge equivalence is well-known to
be identiﬁable as the space R
(
π1(Σ,s ),G
)
= Hom
(
π1(Σ,s ),G
)
/G of equivalence classes of
representation of π1(Σ) into G, our discussion leads us to believe that this space (which is
ﬁnite dimensional) should have a natural K¨ ahler structure on it. This is indeed the case,
and the geometry of this K¨ ahler metric is the subject of curr ent interest.
HyperK¨ ahler Manifolds.
In this section, we will generalize the K¨ ahler reduction pr ocedure to the case of man-
ifolds with holonomy Sp( m), the so-called hyperK¨ ahler case.
Quaternion Hermitian Linear Algebra. We begin with some linear algebra over
the ring H of quaternions. For our purposes, H can be identiﬁed with the vector space of
dimension 4 over R of matrices of the form
x =
(
x0 +ıx 1 x2 +ıx 3
−x2 +ıx 3 x0 −ıx 1
)
def
= x0 1 +x1i +x2j +x3k.
(We are identifying the 2-by-2 identity matrix with 1 in this representation.) It is easy to
see that H is closed under matrix multiplication. If we deﬁne ¯ x = x0 −x1i −x2j −x3k,
then we easily get
xy = ¯y ¯x and
x¯x =
(
(x0)2 + (x1)2 + (x2)2 + (x3)2)
1 = det(x) 1
def
= |x|2 1.
It follows that every non-zero element of H has a multiplicative inverse. Note that the
space of quaternions of unit norm, S3 deﬁned by |x| = 1, is simply SU(2).
L.8.12 142

Much of the linear algebra that works for the complex numbers can be generalized
to the quaternions. However, some care must be taken since H is not commutative. In
the following exposition, it turns out to be most convenient to deﬁne vector spaces over H
as right vector spaces instead of left vector spaces. Thus, the stand ard H-vector space of
H-dimension n is Hn (thought of as columns of quaternions of height n) where the action
of the scalars on the right is given by


x1
.
.
.
xn

 ·q =



x1q
.
.
.
xnq


.
With this convention, a quaternion linear map A: Hn → Hm, i.e., an additive map satisfying
A(vq ) = A(v)q, can be represented by an m-by-n matrix of quaternions acting via matrix
multiplication on the left.
Let H: Hn × Hn → H be the “quaternion Hermitian” inner product given by
H(z,w ) = t¯zw = ¯z1w1 + · · · + ¯znwn.
Then by our conventions, we have
H(zq,w ) = ¯qH (z,w ) and H(z,wq ) = H(z,w )q.
We also have H(z,w ) =
H(w,z ), just as before.
We deﬁne Sp(n) ⊂ GL(n, H) to be the group of H-linear transformations of Hn that
preserveH, i.e., H(Az,Aw ) = H(z,w ) for all z,w ∈ Hn. It is easy to see that
Sp(n) =
{
A ∈ GL(n, H) |t ¯AA =In
}
.
I leave as an exercise for the reader to show that Sp( n) is a compact Lie group of
dimension 2n2 +n. Also, it is not diﬃcult to show that Sp( n) is connected and acts
irreducibly on Hn. (see the Exercises)
NowH can be split into one real and three imaginary parts as
H(z,w ) = ⟨z,w ⟩ + Ω 1(z,w )i + Ω 2(z,w )j + Ω 3(z,w )k.
It is clear from the relations above that ⟨, ⟩ is symmetric and positive deﬁnite and that
each of the Ω a is skew-symmetric. Moreover, we have the following identit ies:
⟨z,w ⟩ = Ω 1(z,wi ) = Ω 2(z,wj ) = Ω 3(z,wk )
and
Ω 2(z,wi ) = Ω 3(z,w )
Ω 3(z,wj ) = Ω 1(z,w )
Ω 1(z,wk ) = Ω 2(z,w ).
L.8.13 143

Proposition 1: The subgroup of GL(4n, R) that ﬁxes the three 2-forms (Ω 1, Ω 2, Ω 3) is
equal to Sp(n).
Proof: Let G ⊂ GL(4n, R) be the subgroup that ﬁxes each of the Ω a. Clearly we have
Sp(n) ⊂G.
Now, from the ﬁrst of the identities above, it follows that ea ch of the forms Ω a is
non-degenerate. Then, from the second set of these identiti es, it follows that the subgroup
G must also ﬁx the linear transformations of R4n that represent multiplication on the right
by i, j, and k. Of course, this, by deﬁnition, implies that G is a subgroup of GL( n, H).
Returning to the ﬁrst of the identities, it also follows that G must preserve the inner
product deﬁned by ⟨, ⟩. Finally, since we have now seen that G must preserve all of the
components of H, it follows that G must preserve H as well. However, this was the very
deﬁnition of Sp( n). □
Proposition 1 motivates the way we will want to deﬁne HyperK¨ ahler structures on
manifolds: as triples of 2-forms that satisfy certain condi tions. Here is the linear algebra
deﬁnition on which the manifold deﬁnition will be based.
Deﬁnition 5: LetV be a vector space over R. A hyperK¨ ahler structureonV is a choice of
a triple of non-degenerate 2-forms (Ω 1, Ω 2, Ω 3) that satisfy the following properties: First,
the linear maps Ri, Rj that are deﬁned by the equations
Ω 2(v,Riw) = Ω 3(v,w ) Ω 1(v,Rjw) = −Ω 3(v,w )
satisfy
(
Ri
)2
=
(
Rj
)2
= −id and skew-commute, i.e., RiRj = −RjRi. Second, if we set
Rk = −RiRj, then
Ω 1(v,Riw) = Ω 2(v,Rjw) = Ω 3(v,Rkw) = ⟨v,w ⟩
where ⟨, ⟩ (which is deﬁned by these equations) is a positive deﬁnite sy mmetric bilinear
form on V . The inner product ⟨, ⟩ is called the associated metric on V .
This may seem to be a rather cumbersome deﬁnition (and I admit that it is), but it is
suﬃcient to prove the following Proposition (which I leave a s an exercise for the reader).
Proposition 2: If (Ω 1, Ω 2, Ω 3) is a hyperK¨ ahler structure on a real vector spaceV , then
dim(V ) = 4n for some n and, moreover, there is an R-linear isomorphism of V with Hn
that identiﬁes the hyperK¨ ahler structure on V with the standard one on Hn. □
We are now ready for the analogs of Deﬁnitions 3 and 4:
Deﬁnition 6: If M is a manifold of dimension 4 n, an almost hyperK¨ ahler structureon
M is a triple (Ω 1, Ω 2, Ω 3) of 2-forms on M that have the property that they induce a
hyperK¨ ahler structure on each tangent spaceTmM .
Deﬁnition 7: An almost hyperK¨ ahler structure (Ω 1, Ω 2, Ω 3) on a manifold M 4n is a
hyperK¨ ahler structure onM if each of the forms Ω a is closed.
L.8.14 144

At ﬁrst glance, Deﬁnition 7 may seem surprising. After all, i t appears to place no
conditions on the almost complex structures Ri,Rj, and Rk that are deﬁned on M by the
almost hyperK¨ ahler structure onM and one would surely want these to be integrable if
the analogy with K¨ ahler geometry is to be kept up. The nice re sult is that the integrability
of these structures comes for free:
Theorem 4: For an almost hyperK¨ ahler structure (Ω 1, Ω 2, Ω 3) on a manifold M 4n, the
following are equivalent:
(1) dΩ 1 =dΩ 2 =dΩ 3 = 0.
(2) Each of the 2-forms Ωa is parallel with respect to the Levi-Civita connection of th e
associated metric.
(3) Each of the almost complex structures Ri, Rj, and Rk are integrable.
Proof: (Idea) The proof of Theorem 4 is much like the proof of Theorem 2. One s hows
by local calculations in Gauss normal coordinates at any poi nt on M that the covariant
derivatives of the forms Ω a with respect to the Levi-Civita connection of the associate d
metric can be expressed in terms of the coeﬃcients of their ex terior derivatives and vice-
versa. Similarly, one shows that the formulas for the Nijenh uis tensors of the three almost
complex structures on M can be expressed in terms of the covariant derivatives of the
three 2-forms and vice-versa. This is a rather formidable li near algebra problem, but it is
nothing more. I will not do the computation here. □
Note that Theorem 4 implies that the holonomy H of the associated metric of a
hyperK¨ ahler structure onM 4n must be a subgroup of Sp( n). If H is a proper subgroup
of Sp(n), then by Theorem 1, the associated metric must be locally a p roduct metric. Now,
as is easy to verify, the only products from Berger’s List tha t can appear as subgroups
of Sp(n) are products of the form
{e}n0 × Sp(n1) × · · · × Sp(nk)
where {e}n0 ⊂ Sp(n0) is just the identity subgroup and n = n0 + · · · +nk. Thus, it
follows that a hyperK¨ ahler structure can be decomposed loc ally into a product of the ‘ﬂat’
example with hyperK¨ ahler structures whose holonomy is the full Sp(ni). (If M is simply
connected and the associated metric is complete, then the de Rham Splitting Theorem
asserts that M can be globally written as a product of such metrics.) This mo tivates our
calling a hyperK¨ ahler structure onM 4n irreducible if its holonomy is equal to Sp( n).
The reader may be wondering just how common these hyperK¨ ahl er structures are
(aside from the ﬂat ones of course). The answer is that they ar e not so easy to come by. The
ﬁrst known non-ﬂat example was the Eguchi-Hanson metric (of ten called a “gravitational
instanton”) on T ∗CP1. The ﬁrst known irreducible example in dimensions greater t han 4
was discovered by Eugenio Calabi, who, working independent ly from Eguchi and Hanson,
constructed an irreducible hyperK¨ ahler structure on T ∗CPn for each n that happened to
L.8.15 145

agree with the Eguchi-Hanson metric for n = 1. (We will see Calabi’s examples a little
further on.)
The ﬁrst known compact example was furnished by Yau’s soluti on of the Calabi Con-
jecture:
Example: K3 Surfaces. AK3 surface is a compact simply connected 2-dimensional
complex manifoldS with trivial canonical bundle. What this latter condition m eans is that
there is nowhere-vanishing holomorphic 2-form Υ on S. An example of such a surface is a
smooth algebraic surface of degree 4 in CP3.
A fundamental result of Siu [Si] is that every K3 surface is K¨ ahler, i.e., that there
exists a 2-form Ω on S so that the hermitian structure (Ω ,J ) on S is actually K¨ ahler.
Moreover, Yau’s solution of the Calabi Conjecture implies t hat Ω can be chosen so that Υ
is parallel with respect to the Levi-Civita connection of th e associated metric.
Multiplying Υ by an appropriate constant, we can arrange tha t 2 Ω 2 = Υ ∧Υ. Since
Ω ∧Υ = 0 and Υ ∧Υ = 0, it easily follows (see the Exercises) that if we write Ω = Ω 1 and
Υ = Ω 2 −ı Ω 3, then the triple (Ω 1, Ω 2, Ω 3) deﬁnes a hyperK¨ ahler structure on S.
For a long time, the K3 surfaces were the only known compact manifolds with hy-
perK¨ ahler structures. In fact, a “proof” was published sho wing that there were no other
compact ones. However, this turned out not to be correct.
Example: Let M 4n be a simply connected, compact complex manifold (of complex
dimension 2n) with a holomorphic symplectic form Υ. Then Υ n is a non-vanishing holo-
morphic volume form, and hence the canonical bundle of M is trivial. If M has a K¨ ahler
structure that is compatible with its complex structure, th en, by Yau’s solution of the
Calabi Conjecture, there is a K¨ ahler metric g on M for which the volume form Υ n is
parallel. This implies that the holonomy of g is a subgroup of SU(2 n). However, this in
turn implies that g is Ricci-ﬂat and hence, by a Bochner vanishing argument, tha t every
holomorphic form on M is parallel with respect to g. Thus, Υ is also parallel with respect
to g and hence the holonomy is a subgroup of Sp( n). If M can be constructed in such a
way that it cannot be written as a non-trivial product of comp lex submanifolds, then the
holonomy of g must act irreducibly on C2n and hence must equal Sp( n).
Fujita was the ﬁrst to construct a simply connected, compact complex 4-manifold that
carried a holomorphic 2-form and that could not be written no n-trivially as a product. This
work is written up in detail in a survey article by [Bea].
HyperK¨ ahler Reduction.I am now ready to describe another method of construct-
ing hyperK¨ ahler structures, known as hyperK¨ ahler reduction. This method ﬁrst appeared
in a famous paper by Hitchin, Karlhede, Lindstr¨ om, and Roˇ cek, [HKLR].
Theorem 5: Suppose that (Ω 1, Ω 2, Ω 3) is a hyperK¨ ahler structure onM and that there
is a left action λ:G ×M →M that is Poisson with respect to each of the three symplectic
forms Ωa. Let
µ = (µ1,µ 2,µ 3):M → g∗ ⊕ g∗ ⊕ g∗
L.8.16 146

be a G-equivariant momentum mapping. Suppose that 0 ∈ g∗ ⊕g∗ ⊕g∗ is a clean value for µ
and that the quotient M0 = G\µ−1(0) has a smooth structure for which the projection
π0:µ−1(0) →M0 is a smooth submersion. Then there is a unique hyperK¨ ahler s tructure
(Ω 0
1, Ω 0
2, Ω 0
3) on M0 with the property that π∗
0(Ω 0
a) is the pull back of Ωa to µ−1(0) ⊂M
for each a = 1, 2, or 3.
Proof: Assume the hypotheses of the Theorem. Let ˜Ω 0
a be the pullback of Ω a toµ−1(0) ⊂
M . It is clear that each of the forms ˜Ω 0
a is a closed, G-invariant 2-form on µ−1(0).
I ﬁrst want to show that each of these can be written as a pullba ck of a 2-form on
M0, i.e., that each is semi-basic for π0. To do this, I need to characterize Tmµ−1(0) in an
appropriate fashion. Now, the assumption that 0 be a clean va lue for µ implies µ−1(0) is
a smooth submanifold of M and that for m ∈ µ−1(0) any v ∈ TmM lies in Tmµ−1(0) if
and only if Ω a
(
v,λ ∗(x)(m)
)
= 0 for all x ∈ g and all three values of a. Thus,
Tmµ−1(0) = {v ∈TmM
⟨v,wi ⟩ = ⟨v,wj ⟩ = ⟨v,wk ⟩ = 0, for all w ∈TmG·m}.
Also, by G-equivariance, G·m ⊂ µ−1(0) and hence TmG·m ⊂ Tmµ−1(0). It follows that
v ∈TmG·m implies that v is in the null space of each of the forms ˜Ω 0
a. Thus, each of the
forms ˜Ω 0
a is semi-basic for π0, as we wished to show. This, combined with G-invariance,
implies that there exist unique forms Ω 0
a on M0 that satisfy π∗
0(Ω 0
a) = ˜Ω 0
a. Since π0 is a
submersion, the three 2-forms Ω 0
a are closed.
To complete the proof, it suﬃces to show that the triple (Ω 0
1, Ω 0
2, Ω 0
3) actually deﬁnes
an almost hyperK¨ ahler structure onM0, for then we can apply Theorem 4.
We do this as follows: Use the associated metric ⟨, ⟩ to deﬁne an orthogonal splitting
Tmµ−1(0) = TmG·m ⊕Hm.
By the hypotheses of the theorem, the ﬁbers of π0 are the G-orbits in µ−1(0) and, for
eachm ∈µ−1(0), the kernel of the diﬀerential π′
0(m) is TmG·m. Thus, π′
0(m) induces an
isomorphism from Hm to Tπ0(m)M0 and, under this isomorphism, the restriction of the
form ˜Ω 0
a to Hm is identiﬁed with Ω 0
a.
Thus, it suﬃces to show that the forms ( ˜Ω 0
1, ˜Ω 0
2, ˜Ω 0
3) deﬁne a hyperK¨ ahler structure
when restricted to Hm. By Proposition 2, to do this, it would suﬃce to show that Hm is
stable under the actions of Ri, Rj, and Rk. However, by deﬁnition, Hm is the subspace
of TmM that is orthogonal to the H-linear subspace
(
TmG·m
)
· H ⊂ TmM . Since the
orthogonal complement of an H-linear subspace of TmM is also an H-linear subspace, we
are done. □
Note that the proof also shows that the dimension of the reduc ed space M0 is equal to
dimM −4 dim(G/Gm), since, at each point m ∈µ−1(0), the space TmG·m is perpendicular
to Ri
(
TmG·m
)
⊕Rj
(
TmG·m
)
⊕Rk
(
TmG·m
)
and this latter direct sum is orthogonal.
Unfortunately, it frequently happens that 0 is not a clean va lue of µ, in which case,
Theorem 5 cannot be applied to the action. Moreover, there do es not appear to be any
simple way to perform hyperK¨ ahler reduction at the general clean value of µ in g∗ ⊕g∗ ⊕g∗
L.8.17 147

(in marked contrast to the K¨ ahler case). In fact, for the gen eral clean value ξ ∈ g∗ ⊕g∗ ⊕g∗
of µ, the quotient space Mξ = Gξ\µ−1(ξ) need not even have its dimension be divisible
by 4. (See the Exercises for a cautionary example.)
However, if [g, g]⊥ ⊂ g∗ denotes the annihilator of [ g, g] in g, then the points ξ ∈ [g, g]⊥
are the ﬁxed points of the coadjoint action of G. It is then possible to perform hyperK¨ ahler
reduction at any clean value ξ = (ξ1,ξ 2,ξ 3) ∈ [g, g]⊥ ⊕ [g, g]⊥ ⊕ [g, g]⊥ since, in this case,
we again have Gξ = G, and so the argument in the proof above that Hm ⊂ Tmµ−1(ξ)
is a quaternionic subspace for each m ∈ Tmµ−1(ξ) is still valid. Of course, this is not
really much of a generalization, since reduction at such a ξ is simply reduction at 0 for the
modiﬁed (but still G-equivariant) momentum mapping µξ =µ −ξ.
Example: One of the simplest things to do is take M = Hn and let G ⊂ Sp(n)
be a closed subgroup. It is not diﬃcult to show (see the Exerci ses) that the standard
hyperK¨ ahler structure onHn has its three 2-forms given by
i Ω 1 +j Ω 2 +k Ω 3 = 1
2
td¯q ∧dq
where q : Hn → Hn is the identity, thought of as a Hn-valued function on Hn. Using this
formula, it is easy to show that the standard left action of Sp (n) on Hn is Poisson, with
momentum mapping µ : Hn → sp(n) ⊕ sp(n) ⊕ sp(n) given by the formula*
µ(q) = 1
2
(
qi t ¯q, qjt ¯q, qkt ¯q
)
.
Note that 0 is not a clean value of µ with respect to the full action of Sp( n). However, the
situation can be very diﬀerent for a closed subgroup G ⊂ Sp(n): Let πg : sp(n) → g be the
orthogonal projection relative to the Ad-invariant inner product on sp(n). The momentum
mapping for the action of G on Hn is then given by
µG(q) = 1
2
(
πg(qi t ¯q), πg(qj t ¯q), πg(qk t ¯q)
)
.
SinceG is compact, there is an orthogonal direct sum g = z ⊕ [g, g], where z is the tangent
algebra to the center of G. Thus, there will be a hyperK¨ ahler reduction for each clean
value of µG that lies in z⊕z⊕z.
Let us now consider a very simple example: Let S1 ⊂ Sp(n) act diagonally on Hn by
the action
eiθ ·



q1
.
.
.
qn


 =



eiθq1
.
.
.
eiθqn


.
* Here, I am identifying sp(n) with sp(n)∗ via the positive deﬁnite, Ad-invariant sym-
metric bilinear pairing deﬁned by ⟨a,b ⟩ = − 1
2 tr(ab +ba). (Because of the noncommuta-
tivity of H, we do not have tr( ab) = tr(ba) for all a,b ∈ sp(n).)
L.8.18 148

Then it is not diﬃcult to see that the momentum mappping can be identiﬁed with the
map
µ(q) = t¯qiq.
The reduced space Mp for any p ⁄= 0 is easily seen to be complex analytically equivalent to
T ∗CPn−1, and the induced hyperK¨ ahler structure is the one found by Calabi. In particular,
for n = 2, we recover the Eguchi-Hansen metric.
In the Exercises, there are other examples for you to try.
The method of hyperK¨ ahler reduction has a wide variety of ap plications. Many of the
interesting moduli spaces for Yang-Mills theory turn out to have hyperK¨ ahler structures
because of this reduction procedure. For example, as Atiyah and Hitchin [AH] show, the
space of magnetic monopoles of “charge” k on R3 turns out to have a natural hyperK¨ ahler
structure that is derived by methods extremely similar to th e example presented earlier of
a K¨ ahler structure on the moduli space of ﬂat connections ov er a Riemann surface.
Peter Kronheimer [Kr] has used the method of hyperK¨ ahler re duction to construct,
for each quotient manifold Σ of S3, an asymptotically locally Euclidean (ALE) Ricci-ﬂat
self-dual Einstein metric on a 4-manifold MΣ whose boundary at inﬁnity is Σ. He then
went on to prove that all such metrics on 4-manifolds arise in this way.
Finally, it should also be mentioned that the case of metrics on manifolds M 4n with
holonomy Sp(n) · Sp(1) can also be treated by the method of reduction. I don’t h ave time
to go into this here, but the reader can ﬁnd a complete account in [GL].
L.8.19 149

Exercise Set 8:
Recent Applications of Reduction
1. Show that the following two deﬁnitions of compatibility be tween an almost complex
structure J and a metric g on M 2n are equivalent
(i) (g,J ) are compatible if g(v) = g(Jv ) for all v ∈TM .
(ii) (g,J ) are compatible if Ω( v,w ) = ⟨Jv,w ⟩ deﬁnes a (skew-symmetric) 2-form on M .
2. A Non-Integrable Almost Complex Structure. Let J be an almost complex
structure on M . Let A1,0 ⊂ C ⊗ A1(M ) denote the space of C-valued 1-forms on M that
satisfy α(Jv ) = ıα (v) for all v ∈TM .
(i) Show that if we deﬁne A0,1(M ) ⊂ C ⊗ A1(M ) to be the space of C-valued 1-forms on
M that satisfy α(Jv ) = −ıα (v) for all v ∈ TM , then A0,1(M ) = A1,0(M ) and that
A1,0(M ) ∩ A0,1(M ) = {0}.
(ii) Show that if J is an integrable almost complex structure, then, for any α ∈ A 1,0(M ),
the 2-form dα is (at least locally) in the ideal generated by A1,0(M ). (Hint: Show
that, if z :U → Cn is a holomorphic coordinate chart, then, on U , the space A1,0(U )
is spanned by the forms dz1,...,dz n. Now consider the exterior derivative of any
linear combination of the dzi.)
It is a celebrated result of Newlander and Nirenberg that thi s condition is suﬃcient
for J to be integrable.
(iii) Show that there is an almost complex structure on C2 for which A1,0(C2) is spanned
by the 1-forms
ω1 =dz1 − ¯z1d¯z2
ω2 =dz2
and that this almost complex structure is not integrable.
3. Let M = Cn1 ⊕ Cn2 \ {(0, 0)}. Let G =S1 act on M by the action
eıθ · (z1,z 2) =
(
eıd1θz1,eıd2θz2
)
where d1 and d2 are integers. Let M have the standard ﬂat K¨ ahler structure. Compute
the moment map µ and the K¨ ahler structures on the reduced spaces. How do the r elative
signs of d1 and d2 aﬀect the answer? What interpretation can you give to these s paces?
E.8.1 150

4. Go back to the the example of the “K¨ ahler structure” on the s pace A(P ) of connections
on a principal right G-bundle P over a connected compact Riemann surface Σ. Assume
thatG =S1 and identify g with R in the natural way. Thus, FA is a well-deﬁned 2-form on
Σ and the cohomology class [ FA] ∈H 2
dR(Σ, R) is independent of the choice of A. Assume
that [FA] ⁄= 0. Then, in this case, µ −1(0) is empty so the construction we made in the
example in the Lecture is vacuous. Here is how we can still get some information.
Fix any non-vanishing 2-form Ψ on Σ so that [Ψ] = [ FA]. Show that even though µ has
no regular values, Ψ is a non-trivial clean value of µ . Show also that, for any A ∈ µ −1(Ψ),
the stabilizer GA ⊂ Aut(P ) is a discrete (and hence ﬁnite) subgroup of S1. Describe, as
fully as you can, the reduced space MΨ and its K¨ ahler structure.
5. Verify that Sp( n) is a connected Lie group of dimension 2 n2 +n. (Hint: You will
probably want to study the function f (A) = t ¯AA =In.) Show that Sp( n) acts transitively
on the unit sphere S4n−1 ⊂ Hn deﬁned by the relation H(x,x ) = 1. (Hint: First show
that, by acting by diagonal matrices in Sp( n), you can move any element of Hn into the
subspace Rn. Then note that Sp( n) contains SO(n).) By analysing the stabilizer subgroup
in Sp(n) of an element of S4n−1, show that there is a ﬁbration
Sp(n−1) → Sp(n)
↓
S4n−1
and use this to conclude by induction that Sp( n) is connected and simply connected for
all n.
6. Prove Proposition 2. (Hint: First show how the maps Ri, Rj, and Rk deﬁne the
structure of a right H-module on V . Then show that V has a basis b1,...,b n over H and
use this to construct an H-linear isomorphism of V with Hn. If you pick the basis ba
carefully, you will be done at this point. Warning: You must u se the positive deﬁniteness
of ⟨, ⟩!)
7. Determine a formula for the dimension of the Hyperk¨ ahler r educed space Mξ in terms
of the dimensions of M ,G, Gξ and Gm (where m lies in µ−1(ξ)).
8. Apply the Hyperk¨ ahler reduction procedure to H2 with R acting by the rule
θ ·
(
q1
q2
)
=
(
eiθq1
q2 +θ
)
.
Determine which values of µ are clean and describe the resulting complex surfaces and
their Hyperk¨ ahler structures.
E.8.2 151

Lecture 9:
The Gromov School of Symplectic Geometry
In this lecture, I want to describe some of the remarkable new information we have
about symplectic manifolds owing to the inﬂuence of the idea s of Mikhail Gromov. The
basic reference for much of this material is Gromov’s remark able book Partial Diﬀerential
Relations.
The fundamental idea of studying complex structures “tamed by” a given symplectic
structure was developed by Gromov in a remarkable paper Pseudo-holomorphic Curves on
Almost Complex Manifolds and has proved extraordinarily fruitful. In the latter part of
this lecture, I will try to introduce the reader to this theor y.
Soft T echniques in Symplectic Manifolds
Symplectic Immersions and Embeddings. Before beginning on the topic of
symplectic immersions, let me recall how the theory of immer sions in the ordinary sense
goes.
Recall that the Whitney Immersion Theorem (in the weak form) asserts that any
smoothn-manifoldM has an immersion into R2n. This result is proved by ﬁrst immersing
M into some RN for N ≫ 0 and then using Sard’s Theorem to show that if N > 2n,
one can ﬁnd a vector u ∈ RN so that u is not tangent to f (M ) at any point. Then the
projection of f (M ) onto a hyperplane orthogonal to u is still an immersion, but now into
RN−1.
This result is not the best possible. Whitney himself showed that one could always im-
merseMn into R2n−1, although “general position” arguments are not suﬃcient to do this.
This raises the question of determining what the best possib le immersion or embedding
dimension is.
One topological obstruction to immersing Mn into Rn+k can be described as follows:
If f :M → Rn+k is an immersion, then the trivial bundle f ∗(T Rn+k) = M × Rn+k can
be split into a direct sum f ∗(T Rn+k) = TM ⊕νf where νf is the normal bundle of the
immersion f . Thus, if there is no bundle ν of rank k over M so that TM ⊕ν is trivial,
then there can be no immersion of M into Rn+k.
The remarkable fact is that this topological necessary cond ition is almost suﬃcient. In
fact, we have the following result of Hirsch and Smale for the general immersion problem.
Theorem 1: Let M and N be connected smooth manifolds and suppose either that M
is non-compact or else that dim(M )< dim(N ). Let f :M →N be a continuous map, and
suppose that there is a vector bundle ν over M so that f ∗(TN ) = TM ⊕ν. Then f is
homotopic to an immersion of M intoN
Theorem 1 can be interpreted as an example of what Gromov call s the h-principle,
which I now want to describe.
L.9.1 152

The h-Principle. Let π:V → X be a surjective submersion. A section of π is, by
deﬁnition, a map σ:X → V that satisﬁes π ◦σ = idX . Let Jk(X,V ) denote the space
of k-jets of sections of V , and let πk:Jk(X,V ) → X denote the basepoint or ‘source’
projection. Given any section s of π, there is an associated section jk(s) of πk that is
deﬁned by letting jk(s)(x) be the k-jet of s at x ∈ X. A section σ of πk is said to be
holonomic if σ =jk(s) for some section s of π.
A partial diﬀerential relation of order k for π is a subset R ⊂Jk(X,V ). A section s
of π is said to satisfy R if jk(s)(X) ⊂R. We can now make the following deﬁnition:
Deﬁnition 1: A partial diﬀerential relation R ⊂Jk(X,V ) satisﬁes the h-principle if, for
every section σ of πk that satisﬁes σ(X) ⊂R, there is a one-parameter family of sections
σt (0 ≤t ≤ 1) of πk that satisfy the conditions that σt(X) ⊂R for all t, that σ0 =σ, and
that σ1 is holonomic.
Very roughly speaking, a partial diﬀerential relation sati sﬁes the h-principle if, when-
ever the “topological” conditions for a solution to exist ar e satisﬁed, then a solution exists.
For example, if X = M and V = M ×N , where dim( N ) ≥ dim(M ), then there is
an (open) subset R = Imm(M,N ) ⊂ J 1(M,M ×N ) that consists of the 1-jets of graphs
of (local) immersions of M intoN . What the Hirsch-Smale immersion theory says is that
Imm(M,N ) satisﬁes the h-principle if either dim M = dim N and M has no compact
component or else dim M <dim N .
Of course, the h-principle does not hold for every relation R. The real question is
how to determine when the h-principle holds for a given R. Gromov has developed sev-
eral extremely general methods for proving that the h-principle holds for various partial
diﬀerential relations R that arise in geometry. These methods include his theory of t opo-
logical sheaves and techniques like his method of convex int egration. They generally work
in situations where the local solutions of a given partial di ﬀerential relation R are easy to
come by and it is mainly a question of ‘patching together’ loc al solutions which are fairly
‘ﬂexible’.
Gromov calls this collection of techniques ‘soft’ to distin guish them from the ‘hard’
techniques, such as elliptic theory, that come from analysi s and deal with situations where
the local solutions are somewhat ‘rigid’.
Here is a sample of some of the results that Gromov obtains by t hese methods:
Theorem 2: Let X 2n be a smooth manifold and let V ⊂ Λ 2(
T ∗(M )
)
denote the open
subbundle consisting of non-degenerate 2-forms ω ∈ TxX. Let Z 1(X,V ) ⊂ J 1(X,V )
denote the space of 1-jets of closed non-degenerate 2-forms on X. Then, if X has no
compact component, Z 1(X,V ) satisﬁes the h-principle.
In particular, Theorem 2 implies that a non-compact, connec ted X has a symplectic
structure if and only if it has an almost symplectic structur e.
Note that this result is deﬁnitely not true for compact manifolds. We have already seen
several examples, e.g., S1 ×S3, that have almost symplectic structures but no symplectic
structures because they do not satisfy the cohomology ring o bstruction. Gromov has asked
the following:
L.9.2 153

Question : IfX 2n is compact and connected and satisﬁes the condition that the re exists
an element u ∈H 2
dR(X, R) that satisﬁes un ⁄= 0, does Z 1(X,V ) satisfy the h-principle?
The next result I want to describe is Gromov’s theorem on symp lectic immersions.
This theorem is an example of a sort of ‘restricted h-principle’ in that it is only required
to apply to sections σ that satisfy speciﬁed cohomological conditions.
First, let me make a few deﬁnitions: Let ( X, Ξ) and (Y, Ψ) be two connected symplectic
manifolds. Let S(X,Y ) ⊂ J 1(X,X ×Y ) denote the space of 1-jets of graphs of (local)
symplectic maps f :X → Y . i.e., (local) maps f :X → Y that satisfy f ∗(Ψ) = Ξ. Let
τ : S(X,Y ) →Y be the obvious “target projection”.
Theorem 3: If either X is non-compact, or dim(X) < dim(Y ), then any section σ of
S(X,Y ) for which the induced map s =τ ◦σ:X →Y satisﬁes the cohomological condition
s∗([Ψ]) = [Ξ] is homotopic to a holonomic section of S(X,Y ).
This result can be also stated as follows: Suppose that eithe rX is non-compact or else
that dim(X)< dim(Y ). Let φ:X →Y be a smooth map that satisﬁes the cohomological
condition φ∗(
[Ψ]
)
= [Ξ]. Suppose that there exists a bundle map f :TX → φ∗(TY ) that
is symplectic in the obvious sense. Then φ is homotopic to a symplectic immersion.
As an application of Theorem 3, we can now prove the following result of Narasimham
and Ramanan.
Corollary : Any compact symplectic manifold (M, Ω) for which the cohomology class
[Ω] is integral admits a symplectic immersion into (CPN, ΩN ) for some N ≫n.
Proof: Since the cohomology class [Ω] is integral, there exists a sm ooth mapφ:M → CPN
for some N suﬃciently large so that φ∗(
[ΩN ]
)
= [Ω]. Then, choosing N ≫ n, we can
arrange that there also exists a symplectic bundle map f :TM → f ∗(T CPN ) (see the
Exercises). Now apply Theorem 3. □
As a ﬁnal example along these lines, let me state Gromov’s emb edding result. Here,
the reader should be thinking of the diﬀerence between the Wh itney Immersion Theorems
and the Whitney Embedding Theorems: One needs slightly more room to embed than to
immerse.
Theorem 4: Suppose that (X, Ξ) and (Y, Ψ) are connected symplectic manifolds and
that either X is non-compact and dim(X)< dim(Y ) or else that dim(X)< dim(Y ) − 2.
Suppose that there exists a smooth embedding φ:X → Y and that the induced map on
bundles φ′:TX →φ∗(TY ) is homotopic through a 1-parameter family of injective bundle
maps ϕt:TX → φ∗(TY ) (with ϕ0 = φ′) to a symplectic bundle map ϕ1:TX → φ∗(TY ).
Then φ is isotopic to a symplectic embedding ϕ:X →Y .
This result is actually the best possible, for, as Gromov has shown using “hard” tech-
niques (see below), there are counterexamples if one leaves out the dimensional restrictions.
Note by the way that, because Theorem 4 deals with embeddings rather than immersions,
it not straightforward to place it in the framework of the h-principle.
L.9.3 154

Blowing Up in the Symplectic Category . We have already seen in Lecture 6 that
certain operations on smooth manifolds cannot be carried ou t in the symplectic category.
For example, one cannot form connected sums in the symplecti c category.
However, certain of the operations from the geometry of comp lex manifolds can be car-
ried out. Gromov has shown how to deﬁne the operation of “blow ing up” in the symplectic
category.
Recall how one “blows up” the origin in Cn. To avoid triviality, let me assume that
n> 1. Consider the subvariety
X = {(v, [w]) ∈ Cn × CPn−1 |v ∈ [w]} ⊂ Cn × CPn−1.
It is easy to see that X is a smooth embedded submanifold of the product and that the
projection π:X → Cn is a biholomorphism away from the “exceptional point” 0 ∈ Cn.
Moreover, if Ω 0 and Φ are the standard K¨ ahler 2-forms on Cn and CPn−1 respectively,
then, for each ǫ> 0, the 2-form Ω ǫ = Ω 0 +ǫΦ is a K¨ ahler 2-form on X.
Now, Gromov realized that this can be generalized to a “blow u p” construction for
any point p on any symplectic manifold ( M 2n, Ω). Here is how this goes:
First, choose a neighborhood U of p on which there exists a local chart z:U → Cn
that is symplectic, i.e., satisﬁes z∗(Ω 0) = Ω, and satisﬁes z(p) = 0. Suppose that the ball
B2δ(0) in Cn of radius 2 δ centered on 0 lies inside z(U ). Since π:π−1(
B∗
2δ(0)
)
→ B∗
2δ(0)
is a diﬀeomorphism, there exists a closed 2-form ˜Φ on B∗
2δ(0) so that π∗( ˜Φ) = Φ. Since
H 2
dR
(
B∗
2δ(0)
)
= 0, there exists a 1-form ϕ on B∗
2δ(0) so that dϕ = Φ.
Now consider the family of symplectic forms Ω 0+ǫdϕ onB∗
2δ(0). By using a homotopy
argument exactly like the one used to Prove Theorem 1 in Lectu re 6, it easily follows that
for all t > 0 suﬃciently small, there exists an open annulus A(δ −ε,δ +ε) and a one-
parameter family of diﬀeomorphisms φt:A(δ −ε,δ +ε) →B∗
2δ(0) so that
φ∗
t (Ω 0) = Ω 0 +tdϕ.
It follows that we can set
ˆM =π−1(
B∗
δ+ε(0)
)
∪ψtM \z−1(
φt
(
B∗
δ−ε(0)
))
where
ψt:π−1(
A(δ −ε,δ +ε)
)
→M \z−1(
φt
(
A(δ −ε,δ +ε)
))
is given by ψt = z−1 ◦φt ◦π. Since ψt identiﬁes the symplectic structure Ω t with Ω 0 on
the annulus “overlap”, it follows that ˆM is symplectic. This is Gromov’s symplectic blow
up procedure. Note that it can be eﬀected in such a way that the symplectic structure on
M \ {p} is not disturbed outside of an arbitrarily small ball around p. Note also that there
is a parameter involved, and that the symplectic structure i s certainly not unique.
This is only describes a simple case. However, Gromov has sho wn how any compact
symplectic submanifoldS2k ofM 2n can be blown up to become a symplectic “hypersurface”
ˆS in a new symplectic manifold ˆM that has the property that M \S is diﬀeomorphic to
ˆM \ ˆS.
L.9.4 155

The basic idea is the same as what we have already done: First, one mimics the
topological operations that would be performed if one were b lowing up a complex sub-
manifold of a complex manifold. Thus, the submanifold S gets ‘replaced’ by the complex
projectivization ˆS = PNS of a complex normal bundle. Second, one shows how to deﬁne
a symplectic structure on the resulting smooth manifold tha t can be made to agree with
the old structure outside of an arbitrarily small neighborh ood of the blow up.
The details in the general case are somewhat more complicate d than the case of
blowing up a single point, and Dusa McDuﬀ ([McDuﬀ 1984]) has w ritten out a careful
construction. She has also used the method of blow ups to prod uce an example of a simply
connected compact symplectic manifold that has no K¨ ahler s tructure.
Hard T echniques in Symplectic Manifolds.
(Pseudo-) holomorphic curves. I begin with a fundamental deﬁnition.
Deﬁnition 2: Let M 2n be a smooth manifold and let J:TM → TM be an almost
complex structure on M . For any Riemann surface Σ, we say that a map f : Σ → M is
J-holomorphic if f ′(ıv ) = Jf ′(v) for all v ∈T Σ.
◮ Often, when J is clear from context, I will simply say “ f is holomorphic”. Several
authors use the terminology “almost holomorphic” or “pseud o-holomorphic” for this con-
cept, reserving the word “holomorphic” for use only when the almost complex structure
on M is integrable to an actual complex structure. This distinct ion does not seem to be
particularly useful, so I will not maintain it.
It is instructive to see what this looks like in local coordin ates. Let z =x+ıy be a local
holomorphic coordinate on Σ and let w:U → R2n be a local coordinate on M . Then there
exists a matrix J(w) of functions on w(U ) ⊂ R2n that satisﬁes w′(Jv ) = J
(
w(p)
)
w′(v) for
all v ∈TpU . This matrix of functions satisﬁes the relation J2 = −I2n. Now, if f : Σ →M
is holomorphic and carries the domain of the z-coordinate into U , then F =w ◦f is easily
seen to satisfy the ﬁrst order system of partial diﬀerential equations
∂F
∂y = J(F )∂F
∂x.
Since J2 = −I2n, it follows that this is a ﬁrst-order, elliptic, determined system of partial
diﬀerential equations for F . In fact, the “principal symbol” of these equations is the sa me
as that for the Cauchy-Riemann equations. Assuming that J is suﬃciently regular ( C∞ is
suﬃcient and we will always have this) there are plenty of loc al solutions. What is at issue
is the nature of the global solutions.
A parametrized holomorphic curve inM is a holomorphic map f : Σ →M . Sometimes
we will want to consider unparametrized holomorphic curves in M , namely equivalence
classes [Σ ,f ] of holomorphic curves in M where (Σ 1,f 1) is equivalent to (Σ 2,f 2) if there
exists a holomorphic map φ: Σ 1 → Σ 2 satisfying f1 =f2 ◦φ.
L.9.5 156

We are going to be particularly interested in the space of hol omorphic curves in M .
Here are some properties that hold in the case of holomorphic curves in actual complex
manifolds and it would be nice to know if they also hold for hol omorphic curves in almost
complex manifolds.
Local Finite Dimensionality. If Σ is a compact Riemann surface, and f : Σ →M
is a holomorphic curve, it is reasonable to ask what the space of “nearby” holomorphic
curves looks like. Because the equations that determine the se mappings are elliptic and
because Σ is compact, it follows without too much diﬃculty th at the space of nearby
holomorphic curves is ﬁnite dimensional. (We do not, in general know that it is a smooth
manifold!)
Intersections. A pair of distinct complex curves in a complex surface always inter-
sect at isolated points and with positive “multiplicity.” T his follows from complex analytic
geometry. This result is extremely useful because it allows us to derive information about
actual numbers of intersection points of holomorphic curve s by applying topological inter-
section formulas. (Usually, these topological intersecti on formulas only count the number
of signed intersections, but if the surfaces can only inters ect positively, then the topological
intersection numbers (counted with multiplicity) are the a ctual intersection numbers.)
K¨ahler Area Bounds. If M happens to be a K¨ ahler manifold, with K¨ ahler form
Ω, then the area of the image of a holomorphic curve f : Σ →M is given by the formula
Area
(
f (Σ)
)
=
∫
Σ
f ∗(Ω).
In particular, since Ω is closed, the right hand side of this e quation depends only on the
homotopy class of f as a map into M . Thus, if (Σ t,ft) is a continuous one-parameter
family of closed holomorphic curves in a K¨ ahler manifold, t hen they all have the same
area. This is a powerful constraint on how the images can beha ve, as we shall see.
Now the ﬁrst two of these properties go through without chang e in the case of almost
complex manifolds.
In the case of local ﬁniteness, this is purely an elliptic the ory result. Studying the
linearization of the equations at a solution will even allow one to predict, using the Atiyah-
Singer Index Theorem, an upper bound for the local dimension of the moduli space and,
in some cases, will allow us to conclude that the moduli space near a given closed curve is
actually a smooth manifold (see below).
As for pairs of complex curves in an almost complex surface, G romov has shown that
they do indeed only intersect in isolated points and with pos itive multiplicity (unless they
have a common component, of course). Both Gromov and Dusa McD uﬀ have used this
fact to study the geometry of symplectic 4-manifolds.
The third property is only valid for K¨ ahler manifolds, but i t is highly desirable. The
behaviour of holomorphic curves in compact K¨ ahler manifolds is well understood in a large
part because of this area bound. This motivated Gromov to inv estigate ways of generalizing
this property.
L.9.6 157

Symplectic T amings. Following Gromov, we make the following deﬁnition.
Deﬁnition 3: A symplectic form Ω on M tames an almost complex structure J if it is
J-positive, i.e., if it satisﬁes Ω( v,Jv )> 0 for all non-zero tangent vectors v ∈TM .
The reader should be thinking of K¨ ahler geometry. In that ca se, the symplectic form
Ω and the complex structure J satisfy Ω( v,Jv ) = ⟨v,v ⟩> 0. Of course, this generalizes to
the case of an arbitrary almost K¨ ahler structure.
Now, if M is compact and Ω tames J, then for any Riemannian metric g on M (not
necessarily compatible with either J or Ω) there is a constant C >0 so that
|v ∧Jv | ≤ C Ω(v,Jv )
where |v∧Jv | represents the area in TpM of the parallelogram spanned by v andJv inTpM
(see the Exercises). In particular, it follows that, for any holomorphic curve f : Σ → M ,
we have the inequality
Area
(
f (Σ)
)
≤C
∫
Σ
f ∗(Ω).
Just as in the K¨ ahler case, the integral on the right hand side depends only on the homotopy
class off . Thus, if an almost complex structure can be tamed, it follow s that, in any metric
onM , there is a uniform upper bound on the areas of the curves in an y continuous family
of compact holomorphic curves in M .
Example: Let N C
3 denote the complex Heisenberg group. Thus, N C
3 is the complex Lie
group of matrices of the form
g =


1 x z
0 1 y
0 0 1

.
Let Γ ⊂N C
3 be the subgroup all of whose entries belong to the ring of Gaus sian integers
Z[ı].
LetM =N C
3/Γ. Then M is a compact complex 3-manifold. I claim that the complex
structure on M cannot be tamed by any symplectic form.
To see this, consider the right-invariant 1-form
dgg −1 =


0 ω1 ω3
0 0 ω2
0 0 0

.
Since they are right-invariant, it follows that the complex 1-forms ω1,ω 2,ω 3 are also well-
deﬁned on M . Deﬁne the metric G on M to be the quadratic form
G =ω1 ◦
ω1 +ω2 ◦ω2 +ω3 ◦ω3.
L.9.7 158

Now consider the holomorphic curve Y : C →N C
3 deﬁned by
Y (y) =


1 0 0
0 1 y
0 0 1

.
Let ψ: C →M be the composition. It is clear that ψ is doubly periodic and hence deﬁnes
an embedding of a complex torus into M . It is clear that the G-area of this torus is 1.
NowN C
3 acts holomorphically on M on the left (not by G-isometries, of course). We
can consider what happens to the area of the torus ψ(C) under the action of this group.
Speciﬁcally, for x ∈ C, let ψx denote ψ acted on by left multiplication by the matrix


1 x 0
0 1 0
0 0 1

.
Then, as the reader can easily check, we have
ψ∗
x(G) =
(
1 + |x|2)
⏐
⏐dy
⏐
⏐2
.
Thus, the G-area of the torus ψx(C) goes oﬀ to inﬁnity as x tends to inﬁnity. Obviously,
there can be no taming of the complex manifold M . (In particular, M cannot carry a
K¨ ahler structure compatible with its complex structure.)
Gromov’s Compactness Theorem. In this section, I want to discuss Gromov’s
approach to compactifying the connected components of the s pace of unparametrized holo-
morphic curves in M .
Example: Before looking at the general case, let us look at what happen s in a very
familiar case: The case of algebraic curves in CP2 with its standard Fubini-Study metric
and symplectic form Ω (normalized so as to give the lines in CP2 an area of 1).
Since this is a K¨ ahler metric, we know that the area of a conne cted one-parameter
family of holomorphic curves (Σ t,ft) in CP2 is constant and is equal to an integer d =∫
Σ t
f ∗
t (Ω), called the degree. To make matters as simple as possible, let me consider the
curves degree by degree.
d = 0. In this case, the “curves” are just the constant maps and ( in the unparametrized
case) clearly constitute a copy of CP2 itself. Note that this is already compact.
d = 1. In this case, the only possibility is that each Σ t is just CP1 and the holo-
morphic map ft must be just a biholomorphism onto a line in CP2. Of course, the space
of lines in CP2 is compact, just being a copy of the dual CP2. Thus, the space M1 of
unparametrized holomorphic curves in CP2 is compact. Note, however, that the space H1
of holomorphic maps f : CP1 → CP2 of degree 1 is not compact. In fact, the ﬁbers of the
natural map H1 → M1 are copies of Aut( CP1) = PSL(2, C).
L.9.8 159

d = 2. This is the ﬁrst really interesting case. Here again, deg ree 2 (connected,
parametrized) curves in CP2 consist of rational curves, and the images f : CP1 → CP2
are of two kinds: the smooth conics and the double covers of li nes. However, not only is
this space not compact, the corresponding space of unparame trized curves is not compact
either, for it is fairly clear that one can approach a pair of i ntersecting lines as closely as
one wishes.
In fact, the reader may want to contemplate the one-paramete r family of hyperbolas
xy =λ2 as λ → 0. If we choose the parametrization
fλ(t) = [t,λt 2,λ ] = [1,x,y ],
then the pullback Φ λ =f ∗
λ(Ω) is an area form on CP1 whose total integral is 2, but (and the
reader should check this), as λ → 0, the form Φ λ accumulates equally at the points t = 0
and t = ∞ and goes to zero everywhere else. (See the Exercises for a fur ther discussion.)
Now, if we go ahead and add in the pairs of lines, then this “com pleted” moduli
space is indeed compact. It is just the space of non-zero quad ratic forms in three variables
(irreducible or not) up to constant multiples. It is well kno wn that this forms a CP5.
In fact, a further analysis of low degree mappings indicates that the following phe-
nomena are typical: If one takes a sequence (Σ k,fk) of smooth holomorphic curves in CP2,
then after reparametrizing and passing to a subsequence, on e can arrange that the holo-
morphic curves have the property that, at a ﬁnite number of po ints pα
k ∈ Σ, the induced
metric f ∗
k (Ω) on the surface goes to inﬁnity and the integral of the indu ced area form on
a neighborhood of each of these points approaches an integer while along a ﬁnite number
of loops γi, the induced metric goes to zero.
The ﬁrst type of phenomenon is called “bubbling”, for what is happening is that
a small 2-sphere is inﬂating and “breaking oﬀ” from the surfa ce and covering a line in
CP2. The second type of phenomenon is called “vanishing cycles” , a loop in the surface
is literally contracting to a point. It turns out that the lim iting object in CP2 is a union
of algebraic curves whose total degree is the same as that of t he members of the varying
family.
Thus, for CP2, the moduli space Md of unparametrized curves of degree d has a
compactiﬁcation
Md where the extra points represent decomposable or degenerat e curves
with “cusps”.
Other instances of this “bubbling” phenomena have been disc overed. Sacks and Uh-
lenbeck showed that when one wants to study the question of re presenting elements of
π2(X) (where X is a Riemannian manifold) by harmonic or minimal surfaces, o ne has
to deal with the possibility of pieces of the surface “bubbli ng oﬀ” in exactly the fashion
described above.
More recently, this sort of phenomenon has been used in “reve rse” by Taubes to
construct solutions to the (anti-)self dual Yang-Mills equ ations over compact 4-manifolds.
With all of this evidence of good compactiﬁcations of moduli spaces in other problems,
Gromov had the idea of trying to compactify the connected com ponents of the “moduli
L.9.9 160

space” M of holomorphic curves in a general almost complex manifold M . Since one would
certainly expect the area function to be continuous on each c ompactiﬁed component, it
follows that there is not much hope of ﬁnding a good compactiﬁ cation of the components
of M in a case where the area function is not bounded on the compone nts of M (as in the
case of the Heisenberg example above).
However, it is still possible that one might be able to produc e such a compactiﬁcation
if one can get an area bound on the curves in each component. Gromov’s in sight was
that having the area bound was enough to furnish a priori estimates on the derivatives of
curves with an area bound, at least away from a ﬁnite number of points.
With all of this in mind, I can now very roughly state Gromov’s Compactiﬁcation
Theorem:
Theorem 5: LetM be a compact almost complex manifold with almost complex str ucture
J and suppose that Ω tames J. Then every component Mα of the moduli space M of
connected unparametrized holomorphic curves in M can be compactiﬁed to a space
Mα
by adding a set of “cusp” curves, where a cusp curve is essenti ally a ﬁnite union of (possibly)
singular holomorphic curves in M that is obtained as a limit of a sequence of connected
curves in Mα by ‘pinching loops’ and ‘bubbling’.
For the precise deﬁnition of ‘cusp curve’ consult [Gr 1], [Wo ], or [Pa]. The method
that Gromov uses to prove his compactness theorem is basical ly a generalization of the
Schwarz Lemma. This allows him to get control of the sup-norm of the ﬁrst derivatives of
a holomorphic curve in M terms of the L2
1-norm (i.e., area norm) at least in regions where
the area form stays bounded.
Unfortunately, although the ideas are intuitively compell ing, the actual details are
non-trivial. However, there are, by now, several good sourc es, from diﬀerent viewpoints,
for proofs of Gromov’s Compactiﬁcation Theorem. The articl es [M 4] and [Wo] listed in
the Bibliography are very readable accounts and are highly r ecommended. I hear that the
(unpublished) [Pa] is also an excellent account that is clos er in spirit to Gromov’s original
ideas of how the proof should go. Finally, there is the quite r ecent [Ye], which generalizes
this compactiﬁcation theorem to the case of curves with boun dary.
Actually, the most fruitful applications of these ideas hav e been in the situation when,
for various reasons, it turns out that there cannot be any cus p curves, so that, by Gromov’s
compactness theorem, the moduli space is already compact. H ere is a case where this
happens.
Proposition 1: Suppose that (M,J ) is a compact, almost complex manifold and that
Ω is a 2-form that tames J. Suppose that there exists a non-constant holomorphic curv e
f :S2 → M , and suppose that there is a number A > 0 so that
∫
S2f ∗(Ω) ≥ A for all
non-constant holomorphic maps f :S2 → M . Then for any B < 2A, the set MB of
unparametrized holomorphic curves f (S2) ⊂M that satisfy
∫
S2f ∗(Ω) = B is compact.
L.9.10 161

Proof: (Idea) If the space MB were not compact, then a point of the compactiﬁcation
would would correspond a union of cusp curves that would cont ain at least two distinct
non-constant holomorphic maps ofS2 intoM . Of course, this would imply that the limiting
value of the integral of Ω over this curve would be at least 2 A>B , a contradiction. □
An example of this phenomenon is when the taming form Ω repres ents an integral
class in cohomology. Then the presence of any holomorphic ra tional curves at all implies
that there is a compact moduli space at some level.
Applications. It is reasonable to ask how the Compactness Theorem can be app lied
in symplectic geometry.
To do this, what one typically does is ﬁrst ﬁx a symplectic man ifold (M, Ω) and then
considers the space J(Ω) of almost complex structures on M that Ω tames. We already
know from Lecture 5 that J(Ω) is not empty. We even know that the space K(Ω) ⊂ J(Ω)
of Ω-compatible almost complex structures is non-empty. Mo reover, it is not hard to show
that these spaces are contractible (see the Exercises).
◮ Thus, any invariant of the almost complex structures J ∈ J(Ω) or of the almost
K¨ ahler structuresJ ∈ K(Ω) that is constant under homotopy through such structures is
an invariant of the underlying symplectic manifold (M, Ω) .
This idea is extremely powerful. Gromov has used it to constr uct many new invariants
of symplectic manifolds. He has then gone on to use these inva riants to detect features of
symplectic manifolds that are not presently accessible by a ny other means.
Here is a sample of some of the applications of Gromov’s work o n holomorphic curves.
Unfortunately, I will not have time to discuss the proofs of a ny of these results.
Theorem 6: (Gromov) If there is a symplectic embedding of B2n(r) ⊂ R2n into
B2(R) × R2n−2, then r ≤R.
One corollary of Theorem 6 is that any diﬀeomorphism of a symp lectic manifold that
is a C0-limit of symplectomorphisms is itself a symplectomorphis m.
Theorem 7: (Gromov) If Ω is a symplectic structure on CP2 and there exists an
embedded Ω -symplectic sphere S ⊂ CP2, then Ω is equivalent to the standard symplectic
structure.
The next two theorems depend on the notion of asymptotic ﬂatn ess: We say that
a non-compact symplectic manifold M 2n is asymptotically ﬂat if there is a compact set
K1 ⊂M 2n and a compact set K2 ⊂ R2n so that M \K1 is symplectomorphic to R2n \K2
(with the standard symplectic structure on R2n).
Theorem 8: (McDuff) Suppose that M 4 is a non-compact symplectic manifold that
is asymptotically ﬂat. Then M 4 is symplectomorphic to R4 with a ﬁnite number of points
blown up.
L.9.11 162

Theorem 9: (McDuff, Floer, Eliashberg) Suppose that M 2n is asymptotically
ﬂat and contains no symplectic 2-spheres. Then M 2n is diﬀeomorphic to R2n.
It is not known whether one might replace “diﬀeomorphic” wit h “symplectomorphic”
in this theorem for n> 2.
Epilogue
I hope that this Lecture has intrigued you as to the possibili ties of applying the ideas
of Gromov in modern geometry. Let me close by quoting from Gro mov’s survey paper on
symplectic geometry in the Proceedings of the 1986 ICM:
Diﬀerential forms (of any degree) taming partial diﬀerenti al equations pro-
vide a major (if not the only) source of integro-diﬀerential inequalities needed for
a priori estimates and vanishing theorems. These forms are d eﬁned on spaces of
jets (of solutions of equations) and they are often (e.g., in Bochner-Weitzenbock
formulas) exact and invariant under pertinent (inﬁnitesim al) symmetry groups.
Similarly, convex (in an appropriate sense) functions on sp aces of jets are re-
sponsible for the maximum principles. A great part of hard an alysis of PDE will
become redundant when the algebraic and geometric structur e of taming forms
and corresponding convex functions is clariﬁed. (From the P DE point of view,
symplectic geometry appears as a taming device on the space o f 0-jets of solutions
of the Cauchy-Riemann equation.)
L.9.12 163

Exercise Set 9:
The Gromov School of Symplectic Geometry
1. Use the fact that an orientable 3-manifold M 3 is parallelizable (i.e., its tangent bundle
is trivial) and Theorem 1 to show that a compact 3-manifold ca n always be immersed in
R4 and a 3-manifold with no compact component can always be imme rsed in R3.
2. Show that Theorem 2 does, in fact imply that any connected no n-compact symplectic
manifold that has an almost complex structure has a symplect ic structure. (Hint: Show
that the natural projection Z 1(X,V ) →V has contractible ﬁbers (in fact, Z 1(X,V ) is an
aﬃne bundle over V , and then use this to show that a non-degenerate 2-form on X can
be homotoped to a closed non-degenerate 2-form on X.)
3. Show that the hypothesis in Theorem 3 that X either be non-compact or that dim(X)<
dim(Y ) is essential.
4. Show that if E is a symplectic bundle over a compact manifold M 2n whose rank is
2n + 2k for some k > 0, then there exists a symplectic splitting E = F ⊕T where T is
a trivial symplectic bundle over M of rank k. (Hint: Use transversality to pick a non-
vanishing section of E. Now what?)
Show also that, if E is a symplectic bundle over a compact manifold M 2n, then there
exists another symplectic bundle E′ over M so that E ⊕E′ is trivial. (Hint: Mimic the
proof for complex bundles.)
Finally, use these results to complete the proof of the Corol lary to Theorem 3.
5. Show that if a symplectic manifold M is simply connected, then the symplectic blow
up ˆM of M along a symplectic submanifold S of M is also simply connected. (Hint: Any
loop in ˆM can be deformed into a loop that misses ˆS. Now what?)
6. Prove, as stated in the text, that if M is compact and Ω tames J, then for any
Riemannian metric g on M (not necessarily compatible with either J or Ω) there is a
constantC >0 so that
|v ∧Jv | ≤ C Ω(v,Jv )
where |v∧Jv | represents the area in TpM of the parallelogram spanned by v andJv inTpM .
E.9.1 164

7. First Order Equations and Holomorphic Curves. The point of this problem is
to show how elliptic quasi-linear determined PDE for two fun ctions of two unknowns can
be reformulated as a problem in holomorphic curves in an almo st complex manifold.
Suppose thatπ:V 4 →X 2 is a smooth submersion from a 4-manifold onto a 2-manifold.
Suppose also that R ⊂ J 1(X,V ) is smooth submanifold of dimension 6 that has the
property that it locally represents an elliptic, quasi-lin ear pair of ﬁrst order PDE for
sections s of π. Show that there exists a unique almost complex structure on V so that
a section s of π is a solution of R if and only if its graph in V is an (unparametrized)
holomorphic curve in V .
(Hint: The hypotheses on the relation R are equivalent to the following conditions.
For every point v ∈ V , there are coordinates x,y,f,g on a neighborhood of v in V with
the property that x and y are local coordinates on a neighborhood of π(v) and so that a
local section s of the form f = F (x,y ), g = G(x,y ) is a solution of R if and only if they
satisfy a pair of equations of the form
A1fx +B1fy +C1gx +D1gy +E1 = 0
A2fx +B2fy +C2gx +D2gy +E2 = 0
where the A1,...,E 2 are speciﬁc functions of ( x,y,f,g ). The ellipticity condition is equiv-
alent to the assumption that
det
(
A1ξ +B1η C 1ξ +D1η
A2ξ +B2η C 2ξ +D2η
)
> 0
for all (ξ,η ) ⁄= (0, 0).)
Show that the problem of isometrically embedding a metric g of positive Gauss curva-
ture on a surface Σ into R3 can be turned into a problem of ﬁnding a holomorphic section
of an almost complex bundle π:V → Σ. Do this by showing that the bundle V whose
sections are the quadratic forms that have positive g-trace and that satisfy the algebraic
condition imposed by the Gauss equation on quadratic forms t hat are second fundamental
forms for isometric embeddings of g is a smooth rank 2 disk bundle over Σ and that the
Codazzi equations then reduce to a pair of elliptic ﬁrst orde r quasi-linear PDE for sections
of this bundle.
Show that, if Σ is topologically S2, then the topological self-intersection number of a
global section of V is −4. Conclude, using the fact that distinct holomorphic curve s in V
must have positive intersection number, that (up to sign) th ere cannot be more that one
second fundamental form on Σ that satisﬁes both the Gauss and Codazzi equations. Thus,
conclude that a closed surface of positive Gauss curvature i n R3 is rigid.
This approach to isometric embedding of surfaces has been ex tensively studied by
Labourie [La].
E.9.2 165

8. Prove, as claimed in the text that, for the map fλ: CP1 → CP2 given by the rule
fλ(t) = [t,λt 2,λ ] = [1,x,y ],
the pull-back of the Fubini-Study metric accumulates at the points t = 0 and t = ∞ and
goes to zero everywhere else. What would have happened if, in stead we had used the map
gλ(t) = [t,t 2,λ 2] = [1,x,y ]?
Is there a contradiction here?
9. Verify the claim made in the text that, for a symplectic mani fold (M, Ω), the spaces
K(Ω) and J(Ω) of Ω-compatible and Ω-tame almost complex structures on M are indeed
contractible. (Hint: Fix an element J0 ∈ K(Ω), with associated inner product ⟨, ⟩0 and
show that, for any J ∈ J(Ω), we can write J = J0(S +A) where S is symmetric and
positive deﬁnite with respect to ⟨, ⟩0 and A is anti-symmetric. Now what?)
10. The point of this exercise is to get a look at the pseudo-holo morphic curves of a non-
integrable almost complex structure. Let X 4 = C × ∆ = {(w,z ) ∈ C2
|z|< 1}, and give
X 4 the almost complex structure for which the complex valued 1- formsα =dw + ¯zd ¯w and
β =dz are a basis for the (1 , 0)-forms. Verify that this does indeed deﬁne a non-integrab le
almost complex structure on the 4-manifold X. Show that the pseudo-holomorphic curves
in X can be described explicitly as follows: If M is a Riemann surface and φ:M 2 →X is
a pseudo-holomorphic mapping, then one of the following is t rue: Either φ∗(β) = 0 and
there exists a holomorphic function h on M and a constant z0 so that
φ =
(
h − ¯z0 ¯h, z0
)
,
or else there exists a non-constant holomorphic function g on M that satisﬁes |g| < 1, a
meromorphic function f on M so that fdg and fgdg are holomorphic 1-forms without
periods on M , and a constant w0 so that
φ(p) =
(
w0 +
∫ p
p0
(fdg −fgdg ), g (p)
)
where the integral is taken to be taken over any path from some basepoint p0 to p in M .
(Hint: It is obvious that you must take g = φ∗(z), but it is not completely obvious
where f will be found. However, if g is not a constant function, then it will clearly be
holomorphic, now consider the “function”
f = φ∗(α)(
1 − |g|2)
dg
and show that it must be meromorphic, with poles at worst alon g the zeroes of dg.)
E.9.3 166

Bibliography
[A] V. I. Arnol’d, Mathematical Methods of Classical Mechanics, Second Editi on,
Springer-Verlag, Berlin, Heidelberg, New York, 1989.
[AH] M. F. Atiyah and N. Hitchin, The Geometry and Dynamics of Magnetic
Monopoles, Princeton University Press, Princeton, 1988.
[Bea] A. Beauville, Vari´ et´ es K¨ ahleriennes dont la premi` ere classe de Chernest nulle,
J. Diﬀerential Geom. 18 (1983), 755–782.
[Ber] M. Berger, Sur les groupes d’holonomie homog` ene des vari´ et´ es a connexion aﬃne
et des vari´ et´ es Riemanniennes,Bull. Soc. Math. France 83 (1955), 279–330.
[Bes] A. Besse, Einstein Manifolds , Springer-Verlag, Berlin, Heidelberg, New York, 1987.
[Ch] S.-S. Chern, On a generalization of K¨ ahler geometry , in Algebraic Geometry and
Topology: A Symposium in Honor of S. Lefshetz , Princeton University Press, 1957,
103–121.
[FGG] M. Fernandez, M. Gotay, and A. Gray, Four-dimensional parallelizable symplec-
tic and complex manifolds, Proc. Amer. Math. Soc. 103 (1988), 1209–1212.
[Fo] A. T. Fomenko, Symplectic Geometry, Gordon and Breach, New York, 1988.
[GL] K. Galicki and H.B. Lawson, Quaternionic Reduction and quaternionic orbifolds,
Math. Ann. 282 (1988), 1–21.
[GG] M. Golubitsky and V. Guillemin , Stable Mappings and their Singularities, Grad-
uate Texts in Mathematics 14, Springer-Verlag, Berlin, Heidelberg, New York, 1973.
[Gr 1] M. Gromov, Pseudo-holomorphic curves on almost complex manifolds, Inventiones
Mathematicae 82 (1985), 307–347.
[Gr 2] M. Gromov, Partial Diﬀerential Relations, Ergebnisse der Math., Springer-Verlag,
Berlin, Heidelberg, New York, 1986.
[Gr 3] M. Gromov, Soft and hard symplectic geometry, Proceedings of the ICM at Berkeley,
1986, 1987, vol. 1, Amer. Math. Soc., Providence, R.I., 81–9 8.
[GS 1] V. Guillemin and S. Sternberg, Geometric Asymptotics, Mathematical Surveys
14, Amer. Math. Soc., Providence, R.I., 1977.
[GS 2] V. Guillemin and S. Sternberg, Symplectic Techniques in Physics, Cambridge
University, Cambridge and New York, 1984.
[GS 3] V. Guillemin and S. Sternberg, Variations on a Theme of Kepler, Colloquium
Publications 42, Amer. Math. Soc., Providence, R.I., 1990.
[Ha] R. Hamilton, The inverse function theorem of Nash and Moser, Bulletin of the
AMS 7 (1982), 65–222.
Bib.1 167

[He] S. Helgason, Diﬀerential Geometry, Lie Groups, and Symmetric Spaces, Academic
Press, Princeton, 1978.
[Hi] N. Hitchin, Metrics on moduli spaces, in Contemporary Mathematics 58 (1986),
Amer. Math. Soc., Providence, R.I., 157–178.
[HKLR] N. Hitchin, A. Karlhede, U. Lindstr ¨om, and M. Ro ˇcek, HyperK¨ ahler metrics
and supersymmetry, Comm. Math. Phys. 108 (1987), 535–589.
[Ki] F. Kirwan, Cohomology of Quotients in Symplectic and Algebraic Geomet ry, Math-
ematical Notes 31, Princeton University Press, Princeton, 1984.
[KN] S. Kobayashi and K. Nomizu, Foundations of Diﬀerential Geometry, vols. I and II ,
John Wiley & Sons, New York, 1963.
[Kr] P. Kronheimer, The construction of ALE spaces as hyper-K¨ ahler quotients , J. Dif-
ferential Geometry 29 (1989), 665-683.
[La] F. Labourie, Immersions isom´ etriques elliptiques et courbes pseudo-holomorphes, J.
Diﬀerential Geometry 30 (1989), 395-424.
[M 1] D. McDuff, Symplectic diﬀeomorphisms and the ﬂux homomorphism, Inventiones
Mathematicae 77 (1984), 353–366.
[M 2] D. McDuff, Examples of simply-connected symplectic non-K¨ ahlerian m anifolds,
J. Diﬀerential Geom. 20 (1984), 267–277.
[M 3] D. McDuff, Examples of symplectic structures, Inventiones Mathematicae 89 (1987),
13–36.
[M 4] D. McDuff, Symplectic 4-manifolds, Proceedings of the ICM at Kyoto, 1990, to
appear
[M 5] D. McDuff, Elliptic methods in symplectic geometry, Bull. Amer. Math. Soc. 23
(1990), 311–358.
[MS] J. Milnor and J. Stasheff, Characteristic Classes, Annals of Math. Studies 76,
Princeton University Press, Princeton, 1974.
[Mo] J. Moser, On the volume element on manifolds, Trans. Amer. Math. Soc. 120
(1965), 280–296.
[Pa] P. Pansu, Pseudo-holomorphic curves in symplectic manifolds, preprint, ´Ecole Poly-
technique, Palaiseau, 1986.
[Po] I. Postnikov, Groupes et alg` ebras de Lie, (French translation of the Russian original),
´Editions Mir, Moscow 1985.
[Sa] S. Salamon, Riemannian geometry and holonomy groups , Pitman Research Notes in
Math. no. 201, Longman scientiﬁc & Technical, Essex, 1989.
[Si] Y. T. Siu, Every K3 surface is K¨ ahler, Inventiones Math. 73 (1983), 139–150.
Bib.2 168

[SS] I. Singer and S. Sternberg, The inﬁnite groups of Lie and Cartan, I (The transitive
groups), Journal d’Analyse 15 (1965).
[Wa] F. W arner, Foundations of Diﬀerentiable Manifolds and Lie Groups, Springer-
Verlag, Berlin Heidelberg New York, 1983.
[We] A. Weinstein, Lectures on Symplectic Manifolds, Regional Conference Series in
Mathematics 29, Amer. Math. Soc., Providence, R.I., 1976.
[Wo] J. Wolfson, Gromov’s compactness of pseudo-holomorphic curves and sym plectic
geometry, J. Diﬀerential Geom. 28 (1988), 383–405.
[Ye] R. Ye, Gromov’s compactness theorem for pseudo-holomorphic curv es, Transactions
of the AMS , to appear.
Bib.3 169

