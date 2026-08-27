CONTENTS Kari Eiﬂer
Solutions to Texas A&M’s Real Analysis Qual Courses
Kari Eiﬂer
August 29, 2019
These are the solutions to the majority of the available past real qualifying exams for Texas A&M.
Incomplete/non-existent solutions are marked in red. If you ﬁnd any errors/typos or have solutions
to the unsolved questions, please email me at keifer@math.tamu.edu.
Contents
1 August 2019 3
2 January 2019 5
3 August 2018 10
4 January 2018 17
5 August 2017 25
6 January 2017 32
7 August 2016 40
8 January 2016 46
9 August 2015 53
10 January 2015 59
1

CONTENTS Kari Eiﬂer
11 August 2014 65
12 January 2014 71
13 August 2013 75
14 January 2013 81
15 August 2012 87
16 January 2012 92
17 August 2011 97
2

1 AUGUST 2019 Kari Eiﬂer
1 August 2019
Problem 1. Let (X,M,µ ) be a measure space and f a measurable non-negative function on X.
Deﬁne ν :M→ [0,∞] by
ν(E) =
∫
E
fdµ.
(a) Prove that ν is a measure
Proof. Indeed, it’s clear that ν(E) =
∫
Efdµ ≥ 0 for all E since f is assumed to be non-
negative. It’s equally clear that ν(∅) =
∫
∅fdµ = 0.
We are only left to prove countable additivity. Take a countable collection {Ei} of pairwise dis-
joint sets inM, so we see for ﬁnitely many
ν
(
∪N
k=1Ek
)
=
∫
∪N
k=1Ek
fdµ =
∫
χ∪N
k=1Ekfdµ =
N∑
k=1
∫
χEkfdµ =
N∑
k=1
∫
Ek
fdµ =
N∑
k=1
ν(Ek).
By the monotone convergence theorem (the ﬁnite sums of characteristic functions form an in-
creasing sequence that converges to the inﬁnite sum pointwise), then ν is countably additive.
Hence, ν is a measure.
(b) Prove that g∈L1(ν) if and only if gf∈L1(µ) and in that case
∫
Xgdν =
∫
Xgfdµ .
Proof. First we show that ν ≪ µ. Indeed, if µ(E) = 0 then choose an increasing sequence of
simple functions fn such that fn→ f. Then by monotone convergence theorem and the deﬁni-
tion of integral for simple functions, we have
ν(E) =
∫
E
fdµ =
∫
E
(limfn)dµ = lim
∫
E
fndµ = 0.
Then we may apply Radon-Nikodym theorem to see that f = dν
dµ and see that g ∈ L1(ν) if
and only if
∫
X|g|dν < ∞ which is equivalent to
∫
X|g|fdµ =
∫
X|g|dν
dµdµ <∞. Since f is
non-negative, this is equivalent to having
∫
X|gf|dµ <∞. Radon-Nikodym also tells us that∫
Xgdν =
∫
Xgfdµ .
Problem 2. (a) State Fatou’s lemma
Proof. Forfn∈L+ then
∫
lim inffn≤ lim inf
∫
fn
(b) State the dominated convergence theorem
3

1 AUGUST 2019 Kari Eiﬂer
Proof. Let g,gn∈ L+ be measurable,|fn|≤ gn µ-a.e., fn→ f and gn→ f µ-a.e. with
∫
gn→∫
g <∞. Then
∫
fn→
∫
f. Moreover,
∫
|f−fn|→ 0.
(c) Let fn,gn,hn,f,g,h be measurable functions on Rn satisfying fn ≤ gn ≤ hn, fn → f a.e.,
gn→ g a.e., and hn→ h a.e. Suppose moreover that f,h ∈ L1 and
∫
fn→
∫
f,
∫
hn→
∫
h.
Prove that g∈L1 and
∫
gn→
∫
g.
Proof. here
Problem 3. Let{Ak}∞
k=1 be measurable subsets of a measure space and deﬁne Bm to be the set of
all points which are contained in at least m of the sets {Ak}∞
k=1. Prove that Bm is measurable and
µ(Bm)≤ 1
m
∞∑
k=1
µ(Ak).
Proof. Let C ={F⊆ N||F| =m} which is a countable inﬁnite set. Then we may express
Bm =
⋃
F∈C
⋂
i∈F
Ai.
Therefore, each Bm is measurable.
here
Problem 4. LetE be a subset of R which is not Lebesgue measurable. Prove that there exists an
η >0 such that for any two Lebesgue measurable sets A,B satisfying A⊆E⊆B one has λ(B\A)>
η, where λ denotes Lebesgue measure.
Proof. here
Problem 5. Let{Ak}∞
k=1 be Lebesgue measurable sets in Rn equipped with Lebesgue measureλ.
(a) Prove that if Ak⊆Ak+1 for all k then λ(∪∞
k=1Ak) = limk→∞λ(Ak)
Proof. We will assume that λ is subadditive, so λ(∪∞
1 Ak)≤∑∞
1 λ(Ak).Then by setting Ak =∅,
we have
λ (∪∞
1 Ak) =
∞∑
1
λ(Aj\Aj−1) = lim
n→∞
n∑
1
λ(Aj\Aj−1) = lim
n→∞
λ(An).
(b) Prove that if Ak+1⊆Ak for all k and λ(A1)<∞ then λ(∩∞
k=1Ak) = limk→∞λ(Ak)
Proof. Let Bj = A1\Aj so B1 ⊂ B2 ⊂ ... , and λ(A1) = λ(Bj) + λ(Aj), and∪∞
1 Bj =
E1\(∩∞
1 Aj). Then by part (a), we have
4

2 JANUARY 2019 Kari Eiﬂer
λ(A1) =λ
(∞⋂
1
Aj
)
+ lim
j→∞
λ(Bj) =λ (∩∞
1 Aj) + lim
j→∞
(λ(A1)−λ(Aj)).
Since λ(A1)<∞, we may subtract it from both sides to yield the desired result.
(c) Give an example showing that without assuming λ(A1) <∞ the conclusion of the previous part
does not hold.
Proof. Consider Aj = [j,∞) so that for each j, λ(Aj) =∞ but∩∞
1 Aj =∅ so λ(∩∞
1 Aj) = 0.
Problem 6. LetX and Y be Banach spaces. Show that the linear space X⊕Y is a Banach space
under the norm ‖(x,y )‖ =‖x‖ +‖y‖. Also determine (with justiﬁcation) the dual (X⊕Y )∗.
Proof. here
Problem 7. For each n∈ N deﬁne on 𝓁∞ the linear functional ϕn(x) = n−1∑n
k=1x(k). Let ϕ be
the weak* cluster point of the sequence {ϕn}. Show that ϕ does not belong to the image of 𝓁1 under
the canonical embedding 𝓁1 ↪→ (𝓁∞)∗.
Proof. here
Problem 8. LetT : X → Y be a surjective linear map between Banach spaces and suppose that
there is a λ> 0 such that‖Tx‖≥ λ‖x‖ for all x∈X. Show that T is bounded.
Proof. here
Problem 9. LetX be a compact metric space and µ a regular Borel measure on X. Let f : X→
[0,∞) be a continuous function and for each n∈ N set fn(x) = f(x)1/n for all x∈ X. Show that∫
fndµ→µ(suppf) as n→∞ where suppf ={x∈X|f(x)> 0}.
Proof. here
Problem 10. LetX be a compact metric space and let x∈ X. Suppose that the point mass δx is
the weak* limit of a sequence of atomless Radon measures on X (viewing all of these measures as
elements of C(X)∗). Show that every neighborhood of x is uncountable.
Proof. here
2 January 2019
Problem 1. True or false (prove or give a counter example)
(a) Let E⊆ R be a Borel set, then {(x,y )∈ R2|x−y∈E} is a Borel set in R2.
5

2 JANUARY 2019 Kari Eiﬂer
Proof. TRUE.
Deﬁne f(x,y ) =x−y : R2→ R. This is continuous. Let
A :={S⊆ R|f−1(S) is a Borel set of R2}
ThenA is a σ-algebra (easy to check). If S is open, then f−1(S) is open in R2, thus Borel. So
{open sets}⊆A and so the Borel algebra is a subset of A. In particular, E∈A .
(b) Let E⊆Q := [0, 1]× [0, 1]. Assume that for every x,y∈ [0, 1] the sets Ex ={y∈ [0, 1]| (x,y )∈
E} and Ey ={x∈ [0, 1]| (x,y )∈E} are Borel. Then E is Borel.
Proof. FALSE.
Consider a non-Borel set A ⊂ [0, 1]. Set E = {(x,x ) | x ∈ A}. Then each Ey and Ex is a
singleton which is Borel, but E is not.
(c) A function f : R→ R is called Lipschitz if there exits a M > 0 such that∀x,y ∈ R,|f(x)−
f(y)|≤ M|x−y|. If A⊆ R is Lebesgue measureable and f is Lipschitz then f(A) is Lebesgue
measurable.
Proof. TRUE.
Since A is Lebesgue measurable, then we can write A = (∪jKj)∪N where each Kj is a compact
set and N has Lebesgue measure zero. Then f(A) = (∪jf(Kj))∪f(N). It’s clear that each
f(Kj) is Lebesgue measurable, since f is Lipschitz. We are only left to see that f(N) is also
Lebesgue measurable.
Indeed, for every ϵ > 0 we can write N ⊆ ∪kBk where each Bk is a ball of radius rk and∑
km(Bk) < ϵ. But then by Lipschitz continuity, f(Bk) is contained in a ball of radius Mrk
where M is the Lipschitz constant of f. Thus, m(f(Bk)) ≤ Mm(Bk) so that m(f(N)) ≤
M∑
km(Bk) < Mϵ. Let ϵ→ 0 so f(N) must have outer measure equal to zero, hence it is a
null set.
Problem 2. Let (X,F,µ ) be a measure space. is it true that for every measurable essentially bounded
f : X→ R we have limp→∞‖f‖p =‖f‖∞? Give an answer both in the case that µ is ﬁnite and the
case that µ is σ-ﬁnite.
Proof. If µ is ﬁnite: By H¨ older, we know that‖f‖p≤‖f‖q when p≤q. Also, ‖f‖p≤‖f‖∞ for all p.
Therefore,‖f‖p↗≤‖f‖∞ and so limp‖f‖p≤‖f‖∞.
On the other hand, for every ϵ> 0, let E ={x||f(x)|>‖f‖∞−ϵ} and 0 <µ (E)≤ 1 since‖f‖∞ =
esssup|f(x)|<∞. Then ‖f‖p
p≥
∫
E|f|p >
(
‖f‖∞−ϵ
)p
µ(E). Take p→∞ so limp‖f‖p≥‖f‖∞−ϵ,
implying limp‖f‖p≥‖f‖∞.
If µ is σ-ﬁnite: No, this is not true. Consider f(x) = 1
x on [1,∞). Then limp‖f‖p = 0 ⁄=‖f‖∞ =
1.
Problem 3. Letf : R→ R Lebesgue integrable and for n∈ N deﬁne
gn(x) =n
∫
(x,x+1/n)
fdλ.
6

2 JANUARY 2019 Kari Eiﬂer
(a) Prove that limn→∞gn =f λ-a.e.
Proof. This is Lebesgue Diﬀerentiation Theorem, with Er = (x,x +r).
(b) Prove that for every n∈ N,
∫
R|gn|dλ≤
∫
R|f|dλ.
Proof. here!
(c) Prove limn→∞
∫
R|gn|dλ =
∫
R|f|dλ.
Proof. Apply dominated convergence theorem with parts (a) and (b).
Problem 4. Letf∈L1((0, 1]2,λ 2) such that
∫
(0,x]×(0,y]fdλ 2 = 0 for every x,y ∈ (0, 1]. Prove that
f = 0 λ2-a.e.
Proof. First note that
(a,b )× (c,d ) =
⋃
n
((0,b− 1/n]× (0,d− 1/n])\ ((0,a ]× (0, 1]∪ (0, 1]× (0,b ])
And since all open rectangles generate all Borel sets in R2, then we have that for every Borel set
B⊆ R2,
∫
Bfdλ 2 = 0.
Since every Lebesgue set A is of the form A =B∪N where B is a Borel measurable set and N is a
set of measure zero. Hence,
∫
Afdλ 2 = 0 for any Lebesgue measurable set A.
Now consider A+ ={x| f(x) > 0} and A− ={x| f(x) < 0}. Since both are measurable, then∫
A+fdλ 2 = 0 =
∫
A−fdλ 2. Hence, f = 0 λ2-a.e.
Problem 5. Letλ be the Lebesgue measure on R. Let E ⊆ R be Lebesgue measurable such that
0<λ (E)<∞. Prove that for all 0≤γ <1 there exists an open interval I⊆ R such that
λ(E∩I)≥γλ(I).
Proof. Choose an open set O⊃ E such that λ(E)≥ γλ(O). We can write O =∪iOI for open and
disjoint intervalsOi. Hence
E =E∩O =E∩
⋃
i
Oi =
⋃
i
(E∩Oi)
Suppose to the contrary that λ(E∩Oi)<γλ (Oi) for all i. Then
λ(E) =λ
(⋃
(E∩Oi)
)
=
∑
i
λ(E∩Oi)<γ
∑
i
λ(Oi) =γλ(O)
which is a contradiction with the fact that λ(E)≥γλ(O). Hence, it must be that for some k, λ(E∩
Ok)≥γλ(Ok).
7

2 JANUARY 2019 Kari Eiﬂer
Problem 6. LetX be a compact metrizable space and {µn} a sequence of Borel measures on X
with µn(X) = 1 for every n. Consider the linear map ϕ : C(X) → 𝓁∞(N) deﬁned by ϕ(f) =(∫
Xfdµn
)
n. What conditions on the sequence {µn} are equivalent to ϕ being an isometry? Provide
justiﬁcation.
Proof. We would require, for all f∈C(X)
sup
x∈X
|f(x)| =‖f‖∞ =
‖‖‖‖
(∫
fdµn
)‖‖‖‖
∞
= sup
n
⏐⏐⏐⏐
∫
fdµn
⏐⏐⏐⏐
here
Problem 7. LetX be a compact metric space and {fn} a sequence in C(X). Prove that {fn} con-
verges weakly in C(X) if and only if it converges pointwise and supn‖fn‖<∞. Also, give an exam-
ple of an X and a sequence{fn} in C(X) which converges weakly but not uniformly.
Proof. By considering fn−f, we may assume without loss of generality that fn converges to 0.
⇒) We know C[0, 1]∗ =M[0, 1]. Then fn → 0 weakly implies
∫
fndµ→ 0 for all µ∈ M[0, 1].
Choose µ =δt so
∫
fndδt =fn(t)→ 0 ∀t∈ [0, 1]
(this follows from the fact that weak convergence implies uniformly bounded). Consider
χ :C[0, 1]→C[0, 1]∗∗ =M[0, 1]∗
χ(fn)(µ) =µ(fn)
Since µ(fn)→ 0 then χ(fn)(µ)→ 0 for all µ∈M [0, 1]. Since convergent sequences are bounded,
then supn|χ(fn)(µ)|≤ M.
By the uniform boundedness theorem, sup n‖χ(fn)‖<∞. By isometry,‖fn‖ =‖χ(fn)‖ so supn‖fn‖<
∞.
⇐) By Dominated Convergence Theorem, fn→ 0 in L1(µ). So therefore, |
∫
fndµ|≤
∫
|fn|d|µ|→ 0.
So fn→ 0 weakly.
Example: TakeX = [0, 1] and consider the functions
fn(x) =



nx x ∈ [0, 1/n]
−nx + 2 x∈ (1/n, 2/n]
0 x∈ (2/n, 1]
Then they converge to 0 weakly, but not strongly.
8

2 JANUARY 2019 Kari Eiﬂer
Problem 8. LetX be a Banach space. Show that if X∗∗ is separable then so is X. Also, give an
example, with justiﬁcation, to show that the converse is false.
Proof. We will show the weaker result that states that if the dual X∗ is separable, then so is X.
Let X∗ be separable. Consider the unit sphere SX∗ ={ϕ∈ X∗|‖ ϕ‖ = 1}. Then SX∗ is separable
and so we can let {ϕn} be a countable dense subset of SX∗.
For eachn∈ N, choose xn∈ N with‖xn‖ = 1 such that|ϕn(xn)|> 1/2. Let D = span{x1,x 2,... }.
Then D is countable; ex. we can consider the following set countable and dense subset of D:
⋃
n∈N



n∑
j=1
(aj +ibj)xj|aj,bj∈ Q



We want to show that D = X. Suppose it were not, then there ewould be some ϕ ∈ SX∗ with
ϕ|D = 0. Since {ϕn} is dense, there exists some n such that‖ϕ−ϕn‖< 1/4. Therefore,
1
2≤|ϕn(xn)| =|ϕn(xn)−ϕ(xn)|≤‖ ϕn−ϕ‖‖xn‖< 1
4.
This is a contradiction and hence, D =X.
example. c0 is separable, but 𝓁∞ =c∗∗
0 is not separable.
Problem 9. (a) Let X be a compact metrizable space. Describe the dual of C(X) according to the
Riesz representation theorem.
Proof. For everyϕ∈ C(X)∗, there exists a unique ﬁnite regular signed measure µ on the Borel
subsets of X such that
ϕ(f) =
∫
X
fdµ
for each f∈C(X). Moreover,‖ϕ‖ =|µ|(X).
(b) Consider the spaces X ={1/n| n∈ N}∪{ 0} and Y = [0, 1] with the topologies inherited from
R. Prove that there does not exist a bijective bounded linear map from C(X) to C(Y ).
Proof. By contradiction. Suppose there exists a bijective bounded linear map T : C(X) →
C(Y ). Then by the Open Mapping Theorem (or more accurately, the corollary that is the Bounded
Inverse Theorem), then T−1 is a bijective bounded linear map from C(Y ) to C(X). This says
that the two spaces are isomorphic.
Therefore, the duals of these two spaces should also be isomorphic, C(X)∗∼=C(Y )∗. But by the
Riesz-representation theorem, here!
Problem 10. LetX be a Banach space and Y a subspace of X. Show that ‖x +Y‖ = inf{‖x +y‖|
y∈Y} deﬁnes a norm on X/Y if and only if Y is closed.
9

3 AUGUST 2018 Kari Eiﬂer
Proof.⇐) Suppose Y is closed. It’s easy to see ‖x +Y‖ is well-deﬁned and a semi-norm. Suppose
‖x +Y‖ = 0. Then there exists yn∈ Y such that‖x−yn‖→ 0. Since Y is closed, then x∈ Y .
Therefore, x +Y =Y = 0 +Y which is the zero vector in X/Y .
⇒) Suppose this is a norm. Take any convergent sequence yn in Y with yn→y′. Then inf y∈Y‖y−
y′‖≤‖ yn−y′‖→ 0 and so‖y′ +Y‖ = 0. Since this is a norm, then y′ +Y = 0 + Y = Y and so
y′∈Y . Hence Y must be closed.
3 August 2018
(Solve any 10 of the following 12 problems)
Problem 1. Letµ and ν be positive measures on the same measurable space with ν ﬁnite and abso-
lutely continuous with respect to µ. Show that for every ϵ> 0, there exists δ >0 such that µ(E)<δ
implies ν(E)<ϵ .
Proof. Suppose for contradiction that ∃ϵ >0 such that µ(E) < δthen ν(E)≥ ϵ for all δ > 0 adn
for some E. We’ll construct the set En to be some set with µ(En) < 2−n. Let Fk =∪∞
n=kEn so
µ(Fk)< 2−k+1.
Let F =∩∞
k=1Fk so µ(F ) = 0. Since ν≪µ, then ν(F ) = 0.
However, sinceFk is a decreasing sequence, we have
ν(F ) = lim
n
ν (∩n
k=1Fk) = lim
n
ν(Fn)≥ϵ.
Contradiction!
Problem 2. Letµ be a positive measure. Suppose that (fn)∞
n=1 is a Cauchy sequence in L1(µ).
Show that for all ϵ> 0 there exists a δ >0 such that µ(E)<δ implies
∀n≥ 1
⏐⏐⏐⏐
∫
E
fndµ
⏐⏐⏐⏐<ϵ.
You may use without proof the result of problem #1.
Proof. Let ϵ > 0. Since {fn} is Cauchy in L1(µ), there exists f ∈ L1(mu) such that fn → f in
L1(µ) as n→∞ , since L1(µ) is a Banach space.
Deﬁne ν(E) :=
⏐⏐∫
Efdµ
⏐⏐.
Then by Problem 1, there exists some δ >0 such that ν(E) =
⏐⏐∫
Efdµ
⏐⏐<ϵ/ 2 when µ(E)<δ , thenf
or large enough n (sayn≥N) we have
⏐⏐⏐⏐
∫
E
fndµ
⏐⏐⏐⏐ =
⏐⏐⏐⏐
∫
E
(fn−f +f)dµ
⏐⏐⏐⏐≤
⏐⏐⏐⏐
∫
E
fn−fdµ
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫
E
fdµ
⏐⏐⏐⏐< ϵ
2 + ϵ
2 =ϵ
10

3 AUGUST 2018 Kari Eiﬂer
for µ(E)<δ .
For eachi,N , we can ﬁnd δi such that
⏐⏐∫
Efidµ
⏐⏐ < ϵ when µ(E) < δi. By the same reasoning as
above, if we set ˜δ = min{δ1,...,δ N−1,δ} then
⏐⏐∫
Efndµ
⏐⏐<ϵ wheneverµ(E)< ˜δ for all n∈ N.
Problem 3. Letf : [0, 1]→ [0,∞) be Lebesgue measurable. For n∈ N deﬁne
gn = fn
1 +fn.
(a) Explain why
∫ 1
0 gn(t)dt exists and is ﬁnite for all n.
Proof. Since gn = fn
1+fn≤ 1 for all n, then
∫ 1
0 gndx≤
∫ 1
0 1dx = 1 for all n.
(b) Prove that limn
∫ 1
0 gn(t)dt exists and ﬁnd an expression for it. Make sure to state which major
theorems you are using in your proof.
Proof. Deﬁne E1 ={x| 0≤f(x)< 1}, E2 ={x|f(x) = 1} and E3 ={x|f(x)> 1}.
If x∈E1 then gn(x) = fn(x)
1+fn(x)→ 0. So by DCT, lim n
∫
E1
gndx =
∫
E1
0dx = 0.
If x∈E2 then gn(x) = fn(x)
1+fn(x) = 1
2 for all n and so
lim
n
∫
E2
gndx =
∫
E2
1
2dx = 1
2m(E2).
If x∈E3 then gn(x) = fn(x)
1+fn(x)→ 1 and so by DCT,
lim
n
∫
E3
gndx =
∫
E3
dx =m(E3).
Thus,
lim
n
∫ 1
0
gndx = lim
n
∫
E1
gndx +
∫
E2
gndx +
∫
E3
gndx = 1
2m(E2) +m(E3).
Problem 4. Consider C([0, 1]) endowed with its usual uniform norm. Prove or disprove that there
is a bounded linear functional ϕ on C([0, 1]) such that for all polynomials p, we have ϕ(p) = p′(0),
wherep′ is the derivative of p.
Proof. DISPROVE.
Consider pn = 1− (x− 1)n so then‖pn‖∞ = 1 but p′
n(0) = n→∞ . If such a ϕ existed, then
n =|ϕ(pn)| =‖ϕ(pn)‖≤ c‖pn‖ which cannot happen.
Problem 5. (a) Deﬁne the product topology on the Cartesian product Πα∈AXα of a family of topo-
logical spaces (Xα)α∈A
Proof. here!
11

3 AUGUST 2018 Kari Eiﬂer
(b) State Tychonoﬀ’s compactness theorem.
Proof. If{Xα} is a family of compact topological spaces then Π α∈AXα is compact.
(c) State and prove the Banach-Alaoglu theorem (Hint: Use Tychonoﬀ’s theorem)
Proof. Thoerem: Let X be a normed vector space. The closed unit ball {f∈ X∗|‖ f‖≤ 1} is
compact in the weak*-topology.
For allx∈X, let Dx :={ξ||ξ|≤‖ x‖}⊆ C. Then Dx is compact, and by Tychonoﬀ’s theorem,
D := Πx∈XDx is comapct. Deﬁne complex function ϕ with ϕ(x)≤‖x‖.
We deﬁneB∗⊆ D to consist of linear functions of D. We claim B∗ is closed. Indeed, let {fα}
be a net in B∗ that converges to f. Then
f(ax +by) = limfα(ax +by) = lim(afα(x) +bfα(y)) =a limfα(x) +b limfα(y) =af(x) +bf(y).
So f ∈ B∗. Since closed subsets of comapct spaces are compact, then B∗ is compact in the
weak*-topology.
Problem 6. Let (X,d ) be a compact metric space.
(a) Show that X has a countable, dense set {xn|n∈ N}.
Proof. If X is countable, we are done. So suppose X is uncountable. Since X is compact, for
all n∈ N, X can be covered by ﬁnitely many balls of radius 1
n. For each n, choose such a ﬁnite
cover with balls centered at the points {xn
j}Nn
j=1. Then the collection E :=∪n{xn
j}Nn
j=1 is count-
able.
Forx∈X, for all n∈ N, x∈B(1/n,xn
j ) for some xn
j∈E so E is dense.
(b) Let fn :X→ [0,∞) befn(x) =d(x,xn). Show that if x,y∈X and fn(x) =fn(y) for all n∈ N,
then x =y.
Proof. We then have that d(x,xn) = d(y,xn) for all n. We know for all m∈ N we can ﬁnd xm
such that d(x,xm) < 1/m so d(y,xm) < 1/m. So we can ﬁnd a sequence {xm}∞
m=1 such that
xm→ x and xm→ y as m→∞ . But X is a metric space and thus Hausdorﬀ, so limits are
unique. Therefore, x =y.
Problem 7. LetK > 0 and let LipK be the set of functions f : R→ R satisfying|f(x)−f(y)|≤
K|x−y|.
(a) Prove that
d(f1,f 2) =
∞∑
j=0
2−j sup
x∈[−j,j]
|f1(x)−f2(x)|
deﬁnes a metric on LipK
12

3 AUGUST 2018 Kari Eiﬂer
Proof. First, suppose d(f1,f 2) = 0. Then ∑∞
j=0 2−j supx∈[−j,j]|f1(x)−f2(x)| = 0 so supx∈[−j,j]|f1(x)−
f2(x)| = 0 for all j. Thus, f1(x) =f2(x) for all x.
It’s trivial to see that d(f1,f 2) =d(f2,f 1).
Finally,we’ll show the triangle inequality. This again follows directly: |f1(x)−f2(x)|≤| f1(x)−
f3(x)| +|f3(x)− f2(x)| for all x. Taking sup on both sodies and multiplying by 2 −j we get
d(f1,f 2)≤d(f1,f 3) +d(f1,f 2).
(b) Prove that LipK is a complete metric space
Proof. Suppose (fn) is a Cauchy sequence in Lip K. Then for every ϵ > 0 there exists N ∈ N
such that d(f1,fm) = ∑∞
j=1 2−j supx∈[−j,j]|f1(x)−f2(x)| < ϵ. Then for each j and x∈ [−j,j ]
we have|fn(x)−fm(x)|<ϵ′.
Thus,{fn(ξ)} is Cauchy sequence on [−j,j ] for each ξ. But we can ﬁnd f(x) such that fn(x)→
f(x).
We want to show that d(fn,f )→ 0. Since fn(x)→ f(x), then for all ϵ > 0 we can ﬁnd some
N∈ N such that for all n≥N,|fn(x)−f(x)|<ϵ . THen
d(fn,f ) =
∞∑
j=1
2−j sup
x∈[−j,j]
|fn(x)−f(x)|<
∞∑
j=1
2−jϵ =ϵ
So d(fn,f )→ 0. To see f∈ LipK,
|f(x)−f(y)| =
⏐⏐⏐lim
n
fn(x)− lim
n
fn(y)
⏐⏐⏐ = lim
n
|fn(x)−fn(y)|≤ K lim
n
|x−y| =K|x−y|.
Problem 8. LetX,Y be topological spaces. A map f : X → Y is said to be proper if for every
compact subset K⊆Y , the inverse image f−1(K) is compact.
(a) Suppose X is a compact space and Y is Hausdorﬀ. Prove that every continuous map f :X→Y
is proper.
Proof. Let K⊆ Y be compact. Since Y is Hausdorﬀ, then K is closed. Since f is continuous,
and Y\K is open in Y then f−1(Y\K) is open in X. So f−1(K) = X\f−1(Y\K) is closed.
Since X is compact, f−1(K) is compact.
(b) Give an example of a continuous map which is not proper.
Proof. Consider the constant function 1 : R→ R which sends x↦→ 1. So 1−1({1}) = R.
(c) Suppose f : Rm→ Rn is a proper continuous map. Prove that f is a closed map, ie. f(C) is
closed in Rn whenever C is a closed subset of Rm.
Proof. Let{yn} ⊆f(C) with yn → y. Deﬁne A = {y}∪{ yn} (compact). Then f−1(A) is
compact, so there exists xn∈f−1(A)∩C such that f(xn) =yn. Find a convergent subsequence
xnk with xnk→x for x∈C∩f−1(A). By continuity of f, we have f(x) =y.
13

3 AUGUST 2018 Kari Eiﬂer
Problem 9. Consider the interval [−π,π ] equipped with Lebesgue measureµ. For n∈ Z, consider
the functions fn∈C([−π,π ]) given by fn(t) =eint.
(a) Prove that spanC{fn|n∈ Z} is dense in the space
A :={f∈C([−π,π ])|f(−π) =f(π)}
with respect to the uniform norm.
Proof. LetB = spanC{fn}⊆A⊆ C([−π,π ]). Note that B separates points and is closed under
complex conjugates. By Stone-Weierstrass, B is dense in C[−π,π ] hence also dense in B.
(b) Show that
{
fn√
2π|n∈ Z
}
is an orthonormal basis for the Hilbert space L2([−π,π ],µ ).
Proof. Note that
‖⟨fn,fn⟩‖2 =
⏐⏐⏐⏐
∫ π
−π
einte−intdt
⏐⏐⏐⏐
1/2
=
√
2π
Forn⁄=m,
⟨fn,fm⟩ =
∫ π
−π
einte−intdt = ei(n−m)t
n−m |π
−π = 0.
So they are orthonormal.
(c) Is the following statement true or false?:
“For every f∈A , f = limN→∞ 1
2π
∑N
n=−N⟨f,fn⟩fn with respect to the uniform norm.”
Give a brief explanation why or why not.
Proof. TRUE.
Claim: ∑∞
−∞⟨f,fn⟩fn exists. By Pythagorean theorem,
‖‖∑∞
−∞⟨f,fn⟩fn
‖‖ =∑∞
−∞‖⟨f,fn⟩fn‖.
By Bessel’s inequality,∑∞
−∞⟨f,fn⟩fn is bounded so it exists.
Let g :=f−∑∞
−∞⟨f,fn⟩fn so that
⟨g,fm⟩ =⟨f,fm⟩−
∞∑
−∞
⟨⟨f,fn⟩fn,fm⟩ =⟨f,fm⟩−⟨ f,fm⟩ = 0.
By completeness of Hilbert spaces, g = 0. So f =∑∞
−∞⟨f,fn⟩fn.
Problem 10. Let (X,‖·‖ ) be a normed linear space and let (X∗,‖·‖ X∗) denote its dual Banach
space of bounded linear functionals. Recall that ‖ϕ‖X∗ = sup‖x‖=1|ϕ(x)| for ϕ∈X∗
(a) Prove that for each x∈X, there exits ϕ∈X∗ with‖ϕ‖X∗ = 1 and‖x‖ =ϕ(x).
14

3 AUGUST 2018 Kari Eiﬂer
Proof. We will prove the more general case: let M be closed and x∈ X\M. Then there exists
φ∈X∗ such that φ(x) = infy∈M‖x−y‖ and‖φ‖ = 1 and φ|M = 0.
Restrict to the space M + Cx and deﬁne φ(y +λx) =λ infy∈M‖x−y‖. Then φ(x) = infy∈M‖x−
y‖ and φ|M = 0.
Since φ(x) =‖x‖, then 1 = ‖x‖
‖x‖ = |φ(x)|
‖x‖ ≤‖φ‖ and
|φ(y +λx)|≤| φ(y)| +|φ(λx)| = 0 +|λ||φ(x)| =|λ| inf
y∈M
‖x−y‖≤| λ|‖x−λ−1y‖ =‖λx +y‖.
Therefore,‖φ‖ = supy+λx
|φ(y+λx)|
‖λx+y‖ ≤ 1 so‖φ‖ = 1.
Finally, if we deﬁne p(x) =‖x‖ for x∈ M + Cx then by Hahn-Banach, φ can be extended to ψ
on all x with ψ|M +Cx =φ. To prove the result, set M ={0}.
(b) Prove that the linear map ι :X→X∗∗ given by
ι(x)(ϕ) =ϕ(x) x∈X,ϕ∈X∗
is an isometry.
Proof. Fix x∈X, so
‖ι(x)‖ =|ι(x)(φ)|
‖φ‖X∗
= sup
φ∈X∗
|φ(x)|
‖φ‖X∗
By part (a), there exists φ ∈ X∗ such that‖φ‖X∗ = 1 and φ(x) = ‖x‖, which implies that
‖x‖≤‖ ι(x)‖X∗.
Also, for any φ∈X∗,|φ(x)|≤‖ φ‖X∗‖x‖ and so
‖ι(x)‖≤ sup
φ∈X∗
|φ(x)|
‖φ‖X∗
≤‖φ‖‖x‖
‖φ‖ =‖x‖.
So‖ι(x)‖ =‖x‖ and so ι is an isometry.
(c) A Banach space X is called reﬂexive if ι(X) =X∗∗. Prove that the Banach space
𝓁1 ={f∈ N→ C|‖f‖1 =
∑
k
|f(k)|<∞}.
is not reﬂexive.
Hint: Consider a weak-∗ cluster point of the sequence (ι(fn))n∈N⊆ (𝓁1)∗∗, where fn∈ 𝓁2 is the
unit vector
fn(k) =
{
1/n k ≤n
0 k>n
Proof. here!
15

3 AUGUST 2018 Kari Eiﬂer
Problem 11. Let (gn)n∈N⊆ C([0, 1]) be a sequence of non-negative continuous functions. Assume
that for each k = 0, 1, 2,... the limit
lim
n→∞
∫ 1
0
xkgn(x)dx exists.
Prove that there exists a unique ﬁnite positive Radom measure µ on [0, 1] such that
∫ 1
0
f(x)dµ(x) = lim
n→∞
∫ 1
0
f(x)gn(x)dx for all f∈C([0, 1]).
Proof. Deﬁne M := limn
∫ 1
0 gn(x)dx <∞. Let A = span{xk|k∈ N}. For each φ∈A , by linearity,
limn
∫ 1
0 φ(x)gn(x)dx exists.
By Stone-Weierstrass,A is dense in C[0, 1], so for every f∈C[0, 1], limn
∫ 1
0 f(x)gn(x)dx.
Next, let φ : C[0, 1]→ C be deﬁned by φ(f) = lim
∫ 1
0 f(x)gn(x)dx. Linearity is obvious. Moreover,
for every f∈C[0, 1],
|φ(f)| =
⏐⏐⏐⏐lim
n
∫ 1
0
fgn(x)dx
⏐⏐⏐⏐≤ lim
n
∫ 1
0
|f(x)||gn(x)|dx≤‖f‖n lim
n
∫ 1
0
gn(x)dx =M‖f‖∞
Hence, φ is a bounded linear functional on C[0, 1].
By Riesz-Representation, there exists a positive Radon measure µ such taht
lim
n
∫ 1
0
f(x)gn(x)dx =φ(f) =
∫ 1
0
f(x)dµ(x) ∀f∈C[0, 1].
Problem 12. LetX be a locally compact Hausdorﬀ space equipped with a Radon probability mea-
sureµ. Let E⊆L2(X,µ ) be a closed linear subspace and assume that E is contained in C0(X). The
goal of this problem is to prove that dim(E)<∞ by justifying the following steps:
(a) There exists a constant 1≤K <∞ such that
‖f‖2≤‖f‖u≤K‖f‖2 for all f∈E,
where‖·‖ u denotes the uniform norm. Hint: us the closed graph theorem for one of the inequal-
ities.
(b) For each x∈X, there exists a unique gx∈E such that‖gx‖2≤K and
f(x) =⟨f,gx⟩ for all f∈E.
(c) Let (fi)i∈I be any orthonormal basis for E. Then
16

4 JANUARY 2018 Kari Eiﬂer
∑
i∈I
|fi(x)|2 =‖gx‖2
2≤K 2 for all x∈X.
(d) dim(E) =|I|≤ K 2.
Proof. See January 2017, Problem #5 for a solution to a similar question.
4 January 2018
Problem 1. SupposeU1,U 2,... are open subsets of [0, 1]. In each case, either prove the statement
or disprove it.
(a) If λ
(
∩∞
n=1Un) = 0 then for some n≥ 1, we have λ(Un) < 1, where λ is Lebesgue measure and
Un is the closure of Un in the usual topology on [0, 1].
Proof. FALSE. Letrm be an enumeration of the rationals on [0 , 1], and set an,m = 1/2n+m. Set
Un :=∪m(rm−an,m,rm +an,m)
These are open since they are a union of open intervals. Moreover, since Q⊆ Un then λ(Un) =
λ([0, 1]) = 1. But by upper continuity of the Lebesgue measure, then
λ (∩Un) = lim
m
λ (∪(rn−an,m,rn +an,m)) = 0.
(b) If ∩∞
n=1Un =∅, then for some n≥ 1, the set [0, 1]\Un contains a non-empty open interval.
Proof. TRUE. Recall that the Baire Category Theorem states that under these assumptions, if
eachUn is dense in [0, 1] then∩∞
n=1Un is also dense in [0, 1]. Then since we have that ∩∞
n=1Un
is not dense, then there must be some n such that [0, 1]\Un is not dense. This precisely means
that Un contains a non-empty open interval.
Problem 2. LetX be a separable compact metric space and show that C(X) is separable.
Proof. Remark: If X is a compact metric space, then X is separable. So the separable assumption
is superﬂuous.
Suppose d is the metric on X and (xn) is a dense countable subset of X. For each n ∈ N, de-
ﬁne the functional fn byfn(x) := d(x,xn). Then each fn is a continuous functional. Consider
F ={1,f 1,f 2,... } and consider the subalgebra generated by the rational span of F , call it Q[F ]
(this is still countable, we can consider the span, then cosider the set where two elements of it are
multiplied together, then the set where three elements are multiplied together, etc). This is count-
able and dense in A := R[F ]. so it is suﬃcient to show that A is dense inC(X).
17

4 JANUARY 2018 Kari Eiﬂer
We will attempt to use the Stone Weierstrass Theorem:
By deﬁnition, R[F ] contains the constant function 1. We are left to show it separates points. Take
two points x⁄= y in X. Since {xn} is dense, then there must exist some m such that d(x,xm)≤
1
3d(x,y )⁄= 0. If d(y,xm) =d(x,xm) then
d(x,y )≤d(x,xm) +d(y,xm) = 2d(x,xm)≤ 2
3d(x,y ).
This cannot be true under our assumption d(x,y )⁄= 0. So then fm(y) = d(y,xm)⁄= d(x,xm) =
fm(x). So fm separates x and y.
Therefore, by Stone-Weierstrass,A is dense inC(X). But Q[F ] is countable and dense in A, so
thereforeC(X) is separable.
Problem 3. Letf : [0, 1]→ R be a bounded Lebesgue measurable function such that
∫ 1
0
f(t)entdt = 0
for every n∈{ 0, 1, 2,... }. Prove that f(t) = 0 for almost every t∈ [0, 1].
Proof. Let f(t) = 0 on t = 0, 1. Using Stone-Weierstrass to show we can pass to the case
∫ 1
0 f(t)g(t) =
0 for all g∈C [0, 1].
By a standard density argument, we may pass to the case where g is a step function. We claim that
f = 0 a.e.
Assume not. WLOG there exists some E ={x∈ [0, 1]| f(x) > 0} with m(E) > 0 (else consider
−f).
Since f is bounded, then E∞ :={x∈ [1, 2]| f(x) = ∞} is a null set. Deﬁne En :={x∈ [0, 1]|
1/n<f (x)<n}. We can write E = (⋃
nEn)∪E∞. So there exists some N such that m(EN) =a>
0.
We can write A as a ﬁnite disjoint union of open intervals, A =⊔m
i=1Ii, such that m(EN∆A) < ϵ
and A⊆EN.
Put g =∑m
i=1χIi, then
∫ 2
1 g(x)f(x) =
∫
EN
f(x)dx. Since
⏐⏐⏐⏐
∫
EN
f(x)−
∫
A
f(x)
⏐⏐⏐⏐≤Nm(EN∆A)<Nϵ
If we choose ϵ small enough, we see the contradiction since
∫ 1
0 g(x)f(x)> 0.
Problem 4. (a) Prove that every compact subset of a Hausdorﬀ space is closed.
Proof. Let A be a compact subset of the Hausdorﬀ space X. To show A is closed, we’ll show
Ac =X\A is open. Take x∈X\A. Then for every y∈A, there are disjoint sets Uy and Vy with
x∈Vy and y∈Uy.
18

4 JANUARY 2018 Kari Eiﬂer
The collection of open sets {Uy | y ∈ A} forms an open cover of A. Since A is compact, this
open cover has a ﬁnite subcover, Uy1,Uy2,...,U yn. Let
U :=∪n
i=1Uyi V :=∩n
i=1Vyi
Since each Uyi and Vyi are disjoint, then U and V are disjoint. Also, A⊆U and x∈V .
Thus, for every point x∈X\A we have found an open set V containingx which is disjoint from
A. So X\A is open and A is closed.
(b) Let f : X→ Y be a bijective continuous function between topological spaces. Suppose that X is
compact and Y is Hausdorﬀ and prove that f is a homeomorphism.
Proof. Let g =f−1. We need to show that g is continuous.
For everyV ⊆ X, we have g−1(V ) = f(V ). We want to show that if V is closed in X then
g−1(V ) is closed in Y .
Suppose V is closed in X. Since X is compact, V is compact by part (a). So f(V ) is compact
since the continuous image of a compact space is compact.
Since Y is Hausdorﬀ, f(V ) is closed by the fact that a compact subspace of Hausdorﬀ space is
closed. But f(V ) = g−1(V ) so g−1(V ) is closed. So g is continuous and f is a homeomorphism.
(c) Prove or disprove that if X is a dense subset of a topological space Y and if X is Hausdorﬀ in
the relative topology, then Y is also Hausdorﬀ.
Proof. FALSE. ConsiderY ={a,b} with discrete topology τ ={∅,{a,b}}. Let X ={a} with
relative topology τX ={∅,{a}}.
Then it’s easy to see X is dense in Y (since every open set containing an element of Y has nonempty
intersection with X, trivially). Since X has only a single element, it’s Hausdorﬀ in the relative
topology trivially. But Y is not Hausdorﬀ.
Problem 5. Prove that the following limit exists and compute its value:
lim
n→∞
∫ n
0
( n∑
k=0
(−1)kx2k
(2k)!
)
e−2xdx.
Proof. Solution from Sheagan John
Let us ﬁrst note an important simpliﬁcation of the integrand, by considering the Taylor series ex-
pansion of cosx around a neighbourhood of 0.
cosx =
∞∑
k=0
(−1)k
(2k)! x2k
Letting f(x) := (cos x)e−2x and fk(x) := e−2x (−1)k
(2k)!x2k then it’s clear that {fk} is a convergent
sequence which converges to f(x).
19

4 JANUARY 2018 Kari Eiﬂer
Now, since| cosx|≤ 1 we further have that for some positive constant c< 2
|fn(x)|≤ c|f(x)| =c| cosxe−2x| =c| cosx|e−2x≤ce−2x
Since g(x) =ce−2x is integrable on the positive half line
∫ ∞
0
ce−2x dx = −c
2 e−2x
⏐⏐⏐⏐
∞
0
= c
2
the dominated convergence theorem can be applied to the original Lebesgue integral limit, with
fn−→f, and with g as the dominating function.
lim
n−→∞
∫ n
0
(∞∑
k=0
(−1)k
(2k)! x2k
)
e−2x dx = lim
n−→∞
∫ n
0
fn(x)dx =
∫ ∞
0
f(x)dx =
∫ ∞
0
e−2x cosxdx
Recall that the Laplace transform of cos x is
∫∞
0 e−st cosatdt =L{cosax}(s) = s
s2+a2 . Therefore,
the last integral is equal to 2
22+1 = 2/5.
Problem 6. LetX and Y be Banach spaces (over C)
(a) A linear map T : X→ Y is called adjointable if T∗f∈ X∗ for every f∈ Y∗. Prove that T is
adjointable if and only if T∈B (X,Y ).
Proof.⇐) if T∈B (X,Y ) then by deﬁnition, for every f∈Y∗, we have T∗f∈X∗
⇒) Suppose T∗f ∈ X∗ for every f ∈ Y∗. We will use the Closed Graph Theorem. Suppose
xn→x in X and that Txn→y in Y . Then since T∗f∈X∗ for every f∈Y∗ we can apply this
to the convergence to see that
f(Txn) = (T∗f)(xn)→ (T∗f)(x) =f(Tx ) ∀f∈Y∗
By the Hahn-Banach theorem, Y∗ separates points in Y so therefore, Txn→ Tx . Uniqueness
of limits implies Tx = y and so the graph of T is closed. By the Closed Graph Theorem, T is
bounded.
(b) Suppose a bounded linear functional ψ : X∗→ C is weak*- continuous. Show (from the deﬁni-
tions) that there exists x∈X such that ψ(φ) =φ(x).
Proof. Deﬁne the functional
evx :X∗→ C
f↦→f(x)
20

4 JANUARY 2018 Kari Eiﬂer
We want to show that every bounded, linear, weak*-continuous functional ψ :X∗→ C is of this
form.
Indeed, since ψ is weak*-continuous, then it is weak* continuous at 0. Thus, the set {f∈ X∗|
|ψ(f)| < 1} is weak* open and must containa neighborhood of 0. By deﬁnition of weak* topol-
ogy, there must exist x1,...,x n∈X such that
V (x1,...,x n) :={f∈X∗ | |f(xi)|≤ 1,i = 1,...,n }⊆{ f∈X∗||ψ(f)|< 1}.
Then we will next show that ∩n
i=1 ker(evxi)⊆ ker(ψ).
Indeed, let f∈ ker(evxi) so|f(xi)| = 0 for all i = 1,...,n . Take ϵ >0 and conser g = 1
ϵf, so
|g(xi)| = 1
ϵ|f(xi)| = 0 for all i = 1,...,n . In particular, g∈ V (x1,...,x n) and so then we have
if|ψ(g)|< 1 then|ψ(f)|<ϵ . But ϵ is arbitrary so ψ(f) = 0, i.e. f∈ ker(ψ).
Now recall the linear algebra trick that says if for linear functionals ker( T )⊆ ker(S) then S is a
scalar multiple of T . In this case, we get that ψ is a linear combination of the ev xi, i.e. is of the
form evx where x is a linear combination of the xi’s.
Moreover, because the weak* topology is Hausdorﬀ, x is necessarily unique.
(c) Let S ∈B (Y∗,X∗). Prove that S is weak*-weak*-continuous if and only if S = T∗ for some
T∈B (X,Y ).
Proof.⇐) If S = T∗ then if fα → f is a weak* convergent net in Y∗ then for any y ∈ Y ,
fα(y)→f(y). Therefore,
(Sfα−Sf )| {z }
∈X∗
(x) = (Tx ) (fα−f)| {z }
→0
→ 0.
So S is weak*-weak* continuous.
⇒) Suppose S : Y∗ → X∗ is weak*-weak* continuous. Then the evaluation function on x,
evx(S) is weak* continuous on Y∗ (where evx(S) :Y∗→ C, (evx(S))(f) = (Sf )(x)).
By part (b), we know that ev x(S) is of the form ev T (x) for some unique T (x)∈Y . Since T (x) is
uniquely determined, it follows that T is linear.
We will now check that T is continuous by the closed graph theorem: if xn→ x adn Txn→ y
in norm then for each φ∈Y∗ we have
⟨φ,y⟩ = lim⟨φ,Tx n⟩ = lim⟨Sφ,xn⟩ =⟨Sφ,x⟩ =⟨φ,Tx⟩.
And so y =Tx as desired. So T is bounded and therefore, S =T∗ is bounded as well.
Problem 7. Let (fn)∞
n=1 be a sequence of functions fn : [0, 1]→ R.
NOTE: I think we also require continuous....
(a) What does it mean for {fn|n≥ 1} to be equicontinuous?
Proof.{fn|n≥ 1} is said to be equicontinuous if for every ϵ> 0, there exists a δ >0 such that
for all x,y∈ [0, 1], if|x−y|<δ then|f(x)−f(y)|<ϵ .
21

4 JANUARY 2018 Kari Eiﬂer
(b) Suppose that for every n, fn is diﬀerentiable and |f′
n(t)|≤ 1 for all t. Prove that {fn|n≥ 1} is
equicontinuous.
Proof. Since|f′
n(t)|≤ 1 for all t, then for all n, we have by the mean value theorem that
|fn(x)−fn(y)|
|x−y| ≤ 1.
Hence, for any ﬁxed ϵ> 0, setting δ =ϵ and for|x−y|<δ then
|fn(x)−fn(y)|≤| x−y|<δ =ϵ.
(c) Suppose the hypothesis of (b) holds and assume in addition that |fn(0)|≤ 1 for every n≥ 1.
Prove that there exists a continuous function f : [0, 1]→ R and a subsequence (fn(k))∞
k=1 con-
verging uniformly to f.
Proof. This is essentially the Arzela-Ascoli Theorem. Since |fn(0)| ≤ 1 for all n and since
|f′
n(t)|≤ 1 for all t, then|fn(t)|≤ 2 for all t∈ [0, 1] and for all n. That is, {fn} is uniformly
bounded. It’s also equicontinuous by part (b). Therefore, Arzela-Ascoli theorem states that
there is a subsequence {fnk} which converges uniformly. Let f be the limit, and we ﬁnish by
recalling that the uniform convergence of continuous functions is also continuous.
Note: it might be good to know the Arzela-Ascoli Theorem.
(d) Show by example that the limit function f need not be diﬀerentiable.
Proof. Takefn(x) =
√
x2 + 1/n so fn(0) = 1√n≤ 1 for all n and so{fn} is uniformly bounded.
Next, we can see that f′
n(x) = x√
x2+1/n
so that for x∈ [0, 1] we have|f′
n(x)|≤
√
n
n+1 ≤ 1 as
desired.
However, it’s also clear that the limit must be f =|x| which is not diﬀerentiable.
Problem 8. LetH be a complex Hilbert space. Given a non-empty set E ⊆ Hand x ∈ H, put
dist(x,E ) = inf{‖x−y‖| y∈E} and E⊥ ={x∈H|⟨ x,y⟩ = 0∀y∈E}.
(a) Let H0⊆H be a closed subspace and x∈H . Prove that there exists x0∈H 0 such that‖x−
x0‖ = dist(x,H0).
Proof. Let δ = dist(x,H0). Then there exists a sequence ( yn)∈H 0 such that δn :=‖x−yn‖→
δ. We will show that (yn) is Cauchy. Indeed,
0≤‖yn−ym‖2 =−‖yn +ym− 2x‖2 + 2(‖yn−x‖2 +‖ym−x‖2)≤− 4δ2 + 2(δ2
n +δ2
m)→ 0.
where we use the fact that
22

4 JANUARY 2018 Kari Eiﬂer
‖yn +ym− 2x‖2 = 4
‖‖‖‖‖‖‖‖
yn +ym
2| {z }
∈H0
−x
‖‖‖‖‖‖‖‖
2
≤ 4δ.
Thus, (yn) is a Cauchy sequence and so because we are in a Hilbert space, ( yn) converges to
some point x0∈H . Since H0 is closed and yn∈H 0 for all n then we get that x0∈H 0. Finally,
‖x−x0‖ = lim‖x−yn‖ = limδn =δ.
Exercise: it can be shown if H0 is convex, then the choice of x0 is unique!
(b) With x and x0 as above, prove that x−x0 is orthogonal to H0.
Proof. Let y∈H 0 be an arbitrary vector with ‖y‖ = 1, set α :=⟨x−x0,y⟩. Then since α⟨x−
x0,y⟩ =αα =|α|2 and α⟨y,x−x0⟩ =αα =|α|2, we have
‖x−(x0 +αy)‖2 =‖x−x0−αy‖2 =‖x−x0‖2−α⟨x−x0,y⟩−α⟨y,x−x0⟩+|α|2 =‖x−x0‖2−|α|2.
So since x0 +αy∈H 0 then‖x−x0−αy‖≥‖ x−x0‖. Hence α = 0.
Therefore, for any nonzero y∈H 0 we can write
⟨x−x0,y⟩ =‖y‖⟨x−x0,y/‖y‖⟩ =‖y‖0 = 0.
So⟨x−x0,y⟩ = 0 for all y∈H 0 so x−x0⊥H 0.
(c) Prove that H =H0⊕H⊥
0 (the algebraic direct sum)
Proof. This follows immediately from parts (a) and (b). Take some arbitrary x∈H . We can
ﬁnd the appropriate x0 as above, so x =x0 + (x−x0)∈H 0⊕H⊥
0 .
The fact that it is a direct sum follows from the fact that H0∩H⊥
0 ={0}.
(d) Let E⊆H be non-empty. Prove that (E⊥)⊥ =E if and only if E is a closed subspace.
Proof. If E is closed, then the above parts (a),(b), and (c) apply and prove that ( Eperp)⊥ =
E. To see the converse, we will instead show that ( E⊥)⊥ = E. The desired result will then
immediately follow.
Since E⊆ E then E
⊥
⊆ E⊥ and therefore, (E⊥)⊥⊆ (E
⊥
)⊥. Since E is closed, then (E
⊥
)⊥ =
E so (E⊥)⊥⊆E.
Conversely, sinceE⊥ is closed for every E (independent of whether E is closed or not) then
(E⊥)⊥ is closed and so since E ⊆ (E⊥)⊥, then by the monotonicity of topological closure we
have that E⊆ (E⊥)⊥ = (E⊥)⊥.
Therefore, (E⊥)⊥ =E.
Problem 9. LetV be a vector space over R or C. Recall that a Hamel basis for V is a linearly in-
dependent subset of V whose linear span equals V .
23

4 JANUARY 2018 Kari Eiﬂer
(a) Let S⊆ V and suppose the linear span of S equalsV . Show that V has a Hamel basis that is a
subset of S.
Proof. Choose a Hamel basis B of S. Then it is easy to check that B is a Hamel basis of V .
(b) Suppose V has an inﬁnite Hamel basis and show that all hamel bases of V have the same cardi-
nality.
Proof. Suppose that{vi}i∈I and{uj}j∈J are two inﬁnite bases for V . For each i∈ I, then vi is
in the linear span of {uj}j∈J. Therefore, there exists a ﬁnite subset Ji⊆J such that vi is in the
linear span of the vectors {uj}j∈Ji. Therefore, V = span({vi}i∈I)⊆ span{uj}j∈∪Ji. Since no
proper subset of{uj}j∈J can span V , it follows that J =∪i∈IJi. Therefore |J|≤| I|.
A symmetric argument shows that |I|≤| J|.
Problem 10. Suppose (X,M,ρ ) is a ﬁnite measure space and A⊆M is an algebra of sets with a
ﬁnitely additive complex measure µ :A→ C such that|µ(E)|≤ ρ(E) for all E∈A . Show that there
exists a complex measure ν :M→ C whose restriction to A is µ and such that |ν(E)|≤ ρ(E) for all
E∈M .
Hint: you may want to consider the subspace V ⊆L1(ρ) that is spanned by the set of characteristic
functions χE for E∈A , and a certain linear functional on V .
Proof. Solution from Minh Kha.
For each subalgebraU ofM, we deﬁne SU to be the set of all simple functions of the form ∑n
i=1ciχEi
where ci∈ R, Ei∈U . Then SA is a vector subspace of SM.
Now deﬁne p :SM→ R such that
p(f) = sup
{ n∑
i=1
|ci|ρ(Ei) | f =
n∑
i=1
ciχEi,Ei∩Ej =∅∀ i⁄=j,Ei∈M,ci∈ R
}
∀f∈SM
It’s not diﬃcult to check that p satisﬁes p(f +g)≤ p(f) +p(g) for all f,g ∈ SM and p(tf) = tp(f)
for all t∈ R+,f ∈ SM. Thus, p is a seminorm and is just an extension of the total variation of the
measure p when you apply to the function f = 1.
Deﬁne a linear map T :SA→ R deﬁned by
T (f) =
∫
X
fdµ ∀f∈SA
This is linear because of the ﬁnite additive property of µ. Then |T (f)|≤ p(f) for all f ∈ SA. By
Hahn-Banach, we get a linear extension of T on SM, which we denote by ~T . Moreover, this exten-
sion ~T :SM→ R satisﬁes|~T (f)|≤ p(f) for all f∈SM.
Now, we deﬁne a ﬁnite additive measure ν onM by letting ν(E) = ~T (χE) for all E∈M . Thus,
ν|A =µ and|ν(E)|≤ p(E) for all E∈M .
24

5 AUGUST 2017 Kari Eiﬂer
To check the countably additive property of ν, consider any countable collection of disjoint measur-
able subsets Ei∈M and so χ∪iEi =∑
iχEi. Thus, ν(∪iEi) = ∑
iν(Ei) since the series ∑
i~T (Ei)
converges (use|~T (f)|≤ p(f) for all f∈SM and properties of the measure p).
For the complex case, repeat the trick by proving the complex version of the Hahn-Banach theorem
from the real version.
5 August 2017
Problem 1. Let (Ω,A,µ ) be a measure space and let {fn} be a sequence of measurable functions
on X. Prove, directly from the deﬁnition of convergence almost everywhere, that if ∑
nµ[|fn| >
1/n] <∞, then the sequence {fn} converges almost everywhere to zero. Deduce that every sequence
of measurable functions that converges in measure to zero has a subsequence that converges almost
everywhere to zero.
Proof. Let E ={x∈ Ω| limn|fn(x)| = 0}. We want µ(Ec) = 0. Let
M =
∞⋂
m=1
∞⋃
n=m
{x∈ Ω||fn(x)|> 1/n}
Since
µ
( ∞⋃
n=m
{
x∈ Ω||fn(x)|> 1
n
})
≤
∞∑
n=m
µ
({
x∈ Ω||fn(x)|> 1
n
})
→ 0.
Therefore, µ(M) = 0 and
Mc =
∞⋃
m=1
∞⋂
n=m
{x∈ Ω||fn(x)|≤ 1/n}.
Note: fn(x)→ 0 if and only if ∀ϵ> 0,∃N s.t.∀n>N ,|fn(x)|<ϵ .
So for any x∈Mc choose 1/N <ϵ s.t.∀n>N we have|fn(x)|≤ 1
n < 1
N <ϵ .
Therefore Mc⊆ E, so Ec⊆ M, implying µ(Ec) = 0. So then {fn} converges almost everywhere to
zero.
Step 2: We will show that if fn→ 0 in measure, then there exists a subsequence that converges to 0
pointwise almost everywhere.
Suppose for every ϵ> 0, µ({x||fn(x)|≥ ϵ})→ 0. Choose a subsequence {fnk} such that if
Ej ={x||fnj(x)−fnj+1(x)|> 2−j}
25

5 AUGUST 2017 Kari Eiﬂer
satisﬁes µ(Ej)< 2−j. Let Fk =∪∞
j=kEj so µ(Fk)≤∑∞
j=k 2−j≤ 21−k. Let F =∩kFk so µ(F ) = 0.
Forx /∈Fk and for i≥j≥k then
|fni(x)−fnj(x)|≤
i−1∑
𝓁=j
|fn𝓁(x)−fn𝓁+1(x)|≤
i−1∑
𝓁=j
2𝓁≤ 2−j→ 0 as k→∞.
So fnk is pointwise Cauchy on x /∈F , so let
f(x) =
{
limfnk(x) x /∈F
0 otherwise
So fnk→ 0 almost everywhere and fn→f in measure since
µ({x||fn(x)−f(x)|≥ ϵ})≤µ({x||fn(x)−fn𝓁(x)|≥ ϵ/2})| {z }
→0
+µ({x||fn𝓁(x)−f(x)|≥ ϵ})| {z }
→0
and
µ({x||f(x)|≥ ϵ})≤µ({x||f(x)−fn(x)|≥ ϵ/2}| {z }
→0
+µ({x||fn(x)|≥ ϵ/2})| {z }
→0
so f = 0 almost everywhere. Thus, {fnk} converges to 0 almost everywhere.
Problem 2. Show that there is a sequence of nonnegative functions {fn} in L1(R) such that‖fn‖L1(R)→
0, but for any x∈ R, lim supnfn(x) =∞.
Proof. We will explicitely construct such a sequence. Consider the following pattern:
To cover [−1, 1] let
f1 =
√
1χ[−1,0], f 2 =
√
1χ[0,1].
so that‖f1‖L1(R) = 1 =‖f2‖L1(R). To cover [−2, 2], next let
f3 =
√
2χ[−2,−1.5], f 4 =
√
2χ[−1.5−1] ...,f 10 =
√
2χ[1.5,2]
so then 1√
2 =‖f3‖L1(R) =‖f4‖L1(R) =... =‖f10‖L1(R). Next, we cover [−3, 3] so that
f11 =
√
3χ[−3,−2.666],...f 28 =
√
3χ[2.666,3]
so that 1√
3 = ‖f11‖L1(R) = ... = ‖f28‖L1(R). If we continue in this fashion, we get the desired
functions.
26

5 AUGUST 2017 Kari Eiﬂer
Explicitely, forn =∑N−1
i=1 2i2 +k = 1
3(N− 1)(N)(2N− 1) +k where N∈ N, 0≤k <2N 2, then we
set
fn =
√
Nχ[−N +k/N,−N +(k+1)/N]
so that‖fn‖L1(R) = 1√
N but for every x∈ R, it’s clear that lim supnfn(x) =∞.
Problem 3. Construct a sequence of nonnegative Lebesgue measurable functions {fn} on [0, 1] such
that
(a) fn→ 0 almost everywhere, and
(b) for any interval [a,b ]⊆ [0, 1],
lim
n→∞
∫ b
a
fn(x)dx =b−a.
Proof. Claim. For anyf≥ 0 that is continuous on [0, 1], n
∫
[x,x+ 1
n2 ](f(y)−f(x))dy =o( 1
n).
For anyϵ> 0,∃N∈N such that 0 <x< 1
N then f(x)−f(0)<ε . Hence for n>N , n
∫
[0, 1
n2 ](f(x)−
f(0))<nϵ 1
n2 .
A clear extension to this is that
∫
[x,x+ 1
n ](f(y)−f(x))dy =o( 1
n).
Let fn(x) := ∑n−1
k=0nχ[k
n,k
n + 1
n2 ], and let ε,N be as above. Clearly fn is measurable and satisﬁes (a)
above. To prove (b), observe that, for n>N ,
Ik :=
⏐⏐⏐⏐⏐
∫ k+1
n
k
n
nfχ [k
n,k
n + 1
n2 ]−f
⏐⏐⏐⏐⏐
=
⏐⏐⏐⏐⏐n
∫ k
n + 1
n2
k
n
f−
∫ k+1
n
k
n
f
⏐⏐⏐⏐⏐
=o
( 1
n
)
.
Hence|
∫
(ffn−f)|≤ ∑n−1
k=0Ik =o(1).
This holds for all f∈C ([0, 1]), so in particular, it will hold for f =χ[a,b].
Problem 4. In this problem the measure is Lebesgue measure on [0, 1]. The norm on L∞[0, 1] is
the essential supremum norm, which for a continuous function is the same as the supremum norm.
(a) Prove or disprove that L∞[0, 1] is separable in the norm topology.
Proof. L∞[0, 1] is not separable in the norm topology. Consider the collection of functions fr =
χ[−r,r] for real 1≥ r >0. Since there are uncountably many such r and since‖fr−fr′‖∞ = 1
for any r⁄=r′, it’s impossible to have a countable subset of L∞[0, 1] that is dense in it.
27

5 AUGUST 2017 Kari Eiﬂer
(b) Recall that L∞[0, 1] = ( L1[0, 1])∗. What is the weak* closure in L∞[0, 1] of the unit ball of
C[0, 1]? Prove your assertion.
Proof. More general claim: ForX an inﬁnite dimensional Banach space, SX∗
w∗
=BX∗.
We know for any x1,x 2,...,x n∈ X, there exists some x∗
0⁄= 0 such that x∗
0(xi) = 0. Indeed,
if this were not true then otherwise, x∗
0(xi) ⁄= 0 for some i, let ϕ : X∗ → Rn be ϕ(x∗) =
(x∗(x1),...,x ∗(xn)) then ϕ is injective so dim(X∗)≤ dim(Rn) =n. Contradiction, so true.
Now for any x∗∈BX∗, consider it’s neighborhood (open under the w∗-neighborhood)
V =∩n
i=1{y∗∈X∗|| ˆxi(x∗−y∗)| =|x∗(xi)−y∗(xi)|<ϵ}
for each{xi}n
i=1 choose such an x∗
0⁄= 0 from the claim.
Consider the line{x∗ +tx∗
0|t∈ R} in X∗.
Since for any ˆxi,
ˆxi(x∗ +tx∗
0−x∗) =t ˆxi(x∗
0) =tx∗
0(xi) = 0<ϵ.
Then{x∗ +tx∗
0| t∈ R}⊆ V . Since ‖x∗ +tx∗
0‖ is continuous about t, then we can ﬁnd t0 such
that‖x∗ +t0x∗
0‖ = 1⇒ V∩SX∗⁄=∅.
Since any neighborhood of x∗ contains a neighborhood of the form V as above (i.e. these V ’s
are a neighborhood basis) then BX∗⊆SX∗
w∗
.
On the other hand, for any x∗
0 ∈ BX∗, by Hahn-Banach separation Theorem, we know there
exists x∈X and c∈ R such that x∗(x)<c<x ∗
0(x) for all x∗∈BX∗.
Then for all{x∗
n}⊆ BX∗, x∗
n(x)≤c < x∗
0(x). Therefore, x∗
0 isn’t an accumulation point of BX∗
which implies BX∗
w∗
=BX∗. Thus, SX∗
w∗
⊆BX∗
w∗
=BX∗ so BX∗ =SX∗
w∗
.
Problem 5. Prove that if a1,a 2,...,a N are complex numbers, then
(a)
∫ 1
0|∑N
k=1ak exp(2πikt)|pdt≤∑N
k=1|ak|p, if 1≤p≤ 2, and
(b)
∫ 1
0|∑N
k=1ak exp(2πikt)|pdt≥∑N
k=1|ak|p, if 2≤p< ∞.
Proof. Note ﬁrst the following facts:
• {exp(2πikt)} is orthonormal in L2
• For a ﬁnite measure space and p≤q, then
‖f‖p≤µ(X)1/p−1/q‖f‖q
• For a discrete X and p≤q,‖f‖q≤‖f‖p.
28

5 AUGUST 2017 Kari Eiﬂer
Since{exp(wπikt)} is orthonormal, then
‖‖‖‖‖
N∑
k=1
ak exp(2πikt)
‖‖‖‖‖
2
2
=
N∑
k=1
|ak|2.
Then if we let a = (a1,...,a N) and f =∑N
k=1ak exp(2πikt), we see that for 1 ≤p≤ 2, we have
∫ 1
0
⏐⏐⏐⏐⏐
N∑
k=1
ak exp(2πikt)
⏐⏐⏐⏐⏐
p
dt =‖f‖p
p≤‖f‖p
2 =‖a‖p
2≤‖a‖p
p.
To see (b), then similarly for 2 ≤p< ∞,
∫ 1
)
⏐⏐⏐⏐⏐
N∑
k=1
ak exp(2πikt)
⏐⏐⏐⏐⏐
p
dt =‖f‖p
p≥‖f‖p
2 =‖a‖p
2≥‖a‖p
p.
Problem 6. Prove that if X is an inﬁnite dimensional Banach space and X∗ is separable in the
norm topology, then there is a sequence {xn} of norm one vectors in X such that{xn} converges
weakly to zero.
Proof. Suppose{x∗
n} is a dense, countable subset of X∗.
Claim: For everyn, then∩n
k=1 ker(x∗
k) is non-trivial.
Indeed, assume to the contrary that ∩n
k=1 ker(x∗
k) ={0}. Then the map
F :X→ Fn
x↦→ (x∗
1(x),...,x ∗
n(x))
is linear and injective. Let {e1,...,e m} be a basis for F (X). Choose yk∈ F−1({ek}). For all x∈
X, we can write F (x) =∑m
i=1aiei. so F (x−∑aiyi) =∑aiei−∑aiei = 0 so x is in the span and
then X must be ﬁnite dimensional, contradiction! So the claim holds.
Now, choose xn∈ SX∩ (∩n
k=1 ker(xk)). Fix x∗∈ X∗, ϵ >0, so∃N∈ N such that‖x∗−x∗
N‖ < ϵ.
Then for all n≥N, xn∈ ker(x∗
N) so
|x∗(xn)| =|(x∗−x∗
n)(xn)|≤‖ x∗−x∗
N‖<ϵ
So then x∗(xn)→ 0.
Problem 7. Prove or disprove each of the following statements.
(a) If {fn} is a sequence in C[0, 1] that converges weakly, then also {f 2
n} converges weakly.
29

5 AUGUST 2017 Kari Eiﬂer
Proof. YES. Recall that fn∈ C[0, 1] converges weakly if and only if it converges pointwise and
is uniformly bounded.
Suppose fn→f weakly, letM := supn‖fn‖<∞. Then fn→f pointwise so f 2
n→f 2 pointwise
and supn‖f 2
n‖ =M 2 <∞. So f 2
n→f 2 weakly.
(b) If {fn} is a sequence in L2[0, 1] that converges weakly, then also {f 2
n} converges weakly. (Lebesgue
measure on [0, 1])
Proof. NO. Takefn(x) =x−1/3χ[1/n,1](x), so fn→f =x−1/3 in norm but f 2
n(x) =x−2/3χ[1/n,1](x)
but
∫ 1
0
f 2
n(x)x−1/3dx =
∫ 1
0
x−1χ[1/n,1] = log(n)→∞.
Problem 8. Let{fn} be a sequence of continuous functions on R that converges pointwise to a real
valued function f. Prove that for each a<b , the function f is continuous at some point of [a,b ].
Hint: Let En,m,k = [|fn−fm|≤ 1/k].
Proof. Fix some [a,b ]⊆ [0, 1]. By Egoroﬀ’s Theorem, fn→ f uniformly outside a set of measure
b−a
2 . Then f must be continuous outside of this set.
Note: Likely, the question was meant to prove Egoroﬀ’s theorem, see Folland for that proof!
Problem 9. LetX and Y be compact Hausdorﬀ spaces and let S be the set of all real functions on
X×Y of the form h(x,y ) =f(x)g(y) with f in C(X) and g in C(Y ).
Prove or disprove that the linear span of S is dense in C(X×Y ).
Proof. We will use Stone-Weirstrass theorem here. Note that if h1(x,y ) =f1(x)g1(y) and h2(x,y ) =
f2(x)g2(y) are two functions in S, then
(h1h2)(x,y ) =h1(x,y )h2(x,y ) =f1(x)g1(y)f2(x)g2(y) = (f1f2)(x)(g1g2)(y)
where if f1,f 2∈ C(X) then so is f1f2 (and similarly,g1g2∈ C(Y )). So then S is an algebra. Thus,
it follows that span(S) is an algebra as well.
Next, S separates points. Indeed, suppose ( x,y )⁄= (x′,y′) in X×Y . If x⁄= x′ then choose some
f∈ C(X) that separates x and x′. Take g∈ C(Y ) to be the constant function g = 1. Then letting
h(x,y ) := f(x)g(y) = f(x), h separates the two points. If x = x′ then y ⁄= y′ so the same trick
works, setting f = 1∈C(X) and choosing g to separate y and y′, letting h(x,y ) := f(x)g(y) = g(y)
to then separate points.
Therefore, by the Stone-Weierstass theorem, span(S) is dense in C(X×Y ).
Problem 10. LetX be a Hilbert space and assume that {xn} is a sequence in X that converges
weakly to zero. Prove that there is a subsequence {yk} of{xn} such that the sequence ‖N−1∑N
k=1yk‖
converges to zero.
30

5 AUGUST 2017 Kari Eiﬂer
Caution: the same statement is NOT true in all Banach spaces, not even in all reﬂexive Banach
spaces.
Proof. Note: This is the Banach-Saks Theorem
We shall successively choose the nk in the following manner. Beginning for deﬁniteness with n1 = 1,
let n2 be the ﬁrst index such that |⟨f1,fn⟩|≤ 1 (this choice is possible since ⟨f1,fn⟩→ 0 as n→
∞). In general, after having chosen fn1,fn2,...,f nk, we choose nk+1 so that
|⟨fn1,fnk+1⟩|≤ 1
k,..., |⟨fnk,fnk+1⟩|≤ 1
k
Since{fn} converges weakly, then it is bounded and so ‖fn‖ forms a bounded sequence, say ‖fn‖≤
M so by expanding the inner product, we get
‖‖‖‖
fn1 +fn2 +... +fnk
k
‖‖‖‖
2
≤
kM 2 + 2× 1 + 4× 1
2 +... + 2(k− 1)× 1
k−1
k2 < M 2 + 2
k
which then implies
‖‖‖‖
fn1 +fn2 +... +fnk
k
‖‖‖‖
2
→ 0.
Problem 11. LetF⊆C([0, 1]) be a family of continuous functions such that
(a) the derivative f′(t) exists for all t∈ (0, 1) and f∈F .
(b) supf∈F|f(0)|<∞ and supf∈F supt∈(0,1)|f′(t)|<∞.
Prove that F is precompact in the Banach space C([0, 1]) equipped with the norm ‖f‖ = supt∈[0,1]|f(t)|.
Proof. We will use the Arzela-Ascoli Theorem.
To seeF is equicontinuous, ﬁx some ϵ> 0, and let δ = ϵ
M where M = supf∈F supt∈(0,1)|f′(t)|<∞.
Then by the mean value theorem, for any a < b, there exists some c ∈ (a,b ) such that f′(c) =
f (b)−f (a)
b−a so that|f(b)−f(a)|≤| f′(c)||b−a|≤ M|b−a|<Mδ =ϵ.
To seeF is pointwise bounded, we see that for any b∈ [0, 1], then for some c∈ [0,b ], we have f(b) =
f′(c)b +f(0), so that
|f(b)|≤ M + sup
f∈F
|f(0)|.
That is, F is uniformly bounded!
Then by Arzela-Ascoli, F is compact.
31

6 JANUARY 2017 Kari Eiﬂer
Problem 12. Let{xn} be a weakly Cauchy sequence in a normed linear space X. Prove that
(a) xn is norm bounded in X
Proof. Let c denote the space of convergent sequences, and consider the map
T :X∗→c
x∗↦→ (x∗(xn))
By the Uniform Boundedness Principle, T is closed. Then by the closed graph theorem, T is
continuous, so‖T‖<∞. By Hahn-Banach Theorem, ‖T‖ = supn‖xn‖.
(b) There exists x∗∗ in X∗∗ such that xn converges weak* to x∗∗, and‖x∗∗‖≤ lim inf‖xn‖.
Proof. Since (xn) is weakly Cauchy, then for every x∗∈ X∗ the sequence (x∗(xn)) is Cauchy,
hence convergent. We can deﬁne
x∗∗ :X∗∗→ C
x∗↦→ lim
n
x∗(xn)
Uniform boundedness shows that ‖xn‖ is bounded, hence x∗∗ is bounded. Finally,
|x∗∗(x∗)| = lim inf|x∗(xn)|≤ lim inf‖x∗‖‖xn‖ =
(
lim inf‖xn‖
)(
‖x∗‖
)
.
So then‖x∗∗‖≤ lim inf‖xn‖.
6 January 2017
Problem 1. Let (Ω,A,µ ) be a measure space. Prove directly from the deﬁnition of convergence
almost everywhere that if for all n, µ
({
x∈ Ω||fn(x)|> 1
n
})
<n−3/2, then fn→ 0 µ-a.e.
Proof. Let E ={x∈ Ω| limn|fn(x)| = 0}. We want µ(Ec) = 0. Let
M =
∞⋂
m=1
∞⋃
n=m
{x∈ Ω||fn(x)|> 1/n}
Since
µ
( ∞⋃
n=m
{x∈ Ω||fn(x)|> 1
n}
)
≤
∞∑
n=m
µ
({
x∈ Ω||fn(x)|> 1
n
})
<
∞∑
n=m
n−3/2→ 0.
32

6 JANUARY 2017 Kari Eiﬂer
Therefore, µ(M) = 0 and
Mc =
∞⋃
m=1
∞⋂
n=m
{x∈ Ω||fn(x)|≤ 1/n}.
Note: fn(x)→ 0 if and only if ∀ϵ> 0,∃N s.t.∀n>N ,|fn(x)|<ϵ .
So for any x∈Mc choose 1/N <ϵ s.t.∀n>N we have|fn(x)|≤ 1
n < 1
N <ϵ .
Therefore Mc⊆E, so Ec⊆M, implying µ(Ec) = 0.
Problem 2. Find all f in L1(1, 2) such that for every natural number n we have
∫ 2
1 x2nf(x)dx = 0.
Give reasons for all assertions you make.
Proof. Let f(x) = 0 on x = 1, 2. We now consider f∈L1[1, 2]. Using Stone-Weierstrass to show we
can pass to the case
∫ 2
1 g(x)f(x) = 0 for all g∈C [1, 2].
By a standard density argument, we may pass to the case where g is a step function. We claim that
f = 0 a.e.
Assume not. WLOG there exists some E ={x∈ [1, 2]| f(x) > 0} with m(E) > 0 (else consider
−f).
Since f∈L1[1, 2] then E∞ :={x∈ [1, 2]|f(x) =∞} is a null set. Deﬁne En :={x∈ [1, 2]| 1/n <
f(x)<n}. We can write E = (⋃
nEn)∪E∞. So there exists some N such that m(EN) =a> 0.
We can write A as a ﬁnite disjoint union of open intervals, A =⊔m
i=1Ii, such that m(EN∆A) < ϵ
and A⊆EN.
Put g =∑m
i=1χIi, then
∫ 2
1 g(x)f(x) =
∫
EN
f(x)dx. Since
⏐⏐⏐⏐
∫
EN
f(x)−
∫
A
f(x)
⏐⏐⏐⏐≤Nm(EN∆A)<Nϵ
If we choose ϵ small enough, we see the contradiction since
∫ 2
1 g(x)f(x)> 0.
Problem 3. A. Prove that there exists a sequence of measurable functions gn on [0, 1] such that
(a) gn(x)≥ 0 for any x∈ [0, 1];
(b) limngn(x) = 0 a.e.;
(c) For any continuous function f∈C[0, 1],
lim
n→∞
∫ 1
0
f(x)gn(x)dx =
∫ 1
0
f(x)dx.
Proof. (Solution from Ting Lu, TeX-ed by John Weeks)
It suﬃces to assume f is non-negative. Any f ∈ C[0, 1] is uniformly continuous since [0, 1] is
compact. The following lemma will then come in handy:
Claim. With f as above, n
∫
[x,x+ 1
n2 ](f(y)−f(x))dy =o( 1
n).
33

6 JANUARY 2017 Kari Eiﬂer
For anyϵ > 0,∃N ∈ Nsuch that 0 < x < 1
N then f(x)−f(0) < ε. Hence for n > N,
n
∫
[0, 1
n2 ](f(x)−f(0))<nϵ 1
n2 .
A clear extension to this is that
∫
[x,x+ 1
n ](f(y)−f(x))dy =o( 1
n).
Let gn(x) := ∑n−1
k=0nχ[k
n,k
n + 1
n2 ], and let ε,N be as above. Clearly gn is measurable and satisﬁes
(a) and (b) above. To prove (c), observe that, for n>N ,
Ik :=
⏐⏐⏐⏐⏐
∫ k+1
n
k
n
nfχ [k
n,k
n + 1
n2 ]−f
⏐⏐⏐⏐⏐
=
⏐⏐⏐⏐⏐n
∫ k
n + 1
n2
k
n
f−
∫ k+1
n
k
n
f
⏐⏐⏐⏐⏐
=o
( 1
n
)
.
Hence|
∫
(fgn−f)|≤ ∑n−1
k=0Ik =o(1).
B. If gn is a sequence of measurable functions on [0, 1] such that (a), (b), and (c) are satisﬁed,
what can you say about
∫ 1
0 supngn(x)dx?
Proof. here
Problem 4. We say that a sequence {an}∞
n=1 in [0, 1] is equidistributed (in [0, 1]) if and only if for
all intervals [c,d ]⊂ [0, 1],
lim
n→∞
|{a1,...,a n}∩ [c,d ]|
n =d−c.
(Here|A| denotes the number of elements in the set A.)
LetµN = 1
N
∑
1≤n≤Nδan with δan the point measure at an, that is, for any subset S ∈ [0, 1],
δan(S) =
{
1 if an∈S
0 if an /∈S
.
Show that{an}⊂ [0, 1] is equidistributed if and only if
lim
N→∞
∫ 1
0
fdµN =
∫ 1
0
fdm,
for all continuous functions on [0, 1], where m is Lebesgue measure.
Proof. Note that{an} is equidistributed if and only if
lim
n
|{a1,...,a n}∩ [c,d ]|
n =d−c
34

6 JANUARY 2017 Kari Eiﬂer
if and only if
lim
n
∫ 1
0
fdµN =
∫ 1
0
fdm for f simple functions (since we can take f =χ[c,d])
⇒) It’s easy to see if {an} is equidistributed for f =χ[c,d].
lim
N
∫ 1
0
fdµN = lim
N
|{a1,...,a N}∩ [c,d ]|
N =d−c =
∫ 1
0
fdm
Thus, ”=” holds for step functions.
Using Darboux’s deﬁnition of integral for f∈ C[0, 1],∀ϵ >0 there exists step functions f1,f 2 such
that f1≤f≤f2 and
∫ 1
0 (f2−f1)dx<ϵ where the lower sum is
∫ 1
0
f1(x)dx = lim
N
1
N
N∑
1
f1(an)≤ lim inf
N
1
N
N∑
1
f(an)
and the upper sum is
∫ 1
0
f2(x)dx = lim
N
1
N
N∑
1
f2(an)≥ lim sup
N
1
N
N∑
1
f(an)
Then
⏐⏐⏐⏐⏐lim sup
N
1
N
N∑
1
f(an)− lim inf
N
1
N
N∑
1
f(an)
⏐⏐⏐⏐⏐≤ϵ.
Therefore limN 1
N
∑N
1 f(an) exists and by deﬁnition must be
∫ 1
0 fdµ.
⇐) If we know limK
∫ 1
0 gndµK =
∫ 1
0 gndµ for all gn∈ C[0, 1]. Let f = χ[c,d], choose gn→ f in L1
and each gn↘f positive, gn∈C[0, 1] with gn|[c,d] = 1 =f|[c,d].
We want to show limK
∫ 1
0 fdµK =
∫ 1
0 fdm. Indeed,
35

6 JANUARY 2017 Kari Eiﬂer
⏐⏐⏐⏐
∫ 1
0
fdµK−
∫ 1
0
fdm
⏐⏐⏐⏐ =
⏐⏐⏐⏐⏐
∫ d
c
fdµK−
∫ d
c
fdm
⏐⏐⏐⏐⏐
=
⏐⏐⏐⏐⏐
∫ d
c
gndµK−
∫ d
c
fdm
⏐⏐⏐⏐⏐
=
∫ d
c
gndµK−
∫ d
c
fdm
≤
∫ 1
0
gndµK−
∫ 1
0
fdm
≤
⏐⏐⏐⏐
∫ 1
0
gndµK−
∫ 1
0
gndm
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫ 1
0
gndm−
∫ 1
0
fdm
⏐⏐⏐⏐→ 0.
Problem 5. Consider the space C([0, 1]) of real-valued continuous functions on the unit interval
[0, 1]. We denote by ‖f‖∞ := supx∈[0,1]|f(x)| the supremum norm of f∈ C([0, 1]) and by‖f‖2 :=
(
∫ 1
0|f(x)|2dx)
1
2 the L2-norm of f∈C([0, 1]). Let S be a closed linear subspace of (C([0, 1]),‖·‖ ∞).
Show that if S is complete in the norm ‖·‖ 2, then S is ﬁnite-dimensional.
Proof. Let T : (S,‖·‖ 2)→ (S,‖·‖ ∞) by T (x) =x. Note that both spaces are complete.
Assume xn→x in‖·‖ 2 and T (xn)→y in‖·‖ ∞ then
‖T (xn)−y‖2≤‖T (xn)−y‖∞→ 0.
So
‖x−y‖2≤‖x−T (xn)‖2 +‖T (xn)−y‖2≤‖x−xn‖2 +‖T (xn)−y‖∞→ 0
so x =T (x) =y.
Therefore, by closed graph theorem, we know T is bounded. So there exists some C such that‖f‖∞≤
C‖f‖2.
Now let f1,...,f n be an orthonormal family in S. Then for all ﬁxed x∈ [0, 1]
f1(x)2 +··· +fn(x)2≤‖f1(x)f1 +··· +fn(x)fn‖∞≤C‖f1(x)f1 +··· +fn(x)fn‖2
So then because fn’s are orthogonal and ‖fk‖2
2 = 1,
(f1(x)2 +··· +fn(x)2)2≤C 2(
f1(x)2‖f1‖2
2 +··· +fn(x)2‖fn‖2
2
)
=C 2(f1(x)2 +··· +fn(x)2)
36

6 JANUARY 2017 Kari Eiﬂer
Then f1(x)2 +··· +fn(x)2≤C 2. So
n =
∫ 1
0
f1(x)2 +··· +fn(x)2dx≤
∫ 1
0
C 2dx =C 2⇒n≤C 2
Thus, the number of orthogonal family in S is at most C 2. So S is ﬁnite dimensional.
Problem 6. Prove that if a function f : [0, 1]→ R is Lipschitz, with
|f(x)−f(y)|≤ M|x−y|
for all x,y ∈ [0, 1], then there is a sequence of continuously diﬀerentialbe functions fn : [0, 1]→ R
such that
(i) |f′
n(x)|≤ M for all x∈ [0, 1];
(ii) fn(x)→f(x) for all x∈ [0, 1].
Proof. It’s easy to prove f is aboslutely continuous⇒ f is of bounded variable⇒ f is diﬀerentiable
a.e.⇒ f′ exists a.e.
Also, when f′ exists,|f′(x)|≤ M.
Then there exists simple φ1,φ 2,... such that 0≤| φ1|≤| φ2|≤···≤| φn|≤···≤| f′|≤ M and
φn→f′ uniformly on [0, 1] where f′ exists. Deﬁne
fn(x) :=
∫ x
0
φn(t)dt +f(0) f(x) :=
∫ x
0
f′(t)dt +f(0)
Then|f′
n(x)| =|φn(x)|≤ M and for all x∈ [0, 1],
|fn(x)−f(x)|≤
∫ x
0
|φn(t)−f′(t)|dt→ 0
since φn converges to f′ uniformly.
Problem 7. Given f : R→ R bounded and uniformly continuous and Kn with Kn∈ L1(R) for
n = 1, 2, 3,... such that
(i) ‖Kn‖1≤M <∞, n = 1, 2, 3,...
(ii)
∫∞
−∞Kn(x)dx→ 1 as n→∞ .
(iii)
∫
{x||x|>δ}|Kn(x)|→ 0 as n→∞ for all δ >0.
Show that Kn∗f→f uniformly, where
37

6 JANUARY 2017 Kari Eiﬂer
Kn∗f(x) =
∫ ∞
−∞
Kn(y)f(x−y)dy.
Proof. For allx∈ R,
|Kn∗f(x)−f(x)|≤
⏐⏐⏐⏐Kn∗f(x)−
∫ ∞
−∞
Kn(y)f(x)dy
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫ ∞
−∞
Kn(y)f(x)dy−f(x)
⏐⏐⏐⏐
≤
∫ ∞
−∞
|Kn(y)||f(x−y)−f(x)|dy +‖f‖∞
⏐⏐⏐⏐
∫ ∞
−∞
Kn(y)dy− 1
⏐⏐⏐⏐
≤
∫ ∞
−∞
|Kn(y)||f(x−y)−f(x)|dy +cϵ
=
∫
B(0,δ)
|Kn(y)||f(x−y)−f(x)|dy +
∫
B(0,δ)c
|Kn(y)||f(x−y)−f(x)|dy +cϵ
For
∫
B(0,δ)|Kn(y)||f(x−y)−f(x)|dy, by uniform continuity we ahve
∫
B(0,δ)
|Kn(y)||f(x−y)−f(x)|dy≤ϵ
∫
B(0,δ)
|Kn(y)|dy≤ϵ‖Kn‖1 <ϵM
For
∫
B(0,δ)c|Kn(y)||f(x−y)−f(x)|dy, by the third assumption we have
∫
B(0,δ)c
|Kn(y)||f(x−y)−f(x)|dy≤ 2‖f‖∞
∫
B(0,δ)c
|Kn(y)|dy≤ 2Cϵ
Let ϵ→ 0, so we’ve got it.
Problem 8. (a) Construct a Lebesgue measurable subset A of R so that for all reals a < b, 0 <
m(A∩ [a,b ])<b −a wherem is Lebesgue measure on R.
Proof. Enumerate all rational intervals I1,I 2,... . For each In, construct a fat Cantor set Nn⊆
In with positive measure.
Since Nn is nowhere dense, there exists some interval ~In⊆In and ~In∩Nn =∅.
Construct another fat Cantor set Mn⊆ ~In and deﬁne A :=∪Mn.
Now, for all I = [a,b ] there exists some n such that Nn⊆In⊆I with Nn∩A =∅ (can be done
by induction). We see m(A∩I)≥m(Mn)> 0 and
m(A∩I)<m (I\Nn) =m(I)−m(Nn)<m (I) =b−a.
(b) Suppose A⊆ R is a Lebesgue measurable set and assume that
m(A∩ (a,b ))≤ b−a
2
38

6 JANUARY 2017 Kari Eiﬂer
for any a,b∈ R, a<b . Prove that µ(A) = 0.
Proof. Consider an open set U⊇ A with m(U\A) < ϵ. Then U =⊔∞
i=1(ai,bi) and measurable.
So
m(U) =m(A∩U) +m(U∩Ac)<m (A∩U) +ϵ
Since
m(A∩U) =m (A∩ (⊔∞
i=1(ai,bi))) =
∞∑
i=1
m(A∩ (ai,bi))≤
∞∑
i=1
bi−ai
2 = 1
2m(U)
then
m(U)< 1
2m(U) +ϵ ⇒ m(U)< 2ϵ ⇒ m(A)≤m(U)→ 0
Problem 9. Prove or disprove that the unit ball of L7(0, 1) is norm closed in L1(0, 1).
Proof. Let
B :=
{
f|
∫ 1
0
|f|7dx≤ 1
}
.
Let{fn}⊆ B such that fn→f in L1. We want to show f∈B⇔
∫ 1
0|f|7dx≤ 1.
Since fn→f in L1, then fn→f in measure. Thus, there exists a subsequence fnk such that fnk→
f a.e.
Therefore,|fnk|7→|f|7 a.e.. By Fatou’s Lemma,
∫ 1
0
|f|7dx≤ lim inf
k
∫ 1
0
|fnk|7dx≤ 1.
Problem 10. LetC be the Banach space of convergent sequences of real numbers under the supre-
mum norm. Compute the extreme points of the closed unit ball, B, of C and determine whether B
is the closed convex hull of its extreme points.
Proof. If|x(m)|< 1 for some m then there exists δ >0 such that|x(m)−δ|≤ 1,|x(m) +δ|≤ 1.
Deﬁne y1,y 2∈B such that
y1(n) =x(n) for n⁄=m and y1(m) =x(m) +δ
y2(n) =x(n) for n⁄=m and y2(m) =x(m)−δ
39

7 AUGUST 2016 Kari Eiﬂer
Then y1⁄=y2 and x = 1
2(y1 +y2) so x is not an extreme point.
If|x(n)| = 1 for all n, if x =λy1 + (1−λ)y2 for y1⁄=y2∈B then since|yi(n)|≤ n,
|x(n)| = 1 =|λy1(n) + (1−λ)y2(n)|≤ λ|y1(n)| + (1−λ)|y2(n)|≤ 1
Equality holds only when y1(n) = y2(n) =±1. So y1 = y2 so x is indeed an extreme point. Also, x
needs to be convergent so
Ext(B) ={x||x(n)| = 1∃N s.t. x(n) = 1 or − 1 for all n>N }.
Problem in my proof of determining whether B is the closed convex hull of it’s extreme points.
Problem 11. Show that every convex continuous function deﬁned on the convex unit ball of a re-
ﬂexive Banach space achieves a minimum. (A convex function on a convex subset A of a normed
space is a real valued function, f, on A s.t. for every x,y ∈ A and every 0 < λ < 1 we have
f(λx + (1−λ)y)≤λf(x) + (1−λ)f(y).)
Proof. Recall the following classical result in convex analysis: f is lower-semicontinuous convex⇔
f is weakly lower-semicontinuous convex⇒ f can achieve minimum (since the unit ball is weak-
compact).
Then by Alaoglu, closed unit ball of a reﬂexive Banach space is weak-compact = weak*-compact.
here
7 August 2016
Problem 1. LetA be the set of all real valued functions on [0, 1] for which f(0) = 0 and|f(t)−
f(s)|1/2≤t−s for all 0≤s<t ≤ 1
(a) Prove that A is a compact subset of C[0, 1].
Proof. It should be clear to the reader that this question requires Arezela-Ascoli Theorem. To
seeA is equicontinuous, ﬁx x∈ [0, 1] and ϵ> 0. Then for y∈B(√ϵ,x ),
|f(x)−f(y)|≤| x−y|2 <ϵ
For pointwise bounded, for x∈ [0, 1] then|f(x)|1/2 =|f(x)−f(0)|1/2≤x implies|f(x)|≤ x2.
To seeA is closed, take a sequence {fn}⊆A such that fn→ f (i.e. for all open U containing
f, there exists N such that for all n≥N, fn∈U), then
|f(t)−f(s)|≤| f(t)−fn(t)| +|fn(t)−fn(s)| +|fn(s)−f(s)|< 2ϵ +|t−s|2
This holds for all ϵ> 0 so|f(t)−f(s)|≤| t−s|2.
40

7 AUGUST 2016 Kari Eiﬂer
Clearly,f(0) = 0 so f∈A . ThusA is closed so by Arzela-Ascoli, A is compact inC[0, 1].
(b) Prove that A is a compact subset of L1[0, 1]
Proof. Consider the map
id :C[0, 1]→L1[0, 1]
f↦→f
Since‖ id‖1 =
∫ 1
0|f|dx≤‖f‖∞, id is a bounded map.
From (a),A is compact in C[0, 1] so id(A) =A⊆ L1[0, 1] is also compact.
Remark:A is also closed in L1[0, 1] since all compact subsets of a metric space is closed.
Problem 2. (a) Let f(x) be a real valued function on the real line that is diﬀerentiable almost ev-
erywhere. Prove that f′(x) is a Lebesgue measurable function.
Proof. Let
fn9x) = f(x + 1/n)−f(x)
1/n
so fn→f′ almost everywhere. Since f is diﬀerentiable almost everywhere, then f is continuous
almost everywhere.
Claim: f is Lebesgue measurable
Let D ={all discontinuities of f} so m(D) = 0 and D is measurable. Let E = Dc ={x|
f is continuous at x} so E is measurable too.
f−1((a,∞)) =f−1((a,∞)∩E)∪f−1((a,∞)∩Ec)
Since f|E is continuous, f−1(a,∞)∩E = f|−1
E (a,∞) is open in E. So f−1(a,∞)∩E = U∩E
for some open set U⊆ R. Then f−1(a,∞)∩E is measurable.
Nowf−1(a,∞)∩Ec⊆ Ec, so completeness implies f−1(a,∞)∩Ec is measurable. Thus, f is
Lebesgue measurable so the claim holds.
So each fn is measurable, thus f′ = limfn almost everywhere is also Lebesgue measurable.
(b) Prove that if f is a continuous real valued function on the real line, then the set of points at
which f is diﬀerentiable is measurable.
Proof. Let
F (x,h ) = f(x +h)−f(x)
h
which is continuous on R× (R\{0}). If x is a diﬀerentiable point of f, then for all ϵ >0, there
exists a δ >0 and some Y such that for all h with|h|<δ , we have|F (x,h )−Y|<ϵ . i.e.
41

7 AUGUST 2016 Kari Eiﬂer
D ={x| diﬀerentiable point of f} =
⋂
ϵ
⋃
δ
⋃
Y
⋂
|h|<ϵ
{x||F (x,h )−Y|<ϵ}
For ﬁxedϵ,δ,Y,h then{x||F (x,h )−Y|<ϵ} is open, thus Borel.
By taking only rational ϵ,δ,Y,h we haveD Borel measurable.
Problem 3. (a) Let f be a real valued function on the unit interval [0, 1]. Prove that the set of
points at which f is discontinuous is a countable union of closed subsets.
Proof. f is continuous at p if for all n, there exists an open U containingp such that|f(x)−
f(y)|< 1/n for all x,y∈U. Fix n and let
Vn =
⋃
p
{p s.t. there exists an appropriate U} =
⋃
{appropriate U}
Hence, Vn is open. Then
{points where f is continuous} =
⋂
n
Vn
So{points where f is discontinuous} =⋃
nVc
n where Vc
n is closed.
(b) Prove that there does not exist a real valued function on [0, 1] that is continuous at all rational
points but discontinuous at all irrational points.
Proof. By (a), the irrational poitns would be a countable union of closed subsets. Note that be-
cause any open set in [0, 1] contains a rational point, then if Qc
[0,1] =⋃
nFn where Fn is closed
and F◦
n =∅. Then
[0, 1] = Q[0,1]∪ Qc
[0,1] =

⋃
q∈Q
{q}

∪
(⋃
n
Fn
)
So [0, 1] is a countable union of nowhere dense sets. This contradicts Baire-Category Theorem.
Problem 4. Let (Ω,A,µ ) be a ﬁnite measure space and let (fn) be a sequence of measurable func-
tions on X that converges pointwise to zero. Prove that (fn) converges in measure to zero. Show
that the converse is false for [0, 1] with Lebesgue measure.
Proof. Fix ϵ > 0. To show µ({x | |fn(x)| > ϵ}) → 0, we need∀m∃Nm such that∀n ≥ Nm,
µ({x|fn(x)|>ϵ})< 1/m.
By Egoroﬀ’s Theorem, there exists some E⊆X with µ(E)< 1/m and fn ⇒ 0 uniformly on Ec.
Thus,∃Nm such that for n≥Nm|fn(x)|<ϵ for all x∈Ec so
µ({x||fn(x)|>ϵ})≤µ(E)< 1
m ∀n≥Nm
42

7 AUGUST 2016 Kari Eiﬂer
Thus,µ({x||fn(x)|>ϵ})→ 0.
Counterexample: Let f1 = χ[0,1],f 2 = χ[0,1/2],f 3 = χ[1/2,1],...,f n = χ[j/2k,(j+1)/2k] for n =
2k +j, 0≤j <2k.
So fn does not approach 0 pointwise, but fn→ 0 in L1, hence in measure.
Problem 5. If f is Lebesgue integrable on the real line, prove that limh→0
∫
R|f(x+h)−f(x)|dx = 0.
Proof. Recall: the set Cc(R) of continuous, compactly supported functions is dense in L1(R).
Fix ϵ >0 and ﬁnd g∈Cc(R) with‖f−g‖1 < ϵ. Since g is continuous, limn|g(x + 1/n)−g(x)| = 0
ofr all x.
Since g is compactly supported, then there exists some compact K such that supp(g)⊆K.
So there exists a compact K′ such that supp(g)∪ supp(g(x + 1/n))⊆K′ for all n (this follows from
1/n≥ 1 for all n since we can take K′ ={k +x|k∈K,x∈ [0, 1]}).
Dini’s theorem implies that |g(x + 1/n)−g(x)| ⇒ 0 so
∫
R|g(x + 1/n)−g(x)|dx =
∫
K′
|g(x + 1/n)−g(x)|dx→ 0
So then
∫
R
|f(x + 1/n)−f(x)|dx
≤
∫
R
|f(x + 1/n)−g(x + 1/n)|dx +
∫
R
|g(x + 1/n)−g(x)|dx +
∫
R
|g(x)−f(x)|dx
< 2ϵ +
∫
R
|g(x + 1/n)−g(x)|dx→ 2ϵ
Since it holds for all ϵ> 0 then limn
∫
R|f(x + 1/n)−f(x)|dx = 0.
43

7 AUGUST 2016 Kari Eiﬂer
Problem 6. Prove or disprove that there exists a sequence (Pn) of polynomials such that (Pn(t))
converges to one for every t∈ [0, 1] but
∫ 1
0 Pn(t)dt converges to two as n→∞ .
Proof. Consider
fn(x) =



n2x x ∈ [0, 1/n]
−n2x + 2n + 1 x∈ [1/n, 2/n]
1 x∈ [2/n, 1]
(that is, fn linearly connects the points (0, 1), (1/n,n + 1), (2/n, 1), (1, 1).)
So fn(x)→ 0 for all x∈ [0, 1] but
∫ 1
0 fn(x)dx = 2.
Then by Stone-Weierstrass, we can ﬁnd polynomials Pn such that‖fn−Pn‖∞≤ 2−n. Then ∀x
|Pn(x)− 1|≤| Pn(x)−fn(x)| +|fn(x)− 1|→ 0
and
∫ 1
0|fn(x)−Pn(x)|dx→ 0 so
∫ 1
0 Pn(x)dx→ 2.
Problem 7. Let (fn) be a uniformly bounded sequence of continuous functions on [0, 1] that con-
verges pointwise to zero. Prove that 0 is in the norm closure in C[0, 1] of the convex hull of (fn)
(the norm is of course the sup norm on C[0, 1]).
Proof. By the Geometrical version of the Hahn-Banach,
conv{fn}
weak
= conv{fn}
‖·‖
We just need to show that 0 ∈ conv{fn}
weak
. By Riesz-Representation Theorem, C[0, 1]∗ =M[0, 1].
For allµ∈M[0, 1],
⏐⏐⏐⏐⏐
∫
[0,1]
fndµ
⏐⏐⏐⏐⏐≤
∫
[0,1]
|fn|d|µ|→ 0
by Dominated Convergence Theorem. Thus, fn→ 0 weakly.
Problem 8. Assume that X is a reﬂexive Banach space and φ is a continuous linear functional on
X. Prove that φ achieves its norm; that is, prove that there is a norm one vector x in X such that
φ(x) = ‖x‖. Show by example that there is a continuous linear functional on the Banach space 𝓁1
that does not achieve its norm.
Proof. Recall: X reﬂexive⇒ BX is weak-compact⇒ BX is weak-sequentially compact.
There exists a sequence {xn}⊆ BX such that φ(xn)↗‖φ‖.
Choose a weakly-convergent subsequence{xnk} that converges to x∈ BX. Then for all ϕ∈ X∗,
ϕ(xnk)→ϕ(x).
44

7 AUGUST 2016 Kari Eiﬂer
In particular,
‖φ‖ = lim
n
φ(xn) = lim
k
φ(xnk) =φ(x).
Alternative Proof. For allφ∈ X∗, by Hahn-Banach Separation Theorem, there exists some x∗∗∈
X∗∗ such that‖x∗∗‖X∗∗ = 1 and x∗∗(φ) =‖φ‖X∗.
Since X is reﬂexive,∃x∈X such that ˆx =x∗∗ so
‖φ‖X∗ =x∗∗(φ) = ˆx(φ) =φ(x).
Counterexample: Choose y = (1− 1/n)n∈𝓁∞. Then ∀x∈𝓁1,
y(x) =
⏐⏐⏐⏐⏐
∞∑
n=1
(
1− 1
n
)
x(n)
⏐⏐⏐⏐⏐≤
∞∑
n=1
(
1− 1
n
)
|x(n)|<
∞∑
n=1
|x(n)| =‖x‖1 = 1 =‖y‖∞.
Problem 9. Suppose that X is a non separable Banach space. Prove that there is an uncountable
subset A of the unit ball of X such that for all x⁄=u in X,‖x−y‖> 0.9.
Proof. By transﬁnite induction, construct (xα)α<ω 1⊆BX where ω1 is the uncountable ordinal.
Givenα<ω 1, let Uα := span{xβ|β <α} which is separable.
Since X is not separable, Uα ⊊X.
By Riesz-Lemma, there exists ‖xα‖ = 1 such that d(xα,Uα)≥ 1−ϵ (put ϵ> 0.1).
So (xα) satisﬁes‖xα−xβ‖≥ 0.9 and is uncountable.
Alternative Proof if it were not restricted to BX. Fix r >0. Zornicate over all subsets A⊆X such
that∀x⁄=y,‖x−y‖>r .
Find a maximal subset Ar⊆X as above. If Ar is uncountable, by scaling of r, we’re done.
Suppose not, so each Ar is countable. Enumerate as {xr
n}n. By maximality, for all x∈X,∀ϵ >0 if
r> 1/ϵ then there exists n∈ N such taht‖x−xm
n‖<r<ϵ (i.e. d(x,Ar)<r,∀x∈X).
Let A =⋃
q∈QAq so A is a countable dense subset of X. Contradiction!
Therefore, there exists q∈ Q such that Aq is uncountable. Consider A′ ={ 0.9
q x| x∈ Aq} so for all
x′,y′∈A,
‖x′−y′‖ =
‖‖‖‖
0.9
q x− 0.9
q y
‖‖‖‖ = 0.9
q ‖x−y‖> 0.9
Thus, there eixsts an uncountable A⊆X such that for all x,y∈A,‖x−y‖> 0.9.
45

8 JANUARY 2016 Kari Eiﬂer
Problem 10. If A is a Borel subset of the line, then E ={(x,y )| x−y∈ A} is a Borel subset of
the plane. If the Lebesgue measure of A is 0, then the Lebesgue measure of E is 0.
Proof. Deﬁne f(x,y ) =x−y : R2→ R. This is continuous. Let
A :={S⊆ R|f−1(S) is a Borel set of R2}
ThenA is a σ-algebra (easy to check). If S is open, then f−1(S) is open in R2, thus Borel. So {open sets}⊆
A and so the Borel algebra is a subset of A. In particular, A∈A .
Let E =f−1(A) which is a Borel set of R2. If m(A) = 0, let
Ey ={x∈ R| (x,y )∈E} =y +A
This is a null set since m(y +A) =m(A) = 0. Thus, (m×m)(E) =
∫
m(Ey)dm(y) = 0.
8 January 2016
Problem 1. LetE be a measurable subset of [0, 1]. Suppose there exists α∈ (0, 1) such that
m(E∩J)≥α·m(J)
for all subintervals J of [0, 1]. Prove that m(E) = 1.
Proof. It’s easy to see that m(E)≤ 1.
For any open U⊆ [0, 1], write U =⊔∞
i=1Ii where each Ii is an open interval. Then
m(E∩U) =
∞∑
i=1
m(E∩Ii)≥
∞∑
i=1
αm(Ii) =αm(U).
Assume m(E) < 1, so m(Ec) := a > 0. We may ﬁnd some open U ⊇ Ec such that m(U∩E) =
m(U\Ec)<ϵ . So
ϵ>m (U∩E)≥αm(U)≥αm(Ec) =αa> 0.
Letting ϵ→ 0, this leads to a contradiction.
Problem 2. Letf,g ∈L1([0, 1]). Suppose
∫ 1
0
xnf(x)dx =
∫ 1
0
xng(x)dx
46

8 JANUARY 2016 Kari Eiﬂer
for all integers n≥ 0. Prove that f(x) =g(x) a.e.
Proof. See # 2 from January 2017.
Problem 3. Letf,g ∈L1([0, 1]). Assume for all functions ϕ∈C∞[0, 1] with ϕ(0) =ϕ(1) we have
∫ 1
0
f(t)ϕ′(t)dt =−
∫ 1
0
g(t)ϕ(t)dt.
Show that f is absolutely continuous and f′ =g a.e.
Proof. Fix x∈ [0, 1] and construct hn via
hn(t) =



nt t ∈ [0, 1/n]
1 t∈ [1/n,x ]
1−n(t−x) t∈ [x,x + 1/n]
0 t∈ [x + 1/n, 1]
(i.e. hn(t) linearly connects the points (0, 0), (1/n, 1), (x, 1), (x + 1/n, 0), and (1, 0).
Since C∞[0, 1] is dense in ‖·‖ ∞, we may use this example rather than some ϕ∈ C∞[0, 1] (i.e. pass
to the continuous case). Then
∫ 1
0
f(t)h′
n(t)dt =
∫ 1/n
0
f(t)ndt + 0 +
∫ x+1/n
x
f(t)(−n)dt + 0→f(0)−f(x)
where the limit follows from Lebesgue Diﬀerentiation Theorem. Also,
∫ 1
0
g(t)hn(t)dt =
∫ 1/n
0
ntg (t)|{z}
→0
dt +
∫ x
1/n
g(t)dt +
∫ x+1/n
x
g(t)dt−
∫ x+1/n
x
n (t−x)g(t)| {z }
→0 as t→x
dt + 0
→ 0 +
∫ x+1/n
1/n
g(t)dt− 0
where the limit again follows from Lebesgue Diﬀerentiation Theorem. Taking the limit as n→∞
on both sides, we get
∫x
0 g(t)dt = limn
∫x+1/n
1/n g(t)dt. So
f(0)−f(x) = lim
n
∫ 1
0
f(t)h′
n(t) = lim
n
−
∫ 1
0
g(t)hn(t)dt =−
∫ x
0
g(t)dt
Implying f(x) =f(0) +
∫x
0 g(t)dt. Then
47

8 JANUARY 2016 Kari Eiﬂer
f′(x) = lim
h→0
f(x +h)−f(x)
h = lim
h→0
f(0) +
∫x+h
0 g(t)dt−f(0)−
∫x
0 g(t)dt
h = lim
h→0
∫x+h
x g(t)dt
h =g(x)
and f is absolutely continuous.
Problem 4. Let{gn} be a sequence of measureable functions on [0, 1] such that
(i) |gn(x)|≤ C, for a.e. x∈ [0, 1]
(ii) and limn→∞
∫a
0 gn(x)dx = 0 for every a∈ [0, 1].
Prove that for each f∈L1([0, 1]), we have
lim
n→∞
∫ 1
0
f(x)gn(x)dx = 0.
Proof. Let S = span{χ[0,a]| a∈ [0, 1]}. Then S is dense in the space of step functions in L1. Step
function space is dense in L1 so S is dense in L1. Then for every f∈L1[0, 1] there exists a sequence
hm =∑Km
i=1K (m)
i χ[0,ai]→f in L1.
For a ﬁxed m,
lim
n
∫ 1
0
hmgndx =
Km∑
i=1
K (m)
i lim
n
∫ ai
0
gn(x)dx = 0
where the second equality follows from (ii). For every ϵ> 0, we can choose some m such that‖hm−
f‖1 <ϵ .
For thatm, choose soem N such that
⏐⏐⏐
∫ 1
0 hmgndx
⏐⏐⏐<ϵ for all n>N . Then
⏐⏐⏐⏐
∫ 1
0
f(x)gn(x)dx
⏐⏐⏐⏐≤
⏐⏐⏐⏐
∫ 1
0
(
f(x)−hm(x)
)
gn(x)dx
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫ 1
0
hm(x)gn(x)dx
⏐⏐⏐⏐
≤c‖f−hm‖1 +ϵ
< (c + 1)ϵ
Thus,
∫ 1
0 f(x)gn(x)dx = 0.
Problem 5. (a) Let X be a normed vector space and Y be a closed linear subspace of X. Assume
Y is a proper subspace, that is, Y ⁄=X. Show that, for all 0<ϵ< 1, there is an element x∈X
such that‖x‖ = 1 and
inf
y∈Y
‖x−y‖> 1−ϵ
48

8 JANUARY 2016 Kari Eiﬂer
Proof. Fix some x0∈ X\Y , denote infy∈Y‖x0−y‖ = d >0. Now for every ϵ >0 choose some
δ >0 such that d
d+δ > 1−ϵ.
Choose y0∈Y such that‖x0−y0‖<d +δ. Let x = x0−y0
‖x0−y0‖ so‖x‖ = 1 and
inf
y∈Y
‖x−y‖ = inf
y∈Y
‖‖‖‖
x0−y0
‖x0−y0‖−y
‖‖‖‖ = 1
‖x0−y0‖ inf
y′∈Y
‖x0−y′‖> d
d +δ > 1−ϵ.
(b) Use part (a) to prove that, if X is an inﬁnite dimensional normed vector space, then the unit
ball of X is not compact.
Proof. If we construct a sequence {xn} such that there are no convergent subsequences, we are
done.
Assume we have chosen{x1,x 2,...,x n−1}⊆ BX. Let Y = span{x1,x 2,...,x n−1}. By part (a),
there exists some xn∈B such that‖xn‖ = 1 and infy∈Y‖xn−y‖> 1/2.
Then we have a sequence{xn}⊆ BX such that‖xn−xm‖> 1/2 for all n⁄=m so no convergent
subsequence may exist.
Problem 6. Let{fk} be a sequence of increasing functions on [0, 1]. Suppose
∞∑
k=1
fk(x)
converges for all x∈ [0, 1]. Denote the limit function by f, that is,
f(x) =
∞∑
k=1
fk(x).
Prove that
f′(x) =
∞∑
k=1
f′
k(x), a.e. x∈ [0, 1].
Proof. It’s easy to see f is increasing, so it’s diﬀerentiable almost everywhere. Let FN = ∑N
n=1fn
so FN→f for all x∈ [0, 1]. Choose an increasing sequence Nk such taht 0≤f(1)−FNk(1)≤ 2−k.
Then
∞∑
k=1
(
f(1)−FNk(1)
)
≤
∞∑
k=1
2−k = 1.
Now, let g(x) :=∑∞
k=1
(
f(x)−FN−k(x)
)
=∑∞
k=1
∑∞
n=Nk+1fn(x).
Since∑∞
n=Nk+1fn(x) is increasing as x increases, then g is increasing.
49

8 JANUARY 2016 Kari Eiﬂer
So 0≤g(x)≤g(1)≤ 1 and g is diﬀerentiable almost everywhere. Now,
1
h
(
g(x +h)−g(x)
)
= 1
h
∞∑
k=1
(
f(x +h)−FNk(x +h)
)
−
(
f(x)−FNk(x)
)
.
So since f′(x)−FNk(x) =∑∞
n=Nk+1fn(x) is increasing, g′(x)≥∑∞
k=1f′(x)−F′
Nk(x)≥ 0. Therefore,∑∞
k=1f′(x)−FNk(x) converges. So limkF′
Nk(x) = f′(x), implying f′(x) = ∑∞
k=1f′
k(x) almost
everywhere.
Problem 7. Supposef,g : [a,b ]→ R are both continuous and of bounded variation. Show that the
set
{(f(t),g (t))∈ R2|t∈ [a,b ]}
cannot cover the entire unit square [0, 1]× [0, 1].
Proof. Deﬁne r(t) = (f(t),g (t)). Since R2 is ﬁnite dimensional, 𝓁1∼𝓁2. Since f and g have bounded
variation, so does r. Thus, we know that whenever a = x0 < x1 < x2 < ... < xn = b we have∑n
i=1‖r(xi)−r(xi−1)‖2 <M .
Now suppose [0, 1]× [0, 1] can be covered. Divide [0 , 1]× [0, 1] into n2 small squares with center zj
and the length of each edge is 1 /n. Then choose tj such that r(tj) =zj.
Now relabel/reorder the tj in increasing order so that s1 < s2 < ... < sn2. Then since the distance
between two centers is at least 1/n,
n2−1∑
j=1
‖r(sj+1)−r(sj)‖2≥
n2−1∑
j=1
1/n = n2− 1
n →∞.
This is a contradiction!
Problem 8. Prove the following two statements:
(a) Suppose f is a measurable function on [0, 1], then
‖f‖L∞ = lim
p→∞
‖f‖Lp
Proof. In [0, 1], by H¨ older, we know that‖f‖p≤‖f‖q when p≤q. Also, ‖f‖p≤‖f‖∞ for all p.
Therefore,‖f‖p↗≤‖f‖∞ and so limp‖f‖p≤‖f‖∞.
On the other hand, for every ϵ >0, let E ={x|| f(x)| >‖f‖∞−ϵ} and 0 < µ(E)≤ 1 since
‖f‖∞ = esssup|f(x)|. Then ‖f‖p
p≥
∫
E|f|p >
(
‖f‖∞−ϵ
)p
µ(E). Take p→∞ so limp‖f‖p≥
‖f‖∞−ϵ, implying limp‖f‖p≥‖f‖∞.
(b) If fn≥ 0 and fn→f in measure, then
∫
f≤ lim inf
∫
fn.
50

8 JANUARY 2016 Kari Eiﬂer
Proof. Choose a subsequence{fnk} such that limk
∫
fnk = lim inf
∫
fn. Since fn→ f in mea-
sure, fnk → f in measure, so there exists a further subsequence {fnk𝓁
}→ f a.e. Then by Fa-
tou’s Lemma,
∫
f =
∫
lim
𝓁
fnk𝓁
≤ lim inf
𝓁
∫
fnk𝓁
= lim
k
inffnk = lim inf
n
∫
fn.
Problem 9. Suppose{fn} is a sequence of functions in L2([0, 1]) such that‖fn‖L2 ≤ 1. If f is
measurable and fn→f in measure, then
(a) f∈L2([0, 1]);
Proof. fn → f in measure implies{fnk}→ f almost everwhere which implies|fnk|2 →| f|2
almost everywhere. By Fatou’s Lemma,
∫ 1
0
|f|2dx≤ lim
n
∫ 1
0
|fnk|2dx≤ 1.
So f∈L2.
(b) fn→f weakly in L2;
Proof. Let g ∈ L2. We want to show that fng → fg in L1. Now, fn → f in measure, then
fng→fg in measure and thus is Cauchy in measure.
Deﬁne Am,n ={x∈ [0, 1]||fng(x)−fmg(x)|≥ ϵ}. Then
∫ 1
0
|fng−fmg|dx =
∫
Am,n
|fng(x)−fmg(x)|dx+
∫
[0,1]\Am,n
|fng(x)−fmg(x)|dx≤
∫
Am,n
|fng|+|fmg|dx+ϵ.
We know for all ϵ> 0 there exists some δ >0 such that µ(Am,n)<δ ,
∫
Am,n
|fng|≤
(∫
Am,n
|fn|2dx
)1/2(∫
Am,n
|g|2dx
)1/2
≤
(∫
Am,n
|g|2
)1/2
<ϵ.
since g ∈ L2. Then since {fng} is Cauchy in measure, there exists some N such that for all
m,n>N , µ(Am,n)<δ . Then
∫ 1
0|fng−fmg|dx< 3ϵ implies{fng} is Cauchy in L1.
Therefore, there exists some h∈L1 such taht fng→h in L1.
We knowfng→ fg in measure, so fnkg→ fg almost everywhere. Also, ∀ϵ > 0,∃δ > 0 such
that
∫
A|fnkg|<ϵ for all A such that µ(A)<δ .
Therefore,{fnk} is uniformly integrable. By Viteli Convergence Theorem, fnkg → fg in L1.
Thus,h =fg so fng→fg in L1. So fn→f weakly.
Note: We could also have used the uniqueness of limit in the measure.
(c) fn→f with respect to norm in Lp for 1≤p< 2.
51

8 JANUARY 2016 Kari Eiﬂer
Proof. Deﬁne En ={x|| fn(x)−f(x)|≥ ϵ}. From problem 8 on this exam, we know ‖fn‖p≤
‖fn‖2≤ 1 and‖f‖p≤‖f‖2 <∞. Then
∫
|fn−f|p =
∫
En
|fn−f|p +
∫
Ecn
|fn−f|pdx≤ 2p−1
∫
En
|fn|p +|f|p +ϵ
where the inequality follows from the fact that |a−b|p≤ 2p−1(|a|p +|b|p).
Since fn→ f in measure and m(En)→ 0 as n→∞ , so since f∈ Lp then
∫
En
|f|pdx→ 0 as
n→∞ .
For someA⊆ [0, 1], we have
∫
A
|fn|p =
∫ 1
0
|fn|pχA≤‖|fn|p‖2/p‖χA‖2/2−p =‖fn‖p
2m(A)
2
2−p≤m(A)
2
2−p.
So similar to the previous case, we can take m(En) small enough such that
∫
En
|fn|pdx < ϵfor
any ﬁxed 1≤p< 2.
There are a few hints in the qual
Problem 10. SupposeE is a measurable subset of [0, 1] with Lebesgue measure m(E) = 99
100.
Show that there exists a number x∈ [0, 1] such that for all r∈ (0, 1),
m(E∩ (x−r,x +r))≥ r
4.
Hint: Use the Hardy-Littlewood maximal inequality
m({x∈ R|Mf (x)≥α})≤ 3
α‖f‖1
for all f∈L1(R). Here Mf denotes the Hardy-Littlewood Maximal function of f.
Proof. The Hardy-Littlewood Maximal function of χA is
MχA = sup
r>0
1
2r
∫ x+r
x−r
χA(x)dx = sup
r>0
1
2rm(A∩ (x−r,x +r)).
Assume the result is not true. Then ∀x∈ [0, 1],∃rx∈ (0, 1) such that m(E∩ (x−xr,x +xr))< rx
4 .
This happens if and only if 1
2rx
m(E∩ (x−rx,x +rx))< 1/8 which is equivalent to 1
2rx
m(Ec∩ (x−
rx,x +rx))≥ 7
8.
Now set A =Ec so MχA(x)≥ 7
8. However,
m
(
{x∈ [0, 1]|MχA(x)≥ 7
8}
)
≤ 38
7‖χA‖ = 24
7
1
100 = 24
100.
But we need it to be equal to 1. Contradiction!
52

9 AUGUST 2015 Kari Eiﬂer
9 August 2015
Problem 1. Letf : R→ R be a Borel measurable function. For each t∈ R deﬁne
ft(x) =f(t +x), x ∈ R.
Prove that ft(x) is a Borel measurable function (in x) for each ﬁxed t∈ R.
Proof. We see that
f−1
t (−∞,a ) ={x|f(x +t)∈ (−∞,a )} ={x|x +t∈f−1(−∞,a )} =f−1((−∞,a ))−t =B−t.
Since Tt(x) =x +t is continuous, then T−1
t (B) =B−t is Borel.
Problem 2. Justify the statement that
∫ 1
0
∫ 1
0
(x−y) sin(xy)
x2 +y2 dx dy=
∫ 1
0
∫ 1
0
(x−y) sin(xy)
x2 +y2 dy dx.
Proof. We just need to show that
∫ 1
0
∫ 1
0
⏐⏐⏐ (x−y) sin(xy)
x2+y2
⏐⏐⏐dxdy <∞. But
∫ 1
0
∫ 1
0
⏐⏐⏐⏐
(x−y) sin(xy)
x2 +y2
⏐⏐⏐⏐dxdy =
∫ π/2
0
∫ √
2
0
⏐⏐⏐⏐
r cosθ−r sinθ
r2
⏐⏐⏐⏐|r|drdθ≤ 2
∫ π/2
0
∫ √
2
0
drdθ =
√
2π <∞.
So the function is in L1 and Fubini gives us the desired result.
Problem 3. Assume that (fn) is a sequence in C[0, 1].
(a) Show that (fn) converges weakly to 0 if and only if (fn) is bounded in C[0, 1] and limn→∞fn(t) =
0 for all t∈ [0, 1].
Proof.⇒) We know C[0, 1]∗ =M[0, 1]. Then fn→ 0 weakly implies
∫
fndµ→ 0 for all µ∈
M[0, 1]. Choose µ =δt so
∫
fndδt =fn(t)→ 0 ∀t∈ [0, 1]
(this follows from the fact that weak convergence implies uniformly bounded). Consider
χ :C[0, 1]→C[0, 1]∗∗ =M[0, 1]∗
χ(fn)(µ) =µ(fn)
53

9 AUGUST 2015 Kari Eiﬂer
Since µ(fn) → 0 then χ(fn)(µ) → 0 for all µ ∈ M[0, 1]. Since convergent sequences are
bounded, then supn|χ(fn)(µ)|≤ M.
By the uniform boundedness theorem, sup n‖χ(fn)‖ < ∞. By isometry,‖fn‖ = ‖χ(fn)‖ so
supn‖fn‖<∞.
⇐) By Dominated Convergence Theorem, fn→ 0 in L1(µ). So therefore, |
∫
fndµ|≤
∫
|fn|d|µ|→
0. So fn→ 0 weakly.
(b) Show that if (fn) converges weakly in C[0, 1], then it converges in norm in Lp[0, 1] for all 1≤
p< ∞.
Proof. WLOG fn → 0 weakly. By (a) we know fn(t) → 0 and‖fn‖∞ is bounded. Thus,
|fn(t)|p→ 0 pointwise and‖|fn|‖∞ is bounded.
By the Dominated Convergence Theorem, we have ‖fn‖p→ 0.
Problem 4. LetA be a Lebesgue null set in R. Prove that
B :={ex|x∈A}
is also a null set.
Proof. First, assume A⊆ [0, 1]. Then f(x) =ex is Lipschitz-continuous (i.e.|f(x)−f(y)|≤ M|x−y|
for some M). Since m(A) = 0, we can ﬁnd ∪∞
k=1Bk where Bk are open intervals such that A ⊆
∪∞
k=1Bk and m (∪∞
k=1Bk)<ϵ . Then
m(f(A))≤m (f (∪∞
k=1Bk))≤
∞∑
k=1
Mm(Bk)<Mϵ.
So m(f(A)) = 0. Now we can write A =∪∞
n=−∞A∩ [n,n + 1] so m(f(A)) =∑∞
−∞m(f(A∩ [n,n +
1])) = 0.
Problem 5. (a) Deﬁne absolute continuity of a function f : R→ R and of a function f : [a,b ]→
R.
Proof. The function f : [a,b ]→ R is absolutely continuous if∀ϵ > 0,∃δ > 0 such that when-
ever a ﬁnite sequence of disjoint subintervals (xk,yk)⊆ I satisﬁes∑N
k=1(yk−xk) < δ then∑∞
k=1|f(yk)−f(xk)|<ϵ .
(b) Show that if f and g are absolutely continuous on [a,b ], a,b ∈ R, a < b, then f·g is absolutely
continuous on [a,b ].
Proof. Since f and g are continuous on [a,b ], then they achieve a maximum so we can let Mf =
sup{f(x)|a≤x≤b}<∞, Mg = sup{g(x)|a≤x≤b}.
Fix ϵ> 0. Then there exists some δf,δg > 0 such that
54

9 AUGUST 2015 Kari Eiﬂer
∑
(yk−xk)<δ f ⇒
∑
|f(yk)−f(xk)|< ϵ
2Mg
∑
(yk−xk)<δ g ⇒
∑
|f(yk)−f(xk)|< ϵ
2Mf
Choose ﬁnite and disjoint such that ∑yk−xk < min(δf,δg). Then
∑
|f(yk)g(yk)−f(xk)g(xk)|≤
∑
|f(yk)g(yk)−f(yk)g(xk)| +
∑
|f(yk)g(xk)−f(xk)g(xk)|
≤
∑
|f(yk)||g(yk)−g(xk)| +
∑
|g(xk)||f(yk)−f(xk)|
≤Mf
∑
|g(yk)−g(xk)| +Mg
∑
|f(yk)−f(xk)|
≤Mf
ϵ
2Mf
+Mg
ϵ
2Mg
=ϵ
This is what we wanted.
(c) Give an example to show that (b) is false if [a,b ] is replaced by R.
Proof. Takef(x) =g(x) =x so fg =x2. Then
|(x +δ)2−x2| =|x2 + 2δx +δ2−x2| =|2δx +δ2|→∞ as x→∞.
So there does not exist any δ such that|fg (y)−fg (x)|<ϵ (even for just one interval!)
Problem 6. LetX and Y be Banach spaces and T : X→ Y be a one-to-one, bounded and linear
operator for which the range T (X) is closed in Y . Show that for each continuous linear functional φ
on X there is a continuous linear functional ψ on Y , so that φ =ψ◦T .
Proof. Since T :X→T (X) is bijective, by teh open mapping theorem, T−1 is bounded so φ◦T−1∈
T (X)∗.
Then by the Hahn-Banach, there exists some ψ∈Y∗ such that ψ(y) = (φ◦T−1)(y) for all y∈Y .
For anyx∈X, T (x) =y∈Y and we have
φ(x) =φ
(
T−1(Tx )
)
=ψ(Tx ) = (ψ◦T )(x).
Since this is true for all x∈X, φ =ψ◦T .
Problem 7. State the Open Mapping Theorema nd the Closed Graph Theorem for Banach spaces.
Derive the Open Mapping Theorem from the Closed Graph Theorem.
Proof. Assume T : X→ Y is surjective, linear, and bounded. WLOG we want to show B(0,δ )⊆
T (B(0, 1)) for some δ >0. Deﬁne
55

9 AUGUST 2015 Kari Eiﬂer
G :Y →X/ ker(T )
y↦→ [x] =x + ker(T ) where y =Tx
Then G is well-deﬁned, because T is surjective.
Claim: G is closed.
Assume yn→y in Y and G(yn)→ [x] in X/ ker(T ). WTS G(y) = [x]⇔Tx =y.
We haveTxn = yn so since [xn]→ [x] then‖[xn]− [x]‖ = infz∈kerT‖xn−x−z‖→ 0. Then take
(zn)⊆ ker(T ) such that‖xn−x−zn‖< 1/n. So xn−zn→x. Then
‖T (xn−zn)−T (x)‖≤‖ T‖‖xn−x−zn‖→ 0.
Thus,T (xn−zn) = T (xn)→T (x). And also T (xn−zn) = T (xn) = yn→y. Together, these imply
T (x) =y. So G is closed, and the claim holds.
By the closed graph theorem, G is bounded so there exists some δ > 0 such that G(B(0,δ )) ⊆
B(0, 1) in X/ ker(T ). Now, let y∈B(0,δ ) so then [x] =G(y)∈B(0, 1). Thus, if inf z∈ker(T )‖x−z‖<
1, then there exists some z0∈ ker(T ) such that‖x−z0‖ < 1. This implies y = Tx = T (x−z0)∈
T (B(0, 1)) so B(0,δ )⊆T (B(0, 1)).
Problem 8. LetY be a closed subspace of a Banach space X, with norm ‖·‖ . Let ‖·‖ 1 be a norm
on Y which is equivalent to ‖·‖ , meaning that there is a C≥ 1 so that
1
C‖y‖1≤‖y‖≤ C‖y‖1 for all y∈Y.
LetS be the set of all linear functions φ :X→ R, so that
(i) |φ(y)|≤‖ y‖1 for all y∈Y , and
(ii) |φ(x)|≤ C‖x‖ for all x∈X.
Prove the following statements
(a) ‖x‖2 := supφ∈S|φ(x)|, x∈X, deﬁnes a norm on X.
Proof. Easy to check.
(b) ‖y‖2 =‖y‖1 for y∈Y .
Proof. Since|φ(y)|≤‖ y‖1 then‖y‖2≤‖y‖1.
On the other hand, from the Hahn-Banach separation theorem, for all y⁄= 0, there exists some
φ∈X∗ such that‖φ‖ = 1 and φ(y) =‖y‖1 so‖y‖2≥‖y‖1.
To check thatφ∈S:|φ(y)| =‖y‖1 and|φ(x)|≤‖ φ‖‖x‖ =‖x‖.
56

9 AUGUST 2015 Kari Eiﬂer
(c) The norms ‖·‖ 2 and‖·‖ are equivalent on X.
Proof. We just need to consider this on X\Y . For x∈X\Y , we have
‖x‖2 = sup
φ∈S
|φ(x)|≤ C‖x‖.
Again by Hahn-Banach, for ˜x⁄= 0, there exists some φ∈X∗ such that φ(˜x) =‖˜x‖ and‖φ‖ = 1.
Deﬁne ψ = 1
Cφ so‖ψ‖ = 1
C .
Then to see ψ∈S:
• |ψ(x)|≤ 1
C‖x‖≤ C‖x‖ for all x∈X
• |ψ(y)|≤ 1
C‖y‖≤‖ y‖1 for all y∈Y
So ψ∈S and‖˜x‖≥| ψ(˜x)| = 1
C‖˜x‖ so 1
C‖x‖≤‖ x‖2≤C‖x‖.
Problem 9. Letf be increasing on [0, 1] and let
g(x) = lim sup
h→0
f(x +h)−f(x−h)
2h , for 0<x< 1.
Prove that if A ={x∈ (0, 1)|g(x)> 1} then
f(1)−f(0)≥m∗(A).
Proof. Forx∈A,
lim sup
h→0
f(x +h)−f(x−h)
2h > 1
so for all ϵ > 0, there exists some h > 0 such that 2h < ϵand f (x+h)−f (x−h)
2h > 1 if and only if
f(x +h)−f(x−h)> 2h.
Let I ={(x−h,x +h)| x∈ A, 2h < ϵ,(x−h,x +h)⊆ [0, 1]}. Then I coversA in the sense
of Vitali. By Vitali’s Lemma, for every ϵ > 0, there exists I1,I 2,...,I n disjoint from I such that
m∗ (A\∪n
i=1Ii)<ϵ .
Since m∗(A) = m∗ (A\∪n
i=1Ii) + m∗ (∪n
i=1Ii) for all Ii then write Ii = (xi− hi,xi + hi) and
x1−h1 <x 1 +h1 <x 2−h2 <...<x n +hn. Then
m∗(A)<ϵ +
n∑
i=1
2hi <ϵ +
n∑
i=1
|f(xi +hi)−f(xi−hi)|.
Since f is increasing, ∑n
i=1
(
f(xi +hi)−f(xi−hi)
)
≤f(1)−f(0).
So m∗(A)<ϵ +f(1)−f(0) so m∗(A)≤f(1)−f(0).
57

9 AUGUST 2015 Kari Eiﬂer
Problem 10. (a) State a version of the Stone-Weierstrass Theorem.
Proof. See textbook.
(b) Let A be a uniformly dense subspace of C[0, 1] and let
B =
{
F (x)|F (x) =
∫ x
0
f(t)dt, 0≤x≤ 1,f ∈A
}
.
Prove that B is uniformly dense in
C0[0, 1] :={g∈C[0, 1]|g(0) = 0}.
Proof. Deﬁne B′ ={F (x)| F (x) =
∫x
0 f(t)dt, 0≤ x≤ 1,f ∈ C[0, 1]}. First show B is dense in
B′.
For everyF∈B′, G =B, F (x) =
∫x
0 f(t)dt and G(x) =
∫x
0 g(t)dt. Then
‖F (x)−G(x)‖∞≤
∫ 1
0
|f−g|dt≤‖f−g‖∞.
Since A is dense in C[0, 1], then‖f−g‖∞ <ϵ so‖F−G‖∞ <ϵ . So B is indeed dense in B′.
Then we will show B′ is an algebra (in order to use Stone-Weierstrass). Let F,G∈B′ so
F (x)G(x) =
∫ x
0
f(t)dt
∫ x
0
g(s)ds =
∫ x
0
∫ x
0
f(t)g(s)dsdt =
∫ x
0
F (t)g(t)+G(t)f(t)dt =
∫ x
0
∫ t
0
f(s)g(t)+g(s)f(t)dsdt.
Since F (t)g(t) +G(t)f(t)∈C[0, 1] then FG∈B′.
Also, x =
∫ 1
0 1dt∈B′ so B′ separates points.
By Stone-Weierstrass,B′ is dense in C0[0, 1] since any function F∈B′, F (0) = 0. So B is dense
in C0[0, 1].
(c) Prove that the span of {sin(nx)|n∈ N} is dense in C0[0, 1].
Proof. sin(nx) =
∫x
0 n cos(nx)dt. From part (b), it is suﬃcient to show
A = span{n cos(nx)} = span{cos(nt)}
is dense in C[0, 1]. A is an algebra:
• cos(nt) cos(mt) = 1
2
(
cos((m +n)t) + cos((m−n)t)
)
∈A
• cos(t) separates [0, 1] (since 1 <π/ 2) so A is dense in C[0, 1].
58

10 JANUARY 2015 Kari Eiﬂer
10 January 2015
Problem 1. Letf∈L1(R). If
∫ b
a
f(x)dx = 0
for all rational numbers a<b , prove that f(x) = 0 for almost all x∈ R.
Proof. Let E+ :={x| f(x) > 0}. Assume m(E+) > 0 (the same argument will show E− :={x|
f(x)< 0} has measure zero).
There exists some n such that E+∩ [n,n + 1] has positive measure. Consider F closed in R and
F⊆E+∩[n,n +1] with m(F )> 0. Then [n,n +1]\F is open in [n,n +1]. Thus, [n,n +1]\F =∪∞
n=1In
for In being disjoint open intervals in [n,n + 1].
For allIn = (an,bn), there exists some (ani)i, (bni)i⊆ Q such that ani→an and bni→bn. Since
∫ bn
an
f(x)dx =
∫
R
f(x)χ[an,bn]dx lim
i
f(x)χ[ani,bni ] =f(x)χ[an,bn]
then|f(x)χ[ani,bni ]≤|f(x)|∈ L1 so by Dominated Convergence Theorem,
∫bn
an
f(x)dx = 0.
Since
∫
Ff(x)dx >0, by condition we know
∫n+1
n f(x)dx = 0 for all n. So then
∫
[n,n+1]\Ff(x)dx <
0.
So there exists some Im = (am,bm) such that
∫
Im
f(x)dx< 0. Contradiction!
Proof #2 as in Problem 3 from August 2014, not restricted to rationals with f∈L1.
For every open U, write U =∪∞
n=1(an,bn) for disjoint open intervals, so
∫
U
f(x)dx =
∞∑
n=1
∫ bn
an
f(x)dx = 0.
For every compact K⊆ (a,b ) then (a,b )\K is open in R and
∫
K
f(x)dx =
∫ b
a
f(x)dx−
∫
(a,b)\K
f(x)dx
(because each is ﬁnite). Suppose E+ ={x| f(x) > 0} has positive measure. Since E+ =∪nEn
whereEn ={x|f(x)> 1/n} so there must exist some n such that m(En)> 0.
By inner regularity, there exists some K⊆En with m(K)> 0. Then
0 =
∫
K
f(x)dx>
∫
K
1
ndx = 1
nm(K)> 0
59

10 JANUARY 2015 Kari Eiﬂer
Contradiction!
Problem 2. Let{gn}∞
n=1 and g be in L1(R) and satisfy
lim
n→∞
‖gn−g‖1 = 0.
Prove that there is a subsequence of {gn}∞
n=1 that converges pointwise almost everywhere to g.
Proof. Step 1: Suppose gn→g in L1. Let En,ϵ ={x||fn(x)−f(x)|≥ ϵ}. Then
∫
|fn−f|≥
∫
En,ϵ
|fn−f|≥ ϵµ(En,ϵ)
So then µ(En,ϵ)≤ 1
ϵ
∫
|fn−f|→ 0.
Step 2: We will show that if gn→g in measure, then there exists a subsequence that converges to g
pointwise almost everywhere.
Suppose for every ϵ> 0, µ({x||fn(x)−f(x)|≥ ϵ})→ 0. Choose a subsequence {gnk} such that if
Ej ={x||gnj(x)−gnj+1(x)|> 2−j}
satisﬁes µ(Ej)< 2−j. Let Fk =∪∞
j=kEj so µ(Fk)≤∑∞
j=k 2−j≤ 21−k. Let F =∩kFk so µ(F ) = 0.
Forx /∈Fk and for i≥j≥k then
|gni(x)−gnj(x)|≤
i−1∑
𝓁=j
|gn𝓁(x)−gn𝓁+1(x)|≤
i−1∑
𝓁=j
2𝓁≤ 2−j→ 0 as k→∞.
So gnk is pointwise Cauchy on x /∈F , so let
f(x) =
{
limgnk(x) x /∈F
0 otherwise
So gnk→f almost everywhere and gn→f in measure since
µ({x||gn(x)−f(x)|≥ ϵ})≤µ({x||gn(x)−gn𝓁(x)|≥ ϵ/2})| {z }
→0
+µ({x||gn𝓁(x)−f(x)|≥ ϵ})| {z }
→0
and
µ({x||f(x)−g(x)|≥ ϵ})≤µ({x||f(x)−gn(x)|≥ ϵ/2}| {z }
→0
+µ({x||gn(x)−g(x)|≥ ϵ/2})| {z }
→0
60

10 JANUARY 2015 Kari Eiﬂer
so f =g almost everywhere. Thus, {gnk} converges to g almost everywhere.
Problem 3. Let (X,M,µ ) be a measure space with µ(X)<∞. Let N⊆M be a σ-algebra. If f≥
0 isM-measurable and µ-integrable then prove that there exists an N -measurable and µ-integrable
function g≥ 0 so that
∫
E
gdµ =
∫
E
fdµ, E ∈N .
Proof. Deﬁne ν(E) =
∫
Efdµ a ﬁnite positive measure on (X,N,µ ). Then since µ(E) = 0, ν(E) = 0
so ν≪µ.
Then by Radon-Nikodym Theorem, there exists some g : X→ [0,∞) andN -measurable and g∈
L1(µ) such that ν(E) =
∫
Egdµ. Then
ν(E) =
∫
E
fdµ =
∫
E
gdµ ∀E∈N .
Note: Folland doesn’t mention positive but there are other versions that give positive.
Problem 4. (a) State the closed graph theorem.
Proof. See wikipedia.
(b) If H is a Hilbert space and T :H→H is a linear operator satisfying
⟨Tx,y⟩ =⟨x,Ty⟩, x,y ∈H,
then prove that T is bounded.
Proof. Let xn→x and Txn→y. We want to show Tx =y.
⟨Txn,z⟩| {z }
→⟨y,z⟩
=⟨xn,Tz⟩→⟨ x,Tz⟩ =⟨Tx,z⟩.
So⟨Tx−y,z⟩ = 0 for all z∈H so then Tx−y = 0 and so Tx =y.
Problem 5. Letf,g ∈L1(R). Prove that h∈L1(R), where h(x) is deﬁned by
h(x) =
∫
R
f(y)g(x−y)dy
whenever this integral is ﬁnite.
Proof. We want to show that
∫
R|h(x)|dx =
∫
R
⏐⏐∫
Rf(y)g(x−y)dy
⏐⏐dx< ∞. Indeed,
61

10 JANUARY 2015 Kari Eiﬂer
∫
R
⏐⏐⏐⏐
∫
R
f(y)g(x−y)dy
⏐⏐⏐⏐dx≤
∫
R
∫
R
|f(y)||g(x−y)|dydx
=
∫
R
|f(y)|
(∫
R
|g(x−y)|dx
)
dy
=
∫
R
|f(y)|‖g‖1dy
=‖g‖1
∫
R
|f(y)|dy
=‖g‖1‖f‖1 <∞.
Problem 6. Letf,g ∈C[0, 1] with f(x)<g (x) for all x∈ [0, 1].
(a) Prove that there is a polynomial p(x) so that
f(x)<p (x)<g (x), x ∈ [0, 1].
Proof. Let ϵ = inf{g(x)−f(x)|x∈ [0, 1]}. Since h(x) = g(x)−f(x)> 0 on [0, 1] and attains a
minimum on the compact set [0, 1] then the inf is attained and thus is positive. So ϵ> 0.
By Stone-Weierstrass, polynomials are dense in C[0, 1] so there exists a polynomial p(x) such
that
‖‖‖p−
(
f +g
2
)‖‖‖
∞
<ϵ/ 2. Then
p(x)< f(x) +g(x)
2 + ϵ
2≤ 1
2
(
f(x) +g(x) + (g(x)−f(x))
)
= 1
2(2g(x)) =g(x).
p(x)> f(x) +g(x)
2 − ϵ
2 > 1
2
(
f(x) +g(x)− (g(x)−f(x))
)
= 1
2(2f(x)) =f(x).
So f(x)<p (x)<g (x).
Remark: Let M = max{g(x)−f(x)} then
|g(x)−f(x)|≤
⏐⏐⏐⏐g(x)−
(f +g
2
)
(x)
⏐⏐⏐⏐ +
⏐⏐⏐⏐
(f +g
2
)
(x)−p(x)
⏐⏐⏐⏐< M
2 +ϵ.
Alternative Proof. Let M := minx∈[0,1]g(x)−f(x). By Stone-Weierstrass, there exists some ˜p(x)
polynomial such that‖˜p(x)−g(x)‖∞ <M/ 3. Let p(x) = ˜p(x)−M/2. Then
g(x)−p(x) =g(x)− ˜p(x) +M
2 >−M
3 + M
2 = M
6 > 0.
p(x)−f(x) =p(x)−g(x)+g(x)−f(x) = ˜p(x)−g(x)−M
2 +
(
g(x)−f(x)
)
>−M
3 −M
2 +M = M
6 > 0.
So f(x)<p (x)<g (x).
62

10 JANUARY 2015 Kari Eiﬂer
(b) Prove that there is an increasing sequence of polynomial {pn(x)}∞
n=1 so that
f(x)<p n(x)<g (x), x ∈ [0, 1],
and pn→g uniformly on [0, 1].
Proof. Find p1 such taht g− 1
2 < p1 < g with
‖‖p1−
(g+g−1
2
)‖‖ < 1
4. Then |g(x)−p1(x)| <
1
4 + 1
4 = 1
2.
Recursively ﬁnd a polynomial pn such that pn−1 < pn < g with
‖‖‖pn−
(
g+pn−1
2
)‖‖‖ < 1
2n−1 ,
implying
|g(x)−pn(x)|< Mn−1
2 + 1
2n+1 = 1
2n+1 + 1
2n+1 = 1
2n.
So Mn < 1
2n . Then for every ϵ> 0 choose N such that 1
2N <ϵ , so for all n>N
|pn(x)−g(x)|< 1
2N <ϵ ∀x∈ [0, 1].
Alternative Proof. From part (a) we can ﬁnd f(x) < p1(x) < g(x). Repeating, we can ﬁnd
p1(x)< p2(x)< g(x). By requiring ϵn instead of M, in‖˜p(x)−g(x)‖∞ < ϵand letting ϵn→ 0,
we get
‖pn(x)−g(x)‖∞≤‖pn(x)− ˜pn(x)‖∞ +‖ ˜pn(x)−g‖∞ < ϵn
2 + ϵn
3 = 5
6ϵn→ 0.
Problem 7. If f∈L2(R), g∈L3(R), and h∈L6(R) then prove that the product fgh is in L1(R).
Proof. Note:
‖‖|f|k‖‖
p =
(∫
|f|kpdx
)1/p
=
(∫
|f|kpdx
) 1
kpp
=‖f‖p
kp.
Then it follows that
‖fgh‖1≤‖f‖2‖gh‖2≤‖f‖2‖|g|2|h|2‖1/2
1 ≤‖f‖2
(
‖|g|2‖p=3/2‖|h|2‖q=3
)1/3
≤‖f‖2
(
‖g‖3‖h‖6
)1/3
<∞.
Where we use p = 3/2, q = 3 so 1
p + 1
q = 2
3 + 1
3 = 1.
Problem 8. (a) A point y in a metric space Y is isolated if the set {y} is both open and closed in
Y . Prove taht y∈Y is isolated if and only if the complement {y}C is not dense in Y .
Proof.⇒) If y is isolated, then{y} is open. But {y}c∩{y} =∅ so{y}c is not dense.
⇐) Trivially,{y} is closed since we’re in a metric space. Suppose {y}c is not dense in Y . Then
there exists an open U⁄=∅ such that U∩{y}c =∅ (since A is dense in Y ⇔ for all open U⁄=∅,
U∩A⁄=∅).
But if U∩{y}c =∅ then U⊆{y}cc ={y} so U ={y} is open.
63

10 JANUARY 2015 Kari Eiﬂer
(b) Let X be a countable nonempty complete metric space. Prove that the set of isolated points is
dense in X.
Proof. Let Y ⊆X be the set of isolated points. Let X\Y ={zj}∞
j=1 (or{zj}n
j=1).
Since the singleton{zk} is not an isolated point, by (a) we know {zk}c is dense in X, so{zk}c =
X. So each {zk}c is open and dense in X.
By Baire-Category,Y =∩∞
j=1{zj}c (or∩n
j=1{zj}c) is also dense in Y .
Problem 9. Suppose that f ∈ Lp(R) for all p∈ (1, 2) and that supp∈(1,2)‖f‖p <∞. Prove that
f∈L2(R) and that
lim
p→2−
‖f‖p =‖f‖2.
Proof. Let A ={x|| f(x)|≥ 1}, B ={x|| f(x)| < 1}. Then by Monotone Convergence Theorem,∫
A|f|pdx↗
∫
A|f|2dx.
Let pn ↑ 2. WLOG assume p1 = 3/2. We know on B,|f|p ≤ |f|3/2 ∈ L1(B). By Dominated
Convergence Theorem,
∫
B|f|pdx→
∫
B|f|2dx which implies
∫
R|f|pdx→
∫
R|f|2dx.
Therefore,‖f‖p
p→‖f‖2
2 so‖f‖p/2
p →‖f‖2 as p→ 2.
Also, since M = supp∈(1,2)‖f‖p <∞, then‖f‖p/2−1
p ≤Mp/2−1 for all p∈ (1, 2).
Then Mp/2−1→ 1 as p→ 2 which implies‖f‖p/2
p −‖f‖p→ 0 as p→ 2.
So then,‖f‖p→‖f‖2 as p→ 2 and‖f‖2 <∞ since M <∞.
Problem 10. Let (X,‖·‖ ) be a normed vector space with a subspace Y and let‖·‖ 1 be another
norm on Y that satisﬁes
1
K‖y‖1≤‖y‖≤ K‖y‖1, y ∈Y,
whereK >1 is a ﬁxed constant. Deﬁne S to be the set of linear functionals φ :X→ R satisfying
(i) |φ(y)|≤‖ y‖1, y∈Y ,
(ii) |φ(x)|≤ K‖x‖, x∈X.
Prove the following statements:
(a) ‖x‖2 := sup{|φ(x)|| φ∈S} deﬁnes a norm on X.
Proof. See August 2015
(b) For y∈Y ,‖y‖1 =‖y‖2.
Proof. See August 2015
64

11 AUGUST 2014 Kari Eiﬂer
(c) The norms ‖·‖ and‖·‖ 2 are equivalent on X.
Proof. See August 2015
11 August 2014
Problem 1. Forn∈ N, let fn : [0, 1]→ R be continuous, and assume that for every x∈ [0, 1]
the sequence (fn(x)) is decreasing. Suppose that fn converges pointwise to a continuous function f.
Show that this convergence is uniform.
Proof. WLOG: by replacing fn byfn(x)−f(x), these are still continuous and decreasing pointwise.
So we want to prove fn ⇒ 0.
This is precisely Dini’s Theorem (aka freebie question).
Fix ϵ> 0 and let Un =f−1
n ((−1,ϵ )) ={x∈X|gn(x)<ϵ} which is open. Then for all x, fn(x)↘ 0
so there exists N such that for all n≥N,|fn(x)|<ϵ which implies x∈Un.
So [0, 1] =∪nUn. By compactness of [0 , 1], there exists a ﬁnite subcover Un1,Un2,...,U nk for n1 <
n2 <...<n k but since Un⊆Un+1 then Un1⊆Un2⊆... ⊆Unk.
Therefore, [0, 1]⊆Unk =:UN so for all x∈ [0, 1], then x∈f−1
N ((−1,ϵ ))⇔|fN(x)|<ϵ .
Decreasing fn implies that for all n≥N,|fn(x)|<ϵ for all x∈ [0, 1].
Problem 2. Letf∈L1(0,∞). For x> 0, deﬁne
g(x) =
∫ ∞
0
f(t)e−txdt.
Prove that g(x) is diﬀerentiable for x> 0 with derivative
g′(x) =
∫ ∞
0
−tf(t)e−txdt.
Proof. Since
∫ ∞
0
∫ x
0
|tf(t)e−ty|dydt =
∫ ∞
0
t|f(t)|
(∫ x
0
e−tydy
)
dt =
∫ ∞
0
−e−tx
| {z }
≤1
|f(t)|dt+
∫ ∞
0
|f(t)|dt≤ 2
∫ ∞
0
|f(t)|dt< ∞.
By Fubini,h(x) =
∫∞
0
∫x
0−tf(t)e−tydtdy =
∫∞
0 f(t)e−txdt +c.
So h(x) =g(x) +c.
From the deﬁnition of h, we know h′(x) = g′(x) and thus g(x) is diﬀerentiable. And h is diﬀeren-
tiable since it’s absolutely continuous.
65

11 AUGUST 2014 Kari Eiﬂer
Problem 3. Letf : R→ R be a Lebesgue integrable function such that
∫ b
a
f(x)dx = 0 for every a<b.
Show that f(x) = 0 for almost every x∈ R.
Proof. See question 1 from January 2015.
Problem 4. Letf be Lebesgue measurable on [0, 1] with f(x) > 0 a.e. Suppose (Ek) is a sequence
of measurable sets in [0, 1] with the property that
∫
Ek
f(x)dx→ 0 as k→∞ .
Prove that m(Ek)→ 0 as k→∞ .
Proof. Let Fm ={x|f(x)≥ 1/m} so Fn⊆Fn+1.
Since f(x)> 0 almost everywhere, then
m (∪∞
n=1Fn) = lim
n
m(Fn) = 1.
Fix ϵ> 0, so there exists N such that m(Fc
n)<ϵ/ 2 for n≥N. Now,
1
Nm(Ek∩FN)≤
∫
Ek∩FN
f(x)dx≤
∫
Ek
f(x)dx→ 0 as k→∞.
So there exists some K such that m(Ek∩FN)<ϵ/ 2 for all k≥K. Thus,
m(Ek) =m(EK∩FN) +m(Ek∩Fc
N)< ϵ
2 + ϵ
2 =ϵ ∀k≥K.
Problem 5. Let (fn) be a sequence of continuous functions on [0, 1] such that for each x∈ [0, 1]
there is an N =Nx so that
fn(x)≥ 0 for all n≥Nx.
Show that there is an open nonempty set U⊂ [0, 1] and an N∈ N, so that fn(x)≥ 0 for all n≥ N
and all x∈U.
Proof. Let
En :={x|fm(x)≥ 0∀m≥n} =
∞⋂
n=m
{x|fn(x)≥ 0}
66

11 AUGUST 2014 Kari Eiﬂer
so En is closed and En⊇ En+1. For all x∈ [0, 1] there exists N = Nx such taht fm(x)≥ 0 for all
m≥N. Thus, x∈EN.
Then, [0, 1] =∪∞
n=1En. Since [0, 1] is compact, by Baire-Category we know there exists N such that
EN
◦
⁄=∅ (i.e. E◦
N⁄=∅).
Let U =E◦
N be open, non-empty so for all x∈U, fn(x)≥ 0 for all n≥N.
Problem 6. (a) Deﬁne the w∗-topology on the dual X∗ of a Banach space X.
Proof. See wikipedia!
(b) Let X be an inﬁnite dimensional Banach space. What is the w∗-closure of
SX∗ ={x∗∈X∗|‖x∗‖ = 1}?
(as usual, prove your answer.)
Proof. Claim: SX∗
w∗
=BX∗.
We know for any x1,x 2,...,x n∈ X, there exists some x∗
0⁄= 0 such that x∗
0(xi) = 0. Indeed,
if this were not true then otherwise, x∗
0(xi) ⁄= 0 for some i, let ϕ : X∗ → Rn be ϕ(x∗) =
(x∗(x1),...,x ∗(xn)) then ϕ is injective so dim(X∗)≤ dim(Rn) =n. Contradiction, so true.
Now for any x∗∈BX∗, consider it’s neighborhood (open under the w∗-neighborhood)
V =∩n
i=1{y∗∈X∗|| ˆxi(x∗−y∗)| =|x∗(xi)−y∗(xi)|<ϵ}
for each{xi}n
i=1 choose such an x∗
0⁄= 0 from the claim.
Consider the line{x∗ +tx∗
0|t∈ R} in X∗.
Since for any ˆxi,
ˆxi(x∗ +tx∗
0−x∗) =t ˆxi(x∗
0) =tx∗
0(xi) = 0<ϵ.
Then{x∗ +tx∗
0| t∈ R}⊆ V . Since ‖x∗ +tx∗
0‖ is continuous about t, then we can ﬁnd t0 such
that‖x∗ +t0x∗
0‖ = 1⇒ V∩SX∗⁄=∅.
Since any neighborhood of x∗ contains a neighborhood of the form V as above (i.e. these V ’s
are a neighborhood basis) then BX∗⊆SX∗
w∗
.
On the other hand, for any x∗
0 ∈ BX∗, by Hahn-Banach separation Theorem, we know there
exists x∈X and c∈ R such that x∗(x)<c<x ∗
0(x) for all x∗∈BX∗.
Then for all{x∗
n}⊆ BX∗, x∗
n(x)≤c < x∗
0(x). Therefore, x∗
0 isn’t an accumulation point of BX∗
which implies BX∗
w∗
=BX∗. Thus, SX∗
w∗
⊆BX∗
w∗
=BX∗ so BX∗ =SX∗
w∗
.
Problem 7. (a) State the Riesz Representation Theorem for the dual L∗
p(µ) of Lp(µ), 1≤p< ∞.
Proof. See Wikipedia!
67

11 AUGUST 2014 Kari Eiﬂer
(b) Let µ be a ﬁnite measure on the measurable space (Ω, Σ). Prove the following part of the above
theorem:
If F∈L∗
p(µ), then there exists an h∈L1(µ) so that
F (χA) =
∫
A
hdµ for all A∈ Σ.
Proof. Let ν(A) =F (χA). The goal is to show ν is a σ-ﬁnite signed measure.
(a) ν(∅) =F (χ∅) =F (0) = 0
(b) Let {Ei} be disjoint, let E =∪∞
i=1Ei. Then
ν(E)−
n∑
i=1
ν(Ei) =F (χE)−F
( n∑
i=1
χi
)
≤‖F‖L∗p
‖‖‖‖‖
χE−
n∑
i=1
χi
‖‖‖‖‖
p
≤‖F‖L∗p
‖‖‖‖‖
∞∑
i=n+1
χi
‖‖‖‖‖
p
=‖F‖L∗pµ
(
∪∞
i=n+1Ei
)1/p
→ 0 as n→∞.
Therefore, ν(E) =∑∞
i=1ν(Ei).
When µ(A) = 0, then
ν(A) =F (χA)≤‖F‖L∗p‖χA‖p =‖F‖L∗pµ(A)1/p = 0.
So ν≪µ.
Then from the Radon-Nikodyn Theorem, there exists some h∈L1(µ) such that ν(A) =
∫
Ahdµ.
So
F (χA) =ν(A) =
∫
A
hdµ.
Problem 8. Assume that (xn) is a weakly converging sequence in a Hilbert space H. Show that
there is a subsequence (yn) of (xn) so that
1
n
n∑
j=1
yj
converges in norm.
68

11 AUGUST 2014 Kari Eiﬂer
Proof. WLOG xn → 0 weakly (⟨xn,y⟩ → ⟨0,y⟩ for all y ∈ H) and we know‖xn‖ is bounded,
supn‖xn‖≤ C. For n>m ,
‖‖‖‖‖‖
1
m
m∑
j=1
yj− 1
n
n∑
j=1
yj
‖‖‖‖‖‖
2
=
⟨
1
m
m∑
j=1
yj− 1
n
n∑
j=1
yj, 1
m
m∑
j=1
yj− 1
n
n∑
j=1
yj
⟩
=
⟨( 1
m− 1
n
) m∑
j=1
yj− 1
n
n∑
j=m+1
yj,
( 1
m− 1
n
) m∑
j=1
yj− 1
n
n∑
j=m+1
yj
⟩
≤
( 1
m− 1
n
)2
‖‖‖‖‖‖
m∑
j=1
yj
‖‖‖‖‖‖
2
+ 2
⏐⏐⏐⏐⏐⏐
⟨( 1
m− 1
n
) m∑
j=1
yj, 1
n
n∑
j=m+1
yj
⟩⏐⏐⏐⏐⏐⏐
+
( 1
n
)2
‖‖‖‖‖‖
n∑
j=m+1
yj
‖‖‖‖‖‖
2
.
Now by induction, we can choose yj such that|⟨yj,∑m
n=1yn⟩| < 2−j for all m≤ j− 1. Pick y1
randomly.
Since⟨xn,y⟩→⟨ 0,y⟩ for all y∈H , then we can ﬁnd y2 such that⟨y2,y 1⟩< 2−2.
Similarly, ﬁndy3 such that⟨y3,y 1 +y2⟩< 2−3 and⟨y3,y 1⟩< 2−3, etc. Then
‖‖‖‖‖‖
m∑
j=1
yj
‖‖‖‖‖‖
2
=
⟨ m∑
j=1
yj,
m∑
j=1
yj
⟩
=⟨ym,ym⟩+⟨ym,
m−1∑
j=1
yj⟩+... +⟨y1,y 1⟩≤
m∑
j=1
‖yj‖2+
m∑
j=1
2−j <
m∑
j=1
‖yj‖2+2.
Therefore,
( 1
m− 1
n
)2
‖‖‖‖‖‖
m∑
j=1
yj
‖‖‖‖‖‖
2
≤ 1
m2


m∑
j=1
‖yj‖2 + 2

< 1
m2 (mc + 2)→ 0 as m→∞.
Similar argument holds for
( 1
n
)2‖‖‖∑n
j=m+1yj
‖‖‖
2
.
Finally,
⏐⏐⏐⏐⏐⏐
⟨( 1
m− 1
n
) m∑
j=1
yj, 1
n
n∑
j=m+1
yj
⟩⏐⏐⏐⏐⏐⏐
≤ 1
n
( 1
m− 1
n
) n∑
j=m+1
⟨
yj,
m∑
k=1
yk
⟩
≤ 1
n
( 1
m− 1
n
) n∑
j=m+1
2−(m+1)
≤ 1
n
( 1
m− 1
n
)
→ 0
69

11 AUGUST 2014 Kari Eiﬂer
So then
‖‖‖ 1
m
∑m
j=1yj− 1
n
∑n
j=1yj
‖‖‖
2
→ 0 as n,m→∞ so it’s Cauchy and therefore converges.
Problem 9. Show that a linear functional φ on a Banach space X is continuous if and only if {x∈
X|φ(2x) = 3} is norm closed.
Proof.⇒) A ={x|φ(2x) = 3)} ={x| 2x∈φ−1({3})}. Let ψ(x) =φ(2x) so A =ψ−1(φ−1({3})).
⇐) We want to show ker(φ) is closed. Note that {x∈X|φ(2x) = 3} ={x∈X|φ(x) = 3/2}.
Pick some a∈X such that φ(a) = 3/2. Then clearly
a + ker(φ)⊆{x∈X|φ(x) = 3/2}
and if φ(x) = 3/2 then φ(x−a) = 0 so x =a + (x−a)∈a + ker(φ).
Thus,a + ker(φ) ={x∈X|φ(2x) = 3}. Therefore ker(φ) ={x∈X|φ(2x) = 3}−a which is closed.
Then
φ′ :X/ ker(φ)→ R
x + ker(φ)↦→φ(x)
is an isomorphism. Let π :X→X/ kerφ which is also continuous, so φ =φ′◦π is continuous.
Problem 10. LetC 1[0, 1] be the space of functions f∈C[0, 1] such taht f′ exists and is continuous
in [0, 1]. The space C 1[0, 1] is given the supremum norm. Deﬁne T : C 1[0, 1]→ C[0, 1] by Tf =
f′ for f ∈ C 1[0, 1]. Show that T has a closed graph and that T is not bounded. Decide if C 1[0, 1]
(together with the supremum norm) is a Banach space or not. (Explain your answer).
Proof. Let fn→f and Tfn→f′
n→g in‖·‖ ∞.
fn(x) =
∫ x
0
f′
n(t)dt +fn(0) f(x) =
∫ x
0
f′(t)dt +f(0)
Since fn→f then fn(0)→f(0). Let G =
∫x
0 g(t)dt +f(0). Then
‖f−G‖≤‖ f−fn‖ +‖fn−G‖≤‖ f−fn‖ +
∫ x
0
‖fn−g‖∞≤‖f−fn‖ +‖fn−g‖∞→ 0.
So f′ =g meaning T has a closed graph.
To seeT is not bounded, consider fn =xn so‖fn‖∞ = 1 but‖Tfn‖ =‖nxn−1‖∞ =n→∞ .
Thus, by the closed graph theorem, C 1[0, 1] is not a Banach space.
70

12 JANUARY 2014 Kari Eiﬂer
12 January 2014
Problem 1. Let (X,M,µ ) be a non atomic masure space with µ(X) > 0. Show that there is a
measurablef :X→ [0,∞), for which
∫
f(x)dµ(x) =∞.
Proof. TakeX =E1⊇E2⊇E3⊇... such that µ(E1)>µ (E2)>...> 0. Deﬁne
f(x) =
{
µ(En\En+1)−1 if x∈En\En+1
0 if x∈∩∞
n=1En
Then
∫
f(x)dx =∑∞
n=1 1 =∞.
Problem 2. Assume that µ is a ﬁnite measure on Rn. Prove that there is a closed set A⊂ Rn with
the property that for each closed B ⊊A it follows that µ(A\B)⁄= 0.
Proof. Since Rn is a locally compact Hausdorﬀ space and µ is ﬁnite, µ is Radon (and regular). If
µ(Rn) =a (so V ⁄= Rn) then we can set
Mn :=
{
U|U is open and µ(U)< a
n
}
and V :=∪∞
n=1{U|U∈Mn} so V is open. Let A =Vc is closed.
For anyB ⊊A, A\A∩Bc. Assume µ(A\B) = 0 then
µ(A\B) = inf{µ(U)|A\B⊆U,U open} = 0.
Then there exists U⊆ V such that A\B⊆ U. Then A\B∩U⊆ A∩U⊆ A∩V =∅, so A\B =∅.
Contradiction!
Problem 3. For a nonnegative function f∈L1([0, 1]), prove that
lim
n→∞
∫ 1
0
n
√
f(x)dx =m({x|f(x)> 0}).
Proof. Let
E1 ={x|f(x)≥ 1}
E2 ={x| 0<f (x)< 1}
E3 ={x|f(x) = 0}
71

12 JANUARY 2014 Kari Eiﬂer
Then
∫ 1
0
f(x)1/ndx =
∫
E1
f(x)1/ndx +
∫
E2
f(x)1/ndx +
∫
E3
f(x)1/ndx
For the ﬁrst integral on E1, limnf(x)1/ndx = 1 and|f(x)1/n|≤| f(x)|∈ L1, so by DCT,
∫
E1
f(x)1/ndx =∫
E1
dx =m(E1).
For the second integral on E2, limnf(x)1/n = 1 and|f(x)1/n|≤ 1∈L1 so again by DCT,
∫
E2
f(x)1/ndx =∫
E2
dx =m(E2). Therefore,
∫ 1
0
f(x)1/ndx =m(E1) +m(E2) =m({x|f(x)> 0}).
Problem 4. Letf be Lebesgue integrable on (0, 1). For 0<x< 1 deﬁne
g(x) =
∫ 1
x
t−1f(t)dt.
Prove that g is Lebesgue integrable on (0, 1) and that
∫ 1
0
g(x)dx =
∫ 1
0
f(x)dx.
Proof. Notice that
∫ 1
0
∫ t
0
t−1f(t)dtdx =
∫ 1
0
|f(t)|dt< ∞
since f∈L1(0, 1) so then by Fubini, we have that
∫ 1
0
∫ 1
x
t−1f(t)dtdx =
∫ 1
0
∫ t
0
t−1f(t)dxdt.
So we have
∫ 1
0
g(x)dx =
∫ 1
0
∫ 1
x
t−1f(t)dtdx =
∫ 1
0
∫ t
0
t−1f(t)dxdt =
∫ 1
0
f(t)dt.
Problem 5. Assume that ν and µ are two ﬁnite measures on a measurable space (X,M). Prove
that
72

12 JANUARY 2014 Kari Eiﬂer
ν <<µ⇔ lim
n→∞
(ν−nµ)+ = 0.
Proof.⇐) Let µ(E) = 0. Then for all ϵ> 0, there exists some N such that for all n≥N,
ϵ> (ν−nµ)+(E)≥ (ν−nµ)(E) =ν(E)−nµ(E)≥ν(E).
Letting ϵ approach 0, we have that ν(E) = 0 so that ν <<µ.
Problem 6. Let (pn) be a sequence of polynomials which converges uniformly on [0, 1] to some
function f, and assume that f is not a polynomial. Prove the limn→∞ deg(pn) = ∞, where deg(p)
denotes the degree of a polynomial p.
Proof. Assume to the contrary and consider the space P = span{1,x,x 2,...,x m} with (pn)⊆P .
Since{1,x,...,x m} are basis elements andP is ﬁnite dimensional, then any two norms are equiva-
lent onP and so if P =∑∞
k=0akxk, we can consider the two norms deﬁned by
‖P‖1 := sup|ak| ‖ P‖2 := sup
x∈[0,1]
|P (x)|
Since‖pnk−pn𝓁‖2→ 0, then‖pnk−pn𝓁‖1→ 0 so{ank} is Cauchy. Hense, P =∑m
𝓁=0a𝓁x𝓁 where
a𝓁 = limka𝓁
nk is a polynomial of degree at most m and pn converges uniformly to p. So therefore,
p =f. Contradiction!
Alternative proof. Assume not, so there exists some M such that for all N∈ N, there exists some
n≥ N such that deg(pn)≤ M. For N = 1, ﬁnd n1 such that deg(pn1)≤ M. For N = n1, ﬁnd n2
such that deg(pn2)≤M, etc.
Get a subsequence{pnk} such that deg(pnk)≤M.
Since pn converges to f uniformly on [0, 1] then pnk converges to f uniformly on [0, 1].
We writepni :=∑m
j=1aijxj, then
f = lim
i→∞
m∑
j=i
aijxj =
m∑
j=1
lim
i→∞
aijxj =
∑
j=1
xj where bj = lim
i→∞
aij.
To see limi→∞aij exists: let X =Pp| p polynomial with degree ≤ M} is a ﬁnite dimensional
subspace ofC[0, 1] hense closed so f∈X so f is a polynomial.
Problem 7. Let (fn) be sequence of non zero bounded linear functionals on a Banach space X.
Show that there is an x∈X so that fn(x)⁄= 0, for all n∈ N.
Proof. Let En ={x|fn(x)} which is closed in X. Assume the result is not true, so for every x∈X,
there exists some n such that fn(x) = 0 implies x∈En, that is, X =∪nEn.
73

12 JANUARY 2014 Kari Eiﬂer
Since X is a Banach space, then by Baire Category Theorem, there exists some n such that∅ ⁄=
E◦n =E◦
n.
Thus, there exists some r> 0, x∈X such that B(r,x )⊆En.Then for all y∈X,
r y
‖y‖ +x∈x +B(r, 0) =B(r,x )
so then if fn(r y
‖y‖ +x) = 0, then r
‖y‖fn(y) =−fn(x) = 0 so fn(y) = 0 so fn = 0.
Thus, by Baire Category,∪Cn⁄=X. Contradiction!
Problem 8. Assume that T : 𝓁1→ 𝓁2 is bounded, linear and one-to-one. Prove that T (𝓁1) is not
closed in 𝓁2.
Proof. If T (𝓁1) is closed, then T (𝓁1) is a hilbert space. Since T :𝓁1→T (𝓁1) is bijective, by the open
mapping theorem. T is open and T−1 is bounded so T is an isomorphism. Then 𝓁1∼=T (𝓁1). But 𝓁1
is not reﬂexive and T (𝓁1) is reﬂexive, so contradiction.
Alternative Proof. T (𝓁1) is closed, hence complete. So T : 𝓁1→ T (𝓁1) is bijective, so by the open
mapping theorem, T is an open map so T (𝓁1) is both open and closed in 𝓁2. Hence, T (𝓁1)∼= 𝓁2 so
then 𝓁1∼=𝓁2. Contradiction!
Problem 9. For a uniformly bounded sequence (fn) in C[0, 1] (i.e. supn∈N supξ∈[0,1]|fn(ξ)| <∞)
show that fn converges weakly to 0 ⇔ limn→∞fn(ξ) = 0 for all ξ∈ [0, 1].
Is the equivalence true if we do not assume that (fn) is uniformly bounded, explain?
Proof. This question is the same as 3 from August 2015.
⇒)C([0, 1])∗ =M[0, 1] for all ξ∈ [0, 1], δξ ∈M [0, 1]. So 0 = lim n
∫
fndδξ = limnfn(ξ) so then
limnfn(ξ) = 0 (note that this does not require uniformly boundedness!)
⇐) Fix µ∈M [0, 1], we want to show that
∫
fndµ→ 0. Since |fn(x)|≤ M for all x and all n, then
by dominated convergence theorem,
∫
fndµ→ 0.
Finally, considerhn given by connecting (0, 0), (1/n,n ), (2/n, 0) and (1, 0). So hn(ξ)→ for all xı∈
[0, 1]. But by taking Lebesgue measure,
∫
hn(x)dµ(x) = 1 so fn ↛ 0 weakly.
Problem 10. Assume that f is measurable and non negative function on [0, 1]2 and that 1≤ r <
p< ∞. Show that
(∫ 1
0
(∫ 1
0
fr(x,y )dy
)p/r
dx
)1/p
≤
(∫ 1
0
(∫ 1
0
fp(x,y )dx
)r/p
dy
)1/r
.
Hint: Let s =p/r, let 1<s′ <∞ be the conjugate of s and let
F : [0, 1]→ R+
0, x ↦→
∫ 1
0
fr(x,y )dy.
74

13 AUGUST 2013 Kari Eiﬂer
Then consider for an appropriate function h∈Ls′[0, 1] the product hF .
Proof. Let F (x) :=
∫ 1
0 fr(x,y )dy. Let h∈Ls′
[0, 1] with‖h‖s′ = 1 and h≥ 0. Then by Tonelli (since
Fh≥ 0), we have
∫ 1
0
F (x)h(x)dx =
∫ 1
0
∫ 1
0
fr(x,y )h(x)dydx
=
∫ 1
0
∫ 1
0
fr(x,y )h(x)dxdy
≤
∫ 1
0
‖fr(·,y )‖s‖h‖s′dy
=
∫ 1
0
(∫ 1
0
fp(x,y )dx
)r/p
dy
So then
∫ 1
0 F (x)h(x)dx≤
∫ 1
0
(∫ 1
0 fp(x,y )dx
)r/p
dy for all‖h‖s′ = 1, h≥ 0.
Notice that F≥ 0 so when‖˜h‖s′ = 1, we have
sup
‖˜h‖s′ =1
∫ 1
0
F (x)h(x)dx = sup
‖h‖s′ =1,h≥0
∫ 1
0
F (x)h(x)dx
Therefore,
sup
‖h‖s′ =1,h≥0
∫ 1
0
F (x)h(x)dx =‖F‖s =
(∫ 1
0
(∫ 1
0
fr(x,y )dy
)p/r)r/p
≤
∫ 1
0
(∫ 1
0
fp(x,y )dx
)r/p
dy
So then,
(∫ 1
0
(∫ 1
0
fr(x,y )dy
)p/r
dx
)1/p
=
(∫ 1
0
(∫ 1
0
fp(x,y )dx
)r/p
dy
)1/r
.
13 August 2013
Problem 1. Let 1≤ p≤∞ and let f ∈ Lp(R). For t∈ R, let ft(x) = f(x−t) and consider
the mapping G : R→ Lp(R) given by G(t) = ft. The space Lp(R) is equipped with the usual norm
topology.
(a) Show that G is continuous if 1≤p< ∞.
75

13 AUGUST 2013 Kari Eiﬂer
Proof. Since C∞
c (R) is dense in Lp(R) for 1 ≤ p <∞, we can choose g ∈ C∞
c (R) such that
‖g−f‖p <ϵ . Then
‖ftn−ft‖p≤‖ftn−gtn‖p +‖gtn−gt‖p +‖gt−ft‖p
It’s easy to see ‖ftn−gtn‖p and‖gt−ft‖p are small since‖g−f‖p <ϵ . For‖gtn−gt‖p, then
‖gtn−gt‖p =
(∫
R
|g(x−tn)−g(x−t)|pdx
)1/p
≤
(∫
A
ϵp
)1/p
=ϵµ(A)
where for each ﬁxed tn→t, we can ﬁnd a bounded set A⊆ R such that∪n suppgtn∪ suppgt⊆
A.
(b) Find an f for which the mapping G is not continuous when p =∞ (and justify your answer)
Proof. We will take f =χ[0,1], so
‖χ[0,1](tn)−χ[0,1](t)‖∞ =‖χ[tn,tn+1)−χ[t,t+1)‖∞ = 1 ∀n
although tn→t, we have‖·‖ ∞ ↛ 0.
(c) Let 1 ≤ p,q ≤ ∞be conjugate exponents (i.e. satisfying 1
p + 1
q = 1 ). Let f ∈ Lp(R) and
g∈Lq(R) and show that their convolution h =f∗g is continuous. Recall
h(t) =
∫ ∞
−∞
f(x)g(t−x)dx.
Proof. Letting gt(x) =g(t−x), then we have (by H¨ older)
|h(t)−h(tn)|≤
∫
R
|f(x)||g(t−x)−g(tn−x)|dx≤‖f‖p‖gt−gtn‖q
This goes to zero when 1 <p,q <∞ from part (a).
Also notice that
h(t) =
∫ ∞
−∞
f(x)g(t−x)dx =
∫ ∞
−∞
f(t−y)g(y)dy =g∗f.
So when p = 1, q =∞ the same is true.
Problem 2. (a) For f∈ CR([0, 1]), show that f≥ 0 if and only if ‖λ−f‖u≤ λ for all λ≥‖ f‖u,
where‖·‖ u denotes the uniform (supremum) norm.
Proof.⇒) Assume there exists some λ≥‖f‖u such that‖λ−f‖∞ >λ . Then there exists some
x∈ [0, 1] such that|λ−f(x)| =λ−f(x)>λ so then f(x)< 0. Contradiction!
⇐) If there exists some x such that f(x) < 0, then if λ≥‖ f‖∞ so λ > 0. Then ‖λ−f‖∞≥
λ−f(x)>λ . Contradiction!
76

13 AUGUST 2013 Kari Eiﬂer
(b) Suppose E ⊆ CR([0, 1]) is a closed subspace containing the constant function 1. For φ∈ E∗,
we deﬁne φ≥ 0 to mean φ(f)≥ 0 whenever f ∈ E and f ≥ 0. Show φ≥ 0 if and only if
‖φ‖ =φ(1).
Proof.⇒) We have
‖φ‖ = sup
‖f‖u=1
|φ(f)|≥ φ(1).
Also for‖f‖u = 1, we have 1−f≥ 0 so φ(1−f)≥ 0 implies φ(1)≥φ(f). Moreover, φ(1 +f) =
φ(1) +φ(f)≥ 0 and so φ(1)≥−φ(f) so then φ(1)≥|φ(f)|. Therefore, φ(1) =‖φ‖
⇐) φ(1) =‖φ‖≥| φ(f)| for all‖f‖u≤ 1. Assume there exists some f≥ 0 but φ(f)< 0.
By rescaling we can assume ‖f‖u < 1, so then
‖φ‖≥ φ
( 1−f
‖1−f‖
)
= 1
‖1−f‖(φ(1)−φ(f))≥φ(1)−φ(f)>φ (1) =‖φ‖
which contradicts!
(c) If φ ∈ E∗ and φ ≥ 0, show that there is a bounded linear functional ψ on CR([0, 1]) so that
ψ≥ 0 and the restriction of ψ to E is φ.
Proof. By Hahn-Banach, there exists some ψ which is an extension of φ such that‖ψ‖ =‖φ‖ =
φ(1) =ψ(1). So ψ≥ 0 follows from (b).
Problem 3. (a) Let µ and λ be mutually singular complex measures deﬁned on the same measur-
able space (X,M) and let ν =µ +λ. Show |ν| =|µ| +|λ|.
Proof. Let X = E⊔F be a disjoint union such that λ(F ) = mu(E) = 0. Let P2⊔N2 = E be
the Hahn-decomposition for λ. Let P3⊔N3 =F be the Hahn-decomposition for µ.
Then P1 =P2⊔P3, N1 =N2⊔N3 will be the Hahn-decomposition for ν =λ +µ. Then
ν+(A) =ν(A∩P2) +ν(A∩P3) =λ(A∩P2) +µ(A∩P3)
ν−(A) =ν(A∩N2) +ν(A∩N3) =λ(A∩N2) +µ(A∩N3)
So then
|ν|(A) =λ(A∩P2) +µ(A∩P3) +λ(A∩N2) +µ(A∩N3) =|µ|(A) +|λ|(A)
Therefore,|ν| =|µ| +|λ|.
(b) Construct a nonzero, atomless Borel measure on [0, 1] that is mutually singular with respect to
Lebesgue measure.
Proof. here. Maybe Cantor-Lebesgue?
77

13 AUGUST 2013 Kari Eiﬂer
Problem 4. Let (fn)∞
n=1 be a sequence of continuous functions on [0, 1] and suppose that for all
x∈ [0, 1], fn(x) is eventually nonnegative. Show that there is an open interval I⊆ [0, 1] such that
for all n large enough, fn is nonnegative everywhere on I.
Proof. Let UN =∩∞
n=Nf−1
n [0,∞) ={x| fn(x)≥ 0∀n≥ N}. This is closed. For every x∈ [0, 1],
fn(x) is eventually non-negative so [0, 1] =∪NUN.
By Baire-Category, there exists some N such that∅⁄ = UN
◦
= U◦
N. So there exists some open I⊆
U◦
N⊆ [0, 1] and then for all n≥N, fn≥ 0 on I.
Problem 5. Letµ be a nonatomic signed measure on a measure space (X, Ω), with µ(X) = 1 .
Show that there is a measureable subset E⊂X with µ(E) = 1/2.
Proof. First notice that for every ϵ> 0, there exists some E⊆X with µ(E)<ϵ . This is because we
can recursively divide our set into two non-trivial sets and chose the smaller one.
Therefore, for all n, we can ﬁnd a set En such taht 0 <µ (En)< 2−n. Let S ={E⊆X|µ(E)≤ 1
2}
ordered by inclusion.
Zorn’s Lemma implies that there exists a maximal element E. If µ(E) < 1
2 then we can ﬁnd some
F ⊆ Ec with 0 < µ(F ) < 1
2−µ(E) but then µ(F∪E)≤ µ(F ) +µ(E)≤ 1
2 which contradicts
maximality.
Problem 6. Compute
lim
n→∞
∫ ∞
0
n sin(x/n)
x(1 +x2)dx
and justify your computation.
Proof. Let fn(x) = n sin(x/n)
x(1+x2) . Recall that lim t→0 sint
t = 1, so lim n
n sin(x/n)
x(1+x2) = 1
1+x2 and since
| sin(x/n)|≤ x/n for x,n positive,
⏐⏐⏐⏐
n sin(x/n)
x(1 +x2)
⏐⏐⏐⏐≤
⏐⏐⏐⏐
n
x
x
n
1
1 +x2
⏐⏐⏐⏐ = 1
1 +x2∈L1[0,∞).
Then by DCT,
lim
n
∫ ∞
0
n sin(x/n)
x(1 +x2) =
∫ ∞
0
lim
n
n sin(x/n)
x(1 +x2) = arctan|∞
0 = π
4.
Problem 7. Prove or disprove: for every real-valued continuous function f on [0, 1] such that f(0) =
0 and every ϵ> 0, there is a real polynomial p having only odd powers of x, i.e. p is of the form
p(x) =a1x +a3x3 +a5x5 +··· +a2n+1x2n+1,
78

13 AUGUST 2013 Kari Eiﬂer
such that supx∈[0,1]|f(x)−p(x)|<ϵ .
Proof. Let
A ={ polynomial with even power}
soA is an algebra that separates points. Stone-Weierstrass implies that A is dense inC[0, 1]. We
can let
B =F (x)|F (x) =
∫ x
0
f(t)dt 0≤x≤ 1,f ∈A} ={ all polynomials with odd powers}
From problem 10 of August 2015, B =C0[0, 1].
Problem 8. Letf∈L1
loc(R).
(a) What (by deﬁnition) are the Hardy-Littlewood maximal function Hf and the Lebesgue set Lf of
f?
Proof.
Hf (x) = sup
r>0
1
m(B(r,x ))
∫
B(r,x)
|f(y)|dy
| {z }
=:Arf (x)
.
Lf =
{
x| lim
r→0+
∫
B(r,x)|f(y)−f(x)|dy
m(B(r,x )) = 0
}
(b) State the Hardy-Littlewood Maximal Theorem.
Proof.‖Hf (x)‖p≤‖f‖p.
(c) In each case, either construct concretely an example of f with the required property, or explain
why no such example exists (you may use theorems from Folland about the Lebesgue set, if you
state them).
(i) Lf = R
(ii) the complement of Lf is uncountable
(iii) Lf⊆ (−∞, 0]∪ [1,∞).
Proof. here
Problem 9. LetX be a separable Banach space, let {xn|n≥ 1} be a countable, dense subset of the
unit ball of X and let B be the closed unit ball in the dual Banach space X∗ of X. For φ,ψ∈B, let
79

13 AUGUST 2013 Kari Eiﬂer
d(φ,ψ ) =
∞∑
n=1
2−n|φ(xn)−ψ(xn)|.
Show that d is a metric on B whose topology agrees with the weak*-topology of X∗ restricted to B.
Proof. We ﬁrst check that d is a metric on B:
• d(φ,ψ )≥ 0 clear
If d(φ,ψ ) = 0 then φ =ψ on{xn} so φ =ψ by continuity / density
• triangle inequality follows as well
the weak*-topology is{z∗∈X∗|| (x∗−z∗)(x)|<ϵ} for ﬁxed x∗∈X∗,x∈X,ϵ> 0.
For ﬁxedx∗∈X∗ consider the ϵ-ball in the metric d which is
ψ∈X∗|d(x∗,ψ )<ϵ} ={ψ∈X∗|
∞∑
n=1
2−n|x∗(xn)−ψ(xn)|<ϵ}
We want to show that|(x∗−ψ)(x)| < ϵ′ for any x∈ BX and some ϵ′ > 0. Since xn is dense in BX
then there exists a xnk→x. Then
|(x∗−ψ)(x)|≤| (x∗−ψ)(x−xnk)| +|(x∗−ψ)(xnk)|<ϵ′
On the other hand, if ψ is in a weak* neighborhood of x∗, we want to show ∑∞
n=1 2−n|x∗(xn)−
ψ(xn)|<ϵ . Let |(ψ−x∗)(xn)|<ϵ′ for all n, then
∞∑
n=1
2−n|x∗(xn)−ψ(xn)|<
∞∑
n=1
2−nϵ =ϵ.
Alternative Proof. We ﬁrst check that d is a metric on B:
• d(φ,ψ )≥ 0 clear
If d(φ,ψ ) = 0 then φ =ψ on{xn} so φ =ψ by continuity / density
• triangle inequality follows as well
To see that the topologies agree:
Consider B(r,ϕ ) under the metric. We need to show it contains an open U under the weak*-topology.
Sayd(φk,ψ )→ 0. Then ∑∞
n=1 2−n|φk(xn)−ψ(xn)|→ 0. So under the weak* topology, we need to
show for all x∈BX,|φk(x)−ψ(x)|→ 0.
Indeed, this follows by density of {xn}. For large k,‖φk‖ = supn|φk(xn)| ≤M and|φk(xn)| ∼
|ψ(xn)|.
80

14 JANUARY 2013 Kari Eiﬂer
Then for every ϵ> 0, there exists some n such that‖xn−x‖<ϵ so
|φk(x)−ψ(x)|≤| φk(x)−φk(xn)| +|φk(xn)−ψ(xn)| +|ψ(xn)−ψ(x)|
If|φk(x)−ψ(x)|→ 0 for all x, then for all ϵ, choose N such that∑∞
n=N 2−n < ϵ, so d(φk,ψ ) =∑∞
n=1 2−n|φk(xn)−ψ(xn)|.
Problem 10. LetT :X→Y be a linear map between Banach spaces that is surjective and satisﬁes
‖Tx‖≥ ϵ‖x‖ for some ϵ> 0 and all x∈X. Show that T is bounded.
Proof. Is Γ(T ) ={(x,Tx )|x∈X} closed in X×Y ?
If xn→ x and Txn→ y, we want to show y = Tx . T is surjective, so y = Tx 0. Then for all ˜ϵ >0,
there exists N such that for all n≥N,
˜ϵ> ‖Txn−Tx 0‖≥ ϵ‖xn−x0‖.
So xn→x0, and Txn→Tx 0.
The closed graph theorem implies T is bounded.
14 January 2013
Problem 1. Letf be a Lebesgue integrable, real-valued function on (0, 1) and for x∈ (0, 1) deﬁne
g(x) =
∫ 1
x
t−1f(t)dt.
Show that g is Lebesgue integrable on (0, 1) and that
∫ 1
0 g(x)dx =
∫ 1
0 f(x)dx.
Proof. See January 2014, # 4
Problem 2. Letfn ∈ C[0, 1]. Show that fn → 0 weakly if and only if the sequence (‖fn‖)∞
n=1 is
bounded and fn converges pointwise to 0.
Proof. See August 2015, # 3
Problem 3. Let (X,µ ) be a measure space with 0 < µ(X)≤ 1 and let f : X→ R be measurable.
State the deﬁnition of ‖f‖p for p ∈ [1,∞]. Show that ‖f‖p is a monotone increasing function of
p∈ [1,∞) and that limp→∞‖f‖p =‖f‖∞.
Proof. See January 2016, # 8
81

14 JANUARY 2013 Kari Eiﬂer
Problem 4. (a) Is there a signed Borel measure µ on [0, 1] such that
p′(0) =
∫ 1
0
p(x)dµ(x)
for all real polynomials p of degree at most 19?
Proof. We ﬁrst deﬁne the linear functional I(p) =p′(0).
WriteP = span{1,x,x 2,...,x 19}, which is a ﬁnite dimensional space. Thus, all norms are
equivalent. We take, in particular, the norms ‖·‖ m = maxi=1,...,19|ai| and‖·‖ ∞. Then there
must exist some C such that if‖p‖∞ = 1 then ‖p‖m≤ C so|a1|≤ C which implies that I is
bounded.
By Hahn-Banach, there exists some ˜I∈C [0, 1]∗ such that ˜I(p) = I(p) for all p∈P . By Riesz,
there exists some µ such that ˜E(p) =p′(0) =
∫ 1
0 p(x)dµ.
(b) Is there a signed Borel measure µ on [0, 1] such that
p′(0) =
∫ 1
0
p(x)dµ(x)
for all real polynomials p?
Proof. Suppose there did exist such a measure µ on [0, 1]. Then since µ([0, 1]) =
∫ 1
0 1dµ = 0, we
have that|µ|([0, 1])<∞. Therefore, the mapping T :p↦→
∫ 1
0 p(x)dµ(x) can extend continuously
to C[0, 1].
Consider fn(x) deﬁned by nx for x∈ [1/n, 2/n], fn(x) = 1 for x∈ [2/n, 1] and smooth on the
interval [1/n, 2/n] but bounded above by 2 (it’s always possible to construct such an fn). Then
f′
n(0) =
∫ 1
0
fn(x)dµ≤‖fn‖∞‖µ‖≤‖ µ‖<∞
But limn|f′
n(0)| = limn =∞. Contradiction!
Problem 5. LetF be the set of all real-valued functions on [0, 1] of the form
f(t) = 1
Πn
j=1(t−cj)
for natural numbers n and for real numbers cj /∈ [0, 1]. Prove or disprove: for all continuous, real-
valued functions g and h on [0, 1] such that g(t) < h(t) for all t∈ [0, 1], there is a function a∈
spanF such that g(t)<a (t)<h (t) for all t∈ [0, 1].
Proof. LetA = spanF. It’s easy to see this is an algebra since cj /∈ [0, 1]. Also 1
t+1 separates
points, so Stone-Weierstrass theorem impliesA =C[0, 1].
Let M = mint∈[0,1]|h(t)−g(t)|, so we can choose some a∈A such that
‖‖‖a− h+g
2
‖‖‖
∞
< M
6 . Then
−M
6 <a − h+g
2 < M
6 and since h−g≥M, then
82

14 JANUARY 2013 Kari Eiﬂer
h−a = h
2−a + h
2≥ h
2−a + g
2 + M
2 = h +g
2 −a + M
2 > M
2 − M
6 = M
3 > 0
a−g =a− g +g
2 ≥a− g +h
2 + M
2 >−M
6 + M
2 = M
3 > 0
So then g <a<h .
Problem 6. Letk : [0, 1]× [0, 1]→ R be continuous and let 1<p< ∞. For f∈Lp[0, 1], let Tf be
the function on [0, 1] deﬁned by
(Tf )(x) =
∫ 1
0
k(x,y )f(y)dy.
Show that Tf is a continuous function on [0, 1] and that the image under T of the unit ball in Lp[0, 1]
has compact closure in C[0, 1].
Proof. Note that
|Tf (x)−Tf (y)|≤ int1
0|k(x,z )−k(y,z )||f(z)|dz≤‖k(x,·)−k(y,·)‖q‖f‖p for q = p
p− 1
Since k is continuous on [0, 1]2, then for every ϵ> 0 there exists some δ >0 such that if|x−y|<δ ,
then
‖k(x,·)−k(y,·)‖q
q =
∫ 1
0
|k(x,z )−k(y,z )|qdz <
∫ 1
0
ϵpdz =ϵp.
Therefore, Tf is continuous.
Now considerF ={Tf |‖f‖p≤ 1}⊆ C[0, 1]. We’ll use Arzela-Ascoli:
• equicontinuous
follows from above
• pointwise bounded
|Tf (x)|≤‖ K(x,·)‖q‖f‖p≤‖K(x,·)‖q≤
(∫ 1
0
Mqdz
)1/q
=M
so it’s actually uniformly bounded
Therefore, by Arzela-Ascoli,F is compact in C[0, 1].
83

14 JANUARY 2013 Kari Eiﬂer
Problem 7. (a) Deﬁne the total variation of a function f : [0, 1]→ R and absolute continuity of f.
Proof. here
(b) Suppose f : [0, 1]→ R is absolutely continuous and deﬁnes g∈C[0, 1] by
g(x) =
∫ 1
0
f(xy)dy.
Show that g is absolutely continuous.
Proof. Since f is absolutely continuous, there exists some δ′ > 0 such that ∑n
i=1|bi−ai| < δ′
implies∑n
i=1|f(bi)−f(ai)|<ϵ . Fix some y∈ [0, 1] so that
n∑
i=1
|biy−aiy|≤
n∑
i=1
|bi−ai|<δ′
This implies then that ∑n
i=1|f(biy)−f(aiy)|<ϵ . Therefore,
n∑
i=1
|g(bi)−g(ai)|≤
∫ 1
0
n∑
i=1
|f(bi)−f(ai)|≤
∫ 1
0
ϵdx =ϵ.
So g is absolutely continuous.
Problem 8. (a) State the deﬁnition of absolute continuity, v << µ, for positive measures µ and
ν, and state the Radon-Nikodym Theorem, (or the Lebesgue-Radon-NIkodym Theorem, if you
prefer.)
Proof. here
(b) Suppose that we have ν1 << µ1 and ν2 << µ2 for positive measures νi and µi on measurable
spaces (Xi,Mi) for i = 1, 2. Show that we have ν1×ν2 <<µ 1×µ2, and
d(ν1×ν2)
d(µ1×µ2)(x,y ) = dν1
dµ1
(x)dν2
dµ2
(y).
Proof. Assume E∈M 1⊗M 2 and µ1×µ2(E) = 0. Deﬁne
Ex ={y∈X2| (x,y )∈E} Ey ={x∈X| (x,y )∈E}
Then Ex ∈ M1 and Ey ∈ M2 for all x ∈ X1,y ∈ X2. Since µ1 and µ2 are positive, then
0 = ( µ1× µ2)(E) =
∫
µ1(Ey)dµ2(y) then µ1(Ey) = 0 µ2-almsot everywhere and so then
ν1(Ey) = 0 µ2-almost everywhere.
Thus,µ2({y∈X2|ν1(Ey)> 0}) = 0 so then ν2({y∈X2|ν1(Ey)> 0}) = 0. Thus, ν1(Ey) = 0
for ν2-almost everywhere and therefore, (ν1×ν2)(E) =
∫
ν1(Ey)dν2(y) = 0.
Thus,ν1×ν2 <<µ 1×µ2. By Radon-Nikodym theorem,
84

14 JANUARY 2013 Kari Eiﬂer
ν1×ν2(E) =
∫
E
d(ν1×ν2)
d(µ1×µ2)(x,y )d(µ1×µ2) for E∈M 1⊗M 2
Since ν1 <<µ 1, by Proposition 3.9(a) in Folland,
(ν1×ν2)(E) =
∫
ν2(Ex)dν1(x)
=
∫
ν2(Ex)dν1
dµ1
(x)dµ1(x)
=
∫ (∫
Ex
dν2
dµ2
(y)dµ2(y)
) dν1
dµ1
(x)dµ1(x)
=
∫
E
dν2
dµ2
(y)dν1
dµ1
(x)d(µ1×µ2)(x,y )
By the uniqueness of Radon-Nikodym derivative, we have
d(ν1×ν2)
d(µ1×µ2)(x,y ) = dν1
dµ1
(x)dν2
dµ2
(y).
Problem 9. (a) Let E be a nonzero Banach space and show that for every x∈ E, there is φ∈ E∗
such that‖φ‖ = 1 and|φ(x)| =‖x‖.
Proof. This is the Hahn-Banach separation Theorem.
(b) Let E and F be Banach spaces, let π :E→F be a bounded linear map and let π∗ :F∗→E∗ be
the induced map on dual spaces. Show that ‖π∗‖ =‖π‖.
Proof. We haveπ∗(y∗)(x) = y∗(π(x)) for all y∗ ∈ F∗ and x ∈ E. Then ‖π∗(y∗)(x)‖ ≤
‖y∗‖‖π‖‖x‖ so then‖π∗‖≤‖ π‖.
On the other hand, by part (a), for each x ∈ E such that‖x‖ ≤1, π(x) ∈ F , we can ﬁnd
y∗∈F∗ such that|y∗(π(x))| =‖π(x)‖ and‖y∗‖ = 1. Then
‖π∗‖≥‖ π∗(y∗)‖≥| π∗(y)(x)| =|y∗(π(x))| =‖π(x)‖ ∀‖ x‖≤ 1
So‖π∗‖≥‖ π‖. THus, ‖π‖ =‖π∗‖.
Problem 10. LetX be a real Banach space and suppose C is a closed subset of X such that
(i) x1 +x2∈C for all x1,x 2∈C,
(ii) λx∈C for all x∈C and λ> 0,
(iii) for all x∈X there exists x1,x 2∈C such that x =x1−x2.
85

14 JANUARY 2013 Kari Eiﬂer
Prove that, for some M >0, the unit ball of X is contained in the closure of
{x1−x2|xi∈C,‖xi‖≤ M}.
Deduce that every x∈X can be written x =x1−x2, with xi∈C and‖xi‖≤ 2M‖x‖.
Proof. Deﬁne
Cn ={x1−x2|xi∈C,‖xi‖≤ n}
By (iii), we know that X =∪Cn. By Baire Category, there exists some M such that∅⁄ = CM
◦
=
C◦
M. Thus, there exists an open ball B⊆CM, B =B(x0, 2r).
For anyx∈ BX, x0 +rx∈ B ⊆ CM. From (i), we know that CM−CM ⊆ C2M so then rx =
(x0 +rx)−x0∈CM−CM⊆C2M. From (ii), we know x∈C2M/r, so BX⊆C2M/r. Let M′ = 2M
r .
For anyx∈X, x∈CM′‖x‖. So we can ﬁnd z1,y 1∈C such that‖z1‖,‖y1‖≤ M‖x‖ and‖x− (z1−
y1)‖< 1
2‖x‖. Therefore,
2(x− (z1−y1))
‖x‖ ∈CM ⇒ x− (z1−y1)∈CM‖x‖/2
So we can ﬁnd z2,y 2∈C such that‖z2‖,‖y2‖≤ M
2‖x‖ and
‖‖‖‖‖x−
2∑
i=1
(zi−yi)
‖‖‖‖‖< 1
22‖x‖.
Inductively, we can ﬁnd{zn},{yn}⊆ C such that‖zk‖,‖yk‖≤ M
2k−1‖x‖ and
‖‖‖‖‖x−
k∑
i=1
(zi−yi)
‖‖‖‖‖< 1
2k‖x‖.
Then,
∞∑
k=1
‖zk‖≤
∞∑
k=1
M‖x‖ 1
2k < 2M‖x‖<∞
so∑∞
k=1zk converges to some x1 in C and similarly ∑∞
k=1yk converges to some x2 in C (since C is
closed). Moreover,
lim
n
‖‖‖‖‖x−
n∑
i=1
(zi−yi)
‖‖‖‖‖ = lim
n
‖‖‖‖‖x−
( n∑
i=1
zi−
n∑
i=1
yi
)‖‖‖‖‖ = 0.
86

15 AUGUST 2012 Kari Eiﬂer
So then x =∑∞
i=1(zi−yi) =x1−x2.
15 August 2012
Problem 1. Let (X,M,µ ) be a measure space. Prove that the normed vector space L1(X,µ ) is
complete. You may use any results except the convergence of function series.
Proof. See class notes.
Problem 2. Fix two measure spaces (X,M,µ ) and (Y,N,ν ) with µ(X),ν (Y )> 0. Let f :X→ C,
g : Y → C be measurable. Suppose f(x) = g(y), (µ×ν)-a.e. Show that there is a constant a∈ C
such that f(x) =a µ-a.e. and g(y) =a ν-a.e.
Proof. Let E :={(x,y )∈ X×Y | f(x) = g(y)}, so (µ⊗ν)(Ec) = 0. Then for every a∈ C, by
Fubini-Tonelli,
0 = (µ⊗ν) ({(x,y )∈X×Y |f(x) =a,g (y)⁄=a}) =µ ({x∈X|f(x) =a})ν ({y∈Y |g(y)⁄=a}).
Assume µ({x∈X|f(x) =a}) = 0 for all a∈ C. Then
0< (µ⊗ν)(X×Y )
= (µ⊗ν)(E) =
∫
X×Y
χ{(x,y)|f (x)=g(y)}dµ(x)dν(y)
=
∫
Y
(∫
X
χ{x|f (x)=g(y)}dµ(x)
)
dν(y)
=
∫
Y
0dν(y) = 0.
This is a contradiction so there must exist some a∈ C with µ({x∈ X | f(x) = a}) > 0. Then
ν({y∈Y |g(y)⁄= 0}) = 0 so g(y) =a ν-a.e.
Similarly, we have (µ⊗ν)({(x,y )|f(x)⁄=a,g (y) =a}) = 0. Since ν({y∈Y |g(y) =a}) =ν(Y )⁄= 0,
then µ({x|f(x)⁄=a}) = 0 so f(x) =a µ-a.e.
Problem 3. Letf : R3 → R be a Borel measurable function. Suppose for every ball B, f is
Lebesgue integrable on B and
∫
Bf(x)dx = 0 . What can you deduce about f? Justify your answer
carefully.
Proof. Since f∈L1
loc(R2), by Lebesgue Diﬀerentiation Theorem, for a.e. x0∈ R2,
lim
r→0
1
|B(r,x 0)|
∫
B(r,x0)
f(x)dx =f(x0)
87

15 AUGUST 2012 Kari Eiﬂer
This implies f(x0) = 0 so f = 0 almost everywhere.
Problem 4. LetX be a locally compact Hausdorﬀ space. Denote by C0(X) the space of complex-
valued continuous functions on X which vanish at inﬁnity, and by Cc(X) the subset of compactly
supported functions. Use an approximate version of the Stone-Weierstrass theorem to prove that
Cc(X) is dense in C0(X).
Proof. For anyf,g ∈Cc(X), the complex conjugation of f is also in Cc(X).
By complex-LCH-Stone-Weierstrass, we only need to show that Cc(X) separates points.
For everyx⁄=y, we can ﬁnd open U,V with x∈U,y ∈V with U∩V =∅. Since X is LCH, we can
require U to be compact.
Now{x}⊆ U⊆U⊆X\V ⊆X\{y}. Then by Urysohn’s Lemma for LCH, we can ﬁnd a continuous
function f : X → [0, 1] such taht f|U = 1 and f(x) = 0 outside a compact subset of X\{y}. So
f(x) = 1, f(y) = 0, and f∈Cc(X).
So Cc(X) separates points. Also, there does not exist any x0∈ X such that f(x0) = 0 for all f ∈
Cc(X).
Therefore, by Stone-Weierstrass, Cc(X) =C0(X).
Problem 5. Give an example of each of the following. Justify your answers
(a) A nowhere dense subset of R of positive Lebesgue measure
Proof. Take a fat Cantor set.
(b) A closed, convex subset of a Banach space with multiple points of minimal norm.
Proof. Let X = L1[0, 1], C ={f ∈ X |
∫ 1
0 f(t)dt = 0}. It’s easy to see that C is closed and
convex. The minimum norm of elements in C is 1 because
‖f‖1 =
∫ 1
0
|f(t)|dt≥
⏐⏐⏐⏐
∫ 1
0
f(t)dt
⏐⏐⏐⏐ = 1.
But every element of{aχ[0,1/2] + (2−a)χ[1/2,1]}0≤a≤2 in C has norm 1.
Problem 6. Let
S =
{
f∈L∞(R)||f(x)|≤ 1
1 +x2 a.e.
}
.
Which of the following statements are true? Prove your answers.
(a) The closure of S is compact in the norm topology
88

15 AUGUST 2012 Kari Eiﬂer
Proof. NO. Let
fn(x) := 1
x2 + 1
χ[ 1
n+1, 1
n ](x)
in S. So there are no subsequences of ( fn) which are Cauchy in L∞ since‖fn−fm‖∞≥ 1 for
n⁄=m.
(b) S is closed in the norm topology.
Proof. YES. Suppose (fn)⊆S, fn→f in L∞. Then
|f(x)|≤| fn(x)| +|fn(x)−f(x)|< 1
1 +x2 +‖fn−f‖∞ < 1
1 +x2 +ϵ a.e.
Letting ϵ→ 0, we have|f(x)|≤ 1
1+x2 a.e. and f∈L∞ so f∈S.
(c) The closure of S is compact in the weak* topology
Proof. YES. The unit ball in L∞(R) is weak*-compact by Alaoglu. Since 1
1+x2 ≤ 1 for all x∈
R, then S is a subset of the unit ball in L∞. Therefore, S
w∗
is weak* compact.
Problem 7. LetT be a bounded operator on a Hilbert space H. Prove taht ‖T∗T‖ =‖T‖2. State
the results you are using.
Proof. Clearly,‖T∗T‖≤‖ T∗‖‖T‖ =‖T‖2. On the other hand,
‖T‖2 = sup
‖x‖=1
|⟨Tx,Tx⟩| = sup
‖x‖=1
|⟨T∗Tx,x⟩|.
Since for‖x‖ = 1,
|⟨T∗Tx,x⟩|≤‖ T∗Tx‖‖x‖≤‖ T∗T‖‖x‖2≤‖T∗T‖
then‖T‖2≤‖T∗T‖.
Problem 8. (a) Let g be an integrable function on [0, 1]. Does there exist a bounded measurable
function f such that‖f‖∞⁄= 0 and
∫ 1
0 fgdx =‖g‖1‖f‖∞? Give a construction or a counterex-
ample.
Proof. YES. For any g ∈ L1, let f = sgn(g) where g(x)⁄= 0, and 1 where g(x) = 0. Then
‖f‖∞ = 1 and
∫ 1
0
fg =
∫ 1
0
|g(x)|dx =‖g‖1 =‖g‖1‖f‖∞.
89

15 AUGUST 2012 Kari Eiﬂer
(b) Let g be a bounded measurable function on [0, 1]. Does there exist an integrable function f such
that‖f‖1⁄= 0 and
∫ 1
0 fgdx =‖g‖∞‖f‖1? Give a construction or a counterexample.
Proof. NO. Let g(x) = x on [0, 1] so‖g‖∞ = 1, implying g∈ L∞[0, 1]. Assume such an f∈ L1
exists, so
‖f‖1 =‖f‖1‖g‖∞ =
∫ 1
0
fgdx =
∫ 1
0
xf(x)dx
and also‖f‖1 =
∫ 1
0|f|dx so then
∫ 1
0 f(x)xdx =
∫ 1
0|f|dx. Therefore,
∫ 1
0
|f(x)|dx =
∫ 1
0
xf(x)dx≤
∫ 1
0
x|f(x)|dx≤
(
1− 1
n
)∫ 1−1/n
0
|f(x)|dx +
∫ 1
1−1/n
|f(x)|dx
So then
∫ 1−1/n
0
|f(x)|dx +
∫ 1
1−1/n
|f(x)|dx≤
(
1− 1
n
)∫ 1−1/n
0
|f(x)|dx +
∫ 1
1−1/n
|f(x)|dx
Thus,
∫ 1−1/n
0 |f(x)|dx = 0 for all n∈ N. Letting fn(x) = χ[0,1−1/n]|f(x)|↗| f(x)| then by
monotone convergence theorem,
∫
|f(x)dx = limn
∫
fn(x) = 0 so‖f‖1 = 0.
Problem 9. LetF : R→ C be a bounded continuous function, µ the Lebesgue measure, and f,g ∈
L1(µ). Let
˜f(x) =
∫
F (xy)f(y)dµ(y), ˜g(x) =
∫
F (xy)g(y)dµ(y).
Show that ˜f and ˜g are bounded continuous functions which satisfy
∫
f ˜gdµ =
∫
˜fgdµ.
Proof. We have‖ ˜f‖|infty ≤ ‖F‖∞‖f‖1 < ∞ and‖˜g‖ ≤ ‖F‖∞‖g‖1 < ∞ so ˜f, ˜g ∈ L∞. By
dominated convergence theorem, we know that limn
∫
[−n,n]|f(x)dµ =‖f‖1. So then for every ϵ> 0,
there exists some N such that
∫
R\[−n,n]|f(x)|dµ<ϵ . Then
| ˜f(x1)− ˜f(x2)|≤
∫
|F (x1y)−F (x2y)||f(y)|dµ(y)
=
∫
[−n,n]
|F (x1y)−F (x2y)||f(y)|dµ(y) +
∫
R\[−n,n]
|F (x1y)−F (x2y)||f(y)|dµ(y)
≤ sup
y∈[−n,n]
|F (x1y)−F (x2y)|‖f‖1 + 2‖F‖∞ϵ
90

15 AUGUST 2012 Kari Eiﬂer
Since F is continuous, let|x1−x2|< δ
n such that|x1y−x2y|<δ imples|F (x1y)−F (x2y)|<ϵ . So
| ˜f(x1)− ˜f(x2)|→ 0 as|x1−x2|→ 0.
A similar argument will show that ˜g is continuous. Since f ˜g∈L1, by Fubini,
∫
f ˜gdµ =
∫ ∫
f(x)F (xy)g(y)dµ(y)dµ(x)
=
∫
g(y)
(∫
f(x)F (xy)dµ(x)
)
dµ(y)
=
∫
g(y) ˜f(y)dµ(y)
=
∫
˜fgdµ.
Problem 10. Letµ,{µn|n∈ N} be ﬁnite Borel measures on [0, 1]. µn→µ vaguely if it converges
in the weak* topology on M[0, 1] = (C[0, 1])∗. µn→µ in moments if for each k∈{ 0}∪ N,
∫
[0,1]
xkdµn(x)→
∫
[0,1]
xkdµ(x).
Show that µn→µ vaguely if and only if µn→µ in moments.
Proof.⇒) trivial by the deﬁnitions
⇐) We want to show that for all f ∈ C[0, 1],
∫
fdµn→
∫
fdµ. By Stone-Weierstrass, we can ﬁnd
pn to be a sequence of polynomials which converge uniformly to f on [0, 1]
⏐⏐⏐⏐
∫
f(x)dµ−
∫
f(x)dµn
⏐⏐⏐⏐≤
⏐⏐⏐⏐
∫
fdµ−
∫
pmdµ
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫
pmdµ−
∫
pmdµn
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫
pmdµn−
∫
fdµn
⏐⏐⏐⏐
For the ﬁrst part,|
∫
fdµ−
∫
pmdµ|≤‖ f−pm‖∞µ(X)→ 0 as m→∞ . Similarly,
⏐⏐∫
pmdµn−
∫
fdµn
⏐⏐≤
‖f−pm‖∞µn(X)→ 0 for all n.
Next, ﬁnd a polynomial qmj with degree at most j such that‖qmj−pm‖∞→ 0 as j→∞ . Then
since µn→µ in moments, then
⏐⏐∫
qmjdµ−
∫
qmjdµn
⏐⏐→ 0 for all j. Thus,
⏐⏐⏐⏐
∫
pmdµ−
∫
pmdµn
⏐⏐⏐⏐≤
⏐⏐⏐⏐
∫
pndµ−
∫
qmjdµ
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫
qmjdµ−
∫
qmjdµn
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫
qmjdµn−
∫
pmdµn
⏐⏐⏐⏐
≤‖pm−qmj‖∞ (µ(X) +µn(X)) +
⏐⏐⏐⏐
∫
qmjdµ−
∫
qmjdµn
⏐⏐⏐⏐→ 0.
91

16 JANUARY 2012 Kari Eiﬂer
16 January 2012
Problem 1. LetA be the subset of [0, 1] consisting of numbers whose decimal expansions contain
no sevens. Show that A is Lebesgue measurable, and ﬁnd its measure. Why does non-uniqueness of
decimal expansions not cause any problems?
Proof. Let Ai be the subset of [0, 1] consisting of numbers whose ﬁrst i digits are not 7. Then An+1⊆
An and A =∩nAn,
A1 = [0, 0.7]∪ [0.8, 1]
A2 = [0, 0.07]∪ [0.08, 0.17]∪... ∪ [0.98, 1]
So An is the union of some Borel intervals in [0 , 1], so An is Lebesgue measurable. Therefore, A is
Lebesgue measurable.
Now for 0≤ i≤ 9, let Ai
n be the subset of An such that the (n + 1)th digit is i. Then we can write
An =⊔9
i=0Ai
n.
Also, m(Ai
n) = m(Aj
n), so m(An) = 10m(Ai
n) and An+1 =⊔i⁄=7Ai
n so m(An+1) = 9m(Ai
n). There-
fore, m(An+1) = 9
10m(An). Then
m(A) =m (∩∞
n=1An) = lim
n
m(An) = lim
n
( 9
10
)n−1
m(A1) = 0
The only numbers with non-unique decimal representation are 0 .a1a2...a n = 0.a1a2...a n−1999... .
However∀n there are only ﬁnitely many, so non-unique = ∪n{0.a1...a n} which is countable, hence
null, hence Lebesgue.
Problem 2. Let the functions fα be deﬁned by
fα(x) =
{
xα cos(1/x) x> 0
0 x = 0
Find all values of α≥ 0 such that
(a) fα is continuous
Proof. When a > 0, xa cos(1/x)≤ xa→ 0 as x→ 0 so fa is continuous. If a = 0, we know
cos(1/x) isn’t continuous at 0.
(b) fα is of bounded variation on [0, 1]
Proof. First, 0 <a ≤ 1, put partitions
92

16 JANUARY 2012 Kari Eiﬂer
Pm =
{
0, 1
2πm, 1
π(2m− 1),..., 1
π, 1
}
Then
fa(Pm) =
{
0, 1
(π2m)a, −1
(π(2n− 1))a,..., −1
πa, cos(1)
}
So
Tfα(Pm) =
⏐⏐⏐⏐
1
(π(2m))a− 0
⏐⏐⏐⏐ +
⏐⏐⏐⏐
−1
(π(2m− 1))a− 1
(π2m)a
⏐⏐⏐⏐ +... +
⏐⏐⏐⏐cos(1)−−1
πa
⏐⏐⏐⏐≈
2m∑
i=1
c
(πi)a→∞
when 0 <a ≤ 1 as m→∞ .
So when 0 < a≤ 1, fa is not of bounded variation when 0 < a≤ 1. For a > 1, let’s look at
(c).
(c) fα is absolutely continuous on [0, 1]
Proof. When a > 1, we see f′
a(0) = 0 and f′
a is integrable because f′
a(x) = axa−1 cos(1/x) +
xa−2 sin(1/x) so then fa(x) =
∫x
0 f′
a(t)dt. Thus, f is absolutely continuous.
So in (b) we have fa is of bounded variation for a > 1. Since fa isn’t bounded variation when
0<a ≤ 1, so fa isn’t absolutely continuous either when 0 <a ≤ 1.
Problem 3. LetF denote the family of functions on [0, 1] of the form
f(x) =
∞∑
n=1
an sin(nx)
wherean are real and|an|≤ 1/n3. State a general theorem and use that theorem to prove taht any
sequences inF has a subsequence that converges uniformly on [0, 1].
Proof. We’ll use Arzela-Ascoli.
For allf∈F ,
|f(x)| =
⏐⏐⏐⏐⏐
∞∑
n=1
an sin(nx)
⏐⏐⏐⏐⏐≤
∞∑
n=1
|an|≤
∞∑
n=1
n−3 <∞
so uniformly bounded. Also, for all f∈F ,
|f(x)−f(y)|≤
∞∑
n=1
|an|| sin(nx)−sin(ny)|≤
∞∑
n=1
2n−3
⏐⏐⏐⏐cosnx +ny
2
⏐⏐⏐⏐
⏐⏐⏐⏐sinnx +ny
2
⏐⏐⏐⏐≤
∞∑
n=1
n−2|x−y| = π2
6|x−y|
93

16 JANUARY 2012 Kari Eiﬂer
SoF is equicontinuous.
ThenF is compact, hence sequentially compact. So F has a subsequence that converges in the uni-
form norm.
Problem 4. LetH be a Hilbert space and W⊂H a subspace. Show that H =W⊕W⊥ whereW is
the closure of W .
Note: Do not just state this as a consequence of a standard result, prove the result.
Proof. here!
Problem 5. SupposeA is a bounded linear operator on a Hilbert space H with the property that
‖p(A)‖≤ C sup{|p(z)|| z∈ C,|z| = 1}
for all polynomials p with complex coeﬃcients, and a ﬁxed constant C. Show that to each pair x,y∈
H there corresponds a complex Borel measure µ on the circle S1 ={z∈ C||z| = 1} such that
⟨Anx,y⟩ =
∫
zndµ(z) n = 0, 1, 2,...
Proof. Consider
Tx,y :P (S1)→ C
p↦→⟨P (A)x,y⟩
Then
|⟨P (A)x,y⟩|≤‖ P (A)‖‖x‖‖y‖≤ C‖P‖∞‖x‖‖y‖
Thus,|Tx,y(P )|≤ C‖x‖‖y‖‖P‖∞ = f(P ) which is obviously a seminorm. By Hahn-Banach, Tx,y
can be extended to C(S1).
Then apply Riesz-Representation Theorem, there exists a complex Borel measure µ on S1 such that
Tx,y(P ) =⟨P (A)x,y⟩ =
∫
S1
P (z)dµ(z)
TakeP (z) =zn so⟨Anx,y⟩ =
∫
S1zndµ(z).
Problem 6. Letφ be the linear functional
φ(f) =f(0)−
∫ 1
−1
f(t)dt
(a) Compute the norm of φ as a functional on the Banach space C[−1, 1] with uniform norm
94

16 JANUARY 2012 Kari Eiﬂer
Proof.
|φ(f)|≤| f(0)| +
∫ 1
−1
|f(t)|dt≤‖f‖∞ +‖f‖∞
∫ 1
−1
dt = 3‖f‖∞
So‖φ‖ ≤3. On the other hand, let fn be piecewise linear functional such that fn = −1 on
[−1,−1/n] and [1/n, 1] and fn(0) = 1. Then
∫ 1
−1
fn(t)dt =−2(1− 1/n) + 2
n =−2 + 4
n→− 2
So sup|φ(fn)|≥ 3 so‖φ‖ = 3.
(b) Comptue the norm of φ as a functional on the normed vector space LC[−1, 1] which is C[−1, 1]
with the L1 norm.
Proof.
‖φ‖ = sup
f∈LC[−1,1]
|f(0)−
∫ 1
−1f(t)dt|
‖f‖1
≥ lim
n
|1− 1/n|
(1/n) =∞
Problem 7. LetX be a normed space and A⊂ X be a subset. Show that A is bounded (as a set) if
and only if it is weakly bounded (that is, f(A)⊂ C is bounded for each f∈X∗).
Proof.⇒) for all x∈A, for all f∈X∗,|f(x)|≤‖ f‖‖x‖<∞ so A is weakly bounded
⇐) on the other hand, consider A∗∗ ={a∗∗| a∈ A} bya∗∗(f) = f(a) for all f∈ X∗. Since X∗ is
Banach, and we know
sup
a∗∗∈A∗∗
‖a∗∗(f)‖ = sup
a∈A
|f(a)|<∞ ∀ f∈X∗
By the uniform boundedness principle, sup a∈A‖a‖ = supa∗∗∈A∗∗‖a∗∗‖<∞.
Problem 8. LetX be a topological vector space.
(a) Deﬁne what this means.
Proof. Let X be a vector space, T a topology on X. Then (X,T ) is a topological vector space
provided
• + :X×X→X is continuous
• ·: R×X→X is continuous
(b) Let A⊂X be compact and B⊂X be closed. Show that A +B⊂X is closed.
95

16 JANUARY 2012 Kari Eiﬂer
Proof. Fix z∈ (A +B)c. For x∈ A, z−x∈ Bc so there exists an open neighborhood Vx∋
0 in X such that (z− x + Vx)∩ B = ∅. Since addition is continuous, there exists U1x,U 2x
neighborhoods of 0 such that U1x +U2x⊆Vx.
Ux =U1x∩U2x∩ (−U1x)∩ (−U2x) so Ux =−Ux. Then {x +Ux}x∈A is an open cover of A. Since
A is compact, there exists a ﬁnite subcover x1,...,x n∈A such that
A⊆∪ n
i=1xi +Uxi
Put U =∩n
i=1Uxi. Then z +U is an open neighborhood of z. If there exists x∈ A y∈ B such
that x +y∈z +U then x∈xi +Uxi for some i and y∈z−x +U⊆z−xi +Uxi⊆z−xi +Vxi
but (z−xi +Vxi)∩B =∅. Contradiction!
So (z +U)∩ (A +B) =∅.
(c) Give an example indicating that the condition ‘A closed’ is insuﬃcient for the conclusion.
Proof. X = R2, A ={(x, 0)| x∈ R} and B ={(x, 1/x)| x >0}. Then A +B ={(x,y )| y >
0}.
Problem 9. Let (X,M,µ ) be a ﬁnite measure space. Let f,fn∈ L3(X,dµ ) for n∈ N be functions
such that fn→f µ-a.e. and |fn|≤ M for all n. Let g∈L3/2(X,dµ ). Show that
lim
n
∫
fngdµ =
∫
fgdµ.
Proof.|fng|≤ M|g|. Since µ is a ﬁnite measure, M1∈L3(µ). By Holder, M|g|∈ L1(µ). The result
follows from Dominated Convergence Theorem.
Problem 10. LetX be a σ-ﬁnite measure space, and fn : X→ R a sequence of measurable func-
tions on it. Suppose fn→ 0 in L2 and L4.
(a) Does fn→ 0 in L1?
Proof. NO.
Let X = R, µ=Lebesgue measure. fn = n−1χ[0,n] so‖fn‖1 = 1 does not converge to 0, but
‖fn‖2 =n−1/2→ 0 and‖fn‖4 =n−3/4→ 0.
(b) Does fn→ 0 in L5?
Proof. YES.
Since 0 < 2 < 3 < 4 <∞, L2∩L4⊆ L3 and‖f‖3≤‖ f‖λ
2‖f‖1−λ
4 where 1
3 = λ
2 + 1−λ
4 implies
λ = 1
3. So
‖fn‖3≤‖fn‖1/3
2 ‖fn‖2/3
4 → 0
(c) Does fn→ 0 in L5?
96

17 AUGUST 2011 Kari Eiﬂer
Proof. NO.
X = [0, 1], µ: Lebesgue measure. Let fn = nχ[0,n−5]. Then ‖fn‖5 = 1 but‖fn‖2 = n−3/2→ 0
and‖fn‖4 =n−1/4→ 0.
17 August 2011
Problem 1. Let (X,M,µ ) be a measure space.
(a) Give the deﬁnitions of convergence a.e. and convergence in measure for a sequence of measur-
able functions on X.
Proof. We say a sequence of measurable functions fn converge to f almost everywhere if µ({x|
limnfn(x)⁄=f(x)}) = 0.
We say that fn converges to f in measure if∀ϵ> 0, limnµ({x||f(x)−fn(x)|>ϵ}) = 0.
(b) Show that every sequence of measurable functions on X which converges in measure to 0 has a
subsequence which converges a.e. to 0.
Proof. Suppose for every ϵ> 0, µ({x||fn(x)|≥ ϵ})→ 0. Choose a subsequence {fnk} such that
if
Ej ={x||fnj(x)−fnj+1(x)|> 2−j}
satisﬁes µ(Ej) < 2−j. Let Fk =∪∞
j=kEj so µ(Fk)≤ ∑∞
j=k 2−j ≤ 21−k. Let F =∩kFk so
µ(F ) = 0.
Forx /∈Fk and for i≥j≥k then
|fni(x)−fnj(x)|≤
i−1∑
𝓁=j
|fn𝓁(x)−fn𝓁+1(x)|≤
i−1∑
𝓁=j
2𝓁≤ 2−j→ 0 as k→∞.
So fnk is pointwise Cauchy on x /∈F , so let
f(x) =
{
limfnk(x) x /∈F
0 otherwise
So fnk→ 0 almost everywhere and fn→f in measure since
µ({x||fn(x)−f(x)|≥ ϵ})≤µ({x||fn(x)−fn𝓁(x)|≥ ϵ/2})| {z }
→0
+µ({x||fn𝓁(x)−f(x)|≥ ϵ})| {z }
→0
and
97

17 AUGUST 2011 Kari Eiﬂer
µ({x||f(x)|≥ ϵ})≤µ({x||f(x)−fn(x)|≥ ϵ/2}| {z }
→0
+µ({x||fn(x)|≥ ϵ/2})| {z }
→0
so f = 0 almost everywhere. Thus, {fnk} converges to 0 almost everywhere.
Problem 2. LetX be a separable Banach space. Show that there exists an isometric linear map
fromX into 𝓁∞. Also, show that this is false in general if 𝓁∞ is replaced by 𝓁2.
Proof. Let (xn) be a dense sequence in BX. For each n, use Hahn-Banach Theorem to ﬁnd a norm-
one functional fn∈X∗ with fn(xn) = 1.
Deﬁne φ :X→𝓁∞ via φ(x) =
(
fn(x)
)
. Suppose x∈X has norm one and let 1 > ϵ >0. Choose nϵ
so that‖xnϵ−x‖<ϵ . Then
ϵ> |fnϵ(xnϵ−x)| =|fnϵ(x)|
So‖φ(x)‖ = supn|fn(x)|≥ 1. For every n,|fn(x)|≤‖ fn‖‖x‖ = 1 so ‖φ(x)‖≤ 1. So ‖φ(x)‖ = 1
whenever‖x‖ = 1. Then for all non-zero x,‖φ(x)‖ = ‖x‖ supn|fn(x/‖x‖)| = ‖x‖. So φ is an
isometry.
Why FALSE for𝓁2?
Problem 3. LetX be a locally compact metric space and let {xk} be a sequence in X which has no
convergent subsequence. Show that {n−1∑n
k=1δxk} converges to 0 in the weak* topology on C0(X)∗,
whereδxk denotes the point mass at xk.
Proof. here
Problem 4. LetP be the set of all polynomials f on [0, 1] such that f(0) = f′(0) = 0 . Determine,
with proof, the values of p with 1≤p≤∞ such thatP is dense in Lp[0, 1].
Proof. All 1≤ p <∞. Clearly,P is an algebra which separates points (ex. x2). Stone-Weierstrass
impliesP ={f∈ C[0, 1]| f(0) = 0}. Now for any f∈ Lp, for all ϵ >0, there exists some N such
that
‖‖f−fχ[−N≤f≤N ]
‖‖
p≤ ϵ
2
Deﬁne fN = fχ[−N≤f≤N ]. By Lusin’s theorem, there exists a closed set F such that m([0, 1]\F )≤
1
2p
ϵp
(2N )p = 1
2p
( ϵ
2N
)p
. and fN|F continuous.
Tietze extension theorem applied to fN and F implies the extension g is still bounded by N. Then
‖fN−g‖p
p =
∫
[0,1]\F
|fN−g|p≤ (2N)pm([0, 1]\F )≤ ϵp
2p
So then
98

17 AUGUST 2011 Kari Eiﬂer
‖f−g‖p≤‖f−fN‖p +‖fN−g‖p≤ ϵp
2p + ϵ
2≤ϵ
NOT L∞[0, 1] sinceP ={f∈ C[0, 1]| f(0) = 0}. If f∈ L∞[0, 1] with f(0) = a⁄= 0, then∀g∈P,
‖f−g‖∞ =a.
Problem 5. Let 1<p< ∞ and let{xk}∞
k=1 be a sequence in 𝓁p(N) such that limkxk(n) = 0 for all
n∈ N. Show that if there is an M >0 such that‖xk‖≤ M for all k∈ N then xk→ 0 weakly.
Also, show that if no such M exists, then{xk} can fail to converge weakly.
Proof. Note: Similar to August 2015, #3, just in a diﬀerent space now.
Fix some y∈𝓁q where 1
p + 1
q = 1. We want to show that ∑
nxk(n)y(n)→ 0 as k→∞ . Fix ϵ> 0.
Then we may choose a ﬁnite A⊆ N such that∑
Ac|y(n)|q < ϵq. Since A is ﬁnite, choose some K
such that for all k≥K we have|xk(n)|p < ϵp
|A|. Then for all k≥K, by using Holder, we have
|y(xk)|≤
∑
n∈N
|xk(n)||y(n)|
=
∑
n∈A
|xk(n)||y(n)| +
∑
n∈Ac
|xk(n)||y(n)|
≤
(∑
n∈A
|xk(n)|p
)1/p(∑
n∈A
|y(n)|q
)1/q
+
(∑
n∈Ac
|xk(n)|p
)1/p(∑
n∈Ac
|y(n)|q
)1/q
≤
(
|A| ϵp
|A|
)1/p
‖y‖q +Mϵ
=ϵ (‖y‖q +M)
By making ϵ small enough, we see that |y(xk)|→ 0 as k→∞ .
To see why we require (xk) to be bounded, consider p =q = 2. Take
xk = (0, 0,..., 0, 2k, 0,... ) = 2kek y =
(1
2, 1
22,..., 1
2n,...
)
where xk is all zeros except in the kth spot. Then we can see that lim kxk(n) = 0 for all n, but that
for all k,
y(xk) =
∑
n
xk(n)y(n) = 2k 1
2k = 1
Problem 6. Letf∈C0(R) and for every t∈ R deﬁne ft∈C0(R) by ft(x) =f(x +t) for all x∈ R.
(a) Prove that {ft|t∈ [0, 1]} is compact in the norm topology.
99

17 AUGUST 2011 Kari Eiﬂer
Proof. Similar to August 2013 #1
Since C∞
c (R) is dense in C0(R), we can choose g∈C∞
c (R) such that‖g−f‖∞ <ϵ . Then
‖ftn−ft‖∞≤‖ftn−gtn‖∞ +‖gtn−gt‖∞ +‖gt−ft‖∞
It’s easy to see ‖ftn−gtn‖∞ and‖gt−ft‖∞ are small since‖g−f‖∞ <ϵ . For‖gtn−gt‖∞, then
‖gtn−gt‖∞ = sup
x∈R
|gtn(x)−gt(x)| = sup
x∈R
|g(x +tn)−g(x +t)|
where for each ﬁxed tn→ t, since g is compactly supported and continuous then can be suﬃ-
ciently small for large enough n.
Therefore, the map G : R→ C0(R) given by G(t) = ft is continuous. Since {ft| t∈ [0, 1]} =
G([0, 1]) and continuous maps preserve compactness, then the set is compact in the norm topol-
ogy.
(b) Prove that {ft|t∈ R} is relatively compact in the weak topology.
Proof. here
Problem 7. Letf be an arbitrary real valued function on [0, 1]. Show that the set of points at
which f is continuous is a Lebesgue measurable set.
Proof. Similar to August 2016, #3.
In fact, we will prove that the set of points at which f is discontinuous is a countable union of closed
subsets.
f is continuous at p if for all n, there exists an open U containingp such that|f(x)−f(y)| < 1/n
for all x,y∈U. Fix n and let
Vn =
⋃
p
{p s.t. there exists an appropriate U} =
⋃
{appropriate U}
Hence, Vn is open. Then
{points where f is continuous} =
⋂
n
Vn
So{points where f is discontinuous} =⋃
nVc
n where Vc
n is closed.
Problem 8. Show that not every nonempty bounded closed subset of 𝓁2 has a point of minimal
norm, but that every nonempty bounded closed convex subset of 𝓁2 has a point of minimal norm.
Proof. Let C be the bounded, closed, convex subset of 𝓁2. Consider the set {y∈ R|y =‖x‖,x∈C}
and since this set is bounded below, there exists an inﬁmum of the set, say s. Then we can ﬁnd a
sequence xn∈C such that s≤‖xn‖≤ s + 1
n.
100

17 AUGUST 2011 Kari Eiﬂer
I claim that (xn) is a Cauchy sequence. Indeed, for any ϵ > 0, choose r to be the positive root of
the equation r2 + 2rs− ϵ2
4 = 0.
Since‖xn‖→ s then there is an N such that s≤‖xn‖<s +r for all n≥N. If n,m≥N, then
‖‖‖‖
xm−xn
2
‖‖‖‖
2
= 2
‖‖‖xm
2
‖‖‖
2
+ 2
‖‖‖xn
2
‖‖‖
2
−
‖‖‖‖
xm +xn
2
‖‖‖‖
2
< (s +r)2
2 + (s +r)2
2 −s2 = 2sr +r2 = ϵ2
4.
So (xn) is a Cauchy sequence, which means it converges to some x. Since C is closed, x∈ C and
obtains minimal norm.
Note: This choice of x is unique! If there were two points of minimal norm, say x1 and x2 then
1
2(x1 + x2) ∈ C by the convexity of C. So s ≤
‖‖ 1
2(x1 +x2)
‖‖ ≤ 1
2‖x1‖ + 1
2‖x2‖ = s. Hence,
‖x1 +x2‖ = 2s. By the parallelogram law,
‖x1 +x2‖2 +‖x1−x2‖2 = 2‖x1‖2 + 2‖x2‖2
And so‖x1−x2‖2 = 4s2− 4s2 = 0 so x1 =x2, proving uniqueness.
Counterexample: Consider M =
{n+1
n en|n∈ N
}
. M is closed since the distance between any two
of its elements is greater than
√
2 (and thus the only convergent sequences from M are those that
are eventually constant). M is clearly non-empty and has no element of minimal norm.
Problem 9. Show that there is a sequence {fn} of continuous functions on [0, 1] such that
(a) |fn(t)| = 1 for all n and all t∈ [0, 1] and
(b) for all g∈L1[0, 1] one has
∫ 1
0 fn(t)g(t)dt→ 0 as n→∞
Proof. NOT POSSIBLE??
If fn is continuous on [0, 1] and|fn(t)| = 1 then fn(t) = ±1. Since fn is continous, each fn is the
constant function at either 1 or −1. Write it as fn(x) = (−1)kn where kn is even or odd depending
on n.
Then if we take g to be the constant function 1, we get
∫ 1
0
fn(t)g(t)dt =
∫ 1
0
(−1)kndt = (−1)kn
which does not have to converge to 0 as n→∞ .
right? obvious? I don’t get it...
Problem 10. (a) Deﬁne what it means for a real valued function on [0, 1] to be absolutely continu-
ous.
101

17 AUGUST 2011 Kari Eiﬂer
Proof. The function f : [0, 1]→ R is absolutely continuous if for every ϵ > 0 there exists δ >
0 such that whenever a ﬁnite sequence of pairwise disjoint sub-intervals ( xk,yk) of [0, 1] with
xk,yk∈ [0, 1] satisfy∑
k(yk−xk)<δ then∑
k|f(yk)−f(xk)|<ϵ .
Equivalently,f has a derivative f′ almost everywhere and the derviative is Lebesgue integrable
and for all x∈ [0, 1],
f(x) =f(0) +
∫ x
0
f′(t)dt.
(b) Prove that if f and g are absolutely continuous strictly positive functions on [0, 1] then f/g is
absolutely continuous on [0, 1].
Proof. Step 1: If f is absolutely continuous, then so is 1/f.
Since f >0 is continuous on a compact space, there exists some M∈ N such that 1
M≤|f(x)|≤
M for all x∈ [0, 1].
Indeed, since g is absolutely continuous then for every ϵ > 0, there exists a δ > 0 such that
whenever a ﬁnite sequence of pairwise disjoint sub-intervals ( xk,yk) of [0, 1] with xk,yk∈ [0, 1]
satisfy∑
k(yk−xk)<δ then∑
k|f(yk)−f(xk)|< ϵ
M 2 . Then for such intervals, we have
∑⏐⏐⏐⏐
1
f(yk)− 1
f(xk
⏐⏐⏐⏐ =
∑⏐⏐⏐⏐
f(xk)−f(yk)
f(yk)f(xk)
⏐⏐⏐⏐
≤
∑⏐⏐⏐⏐
1
f(yk)
⏐⏐⏐⏐
⏐⏐⏐⏐
1
f(xk)
⏐⏐⏐⏐|f(yk)−f(xk)|
≤M 2∑
|f(yk)−f(xk)|
=M 2 ϵ
M 2 =ϵ.
Step 2: If f and g are both absolutely continuous, then so is fg .
Find M∈ N such that|f(x)|,|g(x)|≤ M for all x∈ [0, 1].
Takeδ1 such that if ∑yk−xk <δ 1 then∑|f(yk)−f(xk)|<ϵ/ 2M. Similarly, take δ2 such that
if∑yk−xk <δ 2 then∑|g(yk)−g(xk)|<ϵ/ 2M. Let δ = min(δ1,δ 2). Now
∑
|(fg )(yk)− (fg )(xk)| =
∑
|f(yk)g(yk)−f(xn)g(xn)|
≤
∑
|f(yk)g(yk)−f(yk)g(xk)| +|f(yk)g(xk)−f(xk)g(xk)|
≤
∑
|f(yk)||g(yk)−g(xk)| +
∑
|g(xn)||f(yk)−f(xk)|
≤M
∑
|g(yk)−g(xk)| +M
∑
|f(yk)−g(xk)|
≤M ϵ
2M +M ϵ
2M
=ϵ
Combining the two steps, we see immediately that f/g is absolutely continuous.
102

