Part IB — Analysis II
Based on lectures by N. Wickramasekera
Notes taken by Dexter Chua
Michaelmas 2015
These notes are not endorsed by the lecturers, and I have modiﬁed them (often
signiﬁcantly) after lectures. They are nowhere near accurate representations of what
was actually lectured, and in particular, all errors are almost surely mine.
Uniform convergence
The general principle of uniform convergence. A uniform limit of continuous functions
is continuous. Uniform convergence and termwise integration and diﬀerentiation of
series of real-valued functions. Local uniform convergence of power series. [3]
Uniform continuity and integration
Continuous functions on closed bounded intervals are uniformly continuous. Review of
basic facts on Riemann integration (from Analysis I). Informal discussion of integration
of complex-valued and Rn-valued functions of one variable; proof that ‖
∫ b
a f(x) dx‖≤∫ b
a‖f(x)‖ dx. [2]
Rn as a normed space
Deﬁnition of a normed space. Examples, including the Euclidean norm on Rn and the
uniform norm on C[a, b]. Lipschitz mappings and Lipschitz equivalence of norms. The
Bolzano-Weierstrass theorem in Rn. Completeness. Open and closed sets. Continuity
for functions between normed spaces. A continuous function on a closed bounded
set in Rn is uniformly continuous and has closed bounded image. All norms on a
ﬁnite-dimensional space are Lipschitz equivalent. [5]
Diﬀerentiation from Rm to Rn
Deﬁnition of derivative as a linear map; elementary properties, the chain rule. Partial
derivatives; continuous partial derivatives imply diﬀerentiability. Higher-order deriva-
tives; symmetry of mixed partial derivatives (assumed continuous). Taylor’s theorem.
The mean value inequality. Path-connectedness for subsets of Rn; a function having
zero derivative on a path-connected open subset is constant. [6]
Metric spaces
Deﬁnition and examples. *Metrics used in Geometry*. Limits, continuity, balls,
neighbourhoods, open and closed sets. [4]
The Contraction Mapping Theorem
The contraction mapping theorem. Applications including the inverse function theorem
(proof of continuity of inverse function, statement of diﬀerentiability). Picard’s solution
of diﬀerential equations. [4]
1

Contents IB Analysis II
Contents
0 Introduction 3
1 Uniform convergence 4
2 Series of functions 12
2.1 Convergence of series . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.2 Power series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3 Uniform continuity and integration 16
3.1 Uniform continuity . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2 Applications to Riemann integrability . . . . . . . . . . . . . . . 17
3.3 Non-examinable fun* . . . . . . . . . . . . . . . . . . . . . . . . . 21
4 Rn as a normed space 25
4.1 Normed spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.2 Cauchy sequences and completeness . . . . . . . . . . . . . . . . 32
4.3 Sequential compactness . . . . . . . . . . . . . . . . . . . . . . . 35
4.4 Mappings between normed spaces . . . . . . . . . . . . . . . . . . 36
5 Metric spaces 40
5.1 Preliminary deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . 40
5.2 Topology of metric spaces . . . . . . . . . . . . . . . . . . . . . . 42
5.3 Cauchy sequences and completeness . . . . . . . . . . . . . . . . 45
5.4 Compactness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.5 Continuous functions . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.6 The contraction mapping theorem . . . . . . . . . . . . . . . . . 51
6 Diﬀerentiation from Rm to Rn 58
6.1 Diﬀerentiation from Rm to Rn . . . . . . . . . . . . . . . . . . . 58
6.2 The operator norm . . . . . . . . . . . . . . . . . . . . . . . . . . 66
6.3 Mean value inequalities . . . . . . . . . . . . . . . . . . . . . . . 68
6.4 Inverse function theorem . . . . . . . . . . . . . . . . . . . . . . . 70
6.5 2nd order derivatives . . . . . . . . . . . . . . . . . . . . . . . . . 75
2

0 Introduction IB Analysis II
0 Introduction
Analysis II, is, unsurprisingly, a continuation of IA Analysis I. The key idea in
the course is to generalize what we did in Analysis I. The ﬁrst thing we studied
in Analysis I was the convergence of sequences of numbers. Here, we would like
to study what it means for a sequence of functions to converge (this is technically
a generalization of what we did before, since a sequence of numbers is just a
sequence of functions fn :{0}→ R, but this is not necessarily a helpful way
to think about it). It turns out this is non-trivial, and there are many ways
in which we can deﬁne the convergence of functions, and diﬀerent notions are
useful in diﬀerent circumstances.
The next thing is the idea of uniform continuity. This is a stronger notion
than just continuity. Despite being stronger, we will prove an important theorem
saying any continuous function on [0, 1] (and in general a closed, bounded subset
of R) is uniform continuous. This does not mean that uniform continuity is a
useless notion, even if we are just looking at functions on [0 , 1]. The deﬁnition
of uniform continuity is much stronger than just continuity, so we now know
continuous functions on [0, 1] are really nice, and this allows us to prove many
things with ease.
We can also generalize in other directions. Instead of looking at functions, we
might want to deﬁne convergence for arbitrary sets. Of course, if we are given a
set of, say, apples, oranges and pears, we cannot deﬁne convergence in a natural
way. Instead, we need to give the set some additional structure, such as a norm
or metric. We can then deﬁne convergence in a very general setting.
Finally, we will extend the notion of diﬀerentiation from functions R→ R
to general vector functions Rn→ Rm. This might sound easy — we have been
doing this in IA Vector Calculus all the time. We just need to formalize it a bit,
just like what we did in IA Analysis I, right? It turns out diﬀerentiation from Rn
to Rm is much more subtle, and we have to be really careful when we do so, and it
takes quite a long while before we can prove that, say, f(x,y,z ) =x2e3z sin(2xy)
is diﬀerentiable.
3

1 Uniform convergence IB Analysis II
1 Uniform convergence
In IA Analysis I, we understood what it means for a sequence of real numbers
to converge. Suppose instead we have sequence of functions. In general, let E
be any set (not necessarily a subset of R), and fn :E→ R for n = 1, 2,··· be
a sequence of functions. What does it mean for fn to converge to some other
function f :E→ R?
We want this notion of convergence to have properties similar to that of
convergence of numbers. For example, a constant sequence fn = f has to
converge tof, and convergence should not be aﬀected if we change ﬁnitely many
terms. It should also act nicely with products and sums.
An obvious ﬁrst attempt would be to deﬁne it in terms of the convergence of
numbers.
Deﬁnition (Pointwise convergence). The sequence fn converges pointwise to f
if
f(x) = lim
n→∞
fn(x)
for all x.
This is an easy deﬁnition that is simple to check, and has the usual properties
of convergence. However, there is a problem. Ideally, We want to deduce
properties off from properties of fn. For example, it would be great if continuity
of all fn implies continuity of f, and similarly for integrability and values of
derivatives and integrals. However, it turns out we cannot. The notion of
pointwise convergence is too weak. We will look at many examples where f fails
to preserve the properties of fn.
Example. Let fn : [−1, 1]→ R be deﬁned by fn(x) =x1/(2n+1). These are all
continuous, but the pointwise limit function is
fn(x)→f(x) =
{


1 0 <x ≤ 1
0 x = 0
−1 −1≤x< 0
,
which is not continuous.
x
y
Less excitingly, we can let fn be given by the following graph:
4

1 Uniform convergence IB Analysis II
x
y
− 1
n
1
n
which converges to the same function as above.
Example. Letfn : [0, 1]→ R be the piecewise linear function formed by joining
(0, 0), ( 1
n,n ), ( 2
n, 0) and (1, 0).
x
y
0 2
n
1
n
n
The pointwise limit of this function is fn(x)→f(x) = 0. However, we have
∫ a
0
fn(x) dx = 1 for all n;
∫ 1
0
f(x) dx = 0.
So the limit of the integral is not the integral of the limit.
Example. Let fn : [0, 1]→ R be deﬁned as
fn(x) =
{
1 n!x∈ Z
0 otherwise
Since fn has ﬁnitely many discontinuities, it is Riemann integrable. However,
the limit is
fn(x)→f(x) =
{
1 x∈ Q
0 x⁄∈ Q
which is not integrable. So integrability of a function is not preserved by pointwise
limits.
This suggests that we need a stronger notion of convergence. Of course, we
don’t want this notion to be too strong. For example, we could deﬁne fn→f
to mean “fn =f for all suﬃciently large n”, then any property common to fn
is obviously inherited by the limit. However, this is clearly silly since only the
most trivial sequences would converge.
Hence we want to ﬁnd a middle ground between the two cases — a notion of
convergence that is suﬃciently strong to preserve most interesting properties,
5

1 Uniform convergence IB Analysis II
without being too trivial. To do so, we can examine what went wrong in the
examples above. In the last example, even though our sequence fn does indeed
tends pointwise to f, diﬀerent points converge at diﬀerent rates to f. For
example, at x = 1, we already have f1(1) =f(1) = 1. However, at x = (100!)−1,
f99(x) = 0 while f(x) = 1. No matter how large n is, we can still ﬁnd some x
where fn(x) diﬀers a lot from f(x). In other words, if we are given pointwise
convergence, there is no guarantee that for very large n, fn will “look like” f,
since there might be some points for which fn has not started to move towards
f.
Hence, what we need is for fn to converge to f at the same pace. This is
known as uniform convergence.
Deﬁnition (Uniform convergence). A sequence of functions fn :E→ R con-
verges uniformly to f if
(∀ε)(∃N)(∀x)(∀n>N )|fn(x)−f(x)|<ε.
Alternatively, we can say
(∀ε)(∃N)(∀n>N ) sup
x∈E
|fn(x)−f(x)|<ε.
Note that similar to pointwise convergence, the deﬁnition does not require E
to be a subset of R. It could as well be the set{Winnie, Piglet, Tigger}. However,
many of our theorems about uniform convergence will require E to be a subset
of R, or else we cannot sensibly integrate or diﬀerentiate our function.
We can compare this deﬁnition with the deﬁnition of pointwise convergence:
(∀ε)(∀x)(∃N)(∀n>N )|fn(x)−f(x)|<ε.
The only diﬀerence is in where there (∀x) sits, and this is what makes all the
diﬀerence. Uniform convergence requires that there is an N that works for every
x, while pointwise convergence just requires that for each x, we can ﬁnd an N
that works.
It should be clear from deﬁnition that if fn→ f uniformly, then fn→ f
pointwise. We will show that the converse is false:
Example. Again consider our ﬁrst example, where fn : [−1, 1]→ R is deﬁned
byfn(x) =x1/(2n+1). If the uniform limit existed, then it must be given by
fn(x)→f(x) =
{


1 0 <x ≤ 1
0 x = 1
−1 −1≤x< 0
,
since uniform convergence implies pointwise convergence.
We will show that we don’t have uniform convergence. Pick ε = 1
4. Then
for each n, x = 2−(2n+1) will have fn(x) = 1
2, f(x) = 1. So there is some x such
that|fn(x)−f(x)|>ε . So fn⁄→f uniformly.
Example. Let fn : R→ R be deﬁned by fn(x) = x
n. Then fn(x)→f(x) = 0
pointwise. However, this convergence is not uniform in R since|fn(x)−f(x)| =
|x|
n , and this can be arbitrarily large for any n.
6

1 Uniform convergence IB Analysis II
However, if we restrict fn to a bounded domain, then the convergence is
uniform. Let the domain be [−a,a ] for some positive, ﬁnite a. Then
sup|fn(x)−f(x)| =|x|
n ≤ a
n.
So given ε, pick N such that N >a
ε , and we are done.
Recall that for sequences of normal numbers, we have normal convergence and
Cauchy convergence, which we proved to be the same. Then clearly pointwise
convergence and pointwise Cauchy convergence of functions are equivalent. We
will now look into the case of uniform convergence.
Deﬁnition (Uniformly Cauchy sequence). A sequence fn :E→ R of functions
is uniformly Cauchy if
(∀ε> 0)(∃N)(∀m,n>N ) sup
x∈E
|fn(x)−fm(x)|<ε.
Our ﬁrst theorem will be that uniform Cauchy convergence and uniform
convergence are equivalent.
Theorem. Let fn : E→ R be a sequence of functions. Then ( fn) converges
uniformly if and only if (fn) is uniformly Cauchy.
Proof. First suppose that fn→ f uniformly. Given ε, we know that there is
some N such that
(∀n>N ) sup
x∈E
|fn(x)−f(x)|< ε
2.
Then if n,m>N , x∈E we have
|fn(x)−fm(x)|≤| fn(x)−f(x)| +|fm(x)−f(x)|<ε.
So done.
Now suppose (fn) is uniformly Cauchy. Then (fn(x)) is Cauchy for all x. So
it converges. Let
f(x) = lim
n→∞
fn(x).
We want to show that fn→ f uniformly. Given ε >0, choose N such that
whenever n,m > N, x∈ E, we have |fn(x)−fm(x)| < ε
2. Letting m→∞ ,
fm(x)→f(x). So we have |fn(x)−f(x)|≤ ε
2 <ε . So done.
This is an important result. If we are given a concrete sequence of functions,
then the usual way to show it converges is to compute the pointwise limit and
then prove that the convergence is uniform. However, if we are dealing with
sequences of functions in general, this is less likely to work. Instead, it is often
much easier to show that a sequence of functions is uniformly convergent by
showing it is uniformly Cauchy.
We now move on to show that uniform convergence tends to preserve proper-
ties of functions.
Theorem (Uniform convergence and continuity) . Let E ⊆ R, x ∈ E and
fn,f :E→ R. Suppose fn→f uniformly, andfn are continuous at x for all n.
Then f is also continuous at x.
In particular, if fn are continuous everywhere, then f is continuous every-
where.
7

1 Uniform convergence IB Analysis II
This can be concisely phrased as “the uniform limit of continuous functions
is continuous”.
Proof. Let ε> 0. Choose N such that for all n≥N, we have
sup
y∈E
|fn(y)−f(y)|<ε.
Since fN is continuous at x, there is some δ such that
|x−y|<δ ⇒|fN(x)−fN(y)|<ε.
Then for each y such that|x−y|<δ , we have
|f(x)−f(y)|≤| f(x)−fN(x)| +|fN(x)−fN(y)| +|fN(y)−f(y)|< 3ε.
Theorem (Uniform convergence and integrals) . Let fn,f : [a,b ] → R be
Riemann integrable, with fn→f uniformly. Then
∫ b
a
fn(t) dt→
∫ b
a
f(t) dt.
Proof. We have
⏐⏐⏐⏐⏐
∫ b
a
fn(t) dt−
∫ b
a
f(t) dt
⏐⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐
∫ b
a
fn(t)−f(t) dt
⏐⏐⏐⏐⏐
≤
∫ b
a
|fn(t)−f(t)| dt
≤ sup
t∈[a,b]
|fn(t)−f(t)|(b−a)
→ 0 as n→∞.
This is really the easy part. What we would also want to prove is that if fn
is integrable, fn→f uniformly, thenf is integrable. This is indeed true, but we
will not prove it yet. We will come to this later on at the part where we talk a
lot about integrability.
So far so good. However, the relationship between uniform convergence and
diﬀerentiability is more subtle. The uniform limit of diﬀerentiable functions
need not be diﬀerentiable. Even if it were, the limit of the derivative is not
necessarily the same as the derivative of the limit, even if we just want pointwise
convergence of the derivative.
Example. Let fn,f : [−1, 1]→ R be deﬁned by
fn(x) =|x|1+1/n, f (x) =|x|.
Then fn→f uniformly (exercise).
Each fn is diﬀerentiable — this is obvious at x⁄= 0, and at x = 0, the
derivative is
f′
n(0) = lim
x→0
fn(x)−fn(0)
x = lim
x→0
sgn(x)|x|1/n = 0
However, the limit f is not diﬀerentiable at x = 0.
8

1 Uniform convergence IB Analysis II
Example. Let
fn(x) = sinnx√n
for all x∈ R. Then
sup
x∈R
|fn(x)|≤ 1√n→ 0.
So fn→f = 0 uniformly in R. However, the derivative is
f′
n(x) =√n cosnx,
which does not converge to f′ = 0, e.g. at x = 0.
Hence, for diﬀerentiability to play nice, we need a condition even stronger
than uniform convergence.
Theorem. Let fn : [a,b ]→ R be a sequence of functions diﬀerentiable on [ a,b ]
(at the end points a, b, this means that the one-sided derivatives exist). Suppose
the following holds:
(i) For some c∈ [a,b ], fn(c) converges.
(ii) The sequence of derivatives ( f′
n) converges uniformly on [a,b ].
Then (fn) converges uniformly on [a,b ], and iff = limfn, thenf is diﬀerentiable
with derivativef′(x) = limf′
n(x).
Note that we do not assume that f′
n are continuous or even Riemann inte-
grable. If they are, then the proof is much easier!
Proof. If we are given a speciﬁc sequence of functions and are asked to prove
that they converge uniformly, we usually take the pointwise limit and show that
the convergence is uniform. However, given a general function, this is usually not
helpful. Instead, we can use the Cauchy criterion by showing that the sequence
is uniformly Cauchy.
We want to ﬁnd an N such that n,m > Nimplies sup|fn−fm| < ε. We
want to relate this to the derivatives. We might want to use the fundamental
theorem of algebra for this. However, we don’t know that the derivative is
integrable! So instead, we go for the mean value theorem.
Fix x∈ [a,b ]. We apply the mean value theorem to fn−fm to get
(fn−fm)(x)− (fn−fm)(c) = (x−c)(f′
n−f′
m)(t)
for some t∈ (x,c ).
Taking the supremum and rearranging terms, we obtain
sup
x∈[a,b]
|fn(x)−fm(x)|≤| fn(c)−fm(c)| + (b−a) sup
t∈[a,b]
|f′
n(t)−f′
m(t)|.
So given any ε, since f′
n andfn(c) converge and are hence Cauchy, there is some
N such that for any n,m≥N,
sup
t∈[a,b]
|f′
n(t)−f′
m(t)|<ε, |fn(c)−fm(c)|<ε.
9

1 Uniform convergence IB Analysis II
Hence we obtain
n,m≥N⇒ sup
x∈[a,b]
|fn(x)−fm(x)|< (1 +b−a)ε.
So by the Cauchy criterion, we know thatfn converges uniformly. Letf = limfn.
Now we have to check diﬀerentiability. Let f′
n→h. For any ﬁxed y∈ [a,b ],
deﬁne
gn(x) =
{fn(x)−fn(y)
x−y x⁄=y
f′
n(y) x =y
Then by deﬁnition, fn is diﬀerentiable at y iﬀgn is continuous at y. Also, deﬁne
g(x) =
{f (x)−f (y)
x−y x⁄=y
h(y) x =y
Then f is diﬀerentiable with derivative h at y iﬀ g is continuous at y. However,
we know that gn→g pointwise on [a,b ], and we know that gn are all continuous.
To conclude that g is continuous, we have to show that the convergence is
uniform. To show that gn converges uniformly, we rely on the Cauchy criterion
and the mean value theorem.
Forx⁄=y, we know that
gn(x)−gm(x) = (fn−fm)(x)− (fn−fm)(y)
x−y = (f′
n−f′
m)(t)
for somet∈ [x,y ]. This also holds for x =y, sincegn(y)−gm(y) =f′
n(y)−f′
m(y)
by deﬁnition.
Let ε> 0. Since f′ converges uniformly, there is some N such that for all
x⁄=y, n,m>N , we have
|gn(x)−gm(x)|≤ sup|f′
n−f′
m|<ε.
So
n,m≥N⇒ sup
[a,b]
|gn−gm|<ε,
i.e.gn converges uniformly. Hence the limit functiong is continuous, in particular
at x =y. So f is diﬀerentiable at y and f′(y) =h(y) = limf′
n(y).
If we assume additionally that f′
n are continuous, then there is an easy proof
of this theorem. By the fundamental theorem of calculus, we have
fn(x) =fn(c) +
∫ x
c
f′
n(t) dt. (∗)
Then we get that
sup
[a,b]
|fn(x)−fm(x)|≤| fn(c)−fm(c)| + sup
x∈[a,b]
⏐⏐⏐⏐
∫ x
c
(f′
n(t)−f′
m(t)) dt
⏐⏐⏐⏐
≤|fn(c)−fm(c)| + (b−a) sup
t∈[a,b]
|f′
n(t)−f′
m(t)|
<ε
10

1 Uniform convergence IB Analysis II
for suﬃciently large n,m>N .
So by the Cauchy criterion,fn→f uniformly for some functionf : [a,b ]→ R.
Since the f′
n are continuous, h = lim
n→∞
f′
n is continuous and hence integrable.
Taking the limit of (∗), we get
f(x) =f(c) +
∫ x
c
h(t) dt.
Then the fundamental theorem of calculus says that f is diﬀerentiable and
f′(x) =h(x) = limf′
n(x). So done.
Finally, we have a small proposition that can come handy.
Proposition.
(i) Let fn,gn :E→ R, be sequences, and fn→ f, gn→ g uniformly on E.
Then for any a,b∈ R, afn +bgn→af +bg uniformly.
(ii) Let fn→f uniformly, and let g :E→ R is bounded. Then gfn :E→ R
converges uniformly to gf .
Proof.
(i) Easy exercise.
(ii) Say |g(x)|<M for all x∈E. Then
|(gfn)(x)− (gf )(x)|≤ M|fn(x)−f(x)|.
So
sup
E
|gfn−gf|≤ M sup
E
|fn−f|→ 0.
Note that (ii) is false without assuming boundedness. An easy example is to
takefn = 1
n, x∈ R, and g(x) =x. Then fn→ 0 uniformly, but (gfn)(x) = x
n
does not converge uniformly to 0.
11

2 Series of functions IB Analysis II
2 Series of functions
2.1 Convergence of series
Recall that in Analysis I, we studied the convergence of a series of numbers.
Here we will look at a series of functions. The deﬁnitions are almost exactly the
same.
Deﬁnition (Convergence of series). Let gn;E→ R be a sequence of functions.
Then we say the series ∑∞
n=1gn converges at a point x∈E if the sequence of
partial sums
fn =
n∑
j=1
gj
converges at x. The series converges uniformly if fn converges uniformly.
Deﬁnition (Absolute convergence). ∑gn converges absolutely at a point x∈E
if∑|gn| converges at x.∑gn converges absolutely uniformly if∑|gn| converges uniformly.
Proposition. Let gn :E→ R. If ∑gn converges absolutely uniformly, then∑gn converges uniformly.
Proof. Again, we don’t have a candidate for the limit. So we use the Cauchy
criterion.
Let fn =
n∑
j=1
gj and hn(x) =
n∑
j=1
|gj| be the partial sums. Then for n>m ,
we have
|fn(x)−fm(x)| =
⏐⏐⏐⏐⏐⏐
n∑
j=m+1
gj(x)
⏐⏐⏐⏐⏐⏐
≤
n∑
j=m+1
|gj(x)| =|hn(x)−hm(x)|.
By hypothesis, we have
sup
x∈E
|hn(x)−hm(x)|→ 0 as n,m→∞.
So we get
sup
x∈E
|fn(x)−fm(x)|→ 0 as n,m→∞.
So the result follows from the Cauchy criteria.
It is important to remember that uniform convergence plus absolute pointwise
convergence does not imply absolute uniform convergence.
Example. Consider the series
∞∑
n=1
(−1)n
n xn.
This converges absolutely for everyx∈ [0, 1) since it is bounded by the geometric
series. In fact, it converges uniformly on [0, 1) (see example sheet). However,
this does not converge absolutely uniformly on [0, 1).
12

2 Series of functions IB Analysis II
We can consider the diﬀerence in partial sums
n∑
j=m
⏐⏐⏐⏐
(−1)j
j xj
⏐⏐⏐⏐ =
n∑
j=m
1
j|x|j≥
( 1
m + 1
m + 1 +··· + 1
n
)
|x|n.
For eachN, we can make this diﬀerence large enough by picking a really large
n, and then making x close enough to 1. So the supremum is unbounded.
Theorem (Weierstrass M-test). Let gn : E→ R be a sequence of functions.
Suppose there is some sequence Mn such that for all n, we have
sup
x∈E
|gn(x)|≤ Mn.
If∑Mn converges, then∑gn converges absolutely uniformly.
This is in fact a very easy result, and we could as well reproduce the proof
whenever we need it. However, this pattern of proving absolute uniform conver-
gence is so common that we prove it as a test.
Proof. Let fn =
n∑
j=1
|gj| be the partial sums. Then for n>m , we have
|fn(x)−fm(x)| =
n∑
j=m+1
|gj(x)|≤
n∑
j=m+1
Mj.
Taking supremum, we have
sup|fn(x)−fm(x)|≤
n∑
j=m+1
Mj→ 0 as n,m→∞.
So done by the Cauchy criterion.
2.2 Power series
A particularly interesting kind of series is a power series. We have already met
these in IA Analysis I and proved some results about them. However, our results
were pointwise results, discussing how∑cn(x−a)n behaves at a particular point
x. Here we will quickly look into how the power series behaves as a function of
x. In particular, we want to know whether it converges absolutely uniformly.
Theorem. Let
∞∑
n=0
cn(x−a)n be a real power series. Then there exists a unique
numberR∈ [0, +∞] (called the radius of convergence) such that
(i) If |x−a|<R , then∑cn(x−a)n converges absolutely.
(ii) If |x−a|>R , then∑cn(x−a)n diverges.
(iii) IfR> 0 and 0 <r<R , then∑cn(x−a)n converges absolutely uniformly
on [a−r,a +r].
We say that the sum converges locally absolutely uniformly inside the circle
of convergence, i.e. for every point y∈ (a−R,a +R), there is some open
interval aroundy on which the sum converges absolutely uniformly.
13

2 Series of functions IB Analysis II
These results hold for complex power series as well, but for concreteness we will
just do it for real series.
Note that the ﬁrst two statements are things we already know from IA
Analysis I, and we are not going to prove them.
Proof. See IA Analysis I for (i) and (ii).
For (iii), note that from (i), taking x = a−r, we know that ∑|cn|rn is
convergent. But we know that if x∈ [a−r,a +r], then
|cn(x−a)n|≤| cn|rn.
So the result follows from the Weierstrass M-test by taking Mn =|cn|rn.
Note that uniform convergence need not hold on the entire interval of con-
vergence.
Example. Consider∑xn. This converges for x∈ (−1, 1), but uniform conver-
gence fails on (−1, 1) since the tail
n∑
j=m
xj =xn
n−m∑
j=0
xj≥ xm
1−x.
This is not uniformly small since we can make this large by picking x close to 1.
Theorem (Termwise diﬀerentiation of power series). Suppose∑cn(x−n)n is
a real power series with radius of convergence R> 0. Then
(i) The “derived series”
∞∑
n=1
ncn(x−a)n−1
has radius of convergence R.
(ii) The function deﬁned by f(x) = ∑cn(x−a)n, x∈ (a−R,a +R) is
diﬀerentiable with derivative f′(x) =∑ncn(x−a)n−1 within the (open)
circle of convergence.
Proof.
(i) Let R1 be the radius of convergence of the derived series. We know
|cn(x−a)n| =|cn||x−a|n−1|x−a|≤| ncn(x−a)n−1||x−a|.
Hence if the derived series ∑ncn(x−a)n−1 converges absolutely for some
x, then so does ∑cn(x−a)n. So R1≤R.
Suppose that the inequality is strict, i.e. R1 < R, then there are r1,r
such that R1 < r1 < r < R, where ∑n|cn|rn−1
1 diverges while ∑|cn|rn
converges. But this cannot be true since n|cn|rn−1
1 ≤|cn|rn for suﬃciently
large n. So we must have R1 =R.
14

2 Series of functions IB Analysis II
(ii) Let fn(x) =
n∑
j=0
cj(x−a)j. Then f′
n(x) =
n∑
j=1
jcj(x−a)j−1. We want
to use the result that the derivative of limit is limit of derivative. This
requires that fn converges at a point, and that f′
n converges uniformly.
The ﬁrst is obviously true, and we know that f′
n converges uniformly on
[a−r,a +r] for anyr<R . So for each x0, there is some interval containing
x0 on which f′
n is convergent. So on this interval, we know that
f(x) = lim
n→∞
fn(x)
is diﬀerentiable with
f′(x) = lim
n→∞
f′
n(x) =
∞∑
j=1
jcj(x−a)j.
In particular,
f′(x0) =
∞∑
j=1
jcj(x0−a)j.
Since this is true for all x0, the result follows.
15

3 Uniform continuity and integration IB Analysis II
3 Uniform continuity and integration
3.1 Uniform continuity
Recall that we had a rather weak notion of convergence, known as pointwise
convergence, and then promoted it to uniform convergence. The process of this
promotion is to replace the condition “for each x, we can ﬁnd an ε” to “we can
ﬁnd an ε that works for each x”. We are going to do the same for continuity to
obtain uniform continuity.
Deﬁnition (Uniform continuity). Let E⊆ R and f :E→ R. We say that f is
uniformly continuous on E if
(∀ε)(∃δ >0)(∀x)(∀y)|x−y|<δ ⇒|f(x)−f(y)|<ε.
Compare this to the deﬁnition of continuity:
(∀ε)(∀x)(∃δ >0)(∀y)|x−y|<δ ⇒|f(x)−f(y)|<ε.
Again, we have shifted the (∀x) out of the (∃δ) quantiﬁer. The diﬀerence is
that in regular continuity, δ can depend on our choice of x, but in uniform
continuity, it only depends on y. Again, clearly a uniformly continuous function
is continuous.
In general, the converse is not true, as we will soon see in two examples.
However, the converse is true in a lot of cases.
Theorem. Any continuous function on a closed, bounded interval is uniformly
continuous.
Proof. We are going to prove by contradiction. Suppose f : [a,b ]→ R is not
uniformly continuous. Since f is not uniformly continuous, there is some ε> 0
such that for all δ = 1
n, there is some xn,yn such that |xn−yn| < 1
n but
|f(xn)−f(yn)|>ε .
Since we are on a closed, bounded interval, by Bolzano-Weierstrass, (xn) has a
convergent subsequence (xni)→x. Then we also have yni→x. So by continuity,
we must have f(xni)→f(x) and f(yni)→f(x). But|f(xni)−f(yni)|>ε for
all ni. This is a contradiction.
Note that we proved this in the special case where the domain is [ a,b ] and
the image is R. In fact, [a,b ] can be replaced by any compact metric space; R
by any metric space. This is since all we need is for Bolzano-Weierstrass to hold
in the domain, i.e. the domain is sequentially compact (ignore this comment if
you have not taken IB Metric and Topological Spaces).
Instead of a contradiction, we can also do a direct proof of this statement,
using the Heine-Borel theorem which says that [0 , 1] is compact.
While this is a nice theorem, in general a continuous function need not be
uniformly continuous.
Example. Consider f : (0, 1]→ R given by f(x) = 1
x. This is not uniformly
continuous, since when we get very close to 0, a small change in x produces a
large change in 1
x.
In particular, for any δ <1 and x < δ, y = x
2 , then|x−y| = x
2 < δ but
|f(x)−f(y)| = 1
x > 1.
16

3 Uniform continuity and integration IB Analysis II
In this example, the function is unbounded. However, even bounded functions
can be not uniformly continuous.
Example. Let f : (0, 1]→ R, f(x) = sin 1
x. We let
xn = 1
2nπ, y n = 1
(2n + 1
2)π.
Then we have
|f(xn)−f(yn)| =|0− 1| = 1,
while
|xn−yn| = π
2n(4n + 1)→ 0.
3.2 Applications to Riemann integrability
We can apply the idea of uniform continuity to Riemann integration.
We ﬁrst quickly recap and summarize things we know about Riemann integrals
IA Analysis I. Let f : [a,b ]→ R be a bounded function, say m≤f(x)≤M for
all x∈ [a,b ]. Consider a partition of [ a,b ]
P ={a0,a 1,··· ,an}.
i.e. a =a0 <a 1 <a 2 <··· <a n =b. The upper sum is deﬁned as
U(P,f ) =
n−1∑
j=0
(aj+1−aj) sup
[aj,aj+1]
f.
Similarly, the lower sum is deﬁned as
L(P,f ) =
n−1∑
j=0
(aj+1−aj) inf
[aj,aj+1]
f.
It is clear from deﬁnition that
m(b−a)≤L(P,f )≤U(P,f )≤M(b−a).
Also, if a partition P∗ is a reﬁnement of a partition P , i.e. it contains all the
points of P and possibly more, then
L(P,f )≤L(P∗,f )≤U(P∗,f )≤U(P,f ).
It thus follows that if P1 and P2 are arbitrary partitions, then
L(P1,f )≤U(P2,f ),
which we can show by ﬁnding a partition that is simultaneously a reﬁnement of
P1 and P2. The importance of this result is that
sup
P
L(P,f )≤ inf
P
U(P,f ),
17

3 Uniform continuity and integration IB Analysis II
where we take extrema over all partitions P . We deﬁne these to be the upper
and lower integrals
I∗(f) = inf
P
U(P,f ), I ∗(f) = sup
P
L(P,f ).
So we know that
m(b−a)≤I∗(f)≤I∗(f)≤M(b−a).
Now given any ε> 0, by deﬁnition of the inﬁmum, there is a partition P1 such
that
U(P1,f )<I∗(f) +ε
2.
Similarly, there is a partition P2 such that
L(P2,f )>I∗(f)− ε
2.
So if we let P =P1∪P2, then P is a reﬁnement of both P1 and P2. So
U(P,f )<I∗(f) +ε
2
and
L(P,f )>I∗(f)− ε
2.
Combining these, we know that
0≤I∗(f)−I∗(f)<U (P,f )−L(P,f )<I∗(f)−I∗(f) +ε.
We now deﬁne what it means to be Riemann integrable.
Deﬁnition (Riemann integrability). A bounded function f : [a,b ]→ R is
Riemann integrable on [a,b ] if I∗(f) =I∗(f). We write
∫ b
a
f(x) dx =I∗(f) =I∗(f).
Then the Riemann criterion says
Theorem (Riemann criterion for integrability). A bounded function f : [a,b ]→
R is Riemann integrable if and only if for every ε, there is a partition P such
that
U(P,f )−L(P,f )<ε.
That’s the end of our recap. Now we have a new theorem.
Theorem. If f : [a,b ]→ [A,B ] is integrable and g : [A,B ]→ R is continuous,
then g◦f : [a,b ]→ R is integrable.
Proof. Letε> 0. Since g is continuous,g is uniformly continuous. So we can ﬁnd
δ =δ(ε)> 0 such that for any x,y∈ [A,B ], if|x−y|<δ then|g(x)−g(y)|<ε .
Since f is integrable, for arbitrary ε′, we can ﬁnd a partition P ={a =a0 <
a1 <··· <a n =b} such that
U(P,f )−L(P,f ) =
n−1∑
j=0
(aj+1−aj)
(
sup
Ij
f− inf
Ij
f
)
<ε′. (∗)
18

3 Uniform continuity and integration IB Analysis II
Our objective is to make U(P,g◦f)−L(P,g◦f) small. By uniform continuity
of g, if supIjf− infIjf is less than δ, then supIjg◦f− infIjg◦f will be less
than ε. We like these sorts of intervals. So we let
J =
{
j : sup
Ij
f− inf
Ij
f <δ
}
,
We now show properly that these intervals are indeed “nice”. For any j∈J, for
all x,y∈Ij, we must have
|f(x)−f(y)|≤ sup
z1,z2∈Ij
(f(z1)−f(z2)) = sup
Ij
f− inf
Ij
f <δ.
Hence, for each j∈J and all x,y∈Ij, we know that
|g◦f(x)−g◦f(y)|<ε.
Hence, we must have
sup
Ij
(
g◦f(x)−g◦f(y)
)
≤ε.
So
sup
Ij
g◦f− inf
Ij
g◦f≤ε.
Hence we know that
U(P,g◦f)−L(P,g◦f) =
n∑
j=0
(aj+1−aj)
(
sup
Ij
g◦f− inf
Ij
g◦f
)
=
∑
j∈J
(aj+1−aj)
(
sup
Ij
g◦f− inf
Ij
g◦f
)
+
∑
j⁄∈J
(aj+1−aj)
(
sup
Ij
g◦f− inf
Ij
g◦f
)
.
≤ε(b−a) + 2 sup
[A,B]
|g|
∑
j⁄∈J
(aj+1−aj).
Hence, it suﬃces here to make ∑
j⁄∈J
(aj+1−aj) small. From (∗), we know that we
must have ∑
j⁄∈J
(aj+1−aj)< ε′
δ,
or else U(P,f )−L(P,f )>ε′. So we can bound
U(P,g◦f)−L(P,g◦f)≤ε(b−a) + 2 sup
[A,B]
|g|ε′
δ.
So if we are given an ε at the beginning, we can get a δ by uniform continuity.
Afterwards, we pick ε′ such that ε′ =εδ. Then we have shown that given any ε,
there exists a partition such that
U(P,g◦f)−L(P,g◦f)<
(
(b−a) + 2 sup
[A,B]
|g|
)
ε.
Then the claim follows from the Riemann criterion.
19

3 Uniform continuity and integration IB Analysis II
As an immediate consequence, we know that any continuous function is
integrable, since we can just let f be the identity function, which we can easily
show to be integrable.
Corollary. A continuous function g : [a,b ]→ R is integrable.
Theorem. Let fn : [a,b ]→ R be bounded and integrable for all n. Then if
(fn) converges uniformly to a function f : [a,b ]→ R, then f is bounded and
integrable.
Proof. Let
cn = sup
[a,b]
|fn−f|.
Then uniform convergence says that cn→ 0. By deﬁnition, for each x, we have
fn(x)−cn≤f(x)≤fn(x) +cn.
Since fn is bounded, this implies that f is bounded by sup|fn| +cn. Also, for
anyx,y∈ [a,b ], we know
f(x)−f(y)≤ (fn(x)−fn(y)) + 2cn.
Hence for any partition P ,
U(P,f )−L(L,f )≤U(P,fn)−L(P,fn) + 2(b−a)cn.
So givenε> 0, ﬁrst choose n such that 2(b−a)cn < ε
2. Then choose P such that
U(P,fn)−L(P,fn)< ε
2. Then for this partition, U(P,f )−L(P,f )<ε .
Most of the theory of Riemann integration extends to vector-valued or
complex-valued functions (of a single real variable).
Deﬁnition (Riemann integrability of vector-valued function). Let f : [a,b ]→ Rn
be a vector-valued function. Write
f(x) = (f1(x),f 2(x),··· ,fn(x))
for all x∈ [a,b ]. Then f is Riemann integrable iﬀ fj : [a,b ]→ R is integrable for
all j. The integral is deﬁned as
∫ b
a
f(x) dx =
(∫ b
a
f1(x) dx,··· ,
∫ b
a
fn(x) dx
)
∈ Rn.
It is easy to see that most basic properties of integrals of real functions extend
to the vector-valued case. A less obvious fact is the following.
Proposition. If f : [a,b ]→ Rn is integrable, then the function ‖f‖ : [a,b ]→ R
deﬁned by
‖f‖(x) =‖f(x)‖ =
vuu√
n∑
j=1
f 2
j (x).
is integrable, and ‖‖‖‖‖
∫ b
a
f(x) dx
‖‖‖‖‖≤
∫ b
a
‖f‖(x) dx.
20

3 Uniform continuity and integration IB Analysis II
This is a rather random result, but we include it here because it will be
helpful at some point in time.
Proof. The integrability of‖f‖ is clear since squaring and taking square roots
are continuous, and a ﬁnite sum of integrable functions is integrable. To show
the inequality, we let
v = (v1,··· ,vn) =
∫ b
a
f(x) dx.
Then by deﬁnition,
vj =
∫ b
a
fj(x) dx.
If v = 0, then we are done. Otherwise, we have
‖v‖2 =
n∑
j=1
v2
j
=
n∑
j=1
vj
∫ b
a
fj(x) dx
=
∫ b
a
n∑
j=1
(vjfj(x)) dx
=
∫ b
a
v· f(x) dx
Using the Cauchy-Schwarz inequality, we get
≤
∫ b
a
‖v‖‖f‖(x) dx
=‖v‖
∫ b
a
‖f‖ dx.
Divide by‖v‖ and we are done.
3.3 Non-examinable fun*
Since there is time left in the lecture, we’ll write down a really remarkable result.
Theorem (Weierstrass Approximation Theorem*). If f : [0, 1]→ R is continu-
ous, then there exists a sequence of polynomials (pn) such thatpn→f uniformly.
In fact, the sequence can be given by
pn(x) =
n∑
k=0
f
(k
n
)(n
k
)
xk(1−x)n−k.
These are known as Bernstein polynomials.
Of course, there are many diﬀerent sequences of polynomials converging
uniformly to f. Apart from the silly examples like adding 1
n to each pn, there
can also be vastly diﬀerent ways of constructing such polynomial sequences.
21

3 Uniform continuity and integration IB Analysis II
Proof. For convenience, let
pn,k(x) =
(n
k
)
xk(1−x)n−k.
First we need a few facts about these functions. Clearly, pn,k(x)≥ 0 for all
x∈ [0, 1]. Also, by the binomial theorem,
n∑
k=0
(n
k
)
xkyn−k = (x +y)n.
So we get
n∑
k=0
pn,k(x) = 1.
Diﬀerentiating the binomial theorem with respect to x and putting y = 1−x
gives
n∑
k=0
(n
k
)
kxk−1(1−x)n−k =n.
We multiply byx to obtain
n∑
k=0
(n
k
)
kxk(1−x)n−k =nx.
In other words,
n∑
k=0
kpn,k(x) =nx.
Diﬀerentiating once more gives
n∑
k=0
k(k− 1)pn,k(x) =n(n− 1)x2.
Adding these two results gives
n∑
k=0
k2pn,k(x) =n2x2 +nx(1−x).
We will write our results in a rather weird way:
n∑
k=0
(nx−k)2pn,k(x) =n2x2− 2nx·nx +n2x2 +nx(1−x) =nx(1−x). (∗)
This is what we really need.
Now givenε, since f is continuous,f is uniformly continuous. So pick δ such
that|f(x)−f(y)|<ε whenever|x−y|<δ .
22

3 Uniform continuity and integration IB Analysis II
Since∑pn,k(x) = 1, f(x) =∑pn,k(x)f(x). Now for each ﬁxed x, we can
write
|pn(x)−f(x)| =
⏐⏐⏐⏐⏐
n∑
k=0
(
f
(k
n
)
−f(x)
)
pn,k(x)
⏐⏐⏐⏐⏐
≤
n∑
k=0
⏐⏐⏐⏐f
(k
n
)
−f(x)
⏐⏐⏐⏐pn,k(x)
=
∑
k:|x−k/n|<δ
(⏐⏐⏐⏐f
(k
n
)
−f(x)
⏐⏐⏐⏐pn,k(x)
)
+
∑
k:|x−k/n|≥δ
(⏐⏐⏐⏐f
(k
n
)
−f(x)
⏐⏐⏐⏐pn,k(x)
)
≤ε
n∑
k=0
pn,k(x) + 2 sup
[0,1]
|f|
∑
k:|x−k/n|>δ
pn,k(x)
≤ε + 2 sup
[0,1]
|f|· 1
δ2
∑
k:|x−k/n|>δ
(
x− k
n
)2
pn,k(x)
≤ε + 2 sup
[0,1]
|f|· 1
δ2
n∑
k=0
(
x− k
n
)2
pn,k(x)
=ε + 2 sup|f|
δ2n2 nx(1−x)
≤ε + 2 sup|f|
δ2n
Hence given anyε andδ, we can pickn suﬃciently large that that|pn(x)−f(x)|<
2ε. This is picked independently of x. So done.
Unrelatedly, we might be interested in the question — when is a function
Riemann integrable? A possible answer is if it satisﬁes the Riemann integrability
criterion, but this is not really helpful. We know that a function is integrable if
it is continuous. But it need not be. It could be discontinuous at ﬁnitely many
points and still be integrable. If it has countably many discontinuities, then we
still can integrate it. How many points of discontinuity can we accommodate if
we want to keep integrability?
To answer this questions, we have Lebesgue’s theorem. To state this theorem,
we need the following deﬁnition:
Deﬁnition (Lebesgue measure zero*). A subsetA⊆ R is said to have (Lebesgue)
measure zero if for any ε> 0, there exists a countable (possibly ﬁnite) collection
of open intervals Ij such that
A⊆
∞⋃
j=1
IJ,
and ∞∑
j=1
|Ij|<ε.
here|Ij| is deﬁned as the length of the interval, not the cardinality (obviously).
23

3 Uniform continuity and integration IB Analysis II
This is a way to characterize “small” sets, and in general a rather good way.
This will be studied in depth in the IID Probability and Measure course.
Example.
– The empty set has measure zero.
– Any ﬁnite set has measure zero.
– Any countable set has measure zero. If A ={a0,a 1,···} , take
Ij =
(
aj− ε
2j+1,aj + ε
2j+1
)
.
Then A is contained in the union and the sum of lengths is ε.
– A countable union of sets of measure zero has measure zero, using a similar
proof strategy as above.
– Any (non-trivial) interval does not have measure zero.
– The Cantor set, despite being uncountable, has measure zero. The Cantor
set is constructed as follows: start with C0 = [0, 1]. Remove the middle
third
( 1
3, 2
3
)
to obtain C1 =
[
0, 1
3
]
∪
[ 2
3, 1
]
. Removing the middle third of
each segment to obtain
C2 =
[
0, 1
9
]
∪
[2
9, 3
9
]
∪
[6
9, 7
9
]
∪
[8
9, 1
]
.
Continue iteratively by removing the middle thirds of each part. Deﬁne
C =
∞⋂
n=0
Cn,
which is the Cantor set. Since each Cn consists of 2 n disjoint closed
intervals of length 1/3n, the total length of the segments of Cn is
( 2
3
)n
→ 0.
So we can coverC by arbitrarily small union of intervals. Hence the Cantor
set has measure zero.
It is slightly trickier to show that C is uncountable, and to save time, we
are not doing it now.
Using this deﬁnition, we can have the following theorem:
Theorem (Lebesgue’s theorem on the Riemann integral*) . Let f : [a,b ]→ R
be a bounded function, and let Df be the set of points of discontinuities of f.
Then f is Riemann integrable if and only if Df has measure zero.
Using this result, a lot of our theorems follow easily of these. Apart from
the easy ones like the sum and product of integrable functions is integrable,
we can also easily show that the composition of a continuous function with an
integrable function is integrable, since composing with a continuous function
will not introduce more discontinuities.
Similarly, we can show that the uniform limit of integrable functions is
integrable, since the points of discontinuities of the uniform limit is at most the
(countable) union of all discontinuities of the functions in the sequence.
Proof is left as an exercise for the reader, in the example sheet.
24

4 Rn as a normed space IB Analysis II
4 Rn as a normed space
4.1 Normed spaces
Our objective is to extend most of the notions we had about functions of a
single variable f : R→ R to functions of multiple variables f : Rn→ R. More
generally, we want to study functions f : Ω→ Rm, where Ω⊆ Rn. We wish to
deﬁne analytic notions such as continuity, diﬀerentiability and even integrability
(even though we are not doing integrability in this course).
In order to do this, we need more structure on Rn. We already know that
Rn is a vector space, which means that we can add, subtract and multiply by
scalars. But to do analysis, we need something to replace our notion of |x−y|
in R. This is known as a norm.
It is useful to deﬁne and study this structure in an abstract setting, as
opposed to thinking about Rn speciﬁcally. This leads to the general notion of
normed spaces.
Deﬁnition (Normed space). Let V be a real vector space. A norm on V is a
function‖·‖ :V → R satisfying
(i) ‖x‖≥ 0 with equality iﬀ x = 0 (non-negativity)
(ii) ‖λx‖ =|λ|‖x‖ (linearity in scalar multiplication)
(iii) ‖x + y‖≤‖ x‖ +‖y‖ (triangle inequality)
A normed space is a pair (V,‖·‖ ). If the norm is understood, we just say V is
a normed space. We do have to be slightly careful since there can be multiple
norms on a vector space.
Intuitively,‖x‖ is the length or magnitude of x.
Example. We will ﬁrst look at ﬁnite-dimensional spaces. This is typically Rn
with diﬀerent norms.
– Consider Rn, with the Euclidean norm
‖x‖2 =
(∑
x2
i
)2
.
This is also known as the usual norm. It is easy to check that this is a
norm, apart from the triangle inequality. So we’ll just do this. We have
‖x + y‖2 =
n∑
i=1
(xi +yi)2
=‖x‖2 +‖y‖2 + 2
∑
xiyi
≤‖ x‖2 +‖y‖2 + 2‖x‖y‖
= (‖x‖2 +‖y‖2),
where we used the Cauchy-Schwarz inequality. So done.
– We can have the following norm on Rn:
‖x‖1 =
∑
|xi|.
It is easy to check that this is a norm.
25

4 Rn as a normed space IB Analysis II
– We can also have the following norm on Rn:
‖x‖∞ = max{|xi| : 1≤i≤n}.
It is also easy to check that this is a norm.
– In general, we can deﬁne the p norm (for p≥ 1) by
‖x‖p =
(∑
|xi|p
)1/p
.
It is, however, not trivial to check the triangle inequality, and we will not
do this.
We can show that as p→∞ ,‖x‖p→‖ x‖∞, which justiﬁes our notation
above.
We also have some inﬁnite dimensional examples. Often, we can just extend our
notions on Rn to inﬁnite sequences with some care. We write RN for the set of
all inﬁnite real sequences (xk). This is a vector space with termwise addition
and scalar multiplication.
– Deﬁne
𝓁1 =
{
(xk)∈ RN :
∑
|xk|<∞
}
.
This is a linear subspace of RN. We deﬁne the norm by
‖(xk)‖1 =‖(xk)‖𝓁1 =
∑
|xk|.
– Similarly, we can deﬁne 𝓁2 by
𝓁2 =
{
(xk)∈ RN :
∑
x2
k <∞
}
.
The norm is deﬁned by
‖(xk)‖2 =‖(xk)‖𝓁2 =
(∑
x2
k
)1/2
.
We can also write this as
‖(xk)‖𝓁2 = lim
n→∞
‖(x1,··· ,xn)‖2.
So the triangle inequality for the Euclidean norm implies the triangle
inequality for 𝓁2.
– In general, for p≥ 1, we can deﬁne
𝓁p =
{
(xk)∈ RN :
∑
|xk|p <∞
}
with the norm
‖(xk)‖p =‖(xk)‖𝓁p =
(∑
|xk|p
)1/p
.
26

4 Rn as a normed space IB Analysis II
– Finally, we have 𝓁∞, where
𝓁∞ ={(xk)∈ RN : sup|xk|<∞},
with the norm
‖(xk)‖∞ =‖(xk)‖𝓁∞ = sup|xk|.
Finally, we can have examples where we look at function spaces, usually C([a,b ]),
the set of continuous real functions on [ a,b ].
– We can deﬁne the L1 norm by
‖f‖L1 =‖f‖1 =
∫ b
a
|f| dx.
– We can deﬁne L2 similarly by
‖f‖L2 =‖f‖2 =
(∫ b
a
f 2 dx
) 1
2
.
– In general, we can deﬁne Lp for p≥ 1 by
‖f‖Lp =‖f‖p =
(∫ b
a
fp dx
) 1
p
.
– Finally, we have L∞ by
‖f‖L∞ =‖f‖∞ = sup|f|.
This is also called the uniform norm, or the supremum norm.
Later, when we deﬁne convergence for general normed space, we will show
that convergence under the uniform norm is equivalent to uniform convergence.
To show thatL2 is actually a norm, we can use the Cauchy-Schwarz inequality
for integrals.
Lemma (Cauchy-Schwarz inequality (for integrals)). If f,g ∈C([a,b ]), f,g ≥ 0,
then ∫ b
a
fg dx≤
(∫ b
a
f 2 dx)
)1/2(∫ b
a
g2 dx
)1/2
.
Proof. If
∫b
a f 2 dx = 0, then f = 0 (since f is continuous). So the inequality
holds trivially.
Otherwise, let A2 =
∫b
a f 2 dx⁄= 0, B2 =
∫b
a g2 dx. Consider the function
φ(t) =
∫ b
a
(g−tf)2 dt≥ 0.
for every t. We can expand this as
φ(t) =t2A2− 2t
∫ b
a
gf dx +B2.
27

4 Rn as a normed space IB Analysis II
The conditions for a quadratic in t to be non-negative is exactly
(∫ b
a
gf dx
)2
−A2B2≤ 0.
So done.
Note that the way we deﬁned Lp is rather unsatisfactory. To deﬁne the 𝓁p
spaces, we ﬁrst have the norm deﬁned as a sum, and then 𝓁p to be the set of
all sequences for which the sum converges. However, to deﬁne the Lp space, we
restrict ourselves to C([0, 1]), and then deﬁne the norm. Can we just deﬁne,
say, L1 to be the set of all functions such that
∫ 1
0|f| dx exists? We could,
but then the norm would no longer be the norm, since if we have the function
f(x) =
{
1 x = 0.5
0 x⁄= 0.5, then f is integrable with integral 0, but is not identically
zero. So we cannot expand our vector space to be too large. To deﬁne Lp
properly, we need some more sophisticated notions such as Lebesgue integrability
and other fancy stuﬀ, which will be done in the IID Probability and Measure
course.
We have just deﬁned many norms on the same space Rn. These norms are
clearly not the same, in the sense that for many x,‖x‖1 and‖x‖2 have diﬀerent
values. However, it turns out the norms are all “equivalent” in some sense. This
intuitively means the norms are “not too diﬀerent” from each other, and give
rise to the same notions of, say, convergence and completeness.
A precise deﬁnition of equivalence is as follows:
Deﬁnition (Lipschitz equivalence of norms) . Let V be a (real) vector space.
Two norms‖·‖ ,‖·‖ ′ on V are Lipschitz equivalent if there are real constants
0<a<b such that
a‖x‖≤‖ x‖′≤b‖x‖
for all x∈V .
It is easy to show this is indeed an equivalence relation on the set of all norms
on V .
We will show that if two norms are equivalent, the “topological” properties of
the space do not depend on which norm we choose. For example, the norms will
agree on which sequences are convergent and which functions are continuous.
It is possible to reformulate the notion of equivalence in a more geometric
way. To do so, we need some notation:
Deﬁnition (Open ball). Let (V,‖·‖ ) be a normed space, a∈V , r> 0. The
open ball centered at a with radius r is
Br(a) ={x∈V :‖x− a‖<r}.
Then the requirement that a‖x‖≤‖ x‖′≤b‖x‖ for all x∈V is equivalent
to saying
B1/b(0)⊆B′
1(0)⊆B1/a(0),
where B′ is the ball with respect to ‖·‖ ′, while B is the ball with respect to
‖·‖ . Actual proof of equivalence is on the second example sheet.
28

4 Rn as a normed space IB Analysis II
Example. Consider R2. Then the norms ‖·‖ ∞ and‖·‖ 2 are equivalent. This
is easy to see using the ball picture:
where the blue ones are the balls with respect to ‖·‖ ∞ and the red one is the
ball with respect to ‖·‖ 2.
In general, we can consider Rn, again with‖·‖ 2 and‖·‖ ∞. We have
‖x‖∞≤‖ x‖2≤√n‖x‖∞.
These are easy to check manually. However, later we will show that in fact,
any two norms on a ﬁnite-dimensional vector space are Lipschitz equivalent.
Hence it is more interesting to look at inﬁnite dimensional cases.
Example. Let V =C([0, 1]) with the norms
‖f‖1 =
∫ 1
0
|f| dx, ‖f‖∞ = sup
[0,1]
|f|.
We clearly have the bound
‖f‖1≤‖f‖∞.
However, there is no constant b such that
‖f‖∞≤b‖f‖1
for all f. This is easy to show by constructing a sequence of functions fn by
x
y
1
1
n
where the width is 2
n and the height is 1. Then ‖fn‖∞ = 1 but‖fn‖1 = 1
n→ 0.
Example. Similarly, consider the space 𝓁2 =
{
(xn) :∑x2
n <∞
}
under the
regular 𝓁2 norm and the 𝓁∞ norm. We have
‖(xk)‖∞≤‖ (xk)‖𝓁2,
29

4 Rn as a normed space IB Analysis II
but there is no b such that
‖(xk)‖𝓁2≤b‖(xk)‖∞.
For example, we can consider the sequence xn = (1, 1,··· , 1, 0, 0,··· ), where the
ﬁrst n terms are 1.
So far in all our examples, out of the two inequalities, one holds and one does
not. Is it possible for both inequalities to not hold? The answer is yes. This is
an exercise on the second example sheet as well.
This is all we are going to say about Lipschitz equivalence. We are now going
to deﬁne convergence, and study the consequences of Lipschitz equivalence to
convergence.
Deﬁnition (Bounded subset). Let (V,‖·‖ ) be a normed space. A subset E⊆V
is bounded if there is some R> 0 such that
E⊆BR(0).
Deﬁnition (Convergence of sequence). Let (V,‖·‖ ) be a normed space. A
sequence (xk) in V converges to x∈V if‖xk− x‖→ 0 (as a sequence in R), i.e.
(∀ε> 0)(∃N)(∀k≥N)‖xk− x‖<ε.
These two deﬁnitions, obviously, depends on the chosen norm, not just the
vector space V . However, if two norms are equivalent, then they agree on what
is bounded and what converges.
Proposition. If‖·‖ and‖·‖ ′ are Lipschitz equivalent norms on a vector
space V , then
(i) A subsetE⊆V is bounded with respect to‖·‖ if and only if it is bounded
with respect to‖·‖ ′.
(ii) A sequencexk converges tox with respect to‖·‖ if and only if it converges
to x with respect to‖·‖ ′.
Proof.
(i) This is direct from deﬁnition of equivalence.
(ii) Say we have a,b such that a‖y‖≤‖ y‖′≤b‖y‖ for all y. So
a‖xk− x‖≤‖ xk− x‖′≤b‖xk− x‖.
So‖xk− x‖→ 0 if and only if ‖xk− x‖′→ 0. So done.
What if the norms are not equivalent? It is not surprising that there are
some sequences that converge with respect to one norm but not another. More
surprisingly, it is possible that a sequence converges to diﬀerent limits under
diﬀerent norms. This is, again, on the second example sheet.
We have some easy facts about convergence:
Proposition. Let (V,‖·‖ ) be a normed space. Then
(i) If xk→ x and xk→ y, then x = y.
30

4 Rn as a normed space IB Analysis II
(ii) If xk→ x, then axk→ax.
(iii) If xk→ x, yk→ y, then xk + yk→ x + y.
Proof.
(i) ‖x− y‖≤‖ x− xk‖ +‖xk− y‖→ 0. So ‖x− y‖ = 0. So x = y.
(ii) ‖axk−ax‖ =|a|‖xk− x‖→ 0.
(iii) ‖(xk + yk)− (x + y)‖≤‖ xk− x‖ +‖yk− y‖→ 0.
Proposition. Convergence in Rn (with respect to, say, the Euclidean norm) is
equivalent to coordinate-wise convergence, i.e. x(k)→ x if and only if x(k)
j →xj
for all j.
Proof. Fix ε> 0. Suppose x(k)→ x. Then there is some N such that for any
k≥N such that
‖x(k)− x‖2
2 =
n∑
j=1
(x(k)
j −xj)2 <ε.
Hence|x(k)
j −xj|<ε for all k≤N.
On the other hand, for any ﬁxed j, there is some Nj such thatk≥Nj implies
|x(k)
j −xj|< ε√n. So if k≥ max{Nj :j = 1,··· ,n}, then
‖x(k)− x‖2 =
(

n∑
j=1
(x(k)
j −xj)2
)

1
2
<ε.
So done
Another space we would like to understand is the space of continuous functions.
It should be clear that uniform convergence is the same as convergence under the
uniform norm, hence the name. However, there is no norm such that convergence
under the norm is equivalent to pointwise convergence, i.e. pointwise convergence
is not normable. In fact, it is not even metrizable. However, we will not prove
this.
We’ll now generalize the Bolzano-Weierstrass theorem to Rn.
Theorem (Bolzano-Weierstrass theorem in Rn). Any bounded sequence in Rn
(with, say, the Euclidean norm) has a convergent subsequence.
Proof. We induct on n. The n = 1 case is the usual Bolzano-Weierstrass on the
real line, which was proved in IA Analysis I.
Assume the theorem holds in Rn−1, and let x(k) = (x(k)
1 ,··· ,x (k)
n ) be a
bounded sequence in Rn. Then let y(k) = (x(k)
1 ,··· ,x (k)
n−1). Since for any k, we
know that
‖y(k)‖2 +|x(k)
n |2 =‖x(k)‖2,
it follows that both (y(k)) and (x(k)
n ) are bounded. So by the induction hypothesis,
there is a subsequence (kj) of (k) and some y∈ Rn−1 such that y(kj )→ y. Also,
31

4 Rn as a normed space IB Analysis II
by Bolzano-Weierstrass in R, there is a further subsequence ( x
(kj𝓁 )
n ) of (x(kj )
n )
that converges to, say, yn∈ R. Then we know that
x(kj𝓁 )→ (y,yn).
So done.
Note that this is generally not true for normed spaces. Finite-dimensionality
is important for both of these results.
Example. Consider (𝓁∞,‖·‖ ∞). We let e(k)
j = δjk be the sequence with 1
in the kth component and 0 in other components. Then e(k)
j → 0 for all ﬁxed
j, and hence e(k) converges componentwise to the zero element 0 = (0 , 0,··· ).
However,e(k) does not converge to the zero element since ‖e(k)− 0‖∞ = 1 for
all k. Also, this is bounded but does not have a convergent subsequence for the
same reasons.
We know that all ﬁnite dimensional vector spaces are isomorphic to Rn
as vector spaces for some n, and we will later show that all norms on ﬁnite
dimensional spaces are equivalent. This means every ﬁnite-dimensional normed
space satisﬁes the Bolzano-Weierstrass property. Is the converse true? If a
normed vector space satisﬁes the Bolzano-Weierstrass property, must it be ﬁnite
dimensional? The answer is yes, and the proof is in the example sheet.
Example. Let C([0, 1]) have the‖·‖ L2 norm. Consider fn(x) = sin 2nπx. We
know that
‖fn‖2
L2 =
∫ 1
0
|fn|2 = 1
2.
So it is bounded. However, it doesn’t have a convergent subsequence. If it did,
sayfnj→f in L2, then we must have
‖fnj−fnj+1‖2→ 0.
However, by direct calculation, we know that
‖fnj−fnj+1‖2 =
∫ 1
0
(sin 2njπx− sin 2nj+1πx)2 = 1.
Note that the same argument shows also that the sequence ( sin 2nπx) has no
subsequence that converges pointwise on [0, 1]. To see this, we need the result
that if (fj) is a sequence in C([0, 1]) that is uniformly bounded with fj→ f
pointwise, then fj converges to f under the L2 norm. However, we will not
be able to prove this (in a nice way) without Lebesgue integration from IID
Probability and Measure.
4.2 Cauchy sequences and completeness
Deﬁnition (Cauchy sequence). Let (V,‖·‖ ) be a normed space. A sequence
(x(k)) in V is a Cauchy sequence if
(∀ε)(∃N)(∀n,m≥N)‖x(n)− x(m)‖<ε.
32

4 Rn as a normed space IB Analysis II
Deﬁnition (Complete normed space). A normed space (V,‖·‖ ) is complete if
every Cauchy sequence converges to an element in V .
We’ll start with some easy facts about Cauchy sequences and complete spaces.
Proposition. Any convergent sequence is Cauchy.
Proof. If xk→ x, then
‖xk− x𝓁‖≤‖ xk− x‖ +‖x𝓁− x‖→ 0 as k,𝓁→∞.
Proposition. A Cauchy sequence is bounded.
Proof. By deﬁnition, there is some N such that for all n≥N, we have‖xN−
xn‖< 1. So ‖xn‖< 1 +‖xN‖ for n≥N. So, for all n,
‖xn‖≤ max{‖x1‖,··· ,‖xN−1‖, 1 +‖xN‖}.
Proposition. If a Cauchy sequence has a subsequence converging to an element
x, then the whole sequence converges to x.
Proof. Suppose xkj→ x. Since ( xk) is Cauchy, givenε> 0, we can choose an
N such that‖xn− xm‖< ε
2 for all n,m≥N. We can also choose j0 such that
kj0≥n and‖xkj0− x‖< ε
2. Then for any n≥N, we have
‖xn− x‖≤‖ xn− xkj0‖ +‖x− xkj0‖<ε.
Proposition. If‖·‖ ′ is Lipschitz equivalent to‖·‖ onV , then (xk) is Cauchy
with respect to‖·‖ if and only if ( xk) is Cauchy with respect to ‖·‖ ′. Also,
(V,‖·‖ ) is complete if and only if ( V,‖·‖ ′) is complete.
Proof. This follows directly from deﬁnition.
Theorem. Rn (with the Euclidean norm, say) is complete.
Proof. The important thing is to know this is true for n = 1, which we have
proved from Analysis I.
If (xk) is Cauchy in Rn, then (x(k)
j ) is a Cauchy sequence of real numbers for
eachj∈{ 1,··· ,n}. By the completeness of the reals, we know thatxk
j→xj∈ R
for some x. So xk→x = (x1,··· ,xn) since convergence in Rn is equivalent to
componentwise convergence.
Note that the spaces 𝓁1,𝓁 2,𝓁∞ are all complete with respect to the standard
norms. Also, C([0, 1]) is complete with respect to ‖·‖ ∞, since uniform Cauchy
convergence implies uniform convergence, and the uniform limit of continuous
functions is continuous. However, C([0, 1]) with the L1 or L2 norms are not
complete (see example sheet).
The incompleteness of L1 tells us that C([0, 1]) is not large enough to to be
complete under the L1 or L2 norm. In fact, the space of Riemann integrable
functions, say R([0, 1]), is the natural space for the L1 norm, and of course
containsC([0, 1]). As we have previously mentioned, this time R([0, 1]) is too
large for‖·‖ to be a norm, since
∫ 1
0|f| dx = 0 does not imply f = 0. This is a
problem we can solve. We just have to take the equivalence classes of Riemann
integrable functions, where f and g are equivalent if
∫ 1
0|f−g| dx = 0. But still,
33

4 Rn as a normed space IB Analysis II
L1 is not complete on R([0, 1])/∼. This is a serious problem in the Riemann
integral. This eventually lead to the Lebesgue integral, which generalizes the
Riemann integral, and gives a complete normed space.
Note that when we quotient our R([0, 1]) by the equivalence relation f∼g
if
∫ 1
0|f−g| dx = 0, we are not losing too much information about our functions.
We know that for the integral to be zero, f−g cannot be non-zero at a point of
continuity. Hence they agree on all points of continuities. We also know that
by Lebesgue’s theorem, the set of points of discontinuity has Lebesgue measure
zero. So they disagree on at most a set of Lebesgue measure zero.
Example. Let
V ={(xn)∈ RN :xj = 0 for all but ﬁnitely many j}.
Take the supremum norm ‖ · ‖∞ on V . This is a subspace of 𝓁∞ (and is
sometimes denoted 𝓁0). Then ( V,‖·‖ ∞) is not complete. We deﬁne x(k) =
(1, 1
2, 1
3,··· , 1
k, 0, 0,··· ) for k = 1, 2, 3,··· . Then this is Cauchy, since
‖x(k)−x(𝓁)‖ = 1
min{𝓁,k} + 1→ 0,
but it is not convergent in V . If it actually converged to some x, then x(k)
j →xj.
So we must have xj = 1
j , but this sequence not in V .
We will later show that this is because V is not closed, after we deﬁne what
it means to be closed.
Deﬁnition (Open set). Let (V,‖·‖ ) be a normed space. A subspace E⊆V is
open in V if for any y∈E, there is some r> 0 such that
Br(y) ={x∈V :‖x− y‖<r}⊆ E.
We ﬁrst check that the open ball is open.
Proposition. Br(y)⊆V is an open subset for all r> 0, y∈V .
Proof. Let x∈Br(y). Let ρ =r−‖ x− y‖> 0. Then Bρ(x)⊆Br(y).
x
y
Deﬁnition (Limit point). Let (V,‖·‖ ) be a normed space, E⊆V . A point
y∈V is a limit point of E if there is a sequence ( xk) in E with xk⁄= y for all k
and xk→ y.
(Some people allow xk = y, but we will use this deﬁnition in this course)
Example. Let V = R, E = (0, 1). Then 0, 1 are limit points of E. The set of
all limit points is [0, 1].
If E′ = (0, 1)∪{ 2}. Then the set of limit points of E′ is still [0, 1].
34

4 Rn as a normed space IB Analysis II
There is a nice result characterizing whether a set contains all its limit points.
Proposition. Let E⊆V . Then E contains all of its limit points if and only if
V\E is open in V .
Using this proposition, we deﬁne the following:
Deﬁnition (Closed set). Let (V,‖·‖ ) be a normed space. Then E⊆ V is
closed if V\E is open, i.e. E contains all its limit points.
Note that sets can be both closed or open; or neither closed nor open.
Before we prove the proposition, we ﬁrst have a lemma:
Lemma. Let (V,‖·‖ ) be a normed space, E any subset of V . Then a point
y∈V is a limit point of E if and only if
(Br(y)\{ y})∩E⁄=∅
for every r.
Proof. (⇒) If y is a limit point of E, then there exists a sequence ( xk)∈ E
with xk⁄= y for all k and xk→ y. Then for every r, for suﬃciently large k,
xk∈Br(y). Since xk⁄={y} and xk∈E, the result follows.
(⇐) For each k, let r = 1
k. By assumption, we have some xk∈ (B 1
k
(y)\
{y})∩E. Then xk→ y, xk⁄= y and xk∈E. So y is a limit point of E.
Now we can prove our proposition.
Proposition. Let E⊆V . Then E contains all of its limit points if and only if
V\E is open in V .
Proof. (⇒) Suppose E contains all its limit points. To show V\E is open,
we let y∈ V \E. So y is not a limit point of E. So for some r, we have
(Br(y)\{ y})∩E =∅. Hence it follows that Br(y)⊆V\E (since y⁄∈E).
(⇐) Suppose V\E is open. Let y∈V\E. Since V\E is open, there is
some r such that Br(y)⊆V\E. By the lemma, y is not a limit point of E. So
all limit points of E are in E.
4.3 Sequential compactness
In general, there are two diﬀerent notions of compactness — “sequential com-
pactness” and just “compactness”. However, in normed spaces (and metric
spaces, as we will later encounter), these two notions are equivalent. So we will
be lazy and just say “compactness” as opposed to “sequential compactness”.
Deﬁnition ((Sequentially) compact set). Let V be a normed vector space. A
subset K⊆V is said to be compact (or sequentially compact) if every sequence
in K has a subsequence that converges to a point in K.
There are things we can immediately know about the spaces:
Theorem. Let (V,‖·‖ ) be a normed vector space, K⊆V a subset. Then
(i) If K is compact, then K is closed and bounded.
35

4 Rn as a normed space IB Analysis II
(ii) IfV is Rn (with, say, the Euclidean norm), then ifK is closed and bounded,
then K is compact.
Proof.
(i) Let K be compact. Boundedness is easy: if K is unbounded, then we can
generate a sequence xk such that‖xk‖→∞ . Then this cannot have a
convergent subsequence, since any subsequence will also be unbounded,
and convergent sequences are bounded. So K must be bounded.
To show K is closed, let y be a limit point of K. Then there is some
yk∈K such that yk→ y. Then by compactness, there is a subsequence
of yk converging to some point in K. But any subsequence must converge
to y. So y∈K.
(ii) Let K be closed and bounded. Let xk be a sequence in K. Since V = Rn
and K is bounded, ( xk) is a bounded sequence in Rn. So by Bolzano-
Weierstrass, this has a convergent subsequence xkj. By closedness of K,
we know that the limit is in K. So K is compact.
4.4 Mappings between normed spaces
We are now going to look at functions between normed spaces, and see if they
are continuous.
Let (V,‖·‖ ), (V′,‖·‖ ′) be normed spaces, and let E⊆ K be a subset,
and f :E→V′ a mapping (which is just a function, although we reserve the
terminology “function” or “functional” for when V′ = R).
Deﬁnition (Continuity of mapping) . Let y ∈ E. We say f : E → V′ is
continuous at y if for all ε> 0, there is δ >0 such that the following holds:
(∀x∈E)‖x− y‖V <δ ⇒‖f(x)−f(y)‖V ′ <ε.
Note that x∈ E and‖x− y‖ < δis equivalent to saying x∈ Bδ(y)∩E.
Similarly,‖f(x)−f(y)‖<ε is equivalent to f(x)∈Bε(f(y)). In other words,
x∈ f−1(Bε(f(y))). So we can rewrite this statement as there is some δ >0
such that
E∩Bδ(y)⊆f−1(Bε(f(y))).
We can use this to provide an alternative characterization of continuity.
Theorem. Let (V,‖·‖ ), (V′,‖·‖ ′) be normed spaces, E⊆ V , f : E→ V′.
Then f is continuous at y∈E if and only if for any sequence yk→ y in E, we
havef(yk)→f(y).
Proof. (⇒) Suppose f is continuous at y∈E, and that yk→ y. Given ε> 0,
by continuity, there is some δ >0 such that
Bδ(y)∩E⊆f−1(Bε(f(y))).
For suﬃciently large k, yk∈Bδ(y)∩E. So f(yk)∈Bε(f(y)), or equivalently,
|f(yk)−f(y)|<ε.
So done.
36

4 Rn as a normed space IB Analysis II
(⇐) If f is not continuous at y, then there is some ε> 0 such that for any k,
we have
B 1
k
(y)⁄⊆f−1(Bε(f(y))).
Choose yk∈ B 1
k
(y)\f−1(Bε(f(y))). Then yk→ y, yk∈ E, but ‖f(yk)−
f(y)‖≥ ε, contrary to the hypothesis.
Deﬁnition (Continuous function). f :E→V′ is continuous if f is continuous
at every point y∈E.
Theorem. Let (V,‖·‖ ) and (V′,‖·‖ ′) be normed spaces, and K a compact
subset of V , and f :V →V′ a continuous function. Then
(i) f(K) is compact in V′
(ii) f(K) is closed and bounded
(iii) If V′ = R, then the function attains its supremum and inﬁmum, i.e. there
is some y1, y2∈K such that
f(y1) = sup{f(y) : y∈K}, f (y2) = inf{f(y) : y∈K}.
Proof.
(i) Let (xk) be a sequence in f(K) with xk = f(yk) for some yk∈ K. By
compactness of K, there is a subsequence ( ykj) such that ykj→ y. By the
previous theorem, we know that f(yjk)→f(y). So xkj→f(y)∈f(K).
So f(K) is compact.
(ii) This follows directly from ( i), since every compact space is closed and
bounded.
(iii) If F is any bounded subset of R, then either supF∈F or supF is a limit
point of F (or both), by deﬁnition of the supremum. If F is closed and
bounded, then any limit point must be in F . So supF∈F . Applying this
fact to F =f(K) gives the desired result, and similarly for inﬁmum.
Finally, we will end the chapter by proving that any two norms on a ﬁnite
dimensional space are Lipschitz equivalent. The key lemma is the following:
Lemma. Let V be an n-dimensional vector space with a basis {v1,··· , vn}.
Then for any x∈V , write x =∑n
j=1xjvj, withxj∈ R. We deﬁne the Euclidean
norm by
‖x‖2 =
(∑
x2
j
) 1
2
.
Then this is a norm, and S ={x∈V :‖x‖2 = 1} is compact in (V,‖·‖ 2).
After we show this, we can easily show that every other norm is equivalent
to this norm.
This is not hard to prove, since we know that the unit sphere in Rn is
compact, and we can just pass our things on to Rn.
37

4 Rn as a normed space IB Analysis II
Proof.‖·‖ 2 is well-deﬁned since x1,··· ,xn are uniquely determined by x (by
(a certain) deﬁnition of basis). It is easy to check that ‖·‖ 2 is a norm.
Given a sequence x(k) in S, if we write x(k) =∑n
j=1x(k)
j vj. We deﬁne the
following sequence in Rn:
˜x(k) = (x(k)
1 ,··· ,x (k)
n )∈ ˜S ={˜x∈ Rn :‖˜x‖Euclid = 1}.
As ˜S is closed and bounded in Rn under the Euclidean norm, it is compact.
Hence there exists a subsequence ˜x(kj ) and ˜x∈ ˜S such that‖˜x(kj )− ˜x‖Euclid→ 0.
This says that x =∑n
j=1xjvj∈S, and‖xkj− x‖2→ 0. So done.
Theorem. Any two norms on a ﬁnite dimensional vector space are Lipschitz
equivalent.
The idea is to pick a basis, and prove that any norm is equivalent to ‖·‖ 2.
To show that an arbitrary norm‖·‖ is equivalent to‖·‖ 2, we have to show
that for any‖x‖, we have
a‖x‖2≤‖ x‖≤ b‖x‖2.
We can divide by‖x‖2 and obtain an equivalent requirement:
a≤
‖‖‖‖
x
‖x‖2
‖‖‖‖≤b.
We know that any x/‖x‖2 lies in the unit sphere S ={x∈V :‖x‖2 = 1}. So
we want to show that the image of ‖·‖ is bounded. But we know that S is
compact. So it suﬃces to show that ‖·‖ is continuous.
Proof. Fix a basis{v1,··· , vn} for V , and deﬁne‖·‖ 2 as in the lemma above.
Then‖·‖ 2 is a norm on V , and S ={x∈V :‖x‖2 = 1}, the unit sphere, is
compact by above.
To show that any two norms are equivalent, it suﬃces to show that if ‖·‖ is
any other norm, then it is equivalent to ‖·‖ 2, since equivalence is transitive.
For any
x =
n∑
j=1
xjvj,
we have
‖x‖ =
‖‖‖‖‖‖
n∑
j=1
xjvj
‖‖‖‖‖‖
≤
∑
|xj|‖vj‖
≤‖ x‖2
(

n∑
j=1
‖vj‖2
)

1
2
by the Cauchy-Schwarz inequality. So‖x‖≤ b‖x‖2 for b =
(∑‖vj‖2) 1
2 .
To ﬁnda such that‖x‖≥ a‖x‖2, consider‖·‖ : (S,‖·‖ 2)→ R. By above,
we know that
‖x− y‖≤ b‖x− y‖2
38

4 Rn as a normed space IB Analysis II
By the triangle inequality, we know that
⏐⏐‖x‖−‖ y‖
⏐⏐≤‖ x− y‖. So when x is
close to y under‖·‖ 2, then‖x‖ and‖y‖ are close. So ‖·‖ : (S,‖·‖ 2)→ R
is continuous. So there is some x0∈ S such that‖x0‖ = infx∈S‖x‖ =a, say.
Since‖x‖> 0, we know that‖x0‖> 0. So ‖x‖≥ a‖x‖2 for all x∈V .
The key to the proof is the compactness of the unit sphere of ( V,‖·‖ ).
On the other hand, compactness of the unit sphere also characterizes ﬁnite
dimensionality. As you will show in the example sheets, if the unit sphere of a
space is compact, then the space must be ﬁnite-dimensional.
Corollary. Let (V,‖·‖ ) be a ﬁnite-dimensional normed space.
(i) The Bolzano-Weierstrass theorem holds for V , i.e. any bounded sequence
sequence in V has a convergent subsequence.
(ii) A subset of V is compact if and only if it is closed and bounded.
Proof. If a subset is bounded in one norm, then it is bounded in any Lipschitz
equivalent norm. Similarly, if it converges to x in one norm, then it converges to
x in any Lipschitz equivalent norm.
Since these results hold for the Euclidean norm ‖·‖ 2, it follows that they
hold for arbitrary ﬁnite-dimensional vector spaces.
Corollary. Any ﬁnite-dimensional normed vector space (V,‖·‖ ) is complete.
Proof. This is true since if a space is complete in one norm, then it is complete
in any Lipschitz equivalent norm, and we know that Rn under the Euclidean
norm is complete.
39

5 Metric spaces IB Analysis II
5 Metric spaces
We would like to extend our notions such as convergence, open and closed
subsets, compact subsets and continuity from normed spaces to more general
sets. Recall that when we deﬁned these notions, we didn’t really use the vector
space structure of a normed vector space much. Moreover, we mostly deﬁned
these things in terms of convergence of sequences. For example, a space is closed
if it contains all its limits, and a space is open if its complement is closed.
So what do we actually need in order to deﬁne convergence, and hence all
the notions we’ve been using? Recall we deﬁne xk→ x to mean‖xk− x‖→ 0
as a sequence in R. What is ‖xk− x‖ really about? It is measuring the distance
between xk and x. So what we really need is a measure of distance.
To do so, we can deﬁne a distance functiond :V×V → R byd(x,y ) =‖x−y‖.
Then we can deﬁne xk→x to mean d(xk,x )→ 0.
Hence, given any function d : V ×V → R, we can deﬁne a notion of
“convergence” as above. However, we want this to be well-behaved. In particular,
we would want the limits of sequences to be unique, and any constant sequence
xk =x should converge to x.
We will come up with some restrictions on what d can be based on these
requirements.
We can look at our proof of uniqueness of limits (for normed spaces), and
see what properties of d we used. Recall that to prove the uniqueness of limits,
we ﬁrst assume that xk→x and xk→y. Then we noticed
‖x−y‖≤‖ x−xk‖ +‖xk−y‖→ 0,
and hence‖x−y‖ = 0. So x =y. We can reformulate this argument in terms of
d. We ﬁrst start with
d(x,y )≤d(x,xk) +d(xk,y ).
To obtain this equation, we are relying on the triangle inequality. So we would
wantd to satisfy the triangle inequality.
After obtaining this, we know that d(xk,y ) → 0, since this is just the
deﬁnition of convergence. However, we do not immediately know d(x,xk)→ 0,
since we are given a fact aboutd(xk,x ), notd(x,xk). Hence we need the property
that d(xk,x ) =d(x,xk). This is symmetry.
Combining this, we know that
d(x,y )≤ 0.
From this, we want to say that in fact, d(x,y ) = 0, and thus x = y. Hence
we need the property that d(x,y )≥ 0 for all x,y , and that d(x,y ) = 0 implies
x =y.
Finally, to show that a constant sequence has a limit, suppose xk =x for all
k∈ N. Then we know that d(x,xk) =d(x,x ) should tend to 0. So we must have
d(x,x ) = 0 for all x.
We will use these properties to deﬁne metric spaces.
5.1 Preliminary deﬁnitions
Deﬁnition (Metric space). Let X be any set. A metric on X is a function
d :X×X→ R that satisﬁes
40

5 Metric spaces IB Analysis II
– d(x,y )≥ 0 with equality iﬀ x =y (non-negativity)
– d(x,y ) =d(y,x ) (symmetry)
– d(x,y )≤d(x,z ) +d(z,y ) (triangle inequality)
The pair (X,d ) is called a metric space.
We have seen that we can deﬁne convergence in terms of a metric. Hence,
we can also deﬁne open subsets, closed subsets, compact spaces, continuous
functions etc. for metric spaces, in a manner consistent with what we had for
normed spaces. Moreover, we will show that many of our theorems for normed
spaces are also valid in metric spaces.
Example.
(i) Rn with the Euclidean metric is a metric space, where the metric is deﬁned
by
d(x,y ) =‖x−y‖ =
√∑
(xj−yj)2.
(ii) More generally, if ( V,‖·‖ ) is a normed space, then d(x,y ) = ‖x−y‖
deﬁnes a metric on V .
(iii) Discrete metric: let X be any set, and deﬁne
d(x,y ) =
{
0 x =y
1 x⁄=y.
(iv) Given a metric space ( X,d ), we deﬁne
g(x,y ) = min{1,d (x,y )}.
Then this is a metric on X. Similarly, if we deﬁne
h(x,y ) = d(x,y )
1 +d(x,y )
is also a metric on X. In both cases, we obtain a bounded metric.
The axioms are easily shown to be satisﬁed, apart from the triangle
inequality. So let’s check the triangle inequality for h. We’ll use a general
fact that for numbers a,c≥ 0,b,d> 0 we have
a
b≤ c
d⇔ a
a +b≤ c
c +d.
Based on this fact, we can start with
d(x,y )≤d(x,z ) +d(z,y ).
Then we obtain
d(x,y )
1 +d(x,y )≤ d(x,z ) +d(z,y )
1 +d(x,z ) +d(z,y )
= d(x,z )
1 +d(x,z ) +d(z,y ) + d(z,y )
1 +d(x,z ) +d(z,y )
≤ d(x,z )
1 +d(x,z ) + d(z,y )
1 +d(z,y ).
So done.
41

5 Metric spaces IB Analysis II
We can also extend the notion of Lipschitz equivalence to metric spaces.
Deﬁnition (Lipschitz equivalent metrics). Metrics d,d′ on a set X are said to
be Lipschitz equivalent if there are (positive) constants A,B such that
Ad(x,y )≤d′(x,y )≤Bd(x,y )
for all x,y∈X.
Clearly, any Lipschitz equivalent norms give Lipschitz equivalent metrics. Any
metric coming from a norm in Rn is thus Lipschitz equivalent to the Euclidean
metric. We will later show that two equivalent norms induce the same topology.
In some sense, Lipschitz equivalent norms are indistinguishable.
Deﬁnition (Metric subspace). Given a metric space (X,d ) and a subset Y ⊆X,
the restriction d|Y×Y → R is a metric on Y . This is called the induced metric
or subspace metric.
Note that unlike vector subspaces, we do not require our subsets to have any
structure. We can take any subset of X and get a metric subspace.
Example. Any subspace of Rn is a metric space with the Euclidean metric.
Deﬁnition (Convergence). Let (X,d ) be a metric space. A sequence xn∈X is
said to converge to x if d(xn,x )→ 0 as a real sequence. In other words,
(∀ε)(∃K)(∀k>K )d(xk,x )<ε.
Alternatively, this says that given anyε, for suﬃciently largek, we getxk∈Bε(x).
Again, Br(a) is the open ball centered at a with radius r, deﬁned as
Br(a) ={x∈X :d(x,a )<r}.
Proposition. The limit of a convergent sequence is unique.
Proof. Same as that of normed spaces.
Note that notions such as convergence, open and closed subsets and continuity
of mappings all make sense in an even more general setting called topological
spaces. However, in this setting, limits of convergent sequences can fail to be
unique. We will not worry ourselves about these since we will just focus on
metric spaces.
5.2 Topology of metric spaces
We will deﬁne open subsets of a metric space in exactly the same way as we did
for normed spaces.
Deﬁnition (Open subset). Let (X,d ) be a metric space. A subset U⊆X is
open if for every y∈U, there is some r> 0 such that Br(y)⊆U.
42

5 Metric spaces IB Analysis II
This means we can write any open U as a union of open balls:
U =
⋃
y∈U
Br(y)(y)
for appropriate choices of r(y) for every y.
It is easy to check that every open ball Br(y) is an open set. The proof is
exactly the same as what we had for normed spaces.
Note that two diﬀerent metrics d,d′ on the same set X may give rise to the
same collection of open subsets.
Example. Lipschitz equivalent metrics give rise to the same collection of open
sets, i.e. if d,d′ are Lipschitz equivalent, then a subset U ⊆ X is open with
respect to d if and only if it is open with respect to d′. Proof is left as an easy
exercise.
The converse, however, is not necessarily true.
Example. Let X = R, d(x,y ) =|x−y| and d′(x,y ) = min{1,|x−y|}. It is
easy to check that these are not Lipschitz equivalent, but they induce the same
set collection of open subsets.
Deﬁnition (Topology). Let (X,d ) be a metric space. The topology on (X,d ) is
the collection of open subsets of X. We say it is the topology induced by the
metric.
Deﬁnition (Topological notion). A notion or property is said to be a topological
notion or property if it only depends on the topology, and not the metric.
We will introduce a useful terminology before we go on:
Deﬁnition (Neighbourhood). Given a metric space X and a point x∈X, a
neighbourhood of x is an open set containing x.
Some people do not require the set to be open. Instead, it requires a
neighbourhood to be a set that contains an open subset that contains x, but
this is too complicated, and we could as well work with open subsets directly.
Clearly, being a neighbourhood is a topological property.
Proposition. Let (X,d ) be a metric space. Then xk→x if and only if for every
neighbourhood V of x, there exists some K such that xk∈ V for all k≥ K.
Hence convergence is a topological notion.
Proof. (⇒) Suppose xk→X, and let V be any neighbourhood of x. Since V
is open, by deﬁnition, there exists some ε such that Bε(x)⊆V . By deﬁnition
of convergence, there is some K such that xk∈ Bε(x) for k≥ K. So xk∈ V
wheneverk≥K.
(⇒) Since every open ball is a neighbourhood, this direction follows directly
from deﬁnition.
Theorem. Let (X,d ) be a metric space. Then
(i) The union of any collection of open sets is open
(ii) The intersection of ﬁnitely many open sets is open.
43

5 Metric spaces IB Analysis II
(iii) ∅ and X are open.
Proof.
(i) Let U = ⋃
αVα, where each Vα is open. If x∈ U, then x∈ Vα for
some α. Since Vα is open, there exists δ >0 such that Bδ(x)⊆ Vα. So
Bδ(x)⊆⋃
αVα =U. So U is open.
(ii) Let U =⋂n
i=1Vα, where each Vα is open. If x∈ V , then x∈ Vi for all
i = 1,··· ,n . So∃δi > 0 with Bδi(x)⊆Vi. Take δ = min{δ1,··· ,δn}. So
Bδ(x)⊆Vi for all i. So Bδ(x)⊆V . So V is open.
(iii) ∅ satisﬁes the deﬁnition of an open subset vacuously. X is open since for
anyx, B1(x)⊆X.
This theorem is not important in this course. However, this will be a key
deﬁning property we will use when we deﬁne topological spaces in IB Metric and
Topological Spaces.
We can now deﬁne closed subsets and characterize them using open subsets,
in exactly the same way as for normed spaces.
Deﬁnition (Limit point). Let (X,d ) be a metric space and E⊆X. A point
y∈X is a limit point of E if there exists a sequence xk∈E, xk⁄=y such that
xk→y.
Deﬁnition (Closed subset). A subset E⊆X is closed if E contains all its limit
points.
Proposition. A subset is closed if and only if its complement is open.
Proof. Exactly the same as that of normed spaces. It is useful to observe that
y∈X is a limit point of E if and only if (Br(y)\{y})∩E⁄=∅ for all r> 0.
We can write down an analogous theorem for closed sets:
Theorem. Let (X,d ) be a metric space. Then
(i) The intersection of any collection of closed sets is closed
(ii) The union of ﬁnitely many closed sets is closed.
(iii) ∅ and X are closed.
Proof. By taking complements of the result for open subsets.
Proposition. Let (X,d ) be a metric space and x∈X. Then the singleton {x}
is a closed subset, and hence any ﬁnite subset is closed.
Proof. Let y∈X\{x}. So d(x,y )> 0. Then Bd(y,x)(x)⊆X\{x}. So X\{x}
is open. So {x} is closed.
Alternatively, since{x} has no limit points, it contains all its limit points.
So it is closed.
44

5 Metric spaces IB Analysis II
5.3 Cauchy sequences and completeness
Deﬁnition (Cauchy sequence). Let (X,d ) be a metric space. A sequence ( xn)
in X is Cauchy if
(∀ε)(∃N)(∀n,m≥N)d(xn,xm)<ε.
Proposition. Let (X,d ) be a metric space. Then
(i) Any convergent sequence is Cauchy.
(ii) If a Cauchy sequence has a convergent subsequence, then the original
sequence converges to the same limit.
Proof.
(i) If xk→x, then
d(xm,xn)≤d(xm,x ) +d(xn,x )→ 0
as m,n→∞ .
(ii) Suppose xkj→ x. Since ( xk) is Cauchy, given ε >0, we can choose an
N such that d(xn,xm)< ε
2 for all n,m≥N. We can also choose j0 such
that kj0≥n and d(xkj0,x )< ε
2. Then for any n≥N, we have
d(xn,x )≤d(xn,xkj0 ) +d(x,xkj0 )<ε.
Deﬁnition (Complete metric space). A metric space (X,d ) is complete if all
Cauchy sequences converge to a point in X.
Example. Let X = Rn with the Euclidean metric. Then X is complete.
It is easy to produce incomplete metric spaces. Since arbitrary subsets of
metric spaces are subspaces, we can just remove some random elements to make
it incomplete.
Example. Let X = (0, 1) ⊆ R with the Euclidean metric. Then this is
incomplete, since
( 1
k
)
is Cauchy but has no limit in X.
Similarly,X = R\{ 0} is incomplete. Note, however, that it is possible to
construct a metric d′ on X = R\{ 0} such that d′ induces the same topology on
X, but makes X complete. This shows that completeness is not a topological
property. The actual construction is left as an exercise on the example sheet.
Example. We can create an easy example of an incomplete metric on Rn. We
start by deﬁning h : Rn→ Rn by
h(x) = x
1 +‖x‖,
where‖·‖ is the Euclidean norm. We can check that this is injective: if
h(x) =h(y), taking the norm gives
‖x‖
1 +‖x‖ = ‖y‖
1 +‖y‖.
45

5 Metric spaces IB Analysis II
So we must have‖x‖ =‖y‖, i.e. x =y. So h(x) =h(y) implies x =y.
Now we deﬁne
d(x,y ) =‖h(x)−h(y)‖.
It is an easy check that this is a metric on Rn.
In fact, we can show that h : Rn→B1(0), and h is a homeomorphism (i.e.
continuous bijection with continuous inverse) between Rn and the unit ball
B1(0), both with the Euclidean metric.
To show that this metric is incomplete, we can consider the sequence xk =
(k− 1)e1, where e1 = (1, 0, 0,··· , 0) is the usual basis vector. Then ( xk) is
Cauchy in (Rn,d ). To show this, ﬁrst note that
h(xk) =
(
1− 1
k
)
e1.
Hence we have
d(xn,xm) =‖h(xn)−h(xm)‖ =
⏐⏐⏐⏐
1
n− 1
m
⏐⏐⏐⏐→ 0.
So it is Cauchy. To show it does not converge in ( Rn,d ), suppose d(xk,x )→ 0
for some x. Then since
d(xk,x ) =‖h(xk)−h(x)‖≥
⏐⏐‖h(xk)‖−‖ h(x)‖
⏐⏐,
We must have
‖h(x)‖ = lim
k→∞
‖h(xk)‖ = 1.
However, there is no element with ‖h(x)‖ = 1.
What is happening in this example, is that we are pulling in the whole Rn in
to the unit ball. Then under this norm, a sequence that “goes to inﬁnity” in the
usual norm will be Cauchy in this norm, but we have nothing at inﬁnity for it
to converge to.
Suppose we have a complete metric space ( X,d ). We know that we can
form arbitrary subspaces by taking subsets of X. When will this be complete?
Clearly it has to be closed, since it has to include all its limit points. It turns it
closedness is a suﬃcient condition.
Theorem. Let (X,d ) be a metric space, Y ⊆X any subset. Then
(i) If (Y,d|Y×Y ) is complete, then Y is closed in X.
(ii) If (X,d ) is complete, then (Y,d|Y×Y ) is complete if and only if it is closed.
Proof.
(i) Let x∈ X be a limit point of Y . Then there is some sequence xk→ x,
where each xk∈ Y . Since ( xk) is convergent, it is a Cauchy sequence.
Hence it is Cauchy in Y . By completeness of Y , (xk) has to converge to
some point in Y . By uniqueness of limits, this limit must be x. So x∈Y .
So Y contains all its limit points.
(ii) We have just showed that if Y is complete, then it is closed. Now suppose
Y is closed. Let (xk) be a Cauchy sequence in Y . Then (xk) is Cauchy in
X. Since X is complete, xk→x for some x∈X. Since x is a limit point
of Y , we must have x∈Y . So xk converges in Y .
46

5 Metric spaces IB Analysis II
5.4 Compactness
Deﬁnition ((Sequential) compactness). A metric space (X,d ) is (sequentially)
compact if every sequence in X has a convergent subsequence.
A subset K⊆X is said to be compact if ( K,d|K×K) is compact. In other
words,K is compact if every sequence in K has a subsequence that converges to
some point in K.
Note that when we say every sequence has a convergent subsequence, we
do not require it to be bounded. This is unlike the statement of the Bolzano-
Weierstrass theorem. In particular, R is not compact.
It follows from deﬁnition that compactness is a topological property, since it
is deﬁned in terms of convergence, and convergence is deﬁned in terms of open
sets.
The following theorem relates completeness with compactness.
Theorem. All compact spaces are complete and bounded.
Note that X is bounded iﬀ X⊆ Br(x0) for some r∈ R,x 0∈ X (or X is
empty).
Proof. Let (X,d ) be a compact metric space. Let ( xk) be Cauchy in X. By
compactness, it has some convergent subsequence, say xkj→x. So xk→x. So
it is complete.
If (X,d ) is not bounded, by deﬁnition, for any x0, there is a sequence (xk)
such that d(xk,x 0) > kfor every k. But then ( xk) cannot have a convergent
subsequence. Otherwise, if xkj→x, then
d(xkj,x 0)≤d(xkj,x ) +d(x,x 0)
and is bounded, which is a contradiction.
This implies that if (X,d ) is a metric space and E⊆X, and E is compact,
then E is bounded, i.e. E⊆BR(x0) for some x0∈X,R > 0, and E with the
subspace metric is complete. Hence E is closed as a subset of X.
The converse is not true. For example, recall if we have an inﬁnite-dimensional
normed vector space, then the closed unit sphere is complete and bounded, but
not compact. Alternatively, we can take X = R with the metric d(x,y ) =
min{1,|x−y|}. This is clearly bounded (by 1), and it is easy to check that this
is complete. However, this is not compact since the sequence xk = k has no
convergent subsequence.
However, we can strengthen the condition of boundedness to total bound-
edness, and get the equivalence between “completeness and total boundedness”
and compactness.
Deﬁnition (Totally bounded*). A metric space ( X,d ) is said to be totally
bounded if for all ε> 0, there is an integer N∈ N and points x1,··· ,xN∈X
such that
X =
N⋃
i=1
Bε(xi).
It is easy to check that being totally bounded implies being bounded. We
then have the following strengthening of the previous theorem.
47

5 Metric spaces IB Analysis II
Theorem. (non-examinable) Let (X,d ) be a metric space. Then X is compact
if and only if X is complete and totally bounded.
Proof. (⇐) Let X be complete and totally bounded, ( yi)∈X. For every j∈ N,
there exists a ﬁnite set of points Ej such that every point is within 1
j of one of
these points.
Now since E1 is ﬁnite, there is some x1∈E1 such that there are inﬁnitely
manyyi’s in B(x1, 1). Pick the ﬁrst yi in B(x1, 1) and call it yi1.
Now there is some x2 ∈ E2 such that there are inﬁnitely many yi’s in
B(x1, 1)∩B(x2, 1
2). Pick the one with smallest value of i>i 1, and call this yi2.
Continue till inﬁnity.
This procedure gives a sequence xi∈Ei and subsequence (yik), and also
yin∈
n⋂
j=1
B
(
xj, 1
j
)
.
It is easy to see that ( yin) is Cauchy since if m>n , then d(yim,yin)< 2
n. By
completeness of X, this subsequence converges.
(⇒) Compactness implying completeness is proved above. Suppose X is not
totally bounded. We show it is not compact by constructing a sequence with no
Cauchy subsequence.
Suppose ε is such that there is no ﬁnite set of points x1,··· ,xN with
X =
N⋃
i=1
Bε(xi).
We will construct our sequence iteratively.
Start by picking an arbitrary y1. Pick y2 such that d(y1,y 2)≥ε. This exists
or else Bε(y1) covers all of X.
Now given y1,··· ,yn such that d(yi,yj)≥ε for all i,j = 1,··· ,n , i⁄=j, we
pickyn+1 such that d(yn+1,yj)≥ε for all j = 1,··· ,n . Again, this exists, or
else⋃n
i=1Bε(yi) covers X. Then clearly the sequence ( yn) is not Cauchy. So
done.
In IID Linear Analysis, we will prove the Arzel` a-Ascoli theorem that charac-
terizes the compact subsets of the space C([a.b]) in a very concrete way, which
is in some sense a strengthening of this result.
5.5 Continuous functions
We are going to look at continuous mappings between metric spaces.
Deﬁnition (Continuity). Let (X,d ) and (X′,d′) be metric spaces. A function
f :X→X′ is continuous at y∈X if
(∀ε> 0)(∃δ >0)(∀x)d(x,y )<δ ⇒d′(f(x),f (y))<ε.
This is true if and only if for every ε> 0, there is some δ >0 such that
Bδ(y)⊆f−1Bε(f(x)).
f is continuous if f is continuous at each y∈X.
48

5 Metric spaces IB Analysis II
Deﬁnition (Uniform continuity). f is uniformly continuous on X if
(∀ε> 0)(∃δ >0)(∀x,y∈X)d(x,y )<δ ⇒d(f(x),f (y))<ε.
This is true if and only if for all ε, there is some δ such that for all y, we have
Bδ(y)⊆f−1(Bε(f(y))).
Deﬁnition (Lipschitz function and Lipschitz constant). f is said to be Lipschitz
on X if there is some K∈ [0,∞) such that for all x,y∈X,
d′(f(x),f (y))≤Kd(x,y )
Any suchK is called a Lipschitz constant.
It is easy to show
Lipschitz⇒ uniform continuity⇒ continuity.
We have seen many examples that continuity does not imply uniform continuity.
To show that uniform continuity does not imply Lipschitz, take X =X′ = R.
We deﬁne the metrics as
d(x,y ) = min{1,|x−y|}, d ′(x,y ) =|x−y|.
Now consider the function f : (X,d )→ (X′,d′) deﬁned by f(x) = x. We can
then check that this is uniformly continuous but not Lipschitz.
Note that the statement that metrics d and d′ are Lipschitz equivalent is
equivalent to saying the two identity maps i : (X,d )→ (X,d′) and i′ : (X,d′)→
(X,d ) are Lipschitz, hence the name.
Note also that the metric itself is also a Lipschitz map for any metric. Here
we are viewing the metric as a function d : X×X→ R, with the metric on
X×X deﬁned as
˜d((x1,y 1), (x2,y 2)) =d(x1,x 2) +d(y1,y 2).
This is a consequence of the triangle inequality, since
d(x1,y 1)≤d(x1,x 2) +d(x2,y 2) +d(y1,y 2).
Moving the middle term to the left gives
d(x1,y 1)−d(x2,y 2)≤ ˜d((x1,y 1), (x2,y 2))
Swapping the theorems around, we can put in the absolute value to obtain
|d(x1,y 1)−d(x2,y 2)|≤ ˜d((x1,y 1), (x2,y 2))
Recall that at the very beginning, we proved that a continuous map from a
closed, bounded interval is automatically uniformly continuous. This is true
whenever the domain is compact.
Theorem. Let (X,d ) be a compact metric space, and ( X′,d′) is any metric
space. If f :X→X′ be continuous, then f is uniformly continuous.
49

5 Metric spaces IB Analysis II
This is exactly the same proof as what we had for the [0 , 1] case.
Proof. We are going to prove by contradiction. Suppose f : X→ X′ is not
uniformly continuous. Since f is not uniformly continuous, there is some ε> 0
such that for all δ = 1
n, there is some xn,yn such that d(xn,yn) < 1
n but
d′(f(xn),f (yn))>ε .
By compactness of X, (xn) has a convergent subsequence (xni)→x. Then
we also have yni → x. So by continuity, we must have f(xni)→ f(x) and
f(yni)→f(x). But d′(f(xni),f (yni))>ε for all ni. This is a contradiction.
In the proof, we have secretly used (part of) the following characterization of
continuity:
Theorem. Let (X,d ) and (X′,d′) be metric spaces, and f :X→X′. Then the
following are equivalent:
(i) f is continuous at y.
(ii) f(xk)→f(y) for every sequence (xk) in X with xk→y.
(iii) For every neighbourhood V of f(y), there is a neighbourhood U of y such
that U⊆f−1(V ).
Note that the deﬁnition of continuity says something like (iii), but with open
balls instead of open sets. So this should not be surprising.
Proof.
– (i) ⇔ (ii): The argument for this is the same as for normed spaces.
– (i)⇒ (iii): Let V be a neighbourhood of f(y). Then by deﬁnition there is
ε> 0 such that Bε(f(y))⊆V . By continuity of f, there is some δ such
that
Bδ(y)⊆f−1(Bε(f(y)))⊆f−1(V ).
Set U =Bε(y) and done.
– (iii)⇒ (i): for any ε, use the hypothesis with V = Bε(f(y)) to get a
neighbourhood U of y such that
U⊆f−1(V ) =f−1(Bε(f(y))).
Since U is open, there is some δ such that Bδ(y)⊆U. So we get
Bδ(y)⊆f−1(Bε(f(y))).
So we get continuity.
Corollary. A function f : (X,d )→ (X′,d′) is continuous if f−1(V ) is open in
X wheneverV is open in X′.
Proof. Follows directly from the equivalence of (i) and (iii) in the theorem
above.
50

5 Metric spaces IB Analysis II
5.6 The contraction mapping theorem
If you have already taken IB Metric and Topological Spaces, then you were
probably bored by the above sections, since you’ve already met them all. Finally,
we get to something new. This section is comprised of just two theorems. The
ﬁrst is the contraction mapping theorem, and we will use it to prove Picard-
Lindel¨ of existence theorem. Later, we will prove the inverse function theorem
using the contraction mapping theorem. All of these are really powerful and
important theorems in analysis. They have many more applications and useful
corollaries, but we do not have time to get into those.
Deﬁnition (Contraction mapping). Let (X,d ) be metric space. A mapping
f :X→X is a contraction if there exists some λ with 0≤λ< 1 such that
d(f(x),f (y))≤λd(x,y ).
Note that a contraction mapping is by deﬁnition Lipschitz and hence (uni-
formly) continuous.
Theorem (Contraction mapping theorem). Let X be a (non-empty) complete
metric space, and if f :X→X is a contraction, then f has a unique ﬁxed point,
i.e. there is a unique x such that f(x) =x.
Moreover, if f : X → X is a function such that f (m) : X → X (i.e. f
composed with itself m times) is a contraction for some m, then f has a unique
ﬁxed point.
We can see ﬁnding ﬁxed points as the process of solving equations. One
important application we will have is to use this to solve diﬀerential equations.
Note that the theorem is false if we drop the completeness assumption. For
example, f : (0, 1)→ (0, 1) deﬁned by x
2 is clearly a contraction with no ﬁxed
point. The theorem is also false if we drop the assumption λ< 1. In fact, it is
not enough to assume d(f(x),f (y))<d (x,y ) for all x,y . A counterexample is
to be found on example sheet 3.
Proof. We ﬁrst focus on the case where f itself is a contraction.
Uniqueness is straightforward. By assumption, there is some 0 ≤λ< 1 such
that
d(f(x),f (y))≤λd(x,y )
for all x,y∈X. If x and y are both ﬁxed points, then this says
d(x,y ) =d(f(x),f (y))≤λd(x,y ).
This is possible only if d(x,y ) = 0, i.e. x =y.
To prove existence, the idea is to pick a point x0 and keep applying f. Let
x0∈X. We deﬁne the sequence (xn) inductively by
xn+1 =f(xn).
We ﬁrst show that this is Cauchy. For any n≥ 1, we can compute
d(xn+1,xn) =d(f(xn),f (xn−1))≤λd(xn,xn−1)≤λnd(x1,x 0).
51

5 Metric spaces IB Analysis II
Since this is true for any n, for m>n , we have
d(xm,xn)≤d(xm,xm−1) +d(xm−1,xm−2) +··· +d(xn+1,xn)
=
m−1∑
j=n
d(xj+1,xj)
=
m−1∑
j=n
λjd(x1,x 0)
≤d(x1,x 0)
∞∑
j=n
λj
= λn
1−λd(x1,x 0).
Note that we have again used the property that λ< 1.
This implies d(xm,xn)→ 0 as m,n→∞ . So this sequence is Cauchy. By
the completeness of X, there exists some x∈ X such that xn→ x. Since f
is a contraction, it is continuous. So f(xn)→ f(x). However, by deﬁnition
f(xn) = xn+1. So taking the limit on both sides, we get f(x) = x. So x is a
ﬁxed point.
Now suppose that f (m) is a contraction for some m. Hence by the ﬁrst part,
there is a unique x∈X such that f (m)(x) =x. But then
f (m)(f(x)) =f (m+1)(x) =f(f (m)(x)) =f(x).
So f(x) is also a ﬁxed point of f (n)(x). By uniqueness of ﬁxed points, we must
havef(x) =x. Since any ﬁxed point of f is clearly a ﬁxed point of f (n) as well,
it follows that x is the unique ﬁxed point of f.
Based on the proof of the theorem, we have the following error estimate in
the contraction mapping theorem: for x0∈ X and xn = f(xn−1), we showed
that for m>n , we have
d(xm,xn)≤ λn
1−λd(x1,x 0).
If xn→x, taking the limit of the above bound as m→∞ gives
d(x,xn)≤ λn
1−λd(x1,x 0).
This is valid for all n.
We are now going to use this to obtain the Picard-Lindel¨ of existence theorem
for ordinary diﬀerential equations. The objective is as follows. Suppose we are
given a function
F = (F1,F 2,··· ,Fn) : R× Rn→ Rn.
We interpret the R as time and the Rn as space.
Givent0∈ R and x0∈ Rn, we want to know when can we ﬁnd a solution to
the ODE df
dt = F(t, f(t))
52

5 Metric spaces IB Analysis II
subject to f(t0) = x0. We would like this solution to be valid (at least) for all t
in some interval I containingt0.
More explicitly, we want to understand when will there be some ε > 0
and a diﬀerentiable function f = (f1,··· ,fn) : ( t0− ε,t 0 +ε) → Rn (i.e.
fj : (t0−ε,t 0 +ε)→ R is diﬀerentiable for all j) satisfying
dfj
dt =Fj(t,f 1(t),··· ,fn(t))
such that fj(t0) =x(j)
0 for all j = 1,...,n and t∈ (t0−ε,t 0 +ε).
We can imagine this scenario as a particle moving in Rn, passing through x0
at time t0. We then ask if there is a trajectory f(t) such that the velocity of the
particle at any time t is given by F(t, f(t)).
This is a complicated system, since it is a coupled system of many variables.
Explicit solutions are usually impossible, but in certain cases, we can prove the
existence of a solution. Of course, solutions need not exist for arbitrary F . For
example, there will be no solution if F is everywhere discontinuous, since any
derivative is continuous in a dense set of points. The Picard-Lindel¨ of existence
theorem gives us suﬃcient conditions for a unique solution to exists.
We will need the following notation
Notation. For x0∈ Rn, R> 0, we let
BR(x0) ={x∈ Rn :‖x− x0‖2≤R}.
Then the theorem says
Theorem (Picard-Lindel¨ of existence theorem). Let x0∈ Rn, R >0, a < b,
t0∈ [a,b ]. Let F : [a,b ]×BR(x0)→ Rn be a continuous function satisfying
‖F(t, x)− F(t, y)‖2≤κ‖x− y‖2
for some ﬁxed κ >0 and all t∈ [a,b ], x∈ BR(x0). In other words, F (t,· ) :
Rn→ Rn is Lipschitz on BR(x0) with the same Lipschitz constant for every t.
Then
(i) There exists an ε> 0 and a unique diﬀerentiable function f : [t0−ε,t 0 +
ε]∩ [a,b ]→ Rn such that
df
dt = F(t, f(t)) ( ∗)
and f(t0) = x0.
(ii) If
sup
[a,b]×BR(x0)
‖F‖2≤ R
b−a,
then there exists a unique diﬀerential function f : [a,b ]→ Rn that satisﬁes
the diﬀerential equation and boundary conditions above.
Evenn = 1 is an important, special, non-trivial case. Even if we have only
one dimension, explicit solutions may be very diﬃcult to ﬁnd, if not impossible.
For example,
df
dt =f 2 + sinf +ef
53

5 Metric spaces IB Analysis II
would be almost impossible to solve. However, the theorem tells us there will be
a solution, at least locally.
Note that any diﬀerentiable f satisfying the diﬀerential equation is auto-
matically continuously diﬀerentiable, since the derivative is F(t, f(t)), which is
continuous.
Before we prove the theorem, we ﬁrst show the requirements are indeed
necessary. We ﬁrst look at that ε in (i). Without the addition requirement in (ii),
there might not exist a solution globally on [ a,b ]. For example, we can consider
the n = 1 case, where we want to solve
df
dt =f 2,
with boundary condition f(0) = 1. Our F (t,f ) = f 2 is a nice, uniformly
Lipschitz function on any [0,b ]×BR(1) = [0,b ]× [1−R, 1 +R]. However, we
will shortly see that there is no global solution.
If we assume f⁄= 0, then for all t∈ [0,b ], the equation is equivalent to
d
dt(t +f−1) = 0.
So we need t +f−1 to be constant. The initial conditions tells us this constant
is 1. So we have
f(t) = 1
1−t.
Hence the solution on [0, 1) is 1
1−t. Any solution on [0,b ] must agree with this
on [0, 1). So if b≥ 1, then there is no solution in [0 ,b ].
The Lipschitz condition is also necessary to guarantee uniqueness. Without
this condition, existence of a solution is still guaranteed (but is another theorem,
the Cauchy-Peano theorem), but we could have many diﬀerent solutions. For
example, we can consider the diﬀerential equation
df
dt =
√
|f|
with f(0) = 0. Here F (t,x ) =
√
|x| is not Lipschitz near x = 0. It is easy to see
that both f = 0 and f(t) = 1
4t2 are both solutions. In fact, for any α∈ [0,b ],
the function
fα(t) =
{
0 0 ≤t≤α
1
4(t−α)2 α≤t≤b
is also a solution. So we have an inﬁnite number of solutions.
We are now going to use the contraction mapping theorem to prove this.
In general, this is a very useful idea. It is in fact possible to use other ﬁxed
point theorems to show the existence of solutions to partial diﬀerential equations.
This is much more diﬃcult, but has many far-reaching important applications
to theoretical physics and geometry, say. For these, see Part III courses.
Proof. First, note that (ii) implies (i). We know that
sup
[a,b]×BR(x)
‖F‖
54

5 Metric spaces IB Analysis II
is bounded since it is a continuous function on a compact domain. So we can
pick an ε such that
2ε≤ R
sup[a,b]×BR(x)‖F‖.
Then writing [t0−ε,t 0 +ε]∩ [a,b ] = [a1,b 1], we have
sup
[a1,b1]×BR(x)
‖F‖≤ sup
[a,b]×BR(x)
‖F‖≤ R
2ε≤ R
b1−a1
.
So (ii) implies there is a solution on [ t0−ε,t 0 +ε]∩ [a,b ]. Hence it suﬃces to
prove (ii).
To apply the contraction mapping theorem, we need to convert this into
a ﬁxed point problem. The key is to reformulate the problem as an integral
equation. We know that a diﬀerentiable f : [a,b ]→ Rn satisﬁes the diﬀerential
equation (∗) if and only if f : [a,b ]→BR(x0) is continuous and satisﬁes
f(t) = x0 +
∫ t
t0
F(s, f(s)) ds
by the fundamental theorem of calculus. Note that we don’t require f is dif-
ferentiable, since if a continuous f satisﬁes this equation, it is automatically
diﬀerentiable by the fundamental theorem of calculus. This is very helpful, since
we can work over the much larger vector space of continuous functions, and it
would be easier to ﬁnd a solution.
We letX =C([a,b ],BR(x0)). We equip X with the supremum metric
‖g− h‖ = sup
t∈[a,b]
‖g(t)− h(t)‖2.
We see thatX is a closed subset of the complete metric space C([a,b ], Rn) (again
taken with the supremum metric). So X is complete. For every g∈X, we deﬁne
a function Tg : [a,b ]→ Rn by
(Tg)(t) = x0 +
∫ t
t0
F(s, g(s)) ds.
Our diﬀerential equation is thus
f =Tf.
So we ﬁrst want to show that T is actually mapping X → X, i.e. Tg∈ X
whenever g∈X, and then prove it is a contraction map.
We have
‖Tg(t)− x0‖2 =
‖‖‖‖
∫ t
t0
F(s, g(s)) ds
‖‖‖‖
≤
⏐⏐⏐⏐
∫ t
t0
‖F(s, g(s))‖2 ds
⏐⏐⏐⏐
≤ sup
[a,b]×BR(x0)
‖F‖·| b−a|
≤R
55

5 Metric spaces IB Analysis II
Hence we know that Tg(t)∈BR(x0). So Tg∈X.
Next, we need to show this is a contraction. However, it turns out T need
not be a contraction. Instead, what we have is that for g1, g2∈X, we have
‖Tg1(t)−Tg2(t)‖2 =
‖‖‖‖
∫ t
t0
F(s, g1(s))− F(s, g2(s)) ds
‖‖‖‖
2
≤
⏐⏐⏐⏐
∫ t
t0
‖F(s, g1(s))− F(s, g2(s))‖2 ds
⏐⏐⏐⏐
≤κ(b−a)‖g1− g2‖∞
by the Lipschitz condition on F . If we indeed have
κ(b−a)< 1, (†)
then the contraction mapping theorem gives an f∈X such that
Tf = f,
i.e.
f = x0 +
∫ t
t0
F(s, f(s)) ds.
However, we do not necessarily have (†). There are many ways we can solve this
problem. Here, we can solve it by ﬁnding an m such that T (m) =T◦T◦···◦ T :
X→X is a contraction map. We will in fact show that this map satisﬁes the
bound
sup
t∈[a,b]
‖T (m)g1(t)−T (m)g2(t)‖≤ (b−a)mκm
m! sup
t∈[a,b]
‖g1(t)− g2(t)‖. (‡)
The key is the m!, since this grows much faster than any exponential. Given this
bound, we know that for suﬃciently large m, we have
(b−a)mκm
m! < 1,
i.e. T (m) is a contraction. So by the contraction mapping theorem, the result
holds.
So it only remains to prove the bound. To prove this, we prove instead the
pointwise bound: for any t∈ [a,b ], we have
‖T (m)g1(t)−T (m)g2(t)‖2≤ (|t−t0|)mκm
m! sup
s∈[t0,t]
‖g1(s)− g2(s)‖.
From this, taking the supremum on the left, we obtain the bound ( ‡).
To prove this pointwise bound, we induct on m. We wlog assume t>t 0. We
know that for every m, the diﬀerence is given by
‖T (m)g1(t)−T (m)g2(t)‖2 =
‖‖‖‖
∫ t
t0
F (s,T (m−1)g1(s))−F (s,T (m−1)g2(s)) ds
‖‖‖‖
2
.
≤κ
∫ t
t0
‖T (m−1)g1(s)−T (m−1)g2(s)‖2 ds.
56

5 Metric spaces IB Analysis II
This is true for all m. If m = 1, then this gives
‖Tg 1(t)−Tg 2(t)‖≤ κ(t−t0) sup
[t0,t]
‖g1−g2‖2.
So the base case is done.
Form≥ 2, assume by induction the bound holds with m− 1 in place of m.
Then the bounds give
‖T (m)g1(t)−T (m)g2(t)‖≤ κ
∫ t
t0
km−1(s−t0)m−1
(m− 1)! sup
[t0,s]
‖g1−g2‖2 ds
≤ κm
(m− 1)! sup
[t0,t]
‖g1−g2‖2
∫ t
t0
(s−t0)m−1 ds
= κm(t−t0)m
m! sup
[t0,t]
‖g1−g2‖2.
So done.
Note that to get the factor of m!, we had to actually perform the integral,
instead of just bounding ( s−t0)m−1 by (t−t0). In general, this is a good
strategy if we want tight bounds. Instead of bounding
⏐⏐⏐⏐⏐
∫ b
a
f(x) dx
⏐⏐⏐⏐⏐≤ (b−a) sup|f(x)|,
we write f(x) =g(x)h(x), where h(x) is something easily integrable. Then we
can have a bound
⏐⏐⏐⏐⏐
∫ b
a
f(x) dx
⏐⏐⏐⏐⏐≤ sup|g(x)|
∫ b
a
|h(x)| dx.
57

6 Diﬀerentiation from Rm to Rn IB Analysis II
6 Diﬀerentiation from Rm to Rn
6.1 Diﬀerentiation from Rm to Rn
We are now going to investigate diﬀerentiation of functions f : Rn→ Rm. The
hard part is to ﬁrst come up with a sensible deﬁnition of what this means. There
is no obvious way to generalize what we had for real functions. After deﬁning
it, we will need to do some hard work to come up with easy ways to check if
functions are diﬀerentiable. Then we can use it to prove some useful results like
the mean value inequality. We will always use the usual Euclidean norm.
To deﬁne diﬀerentiation in Rn, we ﬁrst we need a deﬁnition of the limit.
Deﬁnition (Limit of function). Let E⊆ Rn and f :E→ Rm. Let a∈ Rn be a
limit point of E, and let b∈ Rm. We say
lim
x→a
f(x) = b
if for every ε> 0, there is some δ >0 such that
(∀x∈E) 0<‖x− a‖<δ ⇒‖f(x)− b‖<ε.
As in the case of R in IA Analysis I, we do not impose any requirements on
F when x = a. In particular, we don’t assume that a is in the domain E.
We would like a deﬁnition of diﬀerentiation for functions f : Rn→ R (or
more generally f : Rn→ Rm) that directly extends the familiar deﬁnition on the
real line. Recall that if f : (b,c )→ R and a∈ (b,c ), we say f is diﬀerentiable if
the limit
Df(a) =f′(a) = lim
h→0
f(a +h)−f(a)
h (∗)
exists (as a real number). This cannot be extended to higher dimensions directly,
since h would become a vector in Rn, and it is not clear what we mean by
dividing by a vector. We might try dividing by ‖h‖ instead, i.e. require that
lim
h→0
f(a + h)−f(a)
‖h‖
exists. However, this is clearly wrong, since in the case of n = 1, this reduces to
the existence of the limit
f(a +h)−f(a)
|h| ,
which almost never exists, e.g. when f(x) =x. It is also possible that this exists
while the genuine derivative does not, e.g. when f(x) =|x|, at x = 0. So this is
clearly wrong.
Now we are a bit stuck. We need to divide by something, and that thing
better be a scalar. ‖h‖ is not exactly what we want. What should we do? The
idea is move f′(a) to the other side of the equation, and ( ∗) becomes
lim
h→0
f(a +h)−f(a)−f′(a)h
h = 0.
Now if we replace h by|h|, nothing changes. So this is equivalent to
lim
h→0
f(a +h)−f(a)−f′(a)h
|h| = 0.
58

6 Diﬀerentiation from Rm to Rn IB Analysis II
In other words, the function f is diﬀerentiable if there is some A such that
lim
h→0
f(a +h)−f(a)−Ah
|h| = 0,
and we call A the derivative.
We are now in a good shape to generalize. Note that if f : Rn→ R is a
real-valued function, then f(a +h)−f(a) is a scalar, but h is a vector. So A is
not just a number, but a (row) vector. In general, if our function f : Rn→ Rm
is vector-valued, then our A should be an m×n matrix. Alternatively, A is a
linear map from Rn to Rm.
Deﬁnition (Diﬀerentiation in Rn). Let U⊆ Rn be open, f : Rn→ Rm. We say
f is diﬀerentiable at a point a∈ U if there exists a linear map A : Rn→ Rm
such that
lim
h→0
f(a + h)− f(a)−Ah
‖h‖ = 0.
We callA the derivative of f at a. We write the derivative as Df(a).
This is equivalent to saying
lim
x→a
f(x)− f(a)−A(x− a)
‖x− a‖ = 0.
Note that this is completely consistent with our usual deﬁnition the case where
n =m = 1, as we have discussed above, since a linear transformation α : R→ R
is just given by α(h) =Ah for some real A∈ R.
One might instead attempt to deﬁne diﬀerentiability as follows: for any
f : Rm→ R, we say f is diﬀerentiable at x if f is diﬀerentiable when restricted
to any line passing through x. However, this is a weaker notion, and we will
later see that if we deﬁne diﬀerentiability this way, then diﬀerentiability will no
longer imply continuity, which is bad.
Having deﬁned diﬀerentiation, we want to show that the derivative is unique.
Proposition (Uniqueness of derivative). Derivatives are unique.
Proof. Suppose A,B : Rn→ Rm both satisfy the condition
lim
h→0
f(a + h)− f(a)−Ah
‖h‖ = 0
lim
h→0
f(a + h)− f(a)−Bh
‖h‖ = 0.
By the triangle inequality, we get
‖(B−A)h‖≤‖ f(a + h)−f(a)−Ah‖ +‖f(a + h)−f(a)−Bh‖.
So
‖(B−A)h‖
‖h‖ → 0
as h→ 0. We set h =tu in this proof to get
‖(B−A)tu‖
‖tu‖ → 0
59

6 Diﬀerentiation from Rm to Rn IB Analysis II
as t→ 0. Since (B−A) is linear, we know
‖(B−A)tu‖
‖tu‖ =‖(B−A)u‖
‖u‖ .
So (B−A)u = 0 for all u∈ Rn. So B =A.
Notation. We writeL(Rn; Rm) for the space of linear maps A : Rn→ Rm.
So Df(a)∈L(Rn; Rm).
To avoid having to write limits and divisions all over the place, we have the
following convenient notation:
Notation (Little o notation). For any function α :Br(0)⊆ Rn→ Rm, write
α(h) =o(h)
if
α(h)
‖h‖ → 0 as h→ 0.
In other words, α→ 0 faster than‖h‖ as h→ 0.
Note that oﬃcially, α(h) =o(h) as a whole is a piece of notation, and does
not represent equality.
Then the condition for diﬀerentiability can be written as: f : U→ Rm is
diﬀerentiable at a∈U if there is some A with
f(a + h)−f(a)−Ah =o(h).
Alternatively,
f(a + h) =f(a) +Ah +o(h).
Note that we require the domain U of f to be open, so that for each a∈ U,
there is a small ball around a on which f is deﬁned, so f(a + h) is deﬁned for
for suﬃciently small h. We could relax this condition and consider “one-sided”
derivatives instead, but we will not look into these in this course.
We can interpret the deﬁnition of diﬀerentiability as saying we can ﬁnd a
“good” linear approximation (technically, it is aﬃne, not linear) to the function f
near a.
While the deﬁnition of the derivative is good, it is purely existential. This is
unlike the deﬁnition of diﬀerentiability of real functions, where we are asked to
compute an explicit limit — if the limit exists, that’s the derivative. If not, it
is not diﬀerentiable. In the higher-dimensional world, this is not the case. We
have completely no idea where to ﬁnd the derivative, even if we know it exists.
So we would like an explicit formula for it.
The idea is to look at speciﬁc “directions” instead of ﬁnding the general
derivative. As always, let f : U→ Rm be diﬀerentiable at a∈ U. Fix some
u∈ Rn, take h =tu (with t∈ R). Assuming u⁄= 0, diﬀerentiability tells
lim
t→0
f(a +tu)− f(a)−Df(a)(tu)
‖tu‖ = 0.
60

6 Diﬀerentiation from Rm to Rn IB Analysis II
This is equivalent to saying
lim
t→0
f(a +tu)− f(a)−tDf(a)u
|t|‖u‖ = 0.
Since‖u‖ is ﬁxed, This in turn is equivalent to
lim
t→0
f(a +tu)− f(a)−tDf(a)u
t = 0.
This, ﬁnally, is equal to
Df(a)u = lim
t→0
f(a +tu)− f(a)
t .
We derived this assuming u⁄= 0, but this is trivially true for u = 0. So this
valid for all u.
This is of the same form as the usual derivative, and it is usually not too
diﬃcult to compute this limit. Note, however, that this says if the derivative
exists, then the limit above is related to the derivative as above. However, even
if the limit exists for all u, we still cannot conclude that the derivative exists.
Regardless, even if the derivative does not exist, this limit is still often a
useful notion.
Deﬁnition (Directional derivative). We write
Duf(a) = lim
t→0
f(a +tu)− f(a)
t
whenever this limit exists. We call Duf(a) the directional derivative of f at
a∈U in the direction of u∈ Rn.
By deﬁnition, we have
Duf(a) = d
dt
⏐⏐⏐⏐
t=0
f(a +tu).
Often, it is convenient to focus on the special cases whereu = ej, a member of
the standard basis for Rn. This is known as the partial derivative. By convention,
this is deﬁned for real-valued functions only, but the same deﬁnition works for
any Rm-valued function.
Deﬁnition (Partial derivative). The jth partial derivative of f : U → R at
a∈U is
Dejf(a) = lim
t→∞
f(a +tej)−f(a)
t ,
when the limit exists. We often write this as
Dejf(a) =Djf(a) = ∂f
∂xj
.
Note that these deﬁnitions do not require diﬀerentiability of f at a. We
will see some examples shortly. Before that, we ﬁrst establish some elementary
properties of diﬀerentiable functions.
Proposition. Let U⊆ Rn be open, a∈U.
61

6 Diﬀerentiation from Rm to Rn IB Analysis II
(i) If f :U→ Rm is diﬀerentiable at a, then f is continuous at a.
(ii) If we write f = (f1,f 2,··· ,fm) :U→ Rm, where each fi :U→ R, then f
is diﬀerentiable at a if and only if each fj is diﬀerentiable at a for each j.
(iii) Iff,g :U→ Rm are both diﬀerentiable at a, then λf +µg is diﬀerentiable
at a with
D(λf +µg)(a) =λDf(a) +µDg(a).
(iv) If A : Rn→ Rm is a linear map, then A is diﬀerentiable for any a∈ Rn
with
DA(a) =A.
(v) If f is diﬀerentiable at a, then the directional derivative Duf(a) exists for
all u∈ Rn, and in fact
Duf(a) =Df(a)u.
(vi) If f is diﬀerentiable at a, then all partial derivatives Djfi(a) exist for
j = 1,··· ,n ; i = 1,··· ,m , and are given by
Djfi(a) =Dfi(a)ej.
(vii) IfA = (Aij) be the matrix representing Df(a) with respect to the standard
basis for Rn and Rm, i.e. for any h∈ Rn,
Df(a)h =Ah.
Then A is given by
Aij =⟨Df(a)ej, bi⟩ =Djfi(a).
where{e1,··· , en} is the standard basis for Rn, and{b1,··· , bm} is the
standard basis for Rm.
The second property is useful, since instead of considering arbitrary Rm-
valued functions, we can just look at real-valued functions.
Proof.
(i) By deﬁnition, if f is diﬀerentiable, then as h→ 0, we know
f(a + h)− f(a)−Df(a)h→ 0.
Since Df(a)h→ 0 as well, we must have f(a + h)→ f(h).
(ii) Exercise on example sheet 4.
(iii) We just have to check this directly. We have
(λf +µg)(a + h)− (λf +µg)(a)− (λDf(a) +µDg(a))
‖h‖
=λf(a + h)− f(a)−Df(a)h
‖h‖ +µg(a + h)− g(a)−Dg(a)h
‖h‖ .
which tends to 0 as h→ 0. So done.
62

6 Diﬀerentiation from Rm to Rn IB Analysis II
(iv) Since A is linear, we always have A(a + h)−A(a)−Ah = 0 for all h.
(v) We’ve proved this in the previous discussion.
(vi) We’ve proved this in the previous discussion.
(vii) This follows from the general result for linear maps: for any linear map
represented by (Aij)m×n, we have
Aij =⟨Aej, bi⟩.
Applying this with A =Df(a) and note that for any h∈ Rn,
Df(a)h = (Df1(a)h,··· ,D fm(a)h).
So done.
The above says diﬀerentiability at a point implies the existence of all direc-
tional derivatives, which in turn implies the existence of all partial derivatives.
The converse implication does not hold in either of these.
Example. Let f 2 : R2→ R be deﬁned by
f(x,y ) =
{
0 xy = 0
1 xy⁄= 0
Then the partial derivatives are
df
dx(0, 0) = df
dy (0, 0) = 0,
In other directions, say u = (1, 1), we have
f(0 +tu)−f(0)
t = 1
t
which diverges as t→ 0. So the directional derivative does not exist.
Example. Let f : R2→ R be deﬁned by
f(x,y ) =
{
x3
y y⁄= 0
0 y = 0
Then for u = (u1,u 2)⁄= 0 and t⁄= 0, we can compute
f(0 +tu)−f(0)
t =
{
tu3
1
u2
u2⁄= 0
0 u2 = 0
So
Duf(0) = lim
t→0
f(0 +tu)−f(0)
t = 0,
and the directional derivative exists. However, the function is not diﬀerentiable
at 0, since it is not even continuous at 0, as
f(δ,δ 4) = 1
δ
diverges as δ→ 0.
63

6 Diﬀerentiation from Rm to Rn IB Analysis II
Example. Let f : R2→ R be deﬁned by
f(x,y ) =
{
x3
x2+y2 (x,y )⁄= (0, 0)
0 ( x,y ) = (0, 0).
It is clear that f continuous at points other than 0, and f is also continuous at
0 since|f(x,y )|≤| x|. We can compute the partial derivatives as
∂f
∂x (0, 0) = 1, ∂f
∂y (0, 0) = 0.
In fact, we can compute the diﬀerence quotient in the direction u = (u1,u 2)⁄= 0
to be
f(0 +tu)−f(0)
t = u3
1
u2
1 +u2
2
.
So we have
Duf(0) = u3
1
u2
1 +u2
2
.
We can now immediately conclude that f is not diﬀerentiable at 0, since if it
were, then we would have
Duf(0) =Df(0)u,
which should be a linear expression in u, but this is not.
Alternatively, iff were diﬀerentiable, then we have
Df(0)h =
(1 0 )(
h1
h2
)
=h1.
However, we have
f(0 + h)−f(0)−Df(0)h
‖h‖ =
h3
1
h2
1+h2
2
−h1
√
h2
1 +h2
2
=− h1h2
2
√
h2
1 +h2
2
3,
which does not tend to 0 as h→ 0. For example, if h = (t,t ), this quotient is
− 1
23/2
for t⁄= 0.
To decide if a function is diﬀerentiable, the ﬁrst step would be to compute
the partial derivatives. If they don’t exist, then we can immediately know the
function is not diﬀerentiable. However, if they do, then we have a candidate for
what the derivative is, and we plug it into the deﬁnition to check if it actually is
the derivative.
This is a cumbersome thing to do. It turns out that while existence of partial
derivatives does not imply diﬀerentiability in general, it turns out we can get
diﬀerentiability if we add some more slight conditions.
Theorem. Let U⊆ Rn be open, f :U→ Rm. Let a∈U. Suppose there exists
some open ball Br(a)⊆U such that
64

6 Diﬀerentiation from Rm to Rn IB Analysis II
(i) Djfi(x) exists for every x∈Br(a) and 1≤i≤m, 1≤j≤n
(ii) Djfi are continuous at a for all 1≤i≤m, 1≤j≤n.
Then f is diﬀerentiable at a.
Proof. It suﬃces to prove for m = 1, by the long proposition. For each h =
(h1,··· ,hn)∈ Rn, we have
f(a + h)−f(a) =
n∑
j=1
f(a +h1e1 +··· +hjej)−f(a +h1e1 +··· +hj−1ej−1).
Now for convenience, we can write
h(j) =h1e1 +··· +hjej = (h1,··· ,hj, 0,··· , 0).
Then we have
f(a + h)−f(a) =
n∑
j=1
f(a + h(j))−f(a + h(j−1))
=
n∑
j=1
f(a + h(j−1) +hjej)−f(a + h(j−1)).
Note that in each term, we are just moving along the coordinate axes. Since
the partial derivatives exist, the mean value theorem of single-variable calculus
applied to
g(t) =f(a + h(j−1) +tej)
on the interval t∈ [0,hj] allows us to write this as
f(a + h)−f(a)
=
n∑
j=1
hjDjf(a + h(j−1) +θjhjej)
=
n∑
j=1
hjDjf(a) +
n∑
j=1
hj
(
Djf(a + h(j−1) +θjhjej)−Djf(a)
)
for some θj∈ (0, 1).
Note that Djf(a + h(j−1) +θjhjej)−Djf(a)→ 0 as h→ 0 since the partial
derivatives are continuous at a. So the second term is o(h). So f is diﬀerentiable
at a with
Df(a)h =
n∑
j=1
Djf(a)hj.
This is a very useful result. For example, we can now immediately conclude
that the function (

x
y
z
)
↦→
(3x2 + 4 siny +e6z
xyze 14x
)
is diﬀerentiable everywhere, since it has continuous partial derivatives. This is
much better than messing with the deﬁnition itself.
65

6 Diﬀerentiation from Rm to Rn IB Analysis II
6.2 The operator norm
So far, we have only looked at derivatives at a single point. We haven’t discussed
much about the derivative at, say, a neighbourhood or the whole space. We
might want to ask if the derivative is continuous or bounded. However, this is
not straightforward, since the derivative is a linear map, and we need to deﬁne
these notions for functions whose values are linear maps. In particular, we want
to understand the map Df :Br(a)→L(Rn; Rm) given by x↦→Df(x). To do so,
we need a metric on the space L(Rn; Rm). In fact, we will use a norm.
LetL =L(Rn; Rm). This is a vector space over R deﬁned with addition and
scalar multiplication deﬁned pointwise. In fact, L is a subspace of C(Rn, Rm).
To prove this, we have to prove that all linear maps are continuous. Let
{e1,··· , en} be the standard basis for Rn, and for
x =
n∑
j=1
xjej,
and A∈L , we have
A(x) =
n∑
j=1
xjAej.
By Cauchy-Schwarz, we know
‖A(x)‖≤
n∑
j=1
|xj|‖A(ej)‖≤‖ x‖
vuu√
n∑
j=1
‖A(ej)‖2.
So we see A is Lipschitz, and is hence continuous. Alternatively, this follows
from the fact that linear maps are diﬀerentiable and hence continuous.
We can use this fact to deﬁne the norm of linear maps. Since L is ﬁnite-
dimensional (it is isomorphic to the space of real m×n matrices, as vector
spaces, and hence have dimension mn), it really doesn’t matter which norm we
pick as they are all Lipschitz equivalent, but a convenient choice is the sup norm,
or the operator norm.
Deﬁnition (Operator norm). The operator norm onL =L(Rn; Rm) is deﬁned
by
‖A‖ = sup
x∈Rn:‖x‖=1
‖Ax‖.
Proposition.
(i) ‖A‖<∞ for all A∈L .
(ii) ‖·‖ is indeed a norm on L.
(iii)
‖A‖ = sup
Rn\{0}
‖Ax‖
‖x‖ .
(iv) ‖Ax‖≤‖ A‖‖x‖ for all x∈ Rn.
66

6 Diﬀerentiation from Rm to Rn IB Analysis II
(v) Let A∈L(Rn; Rm) and B∈L(Rm; Rp). Then BA =B◦A∈L(Rn; Rp)
and
‖BA‖≤‖ B‖‖A‖.
Proof.
(i) This is since A is continuous and{x∈ Rn :‖x‖ = 1} is compact.
(ii) The only non-trivial part is the triangle inequality. We have
‖A +B‖ = sup
‖x‖=1
‖Ax +Bx‖
≤ sup
‖x‖=1
(‖Ax‖ +‖Bx‖)
≤ sup
‖x‖=1
‖Ax‖ + sup
‖x‖=1
‖Bx‖
=‖A‖ +‖B‖
(iii) This follows from linearity of A, and for any x∈ Rn, we have
‖‖‖‖
x
‖x‖
‖‖‖‖ = 1.
(iv) Immediate from above.
(v)
‖BA‖ = sup
Rn\{0}
‖BAx‖
‖x‖ ≤ sup
Rn\{0}
‖B‖‖Ax‖
‖x‖ =‖B‖‖A‖.
For certain easy cases, we have a straightforward expression for the operator
norm.
Proposition.
(i) If A∈ L(R, Rm), then A can be written as Ax = xa for some a∈ Rm.
Moreover,‖A‖ =‖a‖, where the second norm is the Euclidean norm in Rn
(ii) IfA∈L(Rn, R), then Ax = x·a for some ﬁxed a∈ Rn. Again,‖A‖ =‖a‖.
Proof.
(i) Set A(1) = a. Then by linearity, we get Ax =xA(1) =xa. Then we have
‖Ax‖ =|x|‖a‖.
So we have
‖Ax‖
|x| =‖a‖.
(ii) Exercise on example sheet 4.
Theorem (Chain rule). Let U⊆ Rn be open, a∈U, f :U→ Rm diﬀerentiable
at a. Moreover, V ⊆ Rm is open with f(U)⊆V and g :V → Rp is diﬀerentiable
at f(a). Then g◦ f :U→ Rp is diﬀerentiable at a, with derivative
D(g◦ f)(a) =Dg(f(a))Df(a).
67

6 Diﬀerentiation from Rm to Rn IB Analysis II
Proof. The proof is very easy if we use the little o notation. Let A =Df(a) and
B =Dg(f(a)). By diﬀerentiability of f, we know
f(a + h) = f(a) +Ah +o(h)
g(f(a) + k) = g(f(a)) +Bk +o(k)
Now we have
g◦ f(a + h) = g(f(a) +Ah +o(h)| {z }
k
)
= g(f(a)) +B(Ah +o(h)) +o(Ah +o(h))
= g◦ f(a) +BAh +B(o(h)) +o(Ah +o(h)).
We just have to show the last term is o(h), but this is true since B and A are
bounded. By boundedness,
‖B(o(h))‖≤‖ B‖‖o(h)‖.
So B(o(h)) =o(h). Similarly,
‖Ah +o(h)‖≤‖ A‖‖h‖ +‖o(h)‖≤ (‖A‖ + 1)‖h‖
for suﬃciently small‖h‖. So o(Ah +o(h)) is in fact o(h) as well. Hence
g◦ f(a + h) = g◦ f(a) +BAh +o(h).
6.3 Mean value inequalities
So far, we have just looked at cases where we assume the function is diﬀerentiable
at a point. We are now going to assume the function is diﬀerentiable in a region,
and see what happens to the derivative.
Recall the mean value theorem from single-variable calculus: if f : [a,b ]→ R
is continuous on [a,b ] and diﬀerentiable on (a,b ), then
f(b)−f(a) =f′(c)(b−a)
for some c∈ (a,b ). This is our favorite theorem, and we have used it many
times in IA Analysis. Here we have an exact equality. However, in general, for
vector-valued functions, i.e. if we are mapping to Rm, this is no longer true.
Instead, we only have an inequality.
We ﬁrst prove it for the case when the domain is a subset of R, and then
reduce the general case to this special case.
Theorem. Let f : [a,b ]→ Rm be continuous on [a,b ] and diﬀerentiable on (a,b ).
Suppose we can ﬁnd some M such that for all t∈ (a,b ), we have‖Df(t)‖≤ M.
Then
‖f(b)− f(a)‖≤ M(b−a).
Proof. Let v = f(b)− f(a). We deﬁne
g(t) = v· f(t) =
m∑
i=1
vifi(t).
68

6 Diﬀerentiation from Rm to Rn IB Analysis II
Since each fi is diﬀerentiable, g is continuous on [a,b ] and diﬀerentiable on (a,b )
with
g′(t) =
∑
vif′
i(t).
Hence, we know
|g′(t)|≤
⏐⏐⏐⏐⏐
m∑
i=1
vif′
i(t)
⏐⏐⏐⏐⏐≤‖ v‖
( n∑
i=1
f′2
i (t)
)1/2
=‖v‖‖Df(t)‖≤ M‖v‖.
We now apply the mean value theorem to g to get
g(b)−g(a) =g′(t)(b−a)
for some t∈ (a,b ). By deﬁnition of g, we get
v· (f(b)− f(a)) =g′(t)(b−a).
By deﬁnition of v, we have
‖f(b)− f(a)‖2 =|g′(t)(b−a)|≤ (b−a)M‖f(b)− f(a)‖.
If f(b) = f(a), then there is nothing to prove. Otherwise, divide by ‖f(b)− f(a)‖
and done.
We now apply this to prove the general version.
Theorem (Mean value inequality) . Let a ∈ Rn and f : Br(a) → Rm be
diﬀerentiable on Br(a) with‖Df(x)‖≤ M for all x∈Br(a). Then
‖f(b1)−f(b2)‖≤ M‖b1− b2‖
for any b1, b2∈Br(a).
Proof. We will reduce this to the previous theorem.
Fix b1, b2∈Br(a). Note that
tb1 + (1−t)b2∈Br(a)
for all t∈ [0, 1]. Now consider g : [0, 1]→ Rm.
g(t) = f(tb1 + (1−t)b2).
By the chain rule, g is diﬀerentiable and
g′(t) =Dg(t) = (Df(tb1 + (1−t)b2))(b1− b2)
Therefore
‖Dg(t)‖≤‖ Df(tb1 + (1−t)b2)‖‖b1− b2‖≤ M‖b1− b2‖.
Now we can apply the previous theorem, and get
‖f(b1)− f(b2)‖ =‖g(1)− g(0)‖≤ M‖b1− b2‖.
69

6 Diﬀerentiation from Rm to Rn IB Analysis II
Note that here we worked in a ball. In general, we could have worked in a
convex set, since all we need is for tb1 + (1−t)b2 to be inside the domain.
But with this, we have the following easy corollary.
Corollary. Let f :Br(a)⊆ Rn→ Rm haveDf(x) = 0 for all x∈Br(a). Then
f is constant.
Proof. Apply the mean value inequality with M = 0.
We would like to extend this corollary. Does this corollary extend to diﬀeren-
tiable maps f with Df = 0 deﬁned on any open set U⊆ Rn?
The answer is clearly no. Even for functions f : R→ R, this is not true, since
we can have two disjoint intervals [1, 2]∪ [3, 4], and deﬁne f(t) to be 1 on [1, 2]
and 2 on [3, 4]. Then Df = 0 but f is not constant. f is just locally constant on
each interval.
The problem with this is that the sets are disconnected. We cannot connect
points in [1, 2] and points in [3, 4] with a line. If we can do so, then we would be
able to show that f is constant.
Deﬁnition (Path-connected subset). A subset E⊆ Rn is path-connected if for
any a, b∈E, there is a continuous map γ : [0, 1]→E such that
γ(0) = a, γ (1) = b.
Theorem. LetU⊆ Rn be open and path-connected. Then for any diﬀerentiable
f :U→ Rm, if Df(x) = 0 for all x∈U, then f is constant on U.
A naive attempt would be to replace tb1− (1−t)b2 in the proof of the mean
value theorem with a path γ(t). However, this is not a correct proof, since this
has to assume γ is diﬀerentiable. So this doesn’t work. We have to think some
more.
Proof. We are going to use the fact that f is locally constant. wlog, assume
m = 1. Given any a, b∈U, we show that f(a) = f(b). Let γ : [0, 1]→U be
a (continuous) path from a to b. For any s∈ (0, 1), there exists some ε such
that Bε(γ(s))⊆U since U is open. By continuity of γ, there is a δ such that
(s−δ,s +δ)⊆ [0, 1] with γ((s−δ,s +δ))⊆Bε(γ(s))⊆U.
Since f is constant on Bε(γ(s)) by the previous corollary, we know that
g(t) =f◦γ(t) is constant on (s−δ,s +δ). In particular, g is diﬀerentiable at
s with derivative 0. This is true for all s. So the map g : [0, 1]→ R has zero
derivative on (0, 1) and is continuous on (0, 1). So g is constant. So g(0) =g(1),
i.e. f(a) =f(b).
If γ were diﬀerentiable, then this is much easier, since we can show g′ = 0 by
the chain rule:
g′(t) =Df(γ(t))γ′(t).
6.4 Inverse function theorem
Now, we get to the inverse function theorem. This is one of the most important
theorems of the course. This has many interesting and important consequences,
but we will not have time to get to these.
Before we can state the inverse function theorem, we need a deﬁnition.
70

6 Diﬀerentiation from Rm to Rn IB Analysis II
Deﬁnition (C 1 function). Let U⊆ Rn be open. We say f :U→ Rm is C 1 on
U if f is diﬀerentiable at each x∈U and
Df :U→L(Rn, Rm)
is continuous.
We writeC 1(U) or C 1(U; Rm) for the set of all C 1 maps from U to Rm.
First we get a convenient alternative characterization of C 1.
Proposition. Let U⊆ Rn be open. Then f = (f1,··· ,fn) :U→ Rn is C 1 on
U if and only if the partial derivatives Djfi(x) exists for all x∈U, 1≤i≤n,
1≤j≤n, and Djfi :U→ R are continuous.
Proof. (⇒) Diﬀerentiability of f at x implies Djfi(x) exists and is given by
Djfi(x) =⟨Df(x)ej, bi⟩,
where{e1,··· , en} and{b1,··· , bm} are the standard basis for Rn and Rm.
So we know
|Djfi(x)−Djfi(y)| =|⟨(Df(x)−Df(y))ej, bi⟩|≤‖ Df(x)−Df(y)‖
since ej and bi are unit vectors. Hence if Df is continuous, so is Djfi.
(⇐) Since the partials exist and are continuous, by our previous theorem, we
know that the derivative Df exists. To show Df :U→L(Rm; Rn) is continuous,
note the following general fact:
For any linear map A∈L(Rn; Rm) represented by (aij) so that Ah =aijhj,
then for x = (x1,··· ,xn), we have
‖Ax‖2 =
m∑
i=1
(

n∑
j=1
Aijxj
)

2
By Cauchy-Schwarz, we have
≤
m∑
i=1
(

n∑
j=1
a2
ij
)

(

n∑
j=1
x2
j
)

=‖x‖2
m∑
i=1
n∑
j=1
a2
ij.
Dividing by‖x‖2, we know
‖A‖≤
√∑∑
a2
ij.
Applying this to A =Df(x)−Df(y), we get
‖Df(x)−Df(y)‖≤
√∑∑
(Djfi(x)−Djfi(y))2.
So if all Djfi are continuous, then so is Df.
71

6 Diﬀerentiation from Rm to Rn IB Analysis II
If we do not wish to go through all that algebra to show the inequality
‖A‖≤
√∑∑
a2
ij,
we can instead note that
√∑∑ a2
ij is a norm on L(Rn, Rm), since it is just the
Euclidean norm if we treat the matrix as a vector written in a funny way. So by
the equivalence of norms on ﬁnite-dimensional vector spaces, there is some C
such that
‖A‖≤ C
√∑∑
a2
ij,
and then the result follows.
Finally, we can get to the inverse function theorem.
Theorem (Inverse function theorem). Let U⊆ Rn be open, and f :U→ Rm
be a C 1 map. Let a∈U, and suppose that Df(a) is invertible as a linear map
Rn→ Rn. Then there exists open sets V,W ⊆ Rn with a∈V , f(a)∈W ,V ⊆U
such that
f|V :V →W
is a bijection. Moreover, the inverse map f|−1
V :W→V is also C 1.
We have a fancy name for these functions.
Deﬁnition (Diﬀeomorphism). LetU,U′⊆ Rn are open, then a map g :U→U′
is a diﬀeomorphism if it is C 1 with a C 1 inverse.
Note that diﬀerent people have diﬀerent deﬁnitions for the word “diﬀeomor-
phism”. Some require it to be merely diﬀerentiable, while others require it to be
inﬁnitely diﬀerentiable. We will stick with this deﬁnition.
Then the inverse function theorem says: if f is C 1 and Df(a) is invertible,
then f is a local diﬀeomorphism at a.
Before we prove this, we look at the simple case where n = 1. Suppose
f′(a)⁄= 0. Then there exists aδ such thatf′(t)> 0 orf′(t)< 0 int∈ (a−δ,a +δ).
So f|(a−δ,a+δ) is monotone and hence is invertible. This is a triviality. However,
this is not a triviality even for n = 2.
Proof. By replacing f with (Df(a))−1f (or by rotating our heads and stretching
it a bit), we can assume Df(a) =I, the identity map. By continuity of Df, there
exists some r> 0 such that
‖Df(x)−I‖< 1
2
for all x∈Br(a). By shrinking r suﬃciently, we can assume Br(a)⊆U. Let
W =Br/2(f(a)), and let V = f−1(W )∩Br(a).
That was just our setup. There are three steps to actually proving the
theorem.
Claim. V is open, and f|V :V →W is a bijection.
Since f is continuous, f−1(W ) is open. So V is open. To show f|V :V →W
is bijection, we have to show that for each y∈W , then there is a unique x∈V
such that f(x) = y. We are going to use the contraction mapping theorem to
72

6 Diﬀerentiation from Rm to Rn IB Analysis II
prove this. This statement is equivalent to proving that for each y∈ W , the
map T (x) = x− f(x) + y has a unique ﬁxed point x∈V .
Let h(x) = x− f(x). Then note that
Dh(x) =I−Df(x).
So by our choice of r, for every x∈Br(a), we must have
‖Dh(x)‖≤ 1
2.
Then for any x1, x2∈Br(a), we can use the mean value inequality to estimate
‖h(x1)− h(x2)‖≤ 1
2‖x1− x2‖.
Hence we know
‖T (x1)−T (x2)‖ =‖h(x1)− h(x2)‖≤ 1
2‖x1− x2‖.
Finally, to apply the contraction mapping theorem, we need to pick the right
domain for T , namely Br(a).
For any x∈Br(a), we have
‖T (x)− a‖ =‖x− f(x) + y− a‖
=‖x− f(x)− (a− f(a)) + y− f(a)‖
≤‖ h(x)− h(a)‖ +‖y− f(a)‖
≤ 1
2‖x− a‖ +‖y− f(a)‖
< r
2 + r
2
=r.
So T :Br(a)→Br(a)⊆Br(a). Since Br(a) is complete, T has a unique ﬁxed
point x∈Br(a), i.e. T (x) = x. Finally, we need to show x∈Br(a), since this is
where we want to ﬁnd our ﬁxed point. But this is true, since T (x)∈Br(a) by
above. So we must have x∈Br(a). Also, since f(x) = y, we know x∈f−1(W ).
So x∈V .
So we have shown that for each y∈W , there is a unique x∈V such that
f(x) = y. So f|V :V →W is a bijection.
We have done the hard work now. It remains to show that f|V is invertible
with C 1 inverse.
Claim. The inverse map g = f|−1
V :W→V is Lipschitz (and hence continuous).
In fact, we have
‖g(y1)− g(y2)‖≤ 2‖y1− y2‖.
For any x1, x2∈V , by the triangle inequality, know
‖x1− x2‖−‖ f(x1)− f(x2)‖≤‖ (x1− f(x1))− (x2− f(x2))‖
=‖h(x1)− h(x0)‖
≤ 1
2‖x1− x2‖.
73

6 Diﬀerentiation from Rm to Rn IB Analysis II
Hence, we get
‖x1− x2‖≤ 2‖f(x1)− f(x2)‖.
Apply this to x1 = g(y1) and x2 = g(y2), and note that f(g(yj)) = yj to get
the desired result.
Claim. g is in fact C 1, and moreover, for all y∈W ,
Dg(y) =Df(g(y))−1. (∗)
Note that if g were diﬀerentiable, then its derivative must be given by (∗),
since by deﬁnition, we know
f(g(y)) = y,
and hence the chain rule gives
Df(g(y))·Dg(y) =I.
Also, we immediately know Dg is continuous, since it is the composition of
continuous functions (the inverse of a matrix is given by polynomial expressions
of the components). So we only need to check that Df(g(y))−1 satisﬁes the
deﬁnition of the derivative.
First we check that Df(x) is indeed invertible for every x∈Br(a). We use
the fact that
‖Df(x)−I‖≤ 1
2.
If Df(x)v = 0, then we have
‖v‖ =‖Df(x)v− v‖≤‖ Df(x)−I‖‖v‖≤ 1
2‖v‖.
So we must have‖v‖ = 0, i.e. v = 0. So kerDf(x) ={0}. So Df(g(y))−1 exists.
Let x∈V be ﬁxed, and y = f(x). Let k be small and
h = g(y + k)− g(y).
In other words,
f(x + h)− f(x) = k.
Since g is invertible, whenever k⁄= 0, h⁄= 0. Since g is continuous, as k→ 0,
h→ 0 as well.
We have
g(y + k)− g(y)−Df(g(y))−1k
‖k‖
= h−Df(g(y))−1k
‖k‖
= Df(x)−1(Df(x)h− k)
‖k‖
=−Df(x)−1(f(x + h)− f(x)−Df(x)h)
‖k‖
=−Df(x)−1
(f(x + h)− f(x)−Df(x)h
‖h‖ ·‖h‖
‖k‖
)
=−Df(x)−1
(f(x + h)− f(x)−Df(x)h
‖h‖ ·‖g(y + k)− g(y)‖
‖(y + k)− y‖
)
.
74

6 Diﬀerentiation from Rm to Rn IB Analysis II
As k→ 0, h→ 0. The ﬁrst factor −Df(x)−1 is ﬁxed; the second factor tends
to 0 as h→ 0; the third factor is bounded by 2. So the whole thing tends to 0.
So done.
Note that in the case where n = 1, if f : (a,b )→ R is C 1 with f′(x)⁄= 0 for
everyx, then f is monotone on the whole domain (a,b ), and hence f : (a,b )→
f((a,b )) is a bijection. In higher dimensions, this is not true. Even if we know
that Df(x) is invertible for all x∈U, we cannot say f|U is a bijection. We still
only know there is a local inverse.
Example. Let U = R2, and f : R2→ R2 be given by
f(x,y ) =
(ex cosy
ex siny
)
.
Then we can directly compute
Df(x,y ) =
(ex cosy −ex siny
ex siny e x cosy.
)
Then we have
det(Df(x,y )) =ex⁄= 0
for all (x,y )∈ R2. However, by periodicity, we have
f(x,y + 2nπ) =f(x,y )
for all n. So f is not injective on R2.
One major application of the inverse function theorem is to prove the implicit
function theorem. We will not go into details here, but an example of the theorem
can be found on example sheet 4.
6.5 2nd order derivatives
We’ve done so much work to understand ﬁrst derivatives. For real functions,
we can immediately know a lot about higher derivatives, since the derivative is
just a normal real function again. Here, it slightly more complicated, since the
derivative is a linear operator. However, this is not really a problem, since the
space of linear operators is just yet another vector space, so we can essentially
use the same deﬁnition.
Deﬁnition (2nd derivative). LetU⊆ Rn be open, f :U→ Rm be diﬀerentiable.
Then Df :U→L(Rn; Rm). We say Df is diﬀerentiable at a∈U if there exists
A∈L(Rn;L(Rn; Rm)) such that
lim
h→0
1
‖h‖(Df(a + h)−Df(a)−Ah) = 0.
For this to make sense, we would need to put a norm on L(Rn; Rm) (e.g. the
operator norm), but A, if it exists, is independent of the choice of the norm,
since all norms are equivalent for a ﬁnite-dimensional space.
This is, in fact, the same deﬁnition as our usual diﬀerentiability, since
L(Rn; Rm) is just a ﬁnite-dimensional space, and is isomorphic to Rnm. So Df is
75

6 Diﬀerentiation from Rm to Rn IB Analysis II
diﬀerentiable if and only if Df :U→ Rnm is diﬀerentiable with A∈L(Rn; Rnm).
This allows use to recycle our previous theorems about diﬀerentiability.
In particular, we know Df is diﬀerentiable is implied by the existence of
partial derivativesDi(Djfk) in a neighbourhood of a, and their continuity at a,
for all k = 1,··· ,m and i,j = 1,··· ,n .
Notation. Write
Dijf(a) =Di(Djf)(a) = ∂2
∂xi∂xj
f(a).
Let’s now go back to the initial deﬁnition, and try to interpret it. By linear
algebra, in general, a linear map φ : R𝓁→ L(Rn; Rm) induces a bilinear map
Φ : R𝓁× Rn→ Rm by
Φ(u, v) =φ(u)(v)∈ Rm.
In particular, we know
Φ(au +bv, w) =aΦ(u, w) +bΦ(v, w)
Φ(u,a v +bw) =aΦ(u, v) +bΦ(u, w).
Conversely, if Φ : R𝓁× Rn→ Rm is bilinear, then φ : R𝓁→L(Rn; Rm) deﬁned
by
φ(u) = (v↦→ Φ(u, v))
is linear. These are clearly inverse operations to each other. So there is a
one-to-one correspondence between bilinear maps φ : R𝓁× Rn→ Rm and linear
maps Φ : R𝓁→L(Rn; Rm).
In other words, instead of treating our second derivative as a weird linear
map in L(Rn;L(Rn; Rm)), we can view it as a bilinear map Rn× Rn→ Rm.
Notation. We deﬁneD2f(a) : Rn× Rn→ Rm by
D2f(a)(u, v) =D(Df)(a)(u)(v).
We knowD2f(a) is a bilinear map.
In coordinates, if
u =
n∑
j=1
ujej, v =
n∑
j=1
vjej,
where{e1,··· , en} are the standard basis for Rn, then using bilinearity, we have
D2f(a)(u, v) =
n∑
i=1
n∑
j=1
D2f(a)(ei, ej)uivj.
This is very similar to the case of ﬁrst derivatives, where the derivative can be
completely speciﬁed by the values it takes on the basis vectors.
In the deﬁnition of the second derivative, we can again take h =tei. Then
we have
lim
t→0
Df(a +tei)−Df(a)−tD(Df)(a)(ei)
t = 0.
76

6 Diﬀerentiation from Rm to Rn IB Analysis II
Note that the whole thing at the top is a linear map in L(Rn; Rm). We can let
the whole thing act on ej, and obtain
lim
t→0
Df(a +tei)(ej)−Df(a)(ej)−tD(Df)(a)(ei)(ej)
t = 0.
for all i,j = 1,··· ,n . Taking the D2f(a)(ei, ej) to the other side, we know
D2f(a)(ei, ej) = lim
t→0
Df(a +tei)(ej)−Df(a)(ej)
t
= lim
t→0
Dejf(a +tei)−Dejf(a)
t
=DeiDejf(a).
In other words, we have
D2f(ei, ej) =
m∑
k=1
Dijfk(a)bk,
where{b1,··· , bm} is the standard basis for Rm. So we have
D2f(u, v) =
n∑
i,j=1
m∑
k=1
Dijfk(a)uivjbk
We have been very careful to keep the right order of the partial derivatives.
However, in most cases we care about, it doesn’t matter.
Theorem (Symmetry of mixed partials) . Let U⊆ Rn be open, f :U→ Rm,
a∈U, and ρ> 0 such that Bρ(a)⊆U.
Leti,j ∈{ 1,··· ,n} be ﬁxed and suppose that DiDjf(x) andDjDif(x) exist
for all x∈Bρ(a) and are continuous at a. Then in fact
DiDjf(a) =DjDif(a).
The proof is quite short, when we know what to do.
Proof. wlog, assume m = 1. If i =j, then there is nothing to prove. So assume
i⁄=j.
Let
gij(t) =f(a +tei +tej)−f(a +tei)−f(a +tej) +f(a).
Then for each ﬁxed t, deﬁne φ : [0, 1]→ R by
φ(s) =f(a +stei +tej)−f(a +stei).
Then we get
gij(t) =φ(1)−φ(0).
By the mean value theorem and the chain rule, there is some θ∈ (0, 1) such that
gij(t) =φ′(θ) =t
(
Dif(a +θtei +tej)−Dif(a +θtei)
)
.
77

6 Diﬀerentiation from Rm to Rn IB Analysis II
Now apply mean value theorem to the function
s↦→Dif(a +θtei +stej),
there is some η∈ (0, 1) such that
gij(t) =t2DjDif(a +θtei +ηtej).
We can do the same for gji, and ﬁnd some ˜θ, ˜η such that
gji(t) =t2DiDjf(a + ˜θtei + ˜ηtej).
Since gij =gji, we get
t2DjDif(a +θtei +ηtej) =t2DiDjf(a + ˜θtei + ˜ηtej).
Divide byt2, and take the limit as t→ 0. By continuity of the partial derivatives,
we get
DjDif(a) =DiDjf(a).
This is nice. Whenever the second derivatives are continuous, the order does
not matter. We can alternatively state this result as follows:
Proposition. Iff :U→ Rm is diﬀerentiable in U such that DiDjf(x) exists in
a neighbourhood of a∈U and are continuous at a, then Df is diﬀerentiable at
a and
D2f(a)(u, v) =
∑
j
∑
i
DiDjf(a)uivj.
is a symmetric bilinear form.
Proof. This follows from the fact that continuity of second partials implies
diﬀerentiability, and the symmetry of mixed partials.
Finally, we conclude with a version of Taylor’s theorem for multivariable
functions.
Theorem (Second-order Taylor’s theorem). Letf :U→ R beC 2, i.e.DiDjf(x)
are continuous for all x∈U. Let a∈U and Br(a)⊆U. Then
f(a + h) =f(a) +Df(a)h + 1
2D2f(h, h) +E(h),
where E(h) =o(‖h‖2).
Proof. Consider the function
g(t) =f(a +th).
Then the assumptions tell us g is twice diﬀerentiable. By the 1D Taylor’s
theorem, we know
g(1) =g(0) +g′(0) + 1
2g′′(s)
for some s∈ [0, 1].
78

6 Diﬀerentiation from Rm to Rn IB Analysis II
In other words,
f(a + h) =f(a) +Df(a)h + 1
2D2f(a +sh)(h, h)
=f(a) +Df(a)h + 1
2D2f(a)(h, h) +E(h),
where
E(h) = 1
2
(
D2f(a +sh)(h, h)−D2f(a)(h, h)
)
.
By deﬁnition of the operator norm, we get
|E(h)|≤ 1
2‖D2f(a +sh)−D2f(a)‖‖h‖2.
By continuity of the second derivative, as h→ 0, we get
‖D2f(a +sh)−D2f(a)‖→ 0.
So E(h) =o(‖h‖2). So done.
79

