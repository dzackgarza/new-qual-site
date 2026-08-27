Selected Problems in Real Analysis
(with solutions)
Dr Nikolai Chernov
Contents
1 Lebesgue measure 1
2 Measurable functions 4
3 Lebesgue integral: deﬁnition via simple functions 5
4 Lebesgue integral: general 7
5 Lebesgue integral: “equipartitions” 17
6 Limits of integrals of speciﬁc functions 20
7 Series of non-negative functions 31
8 Riemann integral vs Lebesgue integral 33
9 Lp spaces: general 34
10 Lp spaces: estimation of speciﬁc integrals 42
11 𝓁p spaces 46
1 Lebesgue measure
JPE, May 2011. Are the following true of false?
(a) If A is an open subset of [0 , 1], then m(A) = m( ¯A), where ¯A is the closure of
the set.
(b) If A is a subset of [0 , 1] such that m(int(A)) = m( ¯A), then A is measurable.
Here int(A) denotes the interior of the set.
(a) False. Counterexample: the complement to a modiﬁed Cantor set. Its measure
is < 1, but its closure is the entire interval [0 , 1].
(b) True. Indeed, we have
∂A = ¯A \ int(A) ⇒ m(∂A) = m( ¯A) −m(int(A)) = 0.
Now
A = int(A) ∪ (A \ int(A)), A \ int(A) ⊂∂A.
1

HenceA is the union of an open set, int( A), and a subset of the null set ∂A. Since
the latter is always measurable, we conclude that A is a measurable set.
JPE, Sept 2010. Is the following true of false?
Let E be a subset of Rn, and int( E) the set of all interior points of E. Then
int(E) = ∅ if and only if µ∗(E) = 0. (Here µ∗ denotes the outer measure.)
If µ∗(E) = 0, then m(E) = 0, so int( E) is indeed empty. But the converse is
not true. The set of points with irrational coordinates has inﬁnite measure and
empty interior.
JPE, May 2005. Show that if A ⊂ [0, 1] and m(A)> 0, then there are x and y
in A such that |x −y| is an irrational number.
If |x −y| ∈ Q for any x,y ∈A, then A ⊂x + Q for any point x ∈A, hence A
would be a countable set and we would have m(A) = 0.
JPE, Sept 2004 and Jan 1989. Is the following true or false?
There is a subset A of R which is not measurable, but such that B = {x ∈
A : x is irrational } is measurable.
False. The set A \B ⊂ Q is countable, hence measurable. So if B was measur-
able, then A =B ∪ (A \B) would be measurable, too.
JPE, May 2001. Does there exist a non-measurable subset of R whose comple-
ment in R has outer measure zero?
No. If the outer measure of a set is zero, then its inner measure is also zero, so
the set is measurable. Then its complement is measurable, too.
JPE, May 2000. Do there exist two non-measurable sets whose union is mea-
surable?
Yes. If A is any non-measurable set, then its complement Ac is also non-
measurable, but their union is the whole space (a measurable set).
JPE, May 2000. Is the following true of false?
If the boundary of Ω ⊂ Rk has outer measure zero, then Ω is measurable.
True. Since the outer measure of ∂Ω is zero, its inner measure is zero, too,
hence its Lebesgue measure is zero. Then any subset of ∂Ω is a null set, and
therefore it is measurable, too. Now Ω is the union of two sets:
Ω = int(Ω) ∪ (Ω \ int(Ω)).
Note that int(Ω) is an open set, hence it is measurable. And (Ω \ int(Ω)) ⊂∂Ω is
a subset of a null set, hence it is also measurable. Therefore Ω is measurable.
2

JPE, May 1998. Let A ⊂ [0, 1] be a non-measurable set. Let B = {(x, 0) ∈
R2 : x ∈A}.
(a) Is B a Lebesgue measurable subset of R2?
(b) Can B be a closed subset of R2 for some such A?
(a) Yes. The set B is a subset of a straight line ( y = 0), so it has outer measure
zero. Thus it is Lebesgue measurable.
(b) No. If B was closed in R2, then A would be closed in [0 , 1], and then it would
be measurable.
JPE, Sept 1997. For a measurable subset E ⊂ Rn, prove or disprove:
(a) If E has Lebesgue measure zero, then its closure has Lebesgue measure zero.
(b) If the closure of E has Lebesgue measure zero, then E has Lebesgue measure
zero.
(a) False. Example: E consists of points with all rational coordinates. E is count-
able, hencem(E) = 0. On the other hand, E is dense in Rn, hence its closure is Rn.
(b) True. Since E is a subset of its own closure, then E also has Lebesgue measure
zero.
JPE, May 1993. Let rn be an enumeration of rational numbers in R.
(a) Show that R \ ∪∞
n=1(rn − 1
n2,rn + 1
n2 ) is never empty.
(b) Show that R \ ∪∞
n=1(rn − 1
n,rn + 1
n) can be empty or non-empty, depending on
how the rationals are enumerated.
(a) By the σ-subadditivity of the Lebesgue measure
m
(
∪∞
n=1(rn − 1
n2,rn + 1
n2 )
)
≤
∞∑
n=1
m
(
(rn − 1
n2,rn + 1
n2 )
)
=
∞∑
n=1
2
n2 < ∞,
thus these intervals cannot cover the entire R.
(b) Now the above estimate gives ∑∞
n=1
2
n = ∞, thus our previous argument would
not work. However presenting speciﬁc examples of enumeration so that the above
intervals cover (or do not cover) R is not easy. Let us not get into these complica-
tions...
JPE, May 1990. Does there exist a measure space ( X, M,µ ) such that there is
no countable collection of subsets Xn ∈ M satisfying µ(Xn) < ∞ for all n and
X = ∪∞
n=1Xn.
Yes. Example: µ is the counting measure on R with Borel σ-algebra.
JPE, May 1989. Does there exist an open dense subset A ⊂ [0, 1] × [0, 1] such
that its complement ([0 , 1] × [0, 1]) \A has positive Lebesgue measure?
3

Yes. The complement to a modiﬁed two-dimensional Cantor set.
2 Measurable functions
JPE, Sept 2011. Is the following true of false?
If f : [0, 1] → R is continuous a.e., then f is measurable.
True. Let E ⊂ [0, 1] be the set of points where f is discontinuous. We have
m(E) = 0. The restriction of f toEc = [0, 1] \E is continuous, hence for any open
setU ⊂ R its preimage f −1(U )∩Ec is open in Ec, therefore f −1(U ) = (V ∩Ec)∩B
for some open set V ⊂ [0, 1] and some subset B ⊂ E. Any subset of the null set
E is measurable, hence f −1(U ) is a measurable set.
JPE, Sept 2011 and May 2005. Let f : [0, 1] → R. Is it true that if the set
{x ∈ [0, 1] :f (x) = c} is measurable for every c ∈ R, then f is measurable?
False. Let A ⊂ [0, 1] be a non-measurable set. Deﬁne f (x) = x on A and
f (x) = −x on [0, 1] \A. This function is injective, hence {x ∈ [0, 1] :f (x) = c}
is either empty or a one-point set (a singleton) for each c ∈ R; in either case it is
measurable. But f −1([0, 1]) = A is a non-measurable set.
JPE, Sept 2009. Does there exist a sequence {fk} of Lebesgue measurable
functions such thatfk converges to 0 in measure on R but no subsequence converges
uniformly on any subset of positive measure?
No. In one of the homework exercises, we proved that if fk converges in measure,
then there is a subsequence {fnk} that converges a.e. Now by Egorov’s theorem
the convergence must be uniform on a set of positive measure.
JPE, Sept 2007. Show that fn(x) = e−n|1−sinx| converges in measure to f (x) = 0
on [a,b ] ⊂ R.
We have
|fn −f |>ε ⇔ e−n|1−sinx| >ε ⇔ | 1 − sinx|< 1
n ln 1
ε
Note that sin x = 1 whenever x = π
2 + 2kπ (k ∈ N). Thus the above inequality
|1 − sinx|< 1
n ln 1
ε speciﬁes a neighborhood of each point x = π
2 + 2kπ whose size
shrinks as n → ∞ . Note that there can only be ﬁnitely many points π
2 + 2kπ in
any ﬁnite interval [ a,b ]. Thus the Lebesgue measure of the union of the above
neighborhoods of these points tends to zero as n → ∞.
If we replace a ﬁnite interval [ a,b ] with an inﬁnite interval, such as ( a, ∞) or
(−∞,b ), then there would be inﬁnitely many of the above points π
2 + 2kπ and
their neighborhoods within the given interval, and then their union would have an
4

inﬁnite measure. In that case the convergence in measure would fail.
JPE, Sept 2005. Is the following true of false?
If f : [0, ∞) → R is diﬀerentiable, then f ′ is measurable.
True. The derivative can be computed as the following limit
f ′(x) = lim
n→∞
f (x + 1
n) −f (x)
1
n
,
which exists because f is assumed to be diﬀerentiable at every point x ∈ R. Thus
f ′ is a limit of measurable functions, hence it is measurable.
JPE, May 2001. Does there exist a non-measurable function f ≥ 0 such that√f is measurable?
No. Indeed, f = ( √f )2 is a composition of a measurable function √f and a con-
tinuous (and thus Borel) function, x2, thus f is measurable.
JPE, May 1994 Let {fn} be a sequence of measurable functions on a measurable
space (X, M). Deﬁne the set
E = {x ∈X : lim
n→∞
fn(x) exists }
Show that E is a measurable set.
Letg(x) = lim supn→∞fn(x) and h(x) = lim infn→∞fn(x). We know that both
functions g(x) and h(x) are measurable. Also recall that lim n→∞fn(x) exists if
and only if g(x) = h(x). Now E = {x ∈X : g(x) = h(x)}, hence E is measurable.
3 Lebesgue integral: deﬁnition via simple func-
tions
JPE, May 2008. Is the following true or false?
For every non-negative, bounded and measurable function f on [0, 1],
∫
[0,1]
fdm = inf
∫
[0,1]
ϕdm
, where the inﬁmum is taken over all simple measurable functions ϕ with f ≤ϕ.
True. Since f is bounded, let M = supf be its upper bound. Now for every
simple function ϕ ≥f there is a simple function ψ such that ψ ≤M andf ≤ψ ≤
ϕ. Indeed, it is enough to take ψ = min{ϕ,M }. Note that
∫
[0,1]ψdm ≤
∫
[0,1]ϕdm ,
5

hence
inf
f ≤ϕ
∫
[0,1]
ϕdm = inf
f ≤ψ≤M
∫
[0,1]
ψdm,
i.e., it is enough to use only simple functions ψ satisfying f ≤ψ ≤M .
Nowg =M −f is a nonnegative measurable function bounded by M , thus
M −
∫
[0,1]
fdm =
∫
[0,1]
gdm = sup
0≤s≤g
∫
[0,1]
sdm
where the inﬁmum is taken over all simple functions s such that 0 ≤ s ≤ g.
For each such s we have ψ = M −s a simple function satisfying f ≤ ψ ≤ M .
Conversely, for every simple function ψ satisfyingf ≤ψ ≤M we have s =M −ψ
a simple function satisfying 0 ≤s ≤g. Thus the above identity gives
∫
[0,1]
fdm = − sup
f ≤ψ≤M
∫
[0,1]
(−ψ)dm = inf
f ≤ψ≤M
∫
[0,1]
ψdm.
JPE, May 2004. Is the following true or false?
Let f ≥ 0 be bounded and measurable on R. Then
∫
R
fdm = inf
∫
R
φdm
where the inﬁmum is taken over all simple measurable functions φ with f ≤φ?
False. This would be true if the measure of the whole space was ﬁnite (like in
the previous problem). But here m(R) = ∞, in which case the claim is false.
A counterexample is any bounded function f (x) ∈ L1
m(R) such that f (x) > 0
for all x ∈ R. For example, f (x) = e−x2
or f (x) = 1
1+x2 , which you might
remember from Calculus or Probability Theory. If you do not remember any, you
can construct f as follows:
f =
∞∑
n=−∞
2−|n|χ[n,n+1)
For this function we have
∫
R
fdm =
∞∑
n=−∞
2−|n| = 3 < ∞
Now since f (x) > 0 for all x ∈ R, then any simple function φ ≥ f must also be
positive everywhere, so that in the representation
φ =
n∑
i=1
αiχAi
6

all the values αi are positive: αi > 0 for all i = 1,...,n . At the same time at least
one subset Ai0 must have inﬁnite measure, i.e., m(Ai0) = ∞. Therefore
∫
φdm =
n∑
i=1
αim(Ai) ≥αi0m(Ai0) = ∞
for every simple function φ ≥f . Thus inf
∫
Rφdm = ∞, while
∫
Rfdm< ∞.
4 Lebesgue integral: general
JPE, May 2011. Prove that a measurable function f (x) belongs to L1(0, 1) if
and only if
∞∑
n=1
2n ·m{x ∈ [0, 1] : |f (x)| ≥ 2n}< ∞.
JPE, May 2006. Letµ(X)< ∞. Prove that a non-negative measurable function
f (x) belongs to L1(X,µ ) if and only if
∞∑
n=1
2n ·µ{x ∈X : f (x) ≥ 2n}< ∞.
The above two problems are almost identical, we only solve the ﬁrst one. Let
us partition [0, 1] into subsets
E0 = {x : |f (x)|< 2} g(x) = 1
E1 = {x : 2 ≤ |f (x)|< 22} g(x) = 2
...
En = {x : 2n ≤ |f (x)|< 2n+1} g(x) = 2n
...
and a new function g byg(x) = 2n for all x ∈En, as shown above. Note that
g(x) − 1 ≤ |f (x)| ≤ 2g(x) ⇒
∫
g − 1 ≤
∫
|f | ≤ 2
∫
g,
thusf ∈L1(0, 1) if and only if g ∈L1(0, 1).
Denote
S : =
∞∑
n=1
2n ·m{x ∈ [0, 1] : |f (x)| ≥ 2n}
and observe that
m{x : |f (x)| ≥ 2n} =
∞∑
k=n
m(Ek).
7

Now on the one hand,
∫
[0,1]
gdm =
∞∑
n=0
2nm(En) ≤ 2m(E0) +
∞∑
n=1
2nm{x : |f (x)| ≥ 2n} ≤ 2 +S.
On the other hand,
S =
∞∑
n=1
2n
∞∑
k=n
m(Ek) =
∞∑
k=1
m(Ek)
k∑
n=1
2n ≤
∞∑
k=1
2k+1m(Ek) ≤ 2
∫
[0,1]
gdm
thus S
2 ≤
∫
[0,1]
gdm ≤S + 2.
This implies g ∈L1(0, 1) if and only if S <∞.
JPE, May 2010. Is the following true or false?
Let {fk} be a sequence of non-negative measurable functions on R such thatfk →f
a.e. in R. Then lim k→∞
∫
Rfkdm exists and
∫
R
fdm ≤ lim
k→∞
∫
R
fkdm.
False. The limit need not exist. For example, let
f ≡ 0 and fk =k
(
1 + (−1)k)
χ[0,k−1]
Then
∫
Rfkdm alternatively takes values 2 (for all even k) and 0 (for all odd k), so
it does not have a limit.
We note, however, that whenever lim k→∞
∫
Rfkdm does exist, the claimed in-
deed immediately follows from Fatou’s Lemma.
JPE, May 2010. If f ∈L1(0, 1), ﬁnd
lim
k→∞
∫ 1
0
k ln
(
1 + |f (x)|2
k2
)
dx.
The limit is zero. The integrand can be written (and bounded above) as
1
k ln
(
1 + |f (x)|2
k2
)k2
≤ 1
k lne|f (x)|2
= 1
k |f (x)|2,
thus it converges to zero pointwise a.e. (more precisely, for every x ∈ [0, 1] such
that |f (x)|< ∞). However, the Lebesgue Dominated Convergence does not apply
(yet), because |f 2| is not necessarily inL1(0, 1), i.e., we may have
∫ 1
0 |f (x)|2dx = ∞
(example: f (x) = 1/√x is in L1(0, 1), but
∫ 1
0 |f (x)|2dx = ∞).
8

To get a better upper bound we can use an elementary inequality ln(1 + t) ≤
2
√
t, which is true for all t ≥ 0; see a proof below. This inequality gives
k ln
(
1 + |f (x)|2
k2
)
≤ 2k |f (x)|
k = 2|f (x)|,
which is integrable. Now the Lebesgue Dominated Convergence applies and ﬁnishes
the job. Lastly, here is the proof of the elementary inequality:
ln(1 +t) ≤ 2
√
t ⇔ 1 +t ≤e2
√
t = 1 + 2
√
t + 4t
2 + · · ·
and the latter is obvious.
JPE, Sept 2009 and Sept 2004. Assume that {fn}, {gn},f,g are in L1(Rn),
fn → f pointwise a.e., gn → g pointwise a.e., |fn| ≤ gn a.e., and
∫
Rngndm →∫
Rngdm . Show that
∫
Rnfndm →
∫
Rnfdm .
By the triangle inequality |fn −f | ≤ gn + |f |, hence
gn + |f | − |fn −f | ≥ 0.
Now by Fatou’s Lemma (as in the proof of Lebesgue Dominated Convergence)
∫
g +
∫
|f | =
∫
lim inf(gn + |f | − |fn −f |)
≤ lim inf
∫
(gn + |f | − |fn −f |)
= lim inf
(∫
gn +
∫
|f | −
∫
|fn −f |
)
=
∫
g +
∫
|f | − lim sup
∫
|fn −f |
therefore
∫
|fn −f | → 0. Lastly, by the integral triangle inequality
⏐⏐⏐⏐
∫
fn −
∫
f
⏐⏐⏐⏐ =
⏐⏐⏐⏐
∫
(fn −f )
⏐⏐⏐⏐ ≤
∫
|fn −f | → 0,
therefore
∫
fn →
∫
f .
JPE, Sept 2009 and Oct 1990 Assume that {fk} and f are in L1(Rn) and
fk → f pointwise a.e. and
∫
Rn |fk| →
∫
Rn |f |. Show that for any measurable set
E ⊂ Rn ∫
E
fkdm →
∫
E
fdm
By the triangle inequality
⏐⏐|fk| − |fk −f |
⏐⏐ ≤ |f |.
9

Since f ∈L1(Rn), the Lebesgue Dominated Convergence gives
∫
Rn
|fk| −
∫
Rn
|fk −f | =
∫
Rn
(
|fk| − |fk −f |
)
− − − →
k→∞
∫
Rn
|f |
therefore
∫
Rn |fk −f | → 0. Lastly by the integral triangle inequality
⏐⏐⏐⏐
∫
E
fk −
∫
E
f
⏐⏐⏐⏐ =
⏐⏐⏐⏐
∫
E
(fk −f )
⏐⏐⏐⏐ ≤
∫
E
|fk −f | ≤
∫
Rn
|fk −f | → 0.
JPE, May 2009. Let f ∈ L1([0, 1]) be real-valued. Prove the following state-
ments:
(a) xkf (x) ∈L1([0, 1]) for all k ∈ N.
(b) limk→∞
∫ 1
0 xkf (x)dx = 0.
(c) If lim x↑1f (x) = a for some real number a, then
lim
k→∞
k
∫ 1
0
xkf (x)dx =a.
(a) |xkf (x)| ≤ |f (x)|, hence xkf (x) ∈L1([0, 1]).
(b) We have xkf (x) → 0 as k → ∞ for all x ∈ [0, 1). Then the claim follows from
Part (a) and the Lebesgue Dominated Convergence.
(c) An elegant solution exists when f is continuously diﬀerentiable. Since lim k+1
k =
1, we can replace the factor k with k + 1 and then integrate by parts:
(k + 1)
∫ 1
0
xkf (x)dx =
∫ 1
0
f (x)dxk+1 =xk+1f (x)
⏐⏐⏐
1
0
−
∫ 1
0
xk+1f ′(x)dx.
The ﬁrst terms is
xk+1f (x)
⏐⏐⏐
1
0
= 1k+1f (1) − 0k+1f (0) = a,
and the second converges to zero, due to Part (b).
Next we outline a solution for an arbitrary f ∈L1([0, 1]).
(i) Choose small ε> 0 and δ >0 such that |f (x) −a|<ε for all x ∈ (1 −δ, 1].
(ii) Show that lim k→∞k
∫ 1−δ
0 xkf (x)dx = 0 by using the Lebesgue Dominated
Convergence. Note that
sup
k≥1
sup
x∈[0,1−δ)
kxk = sup
k≥1
k(1 −δ)k < ∞,
which provides an integrable upper bound. Now it is enough to prove that
lim
k→∞
k
∫ 1
1−δ
xkf (x)dx =a.
10

(iii) Note that a −ε<f (x)<a +ε on the interval [1 −δ, 1], thus
(a −ε)k
∫ 1
1−δ
xkdx ≤k
∫ 1
1−δ
xkf (x)dx ≤ (a +ε)k
∫ 1
1−δ
xkdx.
Computing the integral
∫ 1
1−δ
xkdx = 1 − (1 −δ)k+1
k + 1
gives
(a −ε)k
k + 1
[
1 − (1 −δ)k+1]
≤k
∫ 1
1−δ
xkf (x)dx ≤ (a +ε)k
k + 1
[
1 − (1 −δ)k+1]
Taking the limitk → ∞ shows that the middle integral will be eventually “squeezed”
betweena −ε and a +ε. Since ε> 0 is arbitrary, Part (c) follows.
JPE, May 2009. Suppose that fn is a sequence of non-negative Lebesgue mea-
surable functions on (0 , 10) such that fn(x) →f (x) for almost all x ∈ (0, 10). Let
F (x) =
∫x
0 fdm and Fn(x) =
∫x
0 fndm. Prove that
∫ 10
0
(f +F )dm ≤ lim inf
n→∞
∫ 10
0
(fn +Fn)dm.
We apply Fatou’s Lemma twice. First,
F (x) =
∫ x
0
fdm =
∫ x
0
lim inffndm ≤ lim inf
∫ x
0
fndm = lim infFn(x).
Second,
∫ 10
0
(f +F )dm ≤
∫ 10
0
(f + lim infFn)dm
=
∫ 10
0
lim inf(fn +Fn)dm
≤ lim inf
∫ 10
0
(fn +Fn)dm.
JPE, Sept 2008. Letf ∈L1(0, ∞). Prove that there is a sequence xn → ∞ such
that limn→∞xnf (xn) = 0.
Denote c = lim infx→∞x|f (x)|. If c = 0, then a sequence as above exists. If
c> 0, then there exists A> 0 such that x|f (x)|>c/ 2 for all x>A . Then
∫
(0,∞)
|f |dm ≥
∫
(A,∞)
|f |dm ≥
∫ ∞
A
c
2xdx = ∞,
11

which contradicts the assumption f ∈L1(0, ∞).
JPE, May 2008 and Sept 2009. Is the following true or false?
There exists a sequence {fn} of functions in L1(0, ∞) such that |fn(x)| ≤ 1 for all
x and for all n, limn→∞fn(x) = 0 for all x, and
lim
n→∞
∫
(0,∞)
fndm = 1.
True. An example: fn =n−1χ(0,n).
JPE, May 2003. Is the following true or false?
There exists a sequence {fn} of functions in L1(0, 1) such that fn → 0 pointwise
and yet
∫
[0,1]fndm → ∞.
True. An example: fn =n2χ(0,n−1).
JPE, May 2008 and Oct 1991. Is the following true or false?
There exists a sequence {gn} of functions on [0 , 1] such that
lim
n→∞
∫
[0,1]
gndm = 0
but gn(x) converges for no x ∈ [0, 1].
True. See “Amazing shrinking sliding rectangles” in the class notes. Note:
in the 1991 version, the functions gn must be continuous. This requires a slight
modiﬁcation of the “sliding rectangles” example.
JPE, Sept 2004. Is the following true or false?
There are measurable functions fn,n = 1, 2,... , and f on [0, 1] such that fn(x) →
f (x) for every x ∈ [0, 1], but
∫
[0,1]fndm →/
∫
[0,1]fdm .
True. Example: fn =nχ(0, 1
n ) and f = 0.
12

JPE, May 2004. Let f ≥ 0 on [0, 1] be measurable.
(a) Show that
∫
[0,1]fndm converges to a limit in [0 , ∞] as n → ∞.
(b) If
∫
[0,1]fndm = C < ∞ for all n = 1, 2,... , then prove the existence of a
measurable subset B of [0, 1] such that f (x) = χB(x) for almost every x.
(Question (b) was given, as a separate problem, in JPE, Jan 1989. )
JPE, May 1995. Let f ≥ 0 on [0 , 1] be measurable. Suppose that
lim supn
∫
[0,1]fndm< ∞. Prove that f (x) ≤ 1 a.e. on [0 , 1].
JPE, Sept 1993. Let f ≥ 0 on [0, 1] be measurable. Prove that lim n
∫
[0,1]fndm
exists (as a ﬁnite number) if and only if m({x ∈ [0, 1] :f (x)> 1}) = 0.
See also a much harder version of this problem in Section on the Lp spaces.
We solve the 2004 problem. The 1995 and 1993 problems will follow as a side
result.
Part (a): Let us partition [0 , 1] into four subsets:
G = {x ∈ [0, 1] :f (x)> 1}
E = {x ∈ [0, 1] :f (x) = 1 }
L = {x ∈ [0, 1] : 0 <f (x)< 1}
Z = {x ∈ [0, 1] :f (x) = 0 }.
Note that ∫
E
fndm =m(E) and
∫
Z
fndm = 0
for all n = 1, 2,... . Next, we have
f (x)<f 2(x)<f 3(x)<... → ∞ for all x ∈G
f (x)>f 2(x)>f 3(x)>... → 0 for all x ∈L.
On the subset G ⊂ [0, 1] we apply the Lebesgue Monotone Convergence:
lim
n→∞
∫
G
fndm =
∫
G
∞dm = ∞ ·m(G).
On the subset L ⊂ [0, 1], we have fn(x)< 1 for all n and all x ∈L, hence we can
apply the Lebesgue Dominated Convergence:
lim
n→∞
∫
L
fndm =
∫
L
0dm = 0.
Putting it all together gives
lim
n→∞
∫
[0,1]
fndm = ∞ ·m(G) +m(E).
13

solving Part (a). Note that
∞ ·m(G) =
{ ∞ if m(G)> 0
0 if m(G) = 0
which solves the 1995 problem, too.
Part (b): The assumption
∫
[0,1]fndm =C <∞ implies that
lim
n→∞
∫
[0,1]
fndm =C <∞
thus we must have m(G) = 0. In addition, we must have m(L) = 0. Indeed, if
m(L)> 0, then we would have
f (x)>f 2(x) ( ∀x ∈L) ⇒
∫
L
fdm>
∫
L
f 2dm ⇒
∫
[0,1]
fdm>
∫
[0,1]
f 2dm
As a result, f =χE a.e.
JPE, May 2001. Let f and fn, n = 1, 2,... , be non-negative measurable func-
tions on [0, 1] such that fn converges pointwise to f . Under each of the following
additional assumptions, either prove that
∫ 1
0 fdm →
∫ 1
0 fdm or show that this is
not generally true.
(a) fn ≥f and fn ∈L1([0, 1]) for all n.
(b) fn ≥fn+1 for all n.
(c) fn ≤f for all n.
(Question (b) was also given in JPE, Sept 1993 and Jan 1989 .)
(Question (c) was also given in JPE, Sept 1995 .)
(a) False: fn =nχ(0,1/n) and f = 0.
(b) False: fn = 1/(nx) and f = 0. (Note that
∫ 1
0 fndm = ∞ for all n.)
(c) True. First note that we cannot apply Lebesgue Dominated Convergence,
because f may not be integrable. We proceed as follows. On the one hand,
fn ≤f ⇒
∫ 1
0
fndm ≤
∫ 1
0
fdm ⇒ lim sup
∫ 1
0
fndm ≤
∫ 1
0
fdm
On the other hand, by Fatou’s Lemma
∫ 1
0
fdm =
∫ 1
0
lim inffndm ≤ lim inf
∫ 1
0
fndm,
thus lim
∫ 1
0 fndm exists and is equal to
∫ 1
0 fdm .
14

JPE, May 1999. Letf ∈L1(R) and E1 ⊂E2 ⊂ · · · be measurable subsets of R.
Prove that
lim
n→∞
∫
En
fdm
exists.
The above limit equals
∫
Efdm , where E = ∪n≥1En. Indeed, we have
⏐⏐⏐⏐
∫
E
fdm −
∫
En
fdm
⏐⏐⏐⏐ =
⏐⏐⏐⏐
∫
E\En
fdm
⏐⏐⏐⏐ ≤
∫
E\En
|f |dm.
We know that µ(A) =
∫
A |f |dm is a measure on R, and µ(R) =
∫
R |f |dm <∞.
Thus by the continuity
∫
E\En
|f |dm =µ(E \En) →µ(E \ ∪∞
n=1En) = µ(∅) = 0.
JPE, Sept 1995, May 1995 and May 1989. Let α > 2 be a real number.
Deﬁne
E =
{
x ∈ [0, 1] :
⏐⏐⏐x − p
q
⏐⏐⏐<q −α for inﬁnitely many p,q ∈ N2
}
.
Prove that m(E) = 0.
In the May 1995 and May 1989 versions, α was set to 3.
Denote
Ep,q =
{
x ∈ [0, 1] :
⏐⏐⏐x − p
q
⏐⏐⏐< 1
qα
}
.
Note that m(Ep,q) = 2/qα, and 0 ≤p ≤q. Thus
∑
p,q
m(Ep,q) ≤
∞∑
q=1
2(q + 1)
qα ≤
∞∑
q=1
4
qα−1 < ∞,
so the claim follows from the Borel-Cantelli lemma.
JPE, May 1995. Assume that f and fn are measurable functions on [0 , 1] and
that fn ≥ 0 a.e. on [0 , 1]. Prove that
∫
[0,1]
fne−fndm →
∫
[0,1]
fe −fdm.
Note that it is not necessarily true that
∫
[0,1]fndm →
∫
[0,1]fdm under the given
conditions. For example, let f ≡ 0 and fn =nχ(0, 1
n ). Then we have fn(x) →f (x)
for all x ∈ [0, 1] but
∫
[0,1]fndm = 1 ⁄= 0 =
∫
[0,1]fdm .
15

It is then really amazing that
∫
[0,1]fne−fndm →
∫
[0,1]fe −fdm.
The reason is that fn(x)e−fn(x) → f (x)e−f (x) a.e. (quite obviously), and the
integrands here are bounded by one integrable function:
0 ≤fn(x)e−fn(x) ≤g(x) = 1.
In fact, the bound can be tightened: the function te−t for t ≥ 0 reaches its maxi-
mum at t = 1 and its maximum value is e−1 < 1.
Now the Lebesgue Dominated Convergence applies and completes the solution.
JPE, Sept 1994. Let (X, M,µ ) be a measure space with a positive measure µ.
Let f be a non-negative function on X such that for any n = 1, 2,... there are
two measurable functions gn and hn on X such that gn(x) ≤f (x) ≤hn(x) for all
x ∈X, and
∫
X(hn −gn)dµ< 1
n. Prove that f is measurable and
∫
X
fdµ = lim
n→∞
∫
X
gndµ.
Note that hn −gn ≥ 0, hence
∫
X(hn −gn)dµ = ‖hn −gn‖1, so we have ‖hn −
gn‖1 < 1
n, i.e., ‖hn−gn‖1 → 0. By a corollary proved in class, there is a subsequence
nk such that hnk −gnk → 0 a.e.
A side note: we can arrive at the same conclusion without using the corollary
or the 1-norm. We can ﬁrst prove that
∫
X(hn −gn)dµ → 0 implies hn −gn → 0 in
measure, and then refer to a homework exercise were we proved that convergence
in measure implies the existence of a subsequence converging a.e.
Now since hnk(x) −gnk(x) → 0 a.e. and gnk(x) ≤f (x) ≤hnk(x), then gnk(x) →
f (x) a.e. In other words, there is a full measure set E ⊂X such thatgnk(x) →f (x)
for all x ∈E. Thus the restriction f |E off toE is a limit of measurable functions,
hence f |E is measurable. The values of f on the null set X \E do not aﬀect the
measurability of f , hence f is measurable on the whole space X.
Next we need to prove that
∫
Xgndµ exists in a certain sense. The function gn
is not necessarily non-negative, so the existence of
∫
Xgndµ is not a trivial issue.
Since hn(x) ≥f (x) ≥ 0, we have
0 ≤g−
n (x) = max {0, −gn(x)} ≤ max{0,hn(x) −gn(x)} =hn(x) −gn(x),
hence ∫
X
g−
n dµ ≤
∫
X
(hn −gn)dµ< ∞.
This implies that
∫
Xgndµ exists, at least in the extended sense (deﬁned in class);
though note that its value may be + ∞. Also note that f ≥ 0 and f −gn ≥ 0, so
the existence of
∫
Xfdµ and
∫
X(f −gn)dµ need no justiﬁcation. Now we have
f =gn + (f −gn) ⇒
∫
X
fdµ =
∫
X
gndµ +
∫
X
(f −gn)dµ.
16

Note that
0 ≤
∫
X
(f −gn)dµ ≤
∫
X
(hn −gn)dµ ≤ 1
n.
Thus taking the limit n → ∞ proves the last claim of the problem.
JPE, May 1990. Does there exist a sequence of functions fn ∈ L1(R) that
converges uniformly to zero on every compact set, but
∫
Rfndm = 1 for all n?
Yes, Example: fn =χ(n,n+1).
JPE, May 1990. Let f be a non-negative function deﬁned on R. Assume that
for all n ≥ 1 ∫
R
n2
n2 +x2f (x)dm ≤ 1.
Show that f ∈L1(R) and ‖f ‖1 ≤ 1.
Note that for each x ∈ R, the sequence n2
n2+x2 monotonically increases and
converges to 1, as n → ∞. Thus the integrand n2
n2+x2f (x) monotonically increases
(in n) and converges to f (x) as n → ∞. By the Lebesgue Monotone Convergence
∫
R
n2
n2 +x2f (x)dm →
∫
R
f (x)dm = ‖f ‖1.
JPE, Sept 1989. Let fn be a sequence of continuous functions Lebesgue inte-
grable on [0, ∞) which converges uniformly to a function f Lebesgue integrable on
[0, ∞). Is it true that
lim
n→∞
∫ ∞
0
|f (x) −fn(x)|dx = 0.
False. Example: we set f (x) ≡ 0 and deﬁne fn byfn(x) = 1
n − x
n2 forx ∈ (0,n )
and f (x) = 0 for x ≥n. Then
∫ ∞
0 |f (x) −fn(x)|dx = 1
2 for all n.
5 Lebesgue integral: “equipartitions”
Note: in all the problems of this section the function f must be real-valued, even
though this assumption is NOT made explicitly in any of them, for some reason.
JPE, May 2011. Letf ∈L1(−∞, ∞). Let {an} be a sequence of strictly positive
numbers, i.e., an > 0 for any n, such that ∑∞
n=1an = 1. Prove that there exists a
partition of R into measurable sets {En}∞
n=1 such that
∫
En
fdm =am
∫
Rfdm for
all n.
17

Consider the function F (x) =
∫
(−∞,x)fdm . It is a continuous function on R.
Indeed,
F (x +δ) −F (x) =
∫
[x,x+δ)
fdm
By the triangle inequality
|F (x +δ) −F (x)| ≤
∫
[x,x+δ)
|f |dm
We know that µ(E) =
∫
E |f |dm is a measure in R, and it is a ﬁnite measure
because µ(R) =
∫
R |f |dm< ∞. Hence by the continuity we have
∫
[x,x+δ)
|f |dm =µ
(
[x,x +δ)
)
− − →
δ→0
µ({x}) =
∫
{x}
|f |dm = 0,
because {x} is a singleton whose Lebesgue measure is zero. (Note: the continuity
of F (x) was a separate problem in JPE, Sept 1995 and May 1992. )
Next, we have the following limits:
lim
x→−∞
F (x) = 0, lim
x→∞
F (x) = I : =
∫
R
fdm.
Indeed,
|F (x)| ≤
∫
(∞,x)
|f |dm
and by the continuity we have
lim
x→−∞
∫
(−∞,x)
|f |dm =
∫
∅
|f |dm = 0,
Similarly,
|I −F (x)| ≤
∫
[x,∞)
|f |dm
and by the continuity we have
lim
x→∞
∫
[x,∞)
|f |dm =
∫
∅
|f |dm = 0.
Now suppose ﬁrst that I ⁄= 0. By the intermediate value theorem there are points
−∞<x 1 <x 2 < · · ·< ∞ such that
F (xn) = (a1 + · · · +an)I for all n ≥ 1.
Letx∗ = limn→∞xn. If x∗ = ∞, we choose E1 = (−∞,x 1] and En = (xn−1,xn] for
alln ≥ 2. If x∗ < ∞, then
∫
[x∗,∞)fdm = 0, and we choose E1 = (−∞,x 1]∪[x∗, ∞)
and En = (xn−1,xn] for all n ≥ 2.
18

In the caseI = 0, i.e.,
∫
Rfdm = 0, we can just choose E2,E 3,... to be arbitrary
disjoint null sets, and deﬁne E1 = R \ ∪∞
n=2En.
Note: in the case
∫
Rfdm = 0 we can also choose sets En diﬀerently, so that
each of them has positive measure. To this end we need to apply the previous
argument to f + and f − separately.
JPE, May 2003. Let f be integrable on [0 , 1]. Prove that there exists c ∈ [0, 1]
such that
∫
[0,c]fdm =
∫
[c,1]fdm .
Similarly to the previous problem, let F (c) =
∫
[0,c]fdm −
∫
[c,1]fdm . It is a
continuous function on [0 , 1] and F (0) = −F (1). If F (0) ⁄= 0, the existence of c
such that F (c) = 0 follows from the intermediate value theorem. If F (0) = 0, we
can choose c = 0 (or c = 1).
Note: in the case F (0) = 0 the choices c = 0 and c = 1 may be the only
possible. Example: f (x) = sin(πx). We have
∫ 1
0 f (x) = 0, but for any c ∈ (0, 1)
we have
∫
[0,c]f (x)> 0 and
∫
[c,1]f (x)< 0.
JPE, Sept 2007 and May 2001. Let f ∈ L1(R2). Prove that there exists a
subset E ⊂ R2 such that ∫
E
fdm =
∫
R2\E
fdm.
Similarly to the previous two problems, let
F (r) =
∫
Dr
fdm −
∫
R2\Dr
fdm,
where Dr = {(x,y ) :x2 +y2 < r2} is the disk of radius r centered at the origin.
Let us prove that F (r) is a continuous function of r. Indeed,
F (r +δ) −F (r) = 2
∫
Rr,r+δ
fdm
where Rr,r+δ = {r2 ≤ x2 +y2 < (r +δ)2} is the ring with the inner radius r and
the outer radius r +δ. By the triangle inequality
|F (r +δ) −F (r)| ≤ 2
∫
Rr,r+δ
|f |dm
We know that µ(E) =
∫
E |f |dm is a measure in R2, and it is a ﬁnite measure
because µ(R2) =
∫
R2 |f |dm< ∞. Hence by the continuity we have
lim
δ→0
∫
Rr,r+δ
|f |dm =
∫
Rr,r
|f |dm = 0,
becauseRr,r = {x2 +y2 =r2} is a circle (a “ring” with zero width) whose Lebesgue
measure is zero. Next, similarly to the previous problems,
F (0) = −
∫
R2
fdm and lim
r→∞
F (r) =
∫
R2
fdm = −F (0).
19

If F (0) ⁄= 0, the existence of r such that F (r) = 0 follows from the intermediate
value theorem, and we can choose E = Dr. If F (0) = 0, we can choose E to be
any null set (or make R2 \E a null set).
Note: in the case
∫
R2fdm = 0 we can choose a more “interesting” set E so
thatm(E)> 0 and m(Ec)> 0. To this end we need to apply the above argument
to f + and f − separately.
6 Limits of integrals of speciﬁc functions
Preliminary Note. In many problems one has to use the following upper bound:
(
1 + x
n
)n
≤ex (1)
which holds for all
n ≥ 1 and x> −n (2)
This bound needs to be proved! You cannot just refer to Calculus or Advanced
Calculus where this fact may have been mentioned.
To prove it, take logarithm of both sides in (1) and convert it to
lnx +n
n ≤ x
n = x +n
n − 1
Since t = x+n
n > 0 due to (2), the last inequality can be written as
lnt ≤t − 1 ∀t> 0 (3)
which is a standard fact which I believe can be used.
With a little more eﬀort we can show that the sequence
an =
(
1 + x
n
)n
is monotonically increasing in n for all n satisfying (2). To prove this, treat n as
a continuous variable and take the derivative:
dan
dn =an
[
ln
(
1 + x
n
)
− x
x +n
]
Since an > 0, we have dan
dn ≥ 0 if and only if
lnx +n
n ≥ x
x +n
or equivalently
ln n
x +n ≤ − x
x +n = n
x +n − 1
20

Since t = n
x+n due to (2), we again reduce our inequality to the standard fact (3).
JPE, May 2012. Find
lim
n→∞
∫
[0,n]
(
1 + x
n
)n
e−πxdx
First, we can replace the above limit with
lim
n→∞
∫
[0,∞)
(
1 + x
n
)n
e−πxχ[0,n]dx
Due to Preliminary Note,
(
1 + x
n
)n
is a monotonically increasing sequence con-
verging to ex. Thus the integrand monotonically converges to ex−πx. Then we can
apply the Lebesgue Monotone Convergence Theorem and get
lim
n→∞
∫
[0,n]
(
1 + x
n
)n
e−πxdx =
∫
[0,∞)
e−(π−1)xdx = 1
π − 1.
JPE, May 2011. Find limn→∞
∫ ∞
0 fndm, where
fn(x) = 1
1 +x
√n
ln(n+2011)
, x ≥ 0.
JPE, May 2006. Find
lim
n→∞
∫ ∞
0
1
1 +x
n
ln n+2006
dx.
The above two problems are almost identical, we only solve the ﬁrst one.
Note that
lim
n→∞
√n
lnn + 2011 = ∞,
hence we have pointwise convergence fn(x) →f (x), where
f (x) =



1 for 0 <x< 1
1
2 for x = 1
0 for x> 1
Also we have fn(x) ≤ 1 for all 0 <x ≤ 1 and n ≥ 1. Next,
√n
lnn + 2011 ≥ 2
for all n ≥n0 for some n0 ≥ 1, hence
fn(x) ≤ 1
1 +x2
21

for all x> 1 and n ≥n0. Thus we have a dominating integrable function:
fn(x) ≤g(x) =
{ 1 for 0 <x ≤ 1
1
1+x2 for x> 1
Thus by the Lebesgue Dominated Convergence, we have
∫ ∞
0
fndm →
∫ ∞
0
fdm = 1.
JPE, Sept 2010. Find
lim
k→∞
∫ ∞
0
dx
(
1 + x
k
)k k√x
.
We have, for all, x> 0
lim
k→∞
1
(
1 + x
k
)k k√x
= 1
ex · 1 =e−x
pointwise. Due to Preliminary Note,
(
1 + x
k
)k
is a monotonically increasing se-
quence (converging to ex). Thus for all k ≥ 2 the integrand is bounded by
1
(
1 + x
k
)k k√x
≤ 1(
1 + x
2
)2
which is an integrable function (it is in L1(0, ∞)). Thus by Lebesgue Dominated
Convergence our integrals converge to
∫ ∞
0 e−xdx = 1.
JPE, May 2010 and May 1990. Is the following true or false?
lim
n→∞
∫ 1
0
ex2/ndx =
∫ 1
0
lim
n→∞
ex2/ndx.
True. The integrand converges pointwise to f (x) ≡ 1, and is bounded by
g(x) = ex2
, which is a bounded, hence integrable function on (0 , 1). Thus Lebesgue
Dominated Convergence applies.
JPE, Sept 2009 and May 2008. Find
lim
n→∞
∫ π/2
0
√
n sin x
ndx.
You can use the fact 0 ≤ sinθ ≤θ for θ ∈ [0,π/ 2].
The pointwise limit of the integrand is √x, which is also its upper bound.
Hence by Lebesgue Dominated Convergence the limit is
∫π/2
0
√xdx = 2
3 (π
2 )3/2.
22

JPE, May 2007. Find
lim
n→∞
∫
[0,n]
( sinx
x
)n
dm.
You can use the fact that | sinx|<x for all x> 0.
JPE, Sept 2006. Find
lim
n→∞
∫ ∞
0
( sinx
x
)n
dx.
For all x> 0 we have
⏐⏐⏐ sinx
x
⏐⏐⏐< 1 hence
( sinx
x
)n
− − − →
n→∞
0 pointwise .
Next we ﬁnd a good upper bound. First, the integrand is bounded by g1(x) = 1.
Second, for all n ≥ 2 the integrand is bounded by g2(x) = 1/x2. Thus we have
⏐⏐⏐
( sinx
x
)n⏐⏐⏐ ≤ min{g1(x),g 2(x)} = min{1, 1/x2}
and this upper bound is integrable (it belongs to L1(0, ∞)). Thus the Lebesgue
Dominated Convergence applies. Therefore the above limit is zero.
JPE, Sept 2005. Find the limit and justify your answer
lim
n→∞
∫ ∞
1
ln(nx)
x +x2 lnndx.
The integrand converges to f (x) = 1
x2 pointwise. Its upper bound is
lnn + lnx
x +x2 lnn ≤ 1
x2 + lnx
x2 ,
which is an integrable function (it is in L1(1, ∞)). Thus the Lebesgue Dominated
Convergence applies and gives the limit
∫ ∞
1
1
x2dx = 1.
JPE, May 2005. Find the limit and justify your answer
lim
n→∞
∫ ∞
0
sin(nx)
1 +x2 dx.
This problem is unusual, because the limit of the integral here is NOT equal
to the integral of the pointwise limit function. In fact, the pointwise limit of the
23

integrand does not even exist. We need to integrate by parts ﬁrst:
∫ ∞
0
sin(nx)
1 +x2 dx = − 1
n
∫ ∞
0
d cos(nx)
1 +x2 dx
= − 1
n
cos(nx)
1 +x2
⏐⏐⏐⏐
∞
0
− 1
n
∫ ∞
0
2x cos(nx)
(1 +x2)2 dx
= 1
n − 1
n
∫ ∞
0
2x cos(nx)
(1 +x2)2 dx.
For the last integral we have
⏐⏐⏐⏐
∫ ∞
0
2x cos(nx)
(1 +x2)2 dx
⏐⏐⏐⏐ ≤
∫ ∞
0
|2x cos(nx)|
(1 +x2)2 dx ≤
∫ ∞
0
2xdx
(1 +x2)2 = 1,
Hence our original integral converges to zero.
JPE, May 2003 and Sept 1999 LetE = [0, ∞). Prove that lim n→∞
∫
E
x
1+xndx
exists and ﬁnd its value.
We have limn→∞
x
1+xn =f (x) pointwise, where f (x) = x forx ∈ [0, 1),f (x) = 0
for x ∈ (1, ∞), and f (1) = 0 .5. For all n ≥ 3 our integrand is bounded by the
function g such that g(x) = x for x ∈ [0, 1] and g(x) = x
1+x3 for x ∈ (1, ∞). We
can easily see that g ∈L1(E), thus Lebesgue Dominated Convergence applies, and
our integral converges to
∫
Efdm = 0.5.
JPE, Sept 2002 and May 1994. Find the limit and justify your steps
lim
n→∞
∫ 1
0
(nx)2
(1 +x2)ndx.
This problem is unusual, because the limit of the integral here is NOT equal
to the integral of the pointwise limit function. In fact, the integrand converges to
zero pointwise while the integral converges to inﬁnity.
A quick inspection shows that the integrand takes high values for x ∼ 1/√n.
So let us estimate the integral from below by
∫ 1
0
(nx)2
(1 +x2)ndx ≥
∫ 1/√n
0
(nx)2
(1 +x2)ndx
Now for all x ∈ [0, 1√n] we have
(nx)2
(1 +x2)n ≥ (nx)2
(1 + 1/n)n ≥ (nx)2
e
because (1 + 1/n)n ≤e. Therefore
∫ 1
0
(nx)2
(1 +x2)ndx ≥ 1
e
∫ 1/√n
0
(nx)2dx =
√n
3e → ∞.
24

(a) JPE, Sept 2001. Compute
lim
k→∞
∫ k
0
(
1 − x
k
)k
ex/3dx.
(b) JPE, May 2000. Compute
lim
k→∞
∫ k
0
(
1 − x
k
)k
ex/2dx.
(a) Due to Preliminary Note,
(
1 − x
n
)n
is a monotonically increasing sequence con-
verging toe−x. Thus the integrand monotonically converges to f (x) = e−2x/3 point-
wise. By Lebesgue Monotone Convergence, our integral converges to
∫ ∞
0 fdx = 3
2 .
(b) The solution is almost identical to Part (a). The answer is 2.
JPE, May 2001 and May 1991. Compute
lim
n→∞
∫ 1
0
nxn−1
2 +x dx.
(in JPE, May 1991 , the value of the limit (= 1
3 ) was given.)
This problem is unusual, because the limit of the integral here is NOT equal
to the integral of the pointwise limit function. In fact, the integrand converges to
zero pointwise while the integral converges to a positive number.
We can integrate by parts ﬁrst:
∫ 1
0
nxn−1
2 +x dx =
∫ 1
0
dxn
2 +x = xn
2 +x
⏐⏐⏐⏐
1
0
+
∫ 1
0
xn
(2 +x)2dx
The ﬁrst term on the right hand side is 1
3 . The last integral converges to zero,
because the integrand converges to zero pointwise for all x ∈ [0, 1) and is bounded
by an integrable function (in fact, it is bounded by a constant function: xn
(2+x)2 ≤ 1
4 ).
Alternatively, we can change variable y =xn, which gives us
lim
n→∞
∫ 1
0
dy
2 +y1/n.
Now the integrand is bounded by 1
2 and its pointwise limit is 1
3 , so the integral
converges to 1
3 .
JPE, Sept 1999. Find the limit
lim
n→∞
∫
[0,1]
cos(xn)dx.
25

For all x ∈ [0, 1) we have
xn → 0 ⇒ cos(xn) → cos 0 = 1,
and for x = 1 we have cos( xn) = cos 1. Note that | cos(xn)| ≤ 1, hence the
Lebesgue Dominated Convergence applies and gives
lim
n→∞
∫
[0,1]
cos(xn)dm =
∫
[0,1]
1dm = 1.
JPE, Sept 1998 and Sept 1993. Find the limit
lim
n→∞
∫ ∞
1
ln(1 +nx)
1 +x2 lnndx.
Note that
x ≥ 1, n ≥ 1 ⇒ nx< 1 +nx ≤ 2nx,
hence
lnn + lnx
1 +x2 lnn ≤ ln(1 +nx)
1 +x2 lnn ≤ lnn + lnx + ln 2
1 +x2 lnn .
By the squeeze theorem, for each x ≥ 1
lim
n→∞
ln(1 +nx)
1 +x2 lnn = 1
x2.
We also have the following upper bound:
ln(1 +nx)
1 +x2 lnn ≤ 1
x2 + lnx
x2 + ln 2
x2
which is an integrable function on (1 , ∞). Thus the Lebesgue Dominated Conver-
gence applies and gives
lim
n→∞
∫ ∞
1
ln(1 +nx)
1 +x2 lnndx =
∫ ∞
1
1
x2dx = 1.
JPE, May 1998 and Sept 1995. Find the limit
lim
n→∞
∫ ∞
0
n sin(x/n)
x(1 +x2) dx.
We have
lim
n→∞
sin(x/n)
(x/n) = 1 ⇒ lim
n→∞
n sin(x/n)
x(1 +x2) = 1
1 +x2
26

for all x> 0, pointwise. Also note that sin θ ≤θ for all θ ≥ 0, thus
n sin(x/n)
x(1 +x2) ≤ 1
1 +x2,
which is an integrable function on (0 , ∞). Thus the Lebesgue Dominated Conver-
gence applies and gives
lim
n→∞
∫ ∞
0
n sin(x/n)
x(1 +x2) dx. =
∫ ∞
0
1
1 +x2dx = tan −1x
⏐⏐⏐
∞
0
=π/2.
JPE, Sept 1997. Show that the hyperelliptic integral
∫ ∞
2
xdx√
(x2 −ε2)(x2 − 1)(x − 2)
converges to the elliptic integral
∫ ∞
2
dx√
(x2 − 1)(x − 2)
as ε tends to zero.
For each x> 2, we have pointwise convergence, as ε → 0,
x√
(x2 −ε2)(x2 − 1)(x − 2)
→ x√
x2(x2 − 1)(x − 2)
= 1√
(x2 − 1)(x − 2)
.
An upper bound for the integrand is
x√
(x2 −ε2)(x2 − 1)(x − 2)
≤ x√
(x2 − 1)(x2 − 1)(x − 2)
= x
(x2 − 1)
√
(x − 2)
.
This is an integrable function on (2, ∞). Indeed, its tail, as x → ∞, has asymptotic
∼x−3/2, which is integrable. It grows to inﬁnity near x = 2 at rate ∼ O (1/√x − 2),
which is also integrable. Thus the Lebesgue Dominated Convergence applies and
gives the result.
JPE, May 1994. Show that
lim
n→∞
∞∑
m=1
(−1)mn
n +nm2 + 1 =
∞∑
m=1
(−1)m
m2 + 1
Let X = N and µ be the counting measure. Then the above claim may be
stated in terms of Lebesgue integrals:
lim
n→∞
∫
X
(−1)xn
n +nx2 + 1dµ =
∫
X
(−1)x
x2 + 1dµ.
27

We have pointwise convergence
(−1)xn
n +nx2 + 1 → (−1)x
x2 + 1 as n → ∞.
And for all n ≥ 1 our integrand has an upper bound
⏐⏐⏐ (−1)xn
n +nx2 + 1
⏐⏐⏐ ≤ 1
x2 + 1,
which is an integrable function onX, because ∑∞
m=1
1
m2+1 < ∞. Thus the Lebesgue
Dominated Convergence applies and gives the result.
JPE, May 1993. Evaluate
lim
n→∞
∫ ∞
−∞
e−x2/n
1 +x2dx
For every x ∈ R the sequence {e−x2/n} monotonically increases and converges
to e0 = 1. Thus by the Lebesgue Monotone Convergence
lim
n→∞
∫ ∞
−∞
e−x2/n
1 +x2dx =
∫ ∞
−∞
dx
1 +x2 = tan −1x
⏐⏐⏐
∞
−∞
=π.
JPE, Oct 1991. (1) Prove that f (t) = t
1+t2 is a bounded function on ( −∞, ∞).
(2) Let
fn(x) = nx
1 +n2x2 (x ∈ [0, 1], n = 1, 2,... )
Then prove that fn(x) does not converge uniformly on [0 , 1].
(3) Find lim n→∞
∫ 1
0 fn(x)dx, if it exists.
(1) This a calculus exercise. Let us just denote the bound by C = max t
1+t2 .
(2) For x = 1/n we have fn(x) = 1/2, thus there is no uniform convergence.
(3) We have pointwise convergence fn(x) → 0 for all x ∈ [0, 1] and a common
upper bound fn(x) ≤C. Thus Lebesgue Dominated Convergence applies.
JPE, Oct 1991. Let
fn =nαχ[ 1
n+1, 1
n ]
where α is a constant, 1 ≤α< 2.
(i) Is there an integrable function Φ on [0 , 1] such that 0 ≤fn(x) ≤ Φ(x) for all n
and x ∈ [0, 1]?
(ii) Find lim n→∞
∫
[0,1]fndm, if it exists.
28

(i) No. Even if we set
Φ(x) = sup
n
fn(x) =
∞∑
n=1
nαχ[ 1
n+1, 1
n ]
then ∫
[0,1]
Φdm =
∞∑
n=1
nα⏐⏐[ 1
n+1, 1
n]
⏐⏐ =
∞∑
n=1
nα−1
n + 1 ≥
∞∑
n=1
1
n + 1 = ∞.
(ii) The limit is zero: ∫
[0,1]
fndm = nα−1
n + 1 → 0.
JPE, Oct 1991. (i) Let f be a step function on a bounded interval [ a,b ]. Then
prove that
(∗) lim
n→∞
∫ b
a
f (x) sin(nx)dx.
(ii) Let f be a bounded measurable function on [ a,b ]. Then prove (*).
(iii) Let f be an integrable function on ( −∞, ∞). Then prove (*).
This problem is almost a research project... We only sketch the solution. First,
let f (x) = αχ(c,d) be a constant function on an interval ( c,d ). Then
∫ d
c
f (x) sin(nx)dx = −α
n cos(nx)
⏐⏐⏐
d
c
= −α
n (cos(nd) − cos(nc)),
hence ⏐⏐⏐⏐
∫ d
c
f (x) sin(nx)dx
⏐⏐⏐⏐ ≤ 2|α|
n → 0.
Next, if f is a step function, then f = ∑N
i=1αiχ(ci,di), and the result follows by
additivity.
(ii) If f is a bounded measurable function on [ a,b ], then f ∈ L1([a,b ]). We can
approximatef by step functions (in the L1 norm) and apply Part (i).
(iii) The same strategy: approximate f by step functions (in the L1 norm) and
apply Part (i).
JPE, May 1991. Let
fn(x) = n1/4e−x2n
1 +x2 .
(a) Prove that fn ∈L1(0, ∞).
(b) Find lim n→∞
∫
(0,∞)fndm.
29

(a) Since e−x2n ≤ 1, we have
∫
(0,∞)
fndm ≤
∫
(0,∞)
n1/4
1 +x2dm =n1/4 tan−1x
⏐⏐⏐
∞
0
=n1/4π/2,
hence fn ∈L1(0, ∞).
(b) We will need a common upper bound for all fn’s. To this end we combine n1/4
with e−x2n as follows. The function g(t) = te−t4
is bounded on (0 , ∞). Indeed,
by a standard Calculus-I argument its maximum is achieved at t = 1/
√
2 and its
maximum value is C = 1√
2e−1/4. Therefore
x1/2n1/4e−x2n ≤C ⇒ n1/4e−x2n ≤C/√x.
So we have ∫
(0,∞)
fndm ≤
∫
(0,∞)
C/√x
1 +x2dm< ∞.
The last integral is ﬁnite, because the integrand has tail O(x−5/2), asx → ∞, which
is integrable. And it grows to inﬁnity near x = 0 at a rate ∼ O (1/√x), which
is also integrable. Thus fn ∈ L1(0, ∞) and fn are bounded by one integrable
function. It is easy to see that lim n→∞fn(x) = 0 for each x > 0, thus by the
Lebesgue Dominated Convergence
lim
n→∞
∫
(0,∞)
fndm =
∫
(0,∞)
0dm = 0.
JPE, May 1990. Let
fn(x) = √nxe−nx3
.
(i) Find the maximum value assumed by fn in the interval [0, 1].
(ii) Find lim n→∞
∫
[0,1]fndm.
(i) This is a Calculus-I problem, never mind. And we do not need it for Part (ii).
(ii) We need a common upper bound on all fn’s. Just like in the previous problem,
the function g(t) = te−t2
is bounded on (0 , ∞). Indeed, by a standard Calculus-
I argument its maximum is achieved at t = 1 /
√
2 and its maximum value is
C = 1√
2e−1/2. Therefore
n1/2x3/2e−nx3
≤C ⇒ √nxe−nx3
≤C/√x.
So we have ∫
[0,1]
fndm ≤
∫
[0,1]
C√xdm = 2C.
It is easy to see that lim n→∞fn(x) = 0 for each x > 0, thus by the Lebesgue
Dominated Convergence
lim
n→∞
∫
[0,1]
fndm =
∫
[0,1]
0dm = 0.
30

7 Series of non-negative functions
JPE, Sept 2010. For all n ∈ N and k ∈ N let fn,k be a non-negative and
measurable on R and assume that
∫
Rfn,kdm ≤ 1
n2 . Show that
f : =
∞∑
n=1
lim inf
k→∞
fn,k ∈L1(R).
Here the series and lim inf are deﬁned pointwise.
Since the integrands are non-negative functions, the summation and integration
“commute”. Next we use Fatou’s Lemma:
∫
R
fdm =
∞∑
n=1
∫
R
lim inf
k→∞
fn,kdm
≤
∞∑
n=1
lim inf
k→∞
∫
R
fn,kdm
≤
∞∑
n=1
1
n2 < ∞,
thusf ∈L1(R).
JPE, Sept 2008 and Sept 2007. Let fn, n = 1 , 2,..., be a sequence of
non-negative continuous functions on R such that
∫
Rfndm < 1
n3 . Let f (x) =∑∞
n=1fn(x). Prove that f (x) is integrable on R.
For non-negative functions, the summation and integration “commute”, hence
∫
R
fdm =
∞∑
n=1
∫
R
fndm<
∞∑
n=1
1
n3 < ∞.
Note: the continuity of fn’s is not necessary, it is enough to assume their measur-
ability. The bound 1
n3 can be relaxed to 1
n2 or 1
n1+a for any a> 0.
JPE, May 2006. Let fn, n = 1, 2,..., be a sequence of non-negative Lebesgue
measurable functions on R such that
∫
fndm< 1
2n . Let f (x) = ∑∞
n=1fn(x). Show
that f ∈L1(0, ∞).
For non-negative functions, the summation and integration “commute”, hence
∫
(0,∞)
fdm =
∞∑
n=1
∫
(0,∞)
fndm<
∞∑
n=1
1
2n < ∞.
Note: strangely, the domain of integration is not speciﬁed in the ﬁrst formula of
the problem. One may naturally assume that it is R. But then it is not clear why
31

they ask for f ∈L1(0, ∞), instead of f ∈L1(R).
JPE, Sept 1997. Evaluate
∞∑
n=0
∫ ∞
1/2
(1 −e−t)ne−t2
dt.
Since the integrands are non-negative functions, the summation and integration
“commute”, hence
∞∑
n=0
∫ ∞
1/2
(1 −e−t)ne−t2
dt =
∫ ∞
1/2
∞∑
n=0
(1 −e−t)ne−t2
dt
=
∫ ∞
1/2
e−t2
∞∑
n=0
(1 −e−t)ndt
=
∫ ∞
1/2
e−t2 1
1 − (1 −e−t)dt
=
∫ ∞
1/2
et−t2
dt
The last integral is computed by “completing the square” and changing variable:
∫ ∞
1/2
et−t2
dt =e1/4
∫ ∞
1/2
e−(t−1/2)2
dt =e1/4
∫ ∞
0
e−s2
ds =e1/4√π/2.
Note: apparently it is assumed here that the students know the value of the inte-
gral
∫ ∞
0 e−s2
ds, or can quickly compute it.
JPE, Sept 1995 and Oct 1991. Evaluate
∞∑
n=0
∫ π/2
0
(1 −
√
sinx)n cosxdx.
Since the integrands are non-negative functions, the summation and integration
32

“commute”, hence
∞∑
n=0
∫ π/2
0
(1 −
√
sinx)n cosxdx =
∫ π/2
0
∞∑
n=0
(1 −
√
sinx)n cosxdx
=
∫ π/2
0
cosx
∞∑
n=0
(1 −
√
sinx)ndx
=
∫ π/2
0
cosx 1
1 − (1 −
√
sinx)
dx
=
∫ π/2
0
cosx√
sinx
dx
The last integral is rather elementary:
∫ π/2
0
cosx√
sinx
dx =
∫ π/2
0
d sinx√
sinx
= 2
√
sinx
⏐⏐⏐
π/2
0
= 2.
8 Riemann integral vs Lebesgue integral
JPE, Sept 2011. Is it true that the characteristic function of the Cantor set is
Lebesgue integrable in [0 , 1] but not Riemann integrable?
False. The characteristic function of the Cantor set is continuous on the com-
plement to the Cantor set (that complement consists of open intervals on which
the function is identically zero). Thus the set of discontinuity points is exactly the
Cantor set, which measure zero. This implies Riemann integrability.
JPE, Sept 2004. Let f : [0, 1] → R be deﬁned by
f (x) =
{ √x if x is irrational
0 otherwise
(i) Show that f is measurable.
(ii) Is f Lebesgue integrable? If yes, ﬁnd its Lebesgue integral.
(iii) Is f Riemann integrable? If yes, ﬁnd its Riemann integral.
(i) just like in some homework exercises.
(ii) yes, because f is measurable and bounded. Changing f on a set of measure
zero will not aﬀect its Lebesgue integral, so we can replace f with g(x) = √x for
all x ∈ [0, 1]. Now
∫
[0,1]
fdm =
∫
[0,1]
gdm =
∫ 1
0
√xdx = 2
3.
33

(iii) no, because f is discontinuous at every x >0, hence the set of the disconti-
nuity points has positive Lebesgue measure.
JPE, Sept 2001. Let f : [0, 1] → R be deﬁned by
f (x) =
{ √x if x is rational
0 otherwise
(i) Show that f is measurable.
(ii) Prove or disprove that f is of bounded variation on [0 , 1].
(iii) Is f Lebesgue integrable but not Riemann integrable?
(i) just like in some homework exercises.
(ii) see some other section...
(iii) yes. It is Lebesgue integrable because it is measurable and bounded. It is not
Riemann integrable because f is discontinuous at every x> 0, hence the set of the
discontinuity points has positive Lebesgue measure.
9 Lp spaces: general
JPE, May 2012. Let p ∈ [1, ∞). Suppose that fn ∈ Lp([0, 1]) converges a.e. to
f ∈Lp([0, 1]). Show that fn converges tof inLp([0, 1]) if and only if ‖fn‖p → ‖f ‖p.
Note: this is the most popular JPE problem. Its variants were given in the
following exams: JPE, May 2005, Sept 1998, and Jan 1989 (for p = 2),
and JPE, May 2003, Sept 2002, Sept 2001, Sept 1999, May 1995, Sept
1994, and Sept 1993 (forp = 1). Sometimes [0 , 1] is replaced with R or with an
unspeciﬁed measurable subset E ⊂ R. See also a clever “extended” version of this
problem given in JPE, May 1994, in this section.
The “only if” part is simple: just use the triangle inequality
‖fn −f ‖p ≥
⏐⏐‖fn‖p − ‖f ‖p
⏐⏐,
hence ‖fn −f ‖p → 0 implies ‖fn‖p → ‖f ‖p.
We now turn to the diﬃcult “if” part. Consider ﬁrst the simpler case p = 1.
There is a relatively fast solution that goes as follows. By the triangle inequality
⏐⏐|fn| − |fn −f |
⏐⏐ ≤ |f |.
Since f ∈L1([0, 1]), the Lebesgue Dominated Convergence gives
∫
|fn| −
∫
|fn −f | =
∫ (
|fn| − |fn −f |
)
− − − →
n→∞
∫
|f |
34

therefore
∫
|fn −f | → 0, i.e., fn →f in L1. However, this solution does not seem
to generalize to the p> 1 case. Hence we present another solution below.
By the triangle inequality |fn −f | ≤ |fn| + |f |, hence
|fn| + |f | − |fn −f | ≥ 0.
Now by Fatou’s Lemma (as in the proof of Lebesgue Dominated Convergence)
2
∫
|f | =
∫
lim inf(|fn| + |f | − |fn −f |)
≤ lim inf
∫
(|fn| + |f | − |fn −f |)
= lim inf
∫
|fn| +
∫
|f | −
∫
|fn −f |
= 2
∫
|f | − lim sup
∫
|fn −f |.
Therefore lim sup
∫
|fn −f | ≤ 0, which implies
∫
|fn −f | → 0, i.e., fn →f in L1.
In the case p> 1 we use the convexity of the function ϕ(x) = |x|p on the entire
real line −∞<x< ∞ and Jensen’s inequality to get
⏐⏐⏐fn −f
2
⏐⏐⏐
p
=
⏐⏐⏐fn + (−f )
2
⏐⏐⏐
p
≤ |fn|p + | −f |p
2 = |fn|p + |f |p
2
hence
2p−1|fn|p + 2p−1|f |p − |fn −f |p ≥ 0;
after that the previous solution for p = 1 is repeated almost verbatim.
JPE, May 2012 and Sept 2004. Are the following true of false?
(a) If f ∈Lp([0, 1]) for all p ∈ (1, ∞), then f ∈L∞([0, 1]).
(b) If 1 ≤p<q < ∞, then Lq([1, ∞)) ⊂Lp([1, ∞)).
(a) False. Counterexample: f = lnx.
(b) False. Counterexample: f =x−r for any 1
q <r < 1
p.
JPE, Sept 2010 and Sept 1988. Is the following true of false?
Suppose fn ∈L1(0, 1) for all n ∈ N, that fn(x) →g(x) for almost every x ∈ [0, 1]
and that fn →f in L1(0, 1). Then f (x) = g(x) for almost every x ∈ [0, 1].
True. By a corollary proved in class: If fn → f in the Lp norm (p ∈ [1, ∞)),
then there is a subsequence {fnk} such that fnk →f a.e. So the subsequence fnk
converges a.e. to f and to g. This implies f =g a.e.
JPE, Sept 2009. Is the following true of false?
If {fk} ∈ Lp(Rn) ∩Lr(Rn) for some p,r ∈ [1, ∞),fk →g inLp(Rn) and fk →h in
Lr(Rn). Then g(x) = h(x) a.e. in Rn.
35

True. By a corollary proved in class: If fk → g in the Lp norm (p ∈ [1, ∞)),
then there is a subsequence {fkm} such that fkm →g a.e. Now that subsequence
converges to h in the Lr norm, so by the same corollary there is a subsubsequence
{fkms } such that fkms → h a.e. Hence the same sequence of functions, {fkms },
converges to both g and h a.e. This implies g =h a.e.
JPE, Sept 2010. Let fn ∈L1(0, 1) ∩L2(0, 1) for all n ∈ N. Prove or disprove:
(a) If ‖fn‖1 → 0, then ‖fn‖2 → 0.
(b) If ‖fn‖2 → 0, then ‖fn‖1 → 0.
(a) False. Example: fn =nχ[0,n−2]. Here ‖f ‖1 = 1
n → 0, but ‖fn‖2 = 1 ( ∀n ∈ N).
(b) True. By the Schwarz inequality,
‖fn‖1 =
∫
|fn| · 1 ≤
[∫
|fn|2
]1/2[∫
12
]1/2
= ‖fn‖2
hence ‖fn‖2 → 0 implies ‖fn‖1 → 0.
JPE, Sept 2010. Letf be a positive measurable function deﬁned on a measurable
set E with m(E)< ∞. Prove that
(∫
E
fdm
)(∫
E
1
f dm
)
≥m2(E).
By the Schwarz inequality,
m(E) =
∫
E
1dm =
∫
E
√
f · 1√f dm ≤
(∫
E
fdm
)1/2(∫
E
1
f dm
)1/2
.
JPE, May 2010 and May 2004. (a) Let f be measurable on [0 , 1]. For
1 ≤p< ∞ deﬁne
g(p) =
(∫ 1
0
|f (x)|pdx
)1/p
.
Show that g is non-decreasing on [1 , ∞).
(b) Assume in addition that f /∈L∞(0, 1). Show that lim p→∞g(p) = ∞.
(a) Let p<q . By the H¨ older inequality
∫ 1
0
|f (x)|p · 1dx ≤
(∫ 1
0
[
|f (x)|p]q/pdx
)p/q(∫ 1
0
1q′
dx
)1/q′
=
(∫ 1
0
|f (x)|qdx
)p/q
.
36

whereq′ =q/(q −p) is just the exponent conjugate to q/p. Now raising both sides
to the power 1 /p proves that g(p) ≤g(q).
(b) For any A> 0 we have mA : = m{x : |f (x)|>A }> 0, hence
g(p) ≥
(∫
{x : |f (x)|>A}
|f (x)|pdx
)1/p
≥ [ApmA]1/p =Am1/p
A .
Taking the limit p → ∞ gives lim infp→∞g(p) ≥A. Since A is arbitrary, we have
limp→∞g(p) = ∞.
JPE, May 2009. Let (X, M,µ ) be a measure space with a positive, ﬁnite measure
µ. Consider a function f ∈L∞(µ) such that ‖f ‖∞ > 0.
(a) Show that, for every positive ε, the set {x : |f (x)| > ‖f ‖∞ −ε} has positive
measure.
(b) Show that
lim
n→∞
‖f ‖n = lim
n→∞
‖f ‖n+1
n+1
‖f ‖n
n
= ‖f ‖∞.
(The convergence ‖f ‖n → ‖f ‖∞ was also given, as a separate problem, in JPE,
May 1998, Sept 1995, May 1994, and May 1990. )
(a) Trivial. Let us just denote mε : = {x : |f (x)|> ‖f ‖∞ −ε}> 0.
(b) First,
‖f ‖n ≤
[
‖f ‖n
∞µ(X)
]1/n
= ‖f ‖∞µ(X)1/n.
Taking the limit n → ∞ gives lim sup ‖f ‖n ≤ ‖f ‖∞. On the other hand, for any
ε> 0 we have
‖f ‖n ≥
[
(‖f ‖∞ −ε)nmε
]1/n
= (‖f ‖∞ −ε)m1/n
ε .
Taking the limit n → ∞ gives lim inf ‖f ‖n ≥ ‖f ‖∞ −ε. Since ε >0 is arbitrary,
we have lim inf ‖f ‖n ≥ ‖f ‖∞. Thus lim ‖f ‖n = ‖f ‖∞.
Next, we have
‖f ‖n+1
n+1 =
∫
X
|f |n+1dµ ≤
∫
X
‖f ‖∞|f |ndµ ≤ ‖f ‖∞‖f ‖n
n,
thus
lim sup ‖f ‖n+1
n+1
‖f ‖n
n
≤ ‖f ‖∞.
On the other hand, by the H¨ older inequality
‖f ‖n
n =
∫
X
|f |n · 1dµ ≤
[∫
X
|f |n+1dµ
] n
n+1
·
[∫
X
1n+1dµ
] 1
n+1
= ‖f ‖n
n+1µ(X)
1
n+1
37

hence
‖f ‖n+1
n+1
‖f ‖n
n
≥ ‖f ‖n+1
µ(X)
1
n+1
and taking the limit n → ∞ gives
lim inf ‖f ‖n+1
n+1
‖f ‖n
n
≥ lim ‖f ‖n+1
µ(X)
1
n+1
= ‖f ‖∞
(because ‖f ‖n+1 → ‖f ‖∞ and µ(X)
1
n+1 → 1). Thus lim
‖f ‖n+1
n+1
‖f ‖nn
= ‖f ‖∞.
JPE, May 2001. Show by example that there exist two functions f ∈L1(R) and
g ∈L2(R) such that f +g is neither in L1(R) nor in L2(R).
Here: f =χ(0,1)/√x and g =χ(1,∞)/x.
JPE, May 2000. Find a function f ∈L1(R) which does not belong to any Lp(R)
with p> 1.
Here: f =χ(0,1)/(x ln2x).
JPE, Sept 1997. (i) Prove that convergence inL1 implies convergence in measure.
(ii) Is the converse true?
(i) By way of contradiction, if fn converges to f in L1 but not in measure, then
∃ε> 0 such that for all N ≥ 1 there is n>N such that
µ{x : |fn(x) −f (x)|>ε }>ε.
In that case
∫
X
|fn −f |dµ ≥εµ{x : |fn(x) −f (x)|>ε } ≥ ε2 > 0,
thusfn cannot converge to f in L1, a contradiction.
(ii) The converse is false. Example: X = [0 , 1], µ is the Lebesgue measure,
and fn = nχ(0,1/n). Then fn → f ≡ 0 in measure, but not in L1, because∫
[0,1] |fn −f |dµ = 1 for all n.
JPE, May 1997. Find a function f on (0, ∞) such that f ∈Lp(0, ∞) if and only
if 1 <p< 2.
Here:
f (x) =
{ 1/√x if x ∈ (0, 1]
1/x if x ∈ (1, ∞)
38

JPE, May 1995. Suppose that fn → f in L1([0, 1]) and that h : R → R is a
continuous function. Prove or disprove: h ◦fn →h ◦f in L1([0, 1]).
This is false. Example: f ≡ 0, fn = √nχ [0, 1
n ], and h(x) = x2.
JPE, May 1995. Let M be a subspace of L2([0, 1]) with the following property:
there is a constant C so that if f ∈ M , then |f (x)| ≤ C‖f ‖2 for a.e. x ∈ [0, 1].
Let f1,...,f n be an orthonormal set in M.
(a) Show that ∑n
j=1 |fj(x)|2 ≤C 2 for a.e. x ∈ [0, 1].
(b) Show that the dimension of M is bounded above by C 2.
(a) An orthonormal set f1,...,f n satisﬁes
∫
[0,1]fifjdm = δij, which is the Kro-
necker delta symbol (the bar here means complex conjugate). Now let c1,...,c n
be any complex numbers. Then c1f1 + · · · +cnfn ∈ M, hence
|c1f1(x) + · · · +cnfn(x)| ≤ C‖c1f1 + · · · +cnfn‖2 =C
[
|c1|2 + · · · + |cn|2]1/2
for a.e. x ∈ M. Setting c1 =f1(x),...,c n =fn(x) and squaring gives
( n∑
j=1
|fj(x)|2
)2
≤C 2
n∑
j=1
|fj(x)|2,
which completes the proof of (a).
(b) Integrating the inequality in (a) gives n ≤ C 2, thus the cardinality of any
orthonormal set does not exceed C 2.
Comment: the subspace M cannot contain all functions with the given property
(i.e., there is a constant C so that |f (x)| ≤ C‖f ‖2 for a.e. x ∈ [0, 1]). For example,
let C = 10 and consider two functions: f = 1 + 9χ(0,ε) and g = −1 + 9χ(0,ε). Note
that ‖f ‖2 > 1 and ‖g‖2 > 1, and at the same time |f (x)| ≤ 10 and |g(x)| ≤ 10 for
all x ∈ [0, 1]; hence f and g have the above property. Now f +g = 18χ(0,ε), so we
have ‖f +g‖2 = 18 √ε and ess-sup( |f +g|) = 18, thus f +g does NOT have the
above property (provided ε is suﬃciently small).
JPE, May 1994. Let fn ∈ L1(R) for n = 1, 2,... and fn → f a.e. as n → ∞ .
Suppose ‖fn‖1 →A as n → ∞.
(a) Show that f is integrable on R and ‖f −fn‖1 →A − ‖f ‖1.
(b) Must ‖f ‖1 =A? Give a proof or a counterexample.
Note: this problem resembles the most popular JPE problem (see May 2012 in
this section), but it goes a little further: it allows the limit 1-norm of fn to exceed
that of f , so that some “mass” of fn “falls through cracks” and “does not reach” f .
(a) The convergence fn →f a.e. implies |fn| → |f | a.e., so by Fatou’s Lemma
∫
|f | =
∫
lim inf |fn| ≤ lim inf
∫
|fn| =A< ∞
39

therefore f ∈L1(R).
Next, by the triangle inequality
⏐⏐|fn| − |fn −f |
⏐⏐ ≤ |f |.
Since f ∈L1(R), the Lebesgue Dominated Convergence gives
∫
|fn| −
∫
|fn −f | =
∫ (
|fn| − |fn −f |
)
− − − →
n→∞
∫
|f |
therefore
‖fn −f ‖1 =
∫
|fn −f | → A − ‖f ‖1.
(b) Not necessarily true. Example: fn =nχ(0,1/n). We have fn →f ≡ 0 pointwise
and A = lim ‖fn‖1 = 1, but ‖f ‖1 = 0 ⁄= 1 = A.
JPE, Sept 1993. Prove or disprove the following statement:
If (X, M,µ ) is a measure space, ϕ is a convex function on ( a,b ) and f : X → (a,b )
is an integrable function, i.e. f ∈L1
µ(X), then
ϕ
(∫
X
fdµ
)
≤
∫
X
(ϕ ◦f )dµ.
This looks very much like Jensen’s inequality, but a crucial assumption is miss-
ing: µ(X) = 1. Without this assumption, the statement is false. Example: ϕ =x2,
X = [0, 10], µ the Lebesgue measure, and f ≡ 1. Then ϕ
(∫
Xfdµ
)
= 10 2 = 100
and
∫
X(ϕ ◦f )dµ = 10.
JPE, May 1993. Let f ∈L2(R). Prove that
lim
n→∞
∫ n+1
n
fdm = 0.
First, by the triangle inequality
⏐⏐⏐⏐
∫ n+1
n
fdm
⏐⏐⏐⏐ ≤
∫ n+1
n
|f |dm.
Now by the Schwarz inequality
∫ n+1
n
|f | · 1dm ≤
(∫ n+1
n
|f |2dm
)1/2(∫ n+1
n
12dm
)1/2
=
(∫ n+1
n
|f |2dm
)1/2
.
Next we show that the last integral converges to zero, asn → ∞. Indeed, recall that
µ(E) =
∫
E |f |2dm is a measure on R, and it is ﬁnite because µ(R) =
∫
R |f |2dm<
∞. Hence by the continuity
∫ n+1
n
|f |2dm =µ([n,n + 1]) ≤µ([n, ∞)) →µ(∩∞
n=1[n, ∞)) = µ(∅) = 0.
40

JPE, Oct 1991. Let f ≥ 0 be Lebesgue measurable on [0 , 1] and
∫
[0,1]
f 2dm =
∫
[0,1]
f 3dm =
∫
[0,1]
f 4dm< ∞
Show that f =f 2 a.e.
By the Schwarz inequality
∫
[0,1]
f ·f 2dm ≤
[∫
[0,1]
f 2dm
]1/2
·
[∫
[0,1]
f 4dm
]1/2
=
∫
[0,1]
f 2dm.
Thus we have an equality in the Schwarz inequality, which is only possible if the
two involved functions (in this case f andf 2) are proportional to each other. From
the relation af = bf 2 a.e. with some a,b ∈ R (at least one of which diﬀers from
zero) we can easily show that f =f 2 a.e.
Note that f =f 2 a.e. implies that f only takes two values, 0 and 1 (a.e.), hence
f =χA a.e. for a subset A ⊂ [0, 1].
JPE, Sept 1989. Let p> 1 and f ∈Lp(
[−1, 1]
)
, i.e.
∫
[−1,1]
|f |pdm< ∞.
(i) Prove that f ∈L1([−1, 1]).
(ii) Let In = (− 1
n, 1
n) and γ = p−1
p . Then prove
lim
n→∞
nγ
∫
In
|f |dm = 0.
(i) By the H¨ older inequality
∫
[−1,1]
|f | · 1dm ≤
[∫
[−1,1]
|f |pdm
]1/p[∫
[−1,1]
1qdm
]1/q
= 2 1/q‖f ‖p < ∞,
where q = p
p−1 is the exponent conjugate to p. Note that 1
q =γ.
(ii) Again by the H¨ older inequality
∫
In
|f | · 1dm ≤
[∫
In
|f |pdm
]1/p[∫
In
1qdm
]1/q
=
( 2
n
)γ[∫
In
|f |pdm
]1/p
.
Thus
nγ
∫
In
|f |dm ≤ 2γ
[∫
In
|f |pdm
]1/p
.
41

Next we show that the last integral converges to zero, as n → ∞ . Indeed, recall
that µ(E) =
∫
E |f |pdm is a measure on [ −1, 1], it is ﬁnite because µ([−1, 1]) =∫
[−1,1] |f |pdm< ∞, hence by the continuity
∫
In
|f |pdm =µ(In) →µ(∩∞
n=1In) = µ({0}) =
∫
{0}
|f |pdm = 0.
10 Lp spaces: estimation of speciﬁc integrals
JPE, May 2012. Let f ∈L∞([0, 1]) and ‖f ‖∞ ≤ 1.
(a) Show that ∫
[0,1]
√
1 −f 2dm ≤
√
1 −
(∫
[0,1]
fdm
)2
(b) Describe the class of functions for which the equality takes place.
(a) Denote g =
√
1 −f 2. Observe that f 2 +g2 = 1 a.e. Now by the Schwarz
inequality, applied twice,
[∫
f
]2
+
[∫
g
]2
≤
∫
f 2 +
∫
g2 =
∫
(f 2 +g2) =
∫
1 = 1.
(b) For strictly convex functions, equality in Jensen’s inequality occurs if and only
if the integrand is constant a.e., hence f must be constant a.e.
JPE, Sept 2011. Given that
∫ ∞
0 e−x sinxdx = 1
2 , prove that
∫ ∞
0
e−x√
3 + 2 sinxdx ≤ 2.
First of all, in the given formula
∫ ∞
0 e−x sinxdx = 1
2 the integral is a Riemann
integral. The corresponding Lebesgue integral
∫
(0,∞)e−x sinxdm has the same
value, because the function is absolutely integrable:
∫ ∞
0
⏐⏐e−x sinx
⏐⏐dx ≤
∫ ∞
0
e−xdx = 1.
Next we apply the Schwarz inequality to f =e−x/2 and g =e−x/2√3 + 2 sinx:
∫
(0,∞)
e−x√
3 + 2 sinxdm ≤
[∫
(0,∞)
e−xdm
]1/2[∫
(0,∞)
e−x(3 + 2 sinx)dm
]1/2
≤ 11/2 · (3 + 2 · 1
2 )1/2 = 2.
42

JPE, Sept 2009. (i) Show that
∫ ∞
1
3√1 +x
x2 dx ≤
3√
6.
(ii) Show that the strict inequality holds in (i).
(i) By the H¨ older inequality
∫ ∞
1
3√1 +x
x · 1
xdx ≤
[∫ ∞
1
1 +x
x3 dx
]1/3[∫ ∞
1
1
x3/2dx
]2/3
=
( 1
2 + 1
)1/3
· 22/3 =
3√
6.
(ii) The H¨ older inequality does not turn into an equality here, because the func-
tions 1+x
x3 and 1
x3/2 are obviously not proportional to one another.
JPE, Sept 2008. Find all functions g(x) ∈L3(0, 1) satisfying the equation
(∫
[0,1]
xg(x)dx
)3
= 4
25
∫
[0,1]
g3(x)dx.
By the H¨ older inequality
∫
[0,1]
xg(x)dx ≤
(∫
[0,1]
x3/2dx
)2/3(∫
[0,1]
g3(x)dx
)1/3
=
( 2
5
)2/3(∫
[0,1]
g3(x)dx
)1/3
.
Since the H¨ older inequality turns into an equality, the functions g3 and x3/2 must
be proportional, i.e., g(x) = c√x, where c ∈ C is an arbitrary constant.
JPE, May 2008. Show that
(∫ 1
0
x3
(1 −x)1/5dx
)5
≤ 16
81.
By the H¨ older inequality
∫ 1
0
x3
(1 −x)1/5dx ≤
(∫ 1
0
(x3)5dx
)1/5(∫ 1
0
1
[(1 −x)1/5]5/4dx
)4/5
=
(∫ 1
0
x15dx
)1/5(∫ 1
0
1
(1 −x)1/4dx
)4/5
=
( 1
16
)1/5( 4
3
)4/5
=
( 16
81
)1/5
.
43

Note: a much better bound can be achieved by
∫ 1
0
x3
(1 −x)1/5dx ≤
(∫ 1
0
(x3)5/3dx
)3/5(∫ 1
0
1
[(1 −x)1/5]5/2dx
)2/5
=
(∫ 1
0
x5dx
)3/5(∫ 1
0
1
(1 −x)1/2dx
)2/5
=
( 1
6
)3/5( 2
1
)2/5
=
( 1
54
)1/5
Here are the corresponding numerical values:
( 16
81
)1/5
≈ 0.723,
( 1
54
)1/5
≈ 0.4503
and the exact value of the integral is
∫ 1
0
x3
(1 −x)1/5dx = 5
4 − 5
3 + 15
14 − 5
19 ≈ 0.3916,
which can be easily found by change of variable x = 1 −y. One may wonder why we
care about applying H¨ older inequality to get a rough upper bound for something
that can be computed precisely by any Calculus-II student. Go ﬁgure...
JPE, Sept 2004. Prove that
∫ 1
0
√
x4 + 4x2 + 3dx ≤ 2
3
√
10.
By the Schwarz inequality
∫ 1
0
√
x4 + 4x2 + 3dx =
∫ 1
0
√
x2 + 3 ·
√
x2 + 1dx
≤
(∫ 1
0
(x2 + 3)dx
)1/2(∫ 1
0
(x2 + 1)dx
)1/2
=
√
10
3 ·
√
4
3 = 2
3
√
10.
JPE, May 2001. (a) Let a1,...,a n be positive numbers. Prove that their har-
monic mean is bounded by their arithmetic mean, i.e.
( 1
n
n∑
k=1
1
ak
)−1
≤ 1
n
n∑
k=1
ak.
(b) Characterize the vectors for which equality holds in (a).
44

(a) LetX = {1, 2,...,n } andµ be the counting measure on X. Let f : X → (0, ∞)
be deﬁned by f (k) = √ak. Then by the Schwarz inequality
n =
∫
X
1dµ =
∫
X
f · 1
f dµ ≤
√∫
X
f 2dx ·
√∫
X
1
f 2dx =
/√ad]cal√√/√ad]calve√√ex/√ad]calve√√ex√
n∑
k=1
ak ·
/√ad]cal√√/√ad]calve√√ex/√ad]calve√√ex√
n∑
k=1
1
ak
(b) Equality holds whenever f is proportional to 1 /f , i.e., ak = c/ak for some
constantc and all k = 1,...,n . This implies a1 = · · · =an.
JPE, May 1999. (i) Prove that
∫ π/2
0
√
x sinxdx ≤ π
2
√
2.
(ii) Prove that in fact the inequality is strict.
(i) By the Schwarz inequality
∫ π/2
0
√
x sinxdx ≤
(∫ π/2
0
xdx
)1/2(∫ π/2
0
sinxdx
)1/2
=
( 1
2
(π
2
)2)1/2
· 11/2 = π
2
√
2.
(ii) The Schwarz inequality does not turn into an equality here, because the func-
tions x and sinx are obviously not proportional to one another.
JPE, Sept 1997. Show that
(∫ 1
0
x1/2
(1 −x)1/3dx
)3
≤ 8
5.
By the H¨ older inequality
∫ 1
0
x1/2
(1 −x)1/3dx ≤
(∫ 1
0
(x1/2)3dx
)1/3(∫ 1
0
1
[(1 −x)1/3]3/2dx
)2/3
=
(∫ 1
0
x3/2dx
)1/3(∫ 1
0
1
(1 −x)1/2dx
)2/3
=
( 2
5
)1/3
· 22/3 =
( 8
5
)1/3
.
JPE, Sept 1994. Prove that
∫ ∞
1
√
1 +x3
x4 dx ≤
√
7
10.
45

By the Schwarz inequality
∫ ∞
1
√
1 +x3
x3
1
xdx ≤
[∫ ∞
1
1 +x3
x6 dx
]1/2[∫ ∞
1
1
x2dx
]1/2
≤
√
1
5 + 1
2 ·
√
1 =
√
7
10.
JPE, Sept 1993. Prove that
∫ ∞
0
e−x√
1 + sinxdx ≤
√
3
2.
We apply the Schwarz inequality to f =e−x/2 and g =e−x/2√1 + sinx:
∫ ∞
0
e−x√
1 + sinxdx ≤
[∫ ∞
0
e−xdx
]1/2[∫ ∞
0
e−x(1 + sinx)dx
]1/2
≤ 11/2 · (1 + 1
2 )1/2 =
√
3
2.
Note that we needed to compute here the integral
∫ ∞
0 e−x sinxdx = 1
2 . Even
though this is a routine Calculus-II exercise, it certainly takes valuable time dur-
ing the exam. At a later JPE (Sept 2011) the value of this elementary integral was
provided, to save time.
11 𝓁p spaces
JPE, May 2000. Do there exist two sequences ( an) ∈𝓁1 and (bn) ∈𝓁2 such that
(an +bn) is neither in 𝓁1 nor in 𝓁2?
No. Any sequence in ( an) ∈𝓁1 is also in 𝓁2. Indeed, there are only ﬁnitely many
an’s such that |an| > 1, and for all the other terms we have |an|2 ≤ |an|. Hence
the convergence of ∑ |an| implies the convergence of ∑ |an|2. Thus ( an +bn) will
be in 𝓁2.
JPE, May 1998. Does there exist a sequence ( xn) which is in 𝓁1+ε for all ε >0
but which is not in 𝓁1?
Yes,xn = 1/n.
JPE, May 1997. Suppose 1 ≤p ≤q ≤ ∞. Prove or disprove: 𝓁p ⊂𝓁q.
The inclusion is true. If p = ∞, then q = ∞ and the inclusion is trivial. If
p< ∞ and (an) ∈𝓁p, then there are only ﬁnitely many an’s such that |an|> 1. This
46

implies (an) ∈𝓁∞. Now suppose q <∞. Then for all an such that |an| ≤ 1 we have
|an|q ≤ |an|p. Hence the convergence of ∑ |an|p implies the convergence of ∑ |an|q.
JPE, May 1991. Find a sequence ( an) which is in 𝓁3 but not in 𝓁2.
Here: an = 1/√n. (More generally: an =n−b with any 1
3 <b ≤ 1
2 .)
47

