Real Analysis
Course Notes
Contents
1 Measure, integration and diﬀerentiation on R . . . . . . . . . 1
1.1 Real numbers, topology, logic . . . . . . . . . . . . . . 2
1.2 Lebesgue measurable sets and functions . . . . . . . . 4
1.3 Integration . . . . . . . . . . . . . . . . . . . . . . . . 9
2 Diﬀerentiation and Integration . . . . . . . . . . . . . . . . . 15
3 The Classical Banach Spaces . . . . . . . . . . . . . . . . . . 28
4 Baire Category . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5 Topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
6 Banach Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . 54
7 Hilbert space . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
8 General Measure Theory . . . . . . . . . . . . . . . . . . . . . 79
1 Measure, integration and diﬀerentiation on R
Motivation. Suppose f : [0,π ] → R is a reasonable function. We deﬁne
the Fourier coeﬃcients of f by
an = 2
π
∫ π
0
f (x) sin(nx)dx.
Here the factor of 2 /π is chosen so that
2
π
∫ π
0
sin(nx) sin(mx)dx =δnm.
We observe that if
f (x) =
∞∑
1
bn sin(nx),
then at least formally an =bn (this is true, for example, for a ﬁnite sum).
This representation of f (x) as a superposition of sines is very useful for
applications. For example, f (x) can be thought of as a sound wave, where
an measures the strength of the frequency n.
1

Now what coeﬃcients an can occur? The orthogonality relation implies
that
2
π
∫ π
0
|f (x)|2dx =
∞∑
−∞
|an|2.
This makes it natural to ask if, conversely, for any an such that∑ |an|2 < ∞,
there exists a function f with these Fourier coeﬃcients. The natural function
to try is f (x) =∑ an sin(nx).
But why should this sum even exist? The functions sin( nx) are only
bounded by one, and ∑ |an|2 < ∞ is much weaker than ∑ |an|< ∞.
One of the original motivations for the theory of Lebesgue me asure and
integration was to reﬁne the notion of function so that this s um really
does exist. The resulting function f (x) however need to be Riemann inte-
grable! To get a reasonable theory that includes such Fourie r series, Cantor,
Dedekind, Fourier, Lebesgue, etc. were led inexorably to a r e-examination
of the foundations of real analysis and of mathematics itsel f. The theory
that emerged will be the subject of this course.
Here are a few additional points about this example.
First, we could try to deﬁne the required space of functions — called
L2[0,π ] — to simply be the metric completion of, say C[0,π ] with respect
to d(f,g ) =
∫
|f −g|2. The reals are deﬁned from the rationals in a similar
fashion. But the question would still remain, can the limiti ng objects be
thought of as functions?
Second, the set of point E ⊂ R where∑ an sin(nx) actually converges is
liable to be a very complicated set — not closed or open, or eve n a countable
union or intersection of sets of this form. Thus to even begin , we must have
a good understanding of subsets of R.
Finally, even if the limiting function f (x) exists, it will generally not be
Riemann integrable. Thus we must broaden our theory of integ ration to
deal with such functions. It turns out this is related to the s econd point
— we must ﬁnd a good notion for the length or measurem(E) of a fairly
general subset E ⊂ R, since m(E) =
∫
χE.
1.1 Real numbers, topology, logic
The real numbers. Conway: Construction of the real numbers [Con,
p.25].
Dedekind: just as a prime is characterized by the ideal of thi ngs it di-
vides, so a number is characterized by the things less than it .
Brouwer and Euclid: the continuum is not a union of points!
2

Hilbert: the axiomatic approach to the reals. Formalism ver sus intu-
itionism.
Other completions of Q: e.g. Q2, Q10. (In the latter case the completion
is a ring but not a ﬁeld! If 5 n accumulates on x and 2n accumulates on y,
then |x|10 = |y|10 = 1 but xy = 0. One can make the solution canonical by
asking that x = (0, 1) and y = (1, 0) in Z10 ∼
= Z2 × Z5; then y = x + 1 =
... 4106619977392256259918212890625.)
Basic topological property of the reals (not shared by the ot her comple-
tions: connectedness).
The irrationals in [0 , 1] are isomorphic to NN by
(a1,a 2,... ) ↦→1/(a1 + 1/(a2 + · · ·)).
(Here N = {1, 2, 3,... }.)
Proof. draw the Farey tree.
Cardinality . Russell’s paradox: if E = {X : X ⁄∈X}, then is E ∈ E?
Make this into a proof that |P(X)| > |X|. Corollary: R is uncountable,
since 2 N is isomorphic to the Cantor set.
Helpful tool: Schr¨ oder-Bernstein.
Question: How many rational numbers are there? How many alge braic
numbers? Are most numbers transcendental?
Answer: in terms of counting, yes.
Answer: in terms of measure: the probability that x ∈ [0, 1] is equal to
a given algebraic number a ∈A is zero. Thus the probability that x ∈A is
zero.
Paradox: why doesn’t the same argument show x ⁄=y for everyy ∈ [0, 1]?
Equivalent, what is wrong with the following equation:
1 = m([0, 1]) = m
(⋃
x
{x}
)
=
∑
m({x}) = 0?
If uncountable additivity is suspect, what about countable additivity?
The Borel hierarchy . Induction, over the natural numbers and over an
ordinal. Example: any C ⊂ P (X) generates a unique smallest algebra. (Use
induction over N). Similar, generates a unique σ-algebra. (Use induction
over Ω, whose existence comes from well-ordering of the real s.)
Ex: ⟨fn⟩continuous = ⇒ the set of points where fn(x) is bounded is an
Fσ. E.g.
fn(x) =
n∑
k=1
| sin(πk!x)|1/n
3

is bounded iﬀ x ∈ Q.
A condensation point of E ⊂ R is a point x ∈ R such that every neigh-
borhood of x meets E in an uncountable set. In other words, its the set of
points where E is ‘locally uncountable’.
Theorem 1.1 Any uncountable set contains an uncountable collection of
condensation points.
The same holds true in any complete, separable metric space. Thus only
countably many Y ’s can be embedded disjointly in R2, and only countably
many M¨ obius bands in R3.
Any closed uncountable set F has the order of the continuum. In fact
it contains a copy of the Cantor set. (Proof: pick two condens ation points,
and then two disjoint closed intervals around them. Within e ach interval,
pick two disjoint subintervals containing condensation po ints, and continue.
By insuring that the lengths of the intervals tend to zero we g et a Cantor
set.)
How many open sets? Theorem. The set of all open subsets of R is of
the same cardinality as R itself. Indeed, the same is true of the set of all
Borel sets.
1.2 Lebesgue measurable sets and functions
On R we will construct a σ-algebra M containing the Borel sets, and a
measure m : M → [0, ∞], such that m(a,b ) = b −a, m is translation-
invariant, and m is countably additive.
Deﬁnition: the outer measure m∗(E) is the inﬁmum of ∑ ℓ(Ii) over all
coveringsE ⊂⋃ Ii by countable unions of intervals.
Basic fact: subadditivity. For any collection of sets Ai, m∗(⋃ Ai) ≤∑ m∗(Ai).
Basic fact: m∗[a,b ] = b −a.
Proof. Clearly the outer measure is at most b −a. But if [ a,b ] is covered
by⋃ Ik, by compactness we can assume the union is ﬁnite, and then
b −a =
∫
χ[a,b ] ≤
∫ ∑
χIk =
∑
|Ik|.
Deﬁnition: E ⊂ R is measurable if
m∗(E ∩A) +m∗(~E ∩A) = m∗(A)
4

for all sets A ⊂ R. Because of subadditivity, only one direction needs to be
checked.
For example, if E ⊂ [0, 1] then m∗(E) +m∗([0, 1] −E) = 1.
Theorem 1.2 E = [a, ∞) is measurable.
Proof. From a good cover ⋃ Ii for A we must construct good covers for
E ∩A and ~E ∩A. This is easy because E cuts each interval Ii into two
subintervals whose lengths add to that of Ii.
Theorem 1.3 The measurable sets form an algebra.
Proof. Closure under complements is by deﬁnition. Now suppose E and
F are measurable, and we want to show E ∩F is. By the deﬁnition of
measurability, E cuts A into two sets whose measures add up. Now F
cuts E ∩A into two sets whose measures add up, and similarly for the
complements. Thus E and F cut A into 4 sets whose measures add up to
the outer measure of A. Assembling 3 of these to form A ∩ (E ∪F ) and the
remaining one to form A ∩ ~E ∪F , we see E ∪F is measurable.
Theorem 1.4 If Ei are disjoint and measurable, i = 1 , 2,...,N , then∑ m∗(Ei ∩A) = m∗(A ∩⋃ Ei).
Proof. By induction, the case N = 1 being the deﬁnition of measurability.
Theorem 1.5 The measurable sets form a σ-algebra.
Proof. Suppose Ei is a sequence of measurable sets; we want to show ⋃ Ei
is measurable. Since we already have an algebra, we can assum e the Ei are
disjoint. By the preceding lemma, we have for any ﬁnite N ,
N∑
1
m∗(Ei ∩A) +m∗(A ∩
N⋂
1
~Ei) = m∗(A).
The second term is only smaller for an inﬁnite intersection, so lettingN → ∞
we get
∞∑
1
m∗(Ei ∩A) +m∗(A ∩
∞⋂
1
~Ei) ≤m∗(A).
Now the ﬁrst term dominates m∗(A ∩⋃ Ei) so we are done.
5

Corollary 1.6 All Borel sets are measurable.
Deﬁnition. m(E) = m∗(E) if E is measurable.
Theorem 1.7 IfEi are disjoint measurable sets, then m(⋃ Ei) =∑ m(Ei).
Proof: follows from the Theorem above, setting A = R and passing to the
limit.
Continuity of measure. If m(E1) is ﬁnite and E1 ⊃ E2 ⊃ E3... , then
m(⋂ Ei) = lim m(Ei). Proof. let F = ⋂ Ei and write E1 = F ∪ (E1 −
E2) ∪ (E2 −E3) ∪... .
Littlewood’s ﬁrst principle. Let E ⊂ R be measurable. Then E is
approximated from the outside (inside) by open (closed) set s, and to within
a set of measure zero by a Gδ (Fσ).
If the measure of E is ﬁnite, then there is a ﬁnite union of intervals J
such that m(E△J)<ǫ .
Proof. First suppose m(E) is ﬁnite. Then there are open intervals such
that E ⊂⋃ Ii and m(⋃ Ii −E) ≥ (∑ m(Ii)) −m(E) < ǫ. This shows E
is approximate from the outside by an open set, and from the in side by a
closed set. Also if we take J to be the union of a large ﬁnite subset of {Ii},
then what’s left over has small measure, so we get m(E△J) small. (The
diﬀerence is covered by ( ⋃ Ii −J) ∪ (⋃ Ii −E).) Why not use this
Theorem to deﬁne
the σ -algebra of
measurable sets?
Corollary: Every Borel set B can be expressed as B =G −N =F ∪N′,
where G is a Gδ, F is an Fσ, and N,N′ are sets of measure zero. Thus
measure theory ‘short circuits’ the Borel hierarchy. Note t hat the notion of
zero measure is elementary (compared to the notion of measur able).
Corollary: If E has positive measure then there exists an interval I such
that m(E ∩I)/m(I) ≈ 1. Proof. Take a very eﬃcient cover of E by
ﬁnitely many intervals J. Then the ratio m(J)/m(E) ≈ 1, and on the other
hand m(J)/m(E) is bounded below by the sup of the density of E in each
subinterval.
Nonmeasurable sets. Let G = R/Z and let H = Q/Z ⊂G be a normal
subgroup. Then there exists a set of coset representatives P ⊂G for G/H.
Since m(G) = 1 and G =⋃
Hh +P , the measure of P cannot be deﬁned.
ThusH is nonmeasurable. Let B be a basis for
R over Q. Is B
measurable?Assume the Continuum Hypothesis. Then we can well-order [0 , 1] such
that each initial segment is countable. Set R = {(x,y ) : x < y} in this
ordering. Then horizontal slices (ﬁxing y) have measure zero, while all
vertical slices (ﬁxing x have measure one).
6

Measurable functions. A function f : R → R is measurable if f−1(U ) is
measurable whenever U is an open set.
First examples: continuous functions, step functions ( ∑ N
1 aiχIi, Ii dis-
joint intervals) and simple functions (∑ N
1 aiχEi,Ei disjoint measurable sets)
are all measurable. Note that simple functions are exactly t he measurable
functions taking only ﬁnitely many values.
In general, if f : A → B is any map, the map f−1 : P(B) → P (A) is
a σ-algebra homomorphism; indeed it preserves unions over any index set.
Thus f is measurable is the same as: (a) f−1(x, ∞) is measurable for all
x ∈ R; or (b) f−1(B) is measurable for any Borel set B.
W arning. It is not true that f−1(M ) is measurable whenever M is mea-
surable! Thus measurable functions are not closed under com position.
More generally, for a topological space X we say f : R → X is mea-
surable if the preimages of open sets are measurable. Exampl e: if f,g are
measurable functions, then h = (f,g ) : R → R2 is measurable. Indeed, for
any open set U ×V ⊂ R2, the preimage h−1(U ×V ) = f−1(U ) ∩g−1(V ) is
measurable. Since every open set in R2 is a union of a countable number of
open rectangles, h is measurable.
Similarly, if h : R2 → R is continuous, then h(f,g ) is measurable when-
ever f and g are. This shows the measurable functions form an algebra:
fg andf +g are measurable if f and g are.
Moreover, the measurable functions are closed under limits . Indeed, if
f = limfn then
f−1(a, ∞) = {x : ∃k ∃N ∀n ≥N fn(x)>a + 1/k}
=
⋃
k
⋃
N
⋂
n≥N
f−1
n (a + 1/k, ∞).
Similarly for lim sup, lim inf etc.
If f =g a.e. and f is measurable then so is g.
Theorem 1.8 (Littlewood’s second principle) Iff is measurable on [a,b ]
then f is the limit in measure of continuous functions: there exist s contin-
uous fn such that for all ǫ> 0, m{|f −fn|>ǫ } → 0.
Proof. LetEM = {|f |>M }; then⋂ EM = ∅, so after truncating f on a set
of small measure we obtain f1 bounded byM . Cutting [ −M,M ] into ﬁnitely
many disjoint intervals of length ǫ, and collecting together the values, we see
f1 is a uniform limit of simple functions. Any simple function i s built from
indicator functions χE of measurable sets. By Littlewood’s ﬁrst principle,
7

χE is approximated in measure by χJ , where J is a ﬁnite union of intervals.
Finally χJ is a limit in measure of continuous functions.
Theorem 1.9 (Lusin’s Theorem; Littlewood’s 2nd principle) Given
a measurable function f on [0, 1], one can ﬁnd a continuous function g :
[0, 1] → R such that g =f outside a set of small measure.
Theorem 1.10 (Egoroﬀ; Littlewood’s 3rd principle) Letf (x) = limfn(x)
for each x ∈ [0, 1], where fn,f are measurable. Then fn →f uniformly out-
side a set of small measure.
Example: Recall the ‘tent functions’ fn supported on [0 , 1/n] with a
triangular graph of height n. We have fn → 0 but
∫
fn = 0; these fn do not
converge uniformly everywhere.
Proof of the Theorem. For any k >0, consider the sets
EN = {x : |fn(x) −f (x)|> 1/k for some n>N }.
Since fn →f , we have ⋂ EN = ∅. Since EN ⊂ [0, 1], we have m(EN ) → 0.
Thus there is an N (k) such thatm(EN (k)) is as small as we like, say less than
2−kǫ. Let A =⋃
kEN (k). Then for x outsideA, we have sup |fn(x)−f (x)| ≤
1/k for all n>N (k), and therefore sup |fn(x) −f (x)| → 0. In other words,
fn →f uniformly outside the set A; and m(A) ≤ǫ.
Finitely-additive measures on N. The natural numbers admit a ﬁnitely-
additive measure deﬁned on all subsets, and vanishing on ﬁnite sets. (Such
a measure is cannot be countably additive.) This constructi on gives a ‘pos-
itive’ use of the Axiom of Choice, to construct a measure rath er than to
construct a non-measurable set.
Filter: F ⊂ P (X) such that sets in F are ‘big’:
(1) ∅ ⁄∈ F,
(2) A ∈ F,B ⊂A =⇒ B ∈ F ; and
(3) A,B ∈ F =⇒ A ∩B ∈ F .
Example: the coﬁnite ﬁlter (if X is inﬁnite).
Example: the ‘principal’ ultraﬁlter Fx of all sets with x ∈F . This is an
ultraﬁlter : if X =A ⊔B then A or B is in F.
Theorem 1.11 Any ﬁlter is contained in an ultraﬁlter.
8

Proof. Using Zorn’s lemma, take a maximal ﬁlter F containing the given
one. Suppose neither A nor X −A is in F. Adjoining to F all sets of the
form F ∩A, we obtain a larger ﬁlter F′, a contradiction. (To check ∅ ⁄∈ F′:
if A ∩F = ∅ then X −A is a superset of F , so X −A was in F.)
Ideals and ﬁlters. In the ring R = (Z/2)X , ideals I ⁄=R and ﬁlters are in
bijection: I = {A : ~A ∈ F }. The ideal consists of ‘small’ sets, those whose
complements are big.
(By (2), A ∈ I =⇒ AB ∈ I. By (3), A,B ∈ I =⇒ A ∪B ∈ I =⇒
(A ∪B)(A△B) = A +B ∈I.)
Lemma: if F is an ultraﬁlter and A ∪B =F ∈ F then A or B is in F.
Proof. We prove the contrapositive. If neither A norB is in F, then their
complements satisfy ~A,~B ∈ F . Since F is a ﬁlter,
~A ∩ ~B = ~A ∪B ∈ F
and thus A ∪B ⁄∈ F.
Corollary: Ultraﬁlters correspond to prime ideals.
By Zorn’s Lemma, every ideal is contained in a maximal ideal; this gives
another construction of ultraﬁlters.
Measures. Let F be an ultraﬁlter. Then we get a ﬁnitely-additive measure
on all subsets of X by setting m(F ) = 1 or 0 according to F ∈ F or not.
Conversely, any 0/1-valued ﬁnitely additive measure on P(X) determines a
ﬁlter.
Measures supported at inﬁnity . The most interesting case is to take the
coﬁnite ﬁlter, and extend it in some way to an ultraﬁlter. The n we obtain a
ﬁnitely-additive measure on P(X) such that points have zero measure but
m(X) = 1. When X = N such a measure cannot be countably additive.
1.3 Integration
We will write f = limfn if f (x) = lim fn(x) for all x ∈ R. Because lim fn
is measurable whenever each fn is, the measurable functions turn out to
work well to represent points in the metric spaces obtained b y completing
the integrable, compactly supported continuous or smooth f unctions (those
satisfying
∫
|f |< ∞,
∫
|f |p< ∞, etc.
Our next goal is to extend the theory of integration to measur able func-
tions.
A simple function φ is a measurable function taking only ﬁnite many
values. It has a canonical representation as φ = ∑ N
1 aiχEi where the ai
9

enumerate the nonzero values of φ andEi = {φ =ai} are disjoint sets. The
simple functions form a vector space.
Simple integration. For a simple function supported on a set of ﬁnite
measure, we deﬁne
∫
φ =
∫ ∑
aiχEi =
∑
aim(Ei).
We also deﬁne
∫
Eφ =
∫
φχE .
Example:
∫
χQ = 0.
Theorem 1.12 Integration is linear on the vector space of simple function s.
Proof. Clearly
∫
aφ =a
∫
φ. We must prove
∫
φ +ψ =
∫
φ +
∫
ψ.
First note that for any representation of φ as∑ biχFi with the sets Fi
disjoint, we have
∫
φ =∑ bim(Fi). Indeed,
∫ ∑
biχFi =
∫ ∑
ajχS
bi=ajFi =
∑
aj
∑
bi=aj
m(Fi) =
∑
bim(Fi).
Now take the ﬁnite collection of sets Fi on which φ andψ are both constant,
and write φ =∑ aiχFi andψ =∑ biχFi. Then
∫
φ +ψ =
∑
(ai +bi)m(Fi) =
∫
φ +
∫
ψ.
The Lebesgue integral. Now let E be a set of ﬁnite measure, let f :E →
R be a function and assume |f | ≤ M . We deﬁne the Lebesgue integral by
∫
E
f = inf
ψ≥f
∫
E
ψ = sup
f≥φ
∫
E
φ,
assuming sup and inf agree. (Here φ and ψ are required to be simple func-
tions.)
Theorem 1.13 The two deﬁnitions of the integral of f above agree iﬀ f is
a measurable function.
10

Proof. Suppose f is measurable. Since
∫
ψ ≥
∫
φ, we just need to show
the simple functions φ and ψ can be chosen such that their integrals are
arbitrarily close. To this end, cut the interval [ −M,M ] into N pieces
[ai,ai+1) of length less than ǫ. Let Ei be the set on which f (x) lies in
[ai,ai+1). Then φ =∑ aiχEi and ψ =∑ ai+1χEi satisfying φ ≤f ≤ψ and∫
(ψ −φ) ≤ǫm(E), so we are done.
Conversely, if the sup and inf agree, then we can choose simpl e functions
φn ≤ f ≤ ψn such that
∫
(ψn −φn) → 0. Let φ = supφn and ψ = inf ψn.
Then φ and ψ are measurable, and φ ≤f ≤ψ.
We claim φ =ψ a.e. (and thus f is measurable). Otherwise, there is a
set of positive measure A and an ǫ> 0 such that ψ −ψ >ǫ onA. But then
ǫχA ≤ψn −φn for all n, and thus
∫
ψn −φn ≥ǫm(A)> 0.
Theorem 1.14 Letf be a bounded function on an interval [a,b ], and sup-
pose f is Riemann integrable. Then f is also Lebesgue integrable, and the
two integrals agree.
Proof. Iff is Riemann integrable then there are step functions φn ≤f ≤
ψn with
∫
(ψn −φn) → 0. Since step functions are special cases of simple
functions, we see f is Lebesgue integrable.
It is now easy to check that the integral of bounded functions over sets
of ﬁnite measure satisﬁes expected properties:
The integral is linear.
If f ≤g then
∫
f ≤
∫
g.
In particular |
∫
f | ≤
∫
|f |, and if A ≤ f ≤ B then Am(E) ≤
∫
Ef ≤
Bm(E).
For disjoint sets,
∫
A∪Bf =
∫
Af +
∫
Bf . The most interesting assertion
is
∫
(f +g) =
∫
f +
∫
g. If ψ1 ≥f and ψ2 ≥g then ψ1 +ψ2 ≥f +g, so by
the inﬁmum deﬁnition of the integral we get
∫
(f +g) ≤
∫
f +
∫
g. To get
the reverse inequality, use the supremum deﬁnition.
Theorem 1.15 (Bounded convergence) Let fn → f (pointwise) Theo-
rem (Bounded convergence) Letfn →f (pointwise) on a set of ﬁnite measure
E, where |fn|, |f | ≤ M . Then
∫
Efn →
∫
Ef .
Proof. We will use Littlewood’s 3rd Principle. Ignoring a set A of small
measure, the convergence is uniform. Then
⏐
⏐
⏐
⏐
∫
E−A
fn −f
⏐
⏐
⏐
⏐ ≤
∫
E−A
|fn −f | ≤ m(E −A) sup
E−A
|fn −f | → 0.
11

On the other hand, |
∫
Afn| and |
∫
Af | are both less than Mm (A), so ig-
noring A makes only a small change in the integrals and therefore we ha ve
convergence.
Banach limits. If we mimic the deﬁnition of the Lebesgue integral using a
ﬁnitely-additive, non-atomic measure on N (i.e. a non-principal ultraﬁlter),
then we obtain a linear map
L :ℓ∞(N) → R
with L(an) ≥ 0 if (an) ≥ 0, and with L(an) = liman if the limit exists.
The general Lebesgue integral. Forf ≥ 0 we deﬁne
∫
f = sup 0≤g≤f
∫
g,
where g ranges over bounded functions supported on sets of ﬁnite mea -
sure. Clearly this is the same as saying
∫
f = lim =
∫
fM , where fM =
min(f,M )|[−M,M ].
For general f , we require that
∫
|f | < ∞ before
∫
f is deﬁned. Then
writing f =f+ −f−, we deﬁne
∫
f =
∫
f+ −
∫
f−.
Linearity . Let us check that
∫
(f +g) =
∫
f +
∫
g. First suppose f,g ≥ 0.
Then from 0 ≤ f1 ≤ f and 0 ≤ g1 ≤ g we get 0 ≤ f1 +g1 ≤ f +g,
so
∫
(f +g) ≥
∫
f +
∫
g. On the other hand, given 0 ≤ h ≤ f +g we
can write h = f1 +g1 with f1 = min(f,h ); then f1 ≤ f and g1 ≤ g so∫
f +g ≤
∫
f +
∫
g. This completes the proof for positive functions.
For the general case, note that if f = g −h with g,h ≥ 0 integrable
functions, then
∫
f =
∫
g −
∫
h. Indeed, we have g ≥ f+ and h ≥ f−, so
their diﬀerences are positive, and indeed ( g −f+) = ( h −f−). Thus by
linearity for positive functions, we get
∫
g −h =
∫
(f+ +g −f+) −
∫
(f− +h −f−)
=
(∫
f+ −
∫
f−
)
+
(∫
(g −f+) −
∫
(h −f−)
)
=
∫
f.
Now to prove linearity, just note that if f = g +h, then f = (g+ +
h+) − (g− +h−) expresses f as a sum of two positive integrable functions.
Integrating each one and using linearity for positive funct ions we get
∫
f =∫
g +
∫
h.
Integrals and limits. In general from fn →f we can deduce no relation-
ship between
∫
f and
∫
fn. The basic example of the tent functions can be
made positive or negative; we can even get
∫
fn to oscillate in an arbitrary
way, while fn → 0 a.e. (This ‘a.e.’ often signals ‘pointwise convergence’. )
Positive functions. The situation is better if f,fn ≥ 0, and fn → f .
There are two main results:
12

Fatou’s Lemma:
∫
f ≤ lim inf
∫
fn.
Monotone Convergence: if f1 ≤f2 ≤... , then
∫
f = lim
∫
fn.
Proofs: For Fatou’s lemma, let g be a bounded function with bounded
support such that g ≤ f and (
∫
f ) −ǫ ≤
∫
g. Then gn = min(g,fn) → g
and gn ≤fn, so
(∫
f
)
−ǫ ≤
∫
g = lim
∫
gn ≤ lim inf
∫
fn.
Here we have used the Bounded Convergence Theorem to interch ange inte-
grals and limits.
Letting ǫ → 0 gives the result.
For monotone convergence: Since f ≥ fn for all n, we have
∫
f ≥
lim sup
∫
fn, while
∫
f ≤ lim inf
∫
fn by Fatou’s Lemma.
Theorem 1.16 (Modulus of integrability) Letf ≥ 0 be integrable. Then
for any ǫ> 0 there is a δ >0 such that m(E)<δ =⇒
∫
Ef <ǫ.
Corollary 1.17 The function F (t) =
∫ t
−∞f (x)dx is uniformly continuous
on R.
Proof of the Theorem. LetfM = min(M,f ). Then fM →f monotonely
as M → ∞, and thus
∫
(f −fM ) → 0. Choose M large enough that
∫
(f −
fM ) < ǫ/2. Then for m(E) < δ= ǫ/(2M ), we have
∫
Ef ≤
∫
E(f −fM ) +
Mm (E) ≤ǫ.
Dominated convergence. Let fn → f , with |fn|, |f | ≤ g and
∫
g < ∞.
Then
∫
fn →
∫
f .
Proof. Givenǫ> 0 there is a δ >0 such that
∫
Ag <ǫ wheneverm(A)<δ .
We can also choose M such that
∫
Eg < ǫ outside [ −M,M ]. Then by
Littlewood’s 3rd principle, there is a set A ⊂ [−M,M ] with m(A) < δ
outside of which fn →f uniformly. Thus
lim sup
⏐
⏐
⏐
⏐
∫
fn −f
⏐
⏐
⏐
⏐ ≤ 2
(∫
R−[−M,M ]
g +
∫
A
g
)
≤ 4ǫ.
Since ǫ was arbitrary,
∫
fn →
∫
f .
Derivatives. Even if f′(x) exists everywhere, the behavior of f′(x) can be
very wild – e.g. not integrable. For example, if f (x) is any function smooth
13

away from x = 0, and |f (x)| ≤ | x|2, then f is diﬀerentiable at 0; but we
can make f′(x) wild, e.g. look at f (x) = x2 sin(e1/x2
x). In particular, f′(x)
need not be integrable.
Here is an easy theorem illustrating the preceding results.
Theorem 1.18 Supposef (x) is diﬀerentiable on R, vanishes outside [0, 1]
and |f′(x)| ≤ M . Then
∫ t
0f′(x)dx =f (t).
Proof. Sincef is diﬀerentiable it is continuous, and fn(x) = n(f (x+1/n)−
f (x)) →f′(x) pointwise. By the mean-value theorem, |fn(x)| = |f′(y)| ≤ M
for some y ∈ [x,x + 1/n]. Thus
∫
fn →
∫
f′. But
∫ t
0
fn(x)dx =n
∫ t+1/n
t
f (t)dt →f (t)
by continuity of f .
Convergence in measure. All the theorems about pointwise convergence
also hold for convergence in measure. This can be proved usin g the following
useful fact.
Theorem 1.19 Iffn →f in measure, then there is a subsequence such that
fn →f pointwise a.e.
As a warm-up to this fact, we prove the easy part of the Borel-C antelli
lemma.
Lemma 1.20 If ∑ m(En) < ∞, then lim supEn, the set of points x that
belong to En for inﬁnitely many n has measure zero.
Remark: χlim supEn = lim supχEn.
Proof. For any N >0, we have
m(lim supEn) ≤m(
∞⋃
N
En) ≤
∞∑
N
m(En) → 0
as N → ∞.
14

Proof of the Theorem. For each k > 0 there is an n(k) such that
Ek = {|f −fn(k)|> 2−k} satisﬁes m(Ek)< 2−k. We claim fn(k)(x) →f (x)
a.e. as k → ∞ . Indeed, ∑ m(Ek) < ∞, so almost every x belongs to but
ﬁnitely many Ek. And ﬁxing x, for all k large enough that x ⁄∈Ek we
|f (x) −fn(k)| ≤ 2−k → 0.
Sample application. Suppose g is integrable, |fn| ≤ g for all n and
fn →f in measure. Then
∫
fn →
∫
f .
Proof. Let A be any limit point of
∫
fn, possibly ±∞. We will show
A =
∫
f .
Pass to a subsequence such that
∫
fn →A. Pass to a further subsequence
so fn → f pointwise. By the pointwise theorem we get
∫
fn →
∫
f , so
A =
∫
f . Since A was any limit point of the original sequence
∫
fn, we have∫
fn →
∫
f .
2 Diﬀerentiation and Integration
F unctions that are diﬀerentiable everywhere. Even if f′(x) exists
everywhere, it does not have to be continuous. For example, i f |f (x)| ≤ x2,
then no matter how badly f′(x) oscillates near x = 0, we have f′(0) = 0.
As an application of interchange of integrals, we can ask: if f′(x) exists
everywhere, then can we assert
∫ b
a
f′(x) = f (b) −f (a)?
The answer is no in general, since
∫ b
a |f′(x)| might be inﬁnite. However, we
can approach the problem by deﬁning gn(x) = n(f (x + 1/n) −f (x)). Then
clearly gn(x) →f′(x) pointwise, and by continuity of f it is easy to see
∫ b
a
gn(x) →f (b) −f (a).
So it is simply a question of interchanging integration and l imits. For ex-
ample, if f is Lipschitz, then gn is bounded, so by the bounded convergence
theorem, f is the integral of f′. More generally, the same conclusion holds
if we can ﬁnd a locally integrable function h such that
|f (x +t) −f (x)| ≤ th(x).
for |t| ≤ 1.
15

A nowhere diﬀerentiable function.
Let f (x) = ∑ ∞
1 an sin(bnx), where ∑ an converges quickly but bnan →
∞ rapidly. For concreteness, we take an = 10−n, bn = 106n.
Then for any n, we can choose t ≈ 1/bn such that ∆ an sin(bnx) ≍ an.
Fork <n, we have
∑
∆ ak sin(bkx) ≤
∑
akbk/bn ≍an−1bn−1/bn ≪an,
and for k >n we have
∆ ak sin(bkx) ≤ak ≪an
Thus ∆ f/ ∆ x ≍an/t ≍anbn → ∞, so f′(x) does not exists.
Riemann’s ‘example’. Riemann thought that the function
f (x) =
∑
exp(2πin2x)/n2
was nowhere diﬀerentiable. This is almost true, however it t urns out that
f′(x) actually does exists at certain rational points.
Monotone functions. We say f : [a,b ] → R is increasing if x ≤ y =⇒
f (x) ≤f (y). If f or −f is increasing then f is monotone.
Example: write Q = {q1,q 2,... } and set f (x) = ∑
qi<x 2−i. Then
f : R → R is monotone increasing, and f has a dense set of points of
discontinuity.
Theorem 2.1 A monotone function f : [a,b ] → R is diﬀerentiable almost
everywhere.
Thus the oscillations of the preceding example are necessary to produce
nowhere diﬀerentiability.
Gleason has remarked that this property of monotone functio ns helped
lead him to his proof of Hilbert’s 5th problem (which topolog ical groups are
Lie groups?).
The proof of the Theorem will use the Vitali covering lemma.
Vitali coverings. Here is use an important covering argument based on
the ‘greedy algorithm’.
LetK be a compact subset of a metric space ( X,d ). A collection of balls
B forms a Vitali covering ofK if for every x ∈K andr> 0 there is a B ∈ B
with x ∈B ⊂B(x,r ).
We can be rather loose about the boundary of B: it is only necessary
that B(y,s ) ⊂ B ⊂
B(y,s ) for some open ball B(y,s ). In the case of the
real numbers, this means B can be any interval except a degenerate one
[a,a ].
16

Theorem 2.2 For any Vitali covering B of K, there is a sequence of dis-
joint balls ⟨B(yi,ri)⟩in B such that K ⊂⋃ B(yi, 3ri). In fact for any N >0
we have
K ⊂
N⋃
1
B(yi,ri) ∪
∞⋃
N +1
B(yi, 3ri).
Proof. Since K is compact, we can assume B is a countable set of balls
whose diameters tend to zero. (For each n, extract from K a ﬁnite subcover
Bn by balls of diameter < 1/n, and replace B with ⋃ ∞
1 Bn — it is still a
cover in the sense of Vitali.)
To construct the disjoint balls, we use the greedy algorithm. Let B(y1,r 1)
be the largest ball in B, and deﬁne B(yn+1,rn+1) inductively as one of
the largest balls among those in B disjoint from the ones already chosen,
B(y1,r 1),...,B (yn,rn).
We claim K ⊂⋃ B(yi, 3ri). Indeed, if x ∈ K then x belongs to some
ballB(y,r ) ∈ B . If B(y,r ) belongs to the sequence of chosen balls B(yi,ri),
then we are done — x is covered.
Otherwise, consider the ﬁrst i for which ri < r. Since B(y,r ) was not
chosen at the ith stage in the inductive deﬁnition, it must meet one of the
earlier balls — say B(yj,rj), with j <i. But then we have rj ≥r, and since
they meet, B(yj, 3rj ) contains B(y,r ). In particular, it contains x.
Now suppose we have N >0 and x ∈K −⋃ N
1 B(yi,ri). Then since the
union of the ﬁrst N balls is closed, there is a ball B(y,r ) ∈ B disjoint from
the ﬁrst N balls and containing x. Once again, by the nature of the greedy
algorithm B(y,r ) must meet B(yi,ri) for some i with ri ≥r; but this time
by our choice of B(y,r ) we can insure that i > N. Since ri ≥ r we have
x ∈⋃ ∞
N +1B(yi, 3ri).
Theorem 2.3 (Vitali covering lemma) For any Vitali covering B of a
setE ⊂ R of ﬁnite measure, and ǫ> 0, there is a ﬁnite collection of disjoint
balls B1,...,B n in B with m(E△⋃ n
1Bi)<ǫ .
Proof. Since m(E) is ﬁnite, we can ﬁnd a compact K and an open U
such that K ⊂E ⊂U and m(K), m(E) and m(U ) all diﬀer by at most ǫ.
Remove from B any balls that are not contained in U ; then B is still a Vitali
covering of E, and hence of K.
Now extract a sequence of disjoint balls ⟨Bi =B(yi,ri)⟩from B by the
greedy algorithm. Then by Vitali’s Lemma, we have m(⋃ Bi) = ∑ 2ri ≤
17

m(U )< ∞, so we can choose n> 0 such that ∑ ∞
n+1ri<ǫ . Then K −⋃ n
1Bi
is covered by ⋃ ∞
n+1B(yi, 3ri), and therefore
m(K −
n⋃
1
Bi) ≤
∞∑
n+1
6ri < 6ǫ.
We also havem(E −K)<ǫ , so m(E −⋃ n
1Bi)< 7ǫ. Finally m(⋃ n
1Bi −E) ≤
m(U −E)<ǫ , so we conclude m(E△⋃ n
1Bi)< 8ǫ.
Proof of monotone diﬀerentiability. We will assume f : [a,b ] → R is
monotone increasing. For any set A ⊂ R let [A] be the smallest interval
containing it, so m[A] = sup A − infA.
Fix rational numbers 0 ≤u<v and consider the set E ⊂ [a,b ] of those
x for which there are arbitrarily small t such that m[f (x +t),f (x)] ≤ ut
and also arbitrarily small t such that m[f (x −t),f (x)] ≥vt. This means the
derivative of f measured from above x wants to lie below u, but from the
right is wants to lie above v, and we have u<v sof is not diﬀerentiable at
x.
The set of all points where f is not diﬀerentiable is a countable union
of sets of the same basic form as E, so we will be content to show E has
measure zero. Also the points of discontinuity of f are countable, so we can
assume f is continuous on E.
The idea of the proof is to show that m(f (E)) = um(E) = vm(E) and
thusm(E) = 0.
More precisely, there is a Vitali covering B ofE by intervals of the form
B = [x,x +t] with m[f (B)]/m(B)<u . From these extract a ﬁnite disjoint
coverB1,...B n with m(E△⋃ n
1Bi)<ǫ . Then we have
∑
m[f (Bi)] ≤u
∑
m(Bi) ≤u(m(E) +ǫ).
Now let A =E ∩⋃ n
1 int(Bi). There is a Vitali covering of A by intervals
C = [x −t,x ] expanded under f by a factor of at least v, and with C ⊂Bi
for some i. We can extract a ﬁnite union of disjoint balls C1,...C m such
that∑ m(Ci)>m (A) −ǫ>m (E) − 2ǫ. Then we ﬁnd
∑
m[f (Ci)] ≥v
∑
m(Ci) ≥v(m(E) − 2ǫ).
But each Ci is a subset of some Bj, so we have
v(m(E) − 2ǫ) ≤
m∑
1
m[f (Ci)]
≤
n∑
1
m[f (Bj)] ≤u(m(E) +ǫ).
18

Letting ǫ → 0 we ﬁnd vm(E) ≤um(E) and thus m(E) = 0.
Theorem 2.4 (Integral of the derivative) If f : [a,b ] → R is mono-
tone, then
∫ b
a f′(x)dx ≤f (b) −f (a).
Proof. Deﬁne fn(x) = n(f (x + 1/n) −f (x)) ≥ 0. Then fn(x) →f′(x), so
by Fatou’s lemma we have
∫
f′ ≤ lim inf inffn. But
∫
fn is, for n large, the
diﬀerence between the averages of f over two disjoint intervals, so it is less
than or equal to the maximum variation f (b) −f (a).
0.2 0.4 0.6 0.8 1
0.2
0.4
0.6
0.8
1
Figure 1. Cantor’s function: the devil’s staircase.
Singular functions. A monotone function is singular if f′(x) = 0 a.e.
An example is the Cantor function or ‘devil’s staircase’,
f (0.a1a2a3... ) =
∑
{2−i : ai ≤ 1 andaj ⁄= 1, 1 ≤j <i.}
where x = 0.a1a2a3... in base 3.
This monotone function has the amazing property that it is co ntinuous,
and it climbs from 0 to 1, but f′(x) = 0 a.e. On the other hand, f′(x)
does not exist (or equals inﬁnity) for x in the Cantor set (in fact f stretches
19

intervals of length 3−n to length 2−n, and so even for a monotone function
f′(x) can fail to exist on an uncountable set (necessarily of meas ure zero).
There is a more sophisticated example, due to Whitney, of a fu nction
f (x,y ) on the plane whose derivatives exist everywhere, but which is not
constant on its critical set. This function describes the to pography of a hill
with a (fractal) road running from top to bottom passing only along the
level or ﬂat parts of the hillside.
Bounded variation. We note that if f = g −h where g and h are both
monotone, then f′(x) also exists a.e. So it is desirable to characterize the
full vector space of functions spanned by the monotone funct ions.
A function f : [a,b ] → R has bounded variation if
sup
n∑
1
|f (ai) −f (ai−1)| = ‖f ‖BV < ∞.
Here the sup is over all ﬁnite dissections of [ a,b ] into subintervals, a =a0<
a1 <...a n =b. This supremum is called the total variation of f over [a,b ].
Theorem 2.5 A function f is of bounded variation iﬀ f (x) = g(x) −h(x)
whereg and h are monotone increasing.
Proof. Clearly ‖f ‖BV =f (b) −f (a) if f is monotone increasing, and thus
f has bounded variation if it is a diﬀerence of monotone functi ons.
For the converse, deﬁne
f+(x) = sup
n∑
1
max(0,f (ai) −f (ai−1)),
over all partitions a =a0 <...<a n =x, and similarly
f−(x) = sup
n∑
1
max(0, −f (ai) +f (ai−1)).
Clearlyf+ andf− are monotone increasing, and they are bounded since the
total variation of f is bounded.
We claimf (x) = f (a) +f+(x) −f+(x). To see this, note that if we reﬁne
our dissection of [a,b ], then both f+ andf− increase. Thus for any ǫ> 0, we
can ﬁnd a dissection for which both sums are within ǫ of their supremums.
20

But for a common partition, it is clear that
sup
n∑
1
max(0,f (ai) −f (ai−1)) − max(0, −f (ai) +f (ai−1))
= sup
n∑
1
f (ai) −f (ai−1) = f (x) −f (a).
Thusf (x) = f (a) +f+(x) −f−(x).
Corollary 2.6 Any function of bounded variation is diﬀerentiable a.e.
Theorem 2.7 (Lebesgue Density) LetE ⊂ R be a measurable set. Then
for almost every x ∈ R,
lim
r→0
m(E ∩B(x,r ))
m(B(x,r )) =
{
1 if x ∈E,
0 otherwise.
Derivative of the integral. This theorem says that if we let F (x) =∫ x
−∞f (t)dt, where f (t) = χE(t), then F′(x) exists a.e. and F′(x) = f (x)
a.e. We will eventually prove that this is the case for all integrablef .
Proof of Lebesgue density. We consider the case E ⊂ [0, 1]. Let En be
the set of x ∈E such that lim inf m(E ∩B(x,r ))/2r <1 − 1/n. Using the
Vitali lemma, we can ﬁnd a ﬁnite set of disjoint intervals I1,...I N such that
m(En△⋃ Ii)<ǫ and the density of E in Ii is less than 1 − 1/n. Then
m(En) −ǫ ≤ m(E ∩
⋃
Ii) =
∑ m(E ∩Ii)
m(Ii) m(Ii)
≤ (1 − 1/n)
∑
m(Ii) ≤ (1 − 1/n)(m(En) +ǫ).
Since ǫ was arbitrary, we get m(En) ≤ (1 − 1/n)m(En) and therefore
m(En)=0.
Thus the limit in the Theorem exists and equals 1 for all x ∈E −⋃ En,
so we have demonstrated half of the Theorem. For the other hal f, replace E
with [0, 1] −E.
21

The Lebesgue density theorem has many basic applications in ergodic
theory. Here is an example.
Theorem 2.8 Letθ ∈ R − Q be an irrational number, and deﬁne f :S1 →
S1 byf (x) = x+θ mod 1. Then f is ergodic: if E ⊂S1 has positive measure,
and f (E) ⊂E, then m(E) = 1 .
Proof. Let δr(x) = m(E ∩B(x,r ))/m(B(x,r )). Since E has positive
measure, there is an x0 ∈E such that for any ǫ> 0 there is an r >0 with
δr(x0)> 1 −ǫ. By invariance of E,δr is constant along the orbits of f . But
each orbit is dense, so we have δr(x) > 1 −ǫ along the dense set ⟨fn(x)⟩.
Since δr(x) is continuous, it is bounded below by 1 −ǫ everywhere. Thus
limr→0δr(x) = 1 = χE(x) a.e., and thus m(E) = 1.
Corollary. Any measurable function h : S1 → R, invariant under the
irrational rotational f , is constant a.e.
Proof. For any partition of R into disjoint intervals Ii of length ǫ, we have
m(f−1(Ii)) = 1 for exactly one i. As ǫ → 0, this distinguished interval
shrinks down to the constant value assumed by f .
Absolute continuity . A function F : [a,b ] → R is absolutely continu-
ous if for any ǫ > 0, there is a δ > 0 such that for any ﬁnite set of non-
overlapping intervals (ai,bi), if ∑ n
1 |ai −bi|<ǫ then∑ n
1 |f (ai) −f (bi)|<δ .
Theorem 2.9 An absolutely continuous function is continuous and of boun ded
variation.
Proof. Continuity is clear. As for bounded variation, choose ǫ and δ as
above; then over any interval of length δ, the total variation of f is at most
ǫ, so over [ a,b ] we have variation about ǫ(b −a)/δ.
Theorem 2.10 Let F : [a,b ] → [c,d ] be an absolutely continuous homeo-
morphism. Then m(A) = 0 implies m(F (A)) = 0 .
Proof. Given ǫ > 0, choose δ as guaranteed by absolute continuity, and
coverA by disjoint open intervals Ii = (ai,bi) with ∑ ∞
1 |bi −ai|<δ . Since
f is a homeomorphism, we have
m(f (A)) ≤m(
⋃
f (Ii)) ≤
∑
m(f (Ii)) =
∑
|f (bi) −f (ai)|<ǫ.
Thusm(f (A)) = 0.
22

Theorem 2.11 The derivative D(F ) = f (x) = F′(x) establishes a bijective
correspondence:
D : {absolutely continuous F : [a,b ] → R, F (a) = 0 } ↔
{integrablef : [a,b ] → R}.
The inverse is given by I(f ) = F (x) =
∫ x
a f (t)dt.
Lemma 2.12 If f is integrable then F (x) =
∫ x
a f is absolutely continuous.
Proof. This follows from the fact that for any ǫ> 0 there is a δ >0 such
that
∫
A |f |<ǫ wheneverm(A)<δ .
Lemma. If f is absolutely continuous, then it is of bounded variation,
so f′(x) is integrable.
Proof. The bounded variation is clear; then f =f+ −f−, both monotone
increasing, and we have
∫
|f′| ≤
∫
f′
+ +f′
− ≤f+(b) −f+(a) +f−(b) −f−(a) = ‖f ‖BV < ∞.
Now we show the derivative of an integral gives the expected r esult. We
have already proved this for the indicator function of a meas urable set; the
following argument gives a diﬀerent proof.
Lemma. If f : [a,b ] → R is integrable, and F (x) =
∫ x
a f (t)dt = 0 for all
x, then f = 0. (This shows injectivity of the map I.)
Proof. Consider the collection of all sets over which the integral o f f is
zero. By assumption this contains all intervals in [ a,b ], and it is closed
under countable unions and complements. Thus it contains al l closed sets
in [a,b ]. But if f ⁄= 0, then either {f >0} or {f <0} contains a closed set
F of positive measure. Then
∫
Ff ⁄= 0, contradiction. Thus f = 0.
Theorem 2.13 If f is bounded, then F = I(f ) is Lipschitz and satisﬁes
F′(x) = f (x) a.e.
Proof. Suppose |f | ≤ M ; then clearly |F (x + t) −F (x)| ≤ Mt . We
will show
∫ c
aF′(x) −f (x)dx = 0 for all c. To this end, just note that
F′(x) = lim Fn(x) = n(F (x + 1/n) −F (x)) satisﬁes |Fn| ≤ M , so it is a
pointwise limit of bounded functions. Thus
∫ c
a
F′(x)dx = lim
∫ c
a
Fn(x)dx = limn
(∫ b+1/n
c
F −
∫ a+1/n
a
F
)
= F (c) −F (a) =
∫ c
a
f (x)dx,
23

by continuity of F .
Theorem 2.14 Even if f is unbounded, but integrable, we have D(I(f )) =
f .
Proof. By linearity, it is enough to prove this assertion for positi vef . Let
fn = min(n,f ) → f , an increasing sequence, and let Fn = I(fn). Then
F =I(f −fn) +Fn and since I(f −fn) is a monotone increasing function,
we have
F′(x) ≥F′
n(x) = fn(x)
a.e. (using the result D(I(fn)) = fn for bounded fn). Therefore
∫ c
a
F′(x)dx ≥
∫ c
a
fn(x)dx =Fn(c) →F (c).
On the other hand,
∫ c
a
F′(x)dx ≤F (c) −F (a) = F (c)
by our general results on integration of increasing functio ns. Thus equality
holds, and we have shown
∫ c
a
F′(x) −f (x)dx = 0
for all c. Thus F′(x) = f (x) a.e.
Now we turn to the converse inequality: to show I(D(F )) = F for all
absolutely continuous F . This direction is a little easier.
Lemma. If F is absolutely continuous and F′(x) = 0 a.e. then F is
constant.
Proof. (This veriﬁes injectivity of D.) Pick any c ∈ [a,b ]. Using the Vitali
lemma, cover [ a,c ] with a ﬁnite number of intervals I1,...,I n such that
|∆ F/∆ t| < ǫ over these intervals, and what’s left over has total measure
at most ǫ. Then by absolutely continuity, the total variation of F over the
complementary intervals is at most δ. Thus
|F (c) −F (a)| ≤ δ +ǫ
∑
m(Ii) ≤δ +ǫ(b −a),
and this can be made arbitrarily small so F (c) = F (a).
24

Theorem 2.15 I(D(F )) = F .
Proof. Let f = F′(x), and let G = I(f ); then we’ve seen that G is
absolutely continuous, and G′(x) = f (x) = F′(x) a.e., so ( G −F )′(x) = 0
a.e. implies G −F is a constant. By our normalization, G(a) = F (a) = 0,
so F =G =I(D(F )).
Summary: letting M =monotone functions, we have
BV =M −M ⊃AC ⇐ ⇒f =
∫
f′.
We will eventually see the diﬀerentiation form of this setup :
{signed µ } = {µ −ν : µ,ν ≥ 0} ⊃ {µ =f (x)dx} ⇐ ⇒ L1(R).
Convexity . A function f : R → R is convex if for all x,y ∈ R andt ≥ 0 we
have
f (tx + (1 −t)y) ≤tf (x) + (1 −t)f (y).
In other words, the graph of the function f lies below every one of its chords.
Theorem 2.16 The right and left derivatives of a convex function exist for
all x, and agree outside a countable set.
Proof. The secant lines move monotonely.
We have yet to use the Monotone Convergence Theorem. When can we
assert that the approximations to the derivative, ft(x) = (f (x +t) −f (x))/t,
converge to f′(x) monotonely as t decreases to zero?
Answer: when f is a convex function!
Theorem 2.17 A function f is convex iﬀ f is absolutely continuous and
f′(x) is increasing.
Proof. Suppose f is convex. Then the slope of the secant line ft(x) =
(f (x +t) −f (x))/t is an increasing function of t and of x. It follows that
ft(x) is uniformly bounded on any compact interval [ c,d ] in the domain of
f . Thus f is Lipschitz, which implies it is absolutely continuously. Finally
f′(x) is increasing since it is a limit of increasing functions.
25

For the converse, just note that when f is absolutely continuous, the
secant slope
ft(x) = 1
t
∫ x+t
x
f′(s)dx
is just the average of f′. But the average of an increasing function is itself
increasing, so the secants of the graph of f have increasing slope, which
implies f is convex.
Corollary 2.18 If f (x) is convex, then f′′(x) exists a.e. and f′′(x) ≥ 0.
Theorem 2.19 (Jensen’s inequality) Iff : R → R is a convex function,
and X : [0, 1] → R is integrable, then
f
(∫
X
)
≤
∫
f (X) =
∫ 1
0
f (X(t))dt.
Proof. First note that equality holds if f is a linear function. Also, both
sides of the equation are linear functions of f (under pointwise addition).
So it is enough to prove the result after modifying f by a linear function. To
this end, let m =
∫
X be the mean of X, take a linear supporting function
g(x) = ax +b with g(m) = f (m) and g(x) ≤f (x) otherwise; and replace f
with f −g. Then f (
∫
X) = 0 but
∫
f (X) ≥ 0.
Probabilistic interpretation. If f is convex, then E(f (X)) ≥ f (E(X))
for any random variable X. Jensen’s theorem is this statement where the
distribution of the random variable is dictated by the funct ionX : [0, 1] → R.
It includes δ-masses as a special case, since these are obtained when X is
a simple function.
The deﬁnition of convexity says the result holds for random v ariables
assuming just two values x ory, with probabilities t and (1 −t) respectively.
A bettor’s dilemma. You are about to gamble with $100 at a fair game.
A generous patron has oﬀered to square your holdings. Do you a sk for this
boost before you start playing, to increase your stakes, or a fter you have
gambled, to increase your payoﬀ?
Answer: let X denote your payoﬀ. Fairness means E(X) = 100. Since x2
is convex, E(X 2) ≥ (E(X))2, so squaring your payoﬀ is better on average.
Arithmetic/Geometric Mean. As is well-known, for a,b > 0, we have√
ab ≤ (a +b)/2, because:
0 ≤ (√a −
√
b)2/2 = (a +b)/2 −
√
ab.
26

More generally, considering a random variable that assumes valuesa1,...a n
with equal likelihood, the concavity of the logarithm impli es
log
(1
n
∑
ai
)
≥ 1
n
∑
logai
and thus (∏
ai
) 1/n
≤ 1
n
∑
ai.
Mnemonic: To remember the direction of this inequality, note that if
ai ≥ 0 but a1 = 0, then the geometric mean is zero but the arithmetic mean
is not.
Appendix: Measure on [ a, b]. There is a correspondence between mono-
tone functionsf : [a,b ] → R and positive, ﬁnite measures µ on [a,b ], namely:
f (x) = µ [a,x ).
(This function is always continuous on one side: we have f (xn) → f (x) if
xn ↑x.)
Now we will later see that µ =µ a +µ s, where µ a and µ s are absolutely
continuous and singular with respect to Lebesgue measure. ( That is, µ s
vanishes outside a set of Lebesgue measure zero, while µ a(E) =
∫
Eg for
some positive integrable g.) Also [ a,b ] may contain countably many ‘atoms’
for µ , i.e. points with µ (p)> 0 (delta masses).
Then we have the following dictionary:
F unctions Measures
f is monotone increasing µ is a positive measure
f′ exists a.e. f′ =g =dµ a/dx a.e.
f is singular µ =µ s
f is absolutely continuous µ =µ a
f is discontinuous at p p is an atom for µ
countably many discontinuities countably many atoms
Finally one can also consider signed measures; these correspond to func-
tions of bounded variation, and the canonical representati on of f as a
diﬀerence of monotone functions corresponds to the Hahn dec omposition,
µ =µ + −µ−, µ + andµ− mutually singular positive measures.
27

3 The Classical Banach Spaces
A normed linear space is a vector space V over R or C, equipped with a
norm ‖v‖ ≥ 0 deﬁned for every vector, such that:
‖v‖= 0 = ⇒ v = 0;
‖αv‖= |α| · ‖v‖; and
‖v +w‖ ≤ ‖v‖ + ‖w‖. A norm is the marriage of metric and linear
structures. It determines a distance by d(v,w ) = ‖v −w‖.
A Banach space is a complete normed linear space.
The unit ball. It is frequently useful to think of a norm in terms of its
closed unit ball , B = {v : ‖v‖ ≤ 1}. Then we can recover the norm by
‖v‖= inf {α> 0 : v ∈αB}. The conditions above insure:
B contains no line through the origin;
B is symmetric; and
B is convex. Conversely, when checking the sub-additivity of a norm, it
suﬃces to show B is convex.
Theorem 3.1 (V erifying completeness) A normed linear space is com-
plete iﬀ ∑ ‖ai‖< ∞ =⇒ there is an a ∈V such that ∑ N
1 ai →a.
Proof. If ai is a Cauchy sequence in V we can pass to a subsequence such
that d(ai,ai+1) < 2i. Then a1 + (a2 −a1) + (a3 −a2) + ... is absolutely
summable, so it sums to some s ∈V , and ai →s. The converse is obvious.
Example: C(X). Let X be any compact Hausdorﬀ space, and let C(X)
be the vector space of continuous functions f : X → R. Deﬁne ‖f ‖ =
supX |f |. Then ∑ ‖fi‖ < ∞ implies the sum converges uniformly, and
therefore∑ fi(x) = f (x) exists and is continuous; thus C(X) is a Banach
space.
Example: ℓp(I). For any index set I, and 1 ≤p ≤ ∞, we let ℓp(I) denote
the space of sequences a = ⟨ai : i ∈I⟩with
‖a‖p =
(∑
I
|ai|p
) 1/p
,
‖a‖∞ = sup
I
|ai|.
The outer exponent is put in to give homogeneity of degree one .
28

Thusℓp(2) gives a norm on R2, with the unit ball deﬁned by xp +yp ≤ 1.
Note that as p increases from 1 to ∞, these balls are all convex, and they
move steadily from a diamond through a circle to a square. In R3 they move
from an octahedron through a sphere to a cube.
The ‘usual’ℓp spaces refer to ℓp(N). We also have c =c(N) = C(N ∪ ∞),
the space of convergent sequences with the sup norm, and c0 ⊂c, the space
of sequences converging to zero.
The Lp spaces. For any measurable subset E ⊂ R, and 1 ≤ p ≤ ∞ ,
we deﬁne Lp(E) as the set of measurable functions f : E → R such that∫
E |f |p< ∞; and set
‖f ‖p =
(∫
E
|f |p
) 1/p
,
‖f ‖∞ = inf {M ≥ 0 : |f | ≤ M a.e}.
Actually for the norm of f to vanish, it is only necessary for f to vanish a.e.,
so the elements of Lp are technically equivalence classes of functions deﬁned
up to agreement a.e.
Indicator functions. If m(A) is ﬁnite, then ‖χA‖p = (m(A))1/p → 1 as
p → ∞.
The scale of spaces. If m(E) < ∞ then L∞(E) ⊂ Lp(E) ⊂ L1(E), i.e.
the Lp spaces shrink as p rises.
If m(E) = ∞ then there is no comparison.
Theorem 3.2 For 1 ≤ p ≤ ∞ , the space Lp(E) with the norm above is a
Banach space.
Theorem 3.3 (Minkowski’s inequality) ‖f +g‖p ≤ ‖f ‖p + ‖g‖p. For
1<p< ∞, equality holds iﬀ f and g lie on a line in Lp.
Proof. As mentioned above, it suﬃces to verify convexity of the unit ball;
that is, assuming ‖f ‖= ‖g‖= 1, we need only verify
‖tf + (1 −t)g‖ ≤ 1
for 0 <t< 1. In fact by convexity of the function xp, p> 1, we have
∫
|tf + (1 −t)g|p ≤
∫
t|f |p + (1 −t)|g|p ≤t + (1 −t) = 1.
This proves B is convex. For 1 < p, the strict convexity of xp gives strict
convexity of B, furnishing strict inequality unless f andg lie on a line.
29

Completeness. It remains to show Lp is complete. Suppose ∑ ‖fi‖p< ∞.
LetF (x) =∑ |fi(x)|. Then by monotone convergence,
∫
Fp ≤ (∑ ∞
1 ‖fi‖p)p,
so F (x) is ﬁnite a.e. and it lies in Lp. Therefore the same is true for
f (x) = ∑ fi(x), since |f (x)| ≤ F (x); and we have ‖f ‖p ≤ ∑ ‖fi‖p. By
virtue of the last inequality we also have
‖f −
n∑
1
fi‖p ≤
∞∑
n+1
‖fi‖p → 0,
and thus every absolutely summable sequence is summable, an dLp is com-
plete.Theorem 3.4 (Cauchy-Schwarz-Bunyakovskii inequality) Iff andg
are in L2, then fg is in L1 and
⟨f,g ⟩=
∫
fg ≤ ‖f ‖2‖g‖2.
Proof. We can assume f,g ≥ 0. For any t> 0 we have
‖f +tg‖2 ≤ (‖f ‖+t‖g‖)2 ≤ ‖f ‖2 + 2t‖f ‖‖g‖+O(t2),
while at the same time
‖f +tg‖2 = ‖f ‖2 + 2t⟨f,g ⟩+t2‖g‖2 ≥ ‖f ‖2 + 2t⟨f,g ⟩;
comparing terms of size O(t), we ﬁnd ‖f ‖‖g‖ ≥ ⟨f,g ⟩.
This inner product ⟨f,g ⟩is a symmetric, deﬁnite bilinear form making
L2 into a Hilbert space. It is an inﬁnite-dimensional analogue of the inner
product in Rn. For example, if E and F are disjoint measurable sets, then
L2(E) and L2(F ) are orthogonal subspaces inside L2(R).
H¨ older’s inequality . Let’s try to mimic this argument for f ∈ Lp and
g ∈ Lq, with 1 /p + 1/q = 1. Then fp/q ∈ Lq, and using the binomial
expansion for (a +b)q we have:
‖fp/q +tg‖q
q ≤ ‖ fp/q‖q
q +qt‖fp/q‖q−1
q ‖g‖q +O(t2)
= ‖f ‖p
p +qt‖f ‖p‖g‖q +O(t2)
30

since (q − 1)/q = 1/p. On the other hand for f,g ≥ 0 we have (by convexity
of xp),
‖fp/q +tg‖q
q =
∫
|fp/q +tg|q ≥
∫
(fp/q)q +qt(fp/q)q−1g
≥ ‖ f ‖p
p +qt
∫
fg.
Putting these inequalities together gives the theorem.
Y oung’s inequality .One can also prove H¨ older’s inequality using the fact
that ab ≤ap/p +bq/q; this is on the homework.
(Proof of Young’s inequality. Draw the curve y = xp−1, which is the
same as the curve x =yq−1. Then the area inside the rectangle [0 ,a ] × [0,b ]
is bounded above by the sum of ap/p, the area between the graph and [0 ,a ],
and bq/q, the area between the graph and [0 ,b ].)
Theorem 3.5 If f : [a,b ] → R is absolutely continuous, and f′ ∈ Lp[a,b ],
then f is H¨ older continuous of exponent 1 − 1/p.
If p = 1 we get no information. If p = ∞ we get Lipschitz continuity.
Proof. We have
|f (x) −f (y)| =
⏐
⏐
⏐
⏐
∫ y
x
1 ·f′(t)dt
⏐
⏐
⏐
⏐ ≤ ‖χ[x,y]‖q‖f′‖p ≤ ‖f′‖p|x −y|1/q.
Theorem 3.6 (Density of simple functions) For any p and E, simple
functions are dense in Lp(E). For p ⁄= ∞, step, continuous and smooth
functions are dense in Lp(R).
Proof. First we treat f ∈L∞. Then f is bounded, so it is a limit of simple
functions in the usual way (cut the range into ﬁnitely many sm all intervals
and round f down so it takes values in the endpoints of these intervals).
Now for f ∈Lp, p ⁄= ∞, we can truncate f in the domain and range to
obtain bounded functions with compact support, fM →f . Since f −fM → 0
pointwise and |f −fM |p ≤ |f |p, dominated convergence shows ‖f −fM ‖p →
0. Finally we can ﬁnd step, continuous or smooth functions gn → FM
pointwise, and bounded in the same way. Then
∫
|gn−FM |p → 0 by bounded
convergence, so such functions are dense.
31

Note! The step, continuous and smooth functions are not dense in L∞!
Lp as a completion. Given say V = C∞
0 (R) with the L2-norm, it is
exceedingly natural to form the metric completion V of V and obtain a
Banach space. But what are the elements of this space? The vir tue of
measurable functions is that they do suﬃce to represent all e lements of V .
It is this completeness that makes measurable functions as i mportant as
real numbers.
Duality . Given a Banach space X, we let X∗ denote the dual space of
bounded linear functionals φ :X → R, with the norm
‖φ‖= sup
x∈X−{0}
|φ(x)|
‖x‖ ·
There is a natural map X →X∗∗. If X =X∗∗ then X is reﬂexive .
Theorem 3.7 (Riesz-Fischer) Let 1/p + 1/q = 1 , with 1 < p,q < ∞.
Then Lp[a,b ]∗ =Lq[a,b ] and vice-versa; in particular, Lp is reﬂexive.
Proof. Supposep ⁄= ∞. Let φ :Lp[a,b ] → R be a bounded linear functional,
with |φ(f )| ≤ M ‖f ‖. Deﬁne
G(x) = φ(χ[a,x]).
Then for any collection of disjoint intervals ( ai,bi) with ∑ |ai −bi|<δ , we
have
∑
|G(ai) −G(bi)| =
∑
|φ(χ(ai,bi))| =φ
(∑
±χ(ai,bi)
)
≤ M
(∑
|ai −bi|
) 1/p
≤Mδ 1/p,
since φ(f ) ≤M ‖f ‖p. Thus G(x) is absolutely continuous, and thus there is
an integrable function g(x) = G′(x) ∈L1[a,b ] such that
φ(χI ) =
∫
I
G′(x)dx =
∫
χIg
for any interval I ⊂ [a,b ]. (For p = ∞, the indicator functions χ[a,x] do not
depend continuously on x, so this step fails!)
Next we check that φ(f ) = ⟨f,g ⟩for all f ∈L∞[a,b ]. Indeed, if |f | ≤ A
there are step functions fn → f with fn → f pointwise and |fn| ≤ A.
Then fn → f in Lp, so by continuity φ(fn) → φ(f ). On the other hand,
32

|fng| ≤ A|g|, and
∫
|g| < ∞, so by the dominated convergence theorem we
have ⟨fn,g ⟩ → ⟨f,g ⟩. Since φ(fn) = ⟨fn,g ⟩, we have φ(f ) = ⟨f,g ⟩.
Now letgn be the truncation of g to a function with |gn| ≤ n, and choose
the sign of gn and gα
n below so the products below are positive. Then:
∫
gq
n = ⟨gq−1
n ,g ⟩=φ(gq−1
n ) ≤M ‖gq−1
n ‖p
= M
(∫
|gn|(q−1)p
) 1/p
=M
(∫
|gn|q
) 1/p
,
since pq =p +q. Thus for every n we have
∫
|gn|q ≤M 1/(1−1/p) =Mq.
Taking the limit as n → ∞ and applying Fatou’s lemma or monotone con-
vergence, we have ‖g‖q ≤M .
Thus by H¨ older’s inequality,⟨f,g ⟩deﬁnes a continuous linear functional
on Lp[a,b ]. Since φ(f ) = ⟨f,g ⟩on the dense set of bounded functions, we
conclude that equality holds everywhere.
Finally, H¨ older’s inequality shows
⟨f,g ⟩ ≤ ‖f ‖p‖g‖q,
with equality for f =gq/p, so the dual norm on Lp[a,b ]∗ agrees with the Lq
norm, ‖g‖q.
On the other hand, ( L1)∗ =L∞ but (L∞)∗ ⁄=L1.
The ﬁrst assertion follows by a modiﬁcation of the proof abov e. For an
indication of the second, recall the analogous fact that we u sed an ultraﬁlter
to construct a bounded linear function L : ℓ∞ → R, extending the usual
function L(an) = lim an on c ⊂ ℓ∞. On the other hand, for any b ∈ ℓ1 we
can ﬁnd a ∈c such that L(a) = 1 but ⟨a,b ⟩is as small as we like (slide the
support of a oﬀ towards inﬁnity.) Thus L is a linear functional that is not
represented by any element of ℓ1.
A similar construction can be carried out extending the poin t evaluations
from C[a,b ] to L∞[a,b ].
4 Baire Category
Theorem 4.1 Let X be a complete metric space, and let Ui be a sequence
of dense open sets in X. Then ⋂ Ui is dense. In particular the intersection
is nonempty (so long as X is nonempty).
33

Proof. We will deﬁne a nested sequence of closed balls B0 ⊃ B1 ⊃ ... by
induction. Let B0 be arbitrary. Since Un is dense, it meets the interior of Bn;
chooseBn+1 to be any ball contained in Bn∩Un, with diamBn+1 ≤ 1/(n+1).
Then (if X ⁄= ∅), the centers of the balls Bn form a Cauchy sequence, so
they converge to a limit x ∈X. By construction, x ∈B0 ∩⋂ Ui. Since B0
was arbitrary, this shows ⋂ Ui is dense.
Category . A subset E of a topological space is nowhere dense if the
interior of E is empty. A space is of ﬁrst category if it is a countable union
of nowhere dense sets; otherwise it is of second category.
For example, Q is of ﬁrst category, but Z is not (since every point of Z
is open).
In a complete metric space, a countable union of nowhere dens e sets is
said to be meager; the complement of such a set is residual. A property is
generic if it holds outside a meager set.
Reformulations of Baire’s theorem. Let X be a nonempty complete
metric space, or locally compact space topological space.
X is of second category.
A countable intersection of dense Gδ’s in X is again a dense Gδ.
If X =⋃ Fi then intFi ⁄= ∅ for some i.
Measure and category . The sets of measure zero and the meager sets
in R both form σ-ideals (in the ring of all subsets of R). That is, they are
closed under taking subsets and countable unions.
Theorem 4.2 (Uniform boundedness) Let F be a collection of contin-
uous functions on a (nonempty) complete metric space X, such that for each
x the functions are bounded — i.e. supFf (x) ≤Mx. Then there is a open
set U ⁄= ∅ on which the functions are uniformly bounded: supUf (x) ≤ M
for all f ∈ F .
Proof. LetFn = {x : f (x) ≤n ∀f ∈ F }. Then Fn is closed and ⋃ Fn =X,
so some FM has nonempty interior U .
Diophantine approximation. A real number x is Diophantine of expo-
nent α if there is a C >0 such that
⏐
⏐
⏐
⏐x − p
q
⏐
⏐
⏐
⏐> C
qα
for all rational numbers p/q.
34

Theorem 4.3 If x is algebraic of degree d > 1, then it is Diophantine of
exponentd.
Proof. Let f (t) = a0td +...a d be an irreducible polynomial with integral
coeﬃcients satisﬁed by x. Then |f (p/q)| ≥ 1/qd. Since |f′| is bounded, say
byM , near x, we ﬁnd
q−d ≤ |f (x) −f (p/q)| ≤ M |x −p/q|
and thus |x −p/q| ≥ 1/(Mqd).
Roth has proved the deep theorem that any algebraic number is Dio-
phantine of exponent 2 + ǫ.
A number is Diophantine of exponent 2 iﬀ the coeﬃcients in its continued
fraction expansion are bounded. For quadratic numbers, the se coeﬃcients
are pre-periodic.
Liouville numbers. We say x is Liouville if x is irrational but for any
n> 0 there exists a rational number with |x −p/q|<q−n. Such a number
is not Diophantine for any exponent, so it must be transcende ntal.
For example, x =∑ 1/10n! is an explicit and easy example of a tran-
scendental number.
Theorem 4.4 (Measure vs. Category) A randomx ∈ [0, 1] is Diophan-
tine of exponent 2 +ǫ for all ǫ> 0. However a generic x ∈ [0, 1] is Liouville.
Proof. For the ﬁrst part, ﬁx ǫ> 0, and let
Eq = {x ∈ [0, 1] : ∃p, |x −p/q|< 1/q2+ǫ}.
Since there are only q choices for p, we ﬁnd m(Eq) = O(1/q1+ǫ), and thus∑ m(Eq)< ∞. Thus m(lim supEq) = 0 (by easy Borel-Cantelli). But this
means that for almost every x ∈ [0, 1], only ﬁnitely rationals approximate x
to within 1/q2+ǫ. Thus x is Diophantine of exponent 2+ǫ. Taking a sequence
ǫn → 0 we conclude that almost every x is Diophantine of exponent 2 + ǫ
for all ǫ> 0.
For the second part, just note that
En = {x ∈ [0, 1] : ∃p,q, |x −p/q|< 1/qn}
contains the rationals and is open. Thus ⋂ En = L is the set of Liouville
numbers, and by construction it is a dense Gδ.
35

Sets with no category .
Lemma 4.5 The set of closed subsets of R has the same cardinality as R
itself.
Lemma 4.6 A closed subset of R with no isolated points contains a Cantor
set.
Lemma 4.7 Every uncountable closed set E in R contains a Cantor set.
Proof. Consider the subset F ofx ∈E such thatF ∩B(x,r ) is uncountable
It is easy to see that F is a nonempty, closed set, without isolated points,
using the fact that countable unions preserve countable set s. Thus F con-
tains a Cantor set.
Corollary 4.8 Every uncountable closed set satisﬁes |F | = |R|.
Corollary 4.9 Every set of positive measure contains a Cantor set.
Proof. It contains a compact set of positive measure, which is neces sarily
uncountable.
By similar arguments, it is not hard to show:
Theorem 4.10 Every dense Gδ X ⊂ [a,b ] contains a Cantor set.
Theorem 4.11 There exists a set X ⊂ R such that X and X′ both meet
every uncountable closed set.
Proof. Use transﬁnite induction, choosing an isomorphism between R and
the smallest ordinal c with |c| = |R|.
Such an X is called a Bernstein set .
Corollary 4.12 IfX is a Bernstein set, then for any interval [a,b ], neither
X ∩ [a,b ] nor ~X ∩ [a,b ] has ﬁrst category.
Proof. IfX ∩ [a,b ] has ﬁrst category, then the complement of X contains a
Cantor set K, contradicting the fact that X meets K. The same reasoning
applies to ~X.
36

Thus X is an analogue, in the theory of category, of a non-measurabl e
set. (One can think of a set X that meets some open set in a set of second
category, as a set of positive measure).
Games and category . (Oxtoby, §6.) Let X ⊂ [0, 1] be a set. Players A
andB play the following game: they alternately choose intervals A1 ⊃B1 ⊃
A2 ⊃ B2 · · ·in [0, 1], then form the intersection Y =⋂ Ai =⋂ Bi. Player
A wins if Y meets X, otherwise player B wins.
Theorem 4.13 There is a winning strategy for B iﬀ X has ﬁrst category.
Proof. If X has ﬁrst category then it is contained in a countable union
of nowhere dense closed sets, ⋃ Fn. Player B simply chooses Bn so it is
disjoint from Fn, and then ⋂ Bn is disjoint from X.
Conversely, supposeB has a winning strategy. Then using this strategy,
we can ﬁnd a set of disjoint ‘ﬁrst moves’ Bi
1 that are dense in [0 , 1]. To
see this, let B1(A) be B’s move if A1 = A. Let J1,J 2,... be a list of the
intervals with rational endpoints in [0 , 1]. Inductively deﬁne B1
1 = B(J1)
and Bi+1
1 = B(Jk) for the ﬁrst k such that Jk is disjoint from B1
1,...,B i
1.
Then every Jk meets some Bi
1 so⋃ Bi
1 is dense.
Similarly, we can ﬁnd disjoint second moves that are dense in Bi
1 for each
i. Putting all these together, we obtain moves Bi
2, each contained in some
Bi
1, that are also dense in [0 , 1].
Continuing in this way, we obtain a sequence Bi
k such that Uk =⋃
iBi
k
is dense in [0 , 1]. Let Z =⋂ Uk. Any point x ∈Z is contained in a unique
nested sequence Bi1
1 ⊃Bi2
2 ⊃ · · ·obtained using B’s winning strategy. Thus
x ⁄∈X. This shows X is disjoint from the dense Gδ Z, and thus X has ﬁrst
category.
By the same reasoning we have:
Theorem 4.14 Player A has a winning strategy iﬀ there is an interval A1
such that I ∩A1 has second category.
Corollary 4.15 There exists a set X such that neither A nor B has a
winning strategy!
One might try to take X equal to a non-measurable set P ⊂ [0, 1) ∼
=
S1 = R/Z constructed so that Q +P =S1. By the Baire category theorem,
P does not have ﬁrst category, but it also does not have second c ategory,
since P ∩P + 1/2 = ∅.
37

However it might be the case that P ∩I is small (even empty!) for some
intervalI. To remedy this, one considers instead a Bernstein set , i.e. a set
X such that both X and its complement X′ meet every uncountable closed
subset of S1. Then, as we have seen above, X ∩ [a,b ] has neither ﬁrst nor
second category.
Poincar´ e recurrence.LetX be a ﬁnite measure space, and let T :X →X
be a measure-preserving automorphism. Then for any set A of positive
measure, there exists an n> 0 such that m(A ∩Tn(A))> 0.
Proof. Let E = T (A) ∪T 2(A) ∪... be the strict forward orbits of the
elements of A. Then, if A is disjoint from its forward orbit, we ﬁnd A andE
are disjoint sets and T (A∪E) = E. Thus m(A∪E) = m(E) = m(E)+m(A),
so m(A) = 0.
Recurrence and category . Now suppose X is also a compact metric
space, T : X → X is a measure-preserving homeomorphism, and every
nonempty open set has positive measure. We say x ∈X is recurrent if x is
an accumulation point of the sequence Tn(x),n> 0.
Theorem 4.16 The set of recurrent points is residual and of full measure.
Proof. If x is not a recurrent point, then there is a positive distance fr om
x to the closure of its forward orbit. That is, for some r> 0 we have
x ∈Er = {y : d(y,T n(y)) ≥r, ∀n> 0}.
Note that Er is closed, and hence compact. We claim m(Er) = 0. If
not, there is a ball such that A =B(x,r/ 2) ∩Er has positive measure. But
then A is disjoint from its forward orbit, contrary to Poincar´ e re currence.
ThusEr is a closed set of measure zero, and hence nowhere dense. Sinc e
the non-recurrent points are exactly the set ⋃
iE1/i, we see the recurrent
points are residual and of full measure.
The space of homeomorphisms. Let X be a compact metric space.
Let us make the space C(X,X ) of all continuous maps f : X → X into
a complete metric space by d(f,g ) = sup d(f (x),g (x)). What can we say
about the subset H(X) of homeomorphisms?
It is easy to see H([0, 1]) is already neither open nor closed. However it
does consist exactly of the bijective maps in C(X,X ). Now surjectivity is
a closed condition, and hence a Gδ-condition. What about injectivity? If f
38

is not injective, then there are two points at deﬁnite distan ce,x andy, that
are identiﬁed. Thus the non-injective maps are a union of clo sed sets,
⋃
n
{f : ∃x,y ∈X,d (x,y ) ≥ 1/n,f (x) = f (y)}.
(The closedness uses compactness of X). Putting these observations to-
gether we have:
Theorem 4.17 For any compact metric space X, the homeomorphisms
H(X) are a Gδ subset of the complete metric space C(X,X ).
The property of Baire. A topological space has the property of Baire if it
satisﬁes the conclusion of the category theorem: namely if any intersection
of dense Gδ’s is still dense.
Theorem 4.18 If X is complete and Y ⊂ X is a Gδ, then Y has the
property of Baire.
Proof. Apply the Baire category theorem to
Y , in which Y is a dense Gδ.
(Actually one can re-metrize Y so Y itself is a complete metric space.)
T ransitive maps of the square. Oxtoby and Ulam proved that a generic
measure-preserving automorphism of any manifold is ergodi c. We will prove
a weaker result that illustrates the method.
Theorem 4.19 There exists a homeomorphism of [0, 1] × [0, 1] with a dense
orbit.
Let X = [0, 1] × [0, 1]. Since H(X) has the property of Baire, it would
suﬃce to show that a generic homeomorphism has a dense orbit. But this
is not true! Once there is a disk such that f (D) ⊂D, any orbit that enters
D can never escape. And in fact any homeomorphism can be pertur bed
slightly so that fn(D) ⊂ D for some disk D. The category method has
failed!
Measure-preserving maps. What Oxtoby and Ulam proved is that the
problem can be solved by making it harder.
Theorem 4.20 A generic measure preserving homeomorphism of the square
has a dense orbit.
39

Proof. Let M (X) ⊂ H(X) be the measure-preserving homeomorphisms.
It also has the property of Baire, because it is a closed subse t of H(X).
Consider two balls, B1 andB2, and let U (B1,B 2) ⊂M (X) be the set of
f :X →X such that fn(B1) meets B2, for some n> 0. Clearly U (B1,B 2)
is open; we will show it is dense.
To this end, ﬁx r > 0, and consider any f ∈ M (X). Choose a chain
of points x0,...,x n with x0 ∈ B1, xn ∈ B2, and d(xi,xi+1) < r. Since a
generic point is recurrent, we can also assume each xi is recurrent. Then we
can also ﬁnd high iterates yi =Tni(xi) such that d(xi,yi)<r .
Now choose a short path Pi (of length less than 2 r) from yi to xi+1,
avoiding all other of the points we have considered; includi ng Tn(xi) for
0 ≤ n ≤ ni. Construct a measure-preserving map within distance r of the
identity, such that g(yi) = xi+1. This map g is supported close to ⋃ Pi.
Then g ◦f , under iteration, moves x0 to yn0−1, then to g(f (yn0−1)) =
g(yn0) = x1, and then x1 tox2), etc.; so that ultimately xn is in the forward
orbit of x0, and hence f movesB1 intoB2.
Using a countable base for X, we can now conclude that a generic f ∈
M (X) has the property that for any two nonempty open sets U,V ⊂ X,
there exists an n> 0 such that fn(U ) ∩V ⁄= ∅.
We claim any such f has a dense orbit. Indeed, consider for any open
ballB the set U (B) of x such that fn(x) ∈B for some n> 0. The set U (B)
is open, and it is dense by our assumption on f . Intersecting these U (B)
over a countable base for X, we ﬁnd a generic x ∈X has a dense orbit.
Open problem. Does a generic C 1 diﬀeomorphism of a surface have a
dense orbit? It is known that a suﬃciently smooth diﬀeomorph ism does not
(KAM theory).
For more discussion, see [Ox, §18] and [Me, Thm. 4.3].
5 Topology
T opological spaces. The collection of open sets T satisﬁes: X, ∅ ∈ T ;
and ﬁnite intersections and arbitrary unions of open sets ar e open. Metric
spaces give particular examples.
Compactness. A space is compact if every open cover has a ﬁnite sub-
cover. Equivalent, any collection of closed sets with the ﬁn ite intersection
property has a nonempty intersection.
Theorem 5.1 . A subset K ⊂ Rn is compact iﬀ K is closed and bounded.
40

Theorem 5.2 A metric space (X,d ) is compact iﬀ every sequence has a
convergent subsequence.
The ﬁrst result does not hold in general metric spaces: for ex ample,
the unit ball in ℓ∞(N) is closed and bounded but not compact. Similarly,
the sequence of functions fn(x) = xn is bounded in C[0, 1], but has no
convergent subsequence.
The second, we will also see, does not hold in general topolog ical spaces.
Nevertheless both results can be modiﬁed so they hold in a gen eral setting.
T otal boundedness. A metric space is totally bounded if for any r > 0,
there exists a covering of X by a ﬁnite number of r-balls. In Rn, bound-
edness and total boundedness are equivalent; but the latter notion is much
stronger in inﬁnite-dimensional spaces, and gives the corr ect generalization
of Theorem 5.1.
Theorem 5.3 A metric space (X,d ) is compact iﬀ X is complete and to-
tally bounded.
Arzela-Ascoli. Here is application of compactness to function spaces.
Let C(X) be the Banach space of continuous functions on a compact
metric space (X,d ). When does a set of functions F ⊂ C(X) have compact
closure? That is, when can we assure that every sequence fn ∈ F has a
convergent subsequence (whose limit may or may not lie in F)?
Recall that C(X) is complete, and that a metric space is compact iﬀ it
is complete and totally bounded. The latter property means t hat for any
r> 0 there is a ﬁnite covering of X byr-balls.
The set F is equicontinuous if all the functions satisfy the same modulus
of continuity: that is, if there is a function m(s) → 0 as s → 0 such that
d(x,y ) < s implies |f (x) −f (y)| < m(s) for all f ∈ F . Of course F is
bounded iﬀ there is an M such that |f (x)| ≤ M for all f ∈ F .
Theorem 5.4 F ⊂ C(X) has compact closure iﬀ F is bounded and equicon-
tinuous.
Proof. First suppose
F is compact. Then clearly F is bounded. Now take
anyǫ> 0, and cover F by a ﬁnite collection of balls B(fi,ǫ/ 3). Since X is
compact, each fi is uniformly continuous, so there is a δ such that
d(x,y )<δ =⇒ ∀ i, |fi(x) −fi(y)|<ǫ/ 3.
41

Then for any f ∈ F , we can ﬁnd fi with d(f,fi) < ǫ/3, and conclude that
|f (x) −f (y)|<ǫ when d(x,y )<δ . Thus F is equicontinuous.
Now suppose F is bounded by M , and equicontinuous. To show F is
compact, we need only show F is totally bounded. To this end, ﬁx r> 0, and
by equicontinuity choose δ >0 such that d(x,y )<δ =⇒ | f (x) −f (y)|<r .
By compactness of X, we can ﬁnd a ﬁnite set E ⊂X such thatB(E,δ ) = X.
Similarly we can pick a ﬁnite set F ⊂ [−M,M ] that comes within r of every
point.
For each map g :E →F , let
B(g) = {f ∈ F : sup
E
|g −f |<r }.
Since there are only ﬁnitely many maps g, and every f is close to some g,
these sets give a ﬁnite cover F. Finally if f1,f 2 ∈B(g), then for any x ∈X,
there is an e ∈E withinδ of x. We then have
|f1(x) −f2(x)| ≤ 2r + |f1(e) −f2(e)| ≤ 4r,
so diam B(g) ≤ 4r. It follows that F is totally bounded, and thus F is
compact.
Example: Normal families. Let F be the set of all analytic functions on
an open set Ω ⊂ C with |f (z)| ≤ M . Then F is compact in the topology of
uniform convergence on compact sets.
Note: The functions fn(z) = zn do not converge uniformly on the whole
disk, so the restriction to compacta is necessary.
Proof. By Cauchy’s theorem, if d(z,∂ Ω) >r , then
|f′(z)| =
⏐
⏐
⏐
⏐
⏐
1
2πi
∫
S1(p,r)
f (ζ)dζ
(ζ −z)2
⏐
⏐
⏐
⏐
⏐ ≤ 2πrM
2πr2 = M
r ·
Thus we can pass to a subsequence converging uniformly on the compact
set Kr = {z ∈ Ω : d(z,∂ Ω) ≥ r}. Diagonalizing, we get a subsequence
converging uniformly on compact sets. Analyticity is prese rved in the limit,
so F is a normal family.
Metrizability , T opology and Separation. Our next goal is to formu-
late purely topological versions of the best properties of m etric spaces. This
properties will help us recognize when a topological space ( X, T ) is metriz-
able, i.e. when there is a metric d that determines the topology T .
42

Given any collection C of subsets of X, there is always a weakest topology
T containing that collection. We say C generates T .
A base B for a topology is a collection of open sets such that for each
x ∈ U ∈ T , there is a B ∈ B with x ∈ B ⊂ U . Then U is the union of
all the B it contains, so B generates T . Indeed T is just the union of the
empty set and all unions of subsets of B.
If B is given, it is a base for some topology iﬀ for any x ∈B1,B 2 there
is a B3 with x ∈B3 ⊂B1 ∩B2.
A sub-base B for a topology T is a collection of open sets such that for
anyx ∈U ∈ T , we have x ∈B1 ∩ · · ·Bn ⊂U for some B1,...,B n ∈ B . Any
sub-base also generates T . Conversely, any collection of set B covering X
forms a sub-base for the topology T it generates.
Example: In Rn, the open half-spaces H =φ−1(a, ∞) for linear functions
φ : Rn → R form a sub-base for the topology. (By intersecting them we ca n
make small cubes).
A base at x is a collection of open sets Bx, all containing x, such that for
any open U with x ∈U , there is a B ∈ Bx with x ∈B ⊂U .
Example: in any metric space, the balls B(x, 1/n) form a base at x.
Countability axioms. A topological space X is:
• ﬁrst countable if every point has a countable base;
• second countable if there is a countable (sub-)base for the whole space;
and
• separable if there is a countable dense set S ⊂X.
Clearly a second countable space is separable: just choice o ne point from
each open set.
Examples. Clearly any metric space is ﬁrst countable.
A Euclidean spaces Rn are ﬁrst and second countable, and separable.
The space ℓ∞(N) is not separable or second countable. The uncountable
collection of balls B(χA, 1/2), as A ranges over all subsets of N, are disjoint.
On the other hand, ℓp(N) is separable for 1 ≤p< ∞.
Theorem 5.5 Any separable metric space is second countable.
Proof. Let (xi) be a countable dense set of let B = {B(xi, 1/n)}. Then if
x ∈U , we have x ∈B(x,r ) ⊂U , and hence x ∈B(xi, 1/n) ⊂U as soon as
d(xi,x )< 1/n and 2/n<r .
43

Theorem 5.6 The number of open (or closed) sets in a separable metric
space (like Rn) is at most |R|.
Proof. |T | ≤ |P (B)| ≤ |P (N)| = |R|.
Corollary 5.7 There are more subsets of R than there are closed subsets.
Question. Does ﬁrst countable and separable imply second co untable?
No!
Example. The half-open interval topology. Let
B = {[a,b ) : a<b };
this is a base for a topology T on R. In this topology, xn → y iﬀ xn
approachesy from above. Thus every strictly increasing sequence diverg es.
This space is ﬁrst countable and separable. (The rationals a re dense.)
But it is not second countable! If a ∈ B ⊂ [a,b ), then a must be the
minimum of B. Thus for any base B, the map B ↦→infB sends B onto R,
and therefore |B| ≥ | R|.
Cor: ( R, T ) is not metrizable.
This space is sometimes denoted Rℓ; for an extended discussion, see
Munkres, Topology.
The Lindel¨ of condition. A topological space is said to be Lindel¨ ofif
every open cover has a countable subcover. A second countable space is
Lindel¨ of. The space Rℓ above is also Lindel¨ of, but not second countable. It
is interesting to note that the Sorgenfrey (carefree?) plan e, Rℓ × Rℓ is not
Lindel¨ of (cf. Munkres, Topology, p. 193).
Separation axioms T i. (T for Tychonoﬀ). Let us say disjoint subsets E,
F of a topological space X can be separated if they lie in disjoint open sets.
The separation axioms (or properties) are:
T1 (Tychonoﬀ): Points are closed.
T2 (Hausdorﬀ): Pairs of points x,y are separated.
T3 (regular): Points are separated from closed sets, and point s
are closed.
T4 (normal): Pairs of closed sets are separated, and points are
closed.
44

Example: any metric space is normal. Given two closed sets A and B,
they are separated by the open sets U = {x : d(x,A ) < d(x,B )} and
V = {x : d(x,B )<d (x,A )}.
Zariski topology . Let k be a ﬁeld. A natural example of a topology that
is not Hausdorﬀ is the Zariski topology on kn. In this topology, a set is F
closed if it is deﬁned by system of polynomial equations: F is the zero set
of a collection of polynomials fα ∈k[x1,...x n].
A base for the topology consists of complements of hypersurf aces,Uf =
kn −Z(f ). Note that Uf ∩Ug =Ufg , so we indeed have a base.
By the Noetherian property, the ideal ( fα) is ﬁnitely generated, so only
a ﬁnite number of polynomials are actually necessary to deﬁn eF . Geomet-
rically, this means any decreasing sequence of closed sets, F1 ⊃F2 ⊃F3... ,
eventually stabilizes. In particular, R2 is compact .
On R, the Zariski topology is the coﬁnite topology. On Rn, any two
nonempty open sets meet; i.e. Rn cannot be covered by a ﬁnite number of
hypersurfaces. Thus the Zariski topology is T 1 but not T 2.
The spectrum of a ring. Given a ring A, one also deﬁnes the Zariski
topology on the set Spec A of all prime ideals p ⊂ A, by taking the closed
sets to have the form V (a) = {p : p ⊃a}, where a ranges over all ideals in
A. A point p ∈ SpecA is closed iﬀ p is a maximal ideal.
Thus SpecA is usually not even Hausdorﬀ. In fact, for any ring A, the
‘generic point’ p coming from the ideal (0) is dense; its closure is the whole
space.
Theorem 5.8 A compact Hausdorﬀ space X is normal.
Proof. We ﬁrst show X is regular. Let p be a point outside a closed set
F . Then for each x ∈ F there are disjoint open sets x ∈ Ux and p ∈ Vx.
Passing to a ﬁnite subcover of F , we have F ⊂⋃ n
1Ui and p ∈⋂ n
1Vi.
Now to prove normality, suppose E andF are disjoint closed sets. Then
for each x ∈ E, there is are disjoint open sets with x ∈ Ux and F ⊂ Vx.
Passing to a ﬁnite subcover, we have E ⊂⋃ n
1Ui andF ⊂⋂ n
1Vi.
Theorem 5.9 (Urysohn’s Lemma) LetA,B be disjoint closed subsets of
a normal space X. Then there exists a continuous function f : X → [0, 1]
such that f (A) = 0 and f (B) = 1 .
Proof. Let U0 = A and let U1 = X. The closed set A is a subset of the
open set ~B. By normality, there exists an open set U1/2 with A ⊂ U1/2 ⊂
45

U1/2 ⊂ ~B. Iterating this construction, we obtain a family of open set s Ur
indexed by the dyadic rationals in [0 , 1] such that Ur ⊂ Ur ⊂Us whenever
r <s. Now let f (x) = inf {r : x ∈Ur}. Then {x : f (x)<s } =⋃
r<sUr is
open, and {x : f (x) ≤s} =⋂
r>sUr is closed, so f is continuous.
Corollary 5.10 In a normal space, there are suﬃciently many functions
f :X → R to generate the topology on X.
Proof. We must show that every closed set A is the intersection of level
sets of functions. But for any p ⁄∈A we can ﬁnd a function with f (A) = 0,
f (p) = 1, and so we are done.
Theorem 5.11 (Tietze Extension) IfX is normal and A ⊂X is closed,
then every continuous function f :A → R extends to a continuous function
on X.
Actually Tietze generalizes Urysohn, since the obvious fun ction f :A ⊔
B → {0, 1} is continuous and A ⊔B is closed.
Approximating sets by submanifolds. For any compact set X ⊂ Rn,
andr> 0, there exists a smooth compact submanifold lying within B(X,r )
and separating X from ∞.
Proof. Smooth the function given by Tietze and apply Sard’s theorem .
Cor. Any compact set in R2 can be surrounded by a ﬁnite number of
smooth loops. Any Cantor set in R3 can be surrounded by smooth closed
surfaces; but their genus may tend to inﬁnity! (Antoine’s ne cklace).
W eak topology . Given a collection of functions F on a set X, we can
consider the weakest topology which makes all f ∈ F continuous. A base
for this topology is given by the sets of the form
f−1
1 (α1,β 1) ∩f−1
2 (α2,β 2) ∩...f −1
n (αn,βn),
where fi ∈ F . We have xn →x iﬀ f (xn) →f (x) for all f ∈ F .
The weak topology on a Banach space X is the weakest topology making
all φ ∈X∗ continuous. For example, fn →f weakly in L1 iﬀ
∫
fng →
∫
fg
46

for all g ∈ L∞. This topology is weaker than norm convergence; e.g. the
functions fn(x) = sin(nx) converge weakly to zero in L1[0, 1], but they do
not convergence at all in the norm topology.
Products. Given any collection of topological spaces {Xα}, the product
X = ∏ Xα can be endowed with the Tychonoﬀ topology, deﬁned by the
sub-basic sets B(U,α ) = {x ∈X : xα ∈U } where U ⊂Xα is open.
This is the weakest topology such that all the projections fα :X →Xα
are continuous.
Example: For any set A, RA is the set of all functions f : A → R,
and fn → f in the Tychonoﬀ topology iﬀ fn(a) → f (a) for all a ∈ A.
So the Tychonoﬀ topology is sometimes called the topology of pointwise
convergence.
Example: In X = (Z/2)A ∼
= P(A), we have An →A iﬀ ( x ∈A iﬀ x ∈An
for all n ≫ 0).
Theorem 5.12 If Xi is metrizable for i = 1, 2, 3,... , then so is ∏ ∞
1 Xi.
Proof. Replacing the metric di by min(di, 1), we can assume each Xi has
diameter at most 1. Then d(x,y ) =∑ 2−id(xi,yi) metrizes ∏ Xi.
For example, RN is metrizable.
Theorem 5.13 (Urysohn metrization theorem) A second countable topo-
logical spaceX is metrizable iﬀ X is normal.
Proof. Clearly a metric space is normal. For the converse, let ( Bi) be a
countable base for X. For each pair with Bi ⊂ Bj, construct a continuous
function fij :X → [0, 1] with fij = 0 on Bi and fij = 1 outside Bj. Let F
be the collection of all such functions, and consider the nat ural continuous
map f : X → [0, 1]F , sending x to (fij(x)). Since F is countable, f (X) is
metrizable; we need only show that the inverse map f (X) → X is deﬁned
and continuous.
To see the map f (X) →X is deﬁned, we must show f is injective. But
given any points x ⁄= y, we can ﬁnd open sets with x ∈ Bi ⊂ Bj and y
outside Bj; then fij separates x from y.
To see f (X) →X is continuous, we just need to show that the weakest
topology T′ making all the functions fij continuous is the original topology
T on X. But if x ∈ U ∈ T , then there are basis elements with x ∈ Bi ⊂
Bj ⊂U . Then V =f−1
ij [0, 1/2) is in T′, and we have x ∈Bi ⊂V ⊂Bj ⊂U .
Since this holds for every x ∈U , we conclude that U ∈ T′ and thus T = T′.
47

Regularity v. Normality . Tychonoﬀ observed that Urysohn’s metriza-
tion theorem also applies to regular spaces, since we have:
Theorem 5.14 A regular space with a countable base is normal.
Proof. LetA, B be disjoint closed sets in such a space. Then A is covered
by a countable collection of open sets Ui whose closures are disjoint from
B. There is a similar cover Vi ofB by open sets whose closures are disjoint
from A. Now set U′
i =Ui − (
V 1 ∪ · · ·Vi), set V′
i =Vi − (U 1 ∪ · · ·Ui), and
observe that U =⋃ U′
i and V =⋃ V′
i are disjoint open sets containing A
and B.
A non-metrizable product. Example: ( Z/2)R ∼
= P(R) is not metrizable
because it is not ﬁrst countable.
A base at the set R consists of the open sets U (F ), deﬁned for each ﬁnite
set F ⊂ R as
U (F ) = {A ⊂ R : F ⊂A}.
Let F be the set of ﬁnite subset A ⊂ R. Then F meets every U (F )
so R ∈
F . But there is no sequence An ∈ F such that An → R! Indeed,
if An ∈ F is given then we can pick x ⁄∈⋃ An, and An never enters the
neighborhood U ({x}) of R.
We will later see that that P(R) is compact. But it has sequences with
no convergent subsequences! To see this, let An be the set of real numbers
x = 0.x1x2x3... such that xn = 1. Given any subsequence nk, we can
ﬁnd an x such that xnk alternates between 1 and 2 as n → ∞ . Suppose
Ank →B. If x ∈B then x ∈Ank for all k ≫ 0, and if x ⁄∈B then x ⁄∈Ank
for all k ≫ 0. Either way we have a contradiction.
Nets. A directed system A is a partially ordered set so any two α,β ∈ A
are dominated by some γ ∈A: γ ≥α and γ ≥β.
A net xα is a map x :A →X from a directed system into a topological
space X.
Example: N is a directed system, and a sequence xn is a net.
Convergence. We say xα →x ∈X iﬀ for any neighborhood U of x there
is an α such that xβ ∈U for all β >α.
Theorem 5.15 In any topological space, x ∈ E iﬀ there is a net xα ∈ E
converging to x.
48

Proof. Let α =α(U ) range over the directed set of neighborhoods of x in
X, and for each U let xα be an element of U ∩E. Then xα →x.
Conversely, ifxα ∈E converges tox, then every neighborhood of x meets
E, so x ∈E.
Subnets. If B is also a directed system, a map f :B →A is coﬁnal if for
anyα0 ∈A there is a β0 ∈B such that f (β) ≥α0 wheneverβ ≥β0. Then
yβ =xf (β) is a subnet of xα.
Example: A function f : N → N is coﬁnal iﬀ f (n) → ∞. So subsequences
are special cases of subnets.
Theorem 5.16 X is compact iﬀ every net has a convergent subnet.
Proof. Let F be a collection of closed sets with the ﬁnite intersection
property, and let α be the directed system of ﬁnite subsets of F, and let xα
be a point lying in their common intersection. Then the limit point y of a
convergent subset of xα will lie in every element of F, so ⋂ F ⁄= ∅.
Conversely, let xα be a net in a compact space X. For every α let
Fα = {xβ : β ≥α}.
Since the index set is directed, any ﬁnite set of indices has a n upper bound,
and thus the
Fα have the ﬁnite intersection property. Therefore there is a y
in⋂ Fα.
Now let B be a base at Y ordered by inclusion, and let C =A ×B with
the product ordering. (This means ( a,b ) < (a′,b′) iﬀ a < a′ and b < b′.)
Then the projection A ×B →A is coﬁnal.
For every pair γ = (α,β (U )) there is an element yγ = xf (γ) ∈ U ∩Fα.
Then yγ is a subnet converging to y.
Theorem 5.17 (Tychonoﬀ ) A product X = ∏
NXn of compact sets is
compact. (Here N is an arbitrary index set).
Proof. By the Axiom of Choice we may assume the index set is an ordinal
N = {0, 1, 2,... }. Given a net xα ∈X, we will produce a convergent subnet
yα, by transﬁnite induction over N . In the process we will deﬁne nets xn for
eachn ∈N , with xn a subnet of xi fori<n , and with each coordinate xn(i)
converging for i < n. We will have fij : Ai → Aj denote the re-indexing
function for i ≥j.
49

Let y0 =x. Passing to a subnet, we obtain a net x0
α indexed by α ∈A0
and with x0
α(0) converging in X0.
Givenn ∈N +1, let Bn = ⊔i<nAi, and let yn(α) = xi
α forα ∈Ai. Order
An byα ≤β if α and β belong to Ai and Aj with i ≤j, and if fji(β) ≥α.
Finally to make yn a subnet of xi, let gnj(α) = fij(α) if α ∈Ai, i ≥j, and
specify gnj(α) ∈Aj arbitrarily if α ∈Ai for i<j .
(Check that this is a subnet: given α0 ∈Ai, if β ≥α0, then β ∈Aj for
some j ≥i, and by deﬁnition of the ordering on Bn we have fji(β) ≥α0, so
gni(β) ≥α0.)
Since yn is a subnet of xi, the net yn
α(i) converges for all indices i < n.
Let (xn,An) be a subnet of ( yn,Bn) that converges in position n.
By induction we obtain, for the ordinal N + 1, a subnet yα =yN +1
α that
converges in all coordinates. This means yα converges in X.
Axiom of Choice. The use of the Axiom of Choice in the preceding
proof cannot be dispensed with, in the strong sense that Tych onoﬀ’s the-
orem implies the Axiom of Choice. Note that this is stronger than the
commonly-heard statement ‘you need the Axiom of Choice to co nstruct a
non-measurable set’.
Partitions of unity .
Theorem 5.18 LetX be a compact Hausdorﬀ space, and let U be an open
cover of X. Then there is a ﬁnite subcover Ui and functions 0 ≤fi(x) ≤ 1
supported on Ui such that ∑ n
1fi(x) = 1 .
Proof. For each x ∈ X there is an open set U ∈ U and a continuous
function f ≥ 0 supported in U , such that f (x) = 1. By compactness there
is a ﬁnite set of such functions such that the open sets {x : fi(x)> 0} cover
X. Then g(x) = ∑ fi(x) > 0 at every point; replacing fi(x) by fi(x)/g(x)
gives the desired result.
Lebesgue number. Corollary. Given an open covering U of a compact
metric space X, there is an r > 0 such that for every x ∈ X, there is a
U ∈ U withB(x,r ) ⊂U . The number r is called the Lebesgue number of U.
Proof. Construct a partition of unity subordinate to U1,...,U n ∈ U ; then
for every x there is an i such that fi(x) ≥ 1/n, and by uniform continuity
of the functions fi there is an r > 0 such that fi(x) > 0 on B(x,r ); then
B(x,r ) ⊂ {fi> 0} ⊂ Ui ∈ U .
50

Local constructions.
Theorem 5.19 Any compact manifold X admits a metric.
Proof. Take a ﬁnite collection of charts φ : Ui → Rn, a partition of unity
fi subordinate to Ui, and let g(v) =∑ fi|Dφi(v)|2.
Maximal ideals in C(X).
Theorem 5.20 Let X be a compact Hausdorﬀ space; then the maximal
ideals in the algebra C(X) correspond to the point evaluations.
Proof. Let I ⊂C(X) be a (proper) ideal. Suppose for all x ∈C(X), I is
not contained in the maximal ideal Mx of functions vanishing at x. Then
we can ﬁnd for each x a function f ∈I not vanishing on a neighborhood of
x. By compactness, we obtain g =f 2
1 + · · ·+f 2
n vanishing nowhere. Then
(1/g)g ∈I so I =C(X), contradiction. So I is contained an some Mx.
Spectrum. Given an algebra A over R, let
σ(f ) = {λ ∈ R : λ +f has no inverse in A}.
Then for A = C(X), we have σ(f ) = f (X), and thus we can reconstruct
‖f ‖∞ from the algebraic structure on A.
Also for A = C(X) we can let Y be the set of multiplicative linear
functionals, and embed Y into RA by sending φ to the sequence ( φ(f ) :
f ∈ A). Then in fact φ(f ) ∈ [−‖f ‖, ‖f ‖], so Y is compact, and Y is
homeomorphic to X.
Local compactness. A topological space X is locally compact if the
open sets U such that U is compact form a base for the topology.
For example, Rn is locally compact.
Alexandroﬀ compactiﬁcation. Let X be a locally compact Hausdorﬀ
space, and let X∗ = X ∪ {∞}, and deﬁne a neighborhood base at inﬁnity
by taking the complements X∗ −K of all compact sets K ⊂X.
Theorem 5.21 X∗ is a compact Hausdorﬀ space, and the inclusion of X
into X∗ is a homeomorphism.
Proof. Compact: if you cover X∗, once you’ve covered the point at inﬁnity,
only a compact set is left. Hausdorﬀ: because of local compac tness, every
x ∈X is contained in a U such that U is compact, and hence V =X∗ −U
is a disjoint neighborhood of inﬁnity.
51

This space is called the one-point compactiﬁcation of X.
Examples: N∗; Sn = (Rn)∗.
Proper maps. A useful counterpart to local compactness is the notion of
a proper map. A map f :X →Y is proper iff−1(K) is compact whenever
K is compact. Intuitively, if xα leaves compact sets in X, then f (xα) leaves
compact sets in f (X). Thus xα → ∞ impliesf (xα) → ∞, and so f extends
to a continuous map from X∗ to Y∗. This shows:
Theorem 5.22 A continuous bijection between locally compact Hausdorﬀ
spaces is a homeomorphism iﬀ it is proper.
Example: There is a bijective continuous map f : R →S1 ∪ [1, ∞) ⊂ C.
The Stone- ˇCech compactiﬁcation.
Theorem 5.23 LetX be a normal space. Then there is a unique compact
Hausdorﬀ space β(X) such that:
1. X is dense in β(X);
2. Every bounded continuous f :X → R extends to a continuous function
on β(X);
3. If X is compactiﬁed by another Hausdorﬀ space Y , in the sense that
the inclusion X ⊂Y is dense, then β(X) is bigger than Y : there is a
continuous map φ :β(X) →Y .
Proof. Let F be the family of all continuousf : X → [0, 1], let Z be the
compact product [0 , 1]F , and let β(X) ⊂ Z be the closure of X under the
embedding x ↦→(xf ) where xf = f (x). The ﬁrst two properties are now
evident.
Finally letY be another compactiﬁcation of X, and let G be the family of
all continuous maps g :Y → [0, 1]. Then there is an embedding Y ⊂ [0, 1]G ,
and the inclusion G ⊂ F gives a natural projection map [0 , 1]F → [0, 1]G .
This projection sends β(X) into Y .
Example: X = β(N). In this space, a sequence xn ∈ N converges iﬀ it
is eventually constant. Thus X is compact but the sequence xn = n has
no convergent subsequence! (However it does have convergen t subnets; for
such a net, f (nα) converges for every f ∈ℓ∞(N)!)
Stone- ˇCech and dual spaces. Another way to look at β(N) is that each
n ∈ N provides a mapn :ℓ∞(N) → R bya ↦→an, and thatβ(N) is the closure
52

of these maps. Note that the maps in the closure are bounded, linear
functionals . A typical example is provided by the ultraﬁlter limit we
constructed before. In general the closure consists of thos e ﬁnitely-additive
measures on N such that µ (N) = 1 and µ (E) = 0 or 1 for all E ⊂ N.
Theorem 5.24 (Stone-W eierstrass) LetX be a compact Hausdorﬀ space,
and let A ⊂C(X) be a subalgebra that contains the constants and separates
points. Then A is dense in C(X).
Examples: in C[0, 1], the functions of bounded variation, or Lipschitz,
orCk, or H¨ older continuous, or polynomials, or those that are re al-analytic,
all form subalgebras that separate points and contain the co nstant.
Lemma. The closure of A is a lattice.
Proof. We must show that f,g ∈ A =⇒ f ∨g ∈ A, where ( f ∨g)(x) =
max(f (x),g (x)). Note that f ∨g is the average of f +g and |f −g|. So
it suﬃces to show f ∈ A =⇒ | f | ∈ A. Now if ǫ < f <1, then √f =√
1 − (1 −f ) ∈A, because √1 −x =∑ anxn can be expanded in a power
series convergent in B(0, 1), and hence uniformly convergent in B(0, 1 −ǫ).
Then
|f | = lim
ǫ→0
√
f 2 +ǫ,
so |f | is in A, and hence f ∨g is in A.
Proof of Stone-Weierstrass. As above we replace A by its closure; then
A is an algebra as well as a lattice.
Given g ∈C(X), let F = {f ∈A : f ≥g}. To show g ∈A, it suﬃces
to show for each x that g(x) = infFf (x). Indeed, if that is the case, then
for any ǫ > 0 and x ∈ X, there is a neighborhood U of x and an f ∈ F
such that g ≤f ≤g +ǫ on U . Taking a ﬁnite sub-cover, we obtain a ﬁnite
number of functions such that g ≤f1 ∧ · · · ∧fn ≤g +ǫ on all of X. Since
A is a lattice, we are done.
It remains to construct, for ǫ >0 and x ∈X, and function f ∈A such
thatf ≥g andg(x) ≤f (x) ≤g(x) +ǫ. By replacing g withag +b, we may
assume g(x) = 0 and sup |g| ≤ 1.
Pick a neighborhood U of x on which |g|<ǫ . Since A separates points,
for each y ⁄∈U there is a function h ∈ A with h(x) = 0, h(y) = 2. Taking
a ﬁnite subcover of X −U by balls on which h >1, we obtain a function
f =h2
1 + · · ·+h2
n +ǫ with f (x) = ǫ =g(x) +ǫ, with f ≥ǫ > gon U , and
withf ≥ 1>g onX −U . Then f ∈ F , and so g(x) = infFf (x) as desired.
53

Paracompactness. For local constructions like making a metric, what’s
needed is not so much compactness (ﬁniteness of coverings) a s paracom-
pactness (local ﬁniteness). This says that any open coverin g has a locally
ﬁnite reﬁnement . Using this property one can show, for example, that any
paracompact manifold admits a metric.
All metric spaces are paracompact (a hard theorem). However there
exists a manifold which is not paracompact, namely the long line . It is ob-
tained from the ﬁrst uncountable ordinal Ω by inserting an in terval between
any two adjacent points, and introducing the order topology .
This space X has the amazing property that every sequence has a
convergent subsequence. Indeed, since a sequence is countable, it is
bounded above by some countable ordinal α, and (by induction) the segment
[0,α ] is homeomorphic to [0 , 1], hence compact.
On the other hand, X is not compact, since the open covering by all
intervals of the form [0,α ) has no ﬁnite subcover. Thus X is not metrizable.
Therefore X is not paracompact.
6 Banach Spaces
The theory of Banach spaces is a combination of inﬁnite-dime nsional linear
algebra and general topology. The main themes are duality, convexity and
completeness.
The ﬁrst two themes lead into the Hahn-Banach theorem, separ ation the-
orems for convex sets, weak topologies, Alaoglu’s theorem, and the Krein-
Milman theorem on extreme points. The third theme leads to th e ‘3 prin-
ciples of functional analysis’, namely the open mapping the orem, the closed
graph theorem and the uniform boundedness principle. These three results
all rest on the Baire category theorem and hence make crucial use of com-
pleteness.
Continuous linear maps. Let φ : X → Y be a linear map between
Banach spaces. The norm of φ, denoted ‖φ‖, is deﬁned as the least M such
that
‖φ(x)‖ ≤M ‖x‖
for all x ∈ X. Note: if Y = R we use the usual absolute value on R as a
norm.
A linear map is bounded if its norm is ﬁnite.
Theorem 6.1 A linear map is bounded iﬀ it is continuous.
54

Proof. Clearly boundedness implies (Lipschitz) continuity. Conv ersely, if
φ is continuous, then φ−1B(0, 1) contains B(0,r ) for some r >0 and then
‖φ‖ ≤ 1/r.
Theorem 6.2 (Hahn-Banach) Letφ :S → R be a linear map deﬁned on
a subspace S ⊂X in a Banach space such that |φ(x)| ≤ M ‖x‖ for all x ∈S.
Thenφ can be extended to a linear map on all of X with the same inequality
holding.
Proof. Using Zorn’s lemma, we just need to show that any maximal such
extension ofφ is deﬁned on all of X. So it suﬃces to consider the case S ⁄=X
and show that φ can be extended to the span of S andy where y ∈X −S.
We may assume M = 1. The extension will be determined by its value
φ(y) = z, and the extension will continue to be bounded by M = 1 so long
as we can insure that z is chosen so for all s ∈S we have:
−‖y +s‖ ≤φ(y +s) = z +φ(s) ≤ ‖y +s‖.
To show such a z exists amounts to showing that for any s,s′ ∈S we have
−φ(s) − ‖y +s‖ ≤ −φ(s′) + ‖y +s′‖,
so that there is a number z between the sup and inf. Now this inequality is
equivalent to:
φ(s′) −φ(s) ≤ ‖y +s‖+ ‖y +s′‖,
and this one is in fact true, since
φ(s′ −s) ≤ ‖s′ +y −y −s‖ ≤ ‖s +y‖+ ‖s′ +y‖.
Linear functionals on L∞ [0, 1]. We can now show more rigorously that
L1[0, 1] is not reﬂexive: namely take point evaluation on C[0, 1], and extend
it by Hahn-Banach to a linear functional φ on L∞[0, 1]. It is clear then
φ|C[0, 1] is not given by an element in L1[0, 1].
Embedding into X ∗∗ .
Theorem 6.3 For any x ∈ X there is a φ ∈ X∗ such that ‖φ‖ = 1 and
φ(x) = ‖x‖.
Proof. Deﬁne φ ﬁrst on the line through x, then extend it by Hahn-Banach.
55

Corollary 6.4 The embedding of X into X∗∗ is isometric.
Lp examples. Let f ∈ Lp(R) with ‖f ‖p = 1 and 1 < p < ∞, there
is a unique φ of norm 1 in the dual space such that φ(f ) = 1: namely
φ = sign(f )|f |p/q, which satisﬁes
φ(f ) =
∫
fφ =
∫
|f |p = 1.
This reﬂects the ‘smoothness’ of the unit ball in Lp: there is a unique sup-
porting hyperplane at each point.
ForL1 things are diﬀerent: for example, if supp f = [0, 1] there is a huge
space of φ ∈L∞ such that ‖φ‖∞ = 1 and φ(f ) = 1.
Non-example: L∞ . Now let f (x) = x in L∞[0, 1], and suppose φ ∈
L1[0, 1] has norm 1. Choose a< 1 such that t =
∫ a
0 |φ|> 0. Then we have:
φ(f ) ≤
∫ a
0
x|φ| +
∫ 1
a
|φ| ≤ at + (1 −t) = 1 − (1 −a)t< 1.
Thusφ(f ) can never be 1! This reﬂects of course the fact that X =L1[0, 1]
is a proper subset of its double dual X∗∗ =L∞[0, 1]∗.
More non-reﬂexive spaces. For the littleℓp spaces we have the following,
rather rich non-reﬂexive example:
c∗
0 =ℓ1, (ℓ1)∗ =ℓ∞, (ℓ∞)∗ =m(Z).
It turns out the last space can be identiﬁed with the space of ﬁ nitely-additive
measures on Z.
W eak closure. The Hahn-Banach theorem implies:
Theorem 6.5 LetS ⊂X be a linear subspace of a Banach space. Then S
is weakly closed iﬀ S is norm-closed.
Proof. Any weakly closed space is norm closed. Conversely, if S is norm
closed, for any y ⁄∈S we can ﬁnd a linear functional φ :X → R that vanishes
on S and sends y to 1, so y is not in the weak closure of S.
56

(More generally, as we will see later, any norm-closed conve x set is weakly
closed.)
The weak* topology . We say φα → φ in the weak* topology on X∗ if
φα(x) →φ(x) for every x ∈X.
Example: weak closures of continuous functions. The space C[0, 1]
is dense in L∞[0, 1] in the weak* topology. Indeed, if g ∈ L∞ then there
are continuous fn → g pointwise a.e. with ‖fn‖∞ ≤ ‖g‖∞. Now for any
h ∈L1[0, 1] the dominated convergence theorem implies
⟨h,fn⟩=
∫
hfn →
∫
hg = ⟨h,g ⟩.
On the other hand, C[0, 1] is already closed in the weak topology, since
it is norm closed.
Theorem 6.6 (Alaoglu) The unit ball B∗ ⊂X∗ is compact in the weak*
topology.
Proof. LetB be the unit ball in X. Then there is a tautological embedding
of B∗ into [ −1, 1]B . Since linearity and boundedness are preserved under
pointwise limits, the image is closed. By Tychonoﬀ, it is com pact!
Metrizability . Theorem. If X is separable, then the unit ball B in X∗ is
a compact metrizable space in the weak* topology.
Proof. Let xn be a dense sequence in X; then the balls
B = {φ : |φ(xn) −p/q|< 1/r}
form a countable base. By Urysohn’s metrization theorem, B is metrizable.
Example: the space of measures. Naturally C[0, 1] is separable. Thus
P [0, 1], the space of probability measures with the weak* topolog y, is a
compact metric space. It can be thought of as a sort of inﬁnite -dimensional
simplex; indeed the measures supported on ≤ n points form an ( n + 1)-
simplex.
Banach limits.
Theorem 6.7 There is a linear map Lim : ℓ∞(N) → R such that
Lim(an) ≥ 0 if an ≥ 0
Lim(1) = 1 , and
Lim(an+1) = Lim(an).
57

Note that | Lim(an)| ≤ ‖an‖ and that Lim extends the usual limit on c
and agrees with the C´ esaro limit when that exists.
Proof. Let φN (a) = N−1∑ N
1 an and let Lim be the limit point of a con-
vergent subnet. Note that φN (an+1) −φN (an) = O(1/N).
Stone- ˇCech compactiﬁcation of N. The unit ball B in ℓ∞(N)∗, while
compact, is not metrizable! Indeed, the integers embed via φn(a) = zn, but
⟨φn⟩has no convergent subsequence! (If φnk is a subsequence, then we can
choose a ∈ ℓ∞ such that ank = ( −1)k; then φnk(a) does not converge, so
φnk does not converge in the weak* topology.
The Banach-T arski paradox . Using the same construction on Z or Zn,
we get ﬁnitely-additive measures by applying Lim to indicat or functions.
Because of these measures, you cannot cut Z into a ﬁnite number of sets,
move them by translation and re-assemble them to form 2 copie s of Z.
However, this type of re-construction is possible for a free group G on 2
generators!
Suppose µ is a ﬁnitely-additive invariant probability measure on G. Let
Wa, Wa′, Wb and Wb′ denote the partition of G − {e} into reduced words
beginning with a,a′,b and b′. Then a′Wa contains Wa, Wb, Wb′ and {e}.
Since translation by a′ preserves measures, we conclude that the extra sets
Wb, Wb′ and {e} have measure zero. By the same token, all the W ’s have
measure zero, which contradicts the assumption that µ (G) = 1.
Cutting up the sun. Note that G = a′Wa ∪Wa′, and similar for Wb
and Wb′. Thus we can cut G into 5 pieces, discard one of them ( e), and
re-assemble the other two into two copies of G.
Now embed G into SO(3) by taking two random rotations. Then G
acts on S2. Let E ⊂S2 be a transversal, consisting of one point from each
G-orbit, so S2 = G ·E. Now cut S2 into pieces of the form Ei = Wi ·E,
i = 1,..., 4. (There will be some S2 left over.) Applying the left action of G
to these pieces — that is, applying rotations — we can re-arra nge W1 and
W2 to form G, and so re-arrange E1 andE2 to form S2. Do the same thing
with E3 and E4, and we can make a second sphere!
Three basic principles of functional analysis. Let A : X → Y be a
linear map between Banach spaces X and Y . Then we have:
1. The open mapping theorem. If A is continuous and onto, then it is
open; that is, Ax =y has a solution with ‖x‖ ≤C‖y‖.
58

Corollaries: If A is continuous and bijective, then it is an isomorphism.
If X is complete with respect to two norms, and ‖x‖1 ≤C‖x‖2, then
a reverse inequality holds.
2. The closed graph theorem. If the graph of A is closed — meaning
xn →x, Axn →y implies Ax =y — then A is continuous.
3. The uniform boundedness principle. Let F ⊂ X∗ satisfy that for each
x ∈X, |f (x)| ≤ Mx‖x‖ for all f ∈ F . Then there is an M such that
‖f ‖ ≤M for all f ∈ F .
The same result holds if we replace X∗ with B(X,Y ).
These principles should be compared to the following result s that hold
when X and Y are compact.
1. If f :X →Y is bijective and continuous, then f is a homeomorphism.
2. If f :X →Y has a closed graph, then f is continuous.
(Note that f (x) = 1 /x for x ⁄= 0, f (0) = 0, gives a map f : R → R
with a closed graph that is not continuous.)
3. Let F ⊂ C(X) satisfy |f (x)| ≤ Mx for all f ∈ F and x ∈ X. Then
there is a nonempty open set U ⊂X and a constant M >0 such that
|f |U | ≤ M for all x ∈U .
Open mapping theorem: proof. Let D =B(0, 1) be the open unit ball
about the origin in X. We must show B =A(D) contains a neighborhood
of the origin in Y . By surjectivity of A, we have Y =⋃ nB, and thus by the
Baire category theorem, nB has nonempty interior for some n; and thus B
has non-empty interior U .
Since B is convex and symmetric, we have ( U −U )/2 ⊂ B and so B
contains a neighborhood of the origin, say B(0,r ).
We now proceed to solve the equation Ax =y. Set M = 1/r. Then there
is an x1 with ‖x1‖ ≤M ‖y‖ and ‖Ax1 −y‖ as small as we like; say less than
‖y‖/2. Solving for the diﬀerence, we obtain an x2 with ‖x2‖ ≤M/2‖y‖ and
‖A(x1+x2)−y‖ ≤ ‖y‖/4. Proceeding by induction we obtain a geometrically
convergent sequence, and by continuity ofA we haveAx =y wherex =∑ xi
satisﬁes ‖x‖ ≤ 2M . Thus A(D) contains a ball of radius at least 1 /(2r)
about the origin.
59

Open-mapping theorem: application. The open mapping theorem
implies:
Corollary 6.8 If X is complete in two norms, and ‖x‖1 ≤ C‖x‖2, then
there is a C′ such that ‖x‖2 ≤C′‖x‖1.
Here is a nice application due to Grothendieck.
Theorem 6.9 Let S ⊂L2[0, 1] be a closed subspace such that every f ∈S
is continuous. Then S is ﬁnite-dimensional.
Proof. We have ‖f ‖∞ ≥ ‖f ‖2, so S is complete in both the L2 and the L∞
norms. Thus there is an M >0 such that M ‖f ‖2 ≥ ‖f ‖∞.
Now let f1,...,f n be an orthonormal set. Then for any p ∈ [0, 1], we
have
‖
∑
fi(p)fi‖2 = (
∑
|fi(p)|2)1/2,
and thus
M (
∑
|fi(p)|2)1/2 ≥ ‖
∑
fi(p)fi‖∞ ≥
∑
fi(p)2,
which implies ∑ fi(p)2 ≤M 2. Integrating from 0 to 1 gives n ≤M 2.
Closed graph theorem: proof. Let |x| = ‖x‖+ ‖Ax‖. Now if |xn| is
Cauchy, then xn → x in X and Axn → y in Y ; since the graph of A is
closed, we have Ax =y and thus |xn −x| → 0. Thus X is complete in the
| · |norm, so by the open mapping theorem we have |x| ≤ M ‖x‖ for some
M ; thus ‖A‖ ≤M andA is continuous.
Uniform boundedness theorem: proof. Let FM = {x : |f (x)| ≤
M ∀f ∈ F } . By Baire category, some FM contains a ball B(p,r ). Then
for ‖x‖ ≤r we have |f (x)| = |f (p +x) −f (p)| ≤ M +Mp and thus ‖f ‖ is
uniformly bounded by ( M +Mp)/r.
Example. Letφn ∈X∗ have the property that ψ(x) = lim φn(x) exists for
everyx ∈X. Then ‖φn‖ ≤M and hence ψ ∈X∗.
Corollary. You cannot construct an unbounded linear functi onal by tak-
ing a pointwise limit of bounded ones.
Remark: if a net satisﬁes xα →y, is ‖xα‖necessarily bounded? No! Let
α range over all ﬁnite subsets of N, directed by inclusion, and let xα be the
minimum of α. Then xα → 0 but sup xα = ∞.
60

Theorem 6.10 (T oeplitz) LetT :H →H be a symmetric linear operator
on Hilbert space, meaning (Tx,y ) = (x,Ty ). Then T is continuous.
Proof. Suppose xn →x and Txn →z. Then for all y ∈H, we have
(y,z ) = lim(y,Tx n) = lim(Ty,x n) = (Ty,x ) = (y,Tx ).
Thus (y,Tx −z) = 0 for all y ∈ H. Taking y = Tx −z, we ﬁnd Tx = z.
ThusT has a closed graph, and hence T is continuous.
Note: a typical symmetric operator is given by (Tf )(x) =
∫
K(x,y )f (y)dy,
where the kernel K(x,y ) is symmetric.
Convexity . A subset K ⊂X is convex if x,y ∈K =⇒ tx + (1 −t)y ∈K
for all t ∈ (0, 1).
Support.
Theorem 6.11 LetK ⊂X be an open convex set not containing the origin.
Then there is a φ ∈X∗ such that φ(K)> 0.
Proof. Geometrically, we need to ﬁnd a closed, codimension-one hyp erplane
H = Ker φ ⊂ X disjoint from K. Consider all subspaces disjoint from K
and let H be a maximal one (which exists by Zorn’s lemma). If H does
not have codimension one, then we can consider a subspace S ⊃ H of two
dimensions higher and all extensions H′ =H + Rvθ of H to S, θ ∈S1.
Now consider the set A ⊂S1 of θ such that H + R+vθ meets K. Then
A is open, connected, and A ∩A +π = ∅; else K would meet H. It follows
thatA is an open interval of length at most π. Taking an endpoint of A, we
obtain an extension of H to H′, a contradiction.
Thus H has codimension one. Since K is open,
H is also disjoint from
K, and hence H =H. Thus H is the kernel of the desired linear functional.
Separation.
Theorem 6.12 Let K,L ⊂X be disjoint convex sets, with K open. Then
there is a φ ∈X∗ separatingK fromL; i.e. φ(K) and φ(L) are disjoint.
Proof. LetM =K −L; this set is open, convex, and it does not contain the
origin because K andL are disjoint. Thus by the support theorem, there is
a linear functional with φ(M ) ≥ 0. Then for all k ∈K and ℓ ∈L, we have
φ(k −ℓ) = φ(k) −φ(ℓ) ≥ 0. It follows that inf φ(K) ≥ supφ(L). Since φ(K)
is open, these sets are disjoint.
61

W eak closure. Recall that K ⊂ X is weakly closed if whenever a net
xα ∈ K satisﬁes φ(xα) → φ(x) for all φ ∈ X∗, we have x ∈ K. The weak
closure of a set is generally larger than the strong (or norm) closure. For
example, the sequence fn(x) = sin( nx) in L1[0, 1] is closed in the norm
topology (it is discrete), but its weak closure adds f0 = 0.
Another good image to keep in mind is that K is weakly closed if for
any x ⁄∈K, there is a continuous linear map Φ : X → Rn such that Φ( K)
is disjoint from Φ( x). This is just because a base for the weak topology
consists of ﬁnite intersections of sets of the form φ−1(α,β ).
Theorem 6.13 A convex set K ⊂ X is weakly closed iﬀ K is strongly
(norm) closed.
Proof. A weakly closed set is automatically strongly closed. Now su ppose
K is strongly closed, and x ⁄∈K. Then there is an open ball B containing
x and disjoint from K. By the separation theorem, there is a φ ∈X∗ such
that φ(x) > φ(K), and thus x is not in the weak closure of K. Thus K is
weakly closed.
Linear combinations. By the preceding result, we see that the weak
closure of a set E ⊂ X is contained in hull( E), the smallest norm-closed
convex set containing E. Now hull( E) can be described as the closure of
ﬁnite convex combinations of points in E. So as an example we have:
Proposition. For any ǫ> 0 there exist constants an ≥ 0,∑ an = 1, such
that ‖
‖
‖
‖
‖
N∑
1
an sin(nx)
‖
‖
‖
‖
‖
1
<ǫ.
Problem. Prove this directly!
(Solution. Just take an = 1/N for n = 1,...,N , and note that for
orthgonal functions en the function f =∑ anen satisﬁes
‖f ‖2
1 ≤ ‖f
22‖1‖2
2 =O(
∑
|an|2) = O(1/N).
Intuitively,f (x) behaves like a random walk with N steps.
LCTVS. A topological vector space X is a vector space with a topology
such that addition and scalar multiplication are continuou s. By translation
invariance, to specify the topology on X it suﬃces to give a basis at the
origin.
A very useful construction comes from continuity of additio n: for any
open neighborhood U of the origin, there is a neighborhood V such that
V +V ⊂U .
62

Usually we assume X is Hausdorﬀ ( T2). This is equivalent to assuming
points are closed ( T1). Indeed, if points are closed and x ⁄=y, then we can
ﬁnd a balanced open neighborhood U of the origin such that y +U is disjoint
from X. We can then ﬁnd a balanced open V such that V +V ⊂ U , and
then x +V is disjoint from y +V .
W arning: Royden at times implicitly assumesX is Hausdorﬀ. For example,
ifX is not Hausdorﬀ, then an extreme point is not a supporting set , contrary
to the implicit assumption in the proof of the Krein-Milman t heorem.
LetX be a Banach space. Then the weak topology on X and the weak*
topology on X∗ are Hausdorﬀ and locally convex. All the results like the
Hahn-Banach theory, the separation theorem, etc. hold for l ocally convex
topologies as well as the norm topology and weak topology.
Extreme points. Let K be convex. A point x ∈K is an extreme point if
there is no open interval in K containing X. More generally, a supporting
setS ⊂K is a closed, convex set with the property that, whenever an op en
intervalI ⊂K meets S, then I ⊂S. One should imagine a face of ∂K or a
subset thereof.
Example: Let K be a convex compact set. Then the set of points where
φ ∈X∗ assumes its maximum on K ⊂X is a supporting set. In particular,
any compact convex set has nontrivial supporting sets.
Theorem 6.14 (Krein-Milman) LetK be a compact convex set in a lo-
cally convex (Hausdorﬀ ) topological vector space X. Then K is the closed
convex hull of its extreme points.
Remark. The existence of any extreme points is already a nontrivial
assertion.
Proof. We will show any supporting set contains an extreme point. In deed,
consider any minimal nonempty supporting set S ⊂K; these exist by Zorn’s
lemma, using compactness to guarantee that the intersectio n of a nested
family of nonempty supporting sets is nonempty. Now if S contains two
distinct points x and y, we can ﬁnd a φ ∈ X∗ (continuous in the given
topology) such that φ(x) ⁄= φ(y). Then the set of points in S where φ
assumes its maximum is nonempty (by compactness) and again a supporting
set, contrary to minimality.
Now let L ⊂K be the closed convex hull of the extreme points. If there
is a point x ∈K −L, then we can separate x fromL by a linear functional,
sayφ(x)>φ (L). But then the set of points where φ assumes its maximum
is a supporting set, and therefore it contains an extreme poi nt, contrary to
the assumption that φ does not assume its maximum on L.
63

Therefore L =K.
Prime example: The unit ball in X∗, in the weak* topology.
What are the extreme points of the unit ball B inL2[0, 1]? Every point
in ∂B is extreme! Because if ‖f ‖2 = 1 then for ǫ andg ⁄= 0, we have
‖f ±ǫg‖2
2 = ‖f ‖2 ± 2ǫ⟨f,g ⟩+ǫ2‖g|2
and this is > ‖f ‖2 = 1 if the sign is chosen properly.
What about the unit ball in L∞[0, 1]? Here the extreme points are
functions with |f | = 1 a.e. Picture the ﬁnite-dimensional case — a cube.
What about in L1[0, 1]? Here there are no extreme points! For example,
if f = 1, then f (x) + a sin(2πx) has norm one for all small a, so f is not
extreme. Similarly, for any f ⁄= 0 we can ﬁnd a set A of positive measure
on which f > a >0 (or 0 > a > f), and then a function g of mean zero
supported on A such that ‖f ±g‖= ‖f ‖.
This fact is compatible with Krein-Milman only because L1[0, 1] is not a
dual space. In fact the preceding remark proves that for any Banach space
X, the dual X∗ is not isomorphic to L1[0, 1].
ForX =C[0, 1], the dual X∗ consists of signed measures of total mass
one, and the extreme points are ±δx.
Stone-W eierstrass revisited. Let X be a compact Hausdorﬀ space, and
letA ⊂C(X) be an algebra of real-valued functions containing the cons tants
and separating points. Then A is dense in C(X).
Proof (de Brange). LetA⊥ ⊂M (X) be the set of measures that annihi-
lateA. By the Hahn-Banach theorem, to show A is dense it suﬃces to show
that A⊥ is trivial.
Let K be the intersection of A⊥ with the unit ball. Then K is a closed,
compact, convex set in the weak* topology. Thus K is the closed convex
hull of its extreme points.
Suppose µ ∈K is a nonzero extreme point. We will deduce a contradic-
tion.
First, let E ⊂ X be the support of µ (the smallest closed set whose
complement has measure zero). Suppose E is not a single point. Choose a
function f ∈ A such that f |E is not constant, and |f | < 1. Consider the
two measures
σ = (1 +f )µ/ 2, τ = (1 −f )µ/ 2.
Since A is an algebra, both σ and τ are in A⊥, and of course we have
σ +τ =µ . Moreover, since 1 ±f >0, we have
‖µ | = ‖σ‖+ ‖τ | = 1.
64

Thusµ is a convex combination:
µ = ‖σ‖ σ
‖σ‖ + ‖τ ‖ τ
‖τ ‖.
Since µ is an extreme point, it follows that µ = σ = τ . Therefore f is
constant a.e. on E, a contradiction.
It follows that µ is a delta-mass supported on a single point. But the µ
is not in A⊥, since it pairs nontrivially with the constant function in A.
Haar measure. As a further application of convexity, we now develop
the Kakutani ﬁxed-point theorem and use it to prove the exist ence of Haar
measure on a compact group. Our treatment follows Rudin, Functional
Analysis, Chapter 5.
Theorem 6.15 (Milman) Let K ⊂ X be a compact subset of a Banach
space and suppose H = hull(K) is compact. Then the extreme points of H
are contained in K.
Proof. Suppose x is an extreme point of H that does not lie in K, and let
r =d(x,K ). Then by compactness we can cover K by a ﬁnite collection of
ballsB(xi,r ),i = 1,...,n . Let Hi be the closed convex hull of K ∩B(xi,r ).
Since the ball is compact, we have Hi ⊂B(xi,r ).
Now H = hull(⋃ n
1Hi), and thus x =∑ tihi is a convex combination of
points hi ∈Hi ⊂H. But x is an extreme point, so x =hi for some i. This
implies x ∈B(xi,r ), contradicting the fact that d(x,K ) = 2r.
Theorem 6.16 (Kakutani) Let K ⊂ X be a nonempty compact convex
subset of a Banach space, and let G be a group of isometries of X leaving
K invariant. Then there exists an x ∈K ﬁxed by all g ∈G.
Proof. Let L ⊂ K be a minimal, nonempty, compact convex G-invariant
set; such a set exists by the Axiom of Choice. If L consists of a single point,
we are done. Otherwise there are points x ⁄=y inL. Let z = (x+y)/2. Then
by minimality of L, we have L = hull(G ·z). Let z′ be an extreme point of
L. By Milman’s theorem, z′ is a limit of points in G ·z. By compactness of
K, we can choose gn ∈G such that gnz →z′, gnx →x′ and gny →y′. But
then z′ = (x′ +y′)/2, so z′ is not an extreme point.
65

Theorem 6.17 LetG be a compact Hausdorﬀ group. Then there is a unique
left-invariant Borel probability measureµ onG, and µ is also right invariant.
Proof. Let G be a compact topological group, and let X = C(G). For
eachg,h ∈G, the shift operators Lg(f ) = f (g−1x) and Rh(f ) = f (xh) are
isometries, and they commute. The only ﬁxed-points for G are the constant
functions.
Now ﬁx f ∈ C(G). Then f , and all its translates, are equicontinuous,
and thus
L(f ) = hull(G ·f ) ⊂C(G)
is compact. Similarly, the closed convex hull of the right tr anslates,R(f ) =
hull(f ·G), is also compact. By Kakutani’s ﬁxed-point theorem, each o f
these convex sets contains at least one constant function, l(f ) and r(f ).
The constant l(f ) can be approximated by averages of the form
T (f ) =
∑
αiLai(f ),
and similarly for r(f ). But the right and left averages commute, and leave
the constants invariant, so l(f ) = r(f ). Thus there is a unique constant
function, M (f ), contained in both L(f ) and R(f ).
To show M (f ) corresponds to Haar measure, we must show M (1) = 1,
M (f ) ≥ 0 when f ≥ 0, and M is linear. The ﬁrst two assertions are
immediate. To show M (f +h) = M (f ) + M (h), choose a left-averaging
operator T such that M (f ) ≈ T (f ). Then T (h) ∈ L(h), so M (T (h)) =
M (h). Thus there is a second left-averaging operator S such thatS(T (h)) ≈
M (h). But then S(T (f +h)) ≈M (f ) +M (h) ∈L(f +h), so M (f +h) =
M (f ) +M (h).
Examples of compact groups: Finite groups, products such as ( Z/2)N,
inverse limits such as Zp = lim
←−
(Z/pn); Lie groups such as SO( n, R) and
SU(n, C); p-adic Lie groups such as SL n(Zp).
Here is a description of Haar measure on G = SO(n, R). Consider the
Lie algebra g = so(n, R); it is the space of trace-zero matrices satisfying
At = −A. There is a natural inner product on this space, given by ⟨A,B ⟩=
tr(AB). This inner product is invariant under the adjoint action o f G, so it
gives rise to an invariant quadratic form on every tangent sp aceTgG. In the
case of SO(n), this metric is negative deﬁnite. Thus its negative determ ines
a bi-invariant metric on SO(n, R), and hence an invariant measure.
This measure can be described as follows: to choose a random f rame in
Rn, one ﬁrst pick a point at random on Sn−1, then a point at random on the
66

orthogonal Sn−2, etc., using the rotation-invariant probability measures on
each sphere. There is a unique choice for the ﬁnal point on S0 that makes
the frame positively oriented.
Unimodularity . More generally, any locally compact group G carries
right and left invariant measures, unique up to scale, but th ey need not
agree. When they do, the group is unimodular. For example, the group
SL2(R) is unimodular, but its upper-triangular subgroup AN is not.
7 Hilbert space
Of great importance in analysis are the Hilbert spaces, such as L2(Rn).
Abstractly, a Hilbert space is a Banach space H equipped with a sym-
metric bilinear form ( x,y ) such that ( x,x ) = ‖x‖2. Examples:
Rn, (x,y ) =∑ xiyi.
ℓ2(N), (x,y ) =∑ xiyi.
L2(Rn), (f,g ) =
∫
f (x)g(x)dx.
Theorem 7.1 (Bunyiakowsky-Cauchy-Schwarz) |(x,y )| ≤ ‖x‖ · ‖y‖.
Proof. For allt we have 0 ≤ (x +ty,x +ty) = (x,x ) +t2(y,y ) + 2t(x,y ), so
the discriminant of this quadratic polynomial must be non-p ositive. Thus
0 ≥b2 − 4ac ≥ 4(x,y )2 − 4(x,x )(y,y ).
An orthonormal set is a collection of unit vectors xi in H, i ∈ I, with
(xi,xj) = δij. The index set I can be ﬁnite, countable or even larger.
Given an orthonormal set, we deﬁne the ‘Fourier coeﬃcients’ of x ∈ H
byai = (x,xi).
Lemma (Bessel). ∑ |ai|2 ≤ ‖x‖2.
Proof. For any ﬁnite sum we have
0 ≤ (x −
∑
aixi,x −
∑
aixi) = (x,x ) − 2
∑
|ai|2 +
∑
|ai|2.
A basis for H is a maximal orthonormal set ( xi). By Zorn’s Lemma,
every Hilbert space has a basis. The elements of a basis are at distance
√
2
from one another. Thus if H is separable, it has a countable basis.
Given a basis, we can use Bessel’s inequality to show ∑ aixi converges
for any ( ai) ∈ ℓ2(I). Moreover, the norm of the sum in H coincides with
67

the norm in ℓ2(I). Finally, if x ∈ H has Fourier coeﬃcients ai, then y =
x −∑ aixi has Fourier coeﬃcients zero, i.e. it is orthogonal to all xi. Since
the (xi) are a maximal orthonormal set, y = 0. This shows:
Theorem 7.2 For any orthogonal basis, and any x ∈ H, we have x =∑ aixi in H.
Theorem 7.3 For any basis (xi,i ∈ I) of a Hilbert space H, there is a
natural isomorphism between H and the Hilbert space ℓ2(I).
Examples: On S1 = R/Z, we can take 1, cos(2 πnx) and sin(2πnx) as an
orthonormal basis. Completeness follows from Stone-Weier strass.
On [ −1, 1] we can apply Gram-Schmidt to the polynomials to obtain
an orthonormal basis of Legendre polynomials pn(x). of degree n. Again
Stone-Weierstrass yields completeness.
Complex Hilbert spaces. Over the ﬁeld C, the natural form for a Hilbert
space is a Banach space H with a Hermitian form ⟨x,y ⟩such that ⟨x,x ⟩=
‖x‖2. In this case, ( x,y ) = Re ⟨x,y ⟩makes H into a Hilbert space over R.
Examples:
⟨x,y ⟩=∑ xi
yi on Cn or ℓ2(N) ⊗ C.
⟨f,g ⟩=
∫
fg on L2(Rn).
The Hardy space. InL2(S1) ⊗ C, a natural orthonormal basis is given by
fn(z) = zn/2π. The span of fn,n ≥ 0 is a closed subspace H 2(S1) known
as the Hardy space of the circle. Every f ∈H 2(S1) is the boundary value of
a holomorphic function on S1.
F ourier series. For a function f (z) in L2(S1), we have f =∑ anzn (norm
convergent in L2) where
an = 1
2πi
∫
S1
f (z)z−n dz
z ·
Note the analogy with Laurent series.
Passing to the coordinate x where z = exp(ix), we can think of L2(S1)
as the subspace of L2(R) consisting of functions that are periodic under
x ↦→x + 2π. Since zn = cos(nx) +i sin(nx), the Fourier series now becomes
a sum of sines and cosines.
68

If we restrict to odd functions — where f (−x) = −f (x) — then only
sine terms appear, and we can identify this subspace with L2[0,π ]. Thus a
function on [0,π ] has a natural Fourier series:
f (x) =
∞∑
n=1
an sin(nx).
Since
∫ π
0 sin2(x)dx =π/2 (its average value is 1 /2), we have
an = 2
π
∫ π
0
f (x) sin(nx)dx.
Example: if the graph of f is a triangle with vertex ( p,x ), then
an = 2h sin(np)
n2p(π −p) ·
0 0.5 1 1.5 2 2.5 3
-0.5
0
0.5
1
0 0.5 1 1.5 2 2.5 3
0
0.2
0.4
0.6
0.8
1
0 0.5 1 1.5 2 2.5 3
0
0.2
0.4
0.6
0.8
1
Figure 2. Solutions to the wave equation (undamped and dampe d) and the
heat equation.
The wave equation and the heat equation. A typical problem in PDE
is to solve the wave equation with given initial data f (x) = u(x, 0) on [0,π ].
This equation, which governs the motion u(x,t ) of a vibrating string, is
given by
utt =uxx
69

(where the subscripts denote diﬀerentiation). If we think o f u(x,t ) as the
motion of a string with ﬁxed end points, it is natural to impos e the boundary
conditions u(0,t ) = u(π,t ) = 0. We will also assume ut(x, 0) = 0, i.e. the
string is intially stationary.
Since the wave equation is linear, it suﬃces to solve it for th e Fourier
basis functions f (x) = sin(nx). And for these we have simply
u(x,t ) = cos(nt) sin(nx).
This solution can be discovered by separation of variables; the key is that
f (x)g(t) solves the wave equation if f and g are eigenfunctions with the
same eigenvalues.
These basic solutions are ‘standing waves’ corresponding t o the bass note
and then the higher harmonics of the string.
The solution to the wave equation for ‘general’ f (x) is then given by:
u(x,t ) =
∞∑
n=1
an cos(nt) sin(nx).
Note that u(x,t + 2π) = u(x,t ), i.e. the string has a natural frequency.
The heat equation
ut =uxx
governs the evolution of temperature with respect to time. I n the case at
hand the boundary conditions mean that the ends of the interv al are kept
at a constant temperature of zero. Now the basic solutions ar e given by
u(x,t ) = e−n2t sin(nx).
and thus
u(x,t ) =
∞∑
n=1
ane−n2t sin(nx).
Note that the Fourier coeﬃcients are severely damped for any positive time;
u(x,t ) is in fact a real-analytic function of x for t> 0.
An actual plucked guitar string does not have a periodic moti on but a
motion that smooths and decays with time. It obeys a combinat ion of the
heat and wave equations:
utt + 2δut =uxx.
Here the basic solutions are given by
u(x,t ) = exp(αnt) sin(nx)
70

where α2
n + 2δαn +n2 = 0. So long as 0 ≤δ ≤ 1 we get
αn = −δ ±i
√
n2 −δ2
and thus the solution with ut(x, 0) = 0 has the form
u(x,t ) = exp( −δt) cos(ωnt +σn) sin(nx),
where ωn =
√
n2 −δ2 and tan(σn) = −δ/ωn. Note that the frequencies are
now slowed and out of harmony — their ratios are no longer rati onal — and
that u(t,x ) is damped but not smoothed out over time!
Discrete F ourier series. Similarly, given an ∈ ℓ2(Z), there is a function
f ∈L2(S1) such that
an =
∫
S1
f (x)e−inxdx.
In other words, an is a ‘continuous superposition’ of the sequences bx
n =einx.
Note that while zn/2π is a basis for L2(S1), the sequences bx
n are not
even in ℓ2(Z).
Convergence of F ourier series. One of the main concerns of analysts for
150 years has been the following problem: given a function f (x) on S1, in
what sense is f represented by its Fourier series ∑ an exp(inx)?
It is traditional to write SN (f ) = ∑ N
−Nan(f ) exp(inx). The simplest
answer to the question is the one we have just seen: so long as f ∈L2(S1),
we have ∫
|f −SN (f )|2 → 0
as N → ∞.
The question of pointwise convergence is equally natural: h ow can we
extract the value f (x) from the numbers an? Of course, if f is discontinuous
this might not make sense, but we might at least hope that when f (x) is
continuous we have SN (f ) →f pointwise, or maybe even uniformly. In this
direction we have:
Theorem 7.4 If f (x) is C 2, then an =O(1/n2) and thus SN (f ) converges
to f uniformly.
In fact we have:
Theorem 7.5 (Dirichlet) If f (x) is C 1, then SN (f ) converges uniformly
to f .
71

Dirichlet’s proof . . . left open the question as to whether th e Fourier
series of every Riemann integrable, or at least every contin uous,
function converged. At the end of his paper Dirichlet made it
clear he thought that the answer was yes (and that he would soo n
be able to prove it). During the next 40 years Riemann, Weier-
strass and Dedekind all expressed their belief that the answ er was
positive. —K¨ orner, Fourier Analysis, §18.
In fact this is false!
Theorem 7.6 (DuBois-Reymond) There exists an f ∈C(S1) such that
supN |SN (f )(0)| = ∞.
Use of functional analysis. To see this, suppose to the contrary that the
sup above is ﬁnite for all continuous f . That is, suppose the values of the
linear functionals f ↦→SN (f )(0) are bounded by Mf . Then, by the uniform
boundedness principle, they are uniformly bounded:
sup
N
|SN (f )(0)| ≤ M ‖f ‖∞.
There is nothing special about the point zero, so in fact we ha ve:
‖SN (f )‖∞ ≤M ‖f ‖∞
where M is independent of N .
Now let us further note that everyL∞ function is the limit in measure of a
uniformly bounded sequence of continuous functions. (Put d iﬀerently, C(S1)
is dense in L∞(S1 in the weak* topology.) Since each Fourier coeﬃcient
varies continuously under such weak* limits, we have ‖SN (f )‖∞ ≤M ‖f ‖∞
for all f ∈L∞(S1).
Next we note that SN (f )(0) = ∑ N
−Nan(f ) is simply the sum of the
Fourier coeﬃcients of f ,
an(f ) = 1
2π
∫
S1
f (x) exp(−inx)dx.
Thus we can write SN (f )(0) = (1 /2π)
∫
fDN , where DN is the Dirichlet
kernel
DN (x) =
N∑
−N
exp(−inx).
72

Then we have shown that
⏐
⏐
⏐
⏐
∫
DNf
⏐
⏐
⏐
⏐ ≤M ‖f ‖∞
for all f ∈L∞. But this implies ‖DN ‖1 ≤M .
We now show that in fact, ‖DN ‖1 → ∞ as N → ∞ . Setting q =
exp(inx), we have
DN (x) =
N∑
−N
q−n =q−N 1 −q2N +1
1 −q = qN +1/2 −q−N−1/2
q1/2 −q−1/2 = sin((N + 1/2)x)
sin(x/2) ·
Clearly all the action occurs near x = 0; indeed, we have |DN (x)| =
O(1/|x|) on [ −π,π ]. But near x = 0, there are periodic intervals on which
| sin((N + 1/2)x)| > 1/2. On these intervals, |1/ sin(x/2)| ≈ 2/|x|. Since∫
dx/|x| diverges, we have ‖DN ‖1 → ∞ . In fact, the L1-norm behaves like∫ 1
1/Ndx/x ≍ log(N ).
After this phenomenon was discovered, a common sentiment wa s that it
was only a matter of time before a continuous function would b e discovered
whose Fourier series diverged everywhere. Thus it was even m ore remarkable
when L. Carleson proved:
Theorem 7.7 For any f ∈L2(S1), the Fourier series of f converges to f
pointwise almost everywhere.
The proof is very diﬃcult.
The F ej´ er kernel.However in the interim Fej´ er, at the age of 19, proved
a very simple result that allows one to reconstruct the value s of f from its
Fourier series for any continuous function.
Theorem 7.8 For any f ∈C(S1), we have
f (x) = lim S0(f ) + · · ·+SN−1(f )
N
uniformly on the circle.
This expression is a special case of C´ esaro summation, where one re-
places the sequence of partial sums by their averages. This p rocedure can
73

-3 -2 -1 1 2 3
-2
2
4
6
8
10
12
-3 -2 -1 1 2 3
0.25
0.5
0.75
1
1.25
1.5
1.75
Figure 3. The Dirichlet and Fej´ er kernels.
be iterated. In the case at hand, it amounts to computing ∑ ∞
−∞an as the
limit of the sums
1
N
N∑
i=−N
(N − |i|)an.
Approximate identities. To explain Fej´ er’s result, it is useful to ﬁrst
understand the idea of convolution and approximate identit ies.
WritingS1 as an additive group, for f,g ∈L1(S1) we let
(f ∗g)(x) = (1/2π)
∫
S1
f (x)g(y −x)dx.
Note that f ∗g = g ∗f . It is easy to show that ( f ∗g)(x) is a continuous
function of x; thus convolution is a smoothing operator.
We say fn is an approximation to the identity if fn ≥ 0, (1/2π)
∫
fn = 1
for all n andfn → 0 uniformly on compact sets outside x = 0.
Theorem 7.9 If fn is an approximation to the identity, and g ∈ C(S1),
then f ∗g →g uniformly on S1.
Proof. Think of fn ∗g are a sum of the translates g(x −y) weighted by
fn(y). The translates with y small are uniformly close to g because g is
continuous. The translates with y large make a small contribution because
their total weight is small. Thus fn ∗g is uniformly close to g.
74

If we let
TN (f ) = S0(f ) + · · ·+SN−1(f )
N ,
then TN (f ) = f ∗FN where the Fej´ er kernelis given by
FN = (D0 + · · ·DN−1)/N.
Of course
∫
FN = 1 since
∫
Dn = 1. But in addition, FN is positive and
concentrated near 0, i.e. it is an approximation to the identity. Indeed, we
have:
FN (x) = sin2(Nx/ 2)
N sin2(x/2) ·
To see the positivity more directly, note for example that
(2N + 1)F2N +1 = z−2N + 2z−2N +1 + · · ·+ (2N + 1) + · · ·2z2N−1 +z2N
= ( z−N + · · ·zN )2 =D2
N,
where z = exp(ix).
F ourier transform. One of the great ideas in analysis is the Fourier
transform on L2(R). We deﬁne it on f ∈L2(R) by
ˆf (ξ) =
∫
R
f (x)e−ixξdx.
This integral at least makes sense when f is smooth and compactly sup-
ported.
We claim ( ˆf, ˆf ) is a constant multiple of ( f,f ). Indeed, on any in-
terval [ −πM,πM ] large enough to contain the support of f , we have an
orthonormal basis gi = einx/M/
√
2πM ; writing f = ∑ aigi we ﬁnd ai =
ˆf (n/M)/
√
2πM , and thus
(f,f ) =
∑
|ai|2 = 1
2πM
∑ ˆf (n/M) → 1
2π
∫
|ˆf |2
as n → ∞. Thus f extends to all of L2 as an isometry.
F ourier transform and diﬀerential equations. The Fourier transform
reverse small-scale and large scale features of f . It turns diﬀerentiation
d/dxi into multiplication by xi. Thus ˆf (0) =
∫
f ; if f is smooth then ˆf
decays rapidly at inﬁnity; etc.
Since diﬀerentiation is turned into multiplication, it bec omes easy to
solve PDEs. For example, to solve ∆ u =f , you just pass to the transform
75

side and divide ˆf by∑ x2
i . There is no diﬃcultly near inﬁnity for the result
to be in L2; this reﬂects that fact that ∆ is a smoothing operator. There is
diﬃculty near 0: both
∫
f and the moments
∫
fxi should vanish for u to be
in L2.
Spherical harmonics. We can also look from L2(S1) in another direction
— towards L2(Sn−1), where the domain remains compact but its symmetry
group becomes larger G = SO(n). How do Fourier series generalize to the
higher-dimensional spheres?
The case of a sphere is especially convenient because we can r egardSn−1
as the unit ball |x| = 1 in Rn. Let Pd denote the space of homogeneous
polynomials of degree d on Rn. We have
dimPd =
(d +n − 1
n − 1
)
·
The Laplacian ∆ = ∑ d2/dx2
i mapsPd toPd−2; its kernel Hd is the space of
harmonic polynomials of degree d. The key property of the Laplace operator
is that it is SO( n)-invariant.
Theorem 7.10 We have L2(Sn−1) = ⊕∞
d=0Hd.
Generally a function f ∈Hd or its restriction to Sn−1 is called a spherical
harmonic. It can be shown that f , considered as a function the sphere, is
actually an eigenfunction of the spherical Laplacian.
One can also study issues of pointwise convergence in this se tting, for
example one has:
Theorem 7.11 If f ∈ C 2(Sn−1) then its Fourier series converges uni-
formly.
To begin the proof that the spherical harmonics forms a ‘basi s’ for
L2(Sn−1), we ﬁrst show there is no relation between them.
Proposition 7.12 The restriction map from Rn to Sn−1 is injective on
⊕Hd.
Proof. A harmonic polynomial which vanishes on the sphere is everyw here
zero, by the maximum principle.
76

Raising operator. Of course this result fails for general polynomails,
because r2 = ∑ x2
i is constant on Sn−1. To take this into account, we
introduce the raising operator
L :Pd →Pd+2
deﬁned by L(f ) = r2f . Here are some of its key properties and their conse-
quences.
1. If f is harmonic, then ∆ L(f ) = 2(n +d)f . This is because
∆( r2f ) = (∆ r2)f + (∇r2) ·(∇f ) +r2∆ f
2. More generally, we have ∆ L(f ) = 2( n +d)f +L∆ f , i.e. [∆ ,L ] =
2(n +d). From this we ﬁnd inductively:
∆ Lk+1 =CkLk +Lk+1∆ ,
whereCk ⁄= 0. This shows:
∆( r2k+2Hd) = r2kHd
(and of course the map is an isomorphism because both sides ha ve the
same dimension).
3. We can now prove by induction:
Pd =Hd ⊕r2Hd−2 ⊕r4Hd−4 ⊕ · · ·
Indeed, once this is known for Pd we simply consider ∆ : Pd+2 →Pd.
This map has kernel Hd+2 and maps r2Hd bijectively to Hd, etc.
4. As a Corollary we immediately see that ⊕Hd|Sn−1 is the same space
of functions as ⊕Pd|Sn−1, since r = 1 on Sn−1. In particular, ⊕Hd is
dense in L2(Sn−1).
5. It remains to check that Hd and He are orthogonal for d ⁄= e. One
way is to consider the spherical Laplacian and note that thes e are
eigenspaces with diﬀerent eigenvalues. Another way is to co nsider the
character of SO(2) acting on Hd.
6. The combination of these observations proves the spheric al harmonics
form a basis for L2(Sn−1).
77

Low-dimensional examples. For example, whenn = 2 we have dimH0 =
1 and dim Hd = 2 for d> 0. A basis is given by Re zd and Imzd.
Forn = 3 we have dim hd = 2d + 1 = 1, 3, 5,... . It is traditional to form
a complex basis Ymd for Hd where −d ≤m ≤d, and
Ymd(x,y,z ) = (x ±iy)|m|Pm
d (z).
Here Pm
d (z) is a Legendre polynomial.
The hydrogen atom. The simplest model for the hydrogen atom in quan-
tum mechanics has as states of pure energy the functions f on R3 which
satisfy
∆ f +r−1f =Ef.
It turns out a basis for such functions has the form of product s of radial
functions with spherical harmonics. The energy is proporti onal to 1 /N2
where N is the principal quantum number. For a given N , the harmonics
with 0 ≤ d < N− 1 all arise, each with multiplicity 2 d + 1, so there are
N 2 independent states altogether. The states with d = 0, 1, 2, 3,... are
traditionally labelled s, p, d, f , g, h.
Irreducibility . Is there a ﬁner Fourier series that is still natural with
respect to rotations? The answer is no:
Theorem 7.13 The action of SO(n) on Hd is irreducible.
Proof. There are many proofs of irreducibility; here is a rather int uitive,
analytic one.
Suppose the action of SO(n) on Hd splits nontrivially as A⊕B. Then we
can ﬁnd in each subrepresentation a function such that f (N ) = 1, where N
is the ‘north pole’ stabilized by SO( n − 1); and by averaging over SO(n − 1),
we can assume f is constant on each sphere Sn−2 ⊂ Sn−1 centered at N .
In particular, if we consider a ball B ⊂ Sn−1 centered at N and of radius
ǫ> 0, we can ﬁnd a nonzero f ∈Hd with f |∂B = 0 and max f |B = 1.
Considere the cone U = [0, 2]B ⊂ Rn. Then f is a harmonic function
which vanishes on all of the boundary of B except the cap 2 B. By homo-
geneity, maxf |2B = 2d. In addition, there is an x ∈B where f (x) = 1. By
the mean value property of harmonic functions, f (x) is the average of the
valuesf (y) over the points y where a random path initiated at x ﬁrst exists
U . But the probability that the path exits through the cap 2 B is p(ǫ) → 0
as ǫ → 0. Thus
1 = f (x) ≤ 2dp(ǫ) → 0,
a contradiction.
78

(Note: this argument gives a priori control over the diameter of a closed
‘nodal set’ for an eigenfunction of the Laplacian on Sn−1 in terms of its
eigenvalue.)
Spherical Laplacian. Here is a useful computation for understanding
spherical harmonics intrinsically.
To compute the Laplacian of f |Sn−1, we use the formula:
∆ s(f ) = ∇ ·πs(∇f ),
where
πs(∇f ) = ∇f − (ˆr · ∇f )ˆr
is the projection of ∇f to a vector ﬁeld tangent to the sphere. Using the
fact that ∇ ·ˆr =n − 1, this gives:
∆ s(f ) = ∆( f ) − (n − 1)(df/dr) −d2f/dr 2.
Now suppose f is a spherical harmonic of degree ℓ. Then ∆( f ) = 0, df/dr =
ℓf , and d2f/dr 2 =ℓ(ℓ − 1)f , which yields:
Theorem 7.14 Iff ∈Hℓ(Rn) thenf |Sn−1 is an eigenfunction of the spher-
ical Laplacian, satisfying
∆ s(f ) = −ℓ(ℓ +n − 2)f.
8 General Measure Theory
Measures. A measure (X, B,m ) consists of a map m : B → [0, ∞] deﬁned
on aσ-algebra of subsets of X, such thatm(∅) = 0 and such that ∑ m(Bi) =
m(⋃ Bi) for countable unions of disjoint Bi ∈ B .
Countable/Co-countable measure. An example is the measure deﬁned
on any uncountable set X by taking B to be the σ-algebra generated by
singletons and m(B) = 0 or ∞ depending on whether B is countable or
X −B is countable.
Hausdorﬀ measure. This is deﬁned on the Borel subsets of Rn by
mδ(E) = lim
r→0
inf
E=SEi
∑
diam(Ei)δ,
where diam(Ei) ≤r. Appropriately scaled, mn is equal to the usual volume
measure on Rn.
79

Dimension; the Cantor set. The Hausdorﬀ dimension of E ⊂ Rn is the
inﬁmum of those δ such that mδ(E) = 0.
For example, the usual Cantor set E can be covered by 2 n intervals of
length 1/3n, so its dimension is at most log 2 / log 3. On the other hand,
there is an obvious measure on E such that m(A) ≤C(diamE)log 2/ log 3 and
from this it is easy to prove the dimension is equal to log 2 / log 3.
Linear maps and dimension. Clearly Hausdorﬀ measure satisﬁes mδ(αE) =
αδm(E). So for the Cantor set E built on disjoint subintervals of lengths
a,b a+b< 1 in [0, 1], one has aδ +bδ = 1 if 0<m δ(E)< ∞.
This makes it easy to guess the dimension of self-similar fra ctals. The
self-aﬃne case is much harder; cf. the M curve, of dimension 1 + 2 log 2/ log 3.
Signed measures. To make the space of all measure into a linear space,
we must allow measures to assume negative values.
A ﬁnite signed measure m on a σ-algebra B is a map m : B → [−M,M ],
such that for any sequence of disjoint Bi we have
∑
m(Bi) = m(
⋃
Bi).
Note that the sum above converges absolutely, since the sum o f its positive
terms individually is bounded above by M , and similar for the negative
terms.
A general signed measure is allowed to assume at most one of th e values
±∞, and the sum above is required to converge absolutely when m(⋃ Bi)
is ﬁnite.
A measure is a signed measure assuming no negative values.
For simplicity we will restrict attention to ﬁnite signed measures.
Positive sets. Given a signed measure m, a set P is positive if m(A) ≥ 0
for all A ⊂P .
Theorem 8.1 If m(A)> 0 then there is a positive set P ⊂A with m(P ) ≥
m(A).
Proof. Let λ(A) = inf {m(B) : B ⊂A} ≥ −M . Pick a set of nonpositive
measure, B1 ⊂ A, with m(B1) < λ(A) + 1. By induction construct a set
of nonpositive measure Bn+1 ⊂An =A − (B1 ∪... ∪Bn) with m(Bn+1)<
λ(An) − 1/n. Then ∑ |m(Bi)|< ∞, so m(Bi) → 0 and thus λ(Ai) → 0.
Letting P =⋂ An, we have P ⊂An so λ(P ) ≥ limλ(An) = 0. Thus P
is a positive set, and m(P ) ≥m(A) since m(Bi) ≤ 0 for each i.
80

The Hahn Decomposition.
Theorem 8.2 Given a ﬁnite signed measure m on X, there is a partition
of X into a pair A,B of disjoint sets, one positive and one negative.
Proof. Let p = sup m(P ) over all positive sets P ⊂ X. We claim p is
achieved for some positive set A. Indeed, we can choose positive sets Ai
with m(Ai) →p and just let A =⋃ Ai.
Now let B =X −A. Then B contains a set of positive measure, then it
contains a positive set P of positive measure; then m(A ∪P )> m(A) = p,
contrary to the deﬁnition of p. Thus B is negative.
Jordan decomposition.
Theorem 8.3 Let m be a signed measure on X. Then m can be uniquely
expressed as m = p −n, where p and n are mutually singular (positive)
measures.
Here mutually singular means p and n are supported on disjoint sets.
Proof. Letp =m|A andn = −m|B, whereA∪B is the Hahn decomposition
ofX (unique up to null sets). This shows p andn of the required form exist.
Now assuming only that m =p−n, where p andn are mutually singular,
we can assert that p(A) = sup {m(B) : B ⊂ A}, and thus p is unique.
Similarly n is unique.
Absolute continuity . Given a pair of measures µ and λ, we say µ ≪ λ,
or µ is absolutely continuous with respect to λ, if λ(E) = 0 = ⇒ µ (E) = 0.
For example, X = [0, 1] and µ (E) =
∫
Ef (x)dx for f ∈ L1[0, 1], then
µ ≪λ if λ is Lebesgue measure on [0 , 1]. In fact the converse holds.
The Radon-Nikodym theorem.
Theorem 8.4 If µ ≪λ then there is an f ≥ 0 such that
µ (E) =
∫
E
f (x)dλ.
Proof. If f has the form above, then the Hahn decomposition of µ is
{f < 0} ∪ {f > 0}. Similarly the Hahn decomposition of µ −αλ is {f <
α} ∪ {f >α}.
So for each rational number α, let Pα be the positive set for the Hahn
decomposition of µ −αλ. Then the Pα are nested (up to null sets). Deﬁne
f (x) = sup {α : x ∈Pα}, and set ν(A) =
∫
Afdλ .
81

Now notice that for α<β , for any A contained in
{α ≤f ≤β} =Pα −Pβ,
we have ν(A) and µ (A) both contained in [ α,β ]λ(A). Chopping [0 , ∞] into
intervals of length 1/n, and pulling these intervals back to a decomposition
Ei of a set E, we ﬁnd that µ (E) is sandwiched between the upper and lower
approximations to
∫
Efdλ . Therefore equality holds.
Derivatives. The function f deﬁned above is commonly written f =
dµ/dλ , so we have
µ = dµ
dλdλ.
Absolutely continuous/singular decomposition. Given a pair of mea-
sures µ,ν on (X, B), we can naturally decompose ν =νa +νs with νa ≪µ
and νs ⊥µ .
To do this, just let π = µ +ν, and write dµ = fdπ , ν = gdπ (using
Radon-Nikodym derivatives). Then we have ν = g/fdµ on the set where
f > 0, and ν ⊥ µ on the set where f = 0. These two restrictions give the
desired decomposition of ν.
Baire measures. We now pass to the consideration of measures µ on
a compact Hausdorﬀ space X compatible with the topology. The natural
domain of such a measure is not the Borel sets but the Baire sets K, the
smallest σ-algebra such that all f ∈C(X) are measurable.
A Baire measure is a measure m on (X, K).
What’s the distinction? In R, all closed sets are G′
δs, so their preimages
under functions are also Gδ. Thus K is generated by the closed Gδ’s in X,
rather than all closed sets.
In a compact metric space, the Borel and Baire sets coincide.
Regular contents. It is useful to have a characterization of those functions
λ : F → X deﬁned on the closed (hence compact) sets F in X such that λ
extends to a Baire measure. Here it is:
Theorem 8.5 Letλ(K) ≥ 0 be deﬁned for all compact Gδ sets K ⊂X and
satisfy:
(i) λ(K1) ≤λ(K2) if K1 ⊂K2;
(ii)λ(K1 ∪K2) = λ(K1) +λ(K2) ifK1 and K2 are disjoint; and
λ(K) = inf λ(
U ) over all open sets U ⊃K.
82

Then there is a unique Baire measure µ such that µ (K) = λ(K) for all
compactK.
Such a λ is called a regular content on X.
Sketch of the proof. Givenλ, we can deﬁne a set-function (inner measure)
by
µ∗(E) = sup
K⊂E
λ(K),
deﬁne a set A to be measurable if µ∗(A ∩E) +µ∗((X −A) ∩E) = µ∗(E)) for
allE, show that the measurable sets contain the Baire sets and tha tµ =µ∗
is a Baire measure extending λ.
Positive functionals.
Theorem 8.6 Let φ : C(X) → R be a linear map such that f ≥ 0 = ⇒
φ(f ) ≥ 0. Then there is a unique Baire measure µ on X such that
φ(f ) =
∫
X
fdµ.
Proof. Let us say f ∈C(X) is admissible for a compact Gδ set K if f ≥ 0
and f ≥ 1 on K. Deﬁne λ(K) as inf φ(f ) over all admissible f .
We claim λ is a regular content. (i) is clear; as for (ii), λ(K1 ∪K2) ≤
λ(K1) +λ(K2) is obvious. For the reverse inequality, use normality of X to
get g1 +g2 = 1, g1g2 = 0, 0 ≤gi ≤ 1 with gi = 1 on Ki. Then given f for
K1 ∪K2 we get competitors fi =gif for Ki with φ(f1) +φ(f2) ≤φ(f ), so
λ(K1 ∪K2) ≤λ(K1 ∪K2).
Finally for (iii): choose f admissible forK withφ(f ) ≤λ(K)+ǫ. Let U =
{f >1−ǫ}. Then f/ (1−ǫ) is admissible for
U , so λ(U ) ≤ (λ(K)+ǫ)/(1−ǫ),
and therefore λ(K) = inf λ(U ).
Thusλ extends to a Baire measure µ . To show that integration against µ
reproduces φ, ﬁrst note that for any K there exist admissible fn decreasing
toχK pointwise, with fn eventually vanishing on any compact set L disjoint
from K (since K is a Gδ), and for which
∫
fn and φ(fn) both converge to
µ (K) = λ(K).
Thus we can approximate χK by a continuous function f with φ(f ) ≈∫
f . Now approximate g from above by sums of indicator functions of com-
pact sets, and approximate these from above by admissible fu nctions f ;
then we get φ(g) ≤φ(f ) ≈
∫
gdµ . Doing the same from below we ﬁnd that
φ(g) =
∫
gdµ .
83

Theorem 8.7 (Riesz) LetX be a compact Hausdorﬀ space. Then the dual
of C(X) is the space of Baire measures on X, with µ = |µ |(X).
Proof. One shows a linear functional can be decomposed into a positi ve
and negative part, each of which is represented by a measure.
Corollary. The space of measures on a compact Hausdorﬀ space is com-
pact in the weak* topology.
F unctions of bounded variation and signed measures on [ a, b]. We
can now address afresh the theory of diﬀerentiation of f : [a,b ] → R. To
each signed measure µ we can associate the function f (x) = µ [a,x ]. This
function is continuous from above and of bounded variation. Conversely, to
each such f one can attach a measure df. The weak topology is the one
where fn →f iﬀ fn(x) →f (x) for each x such that f is continuous at x.
Now signed measure correspond to functions in BV; absolutel y continu-
ous measures, to absolutely continuous functions; f′(x) is dµ a/dλ; disconti-
nuities correspond to atoms; singular measure correspond t o f with f′ = 0
a.e.
Compactness. As an alternative proof of compactness: consider a se-
quence of monotone increasing functions f : [a,b ] → [0, 1] with f (b) = 1.
(I.e. a sequence of probability measures.) Passing to a subs equence, we can
get fn(x) to converge for all rational x ∈ [a,b ]. Then there is a monotone
limit g, which can be arranged to be right-continuous, such that fn → g
away from its discontinuities.
Integration. Given a function f of bounded variation and g ∈ C∞[a,b ],
we can deﬁne
I =
∫ b
a
g(x)df(x) = −
∫ b
a
f (x)g′(x)dx.
Now breaking [a,b ] up into intervals [ ai,ai+1] we get the approximation:
I = −
∑
f (ai)(g(ai+1) −g(ai))
= +
∑
(f (ai+1) −f (ai))g(ai) = O(‖f ‖BV ‖g‖∞).
Thus integration against df gives a bounded linear functional on a dense
subset of C[a,b ], so it extends uniquely to a measure.
This idea is the beginnings of the theory of distributions.
Sample application: Let f :X →X be a homeomorphism. Then there
exists a probability measure µ on X such that µ (A) = µ (f (A)).
84

Proof. Take any probability measure — such as a point mass δ; average it
over the ﬁrst n iterates of f ; and take a weak* limit.
Haar measure. If G is a compact Hausdorﬀ topological group, for each
open neighborhood U of the origin we deﬁne λU (K) = [ K : U ]/[G : U ]
where [E : U ] is the minimal number of left translates gU needed to cover
E. Then as U shrinks towards the identity, we can extract some (Banach)
limit of λU , which turns out to be a content λ. In this way we obtain a
left-invariant measure on G.
References
[Con] J. H. Conway. On Numbers and Games . Academic Press, 1976.
[Me] R. Ma˜ n´ e. Ergodic Theory and Diﬀerentiable Dynamics . Springer-
Verlag, 1987.
[Ox] J. C. Oxtoby. Measure and Category . Springer-Verlag, 1980.
85

