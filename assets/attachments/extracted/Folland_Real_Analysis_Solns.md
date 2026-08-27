Partial Solutions to Folland’s Real Analysis: Part I
(Assigned Problems from MAT1000: Real Analysis I)
Jonathan Mostovoy - 1002142665
University of Toronto
January 20, 2018
Contents
1 Chapter 1 3
1.1 Folland 1.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Folland 1.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Folland 1.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4 Boxes vs cylinder sets w.r.t. σ-algebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.5 Folland 1.7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.6 Folland 1.8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.7 Folland 1.9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.8 Folland 1.10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.9 Folland 1.13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.10 Folland 1.17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
1.11 Folland 1.18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
1.12 Folland 1.26 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
1.13 Folland 1.28 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.14 Folland 1.30 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.15 Folland 1.31 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.16 Folland 1.33 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2 Chapter 2 15
2.1 Folland 2.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.2 Folland 2.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.3 Folland 2.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.4 Folland 2.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.5 Folland 2.7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.6 Folland 2.8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.7 Folland 2.9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
2.8 Folland 2.10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.9 Folland 2.12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.10 Folland 2.13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.11 Folland 2.14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.12 Folland 2.16 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
2.13 Folland 2.17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.14 Diﬀerentiable functions are Borel Measurable . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.15 Folland 2.20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
1

2.16 Folland 2.21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
2.17 Folland 2.24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.18 Folland 2.34 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.18.1 Folland 2.33 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2.19 Folland 2.39 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.20 Folland 2.42 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.21 Folland 2.44: Lusin’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.22 Folland 2.46 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
2.23 Folland 2.48 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
2.24 Folland 2.49 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3 Chapter 3 30
3.1 Folland 3.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.2 Folland 3.7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3 Folland 3.12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.4 Folland 3.13 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.5 Folland 3.17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.6 Folland 3.20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.7 Folland 3.21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.8 Folland 3.24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.9 Folland 3.25 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
3.10 Folland 3.26 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4 Chapter 5 39
4.1 Folland 5.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.2 Folland 5.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.3 Folland 5.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.4 Folland 5.6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.5 Folland 5.9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5 Chapter 6 44
5.1 Folland 6.3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.2 Folland 6.4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.3 Folland 6.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.4 Folland 6.7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.5 Folland 6.10 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.6 Folland 6.14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
2

1 Chapter 1
1.1 Folland 1.2
Prove the following Proposition:
Proposition. 1.1:
BR is generated by each of the following:
(a) the open intervals: E1 ={(a,b )|a<b },
(b) the closed intervals: E2 ={[a,b ]|a<b },
(c) the half-open intervals: E3 ={(a,b ]|a<b }or E4 ={[a,b )|a<b },
(d) the open rays: E5 ={(a,∞)|a∈R}or E6 ={(−∞,a )|a∈R},
(e) the closed rays: E7 ={[a,∞)|a∈R}or E8 ={(−∞,a ]|a∈R},
Proof. Most of the proof is already completed by Folland. What was shown is that M(Ej)⊂BR∀j =
1,..., 8. To ﬁnish the proof and show BR = M(Ej)∀j, we can simply show that BR ⊂M(Ej)∀j.
By invoking Lemma 1.1, if the family of open sets lie in M(Ej), then it must be that BR ⊂M(Ej).
Furthermore, it is actually suﬃcient to only show that all the open intervals lie in M(Ej) since every
open set in R is a countable union of open intervals. Thus, we complete our proof by directly showing
the following:
1. (a,b )∈E1⇒(a,b )∈M(E2).
2. (a,b ) =∪∞
1 [a +n−1,b−n−1]∈M(E2)
3. (a,b ) =∪∞
1 (a,b−n−1]∈M(E3)
4. (a,b ) =∪∞
1 [a +n−1,b )∈M(E4)
5. (a,b ) = (a,∞)\ (−∞,b ) = (a,∞)\ [b,∞)c = (a,∞)\
(
\∞
1 (b−n−1,∞)
{c
∈M(E5)
6. (a,b ) = (a,∞)\ (−∞,b ) = (−∞,a ]c\ (−∞,b ) =
(
\∞
1 (−∞,a +n−1)
{c
\ (−∞,b )∈M(E6)
7. (a,b ) = (a,∞)\ (−∞,b ) =
(
∪∞
1 [a +n−1,∞)
{
\ [b,∞)c∈M(E7)
8. (a,b ) = (a,∞)\ (−∞,b ) = (−∞,a ]c\
(
∪∞
1 (−∞,b−n−1]
{
∈M(E8)
1.2 Folland 1.4
Prove the following proposition:
Proposition. 1.2:
An algebra A is aσ-algebra ⇐⇒A is closed under countable increasing unions (i.e., if{Ej}∞
1 ⊂A
and E1⊂E2⊂···, then∪∞
1 Ej∈A).
3

Proof. The forward direction (σ-algebra⇒closed under countable increasing unions) is by the deﬁnition
ofσ-algebra (closed under countable unions ). The backward direction (closed under countable increasing
unions⇒closed under countable increasing unions ⇒σ-algebra) is slightly more involved:
If{Fi}∞
1 ∈A, then let us deﬁne Ej :=∪j
1Fi. Since countable unions of countable unions is countable,
and since {Ej}∞
1 has the property of E1⊂E2⊂···, then we know that ∪∞
1 Ej∈A. However, since
it is also the case that ∪∞
1 Fi =∪∞
1 Ej, we can conclude that ∪∞
1 Fi∈A as well, and thus proving the
backward direction.
1.3 Folland 1.5
Prove the following Proposition:
Proposition. 1.3:
If M(E) is the σ-algebra generated by E, then M(E) is the union of the σ-algebras generated by
Fαas Fαranges over all countable subsets of E.
Proof. We use the notation Fαto denote a countable subset of E, and we let F :={Fα|α∈A}denote
the (likely uncountable) set of all countable subsets of E. Let us also deﬁne ˆM :=∪α∈AM(Fα). We
proceed now by ﬁrst showing that ˆM is indeed a σ-algebra by showing that ˆM is closed under countable
unions and compliments:
Suppose{Ei}∞
1 ∈ˆM. Since ˆM is simply the union of a many σ-algebras, we know immediately that∀Ei
∃at least one Fi s.t. Ei∈M(Fi). Since a countable union of countable elements is countable, if we deﬁne
H :=∪∞
1 Fi where Ei∈M(Fi), we know that H is also countable subset of E. We can now look at the
properties of the following σ-algebra: M(H).
(1) Since Fi⊂H⊂M(H)⇒M(Fi)⊂M(H) (by Lemma 1.1), and since Ei∈M(Fi), we can say that
{Ei}∞
1 ∈M(H).
(2) Since H is a countable subset of E, we know that∃βs.t. H = Fβ, and hence M(H)⊂ˆM.
Therefore, since M(H) is by construction aσ-algebra and from (1) ({Ei}∞
1 ∈M(H)) it⇒∪∞
1 Ei∈M(H),
and by (2) ( M(H)⊂ˆM)⇒∪∞
1 Ei∈ˆM.
To now show ˆM is closed under compliments, suppose E∈ˆM. By the same argument already used,
there must exist a countable subset Fα⊂E s.t. E∈M(Fα), and obviously since M(Fα) is a σ-algebra,
Ec∈M(Fα). Therefore, since M(Fα)⊂ˆM⇒Ec∈ˆM. We have thus shown that ˆM is is closed under
countable unions and compliments, and hence a σ-algebra.
To neatly ﬁnish up our proof, let us ﬁrst note that ∀α∈A, Fα⊂E⇒M(Fα)⊂M(E), and thus we
can also say ˆM⊂M(E). To show the opposite relation, let ε∈E, then εis trivially countable, so ∃β
s.t. ε= Fβ⇒ε∈ˆM. Now since this is true ∀ε∈E, we can say that E⊂ˆM, which therefore (again by
Lemma 1.1)⇒M(E)⊂M. By showing both opposite relations, we can thus conclude that M(E) = ˆM.
4

1.4 Boxes vs cylinder sets w.r.t. σ-algebras
Exercise. 1.1:
LetA be an index set,{Xα}α∈A a family of non-empty sets and for eachα∈A, Mαbe aσ-algebra
on Xα. Consider the product space:
X =

α∈A
Xα
Let M be the σ-algebra generated by the cylinder sets C :={π−1
α(Eα)|Eα∈Mα,α∈A}, and
M∗be the one generated by boxes B :={
α∈AEα|Eα∈Mα}. Show that M⊂M∗, but in
general M⁄= M∗
Hint 1: Proposition 1.3 implies that if A is countable then M = M∗; we should thus take A to be
not countable.)
Hint 2: You might ﬁnd useful to ﬁrst prove the following intermediate result. For any A′⊂A, let
MA′= M({π−1(Eα)|Eα∈Mα,α∈A′}); let now
˜M =

A′⊂A countable
MA′
Then show that M = ˜M. (Hint 2: show that ˜M is a σ-algebra which contains the cylinders...) The
above can be loosely stated as “any set in M is determined by countably many coordinates”
**Please note the notation used for the box and cylinder sets above.
Answer: To show M⊂M∗, note that π−1
α(Eα) =
β∈AEβ, where Eβ=Xβ∀β⁄=α. In this form, it
is clear that C⊂B ⊂M∗⇒M⊂M∗(by Lemma 1.1).
Next, let us prove that M = ˜M:
Proof. Suppose{Fi}∞
1 ∈˜M. Then since ˜M is a union of σ-algebras, it must be that Fi∈MA′for at least
one A′. Taking A′′to be the union of one of the A′s which satisﬁes Fi∈MA′for each i. Thus, A′′will
naturally also be a countable set. Since A′′is a countable set, MA′′⊂˜M⇒∪∞
1 Fi∈˜M by Lemma 1.1.
Next, suppose F∈˜M, then∃A′s.t. F∈MA′, which impliesFc∈MA′, and since MA′⊂˜M,⇒Fc∈˜M,
and hence ˜M is indeed a σ-algebra.
Next, since A′⊂A,⇒MA′⊂M(= MA)∀A′, and thus since MA′⊂M∀A′⇒˜M⊂M. To show the
opposite inclusion, we know that ∀α∈A∃a countable subset A′⊂A s.t. α∈A′, namely{α}. In this
form, it is perfectly clear that π−1(Eα)⊂˜M, since π−1(Eα)∈MA′={α}⇒M⊂˜M. And thus M = ˜M.
Let us now turn our attention to the form in which the generating family of sets for MA′takes. Each set
is in the formπ−1(Eα) = (
β∈A′Eβ)×(
γ∈A\A′Xγ), whereA′is a countable set, andEβ=Xβ∀β⁄=α.
In this form, it is clear that after countably many intersections, compliments and unions, ∀E∈MA′,
E will still be in the form of ( 
β∈A′Eβ)×(
γ∈A\A′Xγ), where A′is a countable set, and Eβ∈Mβ.
However, when looking at the boxes, it is clear that ∃E∈M(B) s.t. E = (
β∈BEβ)×(
γ∈A\BXγ),
where B is an uncountable set, and Eβ∈Mβ.
1.5 Folland 1.7
Prove the following Proposition:
5

Proposition. 1.4:
If µ1,...,µn are measures on ( X, M) and a1,...,an ∈[0,∞), then ∑n
1ajµj is a measure on
(X, M).
Proof. Since µi i ∈ {1,...,n}are measures, we know that µi(⌀) = 0 ∀i = 1,...,n , and therefore
µ:=∑n
1ajµj(⌀) = 0. Next, suppose {Ej}∞
1 ∈M and{Ej}∞
1 disjoint, then:
µ
( n⨆
i=1
Ei
{
=
n∑
j=1
(
aj·µj
( n⨆
i=1
Ei
{(
=
n∑
j=1
(
aj·
∞∑
i=1
µj
(
Ei
{(
=
n∑
j=1
( ∞∑
i=1
aj·µj
(
Ei
{(
=
∞∑
i=1
µ(Ei)
1.6 Folland 1.8
Prove the following Proposition:
Proposition. 1.5:
If (X, M,µ) is a measure space and {Ej}∞
1 ⊂M, then µ(lim infEj) ≤lim infµ(Ej). Also,
µ(lim supEj)≥lim supµ(Ej) provided that µ(∪∞
1 Ej)<∞.
Proof. We ﬁrst recall the deﬁnitions of lim inf and lim sup for a sequence of sets as:
lim inf
n→∞
(Fn) :=
∞
k=1
(∞⋂
n=k
Fn
(
, and lim sup
n→∞
(Fn) :=
∞⋂
k=1
(∞
n=k
Fn
(
We now quickly prove the following Lemma:
Lemma. 1.1: A Corollary of Monotonicity and Subadditivity - (Again!)
If{Bi}∞
1 ⊂M, then:
(a) µ(\∞
1 Bi)≤µ(B1) (or µ(Bk) by switching B1 for Bk).
(b) µ(∪∞
1 Bi)≥µ(B1) (or µ(Bk) by switching B1 for Bk).
Note: I sorta forget these were either covered or corollaries from Thm 1.8 in Folland, hence why I included
it here - oh well (but I did give a slightly more concise proof for (b) :) )
Proof.
(a) Since (\∞
1 Bi)⊔(B1\\∞
1 Bi) =B1⇒µ(B1) =µ(\∞
1 Bi) +µ(B1\\∞
1 Bi)⇒µ(\∞
1 Bi)≤µ(B1).
(b) Since (B1)⊔(∪∞
2 Bi\B1) =∪∞
1 Bi⇒µ(∪∞
1 Bi) =µ(B1) +µ(∪∞
2 Bi\B1)⇒µ(∪∞
1 Bi)≥µ(B1).
6

We now have all the necessary tools to prove the proposition as follows:
µ
(
lim infEj
{
=µ


∞
k=1


∞⋂
j=k
Ej
(
(
(
( ∗
= lim
k→∞
µ


∞⋂
j=k
Ej
(
( = lim inf
k→∞
µ


∞⋂
j=k
Ej
(
(
∗
≤lim inf
k→∞
µ(Ej)
Where
∗
= is by µ’s “Continuity from below” since\∞
j=kEj⊂\∞
j=k+1Ej∀k∈N, and
∗
≤is by Lem 2.1 (a).
µ
(
lim supEj
{
=µ


∞⋂
k=1


∞
j=k
Ej
(
(
(
( ⋆
= lim
k→∞
µ


∞
j=k
Ej
(
( = lim inf
k→∞
µ


∞
j=k
Ej
(
(
⋆
≥lim inf
k→∞
µ(Ej)
Where
⋆
= is by µ’s “Continuity from above” since∪∞
j=k+1Ej⊂∪∞
j=kEj∀k∈N, and
⋆
≤is by Lem 2.1 (b).
1.7 Folland 1.9
Prove the following Proposition:
Proposition. 1.6:
If (X, M,µ) is a measure space and E,F ∈M, then µ(E) +µ(F ) =µ(E∪F ) +µ(E\F ).
Proof. Firstly, let us make the following observations:
(E\F )⊔F = (E∪F ), and ( E\F )⊔(E\F ) =E
Therefore, since µis countably additive and therefore ﬁnitely additive, we can now see that:
µ(E) +µ(F ) =µ
(
(E\F )⊔(E\F )
{
+µ(F )
=µ(E\F ) +µ(E\F ) +µ(F )
=µ(E\F ) +µ
(
(E\F )⊔F
{
=µ(E\F ) +µ(E∪F )
1.8 Folland 1.10
Prove the following Proposition:
Proposition. 1.7:
Given a measure space, (X, M,µ) and E∈M, deﬁne µE(A) =µ(A\E) for A∈M. Then µE is
a measure.
Proof. We ﬁrst conﬁrm that µE(⌀) = 0 since µE(⌀) =µ(⌀\E) =µ(⌀) = 0. Next, let {Fi}∞
1 ⊂M and
{Fi}∞
1 disjoint. Then:
µE
(∞
i=1
Fi
(
=µ
(
E\
(∞
i=1
Fi
((
=µ
((∞
i=1
E\Fi
((
∗
=
∞∑
i=1
µ(E\Fi) =
∞∑
i=1
µE (Fi)
Where
∗
= since if{Fi}∞
1 is a disjoint family of sets, then{Fi\E}∞
1 will be as well. Thus, we have shown
µE is indeed a measure.
7

1.9 Folland 1.13
Prove the following Proposition:
Proposition. 1.8:
Everyσ-ﬁnite measure is semi-ﬁnite.
Proof. Letµbe a σ-ﬁnite measure on the measurable space (X, M). Firstly, if µ(X)<∞,µwill trivially
be semi-ﬁnite. Therefore, suppose µis σ-ﬁnite, but not ﬁnite. Now, let us arbitrarily pick E∈M s.t.
µ(E) =∞(we know at least one such element exists, namelyX, since otherwiseµwould be ﬁnite). From
the deﬁnition of µbeing σ-ﬁnite, we know that ∃{Fi}∞
1 ⊂M s.t. X =∪∞
1 Fi and µ(Fi) <∞∀i∈N.
One can easily see the following:
µ(E) =µ(E\X) =µ
(∞
i=1
(E\Fi)
(
≤
∞∑
i=1
µ(E\Fi)
And since µ(E) =∞
⇒∞≤
∞∑
i=1
µ(E\Fi)⇒
∞∑
i=1
µ(E\Fi) =∞
Furthermore, sinceE⁄= ⌀ (since otherwiseµ(E) = 0<∞) andµ(E) =µ(⋃∞
i=1(E\Xi)), we know there
must exist at least one k∈N s.t. µ(E\Fk)> 0. On the other-hand, since µ(Fk)<∞by construction,
so too will µ(E\Fk)<∞. Therefore, since trivially E\Fk⊂E, we have shown that for an arbitrary
E∈M s.t. µ(E) = ∞,∃k∈N s.t. Fk\E⊂E and µ(Fk\E) <∞; I.e., all σ-ﬁnite measures are
semi-ﬁnite.
1.10 Folland 1.17
Prove the following Proposition:
Proposition. 1.9:
If µ∗is an outer measure on X and{Aj}∞
1 is a sequence of disjoint µ∗-measurable sets, then
µ∗(E\ (∪∞
1 Aj)) =∑∞
1 µ∗(E\Aj) for any E⊂X.
Proof. Firstly, sinceµ∗is an outer measure, we know that:
µ∗(E\ (∪∞
1 Aj)) =µ∗((∪∞
1 E\Aj))≤
∞∑
j=1
µ∗(E\Aj)
Now, let us deﬁne Bn :=∪n
1Ej. Now, since Aj is µ∗-measurable∀j∈N, we know that∀n> 1:
µ∗(E\Bn) =µ∗((E\Bn)\An) +µ∗((E\Bn)\Ac
n) =µ∗(E\An) +µ∗(E\Bn−1)
Therefore, iteratively using the above formula (by induction) for Bn,...,B 2, and countable additivity
being trivial for n = 1, we have shown that:
µ∗

E\
n
j=1
Aj
(
( =
n∑
j=1
µ∗(E\Aj), ∀n∈N
8

Now, by monotonicty, we can easily see that:
µ∗

E\
∞
j=1
Aj
(
(≥µ∗

E\
n
j=1
Aj
(
( =
n∑
j=1
µ∗(E\Aj), ∀n∈N
And hence µ∗
(
E\⋃∞
j=1Aj
{
≥∑∞
j=1µ∗(E\Aj). And thus since we shown both ≥and≤, we can
conclude that µ∗(E\ (∪∞
1 Aj)) =∑∞
1 µ∗(E\Aj).
1.11 Folland 1.18
Prove the following Proposition:
Proposition. 1.10:
Let A⊂P(X) be an algebra, Aσthe collection of countable unions of sets in A, and Aσδthe
collection of countable intersections of sets inAσ. Let µ0 be a premeasure on A andµ∗the induced
outer measure.
a) For any E⊂X and ϵ>0, there exists B∈Aσwith E⊂B and µ∗(B)≤µ∗(E) +ϵ
b) If µ∗(E) <∞, then E is µ∗-measurable ⇐⇒there exists C ∈Aσδwith E ⊂C and
µ∗(C\E) = 0.
c) If µ0 is σ-ﬁnite, the restriction µ∗(E)<∞in (b) is superﬂuous.
Proof.
a) Let us recall the deﬁnition of µ∗(E) as:
µ∗(E) := inf
{ ∞∑
i=1
µ0(Ai)
⏐⏐⏐⏐{Ai}∞
1 ⊂A,E ⊂
∞
i=1
Ai
{
Therefore, by the deﬁnition of inf, ∀ϵ >0∃{Bi}∞
1 s.t. E⊂∪∞
1 Bi and∑∞
1 µ0(Bi)≤µ∗(E) +ϵ.
Therefore, if we deﬁne B :={Bi}∞
1 (same seq. as before), we note that B∈Aσ, and also that:
µ∗(B)
∗
≤
∞∑
i=1
µ0(Ai)≤µ∗(E) +ϵ
Where
∗
≤because µ0(Bi) =µ∗(Bi), and B is µ∗-measruable.
b) Let us begin with the forward direction ( µ∗(E) <∞, and E is µ∗-measurable). From part (a),
we know ∃ {Ci} ⊂Aσs.t. E ⊂Ck and µ∗(Ck) ≤µ∗(E) + 1
k ∀k ∈N. Let us now deﬁne
C :=\∞
1 Ci, to which we notice that C ∈Aσδand E⊂C since E⊂Ck∀k∈N, and hence
µ∗(E)≤µ∗(C). Furthermore, we note that since Ck is µ∗-measurable, so too will Cc
k, and hence
∪∞
1 Cc
i = (\∞
1 Ci)c = Cc is µ∗-measurable, and hence C is µ∗-measurable. Now, the following
observation becomes apparent:
µ∗(C) =µ∗
(∞⋂
i=1
Ci
(
= lim
n→∞
µ∗
( n⋂
i=1
Ci
(
≤lim
n→∞
µ∗(Cn) =µ∗(E)
9

Moreover, using the fact that E⊂C the above now actually implies that µ∗(E) =µ∗(C). We also
recall that since Ec is µ∗-measurable, and since we already showed that C wasµ∗-measurable, we
can now also say that C\Ec =B\E is µ∗-measurable, and also note that hence:
µ∗(C\E) =µ∗(C)−µ∗(C\E) =µ∗(C)−µ∗(E) = 0
For the backward direction (there exists C∈Aσδwith E⊂C and µ∗(C\E) = 0), ﬁrst note that
sinceE⊂C),C = (B\E)∪E. Next, since µ∗is the Carath` eodory extension,C\E isµ∗-measurable.
Therefore, we can easily conclude that E =B\(B\E) is also µ∗-measurable.
c) Firstly, since µ0 is σ-ﬁnite, we know that∃a disjoint set{Xi}∞
1 ⊂A s.t. X =⊔Xi and µ0(Xk)<
∞ ∀k ∈N. Next, since E ⊂X is measurable, so too will Ek := E\ Xk ∀k ∈N, and by
above and since {E\Ei}∞
1 is disjoint, we know that E =⊔∞
1 (E\Xi) = ⊔∞
1 Ei, and naturally
µ0(E\Xk) <∞∀k∈N. Since we are able to write E in this construction, E is µ∗-measurable.
We can now ﬁgure out the following line of reasoning:
Eµ∗-measurable ⇐⇒Eiµ∗-measurable
⇐⇒ ∃Ci∈A s.t. Ei⊂Ci,µ∗(Ci\Ei) = 0
⇐⇒E⊂C =
∞
i=1
Ci =
∞
i=1


∞⋂
j=1
(∞
k=1
Aijk
((
(⊂
∞⋂
i=1


∞⋂
j=1
(∞
k=1
Aijk
((
(∈Aσδ
Where µ∗(C\E) = µ∗(∪∞
1 Ci\Ei)≤∑∞
1 µ∗(Ci\Ei) =∑∞
1 0 = 0. And hence µ∗(E)<∞did not
matter if µ0 is σ-ﬁnite.
1.12 Folland 1.26
Prove the following Proposition (by using Folland, Theorem 1.19):
Proposition. 1.11:
IfE∈Mµandµ(E)<∞, then∀ϵ>0∃a set A that is a ﬁnite union of open intervals such that
µ(E∆A)<∞.
Proof. We recall that by Theorem 1.18, ∃Uopen s.t. E⊂U and µ(U)≤µ(E) + 1
2ϵ. Furthermore, by the
inequality just stated, we know that µ(U),µ(E)<∞, and hence:
µ(U\E) =µ(U)−µ(E)< 1
2ϵ
Now, by recalling that all open sets in R can be written as⊔∞
1 Ui, we know that∃{Ui}∞
1 s.t.⊔∞
1 Ui = U.
We now prove that actually:
∃N∈N s.t. µ(U) =µ(⊔∞
1 Ui = U)<µ
(
⊔N
1 Ui
{
+ 1
2ϵ
To see this, since{Ui}∞
1 is disjoint:
∞∑
i=1
µ(Ui) =µ(U)<µ(E)<∞
10

Therefore, the series∑∞
1 µ(Ui) must converge, and hence, by the deﬁnition of convergent series’,∃N∈N
s.t. ∑∞
N +1µ(µ(Ui))< 1
2ϵ, and thus the inequality we sought to prove has now been shown.
Carrying on, let us deﬁne ˜U :={Ui}N
1 . Since ˜U⊂U⇒µ(˜U)≤µ(U) <∞and also ⇒˜U\E⊂U\E,
hence:
µ(˜U\E)≤µ(U\E)< 1
2ϵ
Now, also since µ(˜U)<∞, and since ˜U⊂U⇒E\˜U⊂U\˜U, we can see that:
µ(E\˜U)≤µ(U\˜U) =µ(U)−µ(˜U) =
∞∑
i=N +1
µ(Ui)< 1
2ϵ
Therefore, by combining the last two main inequalities, we have found a setA = ˜U which is a ﬁnite union
of open intervals such that:
µ(E∆˜U) =µ(E\˜U) +µ(˜U\E)< 1
2ϵ+ 1
2ϵ=ϵ
1.13 Folland 1.28
Prove the following Proposition:
Proposition. 1.12:
Let F be increasing and right continuous, and let µF be the associated measure. Then:
a) µF ({a}) =F (a)−F (a−)
b) µF ([a,b )) =F (b−)−F (a−)
c) µF ([a,b ]) =F (b)−F (a−)
d) µF ((a,b )) =F (b−)−F (a)
Proof.
a) We ﬁrst note that we may construct {a}from a countable intersection of h-intervals as follows:
{a}=
∞⋂
n=1
(a−1/n,a ]
Furthermore, since (a−1/n,a ]⊃(a−1/(n + 1),a ]∀n∈N, we may invoke continuity from above
in that:
µF ({a}) = lim
n→∞
µF ((a−1/n,a ]) = lim
n→∞
(F (a)−F (a−1/n))
∗
=F (a)−F (a−)
Where
∗
= can be rigorously shown by noting that since F is an increasing function:
lim
n→∞
F (a−1/n) = sup{F (x)|x<a }=F (a−)
11

b) We ﬁrst note that we may construct [ a,b ) from a union of countable intersections and unions of
h-intervals as follows:
[a,b ) = [a, (a +b)/2]∪(a,b ) =
(∞⋂
n=1
(a−1/n, (a +b)/2]
(
∪
( ∞
m=1
(a,b−1/m]
(
Like in part a):
µF ([a, (a +b)/2]) = lim
n→∞
µF
(∞⋂
n=1
(a−1/n, (a +b)/2]
(
= lim
n→∞
(F ((a +b)/2)−F (a−1/n))
∗
=F ((a +b)/2)−F (a−)
Where
∗
= is reasoned exactly as in a). Furthermore, since (a,b−1/m)⊂(a,b−1/(m + 1))∀m∈N,
we may invoke continuity from below in that:
µF ((a,b )) = lim
n→∞
µF
(∞
n=1
(a,b−1/m]
(
= lim
n→∞
(F (b−1/m)−F (a))
⋆
=F (b−)−F (a)
Where
⋆
= can be rigorously shown by noting that since F is an increasing function:
lim
n→∞
F (b−1/m) = sup{F (x)|x<b }=F (b−)
Therefore, since all the sets we’ve been dealing with so far have been bounded, we can see now that:
µF
(
[a,b )
{
=µF
(
[a, (a +b)/2]
{
+µF
(
(a,b )
{
−µF
(
(a,b )\ [a, (a +b)/2]
{
=µF
(
[a, (a +b)/2]
{
+µF
(
(a,b )
{
−µF
(
(a, (a +b)/2]
{
=
⨆
F
(
(a +b)/2
{
−F
(
a−
{
+
⨆
F
(
b−
{
−F
(
a
{
−
⨆
F
(
(a +b)/2
{
−F
(
a
{
=
⨆
F (b−)−F (a−)

+
⨆
F
(
(a +b)/2
{
−F
(
(a +b)/2
{
+
⨆
F
(
a
{
−F
(
a
{
=F (b−)−F (a−)
c) We ﬁrst note that we may construct [ a,b ] from countable intersection of h-intervals as follows:
[a,b ] =
∞⋂
n=1
(a−1/n,b ]
Thus, by making the change of variables of (a +b)/2→b, from the ﬁrst half of b), we have already
shown that µF ([a,b ]) =F (b)−F (a−).
d) We ﬁrst note that we may construct ( a,b ) from a countable union of h-intervals as follows:
∞
n=1
(a,b−1/n]
Thus, from the second half of b), we have already shown that µF ((a,b )) =F (b−)−F (a).
12

1.14 Folland 1.30
Prove the following Proposition:
Proposition. 1.13:
If E∈L and m(E)> 0, for any α<1∃an open interval ˆI such that m(E\I)>αm(I).
Proof. If α≤0, since m(E)> 0⇒∃F⊂E s.t. m(F )> 0, and F = (a,b ],a<b . If we thus take:
ˆI =
(1
4(a +b), 3
4(a +b)
{
We havem(E\I) =m(I)> 0≥αm(I).
Now suppose 0 < α <1. Since m is semi-ﬁnite, if m( ˆE) = ∞, we can simply take E⊂ˆE s.t. 0 <
m(E)<∞, and hence we actually restrict our problem to that of all E’s s.t.E∈L and 0<m (E)<∞.
Let us also quickly note/recall that:
m({b}) = 0⇒m((a,b ]) =m
(
(a,b )⊔{b}
{
=m
(
(a,b )
{
+m
(
{b}
{
=m
(
(a,b )
{
Now, for the sake of contradiction, assume∀I = (a,b ),a<b , we have: m(E\I)≤αm(I). Let us choose
ϵ1 > 0 so that ϵ1 < 1−α
α (and hence α(1 +ϵ1) < 1). Moreover, from (Folland) Theorem 1.18, we know
that∀ϵ2 > 0∃I =⊔∞
1 (ai,bi) s.t. E⊂I and m(I) = ∑∞
1 m
(
(ai,bi)
{
< m(E) +ϵ2. Next, from our
discussion on (a,b ) v.s. (a,b ], we can actually write I =⊔∞
1 (ai,bi], where I still satisﬁes everything that
it did beforehand. Now, if we let ϵ2 =m(E)ϵ1, (which we can certainly do sincem(E)<∞), we see that:
m(I) =
∞∑
i=1
(ai,bi]<m (E) +m(E)ϵ1 =m(E)(1 +ϵ1)<m (E)
(
1 + 1−α
α
{
=m(E) 1
α
⇒αm(I)<m (E)
Therefore, by combining the above inequality with our assumption in that m(E\Ik)≤αm(Ik)∀k∈N,
and that E⊂I, we see that:
m(E) =m(E\I) =
∞∑
i=1
m(E\Ii)≤
∞∑
i=1
αm(Ii) =αm(I)<m (E)
Which is obviously a contradiction on the requirement of m(E) > 0, hence the converse must be true:
I.e. our Proposition is true.
1.15 Folland 1.31
Prove the following Proposition:
Proposition. 1.14:
If E∈L, and m(E)> 0, the set {E−E}:={x−y|x,y ∈E}contains an interval centered at
0. (If I is as in (Folland) Exercise 1.30, with α>3
4, then{E−E}contains (−1
2m(I), 1
2m(I)).)
Proof. From (Folland) 1.30, we know that∃I s.t. 3
4m(I)<m (E\I). Let us now deﬁne F :=E\I⊂E,
and naturally we will have {F−F}⊂{E−E}, hence if∃an interval centered at 0 in {F−F}, so too
will that interval be in {E−E}.
13

We now claim that F\{F +x0}⁄= ⌀⇒x0∈{F−F}. To see this, let y∈F\{F +x0}⇒y∈
F and∃x∈F s.t. y =x +x0⇒x0 =y−x,y,x ∈F⇒x0∈{F−F}.
Trivially 0∈{F−F}sinceF⁄= ⌀. Let us now let z0∈R s.t.|z0|< 1
2m(I)< 3
4m(I)<m (F ). If we can
show that F\{F +z0}⁄= ⌀⇒
(
−1
2m(I), 1
2m(I)
{
⊂{E−E}. Therefore, the remainder of this proof
will be dedicated to showing F\{F +z0}⁄= ⌀ where|z0|< 1
2m(I).
Firstly, we note that:
m(I\F ) =m(I)−m(F ) =m(I)−m(E\I)≤m(I)−3
4m(F ) = 1
4m(F )
Furthermore, by applying the useful fact that A\B = ((A\C)\B)∪((C\A)\B) twice, we ﬁnd:
I\{I +z0}=

F\{F +z0}

∪

F\ ({I\F}+z0)

∪

(I\F )\{I +z0}

Our strategy now will be to show that m
(
F\{F +z0}
{
> 0, which therefore would imply I\{I +z0}
also has positive measure, and hence cannot be empty. To see this ﬁrst note the following four properties:
m(I\{I +z0})≤m

F\{F +z0}

+m

F\ ({I\F}+z0)

+m

(I\F )\{I +z0}

and: m

F\ ({I\F}+z0)

≤m

{(I\F ) +z0}

=m

I\F ]≤1
4m(F ) from previously
and: m

F\ ({I\F}+z0)

≤m(I\F )≤1
4m(I) again
and: 1
2m(I)<m (I)−|z0|=m

I\{I +z0}

And hence combing all these we see that:
1
2m(I)<m

I\{I +z)}

≤m

F\{F +z0}

+ 1
2m(I) ⇒m

F\{F +z0}

> 0
1.16 Folland 1.33
Prove the following Proposition:
Proposition. 1.15:
There exists a Borel set A⊂[0, 1] such that 0<m (A\I)<m (I) for every sub-intervalI of [0, 1].
(Hint: Every sub-interval of [0, 1] contains Cantor-type sets of positive measure.)
Proof. The ﬁrst observation we need to make is that since |Q|=ℵ0⇒|Q×Q|=ℵ0 (ℵ0 := “countably
inﬁnite”). Therefore, we can actually write the set of all closed sets Ik inside [0, 1] where Ik’s endpoints
are rational numbers as a countable list: ˆI ={Ij}∞
1 . By the hint, we know that every sub-interval of
[0, 1] contains Cantor-type sets (which will certainly have rational endpoints). Our plan will therefore
be through induction, to explicitly describe a Borel set made up of necessary Cantor-like sets which will
satisfy the needed inequality.
LetAk,Bk be strict subsets ofIk (which we can do because we’re assumingI⁄= ⌀, and due to the density
of the rationals) s.t. Ai\Bk = ⌀ and m(Ai),m (Bj)> 0∀i,j ≤N. We can therefore deﬁne:
CN :=IN\
N⨆
j=1
(Aj∪Bj)
14

And therefore, we can ﬁnd a Cantor-type set DN and ˜DN s.t. m(DN),D ( ˜DN) > 0∀N∈N. If we let
D :=∪∞
N =1DN, then∀sub-intervalsI⊂[0, 1],∃N s.t. IN⊂I and we will have:
0<m (DN)≤m(D\IN)≤m(D\I)≤m(D\I) +m( ˜DN)≤m(I)
I.e., by seeing that A =D 0<m (I\D)<m (I).
2 Chapter 2
2.1 Folland 2.1
Prove the following Proposition:
Proposition. 2.1:
Let f :X→R and Y =f−1(R). Then f is measurable ⇐⇒f−1({−∞})∈M, f−1({∞})∈M,
and f is measurable on Y .
Proof. To be clear on notation, if X ={±∞}, then either X ={∞}or X ={−∞}, and naturally
{−∞,∞}⁄=X.
For the forward direction, since f is measurable and {±∞}∈BR, it implies f−1({±∞})∈M. Fur-
thermore, again by f’s is measurability and since R∈BR, it implies f−1(R)∈M. Therefore, we may
conclude that ifB∈BR, thenf−1(B)∈M andf−1(B)\f−1(R) =f−1(B)\Y ∈M, I.e.,f is measurable
on Y .
For the converse, if we let B∈BR, then we can see that:
f−1(B) =
(
f−1(B)\f−1(R)
{
⊔
(
f−1(B)\f−1(R\R)
{
And sincef−1(R) is measurable, naturally f−1(B)\f−1(R) =f−1(B\ R) is as well. Next, we note that:
f−1(B)\f−1(R\R) =f−1(B)\f−1({−∞,∞}) =f−1(B\{−∞,∞})
Which naturally is either f−1(⌀) = ⌀,f−1({−∞}),f−1({∞}), or f−1({−∞,∞}= f−1({−∞})∪
f−1({∞}), all of which are measurable since f−1({−∞}) and f−1({∞}) are by assumption measurable.
Combining these two implications of our assumptions, we can see f is measurable since:
f−1(B) =
(
f−1(B)\f−1(R)
{
⊔
(
f−1(B)\f−1(R\R)
{
∈M
2.2 Folland 2.2
Prove the following Proposition:
Proposition. 2.2:
Suppose f,g :X→R are measurable.
a) fg is measurable (where 0·(±∞) = 0).
b) Fix a∈R, and deﬁne h(x) = a if f(x) =−g(x) =±∞, and h(x) = f(x) +g(x) otherwise.
Then h is measurable.
15

Proof. We actually do this problem in reverse ordering.
b) We prove this fact by separating the problem into 2 lemmas, and one ﬁnal main result:
For the ﬁrst mini-lemma, we note that A∞:={x∈X|f(x) =−g(x) =±∞}is measurable since
f and g are measurable.
For the second mini lemma, we make the observation that:
h−1({∞}) = (f +g)−1({∞}) =
(
f−1({∞})\g−1((−∞,∞])
{
∪
(
f−1((−∞,∞])\g−1({∞})
{
Since h(x) = ∞ ⇐⇒either [f(x) = ∞and g(x) >−∞] or [g(x) = ∞and f(x) >−∞], or [
f(x) =g(x) =∞]. Similarly for the {−∞}(sub-) case:
h−1({−∞}) = (f +g)−1({−∞}) =
(
f−1({−∞})\g−1([−∞,∞))
{
∪
(
f−1([−∞,∞))\g−1({−∞})
{
Since h(x) =−∞ ⇐⇒either [f(x) =−∞and g(x) <∞] or [g(x) =−∞and f(x) <∞], or [
f(x) = g(x) =−∞]. We naturally recognize the above to certainly be measurable (again) since f
and g are measurable.
Now for the ﬁnal main result. Let b∈R, then:
h−1((b,∞]) =h−1((b,∞))∪h−1({∞)}
Since we already showed that h−1({∞}) is measurable, we now seek to show that h−1((b,∞)) is
measurable. This can be seen since:
h−1((b,∞)) =
{
(f +g)−1((b,∞)) if a≤b
(f +g)−1((b,a ))∪(h)−1({a})∪(f +g)−1((a,∞)) if a>b
=
{
(f +g)−1((b,∞)) if a≤b
A∞∪(f +g)−1((b,∞)) if a>b
Where we already showed that A∞is measurable, and by f and g’s measurability, all the sets
above which make up h−1((b∞)) are measurable, and hence h−1((b,∞]) is measurable; therefore,
h is measurable.
a) Let us deﬁne Q+ :={r∈Q|r> 0}and Q−:={r∈Q|r< 0}, which is a subsets of Q and hence
countable. Suppose now that f,g ≥0, if a≥0, then we will have:
(fg )−1((a,∞]) ={x∈X|f(x)g(x)>a}
=

r∈Q+
(
{x∈X|f(x)>r}\{x∈X|g(x)>a/r}
{
Furthermore, ifa< 0, (since f,g ≥0) we have:
(fg )−1((a,∞]) ={x∈X|f(x)g(x)>a}=X
Therefore, since irregardless of a, (fg )−1((a,∞]) is a countable union of measurable sets, fg is
measurable for f,g ≥0. Our strategy henceforth will be to write f =f +−f−
∗and g =g+−g−
∗,
where f + := max(0,f ),f−
∗:=−min(0,f ), and similarly for g. Therefore, we naturally have:
fg = (f +−f−
∗)(g+−g−
∗) =
(
f +g+ +f−
∗g−
∗
{
+
(
−
(
f +g−
∗+f−
∗g+{{
Now, by our previous work, since f +,g +,f−
∗,g−
∗≥0, it follows that the ﬁrst half of the above ex-
pression is measurable (since by part b, we showed that the addition of two measurable functions as
deﬁned in this question is measurable). And also recalling that f measurable ⇐⇒ −f measurable,
we can therefore conclude that fg is indeed measurable.
16

2.3 Folland 2.3
Prove the following Proposition:
Proposition. 2.3:
If{fn}is a sequnce of measurable functions on X, then{x|limfn(x) exists}is a measurable set.
Proof. We ﬁrst recall that by (Folland) Proposition 2.7, when{fn}is deﬁned as in the question, g3(x) =
lim supn→∞fn(x) andg4(x) = lim infn→∞fn(x) are both measurable. If, as in Exercise 2.2, we let a = 1,
then function g3−g4 is measurable (and is equal to 1 when g3 = g4 =±∞). Finally, by noting that
limfn(x) exists ⇐⇒g3 =g4, we can actually write:
{x∈X|limfn(x) exists}=Kernel(g3−g4) ={x∈X|g3(x) =g4(x)}= (g3−g4)−1(0)
Which is most certainly measurable sinceg3 andg4 are measurable, and the diﬀerence of such measurable
functions is also measurable (Corollary of Exercise 4 .2 by combining the fact that f measurable ⇐⇒
−f measurable, and taking f−g =f + (−g)).
2.4 Folland 2.4
Prove the following Proposition:
Proposition. 2.4:
If f :X→R and f−1((r,∞])∈M for each r∈Q, then f is measurable.
Proof. Firstly, by the density of the rationals, ( a,∞] = ∪r∈Q+
r
(r,∞], where a∈R, and Q+
a :={r∈
Q|r >a}. Naturally since Q+
a is countable and BR is generated by the intervals in the form of ( a,∞],
and since:
f−1((a,∞])⊂

r∈Q+
a
f−1((r,∞])∈M
By (Folland) Proposition 2.1, it follows that f is measurable.
2.5 Folland 2.7
Prove the following Proposition:
Proposition. 2.5:
Suppose that for each α∈R we are given a set Eα∈M such that Eα⊂Eβwhenever α < β,
∪α∈REα= X, and \α∈REα= ⌀. Then there is a measurable function f : X →R such that
f(x)≤αon Eαand f(x)≥αon Ec
αfor every α. (Use (Folland) Exercises 2.4).
Proof. We claim that f(x) := inf{α∈R|x∈Eα}, where Eαhas the same construction as given in the
Proposition, will satisfy the requirements of being measurable and the stated inequalities. We begin ﬁrst
by showing the latter.
Suppose x∈Eα, then by the construction of f, we immediately have f(x)≤α. Now, suppose α∈Ec
α,
then∀β≤α, Ec
α⊂Ec
βsince Eβ⊂Eα; therefore, x∈Ec
β⇒x⁄∈Eβ∀β≤α⇒f(x)≥αif x∈Ec
α.
17

Again by the construction off, it is clear that∪α∈REα=X and∪α∈REc
α=X. From this, given∀x∈X,
we know that∃α,β∈R such that x∈Eαand x∈Eβand most importantly since α,β∈R:
−∞<α≤f(x)≤β <∞
And hence f(x)⁄=±∞irregardless of x. It’ll now be a lot easier to conclude measurability since we no
longer have to worry about the possibility that f(x) =±∞.
Let us now taker∈Q, and note that by ﬁrst set of inequalities established, if x∈X, thenf(x)<r ⇐⇒
∃q∈R s.t. x∈Eq. Equivalently: f−1((−∞,r )) =∪q<rEα. By the density of Q, we can actually restrict
that q,r ∈Q. We therefore have:
f−1((−∞,r )) =

q<r
Eq, where q,r ∈Q
And sinceEq∈M∀q, and since{q∈Q|q <r}is a countable set, we naturally havef−1((−∞,r ))∈M.
Furthermore, by the inequalities established, we also have:
f−1([r,∞)) =

q<r
Ec
r∈M
And since we showed this to be true ∀r∈Q, by Exercise 4.4, f is measurable.
2.6 Folland 2.8
Prove the following Proposition:
Proposition. 2.6:
If f : R→R is monotone, then f is Borel measurable.
Proof. We ﬁrst state our strategy: If we can show that ∀a∈R, f−1([am∞)) is an interval, then f must
be Borel measurable., let us note that as trivial corollary of (Folland) Proposition 2.3, f measurable
⇐⇒ −f measurable. Thus, without loss of generality, assume f is monotone increasing. Suppose now
that a∈R, x∈f−1([a,∞), and y∈[x,∞). Therefore, since f is monotone increasing:
a≤f(x)≤f(y)⇒y∈f−1([a,∞))
Since this is true ∀x,y ∈[a,∞), it actually proves that f−1([a,∞)) is indeed an interval, and therefore
Borel measurable, and hence f is Borel measurable since this is true ∀a∈R.
2.7 Folland 2.9
Prove the following Proposition:
18

Proposition. 2.7:
Let f : [0, 1]→[0, 1] be the Cantor Function (Folland Section 1.5), and let g(x) =f(x) +x.
a) g is a bijection from [0, 1] to [0, 2], and h =g−1 is continuous from [0, 2] to [0, 1].
b) If C is the Cantor set, m(g(C)) = 1.
c) By (Folland) Exercise 29 of Chapter 1, g(C) contains a Lebesgue non-measurable set A. Let
B =g−1(A). Then B is Lebesgue measurable but not Borel.
d) There exist a Lebesgue measurable function F and a continuous function G on R such that
F◦G is not Lebesgue measurable.
Proof.
a) We ﬁrst recall (from Folland) that the Cantor Function, f(x) is monotone increasing, and naturally
h(x) = x is a strictly increasing function, and hence g(x) = f(x) +x is also strictly increasing
and therefore injective. Next, to show surjectivity, note that g is a continuous function, and
g(0) = f(0) + 0 = 0, and g(1) = f(1) + 1 = 2; hence, by the intermediate value theorem, g is
surjective.
We now have all the necessary components to conclude that g is a bijection, and since g is a
continuous bijective function, and [0 , 1] is compact, g’s inverse,g−1, is continuous from [0 , 2] to
[0, 1].
b) Firstly, by g’s surjectivity, andC being measurable, we see that:
g([0, 1]\C)⊔g(C) =g([0, 1]\Cc)⊔g(C) = [0, 2] ⇒m(g(C)) +m(g([0, 1]\C)) = 2
Next, sinceC is a closed set⇒[0, 1]\C is an open set. Therefore, since all open subsets of [0, 1] may
be written as a countable union of disjoint open sets, let us write [0 , 1]\C =⊔∞
1 Oj, Oj = (aj,bj).
Now, sincef is by construction constant on [0, 1]\C, and recalling that m(C) = 0⇒m([0, 1]\C) =
1⇒m(⊔∞
1 Oj) = 1, we see:
m(g([0, 1]\C)) =m
(
g
(∞⨆
j=1
Oj
{{
=
∞∑
j=1
m(g(Oj))
=
∞∑
j=1
(
m(f(bj)−f(aj)) +m(bj−aj)
{
=
∞∑
j=1
m(Oj) since f(bj) =f(aj)∀j∈N
=m
(∞⨆
j=1
Oj
{
= 1
And hence m(g(C)) = 1 by the the ﬁrst part of this proof.
c) To show Lebesgue measurability, naturallyB⊂C, and sinceC is measurable with measurem(C) =
0, it implies m(B)≤m(C) = 0, and hence Lebesgue measurable since null sets are measurable.
19

For the sake of contradiction, supposeB =g−1(A) is Borel measurable. In part a), we showed that
g−1 is continuous and bijective; therefore g(B) =g(g−1(A)) =A. However, by the continuity of g,
if g−1(A) was Borel, so too would g(g−1(A)) = A, hence a contradiction since A is not Lebesgue
measurable; therefore, B cannot be Borel measurable.
d) Let F = χB; I.e., F (x) =
{
1 if x∈B
0 if x∈Bc , and also set G = g−1. Naturally G is Lebesgue mea-
surable since it is continuous, we now wish to prove that so too is F . This can be seen by notic-
ing F−1((a,∞)) = ⌀ or B or R, but all these possibilities are Lebesgue measurable, hence F is
Lebesgue measurable. We can now look at the following reasoning:
(F◦G)−1((1/2,∞)) =G−1◦F−1([1/2,∞)) ={x∈[0, 2]|χB(g−1(x))∈[1/2,∞)}
={x∈[0, 2]|g−1(x)∈B}
=G−1(B) =g(g−1(A)) =A
Now since A is not Lebesgue measurable, F◦G also will not be Lebesgue measurable.
2.8 Folland 2.10
Prove the following Proposition:
Proposition. 2.8:
The following implications are valid ⇐⇒the measure µis complete:
a) If f is measurable and f =g µ-a.e., then g is measurable.
b) If fn is measurable for n∈N and fn→f µ-a.e., then f is measurable.
Proof.
a) For the forward direction, suppose a) holds. Then let N∈M be a measurable set s.t. µ(N) = 0,
and N1⊂N. If we deﬁne f :≡0 and χN1 := 1 if x∈N1, and 0 otherwise, then trivially f is
measurable and f = χN1 µ-a.e., so by our assumptions g is measurable. Now, by noting that
χ−1
N1({1}) = N1∈M by g’s measurability, and since this is true ∀N1⊂N, we have arrived at the
deﬁnition of µbeing complete.
For the backward direction, suppose µis complete, and let f be measurable and f = g µ-a.e.
Explicitly, let N∈M be the measurable set s.t. µ(N) = 0 and f(x) =g(x)∀x∈Nc. Then if A is
measurable, we have:
g−1(A) =

g−1(A)\N

⊔

g−1(A)\Nc
=

g−1(A)\N

⊔

f−1(A)\N

Looking at the right hand side, we can see g−1(A)\N⊂N is measurable by the deﬁnition of µ
being a complete measure sinceµ(N) = 0. Furthermore,f−1(A)\N⊂f−1(A) sincef is measurable.
With these two facts, we may therefore conclude that g is indeed measurable.
b) For the forward direction, suppose b) holds. Then let N∈M be a measurable set s.t. µ(N) = 0,
and N1⊂N. If we let fn = 0 and χN1 as before, then like in the forward direction of a), we have
fn→χN1 µ-a.e., so χN1 is measurable. Therefore, χ−1
N1({1})∈M, and since this is true ∀N1⊂N,
we have arrived at the deﬁnition of µbeing complete.
20

For the backward direction, suppose µis complete, and fn is measurable ∀n∈N, and fn→f
µ-a.e. By (Folland) Proposition 2.7, g3(x) = lim supj→∞fj(x) is measurable since fn is measurable
∀n∈N. Furthermore, since fn →f µ-a.e., we have g3 = f µ-a.e., and thus by the backward
direction of part a) above, f is measurable.
2.9 Folland 2.12
Prove the following Proposition:
Proposition. 2.9:
If f∈L+ and

f <∞, then{x|f(x) =∞}is a null set and {x|f(x)> 0}is σ-ﬁnite.
Proof. Let E :={x|f(x) =∞}, F :={x|f(x) > 0}, Fn :={x|f(x) > 1/n}, and f satisfy f∈L+
and

f <∞. Let us now deﬁne the two sets of functions {φn}∞
1 and{ϕn}∞
1 , where φn = nχE and
ϕn =χFn/n.
To proveE is a null set, we make the observation that since f(x) =∞∀x∈E, and χn(x)<∞∀n∈N,
we have:
0≤φn(x)≤f(x)∀x∈X ⇒nµ(E) =
∫
φn dµ≤
∫
f dµ
⇒µ(E)≤1
n
∫
f dµ
Thus, since

f δµ<∞, letting n→∞, we see that µ(E) = 0; I.e., E is a null set.
By the construction of{Fn}∞
1 , we have∪∞
1 Fn, so to conclude that F isσ-ﬁnite, we simply need to show
that µ(Fn)<∞∀n∈N. This is easily ascertained since f(x)> 1/n∀x∈Fn, and

f <∞, we have:
0≤ϕn(x)≤f(x)∀x∈Fn ⇒ 1
nµ(Fn) =
∫
ϕn dµ≤
∫
f dµ
⇒µ(Fn)≤n
∫
f dµ<∞
And hence µ(Fn)<∞∀n∈N, which implies F is σ-ﬁnite.
2.10 Folland 2.13
Prove the following Proposition:
Proposition. 2.10:
Suppose{fn}∞
1 ⊂L+, fn →f pointwise, and

f = lim

fn <∞. Then

Ef = lim

Efn
∀E∈M. However, this need not be true if

f = limfn =∞.
Proof. Let E∈M and

f <∞, and so we deﬁne χE s.t.

Ef =

χEf, and so we have:
∫
E
f =
∫
χEf≤
∫
f = lim
∫
fn <∞
21

Furthermore, by (Folland) Theorem 2.15, we have:
∫
f =
∫
(χEf +χEcf) =
∫
χEf +
∫
χEcf
And similarly for substituting fn for f above. Now, since fn→f⇒χFfn→χFf ∀F ∈M, we may
apply Fatou’s Lemma as follows:
∫
E
f =
∫
lim inf
n→∞
χEfn≤lim inf
n→∞
∫
E
fn
∗
= lim inf
n→∞
(∫
fn−
∫
Ec
fn
{
∗∗
=
∫
f−lim sup
n→∞
∫
Ec
fn
Where we have
∗
= since

Ef =

χEf +

χEcf, and
∗∗
= since lim inf

fn = lim

fn =

f and
lim inf−

g =−lim sup

g. However, since all terms above are ﬁnite, we may gain by apply Fatou’s
Lemma (and in noticing the similarity to the steps made above) to see that:
lim sup
n→∞
∫
Ec
fn = lim sup
n→∞
(∫
fn−
∫
E
fn
{
=
∫
f−lim inf
n→∞
∫
E
fn≤
∫
f−
∫
E
f
And thus by substituting this in, we have:
∫
E
f≤lim inf
n→∞
∫
E
fn≤lim sup
n→∞
∫
E
fn≤
∫
E
f
And therefore all the inequalities in the equation(s) above are actually equalities, and so we have:
lim inf
n→∞
∫
E
fn = lim sup
n→∞
∫
E
fn = lim
n→∞
∫
E
f =
∫
E
f
We now turn our attention showing the above result need not hold if

f = lim

f =∞by means of a
counter-example. Let E = (0, 1], f =χ[2,∞), and fn =χ[2,∞) +nχ(0,1/n]. Then fn→f p.w., and:
∫
(0,1]
fn =nµ((0, 1/n]) = 1∀n∈N ⇒ lim
n→∞
∫
(0,1]
fn = 1
However,

(0,1]f = 0, thus

Ef = lim

Efn need not be true if lim

f =

f =∞.
2.11 Folland 2.14
Prove the following Proposition:
Proposition. 2.11:
If f ∈L+, let λ(E) =

Ef dµfor E∈M. Then λis a measure on M, and for any g∈L+,
g dλ=

fg dµ. (First Suppose that g is simple.)
Proof. Trivially, sincef∈L+, we have that λ(E)≥0∀E∈M. Moreover, one can see that λ(⌀) = 0:
λ(⌀) =
∫
⌀
f dµ=
∫
χ⌀f dµ= 0
22

To fully show that λis a measure on M, we need that for any disjoint sequence of sets, {Ej}∞
1 ∈M,
λ(⊔∞
1 Ej) =∑∞
1 λ(Ej). We can deduce this fact from the following:
λ
(∞⨆
j=1
Ej
{
=
∫
⊔∞
1 Ej
f dµ=
∫
χ(⊔∞
1 Ej )f dµ
=
∫( ∞∑
j=1
χEj
{
f dµ
∗
=
∞∑
j=1
∫
χEjf dµ
∗
= by (Folland) Theorem 2.15
=
∞∑
j=1
∫
Ej
f dµ=
∞∑
j=1
λ(Ej)
We have thus shown all the necessary conditions for λto be a measure do indeed hold.
Next, let g∈L+, and assume that g is simple⇒g =∑n
1ajχEj. Therefore:
∫
g dλ=
n∑
j=1
ajλ(Ej) =
n∑
j=1
∫
Ej
f dµ=
n∑
j=1
∫
χEjf dµ
∗
=
∫( n∑
j=1
ajχEj
{
f dµ=
∫
gf dµ
∗
= by (Folland) Theorem 2.15
And so we get the required result when g is simple. However, by (Folland) Theorem 2.10, we know that
since f∈L+,∃{φn}∞
1 s.t. 0 ≤φ1≤φ2≤···≤f, φn→f p.w., and φn→f uniformly on any set on
which f is bounded. Therefore, we can apply the Monotone Convergence Theorem (used if
⋆
= denoted)
as follows:
∫
g dλ
⋆
= lim
n→∞
∫
φn dλ
∗
= lim
n→∞
∫
φnf dµ
⋆
=
∫
gf dµ
∗
= since φn simple∀n∈N
2.12 Folland 2.16
Prove the following Proposition:
Proposition. 2.12:
If f∈L+ and

f <∞,∀ϵ>0∃E∈M s.t. µ(E)<∞and

Ef >
(
f
{
−ϵ
Proof. Firstly, By (Folland) Exercise 2.12 (proved above - 5.2), we know that F :={x|f(x) > 0}is
σ-ﬁnite. In the proof of (Folland) 2.12, we showed that Fn :={x|f(x)> 1/n}has the nice properties
of µ(Fn) < ∞and∪∞
1 Fn = F . Furthermore, it is also apparent from the construction of Fn that
Fn⊂Fn+1∀n∈N - I.e.,{Fn}∞
1 is monotone increasing, and so {χFn}∞
1 will be an increasing sequence
in L+ s.t. χFn≤χFn+1∀n∈N, and limn→∞χFn =χF .
Since{χFn}∞
1 and χF satisfy necessary conditions for the Monotone Convergence Theorem, and in
noticing

f =

χFf, we may apply it as follows:
∫
f =
∫
χFf = lim
n→∞
∫
χFnf =
∫
Fn
f
23

We also note that, since χFn⊂χF∀n∈N, we have:
∫
f =
∫
χFf≤
∫
χFnf =
∫
Fn
f ∀n∈N
Therefore,

Fn
is an increasing sequence with the limit of

f. So by this convergence, we have ∀ϵ >0,
∃N∈N such that: ∫
FN
f >
(∫
f
{
−ϵ
I.e., we have proven the existence of an FN =E∈M which satisﬁes

FN
f >
(
f
{
−ϵ.
2.13 Folland 2.17
Prove the following Proposition:
Proposition. 2.13:
Assume Fatou’s lemma and deduce the monotone convergence theorem from it.
Proof. Let{fn}∞
1 be a sequence in L+ s.t. fj≤fj+1∀j∈N, and f = limn→∞fn. If we’re assuming
Fatou’s Lemma, then: ∫
f =
∫
lim inf
n→∞
fn≤lim inf
n→∞
∫
fn
However, since{fn}∞
1 is monotone increasing with the limit of f, we have fn≤f ∀n∈N⇒

fn≤
f∀n∈N. And hence taking the lim sup on both sides, we get:
lim sup
n→∞
∫
fn≤lim sup
n→∞
∫
f =
∫
f
Therefore, in combining these two inequalities, we see:
lim sup
n→∞
∫
fn≤
∫
f≤lim inf
n→∞
∫
fn
Which can be true ⇐⇒all the inequalities above are actually equalities, hence we have:
lim
n→∞
∫
fn = lim sup
n→∞
∫
fn = lim inf
n→∞
∫
fn =
∫
f
2.14 Diﬀerentiable functions are Borel Measurable
Exercise. 2.1:
Let f : R→R be a diﬀerentiable function, show that its derivative f′is Borel Measurable.
Proof. Firstly, we note that by (Folland) Corollary 2.2, since f∈C 1(R)⇒f∈C(R), we have that f is
Borel measurable.
24

Next, we prove thatgn :=f(x + 1/n) is Borel measurable. This is actually quite easy since hn =x + 1/n
is naturally Borel measurable, and hence f◦hn =gn is Borel measurable since both f and gn are Borel
measurable.
Next, since f∈C 1(R), we know that limh→0
f (x+h)−f (x)
h =f′(x), f′(x)∈R. Therefore, we can also say
that limn→∞n(f(x + 1/n)−f(x)) = f′(x)∀x∈R. Since we already showed f(x + 1/n) and f(x) are
Borel Measurable, by (Folland) Proposition 2.6, f′
n :=n(f(x + 1/n)−f(x)) is Borel measurable∀n∈N.
Finally, by (Folland) Proposition 2.7, we can conclude that f′(x) = limn→∞f′
n(x) is Borel measurable
since f∈C 1(R), f′
n→f, and{fn}∞
1 is a sequence of Borel measurable functions.
2.15 Folland 2.20
Prove the following Proposition:
Proposition. 2.14:
(A generalized Dominated Convergence Theorem) If fn,gn,f,g ∈L1, fn→f and gn→g a.e.,
fn≤gn and

gn→

g, then

fn→

f. (Rework the proof of the dominated convergence
theorem).
Proof. By the same reasoning as in Folland, WLOG we may assume fn and f are real-valued, and that
gn +fn≥0 a.e., and gn−fn≥0 a.e. Now, we apply (Folland) Corollary (of Fatou’s Lemma) 2.19 to
both gn +fn and gn−fn as follows (we can do so due to the convergent and L1 assumptions):
∫
(g +f) =
∫
lim(gn +fn)≤lim inf
∫
(gn +fn) =
∫
g + lim inf
∫
fn
∫
(g−f) =
∫
lim(gn−fn)≤lim inf
∫
(gn−fn) =
∫
g−lim sup
∫
fn
And so:
lim sup
∫
fn−
∫
g≤−
∫
g +
∫
f and
∫
g +
∫
f≤
∫
g + lim inf
∫
fn
And by combining these inequalities, we see that:
lim sup
∫
fn≤
∫
f≤lim inf
∫
fn
And since f,fn∈L1, we know that the above inequalities imply equalities, everywhere, I.e., lim

fn
exists and

fn→

f.
2.16 Folland 2.21
Prove the following Proposition:
Proposition. 2.15:
Suppose fn,f ∈L1 and fn→f a.e. Then

|fn−f|→0 ⇐⇒

|fn|→

|f|, (Use (Folland)
Exercise 20).
25

Proof. For the forward direction, assume

|fn−f|→0, then since:
⏐⏐⏐⏐
∫
|fn|−
∫
|f|
⏐⏐⏐⏐=
⏐⏐⏐⏐
∫(
|fn|−|f|
{⏐⏐⏐⏐≤
∫⏐⏐⏐
(
|fn|−|f|
{⏐⏐⏐≤
∫
|fn−f|, since|fn|−|f|≤|fn−f|
we know that the right hand side→0 asn→∞, and since the above holds∀n∈N (and sincefn,f ∈L1),⏐⏐
|fn|−

|f|
⏐⏐→0⇒

|fn|→

|f|.
For the backward direction, assume

|fn|→

|f|. If we let gn :=|fn|+|f|, then naturally|fn−f|≤gn,
and since fn,f ∈L1, we know that

gn =

(|fn|+|f|) = 2

|f|. We may now invoke the generalized
dominated convergence theorem, (Folland) Exercise 2.20 above, which implies:
lim
∫
|fn−f|=
∫
lim|fn−f|
And since fn→f, we therefore have

|fn−f|→0.
2.17 Folland 2.24
2.18 Folland 2.34
Prove the following Proposition:
Proposition. 2.16:
Suppose|fn|≤g∈L1 and fn→f in measure.
a)

f = lim

fn.
b) fn→f in L1.
Before we begin, we present Folland Exercise 33 as a necessary Lemma for part a):
2.18.1 F olland 2.33
Lemma. 2.1:
If fn≥0 and fn→f in measure, then

f≤lim inf

fn.
Proof.
a) By (Folland) Theorem 2.30, ∃a subsequence{fnk}∞
1 s.t. fnk→h, where f =h a.e. Furthermore,
by (Folland) Proposition 2.11, since f =h a.e., f is measurable. As is standard by this point, we
may assume fn and g are real-valued functions; therefore, g +fn≥0 a.e., and g−fn≥0 a.e.
Moreover, we naturally have g +fn→g +f, g−fn→g−f in measure. We now make use of our
Lemma as follows:
∫
g +
∫
f =
∫
(g +f)≤lim inf
∫
(g +fn) =
∫
g + lim inf
∫
fn
∫
g−
∫
f =
∫
(g−f)≤lim inf
∫
(g−fn) =
∫
g−lim sup
∫
fn
And so in combining these inequalities, we have:
lim sup
∫
fn≤
∫
f≤lim inf
∫
fn
26

Which we recognize as in previous exercises to be true ⇐⇒all the above inequalities are actually
equalities; hence:

f = lim

fn.
b) From (Folland) Proposition 2.29, we know that since fn→f in L1, fn→f in measure as well.
Thus, since:
µ
({
x∈X
⏐⏐||fn(x)−f(x)|−0|≥ϵ
}{
=µ
({
x∈X
⏐⏐|fn(x)−f(x)|≥ϵ
}{
→0 as n→∞
We also have that|fn−f|→0 in measure. Furthermore, since: |fn−f|≤|fn|+|f|≤2g∈L1, we
may apply Part a) to see that:
0 =
∫
0 dµ= lim
∫
|fn−f|dµ
Hence fn→f in L1.
2.19 Folland 2.39
Prove the following Proposition:
Proposition. 2.17:
If fn→f almost uniformly, then fn→f a.e. and in measure.
Proof. We ﬁrst recall thefn→f almost uniformly means that∃{En}∞
1 ⊂M s.t. µ(Ec
n)< 1
n andfn→f
uniformly on En. If we deﬁne E :=∪∞
1 En, then µ(Ec)≤lim infµ(Ec
n) = 0; hence, fn→f a.e.
Now to show fn→f in measure, we proceed as follows. ∀ϵ,δ >0, since fn→f almost uniformly,
∃E∈M and an N∈N s.t. ∀n≥N,|fn(x)−f(x)|< ϵ∀x∈E and µ(Fc)< δ. An immediate result of
this set up is therefore:
lim inf
n→∞
µ
({
x∈X||fn(x)−f(x)|≥ϵ
}{
≤µ(Fc)<δ
And since our result works ∀δ >0, letting δ→0 proves fn→f in measure.
2.20 Folland 2.42
Prove the following Proposition:
Proposition. 2.18:
Let µbe a counting measure on N. Then fn→f in measure ⇐⇒fn→f uniformly.
Proof. For the forward direction, suppose fn→f in measure (µa counting measure on N). Then∀ϵ>0
∃N∈N s.t.∀n≥N:
µ
({
x∈N
⏐⏐|fn(x)−f(x)|≥ϵ
}{
< 1
2 ⇒
{
x∈N
⏐⏐|fn(x)−f(x)|≥ϵ
}
= ⌀
I.e.,|fn(x)−f(x)|<ϵ∀x∈N (and n≥N), which is by deﬁnition uniform convergence.
27

For the converse, suppose fn→f uniformly (again µa counting measure on N). Then ∀ϵ>0,∃N∈N
s.t.∀n≥N:
|fn(x)−f(x)|<ϵ∀x∈N ⇒µ
({
x∈N
⏐⏐|fn(x)−f(x)|≥ϵ
}{
=µ(⌀) = 0
For which the latter equality vacuously satisﬁes our deﬁnition of convergence in measure.
2.21 Folland 2.44: Lusin’s Theorem
Prove the following Theorem:
Theorem. 2.1: Lusin’s Theorem
If f : [a.b]→C is Lebesgue measurable and ϵ >0, there is a compact set E⊂[a,b ] such that
µ(Ec)<ϵand f|E is continuous. (Use Egoroﬀ’s Theorem and (Folland) Theorem 2.26.)
Proof. Following the hint, by (Folland) Theorem 2.26,∃{fn}∞
1 s.t. fn : [a,b ]→C andfn→f a.e. Also,
by Egoroﬀ’s Theorem,∃F⊂[a,b ] s.t. µ(Fc)<ϵ/2 and fn→f uniformly on F .
Naturally, sincefn→f uniformly onFc,f|F will be continuous. We now make use of (Folland) Theorem
1.18 which states that∀F∈Mµ:
µ(F ) = sup{µ(K)|Kcpt⊂F}
And so by deﬁnition of sup, ∃Ecpt⊂F s.t. µ(F\E)<ϵ/2. We thus have:
µ(Ec) =µ(Fc) +µ(F\E)< ϵ
2 + ϵ
2 =ϵ
And since E⊂F , we know that f|E is also continuous, thereby proving the Theorem.
2.22 Folland 2.46
Prove the following Proposition:
Proposition. 2.19:
Let X = Y = [0, 1], M = N = B[0,1],µ= Lebesgue measure, and ν= counting measure. If
D ={(x,x )|x∈[0, 1]}is the diagonal inX×Y , then

χDdµdν,

χDdνdµ, and

χDd(µ×ν)
are all unequal. (To compute

χDd(µ×ν) =µ×ν(D), go back to the deﬁnition of µ×ν.)
Proof. We begin by making the following two observations: ∀x ∈[0, 1],

χDdν(y) =

{x}dν(y) =
ν({x}) = 1 and ∀y∈[0, 1],

χDdµ(x) =

{y}dν(x) = µ({y}) = 0. Therefore, we’ll now be able to
compute

χDdµdνand

χDdνdµas follows:
∫ ∫
χDdµdν=
∫(∫
χD(x,y )dµ(x)
{
dν(y) =
∫
0dν(y) = 0
∫ ∫
χDdνdµ=
∫(∫
χD(x,y )dν(y)
{
dµ(x) =
∫
[0,1]
dµ(x) = 1
We now claim that

χDd(µ×ν) =∞. To see this, suppose{An×Bn}∞
1 s.t. An,Bn⊂[0, 1] (measurable
subsets) s.t. D ⊂ ∪∞
1 (An×Bn). Therefore, [0 , 1]⊂ ∪∞
1 (An×Bn). Because of this, ∃N ∈N s.t.
µ∗(AN×BN) > 0, and explicitly µ(AN) > 0, and ν(BN) = ∞. Therefore, ∑∞
1 µ(An)ν(Bn) = ∞⇒
χDd(µ×ν) =∞.
28

2.23 Folland 2.48
Prove the following Proposition:
Proposition. 2.20:
Let X =Y = N, M = N = P(N),µ=ν= counting measure. Deﬁne:
f(m,n ) =

}

1 if m =n
−1 if m =n + 1
0 otherwise
Then

|f|d(µ×ν) =∞, and

f dµdνand

f dνdµexist and are unequal.
Proof. We ﬁrst claim that µ×µis also a counting measure. We may actually note that fundamentally,
a counting measure τon N×N will satisfy τ(A×B) =|A||B|=µ(A)ν(B). Therefore, since rectangles
generate the product σ-algebra, the σ-ﬁnitness of τimplies µ×ν=τ.
We now proceed to computing each of the quantities of interest. For the ﬁrst, if we letE :=∪∞
1{{(n,n )}∪
{(n,n + 1)}}, then clearly|E|=∞, and|f|=χE. Therefore:
∫
|f|d(µ×ν) =|E|=∞
Furthermore, the other two calculations are nearly immediate:
∫ ∫
fdµdν=
∫ ∫
f(m,n )dµ(m)dν(n) =
∑
n
∑
m
f(m,n ) =
∑
n
0 = 0
∫ ∫
fdµdν=
∫ ∫
f(m,n )dν(n)dν(m) =
∑
m
∑
n
f(m,n ) =
∑
m
χ{m=1}= 1
2.24 Folland 2.49
Prove the following Proposition:
Proposition. 2.21:
Prove (Folland) Theorem 2.38 by using Theorem 2.37 and Proposition 2.12 together with the
following lemmas:
a) If E∈M×N and µ×ν(E) = 0, then ν(Ex) =µ(Ey) = 0 for a.e. x and y.
b) If f is L-measurable and f = 0 λ-a.e., then fx and fy are integrable for a.e. x and y, and
fxdν=

fydµ= 0 for a.e. x and y. (Here the completeness of µand νis needed.)
Proof.
a) Immediately by (Folland) Theorem 2.36, since ( X, M,µ) and (Y, N,ν) are σ-ﬁnite measure spaces,
we have:
0 =µ×ν(E) =
∫
ν(Ex)dµ(x) =
∫
µ(Ey)dν(y)
29

b) Let us deﬁne F :={(x,y )∈M×N|f(x,y )⁄= 0}. Thus, ∃E∈M⊗N where µ×ν(E) = 0 and
F ⊂E. From a), µ(Ex) = ν(Ey) = 0 for x,y a.e. Furthermore, by the fact that Fx⊂Ex and
Fy⊂Ey, by linearity of measures we have µ(Fx) =ν(Fy) = 0 as well. We may now conclude thus
that: ∫
|fx|dν=
∫
χFx|fx|dν= 0 =
∫
χF y|fy|dµ=
∫
|fy|dµ= 0 for a.e. x and y
For which the intended result trivially follows.
Please see the next (attached) page for our proof of (Folland) Theorem 2.38.
3 Chapter 3
3.1 Folland 3.2
Prove the following Proposition:
Proposition. 3.1:
a) If νis a signed measure, E is ν-null ⇐⇒ |ν|(E) = 0.
b) If νane µare signed measures, ν⊥µ⇐⇒ |ν|⊥µ⇐⇒ν+⊥µand ν−⊥µ.
Proof.
a) For the forward direction, suppose νis a signed measure and that E isν-null. Suppose for the sake
of contradiction that|ν|(E) =ν+(E)+ν−(E)> 0, whereν=ν+−ν−is the Jordon Decomposition
of ν. By the Hahn Decomposition Theorem, ∃P,N s.t. ν(X) = ν(P∪N) = ν+(P )−ν−(N) and
ν+(N) = 0 =ν−(P ).
We thus can thus make the following observations:
|ν|(E) =ν+(E) +ν−(E) = 2ν+(E)> 0 since ν(E) = 0⇒ν+(E) =ν−(E)
ν+(E\P ) =ν+(E\N) +ν+(E\P ) =ν+(E\X) =ν+(E)> 0 since 2 ν+(E)> 0
ν−(E\P )≤ν−(P ) = 0
And so:
ν(E\P ) =ν+(E\P ) +ν−(E\P ) =ν+(E\P )> 0
However, since E\P⊂E, and we are assuming that ν(E) = 0, we arrive at a contradiction with
the last inequality. Thus, actually if E is ν-null,|ν|(E) = 0.
For the converse, suppose|ν|(E) = 0, hence|ν|(E′) = 0∀E′⊂E (E′measurable). Since|ν|(E′) =
ν+(E′) +ν−(E′) = 0 ⇐⇒ν+(E′) = 0 = ν−(E′), we thus trivially satisfy ν(E′) = ν+(E′)−
ν−(E′) = 0 since both are already zero.
b) Let us recall that, explicitly, if∃E,F ∈M s.t. E\F = ⌀,E⊔F =X andµ(E′) = 0 =ν(F′)∀E′⊂
E,F′⊂F (E′,F′measurable), we denote this property as ν⊥µ.
We begin by showing ν⊥µ⇒|ν|⊥µ. To see this, since F is ν-null, by Part a), we know that
|ν|(F ) = 0. Since |ν|is a positive (regular) measure, by monotonicity we have that |ν|is F -null.
Thus, by deﬁnition,|ν|⊥µ.
30

We now show|ν|⊥µ⇒ν+⊥µand ν−⊥µ. Since ν= ν+ +ν−, we have ν+≤νand ν−≤ν,
and so ν+(F′) =ν−(F′) = 0, I.e., F is both ν+-null and ν−-null; hence, ν+⊥µand ν−⊥µ.
We may now complete Part b) by showing [ν+⊥µandν−⊥µ]⇒ν⊥µ. Let us make explicit the
properties associated with ν+⊥µand ν−⊥µby replacing the roles of E,F (from the beginning
of this proof) with A1,A 2 for ν+⊥µand B1,B 2 for ν−⊥µ. We ﬁrst note that since A1,B 1
are both µ-null, so too is A1∪B1. This is true since by looking at the following representation:
A1∪B1≡A1⊔(B1\A1), and in noting B1\A1⊂B1,∀E′⊂A1∪B1,∃A′
1⊂A1,B′
1⊂B1 s.t.
E′=B′
1⊔A1 and both B′
1 andA′
1 areµ-null. Furthermore, since A1∪A2 =X =B1∪B2, we have
X\(A1∪B1) =A2\B2, which is both ν+-null and ν−-null since A2\B2⊂A2 andA2\B2⊂B2.
Thus, by setting E =A1∪B1, and F =A2\B2, we see that indeed ν⊥µ.
3.2 Folland 3.7
Prove the following Proposition:
Proposition. 3.2:
Suppose that νis a signed measure on (X, M) and E∈M.
a) ν+(E) = sup
{
ν(F )
⏐⏐E∈M,F ⊂E
}
and ν−(E) =−inf
{
ν(F )
⏐⏐F∈M,F ⊂E
}
.
b) |ν|(E) = sup
{∑n
1|ν(Ej)|
⏐⏐n∈N,E 1,...,En are disjoint, and ⊔n
1 Ej =E
}
.
Proof.
a) For the ﬁrst equality, ∀F⊂E we have:
ν(F ) =ν+(F )−ν−(F )≤ν+(F )≤ν+(E)
And so ν+(E) ≥sup{ν(F )|E ∈M,F ⊂E}. To see the reverse inequality, if P,N are our
Hahn Decomposition of ν, we naturally have ν+(E) = ν(E\P ), and since E\P⊂E, ν+(E)≤
sup{ν(F )|E∈M,F ⊂E}, and so:
ν+(E) = sup
{
ν(F )
⏐⏐E∈M,F ⊂E
}
For the second inequality, this follows very similarly. Explicitly, ∀F⊂E, we have:
−ν(F ) =ν−(F )−ν+(F )≤ν−(F )≤ν−(E)
And so ν−(F )≥sup{−ν(F )|F ∈M,F ⊂E}=−inf{ν(F )|F ∈M,F ⊂E}. For the reverse
inequality, since ν−(E) =−ν(E\N), and since E\N⊂E, ν−(E)≤sup{−ν(F )|F∈M,F ⊂
E}=−inf{ν(F )|F∈M,F ⊂E}. Combining our two inequalities, we see:
ν−(E) =−inf
{
ν(F )
⏐⏐F∈M,F ⊂E
}
b) Firstly, if P,N are again the Hahn Decomposition of ν, then E = (E\N)⊔(E\P ), and so:
|ν|(E) =ν+(E) +ν−(E) =ν+(E\P ) +ν−(E\N)
=ν+(E\P ) +ν−(E\N) +ν+(E\N) +ν−(E\P )/∏ce⨆⋃ipuplef⋃/∏ce⨆⋃ipdown∏ig⨆⋃/∏ce⨆⋃ipdownlef⋃/∏ce⨆⋃ipup∏ig⨆⋃
=0
=|ν(E\P )|+|ν(E\N)|
31

And so:
|ν|(E)≤sup
{ n∑
1
|ν(Ej)|
⏐⏐⏐n∈N,E 1,...,En are disjoint, and
n⨆
1
Ej =E
}
To see the reverse inequality, we note that∀E =⊔n
1Ej, we have:
n∑
j=1
|ν(Ej)|=
n∑
j=1
|ν+(Ej)−ν−(Ej)|
≤
n∑
j=1
(
ν+(Ej) +ν−(Ej)
{
=
n∑
j=1
|ν|(Ej)
=|ν|
( n⨆
j=1
Ej
{
=|ν|(E)
And so:
|ν|(E)≥sup
{ n∑
1
|ν(Ej)|
⏐⏐⏐n∈N,E 1,...,En are disjoint, and
n⨆
1
Ej =E
}
And hence combining the two inequalities, we have:
|ν|(E) = sup
{ n∑
1
|ν(Ej)|
⏐⏐⏐n∈N,E 1,...,En are disjoint, and
n⨆
1
Ej =E
}
3.3 Folland 3.12
Prove the following Proposition:
Proposition. 3.3:
Forj = 1, 2, let µj,νj be σ-ﬁnite measures on (Xj, Mj) s.t. νj <<µj. Then ν1×ν2 <<µ1×µ2
and:
d(ν1×ν2)
d(µ1×µ2)(x1,x 2) = dν1
dµ1
(x1)dν2
dµ2
(x2)
Proof. Let us begin by deﬁning fj := dνj
dµj
for j = 1, 2. Thus, if A1×A2 is measurable, by the deﬁnition
of product measure and Radon-Nikodym derivative, we have:
ν1×ν2(A1×A2) =ν1(A1)ν2(A2) =
∫
A1
f1dµ1
∫
A2
f2dµ2
=
∫
f1χA1dµ1
∫
f2χA2dµ2
=
∫ ∫
f1f2χA1χA2dµ1dµ2
∗
=
∫ ∫
A1×A2
f1f2d(µ1×µ2)
32

Where we have
∗
= by Tonelli’s Theorem. Therefore, on A1×A2 measurable, (f1f2)(µ1µ2) = ν1ν2; and
thus we also have equality on the algebra of ﬁnite unions of A1×A2’s. Furhermore, by the uniqueness
of the extension from premeasure to measure, ( f1f2)(µ1µ2) = ν1ν2 on M1⊗M2. We thus immediately
have that if ( µ1×µ2)(E) = 0 ⇒(ν1×ν2)(E) = 0, and so ν1×ν2 << µ1×µ1. Finally, since the
Radon-Nikodym derivative is unique, we have:
d(ν1×ν2)
d(µ1×µ2)(x1,x 2) =f1(x1)f2(x2) = dν1
dµ1
(x1)dν2
dµ2
(x2)
3.4 Folland 3.13
Prove the following Proposition:
Proposition. 3.4:
Let X = [0, 1], M = B[0,1], m = Lebesgue measure, and µ= counting measure on M, then:
a) m<<µ but dm⁄=fdµfor any f.
b) µhas no Lebesgue decomposition with respect to m.
Proof.
a) Firstly, if E∈M and µ(E) = 0, then it must be that E = ⌀, and so m(E) = m(⌀) = 0; I.e.,
m << µ. Suppose for the sake of contradiction that dm =fdµ, then∀x∈[0, 1] and E ={x}, we
have:
0 =m(E) =
∫
E
fdµ=
∫
E
dm =m(E) = 0
Thus we must have that f≡0 on [0, 1]. However:
1 =m([0, 1]) =
∫
[0,1]
fdµ=
∫
[0,1]
0dµ= 0
I.e. we’ve reached a contradiction and hence dm⁄=fdµfor any f.
b) Suppose, for the sake of contradiction, that µhas a Lebesgue decomposition w.r.t. m; namely:
µ=λ+ρwhereλ⊥m andρ<<m. Since λ⊥m, by deﬁnition we know that∃E,F s.tX =E⊔F
where E is λ-null and F is m-null (or just m(F ) = 0 since m is a positive measure). Suppose
x∈F , then µ({x}) = 1, but λ({x}) = 0 and m({x}) = 0 ⇒ρ({x}) = 0, which would be a
contradiction unless we have F = ⌀. Thus, since X =E⊔F =E⊔⌀⇒E =X. However, since
m(E) =m([0, 1]) = 1, yet we are requiring E to be m-null, we arrive at a contradiction. Thus, ∄ a
Lebesgue decomposition of µw.r.t. m.
3.5 Folland 3.17
Prove the following Proposition:
Proposition. 3.5:
Let (X, M,µ) be a σ-ﬁnite measure space, N a sub-σ-algebra of M, and ν= µ|N. If f∈L1(µ),
∃g∈L1(ν) (thus g is N-measurable) s.t.

Efdµ=

Egdν∀E∈N; if g′is another such function,
then g =g′ν-a.e. (In Probability Theory, g is call the conditional expectation of f on N.)
33

Proof. Let us begin by deﬁning the measure λs.t. dλ=fdµand its integration is restricted to E∈N;
I.e.,∀E∈N, we have λ(E) =

Efdµ. To easily see that λ<<ν, note that if ν(E) = 0⇒µ(E) = 0⇒
λ(E) =

Eddµ= 0. We thus have shown the necessary conditions for us to invoke The Lebesgue-Radon-
Nikodym theorem. Explicitly, the Radon-Nikodym derivative, g = dλ
dνexists and is ν-integrable where
fdµ=dλ=gdν; I.e.; ∫
E
fdµ=
∫
E
dλ=
∫
E
gdν∀E∈N
Finally, ifg′satisﬁes

Efdµ=

Eg′dν, then naturally dλ=g′dν, and since the Radon-Nikodym deriva-
tive is unique, we must also have g =g′ν-a.e.
3.6 Folland 3.20
Prove the following Proposition:
Proposition. 3.6:
If νis a complex measure on (X, M) and ν(X) =|ν|(X), then ν=|ν|.
Proof. Suppose that d|ν|=fdµas in the deﬁnition of |ν|. Then if E∈M, then we will have:
ν(E) +ν(Ec) =ν(X)
∗
=|ν|(X) =|ν|(E) +|ν|(Ec), where we have
∗
= by assumption
And so:
ν(Ec)−|ν|(Ec) =|ν|(E)−ν(E)
Taking the real part of the LHS, and using (Folland) Proposition 3.13a ( |ν(E)|≤|ν|(E)), we see that:
Re
(
ν(Ec)−|ν|(Ec)
{
≤Re(ν(Ec)−|ν(Ec)|)
=νr(Ec)−|ν(Ec)|
=νr(Ec)−
∑
ν2r (Ec) +ν2
i (Ec)
≤νr(Ec)−
√
ν2r (Ec) = 0
And similarly for the RHS:
Re
(
|ν|(E)−ν(E)
{
≥Re(|ν(E)|−ν(E))
=|ν(E)|−νr(E)
=
∑
ν2r (E) +ν2
i (E)−νr(Ec)
≤
√
ν2r (E)−νr(E) = 0
And so combining the fact that Re(LHS )≤0≤Re(RHS ), but obviously since Re(LHS ) =Re(RHS ),
we must have that:
Re(|ν|(E)−ν(E)) = 0 ⇒ |ν|(E) =νr(E)
But since, again by (Folland) Proposition 3.13a, we have |ν(E)|≤|ν|(E), we see that this must be true
⇐⇒νi(E) = 0, and so:
|ν|(E) =νr(E) =νr(E) +νi(E) =ν(E) ∀E∈M (I.e.,ν=|ν|)
34

3.7 Folland 3.21
Prove the following Proposition:
Proposition. 3.7:
Let νbe a complex measure on (X, M). If E∈M, deﬁne:
µ1(E) = sup
{ n∑
j=1
|ν(Ej)|
⏐⏐n∈N,E 1,...,En disjoint,E =⊔n
j=1Ej
}
µ2(E) = sup
{ ∞∑
j=1
|ν(Ej)|
⏐⏐n∈N,E 1,E 2,... disjoint,E =⊔∞
j=1Ej
}
µ3(E) = sup
{⏐⏐⏐⏐
∫
E
fdν
⏐⏐⏐⏐
⏐⏐|f|≤1
}
Then µ1 =µ2 =µ3 =|ν|. (First show that µ1≤µ2≤µ3. To see that µ3 =|ν|, let f = dν
d|ν|and
apply (Folland) Prop 3.13. To see that µ3≤µ1, approximate f by a simple function.)
Proof. We proceed as in the hint. Trivially, µ1≤µ2 since given E ∈M,
{
{Ej}∞
1 |E =⊔∞
1 Ej
}
⊃{
{Ej}n
1|E =⊔n
1Ej
}
(set Ej = ⌀∀j >n).
To seeµ2≤|ν|≤µ3, let f := dν
d|ν|, and so if E =⊔∞
1 Ej, we have:
∞∑
j=1
|ν(Ej)|

≤
∞∑
j=1
|ν|(Ej) by (Folland) Prop. 3.13a
=

|ν|(E)

=
∫
E
d|ν|
=
∫
E
|f|2d|ν| by (Folland) Prop. 3.13b
=
∫
E
ffd|ν|
=
∫
E
fdν by (Folland) Prop. 3.9a
≤
⏐⏐⏐⏐
∫
E
fdν
⏐⏐⏐⏐∈
{{∫
E
fdν
} ⏐⏐⏐|f|≤1
}
And so µ2≤|ν|≤µ3 by the steps with square brackets around them.
To show now that µ3≤µ1, let D :={z∈C||z|≤1}. Trivially D is compact, and thus ∃{zj}n
1 s.t.
∀ϵ>0: n
1
Bϵ(zj)⊃D
Moreover, by deﬁnition of supremum,∀ϵ>0,∃f s.t.|f|≤1 and:
µ3(E)≤
⏐⏐⏐⏐
∫
E
fdν
⏐⏐⏐⏐+ϵ
If we are assuming |f|≤1, then f−1(D) = X, and so we will have X =∪n
1f−1(Bϵ(zj)) as well. By
deﬁning Bj := f−1(Bϵ(zj)), we now perform the standard “shuﬄe” to make a disjoint sequence {Aj}n
1
35

out of{Bj}n
1 , namely we let A1 =B1, and Aj =Bj\∪j
i=1Bi, so that X =⊔n
1Aj. Now, in following the
hint, we explicitly deﬁne the simple function φ:=∑n
1zjχAj.
Naturally|φ|≤1 and|f(x)−φ(x)|<ϵ. Thus:
µ3(E)≤
⏐⏐⏐⏐
∫
E
fdν
⏐⏐⏐⏐+ϵ≤
⏐⏐⏐⏐
∫
E
fdν
⏐⏐⏐⏐−
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐+
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐+ϵ
≤
⏐⏐⏐⏐
∫
E
fdν−
∫
E
φdν
⏐⏐⏐⏐+
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐+ϵ by the Reverse Triangle Inequality
≤
⏐⏐⏐⏐
∫
E
|f−φ|dν
⏐⏐⏐⏐+
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐+ϵ
≤
∫
E
ϵd|ν|+
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐+ϵ
≤ϵ|ν|(E) +ϵ+
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐
So, by letting ϵ→0, we have µ3(E)≤|

Eφd|ν|. Now, let us deﬁne {Ej}n
1 by Ej = Aj\E so that
E =⊔n
1Ej; thus:
µ3(E)≤
⏐⏐⏐⏐
∫
E
φdν
⏐⏐⏐⏐=
⏐⏐⏐⏐
∫n∑
j=1
zjχAjχEdν
⏐⏐⏐⏐=
⏐⏐⏐⏐
n∑
j=1
zj
∫
Ej
dν
⏐⏐⏐⏐
=
⏐⏐⏐⏐
n∑
j=1
ν(Ej)
⏐⏐⏐⏐≤
n∑
j=1
|zj||ν(Ej)|
≤
n∑
j=1
|ν(Ej)|∈
{
{Ej}n
1
⏐⏐E =⊔n
1Ej
}
And so µ3≤µ1. Thus since we were able to show µ1≤µ2≤|ν|≤µ3≤µ1, every inequality above is
actually an equality and in fact: µ1 =µ2 =µ3 =|ν|.
3.8 Folland 3.24
Prove the following Proposition:
Proposition. 3.8:
If f∈L1
loc and f is continuous at x, then x is in the Lebesgue set of f.
Proof. To show that x is in the Lebesgue set of f, we need to show that:
lim
r↘0
1
m(Br(x))
∫
Br(x)
|f(y)−f(x)|dy = 0
To see this, suppose that ϵ >0. By the deﬁnition of continuity of f at x, we know that ∃δ >0 s.t. if
||x−y||< δ, I.e., y∈Bδ(x), we have|f(x)−f(y)|< ϵ. We therefore yield the following inequality for
0<r<δ:
1
m(Br(x))
∫
Br(x)
|f(y)−f(x)|≤1
m(Br(x))
∫
Br(x)
ϵdy=Ar(ϵ) =ϵ
Thus, since ϵwas arbitrary, we may conclude that our limit is indeed = 0; I.e., x is in the Lebesgue set
of f.
36

3.9 Folland 3.25
Prove the following Proposition:
Proposition. 3.9:
If E is a Borel set in Rn, the density, DE(x), of x is deﬁned as:
DE(x) = lim
r↘0
m(E\Br(x))
m(Br(x))
whenever the limit exists.
a) Show that:
DE(x) =
{
1 for a.e. x∈E
0 for a.e. x∈Ec
b) Find examples of E andx s.t. DE(x) is a given number α∈(0, 1), or such that DE(x) does
not exist.
Proof.
a) Let us begin by deﬁning ν(A) :=m(E\A)∀A∈BRn. Then, by construction we have ν <<mand
dν
dm = χE. Furthermore, since {Br(x)}r>0 vacuously satisﬁes the requirements for a set to shrink
nicely to x∈Rn, we may make use of (Folland) Theorem 3.22. Explicitly, by 3.22, we have:
DE(x) = lim
r↘0
m(E\B(r,x ))
m(B(r,x )) = lim
r↘0
ν(Br(x))
m(Br(x)) =χE for m−almost everyx∈Rn
Which is precisely what we wanted to show.
b) For the ﬁrst example, we are looking for an E and an x s.t. DE(x) = α, where α∈(0, 1).
Suppose we are dealing in BR2 and we set x = (0, 0) and let E = {(x,y )|x = t cos(θ),y =
t sin(θ),t> 0,θ∈(0, 2πα)}. Intuitively, E is the interior of the 2-dimensional, inﬁnitely-extending,
cone whose vertex is the point x, and walls are deﬁned as the positive x-axis and the line starting
at the origin and passing thought the point (cos(2 πα), sin(2πα)) on the unit circle. Therefore,
E\Br(x) will be the interior of the same cone as deﬁned before, but now bounded by the curve
beginning at (r, 0), which traverses c.c.w. along Cr(0) and stops at (r cos(2πα),r sin(2πα)). With
this geometrical understanding, we can now easily recognize that since m(Br(x)) = 2πr2, m(E\
Br(x)) =αm(Br(x)) =α2πr2. Since our results are true ∀r> 0, we have:
DE(x) = lim
r↘0
m(E\B(r,x ))
m(B(r,x )) = lim
r↘0
α2πr2
2πr2 =α
For the second example, we are looking for an E and an x s.t. DE(x) does not exist. Suppose for
this example we turn our thoughts to BR1 (so that Br(x) = (x−r,x +r)). Let us now set x = 0,
and deﬁne E as follows:
E =
∞⨆
n=1
( 1
22n+1, 1
22n
{
=
(1
8, 1
4
{
⊔
( 1
32, 1
16
{
⊔
( 1
128, 1
64
{
⊔···
Our strategy henceforth will be to compose a countable subsequence, rk, s.t. rk↘0 and where
limk→∞
m(E\Brk (x))
m(Br(x)) will be undeﬁned, therefore also rendering DE(x) undeﬁned. To do this, we
37

set rk = 1
2k . Naturally, we have m(Brk(x)) = 2
2k = 1
2k−1 . We now decompose (with a slight abuse
of notation){rk}∞
1 ={r2l}∞
1 +′{r2l+1}∞
1 , I.e. separate rk into two subsequences, one where k is
even, the other when k is odd. For the former ( k is even), we have:
m(E\Brk(x)) =
∑
n≥l
m
( 1
22n+1, 1
22n
{
=
∑
n≥l
1
22n+1 = 1
2k
∞∑
n=0
1
22n+1 =
( 1
2k
{(2
3
{
= 1
3·2k−1
And (quite) similarly for k being odd we have:
m(E\Brk(x)) =
∑
n≥l+1
m
( 1
22n+1, 1
22n
{
=
∑
n≥l+1
1
22n+1 = 1
2k+1
∞∑
n=0
1
22n+1 =
( 1
2k+1
{(2
3
{
= 1
3·2k
And so, in recalling again that m(Brk) = 1
2k−1 we have:
m(E\Brk(x))
m(Brk(x)) =

}

1/(3·2k−1)
1/2k−1 = 1
3 if k = 2l,l∈N
1/(3·2k)
1/2k−1 = 1
6 if k = 2l + 1,l∈N
And so limk→∞
m(E\Brk (x))
Brk (x) is undeﬁned, and therefore so too is DE(x) by our previous reasoning.
3.10 Folland 3.26
Prove the following Proposition:
Proposition. 3.10:
Ifλandµare positive, mutually singular Borel measures on Rn and λ+µis regular, then so are
λand µ.
Proof. If Kcpt⊂BRn, then λ(K),µ(K) < (λ+ν)(K) <∞. Furthermore, suppose that E,F form the
singular decomposition of λ,µ; I.e., Rn =E⊔F and∀F1⊂F,F 1∈BRn, µ(F1) = 0, and similarly for E
w.r.t. λ.
Suppose now that A∈BRn. By deﬁnition of λ+µ’s regularity, we know that:
(λ+µ)(A) = inf
{
(λ+µ)(Uopen)|U⊃E
}
Therefore,∀ϵ= 2−k,k ∈N,∃Uopen s.t. ( λ+µ)(Uk) < (λ+µ)(A) +ϵ. Thus, we may construct a
countable sequence of these such Uk’s, namely{Uk}∞
1 , for which when letting k→∞, we have:
lim
k→∞
(λ+µ)(Uk) = (λ+µ)(A), where ( λ+µ)(Uk)≥(λ+µ)(A)∀k∈N by positivity of measures
By our set up of the singular decomposition of λ,µwe also note that we may express ( λ+µ)(Uk) =
(λ+µ)(Uk\E) + (λ+µ)(Uk\F ) =µ(Uk\E) +λ(Uk\F ), and similarly for A, namely: (λ+µ)(A) =
µ(A\E) +λ(A\F ). Furthermore, since µ,λare positive measures, and by construction Uk⊃A⇒
Uk\E⊃A\E (and similarly Uk\F⊃A\F ), we haveµ(Uk\E)≥µ(A\E) andλ(Uk\F )≥λ(A\F ).
By applying the last result twice, we can reach the following result:
(λ+µ)(Uk)−(λ+µ)(A) =λ(Uk\F ) +µ(Uk\E)−λ(A\F )−µ(A\E)
≥λ(Uk\F )−λ(A\F )
=λ(Uk\F ) +λ(Uk\E)/∏ce⨆⋃ipuplef⋃/∏ce⨆⋃ipdown∏ig⨆⋃/∏ce⨆⋃ipdownlef⋃/∏ce⨆⋃ipup∏ig⨆⋃
=0
−λ(A\F )−λ(A\E)/∏ce⨆⋃ipuplef⋃/∏ce⨆⋃ipdown∏ig⨆⋃/∏ce⨆⋃ipdownlef⋃/∏ce⨆⋃ipup∏ig⨆⋃
=0
=λ(Uk)−λ(A)≥0
38

For which we already showed that the LHS has limit = 0, and thus taking limits on every equation in
the above reasoning shows that lim k→∞λ(Uk) = λ(A). Furthermore, by the exact same steps but in
swappingλ↔µ, we see that limk→∞µ(Uk) =µ(A) as well. Therefore, the same approximation by open
sets from above for the deﬁnition of ( λ+µ)’s regularity also works as an approximation by open sets
from above for all sets A∈BRn for λand µ, hence we have arrived at the deﬁnition of λand µbeing
regular measures.
4 Chapter 5
4.1 Folland 5.1
Prove the following Proposition:
Proposition. 4.1:
If X is a normed vector space over K (= R or C), then addition and scalar multiplication are
continuous from X×X and K×X to X. Moreover, the norm is continuous from X to [0,∞); in
fact,
⏐⏐||x||−||y||
⏐⏐≤||x−y||.
Proof. Let us deﬁne A : X×X→X as the addition map (I.e., deﬁned as A(x,y ) = x +y). The by
construction,A is a linear map from the NVS X×X to the NVS X. We thus will have (for (x,y )∈X×X):
||A(x,y )||=||x +y||≤||x||+||y||≤2 max{||x||,||y||}= 2||(x,y )||
And therefore by (Folland) Proposition 5.2, since the above shows A is bounded, A must also be contin-
uous.
Let now deﬁneM : X×X→X as the scalar multiplication map (I.e., deﬁned as M(α,x) =αx). Suppose
now that ϵ>0 and we choose δ= min{1,ϵ}. Then if (α,x)∈K×X such that||(α,x)||<δ, we have:
max{|α|,||x||}<δ≤ϵ⇒||M(α,x)||=||αx||=|α|||x||<δ2≤δ≤ϵ
And so is continuous at (0, 0), and hence again by (Folland) Proposition 5.2, M is continuous.
Lastly, let again ϵ>0, but now set δ=ϵ. If x,y∈X such that||x−y||<δ, then:
||x||=||x−y +y||≤||x−y||+||y||⇒||x||−||y||≤||x−y||
And similarly for||y||−||x||≤||y−x||=||x−y||. Therefore:
⏐⏐||x||−||y||
⏐⏐≤||x−y||<δ=ϵ
And so||·||is uniformly continuous and therefore continuous from X to [0,∞).
4.2 Folland 5.2
Prove the following Proposition:
Proposition. 4.2:
L(X, Y) is a vector space and the function||·||deﬁned by (Folland, Equation 5.3) is a norm on it.
In particular, the three expressions on the right of (5.3) are always equal.
39

Proof. We begin by deﬁning:
||T||1 := sup
{
||Tx|||||x||= 1
}
||T||2 := sup
{||Tx||
||x|||x⁄= 0
}
||T||3 := sup
{
C|||Tx||≤C||x||∀x∈X
}
As in (Folland) Equation 5.3. We thus begin by showing||·||1 =||·||2 =||·||3. Firstly, ifx∈X,x⁄= 0, then⏐⏐x/||x||
⏐⏐= 1 and soT (x)/||x||=T (x/||x||)≤||·||1. Since this is true∀x∈X, we may take the supremum
and hence||T||2≤||T||1. Next, again if x∈X and||x||= 1, then ||Tx||≤||T||3, and again taking the
supremum implies||T||1≤||T||3. Lastly, again supposing x∈X, we simply have||Tx||≤||T||2, therefore
||T||3≤||T||2. Summarizing we have: ||T||1≤||T||3≤||T||2≤||T||1, and hence all our inequalities
above are actually equalities, and proving the equivalence of the above forms of (5.3).
To prove that||·||does indeed deﬁne a norm, suppose S,T ∈L(X, Y), and x∈X. We thus have:
||(S +T )x||=||Sx +Tx||≤||Sx||+||Tx||≤(||S||+||T||)||x|| ⇒ ||S +T||≤||S||+||T||
If now α∈K(= C or R), then:
||αTx||=|α|||Tx||≤|α||T||||x||⇒||αT||≤|α|||T||
⇒||α−1(αT)||≤|α−1|||αT||⇒|α|||T||≤||αT||
⇒||αT||=|α|||T||
And ﬁnally,||T||= 0 ⇐⇒ ||Tx||= 0∀x∈X and T≡0. Hence we’ve shown all the conditions for ||·||
to be a norm.
4.3 Folland 5.5
Prove the following Proposition:
Proposition. 4.3:
If X is a normed vector space, the closure of any subspace of X is a subspace.
Proof. Let X be a subspace of X and X denote its closure. Firstly, by deﬁnition, 0 ∈X. The other
property that we need to show is that if that if x,y∈X, and a,b∈K, then ax +by∈X as well. Since
x,y∈X, we know that∃{xj}∞
1 ⊂X and{yj}n
1⊂X s.t. xn→x andyn→y with respect to the norm,
||·||on X. So,∀ϵ/2> 0,∃N1,N 2∈N s.t.||xn−x||<ϵ/2 and||yn−y||<ϵ/2∀n≥N1,N 2 respectively.
So,∀n≥N = max(N1,N 2), we have:
⏐⏐⏐⏐(axn +byn)−(ax +by)
⏐⏐⏐⏐≤||axn−ax||+||byn−by||=|a|||xn−x||+|b|||yn−y||< 2
(ϵ
2
{
=ϵ
And so since axn +byn→ax +by, and axn +byn∈X it implies ax +by∈X by the deﬁnition of X.
Therefore, X is indeed a subspace of X.
4.4 Folland 5.6
Prove the following Proposition:
40

Proposition. 4.4:
Suppose that X is a ﬁnite-dimensional vector space. Let e1,...,en be a basis for X and deﬁne
||∑n
1ajej||1 =∑n
1|aj|.
a) ||·||1 is a norm on X.
b) The map (a1,...,an)→∑n
1ajej is a continuous formKn with the usual Euclidean topology
to X with the topology deﬁned by ||·||1.
c) {x∈X|||x||1 = 1}is compact in the topology deﬁned by ||·||1.
d) All norms on X are equivalent. (Compare any norm to ||·||1.)
Proof.
a) We can ﬁrst see that ||x||1 = 0 ⇐⇒x = 0 since ∑n
1|aj|= 0 ⇐⇒aj = 0∀j = 1,...,n , and
0 := 0e1 +···+ 0en.
Next, to see the triangle inequality, we ﬁrst note that the triangle inequality naturally holds∀x,y∈
K. Therefore, if x, y∈X⇒x =∑n
1αjej, y =∑n
1βjej, and hence:
||x + y||1 =
⏐⏐⏐⏐
⏐⏐⏐⏐
n∑
j=1
αjej +
n∑
j=1
βjej
⏐⏐⏐⏐
⏐⏐⏐⏐
1
=
⏐⏐⏐⏐
⏐⏐⏐⏐
n∑
j=1
(αj +βj)ej
⏐⏐⏐⏐
⏐⏐⏐⏐
1
=
n∑
j=1
|αj +βj|
≤
n∑
j=1
|αj|+
n∑
j=1
|βj|=||x||1 +||y||1
So the triangle inequality holds. Now suppose λ∈K, we therefore have:
||λx||1 =
⏐⏐⏐⏐
⏐⏐⏐⏐λ
n∑
j=1
αjej
⏐⏐⏐⏐
⏐⏐⏐⏐
1
=
⏐⏐⏐⏐
⏐⏐⏐⏐
n∑
j=1
(λαj)ej
⏐⏐⏐⏐
⏐⏐⏐⏐
1
=
n∑
j=1
|λαj|=|λ|
n∑
j=1
|αj|=|λ|||x||1
And hence we have shown the three conditions for ||·||1 to be a norm on X.
b) From Part a), by dropping the absolute values in expressions of the form∑n
1|aj|, and replacing it by∑n
1ajej, the one inequality now becomes an equality, and hence the rest proves that T :Kn→X,
where T (a1,···,an) = ∑n
1ajej, is a linear map . We may now invoke (Folland) Proposition 5.2,
which states T is continuous ⇐⇒T is continuous at 0.
Let ϵ>0, and δ=ϵ/n. Then if:
||x−0||=||x||= (a2
1 +···a2
n)1/2 <δ ⇒a2
i≤(a2
1 +···+a2
n)<δ2 ∀i = 1,...,n
And so|ai|<|δ|=ϵ/n. Therefore, we have:
||T x||1 =
⏐⏐⏐⏐
⏐⏐⏐⏐
n∑
j=1
ajej
⏐⏐⏐⏐
⏐⏐⏐⏐
1
=|a1|+···+|an|<n
(ϵ
n
{
=ϵ
c) We begin by showing Γ := {(a1,...,an)∈Kn|∑n
1|aj|= 1}⊂Kn is compact. To see this, we
can simply show that Γ is closed and bounded since Γ ⊂Kn = Cn or Rn. The boundness of Γ is
easy to see since: ||(a1,...,an)||2 =||x||2 := (∑n
1a2
j)1/2⇒|aj|≤1∀j = 1,...,n ⇒B2(0)⊃Γ,
hence Γ is bounded.
41

To see Γ is closed, we show that Γ c is open. If x∈Γc, then:
x∈
{
(a1,...,an)|
n∑
1
|aj|⁄= 1
}
≡
{
(a1,...,an)|
n∑
1
|aj|< 1
}
⊔
{
(a1,...,an)|
n∑
1
|aj|> 1
}
:= Γ 1⊔Γ 2
I.e., if x = (x1,...,xn), then ∑n
1|xj|< 1 or ∑n
1|xj|> 1. Assume x∈Γ 1, and y∈Kn. Letting
ϵ1 = 1−∑n
1|xj|> 0, then in taking δ1 =ϵ1/n, we have:
||x−y||2 <δ1 ⇒ |xi−yi|≤||x−y||2 <δ1 = ϵ1
n ∀i∈{1,...,n}
⇒ ||x−y||1 =
n∑
j=1
|xj−yj|<n
(ϵ
n
{
= 1−
n∑
j=1
|xj|
⇒
n∑
j=1
|xj|−
n∑
j=1
|yj|< 1−
n∑
j=1
|xj| since|a|−|b|<|b−a|
⇒
n∑
j=1
|yj|< 1
And so Bϵ1/n(x)⊂Γ 1, so Γ 1 is open. Now suppose x∈Γ 2. Letting ϵ2 =∑n
1|xj|−1 and y∈Kn
as before. Then letting δ2 =ϵ2/2, we have:
||x−y||2 <δ2 ⇒ |xi−yi|≤||x−y||2 <δ2 = ϵ2
n ∀i∈{1,...,n}
⇒ ||x−y||1 =
n∑
j=1
|xj−yj|<n
(ϵ
n
{
=
n∑
j=1
|xj|−1
⇒
n∑
j=1
|xj|−
n∑
j=1
|yj|<
n∑
j=1
|xj|−1 since |b|−|a|<|b−a|
⇒
n∑
j=1
|yj|> 1
And so Bϵ2/n(x)⊂Γ 2, and hence Γ 2 is open. Now since Γ c = Γ 1⊔Γ 2, we can now conclude that
Γc is open, and hence Γ is closed, and hence compact. Furthermore, in Part b), we showed that T
(as deﬁned in Part b) is continuous. Therefore, since:
T (Γ) ={x∈X|||x||1 = 1}
We may now conclude that since Γ is compact, so too is{x∈X|||x||1 = 1}in the topology deﬁned
by||·||1.
d) Suppose ||·||: χ→R≥0 is an arbitrary norm on X. We recall that to show ||·||and||·||1 are
equivalent, we need to ﬁnd C1,C 2 > 0 s.t. C1||x||1≤||x||≤C2||x||1∀x∈X. If x = 0, then
||x||1 =||x||since both are norms, selecting any C1≤C2 where C1,C 2 > 0 proves the equivalence
of these norms for x = 0; therefore, assume x⁄= 0.
If we let C2 = max({||ej||n
1 ), then if x∈X ⇒x =∑n
1xjej, then:
||x||
∗
≤
n∑
j=1
|xj|||ej||≤C2
n∑
j=1
=C2||x||1 where we have
∗
≤from the ∆-inequality
42

So we have found an appropriate C2.
We now claim that||·||is continuous in the topology deﬁned by ||·||1. To see this, let ϵ>0, and
δ=ϵ/n. If x, y∈X and||x−y||1 <δ, then by what we found above:
||x−y||≤C2||x−y||1 <C 2
( ϵ
C2
{
=ϵ
Which tells us that||·||is indeed continuous on X in the topology deﬁned by ||·||1.
By Part c), we recall thatA :={x∈X|||x||1 = 1}is a compact set in the topology deﬁned by||·||1.
Therefore, by the continuity of ||·||, and since we are assuming x⁄= 0, we know that min x∈A||x||
exists, so let’s call this min C1. Explicitly now:
C1≤
⏐⏐⏐⏐
⏐⏐⏐⏐
x
||x||1
⏐⏐⏐⏐
⏐⏐⏐⏐⇒C1||x||1≤||x|| ∀x∈X
Hence completing our proof since we found both C1,C 2 which satisfy the necessary inequality.
4.5 Folland 5.9
Prove the following Proposition:
Proposition. 4.5:
Let Ck([0, 1]) be the space of functions on [0 , 1] possessing continuous derivatives up to order k
on [0, 1], including one-sided derivatives at the endpoints.
a) If f∈C([0, 1]), then f∈Ck([0, 1]) ⇐⇒f is k times continuously diﬀerentiable on (0 , 1)
and limx↘nf (j)(x) and limx↗1f (j)(x) exist for j≤k. (The mean value theorem is useful.)
b) ||f||=∑k
0||f (j)||u is a norm on Ck([0, 1]) that makes Ck([0, 1]) into a Banach space. (Use
induction on k. The essential point is that if {fn}⊂C 1([0, 1]), fn→f uniformly, and
f′
n→g uniformly, then f∈C 1([0, 1]) and f′= g. The easy way to prove this is to show
that f(x)−f(0) =
x
0 g(t)dt.)
Proof.
a) We’ll proceed to prove this claim through induction. Suppose k = 0, then the forward case of
f∈C([0, 1]) implying f is diﬀerentiable on (0, 1) and and limx↘nf(x) and limx↗1f(x) existing is
by the deﬁnition of C([0, 1]).
Now, for the backward direction (k = 0), supposef∈C((0, 1)), limx↘nf(x), and limx↗1f(x) exist
- this, however, is simply the deﬁnition of f∈C([0, 1]).
Let L(j)
0 := lim (j)
x↘nf(x) and L(j)
1 := limx↗nf (j)(x). Now assume the property above holds for
k =n−1. The forward direction is simply by deﬁnition. For the backward direction, if we wish to
show that f being k times diﬀerentiable on (0, 1) and lim (j)
x↘nf(x) and limx↗nf (j)(x) existing for
j≤n implies f∈Ck([0, 1]), we may proceed as follows. Firstly, by the existence of the one sided
derivatives, we know that∀ϵ>0,∃δ >0 such that if 0 <x<δ, then|f (j)(x)−L(j)
0 |<ϵ,∀j≤n.
Furthermore, WLOG, we may omit the L(j)
1 case since all we need to chance in the argument is
43

that δ < x <1 instead of 0 < x < δ. Moreover, by the mean value theorem, ∃ˆx∈(0,δ) s.t.
f (j−1)(x)−f (j−1)(0) = (x−0)f (j)(ˆx) =xf (j)(ˆx) Therefore:
⏐⏐⏐⏐
f (j−1)(x)−f (j−1)(x)
x −L0
⏐⏐⏐⏐=|f (j)(ˆx)−L1|<ϵ since ˆx∈(0,δ)
And so limx↘0
f (j−1)(x)−f (j−1)(x)
x =L0∀j≤n, and by the exact same argument for 1, we see that
limx↗0
f (j−1)(x)−f (j−1)(x)
x = L1∀j≤n, and so f∈C (n)([0, 1]), completing our inductive step and
proving this proposition∀k∈N.
b) We proceed, as hinted, by induction. Suppose that {fn}∞
1 is Cauchy in C 1. Then fn→f in C 0
and f′
n→g in C. Therefore:
fn(x) =fn(0) +
∫x
0
f′
n(y)dy
However, sincef′
n→g, by the dominated convergence theorem we have:
f(x) = lim
n→∞
f(x) = lim
n→∞
fn(0) + lim
n→∞
∫x
0
f′
n(y)dy =f(0) +
∫x
0
g(y)dy
And therefore by the fundamental theorem of calculus we may conclude thatg =f′, and sofn→f
in C 1.
We now make our inductive step. Assume the statement is true up until j =k. Suppose then that
{fn}∞
1 is Cauchy in Ck+1 and fn→f in Ck and f (k+1)
n →g in Ck+1. Therefore, f (k)
n →f (k+1)
n
in C, and f (k+1)
n →g in C. We therefore may conclude that f (k+1)
n →f (k+1)
n in C, and ultimately
fn→f in C (k+1).
To ﬁnish our proof, we need to prove that ||·||is indeed a norm. Firstly, if f⁄≡0, then naturally
||f||⁄= 0, so||f||= 0 ⇐⇒f≡0. Since||·||is simply a sum of other norms, the triangle inequality
and absolutely scalability are both trivially immediate like deﬁniteness.
5 Chapter 6
5.1 Folland 6.3
Prove the following Proposition:
Proposition. 5.1:
If 1≤p<r ≤∞,Lp\Lr is a Banach space with norm||f||=||f||p +||f||r, and if p<q <r , the
inclusion map Lp\Lr→Lq is continuous.
Proof. We begin by ﬁrst showing that Lp\Lr is a Banach Space w.r.t. ||f||=||f||p +||f||r (I.e., show
Lp\Lr a normed vector space and complete w.r.t. ||f||).
The fact that||·||r and||·||p are norms implies||·||is a norm. Firstly, ||·||≥0 since||·||p,||·||r≥0.
Now, suppose f,g ∈Lr\Lp, and λ∈K, then we have:
||f +g||=||f +g||p +||f +g||r≤||f||p +||g||p +||f||r +||g||r =||f||+||g||
44

||λf||=||λf||p +||λf||r =|λ|||f||p +|λ|||f||r =|λ|||f||
||f||= 0 ⇐⇒ ||f||p =||f||r = 0 ⇐⇒f≡0 µ-a.e.
We can also immediately see that Lp\Lr is a vector space since if u,v ∈Lp\Lr, then u,v ∈Lp and
Lr, and so all our conditions for being a vector subspace are satisﬁed since both Lp and Lr are vector
subspaces.
Suppose now that {fn}∞
1 be a Cauchy sequence in Lp\ Lr. By noting that ∀n,m ∈N, we have
||fn−fm||p≤||fn−fm||and||fn−fm||r≤||fn−fm||, and hence{fn}∞
1 are also Cauchy in Lp andLr.
We can thus deﬁne g and h as limfn in Lp and Lr respectively. Let ϵ>0, then∃N∈N s.t. if we take
δ=ϵ(p+1)/p, then letting||fn−g||p <δ, and in setting E :={x∈X|ϵ≤|fn(x)−g(x)|}, we have:
µ(E) = 1
ϵp
∫
E
ϵpdµ≤1
ϵp
∫
E
|fn−g|pdµ≤1
ϵp
∫
|fn−g|pdµ= 1
ϵp
(
||fn−g||p
{p
< 1
ϵp
(
δ
{p
=ϵ
I.e., µ(E) < ϵ⇒{fn}∞
1 converges in measure to g. If r <∞, the argument holds for interchanging p
for r. If r =∞, then∃a subsequence fnk of{fn}∞
1 s.t. fnk→h µ-a.e. We have therefore shown that
g =h, and so g∈Lp\Lr. Therefore, since fn→g inLp andLr, we havefn→g inLp\Lr - and hence
Lp\Lr is a Banach space with norm ||·||.
Let now p < q < r. By (Folland) Proposition 6.10, we know that ∃λ∈(0, 1) s.t.||f||λ
p||f||1−λ
r where
1
q = λ
p + 1−λ
r . Thus, since ||f||p≤||f||and||f||r≤||f||, we have:
||f||q≤||f||λ
p||f||1−λ
r ≤||f||λ||f||1−λ=||f||
Suppose now that ϵ>0 and f,g ∈Lp\Lr, then if||f−g||<δ=ϵ, we have||f−g||q≤||f−g||<ϵby
the above inequality. Hence ι:Lp\Lr→Lq is uniformly continuous (and naturally continuous as well).
5.2 Folland 6.4
Prove the following Proposition:
Proposition. 5.2:
If 1≤p < r≤∞, Lp +Lr is a Banach Space with norm ||f||= inf{||g||p +||h||r|f = g +h},
and if p<q <r , the inclusion map Lq→Lp +Lr is continuous.
Proof. We begin by showing ||·||, as deﬁned, is a norm. Firstly, ||·||≥0 since||·||p,||·||r≥0. Now,
suppose f1,f 2∈Lr +Lp, and λ∈K, then we have:
||f1 +f2||= inf
{
||g||p +||h||r
⏐⏐⏐f1 +f2 =g +h
}
= inf
{
||g1 +g2||p +||h1 +h2||r
⏐⏐⏐f1 +f2 =g +h = (g1 +g2) + (h1 +h2)
}
≤inf
{(
||g1||p +||g2||p
{
+
(
||h1||r +||h2||r
{⏐⏐⏐f1 +f2 =g +h = (g1 +g2) + (h1 +h2)
}
≤inf
{
||g1||p +||h1||r
⏐⏐⏐f1 =g1 +h1
}
+ inf
{
||g2||p +||h2||r
⏐⏐⏐f2 =g2 +h2
}
=||f1||+||f2||
45

||λf||= inf
{
||λg||p +||λh||r
⏐⏐⏐λf=λ(g +h)
}
= inf
{
|λ|||g||p +|λ|||h||r
⏐⏐⏐λf=λ(g +h)
}
=|λ|inf
{
||g||p +||h||r
⏐⏐⏐f =g +h
}
=|λ|||f||
||f||= 0 ⇐⇒ ||f||p =||f||r = 0∀g,h s.t. f =g +h ⇐⇒f≡0 µ-a.e.
We can also immediately see that Lp +Lr is a vector space since if u,v∈Lp +Lr, then u =u1 +u2,v =
v1 +v2 where u1,v 1∈Lp and u2,v 2∈Lr, and so all our conditions for being a vector subspace are
satisﬁed since both Lp and Lr are vector subspaces.
To show completeness, we make use of (Folland) Theorem 5.1 which states that a normed vector space,X,
is complete ⇐⇒every absolutely convergent series in X converges. So, suppose ∑∞
1 fn be an absolutely
convergent series inLp +Lr. By the deﬁnition of inf and ||·||, we know that∀n∈N,∃gn∈Lp,hn∈Lr
s.t. fn = gn +hn where||gn||p +||hn||r <||fn||+ 2−n. Therefore, from this inequality, and since both∑∞
1 fn and ∑∞
1 2−n are absolutely convergent, so too will ∑∞
1 gn and ∑∞
1 hn. Since Lp and Lr are
Banach spaces, ∑N
1 gn→g∈Lp and∑N
1 hn→h∈Lr. Furthermore, by deﬁnition ||·||≤||·||p and
||·||≤||·||r, so combining these two reverse inequalities, we have∑∞
1 fn =∑∞
1 (gn +hn), which therefore
has a limit in Lp +Lr, explicitly g +h∈Lp +Lr. We have thus show all the necessary conditions for
Lp +Lr to be a Banach Space w.r.t. ||·||.
Suppose p < q < rand f∈Lq. Let E :={x∈X|1 <|f(x)|}. Thus, by the construction of E, we
therefore have:|fχE|p≤|fχE|q and|fχEc|p≤|fχEc|q (I.e., fχE∈Lp,fχE∈Lr), and hence:
||f||=||fχE +fχEc||≤||fχE||p +||fχE||r≤||fχE||q +||fχEc||q =||f||q
Suppose now that ϵ>0 and f,g ∈Lq, then if||f−g||q <δ=ϵ, we have||f−g||≤||f−g||q <ϵby the
above inequality. Hence ι:Lq→Lp +Lr is uniformly continuous (and naturally continuous as well).
5.3 Folland 6.5
Prove the following Proposition:
Proposition. 5.3:
Suppose 0 <p<q < ∞. Then:
a) Lp⁄⊂Lq ⇐⇒X contains sets of arbitrarily small positive measure.
b) Lq⁄⊂Lp ⇐⇒X contains sets of arbitrarily large ﬁnite measure.
c) What about the case of q =∞?
Proof.
a) We ﬁrst prove the following Lemma:
Lemma. 5.1: Chebyshev’s Inequality
µ(Et)≤
(||f||p
t
{p
Where Et ={x∈X||f(x)|≥t}and p∈(0,∞).
46

Proof. Let g(x) =xp if x≥t, and 0 otherwise. We thus have 0 ≤tpχEt≤|f|pχEt, and hence:
µ(Et) = 1
tp
∫
tpχEtdµ≤1
tp
∫
Et
|f|pdµ≤
(
||f||p
{p
tp
Now back to the problem at hand. For the forward direction, we proceed via the contrapositive,
I.e., suppose ∃ϵ >0 s.t. ∀E⊂M(X),µ(E)⁄∈(0,ϵ). From Chebyshev’s Inequality, we know that
∃T s.t.∀t≥T , µ(Et) = 0 since µ(Et)≤
(||f||p
t
{p
→0, and so|f|≤T a.e. So:
∫
|f|qdµ=
∫
Et
|f|qdµ+
∫
Ec
t
|f|qdµ≤Tqµ(Et) +
∫
Ec
t
|f|pdµ<∞
And so f∈Lq.
For the converse, suppose ∀ϵ >0,∃E∈M(X) s.t. µ(E)∈(0,ϵ). Let us deﬁne {Fn}∞
1 where
0 < µ(Fn) < 1/n so that µ(Fn) →0. By deﬁning Gn := Fn\∪∞
n+1 Fm, we must have 0 <
µ(Fn) ≤µ(∪∞
n Gm). Furthermore, by taking subsequences, we may actually assume now that
0<µ(Gm)≤2−m. Now if we deﬁne:
f :=
∞∑
n=1
(
µ(Gn)
{−1/q
χGnn−2/p (≥0)
Then we have:
∫
|f|pdµ=
∫
fpdµ=
∫∞∑
n=1
(
µ(Gn)
{−p/q
χGnn−2dµ=
∞∑
n=1
1
n2 = π2
6 <∞
And so f∈Lp; however, one can see that f⁄∈Lq since:
∫
|f|qdµ=
∫
fqdµ=
∞∑
n=1
(
µ(Gn)
{1−p/q
n−2q/p≥
∞∑
n=1
2p/q−1n−2q/p =∞
b) For the forward direction, the proof here is completely analogous to that in a). For the converse,
by substituting
(
µ(Gn)
{−1/q
for
(
µ(Gn)
{−1/(p+1)
, and noting that now we have 2 m≤µ(Gm)<∞
instead of 0 <µ(Gm)≤2−m, the same results as in a) still hold.
c) For the case of q =∞, we have L∞⁄⊂Lp ⇐⇒µ(X) =∞, since if|f|p <C ∈R≥0, we have:
∫
|f|pdµ≤C
∫
dµ≤Cµ(X)<∞
5.4 Folland 6.7
Prove the following Proposition:
Proposition. 5.4:
If f∈Lp\L∞for some p< ∞, so that f∈Lq∀q >p, then||f||∞= limq→∞||f||q.
47

Proof. We may ﬁrst assume f ⁄≡0 a.e. by the triviality of this case. From (the proof of Folland)
Proposition 6.10, we know that:
||f||q≤
(
||f||∞
{1−p/q(
||f||p
{p/q
And so:
lim sup
q→∞
||f||q≤lim sup
q→∞
((
||f||∞
{1−p/q(
||f||p
{p/q{
=||f||∞
Furthermore, by our initial assumption, we have ||f||∞> 0. Suppose now that 0 < a <||f||∞and
Ea :={x∈X||f(x)|≥a}. We thus have:
aqµ(Ea)≤
(
||f||p
{p
≤
∫
Ea
|f|qdµ≤
(
||f||q
{q
⇒
(
aqµ(Ea)
{1/q
≤
((
||f||q
{q{1/q
⇒ lim inf
q→∞
a
(
µ(Ea)
{1/q
≤lim inf
q→∞
||f||q
⇒a≤lim inf
q→∞
||f||q
And so letting a→||f||∞, we thus have:
lim sup
q→∞
||f||q≤||f||∞≤lim inf
q→∞
||f||q
And so we must have all our inequalities become equalities: hence lim q→∞||f||q =||f||∞.
5.5 Folland 6.10
Prove the following Proposition:
Proposition. 5.5:
Suppose 1≤p <∞. If fn,f ∈Lp and fn→f a.e., then||fn−f||p→0 ⇐⇒ ||fn||p→||f||p.
[Use Exercise 20 in (Folland) 2.3.]
Proof. For the forward direction, if||fn−f||p→0, by the triangle inequality we have:
⏐⏐||fn||p−||f||p
⏐⏐≤||fn−f||p→0
And we therefore have||fn||p→||f||p.
For the converse, suppose||fn||p→||f||p. We now quickly prove the following result:
If z,w ∈C, then|z−w|p≤2p−1(|z|p +|w|p)∀p≥1
By the second derivative test, g(z) =|z|p is convex (I.e., g(tz + (1−t)w)≤tg(z) + (1−t)g(w)). So, if
we set t = 1/2, and move the 2p over to the other side, we have:
|z−w|p≤2p−1(|z|p +|w|p) ⇐⇒
⏐⏐⏐⏐
z−w
2
⏐⏐⏐⏐
p
≤1
2|z|p + 1
2|w|p
For which the latter is recognizably true due to the convexity of |·|p for p≥1 (and in making a change
of variables w′=−w)
Carrying on, let us deﬁne gn := 2p−1(|f|p +|fn|p)−|f−fn|p. By the above inequality, we know that
gn≥0, and so we may apply Fatou’s Lemma:
2p(
||f||p
{p
≤lim inf
n→∞
∫
gn = 2p(
||f||p
{p
−lim sup
n→∞
∫
|f−fn|pdµ
And so lim sup

|f−fn|pdµ≤0⇒||f−fn||p→0.
48

5.6 Folland 6.14
Prove the following Proposition:
Proposition. 5.6:
If g∈L∞, the operator T deﬁned by Tf = fg is bounded on Lp for 1≤p≤∞. Its operator
norm is at most ||g||∞with equality if µis semi-ﬁnite.
Proof. Firstly, we may assume g⁄≡0 due to the triviality of this case. We now proceed to see that:
(
||Tf||p
{p
=
∫
|fg|pdµ=|f|p|g|pdµ≤
(
||g||∞
{p
∫
|f|pdµ=
(
||g|∞|
{p(
||f||p
{p 
≤since|g|≤||g||∞

⇒||T||≤||g||∞
To see equality if µis semi-ﬁnite, suppose 0 < ϵ <||g||∞, By µ’s semi-ﬁnitness,∃E s.t. ||g||∞−ϵ <
|g|∀x∈E. Thus, we have:
||TχE||p =||gχE||>
(
||g||∞−ϵ
{
||χE||p ⇒ ||T||>||g||∞−ϵ⇒ ||T||≥||g||∞
Where we have the last implication by ϵ’s arbitrarily, and to satisfy both equalities, we must have
||g||∞=||T||.
49

