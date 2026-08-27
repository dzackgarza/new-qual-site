MATH 8210, FALL 2011 LECTURE NOTES
MIKE USHER
1. M ultiv ariable calculus without coordinates
The objects of study in this course are what are called “smoot h manifolds.” For the time being I won’t give
a precise deﬁnition of these (it will come later, or of course you can easily look it up), but for now su ﬃce it to
say that these are topological spaces which locally resembl e Euclidean space and in which, in particular, it is
possible to do something resembling calculus. The surface o f the Earth is (to good approximation) an example
of a two-dimensional smooth manifold. Of course, the Earth is not R2 but rather a closed surface (I was going to
say a sphere, but then it occurred to me that if one looks close ly enough there are some rock formations which
cause the genus to be positive), yet locally it looks enough like R2 that it seems reasonable to speak for instance
of the directional derivatives of a function (the temperature, say) deﬁned on the Earth.
So how can we formulate calculus in such spaces? Part of the de ﬁnition will be that a manifold M will have
an open cover {Uα|α ∈ A} by sets equipped with homeomorphisms (“charts”) φα : Uα → Vα where Vα ⊂ Rn is
open. So we can try to do calculus on M by, roughly speaking, doing standard multivariable calculus in the open
sets Vα and then transporting the constructions back to M by the mapsφα (or their inverses). However, ifm ∈ M,
then m will typically belong to several of the sets Uα in the open cover of M, and one needs to make sure that
one’s constructions don’t depend on which of the charts one is using. To compare between theαth chart and the
βth chart, one needs to look at the “transition function”
φβ ◦φ−1
α : φα(Uα ∩ Uβ) →φβ(Uα ∩ Uβ).
This is a map between two open subsets of Rn, and part of the deﬁnition of a smooth manifold will ensure th at
the map is smooth (i.e., C∞) and invertible (with a smooth inverse), but there won’t be any restrictions on what
φβ ◦φ−1
α other than that. So for example it doesn’t make sense to “take the partial derivative of a function on M
with respect to the ﬁrst coordinate,” since although we can diﬀerentiate a function on Vα with respect to the ﬁrst
coordinate, or we can do the same for a function on Vβ, these operations won’t be equivalent when we try to lift
them up to M using the mapsφα,φβ.
So this makes it important to understand how notions of multi variable calculus behave under the action of
diﬀeomorphisms (i.e., smooth maps with smooth inverses) φ: U → ˜U where U and ˜U are open subsets of Rn.
You should think of the action of such a diﬀeomorphism as being the same as changing one’s coordinate system,
e.g. from Cartesian coordinates to polar coordinates. In partic ular I want to ﬁrst discuss various notions of what
a tangent vector at a point p ∈ U is. (And we’ll later generalize this to the notion of a tangen t vector at a point
in a smooth manifold.) Visually you’re supposed to think of a tangent vector at p as being a little arrow whose
base is at p, pointing in a possible direction of motion from p. The set of these tangent vectors will form a vector
space called the tangent space to U at p and denoted T pU. I’ll give three characterizations, from most concrete
to most abstract.
(1) The way to describe this notion that is used in undergraduate multivariable calculus courses is just to say
that a tangent vector v at p ∈ U is (or is represented by) an n-tuple of numbers ( v1,..., vn) ∈ Rn. One
can then draw the vector whose base is atp and whose ﬁrst coordinate is v1, second coordinate is v2, and
so on. (In somewhat more sophisticated language, the standard Cartesian coordinates on Rn determine a
basis {e1,..., en} of unit vectors, and one has v = ∑viei.)
1

2 MIKE USHER
This characterization is very good for computational purpo ses, but when one is interested in how
tangent vectors behave under coordinate changes φ: U → ˜U it has some disadvantages. The tangent
vector v = (v1,..., vn) ∈ T pU should correspond under the coordinate change φ to a tangent vector
φ∗v ∈ Tφ(p) ˜U at φ(p). Perhaps you’ve learned how this correspondence works: on e constructs the
Jacobian matrix at p of the map φ (with (i, j) entry given by ∂φi
∂x j
where φi is the ith component of φ),
and then the coordinates ofφ∗v are obtained by multiplying the Jacobian matrix by the vector consisting
of the components of v. This is a manageable computation, but it may not be very conc eptually clear
from this discussion what’s going on here. In particular if w e then want to say what a tangent vector
to a point m on a smooth manifold is we’d have to say something like “an n-tuple of numbers for each
chart containing m, such that then-tuples for diﬀerent charts are related by the Jacobians of the transition
functions,” which is much more opaque and less natural-sounding than it really should be.
(2) A more natural characterization of tangent vectors is th e following. The idea is that the tangent space
T pU consists of all possible velocities of curves passing throu gh p. If p ∈ U, consider all C∞ paths
γ: ( −ǫ,ǫ ) → U (for some ǫ > 0) such that γ(0) = p. I would like to declare two of these to be
equivalent if they have the same velocity, i.e., γ1 ∼ γ2 iﬀγ′
1(0) = γ′
2(0) (or equivalently, and maybe
less circularly, γ1 ∼ γ2 if limt→0
γ1(t)−γ2(t)
t = 0). Then simply deﬁne a “tangent vector” at p to be an
equivalence class [γ] of C∞ arcs through p (and so T pU is just the set of equivalence classes). The way
this behaves under coordinate changes is extremely simple,since I’m not using coordinates to deﬁne the
notion: a tangent vector v ∈ T pU has the form v = [γ] for someγ, and the corresponding tangent vector
φ∗v ∈ Tφ(p) ˜U is just [φ ◦γ]. We’ll see later that this adapts to general smooth manifolds very simply and
directly—a tangent vector at a point on a smooth manifold will just be a suitable equivalence class of
curves passing through that point.
The one disadvantage of this characterization is that it’s not so intuitively obvious how to do algebraic
operations (like addition of tangent vectors) on equivalen ce classes of curves through a point (though
you can make a suitable deﬁnition if you put your mind to it).
It shouldn’t be hard to construct a natural correspondence between tangent vectors in this sense and
tangent vectors in the sense of Deﬁnition (1) above, but agai n, the advantage of thinking about it this
way is that it’s less coordinate-dependent.
(3) Now for a characterization of tangent vectors that you al most certainly would not have thought of. To
attempt to motivate it, note that a given tangent vector v ∈ T pU gives you the ability to di ﬀerentiate
smooth functions f : U → R at p—namely you take the directional derivative at p:
(Dv f )(p) = lim
t→0
f (p + tv) − f (p)
t .
So we will deﬁne a tangent vector at p to be “a way of diﬀerentiating functions deﬁned near p,” i.e., we
will abstract some relevant properties of the operation of taking a directional derivative, and then deﬁne
a tangent vector to be one of these operations.
To do this, ﬁrst consider pairs ( f, V) where V is an open neighborhood of p and f : V → R is
C∞, and declare two such pairs ( f, V) and ( g, W) to be equivalent if there is a smaller neighborhood
Z ⊂ V ∩ W of p such that f |Z = g|Z. Let Op be the set of equivalence classes. Since we can set,
for instance [ f, V] ·[g, W] = [ f g, V ∩ W], Op is easily seen to be a commutative R-algebra (i.e., it is
both a commutative ring and a vector space over R, with appropriately compatible operations), called
the “algebra of germs of functions at p.” I’ll tend to denote a germ by just f rather than [ f, V]; it
is to be understood that f is deﬁned not necessarily throughout U but rather on some (varying) open
neighborhood of p. Of course one always has a well-deﬁned value f (p) for f ∈ O p.
A tangent vector at p will then be deﬁned to be a derivation v: Op → R, i.e. v is to satisfy
• (R-linearity) v(c f + g) = cv( f ) + v(g) for c ∈ R and f, g ∈ O p
• (Leibniz rule) v( f g) = f (p)v(g) + g(p)v( f ) for f, g ∈ O p.

MATH 8210, FALL 2011 LECTURE NOTES 3
It’s standard that the directional derivative operationsDv alluded to above satisfy these properties. It’s
not obvious that, conversely, any derivation onOp is given by a directional derivative in some direction,
but we’ll prove this shortly.
Like the characterization of tangent vectors as equivalenc e classes curves, this formulation is com-
pletely coordinate free, making it easy to extend the deﬁnition to manifolds when the time comes. Unlike
the situation with curve characterization, though, it’s quite obvious that derivations form a vector space,
which is another advantage.
To see how this notion behaves under diﬀeomorphisms (or indeed under more general smooth maps)
φ: U → ˜U, if v ∈ T pU (i.e., if v is a derivation on Op), we need to construct a derivation φ∗v on Oφ(p).
Well, if f ∈ Oφ(p) (really we should write [f, V]), so f is a smooth function deﬁned nearφ(p), then f ◦φ
will be a smooth function deﬁned near p (speciﬁcally, it will be deﬁned on the open set φ−1(V) around
p), and so we can deﬁne
(φ∗v)( f ) = v( f ◦φ)
So as with the curve formulation, it’s quite simple to see how derivations transform under coordinate
changes.
Among the three above characterizations of tangent vectors , it should be clear that (1) is equivalent to (2),
under the correspondence which assigns to an equivalence cl ass of curves [ γ] the vector γ′(0) (expressed in
coordinates using the standard basis for Rn). We now set about proving that (1) and (3) are also equivalen t.
Let T pU denote the space of tangent vectors as given by formulation ( 1) (i.e., as elements of Rn) and (for the
moment) ˜T pU that given by (3) (i.e., as derivations). Write the coordinates of p ∈ U ⊂ Rn as (p1,..., pn). Now
we have a linear mapα: T pU → ˜T pU given by
α(v1,..., vn) =
n∑
i=1
vi
∂
∂xi
,
i.e., α sends a vector (in the undergraduate multivariable calculu s sense) to the operation given by directional
diﬀerentiation in the direction of that vector. We claim thatα is bijective, justifying our proposal to regard (3) as
an equivalent deﬁnition of the tangent space at p. It should be clear thatα is injective. Indeed, for each i we have
an element xi − pi ∈ O p, and we see that, whereβ: ˜T pU → T pU is given by
β(v) = (v(x1 − p1),..., v(xn − pn)),
we haveβ ◦α = 1 (as ∂
∂xi
(x j − p j) =δi j). Thusα is injective, andβ surjective. To see thatα is surjective, we note
the following, whenever v ∈ ˜T pU:
• v(1) = v(1 ·1) = 1v(1) + 1v(1) = v(1) + v(1). Hence v(1) = 0, and so by R-linearity v(c) = 0 for every
constant function c.
• For any i and j, if f ∈ O p we have
v
(
(xi − pi)(x j − p j) f
)
= (xi − pi)|pv((x j − p j) f ) + (x j − p j)|p f (p)v((xi − pi)) = 0.
• By the multivariable Taylor formula, any (germ of a) function g ∈ O p can be written (on some neighbor-
hood of p)
g(x) = g(p) +
n∑
i=1
∂g
∂xi
(p)(xi − pi) +
n∑
i, j=1
(xi − pi)(x j − p j) fi j(x)
for some fi j ∈ O p. Hence by the ﬁrst two items and the linearity of v, we get
v(g) =
n∑
i=1
∂g
∂xi
(p)v(xi − pi).

4 MIKE USHER
Thus
v =
∑
vi
∂
∂xi
=α(v1,..., vn),
where the numbers vi are equal to v(xi − pi).
In view of the above correspondence, we can drop the tilde in t he notation ˜T pU, and always view tangent
vectors as derivations on spaces of germs of functions. Even when we express a tangent vector in coordinates,
we will often use notation consistent with the derivation interpretation and write the vector as
v1
∂
∂x1
+ · · ·+ vn
∂
∂xn
rather than (v1,..., vn).
Of course, another familiar notion from multivariable calculus is that of a vector ﬁeld on an open set U, which
can be thought of as a smooth family of tangent vectors at all o f the points of U, or as a smooth vector-valued
function X : U → Rn, expressible in coordinates as X(m) = (X1(m),..., Xn(m)). There is also a coordinate-free
interpretation of what a vector ﬁeld is: it is a map X : C∞(U) → C∞(U) which, as with tangent vectors, is a
derivation, namely:
• X(c f + g) = cX( f ) + X(g) for all c ∈ R, f, g ∈ C∞(U), and
• X( f g) = f X(g) + gX( f ) for all f, g ∈ C∞(M).
Note that while tangent vectors, when viewed as derivations, just take values in R, vector ﬁelds take values in
the space of smooth functions. Just as with tangent vectors, there’s a natural one-to-one correspondence between
the undergraduate versions of vector ﬁelds and the derivations on C∞(U): simply assign to ( X1(·),..., Xn(·)) the
derivation
f ↦→
n∑
i=1
Xi
∂ f
∂xi
.
Again, the great advantage of the derivation interpretation is that it makes no direct reference to coordinates.
So on a smooth manifold M, once have deﬁned the space of smooth functions C∞(M), we will e ﬀortlessly be
able to deﬁne a vector ﬁeld on M as a derivation X : C∞(M) → C∞(M).
Another nice feature of the derivation interpretation for v ector ﬁelds (but not for tangent vectors) is that it
points toward some additional structure on the space of vect or ﬁelds that we wouldn’t have noticed if we just
worked in coordinates. Namely, given that a vector ﬁeld is a c ertain kind of function X : C∞(U) → C∞(U), it
becomes natural to think about composing such functions. Now a slight hitch with this is that the composition of
two derivations will not typically be a derivation. For example, ∂
∂x1
is a derivation, but ∂
∂x1
◦ ∂
∂x1
certainly is not:
namely we have
∂
∂x1
◦ ∂
∂x1
(x1x1) = 2
but
x1
∂
∂x1
◦ ∂
∂x1
(x1) + x1
∂
∂x1
◦ ∂
∂x1
(x1) = 0.
So while we can “compose” two vector ﬁelds the result won’t bea vector ﬁeld. However:
Proposition 1.1. Let A be a commutative R-algebra and let X, Y : A → A be two derivations on A. Then the
commutator [X, Y] := X ◦ Y − Y ◦ X is also a derivation on A.
Proof. The linearity of [X, Y] is trivial, so we just need to check the Leibniz rule. We ﬁnd, for f, g ∈ A:
[X, Y]( f g) = X (Y( f g)) − Y (X( f g)) = X ( f Yg + gY f) − Y ( f Xg + gX f)
= ( f XYg + (X f)(Yg) + gXY f + (Xg)(Y f)) − ( f YXg + (Y f)(Xg) + gYX f + (Yg)(X f))
= f (XY − YX )g + g(XY − YX ) f = f [X, Y](g) + g[Y, X]( f ),
which is precisely the Leibniz rule for [X, Y]. □

MATH 8210, FALL 2011 LECTURE NOTES 5
In local coordinates, if X = ∑Xi ∂
∂xi
and Y = ∑Y j ∂
∂x j
, then one ﬁnds
[X, Y]( f ) =
n∑
i=1
Xi
∂
∂xi








n∑
j=1
Y j
∂ f
∂x j







 −
n∑
i=1
Yi
∂
∂xi








n∑
j=1
X j
∂ f
∂x j








=
n∑
i, j=1
(
XiY j
∂2 f
∂xi∂x j
+ Xi
∂Y j
∂xi
∂ f
∂x j
)
−
n∑
i, j=1
(
YiX j
∂2 f
∂xi∂x j
+ Yi
∂X j
∂xi
∂ f
∂x j
)
=
n∑
j=1







n∑
i=1
Xi
∂Y j
∂xi
− Yi
∂X j
∂xi







∂ f
∂x j
.
Thus [X, Y] is the vector ﬁeld ∑Z j ∂
∂x j
whose jth component is given by
(1) Z j =
n∑
i=1
(
Xi
∂Y j
∂xi
− Yi
∂X j
∂xi
)
This commutator operation on vector ﬁelds (also called the Lie bracket) turns out to be a fairly important one.
Of course, if one wanted to work entirely in coordinates with out taking a more abstract point of view, it would
have been possible to just deﬁne the Lie bracket of two vector ﬁelds X and Y to be the vector ﬁeld given by
formula (1), but it’s not clear why one would be motivated to do so.
In general, the commutator operation [ ·, ·] on the space of linear maps from a vector space to itself sati sﬁes
the Jacobi identity:
(2) [ X, [Y, Z]] + [Z, [X, Y]] + [Y, [Z, X]] = 0
Indeed, the left hand side is equal to
X(YZ − ZY ) − (YZ − ZY )X + Z(XY − YX ) − (XY − YX )Z + Y(XZ − ZX) − (ZX − XZ)Y
and (using associativity of function composition) you can s ee that each of the six three-letter words made up of
one each of the letters X,Y ,Z appears above once positively and once negatively, so the sum is zero. Note that if
[·, ·] were an associative operation we would instead have [ X, [Y, Z]] + [Z, [X, Y]] = [X, [Y, Z]] − [[X, Y], Z] = 0;
thus the Jacobi identity expresses a particular way for a binary operation to be non-associative. In general a vector
space L equipped with a binary operation [·, ·]: A × A → A which is bilinear, which obeys [X, Y] = −[Y, X], and
which satisﬁes the Jacobi identity is called a Lie algebra; thus we have shown that, if U ⊂ Rn is open, then the
space X(U) of vector ﬁelds on U is naturally a Lie algebra.
Exercise 1.2. a) Letφ: U → V be a diﬀeomorphism between two open subsets of Rn, and let X be a vector ﬁeld
on U. Prove that if φ∗X : C∞(V) → C∞(V) is deﬁned by ((φ∗X)( f ))(φ(p)) = (X( f ◦φ))(p), thenφ∗X is a vector
ﬁeld on V. Why did we have to assume that φ was a di ﬀeomorphism (or at least bijective) in order to do this
(unlike the situation with tangent vectors, which can be pushed forward by any smooth map)?
b) Prove that if X, Y are two vector ﬁelds on U and ifφ: U → V is a diﬀeomorphism then
φ∗[X, Y] = [φ∗X,φ ∗Y].

6 MIKE USHER
Exercise 1.3. Deﬁne the following three vector ﬁelds1 on R3:
I = z ∂
∂y − y ∂
∂z
J = x ∂
∂z − z ∂
∂x
K = y ∂
∂x − x ∂
∂y
a) Compute [I, J], [I, K], and [J, K].
b) Deduce as a formal consequence of part (a) that the cross product on R3 satisﬁes the Jacobi identity.
2. B ump functions and partitions of unity in Rn
In point-set topology one learns a result called Urysohn’s L emma, which states that given inclusions A ⊂
U ⊂ X where X is a normal topological space, U is open, and A is closed, there is a continuous function
χ: X → [0, 1] identically equal to one on A and identically zero on X \ U. A version of this result is extremely
important in diﬀerential topology (perhaps more important than in point-se t topology); unfortunately, since we
need our functions to beC∞ and not just continuous, we can’t just cite Urysohn’s Lemma but rather need to prove
a new, smooth, version of the result (of course, this smooth version will apply in a more limited context, if only
because it doesn’t make sense to speak of “smooth functions”on a general normal topological space). The good
news is that the functions can be constructed in a more concrete fashion than one sees in the proof of Urysohn’s
Lemma.
We begin with a result in one-variable calculus.
Lemma 2.1. Deﬁne the function f : R → R by
f (t) =
{e−1/t t> 0
0 t ≤ 0
Then f ∈ C∞(R). Indeed, for all k ∈ N there is a polynomial Pk ∈ R[t] with the property that the kth derivative
f (k) exists and is given by
(3) f (k)(t) =
{Pk(1/t)e−1/t t> 0
0 t ≤ 0
Proof. First note that if (3) holds, then f (k) is continuous on all of R: indeed continuity is obvious everywhere
except zero, and at zero we have, by repeated applications of L’Hˆopital’s rule,
lim
t→0+
Pk(1/t)e−1/t = lim
s→∞
Pk(s)
es = lim
s→∞
ck
es = 0
where ck is some constant (which results from diﬀerentiating degPk-many times the polynomial Pk), from which
continuity at zero follows directly.
Thus we just need to prove (3), which we do by induction on k. So assume (3) holds for k; we prove it for
k + 1. For t< 0 the formula is trivial. For t = 0 we see
lim
t→0+
f (k)(t) − f (k)(0)
t = lim
t→0+
1
t Pk(1/t)e−1/t = lim
s→∞
sPk(s)
es = 0
1Though it’s not necessary in order to do the problem, you might convince yourself that if one interprets these vector ﬁelds in the standard
multivariable calculus sense, I points in the direction of a rotation around the x-axis, J in the direction of a rotation around the y-axis, and K
in the direction of a rotation around the z-axis.

MATH 8210, FALL 2011 LECTURE NOTES 7
by L’Hˆopital’s rule, and so (since the left-hand limit is trivially zero) we have f (k+1)(t) = 0. Finally for t > 0 we
have, by the product and chain rules,
f (k+1)(t) = d
dt
(
Pk(1/t)e−1/t)
= − 1
t2 P′
k
(1
t
)
e−1/t + 1
t2 Pk
(1
t
)
e−1/t,
and so the formula holds with
Pk+1(s) = s2(P′
k(s) + Pk(s)).
□
Note that our function f is a surjection to the half-open interval [0, 1), with f −1({0}) = (−∞, 0]. Out of this
function we can build many other useful ones. For instance:
Corollary 2.2. There is a C ∞ function g : R → [0, 1] with the property that g −1({1}) = [1, ∞) and g−1({0}) =
(−∞, 0].
Proof. Note that the function t ↦→f (1 − t) is smooth and nonnegative, and equals zero precisely on the interval
[1, ∞). In particular f (t) + f (1 − t) is positive everywhere. So we can let
g(t) = f (t)
f (t) + f (1 − t).
I leave it to you to check that this has the desired properties. □
Corollary 2.3. For any real numbers a< b there is a C∞ function ga,b : R → [0, 1] such that g−1
a,b({0}) = (−∞, a]
and g−1
a,b({1}) = [b, ∞).
Proof. Let
ga,b(t) = g
(t − a
b − a
)
.
□
Corollary 2.4. For any real numbers a < b < c < d there is a smooth “bump” function h : R → [0, 1] so that
h−1({1}) = [b, c] and h−1({0}) = (−∞, a] ∪ [d, ∞).
Proof. Let
h(t) = ga,b(t)(1 − gc,d(t)).
□
Corollary 2.5. For x ∈ Rn and r > 0 let Br(x) = {y ∈ Rn|‖y − x‖< r} denote the open ball of radius r around x.
Then for any0< s< r there is a smooth functionβ: Rn → [0, 1] such thatβ−1({1}) = Bs(x) and supp (β) = Br(x).
(Here by supp (β) we mean the support ofβ, i.e., the closed set {y ∈ Rn|β(y) /nequal0})
Proof. Let
β(y) = 1 − gs2,r2(‖y − x‖2).
□
Our goal now is the following theorem:
Theorem 2.6. Let U ⊂ Rn be an open set, and let V = {Vα|α ∈ A} be an open cover of U. Then there are C ∞
functionsχα : U → [0, 1] obeying the following properties:
(i) supp (χα) ⊂ Vα
(ii) Any x ∈ U has a neighborhood W x with the property thatχα|Wx = 0 for all but ﬁnitely manyα.
(iii) For all x ∈ U we have ∑
αχα(x) = 1.

8 MIKE USHER
Note that property (ii) ensures that ∑
αχα is well-deﬁned and smooth (even if there are inﬁnitely many—
perhaps uncountably many—di ﬀerentα), since U is then covered by open sets on each of which the sum ∑
αχα
is really a ﬁnite sum (all but ﬁnitely many terms are zero).
Deﬁnition 2.7. A collection of functions{χα|α ∈ A} obeying properties (i)-(iii) of Theorem 2.6 is called apartition
of unity subordinate to the cover {Vα}.
Theorem 2.6 has an analogue for general smooth manifolds (se e Theorem 3.17); to make this more general
version eventually easier to reach we present the proof for open sets in Rn in a fairly general way (a proof more
speciﬁcally adapted to Rn can be found in Appendix A of Madsen-Tornehave). In particul ar we bring in the
following deﬁnition from point-set topology:
Deﬁnition 2.8. A topological space X is called second-countable if there is a countable basis for the topology of
X.
In other words, there should be a collection {On|n ∈ N} of open sets with the property that if U is open and
x ∈ U then x ∈ On ⊂ U for some n. For example Rn has this property (take the base to consist of open balls
centered at points with rational coordinates and having rat ional radius), as does any open subset of Rn (just use
those rational balls that are contained in the open subset). Part of our eventual deﬁnition will require that any
smooth manifold also has this property.
Lemma 2.9. Let X be a second-countable locally compact Hausdorﬀspace. Then there is a sequence of compact
sets {Ki}∞
i=1 and a sequence of open sets {Hi}∞
i=1 such that
• Ki ⊂ Hi
• X = ∪∞
i=1Ki = ∪∞
i=1Hi
• If j ≥ i + 3 then Hi ∩ H j = ∅.
Proof. First note that a second-countable, locally compact space h as a countable base for its topology which
consists of open sets with compact closure. Indeed, given a c ountable base B, by local compactness any point
x ∈ X has a neighborhood Ox with compact closure, and there will be some V ∈ B such that x ∈ V ⊂ Ox;
evidently
V will be compact, and the set of all V that can be obtained in this fashion will still be a base for th e
topology (and will be contained in the original B, so will be countable).
So let {Ui}∞
i=0 be a base for the topology which is countable and such that each
Ui is compact. In particular the
Ui cover X. We claim now that there is a sequence{Gi}∞
i=0 of open sets with each
Gi compact, such that Gi ⊂ Gi+1
and such that ∪∞
i=0Gi = X. Speciﬁcally, the Gi will have the form
Gi = U0 ∪ · · · ∪U ji
for a certain increasing sequence of natural numbers { ji}. To construct the sequence { ji}, we let j0 = 0 (so
G0 = U0), and assuming that we have chosen jk, so that Gk = U1 ∪ · · · ∪U jk, we note that
Gk is compact since the
Ui are, and so since the Ui cover X there must be some jk+1 > jk so that Gk ⊂ ∪ jk+1
i=1 Ui. Inductively choosing the
jk in this fashion results in a sequence Gi satisfying the required properties (the fact that the Gi cover X follows
from the fact that the Ui do, and the fact that ji → ∞ since the ji are a strictly increasing sequence of natural
numbers).
To construct Ki and Hi, let K1 = G1, W1 = G2, and, for i ≥ 2, let Ki = Gi \ Gi−1 and Hi = Gi+1 \ Gi−2. These
are easily seen to satisfy the required properties.
□
Proof of Theorem 2.6. Let Ki and Hi be subsets of U as in Lemma 2.9 (applied with X = U), and ﬁx any i. For
all x ∈ Ki we may choose αx ∈ A and ǫx > 0 so that B2ǫx(x) ⊂ Vαx ∩ Hi. Then the collection of open balls
{Bǫx(x)|x ∈ Ki} covers Ki, so it has a ﬁnite subcover.
Now letting i vary and taking the union of all of these ﬁnite subcovers, we have a countable collection of balls
{Bk}∞
k=1 that covers X, and such that where ˜Bk denotes the ball with the same center as Bk but twice the radius,

MATH 8210, FALL 2011 LECTURE NOTES 9
there are αk and ik such that ˜Bk ⊂ Vαk ∩ Hik. (While there may be more than one such αk and ik—there might
even be uncountably many possibleαk—we speciﬁcally choose one αk and ik for every k. For convenience let us
take ik to be the i for which Bk was a member of the ﬁnite subcover of Ki, so that in particular for any i there are
just ﬁnitely many k with ik = i.)
I claim that the balls ˜Bk form a locally ﬁnite cover of U, i.e. that any point x ∈ U has a neighborhood Ox which
meets just ﬁnitely many of the ˜Bk. Indeed we could use for Ox any neighborhood of x with compact closure. For
then Ox is contained in the union of just ﬁnitely many of the sets Hi, say Ox ⊂ H1 ∪ · · · ∪Hr. But the Hi have the
property that Hi ∩ Hm = ∅whenever m ≥ i + 3, and so Ox ∩ Hm = ∅for m ≥ r + 3. Consequently ˜Bk ∩ Ox = ∅
unless k is one of the ﬁnitely many indices having ik ≤ r + 2.
We can now construct the desired functions. First, for each k, let ψk : U → [0, 1] be a smooth function
identically equal to 1 on Bk and such that supp (ψk) ⊂ ˜Bk; such ψk exist by Corollary 2.5. By the previous
paragraph, any point in U has a neighborhood which is disjoint from the supports of all but ﬁnitely many of the
ψk; consequently
ψ =
∞∑
k=1
ψk
is a well-deﬁned, smooth function. Moreoverψ> 0 everywhere, since the (smaller) balls Bk cover U. So for any
k we have a well-deﬁned, smooth function ψk
ψ , and obviously ∑
k
ψk
ψ = 1.
Now deﬁne
χα =
∑
k:αk=α
ψk
ψ.
Since ˜Bk ⊂ Vα whenever α = αk, we have supp (χα) ⊂ Vα for all α. Since any point has a neighborhood
intersecting the support ofψk for only ﬁnitely many k, there will be just ﬁnitely manyχα whose supports intersect
this neighborhood (namely, just thoseα which equalαk for one of these k). Finally, we clearly have
∑
α
χα =
∑
α
∑
k:αk=α
ψk
ψ =
∑
k
ψk
ψ = 1.
□
As essentially a special case we get a direct analogue of Urysohn’s Lemma:
Corollary 2.10. If A ⊂ U ⊂ Rn with A closed and U open, there is a C ∞ function f : Rn → [0, 1] with f |A = 1
and supp ( f ) ⊂ U.
Proof. Let {χ1,χ 2} be a partition of unity subordinate to the cover {U, Rn \ A} of Rn, and let f =χ1. I leave it to
you to conﬁrm the desired properties. □
Exercise 2.11. a) Let U ⊂ Rn be open, let p ∈ U, and let X be a vector ﬁeld on U (use the interpretation of X
as a derivation from C∞(U) to itself). Prove that one can obtain a well-deﬁned tangent vector (in the sense of
a derivation Op → R) Xp by the following prescription: If [ f, V] ∈ O p, let ˜f ∈ C∞(U) be a function such that
[ ˜f, U] = [ f, V]. Then X ˜f ∈ C∞(U), and we set
Xp([ f, V]) = (X ˜f )(p)
(Part of the problem is showing that ˜f exists, and moreover that Xp([ f, V]) is independent of the choice of such
a ˜f .)
b) If in coordinates we have X = ∑
i fi ∂
∂xi
, prove that Xp = ∑
i fi(p) ∂
∂xi
.

10 MIKE USHER
3. S mooth manifolds
Deﬁnition 3.1. Let n ∈ N. An n -dimensional topological manifold (or “topological n-manifold”) is a second-
countable Hausdorﬀspace M with the property that, for all m ∈ M, there is a neighborhood U ⊂ M of m and a
homeomorphismφ: U → V where V ⊂ Rn is an open subset.
Remark 3.2. Of course, by replacing V with a small open ball B ⊂ V aroundφ(p) and U withφ−1(B), we could
just as well require the image ofφ is an open ball in Rn rather than an arbitrary open set. In turn, since any open
ball in Rn is homeomorphic (and indeed di ﬀeomorphic) to Rn, we could equally well require the images of the
maps φ in Defnition 3.1 to all be Rn— i.e., a topological n-manifold is a second-countable Hausdor ﬀspace in
which every point has a neighborhood homeomorphic to Rn.
Deﬁnition 3.3. Let M be a topological n-manifold, and let k be either a positi ve integer or ∞. A C k atlas on M
is a collection A = {(Uα,φα)|α ∈ A} where
• The Uα are open subsets of M, and ∪α∈AUα = M.
• Eachφα : Uα → Rn is a homeomorphism from Uα to the open subsetφα(Uα) ⊂ Rn, and
• Ifα,β ∈ A are such that Uα ∩ Uβ /nequal∅, then
φβ ◦φ−1
α : φα(Uα ∩ Uβ) →φβ(Uα ∩ Uβ)
is of class Ck.
The mapsφα : Uα → Rn are called coordinate charts (or sometimes “coordinate patches”) for the atlas A.
Exercise 3.4. (a) If A and B are Ck atlases on a topological n-manifold, write A ∼ B if A ∪ B is also a Ck
atlas. Prove that ∼ deﬁnes an equivalence relation on the set of all atlases.
(b) If A = {(Uα,φα)} is a Ck atlas for M, let Amax denote the set of all pairs ( U,φ ) where φ: U → Rn is
a homeomorphism from an open subset U ⊂ M to an open subset φ(U) ⊂ Rn, and such that whenever
U ∩ Uα /nequal∅the mapφ ◦φ−1
α : φα(U ∩ Uα) →φ(U ∩ Uα) is Ck and has inverse which is Ck. Prove that
Amax is an atlas containing A, and is maximal in the sense that it contains every other atlas that contains
A. Deduce that if A ∼ B then Amax = Bmax.
Deﬁnition 3.5. A C k-diﬀerentiable structure on a topological n-manifold is a maximal atlas A on M ( i.e., an
atlas such that, in the notation of Exercise 3.4(b), A = Amax). An n -dimensional Ck manifold is a topological
n-manifold M equipped with a Ck-diﬀerentiable structure. A C∞ manifold will also be called asmooth manifold,
and a C∞-diﬀerentiable structure will also be called a smooth structure.
Remark 3.6. We will almost exclusively discusssmooth (i.e., C∞) manifolds in this course. This is partly justiﬁed
by the fact that, for 1 ≤ k < ∞, any Ck manifold is Ck-diﬀeomorphic to a C∞ manifold (there is a proof in
Hirsch’s book Diﬀerential Topology). On the other hand there is some real loss of generality in lo oking at C∞
(or even just C1) manifolds rather than just topological (C0) manifolds, as there are topological manifolds which
are not homeomorphic to any C1 manifold. Examples of such are rather complicated—Kervaire constructed a
10-dimensional one in 1960, and the lowest dimension in which any occur is 4, where there are examples due to
Freedman in the early 1980s.
Remark 3.7. The deﬁnition is that a smooth manifold is a certain kind of topological space equipped with a max-
imal C∞ atlas. A maximal atlas is a rather unwieldy object—except in t rivial cases it will consist of uncountably
many coordinate charts. But in view of Exercise 3.4 it is rare ly if ever necessary to really work with a maximal
atlas—you just have to specify one atlas (often with a small, ﬁnite number of charts), and then t his canonically
determines a maximal atlas by the construction in Exercise 3.4(b). One could equally well deﬁne a smooth man-
ifold as a topological manifold equipped with an equivalenc e class of atlases, where the equivalence relation is
the one from Exercise 3.4(a). One advantage of a maximal atla s is that “everything that could be a coordinate
patch is,” so that if you have to work in local coordinates youhave a great variety of possible coordinate systems
to work in and you can choose whichever works best for your purposes at the time.

MATH 8210, FALL 2011 LECTURE NOTES 11
Example 3.8. As the simplest possible example, we note that Rn is canonically a smooth manifold: take an atlas
consisting of the single pair (1 Rn, Rn) where 1 Rn denotes the identity map. As noted in Remark 3.7 specifying
this (very small!) atlas canonically determines a maximal atlas (i.e., a diﬀerentiable structure).
Of course we could just as well have replaced Rn by any open subset U of Rn, using the atlas {(1U, U)} to
make U into a smooth manifold. More generally, ifM is any smooth manifold with atlas{(φα, Uα)} and if U ⊂ M
is an open subset then we naturally get an atlas on U, namely {(φα|U∩Uα, U ∩ Uα)}.
I promised at the outset that a smooth manifold would be the ki nd of space on which it is possible to do
something resembling calculus. In particular if M is a smooth m-manifold it should be possible to speak of
diﬀerentiable functions from M to Rn, or vice versa, for any n (and, more generally, if M and N are two smooth
manifolds we should be able to speak of di ﬀerentiable functions from M to N). The principle is simple: one
checks the diﬀerentiability of a function by using coordinate charts to tu rn the function into one whose domain
and range are open subsets of Euclidean space, where we already have a notion of diﬀerentiability.
Deﬁnition 3.9. Let M be an m-dimensional smooth manifold, with (maximal) atlas {(φα, Uα)|α ∈ A}.
• If f : M → Rn is a continuous function, we say f is of class C k, and write f ∈ Ck(M, Rn), if for every
α ∈ A the function
f ◦φ−1
α : φα(Uα) → Rn
is of class Ck (note that f ◦φ−1
α is a function from an open set in Rm to Rn, so the notion of f ◦φ−1
α being
of class Ck is well-deﬁned from multivariable calculus).
• If V ⊂ Rm is an open subset and g : V → M is a continuous function we say that g is of class C k, and
write Ck(V, M), if for allα ∈ A the function
φα ◦ g: g−1(Uα) → Rm
is of class Ck.
• Suppose that N is an n-dimensional smooth manifold, with (ma ximal) atlas {ψβ, Vβ)|β ∈ B}. If f : M →
N is a continuous function, we say that f is of class C k if, for all α,β such that f (Uα) ∩ Vβ /nequal∅, the
function
ψβ ◦ f ◦φ−1
α : φα(Uα ∩ f −1(Vβ)) → Rn
is of class Ck (as a function from an open subset of Rm to Rn).
The appropriate notion of isomorphism of smooth manifolds is the following:
Deﬁnition 3.10. Let M and N be C k-manifolds. A C k-diﬀeomorphism from M to N is a smooth, bijective map
f : M → N such that f −1 is also smooth.
As mentioned earlier, we will generally just consider the C∞ case—as such a “di ﬀeomorphism” will, unless
otherwise indicated, mean a C∞ diﬀeomorphism.
Of course, it would be a pain to actually check that Deﬁnition 3.9 is satisﬁed since maximal atlases are very
large. But the following exercise shows that the Ck property can be checked more easily (and also implies that,
viewing Rn as a smooth manifold, the third part of the above deﬁnition co ntains the ﬁrst two as special cases).
This exercise is intended in part to demonstrate the role of t he assumption on the functions φβ ◦ φ−1
α in the
deﬁnition of an atlas.
Exercise 3.11. Let M and N be smooth manifolds, and let f : M → N be a continuous function. Prove that
f ∈ Ck(M, N) if and only if the following holds: For each x ∈ M, there exists a coordinate chart φ: U → Rm
from the atlas for M and a coordinate chartψ: V → Rn from the atlas for N such that x ∈ U, f (x) ∈ V and
ψ ◦ f ◦φ−1 : φ(U ∩ f −1(V)) → Rn
is of class Ck.

12 MIKE USHER
Thus in practice to show that a map is Ck we just need to ﬁnd collections of charts covering the manifo lds in
terms of which the map is a Ck map between Euclidean spaces, rather than checking the cond ition on the entire
maximal atlas. Another way of saying this is that the two appearances of the word “(maximal)” in Deﬁnition 3.9
are unnecessary—we can just use any atlases (possibly quite s mall) to check the Ck condition.
Example 3.12. One can see that the n-dimensional sphere
S n =






(x0, x1,..., xn) ∈ Rn+1
⏐
⏐
⏐
⏐
⏐
⏐
⏐
n∑
i=0
x2
i = 1







is a smooth manifold by using stereographic projections. Of course the subspace topology on S n induced by its
inclusion into Rn+1 makes S n into a second-countable Hausdorﬀspace. We construct a smooth atlas on S n with
two charts: deﬁne
U− = {(x0,..., xn) ∈ S n|x0 /nequal1}
U+ = {(x0,..., xn) ∈ S n|x0 /nequal−1}
In other words, U− and U+ are the complements of the north and south poles, respectively. Clearly S n = U− ∪U+.
Now deﬁneφ− : U− → Rn by
φ−(x0,..., xn) =
( x1
1 − x0
,..., xn
1 − x0
)
and similarly deﬁneφ+ : U+ → Rn by
φ+(x0,..., xn) =
( x1
1 + x0
,..., xn
1 + x0
)
Soφ− can be visualized as sending a pointp ∈ S n\{north pole} to the point of intersection between the hyperplane
{x0 = 0} and the unique line through the north pole and p. It is clear from the formulas that φ− and φ+ are
continuous. Both of them are in fact homeomorphisms to Rn: one ﬁnds that the inverses φ−1
± Rn → U± are given
by the formula
φ−1
± (y1,..., yn) =





±1 − ∑y2
i
1 + ∑y2
i
, 2y1
1 + ∑y2
i
,..., 2yn
1 + ∑y2
i





.
Since the inverses are continuous the φ± are indeed homeomorphisms to Rn. What remains is to check that
the “transition function”φ+ ◦φ−1
− : φ−(U+ ∩ U−) → φ+(U+ ∩ U−) is C∞, and likewise that φ− ◦φ−1
+ is C∞ (of
course, the second of these is the inverse of the ﬁrst). Now U+ ∩ U− is the complement of the two (north and
south) poles of S n, i.e. U+ ∩ U− = S n \ {(±1, 0,..., 0)}. Now
φ+(1, 0,..., 0) =φ−(−1, 0,..., 0) = (0,..., 0),
so
φ−(U+ ∩ U−) =φ+(U+ ∩ U−) = Rn \ {(0,..., 0)}.
For any (y1,..., yn) ∈ Rn \ {(0,..., 0)} we have
φ+ ◦φ−1
− (y1,..., yn) =φ+






∑y2
i − 1
∑y2
i + 1, 2y1
∑y2
i + 1,..., 2yn
∑y2
i + 1






=














2∑y2
i
∑y2
i + 1






−1
2y1
∑y2
i + 1,...,






2∑y2
i
∑y2
i + 1






−1
2yn
∑y2
i + 1








=






y1
∑y2
i
,..., yn
∑y2
i





.
Since this map is deﬁned only on the complement of the origin, it is clearly C∞ (the components are quotients of
nonvanishing C∞ functions), and its inverse (which as noted earlier isφ− ◦φ−1
+ ) is evidently C∞ as well (actually

MATH 8210, FALL 2011 LECTURE NOTES 13
if you look at the formula you see that it turns out that this ma p is equal to its own inverse). Thus we’ve shown
that the transition functions for our atlas are C∞, completing the proof that S n is a smooth manifold.
Example 3.13. Recall that the n-dimensional real projective space RPn is the space of lines through the origin in
Rn+1. This is given the structure of a (second-countable, Hausdorﬀ) topological space by identifying it as
RPn = Rn+1 \ {⃗0}
⃗v ∼λ⃗v ∀⃗v ∈ Rn+1 \ {0},λ ∈ R \ {0}
and using the quotient topology. Thus a general element of RPn+1 can be written as an equivalence class
[x0,..., xn] for some xi ∈ R with not all x i = 0, and we have [ x0 : · · ·: xn] = [y0 : · · ·: yn] i ﬀthere is
λ /nequal0 so that yi =λxi for all i. (The xi are called “homogeneous coordinates.”)
We now put a diﬀerentiable structure on RPn, making it a smooth n-manifold. For i = 0,..., n let
Ui = {[x0,..., xn] ∈ RPn|xi /nequal0}
(of course, the truth or falsehood of the statement that xi /nequal0 is independent of which representative of the
equivalence class we choose). The Ui are open sets (why?), and RPn = ∪n
i=0Ui since any element of RPn has at
least one of its homogeneous coordinates nonzero.
It shouldn’t be too hard to convince yourself that each of the open sets Ui is homeomorphic to Rn: for
example for i = n, an element of x ∈ Un has form [ x0 : · · ·: xn] where xn /nequal0, and since xn /nequal0 we
can simultaneously multiply all of the xi by 1
xn
—this doesn’t change the equivalence class, but changes the
last homogeneous coordinate to 1. Thus Un can be identiﬁed with the set of tuples ( x0,..., xn−1, 1), which is
equivalent to Rn.
To make the discussion in the previous paragraph more precis e, we introduce charts φi : Ui → Rn. Namely,
deﬁne
φi : Ui → Rn
φi([x0 : · · ·: xn]) =
(x0
xi
,..., xi−1
xi
, xi+1
xi
,..., xn
xi
)
.
This map is certainly well-deﬁned, since multiplying all en tries of ( x0,..., xn) by the same scalar λ does not
aﬀect the ratios x j/xi. Moreover we see thatφi is bijective, with inverse given by
φ−1
i (y0,..., yi−1, yi+1,..., yn) = [y0 : · · ·, yi−1 : 1 : yi+1 : · · ·: yn].
Bothφi andφ−1
i are continuous—of course to see this one has to think a little b it about the quotient topology, but
it’s not hard and is left to you.
So we have a covering RPn = ∪n
i=0Ui by open sets with homeomorphisms φi : Ui → Rn. It remains to check
that the transition functions φi ◦φ−1
j : φ j(Ui ∩ U j) → φi(Ui ∩ U j) are smooth. This follows quickly from the
formulas that we’ve already written down: assuming thati< j
φi ◦φ−1
j (y0,..., y j−1, y j+1,..., yn) =φi([y0 : · · ·: y j−1 : 1 : y j+1 : · · ·: n])
=
(y0
yi
,..., yi−1
yi
, yi+1
yi
,..., y j−1
yi
, 1
yi
, y j+1
yi
,..., yn
yi
)
.
Of course the case that i > j diﬀers from this only in the ordering of i and j in the above formula. Now on the
open subsetφ j(Ui ∩ U j) ⊂ Rn we will have yi /nequal0, soφi ◦φ−1
j is indeed smooth onφ j(Ui ∩ U j), as required. Thus
{(φi, Ui) : i = 0,..., n} forms a C∞ atlas for RPn, making RPn into a smooth manifold.
Fairly easy modiﬁcations of this argument show that the comp lex projective space CPn is a smooth 2 n-
manifold, and that the quaternionic projective space HPn is a smooth 4n-manifold.
Exercise 3.14. Recall that another way of describing RPn is as a quotient of S n by the equivalence relation
which identiﬁes any x ∈ S n ⊂ Rn+1 with −x. Thus we have a quotient projection π: S n → RPn. Prove that
π ∈ C∞(S n, RPn).

14 MIKE USHER
Exercise 3.15. (a) If M and N are smooth manifolds, construct a C∞ atlas on the product M × N (thus M × N has
the structure of a smooth manifold).
(b) Let M be a Hausdorﬀspace, and suppose that we can write M = U ∪ V where U and V are open sets, and
both U and V are smooth manifolds. Since U ∩V is an open subset ofU, it inherits a diﬀerentiable structure from
U; likewise U ∩ V inherits a diﬀerentiable structure from V. Assume that these two di ﬀerentiable structures on
U ∩ V are the same. Prove that one can then construct a smooth structure on M such that the inclusions U → M
and V → M are both smooth maps.
(c) Prove that for any g the compact surface of genus g (and no boundary) can be given the structure of a
smooth manifold (Hint: The case g = 0 is covered by Example 3.12, and g = 1 follows from Example3.12 and
part (a). Now repeatedly use (b) together with the fact that a n open subset of a smooth manifold is naturally a
smooth manifold.)
Remark 3.16. In our examples we’ve brushed over the question of whether the smooth structures on these spaces
are unique. This is an important but di ﬃcult question; a fair amount is now known, but the proofs are g enerally
beyond the scope of this course. It’s known that in any dimens ion n ≤ 3, every topological n-manifold has a
unique smooth structure; in particular the smooth structur es on surfaces from the exercise above are the only
possible ones. Things become more complicated beginning in (and especially in) dimension 4: in fact there are
uncountably many distinct smooth structures onR4, and there are many compact 4-manifolds with inﬁnitely many
smooth structures, and none that are currently known to have just one smooth structure (though as mentioned
earlier there are some topological 4-manifolds with no smooth structures). For spheres, once n ≥ 7 there is
typically more than one smooth structure on S n; the ﬁrst “exotic” structure on S 7 was a big surprise when it was
discovered by Milnor in 1956. It’s still a major open questio n whether there are any smooth structures on S 4
other than the standard one.
We now record a result asserting the existence of partitionsof unity subordinate to covers of smooth manifolds:
Theorem 3.17. Let M be a smooth manifold and let {Vα|α ∈ A} be a collection of open subsets of M with
∪α∈AVα = M. Then there is a smooth partition of unity on M subordinate t o the cover {Vα}, i.e., a collection
{χα|α ∈ A} where
• Eachχα ∈ C∞(M), with 0 ≤χα(x) ≤ 1 for all x ∈ M
• For allα, supp (χα) ⊂ Vα
• For any x ∈ M there is a neighborhood Ox of x such that Ox ∩ supp (χα) = ∅for all but ﬁnitely manyα
• ∑
αχα = 1
Proof. The special case in which M is an open subset of Rn was proven as Theorem 2.6. That proof carries over
directly to the more general case now that we have the appropr iate deﬁnitions. Indeed, a smooth manifold M is
by deﬁnition second-countable and Hausdor ﬀ, and is certainly locally compact (any point has a neighborh ood
whose closure is homeomorphic to a closed ball in Rn and so is compact), so Lemma 2.9 applies to produce a
sequence of compact sets Ki and open sets Hi. These sets can then be used just as they are used in the proof
of Theorem 2.6. Basically all that needs to be changed is the ﬁ rst paragraph of that proof: if x ∈ Ki we can
ﬁnd a neighborhood of x having the form φ−1(B2rx(φ(x))) which is contained in Vαx ∩ Wi for some αx, where
φ: U → Rn is some chart (depending on x) whose domain U contains x. The sets φ−1(Brx(x)) then cover Ki,
and this cover has a ﬁnite subcover. Aggregating these ﬁnite subcovers gives a countable sequence {Bk} of open
sets covering M; the Bk are preimages of balls in Rn by local charts φ, and where ˜Bk is the preimage of the ball
with the same center and twice the radius we will have Bk ⊂ Vαk ∩ Wik for appropriateαk, ik. Moreover there is a
smooth functionψk supported in ˜Bk and identically equal to one on Bk—just precompose an appropriate smooth
function on Rn given by Corollary 2.5 withφ−1. The proof of Theorem 2.6 then applies verbatim. □
Partitions of unity are very useful in the study of smooth manifolds. For a brief indication of why, consider the
case in which the cover {Vα} consists of the domains of coordinate chartsφα : Vα → Rn (of course, by deﬁnition,

MATH 8210, FALL 2011 LECTURE NOTES 15
any smooth manifold admits such a cover). If f ∈ C∞(M), then we can write
f =







∑
α
χα






 f =
∑
α
(χα f ).
Now for anyα the functionχα f is supported in the set Vα, which is identiﬁed by φα with an open subset in Rn.
So we can hope to analyze f by decomposing it as a sum of smooth functions χα f , where each of these smooth
functions can (at least individually) be treated as though i t were just a compactly supported smooth function on
Rn. To get slightly ahead of myself, the same applies when f is, instead of a smooth function, a diﬀerential form.
3.1. Tangent spaces. If M is a smooth manifold and m ∈ M, we will deﬁne a vector space TmM called the
tangent space to M at m . As suggested at the start of these notes, there are various w ays of trying to do this,
any of which can be considered to be inspired by the special ca se in which M is an open subset of Rn. For
instance we could deﬁne a tangent vector v at m to be an equivalence class [γ] where γ: ( −ǫ,ǫ ) → M is a C∞
map from an open interval around 0 to M withγ(0) = m, with two curves γ1,γ 2 considered to be equivalent if
d
dt (φα ◦γ1)(0) = d
dt (φα ◦γ1)(0) (as vectors in Rn) for one (and hence every—why?) chart φα : Uα → Rn whose
domain contains m. However, for deﬁniteness we will adopt the third interpret ation from the start of the notes:
a tangent vector at m will be, by deﬁnition, a derivation from the algebra of germs of smooth functions deﬁned
near m to R.
So just as earlier we consider pairs ( f, V) where V is an open neighborhood of m in M and f : V → R is C∞
(this notion is well-deﬁned since V, being an open set in a smooth manifold, is itself a smooth manifold, and we
have deﬁned the space of C∞ functions on a smooth manifold). Say that ( f1, V1) ∼ ( f2, V2) if and only if there is
an open set W with m ∈ W ⊂ V1 ∩ V2 and f1|W = f2|W. Let Om denote the set of equivalence classes; this inherits
addition, multiplication, and scalar multiplication from C∞(M) (for example, [ f, V][g, W] = [ f g, V ∩ W]).
Deﬁnition 3.18. TmM is deﬁned as the space of derivations v : Om → R, i.e., maps v such that
• v(c f + g) = cv( f ) + v(g) if c ∈ R and f, g ∈ O p
• v( f g) = f (m)v(g) + g(m)v( f ) if f, g ∈ Om
As indicated in the above deﬁnition we will often abuse notation slightly by just writing f for [ f, V]. Compat-
ibly with this abuse of notation, ifφ: M → N is a smooth map where N is another smooth manifold and m ∈ M,
if we write f for an element [ f, V] ∈ Oφ(m) (thus f is a function deﬁned on a neighborhood of f (m) in N), then
we will write f ◦φ for the element [ f ◦φ,φ −1(V)] ∈ O m. These sorts of abuse of notation are justiﬁed by the
fact that replacing the open set V by a diﬀerent neighborhood of φ(m) will not change either the element [ f, V]
(denoted f ) or the element [ f ◦φ,φ −1(V)] (denoted f ◦φ).
We record here the fact that, ifU ⊂ M is an open subset and m ∈ U, there is a canonical identiﬁcation of TmU
with TmM (convince yourself of this if it’s not obvious). Also, in case U is an open subset of Rn, our deﬁnition
coincides with the one from the start of these notes.
Deﬁnition 3.19. Ifφ: M → N is a smooth map between smooth manifolds and if m ∈ M, the derivative ofφ at
m (sometimes called the linearization ofφ at m is the map
φ∗ : TmM → Tφ(m)N
deﬁned by
(φ∗(v))( f ) = v( f ◦φ)
whenever f ∈ Oφ(m) and v ∈ TmM.
Sometimes it’s helpful to indicatem within the notation forφ∗, in which case we’ll write (φ∗)m. One also sees
the notation dφ or dmφ used to denote what we have calledφ∗.
Proposition 3.20. Where 1M is the identity map then for all m ∈ M, (1M)∗ : TmM → TmM is the identity map.
Also, ifφ: M → N and ψ: N → P are smooth maps then
(ψ ◦φ)∗ =ψ∗ ◦φ∗

16 MIKE USHER
Proof. The ﬁrst statement (about the identity) is obvious from the d eﬁnition. For the second, we have, if f ∈
Oψ◦φ(m),
((ψ ◦φ)∗v)( f ) = v( f ◦ (ψ ◦φ)) = v(( f ◦ψ) ◦φ) = (φ∗v)( f ◦ψ) = (ψ∗φ∗v)( f ).
□
Corollary 3.21. If m ∈ M where M is a smooth n-manifold, then dim TmM = n.
Proof. We can choose a coordinate chartφ: U →φ(U) where U is an open neighborhood of m. As noted earlier
we have TmM = TmU. By Proposition 3.20, ( φ−1)∗ ◦φ∗ = (φ−1 ◦φ)∗ is the identity map from TmU = TmM to
itself, and φ∗ ◦ (φ−1)∗ = (φ ◦φ−1)∗ is the identity map from Tφ(m)φ(U) to itself. Thus φ∗ is an isomorphism of
vector spaces from TmM to Tφ(m)φ(U), with inverse (φ−1)∗. We showed in Section 1 that, since φ(U) is an open
subset of Rn, dim Tφ(m)φ(U) = n, so the conclusion follows. □
Expanding a bit on the above proof, recall that we showed thatTφ(m)φ(U) consists precisely of mapsOφ(m) → R
taking the form g ↦→∑n
i=1 vi
∂g
∂xi
|φ(m). So since ( φ−1)∗ is an isomorphism, we conclude that, in the presence of a
chosen coordinate chartφ: U → Rn around m, a general element v ∈ TmM will be given by the formula
v( f ) =
n∑
i=1
vi
∂
∂xi
( f ◦φ−1)|φ(m).
When this is the case, we will say something along the lines of, “v is given in the coordinate chart φ by
v = ∑vi ∂
∂xi
.” Of course, the coeﬃcients vi will depend on the coordinate chart, not just on the tangent vector v.
Exercise 3.22. Letφ,ψ : U → Rn be two coordinate charts where U is an open subset of a smooth manifold M,
and let m ∈ U. If v is given in the coordinate chart φ by v = ∑vi ∂
∂xi
, and is given in the coordinate chart ψ by
v = ∑wi ∂
∂yi
, ﬁnd, with proof, an expression for the wi in terms of the vi and the mapsφ ◦ψ−1 and/orψ ◦φ−1.
So if M is a smooth n-manifold, we have associated to every point m ∈ M an n-dimensional vector space
TmM. A diﬀeomorphismφ: M → M′ induces an isomorphism of vector spacesφ∗ : TmM → Tφ(m)M′. However
there is (in general) no canonical way of identifying Tm1 M with Tm2 M for distinct point m1, m2 ∈ M (of course,
since the two vector spaces have the same dimension, they are isomorphic as vector spaces, just not canonically
so).
Relatedly, while choosing the point m ∈ M canonically determines the n-dimensional vector space TmM, it
does not canonically determine a basis for this vector space. One way of choosing a basis for TmM is suggested
above: choose a local coordinate chartφ: U → Rn around U; then a basis is given by the derivationsf ↦→∂
∂xi
( f ◦
φ−1)(p) for i = 1,..., n (the members of this basis are typically denoted by ∂
∂xi
. Di ﬀerent choices of coordinate
chart of course give rise to diﬀerent bases; the relationship between the bases is determined by Exercise 3.22.
The tangent bundle of a smooth manifold is, as a set, deﬁned to be the union
T M = ∪m∈M{m} × M.
For any subset S ∈ M (typically S will be open or closed) we deﬁne the “restriction of the tangent bundle to S ”
as
T M|S = ∪m∈S {m} × TmM.
Given a coordinate chartφ: U → Rn where U ⊂ M is open, we have a bijection Φ: T M|U →φ(U) × Rn given
by
Φ
(
m,
∑
vi
∂
∂xi
)
= (φ(m), v1,..., vn).
We can then deﬁne a topology on T M by requiring that each of these bijections be homeomorphism s—more
precisely, we take as a base for this topology the collection of subsets of the form Φ−1(V) where Φ: T M|U →
φ(U) × Rn is a map as above constructed from a coordinate chartφ and V ⊂φ(U) × Rn is open.

MATH 8210, FALL 2011 LECTURE NOTES 17
The various homeomorphisms Φ: T M|U →φ(U) × Rn associated to coordinate chartsφ: U →φ(U) in fact
form a C∞ atlas for T M. Indeed the domains T M|U certainly cover T M (since M is covered by coordinate charts)
and so we just need to check that the transition functions aresmooth. This latter fact follows from Exercise 3.22.
Indeed, if φα : Uα → Rn and φβ : Uβ : Uβ → Rn are two coordinate charts, then it should follow from your
computation in Exercise 3.22 that the transition function
Φβ ◦ Φ−1
α : φα(Uα ∩ Uβ) × Rn →φβ(Uα ∩ Uβ) × Rn
is given by
(4) Φβ ◦ Φ−1
α (x,⃗v) = (φβ ◦φ−1
α (x), gαβ(x)⃗v)
where gαβ is a certain smooth function which takes values in the group o f invertible n × n matrices. Thus the
transition functions are smooth, and so determine a smooth manifold structure on T M.
Of course, we have a projectionπ: T M → M which sends (m, v) to m. In terms of the local coordinate charts
Φon T M andφ on M,π just acts by the projection ofφ(U) × Rn onto its ﬁrst factor; thusπ is a smooth map.
Summing up, out of an n-dimensional smooth manifold M we have constructed a 2 n-dimensional smooth
manifold T M, equipped with a projection π: T M → M. The “ﬁbers” π−1({m}) of π are canonically identiﬁed
with the tangent spaces TmM, and thus are n-dimensional vector spaces. Moreover there is an atlas on T M such
that the transition functions respect the vector space stru ctures on the ﬁbers in the sense that they are given by
a formula of the shape (4) where each gαβ(x) is a linear map. T M is thus an example of what is called a vector
bundle; we will see more examples of vector bundles as the course proceeds.
3.2. Vector ﬁelds. Consistently with what was done in Section 1, we make the following deﬁnition:
Deﬁnition 3.23. Let M be a smooth manifold and U ⊂ M an open subset. A vector ﬁeld on U is a derivation
X : C∞(U) → C∞(U) (i.e., X obeys X(c f + g) = cX f + Xg and X( f g) = f Xg + gX f if f , g ∈ C∞(U), c ∈ R). We
denote the space of vector ﬁelds on U by X(U).
Just as in Section 1, we can scalar multiply, add, and take the commutators of derivations from C∞(U) to
itself, so X(U) naturally has the structure of a Lie algebra.
A vector ﬁeld on U should have another interpretation as a “smoothly-varying ” choice of tangent vector
at m for each m ∈ M. We now lay out how this works. For U ⊂ M we have a (restricted) tangent bundle
π: T M|U → U.
Deﬁnition 3.24. A smooth section of T M over U is a smooth map s : U → T M|U such thatπ ◦ s is the identity.
We write Γ(U, T M) for the space of smooth sections of T M over U.
In other words, s(m) ∈ TmU for all p ∈ U; the notion that the tangent vectors should vary smoothly isencoded
in the requirement that s should be a smooth map. Since TmU is a vector space, we get vector space operations
on Γ(U, T M) deﬁned by ( cs)(m) = c(s(m)) and ( s1 + s2)(m) = s1(m) + s2(m) (there’s something to show here,
namely that for instance the sum of two smooth sections is sti ll smooth, but it’s not hard to check this). One
important example of a section of T M (or more generally of any vector bundle) is the zero section, deﬁned by
s(m) = 0 ∈ TmM for all p. (To see that this is smooth, just note that in the local coord inatesφ(U) × Rn ⊂ R2n
described earlier the map is given by x ↦→(x, 0) which is obviously a smooth map from Rn to R2n).
Recall Exercise 2.11, to which the following gives a solution:
Proposition 3.25. Let M be a smooth manifold, U ⊂ M open, m ∈ U, and X ∈ X (U). Then the following
prescription uniquely speciﬁes an element X m ∈ TmM. For any [ f, V] ∈ O m, choose a ˜f ∈ C∞(U) such that
[ ˜f, U] = [ f, V], and deﬁne Xm([ f, V]) = (X ˜f )(m).
Proof. First of all we need to show that for any [ f, V] ∈ O m (in other words, V is an open set around m and
f is a smooth function on V) there is a smooth function ˜f deﬁned throughout U and coinciding on with f
on some neighborhood G of m. To see this, note that we can ﬁnd a coordinate chart φ: W → Rn around
m and r > 0 so that
φ−1(B2r(φ(m))) ⊂ V. Take a partition of unity {χ1,χ 2} subordinate to the open cover

18 MIKE USHER
{φ−1(B2r(φ(m))), M \φ−1(Br(φ(m)))} of M. Then let ˜f = χ1 f ; initially this function is only deﬁned on V, but
since it has support contained in a compact subset of V we may extend it by zero to obtain a smooth function on
all of M. Since χ1 +χ2 = 1 andχ2 vanishes onφ−1(Br(φ(m))), ˜f coincides with f onφ−1(Br(φ(m))), as desired.
We now show that the value ( X ˜f )(m) is independent of the choice of ˜f with [ ˜f, U] = [ f, V]. If ˜g is another
such choice, there is a neighborhood W of m such that ˜f |W = ˜g|W. Let O be a neighborhood of m such that
m ∈ O ⊂ W (for instance take O to be the preimage of a small ball in a coordinate chart, as in t he previous
paragraph). Just as in the previous paragraph we can ﬁnd a smo oth function χ: M → R such that χ|O = 1 and
supp (χ) ⊂ W. Let β = 1 −χ, soβ vanishes identically on the neighborhood O of m and is equal to 1 outside W.
Hence
(1 −β2) ˜f = (1 −β2)˜g
(both sides are zero everywhere that ˜f /nequal˜g). On the other hand(
X(β2 ˜f )
)
(m) =β(m)
(
X(β ˜f )
)
(m) +β(m) ˜f (m) (Xβ) (m) = 0
and similarly (
X(β2 ˜g)
)
(m) = 0.
Hence
(X ˜f )(m) =
(
X(β2 ˜f )
)
(m) +
(
X((1 −β2) ˜f )
)
(m)
=
(
X((1 −β2) ˜f )
)
(m) =
(
X((1 −β2)˜g)
)
(m)
=
(
X(β2 ˜g)
)
(m) +
(
X((1 −β2)˜g)
)
(m) = (X ˜g)(m).
This conﬁrms that the prescription of the proposition gives a well-deﬁned map Xm : Om → R. It remains to
check that Xm is a derivation. But this follows easily from the derivation property for X. Given [ f, V], [g, W] ∈
Om, if we use ˜f ∈ C∞(U) to compute Xm[ f, V] = (X ˜f )(m) and ˜g ∈ C∞(U) to compute Xm[g, V] = (X ˜g)(m) then
we can use ~f g = ˜f ˜g to compute Xm([ f, V][g, W]) (of course we could make other choices for ~f g, but the start of
the proof ensures that this would result in the same value for Xm([ f, V][g, W])). Then the derivation property for
X shows
Xm([ f, V][g, W]) =
(
X(~f g)
)
(m) = f (m)(X ˜g)(m) + g(m)(X ˜f )(m)
= f (m)Xm[g, W] + g(m)Xm[ f, V].
R-linearity is proved in essentially the same way, completing the proof that Xm ∈ TmM.
□
We now show that giving a vector ﬁeld (in the sense of a derivat ion on the space of smooth functions) is
exactly the same as giving a smooth section of the tangent bundle.
Theorem 3.26. Let U be an open subset of the smooth manifold M. A bijection F : X(U) → Γ(U, T M) may be
deﬁned as follows. For X ∈ X(U), set F (X) equal to the map s X : M → T M deﬁned by sX(m) = Xm (where Xm
is given by Proposition 3.25).
Proof. First we need to show that F is well-deﬁned—we certainly have a well-deﬁned function sX : M → T M
for any X ∈ X(U), and sX is a section in the sense that π ◦ sX = 1M, but we also need to check that sX is smooth
in order for F to take values in the space Γ(U, T M) of smooth sections.
To see this, note ﬁrst of all that a functionf between two smooth manifolds is smooth if and only if the domain
can be covered by open sets to each of which f restricts as a smooth function. If m ∈ M, let φ: V → Rn be a
coordinate chart with m ∈ V ⊂ U, and for r > 0 small enough that B2r(φ(m)) ⊂ φ(V) let Wm = φ−1(Br(φ(m))).
We will show that sX|Wm is smooth, which suﬃces since any point in M has a neighborhood of the form Wm.
In this direction, let χ: M → R be a smooth function with χ|
Wm
= 1 and supp (χ) ⊂ V. For any q ∈ Wm and
f ∈ Oq we have
(sX(q))( f ) = Xq( f ) = Xq(χ f )

MATH 8210, FALL 2011 LECTURE NOTES 19
since f andχ f coincide on a neighborhood (namely Wm) of q.
Now for each j = 1,..., n write g j = (x j ◦ψ) ·χ ∈ C∞(M). Then on Wm, g coincides with the jth coordinate of
the chartψ|Wm : Wm → Rn. We know that, for each q ∈ Wm, since Xq ∈ TqM we can express Xq in the coordinate
chartψ as Xq = ∑
i vi(q) ∂
∂xi
|q for some vi(q) ∈ R. Evaluating on the functions g j we see that, for each j,
v j(q) = (Xg j)(q).
Thus the functions v j : Wm → R are each smooth. Now in terms of the local coordinates for the tangent bundle
described at the end of the previous subsection, the map sX is given within Wm by the formula (where x ∈
ψ(Wm) ⊂ Rn)
x ↦→
(
x, v1(ψ−1(x)),..., vn(ψ−1(x))
)
.
This map is smooth since the v j are smooth. Thus sX|Wm is smooth, and so sX is smooth since U can be covered
by open sets of the form Wm.
Now that we have shown the map F : X(U) → Γ(U, T M) to be well-deﬁned, we show that it is bijective.
Suppose that X, Y ∈ X (U) are two distinct vector ﬁelds on U. Then there is f ∈ C∞(U) and m ∈ U such that
(X f)(m) /nequal(Y f)(m). But then [ f, U] is a well-deﬁned element of Om with Xm([ f, U]) /nequalYm([ f, U]), and thus
Xm /nequalYm, i.e. s X(m) /nequalsY(m). Thus F is injective.
Finally suppose that s ∈ Γ(U, T M); we must ﬁnd X ∈ X (U) so that sX = s. If f ∈ C∞(U) then for all m we
have an element [ f, U] ∈ O m and so a real number ( s(m))([ f, U]). This determines a function X f : U → R by
the formula (X f)(m) = (s(m))([ f, U]). The derivation properties X(c f + g) = cX f + Xg and X( f g) = f Xg + gX f
follow directly from the fact that each s(m) is a derivation from Om to R; however we still need to check that
X f ∈ C∞(U) for any f ∈ C∞(U). In a local coordinate chart ψ: V → Rn, the tangent vectors s(m) for m ∈ V
are represented as s(m) = ∑vi(m) ∂
∂xi
, where the functions vi are C∞ by the fact that s is a smooth map. But then
X f|V = ∑vi
∂ f
∂xi
, which is a smooth function. Thus X f restricts to each coordinate chart as a smooth function, and
so is smooth. It is clear from the deﬁnition that sX = s. □
So we have two equivalent characterizations of vector ﬁelds on M: as derivations C∞ → C∞, and as smooth
sections M → T M (which in coordinate charts can be locally expressed in the f orm ∑vi ∂
∂xi
for suitable smooth
functions vi). Both characterizations are often useful.
4. D ifferential forms
As the title of the course textbook suggests, a very importan t role will be played in the rest of the course by
what are called the diﬀerential forms on a smooth manifold. If M is a smooth n-manifold, we will develop the
notion of a “ p-form” on M for p = 0, 1,..., n (and also for p > n, but for algebraic reasons it turns out that
the only p-forms with p > n will be zero). These p-forms will form a vector space Ωp(M), and we will have a
very important map d, called the exterior derivative, which maps the space of all di ﬀerential forms to itself and
restricts for each p to a map d : Ωp(M) → Ωp+1(M).
To ease into this, let’s start withp = 0 and p = 1.
Deﬁnition 4.1. A 0-form on M is a smooth function f : M → R. In other words Ω0(M) = C∞(M).
The case of 1-forms is a bit more interesting. First we introduce the notion of the cotangent space:
Deﬁnition 4.2. • If M is a smooth manifold and m ∈ M, the cotangent space at m, denoted by T ∗
mM, is the
dual space to the tangent space TmM.
• The cotangent bundle of M is
T ∗M = ∪m∈M{m} × T ∗
mM.
In other words, T ∗
mM consists of linear functionals α: TmM → R. Since a vector space and its dual have the
same dimension, if M is an n-manifold then dim T ∗
pM = n for all m ∈ M.
Deﬁnition 4.2 identiﬁes the cotangent bundle T ∗M as a set. One can equip it with a topology and then with
a smooth manifold structure, in such a way that the projectio nπ: T ∗M → M (sending (m,α ) to m ifα ∈ T ∗
mM)

20 MIKE USHER
makes T ∗M into a vector bundle, just like the situation with the tangent bundle. At least for now we won’t really
need to use this fact, but note that we have (at least at a set-theoretic level) the notion of a section s : M → T ∗M,
i.e. a function s: M → T ∗M such thatπ ◦ s = 1M. A section s: M → T ∗M associates to each m ∈ M an element
sm ∈ T ∗
pM.
Deﬁnition 4.3. A diﬀerential 1-form on a smooth manifold M is a section α: M → T ∗M which satisﬁes the
following smoothness property: Whenever X ∈ X(M) is a vector ﬁeld on M, the function
α(X): m ↦→αm(Xm)
is a C∞ function on M. We denote by Ω1(M) the vector space of diﬀerential 1-forms.
To unpack the above, note that the sectionα of the cotangent bundle determines covectorsαm ∈ T ∗
mM for all
m, while the vector ﬁeld X (which by Theorem 3.26) is equivalent to a section of the tangent bundle, determines
for each m a tangent vector Xm ∈ TmM. Hence we can evaluateαm(Xm), and the smoothness requirement onα is
that (as long as X is smooth) the result of this evaluation varies smoothly with m. If we had gone ahead and put
a smooth manifold structure on T ∗M it turns out that this would be equivalent to requiring α: M → T ∗M to be
a smooth map.
As mentioned earlier, for all p we will deﬁne a map d : Ωp(M) → Ωp+1(M). I can now fulﬁll this promise for
p = 0. Actually if one thinks of tangent vectors as derivations the deﬁnition may seem strangely simple:
To any f ∈ Ω0(M), i.e., any smooth function f , we are to associate a section d f : M → T ∗M. In other words
for each m we should obtain (d f)m : TmM → R. Well, bearing in mind that an element of TmM is a derivation
from functions deﬁned near m to R, we use the formula
(5) ( d f)m(v) = v( f ) if v ∈ TmM.
Suppose now thatφ: U → Rn is a coordinate chart, where U ⊂ M is open. Now U is a smooth manifold in
its own right, so we can consider Ω1(U). The coordinate chart φ distinguishes some special smooth functions
on U, namely the coordinate functions x1,..., xn (perhaps we should really write x1 ◦φ,..., xn ◦φ, or we could
just agree that the decomposition of φ into coordinates is given by φ(m) = (x1(m),..., xn(m))). Since the xi are
smooth functions ( i.e., 0-forms) on U, we obtain 1 -forms dx 1,..., dxn ∈ Ω1(U). So for each m ∈ U we have
covectors (dxi)m ∈ T ∗
mU = T ∗
mM.
On the other hand, recall that the tangent space TmM at m has basis given by ∂
∂x1
|m,..., ∂
∂xn
|m. We have
(dxi)m
( ∂
∂x j
|m
)
= ∂
∂x j
(xi) =δi j.
Thus the (dxi)m form a dual basis to the cotangent space T ∗
mM with respect to the basis
{∂
∂xi
|m
}
for T pM.
Since the (dxi)m form a basis for T ∗
mM at all m, it follows that any 1-formα ∈ Ω1(U) can be written as
α =
n∑
i=1
αidxi
for some functionsαi ∈ C∞(U) (which may be recovered by evaluatingα on ∂
∂xi
).
Exercise 4.4. Suppose that we have two diﬀerent coordinate charts
φ: m ↦→(x1(m),..., xn(m)) and ψ: m ↦→(y1(m),..., yn(m))
each with domain given by some open subset U of a smooth manifold. If α ∈ Ω1(U) can be written as
α =
n∑
i=1
αidxi =
n∑
i=1
βidyi
ﬁnd a general formula (in terms of the derivatives of φ ◦ψ−1 and/or ψ ◦φ−1) for the relationship between the
coeﬃcientsαi andβi.

MATH 8210, FALL 2011 LECTURE NOTES 21
The above exercise is designed to be compared to Exercise 3.22. A single coordinate chart around m produces
distinguished bases
{∂
∂xi
|m
}
for TmM and {(dxi)m} for T ∗
mM, allowing one to parametrize TmM or T ∗
mM by Rn.
Changing the coordinate chart changes the appropriate parametrization for either TmM or T ∗
mM, and you should
have found that the way in which the parametrization transforms under a coordinate change is diﬀerent for TmM
than it is for T ∗
mM. This reﬂects the fact that vector ﬁelds and 1-forms really are fundamentally diﬀerent kinds of
objects.
If (x1,..., xn): U → Rn is a coordinate patch and m ∈ U, we see that
d fm
( ∂
∂xi
)
= ∂ f
∂xi
(m) =








n∑
j=1
∂ f
∂x j
(dx j)m








( ∂
∂xi
)
,
and thus, throughout the coordinate chart U, we have
(6) d f =
n∑
j=1
∂ f
∂x j
dx j.
In principle we could also have deﬁned d : Ω0(M) → Ω1(M) by saying that if f ∈ Ω0(M) has support in a
coordinate chart then d f is given by formula (6), and requiring that d be linear over R—this would determine
d f for any f (not necessarily supported in a coordinate chart) since by using a partition of unity we can write an
arbitrary function as a sum of functions each of which is supp orted in a coordinate chart. (Of course, with this
approach one would need to make sure that d f didn’t depend on the way in which f is decomposed as such a
sum—our more natural and coordinate-free deﬁnition of d evades this issue).
Having deﬁned the map d : Ω0(M) → Ω1(M), one could ask whether it is surjective. A little thought sh ould
convince you that the answer must be no (if dim M ≥ 2)—indeed this may be familiar from multivariable
calculus. Consider just a 1-form α which is supported in a coordinate chart U, so in coordinates α|U = ∑
iαidxi
for some smooth functions αi supported in U, and α vanishes elsewhere. Evidently if α = d f then, on U, we
would have αi = ∂ f
∂xi
. Since f is assumed C∞, its mixed partials are equal and so if we had α = d f we would
need ∂αi
∂x j
= ∂α j
∂xi
for all i, j, and of course these equations have no reason to hold for a general collection of smooth
functionsαi supported in U.
Thus we obtain an obstruction to a 1-form α being in the image of d, which in local coordinates can be seen
as coming from the partial derivatives of the various components ofα. If α is in the image of d it is called exact.
Once we deﬁne the space of 2-forms Ω2(M) and the exterior derivative d : Ω1(M) → Ω2(M), we will see that
the above obstruction vanishes in the sense that the relevan t partial derivatives coincide if and only if dα = 0.
Indeed, d ◦ d : Ω0(M) → Ω2(M) is zero (as, more generally, is d ◦ d : Ωp(M) → Ωp+2(M)). One can then ask
whether everyα for which the obstruction vanishes ( dα = 0) is indeed exact. We’ll see that the answer to this
question depends on the topology of M (as measured by the de Rham cohomology groups). )
4.1. The alternating algebra.
Deﬁnition 4.5. Let V be a vector space over R, and let p be a positive integer. An alternating p-form on V is a
functionη: V p → R with the following properties:
• η is p-linear: For any i, if c ∈ R and v1,..., vp ∈ V and wi ∈ V then
η(v1,..., vi−1, cvi + wi,..., vp) = cη(v1,..., vi−1, vi,..., vp) +η(v1,..., vi−1, wi,..., vp).
• V is antisymmetric: if v, w ∈ V then, for any i < j and any u1,..., ui−1, ui+1,..., u j−1, u j+1,..., up ∈ V
η(u1,..., ui−1, v, ui+1,..., u j−1, w, u j+1,..., up) = −η(u1,..., ui−1, w, ui+1,..., u j−1, v, u j+1,..., up).
We will denote the vector space of alternating p-forms on V by ΛpV ∗. We extend the notation ΛpV ∗ to p = 0 by
setting Λ0V ∗ = R.

22 MIKE USHER
Implicit in the above is that the alternatingp-forms do indeed form a vector space, which should be clear. Our
notation ΛpV ∗ reﬂects a number of algebraic facts, not all of which we will n eed or use: for any vector space V
there is a certain standard vector spaceΛpV (“the pth graded part of the exterior algebra”), and (at least assuming
that V is ﬁnite-dimensional) what we denote by ΛpV ∗ can be canonically identiﬁed both with ( ΛpV)∗ and with
Λp(V ∗) (so our lack of parentheses is in writing ΛpV ∗ is deliberate). There is an obvious identiﬁcation of Λ1V ∗
with V ∗.
With this deﬁnition, there is for all p, q ≥ 0 a map
∧: ΛpV ∗ × ΛqV ∗ → Λp+qV ∗
(α,β ) ↦→α ∧β
called the wedge product, which satisﬁes various important properties. Let us give t he deﬁnition gradually. The
ﬁrst interesting case is when p = q = 1: in this case we deﬁne the wedge product by, for α,β ∈ Λ1V ∗, and
v, w ∈ V,
(α ∧β)(v, w) =α(v)β(w) −α(w)β(v).
It is not hard to see that, with this deﬁnition, α ∧β does indeed belong to Λ2V ∗ (the minus sign ensures that the
antisymmetry condition holds). We then extend this to the case that p = 1 but q is arbitrary by, forα ∈ Λ1V ∗,β ∈
ΛqV ∗,
(α ∧β)(v1, v2,..., vq+1) =α(v1)β(v2,..., vq+1) −α(v2)β(v1, v3,..., vq+1)
+α(v3)β(v1, v2, v4,..., vq+1) + · · ·+ (−1)lα(vq+1)β(v1,..., vq)
=
q+1∑
j=1
(−1) j−1α(v j)β(v1,..., v j−1, v j+1,..., vq+1)
We introduce a notation for “omitting” inputs into k-forms as we often need to do: instead of writing
β(v1,..., v j−1, v j+1,..., vq+1) we will write β(v1,..., ˆv j,..., vq+1); thus the hat signiﬁes that the jth term has
been omitted.
We should check thatα∧β as deﬁned above is actually an element ofΛq+1V ∗. It’s fairly obvious from this def-
inition thatα ∧β is (q + 1)-linear. As for antisymmetry, if we switchvk and vl with k< l then the antisymmetry of
β shows that all terms in the sum change sign except for those with j = k, l. Meanwhile the kth term changes from
(−1)k−1α(vk)β(v1,..., ˆvk,..., vl,..., vq+1) to ( −1)k−1α(vl)β(v1,..., ˆvl,..., vk,..., vq+1), and the lth term changes
from (−1)l−1α(vl)β(v1,..., vk,..., ˆvl,..., vq+1) to (−1)l−1α(vk)β(v1,..., vl,..., ˆvk,..., vq+1). I claim that the new
lth term is the negative of the old kth term, and vice versa. Indeed to convert the new lth term to something that
looks like the oldkth term we can “move thevl past vk+1,..., vl−1”—in other words we should switch vl with vk+1,
then switch vl with vk+2, and so on, until we switch vl with vl−1. Since β is antisymmetric each of these switches
produces a factor of −1, and so since there are a total ofl − k − 1 numbers from k + 1 to l − 1 the whole procedure
produces a factor of (−1)l−k−1. So the new lth term is equal to (−1)l−1(−1)l−k−1α(vk)β(v1,..., ˆvk,..., vq+1), which
is indeed equal to the negative of the old kth term. Similarly, the new kth term can be equated with the negative
of the old lth term by “movingvk l − k − 1 slots to the left.” Summing up, switchingvk with vl causes all the terms
with j /nelement{k, l} to change signs, and also causes the sum of the kth and lth terms to change sign. This proves that
α ∧β is alternating, so our map Λ1V ∗ × ΛqV ∗ → Λq+1V ∗ is well-deﬁned.
Finally we extend the deﬁnition of the wedge product to general values of p and q. One way of characterizing
this extension is that, given our deﬁnition for the case p = 1, there turns out to be a unique way of extending the
deﬁnition to general p so that the operation ∧ will be bilinear and associative (for instance, if α,β ∈ Λ1V ∗, so
thatα ∧β ∈ Λ2V ∗, we take the wedge product withα ∧β (on the left) by insisting that (α ∧β) ∧γ =α ∧ (β ∧γ)
for γ ∈ ΛqV ∗—since we’ve already decided how to take wedge product with 1- forms the right-hand side is
well-deﬁned).
Instead of showing that this indirect argument gives a well- deﬁned prescription, we give a formula. Given
nonnegative integers p and q, let Sp,q denote the collection of p-element subsets of {1,..., p + q}. Then for

MATH 8210, FALL 2011 LECTURE NOTES 23
S ∈ S p,q let the positive integersiS
1 < iS
2 < · · ·< iS
p be the elements ofS , and let the positive integersjS
1 <...< jS
q
be the elements of {1,..., p + q} \ S . Deﬁne ρS : {1,..., p + q} → { 1,..., p + q} by, for 1 ≤ k ≤ p,ρS (k) = iS
k ,
and for p + 1 ≤ k ≤ p + q,ρS (k) = jS
k−p. In other words ρS is the permutation of {1,..., p + q} gotten by writing
all the elements of S in increasing order, and then all the elements of {1,..., p + q} \ S in increasing order. Let
(−)S be 1 if the permutationρS is even and −1 ifρS is odd. The general formula for the wedge product is then
(7) ( α ∧β)(v1,..., vp+q) =
∑
S ∈Sp,q
(−)Sα(viS
1
,..., viSp )β(v jS
1
,..., v jS
q )
In other words, (α ∧β)(v1,..., vp+q) is gotten by looking at all the di ﬀerent products gotten by plugging in p of
the vi intoα and q of them intoβ, and summing these up with a naturally associated sign. It’snot hard to see that
this coincides with our previous deﬁnition in case p = 1.
To help verify some other properties of the wedge product (in particular the fact that the wedge product
of alternating forms is alternating) we rewrite (7) as a sum o ver all permutations on p + q letters. Let Sp+q
denote the group of permutations on p + q letters. Identify Sp × Sq with a subgroup of Sp+q by associating to
(σ,τ) ∈ Sp × Sq with the permutation on p + q letters (still denoted (σ,τ)) such that (σ,τ)(i) =σ(i) for 1 ≤ i ≤ p
and (σ,τ)(p + j) = p +τ( j) for 1 ≤ j ≤ q (in other words,σ acts on the ﬁrst p letters andτ acts on the last q). Any
permutation inη ∈ Sp+q can be written uniquely in the formη =ρS ◦ (σ,τ) whereρS is one of the permutations
from the previous paragraph: namely, let S = {η(1),...,η (p)}; letσ send j to r ifη( j) is the rth largest element
of S ; and letτ send j to s ifη(p + j) is the sth largest element of S \ {η(1),...,η (p)}. Ifη =ρS ◦ (σ,τ) we see that
α(vη(1),..., vη(p)) = sgn(σ)α(vη(σ−1(1)),..., vη(σ−1(p))) = sgn(σ)α(viS
1
,..., viSp )
where sgn(σ) is one ifσ is even and −1 ifσ is odd, and similarly
β(vη(p+1),..., vη(p+q)) = sgn(τ)β(v jS
1
,..., v jS
q ).
Now evidently ifη =ρS ◦ (σ,τ) then sgn(η) = (−)S sgn(σ)sgn(τ), and so we deduce
sgn(η)α(vη(1),..., vη(p))β(vη(p+1),..., vη(p+q)) = (−)Sα(viS
1
,..., viSp )β(v jS
1
,..., v jS
q ) if η =ρS ◦ (σ,τ).
Now as mentioned earlier any η ∈ Sp+q can be expressed uniquely as ρS ◦ (σ,τ) for some S,σ,τ , and so since
the pair (σ,τ) varies through the group Sp × Sq which has order p!q!, we deduce the following (more symmetric
and redundant) version of (7):
(8) ( α ∧β)(v1,..., vp+q) = 1
p!q!
∑
η∈Sp+q
sgn(η)α(vη(1),..., vη(p))β(vη(p+1),..., vη(p+q))
From (8) it is not di ﬃcult to see that α ∧β (which is obviously ( p + q)-linear) is antisymmetric and hence
is an alternating ( p + q)-form: indeed, let τk,l be the transposition which switches letters k and l; of course any
permutation can be written uniquely in the formη ◦τk,l, and so we have
(α ∧β)(v1,..., vp+q) = 1
p!q!
∑
η∈Sp+q
sgn(η ◦τk,l)α(vη◦τk,l(1),..., vη◦τk,l(p))β(vη◦τk,l(p+1),..., vη◦τk,l(p+q))
= 1
p!q!
∑
η∈Sp+q
(−1)sgn(η)α(vη(1),..., vη(p))β(vη(p+1),..., vη(p+q)) but with the places ofη(k) andη(l) switched
= −(α ∧β)(v1,..., vk−1, vl, vk+1,..., vl−1, vk, vl+1,..., vp+q).
This proves that the map∧: ΛpV ∗ ×ΛqV ∗ → Λp+qV ∗ deﬁned by the equivalent formulas (7,8) is well-deﬁned.
The deﬁnition is still valid when p and/or q is zero (recalling that Λ0V ∗ = R by deﬁnition): wedge product with
a 0-form is just multiplication by the corresponding number.
We deﬁne the algebra of alternating forms on V as the direct sum
Λ∗V ∗ = ⊕∞
p=0ΛpV ∗.

24 MIKE USHER
This is equipped with the obvious vector space structure, an d also with a multiplication operation ∧ induced by
extending bilinearly from the above-deﬁned operations ∧: ΛpV ∗ × ΛqV ∗ → Λp+qV ∗
Proposition 4.6. The wedge product obeys:
(a) Forα ∈ ΛpV ∗,β ∈ ΛqV ∗,
β ∧α = (−1)pqα ∧β.
(b) For allα,β,γ ∈ Λ∗V ∗,
α ∧ (β ∧γ) = (α ∧β) ∧γ.
Proof. (a) Let ηp,q ∈ Sp+q be the permutation given by η(i) = q + i for 1 ≤ i ≤ p and η( j) = j − p for
p + 1 ≤ j ≤ p + q. Note that sgn(ηp,q) = (−1)pq (why?). Any permutation in Sp+q can be written uniquely in the
formη ◦ηp,q, so we have
α ∧β(v1,..., vp+q) = 1
p!q!
∑
η∈Sp+q
sgn(η ◦ηp,q)α(vη◦ηp,q(1),..., vη◦ηp,q(p))β(vη◦ηp,q(p+1),..., vη◦ηp,q(p+q))
= 1
p!q!
∑
η∈Sp+q
(−1)pqsgn(η)β(vη(1),..., vη(q))α(vη(q+1),..., vη(p+q))
= (−1)pqβ ∧α,
proving (a).
(b) Using the bilinearity of ∧ we may assume that, for some p, q, r, we have α ∈ ΛpV ∗, β ∈ ΛqV ∗, and
γ ∈ ΛrV ∗. Consider ways of writing {1,..., p + q + r} as a disjoint union {1,..., p + q + r} = S 1
∐S 2
∐S 3
where #S 1 = p, #S 2 = q, #S 3 = r. For any such decomposition, write the elements of S 1 in increasing order
as a1 < · · ·< ap, those of S 2 as b1 < · · ·< bq, and those of S 3 as c1 < · · ·< cr. Also let ( −)S 1S 2S 3 for the sign
of the permutation obtained by sending i to ai for 1 ≤ i ≤ p, to bi−p for p + 1 ≤ i ≤ p + q, and to ci−p−q for
p + q + 1 ≤ i ≤ p + q + r. Then after repeatedly applying our original formula (7) and unraveling the notation it
is easy to check that both
(α ∧ (β ∧γ)) (v1,..., vp+q+r) and ((α ∧β) ∧γ) (v1,..., vp+q+r)
are equal to ∑
S 1,S 2,S 3
(−)S 1S 2S 3α(va1,..., vap)β(vb1,..., vbq)γ(vc1,..., vcr).
□
Of course, one consequence of associativity is that ifα1,...,α m ∈ Λ∗V ∗ we can unambiguously writeα1∧· · ·∧
αm. The results of Proposition 4.6 can be summarized as sayingthat Λ∗V ∗ is an associative, graded commutative
algebra.
We now observe that the exterior algebra behaves nicely unde r linear maps. Suppose that we have two real
vector spaces V, W and a linear map A: V → W. For any p, we obtain a linear map A∗ : ΛpW ∗ → ΛpV ∗ (called
the pullback of A) by setting
(A∗α)(v1,..., vp) =α(Av1,..., Avp).
Note that since we don’t assume A to be invertible it is necessary for A∗ to “go in the opposite direction” to get
a well-deﬁned map. Extending by linearity produces a linear map A∗ : Λ∗W ∗ → Λ∗V ∗ deﬁned on the whole
alternating algebra.
Proposition 4.7. If A : V → W is a linear map and α,β ∈ Λ∗W ∗ then
A∗(α ∧β) = (A∗α) ∧ (A∗β).
Proof. This is an immediate consequence of our formula (7) for the wedge product. □

MATH 8210, FALL 2011 LECTURE NOTES 25
In other words, a linear map A: V → W induces not just a linear map but in fact an algebra homomorph ism
Λ∗W ∗ → Λ∗V ∗. Looking at how compositions behave, one sees easily that th e alternating algebra construction
V ↦→Λ∗V ∗ deﬁnes a contravariant functor from the category of real vector spaces to the category of real associa-
tive graded commutative algebras. (Given what we’ve proven, one just needs to check that 1 ∗
V = 1Λ∗V ∗ and that
(A ◦ B)∗ = B∗ ◦ A∗.)
In the discussion of alternating forms so far, we have avoide d choosing a basis for the vector space V (and
we haven’t even assumed thatV is ﬁnite-dimensional). This has been deliberate, as we inte nd to apply this with
V equal to the tangent space TmM at a point on a smooth manifold, and as mentioned before altho ugh we can
impose a basis on TmM by choosing a coordinate chart aroundm, diﬀerent coordinate charts yield diﬀerent bases
and so there is no canonical choice. However to actually do an y computations on a speciﬁc vector space one
typically does eventually have to choose a basis, and so we now turn to discussing how a basis for V allows one
to do calculations in Λ∗V ∗.
So let V be a real vector space with ﬁnite dimension n and basis {e1,..., en}. Let {e1,..., en} denote the dual
basis for V ∗ (so ei(e j) = δi j), and recall that V ∗ is equal to Λ1V ∗, so that the ei can be viewed as elements of the
alternating algebra Λ∗V ∗.
Proposition 4.8. Letη ∈ ΛpV ∗ and suppose that for all p-tuples of integers(i1,..., ip) with 1 ≤ i1 < · · ·< ip ≤ n
we have
η(ei1,..., eip) = 0.
Thenη = 0.
Proof. Suppose to the contrary that η /nequal0. Then we can choose some v1,..., vp ∈ V with η(v1,..., vp) /nequal
0. Now the vi can be written in the form v = ∑
j v jie j for some real numbers v ji. Repeatedly using the p-
linearity of η we then ﬁnd that the nonzero number η(v1,..., vp) can be written as a linear combination of the
real numbersη(e j1,..., e jp) for various k-tuples ( j1,..., jp). So the fact that η(v1,..., vp) /nequal0 implies that some
η(e j1,..., e jp) /nequal0 where j1,..., jp ∈ { 1,..., n}. Now if two of the numbers ji are equal to each other then it
follows directly from the antisymmetry property ofη thatη(e j1,..., e jp) would be zero, so the numbers j1,..., jp
makingη(e j1,..., e jp) /nequal0 must all be distinct. But again using the antisymmetry property, any reordering of the
numbers j1,..., jp causesη(e j1,..., e jp) to change only by multiplication by ±1. So if we choose i1 < · · ·< ip
to be the result of writing j1,..., jp (which we know to be distinct) in strictly increasing order i t will hold that
η(ei1,..., eip) /nequal0. This proves (the contrapositive of) the proposition. □
Proposition 4.9. Suppose that 1 ≤ p ≤ n and that 1 ≤ i1 < · · ·< ip ≤ n and 1 ≤ j1 < · · ·< jp ≤ n are two
strictly increasing sequences of integers from1 to n. Then
(ei1 ∧ · · · ∧eip)(e j1,..., e jp) =
{1 if il = jl for all l
0 otherwise
Proof. We can use induction on p. For p = 1 this is just the deﬁnition of the dual basis, so assume the re sult
holds for p and consider increasing sequences i1 < · · ·< ip+1 and j1 < · · ·< jp+1. If these sequences are not
identical to each other, then there is some r such that jr /nelement{i1,..., ip+1}. We have (usingˆto signify omission)
(9) ( ei1 ∧ · · · ∧eip+1)(e j1,..., e jp+1) =
p+1∑
s=1
(−1)s−1ei1(e js)(ei2 ∧ · · · ∧eip+1)(e j1,..., ˆe js,..., e jp+1).
The rth term vanishes because jr /nequali1, and all of the other terms vanish by the inductive hypothesi s because
jr /nelement{i2,..., ik+1}. This proves the “otherwise” part of the proposition.
On the other hand if each il coincides with jl, then since the il form an increasing sequence it follows from the
inductive hypothesis that, in (9), the ﬁrst term (i.e. the one with s = 1) equals 1 and all others equal zero. □
Corollary 4.10. If I = (i1,..., ip) is a p-tuple of integers with 1 ≤ i1 < · · ·< ip ≤ n = dim V, and if we write
eI = ei1 ∧ · · · ∧eip,

26 MIKE USHER
then the various eI form a basis for ΛpV ∗. In particular dim ΛpV ∗ =
(n
p
)
= n!
p!(n−p)!
Proof. The various eI are linearly independent: if some linear combination ∑
I cIeI = 0 then, for any J =
( j1,..., jp), evaluating both sides on the tuple (e j1,..., e jp) shows that cJ = 0 by Proposition 4.9.
To see that theeI span ΛpV ∗, ifη ∈ ΛkV ∗ and I = (i1,..., ip) is an increasing sequence, letηI =η(ei1,..., eip).
Then by Proposition 4.9 we have 





η −
∑
I
ηIeI






 (e j1,..., e jp) = 0
for all increasing sequences j1 < · · ·< jp. So by Proposition 4.8 it follows thatη = ∑
IηIeI.
The statement about dim ΛpV ∗ just follows from counting the number of increasing sequenc es of p-tuples
I drawn from the set {1,..., n}, which is evidently the same as the number of p-element subsets of {1,..., n},
which of course is
(n
p
)
.
□
Of course, the formula dimΛpV ∗ =
(dim V
p
)
continues to hold for p = 0 for trivial reasons. We note in particular
that, if dim V = n, ΛpV ∗ is trivial for p > n, and one-dimensional for p = n. Evidently a generator for the one-
dimensional vector space ΛnV ∗ is given by e1 ∧... ∧ en where the ei form a dual basis to a basis {ei} for v. For
some other basis { fi} the element f 1 ∧ · · · ∧f n will then be a multiple of e1 ∧ · · · ∧en; this multiple is given by
the determinant of a certain basis change matrix, as you may be able to see from the following exercise:
Exercise 4.11. Let A: V → V be a linear map, where V is an n-dimensional real vector space. We then have an
induced map A∗ : ΛnV ∗ → ΛnV ∗, which is a linear map from a one-dimensional vector space to itself and hence
is given by the formula A∗x = cAx for all x where cA is some number depending on A. Prove that cA = det A.
(Hint: Choose a basis in terms of which A has Jordan normal form)
Exercise 4.12. Let V be a ﬁnite-dimensional real vector space and letα ∈ ΛpV ∗, with 2 ≤ p ≤ dim V. Let us say
thatα is decomposable if there areα1,...,α p ∈ Λ1V ∗ so thatα =α1 ∧ · · · ∧αp.
(a) Prove that ifα is decomposable thenα ∧α = 0.
(b) Prove that if dim V = 2 or 3 then (for 2 ≤ p ≤ dim V) everyα ∈ ΛpV ∗ is decomposable.
(c) If dim V ≥ 4, construct (with proof, giving an explicit formula) some α ∈ Λ2V ∗ such that α is not
decomposable. (Hint: By (a) it is enough to arrange that α ∧α /nequal0.)
4.2. Higher-degree diﬀerential forms. If M is a smooth manifold and m ∈ M we let ΛpT ∗
mM denote the space
of alternating p-forms on the tangent space TmM (strictly speaking in the notation of the previous subsection we
should instead write ΛpTmM∗, but we do not), and let
ΛpT ∗M = ∪m∈M{m} × ΛpT ∗
mM.
Thus projection onto the ﬁrst factor gives a function π: ΛpT ∗M → M, and so we can consider the notion of a
section s: M → ΛpT ∗M, i.e. a map s obeyingπ ◦ s = 1M, and thus associating to each m ∈ M an alternating
p-form sm on the tangent space TmM.
Deﬁnition 4.13. A diﬀerential p-form on M is a section η: M → ΛpT ∗M obeying the following smoothness
property: If X1,..., Xp are any smooth vector ﬁelds on M, then the function
m ↦→ηm
(
(X1)m,..., (Xp)m
)
is of class C∞. We denote the vector space of diﬀerential p-forms on M by Ωp(M).
Note that this coincides with the previous deﬁnition for p = 1, recalling the general fact that Λ1V ∗ = V ∗. We
also earlier deﬁned Ω0(M) to be the space of smooth functions from M to R; since Λ0V ∗ = R this new deﬁnition
is equivalent (albeit slightly notationally diﬀerent, but this shouldn’t cause a problem) to the previous one.

MATH 8210, FALL 2011 LECTURE NOTES 27
Assume that dim M = n. Choose a coordinate chart ( x1,..., xn): U → Rn with m ∈ U. Recall that, for
each m ∈ M, the covectors ( dx1)m,..., (dxn)m form a basis for T ∗
mM, dual to the basis
{∂
∂xi
|m
}
for TmM. For
I = (i1,..., ip) ∈ {1,..., n}p with i1 <...< ip, write
dx I
m = (dx1)m ∧ · · · ∧(dxn)m.
According to Corollary 4.10, the various dx I
m form a basis for ΛpT ∗
mM. Consequently, for any η ∈ Ωp(M), for
each q in the coordinate patch U we can write
ηq =
∑
I
fI(q)dx I
q
for some functions fI : U → R. Moreover, by evaluating η on tuples of vector ﬁelds whose restrictions to U
coincide with some of the ∂
∂xi
, we see that the functions fI are smooth. Thus, a di ﬀerential p-form restricts to a
coordinate chart (U, x1,..., xn) as an object of the form
η|U =
∑
I
fIdx I where fI ∈ C∞(U).
In less abbreviated notation, we could write
η|U =
∑
i1<···<ip
fi1···ipdxi1 ∧ · · · ∧dxip.
Having deﬁned the spaces of p-forms Ωp(M), we can let Ω∗(M) = ⊕∞
p=0Ωp(M); a diﬀerential form on M is
then simply an element of Ω∗(M).
For each m ∈ M and p, q ≥ 0 we have a wedge product operation ∧ΛpT ∗
mM × ΛqT ∗
mM → Λp+qT ∗
mM. This
then induces a wedge product Ωp(M) × Ωq(M) → Ωp+q(M) in an obvious way, setting (α ∧β)m =αm ∧βm. So,
extending bilinearly, we get a wedge product ∧: Ω∗(M) × Ω∗(M) → Ω∗(M). In view of Proposition 4.6, the
wedge product on diﬀerential forms is associative and graded commutative.
We now complete the deﬁnition of the exterior derivative d: Ω∗(M) → Ω∗(M).
Theorem 4.14. There is a unique R-linear map d : Ω∗(M) → Ω∗(M) obeying the following properties:
(i) For all p, the restriction d|Ωp(M) has image contained in Ωp+1(M).
(ii) d|Ω0(M) coincides with the map d : Ω0(M) → Ω1(M) deﬁned in (5).
(iii) Ifω ∈ Ωp(M) andφ ∈ Ωq(M) we have
d(ω ∧φ) = (dω) ∧φ + (−1)pφ ∧ dω.
(iv) d ◦ d = 0.
For any coordinate chart(x1,..., xn): U → Rn, ifω|U = ∑
I fIdx I, then
(10) dω|U =
n∑
j=1
∑
I
∂ fI
∂x j
dx j ∧ dx I.
Proof. We start with the following lemma. Of course, the support supp (η) of a p-form η is by deﬁnition the
closure of the set of m ∈ M for whichηm ∈ ΛpT ∗
mM is nonzero.
Lemma 4.15. Assume that the linear map d : Ω∗(M) → Ω∗(M) satisﬁes properties (i)-(iv) and suppose that
ω ∈ Ωp(M) has supp (η) equal to a closed subset of M which is contained in the domain U of a coordinate chart
(x1,..., xn): U → Rn. Ifω|U = ∑
I fIdx I, then dω has support contained in U and dω|U = ∑n
j=1
∑
I
∂ fI
∂x j
dx j ∧ dx I.
The same conclusion continues to hold if we only assume that c onditions (i)-(iv) hold for d when d is restricted
to forms whose supports are contained in U.

28 MIKE USHER
Proof. Letβ: M → R be a smooth function such that β|supp (ω) = 1 and supp (β) ⊂ U. Note then that for each
i the smooth function βxi : U → Rn has closed support within U, and therefore extends to a smooth function
on all of M by setting it equal to zero outside of U. Also the functions fI each have support contained in the
support of ω (on which β = 1), so the fI also extend by zero to smooth functions on all of M, and moreover if
I = (i1,..., ip) we have (at least on U, where both sides are deﬁned)
fIdx I = fId(βxi1) ∧ · · · ∧d(βxip).
Thus
ω =
∑
I=(i1,...,ip)
fId(βxi1) ∧ · · · ∧d(βxip)
(the two sides coincide on U, and are both zero outside of U).
Now by induction on the integer r it is easy to see from conditions (iii) and (iv) that, for any smooth functions
g1,..., gr we have
d (dg1 ∧ dg2 ∧ · · · ∧dgr) = 0.
Applying this fact together with (iii) again (and the linearity of d) shows that
dω =
∑
I
d fI ∧ d(βxi1) ∧ · · · ∧d(βxip).
Sinceβ is identically 1 on the union of the supports of thefI (which is contained inU), and since d fI = ∑
j
∂ fI
∂x j
dx j
on U, the result follows. □
Motivated by this lemma, choose once and for all a cover{Uα} by domains of coordinate charts (xα
1,..., xα
n): Uα →
R, and let {χα} be a partition of unity subordinate to the cover{Uα}. For I = (i1,..., ip) let dx I
α = dxα
i1
∧ · · · ∧dxα
ip
.
Lemma 4.16. For anyα let Ω∗
α(M) denote the space of diﬀerential forms on M whose support is contained inα.
Deﬁne dα : Ω∗
α(M) → Ω∗
α(M) by setting, ifω ∈ Ω∗
α(M) withω|Uα = ∑
I fIdx I
α,
dαω|Uα =
∑
I
d fI ∧ dx I
α
(and dαω = 0 outside Uα). Then d α : Ω∗
α(M) → Ω∗
α(M) satisﬁes (i)-(iv) of Theorem 4.14 when restricted to
Ω∗
α(M), and is the unique such map with these properties.
Proof. Uniqueness is already proven in (the last sentence of) Lemma 4.15, so we just need to check that (i)-(iv)
are satisﬁed. (i) is obvious, and (ii) is given by Equation 6. The fact that (iii) holds outside of Uα is trivial (both
sides are zero); inside of Uα let us write ω|Uα = ∑
I fIdx I
α andφ|Uα = ∑
J gJdx J
α (where the multi-indices I have
length p and the multi-indices J have length q). We then have, on Uα,
dα(ω ∧φ) = dα








∑
I,J
fIgJdx I
α ∧ dx J
α







 =
∑
k,I,J
∂( fIgJ)
∂xα
k
dxα
k ∧ dx I
α ∧ dx J
α
=
∑
k,I,J
(∂ fI
∂xα
k
gJ + fI
∂gJ
∂xα
k
)
dxα
k ∧ dx I
α ∧ dx J
α
=
∑
k,I,J
(∂ fI
∂xα
k
dxα
k ∧ dx I
α
)
∧ (gJdx J
α) +
∑
k,I,J
(−1)p( fIdx I
α) ∧
(∂gJ
∂xα
k
)
dxα
k ∧ dx J
α
= (dαω) ∧φ + (−1)pω ∧ dαφ

MATH 8210, FALL 2011 LECTURE NOTES 29
where the (−1)p comes from applying Proposition 4.6 (a) to the wedge product dxα
k ∧ dx I
α. This proves that dα
satisﬁes (iii). As for (iv), if ω|Uα = ∑
I fIdx I
α, then clearly dα(dαω) vanishes outside Uα, and on Uα we have
dα(dαω) = dα







n∑
k=1
∑
I
∂ fI
∂xα
k
dxα
k ∧ dx I
α







=
∑
I







n∑
l=1
n∑
k=1
∂2 fI
∂xα
l∂xα
k
dxα
l ∧ dxα
k






 ∧ dx I
α
=
∑
I







n∑
l=1
∑
k<l
( ∂2 fI
∂xα
l∂xα
k
− ∂2 fI
∂xα
k∂xα
l
)
dxα
l ∧ dxα
k






 ∧ dx I
α = 0
since the mixed partials of the smooth function fI are equal (of course in the second-to-last equation we’ve
switched the indices k and l in the terms that initially had k > l and used the fact that dxα
k ∧ dxα
l = −dxα
l ∧ dxα
k ).
This proves (iv) and so completes the proof of the lemma. □
We now move from these local considerations to prove the glob al Theorem 4.14. We have ﬁxed a (locally
ﬁnite) partition of unity {χα} subordinate to a cover Uα. Then if ω ∈ Ω∗(M) we have
ω =
∑
α
(χαω) where each χαω ∈ Ω∗
α(M).
So for eachα we have a well-deﬁned diﬀerential form dα(χαω), whose support is contained in the support ofχα
(in particular any point in M has a neighborhood meeting the supports of only ﬁnitely many of the dα(χαω), so
the sum ∑
α dα(χαω) is a well-deﬁned diﬀerential form). So deﬁne
dω =
∑
α
dα(χαω).
This is clearly R-linear since each of thedα are, and conditions (i), (ii), and (iv) are each also manifestly inherited
from the corresponding facts for dα (together, in the case of (ii), with the fact that the map d : Ω0(M) → Ω1(M)
deﬁned earlier in (5) is also R-linear). Condition (iii) (the form version of the Leibniz r ule) takes just a little
more work. For eachα letψα be a smooth function which is equal to one on supp (χα) but such that we still have
supp (ψα) ⊂ Uα. If ω ∈ Ωp(M) andφ ∈ Ωq(M), we have by deﬁnition
d(ω ∧φ) =
∑
α
dα(χα(ω ∧φ)).
Note thatχα(ω ∧φ) = (χαω) ∧ (ψαφ) (both factors of which have support in Uα), so
dα(χα(ω ∧φ)) = dα(χαω) ∧ (ψαφ) + (−1)pχαω ∧ dα(ψαφ)
and so (freely using associativity and distributivity of th e wedge product, as well as the fact that ψαφ = φ
wherever d(χαω) /nequal0)
d(ω ∧φ) =
∑
α
dα(χαω) ∧φ + (−1)pω ∧







∑
α
χαdα(ψαφ)







= (dω) ∧φ + (−1)pω ∧







∑
α
χαdα(ψαφ)







So evidently it remains only to show that
(11)
∑
α
χαdα(ψαφ) =? dφ.

30 MIKE USHER
Note also thatχαψα =χα andψαdχα = dχα, so
dα(χαφ) = dα(χαψαφ)
=χαdα(ψαφ) + dχα ∧ (ψαφ) =χαdα(ψαφ) + dχα ∧φ,
i.e.
χαdα(ψαφ) = dα(χαφ) − dχα ∧φ.
Thus
∑
α
χαdα(ψαφ) =
∑
α
dα(χαφ) −
∑
α
dχα ∧φ
= dφ − d







∑
α
χα






 ∧φ = dφ
since ∑
α dχα = 1 and so d (∑
αχα
) = 0.
This completes the proof that d, as we have deﬁned it, satisﬁes the desired properties. The formula (10) given
at the end of the theorem for the behavior of d on an arbitrary coordinate chart then follows from Lemma 4.1 5:
If m ∈ U choose a cuto ﬀfunction β: M → R equal to 1 on a neighborhood of m and with compact support
contained in U; thenω =βω + (1 −β)ω and we have (d((1 −β)ω))m = 0 while Lemma 4.15 ensures that (d(βω))m
is given by evaluating the right-hand side of (10) at m. □
It is not initially obvious that the formula for d given in the proof, namely dω = ∑
α dα(χαω), would give an
answer which is independent of the partition of unity {χα} or of the open cover {Uα}, but the uniqueness part of
the theorem implies that this independence property holds.
In practice, one does not calculate dω by choosing a partition of unity; rather one covers the manif old by
coordinate charts U and uses the formula (10) to express dω in each of these coordinate charts. Again, it is not
initially obvious that, if V is another coordinate chart with U ∩ V = ∅, the forms obtained by using (10) with
reference to the two diﬀerent coordinate charts would give both give the same answer when restricted to U ∩ V.
However, the theorem ensures that this is in fact the case (one can also verify this somewhat tediously by a direct
computation).
Since d ◦ d = 0, we can make the following deﬁnition:
Deﬁnition 4.17. Let M be a smooth manifold, and p a nonnegative integer. The pth de Rham cohomology of M
is the real vector space
H p
dR(M) = ker(d : Ωp(M) → Ωp+1(M))
Im(d : Ωp−1(M) → Ωp(M)).
(For the case p = 0, we regard Ω−1(M) as the trivial vector space, so that H0
dR(M) = ker(d : Ω0(M) → Ω1(M)).)
Remark 4.18. A formω such that dω = 0 is called closed, and a form ω such thatω = dφ for someφ is called
exact. Thus the fact that d ◦ d = 0 expresses that every exact form is closed, and the pth de Rham cohomology
group measures the extent to which it fails to be true that, conversely, every closed p-form is exact.
I would also like to record a fact which we will make use of shor tly, and which basically was proven in the
proof of Theorem 4.14:
Proposition 4.19. Letω ∈ Ωp(M). Then we can write ω as a locally ﬁnite sum ω = ∑
γωγ (i.e., any point has
an open set intersecting only ﬁnitely many of the supp (ωγ)) such that eachωγ is given by
ωγ = fγdg1,γ ∧ · · · ∧dgp,γ
for some functions fγ, g1,γ,..., gp,γ ∈ C∞(M).

MATH 8210, FALL 2011 LECTURE NOTES 31
Proof. Let {Uα} be an open cover of M by domains of coordinate charts ( xα
1,..., xα
n) and {χα} a (locally ﬁnite)
partition of unity subordinate to {Uα}. We can then write ω = ∑
α(χαω) where each χαω is supported in Uα.
In turn, it was shown in the proof of Lemma 4.15 that each χαω can be written as a ﬁnite sum of forms of the
desired type fα,Idg1,α,I ∧ · · · ∧dgp,α,I (as I varies over multi-indices I = (i1,..., ip)), namely one sets g j,α,I =βxα
i j
whereβ is a smooth function supported in Uα and equal to 1 on supp (χα). So by having the index γ vary over
pairs (α, I) the result follows.
□
To get a sense of what the exterior derivative d is measuring, it is instructive to consider the special case s
where the smooth manifold is an open subset U of R2 or R3. As mentioned earlier, for any open subset of Rn the
degree-zero part of d acts by d f = ∑n
i=1
∂ f
∂xi
dxi. So if we use the standard basis of Rn to identify vector ﬁelds with
1-forms2, the exterior derivative of a function is essentially its gradient in the sense of multivariable calculus.
For open subsets U ⊂ R2, the only remaining interesting part of d is that acting on 1-forms. A general 1-form
on U has the shape
ω = P(x, y)dx + Q(x, y)dy
for functions P, Q ∈ C∞(U), and we see that
dω = ∂P
∂x dx ∧ dx + ∂P
∂y dy ∧ dx + ∂Q
∂x dx ∧ dy + ∂Q
∂y dy ∧ dy
=
(∂Q
∂x − ∂P
∂y
)
dx ∧ dy.
So if we consider ω as corresponding to the vector ﬁeld with components P, Q, then dω is obtained by mul-
tiplying the standard 2-form dx ∧ dy by what is sometimes called the scalar curl of this vector ﬁeld, ∂Q
∂x − ∂P
∂y , a
function which is probably familiar from Green’s theorem inmultivariable calculus.
Moving up a dimension to open subsets U ⊂ R3, a general 1-form on U has the form
ω = Pdx + Qdy + Rdz,
and we ﬁnd that in this case
dω =
(∂R
∂y − ∂Q
∂z
)
dy ∧ dz +
(∂P
∂z − ∂R
∂x
)
dz ∧ dx +
(∂Q
∂x − ∂P
∂y
)
dx ∧ dy.
We see that the three coeﬃcients above are the components of the curl of the vector ﬁeld ⟨P, Q, R⟩.
Meanwhile, a general 2-form on U can be written η = Pdy ∧ dz + Qdz ∧ dx + Rdx ∧ dy and so (because we
are working in R3) also corresponds to a vector ﬁeld ⟨P, Q, R⟩. We see that
dη =
(∂P
∂x + ∂Q
∂y + ∂R
∂z
)
dx ∧ dy ∧ dz,
and recognize the coeﬃcient from multivariable calculus as the divergence of the vector ﬁeld ⟨P, Q, R⟩.
Thus in dimension 3 the mapsd : Ω0(U) → Ω1(U), d : Ω1(U) → Ω2(U), and d : Ω2(U) → Ω3(U) correspond
respectively to the gradient, curl, and divergence operators from multivariable calculus. The fact that d ◦ d = 0
expresses the facts that the curl of a gradient is always zero, and that the divergence of a curl is always zero.
Again for open subsets U ⊂ R3, the ﬁrst de Rham cohomology group H1
dR(U) will be zero if and only if,
conversely, every vector ﬁeld whose curl is equal to zero is in fact the gradient of a function. You probably learned
2As I’ve emphasized elsewhere, on a general smooth manifold vector ﬁelds and 1-forms are di ﬀerent kinds of objects and one shouldn’t
try to identify them since they transform di ﬀerently under coordinate changes, but on Rn one can decide to only ever work in the standard
coordinate chart and then there won’t be any harm in making this identiﬁcation

32 MIKE USHER
in multivariable calculus that if U is all of R3 then this statement holds. However if U is more topologically
interesting it may not hold: for example there is the (misleadingly labeled) “dθ” form, given by
dθ = xdy − ydx
x2 + y2
deﬁned on U = {(x, y, z) ∈ R3|x2 + y2 /nequal0}, which you can verify to be closed, but which (despite the notation) is
not exact since it has nonzero integral around closed curves which enclose the z-axis (dθ wants to be the exterior
derivative of the polar coordinateθ, butθ is not a well-deﬁned smooth function on U).
Similarly, the second de Rham cohomology group of an open sub set U ⊂ R3 vanishes if and only if every
vector ﬁeld on U which has divergence equal to zero is in fact the curl of some other vector ﬁeld. If U = R3 then
this is true (we’ll prove a much more general statement not to o long from now), but this statement is false for
U = R3 \ {(0, 0, 0)}. A standard example illustrating this is the form
η = xdy ∧ dz + ydz ∧ dx + zdx ∧ dy
(x2 + y2 + z2)3/2
Physically,η corresponds to the electric ﬁeld on R3 \ {(0, 0, 0)} generated by a point charge located at the origin.
The statement that this vector ﬁeld is not the curl of another vector ﬁeld can be shown using Stokes’ theorem, by
taking the ﬂux integral of the vector ﬁeld over a sphere aroun d the origin. Later we’ll develop language for this
that generalizes such arguments substantially and stays wi thin the realm of di ﬀerential forms rather than vector
ﬁelds.
Exercise 4.20. (A coordinate-free formula for d): Let M be a smooth manifold,ω ∈ Ωp(M), and let X(0),..., X(p)
be vector ﬁelds on M. Prove that
(dω)(X(0),..., X(p)) =
p∑
i=0
(−1)iX(i)
(
ω(X(0),..., ˆX(i),..., X(p))
)
+
∑
i< j
(−1)i+ jω
(
[X(i), X( j)], X(0),..., ˆX(i),..., ˆX( j),..., X(p)
)
.
(To clarify the notation, if we have a diﬀerential q-formα and vector ﬁelds Y(1),..., Y(q), the function
m ↦→αm(Y(1)
m ,..., Y(q)
m )
is a smooth function, which we denote byα(Y(1),..., Y(q)). In particular since vector ﬁelds are derivations on the
space of smooth functions, ifZ is another vector ﬁeld we get another smooth function given by Z
(
α(Y(1),..., Y(q))
)
.
To do this problem, I would suggest ﬁrst showing that the value of the function on the right-hand side at a pointm
is unchanged if some (or all) X(i) are replaced by another vector ﬁeld ¯X(i) such that X(i)
m = ¯X(i)
m , and then proving
the result when the X(i) are (at least on a neighborhood of a given point) equal to stan dard coordinate vector
ﬁelds.)
4.3. Pullbacks of diﬀerential forms and the naturality of d. Letφ: M → N be a smooth map between two
smooth manifolds. Recall then that for each m ∈ M we have a derivative map φ∗ : TmM → Tφ(m)N, deﬁned in
terms of the derivation formalism by the simple formula
(φ∗v)( f ) = v( f ◦φ)
whenever f is a germ of a C∞ function deﬁned near φ(m) ∈ N. As described just before Proposition 4.7, this
induces for all m ∈ N a pullback operation
φ∗ : ΛpT ∗
φ(m)N → ΛpT ∗
mM
by setting, forα ∈ ΛpT ∗
φ(m)N and v1,..., vp ∈ TmM,
(φ∗α)(v1,..., vp) =α(φ∗v1,...,φ ∗vp).
In particular, when p = 1, so that ΛpT ∗
pM is just the cotangent space T ∗
pM,φ∗ coincides with the adjoint map
toφ∗ from linear algebra.

MATH 8210, FALL 2011 LECTURE NOTES 33
Theorem 4.21. Letφ: M → N be a smooth map and let ω ∈ Ωp(M) be a di ﬀerential form. Deﬁne a section
φ∗ω of ΛpT ∗M by
(φ∗ω)m =φ∗(ωφ(m)).
Thenφ∗ω is a diﬀerential form on M, and
(12) d(φ∗ω) =φ∗(dω).
The fact thatφ∗ω is a diﬀerential form requires proof, since there is a smoothness condition to check. In case
p = 0 (so thatω ∈ C∞(M)) the deﬁnition above should be read as saying that
φ∗ω :=ω ◦φ (ifω ∈ Ω0(M)).
Proof. Step 1: We prove the theorem when p= 0. Let h ∈ Ω0(M) = C∞(N) be a 0-form. By deﬁnitionφ∗h = h◦φ,
which is certainly a smooth function ( i.e. a 0-form) on M since compositions of smooth functions are smooth.
For all v ∈ TmM we have, by the deﬁnition of d on 0-forms:
(d(φ∗h))m(v) = v(φ∗h) = v(h ◦φ) = (φ∗v)(h) = (dh)φ(m)(φ∗v) = (φ∗dh)m(v).
This conﬁrms that d(φ∗h) = φ∗dh (It also conﬁrms that φ∗dh satisﬁes the smoothness condition required of a
1-form, since d(φ∗h) certainly does so.)
Step 2: We prove the theorem in case ω = f dg1 ∧ · · · ∧dgp for some f , g1,..., gp ∈ C∞(N). In this case, if
m ∈ M, we have (using Proposition 4.7 and Step 1)
(φ∗ω)m = f (φ(m))φ∗ (
(dg1)φ(m) ∧ · · · ∧(dgp)φ(m)
)
= ( f ◦φ)(m)
(
(φ∗dg1)m ∧ · · · ∧(φ∗dgp)m
)
= ( f ◦φ)(m)
(
d(g1 ◦φ)m ∧ · · · ∧d(gp ◦φ)m
)
,
i.e.
φ∗ω = ( f ◦φ)d(g1 ◦φ) ∧ · · · ∧d(gp ◦φ).
Now the space of diﬀerential forms is closed under wedge product (as the smoothness condition is easily seen to
be preserved), and the zero-form f ◦φ and the 1-forms d(gi ◦φ) are all diﬀerential forms by what we have already
done, so this proves thatφ∗ω is a diﬀerential form. Using the Leibniz rule and the fact that d2 = 0 we see that
d(φ∗ω) = d
(
( f ◦φ)d(g1 ◦φ) ∧ · · · ∧d(gp ◦φ)
)
= d( f ◦φ) ∧ d(g1 ◦φ) ∧ · · · ∧d(gp ◦φ)
= (φ∗d f) ∧ (φ∗dg1) ∧ · · · ∧φ∗(dgp)
=φ∗ (
d f ∧ dg1 ∧ · · · ∧dgp
)
= d
(
f dg1 ∧ · · · ∧dgp
)
= dω.
Step 3: We prove the result in general. By Proposition 4.19, any di ﬀerential formω ∈ Ωp(N) can be written
as a locally ﬁnite sum of forms of the type considered in Step 2 . Now the smoothness condition required of a
diﬀerential form is preserved under locally ﬁnite sums (since t he smoothness of a function can be checked by
looking at its restriction to each member of an open cover, we can reduce to the case of genuinely ﬁnite sums),
so using the linearity ofφ∗ it follows thatφ∗ω is a diﬀerential form. Similarly the R-linearity of d, together with
Step 2, implies that dφ∗ω =φ∗dω □
Corollary 4.22. A smooth mapφ: M → N between two smooth manifolds induces by the pullback opera tion a
mapφ∗ : Ω∗(N) → Ω∗(M). If ω ∈ Ω∗(N) is closed, thenφ∗ω ∈ Ω∗(M) is closed, and ifω ∈ Ω∗(N) is exact, then
φ∗ω ∈ Ω∗(M) is exact
Proof. The ﬁrst sentence has already been proven. Ifω is closed, i.e. dω = 0, then d(φ∗ω) =φ∗dω =φ∗0 = 0. If
ω is exact, i.e.ω = dη for someη ∈ Ω∗(N), thenφ∗ω =φ∗dη = d(φ∗η). □

34 MIKE USHER
Recall that we have deﬁned the pth de Rham cohomology of a smooth manifold M as the quotient vector
space
H p
dR(M) = {closed p-forms}
{exact p-forms} .
If we write H∗
dR(M) = ⊕∞
p=0H p
dR(M), the wedge-product induces a ring structure on H∗
dR(M): if a ∈ H p
dR(M) and
b ∈ Hq
dR(M), then we can ﬁnd closed forms ω ∈ Ωp(M), η ∈ Ωq(M), representing the classes a and b. Then
d(ω ∧η) = (dω) ∧η +(−1)pω ∧(dη) = 0, soω ∧η represents some cohomology class (denoteda ∪b) in H p+q
dR (M).
Moreover this cohomology class is independent of our particular choice of representativesω andη—for example
if we replacedω by some other form ¯ω =ω + dα, then
¯ω ∧η = (ω + dα) ∧η =ω ∧η + (dα) ∧η =ω ∧η + d(α ∧η)
(we’ve used thatdη = 0), i.e. the de Rham cohomology class of ¯ω ∧η is the same as that ofω ∧η (they diﬀer by
an exact form).
Using Proposition 4.6, one easily checks that this multipli cation on H∗
dR(M) (called the cup product) gives
H∗
dR(M) the structure of an associative, graded commutative R-algebra.
Corollary 4.23. If M and N are smooth manifolds andφ: M → N is a smooth map, we obtain a homomorphism
of graded R-algebras (in particular a ring homomorphism)φ∗ : H∗
dR(N) → H∗
dR(M) by settingφ∗[ω] = [φ∗ω] for
any closed formω on N. If φ is a diﬀeomorphism thenφ∗ is an isomorphism.
Proof. The ﬁrst sentence follows directly from various things that we have already done (check this for yourself
if it’s not clear). For the second, note thatφ∗ (acting either on forms or on cohomology) satisﬁes the functoriality
conditions (Id)∗ = (Id) and (φ ◦ψ)∗ = ψ∗ ◦φ∗ (note the order on the right hand side, reﬂecting that φ∗ “goes
in the opposite direction” to φ). From this it follows immediately that if φ is a di ﬀeomorphism then φ∗ is an
isomorphism with inverse (φ−1)∗. □
Exercise 4.24. If M is a smooth manifold, give an explicit formula, in terms of th e point-set topology of M,
for the degree-zero de Rham cohomology H0
dR(M). (As a point of convention, since there is no such thing as a
(−1)-form, we regard the exact 0-forms on M to consist only of 0.)

