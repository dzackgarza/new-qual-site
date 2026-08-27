Symplectic Geometry
Spring School, June 7–14, 2004, Utrecht
J.J. Duistermaat
Department of Mathematics, Utrecht University, Postbus 80.010, 3508 TA Utrecht, The
Netherlands. E-mail: duis@math.uu.nl
Contents
1 Symplectic Linear Algebra 2
1.1 Symplectic Forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Orthogonal Complements in the Dual Space . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Orthogonal Complements for a Bilinear Form . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Isotropic Subspaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 Standard Form of the Sympctic Form . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.6 The Lagrangian Grassmannian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.7 The Symplectic Linear Group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.8 Exterior Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.9 Hermitian Forms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.10 Historical Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.11 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2 Symplectic Manifolds 12
2.1 Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2 The Cotangent Bundle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3 Reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.4 Complex Projective Varieties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.5 Almost Complex Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.6 Cohomology Classes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3 Hamiltonian Systems 18
3.1 Flows of Vector Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.2 Lie Derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3 Hamiltonian Vector Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.4 The Legendre Transform . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.5 Poisson Brackets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3.6 Darboux’s Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.7 Hamiltonian Group Actions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.8 Poisson Structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.9 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
1

4 Hamilton-Jacobi Theory 33
4.1 Lagrange Manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.2 Lie’s View on First Order PDE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.3 An Initial Value Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.4 Ray Bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
4.5 High Frequency Waves and Fourier Integral Operators . . . . . . . . . . . . . . . . . 38
4.6 Some History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
1 Symplectic Linear Algebra
1.1 Symplectic Forms
LetE be a ﬁnite-dimensional vector space over a ﬁeldk, which later usually will be R. A symplectic
form on E is a nondegenerate two-form σ on E. Here the word ”two-form” means that σ is an
antisymmetric bilinear form on E. A bilinear form onE is a mapping σ :E×E→k such that, for
every choice of u∈E, v↦→σ(u, v) :E→k is a linear form and, for every choice of v∈E, σ(u, v)
depends linearly on u. The bilinear form σ is called antisymmetric if
σ(v, u) =−σ(u, v), u, v ∈E. (1.1)
The bilinear form σ is called nondegenerate if σ(u, v) = 0 for every v∈E implies that u = 0.
As usual, we identify a bilinear form σ on E with the linear mapping u↦→ (v↦→σ(u, v)) from
E to the dual spaceE∗ ofE, this linear map will also be denoted by σ. The mapping which assigns
to v∈E the linear form α↦→α(v) on E∗ induces a linear isomorphism from E onto (E∗)∗, which
is used to identify ( E∗)∗ with E. Then the dual (= transposed) mapping σ∗ of the linear map
σ :E→E∗ is a linear mapping from (E∗)∗ =E to E∗ and the antisymmetry of σ is equivalent to
the condition that σ∗ =−σ.
The nondegeneracy of σ means that the linear mapping σ : E→ E∗ has zero kernel (= null
space), and because dim E∗ = dimE, this is equivalent to the condition that the linear mapping
σ :E→E∗ is bijective.
More generally, any linear mapping from E toE∗ corresponds in the above fashion to a unique
bilinear form on E, and the linear mapping E→ E∗ is bijective (= an isomorphism) if and only
if the bilinear form is nondegenerate. In the case that the bilinear form is an inner product, i.e.
symmetric and positive deﬁnite, then it is nondegenerate and we obtain the usual identiﬁcation of
E with E∗ by means of the inner product. In this way we may think of a symplectic form as an
antisymmetric analogue of an inner product.
Example 1.1 On k2n =kn×kn we deﬁne σ by
σ((p, q), (p′, q′)) =
n∑
j=1
pjq′
j−p′
jqj. (1.2)
It is easy to verify that σ is a nondegenerate antisymmetric bilinear form on kn×kn. It is called
the standard symplectic form on kn×kn. A coordinate free version is the symplectic form on
E =F×F∗ deﬁned by
σ((x, ξ), (y, η)) =ξ(y)−η(x), x, y ∈F, ξ, η ∈F∗,
2

deﬁned for any ﬁnite-diemnsional vector space F overk. ⊘
1.2 Orthogonal Complements in the Dual Space
If L is a linear subspace of E, then the orthogonal complement or annihilator L0 of L in E∗ is
deﬁned as the set of all α∈E∗ such that α(v) = 0 for every v∈L. Clearly L0 is a linear subspace
of E∗ and dimL0 = dimE∗− dimL = dimE− dimL = the codimension of L in E.
Similarly the orthogonal complement or annihilator A0 in E of a linear subspace A of E∗ is
deﬁned as the common kernel of all the linear forms α∈ A, i.e. the set of all v∈ E such that
α(v) = 0 for every α∈A. A0 is a linear subspace of E and dimA0 = dimE− dimE.
If L is a linear subspace of E, then obviously L⊂ (L0)0, and because dim( L0)0 = dimE−
dimL0 = dimE− (dimE− dimL) = dimL, we conclude that L = (L0)0. Similarly A = (A0)0 for
any linear subspace A of E∗.
If L and M are linear subspaces of E, then obviously L⊂ M implies M 0⊂ L0. Therefore in
generalL0⊂ (L∩M)0 andM 0⊂ (L∩M)0, which implies that L0 +M 0⊂ (L∩M)0, and similarly
(L +M)0⊂L0∩M 0. Taking orthogonal complements these inclusions imply that
L∩M = ((L∩M)0)0⊂ (L0 +M 0)0⊂ (L0)0∩ (M 0)0 =L∩M,
It follows that both inclusions are equalities and therefore (L∩M)0 =L0 +M 0. Similiarly we have
(L +M)0 =L0∩M 0.
1.3 Orthogonal Complements for a Bilinear Form
Let σ be a nondegenerate bilinear form on E, not necessarily antisymmetric. If L is a linear
subspace of E, then the σ-orthogonal complement Lσ of L in E is deﬁned as
Lσ := (σ(L))0 ={u∈E|σ(u, v) = 0 for every v∈L}. (1.3)
ClearlyLσ is a linear subspace of E. Note that Lσ =Lσ∗
ifσ is symmetric or antisymmetric. That
is, in these case we can interchange the role of u and v in the deﬁnition (1.3).
Becauseσ :E→E∗ is a linear isomorphism, the rules for annihilators in the dual spaces imply
the rules
dimLσ = dimE− dimL, (1.4)
L⊂M =⇒Mσ⊂Lσ, (1.5)
(L∩M)σ =Lσ +Mσ and ( L +M)σ =Lσ∩Mσ (1.6)
for the σ-orthogonal complements. If k = R and σ is an inner product, then the σ-orthogonal
complement ofL is usual orthogonal complement denoted by L⊥, and we recognize (1.4), (1.5) and
(1.6) as familiar properties of the orthogonal complementation. Note that for the inner product we
have the additional property that L∩L⊥ ={0}, which implies that E is equal to the direct sum
L⊕L⊥ of L and L⊥.
3

1.4 Isotropic Subspaces
In the sequel ( E, σ) will be a symplectic vector space, i.e. E is a ﬁnite-dimensional vector space
and σ is a symplectic form on E.
A linear subspace L is called isotropic with respect to σ if L⊂ Lσ, that is σ(u, v) = 0 for all
pairs of vectors u, v∈ L. A maximal isotropic linear subspace of E is called a Lagrange plane.
Because of the ﬁnite-dimensionality of E, any striclty increasing sequence of isotropic subspaces
terminates at a maximal one, which shows that every isotropic subspace is contained in at least
one Lagrange plane.
The antisymmetry of σ implies that σ(v, v) =−σ(v, v), hence 2σ(v, v) = 0. Therefore, if the
characteristic of k is not equal to two, the antisymmetry (1.1) implies that
σ(v, v) = 0, v ∈E. (1.7)
Conversely, if (1.7) holds, then 0 = σ(u +v, u+v) = σ(u, u) +σ(u, v) +σ(v, u) +σ(v, v) =
σ(u, v) +σ(v, u), which implies (1.1). Therefore, if char k⁄= 2, such as for k = R, then (1.1)
is equivalent to (1.7). If char k = 2, then everything what follows remains true if we replace the
antisymmetry condition (1.1) by the stronger condition (1.7).
The condition (1.7) implies that every one-dimensional linear subspace of E is isotropic. This
is very diﬀerent from the situation for an inner product, where {0} is the only isotropic subspace.
If L⊂ Lσ and L⁄= Lσ, then for every v∈ Lσ\L we have that ( L +kv )σ = Lσ∩ (kv )σ
contains L because Lσ⊃ L and kv ⊂ Lσ implies (kv )σ⊃ L. it also contains v because v∈ Lσ
and v∈ (kv )σ. It follows that the linear subspace ( L +kv )σ contains L +kv , which means that
L′ :=L+kv is isotropic,L⊂L′ and dimL′ = dimL+1. We conclude that L is a maximal isotropic
linear subspace if and only if L = Lσ. This is equivalent to the condition that L is isotropic and
dimL = dimLσ = dimE− dimL, or equivalently dimE = 2 dimL.
In particular the dimension of a symplectic vector space must be even, say equal to 2 n. We
have that dim L≤ n for every isotropic linear subspace L of E and that the maximal isotropic
subspaces are the isotropic subspaces which have dimension equal to n.
1.5 Standard Form of the Sympctic Form
In order to identify the symptic form with the standard one of Example 1.1, we start with an
L∈L (E, σ) and introduce a second M ∈L (E, σ) such that L∩M ={0}, which then implies
thatE =L⊕M. The existence of such a Lagrange plane M follows from the fact that, if M is an
isotropic subspace of (E, σ) such that M⁄=Mσ andL∩M ={0}, then there exists a v∈Mσ\M
such that L∩M′ ={0} if M′ := M +kv . If L∩M′⁄={0} then there exist m∈ M and c∈ K
such that l =m +cv is a nonzero element of L, which means that v∈L +M. If this would hold
for every v∈Mσ\M, then Mσ\L +M, which implies that L∩Mσ =Lσ∩Mσ = (L +M)σ⊂
(Mσ)σ = M, which in view of L∩M ={0} means that L∩Mσ ={0}. However, dim L = n
and dimMσ = dimE− dimM >dimE−n, hence dim L + dimMσ > dimE, which implies that
dim(L∩Mσ) = dimL + dimMσ− dimE >0, and we arrive at a contradiction.
The restriction S to M of the mapping m↦→ (σm )|L is a linear isomorphism form M ontoL∗.
Indeed,Sm = 0 means thatm∈Lσ =L, which in view ofL∩M ={0} implies thatm = 0. Now let
ei be a basis ofL and letϵj be the corresponding dual basis ofL∗, determined by the conditions that
ϵj(ei) is equal to zero and zero wheni⁄=j andi =j, respectively. Letfj be the basis ofM such that
Sfj = ϵj. Then we have σ(ei, ei′) = 0, σ(fj, fj′) = 0 and −σ(ei, fj) = σ(fj, ei) = ϵj(ei) = δij.
4

The ei and fj together form a basis on which σ has a standard form. Such a basis is called a
symplectic basis of (E, σ).
More precisely, if we write u =∑n
i=1 piei +qjfj, v =∑n
i=1 p′
iei +q′
jfj, then it follows that
σ(u, v) is equal to the right hand side of (1.2). This means that the pull-back of σ under the linear
isomorphism (p, q)↦→∑n
i=1 piei +qjfj from kn×kn onto E is equal to the standard symplectic
form on kn×kn.
For an arbitrary antisymmetric bilinear form σ on a ﬁnite-dimensional vector space E over a
ﬁeld k, a basis on which σ has a standard form is obtained as follows. If N = kerσ, then the
equation σE/N(u +N, v+N) = σ(u, v) leads to a well-deﬁned antisymmetric bilinear form on
E/N which is nondegenerate, this is called the induced symplectic form onE/N. Write r = dimN,
m = 1
2 dim(E/N), and choose n1, ...nr, e1, ...em, f1, ..., fm inE such that the n1, ...nr from a
basis ofN and thee1 +N, ...em +N, f1 +N, ..., fm +N form a symplectic basis of (E/N, σE/N).
Then these r + 2m vectors for a basis of E, for which σ(ni, nj) = σ(ni, ej) = σ(ni, fj) = 0,
σ(ei, ej) =σ(fi, fj) = 0, and σ(ei, fj) =−σ(fj, ei) =δij.
The fact that antisymmetric bilinear forms on vector spaces of the same dimension and with
the same nullity (= dimension of the kernel) have the same normal form, diﬀers from the situation
for symmetric bilinear forms. If k has the property that every element of k has a square root in
k, then all symmetric bilinear forms with the same nullity have the same normal form, but for
general ﬁelds the classiﬁcation of symmetric bilinear forms can be very complicated. For k = R the
situation still is relatively simple, as a real symmetric bilinear form is determined by its nullity n0,
and its positive and negativity index = the dimension n+ and n− of any maximal linear subspace
on which the form is positive deﬁnite and negative deﬁnite, respectively.
1.6 The Lagrangian Grassmannian
The set L =L(Eσ ) of all Lagrange planes in the symplectic vector space ( E, σ) is called the
Lagrangian Grassmannian of (E, σ). It is a non-empty algebraic subvariety of the Grassmann
manifold Gn(E) of all n-dimensional linear subspaces of E.
If L∈L and k∈ Z≥0, then we denote by LL,k the set of all M∈L such that dimL∩M =k.
LL, 0 is an open subset of L, and in the previous subsection we have seen that it is not empty.
Interchanging the roles of L andM we obtain that theLL, 0 forL∈L form an open covering ofL,
i.e. for every M∈L there exists an L∈L such that M∈L L, 0.
LetL, M∈ Gn(E) be such thatE =L⊕M. For everyL′∈ Gn(E) such thatL′∩M ={0} there
is a unique linear mapping A :L→M such that L′ ={x +Ax|x∈L}. This leads to a bijctive
mapping from the open subset {L′∈ Gn(E)| L′∩M ={0}} of Gn(E) onto the n2-dimensional
vector space Lin(L, M) of all linear mappings from L onto M, and the matrix coeﬃcients of A
with respect to any bases in L and M deﬁne a coordinatization of the aformentioned open subset
of Gn(E). These are the standard coordinatizations of Gn(E). The coordinate changes are rational
mappings and in this way Gn(E) is exhibited as a smooth n2-dimensional manifold.
Now assume thatL, M∈L (E, σ). We have thatL′∈L (E, σ) if and only if, for everyx, y∈L,
0 =σ(x +Ax, y+Ay ) =σ(Ax, y) +σ(x, Ay) =σ(Ax, y)−σ(Ay, x),
where we have used in the second identity that σ(x, y) = 0 and σ(Ax, Ay) = 0 because L and M
are isotropic. This means that the bilinear form ( x, y)↦→ σ(Ax, y) on L is symmetric. Because
A↦→ ((x, y)↦→ σ(Ax, y)) is a linear isomorphism from Lin( L, M) onto the space of all bilinear
5

forms on L, we see that in the aforementioned coordinatization the Lagrangian Grassmannian
appears as the space of all symmetric bilinear forms on L, viewed as a linear subspace of the
space of all bilinear forms on L. This exhibits L(E, σ) as a smooth 1
2n(n + 1)-dimensional linear
submanifold of the n2-dimensional manifold Gn(E).
If ~M is another Lagrange plane which is transversal to L and L′∈L is transversal to both
M and ~M, then we have a second coordinatization of L′ by means of the ~A∈ Lin(L, ~M) such
that L′ ={y + ~Ay | y ∈ L. On the other hand there exists B ∈ Lin(M, L) such that ~M =
{z +Bz | z∈ M}. The elements of L′ are of the form x +Ax = y + ~Ay for unique x, y∈ L,
and ~Ay = z +Bz for a unique z∈ M. Therefore z = Ax , y = x−Bz = x−BAx , hence
x +Ax = (x−BAx ) + ~A (x−BAx ). Taking the symplectic product with u∈L, this leads to
σ(Ax, u) =σ(~A (x−BAx ), u) =σ(~Ax, u)−σ(~ABAx, u ).
For small A, which corresponds to L′ close to L, we see that the symmetric bilinear form on L
deﬁned by the M diﬀers from the symmetric bilinear form on L deﬁned by ~M by a term which
vanishes of second order in A. In this way the tangent space TLL ofL at the element L∈L is
canonically identiﬁed with the space Symm2(L) of all symmetric bilinear forms on L.
1.7 The Symplectic Linear Group
Let (E, σ), (F, τ) be a symplectic vector spaces over a ﬁeld k. A linear mapping A : E→ F is
called a symplectic linear mapping from (E, σ) to (F, τ), if τ(Au, Av) =σ(u, v) for all u, v∈E,
or A∗τA = σ. Because σ : E→ E∗ is injective, A is injective, hence dim E≤ dimF , and we
have that A is bijective if and only dim E = dimF , in which case A is called a symplectic linear
isomorphism from (E, σ) onto (F, τ). If dimE <dimF , thenA is a symplectic linear isomorphism
from (E, σ) onto the symplectic vector subspace (A(E), τ|A(E)×A(E) of (F, τ).
A symplectic linear mapping from ( E, σ) to itself is called a symplectic linear transformation
in (E, σ). The symplectic linear transformations form an algebraic subgroup of the group GL( E)
of all linear transformations in E, which is called the symplectic linear group Sp(E, σ).
If e1, ..., en, f1, ..., fn is a symplectic basis, then a linear mapping A is symplectic if and
only if Ae 1, ..., Aen, Af1, ..., Afn is a symplectic basis. Because any basis of a Lagrange plane
can be extended to a symplectic basis, it follows that the symplectic linear group Sp( E, σ) acts
transitively on the Lagrangian Grassmannian Sp( E, σ). If, for given L∈L (E, σ), Sp(E, σ)L :=
{A∈ Sp(E, σ)|A(L) =L} denotes the stabilizer subgroup of L in Sp(E, σ), then the Lagrangian
GrassmanninaL(E, σ) is identiﬁed with the homogeneous space Sp( E, σ)/ Sp(E, σ)L.
If we write A =
( α β
γ δ
)
on a symplectic basis, in which α, β, γ, δare n×n-matrices, then
A∈ Sp(E, σ) if and only if α∗γ−γ∗α = 0, β∗δ−δ∗β = 0 and α∗δ−β∗γ = I. The ﬁrst two
equations mean that α∗γ =ϵ andβ∗δ =η are symmetric, and we see 2( 1
2n(n− 1)) +n2 = 2n2−n
independent equations. If the ﬁrst n vectors of the symplectic basis span L, then A∈ Sp(E, σ)L if
and only if γ = 0, and the equations are that δ = (α∗)−1 andδ∗β =α−1β is symmetric. It follows
that dim Sp(E, σ)L = n2 + 1
2n(n + 1), and therefore dim Sp( E, σ) = n2 +n(n + 1) = 2n2 +n.
It follows that the codimension of Sp( n, E) in GL(E) is equal to 2 n2−n, in agreement with the
number of independent equations for the matrices α, β, γ, δ.
The equation A∗σA = σ for A∈ Sp(E, σ) implies that A∗ = σAσ −1, which means that the
linear isomorphism σ :E→E∗ conjugates the linear mapping A :E→E with the linear mapping
6

(A∗)−1 :E∗→E∗. This implies that A has the same eigenvalues as (A∗)−1 with the same algebraic
multiplicities. Because A∗ has the same eigenvalues with the same algebraic multiplicities as A, it
follows that if λ is an eigenvalues ofA with algebraic multiplicitym, then 1/λ is also an eigenvalue
of A with algebraic multiplicity m. If k = R, then a passage to the complexiﬁcation leads to the
conclusion that the the complex eigenvalues of A appear in foursomes λ, λ, 1/λ, 1/λ with λ∈ C,
λ /∈ R, λλ⁄= 1, or in real pairs λ, 1/λ, or in complex conjugate pairs on the unit circle, in each
case with equal algebraic multiplicities.
The Lie algebra sp(E, σ) of Sp(E, σ) consists of the linear mappings A : E→ E such that
σ(Au, v) +σ(u, Av) = 0 for all u, v∈E, or σA +A∗σ = 0. These A are called the inﬁnitesimal
symplectic linear transformations in (E, σ). Note also that the mapping which assigns to A∈
sp(E, σ) the bilinear form σA : (u, v)↦→σ(Au, v) is a linear isomomorphism from sp(E, σ) onto
the space Symm 2(E) of all symmetric bilinear forms on E. This shows that dim Sp( E, σ) =
1
2 2n(2n + 1) = 2n2 +n, in agreement with our previous dimension calculations.
The equation A∗ =−σAσ −1 implies that if λ is an eigenvalues of A with multiplicity m, then
−λ is also an eigenvalue of A with m,ultiplicity m. When k = R, this implies that the complex
eigenvalues of A appear in foursomes λ, λ,−λ,−λ with λ∈ C, λ /∈ R, λ /∈ i R, or in real pairs
λ,−λ, or in complex conjugate pairs on the imaginary axis, in each case with equal algebraic
multiplicities.
Fork = R a complete list of normal forms of inﬁnetesimal symplectic linear transformations
has been given by Williamson [30], and one has a corresponding list for the symplectic linear
transformations, see also [2] and [4].
1.8 Exterior Algebra
LetE be anyd-dimensional vector space overk. The space of all antisymmetric p-linear forms onE
is denoted by ΛpE∗. For α∈ ΛpE∗ andβ∈ ΛqE∗, one deﬁnes the exterior product α∧β∈ Λp+qE∗
by
(α∧β)(v1, ..., vp+q) =
∑
π
sgnπα (vπ(1), ..., vπ(p))β(vπ(p+1), ..., vπ(p+q)) (1.8)
for all v1, ..., vp+q∈E. Here the sum is over all equivalence classes of permutations permutations
π of the indices{1, ..., p+q}, where π and π◦ψ are equivalent if ψ maps the subsets{1, ..., p}
and{p + 1, ..., p+q} of indices to themselves. (Note that terms with equivalent permutations
are equal.) The signature sgn π of the permutation is +1 or −1 when π consists of an even or odd
number of transpositions, respectively.
With this product,
ΛE∗ :=
⨁
p≥0
ΛpE∗
becomes an algebra, which is called the exterior algebra of E∗. Here we have used the convention
that Λ0E∗ =k. Note also that Λ 1E∗ =E∗ is a linear subspace of ΛE∗.
The exterior product is associative, meaning that (α∧β)∧γ =α∧(β∧γ). It is anticommutative
in the sense that α∧β = (−1)pqβ∧α if α∈ ΛpE∗ and β∈ ΛqE∗.
Letei be any basis of E andϵj de corresponding dual basis of E∗, characterized byϵj(ei) =δij.
For any strictly increasing function I :{1, ..., p} → {1, ..., d}, write ϵI = ϵI(1)∧ ... ∧ ϵI(p)
and eI = (eI(1), ..., eI(p)). Then ϵI(eJ) = δIJ . Therefore, if α∈ ΛpE∗, then α = ∑
I α(eI)ϵI,
which follows from applying both sides to eJ and observing that the numbers α(eJ) determine α.
7

Conversely, if∑
I cIϵI = 0, then application to eJ yields cJ = 0 for every J, and it follows that
the ϵI form a basis of ΛpE∗, which in turn implies that
dim ΛpE∗ =
( d
p
)
. (1.9)
In particular Λ pE∗ ={0} when p > nand the space Λ dE∗ of oriented volume forms on E is
one-dimensional.
If σ ∈ Λ2E∗ is a symplectic form on E and (e1, ...en, f1, ...fn) is a symplectic basis, with
corresponding dual basis (ϵ1, ...ϵn, φ1, ..., φn), then we see from (1.2) that
σ =
n∑
i=1
ϵi∧φi (1.10)
and therefore the n-the exterior power
σn =σ∧ ... ∧σ =n!ϵ1∧φ1∧ϵ2∧φ2∧... ∧ϵn∧φn (1.11)
of σ is a nonzero volume form on E. (Note that the exterior product is commutative on the
subalgebra generated by the two-forms ϵi∧φi.) Here we assume that the ﬁeld k has characteristic
zero or, in the case of nonzero characteristic, chark>n . This implies that also all the intermediate
powersσm∈ Λ2mE∗, 0≤m≤n, are nonzero.
With the identiﬁcation of E with (E∗)∗, the exterior algebra Λ E of E is deﬁned as the algebra
of antisymmetric multilinear forms on E∗. There is an natural identiﬁcation of λE with the dual
space of ΛE∗ and vice versa, as follows.
If v∈ (ΛpE∗)∗, then
i(v)(α1, ..., αp) :=v(α1∧... ∧αp), α i∈E∗,
deﬁnes an antisymmetric p-linear form on E∗, and therefore belongs to Λ pE. This deﬁnes a linear
mapping i : (ΛpE∗)∗ → ΛpE. Furthermore, if i(v) = 0, then v annihilates all p-fold exterior
products of one-forms and therefore v = 0 because the ϵI form a basis of ΛpE∗. We conclude that
i is injective and because
dim(ΛpE∗)∗ =
( d
p
)
= dim ΛpE,
we conclude that i is a linear isomorphism.
We have a similar linear isomorphismj : (ΛpE)∗→ ΛpE∗. If v1∧...∧vp =i(v) andα1∧...α p =
j(α), then
α(i(v)) = j(α)(v1, ..., vp) = (α1∧... ∧αp)(v1, ..., vp) =
∑
π
sgnπ
p∏
k=1
αk(vπ(k))
= ( v1∧... ∧vp)(α1, ..., αp) =i(v)(α1, ..., αp) =v(j(α)),
which shows that the mappings i and j are each others adjoints.
One uses i and j to identify (ΛpE∗)∗ with ΛpE and (ΛpE)∗ with ΛpE∗. With these identiﬁca-
tions, one has the formulas v(α1∧... ∧αp) = v(α1, ...αp) for v∈ (ΛpE∗)∗ = ΛpE and αi∈ E∗,
and similarly α(v1∧...v p) =α(v1, ..., vp) for α∈ (ΛpE)∗ = ΛpE∗ and vi∈E.
8

1.9 Hermitian Forms
Let E be an n-dimensional vector space over C and let h : E×E→ C be a Hermitian form on
E, i.e. for every u∈ E the mapping v↦→ h(u, v) is complex antilinear ( h(u, cv) = ch (u, v)), for
everyv∈E the mapping u↦→h(u, v) is complex linear, and h(v, v)> 0 for every nonzero element
v of E.
From now on we regardE as a 2n-dimensional vector space overR. Then the real partg := Reh
of h is an inner product on E, and therefore a nondegenerate symmetric bilinear form. Because
Imh(u, v) =− Re(ih(u, v)) =− Reh(iu, v) =− Reh(v, iu) = Re(ih(v, u)) =− Imh(v, u),
we see that the imaginary part σ := Imh is an antisymmetric bilinear form on E. These equations
also show thatσ =−g◦J, ifJ :E→E is the real linear transformation inE deﬁned byJ(u) = iu,
u∈ E, the complex multiplication by means of the complex number i. Because J : E→ E and
g :E→E∗ are injective, σ :E→E∗ is injective as well, and we conclude that σ is a symplectic
form on E. Note that J2 =−1 and therefore g can also be expressed in terms of σ by means of
the formula g =σ◦J, and the Hermitian form is equal to h =σ◦J + iσ.
In general, ifE is a vector space over R, then a complex structure inE is deﬁned as a real linear
mapping J : E→ E such that J2 =−1. This makes E into a complex vector space if we deﬁne
(a + ib)v =av +J(bv ) for any a, b∈ R and v∈E, and it follows that the real dimension of E is
equal to 2n if n denotes the dimension of E as a complex vector space.
That every symplectic form is equal to the imaginary part of a Hermitian form with respect to
a suitable complex structure, can be seen by bringing the symplectic form into the standard form
(1.2), writing zj =qj + ipj and taking the standard Hermitian form
h(z, z′) =
n∑
j=1
zjz′
j (1.12)
in Cn.
The vectors e1, ..., en∈E form an h-orthonormal basis of the complex vector space E, if and
only if they form a g-orthonormal basis of a Lagrange plane L. Let U( E, h) denote the unitary
group of all complex linear transformationsA :E→E such thatA∗(h) =h, in which the Hermitian
form A∗h on E is deﬁned by (A∗h)(u, v) =h(Au, Av) for all u, v∈E. Note that
U(E, h) = GLC(E)∩ O(E, g) = GLC(E)∩ Sp(E, σ) = Sp(E, σ)∩ O(E, g),
in which GLC(E) denotes the group of complex linear transformations oin E and O(E, g) denotes
the group of g-orthogonal real linear transformations in E. This is based on the fact that a real
linear transformation A in E is complex linear if and only if A◦J = J◦A, and g = σ◦J and
h =g + iσ.
Because U(E, h) acts transitively on the set of all h-orthonormal bases of E, the compact
Lie group U(E, h) also acts transitively on the Lagrangian Grassmannian. Because for any A∈
U(E, h) we have that A(L) = L if and only if A is the complex linear extension to E of a g-
-orthogonal transformation in L, this leads to an identiﬁcation of L(E, σ) with the homogeneous
space U(E, h)/ U(E, h)L, in which U(E, h)L is isomorphic to O(L, g). This is the meaning of the
equation Λ(n) = U(n)/ O(n) in [1].
9

1.10 Historical Remarks
The name ”symplectic” has been introduced in 1939 by Hermann Weyl as the Greek adjective
corresponding to the word ”complex”, which for him referred to the linear line complexes introduced
by Pl¨ ucker, see Exercise 1.3. According to the footnote on p. 165 of [29]:
The name ”complex group” formerly advocated by me in allusion to line complexes, as they are
deﬁned by the vanishing of antisymmetric forms, has become more and more embarassing through
collision with the word ”complex” in the connotation of complex number. I therefore propose to
replace it by the corresponding Greek adjective ”symplectic”. Dickson calls the group ”Abelian
linear group” in homage to Abel who ﬁrst studied it.
(The name given by Dickson is even more embarassing, as ”Abelian group” nowadays is used for
”commutative group”, whereas the symplectic group is highly noncommutative.)
The names ”Lagrange plane” and ”Lagrangian Grassmannian” have been introduced by Arnol’d
[1], after the name ”Lagrange manifold”, introduced by Maslov [23, p. 115] in 1965 for a manifold
of which all tangent spaces are Lagrange planes.
1.11 Exercises
Exercise 1.1 In the notation of Subsection 1.9, prove that J∈ Sp(E, σ). Prove that if L is a
Lagrange plane, then J(L) is a Lagrange plane which is g-orthogonal to L, and therefore satisﬁes
J(L)∩L ={0}. ⊘
Exercise 1.2 It was the idea of Pl¨ ucker (1846), to consider the projective lines in the three-
dimensional space as the elements (points) of a new space. The three-dimensional projective space
is deﬁned as the space P(E) of all one-dimensional linear subspaces l of the four-dimensional vector
spaceE. A projective line is equal to the set P(L) of all one-dimensional linear subspacesl of a two-
dimensional linear subspace L of E. In this way, Pl¨ ucker’s space is identiﬁed with the Grassmann
manifold G2(E) of all two-dimensional linear subspaces L of the four-dimensional vector space E.
Let a, b∈ E be linearly independent. Prove that u = a∧b is a nonzero element of Λ 2E such
that u∧u = 0. Prove that every nonzero u∈ Λ2E such that u∧u = 0 arises in this way, and
that x∈ E is equal to a linear combination of a and b, if and only if u∧x = 0. Prove that the
relation between L∈ G2(E) and u∈ Λ2E, that u = a∧b for a basis a, bof L, is equivalent to
u∧x = 0 for every x∈ L. Prove that this relation deﬁnes a bijection between G 2(E) and the
quadric Q in the ﬁve-dimensional projective space P
(
Λ2E
)
deﬁned by the equation u∧u = 0.
Prove that (u, v)↦→ u∧v is a nondegenerate symmetric bilinear form on Λ 2E with values in the
one-dimensional vector space Λ 4E, and that, as a consequence, the quadric Q is smooth.
The co¨ ordinates of Λ2E are called Pl¨ ucker coordinateson G 2(E). Stricly speaking these should
be regarded as projective co¨ ordinates and, as functions on the projective coordinate patches of
P
(
Λ2E
)
, be restricted to the quadric Q. ⊘
Exercise 1.3 Pl¨ ucker [26] deﬁned aline complex of degree m as the intersection of Q with an
algebraic hypersurface in P
(
Λ2E
)
of degree m, deﬁned by the equation F (u) = 0 in which F is a
homogeneous polynomial of degree m on Λ2E. He deﬁned a linear line complex as a line complex
of degree one.
10

Prove that a linear line complex corresponds to a nonzero two-form σ∈ Λ2E∗ on E, unique up to
a nonzero scalar multiple, such that L∈ G2(E) belongs to the linear line complex if and only if L
is σ-isotropic. Prove that if σ is nondegenerate, then the linear line complex deﬁned by σ, viewed
as a subset of G 2(E), is equal to the manifold L(E, σ) of all the Lagrange planes with respect to
the symplectic form σ.
Prove that if σ is degenerate, then ker σ∈ G2(E). In this case Pl¨ ucker called the corresponding
linear line complex special and called kerσ the axis of the special linear line complex. Prove that
the special linear line complex is equal to the set of all L∈ G2(E) such that L∩ kerσ⁄= 0. In
terms of projective lines: the special line complex is equal to the set of all projective lines which
intersect its axis. ⊘
Exercise 1.4 We use the notation of Subsection 1.6.
Let L∈L (E, σ), I ∈ Gm(L). Prove that σ induces a symplectic form on the (2 n− 2m)-
-dimensional vector space Iσ/I. Prove that L′ ∈ L(E, σ) and L′∩L = I if and only if L′/I
is a Lagrange plane in Iσ/I which is transversal to L/I. Prove that the mapping L′↦→ L′∩L
exhibitsLL,,m as a smooth bundle over G m(L) of which each ﬁber is an aﬃne space of dimension
1
2(n−m)(n−m + 1), Prove LL,,m is a smooth submanifold of L(E, σ) of dimension equal to
1
2n(n + 1)− 1
2m(m + 1). Prove that the closure of LL,,m inL(E, σ) is equal to ⋃n
l=mLL,l . ⊘
Exercise 1.5 Let γ be a diﬀerentiable curve in L =L(E, σ) such that γ(t0)∈L L, 1. Prove that
γ(t) intersectsLL, 1 transversally at t =t0, i.e. γ′(t0) /∈ Tγ(t0)LL, 1, if and only if the restriction to
γ(t0)∩L of the symmetric bilinear on γ(t0), which is assigned to γ′t(t0)∈ TL as in Subsection 1.6,
is nonzero. We will call the intersection positive or negative according to whether this restriction
is positive or negative deﬁnite, respectively.
It is known that by slight perturbation every closed curve γ. in L can be made such that all
intersections withLL, 1 are transversal. prove that this implies that γ intersectsLL, 1 only ﬁnitely
many times. Write i(γ) for the number of positive intersections minus the number of negative
intersections.
It is also known that by slight perturbation any homotopy of closed curves, viewed as a mapping
from a two-dimensional cylinder toL can be made to miss each of the manifolds IL,m withm≥ 2,
each of which has codimension≥ 3 inL. This shows that i(γ) only depends on the homotopy class
of γ, and i induces a homomorphism from the fundamental group π1(L) ofL to Z.
Prove thatLL, 1 is connected and thatLL, 0 is simply connected. Prove that if i(γ) = 0, then γ
is contractible inL. Finally, ﬁnd a smooth closed curve γ inL such that i(γ) = 1 and prove that
i :π1(L)→ Z is an isomorphism.
Remark Maslov [23, p. 147–149] called the set Σ =LL, 1 and the integeri(γ) the singular set and
the index of the curve γ, respectively. Arnol’d [1] observed that Σ deﬁnes an oriented codimension
one cycle inL, that the index is equal to the topological intersection number of the one-dimensional
cycle γ with Σ and that the index deﬁnes an isomorphism of the fundamental group of L with Z.
⊘
11

2 Symplectic Manifolds
2.1 Deﬁnition
Let M be a ﬁnite-dimensional smooth manifold. A symplectic form on M is a smooth diﬀerential
form σ of degree two on M such that
i) For every m∈M the bilinear form σm on TmM is nondegenerate, and
ii) σ is closed, i.e. d σ = 0.
Condition i) means that, for every m∈ M, σm is a symplectic form on T mM. This implies that
dimM = dim TmM is even, say equal to 2n, cf. Subsection 1.4. A symplectic manifold is deﬁned
as a pair (M, σ), in which M is a ﬁnite-dimensional smooth manifold and σ is a symplectic form
on M.
Example 2.1 Probably the simplest example is Rn× Rn provided with the ”constant” standard
symplectic form of (1.2), which in diﬀerential form notation is equal to
σ =
n∑
j=1
dpj∧ dqj. (2.1)
Here pj and qj are viewed as (coordinate) functions on Rn× Rn. ⊘
2.2 The Cotangent Bundle
An important generalization of the previous example is obtained by starting with an arbitrary n-
dimensional smooth manifold X. The cotangent bundle T∗X of X is deﬁned as the vector bundle
overX of which the ﬁber at the point x∈X is equal to the dual T ∗
xX := (TxX)∗ of TxX , the
space of all linear forms ξ on the tangent space TxX of X at the point x.
Letπ denote the projection from M := T∗
xX ontoX. which sends every element of T∗
xX tox.
Then, for every ξ∈ T∗
xX, the tangent map Tξπ is a linear mapping from T ξM onto TxX, and if
we subsequently apply the linear form ξ∈ (TxX)∗ to it, we obtain the linear form
τξ :=ξ◦ Tξπ (2.2)
on TξM. This deﬁnes a special smooth diﬀerential form τ of degree one on M.
Ifα is any smooth diﬀerential form of degree one on X, then it can also be viewed as a smooth
mapping α :X→ T∗X such that π◦α is equal to the identity on X. It follows that
(α∗τ)x =τα(x)◦ Txα =α(x)◦ Tα(x)π◦ Txα =α(x)◦ Tx(π◦α) =α(x),
where in the ﬁrst, second, third and last identity we used the deﬁnition of pullback of a diﬀerential
form, the deﬁnition ofτ, the chain rule for diﬀerentiation andπ◦α = Id, respectively. The equation
α =α∗τ for every one-form α on X (2.3)
says that every one-form on X is equal to the pullback of τ by means of the one-form viewed as a
mapping from X to T∗X. For this reason τ is called the tautological one-form on the cotangent
bundle.
12

The exterior derivative
σ := dτ (2.4)
of the tautological one-form is a two-form on T ∗X, which is closed because d(d ω) = 0 for ev-
ery diﬀerential form ω (of any degree). Moroever, in local coordinates ( x1, ..., xn) on X, with
corresponding dual coordinates (ξ1, ..., ξn), the equation (2.2) takes the form
τ =
n∑
i=1
ξi dxi, (2.5)
and therefore
σ =
n∑
i=1
dξi∧ dxi, (2.6)
which shows that σ is equal to the standard symplectic form if we substitute xi =qi and ξi =pi.
This shows that σ := dτ is a symplectic form on T ∗X, which is called the canonical symplectic
form of the cotangent bundle.
2.3 Reduction
LetN be a smooth manifold and let ω be a closed smooth two-form on N for which the kernel has
constant rank, i.e. there exists a nonnegative integer k such that, for everyn∈N, dim(kerωn) =k.
This implies that the Kn := kerωn, n∈ N, deﬁne a smooth vector subbundle K of the tangent
bundle TN of N. (In the present diﬀerential geometric terminology, a smooth vector subundle of
the tangent bundle ofN is also called a distribution onN, not to be confused with the distributions
in Analysis. In the 19-th century literature a smooth vector subbundle of the tangent bundle of N
is called a Pfaﬃan system in N.)
A general smooth vector subbundle K of the tangent bundle T N of any ﬁnite-dimensional
smooth manifold N is called integrable if for each n0∈ N there exists an open neighborhood N0
of n0 in N and a smooth ﬁbration of N0, such that, for each n∈ N0, Kn is equal to the tangent
space of the ﬁber through n. The theorem of Frobenius says that K is integrable if and only if
[X, Y]⊂K holds for any pair of smooth vector ﬁelds X, Y on N such that X⊂K and Y ⊂K.
Returning to our two-form ω with kernel of constant rank, the claim is that the closedness of
ω implies that its kernel K := kerω is integrable. For the proof we use that [ X, Y] is equal to the
Lie derivativeLXY of Y with respect to the vector ﬁeld X. In view of the Leibniz formula for Lie
derivatives, it follows that
i[X,Y ] ω =LX (iY ω)− iY (LXω),
whereas the homotopy formula for the Lie derivaritive yields that
LXω = iX(dω) + d (iXω). (2.7)
Therefore, iY ω = 0, iXω = 0 and dω = 0 imply that i [X,Y ]ω = 0.
Now suppose that π :N→M is a ﬁbration with connected ﬁbers, such that, for each n∈N,
kerωn is equal to the tangent space ker Tnπ of the ﬁber through the point n. Fix m∈M. Then
there exists, for eachn∈π−1({m}), a unique two-formσm,n on TmM, such that (Tnπ)∗σm,n =ωn.
However, for each smooth vector ﬁeld X such that X⊂K we see from (2.7) that LXω = 0, which
implies that (etX)∗ω =ω, whereas on the other handπ◦etX =π. This implies that σm,n′ =σm,n if
13

n′ = etX(n). Because the compositions of the ﬂows etX withX⊂K act locally transitively on the
ﬁbers, and therefore transitively because the ﬁbers are connected, the conclusion is that σm,n =σm
does not depend on the choice of n∈π−1({m}).
The σm, m∈M, deﬁne a smooth two-form on M such that ω =π∗σ. Because
ker Tnπ = kerωn = Tnπ−1(kerσm),
it follows that ker σm ={0}, which means that σm is a symplectic form. Furthermore, π∗(dσ) =
d (π∗σ) = dω = 0, which in view of the surjectivity of the linear mappings Tnπ,n∈N implies that
dσ = 0. In other words, ( M, σ) is a symplectic manifold, which is called the reduced symplectic
manifold of the pair (N, ω).
2.4 Complex Projective Varieties
Let E be an n-dimensional complex vector space with Hermitian form h, which we provide with
real inner product g = Reh and the symplectic form σ = Imh as in Subsection 1.9, which are
related by g =σ◦J. Let
S :={z∈E|h(z, z) =g(z, z) = 1}
be the unit sphere in E with respect to the inner product g. Then, for each z∈S,
TzS ={v∈E|g(z,v ) = 0} ={v∈E|σ(i z, v) = 0}.
It follows that i z∈ TzS, and i z belongs to the kernel of the restriction to T zS. Because T zS
has real codimension one in E, its symplectic orthogonal complement is real one-dimensional, and
therefore equal to R iz. On the other hand R iz is equal to the tangent space of the circle
Cz :={cz|c∈ C,|c| = 1} = (Cz)∩S
through the pointz. If we denote the identity mapping from S toE byι, thenι∗σ is the restriction
to S of the two-form σ, and the ﬁbration of S by the integral curves of the kernels of ι∗σ is equal
to the ﬁbration of S by the circles Cz,z∈S. On the space M of these circles we have the reduced
symplectic form ˆσ, the unique two-form ˆσ on M such that ι∗σ = π∗ˆσ, if π : S→ M denotes the
projection deﬁned by π(z) =Cz, z∈S.
On the other hand the Cz, z∈ S, are the complex one-dimensional linear subspaces l of E,
which form the elements of the complex ( n− 1)-dimensional projective space CP(E) of E. The
mappingl↦→l∩S is a diﬀeomorphism from CP(E) ontoM, which can be used in order to identify
M with CP(E). Note that CP(E) is a complex analytic manifold, with a complex multiplication
Jl by i in each tangent space T l(CP(E)). It is easily veriﬁed that ˆg :=ˆσ◦J is the inner product
on Tl(CP(E)) which correpsonds to the restriction of g to the g-orthogonal complement of i z in
TzS.
IfE = Cn andh is the standard hermitian structure on Cn, then the Hermitian inner product
ˆh := 1
π (ˆg + iˆσ) is called the Fubini-Study metric on CP(E) = CPn−1. Here the factor 1 /π is
inserted in order to arrange that the integral of ω := 1
πˆσ over any complex projective line in
CPn−1 is equal to one.
More generally, ifM is a complex analytic manifold, then a K¨ ahler structureonM is a smooth
Hermitian inner product h on its tangent bundle, such that its imaginary part, the two-form
σ := Imh, is closed. This implies that σ is a symplectic form on M, called the K¨ ahler formof the
14

K¨ ahler manifold(M, h). The Fubini-Study metric is a K¨ ahler structure on the complex projective
space.
Ifι :V →M is a complex analytic submanifold of a K¨ ahler manifold (M, h), then the restriction
ι∗h ofh to TV is a K¨ ahler structure onV . This exhibits every smooth complex projective variety
as a K¨ ahler manifold, by providing it with the restriction to its tangent bundle of the Fubini-Study
metric of the projective space of which it is a subvariety. This is a very rich source of examples
of compact symplectic manifolds. Vice versa, this introduces symplectic diﬀerential geometry into
complex algebraic geometry.
2.5 Almost Complex Structure
An almost complex structure J on a smooth manifold M is a complex structureJm on each tangent
space TmM, depending smoothly on m∈M. As in Subsection 1.9, this turns each tangent space
into a complex vector space. If n is the complex dimension of T mM with respect to the complex
structure Jm, then the real dimension is equal to 2 n.
An almost complex manifold is a pair (M, J) in whichM is a smooth manifold andJ is an almost
complex structure on M. The almost complex structure is called integrable if for every m0∈ M
there is coordinate system in an open neighborhood of m0 in M, in which m↦→ Jm is constant.
If we use the constant complex structure in order to identify R2n with Cn, we obtain a system
of local coordinatizations for which the coordinate changes are complex analytic mappings. With
these coordinatizations, M is a complex analytic manifold for which the Jm are the multiplications
by i in the tangent spaces.
For each m∈ M one has the antisymmetric bilinear mapping [ J, J]m from TmM× TmM to
TmM, which is deﬁned by
[J, J](v, w) = [Jv, Jw ]−J [Jv, w]−J [v, Jw]− [v, w], (2.8)
in whichv andw are smooth vector ﬁelds on M and the brackets in the right hand side are the Lie
brackets of vector ﬁelds. The theorem of Newlander and Nirenberg says that the almost complex
structure J is integrable, if and only if [J, J] = 0, cf. [25], [13], [22].
Lemma 2.2 Let σ be a symplectic form on M. Then there exists an almost complex structure J
on M such that h =σ◦J + iσ is a Hermitian structure on TM. If σ is invariant under the action
of a group G on M, and M carries a G-invariant Riemannian structure, then J can be chosen to
beG-invariant as well.
Proof There exists a Riemannian structure g in M. Such a Riemannian structure exists in local
coordinates. Let ξj be a smooth partition of unity subordinate to ta locally ﬁnite covering of M
by means of open subsets Mj on which we have a Riemannian structure gj. This means that the
ξj are smooth real valued functions on M such that ξj≥ 0, the support of ξj is contained in Mj
and∑
j ξj = 1. Then g =∑
j ξjgj is the desired Riemannian structure on M.
Deﬁne, for each m∈ M, Am := σ−1
m gm. Then gm◦Am = gm◦σ−1
m ◦gm is antisymmetric, or
Am is gm-antisymmetric, and there exists a gm-orthonormal basis in T mM on which the matrix
of Am consists of 2 × 2-matrices
( 0 −aj
aj 0
)
along the diagonal, with aj > 0. Let Bm be the
linear transformation in TmM of which the matrix consists of the 2 × 2-matrices
( 1/aj 0
0 1 /aj
)
15

along the diagonal. Then Jm := Am◦Bm = σ−1
m ◦gm◦Bm is a complex structure on T mM,
ˆgm :=gm◦Bm =σm◦Jm is an inner product on TmM and therefore σm◦Jm + iσ is a Hermitian
form on TmM.
At ﬁrst sight this construction seems to depend on the choice of the gm-orthonormal basis, but
B2
m =−A−2
m , which shows that actually Bm is equal to the unique positive deﬁnite square root of
the positive deﬁnite linear transformation −A−2
m (all with respect to the inner product gm). This
makesJm globally well-deﬁned and depending smoothly on m∈M.
If σ and g are G-invariant, then the uniqueness of the Bm, m∈ M, make that also B and J
are G-invariant. 2
It cannot always be arranged that in addition J is integrable. In other words, not every symplectic
form is equal to a K¨ ahler form on a complex analytic manifold. However, the weaker almost complex
structure is suﬃcient for many purposes.
2.6 Cohomology Classes
It follows from the observation in Subsection 1.8 that the n-the power of a symplectic form is
nonzero that σn is a nowhere vanishing volume form on M.
Assume in the sequel that M is compact and connected. Then the de Rham cohomology class
[σn]∈ H2n(M) of the nowhere vanishing volume form σn is nonzero, and therefore generates the
one-dimensional vector space H 2n(M). Because [ σn] = [σ]n, this in turn implies that the element
[σ]k∈ H2k(M) is nonzero for every 1 ≤k≤n.
The fact that H2k(M)⁄= 0, or more precisely that there exists an s∈ H2(M) such that sk⁄= 0
for every 1≤k≤n, puts a quite severe topological restriction on a compact smooth manifold for
allowing a symplectic form. For instance, if M is a 2n-dimensional sphere, then Hp(M) = 0 for all
p exceptp = 0 and p = 2n, and therefore the only sphere which can carry a symplectic form is the
two-dimensional one.
If M is the complex n-dimensional complex projective space, then H p(M) = 0 except when
p = 2k, 0 ≤ k ≤ n, in which case dim H2k(M) = 1. In other words, in this case the whole
cohomology ring is generated by the cohomology class [ ω] of the K¨ ahler formω deﬁned by the
Fubini-Study metric. This is even true for the cohomology ring with values in Z, cf. [9, pp. 60,
150].
2.7 Exercises
Exercise 2.1 let X and Y be smooth manifolds and let φ :X→Y be a local diﬀeomorphism.
Deﬁne the induced transformation Φ : T∗X→ T∗Y by
Φ(x, ξ) :=
(
φ(x), ((Txφ)∗)−1 (ξ)
)
, x ∈X, ξ∈ (TxX)∗.
Prove that
Φ∗τT∗Y =τT∗X
and that
Φ∗σT∗Y =σT∗X.
In other words, the induced mapping is a canonical transformation, in the sense that it preserves
the canonical symplectic forms. ⊘
16

Exercise 2.2 Consider the standard coordinatization
ϕ : (z1, ..., zn)↦→ C (1, z1, ..., zn)
of the open subset of then-dimensional complex projective space which consist of the one-dimensional
complex linear subspaces l which are not contained in the n-dimensional linear subspace deﬁned
by the equation z0 = 0. Write
w =ψ(z) := (1 + (z, z))−1/2 (1, z1, ..., zn),
wj =uj + ivj with uj, vj∈ R, 0≤j≤n, and zj =xj + iyj with xj, yj∈ R, 1≤j≤n. Prove
that the pullback of the Fubini-Study K¨ ahler formω under ϕ satisﬁes
πω := ψ∗


n∑
j=0
dvj∧ duj

 = (1 + (z, z))−1
n∑
j=1
dyj∧ dxj
−(1 + (z, z))−2
n∑
j,k =1
(xjxk +yjyk) dyj∧ dxk +xjyk (dxj∧ dxk + dyj∧ dyk).
(This may be compared with [9, p. 30, 31].) How easy is it to verify by direct computation that
the two-form in the right hand side is closed?
Verify that for n = 1 we have
πω = (1 +x2 +y2)−2 dy∧ dx,
and that the integral of ω over the complex projective line is equal to 1. ⊘
Exercise 2.3 LetJ be an almost complex structure on the manifoldM. Prove that [J, J](v, Jv) =
0 for any smooth vector ﬁeld v on M and prove that J is integrable if dim M = 2. Now assume
that dimM = 2, that M is connected and that σ is a nowhere vanishing area form = symplectic
form on M. Prove that g := σ◦J is a symmetric bilinear form on each tangent space which is
invariant under the linear transformations etJm. Prove that g is either positive deﬁnite or negative
deﬁnite. In other words, M is a complex analytic ”curve” and eitherσ or−σ is equal to the K¨ ahler
form of a K¨ ahler structure onM. ⊘
Exercise 2.4 For which compact oriented surfaces is the cohomology ring generated by the class
of a symplectic form? ⊘
Exercise 2.5 If n = 2 in Subsection 2.4, identify the projection π :S→ CP(E) with the Hopf
ﬁbration. ⊘
17

3 Hamiltonian Systems
3.1 Flows of Vector Fields
Let M be a smooth manifold. If v is a smooth vector ﬁeld on M then the general theory of
systems of ordinary diﬀerential equations, see for instance [3], implies the following statements.
For everym∈M, there is a unique maximal solution γ =γm :Im→M of the diﬀerential equation
dγ(t)/ dt =v(γ(t)), such that γ(0) = m. The domain of deﬁnition Im of this maximal solution γ
is an open interval in R containing 0. If s := supIm <∞ or i := infIm >−∞, then there exists
for every compact subset K ofM anϵ> 0 such that γ(t) /∈K for everyt∈]s−ϵ, s[ or t∈]i, i+ϵ[,
respectively. In other words, the only way the maximal solutions do not exits for all time is that
run out of every compact subset of M in a ﬁnite time. This implies that if γm(t) stays within a
compact subset of M for all t∈Im, then Im = R. The set D :={(t, m∈ R×M|t∈Im} is an
open subset of R×M which contains{0}× M, and A : (t, m)↦→γm(t) is a smooth mapping from
D to M. If s∈ Im and t∈ Iγm(s), then s +t∈ Im and γm(s +t) = γγm(s)(t). This follows from
the uniquenss of the solutions, because, as a function of t,γm(s +t) and γγm(s)(t) satisfy the same
diﬀerential equation and have the same initial value.
We say that the vector ﬁeld v is complete if D = R×M, in which case A : R×M→M is a
smooth action of the additive group ( R, +) on M. The mapping m↦→ γm(t) : M→ M is called
the timet ﬂow of the vector ﬁeld v an will be denoted by etv . This notation reminds of the deﬁning
equation detv / dt =v◦ etv and of the group homomorphism property e (s+t)v = etv◦ esv . Because
etv◦ e−tv = Id = e−tv◦ etv , the time t ﬂow is a diﬀeomorphism of M, i.e. it is bijective from M
to M and has a smooth inverse (equal to e−tv ).
If D is a proper subset of R×M, then the ﬂow etv is deﬁned on the open subset
Mt :={m∈M| (t, m)∈D}
ofM, and e(s+t)v(m) = etv◦ esv (m) holds whenm∈Ms and esv (m)∈Mt, in which casem∈Ms+t.
Also, etv is a diﬀeomorphism from the open subset Mt ofM onto the open subset M−t ofM, with
inverse equal to e−tv . If D⁄= R×M we don’t have a group action, but we have the same identities
”as far as the objects appearing in the formulas are deﬁned”. Lie [21] called t↦→ etv the one-
parameter group of transformations generated by the vector ﬁeld v, where he did not worry about
domains of deﬁnition.
3.2 Lie Derivatives
Let Ωp(M) denote the space of smooth p-forms on the smooth manifold M, where Ω0(M) =F(M)
denotes the space of smooth real valued functions on M and Ωp(M) ={0} if p >dimM. If M
and N are smooth manifolds of any dimensions, and ϕ : M→ N is a smooth map, then for any
ω∈ Ωp(N) the pullback ϕ∗ω of ω under the map ϕ is deﬁned by
(ϕ∗ω)m (v1, ,, vn) =ωϕ(m) (Tmϕv 1, ,, Tmϕvn). (3.1)
Note thatϕ∗ deﬁnes a continuous linear operator from Ωp(N) to Ωp(M), where the word ”pullback”
reminds of the fact that this goes in the opposite direction of the map ϕ :M→N. For p = 0 we
have ϕ∗ω = ω◦ϕ, which means that the pullback under ϕ is just the substitution n = ϕ(m) in
ω(n), and ϕ∗ is just a convenient notation for the linear mapping ω↦→ω◦ϕ.
18

The transposition symbol∗ in the notation is a reminder to the transposition ofϕ in the formula
ϕ∗ω =ω◦ϕ. It also helps reminding that in the natural composition formula ( ψ◦ϕ)∗ =ϕ∗◦ψ∗
the order is reversed: pullback is an antihomomorphism with respect to composition.
It is known that the exterior derivative d : Ω p(M)→ Ωp+1(M) of diﬀerential forms behaves
naturally under smooth mappings, in the sense that
ϕ∗(dω) = d (ϕ∗ω), ω ∈ Ωp(N), ϕ :M→N. (3.2)
LetX (M) denote the vector space of smooth vector ﬁelds on M. If v∈X (M), then the Lie
derivativeLvω of ω∈ Ωp(M) with respect to the vector ﬁeld v is deﬁned as
Lvω :=
d
dt
(
etv)∗ω
⏐⏐⏐
t=0
. (3.3)
If in (
etv)∗◦ (esv )∗ ω =
(
esv◦ etv)∗ ω =
(
e(t+s)v
)∗
ω
we take the derivative with respect to s at s = 0 in the left and right hand side, we obtain that
(
etv)∗Lvω =
d
dt
(
etv)∗ω.
This implies that Lvω = 0 if and only if t↦→
(
etv)∗ω is constant, hence equal to its value ω at
t = 0. We say that ω is called invariant under the ﬂow of v if, for every t∈ R,
(
etv)∗ω =ω inMt.
We have proved that ω is invariant under the ﬂow of v if and only if the Lie derivative of ω with
respect to v is equal to zero.
If v∈X (M) and ω∈ Ωp(M), then the inner product ivω∈ Ωp−1(M) of ω with v is deﬁned by
(ivω)m (v2, ..., vn) =ωm (v(m), v2, ..., vn). (3.4)
In other words, iv is the continuous linear operator from Ωp(M) to Ωp−1(M) of inserting the vector
ﬁeld v at the ﬁrst slot .
Ifp = 0, then obviouslyLvω = iv(dω), which is the derivative of the function ω in the direction
of the vector ﬁeld v. For general p we have the homotopy formula
Lvω = iv(dω) + d (ivω), (3.5)
orLv = iv◦ d + d◦ iv. Note that in the ﬁrst summand d and i v is a linear operator from Ω p(M) to
Ωp+1(M) and from Ωp+1(M) to Ωp(M), respectively, whereas in the second summand i v and d is
a linear operator from Ωp(M) to Ωp−1(M) and from Ωp−1(M) to Ωp(M), respectively. This makes
the beautiful formula (3.5) easy to remember.
Let v∈X (M) and let ϕ : M→ M be a smooth mapping for which, at each point m∈ M,
Tmϕ : TmM → Tϕ(m)M is invertible. Then the pullback ϕ∗v∈X (M) on M of v under ϕ is
deﬁned by
(ϕ∗v)(m) := (Tmϕ)−1 v(ϕ(m)), m ∈M. (3.6)
This deﬁnition has been arranged in such a way that
ϕ∗(ivω) = iϕ∗v ϕ∗ω
19

for any v∈X (M) and ω∈ Ωp(M). If w is another smooth vector ﬁeld on M, ϕ = etw , and we
diﬀerentiate the left and right hand side with respect to t at t = 0, then we obtain that
Lw(ivω) = i[w,v ] ω + iv (Lwω), (3.7)
if we deﬁne the Lie brackets [w, v]∈X (M) of the vector ﬁelds w and v on M by means of
[v, w] =Lvw := ∂
∂t
(
etv)∗w
⏐⏐⏐⏐
t=0
:= ∂
∂t
( ∂
∂s e−tv◦ esw◦ etv
⏐⏐⏐⏐
s=0
)⏐⏐⏐⏐
t=0
. (3.8)
Note that this yields the opposite sign compared with the usual deﬁnition for the Lie agebra of a Lie
group, but it is probably better to conform with the generally accepted deﬁnition of Lie brackets
of vector ﬁelds.
In local coordinates, the Lie brackets of the vector ﬁelds v and w can be computed as
[v, w](m) = (Dw)(m)v(m)− (Dv)(m)w(m). (3.9)
If in the local coordinates the vector ﬁelds are linear, then this leads to [v, w] =w◦v−v◦w, where
the right hand side is equal to the opposite of the commutator of w and v.
If in (3.7) we substitute ω = df in which f is a smooth function, then we obtain that
L[w,v ]f = [Lw,Lv] f, (3.10)
in which [A, B] := A◦B−B◦A denotes the commutator of the linear operators A and B. It is
customary in diﬀerential geometry to identify the smooth vector ﬁeld v with the derivationD =Lv
of functions in the direction of v, and with this identiﬁcation the Lie brackets of vector ﬁelds is
deﬁned as their commutator. This deﬁnition has been adopted in Lie [21, Vol. I], where the identity
(
etv)∗f = etLv f :=
∞∑
k=0
tk
k! (Lv)k f,
which is valid if the vector ﬁeldv and the functionf are analytic, is presented as another motivation
for the exponential notation for the one-parameter group of transformations generated by the vector
ﬁeld v.
Actually, since derivations are linear operators in the space of smooth functions, and linear
operators are usually denoted by capital letters, the identiﬁcation of vector ﬁelds with derivations
has led to the custom in diﬀerential geometry and in Lie groups to denote vector ﬁelds and elements
of the Lie algebra by capital letters, usually X. This in turn has led to the notation X (M) for the
Lie algebra of all smooth vector ﬁelds on M. Lie’s ”continuous groups” were subgroups G of the
groups of diﬀeomorphism of a smooth manifold M, which depend smoothly on parameters. The
corresponding inﬁnitesimal transformations form a Lie subalgebra g ofX (M).
If in the local coordinates the vector ﬁelds are linear, then (3.9) leads to [ v, w] =w◦v−v◦w,
where the right hand side is equal to the opposite of the commutator of w and v. This is another
consequence of the opposite sign choice for the Lie brackets of vector ﬁelds as compared to the one
in the Lie algebra of a Lie group.
20

3.3 Hamiltonian Vector Fields
Let (M, σ) be a symplectic manifold. Then, according to Subsection 3.2, the ﬂow etv of the smooth
vector ﬁeld v∈X (M) leaves the symplectic form σ invariant, if and only if
0 =Lvσ = iv(dσ) + d (ivσ) = d (ivσ),
i.e. if and only if the one-form i vσ is closed. Here we have used the homotopy formula (3.5) for
the Lie derivative in the second identity and the fact that σ is closed in the third identity.
In turn the condition that i vσ is closed is locally equivalent to the condition that i vσ is equal
to the total derivative of a smooth function. In formula:
ivσ =− df (3.11)
for a locally deﬁned smooth functionf, where the minus sign is a matter of convention. If H1(M) =
0, then there is a globally deﬁned function f on M such that (3.11) holds, and if M is connected,
then f is uniquely determined up to an additive constant.
Conversely, if f is a smooth function on M, then the fact that for every m∈ M the linear
mapping
σm :v↦→ ivσm : TmM→ (TmM)∗
is bijective shows that there is a unique vector ﬁeld v on M which satisﬁes (3.11). Moreover, v is
smooth because df and m↦→ σ−1
m are smooth. The smooth vector ﬁeld v on M such that (3.11)
holds is called the Hamiltonian vector ﬁeld Hf on M deﬁned by the function f. In the literature f
is called the Hamiltonian function of the vector ﬁeld v and denoted by H. However, we would like
to stress that f can be any smooth function on M. It is quite remarkable that there are so many
smooth vector ﬁelds whose ﬂows leave σ invariant: one for every closed one-form on M, or smooth
function on M modulo an additive constant.
A system of coordinates xi, ξi in M is called a canonical system of coordinates if (2.6) holds.
Let, in such a coordinate system, ˙xi, ˙ξi denote the coordinates of the vector ﬁeld
v = Hf =
(
˙x1, ..., ˙xn; ˙ξ1, ..., ˙ξn
)
.
With these notations, the equation (3.11 reads
ivσ =
n∑
i=1
(
˙ξi dxi− ˙xi dξi
)
=−
n∑
i=1
(∂f
∂xi
dxi + ∂f
∂ξi
dξi
)
,
from which obtain that
˙xi = ∂f (x, ξ)
∂ξi
, ˙ξi =−∂f (x, ξ)
∂xi
, 1≤i≤n. (3.12)
In other words, if d m(t)/ dt = v(m(t)) is the diﬀerential equation for the ﬂow deﬁned by
the vector ﬁeld v = Hf, then in canonical local coordinates we arrive at the system of ordinary
diﬀerential equations (3.12), in which we replace ˙xi and ˙ξi by dxi(t)/ dt and dξi(t)/ dt, respectively,
and in the right hand side take the partial derivatives of f at xi =xi(t), ξi =ξi(t). We recognize
the resulting system of ordinary diﬀerential equations as the Hamiltonian system deﬁned by the
21

function f as it appears in the textbooks in Classical Mechanics, where usually the position and
momentum coordinates xi and ξi are denoted by qi and pi, respectively.
Note that if we would have taken the other sign convention in (3.11), then the signs in (3.12)
would be opposite to the standard ones in classical mechanics. Also note that the convention, to
use Greek letters for the momentum coordinates corresponding to the Latin letters for the position
coordinate, allows us to write for example the momentum coordinates coordinates corresponding
to the position coordinates x, y, zas ξ, η, ζ, respectively.
Example 3.1 If X is an n-dimensional smooth manifold and v∈X (X), then the momentum
function of the vector ﬁeld v in the base manifold X is the function µv on the cotangent bundle
M := T∗X, deﬁned by
µv(x, ξ) =ξ(v(x)), x ∈X, ξ ∈ (TxX)∗. (3.13)
Then the ﬁber derivative of µv is equal to
˙x = ∂µv(x, ξ)
∂ξ =v(x)∈ TxX = ((TxX)∗)∗.
It follows that the projection π : (x, ξ)→x : T∗X→X intertwines the Hµv-ﬂow in T∗X with the
v-ﬂow in X, in the sense that
π◦ et Hµv = etv◦π.
More precisely, for every x∈X and ξ∈ (TxX)∗ we have that
et Hµv (x, ξ) =
(
etv (x),
((
Tx etv)∗)−1
(ξ)
)
.
In other words, the ﬂow in T∗X of the Hamiltonian system deﬁned by the function µv is equal to
the ﬂow in T∗X which is induced by the ﬂow in X of the vector ﬁeld v. ⊘
3.4 The Legendre Transform
Let L be a smooth real-valued function on an open subset U of the tangent bundle TX of an
n-dimensional smooth manifold X, where we will writeL(x,v )∈ R wheneverx∈X andv∈ TxX.
For any smooth curveγ : [a, b]→X such that (γ(t), γ′(t))∈U for all t∈ [a, b], deﬁne the integral
I(γ) =
∫ b
a
L(γ(t), γ′(t)) dt. (3.14)
The variational formula of Euler and Lagrange states that if γ =γϵ depends smoothly on a param-
eter ϵ, then
dI(γϵ)
dϵ = −
∫ b
a
[L](t)δ(t) dt
+µ(γ(b), γ′(b))δ(b)−µ(γ(a), γ′(a))δ(a). (3.15)
Here
δ(t) := ∂γϵ(t)
∂ϵ ∈ Tγ(t)X (3.16)
22

denotes the ”variation with respect to ϵ” of the curve γϵ(t), [L](t) is the linear form on T γ(t)X
which in local coordinates is given by
[L]i :=
dµi(γ(t), γ′(t))
dt − ∂L(x, γ′(t)
∂xi
⏐⏐⏐⏐
x=γ(t)
(3.17)
and the linear form µ(x, v) =µL(x, v) on TxX is deﬁned by
µ(x, v) := ∂L(x, v)
∂v ∈ (TxX)∗. (3.18)
The formula (3.15) is obtained by diﬀerentiating with respect to ϵ under the integral sign, and then
performing an integration by parts on the term with the factor
∂2γϵ(t)
∂ϵ∂t = ∂2γϵ(t)
∂t∂ϵ .
The linear formµ(x, v) on the tangent space in (3.18), which is deﬁned in a coordinate-independent
way, is called the momentum vector assigned to the velocity vector v by means of the function L.
It is one of the basic observations of Lagrange [19, Tome I, Partie 2, Section IV] that, although
the two summands in (3.17) transform in a quite complicated manner under a change of coordinates,
the quantity [L](t) transforms as a covector, an element of
(
Tγ(t)X
)∗. His argument is that for
anyw∈ Tγ(t0)X the real number−[L](t0)w is equal to the limit for j→∞ of the left hand side
of (3.17), which is independent of any choice of coordinates, if we take γj
ϵ (t) in such a way that
δj(t) =∂γj
ϵ (t)/∂ϵ is only nonzero fort in a shrinking neighborhood oft0 and is asymptotically equal
to a large multiple of v, in such a way that the integral over t remains equal to w. (Those who
are familiar with the theory of distributions will recognize δj(t) as a sequence of smooth functions
which approximate the Dirac delta function at the point t0 timesw, where the approximation is in
the distributional sense.)
The velocity-to-momentum mapping
Φ = ΦL : (x, v)↦→ (x, µ(x, v)) :U→ T∗X
is a local diﬀeomorphism if and only if its tangent mapping is invertible, which is equivalent to
Legendre’s condition that
the symmetric bilinear form ∂µ(x, v)
∂v = ∂2L(x, v)
∂v2 on TxX is nondegenerate.
Here, in linear coordinates in T xX, the bilinear form ∂2L(x, v)/∂v2 has the symmetric matrix
∂2L(x, v)/∂vi∂vj, 1≤i, j≤n, the Hessian of the function v↦→L(x, v). By restricting U to open
subsets on which Φ is injective, we obtain a diﬀeomorphism from U onto an open subset V of the
cotangent bundle T∗X of X.
A curve γ(t) is called a stationary curve for the integral I in (3.14), if it satisﬁes the Euler-
Lagrange equations
[L](t)≡ 0, (3.19)
i.e. if the integral in (3.15) vanishes for any variation δ(t) of γ(t). If the Legendre condition holds,
then the Euler-Lagrange equations can be written in local coordinates as a second order system of
ordinary diﬀerential equations
d2γi(t)
dt2 =ai(γ(t), γ′(t)), 1≤i≤n,
23

in which the components of the acceleration ai(x, v) are smooth functions of x and v. Actually, it
is more convenient to view this second order system as a ﬁrst order system
x′(t) =v(t), v ′(t) =a(x(t), v(t)),
deﬁned by the vector ﬁeld (v, a(x, v)) in the tangent bundle.
Now deﬁne the functions H on U and h on V subsequently by means of the equations
H(x, v) :=⟨v, µ(x, v)⟩− L(x, v), h =H◦ Φ−1. (3.20)
Here⟨v, ξ⟩ is the customary, more symmetric notation for the value ξ(v) which the linear form ξ
takes on the vector v. The function h on the open subset V of the cotangent bundle T∗X of X is
called the Legendre transform of the function L.
Writev =v(x, ξ) for the solution v of the equation µ(x, v=ξ. Then
h(x, ξ) =⟨v(x, ξ), ξ⟩− L(x, v(x, ξ),
hence
∂h(x, ξ)
∂ξi
=⟨∂v(x, ξ)
∂ξi
, ξ⟩ +vi(x, ξ)−⟨ ∂v(x, ξ)
∂ξi
, µ(x, v(x, ξ))⟩ =vi(x, ξ),
where in the ﬁrst and second identity we have used the deﬁnition (3.18) of µ and the equation
µ(x, v(x, ξ)) =ξ, respectively. Similarly we have
∂h(x, ξ)
∂xi
=⟨∂v(x, ξ)
∂xi
, ξ⟩− ∂L(x, v)
∂xi
⏐⏐⏐⏐
v=v(x,ξ )
−⟨ ∂(v, ξ)
∂xi
, µ(x, v(x, ξ))⟩ =− ∂L(x, v)
∂xi
⏐⏐⏐⏐
v=v(x,ξ )
,
where again in the ﬁrst and second identity we have used the deﬁnition (3.18) ofµ and the equation
µ(x, v) =ξ, respectively.
The Euler-Lagrange equations are
dx(t)
dt =v(t),
dξi(t)
dt = ∂L(x, v)
∂xi
⏐⏐⏐⏐
v=v(x,ξ )
,
where in the second equation we have substituted ξ = µ(x, v) = ∂L(x, v)/∂v. The point of the
computation of the partial derivatives of the function h(x, ξ) is that the velocity-to-momentum
mapping Φ transforms the Euler-Lagrange equations into the Hamiltonian system
dxi
dt = ∂h(x, ξ)
∂ξi
,
dξi
dt =−∂h(x, ξ)
∂xi
on V which is deﬁned by the function h.
Conversely, if h is a smooth real-valued function on an open subset V of T∗X for which the
momentum-to-velocity mapping
Ψ = Ψh : (x, ξ)↦→ (x, v(x, ξ)), v (x, ξ) := ∂h(x, ξ)
∂ξ
is a diﬀeomorphism from V onto an open subset U of TX, then we can deﬁne subsequently
l(x, ξ) :=⟨v(x, ξ), ξ⟩− h(x, ξ), L =l◦ Ψ−1.
24

It is then not hard to verify that Ψ h = Φ−1
L and h is equal to the Legendre transform of L, which
shows that ΨL transforms the Hamiltonian system deﬁned by the functionh into the Euler-Lagrange
equations for the function L.
We now turn to the relation with Classical Mechanics. Lagrange [19, Tome 1, partie 2, Section IV]
actually made his observation, that [L] transforms under changes of local coordinates as a covector,
in the case that L(x, v) is equal to the kinetic energy
T (x, v) = 1
2m(x)(v, v)
of a classical mechanical system. Here m(x), the inertial mass tensor is an inner product on TxX.
If we have local coordinates in which m(x) = m does not depend on x, then [T ] = d (mv )/ dt and
we recognize the equation
[T ] =F = the force acting on the system (3.21)
as Newton’s equations of motion . However, Lagrange observed that under arbitrary nonlinear
changes of coordinates, such as the passage from recangular coordinates to polar coordinates, the
accelerationa = dv/ dt transforms in a complicated way, not at all as a tensor, and the transformed
equations of motion do not look like Newton’s equations F = ma at all. (Also the inertial mass
tensor in this case no longer is independent of the position.)
Because Lagrange had understood that in general a quantity of the form [ L] transforms covari-
antly, he proposed to formulate the equations of motion for a general classical mechanical system
as (3.21), in which T is the kinetic energy function viewed as a smooth function on the tangent
bundle. Moreover, the force ﬁeld F is (has to be equal to) a smooth mapping which assigns to each
x∈X and v∈ TxX an element of (TxX)∗, a linear form on T xX.
The force ﬁeld F is called conservative, if F (x, v) = F (x) does noet depend on v and F (x) =
− dV (x) for a potential energy functionV which is a smooth real-valued function onX. In this case
one has F = [V ] and we recognize the equations of motion (3.21) as the Euler-Lagrange equations
[L] = 0, in which L =T−V .
The momentum deﬁned by L = T−V is equal to µ(x, v) = m(x)v, in which the inertial
mass tensor m(x) is regarded as a bijective linear mapping from T xX onto (TxX)∗. Using that
v↦→ T (x, v) is homogeneous of degree two, one obtains that its Legendre transform is equal to
T◦ Φ−1, whereas the Legendre transform of V is equal to −V . This yields that the Legendre
transform of L =T−V is equal to the total energy function h =T◦ Φ−1 +V , viewed as a function
of the positions and the momenta. In this way the equations of motion for a classical mechanical
system with a conservative force ﬁeld are equivalent to the Hamiltonian system deﬁned by the total
energy function, viewed as a function on the cotangent bundle T ∗X rather than on the tangent
bundle TX.
Remark 3.1 Lagrange [19, Tome 1, Partie 2, Section V] explictly introduced the velocity-to-
-momentum mapping Φ = Φ L and the two-form Φ ∗
Lσ on the tangent bundle T X, but without
mentioning the canonical two-form σ of the cotangent bundle T ∗X. He also proved that Φ ∗
Lσ
is invariant under the ﬂow deﬁned by the Euler-Lagrange equations. His proof is paraphrased in
Exercise 3.4
The equivalence between the Euler-Lagrange equations of variational calculus and Hamiltonian
systems has been found for L = T−V by Hamilton [11], and then it was soon realized by many
25

authors that his proof holds for an arbitrary function L on the tangent bundle which satisﬁes
Legendre’s condition. Earlier, the perturbation equations of a classical mechanical system in which
the potential energy is perturbed were written in a Hamiltonian form by Lagrange [19, Tome I,
p. 310]. He might have missed the general equivalence between Euler-Lagrange equations and
Hamiltonian systems, because he probably was not aware of the Legendre transform. ⊘
3.5 Poisson Brackets
If f, g∈F (M), then the Poisson brackets{f, g} of f and g are deﬁned as the derivative of the
function g in the direction of the Hamiltonian vector ﬁeld H f deﬁned by the function f:
{f, g} :=LHf (g) = iHf (dg) =− iHf
(
iHgσ
)
=σ (Hf, Hg). (3.22)
Here we used (3.11) and the antisymmetry of σ in the third and fourth identity, respectively. The
right hand side shows that the Poisson brackets are antisymmetric in the sense that
{g, f} =−{f, g}, f, g ∈ F(M). (3.23)
In canonical local coordinates the Poisson brackets are given by
{f, g}(x, ξ) =
n∑
i=1
(∂f (x, ξ)
∂ξi
∂g(x, ξ)
∂xi
− ∂f (x, ξ)
∂xi
∂g(x, ξ)
∂ξi
)
. (3.24)
It follows immediately that the following conditions a)–d) are equivalent:
a) g is a constant of motion for the Hamiltonian system deﬁned by the function f, in the sense
that g is invariant under the Hf-ﬂow.
b) {f, g} = 0.
c) {g, f} = 0.
d) f is a constant of motion for the Hamiltonian system deﬁned by the function g.
In the applications, one often has that the H g-ﬂow is a one-parameter group of symmetry for the
function f, which means that d) holds. The conclusion, that in this case g is a constant of motion
for the Hamiltonian system deﬁned by the function f, is called Noether’s principle for Hamiltonian
systems. In many examples we have M = T∗X and g =µv, the momentum function of a smooth
vector ﬁeld v in the base manifold X, cf. Example 3.1.
It also follows from (3.23) that{f, f} = 0, meaning that the function f is a constant of motion
for the Hamiltonian system deﬁned by f. If f is equal to the total energy of a classical mechanical
system as in Subsection 3.4, then this is the law of conservation of the total energy .
The derivative of{f, g} is equal to
d{f, g} = dLHfg =LHf dg =−LHf
(
iHgσ
)
=− i[Hf, Hg]σ.
Here we used in the ﬁrst, second, third and fourth identity the deﬁnition (3.22) of the Poisson
brackets, the fact that exterior diﬀerenitation commutes with pullbacks and therefore with Lie
26

derivatives, the deﬁntion (3.11) of Hamiltonian vector ﬁelds, and formula (3.7) together with the
fact thatLHfσ = 0.
This formula for the derivative of {f, g} just means that
[Hf, Hg] = H{f,g}. (3.25)
In words, the Lie brackets of the Hamiltonian vector ﬁelds of the functions f and g is again a
Hamiltonian vector ﬁeld, namely of the Poisson brackets of f and g.
If we now let act the left and right hand side of (3.25) on a third smooth function h onM, then
we obtain, using (3.10), that
{f,{g, h}}−{ g,{f, h}} ={{f, g}, h}.
Using the antisymmetry (3.23) at several places, this identity can be rewritten as theJacobi identity
for Poisson brackets :
{{f, g}, h} +{{g, h}, f} +{{h, f}, g} = 0. (3.26)
(Note the cyclic permuation of f, g and h in the left hand side of (3.26). Together, (3.26) and
(3.25) mean that
Theorem 3.2 The space of smooth functions F(M) on M is a Lie algebra with respect to the
Poisson brackets, and the mapping which assigns to a smooth function its Hamiltonian vector ﬁeld
is a homomorphism of Lie algebras from F(M) to the Lie algebra X (M) of smooth vector ﬁelds on
M. The kernel of this homomorphism is equal to the space of function which are constant on the
connected components ofM.
Remark 3.2 The Jacobi identity for the Poisson brackets (3.26) (in canonical coordinates) goes
back to the article of Jacobi [18], which appeared posthumously in 1862. Jacobi mentioned that
(3.26) implies the earlier theorem of Poisson, which states that if g and h are constants of motion
for the Hamiltonian system deﬁned by the function f, then{g, h} also is a constant of motion for
the Hamiltonian system deﬁned by f. It could very well be that Jacobi was led to (3.26) by means
of an analysis of Poisson’s proof. This observation of Jacobi may also have led to adoption of the
name ”Poisson brackets”, which brackets appeared earlier in the work of Lagrange [19, Tome I, p.
315].
Inspired by the Jacobi identity for Poisson brackets, Lie [21, Vol. 1, Kap. 5, §26 and Vol.
2, Kap. 7, §44, 45] introduced the Jacobi identity for vector ﬁelds, and coined the name ”Jacobi
identity”. ⊘
3.6 Darboux’s Lemma
Let (M, σ) be a symplectic manifold. The Darboux lemma states that locallyσ form can be brought
into the canonical form (2.6). This means that for everym0∈M there exists an open neighborhood
U of m0 in M and a diﬀeomorphism Φ from U onto an open subset V of Rn× Rn such that
Φ∗
( n∑
i=1
dξi∧ dxi
)
=σ onU.
27

A proof can be given as follows. Let φ be any smooth function deﬁned in a neighborhood of
m0 such that φ(m0) = 0 and d φm0⁄= 0. Choose any codimension one smooth submanifold S of
M through m0 such that Hφ(m0) /∈ Tm0S. Then there is a locally unique smooth function f on
a neighborhood of m0 such that{φ, f} =LHφf = 1 and f = 0 on S. It follows from (3.22) that
the symplectic product of H φ and Hf is equal to one, which implies that at every points these
vectors are linearly independent, which in turn implies that at every point d φ and df are linearly
independent. This implies in particular that
N :={m∈U|f(m) =φ(m) = 0}
is a smooth codimension 2 submanifold of the open neighborhood U of m0 on which φ and f
are deﬁned. Moreover, the restriction σN of σ to N is a symplectic form, because the symplectic
orthogonal complement of TnN is spanned by Hφ(n) and Hf(n), which space is complementary to
the TnN = ker(dφn)∩ ker(dfn), as is readily veriﬁed.
It follows from (3.25) and the fact that the Hamiltonian vector ﬁeld of any constant function is
equal to zero, that the vector ﬁelds H φ and Hf commute, which implies that their ﬂows commute
as well. Now deﬁne, for n∈N and t, τ∈ R,
Φ(n, t, τ) := et Hφ◦ e−τ Hf (n) = e−τ Hf◦ et Hφ(n).
Then ∂Φ(n, t, τ)/∂t = Hφ(Φ(n, t, τ)) and ∂Φ(n, t, τ)/∂τ =− Hf(Φ(n, t, τ)). It follows that the
value s which (Φ∗σ)(n,t,τ ) takes on the pair of vectors ( δn, δt, δτ) and (δn′, δt′, δτ′) is equal to
σΦ(n,t,τ )(v, v′), in which
v = Tn
(
et Hφ◦ e−τ Hφ
)
δn +δt Hφ−δτ Hf,
and v′ is given by the same formule with δn, δt, δτ replaced by δn′, δt′, δτ′, respectively. Using
again that σ(Hφ, Hf) = 1 and that Hamiltonian ﬂows preserve the symplectic form, we arrive at
the conclusion that
s =σn(δn, δn′) +δτδt′−δτ′δt.
This shows that Φ∗σ is equal to the direct sum of σN and the standard symplectic form in R2. The
proof of Darboux’s lemma now follows by induction on n.
Remark 3.3 Weinstein [27] gave a proof of the Darboux lemma which is based on a deformation
argument which has been introduced in normal form theory by Moser [24]. The proof given above
is closer to the one given by Darboux. Both proofs have their merits. ⊘
If we combine the Darboux lemma with the reduction in Subsection 2.3, then one obtains that any
closed two-form of constant rank has a local normal form.
3.7 Hamiltonian Group Actions
If a Lie group G acts on the smooth manifold M, we will denote for eachg∈G the diﬀeomorphism
m↦→ gm of M by gM. For each element X in the Lie algebra g of G we have the inﬁnitesimal
action
XM :=
d
dt (exp(tX ))M
⏐⏐⏐
t=0
28

ofX onM, which is a smooth vector ﬁeld onM. Note that, as a consequence, (exp(tX ))M = etXM
for every t∈ R.
The deﬁnition (3.8) of the Lie brackets of vector ﬁelds implies that
[X, Y]M =−[XM, YM], X, Y ∈ g, (3.27)
i.e. the mapping X↦→ XM is an anti-homomorphism from the Lie algebra g to the Lie algebra
X (M).
Now suppose thatσ is a symplectic form onM. The action ofG onM will be called Hamiltonian
with respect to σ, if for every X∈ g we have given a smooth function ⟨X, µ⟩ on M such that
XM = H⟨X,µ⟩. (3.28)
It will furthermore be required that ⟨X, µ⟩ depends linearly on X∈ g and that
{⟨X, µ⟩,⟨Y, µ⟩} =−⟨[X, Y], µ⟩, X, Y ∈ g. (3.29)
In other words, we require that X↦→⟨ X, µ⟩ is an anti-homomorphism of Lie algebras from g to
the Poisson Lie algebraF(M) of all smooth functions on M.
The condition that the inﬁnitesimal actions are Hamiltonian implies that the one-parameter
subgroups preserve the symplectic form. Therefore, if G is connected, it follows that the G-action
leaves the symplectic form invariant. In other words, the action is a homomorphism from G to the
group of canonical transformations in (M, σ).
For everym∈M, µ(m) :X↦→⟨X, µ⟩(m) is a linear form on g, this deﬁnes a smooth mapping
µ : M→ g∗ which is called the momentum mapping of the Hamiltonian action of G on M. Note
that the notation has been arranged such that ⟨X, µ(m)⟩ =⟨X, µ⟩(m) for every m∈M.
On g we have the adjoint action (g, X)↦→ (Adg)(X) of G, and transposition leads to the action
(g, ξ)↦→ ((Adg)∗)−1 (ξ)
on the dual g∗ of the Lie algebra, which is called the co-adjoint action ofG on g∗. The inﬁnitesimal
co-adjoint action of X∈ g is given by the linear mapping
Xg∗ =−(adX)∗ : g∗→ g∗,
or, more explicitly,
⟨Y, Xg∗ξ⟩ =−⟨[X, Y], ξ⟩, ξ ∈ g∗, X, Y∈ g. (3.30)
If in (3.30) we substitute ξ = µ(m) and combine the resulting equation with (3.29), and use
that the left hand side of (3.29) is equal to LXM⟨Y, µ⟩, we arrive at the conclusion that
LXMµ =Xg∗µ, (3.31)
which means that the momentum mapping µ :M→ g∗ intertwines the inﬁnitesimal action of g on
M with the inﬁnitesimal co-adjoint action of g on g∗. If G is connected, then this implies in turn
that the momentum mapping intertwines the action of G onM with the co-adjoint action of G on
g∗, in the sense that
g∗
Mµ = ((Adg)∗)−1 µ, g ∈G. (3.32)
29

Example 3.3 A very simple, but important example of a Hamiltonian group action on ( M, σ)
can be obtained as follows. Assume that fi, 1≤i≤k, are smooth functions on M which Poisson
commute, i.e. {fi, fj} = 0 for all 1 ≤i, j≤k. Let f :M→ Rk be the mapping which has the fi
as components. Then for every c∈ Rk the level set Mc :={m∈M|f(m) =c} is invariant under
the ﬂows of the Hamiltonian vector ﬁelds H fi. Let us assume that the Hamiltonian vector ﬁelds
Hfi are complete, which condition in view of the above is certainly satisﬁed if the level set Mc is
compact.
In view of (3.25), the fact that the functions fi Poisson commute implies that the Hamiltonian
vector ﬁelds Hfi commute, which in turn implies that their ﬂows commute. This implies that
((t1, ..., tk), m)↦→ etk Hfk◦... ◦ et1 Hf1(m)
deﬁnes an action of tha additive group ( Rk, +) on M. This action is Hamiltonian, with f as its
momentum mapping. Because the Lie algebra Rk is commutative, the adjoint action is trivial,
hence the co-adjoint action is trivial as well and the fact that f intertwines the action on M with
the co-adjoint action reproduces the observation that the functionsfi are invariant under the action
on M.
The system is called integrable if k =n and the mapping f has regular values. If c is a regular
value of f, then Mc is an n-dimensional smooth submanifold of M on which the action is locally
transitive, and therefore is transitive on each connected component C of Mc. If we choose m∈C,
then the period lattice PC in Rn is deﬁned as the set of all T ∈ Rn such that TM(m) = m. PC
does not depend on the choice of m∈C (but in general it depends sensitively on the level c), and
PC is a discrete subgroup of Rn. The mapping t↦→tM(m) induces a diﬀeomorphism from Rn/PC
ontoC, which intertwines the translational action of Rn on Rn/PC with the action of Rn on C.
If C is compact, which certainly is the case if Mc is compact, then Rn/PC is compact, hence a
torus, and the ﬂow of each of the Hamiltonian vector ﬁelds H fi is quasi-periodic, meaning that by
means of a diﬀeomorphism it can be mapped to a constant speed motion on a standard torus. ⊘
3.8 Poisson Structures
It follows from the third expression in (3.22) and from (3.11) that
{f, g}(m) =−σ−1
m (df(m), dg(m)),
in whichπm :=σ−1
m : (TmM)∗→ TmM is regarded as an antisymmetric bilinear form on (TmM)∗,
or as an element of Λ 2 TmM, which is also called a two-vector in TmM.
For any smooth manifold M, a Poisson structure on M is deﬁned as a smooth two-vector ﬁeld
πm∈ Λ2 TmM, m∈M, in such a way that the corresponding Poisson brackets{f, g}, deﬁned by
{f, g}(m) =πm(df(m), dg(m)), m ∈M, (3.33)
satisfy the Jacobi identity (3.26).
Viewingπm as a linear mapping from (TmM)∗ to TmM, we can deﬁned the Hamiltonian vector
ﬁeld Hf of the function f by Hf(m) =πm df(m). With this convention, {f, g} =LHfg.
If πm is surjective, then it is bijective, and we have that πm =−σ−1
m for a symplectic form on
M. We therefore only get really new examples of Poisson structures if πm is not surjective.
30

WriteHm =πm ((TmM)∗). If the rank of πm, the dimension of Hm, is constant as a function
of m∈M, then the Hm, m∈M, deﬁne a smooth vector subbundle H of TM, and it follows from
the Jacobi identity for the Poisson brackets that H is integrable. Furthermore, for each integral
manifoldI ofH, the restriction of{f, g} toI only depends on f|I andg|I, and we obtain a Poisson
structure on I, which turns out to be deﬁned by a sysmplectic structure on I. In this way the
Poisson manifold (M, π) can be characterized as a manifold which is foliated by symplectic leaves,
where the Poisson brackets are deﬁned by taking the Poisson brackets of the restrictions of the
functions to the symplectic leaves.
A prime example is the Poisson structure in g∗ which is deﬁned by
πξ(X, Y) =−⟨[X, Y], ξ⟩, ξ ∈ g∗, X, Y ∈ (g∗)∗ = g. (3.34)
The symplectic leaves are the co-adjoint orbits in g∗.
The formula (3.29) shows that, for a Hamiltonian action ofG on the symplectic manifold (M, σ),
the momentum mapping µ intertwines the Poisson structure on (M, σ) with the Poisson structure
on the dual of the Lie algebra of G.
Remark 3.4 The general concept of Poisson structures has been invented by Lichnerowicz [20].
However, Lie [21, Vol. 2, Kap. 8] introduced a ”function group” as a ﬁbration φ of a symplectic
manifold (M, σ) over a manifoldN with the property that for every smooth pair of functionsf and
g onN the Poisson brackets{f◦φ, g◦φ} are constant along the ﬁbers of φ. This means that there
is a unique Poisson structure on N such that{f◦φ, g◦φ} ={f, g}N◦φ for every f, g∈F (N).
Moreover, in [21, Vol. 2, Kap. 19], Lie discussed the dual g∗ of the Lie algebra of a Lie group G,
and showed that the projection from T∗G onto g∗ by means of the left trivialization T∗G =G× g∗
is a ”function group”. The Poisson structure on g∗ deﬁned by this ”function group” is equal to the
one in (3.34). ⊘
3.9 Exercises
Exercise 3.1 Prove that
L[u,v ]ω = [Lu,Lv] ω
for every u, v∈X (M), ω∈ Ωp(M), p∈ Z≥0. ⊘
Exercise 3.2 Prove that in canonical coordinates the vector ﬁeld H f is linear, if and only if f is
equal to a quadratic form plus a constant. Prove that if f and g are quadratic forms, then {f, g}
is a quadratic form and we have the identity
H{f,g} = Hg◦ Hf− Hf◦ Hg
between 2n× 2n-matrices = linear mappings from R2n to R2n. Hint: verify ﬁrst that we have
H{f,g} = Hf◦ Hg− Hg◦ Hf if we view the vector ﬁelds as derivations. ⊘
Exercise 3.3 Letp∈M andv∈X (M). p is called an equilibrium point ofv if it is a ﬁxed point
for the v-ﬂows etv ,t∈ R. Now let v = Hf for a smooth function f onM. Prove that the following
statements are equivalent:
31

i) p is an equilibrium point of v = Hf.
ii) v(p) = 0.
iii) p is a stationary point of the function f in the sense that df(p) = 0.
In the sequel assume that p is an equilibrium point of v = Hf. Write A(t) := Tp
(
etv)
, which is a
linear mapping from E := TpM to itself. Write B := A′(0), which also is a linear mapping from
E to itself. Prove that A(t) = etB , t∈ R, that A(t)∈ Sp(E, σp), and that B is an inﬁnitesimally
symplectic matrix.
Prove that, if we view B as a (linear) vector ﬁeld on T pM, then B = Hf2, in which f2 denotes
the quadratic term in the Taylor expansion of f at the point p, where the Taylor expansion is
written down in any suitable system of local coordinates. Prove that f2 is independent of the
choice of the system of local coordinates. ⊘
Exercise 3.4 In (3.15), let ϵ run over a ﬁnite-dimensional smooth manifold E. Deﬁne Γ t :E→
TX by Γt(ϵ) = (γϵ(t), γ′
ϵ(t)), and deﬁne i :E→ R byi(ϵ) =I(γϵ). Assume furthermore that, for
everyϵ∈E, γϵ is a solution of the Euler-Lagrange equations [ L] = 0.
Let ΦL : TX→ T∗X be the velocity-to-momentum mapping deﬁned by L. Prove that
di = Γ∗
bΦ∗
Lτ− Γ∗
aΦ∗
Lτ,
in which τ is the tautological one-form on T∗X. Prove that
Γ∗
bΦ∗
Lσ = Γ∗
aΦ∗
Lσ.
Now let, for every ( x, v)∈ TX, t↦→ γ(x,v )(t) denote the solution γ of the Euler-Lagrange
equations such that γ(0) = x and γ′(0) = v. Apply the previous equation to this family of curves
in order to prove that Φ∗
Lσ is invariant under the Euler-Lagrange ﬂow in TX. ⊘
Exercise 3.5 With the notation of (3.13), prove that {µv, µw} =µ[v,w ]. ⊘
Exercise 3.6 Let (M, σ) be a 2n-dimensional symplectic manifold and let Φ : M→ R2n be a
smooth mapping with coordinate functions x1, ..., xn, ξ1, ..., ξn. Prove that
Φ∗
( n∑
i=1
dξi∧ dxi
)
=σ,
if and only if {xi, xj} = 0,{ξi, xj} =δij, and{ξi, ξj} = 0. ⊘
Exercise 3.7 Let β be a closed two-form on the conﬁguration space X, and let the force ﬁeld
F be given by F (x, v) = − dV (x)−βx(v) for every x∈X, v∈ TxX. Here we identify βx in the
usual way with a linear mapping from T xX to (TxX)∗. The term −βx(v) is called a magnetic
term in the force ﬁeld.
Prove thatσ+π∗β is a symplectic form on T∗X. Prove that the velocity-to-momentum mapping
ΦT : (x, v)↦→ (x, ∂T (x,v )
∂v transforms the equations of motion [T ] =F into the Hamiltonian system
deﬁned by the function h = (T +V )◦ Φ−1
T , not with respect to the canonical symplectic form σ of
T∗X, but with respect to the symplectic form σ +π∗β, the canonical stymplectic form ”shifted
by the magnetic term”. ⊘
32

4 Hamilton-Jacobi Theory
4.1 Lagrange Manifolds
Consider a ﬁrst order partial diﬀerential equation
f(x, dφ(x)) = 0, (4.1)
in which the unknown function φ is a smooth function deﬁned on an open subset U of an n-
-dimensional smooth manifold X and f is a given smooth function on an open subset V of the
cotangent bundle T∗X of X.
If we write
N :={(x, ξ)∈V |f(x, ξ) = 0} (4.2)
for the zeroset of f in T∗X and
Λ ={(x, dφ(x))∈ T∗X|x∈U} (4.3)
for the graph of dφ viewed as a subset of T∗X, then (4.1) is equivalent to the inclusion
Λ⊂N (4.4)
between subsets of T∗X.
The mapping dφ :x↦→ (x, dφ(x)) is a smooth mapping from U to T∗X, with image equal to
Λ and with the canonical projection π : T∗X→ X as a left inverse. Therefore d φ is a smooth
embedding and Λ is a smooth n-dimensional submanifold of T∗X. The fact that, for each λ∈ Λ,
the restriction to Tλ Λ of Tλπ is bijective from Tλ Λ to Tπ(λ)X is equivalent to the condition that
Tλ Λ∩ ker Tλπ = 0, (4.5)
i.e. Tλ Λ is complementary to the tangent space ker Tλπ of the ﬁber through the point λ.
Conversely, if Λ is any smooth n-dimensional submanifold of T∗X which satisﬁes (4.5), then
π|Λ is a local diﬀeomorphism from Λ onto an open subset U of X. If moreover π|Λ is injective,
which can be arranged by restricting to a suitable open neighborhood of any given point of Λ, then
π|Λ is a diﬀeomorphism, and its inverse α := (π|Λ)−1 : U → T∗X is a smooth one-form on U.
Locally the condition that α = dφ for a smooth function φ is equivalent to the condition that α is
closed, i.e. dα = 0
It follows from (2.3) and (2.4) that
dα =d(α∗τ) =α∗(dτ) =α∗σ,
and therefore α is closed if and only if α∗σ = 0. The latter condition means that, for every x∈U,
σα(x) (Txα(u), Txα(v)) = 0, u, v ∈ TxX. (4.6)
On the other hand
T(x,α (x)) Λ ={Txα(v)|v∈ TxX},
and therefore (4.6) means that T λ Λ is an isotropic linear subspace of T λ(T∗X), if we write λ =
(x, α(x)). Because dim Tλ Λ =n, it is a Lagrange plane in T λ(T∗X).
A Lagrange submanifold of a 2n-dimensional symplectic manifold ( M, σ) is deﬁned as an n-
dimensional smooth submanifold Λ of M such that, for every λ∈ Λ, Tλ Λ is a Lagrange plane in
TλM, with respect to the symplectic form σλ. We have just proved above that a submanifold Λ
of T∗X is equal to α(U) for a closed one-form on an open subset U of X, if and only if
33

i) Λ is a Lagrange submanifold of T ∗X,
ii) Λ is transversal to the ﬁbers of T ∗X in the sense of (4.5), and
iii) The restriction of π to Λ is injective.
4.2 Lie’s View on First Order PDE
It is the idea of Lie, to generalize the concept of a solution of (4.1) slightly, by ﬁrst investigating
what the condition means for a Lagrange submanifold Λ of a symplectic manifold ( M, σ) to be
contained in the given subset N ofM. Thereby he dropped the conditions ii) and iii), which relate
the position of Λ with respect to the projection π.
In the sequel we will assume that d f(n)⁄= 0 for every n∈N. This implies that N is a smooth
(2n− 1)-dimensional submanifold of M, and TnN = ker(df(n)) for every n∈ N. Furthermore,
Λ⊂N implies that, for every λ∈ Λ,
Tλ Λ⊂ TλN = ker(df(λ)),
which is equivalent to the inclusion
R Hf(λ) = ker(df(λ))σλ⊂ (Tλ Λ)σλ = Tλ Λ. (4.7)
of the σλ-orthogonal complements. In the ﬁrst identity in (4.7) we have used that the codimension
of ker(df(λ) is equal to one, and that σλ(u, Hf(λ)) = df(λ)(u) = 0 if u∈ ker(df(λ)). In the third
identity in (4.7) we have used that T λ Λ is a Lagrange plane with respect to the symplectic form
σλ.
The inclusion (4.7) means that, at every point of Λ, the vector ﬁeld H f is tangent tot Λ. This
implies that Λ is foliated by the one-dimensional solution curves of the Hamiltonian system deﬁned
by the function f.
Clearly, every submanifold I of Λ is isotropic, in the sense that, for every i∈ I, TiI is an
isotropic linear subspace of T iM. Also we have obviously that I⊂ N and that the ”H f-ﬂow-out
of I”, the set
I′ :=
{
et Hf (i)| (i, t)∈J
}
is contained in Λ, if J is a suitable open neighborhood of I×{ 0} in I× R. If dim I =n− 1 and
Hf(i) /∈ TiI for every i∈I, then the mapping
(i, t)↦→ et Hf (i)
is a smooth immersion, hence its image is n-dimensional, and the conclusion is that I′ is an open
subset of Λ. In this sense Λ is locally the only Lagrange submanifold of M such that I⊂ Λ⊂N.
Now suppose conversely thatI is an (n−1)-dimensional isotropic submanifold ofM,I⊂N and
Hf(i) /∈ TiI for every i∈I. Then I′ is an n-dimensional smooth submanifold of M. Furthermore
I′⊂ N, because f is invariant under the H f-ﬂow, and therefore its zeroset N is invariant under
the Hf-ﬂow. If i∈I then TiI⊂ TiN implies that
R Hf(i) = (TiN)σi⊂ (TiI)σ
34

and therefore
TiI′ = TiI + R Hf(i)
is isotropic, and hence a Lagrange plane because it is n-dimensional. If ( i, t)∈ J and we write
Φ = et Hf , then
TΦ(i)I′ = Ti Φ
(
TiI′)
is a Lagrange plane as well, because Ti Φ preserves the symplectic form. The conclusion is that I′ is
a Lagrange submanifold of M such that I⊂I′⊂N, and we have a local existence and uniqueness
theorem for Lagrange submanifolds Λ of M such that I⊂ Λ⊂N.
Remark 4.1 More generally, letN be a smooth submanifold ofM of any dimension, and suppose
that the dimension of Kn := TnN∩ (TnN)σ does not depend on n∈N. Because Kn is equal to
the kernel of the restriction to TnN ofσn, we are in the situation of Subsection (2.3) withω =σ|N.
Let π :N→P be a ﬁbration as in Subsection (2.3), and let σP be the reduced symplect ic form,
the symplectic form on P such that σ|N = π∗σP . Then the Lagrange submanifolds Λ of M such
that Λ⊂N are locally of the form Λ =π−1(ΛP ), in which ΛP is an arbitrary Lagrange submanifold
of P with respect to the symplectic form σP . This characterization is also due to Lie. ⊘
4.3 An Initial Value Problem
Let S be an (n− 1)-dimensional smooth submanifold of X and ψ a smooth real-valued function
on S. The above leads to a local existence and uniqueness theorem for solutions φ of (4.1) which
satisfy the additional ”initial condition” that
φ(s) =ψ(s), s ∈S. (4.8)
We will make the assumptions that x0∈S, ξ0∈ (Tx0X)∗, f (x0, ξ0) = 0,
∂f (x0, ξ)
∂ξ
⏐⏐⏐⏐
ξ=ξ0
/∈ Tx0S. (4.9)
and ﬁnally
dψ(x0) = ξ0|Tx0S. (4.10)
Obviously the condition (4.10) is necessary if we want to have ξ0 = dφ(x0) for a solution φ of (4.1)
and (4.8). The transversality condition (4.9) is the natural one in order to avoid singularities in
the solution.
For every s∈ S, the restriction mapping ξ↦→ ξ|TsS is a linear mapping from (T sX)∗ onto
(TsS)∗ with a one-dimensional kernel, equal to (T sS)0. Therefore the set
ls :=
{
ξ∈ (TsX)∗| ξ|TsS = dψ(s)
}
is a straight line in (T sX)∗, and the condition (4.9) means that, at ξ0, lx0 is transversal to
N∩ (Tx0X)∗. It follows therefore from the implicit function theorem, that there is an open
neighborhood S0 of x0 in S and a neighborhood W of (x0, ξ0) in T∗X, such that for each s∈S0
there is a unique ξ =ξ(s)∈ (TsX)∗, such that (x, ξ)∈W and
ξ|TsS = dψ(s) and f(s, ξ) = 0. (4.11)
35

Moreover,s↦→ (s, ξ(s)) is a smooth mapping from S0 to T∗X. Because it has π as a left inverse,
it is an embedding and the image is a smooth ( n− 1)-dimensional subsmanifold I of T∗X, which
by construction is contained in N.
Below we shall prove that I is isotropic. According to Subsection 4.2, locally there is a unique
Lagrange submanifold Λ of T∗X such that I⊂ Λ⊂N, and
Tλ0 Λ = Tλ0I + R Hf(λ0)
if λ0 = (x0, ξ0). Because T λ0π maps Tλ0I onto Tx0S and maps Hf(λ0) to ∂f/∂ξ (λ0) /∈ Tx0S,
cf. (4.9, we have that the restriction to T λ0 Λ of Tλ0π is surjective from T λ0 Λ to Tx0X, hence
bijective, because both vector spaces have the same dimension n. It follows that the transversality
condition (4.5) holds at λ = λ0, and therefore Λ is locally equal to the graph of d φ for a smooth
function φ, which is a solution of (4.1) because Λ ⊂N. On the other hand I⊂ Λ implies that for
all s in a connected neighborhood S0 of x0 in S we have that the restriction to T sS of dφ(s) is
equal to dψ(s), which implies that d
(
φ|S0
)
= dψ, or φ|S0−ψ = c is a constant. Replacing φ by
φ−c we arrive at the locally unique solution of the initial value problem (4.1), (4.8).
In order to prove thatI is an isotropic submanifold of T∗X, we consider the submanifold T∗
SX
of all (x, ξ)∈ T∗X such that x∈S andξ∈ (TxX)∗. Let ι denote the identity as a mapping from
T∗
SX to T∗X, and deﬁne the restriction mapping ρ : T∗
SX→ T∗S by
ρ(x, ξ) =
(
x, ξ|TxS
)
, x ∈S, ξ ∈ (TxX)∗.
Then
ι∗ (τT∗X) =ρ∗ (τT∗S) on T ∗
SX,
which is a tautology if one writes out the deﬁnitions of the left and right hand side. Taking
the exterior derivative of the left hand side and using that the exterior derivative commutes with
pullbacks by smooth mappings, we obtaine that
ι∗ (σT∗X) =ρ∗ (σT∗S) on T ∗
SX.
Because the graph of d ψ is an isotropic submanifold Λ S of T∗S, it follows that ρ−1(ΛS) is an
isotropic submanifold of T∗X, and therefore I =ρ−1(ΛS)∩N is isotropic as well.
4.4 Ray Bundles
It is a classical observation that the bundles of rays (= straight lines) which appear in geometrical
optics, are orthogonal to some hypersurface S. An example is the bundle of rays which emanate
from a given source point, these are the normals to every sphere with center at the source point.
In the plane every bundle of rays = one-parameter familty of straight lines is orthogonal to some
curve, for this it suﬃces to take a solution curve of a vector ﬁeld which is orthogonal to the rays.
However, in higher dimensions n it is a quite special property of an ( n− 1)-parameter family of
rays to be normal to a hypersuface S.
LetS be an oriented hypersurface, which leads to an orientation of the normals of S. Let φ be
the function which is equal to zero on S and has derivative in the direction of the oriented normals
equal to 1. Then, at least where the normals deﬁne a ﬁbration of the space, φ is a smooth function,
and the rays are orthogonal to every level hypersurface of φ. Indeed, if n(s) denotes the normal
vector to S at the point s∈S, then the level set of φ at the level t is equal to the set of points
St ={s +tn (s)|s∈S}
36

and its tangent space consists of the pointsδs+t Dn(s)δs in whichδs is tangent toS. It follows from
⟨n(s), n(s)⟩≡ 1 that⟨Dn(s)δs, n(s)⟩ = 0, and therefore⟨δs +t Dn(s)δs, n(s)⟩ =⟨δs, n(s)⟩ = 0.
It follows that the gradient of φ at the point s +tn (s) is equal to n(s), which means that the
function φ satisﬁes the nonlinear ﬁrst order partial diﬀerential equation
n∑
i=1
(∂φ(x)
∂xi
)2
= 1. (4.12)
Conversely, ifφ satisﬁes (4.12), then the normals to the level hypersurfaces ofφ form an (n−1)-
parameter family of straight lines.
Hamilton [10] discovered this bijective correspondence between the ray bundles in geometrical
optics and real-valued function φ which satisfy a partial diﬀerential equation of the form (4.12),
where the rays are the the lines which are orthogonal to the level surfaces of φ. He called φ the
characteristic function of the ray bundle , and the partial diﬀerential equation (4.12) is sometimes
called the eikonal equation of geometrical optics.
The equation (4.12) is of the form (4.1), if we take
f(x, ξ) =
n∑
i=1
(ξi)2− 1. (4.13)
The corresponding Hamiltonian system is d x/ dt = 2ξ, dξ/ dt = 0, we obtain that the velocity
vector dx(t)/ dt does not depend on t. Moreover, it is pointing in the direction of ξ = grad φ,
which means that the projections x(t) to the position space X = Rn are straight lines orthogonal
to the level hypersurfaces of φ, they form the ray bundle corresponding to solution φ of the eikonal
equation.
In the construction of the characteristic function, it is essential that the rays deﬁne a ﬁbration of
X, which is the case as long as the Lagrange manifold Λ, which is supposed to be the graph of dφ, is
transversal to the ﬁbers, cf. (4.5). However, it is a very common phenomenon that at some points
the rays start criss-crossing, which correspond to points where the transversality condition (4.5) no
longer holds. At such a point the density of the rays becomes inﬁnite, and for this reason such a
point is called a caustic point, a point ”where the light burns”. At caustic points the characteristic
function is no longer smooth, and at points through which more than one ray passes the function
φ becomes multi-valued.
The good news is that, even if such singularities in the ray bundle and its characteristic function
occur, the Lagrange manifold Λ remains a smoothly immersed submanifold of T∗X. Therefore, in
order to include ray bundles with caustics, we propose the following deﬁnition:
A ray bundle consists of the projections to the base manifold X of the Hf-solution curves in a
smoothly immersed Lagrange submanifold of T∗X, which is contained in the zeroset of f.
This makes Lie’s point of view, of allowing any smoothly immersed Lagrange submanifold of T∗X
which is contained in the zeroset of f as a solution of (4.1), not just aan matter of abstract
generalization, but very relevant from the point of view of practical applications.
Ray propagation in inhomogenous media, where the local speed of propagation c(x) depends
smoothly on the position x∈X, is described by the above theory in which the function f in (4.13)
is replaced by
f(x, ξ) =c(x)2
n∑
i=1
(ξi)2− 1.
37

Ray bundles deﬁned by other types of functions f on T∗X also have applications.
4.5 High Frequency Waves and Fourier Integral Operators
Huygens [15] could not convince the physicists of the wave nature of light, but Young and especially
Fresnel [8] did, with their beautiful quantitative analysis of interference patterns, which have no
decent explanation in a particle model.
Let us consider waves which are solutions of the standard wave equation
2 := ∂2u
∂t2− ∆u := ∂2u
∂t2−
n∑
j=1
∂2u
∂x2
j
. (4.14)
Let us see what happens if we apply the wave operator 2 to a simple progressing wave
u(x, t) =eiω (t−φ(x))a(x), (4.15)
in which φ(x) and a(x) are real valued functions of x, called the phase function and the amplitude
function of the simple progressing wave, where the level surfaces φ(x) = t in the position space,
the x-space, are the wave fronts. ω is a frequency variable, and we are in particular interested in
the asymptotic behaviour as ω→∞ . (Due to the small wave length and the very high speed of
propagation, visible light has an extremely high frequency.)
We have
(2u)(x, t) =eiω (t−φ(x))[
ω2u2(x, t) +iωu 1(x, t) +u0(x, t)
]
,
in which
u2(x, t) =


n∑
j=1
(∂φ(x)
∂xj
)2
− 1

 a(x),
u1(x, t) = 2
n∑
j=1
∂φ(x)
∂xj
∂a(x)
∂xj
+ (∆φ)(x)a(x)
and u0(x, t) =−∆a(x).
Ifa(x)⁄= 0, then (2u)(x, t) grows quadratically as a function of ω forω→∞ , unless the phase
function φ(x) satisﬁes the eikonal equation (4.12).
Assuming that φ satisﬁes the eikonal equation, the leading term in 2u grows linearly with ω,
unless the amplitude satisﬁes the homogeneous linear ﬁrst order partial diﬀerential equation
u1(x, t) = 2
n∑
j=1
∂φ(x)
∂xj
∂a(x)
∂xj
+ (∆φ)(x)a(x) = 0, (4.16)
called the transport equation for the amplitude.
In order to analyse (4.16), we consider the solutions x(s) of the system of ordinary diﬀerential
equations
dxj
ds = 2∂φ(x)
∂xj
, 1≤j≤n. (4.17)
38

The solution curves of (4.17) are orthogonal to the wave fronts φ(x) = constant, and therefore are
equal to the rays of the ray bundle of whichφ is the characteristic function. The transport equation
(4.16) then is equivalent to
da(x(s))
ds + (∆φ)(x(s))a(x(s)) = 0,
a homogeneous ﬁrst order linear ordinary diﬀerential equation for the function s↦→a(x(s)). This
implies that we can prescribe a(x) freely on an (n− 1)-dimensional manifold S which is transversal
to the rays. If we choose the ”initial amplitude” a|S equal to zero outside a small neighborhood of
a given point x0 then the solution a(x) will be equal to zero outisde a narrow tube along the ray
through the point x0. In this sense the waves u of the form (4.15) which are asymptotic solutions
of (4.14) in the sense that 2u remains bounded as ω→∞ , will propagate along the rays . In this
sense geometrical optics is the high frequency limit of wave optics.
The procedure can be reﬁned by replacing the amplitude function a(x) in (4.15) by an asymp-
totic expansion of the form
a(x, ω)∼
∞∑
k=0
aj(x)ω−k, ω →∞
in negative powers of the frequency ω. One may verify that by successively solving inhomogenous
linear ordinary diﬀerential equations along the rays for the ak(x), k≥ 1, one can arrange that, for
anyK, 2u =O(ω−K) as ω→∞ .
As observed in Subsection 4.4, the construction of the phase function φ(x), and therefore of the
simple progressing wave (4.15), brakes down at caustic points, and the amplitude a(x) becomes
inﬁnite if one approaches such a point. It turns out that near such points one can still obtain
asymptotic solutions of the wave equation by replacing the simple progressing wave (4.15) by a
”continuous superposition” of such waves, an oscillatory integral of the form
u(x, t)∼
∞∑
k=0
ωN/2−k
∫
RN
eω (t−φ(x,θ )) ak(x, θ) dθ, ω →∞. (4.18)
Here, in order to avoid any problems with the convergence of the integral over the auxiliary θ-
-variables, it is assumed that ak(x, θ) = 0 for all θ outside a compact subset. Maslov [23] showed
that for quite general linear partial diﬀerential equations Pu = 0 one can construct oscillatory
integrals (4.18) which are global asymptotic solutions, i.e. also in neighborhoods of caustic points.
These oscillatory integrals correspond to Lagrange submanifolds Λ of T ∗X which are contained
in the zeroset of a certain function p on T∗X which is called the principal symbol of the linear
diﬀerential operator P . Cf. [6] for a survey.
If one also integrates over the frequency variable ω, then one obtains distributions, which are
called Fourier integral distributions , invented by H¨ ormander [14]. The singularities of a Fourier
integral distribution, i.e. its behaviour near points where it is not equal to a smooth function, have
a very precise description in terms of the corresponding Lagrange submanifold of T ∗X.
A simple example is Dirac’s delta function situated at a point x∈ X. It is a Fourier integral
distribution and the Lagrange manifold corresponding to it is the ﬁber (T xX)∗ of the cotangent
bundle T∗X over the point x. This is an extreme example of a Lagrange manifold which does not
satisfy the transversality condition (4.5).
Linear integral operators fromF(Y ) toF(X) which have a distribution kernel on X×Y which
is a Fourier integral distribution are called Fourier integral operators. These form a very wide class
39

of operators, which include all the propagation operators = ”Green functions” of linear partial
diﬀerential equations Pu = 0 of wave type. The aforementioned description of the singularites of
Fourier integral distributions leads to very detailed descriptions of the propagation of singularities
of the solutions of the partial diﬀerential equation Pu = 0, or of the corresponding inhomogenous
equation Pu =f, cf. [5].
4.6 Some History
As already mentioned, Hamilton [10] found the description of ray bundles in geometrical optics
in terms of their characteristic functions, together with the nonlinear partial diﬀerential equation
(4.12 satisﬁed by the characteristic function.
However, he did not ask the question how to solve a general nonlinear partial diﬀerential equa-
tion of the form (4.1). — it was Jacobi [16], [17] who observed that the solution of such a partial
diﬀerential equation can be reduced to the solution of a Hamiltonian system of ordinary diﬀerential
equations. Since then the theory is called ”Hamilton-Jacobi theory”.
Lie developed the idea of viewing the solution as a Lagrange submanifold of the cotangent
bundle in a series of articles in 1872–78, and stressed the point that it is based on the fact that the
ﬂow of the Hamiltonian system of the function f leaves the canonical two-form σ of the cotangent
bundle invariant. For him the use of the group of transformations which leavef andσ invariant was
analogous to the use of the Galois group in the solution of polynomial equations. Engel introduced
the name ”Verein” = ”club” for any submanifold of the cotangent bundle. Lie followed this, but
later authors like ´Elie Cartan didn’t. An accessible account of Lie’s ideas on ﬁrst order partial
diﬀerential equations is the book of Engel and Faber [7].
The fact that Lagrange manifolds are fundamental in so many situations made Weinstein [28]
talk about the Symplectic Creed: ”Everything is a Lagrange manifold”. More recently so-called
special Lagrange manifolds, invented by Harvey and Lawson [12], made their appearance in mirror
symmetry.
4.7 Exercises
Exercise 4.1 In the notation of Example 3.3 on integrable systems, prove that the level sets Mc
are Lagrange submanifolds of M. If M = T∗X and the connected component C ofMc is compact,
thenC can only be equal to dφ for some smooth function φ onX, if X is diﬀeomorphic to a torus.
⊘
Exercise 4.2 Prove that, for any givenx∈X, the ﬁber (TxX)j overx is a Lagrange submanifold
of T∗X. Deﬁne
I ={ξ∈ (TxX)∗|f(x, ξ) = 0}.
Suppose that ∂f (x, ξ)/∂ξ⁄= 0 for every ξ∈ I. Prove that N is an (n− 1)-dimensional isotropic
submanifold of T∗X, that (i, t)↦→ et Hf (i) deﬁnes a smooth immersion from an open subset J of
I× R to T∗X, and that the image is a smoothly immersed Lagrange submanifold Λ of T ∗X such
that Λ⊂N, where N denotes the zeroset of f in T∗X. Verify that the the projections in X of the
Hf-solution curves in Λ all pass through the given pointx. This is called the ray bundle emanating
fromx, for a general function f on T∗X. ⊘
40

References
[1] V.I. Arnol’d: Characteristic class entering in quantization condition. Func. Anal. Appl. 1
(1967) 1–13.
[2] N. Burgoyne and R. Cushman: Conjugacy classes in linear groups. J. Algebra 44 (1977) 339–
362.
[3] E.A. Coddington and N. Levinson: Theory of Ordinary Diﬀerential Equations . McGraw-Hill
Book Company, Inc., New York, etc., 1955.
[4] R. Cushman and J.J. Duistermaat: The behavior of the index of a periodic linear hamiltonian
system under iteration. Advances in Math. 23 (1977) 1–21.
[5] J.J. Duistermaat and L. H¨ ormander: Fourier integral operators II. Acta Math. 128 (1972)
183–269.
[6] J.J. Duistermaat: Osicllatory integrals, Lagrange immersions and unfoldings of singularities.
Comm. Pure Appl. Math. 27 (1974) 207–281.
[7] F. Engel und K. Faber: Die Liesche Theorie der partiellen Diﬀerentialgleichungen Erster
Ordnung. Teubner, Berlin, 1935.
[8] A. Fresnel: M´ emoire sur la diﬀraction de la lumi` ere, couronn´ e par l’Acad´ emie des Sciences en
1819. pp. 247–382 in vol. 1 of: Œuvres Compl` etes d’Augustin Fresnel. Paris, 1866. Johnson
Reprint Corporation, New York, 1965.
[9] P. Griﬃths and J. Harris: Principles of Algebraic Geometry. John Wiley and Sons, New York,
etc,. 1978.
[10] W.R. Hamilton: Essay on the theory of systems of rays, with three supplements. Trans. Royal
Irish Acad. 15 (1828) 69–174, 16 (1830 and 1831) 4–62 and 85–92, 17 (1837) 1–144.
[11] W.R. Hamilton: On a general method in dynamics. Phil. Trans. Royal Soc. London (1834)
247–308, (1835) 95–144.
[12] R. Harvey and H.B. Lawson, Jr.: Calibrated geometries. Acta Math. 148 (1982) 47–157.
[13] L. H¨ ormander:An Introduction to Complex Analysis in Several Variables.North-Holland Publ.
Co., Amsterdam, 1973.
[14] L. H¨ ormander: Fourier integral operators I.Acta Math. 127 (1971) 79–183.
[15] C. Huygens: Trait´ e de la Lumi` ere. Van der Aa, Leyden, 1690.
[16] C.G.J. Jacobi: ¨Uber die Reduction der Integration der partiellen Diﬀerentialgleichungen er-
ster ordnung zwischen irgend einer Zahl Variabeln auf die Integration eines einzigen Systemes
gew¨ ohnlicher Diﬀerentialgelichungen.Crelle’s Journal f¨ ur die reine und angewandte Mathe-
matik 1 (8137) 97–162 = Gesammelte Werke, 4. Band, 1886. Reprint Chelsea Publ. Cy., New
York, 1969.
41

[17] C.G.J. Jacobi: Vorlesungen ¨ uber Dynamik. Gehalten an der Universit¨ at K¨ onigsberg im Win-
tersemester 1842–43 und nach einem von C.W. Borchardt ausgearbeiteten Hefte. Verlag G.
Reimer, Berlin, 1881. Reprint Chelsea Publ. Cy., New York, 1969.
[18] C.G.J. Jacobi: Nova methodus, equationes diﬀerentiales partiales primi orins inter numerum
variabilium quemcuque propositas integrandi. Crelle journal f¨ ur die reine und angewandte
Mathematik 60 (1862) 1–181. Also in: Gesammelte Werke , V. Band, 1–189., Berlin 1890.
Reprint Chelsea Publ. Cy., New York, 1969.
[19] J.-L. Lagrange: M´ ecanique Analytique. First print 1788 in Paris. Reprint by A. Blanchard,
Paris, 1965.
[20] A. Lichnerowicz: Les vari´ et´ es de Poisson et leurs alg` ebres de Lie associ´ ees.J. Diﬀerential
Geometry 12 (1977) 253–300.
[21] S. Lie: Theorie der Transformationsgruppen I–III. Unter Mitwirkung von Prof.dr. F. Engel.
Teubner, Leipzig, 1888, 1890, 1893.
[22] B. Malgrange: Sur l’integrabilit´ e des structures presques-complexes. pp. 289-296 in: Symposia
Mathematica II, INDAM, Rome, 1968.
[23] V.P. Maslov: Th´ eorie des Perturbations et M´ ethodes Asymptotiques. Dunod, Gauthier-Villars,
Paris, 1972. This is a French translation of the book published in 1965 by the University of
Moscow, with some additions.
[24] J. Moser: On the volume elements on a manifold. Trans. Amer. Math. Soc.120 (1965) 286–294.
[25] A. Newlander and L. Nirenberg: Complex analytic coordinates in an almost complex manifold.
Annals of Math. 65 (1957) 391–404.
[26] Julius Pl¨ ucker:Neue Geometrie des Raumes, gegr¨ undet auf die Betrachtung der gerade Linie
als Raumelement. Teubner Verlag, Leipzig, 1868/89.
[27] A. Weinstein: Symplectic manifolds and their Lagrangian submanifolds. Advances in Mathe-
matics 6 (1971) 329–346.
[28] A. Weinstein: Symplectic geometry. Bull. Amer. Math. Soc. 5 (1981) 1–13.
[29] Hermann Weyl: The Classical Groups, their invariants and representations. Princeton Univer-
sity Press, Princeton, N.J., 1939, 1946.
[30] John Williamson: On the algebraic problem concerning normal forms of linear dynamical
systems. Amer. J. Math. 58 (1936) 141–163.
42

