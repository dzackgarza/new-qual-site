Advanced Complex Analysis
Course Notes — Harvard University — Math 213a
C. McMullen
December 4, 2017
Contents
1 Basic complex analysis . . . . . . . . . . . . . . . . . . . . . . 2
2 The simply-connected Riemann surfaces . . . . . . . . . . . . 39
3 Entire and meromorphic functions . . . . . . . . . . . . . . . 59
4 Conformal mapping . . . . . . . . . . . . . . . . . . . . . . . 81
5 Elliptic functions and elliptic curves . . . . . . . . . . . . . . 108

Forward
Complex analysis is a nexus for many mathematical ﬁelds, including:
1. Algebra (theory of ﬁelds and equations);
2. Algebraic geometry and complex manifolds;
3. Geometry (Platonic solids; ﬂat tori; hyperbolic manifolds of dimen-
sions two and three);
4. Lie groups, discrete subgroups and homogeneous spaces (e.g. H/ SL2(Z);
5. Dynamics (iterated rational maps);
6. Number theory and automorphic forms (elliptic functions, zeta func-
tions);
7. Theory of Riemann surfaces (Teichm¨ uller theory, curves and their Ja-
cobians);
8. Several complex variables and complex manifolds;
9. Real analysis and PDE (harmonic functions, elliptic equations and
distributions).
This course covers some basic material on both the geometric and analytic
aspects of complex analysis in one variable.
Prerequisites: Background in real analysis and basic diﬀerential topology
(such as covering spaces and diﬀerential forms), and a ﬁrst course in complex
analysis.
Exercises
(These exercises are review.)
1. Let T⊂ R3 be the spherical triangle deﬁned by x2 +y2 +z2 = 1 and
x,y,z ≥ 0. Let α =zdxdz .
(a) Find a smooth 1-form β on R3 such that α =dβ.
(b) Deﬁne consistent orientations for T and ∂T .
(c) Using your choices in (ii), compute
∫
Tα and
∫
∂T β directly, and
check that they agree. (Why should they agree?)
1

2. Let f(z) = (az +b)/(cz +d) be a M¨ obius transformation. Show the
number of rational maps g :ˆC→ˆC such that
g(g(g(g(g(z))))) =f(z)
is 1, 5 or ∞. Explain how to determine which alternative holds for a
givenf.
3. Let ∑anzn be the Taylor series for tanh(z) at z = 0.
(a) What is the radius of convergence of this power series?
(b) Show that a5 = 2/15.
(c) Give an explicit value of N such that tanh(1) and ∑N
0 an agree
to 1000 decimal places. Justify your answer.
4. Let f : U→ V be a proper local homeomorphism between a pair of
open sets U,V ⊂ C. Prove that f is a covering map. (Here proper
means that f−1(K) is compact whenever K⊂V is compact.)
5. Let f : C→ C be given by a polynomial of degree 2 or more. Let
V1 ={f(z) : f′(z) = 0}⊂ C
be the set of critical values of f, let V0 =f−1(V1), and let Ui = C−Vi
for i = 0, 1. Prove that f :U0→U1 is a covering map.
6. Give an example where U0/U1 is a normal (or Galois) covering, i.e.
where f∗(π1(U0)) is a normal subgroup of π1(U1).
1 Basic complex analysis
We begin with an overview of basic facts about the complex plane and
analytic functions.
Some notation. The complex numbers will be denoted C. We let ∆ , H
and ˆC denote the unit disk|z|< 1, the upper half plane Im(z)> 0, and the
Riemann sphere C∪{∞} . We write S1(r) for the circle |z| =r, and S1 for
the unit circle, each oriented counter-clockwise. We also set ∆ ∗ = ∆−{ 0}
and C∗ = C−{ 0}.
2

1.1 Algebraic and analytic functions
The complex numbers are formally deﬁned as the ﬁeld C = R[i], where
i2 =−1. They are represented in the Euclidean plane byz = (x,y ) =x+iy.
There are two square-roots of−1 in C; the numberi is the one with positive
imaginary part.
An important role is played by the Galois involution z↦→z. We deﬁne
|z|2 = N(z) = zz = x2 +y2. (Compare the case of a real quadratic ﬁeld,
whereN(a +b
√
d) =a2−db2 gives an indeﬁnite form.) Compatibility of|z|
with the Euclidean metric justiﬁes the identiﬁcation of C and R2. We also
see that z is a ﬁeld: 1/z =z/|z|.
It is also convenient to describe complex numbers by polar coordinates
z = [r,θ ] =r(cosθ +i sinθ).
Herer =|z| andθ = argz∈ R/2πZ. (The multivaluedness of arg z requires
care but is also the ultimate source of powerful results such as Cauchy’s
integral formula.) We then have
[r1,θ 1][r2,θ 2] = [r1r2,θ 1 +θ2].
In particular, the linear maps f(z) = az +b, a⁄= 0, of C to itself, preserve
angles and orientations.
This formula should be proved geometrically: in fact, it is a consequence
of the formula |ab| =|a||b| and properties of similar triangles. It can then
be used to derive the addition formulas for sine and cosine (in Ahﬂors the
reverse logic is applied).
Algebraic closure. A critical feature of the complex numbers is that
they are algebraically closed; every polynomial has a root. (A proof will be
reviewed below).
Classically, the complex numbers were introducing in the course of solv-
ing real cubic equations. Staring with x3 +ax +b = 0 one can make a
Tschirnhaus transformation so a = 0. This is done by introducing a new
variabley =cx2 +d such that∑yi =∑y2
i = 0; even whena andb are real,
it may be necessary to choose c complex (the discriminant of the equation
for c is 27b2 + 4a3.) It is negative when the cubic has only one real root;
this can be checked by looking at the product of the values of the cubic at
its max and min.
Analytic functions. LetU be an open set in C andf :U→ C a function.
We sayf is analytic if
f′(z) = lim
t→0
f(z +t)−f(z)
t
3

exists for allz∈U. It is crucial here thatt approaches zero through arbitrary
values in C. Remarkably, this condition implies that f is a smooth ( C∞)
function. For example, polynomials are analytic, as are rational functions
away from their poles.
Note that any real linearfunctionφ : C→ C has the formφ(v) =av+bv.
The condition of analytic says that Dfz(v) = f′(z)v; in other words, the v
part is absent.
To make this point systematically, for a general C1 function F :U→ C
we deﬁne
dF
dz = 1
2
(dF
dx + 1
i
dF
dy
)
and dF
dz = 1
2
(dF
dx− 1
i
dF
dy
)
·
We then have
DFz(v) = dF
dzv + DF
dz v.
We can also write complex-valued 1-form dF as
dF =∂F +∂F = dF
dz dz + dF
dz dz
ThusF is analytic iﬀ ∂F = 0; these are the Cauchy-Riemann equations.
We note that (d/dz)zn =nzn−1; a polynomial p(z,z) behaves as if these
variables are independent.
Sources of analytic functions.
1. Polynomials and rational functions. Using addition and multipli-
cation we obtain naturally the polynomial functions f(z) =∑n
0anzn :
C→ C. The ring of polynomials C[z] is an integral domain and a
unique factorization domain, since C is a ﬁeld. Indeed, since C is
algebraically closed, fact every polynomial factors into linear terms.
It is useful to add the allowed value ∞ to obtain the Riemann sphere
ˆC = C∪{∞} . Then rational functions (ratios f(z) =p(z)/q(z) of rel-
atively prime polynomials, with the denominator not identically zero)
determine rational maps f : C→ C. The rational functions C(z) are
the same as the ﬁeld of fractions for the domainC[z]. We setf(z) =∞
if q(z) = 0; these points are called the poles of f.
2. Algebraic functions. Beyond the rational and polynomial functions,
the analytic functions include algebraic functions such that f(z) =√
z2 + 1. A general algebraic functionf(z) satisﬁesP (f) =∑N
0 an(z)f(z)n =
0 for some rational functionsan(z); these arise, at least formally, when
4

one forms algebraic extension of C(z). Such functions are generally
multivalued, so we must choose a particular branch to obtain an ana-
lytic function.
3. Diﬀerential equations. Analytic functions also arise when one solves
diﬀerential equations. Even equations with constant coeﬃcients, like
y′′ +y = 0, can give rise to transcendental functions such as sin( z),
cos(z) andez. Here are some useful facts about these familiar functions
when extended to C:
| exp(z)| = exp Re z
cos(iz) = cosh( z)
sin(iz) = i sinh(z)
cos(x +iy) = cos( x) cosh(y)−i sin(x) sinh(y)
sin(x +iy) = sin( x) cosh(y) +i cos(x) sinh(y).
In particular, the apparent boundedness of sin(z) and cos(z) fails badly
as we move away from the real axis, while |ez| is actually very small
in the halfplane Re z≪ 0.
4. Integration. A special case of course is integration. While
∫
(x2+ax+
b)−1/2dx can be given explicitly in terms of trigonometric functions,
already
∫
(x3 +ax +b)−1/2dx leads one into elliptic functions; and
higher degree polynomials lead one to hyperelliptic surfaces of higher
genus. Note that the ‘periodicity’ of the function in increases from Z
(trigonometric) to Z2 (elliptic) to H1(Σg, Z) (hyperelliptic).
5. Power series. Analytic functions can be given concretely, locally, by
power series such as ∑anzn. Conversely, suitable coeﬃcients deter-
mine analytic functions; for example, ez =∑zn/n!.
For a more interesting example one can consider the partition function
p(n) (satisfyingp(5) = 6 because 5 = 1+1+1+1+1 = 1+1+1+2 =
1 + 1 + 2 + 2 = 1 + 4 = 5), whose generating function satsiﬁes
∞∑
0
p(n)zn =
∞∏
1
(1−zn)−1,
for z∈ ∆. We remark that ∏(1 +an) converges if ∑|an| converges.
6. Riemann surfaces and automorphy. Another natural source of complex
analytic functions is functions that satisfy invariant properties such as
5

f(z +λ) =f(z) for all λ∈ Λ, a lattice in C; or f(g(z)) =f(z) for all
g∈ Γ⊂ Aut(H).
The elliptic modular functions f : H→ C with have the property that
f(z) =f(z + 1) =f(−1/z), and hence f((az +b)/(cz +d)) =f(z) for
all
(a b
c d
)
∈ SL2(Z).
7. Geometric function theory. A complex analytic function can be
speciﬁed by a domain U⊂ C; we will see that for simply-connected
domains (other than C itself), there is an essentially unique analytic
homeomorphism f : ∆→U. When U tiles H or C, this is related to
automorphic functions; and when ∂U consists of lines or circular arcs,
one can also give a diﬀerential equation for f.
8. Limits. We can also deﬁne analytic functions by taking limits of poly-
nomials or other known functions. For example, consider the formula:
ez = lim(1 +z/n)n.
The triangle with vertices 0, 1 and 1 +iθ/n has a hypotenuse of length
1 +O(1/n2) and an angle at 0 of θ +O(1/n2). Thus one ﬁnds geo-
metrically that zn = (1 +iθ/n)n satisﬁes|zn|→ 1 and arg zn→θ; in
other words,
eiθ = cosθ +i sinθ.
In particular, eπi =−1 (Euler).
1.2 Complex integration and power series
We now return to the general theory of analytic functions. Let U be a
compact, connected, smoothly bounded region in C, and let f :U→ C be a
continuous function such that f :U→ C is analytic. We then have:
Theorem 1.1 (Cauchy) For any analytic function f : U → C, we have∫
∂U f(z)dz = 0.
Remark. It is critical to know the deﬁnition of such a path integral.
(For example, f(z) = 1 is analytic, its average over the circle is 1, and
yet
∫
S1 1dz = 0; why is this?)
If γ : [a,b ]→ C parameterizes an arc, then we deﬁne
∫
γ
f(z)dz =
∫ b
a
f(γ(t))γ′(t)dt.
6

Alternatively, we choose a sequence of points z1,...,z n close together along
γ, and then deﬁne
∫
γ
f(z) = lim
n−1∑
1
f(zi)(zi+1−zi).
(If the loop is closed, we choose zn =z1).
This should not be confused with the integral with respect to arclength:
∫
γ
f(z)|dz| = lim
∑
f(zi)|zi+1−zi|.
Note that the former depends on a choice of orientation ofγ, while the latter
does not.
Proof of Cauchy’s formula: (i) observe that d(fdz ) = (∂f )dzdz = 0
and apply Stokes’ theorem. (ii — Goursat). Cut the region U into small
squares, observe that on these squares f(z)≈az +b, and use the fact that∫
∂U (az +b)dz = 0.
Aside: distributions. The ﬁrst proof implicitly assumes f is C1, while
the second does not. (To see where C1 is used, suppose α = udx +vdy
and dα = 0 on a square S. In the proof that
∫
∂Sα = 0, we integrate vdy
over the vertical sides of S and observe that this is the same as integrating
dv/dxdxdy over the square. But if α is not C1, we don’t know that dv/dx
is integrable.)
More generally, we say a distribution (e.g. an L1 functionf) is (weakly)
analytic if
∫
f∂φ = 0 for every φ∈C∞
c (U). By convolution with a smooth
function (a molliﬁer), any weakly analytic function is a limit ofC∞ analytic
functions. We will see below that uniform limits of C∞ analytic functions
are C∞, so even weakly analytic functions are actually smooth.
An important and standard computation in diﬀerential forms shows that,
for f∈C∞
0 (C), we have
∫
C
(∂f )∧ dz
z ≈
∫
C−∆(epsilon)
d(f(z)dz/z) =−
∫
S1(ϵ)
f(z)
z dz≈− 2πif (0),
and hence ∂(dz/z) = 2πiδ0, as a current.
More on the Cauchy–Riemann equations and with minimal smoothness
assumptions can be found in [GM].
Cauchy’s integral formula: Diﬀerentiability and power series.Because
of Cauchy’s theorem, only one integral has to be explicitly evaluated in
7

complex analysis (hence the forgetability of the deﬁnition of the integral).
Namely, settingγ(t) =eit we ﬁnd, for any r> 0,
∫
S1(r)
1
zdz = 2πi.
By integrating between ∂U and a small loop around p∈U, we then obtain
Cauchy’s integral formula:
Theorem 1.2 For any p∈U we have
f(p) = 1
2πi
∫
∂U
f(z)dz
z−p ·
Now the integrand depends on p only through the rational function
1/(z−p), which is inﬁnitely diﬀerentiable. (It is the convolution of f|∂U
and 1/z.) So we conclude that f(p) itself is inﬁnitely diﬀerentiable, indeed,
it is approximated by a sum of rational functions with poles on ∂U . In
particular, diﬀerentiating under the integral, we obtain:
f (k)(p)
k! = 1
2πi
∫
∂U
f(z)dz
(z−p)k+1· (1.1)
If d(p,∂U ) = R, the length of ∂U is L and sup∂U|f| = M, then this gives
the bound:
|ak| =
⏐⏐⏐⏐⏐
f (k)(p)
k!
⏐⏐⏐⏐⏐≤ ML
2πRk+1·
In particular, ∑ak(z− p)k has radius of convergence at least R, since
lim sup|ak|1/k < 1/R. This suggests that f is represented by its power
series, and indeed this is the case:
Theorem 1.3 Iff is analytic on B(p,R ), then f(z) =∑ak(z−p)k on this
ball.
Proof. We can reduce to the case z∈B(0, 1). Then for w∈S1 and ﬁxed
z with|z|< 1, we have
1
w−z = 1
w
(
1 + (z/w) + (z/w)2 +···
)
,
converging uniformly on the circle |w| = 1. We then have:
f(z) = 1
2πi
∫
S1
f(w)dw
w−z =
∑
zk 1
2πi
∫
S1
f(w)dw
wk+1 =
∑
akzk
as desired.
8

Corollary 1.4 An analytic function has at least one singularity on its circle
of convergence.
That is, if f can be extended analytically from B(p,R ) toB(p,R′), then
the radius of convergence is at least R′. So there must be some obstruction
to making such an extension, if 1/R = lim sup|ak|1/k.
Example: Fibonacci numbers. Letf(z) =∑anzn, where an is the nth
Fibonacci number. We have ( a0,a 1,a 2,a 3,... ) = (1, 1, 2, 3, 5, 8,... ). Since
an =an−1 +an−2, except for n = 0, we get
f(z) = (z +z2)f(z) + 1
and so f(z) = 1/(1−z−z2). This has a singularity at z = 1/γ and thus
lim sup|an|1/n = γ, where γ = (1 +
√
5)/2 = 1.618... is the golden ratio
(slightly more than the number of kilometers in a mile).
Note that∑(an−αγn)zn =f(z)−α/(1−γz) has radius of convergence
|γ| > 1, if we choose the constant α to cancel the pole of f(z) at z = 1/γ.
Thus|an−αγn|→ 0. (In fact α =γ/
√
5.)
Theorem 1.5 A power series represents a rational function iﬀ its coeﬃ-
cients satisfy a recurrence relation.
Aside: Pisot numbers. The golden ratio is an example of a Pisot number;
as we have just seen, it has the property that d(γn, Z)→ 0 as n→∞ . It is
an unsolved problem to show that if α> 1 satisﬁes d(αn, Z)→ 0, then α is
an algebraic number.
Kronecker’s theorem asserts that ∑aizi is a rational function iﬀ deter-
minants of the matrices ai,i+j, 0 ≤ i,j ≤ n are zero for all n suﬃciently
large [Sa,§I.3]
Question: why are 10:09 and 8:18 such pleasant times? [Mon].
How to computeπ. The power series for the arctangent is easy to evaluate
by relating it to
∫
dx/(1 +x2). Thus we get:
f(z) = tan−1(z) =z−z3/3 +z5/5 +z7/7 +···
which suggest correctly that
π
4 = 1− 1
3 + 1
5− 1
7 +···
However the convergence is very slow, since the error aftern terms is on the
order of 1/n.
9

In general, to accelerate the convergence of the sumssn =sn(0) =∑n
0ai,
we can set sn(1) = ( sn +sn+1)/2 and take its limit instead. This will
be especially eﬃcacious for an alternating series. But why not repeat the
process again and again? To this end we deﬁne inductively:
sn(k + 1) = sn(k) +sn+1(k)
2 ·
If we have the terms (a0,...,a n) at our disposal, we can then compute
en =s0(n) = 2−n
n∑
0
(n
k
)
sn.
Forf(z) =∑akzk as above, we ﬁnd that
4
100∑
0
ak = 3.121... but 4
100∑
0
2−100
(100
k
)
ak = 3.141592653589793273...,
which agrees with π to 16 decimal places (!)
The reason this works is that if we write F (y) =f(y/(1−y)) =∑bkyk,
thenen =∑n
0bk(1/2)k. Assuming f is analytic in the unit disk,F is analytic
in the halfplane Re(y)≤ 1/2. But if f(z) is analytic in a neighborhood of
z = 1, thenF (y) is analytic inB(0,r ) for somer> 1/2, and hence its power
series converges geometrically fast at y = 1/2.
In the case at hand, f(z) has singularities at z =±i (and nowhere else).
Then F (z) has singularities at ±i/(1 +i), so its radius of convergence is
1/
√
2 which is bigger than 1/2. In fact we expect the error to be roughly of
size 2−n/2 after taking n terms, and 2−50 = 9× 10−16, consistent with the
results above.
To justify this explanation, we must show that
en =
n∑
0
bk2−k. (1.2)
To this end, ﬁrst note that:
1
(1−y)n+1 =
∞∑
0
(n +k
k
)
yk.
This can be seen by either diﬀerentiating both sides, starting with n = 0,
or by observing that the coeﬃcient of yk is the number of ways of writing
10

k = m1 +··· mn with mi≥ 0. Plugging into f(y/(1−y)), we ﬁnd that
b0 =a0 and
bn+1 =
n∑
0
(n
k
)
ak+1.
We can now show (1.2) by induction. We have e0 =b0 =a0, and
en+1−en = s1(n)−s0(n)
2 = 2−(n+1)
n∑
0
(n
k
)
(sk+1−sk)
= 2 −(n+1)
n∑
0
(n
k
)
ak+1 =bn+12−(n+1),
which implies (1.2).
We remark thaten is the expected value of aI(n), where I(n) is the sum
of n independent random variables, each taking on the values 0 or 1 with
probability 1/2. For more on this and other summation methods, see [Har,
§VIII].
Isolation of zeros. If f(z) = ∑an(z− p)n vanishes at p but is not
identically zero, then we can factor out the leading term and write:
f(z) = (z−p)n(an +an+1(z−p) +··· ) = (z−p)ng(z)
where g is analytic and g(p)⁄= 0. This is the simplest case of the Weier-
strass preparation theorem: it shows germs of analytic functions behave like
polynomials times units (invertible functions).
In particular, we ﬁnd:
Theorem 1.6 The zeros of a nonconstant analytic function are isolated.
Warning: we are assuming the domain is connected!
Proof. LetU0⊂U be the largest open set withf|U0 = 0. Let U1 =U−U0.
Then by the factorization theorem above, the zeros of f in U1 are isolated.
ThusU1 is open as well. So either U =U0 — in which case f is constant —
or U =U1 — in which case f has isolated zeros.
Corollary 1.7 An analytic function which is constant along an arc, or even
on a countable set with an accumulation point, is itself constant.
Corollary 1.8 The extension of a function f(x) on [a,b ]⊂ R to an analytic
function f(z) on a connected domain U⊃ [a,b ] is unique — if it exists.
11

1.3 Sequences of analytic functions
In this section we develop the maximum princple and related to ideas that
lead to compactness of spaces of analytic functions.
Mean value and maximum principle. On the circle |z| = r, with
z =reiθ, we have dz/z =idθ . Thus Cauchy’s formula gives
f(0) = 1
2πi
∫
S1(r)
f(z)dz
z = 1
2π
∫
S1(r)
f(z)dθ.
In other words, analytic functions satisfy:
Theorem 1.9 (The mean-value formula) The value of f(p) is the av-
erage of f(z) over S1(p,r ).
Corollary 1.10 (The Maximum Principle) A nonconstant analytic func-
tion does not achieve its maximum in U.
Proof. Suppose f(z) achieves its maximum at p∈ U. Then f(p) is the
average off(z) over a small circleS1(p,r ). Moreover,|f(z)|≤| f(p)| on this
circle. The only way the average can agree is if f(z) =f(p) onS1(p,r ). But
then f is constant on an arc, so it is constant in U.
Corollary 1.11 If U is compact, then supU|f| = sup∂U|f|.
Cauchy’s bound and algebraic completeness of C. Suppose f is
analytic onB(p,R ) and letM(R) = sup|z−p|=R|f(z)|; then Cauchy’s bound
(1.1) becomes:
|f (n)(p)|
n! ≤ M(R)
Rn .
On the other hand, if U = C — sof is an entire function — then the bound
above forcesM(R) to grow unless some derivative vanishes identically. Thus
we ﬁnd:
Theorem 1.12 A bounded entire function is a constant. More generally, if
M(R) =O(Rn), then f is a polynomial of degree at most n.
Corollary 1.13 Any polynomialf∈ C[z] of degree 1 or more has a zero in
C.
12

Otherwise 1/f(z) would be a nonconstant, bounded entire function. Al-
ternatively, 1/f(z)→∞ as|z|→∞ , so we obtain a violation of the maxi-
mum principle.
Corollary 1.14 There is no conformal homeomorphism between C and ∆.
(An analytic map with no critical points is said to be conformal, because
it preserves angles.)
The Picard theorem says an entire function can omit at most one value
in C. Here is an easy form (cf. Weierstrass–Casorati, to be proved later):
Theorem 1.15 Let f : C→ C be an entire function. Then the closure of
its image is either a single point, or C.
Proof. If p⁄∈f(C), then 1/(f(z)−p) is a bounded entire function, hence
constant.
Aside: quasiconformal maps. A diﬀeomorphism f : U → V between
domains in C is quasiconformal if supU|∂f/∂f|<∞. Many qualitative the-
orems for conformal maps also hold for quasiconformal maps. For example,
there is no quasiconformal homeomorphism between C and ∆.
Parseval’s theorem. The power series of an analytic function on the ball
B(0,R ) also contains information about its L2-norm on the circle |z| = R:
namely if f(z) =∑anzn, then we have:
∑
|an|2R2n = 1
2π
∫
|z|=R
|f(z)|2dθ.
This comes from the fact that the functions zn are orthogonal in L2(S1).
It also gives another important perspective on holomorphic functions: they
are the elements in L2(S1) with positive Fourier coeﬃcients, and hence give
a half–dimensional subspace of this inﬁnite–dimensional space.
Cauchy’s bound on a disk also implies that if f is small, then f′ is also
small, at least if we are not too near the edge of U.
Theorem 1.16 Letf(z) be analytic onU and bounded byM. Then|f′(z)|≤
M/d(z,∂U ).
Corollary 1.17 If fn are analytic functions and fn→ f uniformly, then
f′ exists and f′
n→f′ locally uniformly.
13

Corollary 1.18 A uniform limit of analytic functions is analytic.
Note: Many fallacies in real analysis become theorems in complex analysis.
Note that fn(z) =zn/n tends to zero uniformly on ∆, but f′
n(z) =zn−1
only tends to zero locally uniformly.
Corollary 1.19 Let fn be a sequence of functions on U with|fn|≤ M.
Then after passing to a subsequence, there is an analytic function g such
that fn→g locally uniformly on U.
Proof. For any compact set K⊂U, the restrictions fn|K are equicontinu-
ous. Apply the Arzela–Ascoli theorem.
1.4 Laurent series and singularities
In this section we aim to describe the behavior of analytic functions near an
isolated point where they may not be deﬁned.
Laurent series. Using again the basic series 1/(1−z) =∑zn and Cauchy’s
formula over the two boundary components of the annulus A(r,R ) ={z :
r< |z|<R}, we ﬁnd:
Theorem 1.20 If f(z) is analytic on A(r,R ), then in this region we have
f(z) =
∞∑
n=−∞
anzn.
The positive terms converge for |z| < R, and the negative terms converge
for|z|>r .
Corollary 1.21 An analytic function on the annulus r <|z| < R can be
expressed as the sum of a function analytic on |z| < R and a function
analytic on|z|>r .
This fact can be used to show that the sheaf cohomology groupH1(ˆC,O) =
0.
Isolated singularities. As a special case, iff is analytic onU−p, withp∈
U, then near p we have a Laurent series expansion f(z) =∑∞
−∞an(z−p)n.
We sayf has an isolated singularity at p.
We write ord(f,p ) = n if an⁄= 0 but ai = 0 for all i <0. The values
n =−∞ and +∞ are also allowed. We now have 3 possibilities:
14

1. Removable singularities. If n≥ 0, the apparent singularity at p is
removable andf has a zero of order n at p. If −∞<n< 0, we say f
has a pole of order−n at p. In either of these cases, we can write
f(z) = (z−p)ng(z),
where g(p)⁄= 0 and g(z) is analytic near p (soO(g,p ) = 0).
2. Poles. If ord(f,p )>−∞, then f has a ﬁnite Laurent series
f(z) = a−n
(z−p)n +··· + a−1
z−p +
∞∑
n=0
anzn
near p. The germs of functions at p with ﬁnite Laurent tails form
a local ﬁeld, with ord( f,p ) as its discrete valuation. (Compare Qp,
where vp(pna/b) =n.)
3. Essential singularities. If ord(f,p ) =−∞ we say f has an essential
singularity at p. (Example: f(z) = sin(−1/z) at z = 0.)
Bounded functions and essential singularities.
Theorem 1.22 Every isolated singularity of a bounded analytic function is
removable.
Proof. Suppose the singularity is at z = 0, and write f(z) as a Laurent
series∑anzn. Then for any r> 0 we have
Res(f, 0) =a−1 = 1
2πi
∫
S1(r)
f(z)dz.
But if|f|≤ M then this integral tends to zero as r→ 0, and hencea−1 = 0.
Similarly a−(n+1) = Res(znf(z), 0) = 0 for all n≥ 0. Thus the Laurent
power series gives an extension of f to an analytic function at z = 0.
Corollary 1.23 (Weierstrass-Casorati) If f(z) has an essential singu-
larity at p, then there exist zn→p such that f(zn) is dense in C.
Proof. Otherwise there is a neighborhoodU ofp such thatf(U−{p}) omits
some ball B(q,r ) in C. But then g(z) = 1/(f(z)−q) is bounded on U, and
hence analytic at p, with a zero of ﬁnite order. Then f(z) =q + 1/g(z) has
at worst a pole at p, not an essential singularity.
15

Aside: several complex variables. A functionf(z1,...,z n) is analytic if
it isC∞ anddf/dzi = 0 fori = 1,...,n . (There are several other equivalent
deﬁnitions).
Using the same type of argument and some basic facts from several
complex variables, it is easy to show that if V ⊂ U ⊂ Cn is an analytic
hypersurfaces, and f : U−V → C is a bounded analytic function, then f
extends to all of U.
More remarkably,every analytic function extends acrossV if codim(V )≥
2. For example, an isolated point is always a removable singularity in C2.
Let us prove a stronger version of this fact, to illustrate the new phenomena
that arise in several complex variables.
Theorem 1.24 (Hartogs) Letf(z,t ) be analytic on ∆2− ∆(r)2, with r<
1. Then f extends to an analytic function on ∆2.
Proof. Deﬁne F (z,t ) = (2πi)−1∫
S1f(ζ,t )/(z−ζ)dζ. Since the integrand
is holomorphic on as a function of ( z,t ), so is F . But F (z,t ) = f(z,t ) for
|t|>r , so it provides the desired extension.
1.5 The residue theorem, the argument principle, and deﬁ-
nite integrals
In this section we will discuss complex integrals for analytic functions f(z)
with isolated singularities: these are controlled by the residues off. We will
use the residue theorem to show that (nonconstant) analytic functions are
open maps, and to evaluate deﬁnite integrals.
The residue. A critical role is played by the residue of f(z) at p, deﬁned
by Res(f,p ) =a−1. It satisﬁes
∫
γ
f(z)dz = 2πi Res(f,p )
for any small loop encircling the point p in U. Thus the residue is intrin-
sically an invariant of the 1-form f(z)dz, not the function f(z). (If we
regard f(z)dz as a 1-form, then its residue is invariant under change of
coordinates.)
Theorem 1.25 (The residue theorem) Let f : U → C be a function
which is analytic apart from a ﬁnite set of isolated singularities. We then
have: ∫
∂U
f(z)dz = 2πi
∑
p∈U
Res(f,p ).
16

Calculating the residue. The simplest case of the reside arises when
f(z) = 1/g(z) and g(z) has a simple zero at z0. Then we have
Res(f,z 0) = lim
z→z0
z−z0
g(z)−g(z0) = 1
g′(z0)·
For example, for f(z) = 1/(xn + 1) we have
Res(f,ζ 2n) =ζ1−n
2n /n =−ζ2n/n.
Applications of the residue theorem. We will develop two applications
of the residue theorem: the argument principle, and the evaluation of deﬁnite
integrals.
The argument principle. The previous argument for algebraic complete-
ness of C is clever and nonconstructive. One way to make the proof more
transparent and constructive is to employ the argument principle.
We ﬁrst observe that if f has at worst a pole at p, then its logarithmic
derivative
d logf =f′(z)/f(z)dz
satisﬁes
Res(f′/f,p ) = ord(f,p ).
We thus obtain:
Theorem 1.26 (Argument principle) If f is analytic in U and f|∂U is
nowhere zero, then the number of zeros of f in U is given by
N(f,U ) =
∑
p∈U
ord(f,p ) = 1
2πi
∫
∂U
f′(z)dz
f(z) ·
Corollary 1.27 (Rouch´ e’s Theorem)If|f|>|g| along ∂U , then f and
f +g have the same number of zeros in U.
Proof. The continuous, integer-valued function N(f +tg,U ) is constant
for t∈ [0, 1].
Example. Considerp(z) =z5+14z+1. Then all its zeros are inside|z|< 2,
since|z|5 = 32> 29≥| 14z + 1| when|z| = 2; but only one inside|z|< 3/2,
since|z5 + 1|≤ 1 + (3/2)5 < 9<|14z| on|z| = 3/2. (Intuitively, the zeros
of p(z) are close to the zeros of z5 + 14z which are z = 0 and otherwise 4
points on|z| = 141/4≈ 1.93.
17

Corollary 1.28 Letp(z) =zd +a1zd−1 +... +ad, and suppose|ai|<R i/d.
Then p(z) has d zeros inside the disk |z|<R .
Proof. Writep(z) =f(z) +g(z) with f(z) =zd, and let U =B(0,R ); then
on ∂U , we have|f| =Rd and|g|<R d; now apply Rouch´ e’s Theorem.
Geometric picture. Suppose for simplicity that U is a disk, and p⁄∈
f(∂U ). The the number of solutions to f(z) =p in U, counted with multi-
plicity, is:
N(f(z)−p,U ) = 1
2πi
∫
∂U
d log(f(z)−p) = 1
2π
∫
∂U
d arg(f(z)−p)·
This is nothing more than the winding number of f(∂U ) around p.
Observe that N(f(z)−p,U ) is a locally constant function of p on C−
f(∂U ), zero on the noncompact component. This shows:
Theorem 1.29 Supposep∈U and f(p)⁄∈f(∂U ). Then f(U) contains the
component of C−f(∂U ) in which p lies.
Corollary 1.30 A nonconstant analytic function is an open mapping.
Proof. Suppose f(p) =q. Then p is an isolated zero of f(z)−q. Choose a
small ball U such thatf(z)⁄=q on∂U . Then f(U) contains the component
of C−f(∂U ) in which q lies.
The open mapping theorem gives an alternate proof of the maximum
principle and its strict version:
Corollary 1.31 If|f| achieves its maximum in U, then f is a constant.
Moreover, the geometric picture of the argument principle yields:
Theorem 1.32 For anyp∈ C−f(∂U ), the number of solutions to f(z) =p
in U is the same as the winding number of f(∂U ) aroundp.
Using isolation of zeros, we have:
Corollary 1.33 If f′(p)⁄= 0, then f is a local homeomorphism at p.
18

In fact for r suﬃciently small and q close to p, we have
f−1(q) = 1
2π
∫
B(p,r)
zf′(z)dz
f(z)−q·
This shows:
Corollary 1.34 The local inverse of f is analytic wherever it exists.
The Weierstrass preparation theorem. The same idea can be used
to analyze functions of two (or more) complex variables. First a deﬁnition:
we say f(z,t ) is analytic on C2 if it is analytic in each variable separately.
This implies that f is locally given by a convergent power series ∑aij(z−
z0)i(w−w0)j.
A function of one complex variable looks like a polynomial: f(z) =
zng(z). In particular, its zero set agrees with the zero set of a polynomial.
Similar statements hold in C2, but we must allow polynomials with analytic
coeﬃcients.
To be precise, suppose ft(z) = f(z,t ) is analytic near (0 , 0) on C2,
f0(0) = 0, but f0(z) is not identically zero.
Theorem 1.35 There exists analytic functions ai(t) on the unit disk, and
a nowhere vanishing analytic function ht(z), such that
ft(z) = (zn +a1(t)zn−1 +··· +an(t))ht(z)
for (z,t ) near (0, 0), and ai(0) = 0.
For the proof, use the fact that
∫
S1(ϵ)(zkf′
t(z)/ft(z))dz is analytic in t
and gives the sums of the powers of the zeros of ft near the origin.
Algebraicity. It can also be shown that if f(z,t ) = 0 has an isolated
singularity at (0, 0), then one can make an analytic change of coordinates so
thef(Z,T ) becomes a polynomial in (Z,T ). See [Ad] and references therein.
Aside: the smooth case. These results also hold for smooth mappings f
once one ﬁnds a way to count the number of solutions to f(z) =p correctly.
(Some may count negatively, and the zeros are only isolated for generic
values of p.)
Aside: Linking numbers and intersection multiplicities of curves
in C2. Counting the number of zeros of y = f(x) at x = 0 is the same
as counting the multiplicity of intersection between the curves y = 0 and
y =f(x) in C2, at (0, 0).
19

In general, to an analytic curveC deﬁned byF (x,y ) = 0 passing through
(0, 0)∈ C2, we can associate a knot by taking the intersection of C with the
boundary S3(r) of a small ball centered at the origin.
A pair of distinct, irreducible, curves C1 and C2 passing through (0, 0)
(say deﬁned by fi(x,y ) = 0, i = 1, 2), have a multiplicity of intersection
m(C1,C 2). This can be deﬁned geometrically by intersection with a small
sphereS3(r) in C2 centered at (0, 0). Then we get a pair of knots, and their
linking number is the same as this multiplicity.
Examples of links. It is often simpler the use S3 = ∂∆2 instead of
|x|2 +|y|2 = 1. Then S3 is the union of two solid tori, ∆×S1 and S1× ∆.
The axesx = 0 andy = 0 are the core curves of these tori; they have linking
number one. In fact the variety xy = 0 gives the Hopf link in S3.
The liney =x is a (1, 1) curve onS1×S1; more generally, for gcd(a,b ) =
1, ya =xb is an (a,b ) curve, parameterized by (x,y ) =eita,eitb). In partic-
ular, the cusp y2 =x3 meets S3 in a trefoil knot. It links x = 0 twice and
y = 0 three times.
The simplest case is y = 0 — the core core of the solid torus — and
y = xn — a (1 ,n )–torus knot. These have linking number 1. For more
details see [Mil1].
Problem. Show that the ﬁgure-eight knot cannot arise from an analytic
curve.
Functional factorization. Here is an alternate proof of the open mapping
theorem. It is clear that pn(z) =zn is an open map, even at the origin; and
(by the inverse function theorem) that an analytic function is open at any
point p where f′(p)⁄= 0. The general case follows from these via:
Theorem 1.36 Letf be an analytic map atp with ord(f′,p ) =n≥ 0. Then
up to a local chance of coordinates in domain and range, f(z) =zn+1. That
is, there exist analytic diﬀeomorphisms with h1(0) = p, and h2(0) = f(p),
such that
h2◦f◦h−1
1 =zn+1.
Proof. We may assume p = f(p) = 0 and f(z) = zng(z) where g(0)⁄=
0. Then h(z) = g(z)1/n is a well-deﬁned analytic function near z = 0,
once we have chosen a particular value for g(0)1/n. It follows that f(z) =
(zh(z))n = pn(h1(z)) where h′
1(z)⁄= 0. Thus h1 is a local diﬀeomorphism,
and f◦h−1
1 (z) =zn .
20

The argument as the basic multivalued function. It is useful to have
a general discussion of the sometimes confusing notion of ‘branch cuts’ and
‘multivalued functions’. Here are 2 typical results.
Theorem 1.37 Let U⊂ C∗ be a simply-connected region. Suppose p∈U,
θ∈ R and arg(p) = θ mod 2π. Then there is a unique continuous function
Q
Arg :U→ R
such that Arg(p) =θ and Arg(z) = arg(z) mod 2π for all z∈U.
Proof. In fact we can explicitly write
Arg(z) =θ + Im
∫ z
p
dζ
ζ ;
the fact thatU is simply-connected implies that the integral does not depend
on the choice of a path from p to z.
Since log(z) = log|z| +i arg(z), we ﬁnd:
Corollary 1.38 There is a single-valued branch of the logarithm on U.
Since zα = exp(α logz), we have:
Corollary 1.39 There is a single-valued branch of zα on U.
Residue calculus and deﬁnite integrals. The residue theorem can be
used to systematically evaluate various deﬁnite integrals.
Deﬁnite integrals 1: rational functions on R. Whenever a rational
function R(x) = P (x)/Q(x) has the property that
∫
R|R(x)|dx is ﬁnite, we
can compute this integral via residues: we have
∫ ∞
−∞
R(x)dx = 2πi
∑
Imp>0
Res(R,p ).
(Of course we can also compute this integral by factoring Q(x) and using
partial fractions and trig substitutions.)
Example. Where does π come from? It emerges naturally from rational
functions by integration — i.e. it is a period. Namely, we have
∫ ∞
−∞
dx
1 +x2 = 2πi Res(1/(1 +z2),i ) = 2πi(−i/2) =π.
21

Of course this can also be done using the fact that
∫
dx/(1+x2) = tan−1(x).
More magically, for f(z) = 1/(1 +z4) we ﬁnd:
∫ ∞
−∞
dx
1 +x4 = 2πi(Res(f, (1 +i)/
√
2) + Res(f, (1 +i)/
√
2) = π√
2·
Both are obtain by closing a large interval [−R,R ] with a circular arc in the
upper halfplane, and then taking the limit as R→∞ .
We can even compute the general case, f(z) = 1/(1 +zn), with n even.
For this letζk = exp(2πi/k), sof(ζ2n) = 0. Let P be the union of the paths
[0,∞)ζn and [0,∞), oriented soP moves positively on the real axis. We can
then integrate over the boundary of this pie-slice to obtain:
(1−ζn)
∫ ∞
0
dx
1 +xn =
∫
P
f(z)dz = 2πi Res(f,ζ 2n) = 2πi/(nζn−1
2n ),
which gives ∫ ∞
0
dx
1 +xn = 2πi
n(−ζ−1
2n +ζ+1
2n ) = π/n
sinπ/n·
Here we have used the fact that ζn
2n =−1. Note that the integral tends to
1 as n→∞ , since 1/(1 +xn) converges to the indicator function of [0 , 1].
Deﬁnite integrals 2: rational functions of sin( θ) and cos(θ). Here
is an even more straightforward application of the residue theorem: for any
rational function R(x,y ), we can evaluate
∫ 2π
0
R(sinθ, cosθ)dθ.
The method is simple: set z = eiθ and convert this to an integral of an
analytic function over the unit circle. To do this we simple observe that
cosθ = (z + 1/z)/2, sinθ = (z− 1/z)/(2i), and dz =izdθ . Thus we have:
∫ 2π
0
R(sinθ, cosθ)dθ =
∫
S1
R
( 1
2i
(
z− 1
z
)
, 1
2
(
z + 1
z
))dz
iz·
For example, for 0 <a< 1 we have:
∫ 2π
0
dθ
1 +a2− 2a cosθ =
∫
S1
idz
(z−a)(az− 1) = 2πi(i/(a2− 1)) = 2π
1−a2·
Deﬁnite integrals 3: fractional powers of x.
∫∞
0 xaR(x)dx, 0<a< 1,
R a rational function.
22

For example, consider
I(a) =
∫ ∞
0
xa
1 +x2dx.
Let f(z) = za/(1 +z2). We integrate out along [0 ,∞) then around a large
circle and then back along [0 ,∞). The last part gets shifted by analytic
continuation of xa and we ﬁnd
(1− 1a)I(a) = 2πi(Res(f,i ) + Res(f,−i))
and Res(f,i ) = ia/(2i), Res(f,−i) = (−i)a/(−2i) (since xa/(1 + x2) =
xa/(x−i)(x +i)). Thus, if we let ia =ω = exp(πia/2), we have
I(a) = π(ia− (−i)a)
(1− 1a) =πω−ω3
1−ω4 = π
ω +ω−1 = π
2 cos(πa/2)·
For example, when a = 1/3 we get
I(a) =π/(2 cos(π/6)) =π/
√
3.
Residues and inﬁnite sums. The periodic function f(z) =π cot(πz) has
the following convenient properties: (i) it satisﬁes f(z) = f(z + 1); (ii) It
has simple poles with residue 1 for all z∈ Z, and no other poles; and (iii)
it remains bounded as Im z→∞ . From these facts we can deduce some
remarkable properties: by integrating over a large rectangle S(R), we ﬁnd
for k≥ 2 even,
0 = lim
R→∞
1
2πi
∫
S(R)
f(z)dz
zk = Res(f(z)/zk, 0) + 2
∞∑
1
1/nk.
Thus we can evaluate the sum ∑ 1/n2 using the Laurent series
cot(z) = cos(z)
sin(z) = 1−z2/2! +z4/4!−···
z(1−z2/3! +z4/5!−··· )
= z−1(1−z2/2! +z4/4!−··· )(1 +z2/6 + 7z4/360 +··· )
= z−1(1−z2/3−z4/45−··· ),
(using the fact that (1/(3!)2− 1/5! = 7/360), which gives
f(z) =π cot(πz) =z−1(1−π2z/2−π4z3/45−··· ).
23

This shows Res(f(z)/z2, 0) =−π2/3 and hence ∑ 1/n2 = π2/6. Similarly,
2ζ(2k) =− Res(f(z)/z2k, 0). For example, this justiﬁes ζ(0) = 1 + 1 + 1 +
··· =−1/2.
Little is known about ζ(2k + 1). Ap´ ery showed thatζ(3) is irrational,
but it is believed to be transcendental.
We note that ζ(s) = ∑ 1/ns is analytic for Re s > 1 and extends an-
alytically to C−{ 1} (with a simple pole at s = 1). In particular ζ(0) is
well-deﬁned. Because of the factorization ζ(z) = ∏(1− 1/ps)−1, the be-
havior of the zeta function is closely related to the distribution of prime
numbers. The famous Riemann hypothesis states that any zero of ζ(s) with
0 < Res < 1 satisﬁes Re s = 1/2. It implies a sharp form of the prime
number theorem, π(x) =x/ logx +O(x1/2+ϵ).
The zeta function also has trivial zeros ats =−2,−4,−6,... , andζ(0) =
−1/2.
Power series for tan( x). The fact that the power series for tan( x) is
much hard to describe than the power series for sin( x) and cos(x) is almost
always quietly skirted in calculus classes. In fact, the power series for tan(x)
and cot(x), and the value of the ζ-function at positive even integers, are all
expressible in terms of the Bernoulli numbers, deﬁned by
∞∑
0
Bk
tk
k! = t
et− 1·
For example, we have
cot(x) =
k∑
0
B2k
(−1)k4kx2k−1
(2k)! ·
The Bernoulli numbers themselves arise in the calculation of ∑N
1 nk.
Hardy’s paper on
∫
sin(x)/xdx . We claim
I =
∫ ∞
0
sinxdx
x = π
2·
Note that this integral is improper, i.e. it does not converge absolutely.
Also, the function f(z) = sin(z)/z has no poles — so how can we apply the
residue calculus?
The trick is to observe that
−2iI = lim
r→0
∫
r<|x|<1/r
eixdx
x ·
24

We now use the fact that |eix+iy)|≤ e−y to close the path in the upper
halfplane, and conclude that
2iI = lim
r→0
∫
S1(r)+
eizdz
z ·
(Here the semicircle is oriented counter-clockwise, as usual.) Since Res(eiz/z, 0) =
1, we ﬁnd 2iI = (2πi)(1/2) and hence I =π/2.
Diﬀerential operators. The operators ∂ and ∂ extend naturally to maps
from 1-forms to 2-forms; they satisfy, for any function f, ∂(f(z)dz) =
(∂f )dz, ∂(f(z)dz) = 0. Then d =∂ +∂ on 1-forms as well.
If we identify complex numbers with vectors, then for a real function u
and a vector ﬁeld E =E1 +iE2, we have
2∂u =∇u and 2 ∂E = (∇· E) +i(∇× E).
1.6 Harmonic functions
In this section we relate complex analytic functions — deﬁned by the van-
ishing of a ﬁrst order operator — to real harmonic functions, deﬁned by the
vanishing of of a second order operator. Harmonic functions can be deﬁned
on Rn and indeed on any Riemannian manifold, and they play a central role
in diﬀerential geometry and mathematical physics.
Harmonic functions. A C2 real-valued function u on Rn is harmonic if
∆u =
∑d2u
dx2
i
= 0.
Equivalently, we have
d∗du = 0,
where∗ is the Hodge star operator (satisfying dxi∧∗dxi = dx1··· dxn).
(This formulation shows ∆u is naturally a volume form).
In physical terms,∇·∇ u = 0, and d2u = 0 is equivalent to∇×∇ u = 0;
i.e.,u generates a volume preserving ﬂow with zero curl (since it is a gradient
ﬂow). Laplaces’s equation says that u locally minimizes the Dirichlet energy∫
|∇u|2dV
In the case of R2 = C, we have
4 d2u
dzdz = ∆u.
Thus ∆u is a constant multiple of the (1, 1)–form ∂∂u =−∂∂u.
Basic facts:
25

1. If f =u +iv is analytic, then f, f, u and v are harmonic.
2. A function u is harmonic iﬀ du/dz is holomorphic.
3. Any real-valued harmonic function u is locally the real part of a holo-
morphic function f =u +iv.
Indeed, one can integrate∂u to obtain an analytic function with ∂f =
∂u. Then ∂f = ∂u; thus d(f +f) = du and so u = f +f up to an
additive constant.
The function v is called a harmonic conjugate of u; it is well–deﬁned
up to an additive constant.
4. Thus any C2 harmonic function is actually inﬁnitely diﬀerentiable.
5. A harmonic function satisﬁes the mean-value theorem: u(p) is the
average of u(z) over S1(z,p ).
6. A harmonic function satisﬁes the maximum principle. (The real part
of an analytic functions deﬁnes an open map to R.)
7. If u is harmonic and f is analytic, then u◦f is also harmonic.
8. A uniform limit of harmonic functions is harmonic.
/Minus4 /Minus2 2 4
/Minus3
/Minus2
/Minus1
1
2
3
Figure 1. Orthogonal level sets.
Examples. The function Re(z3) = x3− 3xy2 is a harmonic polynomial.
The function arg z is the harmonic conjugate of log |z|. This shows the
harmonic conjugate may be multivalued.
26

Orthogonality and harmonic conjugates. It is an important fact that
the level sets of a pair of harmonic conjugates u and v are orthgonal. This
follows, e.g. from the fact that ( u,v ) are just the pullbacks of ( x,y ) under
the conformal map f(z) =u +iv. More formally, their gradients satisfy
2∂(u +iv) = 0 =∇u +i∇v,
so in fact∇v =i∇u.
The condition that u is harmonic is the same as saying that i∇u =∇v
for some v. Equivalently, it says that d(∂u) =∂∂u = 0.
Flows. Since the level sets of u and v are orthogonal, the area-preserving
ﬂow generated by ∇u follows the level sets of v, and vice-versa. A simple
example is provided by polar coordinates, which give the level sets of u and
v where log|z| =u +iv. The area-preserving ﬂows are rotation around the
origin, and the radial ﬂow at rate 1 /r through circles of radius r.
See Figure 1 for another example, this time on U = C−{− 2, 2}, where
the level sets are conics. These conics are the images of radial lines and
circles under f(z) =z + 1/z, so they are also locally level sets of harmonic
functions.
Electricity. It is often useful to think of the physics behind harmonic
functions, namely the electric potentialu associated to a charge distribution
ρ satisﬁes ∆u =ρ, and the corresponding electric ﬁeld is given by E =∇u.
Thus u is harmonic in the charge-free regions of space, and for a compact
region U, the ﬂux of E through ∂U gives the amount of charge in U.
The potentialu(z) = log|z| represents a point charge at the origin, while
u(z) = Re(1/z) represents a dipole. The level sets of this section function
are tangent circles atz = 0, arising as the pullbacks of the level sets of Re(z)
under z↦→ 1/z.
Harmonic extension. Here is one of the central existence theorems for
harmonic functions.
Theorem 1.40 There is a unique linear map P :C(S1)→C(∆) such that
u =P (u)|S1 and P (u) is harmonic on ∆.
Proof. Uniqueness is immediate from the maximum principle. To see
existence, observe that we must have P (zn) =zn and P (zn) =zn. Thus P
is well-deﬁned on the span S of polynomials in z and z, and satisﬁes there
‖P (u)‖∞ =‖u‖∞. Thus P extends continuously to all of C(S1). Since the
uniform limit of harmonic functions is harmonic, P (u) is harmonic for all
u∈C(S1).
27

Poisson kernel. The map P can be given explicit by the Poisson kernel.
For example, u(0) is just the average of u overS1. We can also say u(p) is
the expected value of u(z) under a random walk starting at p that exits the
disk at z.
To ﬁnd the Poisson kernel explicitly, suppose we have aδ-mass atz = 1.
Then it should extend to a positive harmonic functionu on ∆ which vanishes
along S1 except at 1, and has u(0) = 0. In turn, u should be the real part
of an analytic function f : ∆ → C such that f(0) = 1 and Re f|S1 = 0
and f has a pole at z = 1. Such a function is given simply by the M¨ obius
transformation f : ∆→U ={z : Re z >0}:
f(z) = 1 +z
1−z = 1 +
∞∑
1
2zn.
Convolving, we ﬁnd the analytic function with Re f = u for a given u∈
C(S1) is given by
F (z) = 1
2π
∫
S1
f(z/t)u(t)|dt|,
and thus
u(r,α ) = 1
2π
∫
S1
Pr(α−θ)u(θ)dθ,
where, for z =reiθ, we have
Pr(θ) = Ref(z) = 1−|z|2
|1−z|2 = 1−r2
1− 2r cosθ +r2·
Relation to Fourier series. The above argument suggests that, to deﬁne
the harmonic extension of u, we should just write u(z) =∑∞
−∞anzn onS1,
and then replace z−n by zn to get its extension to the disk. This actually
works, and gives another approach to the Poisson kernel.
In fact, the δ-function at z = 1 on S1 is formally given by
δ =
∞∑
−∞
zn = 1 + 2 Re
∞∑
1
zn = Ref(z),
and so its extension to ∆ is given by
Pr(θ) = 1
1−z + 1
1−z− 1,
where z = exp(iθ).
28

/Minus3 /Minus2 /Minus1 0 1 2 3
2
4
6
8
Figure 2. The Poisson kernel Pr(θ) forr = 0.5, 0.7, 0.8.
Givenu∈C(S1), it is not true, in general, that its Fourier series∑anzn
converges for all z∈ S1. However, it is true that this series converges in
the unit disk and deﬁnes a harmonic function there. As we have seen, this
harmonic function provides a continuous extension of u. This shows:
Theorem 1.41 Ifu∈C(S1) has Fourier coeﬃcientsan, then for all z∈S1
we have
u(z) = lim
r→1−
∞∑
−∞
anr|n|zn.
(Here an = (1/2π)
∫
S1u(θ) exp(−nθ)|dθ|.)
Abel summation. In general, we say S is the Abel sum of the series ∑bn
if S = limr→1−
∑bnrn. For example,
1− 2 + 3− 4 +··· = lim(1− 2r + 3r2−··· ) = lim−1/(1 +r)2 =−1/4.
The result above shows the Fourier series of f is Abel summable to the
original function f.
Liouville’s theorem. Using the Poisson kernel, it is easy to see that a
harmonic function u on C is the real part of an analytic function deﬁned on
all of C (this is true for any simply connected domain). From this one can
deduce that a bounded harmonic function on C is constant. In fact we have:
Theorem 1.42 Any positive harmonic function on C is constant.
29

Proof. Writeu = Re(f) with f analytic; then f(C) is not dense in C, so f
is constant.
These results generalize to Rn, where other proofs are available.
Laplacian as a quadratic form, and physics. Suppose u,v ∈ C∞
c (C)
– so u andv are smooth, real-valued functions vanishing outside a compact
set. Then, by integration by parts, we have
∫
∆
⟨∇u,∇v⟩ =−
∫
∆
⟨u, ∆v⟩ =−
∫
∆
⟨v, ∆u⟩.
To see this using diﬀerential forms, note that:
0 =
∫
∆
d(u∗dv) =
∫
∆
(du)(∗dv) +
∫
∆
u(d∗dv).
In particular, we have
∫
∆
|∇u|2 =−
∫
∆
u∆u.
Compare this to the fact that ⟨Tx,Tx⟩ =⟨x,T∗Tx⟩ on any inner product
space. Thus −∆ deﬁnes a positive-deﬁnite quadratic form on the space of
smooth functions.
The extension of u fromS1 to ∆ is a ‘minimal surface’ in the sense that
it minimizes
∫
∆|∇u|2 over all possible extensions. Similarly, minimizing
the energy in an electric ﬁeld then leads to the condition ∆ u = 0 for the
electrical potential.
Probabilistic interpretation. Brownian motion is a way of constructing
random paths in the plane (or Rn). It leads to the following simply inter-
pretation of the extension operator P . Namely, given p∈ ∆, one considers
a random path pt with p0 =p. With probability one, there is a ﬁrst T >0
such that|pT| = 1; and then one sets u(p) =E(u(pT )). In other words, u(p)
is the expected value of u(pT ) at the moment the Brownian path exits the
disk.
Using the Markov property of Brownian motion, it is easy to see thatu(p)
satisﬁes the mean-value principle, which is equivalent to it being harmonic.
It is also easy to argue that |p0−pT| tends to be small when p0 is close to
S1, and hence u(p) is a continuous extension of u|S1.
The Poisson kernel (1/2π)Pr(θ)dθ gives the hitting density on S1 for a
Brownian path starting at (r, 0).
30

/Minus2 /Minus1 0 1 2
0.0
0.5
1.0
1.5
2.0
Figure 3. Streamlines around a cylinder.
Hyperbolic geometry interpretation. Alternatively, u(z) is the ex-
pected value of u(p) and the endpoint of a random hyperbolic geodesic ray
γ in ∆ with one vertex at z. (The angle of the ray in Tz∆ is chosen at
random in S1.)
Fluid ﬂow around a cylinder. We begin by noticing thatf(z) =z + 1/z
gives a conformal map from the region U ⊂ H where|z| > 1 to H itself,
sending the circular arc to [ −2, 2]. Thus the level sets of Im f = y(1−
1/(x2+y2)) describe ﬂuid ﬂow around a cylinder. Note that we are modeling
incompressible ﬂuid ﬂow with no rotation, i.e. we are assuming the curl of
the ﬂow is zero. This insures the ﬂow is given by the gradient of a function.
Note thatf(z) tends to the identity at inﬁnity, but|f′(z)| =|1−1/z2|≤
1 + 1/|z|2≤ 2 gets close to two near the top of the cylinder. Thus a ﬂow
line starting at the left at a small height h and moving at unit speed is
compressed to heighth/2 as it runs along the top of the cylinder, and moves
at speed close to 2.
Harmonic functions and the Schwarz reﬂection principle. Here is an
application of harmonic functions that will be repeatedly used in geometric
function theory.
Let U⊂ C be a region invariant under z↦→ z. Suppose f : U→ C is
continuous,
f(z) =f(z), (1.3)
and f is analytic on U+ =U∩ H. We can then conclude that f is analytic
on U. In particular, f is analytic at each point of U∩ R.
Here is a stronger statement:
31

Theorem 1.43 Supposef :U+→ C is analytic and Imf(z)→ 0 as Imz→
0. Then f extends to an analytic function on U satisfying (1.3).
Proof. The statement is local, so we can assume U =B(p,r ) where p∈ R.
Letf(z) =u(z)+iv(z); thenv is harmonic onU+ andv extends continuously
to the real axis, with v(x) = 0. Extend v to U byv(z) =−v(z).
Now by the Poisson integral, v|S1(p,r ) extends to a unique harmonic
function h on B(p,r ). By uniqueness, h(z) = −h(z), and hence h also
vanishes on the real axis. Thus h =v on ∂U+. By the maximum principle,
h =v on U+, and hence on U.
We are now done: by the existence of harmonic conjugates, there is some
analytic function on U with ImF =v. But then Im F = Imf on U+, so F
and f diﬀer by a real constant on U+, which can be normalized to be zero.
Example. Suppose f(z) is analytic on H and f(z)→ 0 along an interval
in R. Then f is identically zero. This extends the ‘isolated zero’ principle
to the boundary of a region.
Remark. One can replacez↦→z with reﬂection through any circle, or more
generally with local reﬂection through a real-analytic arc. For example, we
have:
Theorem 1.44 Let U ⊂ ∆ be a region and let f : U → ∆∗ be analytic.
Suppose|f(z)| →1 as|z| →1 in U. Then f extends to U∪ρ(U) by
Schwarz reﬂection, where ρ(z) = 1/z.
Proof. We can assume thatU⊂ ∆∗ since the extension issue is local along
S1. Lift f to an analytic map ~f : ~U → H, using the universal covering
map π : H→ ∆∗ given by π(z) = ez on the domain and range. Then
Im~f(z) = log |f(π(z))| →0 as | Im(z)| →0 in ~U, so we can apply the
reﬂection principle in H to ~f. It then descends by periodicity to give the
require extension of f.
1.7 Additional topics
Here we brieﬂy mention some other classical topics in complex analysis.
The Phragmen–Lindel¨ of Theorems. These theorems address the fol-
lowing question. Suppose f(z) is an analytic function on the horizontal
32

strip U ={x +iy : a < y < b}, and continuous on U. Can we assert that
supU|f| = sup∂U|f|?
The answer is no, in general. However, the answer is yes iff(x+iy) does
not grow too rapidly as |x|→∞ . In fact, this is a property of harmonic
functions u(z). The point is that if we truncate the strip to a rectangle by
cutting along the lines where |x| = R, then the harmonic measure of the
ends (as seen from a ﬁxed point z∈ U) tends to zero exponentially fast.
Thus if|u(x +iy)| =O(|x|n) for some n, we get the desired control.
Runge’s theorem. Here is an interesting and perhaps surprising applica-
tion of Cauchy’s formula.
Let K ⊂ C be a compact set, let C(K) denote the Banach space of
continuous functions with the sup-norm, and let A(K),R (K) and P (K)⊂
C(K) denote the closures of the analytic, rational and polynomial functions.
Note that all three of these subspaces are algebras .
Example. ForK =S1 we have R(K) = A(K) = C(K) by Fourier series,
but P (K)⁄=C(K), since
∫
S1p(z)dz = 0 for any polynomial. In particular,
1/z⁄∈P (S1).
Remarkably, if we remove a small interval from the circle to obtain an
arcK = exp[0, 2π−ϵ], then 1/z can be approximated by polynomials on K.
Theorem 1.45 (Runge) For any compact set K ⊂ C we have R(K) =
A(K), and P (K) =A(K) provided C−K is connected.
Proof. For the ﬁrst result, supposef(z) is analytic on a smoothly bounded
neighborhood U of K. Then we can write
f(z) = 1
2πi
∫
∂U
f(t)dt
t−z =
∫
∂U
Fz(t)dt.
Sinced(z,∂U )≥d(K,∂ )> 0, the functions{Fz} range in a compact subset
of C(∂U ). Thus we can replace this integral with a ﬁnite sum at the cost
of an error that is small independent of z. But the terms f(ti)/(ti−z)
appearing in the sum are rational functions of z, so R(K) =A(K).
The second result is proved by pole–shifting. By what we have just
done, it suﬃces to show that fp(z) = 1/(z−p)∈ P (K) for every p⁄∈ K.
Let E⊂ C−K denote the set of p for which this is true.
Clearly E contains all p which are suﬃciently large, because then the
power series for fp(z) converges uniformly on K. Also E is closed by deﬁni-
tion. To complete the proof, it suﬃces to show E is open.
33

The proof thatE is open is by ‘pole shifting’. Suppose p∈E,q∈B(p,r )
andB(p,r )∩K =∅. Note that fq(z) is analytic on C−B(p,r ), and tends to
zero as|z|→∞ . Thus fq(z) can be expressed as a power series in 1/(z−p):
(z−q)−1 =
∞∑
0
an(z−p)−n =
∑
anfp(z)n,
convergent for|z−p|>|z−q|, and converging uniformly on K. (Compare
the expression
1
z− 1 =
∞∑
n=1
1
zn,
valid for|z|> 1.) Since ( z−q)−1→ 0 as|z|→∞ , only terms with n≥ 0
occur on the right. But fp∈A(K) by assumption, and A(K) is an algebra,
so it also contains fn
p . Thus fq∈A(K) as well.
Aside: Lavrentiev’s Theorem. It can be shown that ifC−K is connected
and K has no interior, then A(K) =C(K). This is deﬁnitely false for a fat
Swiss cheese: if ∂K is rectiﬁable and of ﬁnite length, then
∫
∂Kf(z)dz = 0
for all f in A(K), and so A(K)⁄=C(K). For more details see [Gam].
Applications: pointwise convergence. Runge’s theorem can be used
to show easily that there is a sequence of polynomials fn(z) that converge
pointwise, but whose limit is not even continuous. Indeed, let An = [0,n ]
and let B1⊂B2⊂··· be an increasing sequence of compact sets such that⋃Bn = C− [0,∞). Then every z∈ C eventually belongs to An or Bn. Let
fn(z) be a polynomial, whose existence is guaranteed by Runge’s theorem,
such that|fn(z)| < 1/n on An and|fn(z)− 1| < 1/n on Bn. Then clearly
limfn(z) = 0 on [0,∞) and limfn(z) = 1 elsewhere.
Applications: embedding the disk into aﬃne space. Runge’s theorem
can also be used to show there is a proper embedding of the unit disk into
C3. See [Re, §12.3].
1.8 Exercises
1. For a,b∈ C, express ab in terms of the dot-product and cross-product
of the vectors represented by a and b.
2. Let f(z) be one-to-one and analytic on a neighborhood of the unit
circleS1⊂ C. Relate
∫
S1f(z)f′(z)dz to the area of the region enclosed
byf(S1).
34

3. Compute df/dz and df/dz for the map f : C→ C given in polar
coordinates by f(r,θ ) = (rα,nθ ), α> 0, n∈ Z.
4. Suppose f(z) is analytic. Compute ( d/dz)(d/dz)|f(z)|2.
5. When is a polynomial p(x,y ) expressible in the form
p(x,y ) =f(x +iy) +g(x−iy),
where f and g are holomorphic?
6. Let f1,...,f n be analytic functions on ∆. Suppose ∑|fi(z)|2 = 1 for
all z∈ ∆.
(i) Show allfi are constant functions, by taking the Laplacian of both
sides of this equation.
(ii) Show allfi are constant functions, by applying the maximum prin-
ciple (or open mapping theorem) to suitable linear combinations of
these functions.
(iii) Let H : Cn→ R be a strictly convex smooth function. Using
method (i) or (ii), prove that if H(f1(z),...,f n(z)) is constant on ∆,
then each function fi(z) is constant.
7. Let fn→ f uniformly on compact subsets of an open connected set
Ω⊂ C, where fn is analytic, and f is not identically equal to zero.
Show if f(w) = 0 then we can write w = limzn, where fn(zn) = 0 for
all n suﬃciently large.
8. Prove that the distributional derivative off(z) = 1/z satisﬁesdf/dz =
Cδ0, and evaluate the constant C. (Equivalently, show that
−
∫
C
f(z)(dφ/dz)|dz|2 =Cφ(0)
for every φ∈C∞
0 (C).)
9. Evaluate: ∫ ∞
−∞
x6
(1 +x4)2dx.
10. Let f : C → C be analytic and let U ⊂ C be a bounded region.
Suppose|f(z)| is constant on ∂U . Show that either f is constant, or
f has a zero in U.
35

11. Compute the Laurent series centered at z = 0 such that
∞∑
−∞
anzn = 1
z(z− 1)(z− 2)
in the region 1 <|z|< 2.
12. Show for any polynomial p(z) there is a z with|z| = 1 such that
|p(z)− 1/z|≥ 1.
13. Let f : Rn+1→ Rn+1 be a continuous function, and suppose that f
does not vanish on the unit sphere Sn. Deﬁne a map F :Sn→Sn by
F (x) =f(x)/|f(x)|. Prove that if F has nonzero degree, then f has a
zero in the unit ball.
14. Let p(n) be the number of partitions of n into unequal parts. (E.g.
p(7) = 5 because 7 can be written as 7, 1 + 2 + 4, 1 + 6, 2 + 5 and
3 + 4.)
(i) Show that f(z) =∏∞
1 (1 +zn) deﬁnes an analytic function on ∆.
(ii) Show that f(z) =∑∞
1 p(n)zn.
(iii) Show that f(z) cannot be analytically continued beyond the unit
disk. (This means if g(z) is analytic on a connected domain U⊃ ∆,
and f(z) =g(z) on ∆ then U = ∆.)
15. Let p(z) be a polynomial of degreed≥ 2, with distinct rootsr1,...,r d.
Show that∑ 1/p′(ri) = 0.
16. Let E ⊂ (−1, 1) be a compact set of zero linear measure, and let
f : ∆−E→ C be a bounded analytic function. Show that f extends
to an analytic function on the whole disk.
17. Let fn(z) be a sequence of polynomials such that fn(z)→f(z) point-
wise in C. Show there exists a dense, open set U⊂ C such that f|U
is analytic. (You may quote the Baire Category theorem.)
18. (a) Estimate log(2) by evaluating S =∑5
0an and E =∑5
0bn(1/2)n,
wheref(x) = log(1+x) =∑anxn andg(y) =f(y/(1−y)) =∑bnyn.
How do these approximations compare to log(2)? (Note: you may use
the fact that E =s5(0).)
(b) What is the radius of convergence of the power series for g(y)?
36

19. For each n >0, give an example of an analytic function f : ∆∗→ C
such that (i) f is nowhere zero, (ii) f has an essential singularity at
z = 0, and (iii) Res(f′/f, 0) =n.
20. Consider the equation
∫ ∞
0
xαdx
(1 +x2)2 = π(1−α)
4 cos 1
2πα·
Find the set of real α such that the integral above is absolutely con-
vergent, and prove the equation above holds for all such α.
21. Let C(R) be the circular arc deﬁned by |z| =R and Im(z)> 0. Prove
that
∫
C(R)(eiz/z)dz→ 0 as R→∞ . (This is used in our calculation
of
∫∞
0 sin(x)/xdx .)
22. Prove the identity
∫ 2π
0
cos2nθdθ = 2π 1· 3· 5··· (2n− 1)
2· 4· 6··· (2n)
by applying the residue theorem to
∫
S1 (z + 1/z)2n dz/z.
23. Given w∈ C, ﬁnd an explicit sequence zn→ 0 such that e1/zn→w.
24. Compute the ﬁrst four nonzero terms in the power series for tan( z) at
z = 0 by formally inverting the power series for tan−1(z) =
∫
dz/(1 +
z2).
25. Suppose a pair of analytic functions on a region U satisfy|f(z)| =
|g(z)|. Prove that f(z) =ag(z) for some constant a with|a| = 1.
26. Let Hd ⊂ C[x,y ] be the space of harmonic polynomials p that are
homogeneous of degree d. (Harmonic means d2p/dx2 +d2p/dy2 = 0.)
Compute dimHd, give an explicit example of a nonzero polynomial
p(x,y ) =∑aijxiyj∈Hd, and show the⊕Hd|S1 spans a dense subset
of C(S1), the space of continuous functions on the circle S1 ⊂ C
with‖f‖ = supS1|f(z)|. Explain these results in terms of analytic
functions.
27. Let f(z) be an analytic function on ∆ withf(0) = 0 and
∫
∆|f(z)|2|dz|2<
∞. Prove that:
∫
∆
| Re(f)|2|dz|2 =
∫
∆
| Im(f)|2|dz|2
37

28. Let f(z) be analytic in a region U, and suppose
∫
U|f(z)||dz|2 <∞.
Prove that there is a constant M such that for all z∈U we have
|f(z)|≤ M
d(z,∂U )2.
29. Use the preceding two problems to prove that a uniform limit of har-
monic functions on a domain U⊂ C is harmonic.
30. Find a bounded harmonic functionu : ∆→ R such that limr→1u(reiθ) =
1 for θ∈ (0,π ) and =−1 for θ∈ (π, 2π).
31. Give an example of a bounded harmonic function u on the unit disk
whose harmonic conjugate v is unbounded.
32. Let u : ∆→ R be a smooth function such that ∆ u(z) > 0 for all
z∈ ∆. Show that u satisﬁes the maximum principle.
33. Give an example of an unbounded analytic function on the unit disk
with the property that limz→w|f(z)| = 1 for all w∈S1 exceptw = 1.
34. Given R >1 let AR ={z : 1 <|z| < R}. Let f : AR→ AS be a
bijective holomorphic map. Prove that R =S. (Hint: apply Schwarz
reﬂection to extend f to C∗.)
35. Let p(z) be a polynomial of degree d> 1. Show that the zeros of p′(z)
belong to the convex hull of the zeros of p(z). (The convex hull of a
set E is the intersection of all the convex sets containing E.)
Hint: consider p′(z)/p(z).
36. Deﬁne u(z) on S1 by u(z) = 1 if z2 ∈ H and u(z) = 0 otherwise.
Find a formula for the extension of u to a harmonic function on the
disk, and draw the locus where u(z) = 1/2. (The extension should be
continuous on ∆ apart from ﬁnitely many points on S1.)
37. Prove that for any p≥ 1, the set of analytic functions
F =
{
f : ∆→ C :
∫
|f(z)|p|dz|2≤ 1
}
is compact. That is, every sequence fn∈F has a subsequence con-
verging uniformly on compact subsets of ∆, and f = limfn belongs to
F as well.
38

38. Let f(z) =∑anzn be a power series with coeﬃcientsan∈ Z. Suppose
thatf(z) deﬁnes a bounded analytic function on the unit disk. Prove
that f(z) is a polynomial.
39. Let U ={z : 0 <|z|< 1 and 0 < arg(z)<α}, where 0 < α <2π.
Find a formula for an analytic homeomorphism f :U→ H.
40. Compute ∫
|z|=1/2
dz
z sin2(z)·
41. Let fn : U→ C be a sequence of analytic functions converging uni-
formly on compact sets to a nonconstant function f :U→ C. Assume
the mappings fn(z) are at most d-to-1. Show the same is true of f(z).
2 The simply-connected Riemann surfaces
In this section we discuss C, ˆC and H∼= ∆ from a geometric perspective.
Riemann surfaces. A Riemann surface X is a connected complex 1-
manifold. This means X is a Hausdorﬀ topological space equipped with
a family of charts which are homeomorphisms
φi :Vi→ C,
with Vi⊂ C an open region, such that ⋃φi(Vi) = X and the transition
functions φ−1
i ◦φj are analytic where deﬁned.
It then makes sense to discuss analytic functions on X, or on any open
subset of X: we say f is analytic if f◦φi is analytic for all i.
We then obtain asheaf of ringsOX withOX(U) consisting of the analytic
maps f : U→ C. From a more modern perspective, a Riemann surface is
a connected Hausdorﬀ ringed space ( X,OX) that is locally isomorphic to
(∆,O∆).
Aside from C and connected open sets U⊂ C, the ﬁrst interesting Rie-
mann surface (and the basic example of a compact Riemann surface) is the
Riemann sphere ˆC. The map f :ˆC−{ 0}→ C given byf(z) = 1/z provides
a chart near inﬁnity. The second class of examples come from the complex
tori X = C/Λ, where Λ ∼= Z2 is a discrete subgroup of ( C, +). Charts are
provided by the covering map C→X.
Maps. The space of Riemann surfaces forms a category with the analytic
maps f : X → Y as morphisms. A map is analytic if it gives a locally
39

analytic map on C in all charts; equivalent, f is analytic if f is continuous
and f∗(OY ) is a subsheaf of OX.
Meromorphic functions. A meromorphic function on X is an analytic
mapf :X→ˆC that is not identically∞. Equivalently,f(z) is meromorphic
if it can be locally written as a quotient of two holomorphic functions, not
both zero. The sheaf of meromorphic functions is denoted M. Its construc-
tion fromO is one of the most basic examples of sheaﬁﬁcation.
Since X is connected, the ring M(X) (also denoted C(X)) of all mero-
morphic functions on X forms a ﬁeld, and the ring O(X) of all analytic
functions forms an integral domain.
We will see thatM(ˆC) = C(z), whileO(ˆC) = C, so not every meromor-
phic function is a quotient of holomorphic functions. We will see that O(C)
is much wilder (it contains exp(exp z), etc.), and yet M(C) is the ﬁeld of
fractions ofO(C).
Proper maps. An analytic mapf :X→Y is proper iff−1 sends compact
sets to compact sets. This is equivalent to the condition that f(zn)→∞
wheneverzn→∞ .
Proper analytic maps f : X→ Y are the ‘tamest’ maps between Rie-
mann surfaces. For example, they have the following properties:
1. If f is not constant, it is surjective.
2. If f′ never vanishes, then f is a covering map.
3. If f′ never vanishes and Y is simply-connected, then f is an isomor-
phism.
Note that if X is compact, then every holomorphic map f : X→ Y is
proper, and hence every nonconstant f :X→Y is surjective.
Degree. For a proper holomorphic map f :X→Y , the number of points
in f−1(z), counted with multiplicity, is independent of z. This number is
called the (topological) degree of f. In the case X =Y = C, it is the same
as the degree of the polynomial f.
Example. A polynomial f : C→ C is a proper map, with its topological
degree equal to its algebraic degree. The entire function exp : C→ C is not
proper, since it omits the point 0.
Classiﬁcation. In principle, the classiﬁcation of Riemann surfaces is com-
pleted by the following result:
Theorem 2.1 (The Uniformization Theorem) Every simply-connected
Riemann surface is isomorphic to H, C or ˆC.
40

Then by the theory of covering spaces, an arbitrary Riemann surface sat-
isﬁesX∼=ˆC,X = C/Γ, or X =ˆC/Γ, where Γ is a group of automorphisms.
Such Riemann surfaces are respectively elliptic, parabolic and hyperbolic.
Their natural metrics have curvatures 1, 0 and−1.
In this section we will discuss each of the simply-connected Riemann
surfaces in turn. We will discuss their geometry, their automorphisms, and
their proper endomorphisms.
2.1 The complex plane
Theorem 2.2 An analytic function f : C→ C is proper iﬀ f(z) is a non-
constant polynomial.
Proof. Clearly a polynomial of positive degree is proper. Conversely, if f
is proper, then f has ﬁnitely many zeros, and so no zeros for |z| > some
R. Then g(z) = 1/f(1/z) is a nonzero, bounded analytic function for 0 <
|z| < R. Consequently g(z) has a zero of ﬁnite order at z = 0. This
gives|g(z)|≥ ϵ|z|n, and hence |f(z)|≤ M|z|n. By Cauchy’s bound, f is a
polynomial.
To say f : C→ C is proper is the same as to say that f extends to a
continuous functionF :ˆC→ˆC. The same argument shows, more generally,
that if f :X→Y is a continuous map between Riemann surfaces, and f is
analytic outside a discrete set E⊂X, then f is analytic.
Corollary 2.3 The automorphisms of C are given by the aﬃne maps of the
form f(z) =az +b, where a∈ C∗ and b∈ C.
Thus Aut(C) is a solvable group. If f∈ Aut(C) is ﬁxed-point free, then
it must be a translation. This shows:
Corollary 2.4 Any Riemann surface covered by C has the form X = C/Λ,
where Λ is a discrete subgroup of (C, +).
Example. We have C/(z↦→ z + 1)∼= C∗; the isomorphism is given by
π(z) = exp(2πiz).
Metrics. A conformal metric on a Riemann surface is given in local coor-
dinates by ρ = ρ(z)|dz|. We will generally assume that ρ(z)≥ 0 and ρ is
continuous, although metrics with less regularity are also useful.
41

A conformal metric allows one to measure lengths of arcs, by
L(γ,ρ ) =
∫
γ
ρ =
∫ b
a
ρ(γ(t))|γ′(t)|dt;
and areas of regions, by
A(U,ρ ) =
∫
U
ρ2 =
∫
U
ρ2(z)|dz|2 =
∫
U
ρ2(z)dxdy.
Metrics pull back under analytic maps by the formula:
f∗(ρ) =ρ(f(z))|f′(z)||dz|,
and satisfy natural formulas such as
L(γ,f∗ρ) =L(f(γ),ρ )
(so long as f(γ) is understood as the parameterized path γ◦f).
A metric allows us to intrinsically measure the size of the derivative a
map f : (X1,ρ 1)→ (X2,ρ 2): it is given by
‖Df‖ =|f′(z)|ρ2(f(z))
ρ1(z) = f∗ρ2
ρ1
·
We have‖Df‖≡ 1 iﬀ f is a local isometry.
Flat metrics. The Euclidean metric on the plane is given by ρ =|dz|.
Since|dz| is Λ-invariant, we ﬁnd:
Theorem 2.5 Every Riemann surface covered by C admits a complete ﬂat
metric, unique up to scale.
For example, on C∗∼= C/Z we have the cylindrical metric ρ =|dz|/|z|.
Every circle|z| =r has length 2π in this metric.
Cone metrics. Consider the metric ρ =|z|α|dz|/|z| on C. We claim this
is a ﬂat metric, making the origin into a cone point of total angle θ = 2πα.
To see this is plausible, note that the unit ball B(0, 1) has radius R =∫ 1
0 tαdt/t = 1/α, and circumference C = 2π, so C/R = 2πα.
Alternatively, letf(z) =zn. Then we ﬁnd
f∗(ρ) =|z|nαn|dz|/|z| =n|dz|
ifα = 1/n. Thus the caseα = 1/n gives the quotient metric on (C,n|dz|)/⟨ζn⟩,
where ζn = exp(2πi/n).
42

Orbifold quotients. We can also take the quotient of C by the inﬁnite
dihedral group, D∞ =⟨z + 2π,−z⟩⊂ Aut C. The result is C itself, which
the quotient map given by f(z) = cos(z).
Closely related is the important map C : C∗→ C given by
C(z) = z +z−1
2
This degree two map gives the orbifold quotient of C∗ byz↦→ 1/z. It gives
an intermediate covering space to the one above, if we regard C∗ as C/Z.
The mapπ sends circles to ellipse and radial lines to hyperboli, with foci
[−1, 1]. In fact all conics with these foci arise in this way. (See Figure 1.)
There is a unique (singular) metric ρ on C such that f∗(ρ) = |dz|,
namely:
ρ = |dz|
|1−z2|1/2·
To check this, note we have:
f∗(ρ) =| sin(z)|/|1− cos2(z)|1/2 = 1.
Note also that the length of [ −1, 1] in the ρ-metric is given by
∫ 1
−1(1−
x2)−1/2dx =π.
The quotient space C/D∞ is an orbifold, i.e. a space which is locally
modeled on a quotient of the plane by a rotation. It has cone points of type
2 and z =±1. A loop around a cone point of order n has order n in the
orbifold fundamental group, so π1(X) = Z/2∗ Z/2.
In general, by broadening the scope of covering spaces and deck groups
to include orbifolds and maps with ﬁxed points, we enrich the supply of
Euclidean (and other) Riemann surfaces. For example, the (3 , 3, 3) orbifold
is also Euclidean — it is the double of an equilateral triangle.
Chebyshev polynomials. Let us study the degree two map C : C∗→ C
in more detail.
Since C(zn) =C(z−n), there is a polynomial Tn such that
Tn(C(z)) =C(zn) =Cn(z).
These are the Chebyshev polynomials; they are given by T1(z) =z, T2(z) =
2z2− 1, T3(z) = 4z3− 3z, P4(z) = 8z4− 8z2 + 1, etc.
Cosine and trace. The Chebyshev polynomials give the multiple angle
formulas for cosine: since for z =eiθ we haveC(z) = cosθ, it follows that
Tn(cosθ) = cos(nθ).
43

By the same token, we have
Tn(trA/2) = trAn/2
for all A∈ SL2(C).
-1.0 -0.5 0.5 1.0
-1.0
-0.5
0.5
1.0
Figure 4. The cubic Chebyshev polynomial T3(x).
Sincezn preserves circles and radial lines, and its Julia set isS1, we ﬁnd:
Theorem 2.6 The polynomials Tn(z) preserve the hyperbolas and ellipses
with foci at ±1, and its Julia set is [−1, 1].
The mapszn andTn(z) are the only polynomials with smooth Julia sets.
Sine formulas. It is natural also to introduce the rational function on C∗
deﬁned by
S(z) = z−z−1
2i ,
so that (C(z),S (z)) = (cosθ, sinθ) when z = exp(iθ). Note that S(1/z) =
−S(z). It is straightforward to see that we can ﬁnd a second sequence of
polynomials Un(C) satisfying
Un(C(z))S(z) =S(zn).
For example,U2(z) = 2z andU3(z) = 4z2− 1. (It is more common to index
Un(z) by its degree, which is n− 1.) Since cos 2(nθ) + sin2(nθ) = 1, we have:
Theorem 2.7 For all n≥ 1 and all C∈ C, we have
Tn(C)2− (C2− 1)Un(C) = 1.
44

Units and Pell’s equation. To explain the preceding equation more
conceptually, let us consider the quadratic extension of rings B/A, where
A = C[C] and B = C[C,S ]/(C2 +S2 = 1).
Note that A∼=Oalg(C) and
B∼=Oalg(C∗)∼= C[z, 1/z],
wherez =C +iS. The main diﬀerence in these rings is their units: we have
A∗ = C∗ while
B∗ = C∗zZ.
We can regard B as the extension A[
√
D], where D = C2− 1; then the
preceding theorem shows that (Tn,Un) are solutions to Pell’s equation,
p2−Dq2 = 1,
which gives the norm from B toA and describes the units in B of the form
ϵ =p +q
√
D. In our case,
√
D =iS, and
ϵn =zn =Tn(C) +iUn(C)S.
(A similar discussion can be pursued for all hyperelliptic curves, using an
algorithm due ot Abel.)
The classical solutions to Pell’s equation arise when D∈ Z and describe
the units of norm 1 in Z[
√
D], which form a cyclic group. For example,
when D = 3 this group is generated by ϵ = 2 +
√
3. These solutions can be
very large, even when D has only moderate size, and are responsible for the
enormous numbers arising in Archimedes’ cattle problem.
Solving the cubic. Complex algebra ﬁnds its origins in the work of Car-
dano et al on solving cubic polynomial equations. Remarkably, complex
numbers intervene even when the root to be found is real.
One can always make a simple transformation of the form x↦→x +c to
reduce to the form
x3 +ax +b = 0.
One can further replace x with cx to reduce to the form
x3− 3x =b.
Thus the solution to the cubic involves inverting a single cubic function
P3(z) =z3− 3z.
45

Now observe that P3(z + 1/z) = z3 + 1/z3; i.e., P3(z) is a rescaling
of the Chebyshev polynomial T3(z). Thus, to solve P3(x) = a, we just
write a = y + 1/y (by solving a quadratic equation), and then we have
x =y1/3 +y−1/3.
Classiﬁcation of polynomials. Let us say p(z) is equivalent to q(z) is
there are A,B ∈ Aut(C) such that Bp(Az) =q(z). Then every polynomial
is equivalent to one which is monic and centered (the sum of its roots is
zero). Every quadratic polynomial is equivalent to p(z) =z2.
The reasoning above shows, every cubic polynomial with distinct critical
points is equivalent to P3(z) = z3− 3z. Otherwise it is equivalent to z3.
But for degree 4 polynomials we are in new territory: the cross-ratio of the
3 critical points, together with inﬁnity, is an invariant.
It is a famous fact (proved using Galois theory) that a general quintic
polynomial (with integral coeﬃcients) cannot be solved by radicals.
2.2 The Riemann sphere
We now turn to the Riemann sphere ˆC = C∪{∞} . We will examine the
sphere from several perspectives: as a Riemann surface, as a round sphere,
as the projectively line, and as the boundary of hyperbolic space.
The projective line. We have a natural projection
π : C2−{ (0, 0)}→ ˆC∼= P1
given by π(z0,z 1) = z0/z1; it records the slope of each line. This gives a
natural identiﬁcation of ˆC with the projective line P1, i.e. the space of lines
in C2.
Aside: Some topology of projective spaces. The real projective plane RP2 is
the union of a disk and a M¨ obius band. The natural mapp : C2−{(0, 0)}→
ˆC factors through the Hopf mapS3→S2, whose ﬁbers have linking number
one. This map generates π3(S2).
The topological degree of f(z) =P (z)/Q(z), assuming gcd(P,Q ) = 1 in
C[z], is max(degP, degQ).
f :ˆC→ˆC
byf(z) =P (z)/Q(z), as can be veriﬁed by looking in charts near ∞.
M¨ obius transformations. So long as ad− bc ⁄= 0, the map f(z) =
(az +b)/(cz +d) deﬁnes an automorphism of ˆC. Its inverse can be found by
inverting the matrix
(a b
c d
)
. In fact, the map π above transports the linear
action of SL 2(C) on C2 to the fractional linear action of PSL 2(C) on ˆC.
46

Theorem 2.8 We have Aut(ˆC) = PSL2(C).
Proof. Given f ∈ Aut(ˆC), pick g ∈ PSL2(ˆC) so g(f(∞)) = ∞. Then
g◦f∈ Aut(C)⊂ PSL2(C), so f∈ PSL2(C).
Corollary 2.9 The action of Aut(ˆC) is uniquely triply-transitive: any dis-
tinct triple of points can be sent to (0, 1,∞) by a unique M¨ obius transfor-
mation.
Corollary 2.10 The group PSL2(C) is isomorphic, as a complex manifold,
to the space of distinct triples of points on ˆC.
Rational maps. Note that every analytic map f : ˆC → ˆC is proper,
because ˆC is compact. We can also describe these maps very simply.
Theorem 2.11 Every analytic map f : ˆC→ ˆC is given by a rational map
f(z) =P (z)/Q(z).
Proof. The result is clear if f is constant. Otherwise, f has ﬁnitely many
poles p1,...,p n in C. Let gi(z) = ai/(z−pi)bi +··· be the Laurent tail of
f at pi. Then f−∑gi(z) has no poles, hence it is equal to a polynomial
(if f(∞) =∞) or a constant (if f(∞) is ﬁnite)). It follows that f(z) is a
rational function.
Classiﬁcation of automorphisms up to conjugacy. There is a natural
map tr : PSL2(C)→ C/⟨±1⟩. This is clearly a class function (it is constant
on conjugacy classes), and in fact the conjugation class is almost determined
by this map. Namely we have the following classes:
(1) The identity map, tr(A) =±2.
(2) Parabolics, A(z) =z +a; tr(A) =±2.
(3) Elliptics: A(z) =eiθz; tr(A) = 2 cosθ/2∈ [−2, 2].
(4) Hyperbolics: A(z) =etz, Ret⁄= 0; tr(A) = 2 cosh(t/2).
Note that a M¨ obius transformation (other than the identity) either has
two simple ﬁxed points, or a single ﬁxed point of multiplicity two. The ﬁxed
points of A correspond to its eigenvectors on C2.
Note also that all these elements, except for irrational elliptics, generate
discrete subgroups of Aut(ˆC).
47

If A has eigenvalues λ±1, then tr(A) = λ + 1/λ. Our previous analysis
of this map shows, for example, that the traces of matrices a given value for
|λ| correspond to an ellipse with foci ±2.
Cross-ratios. The cross-ratio is an invariant of ordered 4-tuples of points,
characterized by the conditions that [ a : b : c : d] = [ ga : gb : gc : gd]
for all g∈ Aut(ˆC), and [0 : 1 : ∞ : λ] = λ∈ ˆC−{ 0, 1,∞}. The cross-
ratio gives an explicit isomorphism between the moduli spaceM0,4 and the
triply-punctured sphere.
Stereographic projection. There is a geometric identiﬁcation between
the unit sphere S2⊂ R3 and the Riemann sphere ˆC in which the north pole
N becomes∞ and the rest of the sphere is projected linearly toC = R2×{0}.
Theorem 2.12 Stereographic projection is a conformal map that sends cir-
cles to circles.
Proof of conformality. Consider two vectors at a point p⁄= N on S2.
Construct a pair of circles tangent to these vectors at p and passing through
N. Then these circles meet in the same angles at p and N. On the other
hand, each circle is the intersection of the sphere with a plane. These planes
meet C in the same angle they meet a plane tangent to the sphere at the
north pole N. Thus stereographic projection preserves angles.
1
θ
θ/2
N
x
Figure 5. Stereographic projection on S1.
Theorem 2.13 The Euclidean metric onS2 is transported, by stereographic
projection, to the metric 2|dz|/(1 +|z|2) on ˆC.
48

Proof. Reducing dimensions by one, we obtain the stereographic projec-
tion p : S1− N → R. If θ ∈ [−π,π ] is the angle on the sphere nor-
malized so θ(N) = π, then we ﬁnd x = p(θ) = tan( θ/2). Thus dx =
(1/2) sec2(θ/2)dθ = (1/2)(1 +x2)dθ, which gives dθ = 2dx/(1 +x2). The
case of S2 follows by conformality and rotation invariance.
The unitary point of view. Here is an alternative perspective on the
spherical metric. Let ⟨v,w⟩ = v0w0 +v1w1 be the usual Hermitian metric
on C2. Deﬁne the angle θ between two lines Cv, Cw⊂ C2 by
cos(θ/2) =|⟨v,w⟩|
|v||w|· (2.1)
This θ agrees with the spherical distance on ˆC. (To check this, consider
the points 1 and exp(iα) in S1. Their spherical distance is α, and if we set
v = [1, 1] and w = [eiα/2,e−iα/2], then|v||w| = 2 and⟨v,w⟩ = 2 cos(α/2).)
Exercise. What is the distance, in the spherical metric, from 1 to 1 + i?
For [1 : 1] and [1 +i : 1] we get
cosθ/2 =
√
5/
√
6,
and hence θ = 2 arccos(
√
5/6)≈ 0.841069... .
Given this agreement, it is now clear that the group
SU(2) =
{(
a b
−b a
)
: |a|2 +|b|2 = 1
}
(consisting of matrices satisfying AA∗ =I) acts isometrically on ˆC. In fact
this group is the full group of orientation-preserving isometries.
Theorem 2.14 The isometry group of ˆC in the spherical metric is given by
Isom+(S2) = SU(2)/(±I)⊂ PSL2(C).
Circles and lines. A circle C ⊂ ˆC is either a line through ∞, or an
ordinary Euclidean circle in C.
Theorem 2.15 M¨ obius transformations send circles to circles, and any two
circles are equivalent.
49

Proof 1. A circlex2 +y2 +Ax+By +C = 0 is also given byr2 +r(A cosθ+
B sinθ)+C = 0, and it is easy to transform the latter under z↦→ 1/z, which
replaces r by 1/r and θ by−θ.
Proof 2. A circle is the same, projectively, as the set of null vectors for
a Hermitian form on C2 of signature (1, 1). Any two such forms are, up to
scale, related by an element of SL 2(C).
Subgroups of SU(2). The stabilizer of an oriented circle gives a copy of
S1⊂ SU(2). For example, the stabilizer of the unit circle just corresponds
to the diagonal matrices. On the other hand, the stabilizer of ˆR corresponds
to the real unitary matrices:
K =
{(
cosθ sinθ
− sinθ cosθ
)
: θ∈ R
}
.
These matrices ﬁx±i. For example, the transformation that cyclically per-
mutes (∞, 1, 0,−1) is given by g(z) = (z− 1)/(z + 1).
Area of triangles. The geodesics onS2 are arcs of great circles. The angle
sum of a spherical triangle always exceeds π, and in fact we have:
Theorem 2.16 The area of a spherical triangle is equal to its excess angle,
α +β +γ−π.
Proof. Since the sphere has area 4 π, a lune of angle θ has area 4θ. The
three lunes coming from a given triangle T cover the whole sphere, with
points inside T and its antipode triply covered and the rest simply covered.
Thus 4π + 4 area(T ) = 4(α +β +γ).
This result is a special case of the Gauss-Bonnet formula:
2πχ(X) =
∫
X
K +
∫
∂X
k.
In the case of a polygonP , the boundary integral becomes a sum of external
angles, and in the spherical case we get area( P ) =δ(P ), where δ(P )> 0 is
the angle defect (equal to zero in the Euclidean case).
The general formula can be deduced from the constant curvature formu-
las (for K =±1) by subdivision.
Hyperbolic 3-space. Finally we note that one can identify ˆC = G/AN
with the boundary of hyperbolic 3–space H3 = G/K, where G = SL 2(C)
50

and K = SU(2). From this perspective, H3 is the space of round conformal
metrics on S2; these can be identiﬁed with certain probability measures,
which in turns are compactiﬁed by δ–functions.
Finite quotients of ˆC. The discrete subroups of Aut( ˆC) are isomorphic
to Z/n, D2n and A4, S4 and A5, which quotient orbifolds of type ( n,n ),
(2, 2,n ), (2, 3, 3), (2, 3, 4) and (2, 3, 5) respectively. These ( ai) come from
solutions to the equation ∑k
1 1/ai>k − 2.
2.3 The hyperbolic plane
We now turn to a discussion of the hyperbolic plane H ={z∈ C : Im(z)>
0}. This is the most versatile of the simply-connected Riemann surfaces.
Note that H is isomorphic to ∆, e.g. by the M¨ obius transformation z↦→
z−i
z+i which sends ( i, 0,∞) to (0 ,−1, 1). One often uses these two models
interchangeably.
First, observe that the Schwarz reﬂection principle implies:
Theorem 2.17 Every automorphism of H or ∆ extends to an automor-
phism of ˆC.
Corollary 2.18 Aut(H) corresponds to the subgroup SL2(R)⊂ SL2(C).
Proof. Suppose g(z) = (az +b)/(cz +d) preserves H. Then g preserves
∂H = ˆR = R∪{∞} , so we can assume the coeﬃcients of g are real. Then
Img(i) = Im(ai +b)(−ci +d)/|ci +d|2 = (ad−bc)/|ci +d|2> 0, so det(g)>
0. Thus we can be further rescale by 1 /
√
det(g) so that
(a b
c d
)
∈ SL2(R).
Conversely, every M¨ obius transformation represented by a matrix in SL2(R)
preserves H.
Corollary 2.19 Aut(∆) corresponds to the subgroup SU(1, 1) of isometries
of the form |Z|2 =|Z0|2−|Z1|2.
Proof. This can be deduced from the preceding result by a change of
coordinates. Note that the vectors in C2 with|Z|2 = 0 correspond to ∂∆,
and ∆ itself corresponds to the cone |Z|2< 0.
51

Corollary 2.20 The automorphism group of the disk is given by the sub-
group
Aut(∆) =
{(
a b
b a
)
: |a|2−|b|2 = 1
}
⊂ PSL2(C).
Note that these matrices satisfy AQA∗ =Q, where Q =
( 1 0
0−1
)
.
Hyperbolic geometry. The hyperbolic metric on H is given by ρ =
|dz|/ Imz =|dz|/y. On the unit disk ∆, the hyperbolic metric becomes
ρ = 2|dz|/(1−|z|2).
Theorem 2.21 Every automorphism of H is an isometry for the hyperbolic
metric.
Proof. This is clear for automorphisms of the form g(z) = az +b, and
can be easily checked by g(z) =−1/z. These two types of automorphisms
generate Aut(H).
Let⟨v,w⟩ =v0w0−v1w1. The hyperbolic distance d between two lines
Cv, Cw⊂ C2 representing points in ∆ is given, in analogy with the spherical
formula (2.1), by
cosh(d/2) =|⟨v,w⟩|
|v||w|· (2.2)
Geodesics. The geodesics for the hyperbolic metric are given by circles
orthogonal to the boundary (of H or ∆). For example, in the case of the
imaginary axis γ =iR+⊂ H, it is easy to see that the projection π : H→γ
given by π(x,y ) = (0,y ) is distance-decreasing, and so γ gives a shortest
path between any two of its points. The general case follows from this one,
since any circle orthogonal to the boundary ofH is equivalent, under Aut(H),
to γ.
These geodesics satisfy all of Euclid’s postulates except the ﬁfth. Thus
if we declare them to be straight lines, we ﬁnd:
Theorem 2.22 Euclid’s ﬁfth postulate cannot be deduced from the other
axioms of geometry.
Triangles. Gauss-Bonnet for hyperbolic triangles reads:
area(T ) =π−α−β−γ.
52

For example, anideal triangle in H has vertices at inﬁnity and internal angles
of 0. Its area is π.
Curvature. We remark that the Gauss curvature of a conformal metric
ρ(z)|dz| is readily computed in terms of the Laplacian of ρ: we have
K(ρ) =−ρ−2∆ logρ.
Note that this expression is invariant under change of coordinates, since an
analytic function satisﬁes ∆ log |f′| = 0. It is particularly easy to check
that ∆(− logy) = 1/y2, and hence K(1/y) = −1; that is, ( H,|dz|/y) has
constant curvature−1.
Classiﬁcation of isometries. Let f : H→ H be an automorphism. Then
f is an isometry, and we can deﬁne its translation distance by
τ(f) = inf
H
d(x,f (x)).
This invariant is useful for the classiﬁcation of isometries. Here are the
possibilities:
1. (Elliptic) τ(f) = 0, achieved. Then f is conjugate to a rotation ﬁxing
i, of the form (
a b
c d
)
=
(
cosθ − sinθ
sinθ cosθ
)
.
(Note that when θ =π above, the matrix is −I and so f(z) = z.) In
the disk model, we can simply conjugate so f(z) =e2iθz.
2. (Hyperbolic) τ(f) > 0. In this case τ(f) is achieved along a unique
geodesic γ⊂ H which is translated distance τ(f) by f. Up to conju-
gacy,f(z) =etz where t =τ(f).
3. (Parabolic) τ(f) = 0, not achieved. Then f is conjugate to f(z) =
z + 1.
The Schwarz Lemma. The following fundamental fact is central to the
theory of analytic maps between hyperbolic Riemann surfaces.
Theorem 2.23 Letf : ∆→ ∆ be an analytic function such that f(0) = 0.
Then either (i) f(z) =eiθz is a rotation, or (ii) |f′(0)|< 1 and|f(z)|<|z|
for all z.
Proof. Observe that by the maximum principle, the analytic function de-
ﬁned by g(z) = f(z)/z when z⁄= 0 and g(0) = f′(0) satisﬁes|g(z)|≤ 1. If
equality holds for some z, then g is constant.
53

Corollary 2.24 A holomorphic map f : ∆→ ∆ is either an isometry, or
it is a contraction for the hyperbolic metric. (This means |f′|ρ < 1 and
d(f(x),f (y))<d (x,y ) if x⁄=y.)
Remark. The Schwarz lemma, instead of Schwarz reﬂection, can also be
used to show every automorphism of H or ∆ extends to ˆC.
The hyperbolic metric on other Riemann surfaces. Now suppose,
more generally, thatX = H/Γ is a hyperbolic Riemann surface. (Almost all
Riemann surfaces are of this type — only ˆC, C, C∗ and C/Λ not hyperbolic.
In particular, every region U ⊂ C whose complement contains 2 points is
hyperbolic.)
Since ρ =|dz|/y is invariant under Aut(H), it descends to give a hyper-
bolic metric on X itself. (Also called the Poincar´ e metric.)
Example. The hyperbolic metric on the stripS ={z =x+iy : 0 <y <π}
is given by ρ =|dz|/ sin(y). Indeed, the map f(z) =ez sendsS conformally
to H, and so
ρ =f∗(|dz|/y) =|ez||dz|
Imez = ex|dz|
ex sin(y) = |dz|
sin(y).
The more general version of the Schwarz lemma then reads:
Theorem 2.25 Let f : X → Y be an analytic map between hyperbolic
Riemann surfaces. Then f is either a covering map, or it is a contraction
for the hyperbolic metric.
Proof. Pass to the universal covers of the domain and range and apply the
usual Schwarz lemma.
Proper maps. A Blaschke product B : ∆→ ∆ is a rational map of the
form
f(z) =eiθ
d∏
1
z−ai
1−aiz
with zeros satisfying |ai| < 1. Using the fact that 1 = zz on S1, it is easy
to show that|B(z)| = 1 on S1, and thus B : ∆→ ∆ is proper. Conversely,
we have:
Theorem 2.26 Every proper analytic map f : ∆→ ∆ is a Blaschke prod-
uct.
54

Proof. A proper map is surjective, so f has at least one zero, say a. Let
M(z) = (z−a)/(1−az). Then g = f(z)/M(z) : ∆→ ∆ is analytic, with
one fewer zero than f. The proof now follows by induction on the degree of
f.
Corollary 2.27 Every proper map on the unit disk extends to a rational
map on ˆC.
Remark: Dynamics and the Schwarz Lemma. Here are two sample
applications of the Schwarz lemma to iterated analytic maps.
Theorem 2.28 Letf :ˆC→ˆC be a rational map of degree d> 1. Then the
immediate basin of any attracting cycle contains a critical point.
Corollary 2.29 A rational map f of degreed has at most 2d− 2 attracting
cycles.
Theorem 2.30 (Denjoy-Wolﬀ) Let f : ∆ → ∆ be a holomorphic map
which is not conjugate to z↦→ eiθz. Then there exists a point p∈ ∆ such
that fn(z)→p for all z∈ ∆.
2.4 K¨ ahler potentials
We have seen that the spherical metric on ˆC connects with SU(2), and the
hyperbolic metric on ∆ connects with SU(1 , 1). To conclude we will brieﬂy
sketch how to make the relationship between a metric on ˆC and an inner
product on C2 more concrete.
The idea is that a suitable real–valued subharmonic function φ on a
region U⊂ˆC naturally determines a metric ρ by the equation
ρ2(z) = ∆φ(z).
(More generally, on a complex manifold one uses the symplectic form ω =
i∂∂φ and takes the associated K¨ ahler metric.)
We will be interested in the case where φ(z) = log ψ for some locally–
deﬁned functionψ. Note that if we replaceψ(z) byψ(z)|f(z)|2, wheref(z) is
holomorphic, then the value of ρ is unchanged, since log|f(z)|2 is harmonic.
Here is the construction of ρ from an inner product on C2. First, we
locally choose a section of the mapπ : C2−0→ˆC, sayZ(z) = (Z0(z),Z 1(z)).
Then, we set
ψ(z) =‖Z(z)‖2 =⟨Z(z),Z (z)⟩.
55

Finally, we set ρ2 = ∆ logψ.
Note that if we choose a diﬀerent section W (z), then it diﬀers from
the ﬁrst by a nowhere vanishing holomorphic function: W (z) = f(z)Z(z).
This changes ψ by a factor of |f(z)|2, so the value of ρ2 remains the same.
Consequently the construction is natural, and hence the orthogonal group
of the inner product maps into the isometry group of the metric.
Let us check the formula in the two main cases. In both cases we can
take Z(z) = ( z, 1). For the positive–deﬁnite inner product with ‖Z‖2 =
|Z0|2 +|Z1|2, we obtain
ρ2(z) = 4 d2
dzdz log(1 +|z|2) = 4
(1 +|z|2)2,
which agrees with our previous deﬁnition of the spherical metric. For the
indeﬁnite inner product ‖Z‖2 =|Z0|2−|Z1|2, and z in the unit disk, we
obtain
ρ2(z) = 4 d2
dzdz log(|z|2− 1) = 4
(1−|z|2)2,
also consistent with our formula for the hyperbolic metric. Note that we have
taken the logarithm of a negative quantity, consistent with our convention
that the unit disk corresponds to vectors with ‖Z‖2< 0.
2.5 Exercises
1. Prove there is no proper holomorphic map f : ∆→ C.
2. (i) Find all the proper holomorphic maps f : C∗→ C. (ii) Find all the
proper holomorphic maps g : C→ C∗.
3. Let Γ ⊂ Aut(ˆC) be a ﬁnite group. A rational map f : ˆC→ ˆC is a
quotient map for Γ if f(x) =f(y) iﬀ γ(x) =y for some γ∈ Γ.
(i) Find a quotient map for the dihedral group D2m generated by
z↦→ζmz and z↦→ 1/z, where ζm = exp(2πi/m).
(ii) Let Γ⊂ Aut(ˆC) be the subgroup leaving the set{0, 1,∞} invariant.
Give generators for Γ and ﬁnd a quotient map for Γ, normalized so
that f(∞) =∞, f(ζ6) = 0 and f(−1) = 1.
4. (i) Verify that the spherical metric ρ = 2|dz|/(1 +|z|2) is invariant
underh(z) = (z−1)/(z +1). (ii) Show that the rotations gθ(z) =eiθz,
together with h, generate the full group SU(2)/(±I)⊂ PSL2(C).
56

5. Let p(z) = a0z3 +a1z2 +a2z +a3 be a cubic polynomial. Assume
a0⁄= 0 and p′(z) has distinct zeros.
(a) Show that we can write A(p(B(z))) =C(z) =z3−3z for suitable
A,B∈ Aut C. (Hint: adjust p so its critical points are at ±1.)
(b) Show how to solve the equation z3− 3z = w by radicals, using
the fact that if z =a +a−1, then z3− 3z =a3 +a−3.
(c) Combining the previous calculations, solve the equation z3 +az +
b = 0 by radicals.
6. Find the zeros, critical points and critical values of the Chebyshev
polynomial Tn(z), n≥ 1.
7. Prove that any proper holomorphic map f : ∆→ ∆ of degree two can
be written in the form f(z) = A(S(B(z))), with A,B ∈ Aut ∆ and
S(z) =z2.
8. Consider the half-inﬁnite rectangleS ={z =x+iy :|x|< 1 and y >0}.
Give an explicit conformal map (analytic homeomorphism) from S to
the upper halfplane H.
9. (i) Give a formula for the stereographic projection z∈ C of a point on
S2 with latitude and longitude (α,β ). (ii) Find the distance between
Boston (42 N, 71 W) and Rio (23 S, 43 W), assuming the circumference
of the earth is 40,000 km.
10. Prove that any proper holomorphic map f : H→ H can be written in
the form
f(z) =a0z +b0 +
n∑
1
ai
bi−z,
with ai≥ 0 and bi∈ R.
11. Let f : ∆→ ∆ be a holomorphic map such that f(0) = 0. Prove that
eitherf is a rotation, orfn(z)→ 0 asn→∞ . (Here fn =f◦f◦···◦ f).
12. Let a,b∈ ∆⊂ P1 be represented by vectorsA,B∈ C2, and letδ be the
distance betweena andb in the hyperbolic metricρ∆ = 2|dz|/(1−|z|2).
Prove that
cosh(δ/2) = |A·B|√
|A2||B2|
,
where A·B =A0B0−A1B1, A2 =A·A, and B2 =B·B.
57

13. Let T (a,b,c )⊂ H be a hyperbolic triangle with interior angles a,b,c .
Prove that areaT (a,b,c ) =π−a−b−c as follows.
(i) Note thatT (0, 0, 0) is an ‘ideal triangle’ with all vertices at inﬁnity.
Show all ideal triangles have area π. (ii) Show geometrically that
A(a) =T (π−a, 0, 0) satisﬁes A(a +a′) =A(a) +A(a′), and conclude
A(a) =πa. (iii) Extend the sides of T (a,b,c ) to rays as below:
and use the corresponding vertices at inﬁnity to relate the area of
T (a,b,c ) to the area of T (a, 0, 0), T (b, 0, 0) and T (c, 0, 0).
14. Compute the hyperbolic metric on ∆ ∗ = ∆−{ 0}.
15. Let A(R) ={z : 1 <|z|<R}. (i) Give an explicit analytic covering
mapπ : H→A(R). (ii) Compute the hyperbolic metric on A(R). (iii)
Show that |z| =
√
R is a closed geodesic in A(R), and compute its
hyperbolic length.
16. Let f : ∆→ ∆ be an analytic map. Let fn = f◦f◦···◦ f. Show
that either f has a ﬁxed point in ∆, or |fn(z)|→ 1 for all z∈ ∆.
17. Let f : ∆→ C be an analytic function such that Re f(z)≥ 0. Show
that|f(z)|≤| f(0)|(1 +|z|)/(1−|z|).
18. Observe that any proper analytic map f : ∆→ ∆ extends to a con-
tinuous function F : ∆→ ∆. Suppose f(0) = 0. Show that for all
continuous functions φ :S1→ R, φ and φ◦F have the same average
overS1. (Hint: use the harmonic extension of φ.)
19. Let U be set of positive harmonic function u(z) on the unit disk ∆,
normalized so that u(0) = 1. Show that U is compact; that is, any
sequence has a subsequence converging uniformly on compact subsets
of ∆.
58

20. Prove that there is no conformal metric ρ = ρ(z)|dz| on ˆC that is
invariant under the full automorphism group, Aut(ˆC).
21. Pick a basis for the Lie algebra of SL 2(C), and show how each basis
element can be canonically interpreted as a holomorphic vector ﬁeld
on ˆC = PC2. Check that Lie bracket corresponds to bracket of vector
ﬁelds.
22. Let fn : ˆC→ ˆC be an unbounded sequence in Aut( ˆC). Prove that
after passing to a subsequence, there are p,q ∈ ˆC such that fn(z)→
p uniformly on compact subsets of ˆC−{q}. Give an example of a
sequence fn where p =q = 0.
23. Give an example of a sequence of degree 3 rational maps fn :ˆC→ˆC
such that fn(S1)⊂ S1, and fn(z)→ z uniformly on S1. Compute∫
S1f′
n(z)/fn(z)dz for your example.
24. A circular triangle is a region T⊂ ˆC bounded by three circular arcs
or lines. Let T1,T 2⊂ ˆC be two circular triangles with the same in-
terior angles in the same cyclic order. Prove there exists a M¨ obius
transformation sending T1 to T2.
3 Entire and meromorphic functions
This section discusses general constructions of functions on C with given ze-
ros and poles, and analyzes special cases such as the trigonometric functions
and Γ(z).
The study of zeros leads to expressions for entire functions as inﬁnite
products, and the study of poles leads to expressions for meromorphic func-
tions as inﬁnite sums.
3.1 Zeros of entire functions
An entire function is simply an analytic map f : C→ C. An entire function
has ﬁnite order if|f(z)|≤ A exp(|z|ρ) for some A,ρ≥ 0. The inﬁmum of all
suchρ is the orderρ(f).
In this section we will study the relationship between f and its set of
zeros Z(f). The latter, when inﬁnite, form a sequence an→∞ in C. The
critical exponent of an is inﬁmum of those α> 0 such that ∑ 1/|an|α<∞.
In this sum we ignore the ﬁnitely many terms where an = 0.
59

We will see that Z(f) is close to determining f provided f has ﬁnite
order. Indeed, we will be able to express f in terms of an inﬁnite product
of functions Ep(z/an), where Ep(z) is a carefully chosen entire function
vanishing only at z = 1, generalizing E0(z) = (1−z).
In summary we will show:
1. Every sequence an→∞ arises as the zero set of some entire function.
Consequently every meromorphic function on C can be written as a
ratio of two entire functions. Thus M(C) is the ﬁeld of fractions of
O(C).
2. If f(z) has order ρ, then the critical exponent of its zeros an satisﬁes
α(an)≤ρ(f).
3. Conversely, if ∑|an|p+1<∞ but∑|an|p =∞, then
P (z) =
∞∏
1
Ep(z/an)
is a function of order ρ(P ) =α(an) with the given zeros.
4. Any function f(z) of ﬁnite order can be expressed canonically as an
inﬁnite product:
f(z) =zmeQ(z)∏
Ep(z/an),
where Q(z) is a polynomial in z. (The product is ﬁnite when f is a
polynomial.) The order ρ(f) is the maximum of α(an) and the degree
of Q.
Inﬁnite products. We now turn to a detailed discussion. Our ﬁrst task is
to construct funtions with prescribed zeros as inﬁnite products. For example,
we should like to construct ‘by hand’ a function similar to sin(πz) with zeros
at the intergers Z⊂ C.
Recall that∏(1+an) converges (to an element ofC∗) if∑|an| converges.
(Note: we say ∏(1− 1/n) diverges to zero.) Similarly, ∏(1 +fn(z)) deﬁnes
an entire function on C if ∑|fn(z)| converges uniformly on compact sets.
For example, we have:
Theorem 3.1 If ∑ 1/|an| is ﬁnite, then f(z) = ∏(1−z/an) deﬁnes an
entire function with zero set Z(f) = (an).
60

Multiplicities of zeros can also be speciﬁed – they just correspond to repe-
titions of the same number in the sequence ai.
However this result is still too weak to address problem of constructing
an entire function with Z(f) = Z.
Weierstrass factors. Here is an elegant expression for an entire function
with a zero only at z = 1, which is also close to 1 for|z|< 1. It is called the
Weierstrass factor of order p:
Ep(z) = (1−z) exp
(
z + z2
2 +··· + zp
p
)
.
By convention,E0(z) = (1−z).
The idea behind this expression is that log(1/(1−z)) =z +z2/2+z3/3+
··· , and hence the two terms ‘almost cancel’ to give (1 −z)/(1−z) = 1.
(For more insight, compute the logarithmic derivativeE′
p/Ep or see the proof
below.)
Since we have truncated at the termzp, it is easy to see that for|z|< 1/2
(say) we have
|Ep(z)− 1| =O(|z|p+1).
For many purposes this bound is suﬃcient, however it is sometimes useful
to have a bound which works for all z∈ ∆ and where the implicit constant
(which might depend on p) is explicit. Such a bound is provided by:
Theorem 3.2 For|z|< 1, we have |Ep(z)− 1|≤| z|p+1.
Proof. We wish to control f(z) = 1 − Ep(z) with satisﬁes f(0) = 0,
f(1) = 1, and
f′(z) = (−E′
p(z)/Ep(z))Ep(z).
Taking the negative of the logarithmic derivative of Ep, we obtain:
−E′
p(z)/Ep(z) = 1/(1−z)− 1−z−... −zp−1 =zp/(1−z).
Hence for all z we have
f′(z) =zp exp(z +z2/2 +··· zp/p) =zp
∞∑
0
akzk,
with ak ≥ 0 for all k. Integrating term by term and using the fact that
f(0) = 0 and f(1) = 1, we ﬁnd
f(z) =zp+1
∞∑
0
bkzk
61

with bk≥ 0 and∑bk = 1. Hence for |z|< 1 we have
|f(z)|≤| z|p+1∑
bk =|z|p+1.
Theorem 3.3 For any sequence of nonzero complex numbers an → ∞,
the formula f(z) =∏∞
1 En(z/an) converges for all z and deﬁnes an entire
analytic function with zero set exactly (an).
Proof. In this and later discussions we setrn =|an|. The previous estimate
yields convergence of the tail of the series: for all z with|z|<r we have:
∑
|an|>2r
|1−En(z/an)|≤
∑
rn>2r
(r/rn)n+1≤
∞∑
1
(1/2)n+1<∞.
Corollary 3.4 Every meromorphic function on C is the ratio of two entire
functions.
Hadamard’s 3–circles theorem. The growth of an entire function is
conveniently studied in terms of the functions
M(r) = sup
|z|=r
|f(z)| and m(r) = inf
|z|=r
|f(z)|.
The following result applies not just to entire functions, but also to functions
analytic in an annulus of the form r1<|z|<r 2.
Theorem 3.5 For any analytic function f(z), the quantity logM(r) is a
convex function of logr.
Proof. A function φ(s) of one real variable is convex if and only if φ(s) +
ar satisﬁes the maximum principle for any constant a. This holds for
logM(exp(s)) by considering f(z)za locally.
62

Corollary 3.6 We have M(√rs)≤
√
M(r)M(s).
The convex functions satisfying F (logr) = logM(r) look roughly linear
for polynomials, e.g. like F (x) = deg(f)x +c, and look roughly exponential
for functions of ﬁnite order, e.g. F (x) = exp(ρ(f)x).
Functions of ﬁnite order. For the remainder of this section we will focus
on functions of ﬁnite order. We remark that the order of f is given by
ρ(f) = lim sup
r→∞
log logM(r)
logr · (3.1)
Examples: Polynomials have order 0; sin( z), cos(z) and exp(z) have order
1; cos(√z) has order 1/2; Ep(z) has order p; exp(exp(z)) has inﬁnite order.
Note that ρ(fg )≤ max{ρ(f),ρ (g)}. In fact equality holds, provided
ρ(f)⁄=ρ(g) (see bounds on the minimum modulus below). For example, if
g is a polynomial then ρ(fg ) =ρ(f). Roughly speaking, add or subtracting
ﬁnitely many zeros to f does not change its order.
To see that the functions of ﬁnite order have controlled behavior, we ﬁrst
characterize those with no zeros.
Theorem 3.7 An entire function f(z) with no zeros has ﬁnite order if and
only if f(z) = exp(Q(z)) for some polynomial Q(z); and ρ(f) = deg(Q).
To prove it we strengthen our earlier characterization of polynomials by
M(r) =O(rd).
Lemma 3.8 LetQ(z) be an entire function satisfying ReQ(z)≤A|z|d +B
for some A,B >0. Then Q is a polynomial of degree at most d.
Proof. We ﬁrst observe by the Schwarz lemma that iff : ∆(2R)→ C is an
analytic function with negative real part, then sup ∆(R)|f(z)| = O(|f(0)|).
By assumption, Q(z)−A(2R)d−B has negative real part on ∆(2R), so
sup
∆(R)
|Q(z)| =O(|R|d),
which implies that Q is a polynomial of degree at most d.
Proof of Theorem 3.7. Sincef has no zeros, f(z) =eQ(z) for some entire
function Q(z). Since f has ﬁnite order, |f(z)| = O(e|z|ρ
) for some ρ, and
thus ReQ(z)≤|z|ρ +O(1); now apply the Lemma above.
63

The critical exponent. Our next task will be to examine the zeros of
functions of ﬁnite order.
Let α denote the critical exponent of a sequence of nonzero complex
numbers an→∞ . To express α in a fashion similar to equation (3.1) for
ρ(f), we let N(r) =|{n : |an| < r}| be the counting function. Then the
critical exponent satisﬁes
α(an) = lim sup
r→∞
logN(r)
logr · (3.2)
In other words, the critical exponent is the same as the inﬁmum of those α
such that N(r) =O(rα).
For the proof of equation (3.2), it is useful to observe that, at least
formally,N′(r) = ∑δrn. Integrating by parts, we ﬁnd that for any µ≥ 0
we have: ∑
|an|−µ =
∫ ∞
0
N(r)µr−µdr
r· (3.3)
In particular, if N(r) < rβ for all r ≫ 0, then for any ϵ > 0 we have∑|an|−β−ϵ <∞, and hence α(an)≤ β. On the other hand, if N(ρi) > ρβ
i
along a sequence ρi →∞ , then we can pass to a subsequence such that
the intervals [ρi, 2ρi] are disjoint and use the equation above to show that∑|an|−β =∞, and hence α(an)≥β. This demonstrates equation (3.2).
Jensen’s formula. We can now show that the zeros of f satisfy α(an)≤
ρ(f). To this end we will use:
Theorem 3.9 (Jensen’s formula) Letf(z) be a holomorphic function on
B(0,R ) with zeros a1,...a n. Then:
avgS1(R) log|f(z)| = log|f(0)| +
∑
log R
|ai|.
Proof. We ﬁrst note that if f has no zeros, then log|f(z)| is harmonic and
the formula holds. Moreover, if the formula holds for f andg, then it holds
for fg ; and the case of general R follows from the case R = 1, since both
sides are invariant under replacing z with Rz and ai with Rai.
Next we verify that the formula holds when f(z) = (z−a)/(1−az) on
the unit disk, with |a| < 1. Indeed, in this case log |f(z)| = 0 on the unit
circle, and log|f(0)| + log(1/|a|) = log|a/a| = 0 as well.
The general case now follows, since a general function f(z) on the unit
disk can be written in the form f(z) =g(z)∏(z−ai)/(1−aiz).
64

Let A(r) denote the average of log|f(z)| overS1(r). We always have
A(r)≤ logM(r),
Then Jensen’s theorem can be restated as follows:
Corollary 3.10 We have
A(r) =
∫ r
0
N(s)ds
s + log|f(0)|. (3.4)
Integrating just over [r/2,r ] gives:
Corollary 3.11 We have N(r/2) =O(logM(r))
Corollary 3.12 For any entire functionf(z) with zeros (an), we haveα(an)≤
ρ(f).
Proof. We haveα = lim sup logN(r)/ logr≤ lim sup log logM(2r)/ log(r) =
ρ.
Behavior of the average of log|f |. By equation 3.4, the quantityN(r/2)
is a good approximation to A(r), in the sense that the two diﬀer by a factor
of at most log r.
On the other hand, A(r) is deﬁnitely only a lower bound for log M(r).
For example, when f(z) = exp(Q(z)) with Q a polynomial of degree d, we
have logM(r)≍rd, while
A(r) = avgS1(R) ReQ(z) = ReQ(0)
is constant! Since f is large over much of the circle, it must also be close to
zero somewhere on the same circle. (For example, ez is very large over half
the circle |z| = R, and very small over the rest.) This observation is the
beginning of value distribution theory .
The Hadamard factorization theorem will show that, for entire functions
of ﬁnite order, either f has a factor of exp( Q(z)), or the size of M(r) is
accounted for by the zeros of f (or both).
Canonical products. Let (an) be a sequence with critical exponent α <
∞. There is then a uniquep such that∑ 1/|an|p =∞ but∑ 1/|an|p+1<∞.
Of course p≤α≤p + 1.
The canonical product associated to an is given by
P (z) =
∏
Ep(z/an).
65

To see that it converges, setrn =|an| as usual and suppose|z|≤ r; then we
have ∑
|an|>r
|Ep(z/an)− 1|≤
∑
rn>r
|r/rn|p+1<∞.
ThusP (z) is a function of ﬁnite order whose zero set is exactly ( an). More-
over we have:
Theorem 3.13 The canonical product P (z) associated to (an) has order
ρ(f) =α(an).
Proof. Let rn =|an| and r =|z| as usual, and let log +x = max(0, logx).
Fix ϵ > 0. We wish to show that log +|P (z)| = O(rα+ϵ). Recall that
p≤α≤p + 1 and∑ 1/rp+1
n <∞.
We have seen that for|z|≤ 1 we have|1−Ep(z)|≤| z|p+1 and hence
log+|Ep(z)| =O(|z|p+1).
This shows that
∑
|an|>|z|
log+|Ep(z/an)| =O
(∑
rn>r
(r/rn)p+1
)
.
We claim the ﬁnal sum is O(rα+ϵ). This is clear if α = p + 1; otherwise
α<p + 1, and for ϵ less than the diﬀerence we have
∑
rn>r
(r/rn)p+1≤
∑
rn>r
(r/rn)α+ϵ =O(rα+ϵ),
since r/rn< 1.
Now for|z|> 1 we have
log+|Ep(z)| =O(|z|p + log+|z|) =O(|z|p+ϵ)
for any ϵ> 0. This gives
∑
|an|≤|z|
log+|Ep(z/an)| =O

∑
rn≤r
(r/rn)p+ϵ

.
Since α≥p, we have
∑
rn≤r
(r/rn)p+ϵ≤
∑
rn≤r
(r/rn)α+ϵ =O(rα+ϵ),
66

since r/rn≥ 1. Putting these two bounds together, we get
log+|P (z)| =O(rα+ϵ)
for all ϵ> 0, and hence ρ(f)≤α.
Hadamard’s factorization theorem. We can now state a formula that
describes every entire function of ﬁnite order in terms of its zeros and an
additional polynomial.
Theorem 3.14 (Hadamard) A entire function f(z)⁄= 0 of ﬁnite order ρ
can be uniquely expressed in the form:
f(z) =zm∏
Ep(z/an)eQ(z),
wherem = ord(f, 0), (an) are the other zeros of f, p≥ 0 is the least integer
such that ∑ 1/|an|p+1<∞, and Q(z) is a polynomial of degree q. We have
ρ(f) = max(q,α (an))≥p.
The number p is called the genus of f. Note that ordinary polynomials
arise as a special case, with p =q =ρ = 0.
Remark. This theorem shows that the zeros off determinef up to ﬁnitely
many additional constants, namely the coeﬃcients ofQ(z). It is tempting to
conclude then that if f(z) has no zeros, it is determined by its values at any
⌊ρ + 1⌋ points. This is not quite true, however, since f(z) only determines
Q(z) mod 2πiZ; for example, exp(2 πiz) and the constant function 1 agree
on the integers.
It is, however, true that f′/f =Q′ in this case, so knowing the logarith-
mic derivative at enough points almost determines Q. This shows:
Corollary 3.15 Supposef(z) and g(z) are entire functions of order ρ with
the same zeros, and f′/f =g′/g at⌊ρ⌋ distinct points (where neither func-
tion vanishes). Then f is a constant multiple of g.
The minimum modulus. To control the result of division by a canonical
product, we now estimate its minimum modulus. As an example — for
sin(z), we have m(r)≍ 1 for inﬁnitely many r.
Theorem 3.16 The minimum modulus of the canonical product P (z) asso-
ciated to the sequence (an) with critical exponent α satisﬁes, for each ϵ> 0,
m(r)≥ exp(−rα+ϵ)
for arbitrarily large r.
67

Proof. Fix ϵ> 0, and set log−(x) = max(0, log(1/x)). We must show that
log−m(r) =O(rα+ϵ) for arbitrarily large r.
We must be careful about which values of r to consider, since m(r) = 0
wheneverr =|an|. To this end, we ﬁxN >α and exclude from consideration
the balls Bn deﬁned by|z−an| < 1/rN
n . Since the sum of the radii of the
excluded balls in ﬁnite, there are plenty of large circles |z| =r which avoid⋃Bn.
To complete the proof, we will show that for z on such a circle of radius
r, we have log−|f(z)| =O(rα+ϵ). Our preceding arguments already control
the Weierstrass factors, so it remains to show that:
∑
|z−an|<r
log−|1−z/an| =O(rα+ϵ).
(For|z−an|≥ r we have log−|1−z/an|≥ log−1 = 0.) Note that we must
havern≤ 2r foran to appear in the sum above. Thus the number of terms
in the sum is at most N(2r). Because we have kept z away froman, we also
have
log−|1−z/an)| =O(logr).
Consequently
∑
|z−an|<r
log−|1−z/an)| =O(N(2r) logr) =O(rα+ϵ),
as desired.
Proof of the Hadamard factorization theorem. Letf(z) be an entire
function of orderρ with zeros (ai), and letP (z) be the corresponding canon-
ical product. Then P also has order ρ, as we have just seen. Since f andP
have the same zeros, the quotient f/P is an entire function with no zeros.
Thereforef/P = exp(Q(z)) for some entire functionQ(z). The lower bound
on m(r) just established implies that Re Q(z) = log|f/P| =O(|z|rho+ϵ) on
arbitrarily large circles. Using the Schwarz lemma, one can then deduce
that|Q(z)| =O(rρ+ϵ) on arbitrarily large circles. By Cauchy’s bound, Q(z)
is then a polynomial, and clearly these estimates imply that deg( Q)≤ρ.
3.2 The gamma function and trigonometric functions
There are 3 natural periodic or almost periodic zero sets whose canonical
products lead to entire functions of central importance: Z, Z⊕τ Z, and Z− =
68

{−1,−2,−3,... }. The ﬁrst and last lead to the trigonometric functions and
the gamma function, which we will discuss below. The second leads into the
theory of elliptic functions, which form the subject of a later chapter.
Trigonometric functions. As a ﬁrst application of Hadamard’s theorem,
we determine the canonical factorization of the sine function:
Theorem 3.17 We have
sin(πz)
πz =
∏
n>0
(
1− z2
n2
)
.
Proof. Indeed, the right hand side is a canonical product with p = 1; the
exponential terms for±n have cancelled. On the left hand side, sin(πz) has
order one, so the formula is correct up to a factor exp Q(z) where Q(z) has
degree one. But since sin( πz) is odd, we conclude Q has degree zero, and
by checking the value of both sides at z = 0 we get Q = 0.
Use of the logarithmic derivative. For later application, we record some
useful properties of the logarithmic derivativef′/f of an entire functionf(z).
1. We have (fg )′/fg =f′/f +g′/g.
2. If f′/f =g′/g, then f =Cg for some constant C⁄= 0.
3. We have f′(az +b)/f(az +b) =a(f′/f)(az +b).
Sine, cotangent and zeta. The product formula above gives, under log-
arithmic diﬀerentiation,
(sin(πz))′
sin(πz) =π cot(πz) = 1
z +
∞∑
1
1
z−n + 1
z +n·
This formula is useful in its own right: it showsπ cot(πz) has simple poles at
all points of Z with residue one. This property can be used, for example, to
evaluateζ(2k) =∑∞
1 1/n2k and other similar sums by the residue calculus
— see the examples in Chapter 1.
We note that the product formula for sin( z) can also be used to prove
ζ(2) =π2/6, by looking at the coeﬃcient ofz2 on both sides of the equation.
Similarly, by equating the coeﬃcients of z4,z6, etc., the sine formula shows
69

that ∑
a<b 1/(ab)2 = π4/5!, ∑
a<b<c 1/(abc)2 = π6/7!, etc., so with some
more work it can be used to evaluate ζ(2k). For example, we have
ζ(4) =
(∑ 1
a2
)(∑ 1
b2
)
− 2
(∑
a<b
1
(ab)2
)
= π4
36− π4
60 = π4
90·
Translation and duplication formulas. Many of the basic properties
of the sine and cosine functions can be derived from the point of view of
the uniqueness of an odd entire function with zeros at Zπ. For example,
equations sin(z +π) = sin(z) and sin(2z) = 2 sin(z) sin(z +π/2) hold up to
a factor of exp(az +b) as a consequence of the fact that both sides have the
same zero sets.
Boundaries. In preparation for the study of the Γ function, we remark
more generally that we have a group homomorphism
δ :M(C)∗→M (C)∗
given by
δ(f) =f(z + 1)/f(z).
Its kernel is the functions that satisfy f(z) =f(z + 1). These are all of the
form f(z) =g(exp(2πiz)), where g(z) is meromorphic.
We emphasize that δ(fg ) = δ(f)δ(g). The simplest examples are the
exponentials:
δ(az) =a.
The Γ function arises when we progress to linear polynomials and try to solve
δ(f) = z. Because we already know how to solve δ(f) = a, it suﬃces to
solve this new equation up to a constant, and then correct by an exponential
factor.
The gamma function. We now turn to a discussion of the extension of the
factorial function n↦→ n! to the complex numbers. We will describe three
approaches to Γ(z), involving (i) inﬁnite products, (ii) binomial coeﬃcients
and (iii) the Mellin transform, respectively.
Half of a trigonometric function. We begin by studying the canonical
product associated to the negative integers: namely
G(z) =
∞∏
1
(
1 +z
n
)
e−z/n.
70

It has half the terms that appear in the factorization of sin( πz); indeed, we
have
G(z)G(−z) = sin(πz)
πz · (3.5)
Euler’s constant. We haveG(0) = 1, but what is G(1)? To answer this,
we deﬁne Euler’s constant by:
γ = lim
n→∞
(1 + 2 +··· + 1/n)− log(n + 1).
This expression gives the limiting error obtained when one approximates∫n+1
1 dx/x byn unit rectangles lying above the graph of y = 1/x. (The sum
is ﬁnite because these areas can all be slid horizontally to lie disjointly inside
a ﬁxed rectangle of base one.)
Then, using the fact that (1 + 1)(1 + 1/2)··· (1 + 1/n) = (n + 1), we ﬁnd
G(1) = exp(−γ).
Functional equation. The functions G(z− 1) and zG(z) have the same
zeros. How are they related? By Hadamard’s theorem, we have G(z− 1) =
z exp(az +b)G(z) for a,b . In fact:
Theorem 3.18 We have G(z− 1) =zeγG(z).
Proof. We only know the value of G(z) at 0 and 1, making a direct calcu-
lation of the exponential factor slightly tricky. Instead, we will compare the
derivative of both sides of the equation, or rather the logarithmic derivative,
which is easier to compute.
The logarithmic derivative of zG(z) is given by:
1
z +
∞∑
1
1
z +n− 1
n,
while the logarithmic derivative of G(z− 1) is just
∞∑
1
1
z +n− 1− 1
n = 1
z− 1 +
∞∑
1
1
z +n− 1
n + 1.
Since∑∞
1 (1/n−1/(n+1)) telescopes to 1, these series are equal, and hence
G(z− 1) and zG(z) agree up to a constant. The value of this constant is
determined by setting z = 1.
71

/Minus3 /Minus2 /Minus1 1 2 3
/Minus10
/Minus5
5
10
Figure 6. The Γ function.
The Γ function. We now deﬁne
Γ(z) = 1
zeγzG(z).
Note especially that we have added a factor of exp( γz) to compensate for
the multiplicative factor of eγ. This equation is sometimes written more
explicitly as
zΓ(z) =e−γz
∞∏
n=1
(
1 +z
n
)−1
ez/n.
From the discussion above we ﬁnd:
1. Γ(z + 1) =zΓ(z); Γ(1) = 1; and hence
2. Γ(n + 1) =n! for n≥ 0; equivalently:
3. n! =nΓ(n);
4. Γ(z) has no zeros; and
5. Γ(z) has simple poles at 0, −1,−2,−3, . . . .
Using the fact that
Γ(z−n) = Γ(z + 1)
(z−n)··· (z− 1)z,
we ﬁnd
Res−n(Γ(z)) = (−1)n
n! ·
72

From (3.5) we obtain Euler’s supplement
π
sin(πz) = Γ(z)Γ(1−z),
which implies, for example:
Γ(1/2) =√π.
Variants of the sine formula are:
Γ
(1
2 +z
)
Γ
(1
2−z
)
= π
cosπz and Γ( z)Γ(−z) =− π
z sin(πz)·
Using the fact that Γ(z) = Γ(z), we ﬁnd from this last that
|Γ(iy)|2 = π
y sinh(πy)·
We also note that by the functional equation, Γ(z) has constant sign on
each interval of the form (n,n + 1); in fact the sign is positive for n> 0 and
(−1)n for n< 0.
Gauss’s formula. The formula above for the Γ function would not be easy
to discover from scratch. Here is a formula that could also be taken as a
simpler deﬁnition of the Gamma function.
Theorem 3.19 We have
Γ(z) = lim
n→∞
n!nz
z(z + 1)··· (z +n)·
As motivation, we note that for integers z we have z! = limnz(z+n
n
)−1
,
which is consistent with the formula above if we multiply both sides by z.
Indeed, formally we have
(z +n
n
)
= (z + 1)··· (z +n)
n! ≈ (n + 1)··· (n +z)
z! ≈ nz
z!,
and solving for z! =zΓ(z) and taking the limit gives the formula above.
Proof. By deﬁnition, we have:
1
Γ(z) = lim
n→∞
zeγz
n∏
k=1
(
1 +z
k
)
e−z/k.
Nowγ− 1− 1/2−···− 1/n≈− log(n), and (1 +z/k) = (k +z)/k, so this
becomes
1
Γ(z) = lim
n→∞
z(z + 1)··· (z +n)n−z
n! ,
which gives the formula above.
73

Corollary 3.20 We have|Γ(z)|≤| Γ(Rez)| for all z.
Proof. This inequality holds for each term in the product above.
This Corollary gives us good estimates on Γ( z): it is uniformly bounded
in any region of the form 0 < a <Re(z) < b, and for −n <Rez < bthe
function z(z + 1)··· (z +n)Γ(z) is uniformly bounded.
Characterizing Γ(z). In fact these properties are enough to characterize
the Γ function.
Note that exp(2πiz)Γ(z) satisﬁes the same functional equation as Γ( z),
and its reciprocal still has order 1; but it violates the growth condition. The
boundedness is also needed.
Theorem 3.21 (Wielandt) If F (z + 1) = zF (z) for Rez >0, F (1) = 1
and F (z) is bounded on the strip {z : Re z∈ [1, 2]}, then F (z) = Γ(z).
Proof. The functional equation allows one to extendF (z) to a meromorphic
function on the whole plane, whose poles and their residues agree with those
of Γ(z). Thus G(z) =F (z)−Γ(z) is entire,G(0) =G(1) = 0 andG(z +1) =
zG(z). Our boundedness assumptions now imply that G(z) =G(z + 1)/z is
bounded in the stripS ={Rez∈ [0, 1]}, since it has a removable singularity
at z = 0. Thus H(z) =G(z)G(1−z) is also bounded in S. The functional
equation for G impliesH(z + 1) =−H(z) (as in the sine formula), and thus
H is a constant, which must be zero.
A duplication formula. As an application one can prove ‘multiple angle’
formulas for Γ(nz). The simplest is:
Corollary 3.22 We have 2√πΓ(2z) = 22zΓ(z)Γ(z + 1/2).
Proof. Let F (z) = Γ( z/2)Γ(z/2 + 1/2). Then F (z + 1) = Γ( z/2 +
1/2)Γ(z/2+1) = zF (z)/2. So if write instead F (z) = 2zΓ(z/2)Γ(z/2+1/2),
thenF (z +1) = zF (z). Since F (z) is also bounded for Rez∈ [1, 2], we have
F (z) = CΓ(z) for some C; and indeed, C =F (1) = 2Γ(1/2) = 2
√
2π. The
result above now follows, upon replacing z with 2z.
The integral representation: the Mellin transform. We now turn to
a second motivation for introducing the Γ function.
74

Theorem 3.23 For Re(z)> 0, we have
Γ(z) =
∫ ∞
0
e−ttzdt
t .
In other words, Γ(z) is the Mellin transform of the function e−t on R∗.
The Mellin transform is an integral against charactersχ : R∗→ C∗ (given
byχ(t) =tz), and as such it can be compared to the Fourier transform (for
the group R under addition) and to Gauss sums. Indeed the Gauss sum
σ(χ) =
∑
(n,p)=1
χ(n)e2πin/p
is the analogue of the Gamma function for the group ( Z/p)∗.
Proof. Apply the uniqueness theorem above.
Stirling’s formula. Here is a very brief introduction to the method of
steepest descent, with the aim of explaining Stirling’s formula: as s→∞ ,
we have:
Γ(s)∼
√
2π
s
(s
e
)s
·
The idea is to model Γ(s) =
∫∞
0 e−tts−1dt by the more easily understood
Gaussian integral:
∫ ∞
−∞
ea−b(t−t0)2/2dt =ea√
2π/b,
which is itself proved using the identity
(∫ ∞
−∞
e−x2/2dx
)2
=
∫
e−r2/2rdrdθ = 2π.
To this end we rewrite Γ( s) =
∫∞
0 eφ(t)dt, where φ(t) =−t + (s− 1) logt.
Thenφ′(t) =−1+(s−1)/t vanishes att0 =s−1, withφ′′(t0) =−(s−1)/t2
0 =
−1/(s− 1). So we have
φ(t)≈φ(t0) +φ′′(t0)(t−t0)2/2 =a−b(t−t0)2/2
with a = 1−s + (s− 1) log(s− 1) and b = 1/(s− 1). This gives
Γ(s)∼e1−s(s− 1)s−1√
2π(s− 1)·
75

Using the fact that ( s− 1)s∼ ss/e and√s− 1∼√s, this gives Stirling’s
formula.
As a simple check, we note that Stirling’s formula implies:
lim (n!/nn)1/n = 1/e.
This can be seen by interpreting (1 /n)(2/n)(3/n)··· (n/n) as the exponen-
tial of an integral, and using the fact that
∫ 1
0 logxdx =−1.
The name steepest descent comes from the fact that the real axis passes
through the saddle pass of the absolute value of the integrand at its criti-
cal point, and proceeds in the direction where the absolute value decreases
fastest. Compare [MH, p. 438].
3.3 Meromorphic functions: The Mittag-Leﬄer theorem
We now turn to the problem of describing meromorphic functions with pre-
scribed principal parts. This means we specify a sequence of distinct points
an→∞ , and a ﬁnite Laurent tail
pn(z) = bk
(z−an)k +··· + b1
z−an
at each point. (The values of k and b1,...,b k depend on n.) We say pn(z)
is the principal part of a meromorphic function f(z) if f(z)−pn(z) is holo-
morphic at z =an.
Theorem 3.24 For any sequence of points an → ∞and principal parts
pn(z), there exists a meromorphic function f(z) with poles exactly at an,
and with the prescribed principal parts.
Proof. Let qn(z) be the polynomial given by truncating the power series
for pn(z) so that |pn(z)−qn(z)| < 2−n when|z| <|an|/2. Then f(z) =∑(pn(z)−qn(z)) is the desired function.
Singly-periodic functions. (This is a hint of the theory of elliptic or
doubly-periodic functions to come.)
Any meromorphic function satisfyingf(z+1) =f(z) has the formf(z) =
F (e2πiz) for some meromorphic functionF : C∗→ˆC. This leads to formulas
such as: ∞∑
−∞
1
(z−n)2 = π2
sin2(πz)·
76

Note that the right hand side is a sum of principal parts. Also, compare
this to the series for π cot(πz).
To verify this equation, ﬁrst note that|z−n|2≥| Imz|2 +n2−O(1) for
0≤ Rez≤ 1, and hence the sum on the left converges uniformly in this strip
so long as| Imz|≥ 1. Thus both sides tends to 0 as | Imz|→∞ . But their
diﬀerence is holomorphic and periodic, and so it must vanish identically.
On the other hand, by evaluating the constant term in the Laurent series
on both sides, we obtain the formula ∑∞
1 1/n2 =π2/6.
From Mittag–Leﬄer to Weierstrass. The Weierstrass Theorem — that
there exists a function g(z) with prescribed zeros — is a Corollary of the
Mittag–Leﬄer theorem (which historically came later).
Indeed, to construct an entire function with zeros of multiplicities mn
at distinct points an→∞ , we can simply ﬁrst construct a meromorphic
functionf(z) with principle part pn(z) =mn/(z−an) at an, and then take
g(z) = exp(
∫
f(z)dz). Since the residues of f(z) are integers, the integral is
only well-deﬁned modulo 2πiZ, but this is suﬃcient to make its exponential
well-deﬁned.
...this topsy–turvy way of doing things ( die Dinge auf dem Kopf
zu stellen) should be not sanctioned by anyone who sees mathe-
matics as something other than a disordered heap of mathemat-
ical results.
—A. Pringsheim, 1915.
(See [Re, p.131].)
3.4 Exercises
1. Prove that for any nonzero polynomial p(z) and any λ⁄= 0, the func-
tion f(z) =p(z)−eλz has inﬁnitely many zeros.
2. Let M(r) = sup|z|=r|f(z)| where f : C→ C is an analytic function,
not identically equal to zero. Suppose M(r2)2 =M(r)M(r3) for some
r> 0,r⁄= 1. Prove that f(z) =azn for somea⁄= 0 and integern≥ 0.
3. Prove there is no nonzero analytic function f : ∆→ ∆ with zeros at
the points an = 1− 1/(n + 1),n = 1, 2, 3, 4,... . (Thus in contrast to
f : C→ C, the zeros of a map f : ∆ → ∆ cannot be an arbitrary
discrete set. Hint: consider f(0)/Bn(0), whereBn : ∆→ ∆ is a proper
map of degree n with zeros at a1,...,a n.)
77

4. Formulate and prove an inﬁnite product formula for sin 2(√z).
5. Give an example of a canonical product f(z) = ∏∞
1 (1−z/an) that
has order exactly 1.
6. Show that if τ∈ H is ﬁxed then
θ(z) =
∞∑
n=−∞
exp(2πin2τ) exp(2πinz)
is an entire function of order 2.
7. Prove that for any sequences an,bn∈ C with an→∞ , there exists
an entire function such that f(an) =bn. (Hint: write f(z) =∑gn(z)
wheregn is a polynomial constructed by induction, such that gn(ai) =
0 for i < n, gn(an) = bn−∑n−1
1 gi(an), and |gn(z)| < 2−n when
|z|<|an|/2.)
8. Show that if f,g ∈O (C) have no common zeros, then (f,g ) = (1); i.e.
show there exist r,s∈O (C) such that fr +gs = 1.
Hint: write 1/(fg ) =F +G, where F only has poles at the zeros of f
and G has zeros only at the zeros of g. (Why is this possible?)
9. Let O(C) andM(C) be the rings of analytic and meromorphic func-
tions on C. Show thatO(C) is integrally closed inM(C). (The means
any f ∈ M(C) satisfying a monic polynomial p(X) ∈ O(C)[X] is
actually inO(C).)
IsM(C) algebraically closed?
10. Fix ρ≥ 0 and let Oρ(C) be the set of entire functions of order ≤ ρ.
Show that Oρ(C) is a ring, and that Oρ(C) is integrally closed in
M(C).
11. Prove that any ﬁnitely-generated ideal I⊂O (C) is principal.
12. Let I = (f1,f 2,... )⊂O (C) be the ideal generated by the sequence
of functions fn(z) = sin(z/n)/z. Prove that I⁄=O(C) and I is not
contained in any proper principal ideal. Conclude that O(C) is not a
PID and thatO(C) contains maximal ideals that are not of the form
(z−a).
13. Express f(z) =∑∞
n=−∞(z−n)−4 in terms of trigonometric functions,
and use your result to evaluate ∑∞
1 1/n4.
78

14. Let f(x) be a positive continuous function on R. Prove that there
exists a nonzero entire function g(z) such that 0≤g(x)<f (x) for all
x∈ R.
15. Prove there is no nonconstant analytic function f : ∆ → ∆ with
zeros at the points zn = 1− 1/(n + 1), n = 1, 2, 3,... . (Hint: con-
sider f(0)/Bn(0), where Bn(z) is a Blaschke product with zeros at
z1,...,z n.)
16. Prove:
coth(π)
17 + coth(2π)
27 + coth(3π)
37 +... = 19π7
56700.
(Hint: you may use the fact that the residue of cot(πz) coth(πz)/z7 at
z = 0 is−19π6/14175.)
17. Find the orders of the entire functions sin 2(√z) and exp(sin(z)).
18. Let f(z) be an entire function of ﬁnite order with simple zeros at the
pointsz =n +im, (n,m )∈ Z2. Show there are polynomials P andQ
such that f(z + 1) = eP (z)f(z) and f(z +i) = eQ(z)f(z). Prove that
at least one of P and Q is nonzero.
19. Show that for any α> 0 we have:
∫ ∞
0
exp(−xα)dx =α−1Γ(α−1).
(This generalizes the formula
∫∞
0 exp(−x2)dx =√π/2.)
20. State and prove an asymptotic formula for Γ ′(x) as x→ +∞ along
the real axis. (In other words, ﬁnd a more elementary function A(x)
such that Γ′(x)/A(x)→ 1.)
21. Prove or disprove: Γ ′(3/2) = 0.
22. Show that the entire function 1 /Γ(z) has order one, but there is no
constantC >0 such that 1/Γ(z) =O(exp(C|z|)).
23. Evaluate Γ(1/3)Γ(2/3). Then ﬁnd a formula for Γ(3 z) in terms of Γ
at z, z + 1/3 and z + 2/3.
24. Prove that
∫ 1
0 log Γ(t)dt = log
√
2π, using the duplication formula for
Γ(2z).
79

25. Show that for any polynomial p(z), there exists a meromorphic func-
tion f(z) such that f(z + 1) =p(z)f(z).
26. State and prove a necessary and suﬃcient condition for a meromorphic
1-formω =ω(z)dz on C to be the logarithmic derivative,ω =d logf =
f′(z)/f(z)dz, of a meromorphic function f(z).
27. Give an example of an entire function of order 1 /3.
28. Let ⟨Fp(z)⟩ be a sequence of analytic functions with Fp(1) = 0, with
no other zeros, and with Fp(z)→ 1 uniformly on compact subsets
of C−{ 1}. Let 0 ⁄= an→∞ in C. Show there exist pn such that
G(z) = ∏Fpn(z/an) converges absolutely on C, giving an analytic
function with zeros at ⟨an⟩ and nowhere else.
29. Prove Wallis’s formula
π
2 = 2· 2· 4· 4· 6· 6···
1· 3· 3· 5· 5· 7····
(Hint: use the fact that sin( π/2) = 1.)
30. Let f andg be nonconstant entire functions, and suppose that f◦g =
f. Prove that g∈ Aut(C).
31. Give an example of an entire function of ﬁnite order ρ such that
(log logM(r))/ log(r) does not converge to ρ as r→∞ .
32. Use the method of stationary phase to estimate the average value of
sin(x)100 by hand. (Do not use a calculator. The exact answer is about
1/12.)
33. Let M(x)> 0 be a continuous function on R.
(i) Prove there exists an entire function with |f(x)| > M(x) for all
x∈ R.
(ii) Prove there exists an entire function with 0 <|g(x)| < M(x) for
all x∈ R.
(iii) Prove there does not exist an entire function with |f(z)|>|z| for
all z∈ C.
34. Show there is a constant α∈ [0, 1] such that∑n
1 1/(k +α) = log(n) +
o(1).
80

4 Conformal mapping
We now turn to the theory of analytic functions as mappings. Here the
dominant operation is composition, rather than addition or multiplication.
4.1 The Riemann mapping theorem
A conformal homeomorphisms between plane domains is an isomorphism
in the category of Riemann surfaces. The ﬁrst main result classiﬁes these
domains when they are simply-connected.
Theorem 4.1 (Riemann mapping theorem) Let U ⊂ C be a simply
connected domain, other than C itself. Then there exists a conformal home-
omorphism f :U→ ∆.
The same result holds for any simply-connected region U⊂ˆC such that
|ˆC−U|≥ 1. Note that π1(U) = (1) iﬀˆC−U is connected, so the complement
is either empty, one point or a nontrivial continuum.
The conformal radius and the hyperbolic metric. Since Aut(∆) is
large, the Riemann map is not unique. It can be made unique by picking a
point p∈ ∆ and requiring f(p) = 0 and f′(p)> 0. The value of f′(p) is an
interesting invariant of (U,p ); its reciprocal is called the conformal radius
r(U,p ) of U with center p.
It is easy to show that the hyperbolic metric ρU = ρU(z)dz satisﬁes
ρU(p) = 2/r(U,p ). To check the constant, consider the case where ( U,p ) =
(∆, 0).
Examples of Riemann maps.
1. We ﬁrst note that ∆ ∼= H, e.g. by the M¨ obius transformationA(z) =
−i(z−1)/(z+1). We also remark that A :S1→ˆR becomes in angular
coordinates,
A(θ) = 2
2i
eiθ/2−e−iθ/2
eiθ/2 +e−iθ/2 = tan(θ/2).
This is the change of variables used in calculus to integrate rational
functions of sine and cosine.
2. We also remark that (∆ , 0)∼= (∆,p ), and ( H,i )∼= (H,p ), as can be
seen using the M¨ obius transformationsB(z) = (z +p)/(1 +pz) and
C(z) =az +b where p =ai +b.
3. Of course any region in ˆC bounded by a circle (or line) is also isomor-
phic to ∆.
81

4. Let L⊂ˆC be a lune – the region between two circular arcs. Apply a
M¨ obius transformation so the vertices ofL are at 0 and∞; then after
a rotation, we can assume L ={z : 0 < argz <α}, and f(z) =zπ/α
sendL to H. (This illustrates the idea that the Riemann mapU∼= ∆ is
often constructed as a composition of several simple transformations.)
5. The map f(z) =z + 1/z sends the region Ω = H− ∆ to H. This is a
particular case of a lune.
6. The map f : H→ C− [0,∞) given by f(z) =z2 is conformal.
7. The strip S ={z : 0 < Imz < π} is a lune with angle zero; it is
sent to H byf(z) =ez. The region between any two tangent circles is
isomorphic to S by a M¨ obius transformation.
This is related to the problem of extending the harmonic function
u(z) = 1 for Im z >0 and 0 for Im z <0 from S1 to ∆; we can take
u = Ref(z)/π where f : ∆→S sends±1 to the two ends of S.
8. Let us write S =S+ andS− according to the sign of Re(z). Note that
f(z) =ez sends the imaginary axis to S1. Thus f sendsS− to ∆∩ H,
and sends S+ to H− ∆. Both of these regions are lunes. The map
g(z) = (ez +e−z)/2 = cosh(z) sends f(S−) to−H and f(S+) to + H.
9. As a variation on the discussion above, we observe that f(z) = cosz
maps the half-strip T ⊂ H deﬁned by 0 < Rez < πto−H. Indeed,
cos(z) = (eiz +e−iz)/2 is simply the composition of the map z↦→eiz,
which sends T to ∆∩ H, with the map g(z) = (z + 1/z)/2.
If we reﬂect T through its sides, we obtain a tiling of C. The map
cos(z) sends half the tiles to H and the other half to −H, as can be
seen by Schwarz reﬂection.
10. One last trigonometric example: the map f(z) = sin( z) sends T =
{z∈ H : 0 < Rez <π/2} to the ﬁrst quadrant. As an alternative way
to see this, use the fact that sin( iy) = sinh(iy) and sin(π/2 +iy) =
cosh(y).
Consequently sin2(z) mapsT to H. This is consistent with the previous
example, because sin 2(z) = (1− cos(2z))/2.
11. We note that ∆ ∗ is isomorphic to C− ∆ by z↦→ 1/z. The Riemann
mapping theorem shows there is a conformal map
C− ∆→ C−K
82

for any connected set K with|K|> 1.
Univalence and compactness. To begin the proof of the Riemann map-
ping theorem, we recall a few fundamental facts.
Let us say f : U → C is univalent if f is injective and analytic. By
injectivity, its inverse is analytic, andf provides a homeomorphism between
U and V = f(U). (It need not provide a homeomorphism between their
closures.) We then have:
Lemma 4.2 Let fn : U→ C be a sequence of univalent maps, converging
locally uniformly to f :U→ C. If f is nonconstant, it too is univalent.
Proof. Suppose f(a) = f(b) with a⁄= b, but f is nonconstant. Then
g(z) =f(z)−f(b) has a zero at z =a andg(z) = limgn(z) =fn(z)−fn(b).
It follows by Rouch´ e’s theorem that for n≫ 0 we have gn(an) = 0 with
an→a. But then fn(an) =fn(b), contrary to univalence of fn.
Lemma 4.3 The space of analytic maps f : U → ∆ is compact in the
topology of locally uniform convergence.
Proof. This is a consequence of Arzela-Ascoli and the fact that |f′(z)|≤
1/d(z,∂U ) by Cauchy’s integral formula.
Lemma 4.4 If U⊂ C is simply-connected and 0⁄∈ U, then there exists a
univalent map f :U→ C such that f(z)2 =z.
Proof of the Riemann mapping theorem. Pickp∈U and letF denote
the space of univalent maps f : (U,p )→ (∆, 0). For convenience, we will
also impose the condition that f′(p)> 0.
We ﬁrst observe that F is nonempty. This is clear if U is bounded. It
is also true if U⁄= C, for in this case we can translate to 0 ⁄∈ U; then the
imageV of a particular branched of√z :U→ C is disjoint from−V , so by
composing with 1/(z−a), a∈−V , we obtain a univalent map from U to a
bounded region.
Note that if B(p,r )⊂U, then by the Schwarz lemma we have |f′(p)|≤
1/r for all f∈F . Thus M = supFf′(p) is ﬁnite. By the preceding lemmas,
the boundM is actually realized: there exists anf∈F such thatf′(p) =M.
To complete the proof, we need to show f(U) = ∆. If not, there is an
a∈ ∆−f(U). Let A : ∆→ ∆ be an automorphism such thatA(a) = 0. Let
83

s(z) =z2, and construct a branched of s−1 on the simply-connected region
A(f(U))⊂ ∆∗. Let B : ∆→ ∆ be an automorphism such that
g =B◦s−1◦A◦f :U→ ∆
satisﬁes g(p) = 0 and g′(p)> 0. Then g∈F as well.
Now notice that f = (A◦s◦B)◦g =h◦g. By construction, h : ∆→ ∆
is a proper map of degree two, with h(0) = 0. Thus |h′(0)| < 1 by the
Schwarz lemma. But g′(0) = h′(0)f′(0), so g′(0)> f′(0) = M, contrary to
the deﬁnition of M since g∈F .
Thus f must have been surjective after all, so it provides the desired
conformal map between U and ∆.
Boundary behavior and exotic domains. It is now convenient to reverse
domain and range and consider a Riemann map f : ∆→ U⊂ C. We will
investigate the question of extending f at least to a continuous map on ∂U .
To fully appreciate the power of the Riemann mapping theorem, it is
useful to contemplate how exotic target of a conformal f : ∆ → U might
be. For example, every if U is a Jordan domain, its boundary might be
fractal (like the Koch snowﬂake curve) or it might even have positive area.
On the other hand, the boundary might contain features like a comb or the
topologists sine curve, that render some boundary points inaccessible.
The next few results show that nevertheless, the Riemann map does
extend continuously to S1 = ∂∆ whenever ∂U is tame enough for this to
happen.
Jordan domains. Here is one of the main results. Recall that a compact
set J⊂ C is a Jordan curve if it is homeomorphic to a circle.
Theorem 4.5 If∂U is a Jordan curve, then any conformal map f : ∆→U
extends to a homeomorphism between ∆ and U.
Length–area. Here is the basic argument, exploiting the fact that f
stretches all directions by the same factor, |f′(z)|.
Let R(a,b ) = [0,a ]× [0,b ]⊂ C. For each y∈ [0,b ], let Ly = [0,a ]×{y}.
Then we have
Lemma 4.6 For any conformal map f : R(a,b )→ U⊂ C, there exists a
y∈ [0,b ] such that
b2 length(f(Ly))2≤ area(U) area(R).
In other words, the length of the image of some horizontal line is bounded
above by
√
area(U)a/b.
84

Corollary 4.7 If area(U) = area(R(a,b )), then the image of some horizon-
tal line is shorter in U (or at least no longer).
Proof of Lemma 4.6 The average length of f(Ly), squared, satisﬁes
(1
b
∫ b
0
length(f(Ly))dy
)2
= 1
b2
(∫
R(a,b)
|f′(z)||dz|2
)2
≤ 1
b2
∫
12
∫
|f′|2 = area(U) area(R(a,b ))
b2 ·
Since the average exceeds the minimum, the result follows.
Jordan curves. Here is a basic fact about a Jordan curve J⊂ C. Given
a,b∈J, let [a,b ]⊂J be the subarc joining these two points with smallest
diameter. Then diam[a,b ]→ 0 if|a−b|→ 0.
Proof of Theorem 4.5. Given a pointz∈∂∆, map ∆ to an inﬁnite strip,
sendingz to one end. Then there is a sequence of disjoint squares in the strip
tending towards that end. The images of these squares have areas tending to
zero, so there are cross-cutsγn⊂ ∆ enclosingz such that length(f(γn))→ 0.
Thus the endpoints of f(γn) converge to points an,bn∈J, with z∈ [an,bn]
for n≫ 0. Since diam[ an,bn]→ 0, the disk bounded by f(γn)∪ [an,bn]
shrinks to a point p, and this implies f(zn)→p wheneverzn→z in ∆.
Consequently f extends to a continuous map S1→ J with f(z) = p.
We claimf is injective. Indeed, if f(a) =f(b) for a⁄=b in S1, then we can
join a,b by an arc γ in ∆ which maps to an embedded loop f(γ) meeting
J in the single point p = f(a) = f(b). Then one of the two components
of J−{a,b} must also map to p, since f|∆ is a homeomorphism. But if f
is constant along a subarc of J, then f is constant by Schwarz reﬂection, a
contradiction.
Local connectivity. The key point in the proof above is the following
property of a Jordan domain U: if a,b ∈ ∂U are joined by a short arc
α⊂ U, then the disk cut oﬀ by α has small diameter. This principle is
called ‘short dam, small lake’.
A compact set K is locally connected if for every open set U⊂ K and
x∈U there is a connected open set with x∈V ⊂U.
Exercise. If there exists a continuous surjective map f :S1→K, then K
is locally connected.
The argument in the proof of Theorem 4.5 furnishes short cross-cuts for
any Riemann map, so it also shows:
85

Theorem 4.8 The Riemann map extends continuously to S1 iﬀ ∂U is lo-
cally connected.
Finally, using Schwarz reﬂection one has the useful statement:
Theorem 4.9 The Riemann map extends analytically across an arc α⊂S1
if f(α) is a real-analytic arc in ∂U .
The converse is almost, but not quite, true — the map f : H→ C given
by f(z) = z2 extends analytically over the real axis, but the image has an
endpoint.
Remark. The length–area method also easily shows:
Theorem 4.10 Any Riemann mapping f : ∆→ C has radial limits almost
everywhere; that is, limr→1f(reiθ) exists for almost every θ.
Proof. We may assume the image off is bounded; then
∫
|f′|2<∞, which
implies by Cauchy-Schwarz that
∫
|f′|<∞ along almost every ray.
More generally, it is known that any bounded analytic function has radial
limits a.e. By [Ko], not much more can be said — given a Gδσ set A⊂S1
of measure zero, there exists a bounded analytic function that fails to have
radial limits exactly on the setA. For Riemann mappings, radial limits exist
except outside a very small set — the exceptional set A has capacity zero
and in particular H. dim(A) = 0.
Harmonic functions and conformal maps. Recalling that if u is har-
monic andf is analytic thenu◦f is also harmonic, it is now a simple matter
to solve the Dirichlet problem (at least implicitly) on any Jordan domain.
Theorem 4.11 For any Jordan domain U⊂ C, there exists a unique map
P :C(∂U )→C(U) such that Pu|∂U =u and Pu is harmonic in U.
Proof. Letf : ∆→U be the Riemann map, and let Pu =P0(u◦f)◦f−1,
where P0 is given by the Poisson kernel on the unit disk.
It is interesting to note that analogous theorems do hold in Rn, where al-
most no conformal mappings are available. The more general results concern
elliptic boundary value problems and require new techniques.
Annuli. A domain U⊂ ˆC is an annulus if ˆC−U = K1⊔K2 has exactly
two connected components. Equivalently, π1(U) ∼= Z. Note: in general
H0(S2−U)∼=H1(U); this is an example of Alexander duality.
The standard annulus is A(R) ={z : 1 <|z|<R}. Other examples of
annuli are C∗ and ∆∗. Exercise: none of these annuli are isomorphic.
86

Theorem 4.12 The universal cover of any annulus U⊂ ˆC is isomorphic
to C or H.
Proof. We may suppose the two complementary components of U contain
0 and ∞ respectively. Then the map U ↪→ C∗ induces an isomorphism
π1(U)∼= π1(C∗)∼= Z. The universal cover of C∗ is given by π : C→ C∗,
π(z) =ez, so
V = logU =π−1(U)⊂ C
gives the universal cover of U. By the Riemann mapping theorem, V itself
is isomorphic to H or C.
Remark. Clearly U∼= ∆∗ or C∗ iﬀ one or both of its complementary com-
ponents are singletons. This can be proved e.g. by applying the removable
singularities theorem to f : ∆∗→U.
Theorem 4.13 Any annulus U is isomorphic to C∗, ∆∗, or A(R) for a
unique R> 1.
Proof. Let g : V → V denote a generator for π1(U)∼= Z acting on its
universal cover. If V ∼= C then g is conjugate to g(z) = z + 1 and we have
U∼= C/⟨g⟩∼= C∗ by the map π(z) = exp(2πiz). The same reasoning shows
U∼= ∆∗ if V ∼= H and g is parabolic.
Otherwise V ∼= H and we can assume g(z) =λz, λ> 1. This means the
core curve of U is a geodesic of length L = logλ. Then π(z) = zα maps V
to A(R) if we choose α correctly. We want π to map [1,λ ] onto the unit
circle, so we want π(λ) =λα = exp(αL) = 1; so we take α =−2πi/L. Note
that this is a purely imaginary number, so π sends R+ to the unit circle and
R− to a circle of radius R = (−1)α = exp(απi) = exp(2π2/L). (We put a
minus sign in α so that R> 1.)
Modulus of an annulus. Two natural invariants of an annulus are the
number R such that U ∼= A(R), and the hyperbolic length L of its core
geodesic. These are related by log R = 2π2/L as we have just seen. For a
direct proof, consider the metric|dz|/|z| onA(R). This makes it into a right
cylinder with height over circumference given by h/c = logR/2π. On the
other hand, the same metric makes H/(z↦→eLz) into a right cylinder with
h/c =π/L. Equating these two expressions gives the desired relation.
The quantity h/c is often called the modulus of A, written mod(A).
87

The space of all Riemann mappings. It is traditional to denote the set
of univalent mappings f : ∆→ C such that f(0) = 0 and f′(0) = 1 by S,
for schlicht (plain, simple). So
f(z) =z +a2z2 +z3z3···
We give S the topology of uniform convergence on compact sets. We will
soon show:
Theorem 4.14 The space S is compact.
As a consequence, the coeﬃcients an are bounded. The deeper Bieberbach
Conjecture, now a theorem, asserts that |an|≤ n. This is also more than
suﬃcient to show that S is compact.
Remark: no nesting. There are no nesting relations among the images
of f ∈ S; that is, the Schwarz lemma implies that if f(∆) = g(∆) then
f = g. So if f(∆) contains some points outside the unit disk, it must also
omit some points inside the unit disk.
Remark: an extremal map. The map f(z) =∑nzn =z/(1−z)2 lies in
S and maps the unit disk to the complement of the arc ( −∞,−1/4]. This
map simultaneously maximizes|an| over all maps inS, so it is in some sense
the univalent map farthest from the identity.
The mapf(z) is also closely related to the map gα(z) =zα on the upper
halfplane, at α = 2. The map sends half to the complement of [0 ,∞),
sending i to−1. Up to a M¨ obius transformation in domain and range, f
andg2 are the same. Clearly g2+ϵ is not injective, so this is on the boundary
of S.
Maps to the outside. It is somewhat easier to start with the space Σ of
all univalent maps F : ˆC− ∆→ ˆC with F (∞) = ∞, normalized so that
their Laurent series has the form:
F (z) =z +
∞∑
n=1
bn
zn·
Since F is an open mapping near ∞, the complement of its image is a
compact set K(F )⊂ C.
Example. If we set b1 = 1, and bn = 0 for n≥ 2, we get F (z) = z + 1/z
which satisﬁes K(F ) = [−2, 2].
Theorem 4.15 The area of K(F ) is given by A =π(1−∑n|bn|2).
88

Proof. Integrate FdF over the unit circle and observe that, since |dz|2 =
(−i/2)dzdz , the area A of K(F ) is given by:
A =−i
2
∫
S1
FdF =−i
2
(
1−
∑
n|bn|2
)∫
S1
dz
z =π
(
1−
∑
n|bn|2
)
.
Corollary 4.16 We have ∑n|bn|2 ≤ 1. In particular, we have |bn| ≤
1/√n.
Corollary 4.17 The space Σ is compact.
Proof. This follows from the fact that |bn|≤ 1. So if we ﬁx R >1, then
for|z|≥ R we have
|F (z)−z|≤
∑
|bn|/Rn≤ R
R− 1 <∞.
This uniform bound implies every sequence has a subsequence converging
uniformly on compact sets. As usual, univalence is also preserved in the
limit.
Remark. Little is known about optimal bounds for |bn| over Σ. It is
conjectured that|bn| =O(1/n3/4); see [CJ].
We can now use the statement |b1|≤ 1 to prove the ﬁrst case of the
Bieberbach conjecture. Note that the case of equality, we must have all other
bn = 0, and hence up to a rotation, F (z) =z + 1/z and K(F ) = [−2, 2].
Theorem 4.18 For all f∈S with have|a2|≤ 2.
Proof. We ﬁrst note that F (z) = 1/f(1/z) +a2 is in Σ. Indeed, we ﬁnd:
1/f(1/z) = z
1 +a2/z +a3/z2 +···
= z
(
1− (a2/z +a3/z2 +··· ) + (a2/z +a3/z2 +··· )2−···
)
= z−a2 + a2
2−a3
z +···
and thus F (z) has b1 = a2
2−a3. So we ﬁnd |a2
2−a3|≤ 1, which is sort of
interesting, but not what we are aiming for yet.
89

Next we use a nice trick to make f(∆) more symmetrical: we consider,
instead of f(z), the new map g(z) =
√
f(z2). This map is also in S and it
is given by
g(z) =z
√
1 +a2z2 +a3z2 +··· =z + (a2/2)z3 +···
Thus|a2/2|≤ 1 and hence|a2|≤ 2.
Corollary 4.19 S is compact.
Proof. Suppose fi∈ S and let Fi(z) = 1/f(1/z) +a2(i)∈ Σ. Pass to a
subsequence so Fi(z) converges in Σ, and so a2(i) converges. Then Gi(z) =
Fi(z)−a2(i) converges outside the disk, and hence fi(z) = 1/Gi(1/z) con-
verges on the unit disk.
Universal properties. Here is a useful geometric consequence of the
bound on a2.
Theorem 4.20 (Koebe 1/4 theorem) For anyf∈S we haveB(0, 1/4)⊂
f(∆).
Proof. Suppose p⁄∈f(∆). Note that A(z) =z/(1−z/p) has A(0) = 0 and
A′(0) = 1. Thus g(z) =A(f(z))∈S as well. But we have
g(z) = (z +a2z2 +··· )(1 +z/p +··· ) =z + (a2 + 1/p)z2 +··· ,
so 2≥|a2 + 1/p|≥| 1/p|− 2 and hence|p|≥ 1/4.
From the Koebe theorem we get an important comparison between the
hyperbolic metric ρ and the ‘1/d’ metric δ =δ(z)|dz| =|dz|/d(z,∂U ).
Corollary 4.21 The hyperbolic metric ρ(z)|dz| on a simply-connected re-
gion U⊂ C is comparable to the 1/d metric: we have ρ(z)/δ(z)∈ [1/2, 2]
for all z∈U. Equivalent, ρ(z)d(z,∂U )∈ [1/2, 2].
Proof. We will check this at a given p∈ U. Let f : (∆, 0)→ (U,p ) be a
Riemann mapping. We may suppose p = 0 and f′(0) = 1; then f∈S, and
ρU(p) = ρ∆(p) = 2. By the Schwarz lemma we have d(p,∂U )≤ 1 and by
Koebe we have d(p,∂U )≥ 1/4; hence the result.
90

Corollary 4.22 The conformal radius r of (U,p ) satisﬁes d(p,∂U )≤ r≤
4d(p,∂U ).
Comparison of S and Σ. The most important mapping in Σ is F (z) =
z + 1/z; the most important one in S is
f(z) =
∑
nzn =z d
dz
1
1−z = z
(1−z)2·
These maps are equivalent: F (z) = 1/f(1/z) + 2. We have K(F ) = [−2, 2]
and K(f) = (−∞,−1/4]. The map f(z) shows the Bieberbach conjecture
is sharp. We also note the problem with trying to ﬁnd a ‘Bieberbach con-
jecture’ for Σ: there is no map which simultaneously maximizes all the bn’s.
Indeed, by the area theorem, if b1 = 1 then the rest of the bn’s are zero.
The distortion theorems. Given f∈ S, think of f(∆) as a splattered
egg; then one ﬁnds that no matter what, the yolk f(B(0,r )), r <1, is still
good (not too distorted). For example, the curvature of f(S1(r)) is bounded
by a constant Kr independent of f. Also, f(S1(r)) is convex if r is small
enough.
Qualitative theorems of this type can be easily deduced from compact-
ness of S. The Koebe distortion theorems make these results more precise.
They state:
Theorem 4.23 For all f∈S and z∈ ∆ with|z| =r, we have
(1−r)
(1 +r)3≤|f′(z)|≤ (1 +r)
(1−r)3
and r
(1 +r)2≤|f(z)|≤ r
(1−r)2· (4.1)
The proof can be made rather conceptual. Let U ⊂ C be a proper
simply-connected region, and let f : U→ C be a univalent map. We will
use the hyperbolic metric ρ(z)|dz| on U and the Euclidean metric |dz| on
C. It is then natural to study how these metrics compare under f. To this
end we deﬁne
δ(z) = log(|f′(z)|/ρ(z))
Note that if we replace f(z) with af(z) +b, it only changes δ(z) to δ(z) +
log|a|.
91

Lemma 4.24 The gradient of δ(z) in the hyperbolic metric on U satisﬁes
|dδ|/ρ≤ 2.
Proof. We can assume U = ∆, z = 0 and f∈S by the Riemann mapping
theorem and by the observations above. Then ρ(z) = 2/(1−|z|2) is station-
ary at z = 0. Thus|dδ| =|f′′(0)|/|f′(0)| =|2a2|≤ 4. Since ρ(0) = 2 we get
the bound above.
Proof of Theorem 4.23. We continue to assume U = ∆ and f∈S. Let
D(z) = exp δ(z) =|f′(z)|/ρ(z). Integrating along the hyperbolic geodesic
from 0 to z, we ﬁnd
|δ(z)−δ(0)|≤
∫ z
0
|dδ|≤
∫ z
0
2ρ = 2d(0,r ),
and thus D(z)/D(0) ≤ exp(2d(0,r )), r = |z|. But exp( d(0,r )) = (1 +
r)/(1−r), as can be seen by using i(1−z)/(1 +z) to map to H. Thus
D(z)/D(0)≤ (1 +r)2/(1−r)2. It follows that for f∈ S, since f′(0) = 1,
we have:
|f′(z)| =|f′(z)|
|f′(0)|≤ (1 +r)2
(1−r)2· ρ(r)
ρ(0) = (1 +r)
(1−r)3·
The reverse inequality is similar: we have
|f′(z)|≥ (1−r)2
(1 +r)2· ρ(r)
ρ(0) = (1−r)
(1 +r)3·
Integrating these bounds gives (4.1).
These results also show that S is compact.
Multiply-connected regions. We brieﬂy mention one of the standard
forms for a region that has ‘more than two holes’.
Suppose U = C− (K1∪···∪ Kn), where the Ki are disjoint compact
connected sets, none of which is a single point. We then have:
Theorem 4.25 There exists a unique conformal map F : U → C of the
form F (z) =z +b1/z +··· such that K(F ) consists of n disjoint horizontal
segments.
Remark: smoothing the boundary. As a preliminary remark, we note
that by applying the Riemann mapping toˆC−Ki for eachi, one can arrange
(if desired) that each Ki is a Jordan domain with real-analytic boundary.
92

An extremal problems for slits. For the proof of Theorem 4.25, it is
useful to introduce the familyF of all univalent conformal maps f :U→ C
of the form above. We then have the following complement:
The map F maximizes Reb1(f) over all f∈F .
The proof depends on the following observations. (Cf. [Gol, V.2].)
1. The theorem is true in the case n = 1. Indeed, in this case we can
assumeU = C− ∆, and thenF = Σ, and F (z) =z + 1/z. This is the
unique map maximizing Re b1, by the area theorem.
2. For any pair of maps deﬁned near∞ byz+b1/z+... , we haveb1(f◦g) =
b1(f) +b1(g).
3. Thus the complement is also true in the case n = 1. For in this case
we can assume (after translation) that U is the image of g∈ Σ. Then
F =f◦g−1, and Reb1(F ) = Reb1(f)−b1(g) = 1− Reb1(g).
But even more is true! UnlessU is already a slit domain, Reb1(F )> 0,
by the area theorem applied to g — since|b1(g)|≤ 1.
4. Now return to the case of general U, and suppose F∈F maximizes
Reb1. We haveK(F ) =L1∪···∪ Ln. Suppose one of these components
— say L1 — is not a horizontal slit. Then we can ﬁnd a map G :
C−L1 → C− [a,b ] such that Re b1(G) > 0 by what we have just
observed. But then G◦F∈F andb1(G◦F )>b 1(F ), contrary to the
extremal property of F .
5. We should also check uniqueness. For this it is useful to think of
U as the interior of a compact, smoothly bounded domain in C, and
f1,f 2 :U→ˆC as normalized maps of the formfi(z) = 1/(z−p)+gi(z)
whose images are horizontal slit domains. Then the bounded analytic
function h(z) = f1(z)−f2(z) on U also sends each component of ∂U
into a horizontal line. Thus h(∂U ) has winding number zero about
points not on these lines, so h must be constant.
Number of moduli. The space of n-slit regions in C, i.e. those of the
form S = C−⋃n
1[zi,zi +ai] with ai∈ R, has real dimension 3 n. We can
normalize by an aﬃne transformation so the ﬁrst slit is, say, [ −2, 2]; so up
to isomorphism, the space of such slit regions has dimension 3 n− 3.
Now to take an n-connected region U and produce a slit region, we
need to choose a point p∈ U to send to inﬁnity and we need to choose a
93

‘horizontal’ direction atp. That gives 3 more real parameters. But of course
these choices are only relevant up to the action of the automorphism group
ofU, which has dimension 3, 1 and 0 for n = 1, 2 and n≥ 3. Altogether we
ﬁnd:
dn = dim {moduli space of n-connected regions}
= 3 n− 6 + dim Aut(U)
and hence d1 = 0, d2 = 1 (the modulus of an annulus), d3 = 3, d4 = 6, etc.
Rigidity. We remark that although an n-connected region U can have
automorphisms, it cannot have a positive–dimensional set thereof, whenn>
2. To see this, we can assume U is a plane region bounded by real-analytic
Jordan curves. Then dim Aut( U) > 0 would imply there is a holomorphic
vector ﬁeld v = v(z)(d/dz) on U tangent to ∂U . If v⁄= 0, then the Euler
characteristic of U can be expressed as sum of positive contributions, one
for each zero of v on ∂U or in U. But χ(U)< 0, so v = 0.
A more geometric proof can be given once one knows that U ∼= ∆/Γ
(a proof will be sketched below). Then any automorphism must be an
isometry, and hence send geodesics to geodesics. By looking at intersections
of geodesics one can easily conclude that f is the identity.
4.2 Conformal mappings of polygons
What is the conformal radius of the unit square?
To get explicit forms for Riemann mappings, it is useful to initially try
to determine, not f itself, but the deviation of f from a simpler class of
mappings. This deviation will be a form in general, so we ﬁrst make some
remarks on forms.
Let f :X→ˆC be a meromorphic function on a Riemann surface. Then
ω = df = f′(z)dz is naturally a 1-form. That is, if we change coordinates
by setting z =φ(w), then in these new coordinates we have
φ∗(df) =d(f(φ(w)) =f′(φ(w))φ′(w)dw.
We can similarly deﬁne quadratic diﬀerentials q(z)dz2 which transform by
φ∗q =q(φ(z))φ′(z)2dz2.
In more intrinsic terms, these forms are sections of the complex cotangent
bundle T∗X and its tensor product with itself.
For a meromorphic 1-form, the residue Resp(ω) is also coordinate inde-
pendent, since it can be expressed as (2 πi)−1∫
γω for a small loop around
p. Stokes’ theorem implies:
94

Theorem 4.26 (The Residue Theorem) Ifω is a nonzero meromorphic
1-form on a compact Riemann surface X, then ∑
p∈X Resp(ω) = 0.
Let’s check this in an example: if we take ω(z) = dz/P (z) where P (z)
is a polynomial of degree d≥ 2, then it says:
∑
P (z)=0
1
P′(z) = 0.
This can be veriﬁed using partial fractions: we have P (z) = ∑ai/(z−bi)
and∑ai = 0 because |P (z)| = O(|z|−2) for large z. It can also be proved
by integrating dz/P (z) around a large circle and taking the limit.
Ifω =ω(z)dz is a meromorphic 1-form on the sphere, we can set π(z) =
1/z and form π∗ω to ﬁnd:
Res∞(ω) = Res0(−ω(1/z)dz/z2).
In particular Res∞(dz/z) =−1.
Theorem 4.27 Every meromorphic 1-form on the sphere has 2 more poles
than zeros.
Proof. This is true for ω = dz/z, which has a simple poles at 0 and ∞
and no zeros. It then follows for any other 1-form η, since f = η/ω is a
meromorphic function, which must have the same number of poles as zeros.
Corollary 4.28 A holomorphic 1-form on ˆC must be zero. In particular,
if ω1 and ω2 are 1-forms with the same principal parts, then ω1 =ω2.
Remark: one forms and vector ﬁelds in higher genus. The ﬁrst
assertion can also be seen by integrating ω to obtain a global holomorphic
function onˆC. On a Riemann surface of genus g, a meromorphic 1-form has
2g− 2 more zeros than poles, and dim Ω(X) =g. The space of holomorphic
vector ﬁelds, on the other hand, satisﬁes dim Θ(ˆC) = 3, dim Θ(E) = 1 on a
torus, and dim Θ(X) = 0 in higher genus. This is because a meromorphic
vector ﬁeld has 2g− 2 more poles than zeros.
One can use the vanishing of Θ(X) is see an n-connected plane region U
has a zero-dimensional automorphism group for n⁄= 3; if not, there would
95

be a boundary-parallel holomorphic vector ﬁeld on U, but then the double
X of U would satisfy dim Θ(X)> 0; while its genus is given by g =n− 1.
Measuring distortion: the 3 great cocycles. Now let C(f) be a dif-
ferential operator that sends meromorphic functions to meromorphic forms.
We sayC is a cocycle if it satisﬁes:
C(f◦g) =C(g) +g∗C(f).
This formula implies the maps satisfying C(f) = 0 form a group.
There are 3 important cocycles in complex analysis:
1. The derivative Df(z) = logf′(z).
2. The nonlinearityNf (z)dz =dDf = (f′′/f′)(z)dz.
3. The Schwarzian derivative
Sf (z)dz2 = (Nf )′− 1
2(Nf )2 =
[(f′′
f′
)′
− 1
2
(f′′
f′
)2]
dz2.
Their values are functions, 1-forms and 2-forms respectively. The groups
they annihilate are transformations of the form f(z) =z +a, f(z) =az +b
and f(z) = (az +b)/(cz +d).
Let us check this for Sf : if f(z) = (az +b)/(cz +d) and ad−bc = 1,
then f′(z) = 1/(cz +d)2, hence Nf (z) =−2c/(cz +d), which satisﬁes
(Nf )′ = 2c2
(cz +d)2 = 1
2(Nf )2.
Higher cocycles? There are in fact operators Tdf generalizing Sf with
the property that Tdf = 0 iﬀ f is a rational map of degree d> 1. But these
cannot be cocycles, because the rational maps of degree d> 1 do not form
a group.
To get some insight into Sf (and Td), note that if f(z) = ∑aizi =
(az + b)/(cz + d), then ( cz + d)∑aizi = az + b and hence there must
be a linear relation between most of the coeﬃcients of zf (z) and f(z); in
particular, we must have
det
(
a1 a2
a2 a3
)
=a2
2−a1a3 = 0,
96

which just says that f′f′′′− (3/2)(f′′)2 vanishes. This expression is also the
denominator of Sf = (f′f′′′− (3/2)(f′′)2)/(f′)2. Simiarly a rational map of
degree two is characterized by the property that
det


a2 a3 a4
a3 a4 a5
a4 a5 a6

 = 0
at every point. It is natural to divide this expression by a3
1 just as we have
divided Sf bya2
1 = (f′)2, so we have Td(af +b) =Td(f).
The Schwarz-Christoﬀel formula. We can now use the nonlinearity to
derive a formula for the Riemann mapping to a polygonal region. It is based
on the fact that
N(zα) = (α− 1)dz
z .
Theorem 4.29 Letf : H→U be the Riemann mapping to a polygon with
verticespi, i = 1,...,n and exterior angles πµi. Then
f(z) =α
∫ dζ∏n
1(ζ−qi)µi
dζ +β,
wheref(qi) =pi.
Proof. We will show that:
Nf =
∑−µidz
(z−qi)·
We ﬁrst observe thatNf extends to a holomorphic 1-form onC−{p1,...,p n}.
This follows by Schwarz reﬂection across each complementary interval on
the real axis. These reﬂected maps gi do not agree, but they diﬀer by linear
maps: gj = Aij◦gi, and thus N(gi) = N(gj). It remains to show Nf has
simple poles with the given residues at the pi, and at inﬁnity.
Letαi = 1−µi. The idea of the proof is that f(z) behaves like (z−qi)αi
nearqi, and thus Nf has the same residue, which is αi− 1 =−µi. To check
this, we note thatg(z) = (f(z)−pi)1/αi extends by Schwarz reﬂection across
qi, to give a conformal map g(z) near qi. Then we can locally write
g(z)αi =f(z)−pi.
Taking the nonlinearity of both sides, and using the fact that the residue is
preserved under pullback, we ﬁnd Resqi(Nf ) = 1−αi =−µi.
97

Near inﬁnity,f(z) behaves like 1/z which has nonlinearity−2dz/z and
hence residue 2 at inﬁnity. This is consistent with the residue theorem,
because ∑πµi = 2π. Since a 1-form is determined by its singularities, we
have justiﬁed the formula for Nf .
Integrating, we ﬁnd
logf′ =
∑
−µi log(z−qi) +C;
by exponentiating and integrating again, we get the desired formula for f.
Two Examples. This formula explains the geometric connection between
Riemann maps to polygons and transcendental functions we have seen in
two examples, namely:
log(z) =
∫ dz
z
maps H to a bigon with external angles ofπ, namely the strips 0< Imz <π;
and
sin−1(z) =
∫ dz√
1−z2
maps H to a triangle with external angles π/2,π/2 and π, namely the half-
strip deﬁned by Imz >0,| Re(z)|<π/ 2.
Unit disk version. The key point in the proof above was that the various
results of extending f by Schwarz reﬂection through∂H agree up to compo-
sition with linear maps. The same is true if H is replaced by the unit disk.
Thus if we choose the domain of f to be ∆, with qi∈ S1, we ﬁnd exactly
the same formula for f.
Regular polygons. As a particular example, we ﬁnd:
Theorem 4.30 The map f(z) =
∫
(1−zn)−2/ndz maps the unit disk to
a regular n-gon, sending 0 to its center and the nth roots of unity to its
vertices.
Note that f′(0) = 1, and the distance from the center of the polygon to
one of its vertices is given by
Rn =
∫ 1
0
(1−zn)−2/ndz.
98

The Beta function and conformal radius. The quantity Rn can be
computed explicitly. To this end, we introduce the Euler beta-function
B(α,β ) =
∫ 1
0
uα(1−u)β du
u(1−u) = Γ(α)Γ(β)
Γ(α +β)·
It is elementary to prove the integral above satisﬁes B(α, 1) = 1 /α, and
integration by parts gives B(α,β ) = ((β− 1)/α)B(α + 1,β− 1); this easily
implies
B(α + 1,β + 1) = α!β!
(α +β + 1)! = 1
α +β + 1
(α +β
α
)−1
for integral values of α,β . We also note that |dx|/x, which appears in
the integral deﬁnition of the Γ function, is the hyperbolic metric on R+,
and|dx|/(x(1−x)) is the hyperbolic metric on (0 , 1). Note that formally
these one forms have residue 1 at the endpoints of the interval, just as
2|dx|/(1−|x|2) does on (−1, 1).
Making the substitutionu = 1−zn,du =−nzn−1dz,dz =−(1/n)u1/n−1du,
we ﬁnd
Rn = 1
n
∫ 1
0
u−2/n(1−u)1/n−1du = Γ(1− 2/n)Γ(1/n)
nΓ(1− 1/n) ·
Note thatRn→ 1 asn→∞ , since Γ(1/n)∼n, andRn< 1 by the Schwarz
lemma.
Now if we letPn be the permimeter of the polygon, thenPn = 2n sin(π/n)Rn.
But Γ(1/n)Γ(1− 1/n) =π/ sin(π/n), so we get
Pn = 2πΓ(1− 2/n)
Γ(1− 1/n)2·
Note that Pn → 2π as n→∞ , since Γ(1) = 1. The factor Pn/(2π) by
which the perimeter exceeds the perimeter of the unit circle is given by
(P3,P 4,P 5,P 6)≈ (1.461, 1.180, 1.098, 1.043).
Conformal radius of the unit square. In particular, using the fact that
Γ(1/2) =√π, the conformal radius of the unit square (sides of length 2) is
8/P4 = 4Γ[3/4]2/π3/2 = 1.078705... . (It is clear that the conformal radius
of the unit square lies between 1 and
√
2.)
Quadrilaterals. A quadrilateralQ is a Jordan domain with 4 distinguished
points on its boundary. A conformal map between quadrilaterals is required
to preserve these points as a set.
99

Theorem 4.31 Any quadrilateral is conformally equivalent to a rectangle
of the form R(a) = [0 ,a ]× [0, 1], a > 0. This rectangle is unique up to
a↦→ 1/a.
Proof. By the Riemann mapping theorem, any quadrilateral is isomorphic
to H with 4 distinguished points, q1,...,q 4∈ R. By the Schwarz-Christoﬀel
formula,f(z) =
∫∏(z−qi)−1/2dz maps H to a Euclidean rectangle, sending
qi to its vertices.
Besikovitch lemma. As an exercise, one can now use the method of
extremal length to show, for any quadrilateral Q⊂ C, we have area(Q)≥
AB where A and B are the minimum distances between opposite sides of
Q.
The Schwarzian derivative and hypergeometric functions. Just as
the nonlinearity can be used to ﬁnd a formula for the Riemann mapping to
a polygon with linear sides, the Schwarzian derivative can be used to ﬁnd
the Riemann mapping to a polygon with circular sides.
To describe a result in this direction, we ﬁrst recall that for f(z) = zα
we haveNf (z) = (α− 1)/z, and thus
Sf (z) = (Nf )′− (Nf )2
2 = 1−α2
2
dz2
z2·
The quantity 1−α2 is a version of the residue for the quadratic diﬀeren-
tial Sf (z)dz2. Now given α,β,γ there is a unique quadratic diﬀerential
with double poles at 0 , 1,∞ with the corresponding residues, and no other
singularities. It is given by
Q(α,β,γ ) = 1
2
[1−α2
z2 + 1−β2
(z− 1)2 + 1−γ2− (2−α2−β2)
z(z− 1)
]
dz2.
The third term is chosen to that Q∼ (1−γ2)/z2 as z→∞ .
Theorem 4.32 LetP be a circular triangle with interior angles πα,πβ and
πγ. Then the Riemann mapping f : H→ P sending 0, 1 and∞ to these
vertices satisﬁes Sf =Q(α,β,γ ).
Proof. By Schwarz reﬂection, Sf extends to a meromorphic quadratic
diﬀerential on ˆC whose residues at 0, 1 and∞ are determined by the angles
of P .
100

Ideal triangles. As an example, if P is an ideal triangle, then we have
Q =Q(0, 0, 0) = z2−z + 1
2z2(z− 1)2·
This diﬀerential is symmetric under the action of S3 on H, and it has zeros
at the primitive sixth roots of unity.
Second order diﬀerential equations. To ﬁnd f itself, we remark that
any function f satisfying Sf =Q can be expressed as the ratio f =u1/u2
of two independent solutions to the diﬀerential equation
u′′ + (Q/2)u = 0.
In the case at hand, these solutions in turn can be expressed in terms of
solutions to the hypergeometric equation
z(1−z)u′′ +Au′ +Bu = 0
for suitable constants A and B.
4.3 The Picard theorems
We conclude this section with two further results concerning entire functions
that can be related to geometric function theory.
Theorem 4.33 (Little Picard Theorem) An entire function f : C→ C
which omits two values must be constant.
Corollary 4.34 A meromorphic function on C can omit at most two values
on ˆC.
The Little Picard Theorem is equivalent to the assertion that there is no
solution to the equation ef +eg = 1 where f and g are nonconstant entire
functions. Similarly, it implies there is no solution to Fermat’s equation
fn +gn = 1, n≥ 3, unless the entire functions f and g are constant.
Theorem 4.35 (Great Picard Theorem) An analytic function f :U→
C takes on every value in C, with at most one exception, in every neighbor-
hood of an essential singularity p.
The ﬁrst theorem follows from the second by considering the essential
singularity at z = 0 of f(1/z). These results generalize Liouville’s theorem
and the Weierstrass-Casorati theorem respectively.
Rescaling arguments. Here is a third result that initially seems unrelated
to the ﬁrst two.
101

Theorem 4.36 (Bloch’s Theorem) There exists a universal R> 0 such
that for any f : ∆ → C with|f′(0)| = 1 , not necessarily univalent, there
is an open set U ⊂ ∆ (perhaps a tiny set near S1) such that f maps U
univalently to a ball of radius R.
Corollary 4.37 For any analytic map on ∆, the image f(∆) contains a
ball of radius R|f′(0)|.
Note that the ball usually cannot be centered at f(0); for example,
f(z) = exp(nz)/n satisﬁes f′(0) = 1 but the largest ball about f(0) = 1/n
in f(∆)⊂ C∗ has radius 1/n.
The optimal value ofR is known as Bloch’s constant. It satisﬁes 0.433<√
3/4≤R< 0.473. The best-known upper bound comes from the Riemann
surface branched with order 2 over the vertices of the hexagonal lattice.
These apparently unrelated theorems can both be proved using the same
idea. (Cf. [BD] and references therein; for another way to relate these
theorems, see [Re, Ch. 10].)
Proof of Bloch’s theorem. Givenf : ∆→ C, let
‖f′(z)‖ =‖f′(z)‖∆,C = (1/2)|f′(z)|(1−|z|2)
denote the norm of the derivative from the hyperbolic metric to the Eu-
clidean metric. By assumption, ‖f′(0)‖ = 1/2. We can assume (using
f(rz)) that f is smooth on S1; then ‖f′(z)‖ →0 as |z| →1, and thus
sup|‖f′(z)‖ is achieved at some p∈ ∆.
Now replace f with f◦r where r∈ Aut(∆) moves p to zero. Replacing
f withaf +b with|a|< 1, we can also arrange that f(0) = 0 and‖f′(0)‖ =
1; this will only decrease the size of its unramiﬁed disk. Then ‖f′(z)‖≤
‖f′(0)‖ = 1, and thus f|∆(1/2) ranges in a compact family of nonconstant
analytic functions. Thus the new f has an unramiﬁed disk of deﬁnite radius;
but then the old f does as well.
Rescaling proof of Picard’s theorem. The proof will use the following
remarkably general rescaling theorem. This argument is related to Bloch’s
proof, to Brody’s reparameterization theorem and to other results in com-
plex analysis.
Theorem 4.38 Let fn : C→ C be a sequence of nonconstant entire func-
tions. There after passing to a subsequence, there is a sequence of M¨ obius
transformationsAn and a nonconstant entire function g : C→ C such that
g = limfn◦An uniformly on compact subsets of C.
102

We note that theAn need not ﬁx inﬁnity, sofn◦An is undeﬁned at some
point pn∈ˆC, but we will have pn→∞ .
Example. Forfn(z) =zn we can take fn◦An(z) = (1 +z/n)n→ez.
Metrics. As a preliminary to the proof, for g : C→ˆC we deﬁne
‖g′(z)‖∞ = |g′(z)|
(1 +|g(z)|2),
and‖g′‖∞ = sup‖g′(z)‖ over all z∈ C. This is the norm of the derivative
from the scaled Euclidean metric ρ∞ = 2|dz| to the spherical metric. Note
that g(z) = exp(z) has ‖g′‖∞ = 1/2; a function with bounded derivative
can be rather wild.
Similarly, forg : ∆(R)→ˆC, we deﬁne
‖g′(z)‖R =|g′(z)|1−|z/R|2
1 +|g(z)|2·
This is the derivative from a suitably rescaled hyperbolic metricρR on ∆(R)
to ˆC. Clearly ρR→ρ∞ uniformly on compact sets. Its key property is that
‖(g◦A)′‖R =‖g′‖R for all A∈ Aut(ˆC) stabilizing ∆(R).
We also note that the set of maps with uniformly bounded derivatives
in one of these norms is compact.
Proof of Theorem 4.38. Let us ﬁrst consider an arbitrary nonconstant
analytic function f(z) and a radius R> 0. We claim there exists an S≥R
and an A∈ Aut(ˆC) such that g =f◦A is analytic on ∆(S), and
‖g′(0)‖S =‖g′‖S = 1.
Indeed, by replacing f with f(az +b), we can assume ‖f′(0)‖R = 1. Then
‖f′‖R≥ 1. On the other hand, the R-norm of the derivative of f tends to
zero at the boundary of ∆(R). Thus we can choose B∈ Aut(∆(R)) such
M =‖(f◦B)′(0)‖R =‖(f◦B)′‖R≥ 1.
Now just let g(z) = (f◦B)(z/M), and S =RM.
Applying this claim to fn and a sequence Rn→∞ , we obtain Sn→∞
and maps gn =fn◦An with‖g′
n(0)‖∞ = 1 and‖g′
n‖Sn≤ 1. Now pass to a
convergent subsequence.
103

To complete the proof of Picard’s theorem, we observe:
Lemma 4.39 If fn→ f and f is nonconstant, then any value omitted by
all fn is also omitted by f.
Proof of the Little Picard Theorem. Suppose if f : C→ C is non-
constant and omits 0 and 1. Then fn(z) = f 1/n
n (z) omits more and more
points on the unit circle. We can of rescale in the domain so the spherical
derivative satisﬁes‖f′
n(0)‖∞→∞ . Passing to a subsequence and reparam-
eterizing, we obtain in the limit a nonconstant entire function that omits
the unit circle. This contradicts Liouville’s theorem.
Classical proof. The classical proof of the Little Picard Theorem is based
on the fact that the universal cover of C−{ 0, 1} can be identiﬁed with the
upper halfplane.
To see this, it is useful to start by considering the subgroup Γ0⊂ Isom(∆)
generated by reﬂections in the sides of the ideal triangle T with vertices
{1,i,−1}. For example, z↦→z is one such reﬂection, sending T to−T . By
considering billiards in T , one can see that its translates tile the disk and
thusT is a fundamental domain for Γ0. Thus the quadrilateralF =T∪(−T )
is a fundamental domain for the orientation-preserving subgroup Γ ⊂ Γ0,
and the edges of−T are glued to the edges of T to give a topological triply-
punctured sphere as quotient.
Now let π : T → H be the Riemann mapping sending T to H and its
vertices to{0, 1,∞}. Developing in both the domain and range by Schwarz
reﬂection, we obtain a covering map π : ∆→ˆC−{ 0, 1,∞}.
Given this fact, we lift an entire function f : C→ C−{ 0, 1} to a map
~f : C→ H, which is constant by Liouville’s theorem.
Uniformization of planar regions. Once we know that ˆC−{ 0, 1,∞} is
uniformized by the disk, it is straightforward to prove:
Theorem 4.40 The universal cover of any region U⊂ˆC with|ˆC−U|≥ 3
is isomorphic to the unit disk.
Sketch of the proof. Consider a basepoint p in the abstract universal
coverπ : ~U→U, and letF be the family of all holomorphic maps
f : (~U,p )→ (∆, 0)
that are covering maps to their image. Using the uniformization of the
triply-punctured sphere, we have that F is nonempty. It is also a closed,
104

normal family of functions in O(~U); and by the classical square-root trick,
it contains a surjective function (which maximizes |f′(p)|). By the theory
of covering spaces, this extremal map must be bijective.
Proof of the Great Picard Theorem. Let f : ∆∗→ ˆC−{ 0, 1,∞} be
an analytic function. We will show f does not have an essential singularity
at z = 0.
Consider a loop γ around the puncture of the disk. If f sends γ to a
contractible loop on the triply-punctured sphere, then f lifts to a map into
the universal cover H, which implies by Riemann’s removability theorem
that f extends holomorphically over the origin.
Otherwise, by the Schwarz lemma, f(γ) is a homotopy class that can be
represented by an arbitrarily short loop. Thus it corresponds to a puncture,
which we can normalize to be z = 0 (rather than 1 or ∞). It follows that f
is bounded near z = 0 so again the singularity is not essential.
4.4 Exercises.
Notation as in this chapter: S denotes the space of normalized univalent
maps on ∆, Σ the space of normalized univalent maps onC−∆, andA(R) =
{z : 1 <|z|<R}.
1. Show that if f,g ∈S and f(∆) contains g(∆) then f =g.
2. Suppose f∈S satisﬁes sup∆|f(z)|≤ M. Show that|a2|≤ 2
√
1− 1/M.
(Hint: g(z) = f(z−2)−1/2∈ Σ omits the ball B(0,M−1/2) which has
area π/M.)
3. Show that if f∈ Σ and w is not in the image of f, then|w|≤ 2.
(Hint: apply the bound |b1|≤ 1 to the function
√
f(z2)−w.)
4. Prove the uniformization theorem for plane regions. That is, ﬁll in the
details of the sketch proof of the Theorem 4.40 given above.
5. Let U ⊂ C be a connected open set (which need not be simply-
connected), and let p∈U. Let F be the family of all univalent maps
f : U→ C with f(p) = 0 and f′(p) = 1. Show that F is compact in
the topology of uniform convergence on compact sets.
105

6. For a>b> 0 consider the ellipse E⊂ C with major axis [−a,a ] and
minor axis [−ib,ib ]. Let I⊂ [−a,a ] be the segment joining the foci of
E. Finally let B be the annular region between E and I.
Find an explicit conformal map f :A(R)→B for some R> 1. (Hint:
think about z + 1/z.)
7. Let B⊂ C be an annulus bounded by a pair of Jordan curves C1 and
C2. Prove that there exists an arc α⊂B joiningC1 toC2, and a loop
β⊂B separating C1 from C2, such that their lengths satisfy
L(α)L(β)≤ area(B).
(Hint: let f :A(R)→B be a conformal map from a standard annulus
to B, and consider
∫
A(R)|f′(z)|·| z|−1|dz|2.)
8. Let f : ∆→ C be analytic and suppose
∫
∆|f′(z)|2|dz| <∞. Prove
that F (z) = limr→1f(rz) exists and is ﬁnite for almost every z∈S1.
9. Give an example of a homeomorphism f : ∆ → ∆ that is distance-
decreasing for the hyperbolic metric, but does not extend continuously
to S1. (Hint: try a map of the form f(r,θ ) = (R(r),T (r) +θ), where
T (r)→∞ as r→ 1.)
10. What are the conformal radii of the following pointed regions?
(a) ( H,i );
(b) ({z : −1< Rez <1}, 0);
(c) ({z∈ H : −π <Rez <π},i );
(d) (ˆC− [−2, 2],∞); and
(e) (Sα,r ), where r> 0 and Sα ={z : arg(z)∈ (−α,α )}.
11. Let A ={z∈ S1 : Im(z)≥ 0}. Find a Riemann map f : C− ∆→
C−A.
12. Show that the set of univalent maps whose images are Jordan domains
is dense inS (in the topology of uniform convergent on compact subsets
of ∆).
13. Find a conformal homeomorphism from C− ∆ to C−E(a,b ), where
E(a,b ) is the ellipse {x +iy : x2/a2 +y2/b2≤ 1}.
106

14. Let U ⊂ C be a simply–connected region such that p = 0 ∈ U but
1⁄∈ U. Suppose that conformal radius R of (U,p ) is 2. Is U unique?
What about if R = 4?
15. Is there a univalent map f : C− ∆→ C of the form f(z) = z +∑∞
1 bn/zn with b2 = 1/
√
2?
16. Show that the set of Riemann mappings whose images are polygons is
dense in S, in the topology of uniform convergence on compact sets.
17. Let Dn be the region given by the union of the disks of radius 1 centered
at 0 and 2− 1/n. Let fn : (∆, 0)→ (Dn, 0) be the Riemann mapping,
normalized so that f′
n(0) > 0. n. Prove that fn(z) → f(z) = z
uniformly on compact subsets of ∆. In particular, the image of lim fn
is smaller than the limit of the image of fn.
18. Suppose f ∈ S satisﬁes f(iz) = if(z). Show that f(∆) contains
B(0, 1/
√
2).
19. Give an explicit bound |an| ≤Mn valid for all f ∈ S. (Use only
elementary methods, such as the area theorem or the distortion theo-
rems.)
20. Prove that the Beta function satisﬁes B(a,b ) = Γ(a)Γ(b)/Γ(a +b) for
a,b with Re a, Reb > 0. (Hint: ﬁx b and show that F (a) = Γ( a +
b)B(a,b ) satisﬁes F (a + 1) =aF (a). Use the fact that xa(1−x)b+1 =
(xa−xa+1)(1−x)b.)
21. What is the radius of the largest unramiﬁed disk for the map f : ∆→
C given by f(z) = ez2
? (Recall a disk B(p,r )⊂ C is unramiﬁed if
there is a holomorphic map h : (p,r )→ ∆ such that f(h(z)) = z for
all z∈B(p,r ).)
22. Prove the the nonlinearity Nf = d logf′ satisﬁes N(f◦g) = Ng +
g∗(Nf ). (Here g∗(Nf ) =Nf (g(z))g′(z)dz2.)
23. Prove the the Schwarzian derivativeSf = (Nf )′−(1/2)(Nf )2 satisﬁes
S(f◦g) =Sg +g∗(Sf ). (Here g∗(Sf ) =Sf (g(z))g′(z)2dz2.)
24. Let φ(z) be an analytic function, and let u1,u 2 be two linearly inde-
pendent solutions to the diﬀerential equation d2u/dz2 +φu = 0.
(i) Show W (z) = det
(u1 u2
u′
1 u′
2
)
is a constant.
107

(ii) Show that if f(z) =u1(z)/u2(z), then Sf (z) =Cφ(z) and ﬁnd C.
Why does the value of Sf not depend on the choice of u1 and u2?
25. Find a formula (which may involve an integral) for a covering map
f : H→ C−T whose image is the complement of a square T .
26. Prove that the Little Picard Theorem implies directly that there is a
constant M >0 such that any holomorphic map f : ∆→ C−{ 0, 1}
satisﬁes‖f′‖≤ M, where the derivative is measured using the hy-
perbolic metric on the domain and the spherical metric on the range.
(Hint: supposing the derivative tends to inﬁnity, construct a noncon-
stant entire function f : C→ C−{ 0, 1}.)
27. Let T⊂ R2 be a (closed) Euclidean triangle, and let G⊂ Isom(R2) be
the group generated by reﬂections in the sides of T . (i) Show that the
tilesTg ={g(T ) : g∈G} cover R2. (ii) Give an example where every
point in R2 belongs to the interior of at most one tile. (iii) Give an
example where every point in R2 belongs to the interior of inﬁnitely
many tiles. (Hint: the closure of G is a Lie subgroup of Isom( R2).)
28. Let f andg be entire functions solving Fermat’s equation,fn+gn = 1,
with n> 2. Prove that f and g are constant. (Hint: consider f/g ).
29. Let f(z) be an entire function such that f(z) is never zero and f−1(1)
is ﬁnite. Prove that f is constant.
30. Prove there is a unique quadratic diﬀerential q = q(z)dz2 with dou-
ble poles at 0 , 1,∞ with residues A,B,C respectively, and no other
singularities. (Recall if q = (a/z2 +O(1/z))dz2 then Res0(q) =a.)
5 Elliptic functions and elliptic curves
In this section we move beyond the Riemann sphere and discuss the theory
of functions on compact Riemann surfaces of genus 1. This theory can be
viewed from several diﬀerent perspectives.
1. Periodic functions. The periods of a meromorphic function f : C→ˆC
are the additive group
Per(f) ={λ∈ C : f(z +λ) =f(z)}.
Provided f is nonconstant, Per(f) is a discrete group isomorphic to
Za for some 0≤a≤ 2. We have previously discussed the case where
108

Per(f) = Z — in this case we can write f(z) =g(exp(2πiz)) for some
meromorphic function g on C∗.
A doubly–periodic function on C is a meromorphic functions such that
Λ = Per(f) has rank two. In this case we can write Λ = Zα⊕ Zβ,
and the compact parallelogram with vertices (0 ,α,β,α +β) forms a
fundamental domain for the action of Λ on C.
2. Compact tori. We also attach to Λ the compact Riemann surface
E = C/Λ, and consider doubly–periodic functions as elements of the
function ﬁeld C(E). The study of these elliptic functions is then a nat-
ural entry point into the general theory of compact Riemann surfaces.
3. Algebraic curves. For a third perspective, consider a smooth cubic
curve V ⊂ P2. It can be shown that V is topologically a torus, and
hence we expect its universal cover to be the complex plane. We can
then aim to explicitly uniformizeV by ﬁnding meromorphic functions
f,g such that
P (f,g ) = 0,
where P (x,y ) is a cubic equation deﬁning V in aﬃne coordinates.
Suitably chosens, these functions will give a covering map F : C→V
with deck group Λ, providing an explicit isomorphism between V and
C/Λ.
4. Elliptic integrals. Perhaps the most classical perspective on elliptic
functions arises from the theory of indeﬁnite integrals. Let Q(x) be a
polynomial. We can compute
∫
dx/Q(x) explicitly using partial frac-
tions; it involves logarithms, in general. Similarly, ifQ(x) is quadratic,
we can compute
∫
dx/
√
Q(x) explicitly; the solution involves the in-
verse trigonometric functions.
But what about the functionf(x) =
∫
dx/
√
Q(x) where deg(Q) = 3 or
4? In the case where Q is a quartic with real zeros, it is easy to see (by
the Schwarz–Christoﬀel formula) that the analytic continuation of f
maps H to a rectangle in the plane. In fact the same is true for cubics.
Thus the inverse off can be developed, by Schwarz reﬂection, to give
a doubly–period function. In summary, there is a close relationship
between elliptic functions and elliptic integrals.
In this section we will develop and connect all of these perspectives, starting
for concreteness with the ﬁrst.
109

5.1 Doubly–periodic functions
Let Λ⊂ C be a lattice – meaning a discrete subgroup such that E = C/Λ
is compact. Then Λ ∼= Z2 as an abstract group. We can choose a basis such
that
Λ = Zα⊕ Zβ.
Every point of E is represented by an essentially unique point in the period
parallelogram with vertices 0,α,β and α +β.
Meromorphic functionsF :E→ˆC are the same thing as doubly periodic
functions f : C→ˆC, i.e. meromorphic functions satisfying
f(z +α) =f(z +β) =f(z)
(and hence f(z +λ) = f(z) for all λ∈ Λ. For a ﬁxed Λ, these functions
form a ﬁeld, denotedM(E).
Note that E forms a group under addition, and hence E⊂ Aut(E). We
also have an involution η : E→ E given by η(z) = −z. This is the full
automorphism group of E provided Λ is not a square or hexagonal lattice.
In the latter cases, Aut(E) also contains a cyclic group Z/4 or Z/6.
Because of these automorphisms, if F ∈M (E) then so is F (−z) and
F (z +p), p∈E.
We note that a holomorphic doubly-periodic function must be constant,
by Liouville’s theorem, because the period parallelogram is compact. So to
ﬁnd other functions we must allow poles. The simplest are constructed for
eachk≥ 3 by setting
ζk(z) =
∑
Λ
1
(z−λ)k·
This sum does not quite converge for k = 2; it can be made to converge by
writing
℘(z) = 1
z2 +
∑′
Λ
1
(z−λ)2− 1
λ2·
The critical properties of ℘(z) are that is it even, and it has a unique pole
of order 2 on E.
Theorem 5.1 The Weierstrass ℘-function is doubly-periodic.
Proof. Note that ℘′(z) = −2ζ3(z) is doubly-periodic. Thus ℘(z + 1) =
℘(z) +A and℘(z +λ) =℘(z) +B for some constantsA andB. But we also
have℘(−z) =℘(z); setting z =−1/2 and−λ/2, we ﬁnd A =B = 0.
110

Figure 7. The Weierstrass ℘-function for the hexagonal lattice.
Uniformization of cubic curves. We can now state the main theorems
regarding elliptic functions.
Theorem 5.2 The map π : C→ P2 given by
π(z) = (℘(z),℘′(z))
gives an isomorphism between the Riemann surface E = C/Λ and a smooth
cubic curve of the form y2 = (4x3 +ax +b).
Theorem 5.3 The ﬁeld of all doubly-periodic functions for a given lattice
Λ satisﬁes
M(C/Λ)∼= C[x,y ]/(y2− (4x3 +ax +b)),
where (x,y ) = ( ℘,℘′). In particular, every doubly-periodic function is a
rational function of ℘ and ℘′.
We remark that any smooth cubic curve C⊂ P2 can be put into the
form above by applying a change of coordinates (an automorphism of P2).
Later, will see that every cubic curve occurs for suitable choice of Λ.
Basic properties of elliptic functions. Let f(z) be a nonconstant
doubly-period function for a lattice Λ ⊂ C with period parallelogram P .
Then f deﬁnes a meromorphic function on the compact Riemann surface
E = C/Λ. We also note that the form dz is invariant under Λ, so we also
get a meromorphic 1-form ω =f(z)dz on E. Here are some basic facts.
1. The sum of the residues of f(z)dz overE, or over points in P , is zero.
111

2. The function f has the same number of zeros as poles. The number
of each is called the degreed = deg(f).
3. If f has poles p1,...,p d and zeros a1,...,a d in E, then ∑pi =∑ai
in the group law on E.
Proofs. (1) This follows applying Stokes’ theorem to the closed formf(z)dz
onE−{p1,...,p d}, or by integratingf(z)dz around the boundary of P (we
may assume f has no poles on ∂P .)
(2) This is a general property of proper maps between Riemann surfaces.
For a direct proof, one can also apply the residue theorem to df/f.
(3) This property is special to elliptic curves. Let P = [0,α ]× [0,β ], and
assume f has no zeros or poles in P . Then we have
∑
ai−
∑
pi = (2πi)−1
∫
∂P
zf′(z)dz
f(z) ·
We wish to show that this quantity lies in Λ. The integrals over opposite
edges cancel, up to a terms of the formλ(2πi)−1∫
ef′(z)/f(z)dz withλ∈ Λ.
Since thef is periodic, it has an integral winding numberN(e) on each edge,
and these terms have the form N(e)λ∈ Λ.
We will later see that we may construct an elliptic function with given
zeros and poles subject only to constraint (3).
Pushforward. Here is another way to see property (3). Let f : E→ ˆC
be a nonconstant meromorphic function. Then f∗(dz) = 0, since Ω(ˆC) = 0.
Now choose a path C⊂ ˆC running from 0 to ∞ and avoiding the critical
values of f. Then ~C = f−1(C)⊂ E gives a collection of arcs connecting
(ai) and (pi) in pairs, which we can assume have the same indices. We then
have
0 =
∫
C
f∗ω =
∫
~C
dz =
∑
pi−ai mod Λ.
The diﬀerential equation. We can now give a cubic equation relating
x =℘(z) and y =℘′(z).
Since℘′(z) is an odd function of degree three, its zeros coincide with the
pointsE[2] of order two on E. Using our chosen basis Λ = Zα⊕ Zβ, we can
explicitly label representatives of these points:
E[2] ={0,c 1,c 2,c 3} =
{
0,α
2,β
2,α +β
2
}
.
Let ei =℘(ci).
112

We note that the critical values ei are distinct; indeed, since ℘′(zi) = 0,
the function ℘(z)−ei has a double zero at zi, so it cannot vanish anywhere
else. This shows:
The zeros of ℘′(z) coincide with the points of order two c1,c 2,c 3.
(Morally there is also a critical point at z = 0.) Consequently:
The function ℘(z)−ei has a double zero at ci and no other zeros.
(Note: it is not at all easy to say where the two zeros of ℘(z) lie, except in
the case of symmetric lattices.)
Theorem 5.4 For all z∈ C, we have
℘′(z)2 = 4(℘(z)−e1)(℘(z)−e2)(℘(z)−e3).
Proof. From what we have seen above, the two sides are doubly-periodic
functions with the same zeros and poles. Thus they are multiples of one
another. They are equal since near zero they are both asymptotic to 4 /z6.
Corollary 5.5 The map ℘ : E → ˆC presents E as a 2-sheeted covering
space of ˆC, branched over e1,e 2,e 3 and∞. It gives the quotient of E by the
involution z↦→−z.
Proof. By construction ℘ is even and 2-to-1, and we have just identiﬁed
its critical points and values.
Corollary 5.6 The map π(z) = (℘(z),℘′(z)) maps E = C/Λ bijectively to
the smooth projective cubic curve E deﬁned by
y2 = 4(x−e1)(x−e2)(x−e3).
Proof. Since E is compact, the function x =℘(z) maps E ontoˆC; and for
a given x, the two possible values of y solving the equation above are given
byy =℘′(±z).
113

A B
A B
Figure 8. Visualizing the degree two map from E to E/η∼=ˆC, where
η(z) =−z.
Power series expansion. Let O(d) ⊂ M(E) be the vector space of
doubly–periodic functions f(z) with a pole of order d at z = 0 and no
other poles. Note that such a function is uniquely determined by its Laurent
series at z = 0, up to the constant term:
f(z) = ad
zd +··· a1
z +a0 +O(z).
Theorem 5.7 We have dimO(d) =d for d≥ 1, and dimO(0) = 1.
Proof. We have a1 = 0 by applying the residue theorem to ω = f(z)dz.
Thus dimO(d)≤d. Using ℘(z) and ζk(z) we obtain the reverse inequality.
The condition ∑ Resp(fω ) = 0 for every f ∈M (X) and ω ∈ Ω(X)
holds on any compact Riemann surface X, and leads to the Riemann–Roch
theorem.
Which element ofO(2) is℘? In fact, it is the unique element witha2 = 1
and a0 =a1 = 0. This is evident from its deﬁnition, since each term in the
series for ℘(z), apart from the initial term 1 /z2, is normalized to vanish at
the origin. The fact that a0 = 0 gives rise to the fact that ∑ei = 0, as we
will see below.
The cubic made explicit. More precisely, using the expansion
1
(z−λ)2− 1
λ2 = 1
λ2
[2z
λ + 3z2
λ2 +···
]
= 2z
λ3 + 3z2
λ4 + 4z3
λ5 +··· ,
we obtain:
Theorem 5.8 The Weierstrass ℘-function is given near z = 0 by:
℘(z) = 1
z2 + 3G2z2 + 5G3z4 +··· = 1
z2 +
∞∑
1
(2n + 1)z2nGn+1
114

where
Gn =Gn(Λ) =
∑′
Λ
1
λ2n.
Corollary 5.9 We have ℘′(z)2 = 4℘(z)3−g2℘(z)−g3, where g2 = 60G2
and g3 = 140G3.
Proof. Neglecting terms of order O(z2), we have:
℘(z)3 = 1
z6 + 9G2
z2 + 15G3 and
℘′(z)2 =
(−2
z3 + 6G2z + 20G3z3 +···
)2
= 4
z6− 24G2
z2 − 80G3.
Thus 4℘(z)3−℘′(z)2 = 60G2/z2 + 140G3 +O(z2) =g2℘(z) +g3.
Corollary 5.10 We have ∑ei = 0.
Remark: other constructions of elliptic functions. To construct el-
liptic functions of degree two: if Λ = Z⊕ Zτ, one can ﬁrst sum over Z to
get:
f1(z) =
∞∑
−∞
1
(z−n)2 = π2
sin(πz)2 ;
then
f(z) =
∞∑
−∞
f1(z−nτ)
converges rapidly, and deﬁnes an elliptic function of degree two of the form
f(z) =℘(z) +C for some constant C. Similarly, if E = C∗/⟨z↦→αz⟩, with
|α|⁄ = 0, 1, then we
F (w) =
∞∑
−∞
αnw
(αnw− 1)2
deﬁnes a function on C∗ with a double pole at w = 1 satisfying F (αw) =
F (w); thus f(z) = F (ez) is a degree two doubly-periodic function for the
lattice Λ = Z2πi⊕ Z logα. (Note that z/(z− 1)2 has simple zeros at 0 ,∞
and a double pole at z = 1.)
These functions are not quite canonical; there is a choice of direction in
the lattice to sum over ﬁrst. As a consequence they agree with ℘(z) only
115

up to an additive constant. This constant is a multiple of the important
quasimodular form
G1(τ) =
∑
m
(∑
n
1
(m +nτ)2
)
.
The real case. Now suppose Λ = Zα⊕ Zβ with α∈ R+ and β∈ iR+.
Then the critical points (0 ,c 1,c 2,c 3) of ℘(z) bound a rectangle S⊂ C (see
Figure 9).
Theorem 5.11 The value ℘(z) is real if and only if z lies on one of the
vertical or horizontal lines through (1/2)Λ.
Proof. Since Λ is invariant under both negation and complex conjugation,
we have ℘(z) = ℘(z); since ℘(z) is even and periodic, more generally we
have
℘(z) =℘(λ±z)
for any λ∈ Λ. In particular, ℘ is real along the real and imaginary axes,
since these are ﬁxed underz↦→z andz↦→−z respectively. The ﬁxed loci are
invariant under translation by (1/2)Λ, so℘ is also real on all the vertical and
horizontal lines through the points of (1/2)Λ. (E.g. the locus ﬁxed by z↦→z
consists of two horizontal loops onE, becausex+β/2↦→x−β/2∼x+β/2.)
Now as z traverses∂S, it moves monotonically along ˆR passing through
∞ just once. Thus ℘ maps S bijectively to ˆR, and the same for −S. Since
℘ has degree two, there are no other preimages of ˆR.
Corollary 5.12 The map ℘|S gives the unique conformal map from S to
−H such that ℘(ci) =ei for i = 1, 2, 3 and ℘(0) =∞.
Proof. The region S is a component of the complement of ℘−1(ˆR), con-
taining no critical points of ℘, so it maps homeomorphically to H or−H. In
fact the image is −H because Im℘(z)∼ Im 1/z2< 0 for small z in S.
Theorem 5.13 Any branch f : (±H)→ C of ℘−1 satisﬁes
f(z) =
∫ dζ√
4ζ3−g2ζ−g3
·
116

α+β
0 c 1
2c 3c
α
β
Figure 9. The shaded rectangles map under ℘ to H; the unshaded ones, to
−H.
Proof. If ζ = ℘(z) then f(ζ) = z, and hence f′(℘(z))℘′(z) = 1. Conse-
quently
f′(ζ) = 1
℘′(z) = 1√
4℘(z)3−g2℘(z)−g3
= 1√
4ζ3−g2ζ−g3
·
Thus the theory of elliptic functions emerges as the special case of the
Schwarz-Christoﬀel formula giving the Riemann map for a rectangle.
/Minus2 /Minus1 1 2
/Minus4
/Minus2
2
4
Figure 10. The elliptic curve y2 = 4x3− 8x + 2.
Location of roots. Note that the argument shows the roots of 4x3−g2x−
g3 = 0 are real, and satisfy e2 < e3 < e1. We also note that ℘′(z)∈ R
along the horizontal lines forming ℘−1(R), and ℘′(z)∈iR along the vertical
117

lines, since ℘ most rotate the latter by 90 ◦ to make them real. Thus only
the horizontal lines map to the real points of the cubic y2 = 4x3−g2x−g3.
Periods. This picture makes clear the close relationship between the gen-
erators α,β of Λ and the cubic polynomial
4x3−g2x−g3 = 4(x−e1)(x−e2)(x−e3);
namely, we have
α
2 =
∫ ∞
e1
(4x3−g2x−g3)−1/2dx =
∫ e3
e2
(4x3−g2x−g3)−1/2dx,
and
β
2i =
∫ e2
−∞
(g3 +g2x− 4x3)−1/2dx =
∫ e1
e3
(g3 +g2x− 4x3)−1/2dx.
In all 4 integrals we take the positive square-root; thus, these are simply
integrals of|(℘′)−1(x)|.
In each case, the fact that the two integrals agree follows from Cauchy’s
theorem (applied to two homotopic loops in C−{e1,e 2,e 3}), or via a change
of variables coming from a M¨ obius transformation that swaps one interval
for the other.
More generally, we have:
Theorem 5.14 The lattice Λ with invariants g2 and g3 is generated by the
values of
±
∫
γ
dz√
4z3−g2z−g3
,
whereγ ranges over all oriented loops in C which enclose exactly two roots
of the cubic in the denominator.
The condition on the roots insures that the integrand can be deﬁned
continuously on a neighborhood of γ.
Evaluation of g2 and g3. The preceding formula sometimes permits the
evaluation of g2 and/or g3. For example, we have
140
∑′
Z[ρ]
λ−6 = 4
(∫ ∞
1
dx√
x3− 1
)6
= 256π3Γ[7/6]6
Γ[2/3]6 ·
This follows from the fact that for Λ = Z[ρ], we have g2 = 0 and g3 > 0
satisﬁes
1
2 =
∫ ∞
e1
dx√
4x3−g3
,
118

where e1 = (g3/4)1/3. Similarly, we have
60
∑′
λ∈Z[i]
λ−4 = 4
(∫ ∞
1
dx√
x3−x
)4
= 64π2Γ[5/4]4
Γ[3/4]4 ·
Function ﬁelds. We now return to the case of general elliptic curves.
Theorem 5.15 The function ﬁeld of E = C/Λ is generated by x = ℘ and
y =℘′; more precisely, we have
M(E) = C(x,y )/(y2− 4x3 +g2x +g3).
Proof. To see that ℘ and ℘′ generateM(E) is easy. Any even function
f :E→ˆC factors through℘: f(z) =F (℘(z)), and so lies in C(℘). Any odd
function becomes even when multiplied by ℘′; and any function is a sum of
one even and one odd.
To see that the ﬁeld is exactly that given is also easy. It amounts to
showing thatM(E) is of degree exactly two over C(℘), and ℘ is transcen-
dental over C. The ﬁrst assertion is obvious (else ℘ would be constant), and
if the second fails we would haveM(E) = C(℘), which is impossible because
℘ is even and ℘′ is odd.
The addition law on an elliptic curve. Consider the curve E ⊂ P2
deﬁned by y2 = 4x3−g2x−g3 and parameterized by the Weierstrass ℘-
function via (x,y ) = (℘(z),℘′(z)).
Theorem 5.16 For any line L, the intersection L∩E ={a,b,c} where
a +b +c = 0 on E = C/Λ.
Proof. The intersection L∩E is simply the zero set of A℘′ +B℘ +C for
some (A,B,C ). This function has all its poles at z = 0. Since the sum of
the zeros and poles is zero, its zeros ( a,b,c ) also sum to zero.
Corollary 5.17 For any z,w ∈ C we have
⏐⏐⏐⏐⏐⏐⏐⏐
1 1 1
℘(−z) ℘(−w) ℘(z +w)
℘′(−z) ℘′(−w) ℘(z +w)
⏐⏐⏐⏐⏐⏐⏐⏐
= 0.
119

Corollary 5.18 The map p↦→−p on E is given by (x,y )↦→ (x,−y).
Proof. Then the line passes through∞ which is the origin of E, consistent
with the equation p + (−p) + 0 = 0. (Alternatively, observe that x = ℘(z)
is even and y =℘(z) is odd.)
Corollary 5.19 The pointc =a+b is constructed geometrically by drawing
the lineL through (a,b ), ﬁnding its third point of intersection (−c) = (x,−y)
on E and then negating to get c = (x,y ).
Corollary 5.20 The point 2a can be constructed by taking the line tangent
to E at a, ﬁnding its other point of intersection with E, and then negating
its y coordinate.
Figure 11. Image of 2−5Λ under ℘, for Λ = Z[i] and Z[ρ].
Dynamics of rational maps. There is a rational function f(z) such that
℘(2z) =f(℘(z)).
The preimages of the critical points off lie along the images of the horizontal
and vertical lines in C under ℘, so they give a way of visualizing the ℘
function. For more details, see [Mil2].
An elliptic function with given poles and zeros. It is natural to try
to construct an elliptic function by forming the Weierstrass product for the
lattice Λ:
σ(z) =z
∏′
Λ
(
1− z
λ
)
exp
(z
λ + z2
2λ2
)
.
120

Then (logσ)′′ =−℘(z), which is doubly–periodic, from which it follows that
σ(z +λ) =σ(z) exp(aλ +bλz)
for some aλ,bλ∈ C. (In fact this also follows directly from the Hadamard
theory, because both sides are of order 2 and have the same zeros.) From
this it is easy to see that
σ(z−a1)...σ (z−an)
σ(z−p1)...σ (z−pn)
deﬁnes an elliptic function whenever ∑ai =∑pi. This demonstrates:
Theorem 5.21 A divisor D =∑ai−∑pi onE is principal (it arises from
a meromorphic function) iﬀ degD = 0 and∑(ai−pi) = 0 in the group law
on E.
5.2 Aside: Conics and singly-periodic functions
As a point of reference, we describe the parallel theory for conics and rank
one lattices in C.
Let Λ⊂ C be a discrete subgroup isomorphic to Z. Then we can rescale
so Λ = Z, and form, for k≥ 2, the singly-periodic functions
Zk(z) =
∞∑
−∞
1
(z−n)k
and the function
P (z) = 1
z +
∞∑′
−∞
1
(z−n)− 1
n·
Note that we have the Laurent series (with ζ(0) =−1/2),
P (z) = 1
z−z
∑′ 1
n2−z3∑′ 1
n4−··· = 2
z
∞∑
0
ζ(2k)z2k,
i.e. the coeﬃcients of P (z) carry interesting invariants of the lattice Λ = Z.
We then ﬁnd:
Theorem 5.22 The map P : C/Z→ˆC−(±πi) is an isomorphism, sending
[0, 1] to [∞,−∞].
121

Proof. As we have seen,
P (z) =π cotπz =πie2πiz + 1
e2πiz− 1 =A(e2πiz),
where A(z) =πi(z + 1)/(z− 1) sends the omitted values 0 and ∞ for e2πiz
to±i.
Just as we did for elliptic functions, we next note that the power series
P (z) = 1
z− π2z
3 +···
gives
−P′(z) = 1
z2 + π2
3 +··· and P (z)2 = 1
z2− 2π2
3 +···
yielding the diﬀerential equation
−P′(z) =P (z)2 +π2.
Here we have used the fact that both P (z) and P′(z) are bounded as
| Imz|→∞ . Put diﬀerently, we have:
Theorem 5.23 The map π : C→ P2 given by
π(z) = (x,y ) = (P (z),−P′(z))
gives an isomorphism between the C/Z∼= C∗ and the smooth projective conic
deﬁned by y =x2 +π2 with two points removed.
The omitted values on the parabola y =x2 +π2 are y = 0, where x =±iπ.
We could also verify the ﬁnal identity using the fact that
−P′(z) = π2
sin2πz·
The fundamental period of Λ can now be expressed as
∫ ∞
−∞
dx
y =
∫ ∞
−∞
dx
π2 +x2 =
∫ 1
0
dz = 1.
I.e. the change of variables x = P (z) transforms the integrand into the
standard form dz on C/Z.
Remark. Any smooth conic in P2 is equivalent to the parabola above, so
we have uniformized all conics. The familiar conics x2 +y2 = 1,x2−y2 = 1
and xy = 1 are isomorphic to C/2πZ or C/2πiZ, and are uniformized by
(cos(t), sin(t)), (cosh(t), sinh(t)) and (et,e−t) respectively. Note that all 3
curves have, over C, two asymptotes, corresponding to the ends of C∗.
122

5.3 Moduli spaces and elliptic curves
We now turn to an important complement to the results above.
Theorem 5.24 Suppose the cubic polynomial 4x3+ax+b has distinct roots.
Then there exists a lattice Λ such that (x,y ) = (℘(z),℘′(z)) satisﬁes y2 =
4x3 +ax +b.
Corollary 5.25 Any smooth cubic curve in P2 is isomorphic to C/Λ for
some Λ⊂ C.
Moduli spaces. To approach this ‘metatheory’ of doubly-periodic func-
tions — where the lattice is not ﬁxed but allowed to vary — it is useful to
discussM1, the moduli space of lattices, and the Teichm¨ uller spaceT1∼= H
of marked lattices.
As a set, we let
M1 ={all lattices Λ⊂ C}/(Λ∼αΛ)
denote the space of lattices up to similarity. By associating to Λ the complex
torus E = C/Λ, we ﬁnd
M1 ={all Riemann surfaces of genus one}/(isomorphism).
This is because any isomorphism E1∼=E2 lifts to an automorphism f(z) =
αz +β of the universal cover C.
There is a natural map π : H→M 1, given by
π(τ) = [Z⊕ Zτ]∈M 1.
This map is surjective, since Zα⊕Zβ∼ Z⊕Z(β/α). We can think of a point
τ∈ H as providing both a lattice Λ = Z⊕ Zτ and a marking isomorphism,
φ : Z2→ Λ,
coming from the basis (τ, 1). All other bases for Λ with the same orientation
as this one are given by ( aτ +b,cτ +d), where g =
(a b
c d
)
∈ SL2(Z). The
marked lattice with this new basis is equivalent to ( g(τ), 1) where
g(τ) = aτ +b
cτ +d·
Thus forgetting the marking altogether is the same as taking the quotient
of H by the action of all g∈ SL2(Z), and hence:
123

Theorem 5.26 The moduli spaceM1 is naturally isomorphic to the com-
plex orbifold H/ SL2(Z).
Here SL 2(Z) acts by M¨ obius transformations. The quotient is an orbifold
because the action is not quite free, e.g. τ↦→− 1/τ ﬁxes τ =i.
Lie groups approach. More generally, we can specify a marked lattice
Λ⊂ Rn, normalized so Rn/Λ has volume one, by a linear map
T : Zn→ Λ⊂ Rn
withT∈ SLn(R). Two such lattices are similar iﬀ they diﬀer by a rotation,
i.e. T1 =R◦T2 where R∈ SOn(R). Thus the Teichm¨ uller space of lattices
in Rn is the homogeneous space
H = SOn(R)\ SLn(R).
Forn = 2 we haveH∼= H because SO2(R) is the stabilizer of τ =i for the
usual action of SL 2(R) on H.
FinallyT1(Zn) =T2(Zn) iﬀT1◦T−1
2 gives an isomorphism of Zn to itself,
which shows
Theorem 5.27 The moduli space of lattices in Rn is isomorphic to
L(Rn) = SOn(R)\ SLn(R)/ SLn(Z).
Fundamental domains. We can always normalize a lattice Λ by C∗ so
that its shortest nonzero vector is z = 1 and the shortest vector in Λ− Z is
τ∈ H. Then|τ|≥ 1, and Z +τ⊂ Λ so| Reτ|≤ 1/2. Moreover Z⊕ Zτ = Λ;
otherwise there would be a vector v∈ Λ− R of the form v = a +bτ with
a,b∈ [0, 1/2]; but then
|v|< 1/2 +|τ|/2≤|τ|,
contrary to our assumption that the shortest vector in Λ− Z has length|τ|.
The converse holds as well, and we have:
Theorem 5.28 The region | Reτ|≤ 1/2,|τ| > 1 in H is a fundamental
domain for the action of SL2(Z) on H.
The subgroup Γ(2). To studyM1 further, we now introduce the space
of cross-ratios
~M0,4 =ˆC−{ 0, 1,∞}
124

and its quotient orbifold
M0,4 = ~M0,4/S3.
Here ~M0,4 is the moduli space of ordered quadruples of distinct points onˆC,
up to the action of Aut(ˆC). Any such quadruple has a unique representative
of the form (∞, 0, 1,λ ), giving a natural coordinate for this moduli space.
If we reorder the quadruple, the cross-ratio changes, ranging among the
six values
λ, 1
λ, 1−λ, 1
1−λ, λ
λ− 1,λ− 1
λ .
(There is a natural action of S4, but the Klein 4-group Z/2× Z/2 acts
trivially.) There are 5 points in ~M0,4 with nontrivial stabilizers under the
action of S3: the points
{−1, 1/2, 2} = zeros of 2z3− 3z2− 3z + 2,
which each have stabilizer Z/2 and correspond to the vertices of a square;
and the points
{ρ,ρ} ={1/2±
√
−3/2} = zeros of z2−z + 1,
which have stabilizer Z/3 and correspond to the vertices of a tetrahedron.
The degree 6 rational map
F (z) = 4
27
(z2−z + 1)3
z2(1−z)2
is invariant under S3, and gives a natural bijection
F : (ˆC−{ 0, 1,∞})/S3∼= C
satisfying
F (0, 1,∞) =∞,F (ρ,ρ) = 0, and F (−1, 1/2, 2) = 1.
(The last fact explains the 4 /27.) We should really think of the image as
M0,4 and in particular remember the orbifold structure: Z/2 at F = 1 and
Z/3 at F = 0.
The modular function. We now deﬁne a map J : M1 → M0,4 by
associating to any complex torus, the four critical values of the Weierstrass
℘-function. (Note: any degree two map f :X = C/Λ→ˆC is equivalent, up
125

to automorphisms of domain and range, to the Weierstrass ℘ function, so
the associated point in M0,4 is canonically determined by X.)
More concretely, givenτ∈ H we deﬁne the half-integral points (c1,c 2,c 3) =
(1/2,τ/ 2, (1 + τ)/2) and the corresponding critical values by ei = ℘(ci).
Then their cross-ratio (together with the critical value at inﬁnity) is given
by:
λ(τ) = e3−e2
e1−e2
·
For example, we have seen that if τ = iy ∈ iR+ then e2 < e3 < e1, so
λ(iy)∈ (0, 1); moreovere3 = 0 ande2 =−e1 forτ =i, and thusλ(i) = 1/2.
The value of λ(τ) depends only on the ordering of E(2)∗, the three
nontrivial points of order two on E. Now SL 2(Z) = Aut(Λ) acts on E(2)∼=
(Z/2)2 through the natural quotient
0→ Γ(2)→ SL2(Z)→ SL2(Z/2)→ 0.
In particular, λ is invariant under the subgroup Γ(2) of matrices equivalent
to the identity modulo two.
Now any elliptic element in SL 2(Z) has trace−1, 0 or 1, while the trace
of any element in Γ(2) must be even. Moreover, trace zero cannot arise:
if g =
(a b
c−a
)
∈ Γ(2) then −a2−bc = 1 implies −a2 = 1 mod 4 which is
impossible.
By assembling 6 copies of the fundamental domain for SL2(Z) (some cut
into two pieces), one can then show:
Theorem 5.29 The group Γ(2) is torsion-free, with fundamental domain
the ideal quadrilateral with vertices {∞,−1, 0, 1}.
We may now state the main result relating lattices and cross-ratios.
Theorem 5.30 The natural map
λ : ~M1 = H/Γ(2)→ ~M0,4 =ˆC−{ 0, 1,∞}
sending a torus to the cross-ratio of the critical values of ℘ is a holomorphic
bijection, respecting the action of S3.
Proof. We ﬁrst check that λ is injective. If z = λ(τ1) = λ(τ2), then
the corresponding complex tori E1, E2 both admit degree two maps to ˆC
branched over (0, 1,∞,z ). Lifting one map composed with the inverse of
the other gives an isomorphism E1→E2, and hence τ1∈ SL2(Z)·τ2.
126

We have also seen that there exists a continuous map µ :M0,4→M 1
which satisﬁesµ(λ(τ)) = [τ]; it sendsz to the lattice spanned by integrals of
the form dw/(w(w− 1)(w−z)). The existence of this map shows the image
of λ is closed. It follows that λ is a bijection.
Figure 12. Tiling for Γ(2).
As we have seen, if τ∈iR then e1,e 2,e 3∈ R. This shows:
Theorem 5.31 The function λ is real on the orbit of the imaginary axis
under SL2(Z).
This orbit gives the edges of a tiling of H by ideal triangles; see Figure
12.
Corollary 5.32 The map λ gives an explicit Riemann map from the ideal
triangle spanned by 0, 1 and∞ to H, ﬁxing these three points.
ThusSλ−1 is given by the quadratic diﬀerential Q(0, 0, 0) discussed ear-
lier, and λ−1 itself can be given as a ratio of solutions to a linear diﬀerential
equation of order two.
Picard’s theorem revisited. This gives the one line proof of the Little
Picard Theorem: ‘consider λ−1◦f : C→ H.’
The question recently arose in conversation whether a disserta-
tion of 2 lines could deserve and get a Fellowship... in mathe-
matics the answer is yes....
(Theorem.) An integral function never 0 or 1 is a constant.
(Proof.) exp{iΩ(f(z))} is a bounded integral function.
127

...But I can imagine a referee’s report: ‘Exceedingly striking and
a most original idea. But, brilliant as it undoubtedly is, it seems
more odd than important; an isolated result, unrelated to any-
thing else, and not likely to lead anywhere.’
—J. E. Littlewood.
Cf. [Bol, p.39–40]: Here Ω is our λ−1.
The J-function. To remove the ambiguity of ordering, we now deﬁne
J(τ) =F (λ(τ)) = 4
27
(λ2−λ + 1)3
λ2(1−λ)2 ·
The S3-equivariance of λ then implies:
Theorem 5.33 The map
J :M1 = H/ SL2(Z)→M 0,4 = (ˆC−{ 0, 1,∞})/S3
is a bijection, and a isomorphism of orbifolds.
Forgetting the orbifold structure, we get an isomorphism J : M1 ∼=
C. In other words, J(τ) is a complex number which depends only on the
isomorphism class of E = C/(Z⊕ Zτ); we have J(τ1) = J(τ2) iﬀ E1∼=E2;
and every complex number arises as J(τ) for some τ.
Classical proof. Here is the classical argument that J is a bijection. The
value of J(τ) determines a quadruple B ⊂ ˆC which in turn determines
a unique Riemann surface X → ˆC of degree two, branched over B, with
X∼= C/Z⊕τ Z. Thus J(τ1) = J(τ2) iﬀ the corresponding complex tori are
isomorphic iﬀ τ1 =g(τ2) for some g∈ SL2(Z). Thus J is injective.
To see it is surjective, we ﬁrst observe that J(τ + 1) = J(τ). Now if
Imτ =y→∞ , then on the region | Imz|<y/ 2 we have
℘(z) = 1
z2 +
∑′ 1
(z−n)2− 1
n2 +ϵ(z) = π2
sin2(πz) +C +ϵ(z),
where ϵ(z)→ 0 as y→∞. (In fact we have
ϵ(z) =
∑′
n
π2
sin2(π(z +nτ)) =O(e−πy).
We really only need that it tends to zero; and we will not need the exact
value of the constant C =−π2/3).
128

Since sin(z) grows rapidly as| Imz| grows, we have
(e1,e 2,e 3) = (π2 +C,C,C ) +O(ϵ)
and thus λ(τ) = (e3−e2)/(e1−e2)→ 0 and hence J(τ)→∞ .
ThusJ is a proper open map, which implies it is surjective (its image is
open and closed).
5.4 Modular forms
In this section we will ﬁnd an explicit formula for J(τ), and give a com-
plete analysis of the holomorphic forms and functions on H (with controlled
growth) that are invariant under SL 2(Z).
Modular forms: analytic perspective. A holomorphic function f :
H→ C is said to be a modular form of weight 2k for SL 2(Z) if it has the
following properties:
1. f(τ + 1) =f(τ);
2. f(−1/τ) =τ 2kf(τ); and
3. sup Imτ>1|f(τ)|<∞.
The vector space of all such forms will be denoted by Mk. The product
forms of weight 2k and 2𝓁 has weight 2(k +𝓁), so⊕Mk forms a graded ring.
The ﬁrst two properties imply that
f(g(τ)) = (cτ +d)2kf(τ)
for allg =
(a b
c d
)
∈ SL2(Z). The ﬁrst and third properties imply that we can
write
f(τ) =
∞∑
0
anqn,
where q = exp(2πiτ ). In other words, f(τ) descends to a holomorphic
function on ∆∗ = H/Z with a removable singularity at q = 0. In particular,
f(τ)→a0 as Imτ→∞ . One sometimes writes f(i∞) =a0.
Iff(i∞) = 0, one says that f(τ) is cusp form. The cusp forms ( Spitzen-
formen) give a natural subspace Sk⊂Mk.
Examples.
129

1. Any holomorphic invariant F (Λ) of lattices that is homogeneous of
degree−2k and satisﬁes the right growth conditions deﬁnes a modular
form of weight 2k. That is, if F (tΛ) =t−2kΛ, then the function
f(τ) =F (Z⊕τ Z)
satisﬁes f(τ + 1) =f(τ) and
f(−1/τ) =F (Z⊕τ−1Z) =F (τ−1(Z⊕τ Z) =τ 2kf(τ).
2. In particular, for k≥ 2 the Eisenstein series
Gk(τ) =
∑′
(n +mτ)−2k
are modular forms of weight 2 k. Evidentally Gk converges to 2ζ(2k)
as Imτ→∞ , so these are holomorphic at inﬁnity but not cusp forms.
3. Similarly for the normalized functions g2 = 60G2, g3 = 140G3.
Modular forms: algebraic perspective. If we associate to f(τ) the
form
ω =f(τ)dτk,
then the ﬁrst two conditions above just say that g∗ω =ω for allg∈ SL2(Z).
(Recall thatg′(z) = (cz+d)−2.) Since dz = (2πi)−1dq/q, the third condition
says that ω descends to a form
ω = (2πi)−kf(q)
(dq
q
)k
on ∆∗ = H/Γ with at worst a pole of order k at q = 0.
Thusω also descends to an S3-invariant holomorphick-form on
~M0,4 =ˆC−{ 0, 1,∞} = H/Γ(2)
with poles of order≤k at 0, 1 and∞. The converse is also true. This shows:
Theorem 5.34 The space Mk is naturally isomorphic to the space of S3-
invariant rational forms ω(z)dzk on ˆC with poles of order ≤ k at 0, 1,∞
and no other poles.
This provides a purely algebraic perspective on the initially transcendental–
looking theory of automorphic forms.
We now wish to ﬁnd all the rational holomorphic k-formsω∈Mk. Here
are 2 key properties of any nonzero ω∈Mk:
130

(i) The zerosZ(ω) are invariant underS3 and satisfy|Z(ω)|≤ k,
when counted with multiplicity, and determineω up to constant
multiple.
(ii) The poles of ω at 0, 1,∞ are all of the same order, which can
be k, k− 2, k− 4, etc. We have ω∈ Sk iﬀ the order of pole is
k− 2 or less.
Part (i) comes from the fact that ω has at most 3 k poles, hence at most
3k− 2k = k zeros. The parity constraint in (ii) comes from the fact that
g(z) = 1−z leavesω invariant, andg′(∞) =−1.
Examples.
1. We have M0 = C; it consists of the constant functions.
2. We have dim M1 = 0; the group S3 has no ﬁxed point, so there is no
candidate for Z(ω).
3. We have dim M2 = 1. The only possibility is Z(ω) ={ρ,ρ}; thus the
quadratic diﬀerential
F2 = (z2−z + 1)dz2
z2(z− 1)2
spansM2. (We have met this diﬀerential before in the study of Schwarz
triangle functions.)
4. Similarly, dim M3 = 1; it is spanned by the cubic diﬀerential
F3 = (z− 2)(z− 1/2)(z + 1)dz3
z3(z− 1)3 ,
which has zeros at−1, 1/2, 2.
5. The products F 2
2 and F3F2 span M4 and M5. This is because S3 has
unique invariant sets with|Z| = 4 and 5.
6. We have dim M6 = 2; it is spanned by F 3
2 and F 2
3 . These two forms
are linearly independent because they have diﬀerent zero sets.
7. The discriminant
D6 = 4
27(F 3
2−F 2
3 ) = dz6
z4(z− 1)4
is the ﬁrst nontrivial cusp form; it has poles of order 4 at (0, 1,∞) and
no zeros. It spans S6.
131

8. Ratios of forms of the same weight give all S3-invariant rational func-
tions. Indeed, as we have seen, an isomorphism ˆC/S3∼= ˆC sending
(∞,ρ, 2) to (∞, 0, 1),is given by
F (z) = F 3
2 (z)
F2(z)3−F3(z)2 = 4
27
(z2−z + 1)3
z2(z− 1)2 ·
More generally, any S3-invariant rational function of degree d can be
expressed as a ratio of modular forms of degree d.
9. If desired, we can regard F2 and F3 as forms on ˆC/S3 by substituting
w =J(z). They then come:
F2 = dw2
4w(w− 1) and F3 = dw3
8w2(w− 1)·
We also ﬁnd D6 = (1/432)(w−4(w− 1)−3)dw6.
Cusp forms. We let Sk⊂ Mk denote the space of cusp forms with poles
of order≤k− 2 at 0, 1,∞.
Theorem 5.35 The mapω↦→D6ω gives an isomorphism fromMk toSk+6.
Proof. Any F ∈ Mk has poles of order ≤ k, so FD 6 has poles of order
≤k + 4 and hence lies inSk+6. Conversely, if G∈Sk+6 thenF =G/D6 has
poles of order at most k at 0, 1,∞, and it is otherwise holomorphic since D6
has no zeros.
Every space Mk, k≥ 2 contains a form of the type Fi
2Fj
3 which is not a
cusp form; thus Mk∼= C⊕Sk. By inspection, dim Sk = 0 for k≤ 5. On the
other hand, any cusp form is divisible by D6. This shows:
Corollary 5.36 We have dimM6n+1 = n, and dimM6n+i = n + 1 for
i = 0, 2, 3, 4, 5.
Corollary 5.37 The forms F2 and F3 generate the ring M =⊕Mk.
Corollary 5.38 The forms Fi
2Fj
3 with 2i + 3j =k form a basis for Mk.
Proof. By the preceding Corollary these forms span Mk, and the number
of them agrees with dim Mk as computed above.
132

Corollary 5.39 The ring of modular forms M is isomorphic to the poly-
nomial ring C[F2,F 3].
Proof. The preceding results shows the natural map from the graded ring
C[F2,F 3] to M is bijective on each graded piece.
We have already seen that, under the isomorphism M1 ∼= M0,4, an
analytic modular form is the same as an algebraic modular form. Thus we
also have:
Corollary 5.40 The ring of modular forms is isomorphic to C[g2,g 3].
Corollary 5.41 For every k≥ 2, the quantity
∑′
λ−2k can be expressed
as a polynomial in
∑′
λ−4 and
∑′
λ−6.
Values ofg2 andg3. We now note that forτ =i, the zeros of 4℘3−g2℘−g3
must look like (−1, 0, 1) and thus g3(i) = 0. Similarly for τ = ρ the zeros
are arrayed like the cube roots of unity and hence g3(ρ) = 0.
To determine the values at inﬁnity, we observe that as τ→∞ we have
G2(τ)→ 2ζ(4) =π4/45
and
G3(τ)→ 2ζ(6) = 4π6/945.
This gives the valuesg2(∞) = 60G2(∞) = (4/3)π4 andg3(∞) = 140G3(∞) =
(8/27)π6, and thus
(g3
2/g2
3)(i∞) = 27.
The cusp form ∆ and the modular function J. By the preceding
calculation, the discriminant
∆(τ) =g3
2(τ)− 27g3(τ)2
is a cusp form of weight 12. We have seen such a form is unique up to
a scalar multiple, and is nonvanishing everywhere except for a simple zero
at inﬁnity. This form has a natural meaning: up to a multiple, it is the
discriminant of the cubic polynomial 4 x3−g2x−g3. As we have seen, this
polynomial has distinct roots whenever g2 and g3 come from a lattice; this
explains why ∆(τ) has no zeros in H.
Theorem 5.42 We have J(τ) =g3
2(τ)/∆(τ).
133

Proof. First note that this is a ratio of forms of weight 12 and hence a
modular function, i.e. it is invariant under SL 2(Z). Since g2(∞)⁄= 0, it
has a simple pole at inﬁnity, and thus has degree one on M1. We also have
J(ρ) = 0 since g2(ρ) = 0, and J(i) = 1 since g3(i) = 0.
Remarks. One can use residues to determine the exact relationship be-
tweenF2 and g2. Namely, F2∼ (1/4)dw2/w2, while for q = exp(2πiτ ) we
havedq = 2πiqdτ , and hence
g2 = 60G2(τ)dτ 2∼ 4π4
3
dq2
(2πiq)2 =−π2
3
dq2
q2·
Thusg2 =−(4π2/3)F2. One can similarly calculate g3/F3.
If we let j(τ) = 1728J(τ), then
j(τ) = 1
q + 744 +
∞∑
1
anqn
with an∈ Z.
Direct approach to J(λ). It is also easy to give a direct proof of the
formula
J(λ) = 4
27
λ2−λ + 1
(λ(1−λ))2 = g3
2
g3
2− 27g2
3
·
The ﬁrst equality above is a deﬁnition. For the second, suppose the cross-
ratio of the roots of the polynomial
Q(z) = 4z3−g2z−g3,
suitably ordered, is λ. Then up to scaling, the roots are (0 , 1,λ )−c, where
c = (1 + λ)/3. But J(λ) is scale–invariant, so it suﬃces to compute the
coeﬃcients of
Q(z) = 4(z +c)(z− 1 +c)(z−λ +c).
This gives:
g2 = (4/3)(λ2−λ + 1) and g3 = (4/27)(λ− 2)(λ + 1)(2λ− 1),
and substitution gives the equation above.
Connections with additive and multiplicative number theory.Incredibly,
we have
∆(q) = (2πi)12q
∞∏
1
(1−qn)24.
134

This gives a close connection between the theory of modular forms and the
partition function p(n), since
∏
(1−qn)−1 =
∑
p(n)qn.
The coeﬃcients power series for Gk(τ) involves the function σk(n) =∑
d|ndk .
The Riemann function ζ(s) arises as the Mellin transform of a theta
function, and then modularity translates into the functional equation.
5.5 Exercises.
1. Let Λ ⊂ Rn be a discrete group. Prove that Λ ∼= Za for some a≤n,
and a =n if and only if Rn/Λ is compact.
2. Let Λ ⊂ Rn be a lattice, i.e. a discrete subgroup isomorphic to Zn.
Choose a sequence of vectors a1,a 2,...,a n ∈ Λ such that a1 is a
shortest nonzero vector, and (for i > 1) ai is a shortest vector lin-
early independent from (a1,a 2,...,a i−1).
Is it always the case then that Λ = Za1⊕···⊕ Zan?
3. Let Λ ⊂ C be a lattice, let X = C/Λ and let End(Λ) ={α∈ C : αΛ⊂
Λ}. Show that for each α∈ End(Λ), the formula [f(z)] = [αz] deﬁnes
an analytic covering map f :X→X of degree|α|2.
For what values of α∈ C does there exist a lattice with α∈ End(Λ)?
Conclude that End( Z⊕ Zτ) = Z for almost all values of τ.
4. Where are the zeros of the ℘-function for the lattice Z⊕ Zi? For the
lattice Z⊕ Zω? (Here ω = (1 +√−3)/2.)
5. Let ω = exp(2πi/3), and let Λ = Z⊕ Zi and L = Z⊕ Zω. Prove that∑′
Λ
λ−6 =
∑′
L
λ−4 = 0.
6. Prove that there exists a pair of nonconstant meromorphic functions
on C such thatf(z)3+g(z)3 = 1. (Hint: show the equation x3+y3 = 1
deﬁnes the same elliptic curve in P2 as y2 = 4x3− 1.)
7. State and prove a ‘double angle’ formula for the Weierstrass℘-function.
That is, ﬁnd a rational function f(z) (that may depend on ( g2,g 3))
such that ℘(2z) =f(℘(z)).
135

8. (Continuation.) Let X = C/Λ be a complex torus, and deﬁne a map
F : X→ X by [F (z)] = [2z]. Show that F has a dense orbit on X,
i.e. that there exists a p∈X such that{Fn(p) : n> 0} =X, where
Fn(p) =F (F (··· F (p))).
Then prove the rational function f(z) of the double-angle formula has
a dense orbit on ˆC.
9. Suppose
∑′
λ−4 and
∑′
λ−6 are the same for two lattices Λ 1, Λ2⊂
C. Does it follow that Λ 1 = Λ2?
10. Suppose (x,y ) = (℘(z),℘′(z)) satisﬁesy2 = 4x3 +ax +b witha,b∈ R,
and the polynomial 4x3 +ax +b = 0 has only one real root. What can
you say about the shape of the lattice Λ used to deﬁne ℘(z)?
11. Let T⊂ C be the region bounded by the triangle with vertices (0, 1, 1+
i). Give an explicit formula for a conformal mapping f : T → H in
terms of the Weierstass ℘-function for a suitable lattice.
12. Let Λ = Zλ1⊕ Zλ2 be a lattice in C, with associated Weierstrass
℘-function ℘(z). Let
σ(z) =z
∏′
Λ
(1−z/λ) exp(z/λ + (1/2)(z/λ)2) (5.1)
be the canonical product with zeros at the points of Λ.
Prove there is a unique odd meromorphic functionζ(z) on C such that
ζ′(z) =−℘(z), and relate ζ(z) to σ(z).
13. (Continuation.) Show that ζ(z +λi) = ζ(z) +ηi for suitable ηi∈ C.
Using the residue theorem, show these ‘dual periods’ satisfy
det
(
η1 η2
λ1 λ2
)
= 2πi.
14. (Continuation.) The canonical product satisﬁes σ(z +λi) = exp(ai +
biz)σ(z). Express ai and bi in terms of λi and ηi.
15. Let [zi] be a ﬁnite sequence of distinct points in E = C/Λ. Let
Fi(z) =
1∑
j=Ni
ai,j(z−zi)−j
136

be a Laurent tail centered atzi∈ C. Prove there exists a meromorphic
functionf :E→ˆC with poles atzi and these Laurent tails if and only
if ∑
iai,1 = 0. (Hint: use the residue theorem in one direction, and
translates of the function ζ(z) = 1
z +
∑′
Λ
1
z−λ + 1
λ in the other.)
16. Prove that ℘′(z) =−σ(2z)/σ(z)4, where σ(z) is deﬁned by (5.1).
17. Prove that J(z) =g2(z)3/(g2(z)3− 27g3(z)2). (Recall
J(z) = 4
27
(λ2−λ + 1)3
λ2(1−λ)2 ,
and λ(z) is the cross-ratio of the roots of the cubic equation 4 x3−
g2(z)x−g3(z) = 0, together with∞.)
18. For any λ⁄= 0, 1,∞ let Sλ = ˆC−{ 0, 1,∞,λ}. Let Aut( Sλ) be the
group of holomorphic bijections f :Sλ→Sλ.
(a) Prove that every f∈ Aut(Sλ) is a M¨ obius transformation.
(b) Prove that for all λ, Aut(Sλ) contains a subgroup isomorphic to
Z/2× Z/2. How does this group permute the points {0, 1,∞,λ}?
(c) Find all values of λ such that | Aut(Sλ)| > 4 and identify the
group in each case.
19. Let ρ(z)|dz| be the hyperbolic metric on X = ˆC−{ 0, 1,∞}; that is,
the unique metric such thatλ : H→X is a local isometry. Show there
are constants A,B >0 such that for small values of z,
A
|z log|z||≤ρ(z)≤ B
|z log|z||.
(Hint. Recall|dz|/|z log|z|| is the hyperbolic metric on ∆∗− ∆−{ 0}.
Using the fact that λ(z + 2) = λ(z), write λ(z) = f(exp(πiz)) where
f : ∆∗→X is a covering map. Observe that f(0) = 0 and f′(0)⁄= 0
to complete the proof.)
20. Let L be length in the hyperbolic metric of the closed geodesic γ on
X = ˆC−{ 0, 1,∞} that makes a ﬁgure 8 around 0 and 1. Show that
L = log(17 + 12
√
2). (Hint: show that γ corresponds to a matrix of
trace 6 in π1(X)∼= Γ(2).)
137

21. Recall for any lattice we deﬁned Gn(Λ) =
∑′
λ−2n. It can be shown
(using the fact that there is a unique modular form of weight 8) that
there is a universal constant A such that G2(Λ)2 =AG4(Λ) for all Λ.
What is the value of A? (Hint:
∑′
1/n8 =π8/4725.)
22. What are the orbits of SL 2(Z) acting on Q∪{∞}⊂ ∂H? What are
the orbits of Γ(2)?
23. For k ≥ 0, let Mk denote the space of rational forms f(z)dzk on
ˆC with poles of order at most k at 0, 1,∞ and no other poles. (i)
Determine dimMk and give a basis for this space. (ii) Give a ﬁnite set
of generators for ⊕Mk as a graded ring. (This is the ring of modular
functions for Γ(2).)
24. Prove that λ(i/2) = 12
√
2− 16.
(Hint: Letting Xτ = C/Z⊕τ Z, λ(τ) is the cross-ratio of the critical
values (suitably ordered) of any degree two map fτ : Xτ → ˆC. For
the square torus, τ =i, choose fi so its critical values are the roots of
z4 + 1 = 0. Then one can choose fi/2(z) = (fi(z) +fi(z)−1)/2, and
ﬁnd that its critical values are {−1,−
√
1/2,
√
1/2, 1}.)
25. Prove that
60
∑′
λ∈Z[i]
λ−4 = 64π2Γ[5/4]4
Γ[3/4]4 ·
26. (Continuation.) Relate the equation above to the conformal radius
of the unit square (with sides of length two), previously shown to be
4Γ[3/4]2/π3/2 = 1.078705... .
References
[Ad] W. A. Adkins. Local algebraicity of some analytic hypersurfaces.
Proc. Amer. Math. Soc. 49(1980), 546–548.
[BD] F. Berteloot and J. Duval. Sur l’hyperbolicit´ e de certain
compl` ementaires.Enseign. Math. 47(2001), 253–267.
[Bol] B. Bollabas, editor. Littlewood’s Miscellany. Cambridge University
Press, 1986.
138

[CJ] L. Carleson and P. Jones. On coeﬃcient problems for univalent func-
tions. Duke Math. J. 66(1992), 169–206.
[Gam] T. W. Gamelin. Uniform Algebras. Prentice–Hall, 1969.
[Gol] G. M. Goluzin. Geometric Theory of Functions of a Complex Vari-
able. Amer. Math. Soc, 1969.
[GM] J. D. Gray and S. A. Morris. When is a function that satisﬁes the
Cauchy-Riemann equations analytic? The American Mathematical
Monthly 85(1978), 246–256.
[Har] G. H. Hardy. Divergent Series. Chelsea, 1991.
[Ko] S. V. Kolesnikov. On the sets of nonexistence of radial limits of
bounded analytic functions. Russian Acad. Sci. Sb. Math. 81(1995),
477–485.
[MH] J. E. Marsden and M. J. Hoﬀman. Basic Complex Analysis . W. H.
Freeman, 1999.
[Mil1] J. Milnor. Singular Points of Complex Hypersurfaces , volume 61 of
Annals of Math. Studies . Princeton University Press, 1968.
[Mil2] J. Milnor. On Latt` es maps. In P. G. Hjorth and C. L. Petersen,
editors, Dynamics on the Riemann sphere , pages 9–44. European
Math. Soc., 2006.
[Mon] M. G. Monzingo. Why are 8:18 and 10:09 such pleasant times? Fi-
bonacci. Quart. 2(1983), 107–110.
[Re] R. Remmert. Classical Topics in Complex Function Theory .
Springer, 1998.
[Sa] R. Salem. Algebraic Numbers and Fourier Analysis . Wadsworth,
1983.
139

