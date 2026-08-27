Solutions of Qualifying Exams I, 2013 Fall
1. (Algebra) Consider the algebra M2(k) of 2× 2 matrices over a ﬁeld k.
Recall that an idempotent in an algebra is an element e such that e2 =e.
(a) Show that an idempotent e∈M2(k) diﬀerent from 0 and 1 is conjugate
to
e1 :=
( 1 0
0 0
)
by an element of GL2(k).
(b) Find the stabilizer inGL2(k) ofe1∈M2(k) under the conjugation action.
(c) In case k = Fp is the prime ﬁeld with p elements, compute the number of
idempotents in M2(k). (Count 0 and 1 in.)
Solution. (a) Since e⁄= 0, 1, the image and the kernel of e are both one-
dimensional. Let v1 be a nonzero element in the image, so v1 = e(v0) for
some v0∈k⊕2. Then
e(v1) =e(e(v0)) =e2(v0) =e(v0) =v1.
Pick a nonzero element v2 in the kernel of e, and we get a basis of k⊕2 in
whiche takes the form e1.
(b) For a general element
g =
( a b
c d
)
to be in the stabilizer, it must satisfy ge1 = e1g. Writing the equation in
four entries out, one sees that it means b = c = 0 (and a,d arbitrary). So
the centralizer is the subgroup of diagonal matrices.
(c) By (a) and (b), the set of rank 1 idempotents is in bijection withGL2(Fp)/T (Fp),
whose cardinality is
(p2− 1)(p2−p)
(p− 1)(p− 1) = (p + 1)p.
So the total number of idempotents is equal to p2 +p + 2.
1

2. (Algebraic Geometry) (a) Find an everywhere regular diﬀerential
n-form on the aﬃne n-space An.
(b) Prove that the canonical bundle of the projectiven-dimensional space Pn
isO(−n− 1).
Solution (Sketch). Part (a) is really a hint for Part (b). Lettingx1,x 2,...,x n
be aﬃne ( An) coordinates, putω :=dx1∧dx2···∧ dxn giving (a) . Denoting
the corresponding homogenous Pn coordinates t0,t 1,...,t n, with xi := ti/t0
for i = 1, 2,...,n extend ω to Pn writing dxi = dti/t0−ti/t2
0dt0 and wedg-
ing to discover that the divisor of poles of ω is (n + 1)H where H is the
hyperplane at inﬁnity (t0 = 0) and then conclude (appropriately).
3. (Complex Analysis) (Bol’s Theorem of 1949). Let ˜W be a domain in
C andW be a relatively compact nonempty subdomain of ˜W . Let ε> 0 and
Gε be the set of all (a,b,c,d )∈ C such that max (|a− 1|,|b|,|c|,|d− 1|)<ε .
Assume that cz +d⁄= 0 and az+b
cz+d∈ ˜W for z∈ W and (a,b,c,d )∈ Gε. Let
m≥ 2 be an integer. Prove that there exists a positive integer 𝓁 (depending
on m) with the property that for any holomorphic function ϕ on ˜W such
that
ϕ(z) =ϕ
(az +b
cz +d
) (cz +d)2m
(ad−bc)m
for z∈W and (a,b,c,d )∈Gε, the 𝓁-th derivative ψ(z) =ϕ(𝓁)(z) of ϕ(z) on
˜W satisﬁes the equation
ψ(z) =ψ
(az +b
cz +d
) (ad−bc)𝓁−m
(cz +d)2(𝓁−m)
for z∈W and (a,b,c,d )∈Gε. Express 𝓁 in terms of m.
Hint: Use Cauchy’s integral formula for derivatives.
Solution. Let
Az = az +b
cz +d
for A∈ Gε. We take a positive integer 𝓁 which we will determine later as
a function of n. We use Cauchy’s integral formula for derivatives to take
the 𝓁-th derivative ψ(z) of ϕ(z). For z∈ ˜W we use U(z) to denote an open
2

neighborhood of z in ˜W and use ∂U (z) to denote its boundary. The 𝓁-th
derivativeψ of ϕ at z∈ ˜W is given by the formula
ψ(z) = 𝓁!
2π√−1
∫
ζ∈∂U (z)
ϕ(ζ)dζ
(ζ−z)𝓁+1
and
ψ(Az) = 𝓁!
2π√−1
∫
ζ∈∂U (Az)
ϕ(ζ)dζ
(ζ−Az)𝓁+1 when Az∈ ˜W.
It follows from
ζ∈U(z)⇐⇒Aζ∈U(Az),
ζ∈∂U (z)⇐⇒Aζ∈∂U (Az),
with the change of variable ζ↦→Aζ, that
∫
ζ∈∂U (Az)
ϕ(ζ)dζ
(ζ−Az)𝓁+1 =
∫
Aζ∈∂U (Az)
ϕ(Aζ)d(Aζ)
(Aζ−Az)𝓁+1.
From the following straightforward direct computation of the discrete version
of the formula for the derivative of fractional linear transformation
Aζ−Az = aζ +b
cζ +d− az +b
cz +d
= (aζ +b)(cz +d)− (az +b)(cζ +d)
(cζ +d)(cz +d)
= (acζz +bcz +adζ +bd)− (acζz +adz +bcζ +bd)
(cζ +d)(cz +d)
= (ad−bc)(ζ−z)
(cζ +d)(cz +d)
we obtain
∫
Aζ∈∂U (Az)
ϕ(Aζ)d(Aζ)
(Aζ−Az)𝓁+1 =
∫
ζ∈∂U (z)
ϕ
(
aζ+b
cζ+d
)
ad−bc
(cζ+d)2dζ
(ad−bc)𝓁+1(ζ−z)𝓁+1
(cζ+d)𝓁+1(cz+d)𝓁+1
=
∫
ζ∈∂U (z)
ϕ(ζ) (ad−bc)m
(cζ+d)2m
ad−bc
(cζ+d)2dζ
(ad−bc)𝓁+1(ζ−z)𝓁+1
(cζ+d)𝓁+1(cz+d)𝓁+1
= (cz +d)𝓁+1
(ad−bc)𝓁−m
∫
ζ∈∂U (z)
ϕ(ζ)dζ
(ζ−z)𝓁+1 (cζ +d)𝓁−1−2m.
3

The extra factor ( cζ +d)𝓁−1−2m inside the integrand on the extreme right-
hand side becomes 1 and can be dropped if 𝓁− 1− 2m = 0, that is, if
𝓁 = 2m + 1. Thus, if 𝓁 = 2m + 1, then
ψ(Az) = (cz +d)𝓁+1
(ad−bc)𝓁−mψ(z).
That is,
ψ(z) =ψ
(az +b
cz +d
) (ad−bc)𝓁−m
(cz +d)2(𝓁−m),
because 𝓁 = 2m + 1 implies 𝓁 + 1 = 2(𝓁−m).
4. (Algebraic Topology) (a) Show that the Euler characteristic of any
contractible space is 1.
(b) LetB be a connected CW complex made of ﬁnitely many cells so that its
Euler characteristic is deﬁned. Let E→ B be a covering map whose ﬁbers
are discrete, ﬁnite sets of cardinality N. Show the Euler characteristic of E
is N times the Euler characteristic of B.
(c) Let G be a ﬁnite group with cardinality > 2. Show that BG (the classi-
fying space of G) cannot have homology groups whose direct sum has ﬁnite
rank.
Solution. (a) The homology of a point with coeﬃcients in a ﬁeldk isH0 =k,
Hi = 0 for i >0. Hence its Euler characteristic is ∑(−1)i dimHi = 1. All
contractible spaces are homotopy equivalent so their Euler characteristic is
that of the point.
(b) For any open cover {Ui}, we know that the chain complex of singular
chains living in Ui for some i has equivalent homology to the chain complex
of all chains. Taking the cover of B by trivializing neighborhoods Ui, the
chain complex of chains living in Ui receives a map from chains in E living
inπ−1(Ui). The latter is simply |G| direct sums of the former, and the chain
map between them is the “add every component” map. This shows the ranks
of homology of E is N times the rank of homology of B.
(c) Strictly speaking, this problem cannot be solved based on easy machinery
(as far as I know). A much more reasonable problem would be: Prove BG is
not homotopy equivalent to anything made up of only ﬁnitely many cells. I
did not take oﬀ points for people not distinguishing between this condition,
4

and the condition stated in the problem itself. We know BG =EG/G, but
EG is contractible. So χ(EG) = 1. If BG has ﬁnite homology, χ(BG) =
1/|G|, which cannot be an integer unless |G| = 1.
5. (Differential Geometry) Let H ={(x,y )∈ R2 : y > 0} be the
upper half plane. Let g be the Riemannian metric on H given by
g = (dx)2 + (dy)2
y2 .
(H,g ) is known as the half-plane model of the hyperbolic plane.
(a) Let γ(θ) = (cosθ, sinθ) and η(θ) = (cosθ + 1, sinθ) for θ∈ (0,π ) be two
paths inH. Compute the angle A at their intersection point shown in Figure
1, measured by the metric g.
Figure 1: Angle A between the two curves γ and η in the upper half plane
H.
(b) By computing the Levi-Civita connection
∇ ∂
∂xi
∂
∂xj
=
2∑
k=1
Γk
ij
∂
∂xk
of g or otherwise (where (x1,x 2) = (x,y )), show that the path γ, after arc-
length reparametrization, is a geodesic with respect to the metric g.
Solution. (a) The intersection point is (1/2,
√
3/2): solving for
γ(θ) = (cosθ, sinθ) = (cosφ + 1, sinφ) =η(φ)
we obtain θ =π/3, φ = 2π/3.
5

The angle A satisﬁes
cosA = ⟨γ′(π/3),−η′(2π/3)⟩g
||γ′(π/3)||g||− η′(2π/3)||g
= ⟨(−
√
3/2, 1/2), (
√
3/2, 1/2)⟩g
||(−
√
3/2, 1/2)||g||(
√
3/2, 1/2)||g
=
− 1
2
1
y2
1
y2
=−1
2
and so A = 2π/3.
(b) Using the formula
Γi
jk = 1
2gil(gjl,k +gjl,j−gjk,l)
one obtains
Γi
jk =−1
y (δijδk,2 +δkiδj,2−δjkδi,2).
After arc-length reparametrization, the tangent vectors of the path are
v(θ) = γ′(θ)
||γ′(θ)||g
= (− sin2θ, sinθ cosθ).
Then
∇v(θ)v(θ) =v′(θ) +
( Γ1
1 Γ1
2
Γ2
1 Γ2
2
)
·v(θ)
where
Γ1
1 = (− sinθ)Γ1
11 + (cosθ)Γ1
21 =− cotθ;
Γ1
2 = (− sinθ)Γ1
12 + (cosθ)Γ1
22 = 1;
Γ2
1 = (− sinθ)Γ2
11 + (cosθ)Γ2
21 =−1;
Γ2
2 = (− sinθ)Γ2
12 + (cosθ)Γ2
22 =− cotθ.
Thus one has∇v(θ)v(θ) = 0.
6

6. (Real Analysis) For any positive integern letMn be a positive number
such that the series∑∞
n=1Mn of positive numbers is convergent and its limit
is M. Let a < bbe real numbers and fn(x) be a real-valued continuous
function on [ a,b ] for any positive integer n such that its derivative f′
n(x)
exists for everya<x<b with|f′
n(x)|≤ Mn fora<x<b . Assume that the
series∑∞
n=1fn(a) of real numbers converges. Prove that
(a) the series ∑∞
n=1fn(x) converges to some real-valued function f(x) for
everya≤x≤b,
(b) f′(x) exists for every a<x<b , and
(c)|f′(x)|≤ M for a<x<b .
Hint for (b): For ﬁxed x∈ (a,b ) consider the series of functions
∞∑
n=1
fn(y)−fn(x)
y−x
of the variable y and its uniform convergence.
Solution. (a) Fix x∈ (a,b ]. For q > p≥ 1, by the Mean Value Theorem
applied to the function ∑q
n=pfn on [a,x ] we can ﬁnd a<ξ p,q <x such that
q∑
n=p
fn(x)−
q∑
n=p
fn(a) = (x−a)
q∑
n=p
f′
n (ξp,q),
which implies that
⏐⏐⏐⏐⏐
q∑
n=p
fn(x)
⏐⏐⏐⏐⏐≤
⏐⏐⏐⏐⏐
q∑
n=p
fn(a)
⏐⏐⏐⏐⏐ + (x−a)
⏐⏐⏐⏐⏐
q∑
n=p
f′
n (ξp,q)
⏐⏐⏐⏐⏐
≤
⏐⏐⏐⏐⏐
q∑
n=p
fn(a)
⏐⏐⏐⏐⏐ + (x−a)
q∑
n=p
Mn.
Since both series ∑∞
n=1fn(a) and ∑∞
n=1Mn are convergent and therefore
Cauchy, for anyε> 0 we can ﬁnd a positive integer N1 such that
⏐⏐⏐⏐⏐
q∑
n=p
fn(a)
⏐⏐⏐⏐⏐< ε
2
7

for q >p≥N1 and we can ﬁnd a positive integer N2 such that
⏐⏐⏐⏐⏐
q∑
n=p
Mn
⏐⏐⏐⏐⏐< ε
2(x−a)
for q >p≥N2. Thus for n≥ max(N1,N 2) we have
⏐⏐⏐⏐⏐
q∑
n=p
fn(x)
⏐⏐⏐⏐⏐<ε
and the series∑∞
n=1fn(x) is Cauchy. Hence the series ∑∞
n=1fn(x) converges
to some real-valued function f(x) for every a≤x≤b.
(b) Before the proof of the statement in (b), we would like to state that
the uniform limit of continuous functions is continuous. That is, if hn(x) is a
sequence of functions on a metric spaceE which converges to a functionh(x)
on E uniformly on E and if for some x0∈ E and for every n the function
hn(x) is continuous at x = x0, then h(x) is continuous at x0. This results
from the so-called 3 ε argument as follows. Given any ε >0. The uniform
convergence ofhn→h onE implies that there exists some positive integerN
such that|hN(x)−h(x)|<ε for allx∈E. Since hN is continuous atx =x0,
there exists some δ > 0 such that |hN(x)−hN (x0)| < εfor dE (x,x 0) < δ
(where dE (·,·) is the metric of the metric space E). Thus for dE (x,x 0)<δ
we have
|h(x)−h (x0)|≤| h(x)−hN(x)|+|hN(x)−hN (x0)|+|hN (x0)−h (x0)|< 3ε,
which implies the continuity of h at x =x0.
We now prove the statement in (b). Take x0∈ (a,b ). We introduce the
function gn,x0(x) on [a,b ] which is deﬁned by



gn,x0(x) = fn(x)−fn(x0)
x−x0
for x⁄=x0
gn,x0 (x0) =f′
n (x0).
It follows from the continuity of fn on [a,b ] and the existence of f′
n (x0) that
gn,x0 is a continuous function on [a,b ].
8

When x∈ [a,b ] with x⁄=x0, by the Mean Value Theorem
fn(x)−fn (x0)
x−x0
=f′
n (ξx)
for some ξx strictly between x0 and x and as a consequence
|gn,x0(x)| =|f′
n (x0)|≤ Mn.
When x =x0,
|gn,x0(x)| =|f′
n (x0)|≤ Mn.
Thus|gn,x0(x)|≤ Mn for x∈ [a,b ]. From ∑∞
n=1Mn≤ M <∞ it follows
that the series∑∞
n=1gn,x0 is uniformly convergent on [a,b ]. It follows that the
uniform limit∑∞
n=1gn,x0 is a continuous function on [a,b ] by the 3ε argument
given above. For x⁄=x0
∞∑
n=1
gn,x0(x) =
∞∑
n=1
fn(x)−fn (x0)
x−x0
= f(x)−f (x0)
x−x0
.
The continuity of∑∞
n=1gn,x0(x) at x =x0 means that the limit of
f(x)−f (x0)
x−x0
exists as x→x0, which implies that f′ (x0) exists and is equal to
∞∑
n=1
gn,x0 (x0) =
∞∑
n=1
f′
n (x0).
(c) From
f′ (x0) =
∞∑
n=1
gn,x0 (x0) =
∞∑
n=1
f′
n (x0)
and|f′
n (x0)|≤ Mn, it follows that
|f′ (x0)|≤
∞∑
n=1
Mn =M.
9

Solutions of Qualifying Exams II, 2013 Fall
1. (Algebra) Find all the ﬁeld automorphisms of the real numbers R.
Hint: Show that any automorphism maps a positive number to a positive
number, and deduce from this that it is continuous.
Solution. If t >0, there exists an element s⁄= 0 such that t = s2. If ϕ is
any ﬁeld automorphism of R, then
ϕ(t) =ϕ(s2) = (ϕ(s))2 > 0.
It follows that ϕ preserves the order on R: If t<t ′, then
ϕ(t′) =ϕ(t + (t′−t)) =ϕ(t) +ϕ(t′−t)>ϕ (t).
Any real number α is determined by the set (Dedekind’s cut) of rational
numbers that are less thanα, and any ﬁeld automorphism ﬁxes each rational
number. Therefore ϕ is the identity automorphism.
2. (Algebraic Geometry) What is the maximum number of ramiﬁcation
points that a mapping of ﬁnite degree from one smooth projective curve over
C of genus 1 to another (smooth projective curve of genus 1) can have? Give
an explanation for your answer.
Solution (Sketch). By the Riemann-Hurwitz formula, if we have a mapping
f of ﬁnite degree d from one smooth projective (irreducible, say) curve onto
another the Euler characteristic of the source curve isd times the Euler char-
acteristic of the target minus a certain nonnegative number e, and moreover
e is zero if and only if the mapping is unramiﬁed. Now compute: the Euler
characterstic of our source and target curves is, by hypothesis, 0 and so this
e is zero, and therefore the mapping is unramiﬁed.
3. (Complex Analysis) Let ω and η be two complex numbers such that
Im
(
ω
η
)
> 0. Let G be the closed parallelogram consisting of all z∈ C such
that z =λω +ρη for some 0≤λ,ρ≤ 1. Let ∂G be the boundary of G and
Let G0 =G−∂G be the interior of G. Let P1,··· ,Pk,Q 1,··· ,Q𝓁 be points
inG0 and letm1,··· ,mk,n 1,··· ,n𝓁 be positive integers. Let f be a function
on G such that
f(z)∏𝓁
j=1(z−Qj)nj
∏k
p=1(z−Pp)mp
10

is continuous and nowhere zero on G and is holomorphic on G0. Let ϕ(z)
andψ(z) be two polynomials on C. Assume that f(z +ω) =eϕ(z)f(z) if both
z and z +ω are in G. Assume also that f(z +η) = eψ(z)f(z) if both z and
z +η are in G. Express ∑k
p=1mp−∑𝓁
j=1nj in terms of ω and η and the
coeﬃcients of ϕ(z) and ψ(z).
Solution. Let A = 0, B = η, C = η +ω, and D = ω. Since Im
(
ω
η
)
> 0,
it follows that going from A to B, to C, to D and then back to A is in the
counterclockwise direction. By the argument principle
k∑
p=1
mp−
𝓁∑
j=1
nj = 1
2π√−1
∮
∂G
d logf
= 1
2π√−1
(∫
−→AB
d logf +
∫
− − →BC
d logf +
∫
−−→CD
d logf +
∫
− − →DA
d logf
)
= 1
2π√−1
(∫
−→AB
d logf−
∫
−−→CD
d logf +
∫
− − →BC
d logf−
∫
− − →AD
d logf
)
= 1
2π√−1
(
−
∫
−→AB
dϕ(z) +
∫
− − →AD
dψ(z)
)
= 1
2π√−1 (−ϕ(η) +ϕ(0) +ψ(ω)−ψ(0)).
Thus, the answer is
k∑
p=1
mp−
𝓁∑
j=1
nj = 1
2π√−1 (−ϕ(η) +ϕ(0) +ψ(ω)−ψ(0)).
4. (Algebraic Topology) (a) Fix a basis for H1 of the two-torus (with
integer coeﬃcients). Show that for every element x∈ SL(2, Z), there is an
automorphism of the two-torus such that the induced map on H1 acts by x.
Hint: SL(2, Z) also acts on the universal cover of the torus.
(b) Fix an embedding j : D2×S1→ S3. Remove its interior from S3 to
obtain a manifold X with boundary T 2. Let f be an automorphism of the
two-torus and consider the glued space
Xf := (D2×S1)∪f X.
If X is homotopy equivalent to D2×S1, compute the homology groups of
Xf.
11

Solution. (a) Given g∈ SL(2, Z)⊂ SL(2, R) let x : R2→ R2 be the in-
duced action. Since g is in SL(2, Z) it respects the relationship of whether
two vectors in R2 diﬀer by integer coordinates. So the map on the torus
[(x1,x 2)]↦→ [g(x1,x 2)] is well-deﬁned. This clearly sends a homology gener-
ating pair given by the curves (x1, 0) and (0,x 2) to the expected images via
g.
(b) There is an ambiguity in the problem about how f glues X and D2×
S1 together; so I gave full credit regardless of whether you identiﬁed this
ambiguity or not. Note Xf = (D2×S1)∪S1×S1X. Write U =D2×S1 and
V =X. The Mayer-Vietoris sequence gives
//H0(U∩V ) //H0(U)⊕H0(V ) //H0(U∪V )
//H1(U∩V ) //H1(U)⊕H1(V ) //H1(U∪V )
//H2(U∩V ) //H2(U)⊕H2(V ) //H2(U∪V )
//H3(U∩V ) //H3(U)⊕H3(V ) //H3(U∪V )
but because we know the homology of D2×S1≃S1 andS1×S1, we can ﬁll
in various groups in the long exact sequence:
Z // Z⊕ Z //H0(U∪V )
Z2 g // Z⊕ Z //H1(U∪V )
jj
Z // 0⊕ 0 //H2(U∪V )
jj
0 // 0⊕ 0 //H3(U∪V )
jj
Sinceg is an isomorphism, we know H1 must inject into Z, but the inclusion
map H0(U∩V )→H0(U)⊕H0(V ) is an injection, so H1(U∪V ) = 0.
12

We knowH0 is either equal to Z from the long exact sequence above, or
by observing that Xf is path-connected.
Iff induces an isomorphism, we seeH2 must be zero; this was the intent of
the problem, but you can get a diﬀerent answer based on how you interpreted
the ”gluing” by f.
Finally,H3 is also isomorphic to Z by the exactness of the above sequence.
5. (Differential Geometry) LetM =U(n)/O(n) forn≥ 1, whereU(n)
is the group ofn×n unitary matrices andO(n) is the group ofn×n orthogonal
matrices. M is a real manifold called the Lagrangian Grassmannian.
(a) Compute and state the dimension of M.
(b) Construct a Riemannian metric which is invariant under the left action
of U(n) on M.
(c) Let∇ be the corresponding Levi-Civita connection on the tangent bundle
TM , and X,Y,Z be any U(n)-invariant vector ﬁelds onM. Using the given
identity (which you are not required to prove)
∇XY = 1
2[X,Y ],
show that the Riemannian curvature tensor R of∇ satisﬁes the formula
R(X,Y )Z = 1
4[Z, [X,Y ]].
Solution. (a)
T[I]M∼= u(n)/o(n)∼= Sym2(Rn)
where Sym2(Rn) denotes the space of real n×n symmetric matrices. Thus
dimM = n(n + 1)
2 .
(b) Deﬁne a metric on Sym 2(Rn) by
⟨A,B⟩ = tr(ABt) = tr(AB).
g∈O(n) acts on T[I]M∼= Sym2(Rn) by g·A =gAg−1. Then
⟨g·A,g·B⟩ = tr(g·ABg−1) =⟨A,B⟩.
Hence this metric is invariant under the action of O(n). By translating the
metric to tangent spaces at other points by the action of U(n), this gives a
well-deﬁned invariant metric on U(n)/O(n).
13

(c)
∇XY = 1
2[X,Y ].
Then
R(X,Y )Z =∇X∇YZ−∇Y∇XZ−∇ [X,Y ]Z
= 1
4 ([X, [Y,Z ]]− [Y, [X,Z ]])− 1
2[[X,Y ],Z ]
= 1
4[Z, [X,Y ]]
where the last equality follows from Jacobi identity.
6. (Real Analysis) Show that there is no function f : R→ R whose set
of continuous points is precisely the set Q of all rational numbers.
Solution. For ﬁxed δ >0 let C(δ) be the set of points x∈ R such that for
someε> 0 we have|f(x′)−f(x′′)|<δ for all x′,x′′∈ (x−ε,x +ε). Clearly
C(δ) is open since for every x∈ C(δ), we have (x−ε,x +ε)⊂ C(δ). Now
letC denote the set of continuous points of f. From the deﬁnitions, we have
that
C =
∞⋂
n=1
C(1/n).
Now suppose that C = Q. Then
R− Q =
∞⋃
n=1
Xn,
where Xn = R−C(1/n). Since C(1/n) is open, Xn is closed. Also Q is
countable, say Q ={q1,q 2,... }. Let Yn ={qn}. Then
R =
(∞⋃
n=1
Xn
)
∪
(∞⋃
n=1
Yn
)
,
i.e. we have written R as a countable union of closed sets. Then by Baire’s
theorem, some Xn or Yn has nonempty interior. Clearly it cannot be one of
theYn. So there existsXn containing an interval (a,b ). But this is impossible
because Xn⊂ R− Q and every interval contains a rational number. Thus,
we obtain a contradiction, which shows that C⁄= Q.
14

Solutions of Qualifying Exams III, 2013 Fall
1. (Algebra) Consider the function ﬁelds K = C(x) and L = C(y) of one
variable, and regard L as a ﬁnite extension of K via the C-algebra inclusion
x↦→−(y5− 1)2
4y5
Show that the extension L/K is Galois and determine its Galois group.
Solution. Consider the intermediate extension K′ = C(y5). Then clearly
[L :K′] = 5 and [K′ :K] = 2, therefore [L :K] = 10.
Thus, to prove that L/K is Galois it is enough to ﬁnd 10 ﬁeld automor-
phisms of L over K. Choose a primitive 5th root of 1, say ζ = e2πi/5. For
i∈ Z/5 and s∈{± 1}, the C-algebra automorphism σi,s of L deﬁned by
y↦→ζiys
leavesx, hence K, ﬁxed.
There can be many ways to determine the group, here’s one.
Looking at the law of composition of these automorphisms, one sees that
the subgroup Gal(L/K′)≃ Z/5, (which is necessarily normal, being of index
2) is not central, for conjugation by σ0,−1 acts as−1 on it.
So the group is the dihedral group of 10 elements.
2. (Algebraic Geometry) Is every smooth projective curve of genus
0 deﬁned over the ﬁeld of complex numbers isomorphic to a conic in the
projective plane? Give an explanation for your answer.
Solution (Sketch). Yes. Apply the Riemann-Roch theorem which guar-
antees the existence of a nonconstant meromorphic function with a simple
pole at exactly one point. Argue that this meromorphic function identiﬁes
the curve with P1, and using that fact, embed the curve as a conic in the
plane in any convenient way, e.g., If t0,t 1 are projective ( P1) coordinates,
let z0 = t2
0, z1 = t0t1 z2 = t2
1 be the map to P2. The conic, then, would
be z0z2 = z2
1. (Alternatively: one can consider the complete linear system
attached to the anticanonical divisor.)
15

3. (Complex Analysis) Letf(z) =z +e−z forz∈ C and letλ∈ R,λ> 1.
Prove or disprove the statement that f(z) takes the value λ exactly once in
the open right half-plane Hr ={z∈ C : Re z >0}.
Solution. First, let us consider the real function f(x) = x +e−x. Since f
is continuous, f(0) = 1 and lim x→∞f(x) = ∞, by the intermediate value
theorem, there exists u∈ R such that f(u) = λ. Now let us show that such
u is unique. Let R >2λ and let Γ be the closed right half disk of radius R
centered at the origin
{z =x +iy∈ C : x = 0,|y|≤ R}∪
{
z∈ C :|z| =R,−π
2≤ arg(z)≤ π
2
}
.
Let F (z) = λ−z and G(z) = −e−z. Then for z ∈ Γ, we have |G(z)| =
|e−Rez|≤ 1 since Re z≥ 0, while|F (z)| > 1 by construction. Hence by
Rouch´ e’s theorem,λ−f(z) = F (z) +G(z) has the same number of zeros
inside Γ as F (z), namely 1. Since this is true for all R large enough, we
conclude that the point u is unique.
4. (Algebraic Topology) (a) Let X and Y be locally contractible, con-
nected spaces with ﬁxed basepoints. Let X∨Y be the wedge sum at the
basepoints. Show that π1(X∨Y ) is the free product of π1X with π1Y .
(b) Show that π1(X×Y ) is the direct product of π1X with π1Y .
(c) Note the canonical inclusion f : X∨Y → X×Y . Assume that X and
Y have abelian fundamental groups. Show that the map f∗ on fundamental
groups exhibits π1(X×Y ) as the abelianization of π1(X∨Y ).
Hint: The Hurewicz map is natural.
Solution. (a) This follows form the Van Kampen theorem: Writing X∨Y
as the union
X∪∗Y
we have that π1(X∨Y )∼=π1(X)∗π1(∗)π1(Y ) =π1(X)∗π1Y .
(b) There is the obvious continuous map
Maps∗(S1,X )×Maps∗(S1,Y )→Maps∗(S1,X×Y )
given by sending (t↦→ γX(t),t ↦→ γY (t))↦→ (t↦→ (γX(t),γY (t))). This map
is a continuous so it induces a map
π0(Maps∗(S1,X )×Maps∗(S1,Y ))→π0Maps∗(S1,X×Y )
16

where the lefthand side is isomorphic toπ0Maps∗(S1,X )×π0Maps∗(S1,Y )).
Further, the above map is clearly a bijection, so it induces an injection and
a surjection on π0.
(c) The Hurewicz map is natural so we have a commutative diagram
π1(X∨Y )
f∗ //
q

π1(X×Y )

H1(X∨Y )
f∗ //H1(X×Y )
where the vertical maps are abelianizations by the Hurewicz theorem. But
the lower-right corner is equal to H1(X)×H1(Y ) by the Kunneth theorem
(since X and Y are connected), and the bottom copy of f∗ is the obvious
isomorphism onH1. Since q is an abelianization by deﬁnition, but the bottom
arrow and rightmost arrow are both isomorphisms, the top arrow must also
be an abelianization.
5. (Differential Geometry) (a) Let S1 = R/Z be a circle and consider
the connection
∇ := d +π
√
−1dθ
deﬁned on the trivial complex line bundle overS1, whereθ is the standard co-
ordinate on S1 = R/Z descended from R. By solving the diﬀerential equation
for ﬂat sections f(θ)
∇f = df +π
√
−1fdθ = 0
or otherwise, show that there does not exist global ﬂat sections with respect
to∇ over S1.
(b) Let T =V/Λ be a torus, where Λ is a lattice and V = Λ⊗ R is the real
vector space containing Λ. Let L be the trivial complex line bundle equipped
with the standard Hermitian metric. By identifying ﬂat U(1) connections
withU(1) representations of the fundamental groupπ1(T ) or otherwise, show
that the space of ﬂat unitary connections onL is the dual torusT∗ =V∗/Λ∗,
where Λ∗ := Hom(Λ, Z) is the dual lattice and V∗ := Hom(V, R) is the dual
vector space.
17

Solution. (a) The diﬀerential equation
f′(θ) +π
√
−1f(θ) = 0
has a unique solution
f(θ) =Ae−π√−1θ
up to a constant A∈ C. This is not a well-deﬁned function over S1 because
f(0)⁄=f(1).
(b) The space of ﬂat G-connections over T can be identiﬁed as
Hom(π1(T ),G )/AdG.
Since π1(T ) = Λ and for the abelian group G = U(1) the adjoint action is
trivial, we have
Hom(π1(T ),G )/AdG = Hom(Λ,U (1)) =T∗.
6. (Real Analysis) (Fundamental Solutions of Linear Partial Diﬀerential
Equations with Constant Coeﬃcients). Let Ω be an open interval (−M,M ) in
R with M >0. Let n be a positive integer and L =∑n
ν=0aν
dν
dxν be a linear
diﬀerential operator of order n on R with constant coeﬃcients, where the
coeﬃcientsa0,··· ,an−1,an⁄= 0 are complex numbers andx is the coordinate
of R. Let L∗ = ∑n
ν=0(−1)νaν
dν
dxν . Prove, by using Plancherel’s identity,
that there exists a constant c >0 which depends only on M and an and is
independent of a0,a 1,··· ,an−1 such that for any f∈L2(Ω) a weak solution
u of Lu = f exists with‖u‖L2(Ω)≤ c‖f‖L2(Ω). Give one explicit expression
for c as a function of M and an.
Hint: A weak solutionu ofLu =f means that (f,ψ )L2(Ω) = (u,L∗ψ)L2(Ω) for
every inﬁnitely diﬀerentiable functionψ on Ω with compact support. For the
solution of this problem you can consider as known and given the following
three statements.
(I) If there exists a positive numberc> 0 such that‖ψ‖L2(Ω)≤c‖L∗ψ‖L2(Ω)
for all inﬁnitely diﬀerentiable complex-valued functions ψ on Ω with
compact support, then for any f∈L2(Ω) a weak solution u ofLu =f
exists with‖u‖L2(Ω)≤c‖f‖L2(Ω).
18

(II) Let P (z) = zm +∑m−1
k=0 bkzk be a polynomial with leading coeﬃcient
1. If F is a holomorphic function on C, then
|F (0)|2≤ 1
2π
∫ 2π
θ=0
⏐⏐P
(
eiθ)
F
(
eiθ)⏐⏐2
dθ.
(III) For an L2 function f on R which is zero outside Ω = ( −M,M ) its
Fourier transform
ˆf(ξ) =
∫ M
−M
f(x)e−2πixξdx
as a function of ξ∈ R can be extended to a holomorphic function
ˆf (ξ +iη) =
∫ M
−M
f(x)e−2πix(ξ+iη)dx
on C as a function of ξ +iη.
Solution. This problem is to compute the constant c in Lemma 3.3 on
p.225 of the book of Stein and Shakarchi on Real Analysis by going over its
arguments and keeping track of the constants involved in each step.
Introduce the polynomial
Q(ζ) =
n∑
k=0
(−1)kak (2πζ)k
so that
(#)
(
ˆL∗ψ
)
(ζ) =Q(ζ) ˆψ(ζ)
any ψ∈C ∞
0 (R), where ˆ denotes taking the Fourier transform. Consider
ﬁrst the special case where an = 1
(2πi)n so that the coeﬃcient of ξn in the
polynomial Q(ζ) of degree n in ζ is 1. Writing ζ =ξ +√−1η (with both ξ
and η real) and taking the L2 of both sides of (#) over R as functions of η.
Then
(♭)
∫ ∞
−∞
⏐⏐⏐Q (ξ +iη) ˆψ (ξ +iη)
⏐⏐⏐
2
dξ =
∫ ∞
−∞
⏐⏐⏐
(
ˆL∗ψ
)
(ξ +iη)
⏐⏐⏐
2
dξ.
Since from the deﬁnition of Fourier transform
(
ˆL∗ψ
)
(ξ +iη) =
∫ ∞
x=−∞
(L∗ψ) (x)e−2πi(ξ+iη)xdx =
∫ ∞
x=−∞
(
(L∗ψ) (x)e2πηx)
e−2πiξxdx,
19

it follows that
(
ˆL∗ψ
)
(ξ +iη) is equal to the value at ξ of the Fourier trans-
form of the function (L∗ψ) (x)e2πηx. Thus, by applying Plancherel’s identity
to the function (L∗ψ) (x)e2πηx, we get
∫ ∞
ξ=−∞
⏐⏐⏐
(
ˆL∗ψ
)
(ξ +iη)
⏐⏐⏐
2
dξ
=
∫ ∞
x=−∞
⏐⏐(L∗ψ) (x)e2πηx⏐⏐2
dx≤e4π|η|M
∫ ∞
−∞
|(L∗ψ) (x)|2dx,
because the support of ψ(x) (as well as the support of ( L∗ψ) (x)) is in the
interval Ω = (−M,M ). Thus from (♭) it follows that
(♯)
∫ ∞
−∞
⏐⏐⏐Q (ξ +iη) ˆψ (ξ +iη)
⏐⏐⏐
2
dξ≤e4π|η|M
∫ ∞
−∞
|(L∗ψ) (x)|2dx.
Setting η = sinθ in (♯), we get from|η|≤ 1 that
(†)
∫ ∞
−∞
⏐⏐⏐Q (ξ +i sinθ) ˆψ (ξ +i sinθ)
⏐⏐⏐
2
dξ≤e4πM
∫ ∞
−∞
|(L∗ψ) (x)|2dx.
Replacingξ byξ + cosθ in the integrand on the left-hand side of (†), we get
(‡)
∫ ∞
−∞
⏐⏐⏐Q (ξ + cosθ +i sinθ) ˆψ (ξ + cosθ +i sinθ)
⏐⏐⏐
2
dξ
≤e4πM
∫ ∞
−∞
|(L∗ψ) (x)|2dx.
By Statement (III) given above the functionˆψ (ξ +iη) as a function ofξ+iη∈
C is holomorphic on C. Since Q (ξ +iη) as a function of ξ +iη∈ C is a
polynomial of degree n with leading coeﬃcient 1, it follows from Statement
(II) applied to F (z) = ˆψ(ξ +z) and P (z) =Q(ξ +z) that
⏐⏐⏐ ˆψ (ξ)
⏐⏐⏐
2
≤ 1
2π
∫ 2π
θ=0
⏐⏐⏐Q (ξ + cosθ +i sinθ) ˆψ (ξ + cosθ +i sinθ)
⏐⏐⏐
2
dθ.
Integrating both sides over ξ∈ (−∞,∞) and using (‡), we get
∫ ∞
ξ=−∞
⏐⏐⏐ ˆψ (ξ)
⏐⏐⏐
2
≤
∫ ∞
ξ=−∞
( 1
2π
∫ 2π
θ=0
⏐⏐⏐Q (ξ + cosθ +i sinθ) ˆψ (ξ + cosθ +i sinθ)
⏐⏐⏐
2
dθ
)
dξ
= 1
2π
∫ 2π
θ=0
(∫ ∞
ξ=−∞
⏐⏐⏐Q (ξ + cosθ +i sinθ) ˆψ (ξ + cosθ +i sinθ)
⏐⏐⏐
2
dξ
)
dθ
≤ 1
2π
∫ 2π
θ=0
(
e4πM
∫ ∞
−∞
|(L∗ψ) (x)|2dx
)
dθ =e4πM
∫ ∞
−∞
|(L∗ψ) (x)|2dx.
20

By applying Plancherel’s formula to ψ, we conclude that
‖ψ (ξ)‖2
L2(Ω)≤e4πM‖(L∗ψ) (x)‖2
L2(Ω)
under the additional assumption that an = 1
(2πi)n . When this additional
assumption is not satisﬁed, we can apply the argument for the special case
to 1
an (2πi)nL
instead of to L to conclude that
‖ψ (ξ)‖2
L2(Ω)≤ e4πM
|an (2π)n|2‖(L∗ψ) (x)‖2
L2(Ω),
or
‖ψ (ξ)‖L2(Ω)≤c‖(L∗ψ) (x)‖L2(Ω),
with
c = e2πM
|an| (2π)n.
By Statement (I) given above, when we set
c = e2πM
|an| (2π)n,
we can conclude that for any f∈L2(Ω) a weak solution u of Lu =f exists
with‖u‖L2(Ω)≤c‖f‖L2(Ω).
21

