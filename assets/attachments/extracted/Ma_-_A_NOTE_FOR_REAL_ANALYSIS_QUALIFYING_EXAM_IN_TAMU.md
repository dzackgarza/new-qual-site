A NOTE FOR REAL ANAL YSIS QUALIFYING EXAM IN T AMU
XIN MA
Abstract. This note contains solutions to the questions occurred in past Real
analysis qualifying exams from Jan 2009 to Jan 2017. I did most of them. The
rest are folklore. Typos and errors are inevitable. Comments and corrections
are welcome.
1. January 2017
Problem 1.1. Let (Ω,A,µ ) be a measure space. Show that if for all n, µ{x :
|fn(x)|> 1/n}<n−3/2, then fn→ 0 a.e. (µ).
Proof. Deﬁne M = ⋂∞
m=1
⋃∞
n=m{x :|fn(x)| > 1/n}. Then µ(⋃∞
n=m{x :|fn(x)| >
1/n})≤ ∑∞
n=mn−3/2→ 0 as m→∞ . Then µ(M) = 0. Consider x∈Mc iﬀ there
is a m such that for all n>m ,|fn(x)|≤ 1/n, i.e. fn→ 0 a.e. □
Problem 1.2. Find all f∈L1(1, 2) such that for all n∈N,
∫ 2
1 x2nf = 0.
Proof. We ﬁrstly extendf to be deﬁned on [1, 2] by setting f(1) = 0 and f(2) = 0.
We still denote this function f. Now, f∈ L1[1, 2] and we still have
∫ 2
1 x2nf = 0.
Then, by Stone-Weirtrass theorem, we have for any continuous functiong∈C[1, 2],∫ 2
1 gf = 0. Then use the same argument occurred in problem 2 in Jan 2016. We
can see f = 0 a.e. (µ). □
Problem 1.3.
Problem 1.4. We say a sequence{an} in [0, 1] is equi-distributed if for all interval
[c,d ]⊂ [0, 1], limn→∞
|{a1,...,an} ⋂[c,d]|
n = d−c. Prove that {an} in [0, 1] is equi-
distributed iﬀ limn→∞
∫
fdµn =
∫
fdm for all f∈C[0, 1], where µn = 1
n
∑n
k=1δan
Proof. By the deﬁnition, we see that {an} is equi-distributed iﬀ for all interval
[c,d ]⊂ [0, 1], limn→∞
∫
χ[c,d]dµn =
∫
χ[c,d]dm.
Then if lim n→∞
∫
fdµn =
∫
fdm for all f ∈ C[0, 1]. For any interval [ c,d ],
deﬁne continuous functions 1≥fn≥ 0 (n>N for some proper N) with fn = 1 on
[c,d ] andsupp(fn)⊂ [c−1/n,d +1/n] such thatfn↓χ[c,d]. Then for all ϵ> 0, there
is aK such that wheneverk>K ,µk[c,d ]≤
∫
fndµk≤
∫
fndµ+ϵ≤µ[c,d ]+2/n+ϵ.
Date: Nov 20, 2016.
1

2 XIN MA
Note that this K depend on the interval [ c,d ]. Use this argument for [ c− 1/n,c ]
and [d,d + 1/n], for the ϵ, for each n, there is a Kn such that whenever k >
Kn,
∫
|fn−χ[c,d]|dµk≤
∫
χ[c−1/n,c]dµk +
∫
χ[d,d+1/n]dµk≤ 4/n +ϵ. In addition,∫
|fn−χ[c,d]|dm≤ 2/n also holds. Now, ﬁx a n big enough such that 6 /n < ϵ
and|
∫
fndµk−
∫
fndm| < ϵ. This implies that whenever k > Kn,|
∫
χ[c,d]dµk−∫
χ[c,d]dm|≤
∫
|fn−χ[c,d]|dµk+|
∫
fndµk−
∫
fndm|+
∫
|fn−χ[c,d]|dm≤ 6/n+2ϵ<
3ϵ. We are done.
In the converse, If for all interval [c,d ]⊂ [0, 1], limn→∞
∫
χ[c,d]dµn =
∫
χ[c,d]dm.
Then this pass to all step functions. For any continuous function f∈ C[0, 1], we
can use step functions to approximatef under the norm‖·‖∞. say for every ϵ> 0,
there is a 0 = x0 < x1 < ... < xN = 1 such that for all n≤N,| max
xn≤x≤xn+1
f(x)−
min
xn≤x≤xn+1
f(x)| < ϵ. Now, deﬁne g = ∑N
n=0anχ[xn,xn+1] where an is an arbitrary
number between min
xn≤x≤xn+1
f(x) and max
xn≤x≤xn+1
f(x). Thus ‖g−f‖∞ < ϵ. Now,
for the ϵ, there is a K such that whenever k >K,|
∫
gdµk−
∫
gdm|<ϵ and thus
|
∫
fdµk−
∫
fdm|≤
∫
|fdµk−
∫
gdµk| +|
∫
gdµk−
∫
gdm| +|fdm−
∫
gdm| <
2‖f−g‖∞ +ϵ< 3ϵ. We are done. □
Problem 1.5. Let S be a closed subspace of ( C[0, 1],‖·‖ ∞). If S is also closed
under‖·‖ ∞, then show S is ﬁnite-dimensional. (This is question 66 in Folland on
page 178, see also mathoverﬂow 52509 for other solutions.)
Proof. Consider the identity map id : (S,‖·‖ ∞)→ (S,‖·‖ 2) is bounded since
‖f‖2 ≤ ‖f‖∞ in general (see problem 8 in Jan 2016). Then by open mapping
theorem. ‖·‖ 2 is equivalent to ‖·‖ ∞ on S, say for all f ∈ S,‖f‖∞≤ C‖f‖2.
Note that S is a Hilbert space. Let {fn}n∈I be an orthonormal basis of S. For all
f∈ S, x∈ [0, 1]. The evaluation map δx(f) = f(x) is bounded and linear w.r.t
‖·‖ 2. Indeed,|δx(f)| =|f(x)|≤‖ f‖∞≤C‖f‖2. Then, by Riesz’s lemma, there is
a function gx∈C[0, 1] such that f(x) =⟨f,gx⟩ with‖gx‖≤ C
Thus, ∑
n∈I|f(x)|2 = ∑
n∈I|⟨f,gx⟩|2 =‖gx‖2
2≤C2. Then integration implies
that|I|≤ C2. □
Problem 1.6.
Problem 1.7.
Problem 1.8. (1) Construct a Lebesgue measurable setA⊂R so that for alla<b
0<m (A ⋂[a,b ])<b −a.
(2) Suppose that a Lebesgue measurable setA⊂R so that for alla<b ,m(A ⋂[a,b ])<
(b−a)/2. Prove that m(A) = 0.

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 3
Proof. (1) It suﬃces to show the case A⊂ [0, 1] since then B = ⋃
n∈Zn +A works.
It also suﬃces to consider all intervals with rational endpoints by density of Q.
Now ﬁx an enumeration of all this subintervals of [0, 1], say{In :n∈N}. We deﬁne
sequences of generalized cantor set {Cn} and{Dn} such that (i) m(Cn) > 0 and
m(Dn)> 0; (ii) Cn
⋃Dn⊂In; (iii) ( ⋃n
k=1Ck) ⋂(⋃n
k=1Dk) =∅.
We deﬁne these sequence by induction. If C1,....,C n and D1,....,D n are de-
ﬁned. They are nowhere dense closed sets. Then ⋃n
k=1Ck
⋃Dk is also nowhere
dense closed set (Indeed, if F1 and F2 are nowhere dense. If there is an open set
O⊂ F1
⋃F2, then ∅⁄ = O ⋂Fc
2 = O ⋂Fc
2
⋂F1⊂ F1, which is a contradiction.).
ThenIn+1\⋃n
k=1Ck
⋃Dk is a nonempty open set which is a union of open intervals
and thus contains a generalized cantor set Cn+1 of positive measure. Then, in the
same manner, we can also choose Dn+1⊂In+1\ (⋃n
k=1(Ck
⋃Dk) ⋃Cn+1), which
is of positive measure.
Now, deﬁne A = ⋃
nCn. By the construction, A works.
(2) We also restrict to [0 , 1]. Then for any subinterval I⊂ [0, 1], m(A ⋂I)≤
0.5m(I) implies thatm(Ac ⋂I)≥ 0.5m(I). Then apply problem 1 in Jan 2016. □
Problem 1.9. Prove or disprove that the unit ball of L7(0, 1) is closed in L1(0, 1)
Proof. It is right. Indeed, B1 ={f :‖f‖7≤ 1}. Now, let fn→f inL1, wherefn∈
B1. Then, fn→ f in measure and thus there is a subsequence fnk→ f a.e.(m).
Then|fnk|7→| f|7 a.e.(m). Then, by Fatou’s lemma,
∫
|f|7≤ lim infk
∫
|fnk|7 =
1. □
Problem 1.10. LetC denote the Banach space of all convergent sequences under
the norm‖·‖∞. Compute the extreme points of the unit ballB ofC and determined
that whether B is the closed convex hull of its extreme points.
Proof. Fix a a∈ B, if there is a m such that|a(m)| < 1. then there is a number
δ such that|a(m)−δ|≤ 1 and |a(m) +δ|≤ 1. Now deﬁne b1,b 2∈ B such that
b1(n) =a(n) whenever n⁄=m and b1(m) =a(m) +δ. In the same manner, deﬁne
b2(n) =a(n) whenever n⁄=m and b1(m) =a(m)−δ. Then a = (b1 +b2)/2. Thus
a is not an extreme point.
If for all n, |an| = 1. Let a = (b1 + b2)/2. Since |bi(n)| ≤1 for all n,
b1(n) = b2(n) = a(n), which implies that a is an extreme point. Thus Ext( B) =
{a :∀n, |a(n)| = 1 and∃N,∀n>N a (n)≡ 1 or a(n)≡− 1.}
(Not sure)I thinkconv(Ext(B))⁄=B. Let e0 = (1, 1, 1, 1,.... ),en = (0,.. 0, 1, 0,... )
for n≥ 1. It can be seen that ±en∈ conv(Ext(B)) for all n≥ 0. Consider {en :
n≥ 0} form a basis of C. Then conv(Ext(B)) =B iﬀ ∑k
n=0αnen∈ conv(Ext(B))

4 XIN MA
for 1≥|αn|→ 0. This may induce a contradiction of the convexity. Like consider
(1/n).
□
Problem 1.11. Show that every continuous convex function f deﬁned on the
closed unit ball of a reﬂexive Banach space X can achieve the minimum
Proof. At ﬁrst, Since X is reﬂexive, then X is isomorphic to X∗∗. By Alaoglu’s
theorem, The unit ball of X∗∗ is w∗-compact, which implies that the unit ball of
X, B is weak compact. Then, we know that any function is lower semi-continuous
convex iﬀ it is weak lower-semi continuous convex. (This is a classical result in
convex analysis. The epigraph is used in its proof or Mazur’s lemma?) Thus f
is weak-lower-semi-continuous. Thus it can achieve the minimum since B is weak
compact. □
2. August 2016
Problem 2.1. LetA be the set of all real valued functions on [0 , 1] for which
f(0) = 0 and|f(t)−f(s)|≤ (t−s)2 for 0≤s<t ≤ 1.
(1) Prove thatA is a compact subset of C[0, 1].
(2) Prove thatA is a compact subset of L1[0, 1].
Proof. (1) At ﬁrst, A is closed. Let fn→ f under‖·‖ ∞. Then |f(t)−f(s)|≤
|f(t)−fn(t)|+|fn(t)−fn(s)|+|fn(s)−f(s)| implies thatA is closed. It is also easy
to check thatA is equicontinuous and pointwise bounded. Then by Arzela-Ascoli
theorem,A is compact in C[0, 1].
(2) Consider the identity mapid fromC[0, 1] toL1[0, 1] is continuous by‖f‖1 =∫
|f| ≤ ‖f‖∞. Then A is compact in L1[0, 1] since any continuous image of a
compact set is also compact. □
Problem 2.2. (1) Let f(x) be a real valued function on the real line that is diﬀer-
entiable almost everywhere. Prove that f′(x) is a Lebesgue measurable function.
(2) If f is continuous real values function on the real line, then the set of points at
whichf is diﬀerentiable is measurable.
Proof. f′(x) = limn→∞n(f(x + 1/n)−f(x)) if the limit exists. Then Module a
null set, f′ is measurable. Thus, it is measurable.
For the second part, By the similar argument, We know thatD+f,D−f,D+f
and D−f are measurable. Then {x : f′(x) exsits} ={x : D+f(x) = D−f(x) =
D+f(x) =D−f(x)} is measurable. □

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 5
Problem 2.3. (a) Letf be a real valued function on the unit interval [0, 1]. Prove
that the set of points at which f is discontinuous is a countable union of closed
subsets.
(b) Prove that there is no real valued function on [0 , 1] that is continuous at
all rational points but discontinuous at all irrational points.
Proof. Deﬁne oscf(x) = inf{supz,y∈U|f(z)−f(y)| : U is a nbhd of x}. It is not
hard to see oscf(x) is a continuous function and {x :f is continuous at x} ={x :
oscf(x) = 0} = ⋂∞
n=1{x : oscf(x) < 1/n}, which is a Gδ set. It implies that
{x :f is discontinuous at x} is a Fσ, i.e. a countable union of closed subsets.
For the second part, suppose there is a one. Then {x :f is continuous at x} =
Q is a dense Gδ set, say co-meager, which means that the set Ir of all irrationals
is meager. Since Q is also countable, thus meager, [0, 1] =Q ⨆Ir is also a meager
set. A contradiction to the Baire category theorem. □
Problem 2.4. Let (Ω,A,µ ) be a ﬁnite measure space and ( fn) be a sequence
of measurable functions on X that converges pointwise to zero. Prove that ( fn)
converges in measure to zero. Show that the converse is false for [0, 1] with Lebesgue
measure.
Proof. Fix ϵ> 0, δ >0 and deﬁne An ={x :|fn(x)|≥ ϵ}. For the δ, By Egoroﬀ’s
theorem, there is a measurable set E with µ(E)<δ and fn→ 0 on Ec uniformly,
say, there is a N, whenever n > N, x∈ Ec,|fn(x)| < ϵ. It implies that An⊂ E
and thus µ(An)<δ . It shows that µ(An)→ 0, which means fn→ 0 in measure.
For the second part. A counterexample isfn =χ[j/2k,(j+1)/2k] wheren = 2k+j
with 0≤j <2k and k∈N. □
Problem 2.5. Iff is Lebesgue integrable on the real line, prove that limh→0
∫
R|f(x+
h)−f(x)|dx = 0.
Proof. It suﬃces to show limn→∞
∫
R|f(x +hn)−f(x)|dx = 0 for every (hn)→ 0.
Suppose at ﬁrst that f is continuous, then gn = |f(x +hn)−f(x)| →0 and
gn ≤ |f(x +hn)| +|f(x)| ∈L1(R). Then DCT implies that lim n→∞
∫
R|f(x +
hn)−f(x)|dx = 0. Then in general, since Cc(R) is dense in L1(R), there is a
p∈Cc(R) such that
∫
R|f−p|<ϵ/ 3. Then by the inequality |f(x +hn)−f(x)|≤
|f(x +hn)−p(x +hn)| +|p(x +hn)−p(x)| +|f(x)−p(x)|, we can see that for the ϵ
above, there is a N such that whenever n>N ,
∫
R|f(x +hn)−f(x)|dx<ϵ . Then
we are done. □

6 XIN MA
Problem 2.6. Prove or disprove that there is a sequence (Pn) of polynomials such
that (Pn(t)) converges to one for every t∈ [0, 1] but
∫ 1
0 Pn(t)dt converge to two as
n→∞
Proof. It is not hard to see there is a sequence of continuous functions (fn) satisfying
the statement. Like fn is deﬁned to be≡ 1 on [0, 1− 1/n] and fn be the piecewise
linear function on [1−1/n, 1] which are two line pass points (1-1/n,1), (1-1/2n,2n+1)
and (1, 1). It satisﬁes that fn(t)→ 1 for all t∈ [0, 1] but
∫ 1
0 fn(t)dt≡ 2. Then
for each n, applying Stone-Weirstrass theorem, we can ﬁnd a polynomial Pn with
‖fn−Pn‖∞ < 2−n. It is not hard to check ( Pn) works. □
Problem 2.7. Let (fn) be a uniformly bounded sequence of continuous functions
on [0, 1] that converges pointwise to zero. Prove that 0 is in the norm closure in
C[0, 1] of the convex hull of (fn).
Proof. By Geometrical version of Hahn-Banach theorem,conv{(fn)}
w
= conv{(fn)}
n
.
Then, it suﬃce to verify that 0 ∈ conv{(fn)}
w
. Indeed, by Reisz’s representation
theorem,C[0, 1]∗ =M[0, 1]. Then for all µ∈M[0, 1],|
∫
fndµ|≤
∫
|fn|d|µ|→ 0 by
DCT since (fn) are uniform bounded and converges pointwise to 0. Then (fn)→ 0
in the weak topology and we are done. □
Problem 2.8. Assume that X is a reﬂexive Banach space and φ is a continuous
linear functional on X. Prove that there is a norm one vector x such that φ(x) =
‖φ‖. Give an counterexample in the case X =l1.
Proof. By problem 11 in Jan 2017, we see the Ball B of X is weak compact. It
is also easy to verify that φ is weak continuous since it is norm continuous and so
is|φ|. Then |φ| achieve the max value on B, say there is an element x such that
|φ(x)| = maxy∈B|φ(y)|≥ sup{|φ(y)| :‖y‖≤ 1} =‖φ‖. Thus |φ(x)| =‖φ‖ and
‖x‖ = 1 holds necessarily by |φ(x)|≤‖ φ‖‖x‖. Then we can choose a number eiθ
such that φ(eiθx) =|φ(x)| =‖φ‖ and‖eiθx‖ = 1.
A counterexample: l∗
1 = l∞. Then let f = (1− 1/n)n∈ l∞. Then for every
x = (αn)∈l1 of norm 1,|f(x)| =| ∑
n(1−1/n)αn|≤ ∑
n(1−1/n)|αn|< ∑
n|αn| =
1 =‖f‖. □
Problem 2.9. Suppose that X is a non separable Banach space. Prove that there
is an uncountable subset A of the unit ball of X such that for all x⁄= y ∈ A,
‖x−y‖> 0.9.
Proof. Well, if you are familiar with set theory, you can deﬁne A by transﬁnite
recursion by applying Reisz’s lemma, i.e. Problem 5 in Jan 2016.

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 7
Indeed, we choose any norm one element x0 to start. Assume we have deﬁned
{x0,...,x α}, where α is a countable ordinal i.e. α < ω1 such that xβ⁄=xγ implies
that‖xβ−yγ‖ > 0.9. To deﬁne xα+1, Let Y = Q− span{xβ : 0 ≤ β≤ α} is a
proper Banach subspace of X since X is non separable. Then, by Problem 5(a)
in Jan 2016, we can choose a xα+1 of norm 1 such that ‖xα+1−xβ‖> 0.9 for all
β≤α.
Now, If we have deﬁned {x0,...,x β : β < α} and α < ω1 is a limit ordinal.
To deﬁne xα, in the same manner, ﬁrstly deﬁne Y =Q− span{xβ : 0≤ β < α},
which is a proper Banach subspace of X and we can pick up xα of norm 1 such
that‖xα−xβ‖> 0.9 for all β <α.
Now let A ={xα :α<ω 1} works. □
Problem 2.10. If A is a Borel subset of the line. Then E ={(x,y ) : x−y∈A}
is a Borel subset of the plane. If m(A) = 0, then m×m(E) = 0.
Proof. f :R2→R by f(x,y ) = x−y is continuous. Thus, E = f−1(A) is Borel.
Ey ={x∈R : (x,y )∈E} =y +A which is a null set since m(y +A) =m(A) = 0.
Thusm×m(E) =
∫
m(Ey)dm(y) = 0. □
3. January 2016
Problem 3.1. Let E be a measurable subset of [0 , 1]. Suppose there exists α∈
(0, 1) such that m(E ⋂J)≥ α·m(J) for all subintervals J of [0, 1]. Prove that
m(E) = 1.
Proof. For any open subset U of [0, 1], U =⊔∞
i=1Ji for countable many open in-
tervals Ji. It implies that m(E ⋂U) = ∑m(Ji
⋂E) ≥ α· ∑m(Ji) = m(U).
So if m(E) < 1, say, m(Ec) = a > 0. For all ϵ > 0, Let U be open such that
m(U−Ec) = m(U∩E) < ϵ. But ϵ > m(U∩E)≥ αm(U)≥ αa. A contradic-
tion. □
Problem 3.2. let f,g ∈ L1([0, 1]). Suppose
∫ 1
0 xnf(x)dx =
∫ 1
0 xng(x)dx for all
integersn≥ 0. Prove that f =g a.e.
Proof. Let h = f−g. By the assumption,
∫ 1
0 p(x)h(x)dx = 0 for all polynomial
p(x) on [0, 1]. Then, by Stone-Weirstrass theorem, for all continuous function u on
[0, 1],
∫ 1
0 uh = 0. Now, suppose there is a measurable set E which is not a null
set, such that h⁄= 0 on E. Without loss of generality, we may assume h >0 on
E by replacing E with E+ ={x∈E : h >0} or replacing h with−h and E with
E− ={x∈ E : h < 0}. We may also assume h is bounded on E, say, h < m
for some m∈ N. Indeed, since h∈ L1, E∞ ={x∈ E : h =∞} is null. Then

8 XIN MA
consider E = ⋃∞
m=1{x∈ E : h < m} ⋃E∞. There is a m such that Em is not
null and replace E by this Em. It also implies that
∫
Eh > 0. Then, we know
E can be approximated by a ﬁnite union of open intervals, say, for every ϵ > 0,
there is a A = ⨆n
i=1Ii such that µ(E∆A) < ϵ. Thus, we have
∫
Ah > 0 since
|
∫
Eh−
∫
Ah|≤
∫
E∆Ah≤mµ(E∆A)<mϵ . Then, ﬁx a continuous function u such
that u = 1 on A. It implies that
∫
Auh>
∫
Ah> 0. A contradiction. □
Problem 3.3. Let f,g
Problem 3.4. Let{gn} be a sequence of measurable functions on [0 , 1] such that
(1)|gn(x)|≤ C for a.e.x∈ [0, 1] and (2) lim n→∞
∫a
0 gn = 0 for every a∈ [0, 1].
Prove that for each f∈L1[0, 1], we have limn→∞
∫ 1
0 fgn = 0
Proof. By some standard approximation argument, we can seeS = span{χ[0,a] : 0≤
a≤ 1} is dense inCc([0, 1]) with respect toL1−norm. Furthermore, since Cc([0, 1])
is also dense in L1[0, 1] with respect to L1−norm, S is also dense in L1[0, 1] with
respect to L1−norm. Then, for every f ∈ L1[0, 1], there is a sequence hm =
∑Km
i=1k(m)
i χ[0,ai]→f. Then, by (2), for every m, limn→∞
∫ 1
0 hmgn = 0. Then, for
everyϵ, choose a m such that‖hm−f‖1 <ϵ . Then for such m, there is a N such
that whenever n>N ,|
∫ 1
0 hmgn|<ϵ . It implies that |
∫ 1
0 fgn|≤|
∫ 1
0 (f−hm)gn| +
|
∫ 1
0 hmgn|≤ C‖hm−f‖1 +ϵ≤ (C + 1)ϵ. Then we are done. □
Problem 3.5. (a) LetX be a normed vector space andY be a closed liner subspace
of X. Assume Y is a proper subspace, that is, Y ⁄= X. Show that, for arbitrary
ϵ∈ (0, 1), there is an element x∈X such that‖x‖ = 1 and infy∈Y‖x−y‖> 1−ϵ.
(b) Use part (a) to prove that, if X is an inﬁnite dimensional normed vector
space, then the unit ball of X is not compact.
Proof. For allϵ, and ax /∈Y , infy∈Y‖x−y‖ =d> 0. Now, choose aδ >0 such that
d
d+δ > 1−ϵ. For thisδ, choosey0∈Y such that‖x−y0‖<d +δ. Deﬁne u = x−y0
‖x−y0‖.
Then‖u‖ = 1 and‖u +Y‖ = infy∈Y‖ x−y0
‖x−y0‖−y‖ = ‖x+Y‖
‖x−y0‖ > d
d+δ > 1−ϵ.
IfX is inﬁnite dimensional, we can choose a sequence{xn} by induction in the
unit ball. We begin with any element x1 in the unit ball. Then If {x1,x 2,...,x n−1}
has been deﬁned, then by (a), there is an elementxn of norm 1 such that‖xn+Y‖>
1
2 where Y = span{x1,...,x n−1}. Then {xn} witnesses that the unit ball is not
compact since‖xn−xm‖> 1
2 for all n,m . □
Problem 3.6. Let{fk} be a sequence of increasing functions on [0 , 1]. Suppose
∑∞
k=1fk(x) converges for all x∈ [0, 1]. Denote the limit function by f. Prove that
f′(x) = ∑∞
k=1f′
k(x) a.e. x∈ [0, 1].

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 9
Proof. n(f(x + 1/n)−f(x)) = n ∑
k(fk(x + 1/n)−fk(x))≥ n ∑
k
∫x+1/n
n f′
k =
n
∫x+1/n
x
∑
kf′
k since eachf′
k is positive. Then, we know that limn→∞n
∫x+1/n
x
∑
kf′
k =
∑
kf′
k(x), which implies that f′(x)≥ ∑
kf′
k(x). In the converse, ﬁx x∈ [0, 1]. S-
ince fk and f are increasing, then the points that fk and f are not continuous
are countable. Now, choose hn↓ 0 and deﬁne A ={x,x +hn : n∈N} on which
fk and f are continuous. A is closed and thus compact. Let gm(x) = ∑m
k fk(x).
W.L.O.G, we may assumefk≥ 0 by replacingfk withfk−fk(0). Then gm > 0 and
gm↑ f on A. Deﬁne σ(hn) = f(x+hn)−f(x)
hn
and σm(hn) = gm(x+hn)−gm(x)
hn
, which
are deﬁned on A−x ={0,hn : n∈ N}, which is also compact. It can be veriﬁed
thatσ and allσm are continuous onA−x andσm↑σ onA−x and thus uniformly
by Dini’s theorem. It implies that for every ϵ, there is a M such that whenever
m > Mand all n∈N, σ(hn) < σm(hn) +ϵ. Take a limit with respect to n, we
havef′(x)≤g′
m(x) +ϵ = ∑m
k f′
k(x) +ϵ≤ ∑∞
k f′
k(x) +ϵ. Thus, f′(x)≤ ∑
kf′
k(x).
The following argument may be helpful to simplify the proof above but it lacks
some uniform bound of v(k,x ) with respect to k now in order to apply DCT. f′
k(x)
is a good candidate but not good enough. See below.
Fix x∈ [0, 1]. Deﬁne u(k,x ) = fk(x) and let δ be the counting measure on
N. Then f(x) = ∑
kfk(x) =
∫
Nu(k,x )dδ(k). Let hn↓ 0. Also deﬁne vn(k,x ) =
u(k,x+hn)−u(k,x)
hn
. By deﬁnition, vn(k,x )→ f′
k(x). Furthermore, f(x+hn)−f(x)
hn
=∫
N
u(k,x+hn)−u(k,x)
hn
dδ(k) =
∫
Nvn(k,x )dδ(k). It implies thatf′(x) = limn
∫
Nvn(k,x )dδ(k).
If we can apply DCT, then we are done. □
Problem 3.7. Suppose f,g : [0, 1]→R are both continuous and of bounded vari-
ation. Show that the set {(f(t),g (t))∈R2 : t∈ [0, 1]} cannot cover the entire unit
square [0, 1]× [0, 1].
Proof. Deﬁne r(t) = ( f(t),g (t)). Then since on R2, l2
1 norm is equivalent to l2
2
norm, r is a R2-valued function of BV, say whenever 0 = x0 < x1 < ... < xn =
b, ∑n
i=1‖r(xi)−r(xi−1)‖2 <∞. Suppose [0 , 1]× [0, 1] can be covered. Divide
[0, 1]× [0, 1] into n2− 1 small squares, with center zj, in which the length of each
edge is 1/n. Then, we can choosetj such thatr(tj) =zj and reordertj in increasing
order i.e. s1 < s2 < ... < sn2. Then, ∑n2−1
j=1 ‖r(sj)−r(sj+1)‖2≥ ∑n2−1
j=1 1/n =
(n2− 1)/n =n− 1/n→∞ . A contradiction. □
Problem 3.8. (a) Suppose f is a measurable function on [0 , 1], then ‖f‖L∞ =
limp‖f‖Lp.
(b) If fn≥ 0 and fn→f in measure, then
∫
f≤ lim inf
∫
fn.
Proof. (a) By H¨ older, assuming 1≤ p < q <∞, we have ‖f‖p
p =
∫
|f|p· 1≤
‖|f|p‖q
p
·‖ 1‖ q
q−p
=‖f‖p
q·µ([0, 1])
q−p
q , which implies that ‖f‖p≤‖ f‖q. If q =∞,

10 XIN MA
‖f‖p
p =
∫
|f|p ≤‖ f‖∞·µ([0, 1]). Thus, we see ‖f‖p is increasing and bounded
by‖f‖∞. for all ϵ, let E ={x:|f(x)| >‖f‖∞−ϵ}. Then, ‖f‖p
p ≥
∫
E|f|p ≥
(‖f‖∞−ϵ)pµ(E). Then, ‖f‖p≥ µ(E)
1
p (‖f‖∞−ϵ). Now, let p→∞ , we have
lim‖f‖p≥‖f‖∞−ϵ, which implies that limp‖f‖p =‖f‖∞
(b) For the lim infn
∫
fn, we can choose a sequence
∫
fnk such that limk
∫
fnk =
lim infn
∫
fn. Since fn → f in measure, fnk → f in measure. Then there is a
subsequence fnkm converging to f a.e. This implies that
∫
f =
∫
limmfnkm ≤
limm
∫
fnkm = lim infn
∫
fn by Fatou’s lemma. □
Problem 3.9. Suppose{fn} is a sequence of functions inL2[0, 1] such that‖fn‖2≤
1. If fn→f in measure, then
(a) f∈L2[0, 1];
(b) fn→f weakly in L2;
(c) fn→f w.r.t norm in Lp for 1≤p< 2
Proof. (a) Since fn→ f in measure, there is a subsequence fnk converging to f
a.e. Then
∫
|f|2≤ lim inf
∫
|fnk|2≤ 1.
(b)fn→f in measure. Then, for all h∈L2[0, 1],fnh→fnh in measure, thus
cauchy in measure. Let Am,n ={x:|fn(x)h(x)−fm(x)h(x)|≥ ϵ}. Then,
∫ 1
0|fnh−
fmh| =
∫
Am,n
|fnh−fmh| +
∫
[0,1]\Am,n
|fnh−fmh|≤
∫
Am,n
|fnh| +
∫
Am,n
|fmh| +
ϵµ([0, 1]\Am,n). Then, for allϵ, there is aδ such that wheneverµ(A)<δ ,
∫
A|fnh|≤
(
∫
A|fn|2·
∫
A|h|2)
1
2≤ (
∫
A|h|2)
1
2 . Now, choose N big enough, such that m,n > N
implies that µ(Am,n)<δ . Thus, m,n>N also implies that
∫ 1
0|fnh−fmh|≤ 3ϵ.
Thus,fnh is cauchy inL1[0, 1], and thus converges to someg. Meanwhile, fnh→g
in measure, which implies that g =fh and thus|
∫
fnh−
∫
fh|≤
∫
|fnh−fh|→ 0.
Thus,fn→f weakly in L2.
(c) Deﬁne En ={x:|fn(x)−f(x)|≥ ϵ}. By the problem 1.8(a), ‖fn‖p≤
‖fn‖2 ≤ 1 and ‖f‖p ≤ ‖f‖2 ≤ ∞. Then,
∫
En
|fn− f|p +
∫
Ecn
|fn− f|p ≤
2p(
∫
En
|fn|p +
∫
En
|f|p) +ϵµ(Ec
n). It remains to show that ‖fn‖p are uniformly
integrable(see the Hint in the original problem). Indeed, by H¨ older,
∫
‖fn‖p·χA≤
‖|fn|p‖ 2
p
·‖χA‖ 2
2−p
=‖fn‖p
2·µ(A)
2
2−p ≤ µ(A)
2
2−p , which shows that ‖|fn|p‖ are
uniformly integrable. □
Problem 3.10. Suppose E is a measurable subset of [0, 1] with Lebesgue measure
m(E) = 99 /100. Show that there is a x ∈ [0, 1] such that for all r ∈ (0, 1),
m(E ⋂(x−r,x +r))≥r/4.
Proof. For any subset A⊂ [0, 1], the Hardy-Littlewood Maximal function of χA is
MχA(x) = supr>0
1
2r
∫x+r
x−r χA = supr
1
2rm(A ⋂(x−r,x +r)). Now, suppose that
the conclusion is not right, for every x∈ [0, 1], there is a rx such that m(E ⋂(x−

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 11
rx,x +rx)) ≤ rx/4 i.e. 1
2rx
m(E ⋂(x−rx,x +rx)) ≤ 1/2, which implies that
1
2rx
m(Ec ⋂(x−rx,x +rx))≥ 1/2. Let f =χEc. Then, for everyx∈ [0, 1],Mf (x)≥
1/2. However, m{x: Mf (x)≥ 1/2}≤ 6
∫
χEc = 3/50. A contradiction. □
4. August 2015
Problem 4.1. Let f :R→ R be a Borel measurable function. For each t∈ R,
deﬁneft(x) =f(t +x). Prove ft(x) is a Borel measurable function for each ﬁxed t.
Proof. f−1
t ((−∞,a )) ={x: x+t∈f−1((−∞,a ))} =f−1((−∞,a ))−t is Borel. □
Problem 4.2. justify the statement that
∫ 1
0
∫ 1
0
(x−y) sin(xy)
x2+y2 dxdy =
∫ 1
0
∫ 1
0
(x−y) sin(xy)
x2+y2 dydx.
Proof. To apply the Fubini’s thm, it suﬃces to show
∫ 1
0
∫ 1
0| (x−y) sin(xy)
x2+y2 |dxdy <∞.
We integrate this on the quarter of a disk of radius
√
2 in the ﬁrst quadrant, which
contains [0, 1]×[0, 1]. We see that
∫ π
2
0
∫√
2
0 |r cos(θ)−r sin(θ)
r2 |rdrdθ≤ 2
∫ π
2
0
∫√
2
0 drdθ =√
2π. □
Problem 4.3. Assume that{fn} is a sequence in C[0, 1]. Show that:
(a) (fn) converges weakly to 0 iﬀ (fn) is bounded inC[0, 1] and limn→∞fn(t) =
0 for all t∈ [0, 1].
(b) If (fn) converges weakly inC[0, 1], then it converges in norm in Lp[0, 1] for
all 1≤p< ∞.
Proof. Consider C[0, 1]∗ =M[0, 1].
(a) If fn→ 0 weakly, then, for all µ∈ M[0, 1],
∫
fndµ→ 0. In particular,
µ = δt, t∈ [0, 1], implies that fn(t)→ 0. If we view fn∈ M[0, 1]∗, then fn(µ) =
µ(fn)→ 0. Then supn|fn(µ)|<∞, which supn‖fn‖<∞ by Principle of uniform
boundedness theorem. In the converse, by DCT, |
∫
fndµ|≤
∫
|fn|d|µ|→ 0.
(b) W.L.O.G, we may assume fn→ 0 weakly, then by (a), |fn(t)|p→ 0 and
(|fn|p) is bounded. Then DCT implies that fn→ 0 in Lp. □
Problem 4.4. Let A be a Lebesgue null set in R. Prove that B ={ex : x∈A} is
also a null set.
Proof. f(x) = ex is absolutely continuous on any interval [ a,b ] since f is diﬀeren-
tiable on [a,b ] and|f(x)−f(y)|≤ M|x−y|, where M = eb and x,y ∈ [a,b ]. At
ﬁrst, assume that A⊂ [a.b]. A⊂ On, where On is a sequence of open sets such
that m(On)→ 0. Let On = ⨆∞
i=1Ii,n. Then f(A)⊂f(On) = ⨆∞
i=1f(Ii,n), which
implies that m(f(A))≤ ∑∞
i=1m(f(Ii,n))≤ M ∑∞
i=1m(Ii,n) = M·m(On)→ 0.
Then m(f(A)) = 0. If A is not bounded. Deﬁne An = A ⋂[n,n + 1) for all
n∈Z. A = ⨆
nAn. By the argument above m(f(An)) = 0 and thus m(f(A)) =
∑
nm(f(An)) = 0. □

12 XIN MA
Problem 4.5. (b) Show that if f and g are absolutely continuous on [ a,b ], then
so does f·g.
(c) Give an example to show that ( b) is false if [a,b ] is replaced by R.
Proof. (b) Sincef,g are continuous on [a,b ], thus bounded byM andN, respective-
ly. Then, for all ϵ there is a δ such that whenever ∑n
i=1|xi−yi|<δ , ∑n
i=1|f(xi)−
f(yi)|<ϵ/ 2N and ∑n
i=1|g(xi)−g(yi)|<ϵ/ 2M. Thus ∑n
i=1|f(xi)g(xi)−f(xi)g(yi)| =
∑n
i=1|f(xi)g(xi)−f(xi)g(yi) +f(xi)g(yi)−f(xi)g(yi)|≤ M ∑n
i=1|g(xi)−g(yi)| +
N ∑n
i=1|f(xi)−f(yi)| =ϵ
(c) f(x) = g(x) = x are absolutely continuous on R. However, for all δ >0,
choose disjoint intervals Ii = (mi,mi +δi) for i = 1, 2,...,n such that ∑
iδi = δ,
mi < mi+1 and m1δ≥ 1/2. then ∑n
i=1|f(mi +δi)g(mi +δi)−f(mi)g(mi)| =
∑n
i=1|m2
i + 2miδi +δ2
i−m2
i|≥ 2 ∑n
i=1miδi≥m1δ≥ 1/2 □
Problem 4.6. LetX,Y be Banach spaces andT : X→Y be a one-to-one, bounded
and linear operator for which the range T (X) is closed in Y . Show that for each
continuous linear functionalφ onX there is a continuous linear functional ψ onY ,
so that φ =ψ◦T .
Proof. By open mapping theorem, φ◦T−1 is a well-deﬁned linear bounded func-
tional on T (X). Then, by Hahn-Banach Thm, it can be extent to some ψ on Y ,
say,y∈T (X) implies that φ◦T−1(y) = ψ(y). It implies that ψ(T (x)) = φ(x) for
all x∈X. □
Problem 4.7. Derive Open Mapping Theorem from the Closed Graph Theorem.
Proof. Let T : X → Y surjective, continuous linear. Deﬁne the quotient map
T′ : X/ ker(T )→Y byT′(x+ker(T )) =T (x). We show that T′ is an isomorphism.
At ﬁrst. ‖T′(x + ker(T ))‖ =‖T (x +y)‖≤‖ T‖‖x +y‖ for all y∈ ker(T ), which
implies that‖T′‖≤‖ T‖. In the converse, consider T−1. Let T (xn)→ T (x) and
xn +ker(T )→y +ker(T ), say,‖xn−y +ker(T )‖→ 0. For all n, choosezn∈ ker(T )
s.t.‖xn+zn−y‖−2−n≤‖xn−y+ker(T )‖→ 0. Thus T (xn) =T (xn+zn)→T (y).
Then T (xn)→T (x) implies that T (x) = T (y) and thus x + ker(T ) = y + ker(T ).
By Closed Graph theorem, T′ is an isomorphism, and T = T′P , where P is the
projection from X to X/ ker(T ), which is an open map. Then, T (O) = T′(P (O))
is open for all open subset of X. □
Problem 4.8. Let Y be a closed subspace of a Banach space X, with norm‖·‖ .
Let|||·|||be a norm on Y which is equivalent to‖·‖ , meaning that there is a C≥ 1
so that for all y∈Y :
1
C|||y|||≤‖ y‖≤ C|||y|||.

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 13
Let S be the set of all linear functionals ψ : X→R, so that
|ψ(y)|≤||| y|||for all y∈Y and
‖ψ(x)‖≤‖ x‖ for all x∈X.
Prove the following statements:
(1) ||||a||||: = sup ψ∈S|ψ(x)| deﬁnes a norm on X.
(2) ||||y||||=|||y|||for y∈Y .
(3) The norm ||||·||||and‖·‖ are equivalent on X.
Proof. (1) easy to verify.
(2) Fory∈Y , by deﬁnition of||||·||||,||||y||||≤|||y|||.
In the converse, choose a φ∈ (Y,|||·|||)∗, s.t. φ(y) =|||y|||and norm of φ is 1. Thus
for all y∈ Y ,|φ(y)|≤||| y|||≤ C‖y‖. Then, φ can be extent to whole X with the
same norm, say for all x∈X,|φ(x)|≤ C‖x‖. Then φ∈S and thus||||y||||≥|||y|||.
(3) By def of ||||·||||,||||x||||≤ C‖x‖. In the converse, for all x∈ X, by Hahn-
Banach theorem, there is a φ s.t. φ(x) = ‖x‖, and ‖φ‖ = 1. Deﬁne ψ = 1
Cφ,
which implies that ψ(x) = 1
C‖x‖ and‖ψ(z)‖≤ 1
C‖z‖≤ C‖z‖ for all z∈ X while
‖ψ(y)‖≤ 1
C‖y‖≤||| y|||for all y∈Y . Thus ψ∈S and thus||||x||||≥ 1
C‖x‖. □
Problem 4.9. Let f be increasing on [0, 1] and let
g(x) = lim sup
h→0
f(x +h)−f(x−h)
2h , x ∈ (0, 1).
Prove that if A ={x∈ (0, 1): g(x)> 1}, then f(1)−f(0)≥m∗(A).
Proof. For allx∈A, for all δ >0, there is a hδ s.t.|hδ|<δ and f(x+hδ)−f(x−hδ)
2hδ
>
1. Now, we consider closed intervals Iδ
x centered at x of radius hδ, then{Iδ
x : x∈
A,δ >0} form a Vitali cover of A. By Vitali’s Lemma. For ϵ> 0, there is{Iδi
xi}n
i=1
such that ∑n
i=1l(Iδi
xi)>m∗(A)−ϵ and Iδi
xi
⋂Iδj
xj =∅. Then
f(1)−f(0)≥
n∑
i=1
(f(xi +hδi)−f(xi−hδi))≥
n∑
i=1
2hδi =
n∑
i=1
l(Iδi
xi)>m∗(A)−ϵ,
which implies that f(1)−f(0)≥m∗(A). □
Problem 4.10. Let A be a uniformly dense subspace of C[0, 1] and let B =
{F (x): F (x) =
∫x
0 f(t)dt, 0 ≤ x ≤ 1,f ∈ A}. Prove B is uniformly dense in
C0[0, 1] ={g∈C[0, 1]: g(0) = 0}. And prove that the span of {sin(nx): n∈N} is
dense in C0[0, 1].
Proof. Let B′ ={F (x): F (x) =
∫x
0 f(t)dt, 0≤ x≤ 1,f ∈ C[0, 1]}. Firstly, B is
dense in B′. Indeed, Let F ∈ B′ and G∈ B. F (x)−G(x) =
∫x
0 (f(t)−g(t))dt
implies that‖F−G‖∞≤
∫ 1
0|f(t)−g(t)|dt≤‖f−g‖∞. Then, since A is dense in
C[0, 1], B is dense in B′.

14 XIN MA
B′ is an algebra. Let F,G ∈B′, say, F (x) =
∫x
0 f(t)dt and G(x) =
∫x
0 g(t)dt.
Then, F (x)·G(x) =
∫x
0 (F (t)g(t) +G(t)f(t))dt∈B′. B′ also separate points since
x =
∫x
0 1dt∈ B′. Then, by Stone-Weirstrass theorem, B′ is dense in C0[0, 1] and
thus so does B
sin(nx) =
∫x
0 n cos(nt)dt. Then by the argument above, it suﬃces to show that
A = span{n cos(nt)} = span{cos(nt)} is dense inC[0, 1]. Indeed, cos(mt) cos(nt) =
1
2(cos(|m−n|t) + cos((m +n)t))∈ A and 1 = cos(0 ·t)∈ A separates points on
[0, 1]. Then Stone-Weirstrass thm implies that A is dense in C[0, 1]. □
5. January 2015
Problem 5.1. Let f∈ L1(R). If
∫b
a f(x)dx = 0 for all rational numbers a < b,
prove that f = 0 a.e. in R.
Proof. For all c < d∈ R, let an ↓ c and bn ↑ d, where an,bn ∈ Q. Deﬁne
fn = f·χ[an,bn], then fn→ f·χ[c,d]. In addition, |fn|≤| f|∈ L1. Then, DCT
implies that
∫
[an,bn]f→
∫
[c,d]f = 0. Then, if µ({x: f(x)⁄= 0})> 0, we may assume
µ({x: f+(x)⁄= 0})> 0 by f =f+ or f =−f− wheneverf⁄= 0 . Then, there is a
n∈N such thatEn ={x: f+(x)> 1/n} is of positive measures> 0. Forϵ =s/3n,
there is a δ1 such that if µ(A)<δ 1,|
∫
Afdµ|<ϵ . Let δ = min{s/3,δ 1}, then there
is an open set A = ⨆m
1 Ii such that µ(A∆ En) < δand thus µ(A ⋂En)≥ s−δ.
Then,
∫
Afdµ =
∫
A ⋂En
f+dµ+
∫
A\En
fdµ≥ 1
n(s−δ)−ϵ≥ s
3n > 0. A contradiction
to
∫
Af = ∑m
i=1
∫
Ii
fdµ = 0. □
Problem 5.2. Let{gn} andg be L1(R) and satisfy limn→∞‖gn−g‖1 = 0. Prove
that there is a subsequence of gn that converges pointwise to g a.e.
Proof. Let Eϵ,n ={x:|gn(x)−g(x)| > ϵ}. Then ϵµ(Eϵ,n)≤
∫
Eϵ,n
|gn−g|→ 0.
Then for any ϵ > 0, for all δ > 0, there is a N such that whenever n > N,
µ(Eϵ,n) < δ. Then, we choose {nm} by induction such that µ(Fm) < 2−m, where
Fm ={x:|gnm(x)−g(x)|> 2−m}. Now, deﬁne Dk = ⋃∞
m=kFm andD = ⋂∞
k=1Dk.
Since µ(Dk)≤ ∑∞
m=k 2−m→ 0 , µ(D) = 0. Now, x∈ Dc iﬀ there is a k∈ N,
wheneverm≥k,|gnm(x)−g(x)|< 2−m. Then we are done. □
Problem 5.3. Let (X,M,µ ) be a measure space with µ(X) <∞. Let N ⊂M
be a σ-algebra. If f≥ 0 isM-measurable and µ-integrable then prove that there
exists anN -measurable and µ-integrable function g≥ 0 so that
∫
E
gdµ =
∫
E
fdµ, E ∈N .
Proof. Deﬁne ν(E) =
∫
Efdµ is a measure on M. Then ν ≪ µ. Then ν|N ≪
µ|N . Then there is a g, which is N -measurable, such that ν(E) =
∫
Egdν by

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 15
Radon-Nikodym Theorem. In addition, ν(X) =
∫
Xfdµ <∞ implies that g is
µ-integrable. □
Problem 5.4. If H is a Hilbert space and T ∈ L(H) satisfying that ⟨Tx,y⟩ =
⟨x,Ty⟩ for all x,y∈H, then prove that T is bounded.
Proof. Let xn→ x and Txn→ y, we show that Tx = y. Indeed, for all u∈ H.
|⟨xn,Tu⟩−⟨x,Tu⟩| =|⟨xn−x,Tu⟩|≤‖ xn−x‖‖Tu‖→ 0 and⟨Txn,u⟩→⟨ y,u⟩ by
the same argument. Thus⟨Tx,u⟩ =⟨y,u⟩ for allu∈H. Then⟨Tx−y,Tx−y⟩ = 0,
by replacing u by Tx−y, which implies that Tx = y. Then Closed Graph Thm
implies that T is bounded. □
Problem 5.5. Letf,g ∈L1(R). Prove that h∈L1(R), whereh(x) =
∫
Rf(y)g(x−
y)dy whenever this integral is ﬁnite.
Proof.|h(x)|≤
∫
R|f(y)||g(x−y)|dy. Then, by Tonelli,
∫
R|h(x)|dx≤
∫
R(
∫
R|f(y)||g(x−
y)|dy)dx =
∫
R(
∫
R|f(y)||g(x−y)|dx)dy =
∫
R|g|·
∫
R|f|<∞ □
Problem 5.6. Let f,g ∈C[0, 1] with f(x)<g (x) for all x∈ [0, 1].
(1) Prove there is a polynomial p(x) so that
f(x)<p (x)<g (x), x ∈ [0, 1].
(2) Prove that there is an increasing sequence of polynomials {pn(x)} so that
f(x)<p n(x)<g (x), x ∈ [0, 1]
and pn→g uniformly on [0, 1].
Proof. g−f ∈ C[0, 1] and thus deﬁne k = minx∈[0,1](g(x)−f(x)) > 0. Then,
by Stone-Weirstrass Thm, there is a polynomial h such that ‖f−h‖∞ < k/2,
which implies that for all x∈ [0, 1], f(x) < h(x) +k/2 and g(x)−h(x) = g(x)−
f(x) +f(x)−h(x)>k/ 2, which implies that f(x)<h (x) +k/2<g (x) and deﬁne
p(x) =h(x) +k/2.
For (2), deﬁne by induction, choose p1 such that f(x) < p1(x) < g(x) and if
f(x)≤ g(x)− k
2n ≤ pn(x) < g(x). Choose a pn+1 such that g(x) > pn+1(x)≥
max{g(x)− 1
2n+1,pn(x)} □
Problem 5.7. If f ∈ L2(R), g∈ L3(R) and h∈ L6(R), then prove that fgh ∈
L1(R)
Proof.|f(x)g(x)h(x)|≤ 1
2|f(x)|2 + 1
2|g(x)h(x)|2, while |g(x)h(x)|2≤ ( 2
3|g(x)|3 +
1
3|h(x)|6). This implies that|f(x)g(x)h(x)|≤ 1
2|f(x)|2 + 1
3|g(x)|3 + 1
6|h(x)|6. Then,∫
|f(x)g(x)h(x)|dx≤ 1
2
∫
|f(x)|2dx + 1
3
∫
|g(x)|3dx + 1
6
∫
|h(x)|6dx< ∞. □

16 XIN MA
Problem 5.8. (1) Y is metric space. Prove y∈ Y is isolated iﬀ the complement
{y}c is not dense in Y
(2) Let X be a countable nonempty complete metric space. Prove that the set
of isolated points is dense in X.
Proof. If{y} is open, then{y} ⋂{y}c =∅, which implies that{y}c is not dense. In
the converse,{y}c being not dense implies that there is an open set O such that
{y}c ⋂O =∅. Then {y} =O and thus y is an isolated point.
For (2), If not, there is an open set O such thatO ⋂{y∈X : yis isolated} =∅.
It is not hard to see since X is complete, O itself is a Baire space, say, given a
sequence On⊂O, in which memebers On are open and dense in O, then ⋂
nOn is
also dense in O (consider Un = On
⋃O
c
). Then, for all y∈ O, y is not isolated.
It implies that O\{ y} is dense in O. Then by Baire category theorem, ∅ =
⋂
y∈O(O\{y}) is also dense in O. A contradiction. □
Problem 5.9. Suppose f∈Lp(R) for all p∈ (1, 2) and that supp∈(1,2)‖f‖p <∞.
Prove that f∈L2(R) and that limp→2−‖f‖p =‖f‖2.
Proof.‖f‖p
p =
∫
E|f|p +
∫
Ec|f|p, where Ec ={x:|f(x)|≤ 1}. Now, for all in-
creasing sequence {pn > 1}↑ 2. On E,|f(x)|pn ↓| f(x)|2. In addition, on Ec,
|f(x)|pn↑| f(x)|2. Then, MCT implies that
∫
E|f|pn +
∫
Ec|f|pn→
∫
R|f|2, which
implies that‖f‖
pn
2
pn →‖f‖2. Now, since M = supp∈(1,2)‖f‖p <∞, then‖f‖
pn
2−1
pn ≤
M
pn
2−1→ 1, which implies that‖f‖
pn
2
pn −‖f‖pn→ 0 and thus‖f‖pn→‖f‖2.
Since{pn} is arbitrary, limp→2−‖f‖p =‖f‖2 holds and‖f‖2 <∞ since M =
supp∈(1,2)‖f‖p <∞. □
Problem 5.10. This problem is same with Problem 8 in Aug 2015
6. August 2014
Problem 6.1. Forn∈N, let fn : [0, 1]→R be continuous, and for every x∈ [0, 1]
the sequence ( fn(x)) is decreasing. Suppose that fn → f pointwise. Show the
convergence is uniform.
Proof. This is Dini’s theorem. Given anϵ> 0.Consider open setsUm ={x:|fm(x)−
f(x)|<ϵ} ={x:∀x≥M,|fm(x)−f(x)|<ϵ} sincefm is monotone. Since fm→f
pointwise, [0, 1] = ⋃∞
m=1Um. Then by the compactness of [0, 1], [0, 1] = ⋃N
n=1Umn.
Now, let M = max{m1,...,m N}. Then whenever n > M, for all x ∈ [0, 1],
|fm(x)−f(x)|<ϵ . □
Problem 6.2. Let f∈L1(0,∞). For x >0, deﬁne g(x) =
∫∞
0 f(t)e−txdt. Prove
that g(x) is diﬀerentiable for x> 0 with derivative g′(x) =
∫∞
0 −tf(t)e−txdt

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 17
Proof. Deﬁne h(x) =
∫x
0
∫∞
0 −tf(t)e−tydtdy. Then
∫x
0
∫∞
0 |− tf(t)e−ty|dtdy =∫∞
0 (
∫x
0 e−tydy)·|− tf(t)|dt =
∫∞
0 |− tf(t)|· (− 1
te−tx + 1
t )dt =
∫∞
0 −|f(t)|e−txdt +∫∞
0 |f(t)|dt ≤ 2‖f‖1. Thus, by Fubini, h(x) =
∫∞
0 (
∫x
0 e−tydy)· (−tf(t))dt =∫∞
0 (−tf(t))·(− 1
te−tx+ 1
t )dt =
∫∞
0 f(t)e−txdt−
∫∞
0 f(t)dt. Then, g =h+
∫∞
0 f(t)dt.
We are done. □
Problem 6.3. This problem is same with Problem 1 in Jan 2015.
Problem 6.4. Letf be Lebesgue measurable on [0, 1] withf >0 a.e. Suppose Ek
is a sequence of measurable sets in [0 , 1] with the property that
∫
Ek
f(x)dx→ 0 as
k→∞ . Prove that µ(Ek)→ 0 as k→∞ .
Proof. Deﬁne Fn ={x: f(x) > 1/n}. 1
nµ(Fn
⋂Ek)≤
∫
Fn
⋂Ek
f≤
∫
Ek
f→ 0 as
k→∞ . Since Fn are increasing to the whole space, µ(Ek) = limn→∞µ(Ek
⋂Fn)
uniformly. Indeed, given an ϵ, there is a N such that whenever n≥ N, for all k,
|µ(Ek
⋂Fn)−µ(Ek)|≤ µ(Fc
n)< ϵ/2. For such N, there is a K, whenever k > K
µ(FN
⋂Ek)≤ N
∫
Ek
f≤ ϵ/2, which implies µ(Ek) < ϵ. Thus, lim k→∞µ(Ek) =
0. □
Problem 6.5. Let (fn) be a sequence of continuous functions on [0 , 1] such that
for eachx∈ [0, 1] there is an Nx so that fn(x)≥ 0 for all n≥Nx. Show that there
is an open nonempty set U⊂ [0, 1] and an N∈N, so that fn(x)≥ 0 for all n≥N
and all x∈U.
Proof. If not, for all open setU, integerN, there is an>N and a pointx∈U, such
that fn(x)< 0. Consider open sets En ={x:∃m≥n, f(x)< 0} are dense since
En
⋂U⁄=∅. However, ⋂
nEn =∅. A contradiction to Baire category theorem. □
Problem 6.6. Let X be an inﬁnite dimensional Banach space. What is the w∗-
closure of SX∗ ={x∗ :‖x∗‖ = 1}. (The best exercise to use Hahn-Banach and
Krein-Milman theorem I have ever seen)
Proof. We claim thatSX∗ in thew∗ topology is BallX∗. Indeed, at ﬁrst, if‖x∗‖> 1,
then there is a x∈X such that‖x‖ = 1 and|x∗(x)|> 1. Then, there is an ϵ such
that the nbhd of x∗, A ={y∗ :|x∗(x)−y∗(x)|<ϵ} does not intersect with BallX∗.
To see this, for all y∗∈A,|y∗(x)|> 1 and thus‖y∗‖> 1.
Then, ﬁx a x∗ with‖x∗‖ ≤1. Consider a general nbhd of x∗, say O =
⋂n
i=1{y∗ :|x∗(xi)−y∗(xi)| < ϵ}. Let M = span{xi : i = 1,...,n}. To simplify the
notation, we denote φ for x∗. Let Hφ ={f∈X∗ : f|M =φ}. We claim that Hψ is
weak∗-closed, convex and nonempty set.
Indeed, any Hahn-Banach extension of φ, say, f with‖f‖ =‖ψ‖≤ 1 implies
that Hφ is nonempty. For all f1,f 2∈ Hφ, 0 < λ <1, λf1 + (1−λ)f2|M = φ and

18 XIN MA
‖λf1 + (1−λ)f2‖≤ 1. Thus, Hφ is convex. Now, let fµ(x)→f(x) for all x∈X,
where fµ∈ Hφ. Then since fµ|M = φ, f|M = φ. In addition, for all x is of norm
1,|fµ(x)|≤‖ fµ‖‖x‖≤ 1. This implies that |f(x)|≤ 1 and thus ‖f‖≤ 1, which
implies that Hφ is w∗-closed.
Then, by Krein-Milman theorem, Ext( Hφ)⁄=∅. Let f∈ Ext(Hφ), we claim
‖f‖ = 1. Indeed, suppose ‖f‖< 1. Let g be a linear functional, such that g|M = 0
but‖g‖ = 1. Then deﬁne f1 =f +(1−‖f‖)g andf1 =f−(1−‖f‖)g. Then, it can
be veriﬁed that‖f1‖≤ 1,‖f2‖≤ 1 andf1|M =f2|M =φ. However,f = (f1+f2)/2.
This contradicts to f∈ Ext(Hφ). Thus, f∈SX∗
⋂O. We are done. □
Problem 6.7. Let µ be a ﬁnite measure on the measurable space (Ω , Σ). Prove
the following part of the proof of the above Theorem: If F ∈ L∗
p(µ), then there
exists an h∈L1(µ) so that F (χA) =
∫
Ahdµ for all A∈ Σ.
Proof. F (χA) is a measure on (Ω , Σ) such that F (χA)≪ µ. Indeed, F (χ∅) =
F (0) = 0. Let A = ⨆∞
n=1An. χA = ∑∞
n=1χAn implies that ∑m
n=1χAn→ χA in
Lp(µ). Then since F ∈ Lp(µ)∗, F (∑m
n=1χAn) = ∑m
n=1F (χAn)→ F (χA), which
implies that F (χA) = ∑∞
n=1F (χAn). Thus, F (χA) is a measure. If µ(A) = 0,
|F (χA)|≤ K‖χA‖p =Kµ(A)p = 0. Then, Radon-Nikodym theorem applies. □
Problem 6.8. Assume that (xn) is a weakly converging sequence in a Hilbert space
H. Show that there is a subsequence ( yn) of (xn) so that 1
n
∑n
j=1yj converges in
norm.
Proof. (xn) is bounded. W.L.O.G, we may assume ( xn)→ 0 by subtract its’ limit.
It allows to chooseyj by induction such that|⟨yj, ∑j−1
k=1yk⟩|< 2−j. Now, forn>m ,
‖ 1
m
∑m
j=1yj− 1
n
∑n
j=1yj‖ =⟨ 1
m
∑m
j=1yj− 1
n
∑n
j=1yj, 1
m
∑m
j=1yj− 1
n
∑n
j=1yj⟩ =
⟨( 1
m− 1
n) ∑m
j=1yj− 1
n
∑n
j=m+1yj, ( 1
m− 1
n) ∑m
j=1yj− 1
n
∑n
j=m+1yj⟩ (⋆)
Let ϵ > 0, by the choice of yj, there is a m∈ N, whenever n≥ m,|( 1
m−
1
n) ∑m
j=1yj, 1
n
∑n
j=m+1yj⟩|<ϵ 2. Then (⋆)≤ ( 1
m− 1
n)2‖ ∑m
j=1yj‖2+2ϵ2+ 1
n2‖ ∑n
j=m+1yj‖2≤
1
m2 (∑n
j=1‖yj‖2 + 2) + 1
n2 (∑n
j=m+1‖yj‖2 + 2) + 2ϵ2≤ 1
m2 (m· supj∈N‖yj‖2 + 2) +
1
n2 (n· supj∈N‖yj‖2 + 2) + 2ϵ2 □
Problem 6.9. Show that a linear functional φ on a Banach space X is continuous
iﬀ{x: φ(2x) = 3} is norm closed.
Proof. =⇒ is trivial. In the converse.{x: φ(2x) = 3} = 3/2+ker(φ). Since the shift
by 3/2 is a homeomorphism, then{x: φ(2x) = 3} is closed iﬀ ker(φ) is closed. Deﬁne
φ′ : X/ ker(φ)→C by φ′(x + ker(φ)) = φ(x), which is an isomorphism. Indeed,
ﬁx a point x0∈ X, s.t. φ(x0) = r⁄= 0. Then for all w∈C, φ′(w
rx0 + ker(φ)) =
w. Injectivity follows from the deﬁnition of the quotient map φ′. Thus, φ′ is an

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 19
isomorphism since dim(C) = 1. Thus, φ =φ′◦P is continuous since projection P
is also continuous. □
Problem 6.10. Deﬁne T :C1[0, 1]→C[0, 1] by Tf =f′. Show that T has closed
graph and that T is not bounded.
Proof. Let f(x) =
∫x
0 f′(t)dt +M and fn(x) =
∫x
0 f′
n(t)dt +Mn. Let fn→f and
f′
n→ g under‖·‖ ∞. Since fn(0)→ f(0), Mn→ M. Then, f′
n→ g implies that
fn(x) =
∫x
0 f′
n(t)dt +Mn→
∫x
0 g(t)dt +M under‖·‖ ∞. Thus, g =f′.
On the other hand, let fn(x) = xn. ‖fn‖∞ = 1 while‖f′
n‖∞ =n. Thus, T is
unbounded and C1[0, 1] is not a Banach space under the uniform norm. □
7. January 2014
Problem 7.1. Let (X,M,µ ) be a non atomic measure space withµ(X)> 0. Show
that there is a measurable f :X→ [0,∞), for which
∫
Xfdµ =∞.
Proof. µ is called atomic if there is aA∈M such thatµ(A)> 0 such that whenever
B⊂ A with µ(B) < µ(A), µ(B) = 0. Then, if µ is not atomic, we can deﬁne a
decreasing sequence X =E1⊃E2⊃.... such that µ(E1)>µ (E2)>µ (E3)>...>
0. Thus deﬁne f(x) = 1
µ(En\En+1) > 0 if x∈En\En+1 andf(x) = 0 if x∈ ⋂
nEn.
Then
∫
Xfdµ =∞. □
Problem 7.2. Assume that µ is a ﬁnite measure on Rn. Prove that there is a
closed set A⊂ Rn with the property that for each closed B ⊊ A it follows that
µ(A\B)⁄= 0.
Proof. µ is Radon since it is ﬁnite. Now, let M ={U : U is open and µ(U) = 0}
and O = ⋃{U : U ∈ M}. For any compact set K⊂ O, there is a subcover i.e.
K⊂ ⋃n
i=1Ui, where all Ui∈ M. It implies that µ(K) = 0 and thus µ(O) = 0 by
the regularity of a Radon measure. Deﬁne A = Rn\O. Then for all closed set
B⊊A, Bc is open and µ(Bc)> 0 by deﬁnition of A. Then µ(A\B) =µ(Bc)> 0
since µ(O\B) = 0. □
Problem 7.3. For a nonnegative functionf∈L1[0, 1], prove that limn→∞
∫ 1
0
n
√
f(x)dx =
m{x :f(x)> 0}.
Proof. WLOG, We may assume f > 0 everywhere. Let F = {x : f(x) ≥ 1}.∫ 1
0 f(x)1/ndx =
∫
Ff(x)1/ndx +
∫
Fcf(x)1/ndx. On F , f(x)1/n↓ 1. Similarly, On
Fc, f(x)1/n ↑ 1. Then
∫
Ff(x)1/ndx→ m(F ) and
∫
Fcf(x)1/ndx→ m(Fc) by
MCT and thus
∫ 1
0 f(x)1/ndx→m{x :f(x)> 0}. □

20 XIN MA
Problem 7.4. Letf be Lebesgue integrable on (0, 1). For 0 <x< 1 deﬁneg(x) =∫ 1
x t−1f(t)dt. Prove that g is Lebesgue integrable on (0 , 1) and that
∫ 1
0 g(x)dx =∫ 1
0 f(x)dx.
Proof.
∫ 1
0|g(x)|dx≤
∫ 1
0
∫ 1
x|t−1f(t)|dtdx =
∫ 1
0 (
∫t
0|t−1f(t)|dx)dt =
∫ 1
0|f(t)|dt< ∞
by Tonelli. Then Fubini is applied here to see
∫ 1
0 g(x)dx =
∫ 1
0 f(x)dx with the same
calculation. Note that the integration area is the upper triangle of the unit square
of x-t axis. i.e. the triangle constructed by lines x =t, x = 1 and t = 0. □
Problem 7.5. Assume thatν andµ are two ﬁnite measures on a measurable space
(X,M). Prove that ν≪µ iﬀ limn→∞(ν−nµ)+ = 0.
Proof. (⇐): If µ(E) = 0. Then ( ν− nµ)(E) = ν(E) and then lim n→∞(ν−
nµ)+(E) =ν(E) = 0, which implies that ν≪µ.
(⇒): If ν ≪ µ holds, then ν(E) =
∫
Efdµ for some positive µ-integrable
function f. Then (ν−nµ)(E) =
∫
E(f−n)dµ, which implies that (ν−nµ)+(E) =∫
E(f−n)+dµ. Since ( f(x)−n)+ ↓ 0 for all x∈ X. Then MCT implies that
limn→∞(ν−nµ)+ = 0. □
Problem 7.6. Let (pn) be a sequence of polynomials which converges uniformly
on [0, 1] to some function f, and assume that f is not a polynomial. Prove that
limn→∞ deg(pn) =∞.
Proof. If not, say, suppose max{deg(pn)} =m. X ={p :p is a polynomial and deg(p)≤
m} is a ﬁnite dimensional liner subspace of C[0, 1], thus closed, which implies that
f∈X is a polynomial. A contradiction. □
Problem 7.7. Let (fn) be sequence of non zero bounded linear functionals on a
Banach space X. Show that there is an x∈X so that fn(x)⁄= 0 for all n∈N.
Proof. For eachn, ker(fn) is nowhere dense. Indeed, suppose there is a B(x,ϵ )⊂
ker(fn). Then the open Ball of radius ϵ, Ball(ϵ)⊂ ker(fn), which implies that fn≡
0. Thus, if the statement does not hold, X = ⋃
n ker(fn), which is a contradiction
to Baire category theorem. □
Problem 7.8. Assume that T :l1→l2 is bounded, linear and one-to-one. Prove
that T (l1) is not closed in l2.
Proof. IfT (l1) is closed, then it is a Hilbert space and thusl1 is also a Hilbert space
by open mapping theorem, say T is in fact an isomorphism. A contradiction. □
Problem 7.9. This is same to Problem 3 in Angust 2015.

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 21
Problem 7.10. Assume that f is a measurable and non negative function on
[0, 1]2 and that 1 ≤ r < p < ∞. Show that (
∫ 1
0 (
∫ 1
0 fr(x,y )dy)p/rdx)1/p ≤
(
∫ 1
0 (
∫ 1
0 fp(x,y )dx)r/pdy)1/r.
Proof. DeﬁneF (x) =
∫ 1
0 fr(x,y )dy is a non negative function,s =p/r ands′ be the
conjugate of s. Then for h∈Ls′[0, 1] with‖h‖s′ = 1, Fh∈L1[0, 1] by H¨ older. By
Tonelli’s theorem,
∫ 1
0
∫ 1
0|fr(x,y )h(x)|dydx =
∫ 1
0
∫ 1
0 fr(x,y )|h(x)|dydx =
∫ 1
0 F (x)|h(x)|dx<
∞. Then|
∫ 1
0 F (x)h(x)dx| =|
∫ 1
0 (
∫ 1
0 fr(x,y )dy)h(x)dx| =|
∫ 1
0 (
∫ 1
0 fr(x,y )h(x)dx)dy|≤∫ 1
0‖fr(·,y )‖s‖h‖s′dy =
∫ 1
0 (
∫ 1
0 fp(x,y )dx)r/pdy by Fubini and H¨ older.
Then,‖F‖s = sup{|
∫ 1
0 F (x)h(x)dx| :‖h‖s′ = 1}≤
∫ 1
0 (
∫ 1
0 fp(x,y )dx)r/pdy.
Then we are done since ‖F‖s = (
∫ 1
0 (
∫ 1
0 fr(x,y )dy)p/rdx)r/p. □
8. August 2013
Problem 8.1. Let 1 ≤ p≤∞ and f∈ Lp(R). For t∈ R, let ft(x) = f(x−t)
and consider the mapping G :R→Lp(R) given by G(t) =ft. The space Lp(R) is
equipped with the usual norm topology. (a) Show thatG is continuous if 1≤p< ∞.
(b) Find an f for which the mapping G is not continuous when p =∞. (c) Let
1≤ p,q ≤∞ be conjugate exponents(i.e 1 /p + 1/q = 1). Let f ∈ Lp(R) and
f∈Lq(R). Show that h =f∗g is continuous, where h(t) =
∫
Rf(t)g(t−x)dx.
Proof. The continuity of G when 1≤ p <∞ share a same proof of Problem 5 in
August 2016. If p =∞, Consider f = χ[0,1). Then for any tn→ 0,‖χ[0,1),tn−
χ[0,1)‖≡ 1.
For the last statement, deﬁne gt(x) =f(t−x).|h(t)−h(tn)|≤
∫
R|f(x)||g(t−
x)−g(tn−x)|dx≤‖f‖p‖gtn−gt‖q by H¨ older. By the same argument of the ﬁrst
part, if tn→t, then‖gtn−gt‖q→ 0. □
Problem 8.2. (a) For f ∈ CR[0, 1], show that f ≥ 0 iﬀ ‖λ−f‖∞≤ λ for all
λ≥‖f‖∞
(b) SupposeE⊂CR[0, 1] is a closed subspace containing the constant function
1. For φ∈E∗, show φ≥ 0 iﬀ‖φ‖ =φ(1).
(c) If φ∈E∗ and φ≥ 0, show that there is a bounded linear functional ψ on
CR[0, 1] so that ψ≥ 0 and the restriction of ψ to E is φ.
Proof. (a) (⇒) suppose that f≥ 0 and λ≥‖ f‖∞, then 0 ≤ λ−f≤ λ, whence
‖λ−f‖∞≤ λ. (⇐) If there is a x∈ [0, 1] such that f(x) < 0, which entails that
λ−f(x)>λ and thus‖λ−f‖∞ >λ .
(b)(⇒)|f|≤ 1 implies that 1 ±f ≥ 0 and thus φ(1±f)≥ 0 since φ≥ 0.
Thus|φ(f)|≤ φ(1), whence φ(1)≥‖ φ‖ and thus φ(1) = ‖φ‖. (⇐) ﬁx a f≥ 0.

22 XIN MA
φ(‖f‖∞· 1−f)≤ φ(1)‖‖f‖∞−f‖≤ φ(1)‖f‖∞ = φ(‖f‖∞) by part (a). Thus
φ(f)≥ 0
(c)By Hahn-Banach thm, there is an extension ψ of φ with the same norm,
which implies that‖ψ‖ =‖φ‖ =φ(1) =ψ(1). Thus ψ≥ 0 by part (b). □
Problem 8.3. (a) Let µ andλ be mutually singular complex measures deﬁned on
the same measurable space (X,M) and let ν =µ +λ. Show that |ν| =|µ| +|λ|.
(b) Construct a nonzero atomless Borel measure on [0 , 1] that this mutually
singular with respect to Lebesgue measure m.
Proof. (a) LetF is null forλ whileE is null forµ, withE ⨆F =X. Let P2
⋃N2 =
F be a Hahn decomposition for λ while P3
⋃N3 = E be a Hahn decomposition
for µ. Then P1 = P2
⋃P3, with N1 = N2
⋃N3 is a Hahn decomposition for ν.
Then ν+(A) = ν(A ⋂P2) + ν(A ⋂P3) = µ(A ⋂P2) + λ(A ⋂P3) and similarly,
ν−(A) = ν(A ⋂N2) +ν(A ⋂N3) = µ(A ⋂N2) +λ(A ⋂N3), which implies that
|ν| =|µ| +|λ|.
(b) Let f be the cantor function and consider the Borel measure µf, which is
the Lebesgue-Stieltjes measure associated tof. It can be checked thatµf works. □
Problem 8.4. Let (fn) be a sequence of continuous functions on [0, 1] and suppose
that for all x∈ [0, 1], fn(x) is eventually nonnegative. Show that there is an open
intervalI⊂ [0, 1] such that for all n large enough, fn is nonnegative everywhere on
I.
Proof. Deﬁne En ={x :∀m≥n fm(x)≥ 0}. Suppose the conclusion is not right.
For all subinterval I⊂ [0, 1], I ⊈ En, which entails that En is an nowhere dense
closed set. However, [0, 1] = ⋃
nEn, which is a contradiction. □
Problem 8.5. Letµ be a nonatomic signed measure on a measurable space (X, Ω),
with µ(X) = 1. Show that there is a measurable subset E⊂X with µ(E) = 1/2.
Proof. At ﬁrst, assume µ is a positive measure. We show that there is a function
S : [0, 1]→ Ω such that for all 0 ≤ t≤ t′≤ 1, µ(S(t)) = t and S(t)⊂ S(t′) (i.e.
increasing function).
LetK ={S :D→ Ω :D⊂ [0, 1],S is increasing,∀t∈D, µ(S(t)) =t}. Order
K by S ≤ S′ if graph(S)⊂ graph(S′). At ﬁrst, K ⁄=∅ since S :{1}→ Ω by
S(1) = X. Let {Sα} be a chain in K. Deﬁne S : ⋃Dα→ Ω by S(t) = Sα(t) if
t∈DSα. Then S∈K. Now, Zorn’s lemma entails that there is a maximal element
S0∈ K. We claim that DS0 = [0, 1]. Suppose not, let u = inf{x : x /∈ DS0}, if
u = 0, we extend S0 by deﬁneS0(0) = ∅. If u > 0, there is a sequence ( un)⊂
DS0↑u. Then we extend S0 by deﬁneS0(u) = ⋃S0(un). It is compatible with the

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 23
original S0. Indeed, since S0 is increasing, µ(S0(u)) =µ(⋃S0(un)) = limnun =u.
A contradiction to the maximality of S0. Then S(1/2) is the set we want.
Now, if µ is a signed measure. Consider a Hahn decomposition X = P ⋃N.
µ is positive on P with µ(P )≥ 1. By the argument above, there is a E such that
µ(E) = 1/2. □
Problem 8.6. Compute limn→∞
∫∞
0
n sin(x/n)
x(1+x2) dx
Proof. At ﬁrst, sin(x/n)<x/n implies that n sin(x/n)
x(1+x2) ≤ 1
1+x2 , which is an integrable
function onR+. Then since n sin(x/n)
x(1+x2) → 1
1+x2 , DCT implies that limn→∞
∫∞
0
n sin(x/n)
x(1+x2) dx =∫∞
0
1
1+x2dx =some number. □
Problem 8.7. Prove or disprove: for every real-valued continuous function f on
[0, 1] such that f(0) = 0 and every ϵ> 0, there is a real polynomial p having only
odd powers of x, i.e. p = ∑n
i=1a2i+1x2i+1 such that supx∈[0,1]|f(x)−p(x)|<ϵ .
Proof. At ﬁrst, consider A ={xf(x) :f∈C[0, 1]} is a subalgebra which separates
points by g(x) = x. It implies that A = {f ∈ C[0, 1] : f(0) = 0} by Stone-
Weirstrass theorem. Then similar argument shows that B ={p :p(x) = ∑n
0aix2i}
is dense inC[0, 1] under‖·‖∞. Then for every f∈C[0, 1] withf(0) = 0, there is an
elementg∈C[0, 1] such that supx∈[0,1]|f(x)−xg(x)|<ϵ/ 2 sincexg(x)∈A. For g,
there is a p∈B such that‖g−p‖∞≤ϵ and thus supx∈[0,1]|xg(x)−xp(x)|<ϵ/ 2.
Combine them, we have supx∈[0,1]|f(x)−xp(x)|<ϵ , where xp(x) is a polynomial
having only odd powers of x. □
Problem 8.8.
Problem 8.9. Let X be a separable Banach space, let{xn :n≥ 1} be a countable,
dense subset of the unit ball ofX and letB be the closed unit ball in the dual Banach
space X∗ of X. For φ,ψ ∈B, let d(φ,ψ ) = ∑∞
n=1 2−n|φ(xn)−ψ(xn)|. Show that
d is a metric on B whose topology agrees with the weak*-topology of X∗ restricted
to B.
Proof. It suﬃces to show open sets in two topologies coincide. Let Px∗,ϵ,x ={y∗ :
|y∗(x)−x∗(x)| < ϵ} and D ={xn} is dense subset of X. if x∗∈ ⋂m
i=1Px∗
i,ϵ,zi.
At ﬁrst, By the density of D, there is a δ and{xnk : k = 1, 2,...,m} so that
x∗∈ ⋂m
i=1Px∗
i,δ,xni
⊂ ⋂m
i=1Px∗
i,ϵ,zi. Then, there is a r so that d(x∗,y∗)<r implies
that|x∗(xnk)−y∗(xnk)|<δ for k = 1, 2,...,m . This implies that x∗∈Bd(x∗,r )⊂
⋂m
i=1Px∗
i,δ,xni
⊂ ⋂m
i=1Px∗
i,ϵ,xi.
In the converse, for all φ,ψ ∈B,|φ(xn)−ψ(xn)|≤‖ φ‖ +‖ψ‖≤ 2, and thus
d(φ,ψ ) = ∑∞
n=1 2−n|φ(xn)−ψ(xn)|≤ ∑∞
n=1 2−n+1, which implies that for every

24 XIN MA
ϵ> 0, there is a m∈N such that for all φ,ψ∈B, ∑∞
n=m+1 2−n|φ(xn)−ψ(xn)|<
ϵ/2. Now, for all y∗ ∈ Bd(x∗,ϵ ), ∑∞
n=m+1 2−n|x∗(xn)−y∗(xn)| < ϵ/2. Then
x∗∈ ⋂m
k=1Px∗, ϵ
2m,xk⊂Bd(x∗,ϵ ). Then we are done. □
Problem 8.10. Let T : X→ Y be a linear map between Banach spaces that is
surjective and satisﬁes‖Tx‖≥ ϵ‖x‖ for some ϵ> 0 and all x∈X. Show that T is
bounded.
Proof. Let xn→x and Txn→y. Since T is surjective, there is a z∈X such that
Tz = y. Then ‖Txn−Tz‖≥ ϵ‖xn−z‖ entails that xn→ z and thus x = z and
Tx =y. By closed graph theorem, T is bounded. □
9. January 2013
Problem 9.1. This problem is same with Problem 4 in Jan 2014.
Problem 9.2. This problem is same with Problem 3 in Aug 2015.
Problem 9.3. This problem is same with Problem 8 in Jan 2016.
Problem 9.4. (a) Is there a signed Borel measure µ on [0, 1] such that p′(0) =∫ 1
0 p(x)dµ(x) for all real polynomials p of degree at most 19.
(b) Is there a signed Borel measure µ on [0, 1] such that p′(0) =
∫ 1
0 p(x)dµ(x)
for all real polynomials p.
Proof. (a) LetX = span{xi : 0≤i≤ 19}⊂ C[0, 1] is a ﬁnite-dimensional subspace.
Then deﬁne F : X → R by F (p) = p′(0) is a linear map and thus continuous
since dim(X) = 20. Then by Hahn-Banach theorem, we can extend F to some
bounded linear map G on C[0, 1]. Then there is a Radon Borel measure such that
G(f) =
∫ 1
0 fdµ. Restrict G to X, we have p′(0) =
∫ 1
0 p(x)dµ(x).
(b) Suppose it is true. Consider f(x) = ax, where a > 0. Then by Stone-
Weirstrass theorem, there is a sequence of polynomials pn(x) = ∑mn
i=1a(i,n)x2i→f
under‖·‖∞. Then|
∫ 1
0 pndµ−
∫ 1
0 fdµ|≤‖ pn−f‖∞→. However, by the assumption,
p′
n(0) = 0 and thus a =
∫ 1
0 dµ = 0. A contradiction. □
Problem 9.5. LetF be the set of all real valued functions on [0 , 1] of the form
f(t) = 1∏n
j=1(t−cj) for natural numbers n and for real numbers cj /∈ [0, 1]. Prove or
disprove: for all continuous real-valued functions g andh on [0, 1] such that g(t)<
h(t) for all t∈ [0, 1], there is a function a∈ spanF such thatg(t)<a (t)<h (t) for
all t∈ [0, 1].
Proof. It can be seen thatA = spanF is an algebra and separates points. Then by
Stone-Weirstrass theoremA =C[0, 1]. Let k = min{h(t)−g(t)}. Now, choose a1∈

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 25
A such that‖a1−g‖∞ <k/ 3, whenceg(t)<a 1(t)+k/3 and alsoa1(t)<g (t)+k/3.
Then we need to ﬁnd a a2 such that k/3≤ a2(t)≤ 2k/3. Indeed, for u≡ k/2,
there is an a2∈A so that‖a2−u‖∞ <ϵ<k/ 6, whence k/3≤a2(t)≤ 2k/3. Now,
let a =a1 +a2. Then g(t)<a (t)<g (t) +k/3 + 2k/3≤h(t) □
Problem 9.6. Let k : [0, 1]× [0, 1]→R be continuous and let 1 < p <∞. For
f∈Lp[0, 1], letTf be the function on [0, 1] deﬁned by (Tf )(x) =
∫ 1
0 k(x,y )f(y)dy.
Show that Tf is a continuous function on [0, 1] and that the image under T of the
unit ball in Lp[0, 1] has compact closure in C[0, 1].
Proof.|(Tf )(x)− (Tf )(x′)|≤
∫ 1
0|k(x,y )−k(x′,y )||f(y)|dy. Since k is uniformly
continuous, if|x′−x|<δ , then for all y,|k(x,y )−k(x′,y )|<ϵ . Then |(Tf )(x)−
(Tf )(x′)|≤ ϵ‖f‖1. Then Tf is continuous. It entails thatF ={T (f) :‖f‖p≤ 1} is
equicontinuous by|(Tf )(x)− (Tf )(x′)|≤ ϵ‖f‖1≤ϵ‖f‖p≤ϵ whenever|x′−x|<δ .
Now, since |k(x,y )| ≤M on [0, 1]2. |T (f)(x)| ≤
∫ 1
0|k(x,y )||f(y)| ≤M‖f‖1 ≤
M‖f‖p≤M if‖f‖p≤M. Then Ascoli-Arzela theorem applies there. □
Problem 9.7. Suppose f : [0, 1]→ R is absolutely continuous and deﬁne g ∈
C[0, 1] by g(x) =
∫ 1
0 f(xy)dy. Show that g is absolutely continuous.
Proof. For all ϵ, there is a δ, such that ∑n
i=1|ai−bi| < δ implies ∑n
i=1|f(ai)−
f(bi)|<ϵ . For all y∈ [0, 1], ∑n
i=1|aiy−biy|≤ ∑n
i=1|ai−bi|δ, then ∑n
i=1|f(aiy)−
f(biy)|<ϵ , which implies that ∑n
i=1|g(ai)−g(bi)|≤ ∑n
i=1
∫ 1
0|f(aiy)−f(biy)|dy =∫ 1
0
∑n
i=1|f(aiy)−f(biy)|dy≤
∫ 1
0 ϵdy =ϵ. □
Problem 9.8. Suppose that we have νi≪ µi for i = 1, 2. Show that ν1×ν2≪
µ1×µ2 and d(ν1×ν1)
d(µ1×µ2)(x,y ) = dν1
dµ1
(x)dν2
dµ2
(y)
Proof. µ1×µ2(E) =
∫
µ2(Ex)dµ1(x) = 0 implies that µ1{x : µ2(Ex)⁄= 0} = 0.
Then since νi ≪ µi for i = 1, 2, ﬁrstly {x : ν2(Ex) ⁄= 0} ⊂ {x : µ2(Ex) ⁄=
0} and then µ1{x : ν2(Ex) ⁄= 0} = 0 implies ν1{x : ν2(Ex) ⁄= 0} = 0. Thus
ν1×ν2(E) =
∫
ν2(Ex)dν1(x) = 0 which implies thatν1×ν2≪µ1×µ2. In addition,
ν1×ν2(E) =
∫
X×Y χE(x,y )d(ν1×ν2) =
∫
X(
∫
Y χE(x,y )f2(y)dµ2(y))f1(x)dµ1(x) =∫
X(
∫
Y χE(x,y )f1(x)f2(y)dµ2(y))dµ1(x) =
∫
Ef1(x)f2(y)d(µ1×µ2). We are done.
□
Problem 9.9. (a) LetE be a nonzero Banach space and show that for everyx∈E
there is φ∈E∗ such that‖φ‖ = 1 and|φ(x)| =‖x‖.
(b) Let E and F be Banach spaces, Let π :E→F be a bounded linear map
and let π∗ :F∗→E∗ be the induced map on dual spaces. Show that ‖π∗‖ =‖π‖.
Proof. (a) A standard application of Hahn-Banach theorem.

26 XIN MA
(b) π∗(f) =f◦π. Then ‖π∗‖ = sup‖f‖=1‖π∗(f)‖ = sup‖f‖=1,‖x‖=1|f(π(x))|.
|f(π(x))|≤‖ f‖‖π‖‖x‖ for all f∈F∗,x∈E, whence‖π∗‖≤‖ π‖. In the converse,
by part (a), for every x∈ E, there is a fx∈ F∗ such that |fx(π(x))| =‖π(x)‖
and‖fx‖ = 1. Thus,‖π∗‖ = sup‖f‖=1,‖x‖=1|f(π(x))|≥ sup‖x‖=1|fx(π(x))| =‖π‖.
Then we are done. □
Problem 9.10. LetX be a real Banach space and suppose C is a closed subset of
X such that
(1) x1 +x2∈C for all x1,x 2∈C,
(2) λx∈C for all x∈C and λ> 0,
(3) for all x∈X there exist x1,x 2∈C such that x =x1−x2.
Prove that for some M > 0, the unit ball of X is contained in the closure of
AM ={x1−x2 : xi∈ C,‖xi‖≤ M, (i = 1, 2)}. Deduce that every x∈ X can be
written x =x1−x2, with xi∈C and‖xi‖≤ 2M‖x‖, (i = 1, 2).
Proof. Suppose that there is a ϵ> 0,n∈N so that Bϵ(0)⊂An, then there is a m
such that BX⊂ Am. Indeed, for all x∈ BX,‖ϵx‖≤ ϵ, then there is a sequence
(xk
1−xk
2)∈An so that (xk
1−xk
2)→ϵx, which implies that 1
ϵ (xk
1−xk
2)→x. Now,
deﬁne yk
i = 1
ϵxk
i and choose m such that‖yk
i‖≤ n/ϵ≤m.
So suppose the assumption does not hold, say, for all ϵ,n , Bϵ(0)⊈ An, then
An is nowhere dense for all n. If not, say there is a y +Bϵ(0)⊂An. Then for all
x∈Bϵ(0), there is a sequence ( zn
1−zn
2 )→y +x. For a sequence ( yn
1−yn
2 )→y,
((zn
1 +yn
2 )− (zn
2 +yn
1 ))→x, which implies that x∈A2n and thus Bϵ(0)⊂A2n. A
contradiction. However, X = ⋃∞
n=1An, which is a contradiction to Baire category
theorem. Thus, there is a M such that BX⊂AM.
Now, ﬁxx∈X,x/‖x‖∈ BX⊂AM, then there arey1,z 1 such that‖y1‖,‖z1‖≤
M‖x‖, so that ‖x− (y1−z1)‖≤ (1/2)‖x‖. Then ‖x−(y1−z1)
(1/2)‖x‖ ‖≤ 1. Then there
are y2,z 2 ∈ AM..... We can do this process by induction to obtain yn,zn with
‖zn‖,‖yn‖≤ 2−n+1M‖x‖ and‖x− ∑n
i=1(yi−zi)‖≤ 2−n‖x‖, which implies that
x = ∑
iyi− ∑
izi. □
10. August 2012
Problem 10.1. Let (X,M,µ ) be a measure space. Prove that L1(X,µ ) is com-
plete.
Proof. You can ﬁnd a proof in any real analysis textbook. □
Problem 10.2. Fix two measure spaces (X,M,µ ) and (Y,N,ν ) withµ(X),ν (Y )>
0. Let f :X→C, and g :X→C be measurable. Suppose f(x) =g(y) (µ×ν)-a.e.
Show that there is a constant a∈C such that f(x) =a µ-a.e. and g(y) =a ν-a.e.

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 27
Proof. E ={(x,y ) : f(x)⁄= g(y)} is null. Then
∫
ν(Ex)dµ(x) = 0, which implies
that ν(Ex) = 0 µ-a.e. Now, deﬁne K ={x : ν(Ex) = 0}. Suppose the statement
is not true, say, for all a∈C, either µ{x : f(x)⁄= a} > 0 or ν{y : g(y)⁄= a} > 0.
Now, ﬁx x0∈K and let a =f(x0). Then, by deﬁnition, Ex0 ={y :g(y)⁄=a} and
thusν({y :g(y)⁄=a}) = 0. Thus, µ({x :f(x)⁄=a})> 0 by the assumption. Since
ν(Ex0) = 0, ν({y :g(y) =a}) =ν(Y\Ex0)> 0. Now,{x :f(x)⁄=a}×{ y :g(y) =
a}⊂ E is of positive measure. A contradiction. □
Problem 10.3. LetR3→R be a Borel measurable function. Suppose for every
ball B, f is integrable on B and
∫
Bf = 0. What can you deduce about f.
Proof. Since f is locally integrable, then limr→0 1
m(B(r,x))
∫
B(r,x)f(y)dy =f(x) for
a.e. x, which implies that f(x) = 0 a.e.
We can also use the proof of Problem 1 in Jan 2015 to solve this. Indeed, we
can still deﬁne En. By regularity of lebesgue measure. We can shrink En to some
compact subset K of positive measure s and obtain a ﬁnite cover of K with ﬁnite
balls, say K⊂O = ⋃n
i=1Bn withµ(O\K)<δ . Then replace En withK,In with
Bn to do the same process. We are done. □
Problem 10.4. LetX be a locally compact Hausdorﬀ space. Show that Cc(X) is
dense in C0(X).
Proof. Cc(X) is an algebra. by Usysohn’s lemma, for all x⁄= y∈ X, there is a
g∈ Cc(X) so that g(x)⁄= g(y) and for all x∈ X, there is a function f in Cc(X)
such that f(x) = 1. Then by Stone-Weirstrass theorem for the LCH space, Cc(X)
is dense in C0(X). □
Problem 10.5. Give an example of each of the following. justify your answers
(1) A nowhere dense subset of R of positive Lebesgue measure.
(2) A closed, convex subset of a Banach space with multiple points of minimal
norm.
Proof. (1) A ﬁrst example is any generalized cantor set with positive measure.
We provide another example with more descriptive set theory ﬂavor. Let {rn}
enumerate all rational numbers in R, then deﬁne Om = ⋃∞
n=1(rn− 1
2n+1
1
m,rn +
1
2n+1
1
m) which is dense and µ(Om)≤ 1/m. Then A = ⋂∞
m=1Om is a dense Gδ set
with µ(A) = 0. Then Ac = ⋃
mOc
m is of positive measure. Then there is a m such
that Oc
m is of positive measure and Oc
m is nowhere dense by deﬁnition.
(2) Let X =L1[0, 1] and C ={f∈X :
∫
[0,1]f(t)dt = 1}. The minimal norm
of functions in C is 1. Then {aχ[1/2,1] + (2−a)χ[0,1/2]} : 0 ≥ a≥ 2}⊂ C have
norm 1. □

28 XIN MA
Problem 10.6. LetS ={f∈L∞(R) :|f(x)|≤ 1
1+x2a.e.}. Which of the following
statements are true?
(1) The closure of S is compact in the norm topology.
(2) S is closed in the norm topology.
(3) The closure of S is compact in the weak-∗ topology.
Proof. (1) No. Consider a sequence 1
1+nx2 . If S is compact, then there is a sub-
sequence 1
1+nmx2 converges in S under‖·‖ ∞. Then 1
1+nmx2→ 0 uniformly a.e. ,
which is a contradiction since 1
1+nmx2 does not uniformly converge to 0 on any set
of inﬁnite measure.
(2) For all fn→ f under‖·‖ ∞. Deﬁne En be the null set such that on Ec
n,
|fn(x)|≤ 1
1+x2 . Since fn→f, there is a null set E such on Ec, fn→f uniformly.
Then on ( ⋃
nEn
⋃E)c,|f(x)|≤ 1
1+x2 , where µ((⋃
nEn
⋃E)) = 0
(3) For all f ∈ S,|f(x)|≤ 1
1+x2 a.e. which implies that ‖f‖∞≤ 1. Thus
S⊂BX∗. Thus S is weak-∗ compact. □
Problem 10.7. Let T be a bounded operator on a Hilbert space H. Prove that
‖T∗T‖ =‖T‖2.
Proof.‖T‖2 = sup‖x‖=1‖Tx‖2 = sup‖x‖=1|⟨Tx,Tx⟩| = sup‖x‖=1|⟨x,T∗Tx⟩| ≤
sup‖x‖=1‖x‖‖T∗Tx‖≤‖ T∗T‖. In the converse, ‖T∗Tx‖≤‖ T∗‖‖T‖‖x‖ =‖T‖2
implies that‖T∗T‖≤‖ T‖2. □
Problem 10.8. (a) Let g be an integrable function on [0 , 1]. Does there exist a
bounded measurable function f such that‖f‖∞⁄= 0 and
∫ 1
0 fgdx =‖g‖1‖f‖∞.
(b) Let g be a bounded function on [0 , 1]. Does there exist an integrable
measurable function f such that‖f‖1⁄= 0 and
∫ 1
0 fgdx =‖f‖1‖g‖∞.
Proof. (a) Deﬁne f = sgng. Then
∫ 1
0 fgdx =‖g‖1‖f‖∞.
(b) Not always. Consider g = 1{x} for some x∈ [0, 1]. Suppose there is a f∈
L1[0, 1] so that
∫ 1
0 fgdx =‖f‖1‖g‖∞. Then it implies that ‖f‖1 =
∫
{x}f = 0. □
Problem 10.9. LetF :R→C be a bounded continuous function, µ the Lebesgue
measure, andf,g ∈L1(µ). Let ˜f(x) =
∫
F (xy)f(y)dµ(y), ˜g(x) =
∫
F (xy)g(y)dµ(y).
Show that ˜f and ˜g are bounded continuous functions which satisfy
∫
f ˜gdµ =
∫
g ˜fdµ
Proof. Let supx∈R|F (x)| =M. Consider| ˜f(xn)− ˜f(x)|≤
∫
|F (xny)−F (xy)||f(y)|dy.
Since|F (xny)−F (xy)||f(y)|→ 0 pointwise and|F (xny)−F (xy)||f(y)|≤ 2M|f(y)|,
which is integrable, DCT implies that
∫
|F (xny)−F (xy)||f(y)|dy = 0. Thus ˜f is
continuous.| ˜f(x)|≤
∫
|F (xy)||f(y)|dµ(y)≤M‖f‖1, which is bounded. The same
proof for ˜g.

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 29
∫
|f(x)|(
∫
|F (xy)||g(y)|dµ(y))dµ(x)≤M
∫
|f(x)|‖g‖1dµ(x)≤M‖f‖1‖g‖1. Then,
by Fubini,
∫
f ˜gdµ =
∫
f(x)(
∫
F (xy)g(y)dµ(y))dµ(x) =
∫
g(y)(
∫
F (xy)f(x)dµ(x))dµ(y) =∫
g ˜fdµ. □
Problem 10.10. Let µ,{µn : n∈N} be ﬁnite Borel measures on [0 , 1]. µn→ µ
vaguely if µn→µ if it converges in the weak*-topology. µn→µ in moments if for
eachk∈{ 0} ⋃N,
∫
[0,1]xkdµn→
∫
[0,1]xkdµ. Show these two concepts coincide.
Proof. (⇒) trivial, since xk∈C[0, 1].
(⇐) Fork = 0, we haveµn([0, 1])→µ([0, 1]), which implies that µn([0, 1]) are
uniformly bounded, say, we may assume that sup{µn[0, 1],µ [0, 1] :n∈N}≤ M for
some M. By Stone-Weirstrass theorem, for each continuous function f on [0, 1],
there is a sequence of polynomialspm→f under‖·‖∞. Then for everyϵ> 0, choose
a m such that‖pm−f‖∞≤ϵ/4M. For the m, there is a N whenevern>N such
that|
∫
pmdµn−pmdµ|≤ ϵ/2 sinceµn→µ in moments. Then|
∫
fdµn−
∫
fdµ|≤∫
|f−pm|dµn +
∫
|f−pm|dµ +|
∫
pmdµn−pmdµ|≤ 2M· (ϵ/4M) +ϵ/2 =ϵ. Thus
µn→µ vaguely. □
11. January 2012
Problem 11.1. Let A be the subset of [0, 1] consisting of numbers whose decimal
expansions contain no sevens. Show that A is Lebesgue measurable, and ﬁnd its
measure. Why does non-uniqueness of decimal expansions not cause any problems?
Proof. We can obtainA by following the procedure of the construction of the cantor
set. Firstly divide [0 , 1] into ten pieces and delete (0 .7, 0.8] to obtain A1. Then to
obtainA2, for each of the nine subintervals ofA1, divide it into ten pieces and delete
the seventh subinterval of it. Deﬁne the left set to be A2.Go on this procedure to
obtain An. Then deﬁne A = ⋂
nAn. Since we just delete Borel sets from [0 , 1]. A
is Borel thus measurable. µ(A) = 1− ∑∞
n=0
9n
10n+1 = 0.
Since the number who has more than one expansion are exactly { p
10n :n,p∈
N,p≤ 9} which is countable, thus of measure 0. So it will cause no problems. □
Problem 11.2. Let functions fα be deﬁned by fα(x) = xαcos(1/x) if x >0 and
fα(0) = 0. Find all α≥ 0 such that
(a) fα is continuous.
(b) fα is of bounded variation on [0, 1].
(C) fα is absolutely continuous.
Proof.|fα(x)| =| =xα cos(1/x)|≤| xα|→ 0 whenx→ 0 ifα> 0. Thus for all α>
0,fα is continuous. For part (b), if α≤ 1, deﬁne xn = 1/nπ, ∑|fα(xn)−fα(xn+1|

30 XIN MA
diverges, which implies that fα is not of bounded variation. In the converse, at
ﬁrst, fα is diﬀerentiable on (0, 1] for all α >0. If α >1, fα is also diﬀerentiable
at 0. Then fα(x) =
∫x
0 f′
α(t)dt. Thus, fα is of bounded variation. For part ( c),
If α≤ 1, fα is not of bounded variation, whence fα is not absolutely continuous.
When α> 1, f is of a form of integral, thus absolutely continuous. □
Problem 11.3. LetF denote the family of functions on [0 , 1] of the form f(x) =
∑∞
n=1an sin(nx), where an are real and |an|≤ 1/n3. Prove that F is precompact
i.e. totally bounded.
Proof. For allx,y∈ [0, 1], there is ax0 between them and aM >0 such that|f(x)−
f(y)|≤ ∑|an|| sin(nx)− sin(ny)|≤ ∑|an|| cos(nx0)||nx−ny|≤ ∑
n
1
n2|x−y|≤
M|x−y|, whenceF is equicontinuous on [0, 1]. For all x∈ [0, 1],{f(x) :f∈F} is
bounded since |f(x)|≤ ∑
n 1/n3≤∞ . Then Ascoli-Arzela’s theorem implies the
result. □
Problem 11.4. Let H be a Hilbert space and W⊂H be a subspace. Show that
H =W ⨁W⊥
Proof. You can ﬁnd the proof in every textbook of functional analysis. □
Problem 11.5. Suppose A is a bounded linear operator on a Hilbert space H
with the property that ‖p(A)‖≤ C sup{|p(z)| : z ∈ S1} = C‖p‖ with complex
coeﬃcients and a ﬁxed constant C. Show that to each pair x,y ∈H, there corre-
sponds a complex Borel measure µ on the circle S1 ={z∈C :|z| = 1} such that
⟨Anx,y⟩ =
∫
zndµ(z), n = 0, 1, 2,...
Proof. Deﬁne H(p) = ⟨p(A)x,y⟩ for all polynomials p with complex coeﬃcients.
|H(p)| =|⟨p(A)x,y⟩| ≤ ‖p(A)‖‖x‖‖y‖ ≤C‖p‖‖x‖‖y‖, which implies that H is
extended to whole C(S1) by the density of all polynomials in C(S1) as a bounded
linear functional. Thus, there is a Radon measure µ onS1 such thatH(f) =
∫
fdµ.
Then H(zn) =⟨Anx,y⟩ =
∫
zndµ(z), n = 0, 1, 2,... . □
Problem 11.6. Let φ be the linear functional φ(f) =f(0)−
∫ 1
−1f(t)dt.
(a) Compute the norm of φ as a functional on the Banach space C[−1, 1] with
uniform norm.
(b) Compute the norm ofφ as a functional on the normed vector spaceLC[−1, 1],
which is C[−1, 1] with L1 norm.
Proof. (a) ‖φ‖ = sup{|φ(f)| : ‖f‖∞ = 1}. ‖f‖∞ = 1 implies that |f(0)−∫ 1
−1f(t)dt|≤| f(0)| +
∫ 1
−1|f(t)|dt = 3. Consider the continuous function fn such

A NOTE FOR REAL ANALYSIS QUALIFYING EXAM IN TAMU 31
that fn = 1 on [ −1,−1/n] ⋃[1/n, 1], fn(0) = −1 and fn is peicewise linear on
[−1/n, 1/n]. Then, we can see |φ(fn)|→ 3, whence‖φ‖ = 3.
(b) Deﬁnefn = 0 on [−1,−1/n] ⋃[1/n, 1],fn(0) =n andfn is peicewise linear
on [−1/n, 1/n]. ‖fn‖1 = 1 and |φ(fn)| = n +
∫ 1
−1|fn| = n + 1 which implies that
‖φ‖ =∞. □
Problem 11.7. Let X be a normed space, and A⊂X a subset. Show that A is
bounded(as a set) if and only if it is weakly bounded(that is, f(A)⊂C is bounded
for each f∈X∗).
Proof. (⇒) Suppose that sup{‖x‖ : x∈ A}≤ M. Then for all f∈ X∗,|f(x)|≤
‖f‖‖x‖≤ M‖f‖.
(⇐)X∗ is a Banach space. For allf∈X∗,x∗∗(f) =f(x). Now supx∈A|x∗∗(f)| =
supx∈A|f(x)|<∞. Then uniform boundedness theorem implies that supx∈A‖x‖ =
supx∈A‖x∗∗‖<∞. □
Problem 11.8.

32 XIN MA
E-mail address : dongodel@math.tamu.edu

