MEASURE and INTEGRATION
Problems with Solutions
Anh Quang Le, Ph.D.
October 8, 2013

1
NOTATIONS
A(X): The σ-algebra of subsets of X.
(X, A(X), µ) : The measure space on X.
B(X): The σ-algebra of Borel sets in a topological space X.
ML : The σ-algebra of Lebesgue measurable sets in R.
(R, ML, µL): The Lebesgue measure space on R.
µL: The Lebesgue measure on R.
µ∗
L: The Lebesgue outer measure on R.
1E or χE: The characteristic function of the set E.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

2
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Contents
Contents 1
1 Measure on a σ-Algebra of Sets 5
2 Lebesgue Measure on R 21
3 Measurable Functions 33
4 Convergence a.e. and Convergence in Measure 45
5 Integration of Bounded Functions on Sets of Finite Measure 53
6 Integration of Nonnegative Functions 63
7 Integration of Measurable Functions 75
8 Signed Measures and Radon-Nikodym Theorem 97
9 Diﬀerentiation and Integration 109
10 Lp Spaces 121
11 Integration on Product Measure Space 141
12 Some More Real Analysis Problems 151
3
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

4 CONTENTS
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 1
Measure on a σ-Algebra of Sets
1. Limits of sequences of sets
Deﬁnition 1 Let (An)n∈N be a sequence of subsets of a set X.
(a) We say that (An) is increasing if An ⊂ An+1 for all n ∈N, and decreasing if An ⊃ An+1 for
all n ∈N.
(b) For an increasing sequence (An), we deﬁne
lim
n→∞
An :=
∞⋃
n=1
An.
For a decreasing sequence (An), we deﬁne
lim
n→∞
An :=
∞⋂
n=1
An.
Deﬁnition 2 For any sequence (An) of subsets of a set X, we deﬁne
lim inf
n→∞
An :=
⋃
n∈N
⋂
k≥n
Ak
lim sup
n→∞
An :=
⋂
n∈N
⋃
k≥n
Ak.
Proposition 1 Let (An) be a sequence of subsets of a set X. Then
(i) lim inf
n→∞
An = {x ∈ X : x ∈ An for all but ﬁnitely many n ∈N}.
(ii) lim sup
n→∞
An = {x ∈ X : x ∈ An for inﬁnitely many n ∈N}.
(iii) lim inf
n→∞
An ⊂ lim sup
n→∞
An.
2. σ-algebra of sets
5
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

6 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
Deﬁnition 3 (σ-algebra)
Let X be an arbitrary set. A collection A of subsets of X is called an algebra if it satisﬁes the
following conditions:
1. X ∈ A.
2. A ∈ A ⇒ Ac ∈ A.
3. A, B ∈ A ⇒ A ∪ B ∈ A.
An algebra A of a set X is called a σ-algebra if it satisﬁes the additional condition:
4. An ∈ A, ∀n ∈N ⇒ ⋃
n∈N An ∈ n ∈N.
Deﬁnition 4 (Borel σ-algebra)
Let (X, O) be a topological space. We call the Borel σ-algebra B(X) the smallest σ-algebra of X
containing O.
It is evident that open sets and closed sets in X are Borel sets.
3. Measure on a σ-algebra
Deﬁnition 5 (Measure)
Let A be a σ-algebra of subsets of X. A set function µ deﬁned on A is called a measure if it
satisﬁes the following conditions:
1. µ(E) ∈ [0, ∞] for every E ∈ A.
2. µ(∅) = 0 .
3. (En)n∈N ⊂ A, disjoint ⇒ µ
(⋃
n∈N En
)
= ∑
n∈N µ(En).
Notice that if E ∈ A such that µ(E) = 0, then E is called a null set . If any subset E0 of a null set
E is also a null set, then the measure space ( X, A, µ) is called complete.
Proposition 2 (Properties of a measure)
A measure µ on a σ-algebra A of subsets of X has the following properties:
(1) Finite additivity: (E1, E2, ..., En) ⊂ A, disjoint =⇒ µ (⋃n
k=1 Ek) = ∑n
k=1 µ(Ek).
(2) Monotonicity: E1, E2 ∈ A, E 1 ⊂ E2 =⇒ µ(E1) ≤ m(E2).
(3) E1, E2 ∈ A, E 1 ⊂ E2, µ (E1) < ∞ =⇒ µ(E2 \ E1) = µ(E2) − µ(E1).
(4) Countable subadditivity: (En) ⊂ A =⇒ µ
(⋃
n∈N En
)
≤ ∑
n∈N µ(En).
Deﬁnition 6 (Finite, σ-ﬁnite measure)
Let (X, A, µ) be a measure space.
1. µ is called ﬁnite if µ(X) < ∞.
2. µ is called σ-ﬁnite if there exists a sequence (En) of subsets of X such that
X =
⋃
n∈N
En and µ(En) < ∞, ∀n ∈N.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

7
4. Outer measures
Deﬁnition 7 (Outer measure)
Let X be a set. A set function µ∗ deﬁned on the σ-algebra P(X) of all subsets of X is called an
outer measure on X if it satisﬁes the following conditions:
(i) µ∗(E) ∈ [0, ∞] for every E ∈ P (X).
(ii) µ∗(∅) = 0 .
(iii) E, F ∈ P(X), E ⊂ F ⇒ µ∗(E) ≤ µ∗(F ).
(iv) countable subadditivity:
(En)n∈N ⊂ P (X), µ ∗
( ⋃
n∈N
En
)
≤
∑
n∈N
µ∗(En).
Deﬁnition 8 (Caratheodory condition)
We say that E ∈ P (X) is µ∗-measurable if it satisﬁes the Caratheodory condition:
µ∗(A) = µ∗(A ∩ E) + µ∗(A ∩ Ec) for every A ∈ P (X).
We write M(µ∗) for the collection of all µ∗-measurable E ∈ P (X). Then M(µ∗) is a σ-algebra.
Proposition 3 (Properties of µ∗)
(a) If E1, E2 ∈ M(µ∗), then E1 ∪ E2 ∈ M(µ∗).
(b) µ∗ is additive on M(µ∗), that is,
E1, E2 ∈ M(µ∗), E 1 ∩ E2 =∅ =⇒ µ∗(E1 ∪ E2) = µ∗(E1) + µ∗(E2).
∗ ∗ ∗∗
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

8 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
Problem 1
Let A be a collection of subsets of a set X with the following properties:
1. X ∈ A.
2. A, B ∈ A ⇒ A \ B ∈ A.
Show that A is an algebra.
Solution
(i) X ∈ A.
(ii) A ∈ A ⇒ Ac = X \ A ∈ A (by 2).
(iii) A, B ∈ A ⇒ A ∩ B = A \ Bc ∈ A since Bc ∈ A (by (ii)).
Since Ac, Bc ∈ A, (A ∪ B)c = Ac ∩ Bc ∈ A. Thus, A ∪ B ∈ A. ■
Problem 2
(a) Show that if (An)n∈N is an increasing sequence of algebras of subsets of a set
X, then ⋃
n∈N An is an algebra of subsets of X.
(b) Show by example that even if An in (a) is a σ-algebra for every n ∈N, the
union still may not be a σ-algebra.
Solution
(a) Let A = ⋃
n∈N An. We show that A is an algebra.
(i) Since X ∈ A n, ∀n ∈N, so X ∈ A.
(ii) Let A ∈ A . Then A ∈ A n for some n. And so Ac ∈ A n ( since An is an
algebra). Thus, Ac ∈ A.
(iii) Suppose A, B ∈ A. We shall show A ∪ B ∈ A.
Since {An} is increasing, i.e., A1 ⊂ A 2 ⊂ ... and A, B ∈ ⋃
n∈N An, there is
some n0 ∈N such that A, B ∈ A 0. Thus, A ∪ B ∈ A 0. Hence, A ∪ B ∈ A.
(b) Let X =N, An = the family of all subsets of {1, 2, ..., n} and their complements.
Clearly, An is a σ-algebra and A1 ⊂ A 2 ⊂ .... However, ⋃
n∈N An is the family of all
ﬁnite and co-ﬁnite subsets of N, which is not a σ-algebra. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

9
Problem 3
Let X be an arbitrary inﬁnite set. We say that a subset A of X is co-ﬁnite if its
complement Ac is a ﬁnite subset of X. Let A consists of all the ﬁnite and the
co-ﬁnite subsets of a set X.
(a) Show that A is an algebra of subsets of X.
(b) Show that A is a σ-algebra if and only if X is a ﬁnite set.
Solution
(a)
(i) X ∈ A since X is co-ﬁnite.
(ii) Let A ∈ A. If A is ﬁnite then Ac is co-ﬁnite, so Ac ∈ A. If A co-ﬁnite then Ac
is ﬁnite, so Ac ∈ A. In both cases,
A ∈ A ⇒ Ac ∈ A.
(iii) Let A, B ∈ A. We shall show A ∪ B ∈ A.
If A and B are ﬁnite, then A ∪ B is ﬁnite, so A ∪ B ∈ A. Otherwise, assume
that A is co-ﬁnite, then A ∪ B is co-ﬁnite, so A ∪ B ∈ A. In both cases,
A, B ∈ A ⇒ A ∪ B ∈ A.
(b) If X is ﬁnite then A = P(X), which is a σ-algebra.
To show the reserve, i.e., if A is a σ-algebra then X is ﬁnite, we assume that X
is inﬁnite. So we can ﬁnd an inﬁnite sequence ( a1, a2, ...) of distinct elements of X
such that X \ {a1, a2, ...} is inﬁnite. Let An = {an}. Then An ∈ A for any n ∈N,
while ⋃
n∈N An is neither ﬁnite nor co-ﬁnite. So ⋃
n∈N An /∈ A . Thus, A is not a
σ-algebra: a contradiction! ■
Note:
For an arbitrary collection C of subsets of a set X, we write σ(C) for the smallest
σ-algebra of subsets of X containing C and call it the σ-algebra generated by C.
Problem 4
Let C be an arbitrary collection of subsets of a set X. Show that for a given
A ∈ σ(C), there exists a countable sub-collection CA of C depending on A such
that A ∈ σ(CA). (We say that every member of σ(C) is countable generated).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

10 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
Solution
Denote by B the family of all subsets A of X for which there exists a countable
sub-collection CA of C such that A ∈ σ(CA). We claim that B is a σ-algebra and
that C ⊂ B .
The second claim is clear, since A ∈ σ({A}) for any A ∈ C . To prove the ﬁrst one,
we have to verify that B satisﬁes the deﬁnition of a σ-algebra.
(i) Clearly, X ∈ B .
(ii) If A ∈ B then A ∈ σ(CA) for some countable family CA ⊂ σ(C). Then
Ac ∈ σ(CA), so Ac ∈ B .
(iii) Suppose {An}n∈N ⊂ B . Then An ∈ σ(CAn) for some countable family CAn ⊂ C .
Let E = ⋃
n∈N CAn then E is countable and E ⊂ C and An ∈ σ(E) for all n ∈N.
By deﬁnition of σ-algebra, ⋃
n∈N An ∈ σ(E), and so ⋃
n∈N An ∈ B .
Thus, B is a σ-algebra of subsets of X and E ⊂ B . Hence,
σ(E) ⊂ B .
By deﬁnition of B, this implies that for every A ∈ σ(C) there exists a countable
E ⊂ C such that A ∈ σ(E). ■
Problem 5
Let γ a set function deﬁned on a σ-algebra A of subsets of X. Show that it γ is
additive and countably subadditive on A, then it is countably additive on A.
Solution
We ﬁrst show that the additivity of γ implies its monotonicity. Indeed, let A, B ∈ A
with A ⊂ B. Then
B = A ∪ (B \ A) and A ∩ (B \ A) =∅.
Since γ is additive, we get
γ(B) = γ(A) + γ(B \ A) ≥ γ(A).
Now let ( En) be a disjoint sequence in A. For every N ∈N, by the monotonicity
and the additivity of γ, we have
γ
( ⋃
n∈N
En
)
≥ γ
( N⋃
n=1
En
)
=
N∑
n=1
γ(En).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

11
Since this holds for every N ∈N, so we have
(i) γ
( ⋃
n∈N
En
)
≥
∑
n∈N
γ(En).
On the other hand, by the countable subadditivity of γ, we have
(ii) γ
( ⋃
n∈N
En
)
≤
∑
n∈N
γ(En).
From (i) and ( ii), it follows that
γ
( ⋃
n∈N
En
)
=
∑
n∈N
γ(En).
This proves the countable additivity of γ. ■
Problem 6
Let X be an inﬁnite set and A be the algebra consisting of the ﬁnite and co-ﬁnite
subsets of X (cf. Prob.3). Deﬁne a set function µ on A by setting for every
A ∈ A:
µ(A) =
{ 0 if A is ﬁnite
1 if A is co-ﬁnite.
(a) Show that µ is additive.
(b) Show that when X is countably inﬁnite, µ is not additive.
(c) Show that when X is countably inﬁnite, then X is the limit of an increasing
sequence {An : n ∈N} in A with µ(An) = 0 for every n ∈N, but µ(X) = 1 .
(d) Show that when X is uncountably, the µ is countably additive.
Solution
(a) Suppose A, B ∈ A and A ∩ B = ∅ (i.e., A ⊂ Bc and B ⊂ Ac).
If A is co-ﬁnite then B is ﬁnite (since B ⊂ Ac). So A ∪ B is co-ﬁnite. We have
µ(A ∪ B) = 1 , µ (A) = 1 and µ(B) = 0. Hence, µ(A ∪ B) = µ(A) + µ(B).
If B is co-ﬁnite then A is ﬁnite (since A ⊂ Bc). So A ∪ B is co-ﬁnite, and we have
the same result. Thus, µ is additive.
(b) Suppose X is countably inﬁnite. We can then put X under this form: X =
{x1, x2, ...}, x i ⁄= xj if i ⁄= j. Let An = {xn}. Then the family {An}n∈N is disjoint
and µ(An) = 0 for every n ∈N. So ∑
n∈N µ(An) = 0. On the other hand, we have
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

12 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
⋃
n∈N An = X, and µ(X) = 1. Thus,
µ
( ⋃
n∈N
An
)
⁄=
∑
n∈N
µ(An).
Hence, µ is not additive.
(c) Suppose X is countably inﬁnite, and X = {x1, x2, ...}, x i ⁄= xj if i ⁄= j as in
(b). Let Bn = {x1, x2, ..., xn}. Then µ(Bn) = 0 for every n ∈N, and the sequence
(Bn)n∈N is increasing. Moreover,
lim
n→∞
Bn =
⋃
n∈N
Bn = X and µ(X) = 1 .
(d) Suppose X is uncountably. Consider the family of disjoint sets {Cn}n∈N in A.
Suppose C = ⋃
n∈N Cn ∈ A. We ﬁrst claim: At most one of the Cn’s can be co-ﬁnite.
Indeed, assume there are two elements Cn and Cm of the family are co-ﬁnite. Since
Cm ⊂ C c
n, so Cm must be ﬁnite: a contradiction.
Suppose Cn0 is the co-ﬁnite set. Then since C ⊃ Cn0, C is also co-ﬁnite. Therefore,
µ(C) = µ
( ⋃
n∈N
Cn
)
= 1.
On the other hand, we have
µ(Cn0) = 1 and µ(Cn) = 0 for n ⁄= n0.
Thus,
µ
( ⋃
n∈N
Cn
)
=
∑
n∈N
µ(Cn).
If all Cn are ﬁnite then ⋃
n∈N Cn is ﬁnite, so we have
0 = µ
( ⋃
n∈N
Cn
)
=
∑
n∈N
µ(Cn). ■
Problem 7
Let (X, A, µ) be a measure space. Show that for any A, B ∈ A , we have the
equality:
µ(A ∪ B) + µ(A ∩ B) = µ(A) + µ(B).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

13
Solution
If µ(A) = ∞ or µ(B) = ∞, then the equality is clear. Suppose µ(A) and µ(B) are
ﬁnite. We have
A ∪ B = (A \ B) ∪ (A ∩ B) ∪ (B \ A),
A = (A \ B) ∪ (A ∩ B)
B = (B \ A) ∪ (A ∩ B).
Notice that in these decompositions, sets are disjoint. So we have
µ(A ∪ B) = µ(A \ B) + µ(A ∩ B) + µ(B \ A),(1.1)
µ(A) + µ(B) = 2 µ(A ∩ B) + µ(A \ B) + µ(B \ A).(1.2)
From (1.1) and (1.2) we obtain
µ(A ∪ B) − µ(A) − µ(B) = −µ(A ∩ B).
The equality is proved. ■
Problem 8
The symmetry diﬀerence of A, B ∈ P (X) is deﬁned by
A ∆ B = (A \ B) ∪ (B \ A).
(a) Prove that
∀A, B, C ∈ P (X), A ∆ B ⊂ (A ∆ C) ∪ (C ∆ B).
(b) Let (X, A, µ) be a measure space. Show that
∀A, B, C ∈ A, µ (A ∆ B) ≤ µ(A ∆ C) + µ(C ∆ B).
Solution
(a) Let x ∈ A ∆ B. Suppose x ∈ A \ B. If x ∈ C then x ∈ C \ B so x ∈ C ∆ B. If
x /∈ C, then x ∈ A \ C, so x ∈ A ∆ C. In both cases, we have
x ∈ A ∆ B ⇒ x ∈ (A ∆ C) ∪ (C ∆ B).
The case x ∈ B \ A is dealt with the same way.
(b) Use subadditivity of µ and (a). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

14 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
Problem 9
Let X be an inﬁnite set and µ the counting measure on the σ-algebra A = P(X).
Show that there exists a decreasing sequence (En)n∈N in A such that
lim
n→∞
En =∅ with lim
n→∞
µ(En) ⁄= 0.
Solution
Since X is a inﬁnite set, we can ﬁnd an countably inﬁnite set {x1, x2, ...} ⊂ X with
xi ⁄= xj if i ⁄= j. Let En = {xn, xn+1, ...}. Then ( En)n∈N is a decreasing sequence in
A with
lim
n→∞
En =∅ and lim
n→∞
µ(En) = 0 . ■
Problem 10 (Monotone sequence of measurable sets)
Let (X, A, µ) be a measure space, and (En) be a monotone sequence in A.
(a) If (En) is increasing, show that
lim
n→∞
µ(En) = µ
(
lim
n→∞
En
)
.
(b) If (En) is decreasing, show that
lim
n→∞
µ(En) = µ
(
lim
n→∞
En
)
,
provided that there is a set A ∈ A satisfying µ(A) < ∞ and A ⊃ E1.
Solution
Recall that if ( En) is increasing then lim n→∞ En = ⋃
n∈N En ∈ A , and if ( En) is
decreasing then lim n→∞ En = ⋂
n∈N En ∈ A . Note also that if ( En) is a monotone
sequence in A, then
(
µ(En)
)
is a monotone sequence in [0 , ∞] by the monotonicity
of µ, so that lim n→∞ µ(En) exists in [0 , ∞].
(a) Suppose ( En) is increasing. Then the sequence
(
µ(En)
)
is also increasing.
Consider the ﬁrst case where µ(En0) = ∞ for some En0. In this case we have
limn→∞ µ(En) = ∞. On the other hand,
En0 ⊂
⋃
n∈N
En = lim
n→∞
En =⇒ µ
(
lim
n→∞
En
)
≥ µ(En0) = ∞.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

15
Thus
µ
(
lim
n→∞
En
)
= ∞ = lim
n→∞
µ(En).
Consider the next case where µ(En) < ∞ for all n ∈N. Let E0 =∅, then consider
the disjoint sequence ( Fn) in A deﬁned by Fn = En \En−1 for all n ∈N. It is evident
that ⋃
n∈N
En =
⋃
n∈N
Fn.
Then we have
µ
(
lim
n→∞
En
)
= µ
( ⋃
n∈N
En
)
= µ
( ⋃
n∈N
Fn
)
=
∑
n∈N
µ(Fn) =
∑
n∈N
µ(En \ En−1)
=
∑
n∈N
[
µ(En) − µ(En−1)
]
= lim
n→∞
n∑
k=1
[
µ(Ek) − µ(Ek−1)
]
= lim
n→∞
[
µ(En) − µ(E0)
]
= lim
n→∞
µ(En). □
(b) Suppose ( En) is decreasing and assume the existence of a containing set A with
ﬁnite measure. Deﬁne a disjoint sequence ( Gn) in A by setting Gn = En \ En+1 for
all n ∈N. We claim that
(1) E1 \
⋂
n∈N
En =
⋃
n∈N
Gn.
To show this, let x ∈ E1 \ ⋂
n∈N En. Then x ∈ E1 and x /∈ ⋂
n∈N En. Since the
sequence ( En) is decreasing, there exists the ﬁrst set En0+1 in the sequence not
containing x. Then
x ∈ En0 \ En0+1 = Gn0 =⇒ x ∈
⋃
n∈N
Gn.
Conversely, if x ∈ ⋃
n∈N Gn, then x ∈ Gn0 = En0 \ En0+1 for some n0 ∈ N. Now
x ∈ En0 ⊂ E1. Since x /∈ En0+1, we have x /∈ ⋂
n∈N En. Thus x ∈ E1 \ ⋂
n∈N En.
Hence (1) is proved.
Now by (1) we have
(2) µ
(
E1 \
⋂
n∈N
En
)
= µ
( ⋃
n∈N
Gn
)
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

16 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
Since µ
(⋂
n∈N En
)
≤ µ(E1) ≤ µ(A) < ∞, we have
(3) µ
(
E1 \
⋂
n∈N
En
)
= µ(E1) − µ
( ⋂
n∈N
En
)
= µ(E1) − µ( lim
n→∞
En).
By the countable additivity of µ, we have
(4) µ
( ⋃
n∈N
Gn
)
=
∑
n∈N
µ(Gn) =
∑
n∈N
µ(En \ En+1)
=
∑
n∈N
[
µ(En) − µ(En+1)
]
= lim
n→∞
n∑
k=1
[
µ(Ek) − µ(Ek+1)
]
= lim
n→∞
[
µ(E1) − µ(En+1)
]
= µ(E1) − lim
n→∞
µ(En+1).
Substituting (3) and (4) in (2), we have
µ(E1) − µ( lim
n→∞
En) = µ(E1) − lim
n→∞
µ(En+1).
Since µ(E1) < ∞, we have
µ( lim
n→∞
En) = lim
n→∞
µ(En). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

17
Problem 11 (Fatou’s lemma for µ)
Let (X, A, µ) be a measure space, and (En) be a sequence in A.
(a) Show that
µ
(
lim inf
n→∞
En
)
≤ lim inf
n→∞
µ(En).
(b) If there exists A ∈ A with En ⊂ A and µ(A) < ∞ for every n ∈ N, then
show that
µ
(
lim sup
n→∞
En
)
≥ lim sup
n→∞
µ(En).
Solution
(a) Recall that
lim inf
n→∞
En =
⋃
n∈N
⋂
k≥n
Ek = lim
n→∞
⋂
k≥n
Ek,
by the fact that
(⋂
k≥n Ek
)
n∈N is an increasing sequence in A. Then by Problem 9a
we have
(∗) µ
(
lim inf
n→∞
En
)
= lim
n→∞
µ
( ⋂
k≥n
Ek
)
= lim inf
n→∞
µ
( ⋂
k≥n
Ek
)
,
since the limit of a sequence, if it exists, is equal to the limit inferior of the sequence.
Since ⋂
k≥n Ek ⊂ En, we have µ
(⋂
k≥n Ek
)
≤ µ(En) for every n ∈N. This implies
that
lim inf
n→∞
µ
( ⋂
k≥n
Ek
)
≤ lim inf
n→∞
µ(En).
Thus by ( ∗) we obtain
µ
(
lim inf
n→∞
En
)
≤ lim inf
n→∞
µ(En).
(b) Now
lim sup
n→∞
En =
⋂
n∈N
⋃
k≥n
Ek = lim
n→∞
⋃
k≥n
Ek,
by the fact that
(⋃
k≥n Ek
)
n∈N is an decreasing sequence in A. Since En ⊂ A for all
n ∈N, we have ⋃
k≥n Ek ⊂ A for all n ∈N. Thus by Problem 9b we have
µ
(
lim sup
n→∞
En
)
= µ
(
lim
n→∞
⋃
k≥n
Ek
)
= lim
n→∞
µ
( ⋃
k≥n
Ek
)
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

18 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
Now
lim
n→∞
µ
( ⋃
k≥n
Ek
)
= lim sup
n→∞
µ
( ⋃
k≥n
Ek
)
,
since the limit of a sequence, if it exists, is equal to the limit superior of the sequence.
Then by ⋃
k≥n Ek ⊃ En we have
µ
( ⋃
k≥n
Ek
)
≥ µ(En).
Thus
lim sup
n→∞
µ
( ⋃
k≥n
Ek
)
≥ lim sup
n→∞
µ(En).
It follows that
µ
(
lim sup
n→∞
En
)
≥ lim sup
n→∞
µ(En). ■
Problem 12
Let µ∗ be an outer measure on a set X. Show that the following two conditions
are equivalent:
(i) µ∗ is additive on P(X).
(ii) Every element of P(X) is µ∗-measurable, that is, M(µ∗) = P(X).
Solution
• Suppose µ∗ is additive on P(X). Let E ∈ P (X). Then for any A ∈ P (X),
A = (A ∩ E) ∪ (A ∩ Ec) and ( A ∩ E) ∩ (A ∩ Ec) =∅.
By the additivity of µ∗ on P(X), we have
µ∗(A) = µ∗(A ∩ E) + µ∗(A ∩ Ec).
This show that E satisﬁes the Carath´ eodory condition. Hence E ∈ M (µ∗). So
P(X) ⊂ M(µ∗). But by deﬁnition, M(µ∗) ⊂ P (X). Thus
M(µ∗) = P(X).
• Conversely, suppose M(µ∗) = P(X). Since µ∗ is additive on M(µ∗) by Proposi-
tion 3, so µ∗ is additive on P(X). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

19
Problem 13
Let µ∗ be an outer measure on a set X.
(a) Show that the restriction µ of µ∗ on the σ-algebra M(µ∗) is a measure on
M(µ∗).
(b) Show that if µ∗ is additive on P(X), then it is countably additive on P(X).
Solution
(a) By deﬁnition, µ∗ is countably subadditive on P(X). Its restriction µ on M(µ∗)
is countably subadditive on M(µ∗). By Proposition 3b, µ∗ is additive on M(µ∗).
Therefore, by Problem 5, µ∗ is countably additive on M(µ∗). Thus, µ∗ is a measure
on M(µ∗). But µ is the restriction of µ∗ on M(µ∗), so we can say that µ is a
measure on M(µ∗).
(b) If µ∗ is additive on P(X), then by Problem 11, M(µ∗) = P(X). So µ∗ is a
measure on P(X) (Problem 5). In particular, µ∗ is countably additive on P(X). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

20 CHAPTER 1. MEASURE ON A σ-ALGEBRA OF SETS
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 2
Lebesgue Measure on R
1. Lebesgue outer measure on R
Deﬁnition 9 (Outer measure)
Lebesgue outer measure on R is a set function µ∗
L : P(R) → [0, ∞] deﬁned by
µ∗
L(A) = inf
{ ∞∑
k=1
𝓁(Ik) : A ⊂
∞⋃
k=1
Ik, I k is open interval in R
}
.
Proposition 4 (Properties of µ∗
L)
1. µ∗
L(A) = 0 if A is at most countable.
2. Monotonicity: A ⊂ B ⇒ µ∗
L(A) ≤ µ∗
L(B).
3. Translation invariant: µ∗
L(A + x) = µ∗
L(A), ∀x ∈R.
4. Countable subadditivity: µ∗
L (⋃∞
n=1 An) ≤ ∑∞
n=1 µ∗
L(An).
5. Null set: µ∗
L(A) = 0 ⇒ µ∗
L(A ∪ B) = µ∗
L(B) and µ∗
L(B \ A) = µ∗
L(B)
for all B ∈ P (R).
6. For any interval I ⊂R, µ ∗
L(I) = 𝓁(I).
7. Regularity:
∀E ∈ P (R), ε > 0, ∃O open set in R : O ⊃ E and µ∗
L(E) ≤ µ∗
L(O) ≤ µ∗
L(E) + ε.
2. Measurable sets and Lebesgue measure on R
Deﬁnition 10 (Carath´ eodory condition)
A set E ⊂R is said to be Lebesgue measurable (or µL-measurable, or measurable) if, for all A ⊂R,
we have
µ∗
L(A) = µ∗
L(A ∩ E) + µ∗
L(A ∩ Ec).
21
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

22 CHAPTER 2. LEBESGUE MEASURE ON R
Since µ∗
L is subadditive, the suﬃcient condition for Carath´ eodory condition is
µ∗
L(A) ≥ µ∗
L(A ∩ E) + µ∗
L(A ∩ Ec).
The family of all measurable sets is denoted by ML. We can see that ML is a σ-algebra. The
restriction of µ∗
L on ML is denoted by µL and is called Lebesgue measure.
Proposition 5 (Properties of µL)
1. (R, ML, µL) is a complete measure space.
2. (R, ML, µL) is σ-ﬁnite measure space.
3. BR ⊂ M L, that is, every Borel set is measurable.
4. µL(O) > 0 for every nonempty open set in R.
5. (R, ML, µL) is translation invariant.
6. (R, ML, µL) is positively homogeneous, that is,
µL(αE) = |α|µL(E), ∀α ∈R, E ∈ M L.
Note on Fσ and Gδ sets:
Let ( X, T ) be a topological space.
• A subset E of X is called a Fσ-set if it is the union of countably many closed sets.
• A subset E of X is called a Gδ-set if it is the intersection of countably many open sets.
• If E is a Gδ-set then Ec is a Fσ-set and vice versa. Every Gδ-set is Borel set, so is every Fσ-set.
∗ ∗ ∗∗
Problem 14
If E is a null set in (R, ML, µL), prove that Ec is dense in R.
Solution
For every open interval I in R, µ L(I) > 0 (property of Lebesgue measure). If
µL(E) = 0, then by the monotonicity of µL, E cannot contain any open interval as
a subset. This implies that
Ec ∩ I =∅
for any open interval I inR. Thus Ec is dense in R. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

23
Problem 15
Prove that for every E ⊂R, there exists a Gδ-set G ⊂R such that
G ⊃ E and µ∗
L(G) = µ∗
L(E).
Solution
We use the regularity property of µ∗
L (Property 7).
For ε = 1
n , n ∈N, there exists an open set On ⊂R such that
On ⊃ E and µ∗
L(E) ≤ µ∗
L(On) ≤ µ∗
L(E) + 1
n .
Let G = ⋂
n∈N On. Then G is a Gδ-set and G ⊃ E. Since G ⊂ On for every n ∈N,
we have
µ∗
L(E) ≤ µ∗
L(G) ≤ µ∗
L(On) ≤ µ∗
L(E) + 1
n .
This holds for every n ∈N, so we have
µ∗
L(E) ≤ µ∗
L(G) ≤ µ∗
L(E).
Therefore
µ∗(G) = µ∗(E). ■
Problem 16
Let E ⊂R. Prove that the following statements are equivalent:
(i) E is (Lebesgue) measurable.
(ii) For every ε > 0, there exists an open set O ⊃ E with µ∗
L(O \ E) ≤ ε.
(iii) There exists a Gδ-set G ⊃ E with µ∗
L(G \ E) = 0 .
Solution
• (i) ⇒ (ii) Suppose that E is measurable. Then
∀ε > 0, ∃ open set O : O ⊃ E and µ∗
L(E) ≤ µ∗
L(O) ≤ µ∗
L(E) + ε. (1)
Since E is measurable, with O as a testing set in the Carath´ eodory condition satisﬁed
by E, we have
µ∗
L(O) = µ∗
L(O ∩ E) + µ∗
L(O ∩ Ec) = µ∗
L(E) + µ∗
L(O \ E). (2)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

24 CHAPTER 2. LEBESGUE MEASURE ON R
If µ∗
L(E) < ∞, then from (1) and (2) we get
µ∗
L(O) ≤ µ∗
L(E) + ε =⇒ µ∗
L(O) − µ∗
L(E) = µ∗
L(O \ E) ≤ ε.
If µ∗
L(E) = ∞, let En = E ∩ (n − 1, n] for n ∈Z. Then ( En)n∈Z is a disjoint sequence
in ML with ⋃
n∈Z
En = E and µL(En) ≤ µL
(
(n − 1, n]
)
= 1.
Now, for every ε > 0, there is an open set On such that
On ⊃ En and µL(On \ En) ≤ 1
3 . ε
2|n| .
Let O = ⋃
n∈Z)On, then O is open and O ⊃ E, and
O \ E =
( ⋃
n∈Z
On
)
\
( ⋃
n∈Z
En
)
=
( ⋃
n∈Z
On
)
∩
( ⋃
n∈Z
En
)c
=
⋃
n∈Z
[
On ∩
( ⋃
n∈Z
En
)c]
=
⋃
n∈Z
[
On \
( ⋃
n∈Z
En
)]
⊂
⋃
n∈Z
(On \ En).
Then we have
µ∗
L(O \ E) ≤ µ∗
L
( ⋃
n∈Z
(On \ En)
)
≤
∑
n∈Z
µ∗
L(On \ E)
≤
∑
n∈Z
1
3 . ε
2|n| = 1
3 ε + 2
∑
n∈N
1
3 . ε
2n
= 1
3 ε + 2
3 ε = ε.
This shows that ( ii) satisﬁes.
• (ii) ⇒ (iii) Assume that E satisﬁes ( ii). Then for ε = 1
n , n ∈N, there is an open
set On such that
On ⊃ En and µL(On \ En) ≤ 1
n , ∀n ∈N.
Let G = ⋂
n∈N On. Then G is a Gδ-set containing E. Now
G ⊂ O =⇒ µ∗
L(G \ E) ≤ µ∗
L(On \ E) ≤ 1
n , ∀n ∈N.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

25
Thus µ∗
L(G \ E) = 0. This shows that E satisﬁes ( iii).
• (iii) ⇒ (i) Assume that E satisﬁes ( iii). Then there exists a Gδ-set G such that
G ⊃ E and µ∗
L(G \ E) = 0 .
Now µ∗
L(G \ E) = 0 implies that G \ E is (Lebesgue) measurable. Since E ⊂ G,
we can write E = G \ (G \ E). Then the fact that G and G \ E are (Lebesgue)
measurable implies that E is (Lebesgue) measurable . ■
Problem 17 (Similar problem)
Let E ⊂R. Prove that the following statements are equivalent:
(i) E is (Lebesgue) measurable.
(ii) For every ε > 0, there exists an closed set C ⊂ E with µ∗
L(E \ C) ≤ ε.
(iii) There exists a Fσ-set F ⊂ E with µ∗
L(E \ F ) = 0 .
Problem 18
LetQ be the set of all rational numbers in R. For any ε > 0, construct an open
set O ⊂R such that
O ⊃Q and µ∗
L(O) ≤ ε.
Solution
SinceQ is countable, we can write Q = {r1, r2, ...}. For any ε > 0, let
In =
(
rn − ε
2n+1 , rn + ε
2n+1
)
, n ∈N.
Then In is open and O = ⋃∞
n=1 In is also open. We have, for every n ∈N, r n ∈ In.
Therefore O ⊃Q.
Moreover,
µ∗
L(O) = µ∗
L
( ∞⋃
n=1
In
)
≤
∞∑
n=1
µ∗
L(In)
=
∞∑
n=1
2ε
2n+1
= ε
∞∑
n=1
1
2n = ε. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

26 CHAPTER 2. LEBESGUE MEASURE ON R
Problem 19
LetQ be the set of all rational numbers in R.
(a) Show that Q is a null set in (R, BR, µL).
(b) Show that Q is a Fσ-set.
(c) Show that there exists a Gδ-set G such that G ⊃Q and µL(G) = 0 .
(d) Show that the set of all irrational numbers in R is a Gδ-set.
Solution
(a) Since Q is countable, we can write Q = {r1, r2, ...}. Each {rn}, n ∈N is closed,
so {rn} ∈ BR. Since BR is a σ-algebra,
Q =
∞⋃
n=1
{rn} ∈ BR.
Since µL({rn}) = 0, we have
µL(Q) =
∞∑
n=1
µL({rn}) = 0 .
Thus,Q is a null set in ( R, BR, µL).
(b) Since {rn} is closed and Q = ⋃∞
n=1{rn}, Q is a Fσ-set.
(c) By (a), µL(Q) = 0. This implies that, for every n ∈N, there exists an open set
Gn such that
Gn ⊃Q and µL(Gn) < 1
n .
If G = ⋂∞
n=1 Gn then G is a Gδ-set and G ⊃Q. Furthermore,
µL(G) ≤ µL(Gn) < 1
n , ∀n ∈N.
This implies that µL(G) = 0.
(d) By (b), Q is a Fσ-set, so R \Q, the set of all irrational numbers in R, is a
Gδ-set. ■
Problem 20
Let E ∈ M L with µL(E) > 0. Prove that for every α ∈ (0, 1), there exists a
ﬁnite open interval I such that
αµL(I) ≤ µL(E ∩ I) ≤ µL(I).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

27
Solution
• Consider ﬁrst the case where 0 < µ L(E) < ∞. For any α ∈ (0, 1), set 1
α = 1 + a.
Since a > 0, 0 < ε = aµL(E) < ∞. By the regularity property of µ∗
L (Property 7),
there exists an open set O ⊃ E such that 1
µL(O) ≤ µL(E) + aµL(E) = (1 + a)µL(E) = 1
α µL(E) < ∞. (i)
Now since O is an open set in R, it is union of a disjoint sequence ( In) of open
intervals inR:
O =
⋃
n∈N
In =⇒ µL(O) =
∑
n∈N
µL(In). (ii)
Since E ⊂ O, we have
µL(E) = µL(E ∩ O) = µL
(
E ∩
⋃
n∈N
In
)
=
∑
n∈N
µL(E ∩ In). (iii)
From (i), (ii) and ( iii) it follows that
∑
n∈N
µL(In) ≤ 1
α
∑
n∈N
µL(E ∩ In).
Note that all terms in this inequality are positive, so that there exists at least one
n0 ∈N such that
µL(In0) ≤ 1
α µL(E ∩ In0).
Since µL(O) is ﬁnite, all intervals In are ﬁnite intervals in R. Let I := In0, then I is
a ﬁnite open interval satisfying conditions:
αµL(I) ≤ µL(E ∩ I) ≤ µL(I).
• Now consider that case µL(E) = ∞. By the σ-ﬁniteness of the Lebesgue measure
space, there exists a measurable subset E0 of E such that 0 < µ L(E0) < ∞. Then
using the ﬁrst part of the solution, we obtain
αµL(I) ≤ µL(E0 ∩ I) ≤ µL(E ∩ I) ≤ µL(I). ■
1Recall that for (Lebesgue) measurable set A, µ ∗
L(A) = µL(A).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

28 CHAPTER 2. LEBESGUE MEASURE ON R
Problem 21
Let f be a real-valued function on (a, b) such that f ′ exists and satisﬁes
|f ′(x)| ≤ M for all x ∈ (a, b) and for some M ≥ 0.
Show that for every E ⊂ (a, b) we have
µ∗
L(f (E)) ≤ M µ∗
L(E).
Solution
If M = 0 then f ′(x) = 0 , ∀x ∈ (a, b). Hence, f (x) = y0, ∀x ∈ (a, b). Thus, for any
E ⊂ (a, b) we have
µ∗
L(f (E)) = 0 .
The inequality holds. Suppose M > 0. For all x, y ∈ (a, b), by the Mean Value
Theorem, we have
|f (x) − f (y)| = |x − y||f ′(c)|, for some c ∈ (a, b)
≤ M |x − y|. (∗)
By deﬁnition of the outer measure, for any E ⊂ (a, b) we have
µ∗
L(E) = inf
∞∑
n=1
(bn − an),
where {In = (an, bn), n ∈N} is a covering class of E. By (*) we have
∞∑
n=1
|f (bn) − f (an)| ≤ M
∞∑
n=1
|bn − an|
≤ M inf
∞∑
n=1
|bn − an|
≤ M µ∗
L(E).
Inﬁmum takes over all covering classes of E. Thus,
µ∗
L(f (E)) = inf
∞∑
n=1
|f (bn) − f (an)| ≤ M µ∗
L(E). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

29
Problem 22
(a) Let E ⊂R. Show that F = {∅, E, Ec,R} is the σ-algebra of subsets of R
generated by {E}
(b) If S and T are collections of subsets of R, then
σ(S ∪ T ) = σ(S) ∪ σ(T ).
Is the statement true? Why?
Solution
(a)It is easy to check that F is a σ-algebra.
Note ﬁrst that {E} ⊂ F . Hence
σ({E}) ⊂ F . (i)
On the other hand, since σ({E}) is a σ-algebra, so ∅,R ∈ σ({E}). Also, since
E ∈ σ({E}), so Ec ∈ σ({E}). Hence
F ⊂ σ({E}). (ii)
From (i) and ( ii) it follows that
F = σ({E}).
(b) No. Here is why.
Take S = {(, 1]} and T = {(1, 2]}. Then, by part (a),
σ(S) = {∅, (0, 1], (0, 1]c,R} and σ(T ) = {∅, (1, 2], (1, 2]c,R}.
Therefore
σ(S) ∪ σ(T ) = {∅, (0, 1], (0, 1]c, (1, 2], (1, 2]c,R}.
We have
(0, 1] ∪ (1, 2] = (0 , 2] /∈ σ(S) ∪ σ(T ).
Hence σ(S) ∪ σ(T ) is not a σ-algebra. But, by deﬁnition, σ(S ∪ T ) is a σ-algebra.
And hence it cannot be equal to σ(S) ∪ σ(T ). ■
Problem 23
Consider F = {E ∈R : either E is countable or Ec is countable }.
(a) Show that F is a σ-algebra and F is a proper sub- σ-algebra of the σ-algebra
BR.
(b) Show that F is the σ-algebra generated by
{
{x} : x ∈R
}
.
(c) Find a measure λ : F → [0, ∞] such that the only λ-null set is ∅.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

30 CHAPTER 2. LEBESGUE MEASURE ON R
Solution
(a) We check conditions of a σ-algebra:
• It is clear that ∅ is countable, so ∅ ∈ F .
• Suppose E ∈ F . Then E ⊂R and E is countable or Ec is countable. This is
equivalent to Ec ⊂R and Ec is countable or E is countable. Thus,
E ∈ F ⇒ Ec ∈ F .
• Suppose E1, E2, ... ∈ F . Either all En’s are countable, so ⋃∞
n=1 En is countable.
Hence ⋃∞
n=1 En ∈ F . Or there exists some En0 ∈ F which is not countable. By
deﬁnition, Ec
n0 must be countable. Now
( ∞⋃
n=1
En
)c
=
∞⋂
n=1
Ec
n ⊂ En0.
This implies that ( ⋃∞
n=1 En)c is countable. Thus
∞⋃
n=1
En ∈ F .
Finally, F is a σ-algebra. □
Recall that BR is the σ-algebra generated by the family of open sets in R. It is also
generated by the family of closed sets in R. Now suppose E ∈ F . If E is countable
then we can write
E = {x1, x2, ...} =
∞⋃
n=1
{xn}.
Each {xn} is a closed set in R, so belongs to BR. Hence E ∈ BR. Therefore,
F ⊂ BR.
F is a proper subset of BR. Indeed, [0 , 1] ∈ BR and [0 , 1] /∈ F . □
(b) Let S =
{
{x} : x ∈R
}
. Clearly, S ⊂ F , and so
σ(S) ⊂ F .
Now take E ∈ F and E ⁄=∅. If E is countable then we can write
E =
∞⋃
n=1
{xn}| {z }
∈S
∈ σ(S).
Hence
F ⊂ σ(S).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

31
Thus
σ(S) = F .
(c) Deﬁne the set function λ : F → [0, ∞] by
λ(E) =
{
|E| if E is ﬁnite
∞ otherwise.
We can check that λ is a measure. If E ⁄=∅ then λ(E) > 0 for every E ∈ F . ■
Problem 24
For E ∈ ML with µL(E) < ∞, deﬁne a real-valued function ϕE onR by setting
ϕE(x) := µL(E ∩ (−∞, x]) for x ∈R.
(a) Show that ϕE is an increasing function on R.
(b) Show that ϕE satisﬁes the Lipschitz condition on R, that is,
|ϕE(x′) − ϕE(x′′)| ≤ | x′ − x′′| for x′, x′′ ∈R.
Solution
(a) Let x, y ∈ R. Suppose x < y . It is clear that ( −∞, x] ⊂ (−∞, y]. Hence,
E ∩ (−∞, x] ⊂ E ∩ (−∞, y] for E ∈ ML. By the monoticity of µL we have
ϕE(x) = µL(E ∩ (−∞, x]) ≤ µL(E ∩ (−∞, y]) = ϕE(y).
Thus ϕE is increasing on R.
(b) Suppose x′ < x ′′ we have
E ∩ (x′, x′′] = ( E ∩ (−∞, x′′]) \ (E ∩ (−∞, x′]).
It follows that
ϕE(x′′) − ϕE(x′) = µL(E ∩ (−∞, x′′]) − µL(E ∩ (−∞, x′])
= µL(E ∩ (x′, x′′])
≤ µL
(
(x′, x′′]
)
= x′′ − x′. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

32 CHAPTER 2. LEBESGUE MEASURE ON R
Problem 25
Let E be a Lebesgue measurable subset of R with µL(E) = 1 . Show that there
exists a Lebesgue measurable set A ⊂ E such that µL(A) = 1
2 .
Solution
Deﬁne the function f :R → [0, 1] by
f (x) = µL
(
E ∩ (−∞, x]
)
, x ∈R.
By Problem 23, we have
|f (x) − f (y)| ≤ | x − y|, ∀x, y ∈R.
Hence f is (uniformly) continuous on R. Since
lim
x→−∞
f (x) = 0 and lim
x→∞
f (x) = 1 ,
by the Mean Value Theorem, we have
∃x0 ∈R such that f (x0) = 1
2 .
Set A = E ∩ (−∞, x0]. Then we have
A ⊂ E and µL(A) = 1
2 . ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 3
Measurable Functions
Remark:
From now on, measurable means Lebesgue measurable. Also measure means Lebesgue measure,
and we write µ instead of µL for Lebesgue measure.
1. Deﬁnition, basic properties
Proposition 6 (Equivalent conditions)
Let f be an extended real-valued function whose domain D is measurable. Then the following
statements are equivalent:
1. For each real number a, the set {x ∈ D : f (x) > a} is measurable.
2. For each real number a, the set {x ∈ D : f (x) ≥ a} is measurable.
3. For each real number a, the set {x ∈ D : f (x) < a} is measurable.
4. For each real number a, the set {x ∈ D : f (x) ≤ a} is measurable.
Deﬁnition 11 (Measurable function)
An extended real-valued function f is said to be measurable if its domain is measurable and if it
satisﬁes one of the four statements of Proposition 6.
Proposition 7 (Operations)
Let f, g be two measurable real-valued functions deﬁned on the same domain and c a constant.
Then the functions f + c, cf, f + g, and f g are also measurable.
Note:
A function f is said to be Borel measurable if for each α ∈R the set {x : f (x) > α} is a Borel set.
Every Borel measurable function is Lebesgue measurable.
2. Equality almost everywhere
• A property is said to hold almost everywhere (abbreviated a.e.) if the set of points where it fails
to hold is a set of measure zero.
• We say that f = g a.e. if f and g have the same domain and µ
(
{x ∈ D : f (x) ⁄= g(x)}
)
= 0.
Also we say that the sequence ( fn) converges to f a.e. if the set {x : fn(x)↛ f (x)} is a null set.
33
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

34 CHAPTER 3. MEASURABLE FUNCTIONS
Proposition 8 (Measurable functions)
If a function f is measurable and f = g a.e., then g is measurable.
3. Sequence of measurable functions
Proposition 9 (Monotone sequence)
Let (fn) be a monotone sequence of extended real-valued measurable functions on the same mea-
surable domain D. Then limn→∞ fn exists on D and is measurable.
Proposition 10 Let (fn) be a sequence of extended real-valued measurable functions on the same
measurable domain D. Then max{f1, ..., fn}, min{f1, ..., fn}, lim supn→∞ fn, lim infn→∞ fn, supn∈N, inf n∈N
are all measurable.
Proposition 11 If f is continuous a.e. on a measurable set D, then f is measurable.
∗ ∗ ∗∗
Problem 26
Let D be a dense set in R. Let f be an extended real-valued function on R such
that {x : f (x) > α} is measurable for each α ∈ D. Show that f is measurable.
Solution
Let β be an arbitrary real number. For each n ∈N, there exists αn ∈ D such that
β < α n < β + 1
n by the density of D. Now
{x : f (x) > β } =
∞⋃
n=1
{
x : f (x) ≥ β + 1
n
}
=
∞⋃
n=1
{x : f (x) > α n}.
Since ⋃∞
n=1{x : f (x) > α n} is measurable (as countable union of measurable sets),
{x : f (x) > β } is measurable. Thus, f is measurable. ■
Problem 27
Let f be an extended real-valued measurable function on R. Prove that {x :
f (x) = α} is measurable for any α ∈R.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

35
Solution
• For α ∈R, we have
{x : f (x) = α} = {x : f (x) ≤ α}| {z }
measurable
\ {x : f (x) < α}| {z }
measurable
.
Thus {x : f (x) = α} is measurable.
• For α = ∞, we have
{x : f (x) = ∞} =R \ {x : f (x) < ∞} =R \
⋃
n∈N
{x : f (x) ≤ n}| {z }
measurable
.
Thus {x : f (x) = ∞} is measurable.
• For α = −∞, we have
{x : f (x) = −∞} =R \ {x : f (x) > −∞} =R \
⋃
n∈N
{x : f (x) ≥ −n}| {z }
measurable
.
Thus {x : f (x) = ∞} is measurable. ■
Problem 28
(a). Let D and E be measurable sets and f a function with domain D ∪ E. Show
that f is measurable if and only if its restriction to D and E are measurable.
(b). Let f be a function with measurable domain D. Show that f is measurable
if and only if the function g deﬁned by
g(x) =
{
f (x) for x ∈ D
0 for x /∈ D
is measurable.
Solution
(a) Suppose that f is measurable. Since D and E are measurable subsets of D ∪ E,
the restrictions f |D and f |E are measurable.
Conversely, suppose f |D and f |E are measurable. For any α ∈R, we have
{x : f (x) > α} = {x ∈ D : f |D(x) > α} ∪ {x ∈ E : f |E(x) > α}.
Each set on the right hand side is measurable, so {x : f (x) > α } is measurable.
Thus, f is measurable.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

36 CHAPTER 3. MEASURABLE FUNCTIONS
(b) Suppose that f is measurable. If α ≥ 0, then {x : g(x) > α} = {x : f (x) > α},
which is measurable. If α < 0, then {x : g(x) > α } = {x : f (x) > α } ∪ Dc, which
is measurable. Hence, g is measurable.
Conversely, suppose that g is measurable. Since f = g|D and D is measurable, f is
measurable. ■
Problem 29
Let f be measurable and B a Borel set. Then f −1(B) is a measurable set.
Solution
Let C be the collection of all sets E such that f −1(E) is measurable. We show that
C is a σ-algebra. Suppose E ∈ C . Since
f −1(Ec) =
(
f −1(E)
)c
,
which is measurable, so Ec ∈ C . Suppose ( En) is a sequence of sets in C. Since
f −1
(⋃
n
En
)
=
⋃
n
f −1(En),
which is measurable, so ⋃
n En ∈ C . Thus, C is a σ-algebra.
Next, we show that all intervals ( a, b), for any extended real numbers a, b with
a < b , belong to C. Since f is measurable, {x : f (x) > a } and {x : f (x) < b } are
measurable. It follows that ( a, ∞) and ( −∞, b) ∈ C . Furtheremore, we have
(a, b) = ( −∞, b) ∩ (a, ∞),
so ( a, b) ∈ C . Thus, C is a σ-algebra containing all open intervals, so it contains all
Borel sets. Hence f −1(B) is measurable. ■
Problem 30
Show that if f is measurable real-valued function and g a continuous function
deﬁned on R, then g ◦ f is measurable.
Solution
For any α ∈R,
{x : ( g ◦ f )(x) > α} = (g ◦ f )−1((α, ∞)) = f −1
(
g−1(
(α, ∞)
))
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

37
By the continuity of g, g −1(
(α, ∞)
)
is an open set, so a Borel set. By Problem 24,
the last set is measurable. Thus, g ◦ f is measurable. □
Problem 31
Let f be an extended real-valued function deﬁned on a measurable set D ⊂R.
(a) Show that if {x ∈ D : f (x) < r } is measurable in R for every r ∈Q, then
f is measurable on D.
(b) What subsets of R other than Q have this property?
(c) Show that if f is measurable on D, then there exists a countable sub-collection
C ⊂ M L, depending on f , such that f is σ(C)-measurable on D.
(Note: σ(C) is the σ-algebra generated by C.)
Solution
(a) To show that f is measurable on D, we show that {x ∈ D : f (x) < a } is
measurable for every a ∈R. Let I = {r ∈Q : r < a }. Then I is countable , and
we have
{x ∈ D : f (x) < a} =
⋃
r∈I
{x ∈ D : f (x) < r }.
Since {x ∈ D : f (x) < r } is measurable, ⋃
r∈I{x ∈ D : f (x) < r } is measurable.
Thus, {x ∈ D : f (x) < a} is measurable.
(b) Here is the answer to the question:
Claim 1 : If E ⊂ R is dense in R, then E has the property in (a), that is, if
{x ∈ D : f (x) < r } is measurable for every r ∈ E then f is measurable on D.
Proof.
Given any a ∈R, the interval ( a − 1, a) intersects E since E is dense. Pick some
r1 ∈ E ∩ (a − 1, a). Now the interval ( r1, a) intersects E for the same reason. Pick
some r2 ∈ E ∩ (r1, a). Repeating this process, we obtain an increasing sequence ( rn)
in E which converges to a.
By assumption, {x ∈ D : f (x) < r n} is measurable, so we have
{x ∈ D : f (x) < a} =
⋃
n∈N
{x ∈ D : f (x) < r n} is measurable .
Thus, f is measurable on D.
Claim 2 : If E ⊂R is not dense in R, then E does not have the property in (a).
Proof.
Since E is not dense in R, there exists an interval [ a, b] ⊂ E. Let F be a non
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

38 CHAPTER 3. MEASURABLE FUNCTIONS
measurable set in R. We deﬁne a function f as follows:
f (x) =
{
a if x ∈ F c
b if x ∈ F .
For r ∈ E, by deﬁnition of F , we observe that
• If r < a then f −1([−∞, r)) = ∅.
• If r > b then f −1([−∞, r)) =R.
• If r = a+b
2 then f −1([−∞, r)) = F c.
Since F is non measurable, F c is also non measurable. Through the above observa-
tion, we see that
{
x ∈ D : f (x) < a + b
2
}
non measurable .
Thus, f is not measurable.
Conclusion : Only subsets of R which are dense in R have the property in (a).
(c) Let C = {Cr}r∈Q where Cr = {x ∈ D : f (x) < r } for every r ∈Q. Clearly, C is
a countable family of subsets of R. Since f is measurable, Cr is measurable. Hence,
C ⊂ M L. Since ML is a σ-algebra, by deﬁnition, we must have σ(C) ⊂ M L. Let
a ∈R. Then
{x ∈ D : f (x) < a} =
⋃
r<a
{x ∈ D : f (x) < r } =
⋃
r<a
Cr.
It follows that {x ∈ D : f (x) < a} ∈ σ(C).
Thus, f is σ(C)-measurable on D. ■
Problem 32
Show that the following functions deﬁned on R are all Borel measurable, and
hence Lebesgue measurable also on R:
(a) f (x) =
{
0 if x is rational
1 if x is irrational . (b) g(x) =
{
x if x is rational
−x if x is irrational .
(c) h(x) =
{
sin x if x is rational
cos x if x is irrational .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

39
Solution
(a) For any a ∈R, let E = {x ∈ D : f (x) < a}.
• If a > 1 then E =R, so E ∈ BR (Borel measurable).
• If 0 < a ≤ 1 then E =Q, so E ∈ BR (Borel measurable).
• If a ≤ 0 then E =∅, so E ∈ BR (Borel measurable).
Thus, f is Borel measurable.
(b) Consider g1 deﬁned on Q by g1(x) = x, then g|Q = g1. Consider g2 deﬁned on
R\Q by g(x) = −x, then g|R\Q = g2. Notice that R, R\Q ∈ BR (Borel measurable).
For any a ∈R, we have
{x ∈ D : f1(x) < a} = [−∞, a) ∩Q ∈ BR (Borel measurable) ,
and
{x ∈ D : f2(x) < a} = [−∞, a) ∩ (R \Q) ∈ BR (Borel measurable) .
Thus, g is Borel measurable.
(c) Use the same way as in (b). ■
Problem 33
Let f be a real-valued increasing function on R. Show that f is Borel measurable,
and hence Lebesgue measurable also on R.
Solution
For any a ∈R, let E = {x ∈ D : f (x) ≥ a}. Let α = inf E. Since f is increasing,
• if Im( f ) ⊂ (−∞, a) then E =∅.
• if Im( f )⊈ (−∞, a) then E is either ( α, ∞) or [ α, ∞).
Since∅, (α, ∞), [α, ∞) are Borel sets, so f is Borel measurable. ■
Problem 34
If (fn) is a sequence of measurable functions on D ⊂R, then show that
{x ∈ D : lim
n→∞
fn(x) exists} is measurable.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

40 CHAPTER 3. MEASURABLE FUNCTIONS
Solution
Recall that if fn’s are measurable, then lim sup n→∞ fn, lim infn→∞ fn and g(x) =
lim supn→∞ fn − lim infn→∞ fn are also measurable, and if h is measurable then
{x ∈ D : h(x) = α} is measurable (Problem 22).
Now we have
E = {x ∈ D : lim
n→∞
fn(x) exists } = {x ∈ D : g(x) = 0 }.
Thus, E is measurable. ■
Problem 35
(a) If g : R → R is continuous and f : R → R is measurable then g ◦ f is
measurable.
(b) If f is measurable then |f | is measurable. Does the converse hold?
Solution
(a) For any a ∈R, then
E = {x : ( g ◦ f )(x) < a} = ( g ◦ f )−1(−∞, a)
= f −1 (
g−1(−∞, a)
)
.
Since g is continuous, g−1(−∞, a) is open. Then there is a family of open disjoint
intervals {In}n∈N such that g−1(−∞, a) = ⋃
n∈N In. Hence,
E = f −1
( ⋃
n∈N
In
)
=
⋃
n∈N
f −1(In).
Since f is measurable, f −1(In) is measurable. Hence E is measurable. This tells us
that g ◦ f is measurable.
(b) If g(u) = |u| then g is continuous. We have
(g ◦ f )(x) = g(f (x)) = |f (x)|.
By part (a), g ◦ f = |f | is measurable.
The converse is not true.
Let E be a non-measurable subset of R. Consider the function:
f (x) =
{
1 if x ∈ E
−1 if x /∈ E.
Then f −1( 1
2 , ∞) = E, which is not measurable. Since ( 1
2 , ∞) is open, so f is not
measurable, while |f | = 1 is measurable. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

41
Problem 36
Let (fn : n ∈ N) and f be an extended real-valued measurable functions on a
measurable set D ⊂R such that limn→∞ fn = f on D. Then for every α ∈R
prove that:
(i) µ{x ∈ D : f (x) > α} ≤ lim inf
n→∞
µ{x ∈ D : fn(x) ≥ α}
(ii) µ{x ∈ D : f (x) < α} ≤ lim inf
n→∞
µ{x ∈ D : fn(x) ≤ α}.
Solution
Recall that, for any sequence ( En)n∈N of measurable sets,
µ(lim inf
n→∞
En) ≤ lim inf
n→∞
µ(En), (∗)
lim inf
n→∞
En =
⋃
n∈N
⋂
k≥n
Ek = lim
n→∞
⋂
k≥n
Ek.
Now for every α ∈R, let Ek = {x ∈ D : fk(x) ≥ α} for each k ∈N. Then
lim inf
n→∞
En = lim
n→∞
⋂
k≥n
Ek
= lim
n→∞
⋂
k≥n
{x ∈ D : fk(x) ≥ α}
= {x ∈ D : f (x) > α} since fk(x) → f (x) on D.
Using (*) we get
µ{x ∈ D : f (x) > α} ≤ lim inf
n→∞
µ{x ∈ D : fn ≥ α}.
For the second inequality, we use the similar argument.
Let Fk = {x ∈ D : fk(x) ≤ α} for each k ∈N. Then
lim inf
n→∞
En = lim
n→∞
⋂
k≥n
Fk
= lim
n→∞
⋂
k≥n
{x ∈ D : fk(x) ≤ α}
= {x ∈ D : f (x) < α} since fk(x) → f (x) on D.
Using (*) we get
µ{x ∈ D : f (x) < α} ≤ lim inf
n→∞
µ{x ∈ D : fn ≤ α}. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

42 CHAPTER 3. MEASURABLE FUNCTIONS
Simple functions
Deﬁnition 12 (Simple function)
A function ϕ : X →R is simple if it takes only a ﬁnite number of diﬀerent values.
Deﬁnition 13 (Canonical representation )
Let ϕ be a simple function on X. Let {a1, ..., an} the set of distinct valued assumed
by ϕ on D. Let Di = {x ∈ X : ϕ(x) = ai} for i = 1, ..., n. Then the expression
ϕ =
n∑
i=1
aiχDi
is called the canonical representation of ϕ.
It is evident that Di ∩ Dj =∅ for i ⁄= j and ⋃n
i=1 Di = X.
∗ ∗ ∗∗
Problem 37
(a). Show that
χA∩B = χA · χB
χA∪B = χA + χB − χA · χB
χAc = 1 − χA.
(b). Show that the sum and product of two simple functions are simple functions.
Solution
(a). We have
χA∩B(x) = 1 ⇐ ⇒ x ∈ A and x ∈ B
⇐ ⇒ χA(x) = 1 = χB(x).
Thus,
χA∩B = χA · χB.
We have
χA∪B(x) = 1 ⇐ ⇒x ∈ A ∪ B.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

43
If x ∈ A ∩ B then χA(x) + χB(x) − χA(x) · χB(x) = 1 + 1 − 1 = 1.
If x /∈ A ∩ B, then x ∈ A \ B or x ∈ B \ A. Then χA(x) + χB(x) = 1 and
χA · χBχA(x) + χB(x) = 0.
Also,
χA∪B(x) = 0 ⇐ ⇒x /∈ A ∪ B.
Then
χA(x) = χB(x) = χA(x) · χB(x) = 0 .
Thus,
χA∪B = χA + χB − χA · χB.
If χAc(x) = 1, then x /∈ A, so χA(x) = 0.
If χAc(x) = 0, then x ∈ A, so χA(x) = 1. Thus,
χAc = 1 − χA. □
(b). Let ϕ be a simple function having values a1, ..., an. Then
ϕ =
n∑
i=1
aiχAi where Ai = {x : ϕ(x) = ai}.
Similarly, if ψ is a simple function having values b1, ..., bm. Then
ψ =
m∑
j=1
bjχBj where Bj = {x : ψ(x) = bj}.
Deﬁne Cij := Ai ∩ Bj. Then
Ai ⊂ X =
m⋃
j=1
Bj and so Ai = Ai ∩
m⋃
j=1
Bj =
m⋃
j=1
Cij.
Similarly, we have
Bj =
n⋃
i=1
Cij.
Since the Cij’s are disjoint, this means that (see part (a))
χAi =
m∑
j=1
χCij and χBj =
n∑
i=1
χCij .
Thus
ϕ =
n∑
i=1
m∑
j=1
aiχCij and ψ =
n∑
i=1
m∑
j=1
bjχCij .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

44 CHAPTER 3. MEASURABLE FUNCTIONS
Hence
ϕ + ψ =
n∑
i=1
m∑
j=1
(ai + bj)χCij and ϕψ =
n∑
i=1
m∑
j=1
aibjχCij .
They are simple function. ■
Problem 38
Let ϕ :R →R be a simple function deﬁned by
n∑
i=1
aiχAi where Ai = {x ∈R : ϕ(x) = ai}.
Prove that ϕ is measurable if and only if all the Ai’s are measurable.
Solution
Assume that Ai is measurable for all i = 1, ..., n. Then for any c ∈R, we have
{x : ϕ(x) > c} =
⋃
ai>c
Ai.
Since every Ai is measurable, ⋃
ai>c Ai is measurable. Thus {x : ϕ(x) > c } is
measurable. By deﬁnition, ϕ is measurable.
Conversely, suppose ϕ is measurable. We can suppose a1 < a 2 < ... < a n. Given
j ∈ {1, 2, ..., n}, choose c1 and c2 such that aj−1 < c 1 < a j < c 2 < a j+1. (If j = 1 or
j = n, part of this requirement is empty.) Then
Aj =
( ⋃
ai>c1
Ai
)
\
( ⋃
ai>c2
Ai
)
= {x : ϕ(x) > c 1}| {z }
measurable
\ {x : ϕ(x) > c 2}| {z }
measurable
.
Thus, Aj is measurable for all j ∈ {1, 2, ..., n}. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 4
Convergence a.e. and Convergence
in Measure
1. Convergence almost everywhere
Deﬁnition 14 Let (fn) be a sequence extended real-valued measurable functions on a measurable
set D ⊂R.
1. We say that limn→∞ fn exists a.e. on D if there exists a null set N such that N ⊂ D and
limn→∞ fn(x) exists for every x ∈ D \ N .
2. We say that (fn) converges a.e. on D if limn→∞ fn(x) exists and limn→∞ fn(x) ∈R for every
x ∈ D \ N .
Proposition 12 (Uniqueness)
Let (fn) be a sequence extended real-valued measurable functions on a measurable set D ⊂R. Let
g1 and g2 be two extended real-valued measurable functions on D. Then
[
lim
n→∞
fn = g1 a.e. on D and lim
n→∞
fn = g2 a.e. on D
]
=⇒ g1 = g2 a.e. on D.
Theorem 1 (Borel-Cantelli Lemma)
For any sequence (An) of measurable subsets in R, we have
∑
n∈N
µ(An) < ∞ =⇒ µ
(
lim sup
n→∞
An
)
= 0.
Deﬁnition 15 (Almost uniform convergence)
Let (fn) be a sequence extended real-valued measurable functions on a measurable set D ⊂R and
f a real-valued measurable functions on D. We say that (fn) converges a.u. on D to f if for every
η > 0 there exists a measurable set E ⊂ D such that µ(E) < η and (fn) converges uniformly to f
on D \ E.
Theorem 2 (Egoroﬀ )
Let D be a measurable set with µ(D) < ∞. Let (fn) be a sequence extended real-valued measurable
functions on D and f a real-valued measurable functions on D. If (fn) converges to f a.e. on D,
then (fn) converges to f a.u. on D.
45
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

46 CHAPTER 4. CONVERGENCE A.E. AND CONVERGENCE IN MEASURE
2. Convergence in measure
Deﬁnition 16 Let (fn) be a sequence extended real-valued measurable functions on a measurable
set D ⊂R. We say that (fn) converges in measure µ on D if there exists a real-valued measurable
function f on D such that for every ε > 0 we have
lim
n→∞
µ{D : |fn − f | ≥ ε} := lim
n→∞
µ{x ∈ D : |fn(x) − f (x)| ≥ ε} = 0.
That is,
∀ε > 0, ∀η > 0, ∃N (ε, η) ∈N : µ{D : |fn − f | ≥ ε} < η for n ≥ N (ε, η).
We write fn
µ
− →f on D for this convergence.
Proposition 13 (Uniqueness)
Let (fn) be a sequence extended real-valued measurable functions on a measurable set D ⊂R. Let
f and g be two real-valued measurable functions on D. Then
[fn
µ
− →f on D and fn
µ
− →g on D] =⇒ f = g a.e. on D.
Proposition 14 (Equivalent conditions)
(1) [ fn
µ
− →f on D] ⇐ ⇒ ∀ε > 0, ∃N (ε) ∈N : µ{D : |fn − f | ≥ ε} < ε for n ≥ N (ε).
(2) [ fn
µ
− →f on D] ⇐ ⇒ ∀m ∈N, ∃N (m) : µ
{
D : |fn − f | ≥ 1
m
}
< 1
m for m ≥ N (m).
3. Convergence a.e. and convergence in measure
Theorem 3 (Lebesgue)
Let (fn) be a sequence extended real-valued measurable functions on a measurable set D ⊂R. Let
f be a real-valued measurable functions on D. Suppose
1. fn → f a.e. on D,
2. µ(D) < ∞.
Then fn
µ
− →f on D.
Theorem 4 (Riesz)
Let (fn) be a sequence extended real-valued measurable functions on a measurable set D ⊂R. Let
f be a real-valued measurable functions on D. If fn
µ
− →f on D, then there exists a subsequence
(fnk ) which converges to f a.e. on D.
∗ ∗ ∗∗
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

47
Problem 39 (An exercise to warn up.)
1. Consider the sequence (fn) deﬁned on R by fn = χ[n,n+1], n ∈ N and the
function f ≡ 0. Does (fn) converge to f a.e.? a.u.? in measure?
2. Same questions with fn = nχ[0, 1
n ].
(Note: χA is the characteristic function of the set A. Try to write your solution.)
Problem 40
Let (fn) be a sequence of extended real-valued measurable functions on X and
let f be an extended real-valued function which is ﬁnite a.e. on X. Suppose
limn→∞ fn = f a.e. on X. Let α ∈ [0, µ(X)) be arbitrarily chosen. Show that
for every ε > 0 there exists N ∈ N such that µ{X : |fn − f | < ε } ≥ α for
n ≥ N .
Solution
Let Z be a null set such that f is ﬁnite on X \ Z. Since fn → f a.e. on X, fn → f
a.e. on X \ Z. For every ε > 0 we have 1
µ(lim sup
n→∞
{X \ Z : |fn − f | ≥ ε}) = 0
⇒ lim sup
n→∞
µ{X \ Z : |fn − f | ≥ ε} = 0
⇒ lim
n→∞
µ{X \ Z : |fn − f | ≥ ε} = 0
The last condition is equivalent to
lim
n→∞
µ{X \ Z : |fn − f | < ε} = µ(X \ Z) = µ(X)
⇔ ∀η > 0, ∃N ∈N : µ(X) − µ{X \ Z : |fn − f | < ε} ≤ η for all n ≥ N.
Let us take η = µ(X) − α > 0. Then we have
∃N ∈N : µ{X \ Z : |fn − f | < ε} ≥ α for all n ≥ N.
Since {X : |fn − f | < ε} ⊃ { X \ Z : |fn − f | < ε}, so we have
∀ε > 0, ∃N ∈N : n ≥ N ⇒ µ({X : |fn − f | < ε}) ≥ α. ■
1See Problem 11b. We have
µ
(
lim sup
n→∞
En
)
≥ lim sup
n→∞
µ(En).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

48 CHAPTER 4. CONVERGENCE A.E. AND CONVERGENCE IN MEASURE
Problem 41
(a) Show that the condition
lim
n→∞
µ{x ∈ D : |fn(x) − f (x)| > 0} = 0
implies that fn
µ
− →f on D.
(b) Show that the converse is not true.
(c) Show that the condition in (a) implies that for a.e. x ∈ D we have fn(x) =
f (x) for inﬁnitely many n ∈N.
Solution
(a) Given any ε > 0, for every n ∈N, let
En = {x ∈ D : |fn(x) − f (x)| > ε}; Fn = {x ∈ D : |fn(x) − f (x)| > 0}.
Then we have for all n ∈N
x ∈ En ⇒ | fn(x) − f (x)| > ε
⇒ | fn(x) − f (x)| > 0
⇒ x ∈ Fn.
Consequently, En ⊂ Fn and µ(En) ≤ µ(Fn) for all n ∈N. By hypothesis, we have
that lim n→∞ µ(Fn) = 0. This implies that lim n→∞ µ(En) = 0. Thus, fn
µ
− →f.
(b) The converse of (a) is false.
Consider functions:
fn(x) = 1
n , x ∈ [0, 1] n ∈N.
f (x) = 0 , x ∈ [0, 1].
Then fn → f (pointwise) on [0 , 1]. By Lebesgue Theorem fn
µ
− →f on [0 , 1]. But for
every n ∈N
|fn(x) − f (x)| = 1
n > 0, ∀x ∈ [0, 1].
In other words,
{x ∈ D : |fn(x) − f (x)| > 0} = [0, 1].
Thus,
lim
n→∞
µ{x ∈ D : |fn(x) − f (x)| > 0} = 1 ⁄= 0.
(c) Recall that (Problem 11a)
µ(lim inf
n→∞
En) ≤ lim inf
n→∞
µ(En). (∗)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

49
Let En = {x ∈ D : fn(x) ⁄= f (x)} and E = lim inf n→∞ En. By (a),
lim inf
n→∞
µ(En) = lim
n→∞
µ(En) = 0 .
Therefore, by ( ∗), µ (E) = 0. By deﬁnition, we have
E =
⋃
n∈N
⋂
k≥n
Ek.
Hence, x /∈ E whenever x ∈ Ec
n for inﬁnitely many n’s, that is fn(x) = f (x) a.e. in
D for inﬁnitely many n’s. ■
Problem 42
Suppose fn(x) ≤ fn+1(x) for all n ∈N and x ∈ D \ Z with µ(Z) = 0 . If fn
µ
− →f
on D , then prove that fn → f a.e. on D.
Solution
Let B = D \ Z. Since fn
µ
− →f on D, f n
µ
− →f on B. Then, By Riesz theorem, there
exists a sub-sequence ( fnk) of ( fn) such that fnk → f a.e. on B.
Let C = {x ∈ B : fnk↛ f }. Then µ(C) = 0 and fnk → f on B \ C.
From fn(x) ≤ fn+1(x) for all n ∈N, and since nk ≥ k, we get fk ≤ fnk for all k ∈N.
Therefore
|fk − f | ≤ | fnk − f |.
This implies that fk → f on B \ C. Since B \ C = D \ (Z ∪ C) and µ(Z ∪ C) = 0,
it follows that fn → f a.e. on D ■.
Problem 43
Show that if fn
µ
− →f on D and gn
µ
− →g on D then fn + gn
µ
− →f + g on D.
Solution
Since fn
µ
− →f and gn
µ
− →g on D, for every ε > 0,
lim
n→∞
µ{D : |fn − f | ≥ ε
2 } = 0(4.1)
lim
n→∞
µ{D : |gn − g| ≥ ε
2 } = 0.(4.2)
Now
|(fn + gn) − (f + g)| ≤ | fn − f | + |gn − g|.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

50 CHAPTER 4. CONVERGENCE A.E. AND CONVERGENCE IN MEASURE
By the triangle inequality above, if |(fn + gn) − (f + g)| ≥ ε is true, then at least
one of the two following inequalities must be true:
|fn − f | ≥ ε
2 or |gn − g| ≥ ε
2 .
Hence
{D : |(fn + gn) − (f + g)| ≥ ε} ⊂
{
D : |fn − f | ≥ ε
2
}
∪
{
D : |gn − g| ≥ ε
2
}
.
Therefore,
µ{D : |(fn + gn) − (f + g)| ≥ ε} ≤ µ
{
D : |fn − f | ≥ ε
2
}
+ µ
{
D : |gn − g| ≥ ε
2
}
.
From (4.1) and (4.2) we obtain
lim
n→∞
µ{D : |(fn + gn) − (f + g)| ≥ ε} = 0.
That is, by deﬁnition, fn + gn
µ
− →f + g on D. ■
Problem 44
Show that if fn
µ
− →f on D and gn
µ
− →g on D and µ(D) < ∞, then fngn
µ
− →f g
on D.
(Assume that both fn and gn are real-valued for every n ∈N so that the multiplication fngn
is possible.)
Solution
For every ε > 0 and δ > 0, we want µ{|fngn − f g| ≥ ε} < δ for n large enough.
Notice that
(∗) |fngn − f g| ≤ | fngn − f gn| + |f gn − f g| ≤ | fn − f ||gn| + |f ||gn − g|.
For any N ∈N, let
EN = {D : |f | > N } ∪ {D : |g| > N }.
It is clear that EN ⊃ EN +1 for every N ∈N. Since µ(D) < ∞, we have
lim
N →∞
µ(EN ) = µ
( ⋂
N ∈N
EN
)
= µ(∅) = 0 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

51
It follows that, we can take N large enough to get, for every δ > 0,
(∗∗) ε
2N < 1 and µ(EN ) < δ
3 .
Observe that
{D : |gn| > N + 1} ⊂
{
D : |gn − g| ≥ ε
2N
}
∪ EN
(since |gn| ≤ | gn − g| + |g|). Now if we have
|fn − f | ≥ ε
2(N + 1) ; |gn| > N + 1; |gn − g| ≥ ε
2N , and |f | > N,
then (*) implies
{D : |fngn − f g| ≥ ε} ⊂
{
D : |fn − f | ≥ ε
2(N + 1)
}
∪ EN
∪
{
D : |gn − g| ≥ ε
2N
}
∪ {D : |gn| > N + 1}.
By assumption, given ε > 0, δ > 0, for n > N , we have
µ
{
D : |fn − f | ≥ ε
2(N + 1)
}
< δ
3
µ
{
D : |gn − g| ≥ ε
2N
}
< δ
3 .
From these results, from (*), and (**) we get
µ{D : |fngn − f g| ≥ ε} < δ
3 + δ
3 + δ
3 = δ. ■
Problem 45
(a) Deﬁnition of ”Almost uniform convergence” (a.u).
(b) Show that if fn → f a.u on D then fn
µ
− →f on D.
(c) Show that if fn → f a.u on D then fn → f a.e. on D.
Solution
(a) ∀ε > 0, ∃E ⊂ D such that µ(E) < ε and fn → f uniformly on D \ E.
(b) Suppose that fn → f a.u on D and fn does not converges to f in measure on
D. Then there exists an ε0 > 0 such that
µ{x ∈ D : |fn(x) − f (x)| > ε 0}↛ 0 as n → ∞.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

52 CHAPTER 4. CONVERGENCE A.E. AND CONVERGENCE IN MEASURE
We can choose n1 < n 2 < ... such that
µ{x ∈ D : |fnk(x) − f (x)| > ε 0} ≥ r for some r > 0 and ∀k ∈N.
Now since fn → f a.u on D,
∃E ⊂ D such that µ(E) < r
2 and fn → f uniformly on D \ E.
Let C = {x ∈ D : |fnk(x) − f (x)| > ε 0} ∀ k ∈ N. Then µ(C) ≥ r. Since
fn → f uniformly on D \ E,
∃N : n ≥ N ⇒ |fn(x) − f (x)| ≤ ε0, ∀x ∈ D \ E.
Thus,
C ⊂ (D \ E)c = E.
Hence,
0 < r ≤ µ(C) ≤ µ(E) < r
2 .
This is a contradiction.
(c) Since fn → f a.u. on D, for every n ∈ N, there exists En ⊂ D such that
µ(En) < 1
n and fn → f uniformly on D \ En. Let E = ⋂
n∈N En, then µ(E) = 0.
Since fn → f on D \ En for every n ∈N, f n → f on
⋃
n∈N
(D \ En) = D \
⋂
n∈N
En = D \ E.
Since µ(E) = 0 , f n → f a.e. on D ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 5
Integration of Bounded Functions
on Sets of Finite Measure
In this chapter we suppose µ(D) < ∞.
1. Integration of simple functions
Deﬁnition 17 (Lebesgue integral of simple functions)
Let ϕ be a simple function on D and ϕ = ∑n
i=1 aiχDi be its canonical representation. The Lebesgue
integral of ϕ on D is deﬁned by
∫
D
ϕ(x)µ(dx) =
n∑
i=1
aiµ(Di).
We usually use simple notations for the integral of ϕ:
∫
D
ϕdµ,
∫
D
ϕ(x)dx or
∫
D
ϕ.
If
∫
D ϕdµ < ∞, then we say that ϕ is integrable on D.
Proposition 15 (properties of integral of simple functions)
1. µ(D) = 0 ⇒
∫
D ϕdµ = 0.
2. ϕ ≥ 0, E ⊂ D ⇒
∫
E ϕdµ ≤
∫
D ϕdµ.
3.
∫
D cϕdµ = c
∫
D ϕdµ.
4.
∫
D ϕdµ = ∑n
i=1
∫
Di
ϕdµ.
5.
∫
D cϕdµ = c
∫
D ϕdµ (c is a constant).
6.
∫
D(ϕ1 + ϕ2)dµ =
∫
D ϕ1dµ +
∫
D ϕ2dµ.
7. ϕ1 = ϕ2 a.e. on D ⇒
∫
D ϕ1dµ =
∫
D ϕ2dµ.
53
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

54CHAPTER 5. INTEGRATION OF BOUNDED FUNCTIONS ON SETS OF FINITE MEASURE
2. Integration of bounded functions
Deﬁnition 18 (Lebesgue integral of bounded functions)
Let f be a bounded real-valued measurable function on D. Let Φ be the collection of all simple
functions on D. We deﬁne the Lebesgue integral of f on D by
∫
D
f dµ = inf
ψ≥f
∫
D
ψdµ = sup
ϕ≤f
∫
D
ϕdµ where ϕ, ψ ∈ Φ.
If
∫
D f dµ < ∞, then we say that f is integrable on D.
Proposition 16 (properties of integral of bounded functions)
1.
∫
D cf dµ = c
∫
D f dµ.
2.
∫
D(f + g)dµ =
∫
D f dµ +
∫
D gdµ.
3. f = g a.e. on D ⇒
∫
D f dµ =
∫
D gdµ.
4. f ≤ g on D ⇒
∫
D f dµ ≤
∫
D gdµ.
5. |f | ≤ M on D ⇒
⏐⏐∫
D f dµ
⏐⏐ ≤
∫
D |f |dµ ≤ M µ(D).
6. f ≥ 0 a.e. on D and
∫
D f dµ = 0 ⇒ f = 0 a.e. on D.
7. If (Dn) be a disjoint sequence of measurable subset Dn ⊂ D with ⋃
n∈N Dn = D then
∫
D
f d = µ
∑
n∈N
∫
Dn
f dµ.
Theorem 5 (Bounded convergence theorem)
Suppose that (fn) is a uniformly bounded sequence of real-valued measurable functions on D, and
f is a bounded real-valued measurable function on D. If fn → f a.e. on D, then
lim
n→∞
∫
D
|fn − f |dµ = 0.
In particular,
lim
n→∞
∫
D
fndµ =
∫
D
f dµ.
∗ ∗ ∗∗
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

55
Problem 46
Let f be an extended real-valued measurable function on a measurable set D. For
M1, M2 ∈R, M 1 < M 2, let the truncation of f at M1 and M2 be deﬁned by
g(x) =



M1 if f (x) < M 1
f (x) if M1 ≤ f (x) ≤ M2
M2 if f (x) > M 2.
Show that g is measurable on D.
Solution
Let a ∈R. We need to show that the set E = {x ∈ D : g(x) > a} is measurable.
There are three cases to consider:
1. If a ≥ M2 then E =∅ which is measurable.
2. If a < M 1 then E = D which is measurable.
3. If M1 ≤ a < M 2 then E = {x ∈ D : f (x) > a} which is measurable.
Thus, in all three cases E is measurable, so g is measurable. ■
Problem 47
Given a measure space (X, A, µ). Let f be a bounded real-valued A-measurable
function on D ∈ A with µ(D) < ∞. Suppose |f (x)| ≤ M, ∀x ∈ D for some
constant M > 0.
(a) Show that if
∫
D f dµ = M µ(D), then f = M a.e. on D.
(b) Show that if f < M a.e. on D and if µ(D) > 0, then
∫
D f dµ < M µ(D).
Solution
(a) For every n ∈N, let En = {x ∈ D : f (x) < M − 1
n }. Then, since f ≤ M on
D \ En, we have
∫
D
f dµ =
∫
En
f dµ +
∫
D\En
f dµ
≤
(
M − 1
n
)
µ(En) + M µ(D \ En).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

56CHAPTER 5. INTEGRATION OF BOUNDED FUNCTIONS ON SETS OF FINITE MEASURE
Since En ⊂ D, we have
µ(D \ En) = µ(D) − µ(En).
Therefore,
∫
D
f dµ ≤
(
M − 1
n
)
µ(En) + M µ(D) − M µ(En)
= M µ(D) − 1
n µ(En).
By assumption
∫
D f dµ = M µ(D), it follows that
0 ≤ − 1
n µ(En) ≤ 0, ∀n ∈N,
which implies µ(En) = 0 , ∀n ∈N.
Now let E = ⋃∞
n=1 En then E = {x ∈ D : f (x) < M }. We want to show that
µ(E) = 0. We have
0 ≤ µ(E) ≤
∞∑
n=1
µ(En) = 0 .
Thus, µ(E) = 0. Since |f | ≤ M , the last result implies f = M a.e. on D.
(b) First we note that |f | ≤ M on D implies that
∫
D f dµ ≤ M µ(D). Assume that∫
D f dµ = M µ(D). By part (a) we have f = M a.e. on D. This contradicts the fact
that f < M a.e. on D. Thus
∫
D f dµ < M µ(D). ■
Problem 48
Consider a sequence of functions (fn)n∈N deﬁned on [0, 1] by
fn(x) = nx
1 + n2x2 for x ∈ [0, 1].
(a) Show that (fn) is uniformly bounded on [0, 1] and evaluate
lim
n→∞
∫
[0,1]
nx
1 + n2x2 dµ.
(b) Show that (fn) does not converge uniformly on [0, 1].
Solution
(a) For all n ∈N, for all x ∈ [0, 1], we have 1 + n2x2 ≥ 2nx ≥ 0 and 1 + n2x2 > 0,
hence
0 ≤ fn(x) = nx
1 + n2x2 ≤ 1
2 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

57
Thus, ( fn) is uniformly bounded on [0 , 1].
Since each fn is continuous on [0 , 1], f is Riemann integrable on [0 , 1]. In this case,
Lebesgue integral and Riemann integral on [0 , 1] coincide:
∫
[0,1]
nx
1 + n2x2 dµ =
∫ 1
0
nx
1 + n2x2 dx
= 1
2n
∫ 1+n2
1
1
t dt (with t = 1 + n2x2)
= 1
2n ln(1 + n2) = ln(1 + n2)
2n .
Using L’Hospital rule we get lim x→∞
ln(1+x2)
2x = 0. Hence,
lim
n→∞
∫
[0,1]
nx
1 + n2x2 dµ = 0.
(b) For each x ∈ [0, 1],
lim
n→∞
nx
1 + n2x2 = 0.
Hence, fn → f ≡ 0 pointwise on [0 , 1]. To show fn does not converge to f ≡ 0
uniformly on [0 , 1], we ﬁnd a sequence ( xn) in [0 , 1] such that xn → 0 and fn(xn)↛
f (0) = 0 as n → ∞. Indeed, take xn = 1
n . Then fn(x) = 1
2 . Thus,
lim
n→∞
fn(xn) = 1
2 ⁄= f (0) = 0 . ■
Problem 49
Let (fn)n∈N and f be extended real-valued measurable functions on D ∈ M L with
µ(D) < ∞ and assume that f is real-valued a.e. on D. Show that fn
µ
− →f on D
if and only if
lim
n→∞
∫
D
|fn − f |
1 + |fn − f | dµ = 0.
Solution
• Suppose fn
µ
− →f on D. By deﬁnition of convergence in measure, for any ε > 0,
there exists an N ∈N such that for n ≥ N ,
∃En ⊂ D : µ(En) < ε
2 and |fn − f | < ε
2µ(D) on D \ En.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

58CHAPTER 5. INTEGRATION OF BOUNDED FUNCTIONS ON SETS OF FINITE MEASURE
For n ≥ N we have
(∗)
∫
D
|fn − f |
1 + |fn − f | dµ =
∫
En
|fn − f |
1 + |fn − f | dµ +
∫
D\En
|fn − f |
1 + |fn − f | dµ.
Note that for all n ∈N, we have 0 ≤ |fn−f |
1+|fn−f | ≤ 1 on En and
0 ≤ |fn − f |
1 + |fn − f | = |fn − f | 1
1 + |fn − f | ≤ |fn − f | ≤ ε
2µ(D) on D \ En.
So for n ≥ N , we can write (*) as
0 ≤
∫
D
|fn − f |
1 + |fn − f | dµ ≤
∫
En
1 dµ +
∫
D\En
ε
2µ(D) dµ
= µ(En) + ε
2µ(D) µ(D \ En)
≤ µ(En) + ε
2 < ε
2 + ε
2 = ε.
Thus, lim n→∞
∫
D
|fn−f |
1+|fn−f | µ(dx) = 0 .
• Conversely, suppose lim n→∞
∫
D
|fn−f |
1+|fn−f | dµ = 0 . We show fn
µ
− →f on D. For any
ε > 0, for n ∈N, let En = {x ∈ D : |fn − f | ≥ ε}. We have
|fn − f | ≥ ε ⇒ |fn − f |
1 + |fn − f | ≥ ε
1 + ε
( since the function ϕ(x) = x
1+x , x > 0 is increasing).
It follows that
0 ≤
∫
En
ε
1 + ε dµ ≤
∫
En
|fn − f |
1 + |fn − f | dµ ≤
∫
D
|fn − f |
1 + |fn − f | dµ.
Hence,
0 ≤ ε
1 + ε µ(En) ≤
∫
D
|fn − f |
1 + |fn − f | dµ.
Since lim n→∞
∫
D
|fn−f |
1+|fn−f | dµ = 0, limn→∞ µ(En) = 0. Thus, fn
µ
− →f on D. ■
Problem 50
Let (X, A, µ) be a ﬁnite measure space. Let Φ be the set of all extended real-
valued A-measurable function on X where we identify functions that are equal
a.e. on X. Let
ρ(f, g) =
∫
X
|f − g|
1 + |f − g| dµ for f, g ∈ Φ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

59
(a) Show that ρ is a metric on Φ.
(b) Show that Φ is complete w.r.t. the metric ρ.
Solution
(a) Note that µ(X) is ﬁnite and 0 ≤ |f −g|
1+|f −g| < 1, so 0 ≤ ρ < ∞ .
• ρ(f, g) = 0 ⇔
∫
X
|f −g|
1+|f −g| dµ = 0 ⇔ f − g = 0 ⇔ f = g. (We identify
functions that are equal a.e. on X.)
• It is clear that ρ(f, g) = ρ(g, f ).
• We make use the fact that the function ϕ(x) = x
1+x , x > 0 is increasing. For
f, g, h ∈ Φ,
|f − h|
1 + |f − h| ≤ |f − g| + |g − h|
1 + |f − g| + |g − h|
= |f − g|
1 + |f − g| + |g − h| + |g − h|
1 + |f − g| + |g − h|
≤ |f − g|
1 + |f − g| + |g − h|
1 + |g − h| .
Integrating over X we get
∫
X
|f − h|
1 + |f − h| dµ ≤
∫
X
|f − g|
1 + |f − g| dµ +
∫
X
|g − h|
1 + |g − h| dµ.
That is
ρ(f, g) ≤ ρ(f, h) + ρ(h, g).
Thus, ρ is a metric on Φ.
(b) Let ( fn) be a Cauchy sequence in Φ. We show that there exists an f ∈ Φ such
that ρ(fn, f) → 0 as n → ∞.
First we claim that ( fn) is a Cauchy sequence w.r.t. convergence in measure. Let
η > 0. For n, m ∈N, deﬁne Am,n = {X : |fn − fm| ≥ η}. For every ε > 0, there
exists an N ∈N such that
(∗) n, m ≥ N ⇒ ρ(fn, fm) < ε η
1 + η .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

60CHAPTER 5. INTEGRATION OF BOUNDED FUNCTIONS ON SETS OF FINITE MEASURE
While we have that
ρ(fn, fm) =
∫
X
|fn − fm|
1 + |fn − fm| dµ ≥
∫
Am,n
|fn − fm|
1 + |fn − fm| dµ
≥ η
1 + η µ(Am,n).
For n, m ≥ N , from (*) we get
ε η
1 + η > η
1 + η µ(Am,n).
This implies that µ(Am,n) < ε . Thus, ( fn) is Cauchy in measure. We know that if
(fn) is Cauchy in measure then ( fn) converges in measure to some f ∈ Φ.
Next we prove that ρ(fn, f) → 0. Since fn
µ
− →f , for any ε > 0 there exists E ∈ A
and an N ∈N such that
µ(E) < ε
2 and |fn − f | < ε
2µ(X) on X \ E whenever n ≥ N.
On X \ E, for n ≥ N , we have
∫
X\E
|fn − f |
1 + |fn − f | dµ ≤
∫
X\E
|fn − f |dµ < ε
2µ(X) µ(X \ E) ≤ ε
2 .
On E, for all n, we have
∫
E
|fn − f |
1 + |fn − f | dµ ≤
∫
E
1 dµ = µ(E) < ε
2 .
Hence, for n ≥ N , we have
ρ(fn, f) =
∫
X
|fn − f |
1 + |fn − f | dµ =
∫
E
|fn − f |
1 + |fn − f | dµ +
∫
X\E
|fn − f |
1 + |fn − f | dµ < ε.
Thus, ( fn) converges to f ∈ Φ. And hence, (Φ , ρ) is complete ■
Problem 51 (Bounded convergence theorem under convergence in measure)
Suppose that (fn) is a uniformly bounded sequence of real-valued measurable func-
tions on D, and f is a bounded real-valued measurable function on D. If fn
w
− →f
on D, then
lim
n→∞
∫
D
|fn − f |dµ = 0.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

61
Solution
We will use this fact:
Let (an) be a sequence of real numbers. If there exists a real number a such that
every subsequence (ank) has a subsequence (ankl
) converging to a, then the sequence
(an) converges to a.
Consider the sequence of real numbers
an =
∫
D
|fn − f |dµ, n ∈N.
Take an arbitrary subsequence ( ank). Consider the sequence ( fnk). Since ( fn) con-
verges to f in measure on D, the subsequence ( fnk) converges to f in measure on
D too. By Riesz theorem, there exists a subsequence ( fnkl
) converging to f a.e. on
D. Thus by the bounded convergence theorem, we have
lim
n→∞
∫
D
|fnkl
− f |dµ = 0.
That is, the subsequence ( ankl
) of the arbitrary subsequence ( ank) of ( an) converges
to 0. Therefore the sequence ( an) converges to 0. Thus
lim
n→∞
∫
D
|fn − f |dµ = 0. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

62CHAPTER 5. INTEGRATION OF BOUNDED FUNCTIONS ON SETS OF FINITE MEASURE
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 6
Integration of Nonnegative
Functions
Deﬁnition 19 Let f be a nonnegative extended real-valued measurable function on a measurable
D ⊂R. We deﬁne the Lebesgue integral of f on D by
∫
D
f dµ = sup
0≤ϕ≤f
ϕdµ,
where the supremum is on the collection of all nonnegative simple function ϕ on D.
If the integral is ﬁnite, we say that f is integrable on D.
Proposition 17 (Properties)
Let f, f1 and f2 be nonnegative extended real-valued measurable functions on D. Then
1.
∫
D f dµ < ∞ ⇒ f < ∞ a.e. on D.
2.
∫
D f dµ = 0 ⇒ f = 0 a.e. on D.
3. D0 ⊂ D ⇒
∫
D0
f dµ ≤
∫
D f dµ.
4. f > 0 a.e. on D and
∫
D f dµ = 0 ⇒ µ(D) = 0 .
5. f1 ≤ f2 on D ⇒
∫
D f1dµ ≤
∫
D f2dµ.
6. f1 = f2 a.e. on D ⇒
∫
D f1dµ ≤
∫
D f2dµ.
Theorem 6 (Monotone convergence theorem)
Let (fn) be an increasing sequence of nonnegative extended real-valued measurable functions on D.
If fn → f on D then
lim
n→∞
∫
D
fndµ =
∫
D
f dµ.
Remark: The conclusion is not true for a decreasing sequence.
63
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

64 CHAPTER 6. INTEGRATION OF NONNEGATIVE FUNCTIONS
Proposition 18 Let (fn) be an increasing sequence of nonnegative extended real-valued measur-
able functions on D. Then we have
∫
D
(∑
n∈N
fn
)
dµ =
∑
n∈N
∫
D
fndµ.
Theorem 7 (Fatou’s Lemma)
Let (fn) be a sequence of nonnegative extended real-valued measurable functions on D. Then we
have ∫
D
lim inf
n→∞
fndµ ≤ lim inf
n→∞
∫
D
fndµ.
In particular, if limn→∞ fn = f exists a.e. on D, then
∫
D
f dµ ≤ lim inf
n→∞
∫
D
fndµ.
Proposition 19 (Uniform absolute continuity of the integral)
Let f be an integrable nonnegative extended real-valued measurable functions on D. Then for every
ε > 0, there exists δ > 0 such that ∫
E
f dµ < ε
for every measurable E ⊂ D with µ(E) < δ .
∗ ∗ ∗∗
Problem 52
Let f1 and f2 be nonnegative extended real-valued measurable functions on a
measurable set D ⊂R. Suppose f1 ≤ f2 and f1 is integrable on D. Prove that
f2 − f1 is deﬁned a.e. on D and
∫
D
(f2 − f1)dµ =
∫
D
f2dµ −
∫
D
f1dµ.
Solution
Since f1 is integrable on D, f1 is real-valued a.e. on D. Thus there exists a null set
N ⊂ D such that 0 ≤ f1(x) < ∞, ∀x ∈ D \ N . Then f2 − f1 is deﬁned on D \ N .
That is f2 − f1 is deﬁned a.e. on D. On the other hand, since f2 = f1 + (f2 − f1),
we have
∫
D
f2dµ =
∫
D
[
f1 + (f2 − f1)
]
dµ =
∫
D
f1dµ +
∫
D
(f2 − f1)dµ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

65
Since
∫
D f1dµ < ∞, we have
∫
D
(f2 − f1)dµ =
∫
D
f2dµ −
∫
D
f1dµ. ■
Remark: If
∫
D f1dµ = ∞,
∫
D f2dµ −
∫
D f1dµ may have the form ∞ − ∞.
Problem 53
Let f be a non-negative real-valued measurable function on a measure space
(X, A, µ). Suppose that
∫
E f dµ = 0 for every E ∈ A. Show that f = 0 a.e.
Solution
Since f ≥ 0, A = {x ∈ X : f (x) > 0} = {x ∈ X : f (x) ⁄= 0}. We shall show that
µ(A) = 0.
Let An = {x ∈ X : f (x) ≥ 1
n } for every n ∈N. Then A = ⋃
n∈N An. Now on An we
have
f ≥ 1
n ⇒
∫
An
f dµ ≥ 1
n µ(An)
⇒ µ(An) ≤ n
∫
An
f dµ = 0 (by assumption)
⇒ µ(An) = 0 for every n ∈N.
Thus, 0 ≤ µ(A) ≤ ∑
n∈N µ(An) = 0. Hence, µ(A) = 0. This tells us that f = 0
a.e. ■
Problem 54
Let (fn : n ∈N) be a sequence of non-negative real-valued measurable functions
onR such that fn → f a.e. on R.
Suppose limn→∞
∫
R fndµ =
∫
R f dµ < ∞. Show that for each measurable set
E ⊂R we have
lim
n→∞
∫
E
fndµ =
∫
E
f dµ.
Solution
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

66 CHAPTER 6. INTEGRATION OF NONNEGATIVE FUNCTIONS
Since gn = fn − fnχE ≥ 0, n ∈N and fn → f a.e., we have, by Fatou’s lemma,
∫
R
lim
n→∞
gndµ ≤ lim inf
n→∞
∫
R
gndµ
∫
R
(f − f χE)dµ ≤ lim inf
n→∞
∫
R
(fn − fnχE)dµ
∫
R
f dµ −
∫
E
f dµ ≤ lim
n→∞
∫
R
fndµ − lim sup
n→∞
∫
E
fndµ.
From the last inequation and assumption we get
(6.1)
∫
E
f dµ ≥ lim sup
n→∞
∫
E
fndµ.
Let hn = fn − fnχE ≥ 0. Using the similar calculation, we obtain
(6.2)
∫
E
f dµ ≤ lim inf
n→∞
∫
E
fndµ.
From (6.1) and (6.2) we have
lim
n→∞
∫
E
fndµ =
∫
E
f dµ. ■
Problem 55
Given a measure space (X, A, µ). Let (fn) and f be extended real-valued A-
measurable functions on D ∈ A and assume that f is real-valued a.e. on D.
Suppose there exists a sequence of positive numbers (εn) such that
1. ∑
n∈N εn < ∞.
2.
∫
D |fn − f |pdµ < ε n for every n ∈N for some ﬁxed p ∈ (0, ∞).
Show that the sequence (fn) converges to f a.e. on D. (Note that no integrability
of fn, f, |f |p on D is assumed).
Solution
Since |fn−f |p is non-negative measurable for every n ∈N, the sequence
(∑N
n=1 |fn − f |p
)
N ∈N
is an increasing sequence of non-negative measurable functions. By the Monotone
Convergence Theorem, we have
∫
D
lim
N →∞
( N∑
n=1
|fn − f |p
)
dµ = lim
N →∞
∫
D
N∑
n=1
|fn − f |pdµ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

67
Using assumptions we get
∫
D
∞∑
n=1
|fn − f |pdµ = lim
N →∞
N∑
n=1
∫
D
|fn − f |pdµ
=
∞∑
n=1
∫
D
|fn − f |pdµ
≤
∞∑
n=1
εn < ∞.
This means that the function under the integral symbol in the left hand side is ﬁnite
a.e. on D. We have
∞∑
n=1
|fn − f |p < ∞ a.e. on D ⇒ lim
n→∞
|fn − f |p = 0 a.e. on D
⇒ lim
n→∞
|fn − f | = 0 a.e. on D
⇒ fn → f a.e. on D. ■.
Problem 56
Given a measure space (X, A, µ). Let (fn) and f be extended real-valued mea-
surable functions on D ∈ A and assume that f is real-valued a.e. on D. Suppose
limn→∞
∫
D |fn − f |pdµ = 0 for some ﬁxed p ∈ (0, ∞). Show that
fn
µ
− →f on D.
Solution
Given any ε > 0. For every n ∈N, let An = {D : |fn − f | ≥ ε}. Then
∫
D
|fn − f |pdµ =
∫
An
|fn − f |pdµ +
∫
D\An
|fn − f |pdµ
≥
∫
An
|fn − f |pdµ
≥ εpµ(An).
Since lim n→∞
∫
D |fn − f |pdµ = 0, limn→∞ µ(An) = 0. This means that
fn
µ
− →f on D. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

68 CHAPTER 6. INTEGRATION OF NONNEGATIVE FUNCTIONS
Problem 57
Let (X, A, µ) be a measure space and let f be an extended real-valued A-
measurable function on X such that
∫
X |f |pdµ < ∞ for some ﬁxed p ∈ (0, ∞).
Show that
lim
λ→∞
λpµ{X : |f | ≥ λ} = 0.
Solution
For n = 0, 1, 2, ..., let En = {D : n ≤ |f | < n + 1}. Then En ∈ A and the En’s are
disjoint. Moreover, X = ⋃∞
n=0 En. We have
∞ >
∫
X
|f |pdµ =
∞∑
n=0
∫
En
|f |pdµ ≥
∞∑
n=0
npµ(En).
Since ∑∞
n=0 npµ(En) < ∞, for any ε > 0, there exists N ∈N such that for n ≥ N
we have ∞∑
n=N
npµ(En) < ε.
Note that np ≥ N p since p > 0. So we have
N p
∞∑
n=N
µ(En) < ε.
But ⋃∞
n=N En = {X : |f | ≥ N }. So with the above N , we have
N pµ
( ∞⋃
n=N
En
)
= N pµ{X : |f | ≥ N } < ε.
Thus,
lim
λ→∞
λpµ{X : |f | ≥ λ} = 0. ■
Problem 58
Let (X, A, µ) be a σ-ﬁnite measure space. Let f be an extended real-valued A-
measurable function on X. Show that for every p ∈ (0, ∞) we have
∫
X
|f |pdµ =
∫
[0,∞)
pλp−1µ{X : |f | > λ}µL(dλ). (∗)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

69
Solution
We may suppose f ≥ 0 (otherwise we set g = |f | ≥ 0).
1. If f = χE, E ∈ A, then
∫
X
f pdµ =
∫
X
(χE)pdµ = µ(E).
∫
[0,∞)
pλp−1µ{X : χE > λ}µL(dλ) =
∫ 1
0
pλp−1µ(E)dλ = µ(E).
Thus, the equality ( ∗) holds.
2. If f = ∑n
i=1 aiχEi (simple function), with ai ≥ 0, E i ∈ A, i = 1, ..., n., then the
equality ( ∗) holds because of the linearity of the integral.
3. If f ≥ 0 measurable, then there is a sequence ( ϕn) of non-negative measurable
simple functions such that ϕn ↑ f . By the Monotone Convergence Theorem we have
∫
X
f pdµ = lim
n→∞
∫
X
ϕp
ndµ
= lim
n→∞
∫
[0,∞)
pλp−1µ{X : ϕn > λ}µL(dλ)
=
∫
[0,∞)
pλp−1µ{X : f > λ }µL(dλ). ■
Notes:
1. A = {X : χE > λ} = {x ∈ X : χE(x) > λ}.
• If 0 ≤ λ < 1 then A = E.
• If λ ≥ 1 then A = ∅.
2. Why σ-ﬁnite measure?
Problem 59
Given a measure space (X, A, µ). Let f be a non-negative extended real-valued
A-measurable function on D ∈ A with µ(D) < ∞.
Let Dn = {x ∈ D : f (x) ≥ n} for n ∈N. Show that
∫
D
f dµ < ∞ ⇔
∑
n∈N
µ(Dn) < ∞.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

70 CHAPTER 6. INTEGRATION OF NONNEGATIVE FUNCTIONS
Solution
From the expression Dn = {x ∈ D : f (x) ≥ n} with f A-measurable, we deduce
that Dn ∈ A and
D := D0 ⊃ D1 ⊃ D2 ⊃ ... ⊃ Dn ⊃ Dn+1 ⊃ ...
Moreover, all the sets Dn \ Dn+1 = {D : n ≤ f < n + 1, n ∈N} are disjoint and
D =
⋃
n∈N
(Dn \ Dn+1).
It follows that
nµ(Dn \ Dn+1) ≤
∫
Dn\Dn+1
f dµ ≤ (n + 1)µ(Dn \ Dn+1)
∞∑
n=0
nµ(Dn \ Dn+1) ≤
∫
⋃
n∈N(Dn\Dn+1)
f dµ ≤
∞∑
n=0
(n + 1)µ(Dn \ Dn+1)
∞∑
n=0
nµ[(Dn) − µ(Dn+1)] ≤
∫
D
f dµ ≤
∞∑
n=0
(n + 1)[µ(Dn) − µ(Dn+1)]. (i)
Some more calculations:
∞∑
n=0
nµ[(Dn) − µ(Dn+1)] = 1[ µ(D1) − µ(D2)] + 2[µ(D2) − µ(D3)] + ...
=
∞∑
n=1
µ(Dn),
and
∞∑
n=0
(n + 1)[µ(Dn) − µ(Dn+1)] = 1[ µ(D0) − µ(D1)] + 2[µ(D1) − µ(D2)] + ...
= µ(D) +
∞∑
n=1
µ(Dn).
With these, we rewrite ( i) as follows
∞∑
n=1
µ(Dn) ≤
∫
D
f dµ ≤ µ(D) +
∞∑
n=1
µ(Dn).
Since µ(D) < ∞, we have
∫
D
f dµ < ∞ ⇔
∑
n∈N
µ(Dn) < ∞. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

71
Problem 60
Given a measure space (X, A, µ) with µ(X) < ∞. Let f be a non-negative
extended real-valued A-measurable function on X. Show that f is µ-integrable
on X if and only if
∞∑
n=0
2nµ{x ∈ X : f (x) > 2n} < ∞.
Solution
Let En = {X : f > 2n} for each n = 0, 1, 2, ... Then it is clear that
E0 ⊃ E1 ⊃ ... ⊃ En ⊃ En+1 ⊃ ...
En \ En+1 = {X : 2 n < f ≤ 2n+1} and are disjoint
X \ E0 = {X : 0 ≤ f ≤ 1}
X = (X \ E0) ∪
∞⋃
n=0
(En \ En+1).
Now we have
∫
X
f dµ =
∫
X\E0
f dµ +
∫
⋃∞
n=0(En\En+1)
f dµ
=
∫
X\E0
f dµ +
∞∑
n=0
∫
En\En+1
f dµ.
This implies that
(6.3)
∞∑
n=0
∫
En\En+1
f dµ =
∫
X
f dµ −
∫
X\E0
f dµ.
On the other hand, for n = 0, 1, 2, ..., we have
2nµ(En \ En+1) ≤
∫
En\En+1
f dµ ≤ 2n+1µ(En \ En+1).
Therefore,
∞∑
n=0
2nµ(En \ En+1) ≤
∞∑
n=0
∫
En\En+1
f dµ ≤
∞∑
n=0
2n+1µ(En \ En+1).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

72 CHAPTER 6. INTEGRATION OF NONNEGATIVE FUNCTIONS
From (6.3) we obtain
∞∑
n=0
2nµ(En \ En+1) +
∫
X\E0
f dµ ≤
∫
X
f dµ ≤
∞∑
n=0
2n+1µ(En \ En+1) +
∫
X\E0
f dµ.
Since
0 ≤
∫
X\E0
f dµ ≤ µ(X \ E0) ≤ µ(X) < ∞,
we get
(6.4)
∞∑
n=0
2nµ(En \ En+1) ≤
∫
X
f dµ ≤
∞∑
n=0
2n+1µ(En \ En+1) + µ(X).
Some more calculations:
∞∑
n=0
2nµ(En \ En+1) =
∞∑
n=0
2n[µ(En) − µ(En+1)]
= µ(E0) − µ(E1) + 2[µ(E1) − µ(E2)] + 4[µ(E2) − µ(E3)] + ...
= µ(E0) + µ(E1) + 2µ(E2) + 4µ(E3) + ...
= 1
2 µ(E0) + 1
2
∞∑
n=0
2nµ(En),
and
∞∑
n=0
2n+1µ(En \ En+1) =
∞∑
n=0
2n+1[µ(En) − µ(En+1)]
= 2[ µ(E0) − µ(E1)] + 4[µ(E1) − µ(E2)] + 8[µ(E2) − µ(E3)] + ...
= µ(E0) + [µ(E0) + 2µ(E1) + 4µ(E2) + 8µ(E3) + ...]
= µ(E0) +
∞∑
n=0
2nµ(En).
With these, we rewrite (6.4) as follows
1
2 µ(E0) + 1
2
∞∑
n=0
2nµ(En) ≤
∫
X
f dµ ≤ µ(E0) +
∞∑
n=0
2nµ(En) + µ(X).
This implies that
1
2
∞∑
n=0
2nµ(En) ≤
∫
X
f dµ ≤
∞∑
n=0
2nµ(En) + 2µ(X).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

73
Since µ(X) < ∞, we have
∫
X
f dµ < ∞ ⇔
∞∑
n=0
2nµ{x ∈ X : f (x) > 2n} < ∞. ■
Problem 61
(a) Let {cn,i : n, i ∈ N} be an array of non-negative extended real numbers.
Show that
lim inf
n→∞
∑
i∈N
cn,i ≥
∑
i∈N
lim inf
n→∞
cn,i.
(b) Show that if (cn,i : n ∈N) is an increasing sequence for each i ∈N, then
lim
n→∞
∑
i∈N
cn,i =
∑
i∈N
lim
n→∞
cn,i.
Solution
(a) Let ν :N → [0, ∞] denote the counting measure. Consider the space (N, P(N), ν).
It is a measure space in which every A ⊂ N is measurable. Let i ↦→ b(i) be any
function on N. Then ∫
N
bdν =
∑
i∈N
b(i).
For the array {cn,i}, for each i ∈N, we can write cn,i = cn(i), n ∈N. Then cn is a
non-negative ν-measurable function deﬁned on N. By Fatou’s lemma,
∫
N
lim inf
n→∞
cndν ≤ lim inf
n→∞
∫
N
cndν,
that is ∑
i∈N
lim inf
n→∞
cn,i ≤ lim inf
n→∞
∑
i∈N
cn,i.
(b) If ( cn,i : n ∈N) is an increasing sequence for each i ∈N, then the sequence of
functions ( cn) is non-negative increasing. By the Monotone Convergence Theorem
we have
lim
n→∞
∫
N
cn(i)dν =
∫
N
lim
n→∞
cn(i)dν,
that is
lim
n→∞
∑
i∈N
cn,i =
∑
i∈N
lim
n→∞
cn,i. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

74 CHAPTER 6. INTEGRATION OF NONNEGATIVE FUNCTIONS
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 7
Integration of Measurable
Functions
Given a measure space ( X, A, µ). Let f be a measurable function on a set D ∈ A. We deﬁne the
positive and negative parts of f by
f + := max{f, 0} and f − := max{−f, 0}.
Then we have
f = f + − f − and |f | = f + + f −.
Deﬁnition 20 Let f be an extended real-valued measurable function on D. The function f is said
to be integrable on D if f + and f − are both integrable on D. In this case we deﬁne
∫
D
f dµ =
∫
D
f +dµ −
∫
D
f −dµ.
Proposition 20 (Properties)
1. f is integrable on D if and only if |f | is integrable on D.
2. If f is integrable on D then cf is integrable on D, and we have
∫
D cf dµ = c
∫
D f dµ, where
c is a constant in R.
3. If f and g are integrable on D then f + g are integrable on D, and we have
∫
D(f + g)dµ =∫
D f dµ +
∫
D gdµ.
4. f ≤ g ⇒
∫
D f dµ ≤
∫
D gdµ.
5. If f is integrable on D then |f | < ∞ a.e. on D, that is, f is real-valued a.e. on D.
6. If {D1, ..., Dn} is a disjoint collection in A, then
∫
⋃n
i=1 Di
f dµ =
n∑
i=1
∫
Di
f dµ.
75
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

76 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
Theorem 8 (generalized monotone convergence theorem)
Let (fn) be a sequence of integrable extended real-valued functions on D.
1. If (fn) is increasing and there is a extended real-valued measurable function g such that fn ≥ g
for every n ∈N, then
lim
n→∞
fndµ =
∫
D
gdµ.
2. If (fn) is decreasing and there is a extended real-valued measurable function g such that fn ≤ g
for every n ∈N, then
lim
n→∞
fndµ =
∫
D
gdµ.
Theorem 9 (Lebesgue dominated convergence theorem theorem - D.C.T)
Let (fn) be a sequence of integrable extended real-valued functions on D and g be an integrable
nonnegative extended real-valued function on D such that |fn| ≤ g on D for every n ∈ N. If
limn→∞ fn = f exists a.e. on D, then f is integrable on D and
lim
n→∞
∫
D
fndµ =
∫
D
f dµ and lim
n→∞
∫
D
|fn − f |dµ = 0.
∗ ∗ ∗∗
Problem 62
Prove this statement:
Let f be extended real-valued measurable function on a measurable set D. If f
is integrable on D, then the set {D : f ⁄= 0} is a σ-ﬁnite set.
Solution
For every n ∈N set
Dn =
{
x ∈ D : |f (x)| ≥ 1
n
}
.
Then we have
{x ∈ D : f (x) ⁄= 0} = {x ∈ D : |f (x)| > 0} =
⋃
n∈N
Dn.
Now for each n ∈N we have
1
n µ(Dn) ≤
∫
Dn
|f |dµ ≤
∫
D
|f |dµ < ∞.
Thus
µ(Dn) = µ < ∞, ∀n ∈N,
that is, the set {x ∈ D : f (x) ⁄= 0} is σ-ﬁnite. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

77
Problem 63
Let f be extended real-valued measurable function on a measurable set D. If (En)
is an increasing sequence of measurable sets such that limn→∞ En = D, then
∫
D
f dµ = lim
n→∞
∫
En
f dµ.
Solution
Since ( En) is an increasing sequence with limit D, so by deﬁnition, we have
D =
∞⋃
n=1
En.
Let
D1 = E1 and Dn = En \ En+1, n ≥ 2.
Then {D1, D2, ...} is a disjoint collection of measurable sets, and we have
n⋃
i=1
Di = En and
∞⋃
n=1
Dn =
∞⋃
n=1
En = D.
Hence
∫
D
f dµ =
∞∑
n=1
∫
Dn
f dµ = lim
n→∞
n∑
i=1
∫
Di
f dµ
= lim
n→∞
∫
⋃n
i=1 Di
f dµ = lim
n→∞
∫
En
f dµ. ■
Problem 64
Let (X, A, µ) be a measure space. Let f and g be extended real-valued measurable
functions on X. Suppose that f and g are integrable on X and
∫
E f dµ =
∫
E gdµ
for every E ∈ A. Show that f = g a.e. on X.
Solution
• Case 1: f and g are two real-valued integrable functions on X.
Assume that the statement f = g a.e. on X is false. Then at least one of the two
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

78 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
sets E = {X : f < g } and F = {X : f > g } has a positive measure. Consider the
case µ(E) > 0. Now since both f and g are real-valued, we have
E =
⋃
k∈N
Ek where Ek = E =
{
X : g − f ≥ 1
k
}
.
Then 0 < µ (E) ≤ ∑
k∈N µ(Ek). Thus there exists k0 ∈N such that µ(Ek0) > 0, so
that ∫
Ek0
(g − f )dµ ≥ 1
k0
µ(Ek0) > 0.
Therefore ∫
Ek0
gdµ ≥
∫
Ek0
f dµ + 1
k0
µ(Ek0) >
∫
Ek0
f dµ.
This is a contradiction. Thus µ(E) = 0. Similarly, µ(F ) = 0. This shows that f = g
a.e. on X.
• Case 2: General case, where f and g are two extended real-valued integrable
functions on X. The integrability of f and g implies that f and g are real-valued
a.e. on X. Thus there exists a null set N ⊂ X such that f and g are real-valued on
X \ N . Set
¯f =
{
f on X \ N,
0 on N. and ¯ g =
{
g on X \ N,
0 on N.
Then ¯f and ¯g are real-valued on X, and so on every E ∈ A we have
∫
E
¯f dµ =
∫
E
f dµ =
∫
E
¯gdµ =
∫
E
gdµ.
By the ﬁrst part of the proof, we have ¯f = ¯g a.e. on X. Since ¯f = f a.e. on X
and ¯g = g a.e. on X, we deduce that
f = g a.e. on X. ■
Problem 65
Let (X, A, µ) be a σ-ﬁnite measure space and let f, g be extended real-valued
measurable functions on X. Show that if
∫
E f dµ =
∫
E gdµ for every E ∈ A then
f = g a.e. on X. (Note that the integrability of f and g is not assumed.)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

79
Solution
The space ( X, A, µ) is σ-ﬁnite :
X =
⋃
n∈N
Xn, µ (Xn) < ∞, ∀n ∈N and {Xn : n ∈N} are disjoint .
To show f = g a.e. on X it suﬃces to show f = g a.e. on each Xn (since countable
union of null sets is a null set).
Assume that the conclusion is false, that is if E = {Xn : f < g } and F = {Xn :
f > g } then at least one of the two sets has a positive measure. Without lost of
generality, we may assume µ(E) > 0.
Now, E is composed of three disjoint sets:
E(1) = {Xn : −∞ < f < g < ∞},
E(2) = {Xn : −∞ < f < g = ∞},
E(3) = {Xn : −∞ = f < g < ∞}.
Since µ(E) > 0, at least one of these sets has a positive measure.
1. µ(E(1)) > 0. Let
E(1)
m,k,l = {Xn : −m ≤ f ; f + 1
k ≤ g ; g ≤ l}.
Then
E(1) =
⋃
n∈N
⋃
k∈N
⋃
l∈N
E(1)
m,k,l.
By assumption and the subadditivity of µ we have
0 < µ(E(1) ≤
∑
m,k,l∈N
µ(E(1)
m,k,l).
This implies that there are some m0, k0, l0 ∈N such that
µ(Em0,k0,l0) > 0.
Let E∗ = Em0,k0,l0 then we have
∫
E∗
(g − f )dµ ≥ 1
k0
µ(E∗) > 0 so
∫
E∗
gdµ >
∫
E∗
f dµ.
This is a contradiction.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

80 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
2. µ(E(2)) > 0. Let
E(2)
l = {Xn : −∞ < f ≤ l; g = ∞}.
Then
E(2) =
⋃
l∈N
E(2)
l .
By assumption and the subadditivity of µ we have
0 < µ(E(2)) ≤
∑
l∈N
µ(E(2)
l ).
This implies that there is some l0 ∈N such that
µ(E(2)
l0 ) > 0.
Let E∗∗ = E(2)
l0 . Then
∫
E∗∗
gdµ = ∞ >
∫
E∗∗
f dµ.
This contradicts the assumption that
∫
E f dµ =
∫
E gdµ for every E ∈ A.
3. µ(E(3)) > 0. Let
E(2)
m = {Xn : −∞ = f ; −m ≤ g < ∞}.
Then
E(3) =
⋃
m∈N
E(3)
m .
By assumption and the subadditivity of µ we have
0 < µ(E(3)) ≤
∑
m∈N
µ(E(3)
m ).
This implies that there is some m0 ∈N such that
µ(E(3)
m0) > 0.
Let E∗∗∗ = E(3)
m0. Then
∫
E∗∗∗
gdµ ≥ −mµ(E∗∗∗) > −∞ =
∫
E∗∗∗
f dµ :
This contradicts the assumption.
Thus, µ(E) = 0. Similarly, we get µ(F ) = 0. That is f = g a.e. on X. ■.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

81
Problem 66
Given a measure space (X, A, µ). Let f be extended real-valued measurable and
integrable function on X.
1. Show that for any ε > 0 there exists δ > 0 such that if A ∈ A with µ(A) < δ
then ⏐⏐⏐⏐
∫
A
f dµ
⏐⏐⏐⏐ < ε.
2. Let (En) be a sequence in A such that limn→∞ µ(En) = 0 . Show that
limn→∞
∫
En
f dµ = 0.
Solution
1. For every n ∈N, set
fn(x) =
{
f (x) if f (x) ≤ n
n otherwise.
Then the sequence ( fn) is increasing. Each fn is bounded and fn → f pointwise.
By the Monotone Convergence Theorem,
∀ε > 0, ∃N ∈N such that
⏐⏐⏐⏐
∫
X
fN dµ −
∫
X
f dµ
⏐⏐⏐⏐ < ε
2 .
Take δ = ε
2N . If µ(A) < δ , we have
⏐⏐⏐⏐
∫
A
f dµ
⏐⏐⏐⏐ ≤
⏐⏐⏐⏐
∫
A
(fN − f )dµ
⏐⏐⏐⏐ +
⏐⏐⏐⏐
∫
A
fN dµ
⏐⏐⏐⏐
≤
⏐⏐⏐⏐
∫
X
(fN − f )dµ
⏐⏐⏐⏐ + N µ(A)
< ε
2 + ε
2δ δ = ε.
2. Since lim n→∞ µ(En) = 0, with ε and δ as above, there exists n0 ∈N such that
for n ≥ n0, µ (En) < δ . Then we have
⏐⏐⏐⏐
∫
En
f dµ
⏐⏐⏐⏐ < ε.
This shows that lim n→∞
∫
En
f dµ = 0. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

82 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
Problem 67
Given a measure space (X, A, µ). Let f be extended real-valued A-measurable
and integrable function on X. Let En = {x ∈ X : |f (x)| ≥ n} for n ∈N. Show
that limn→∞ µ(En) = 0 .
Solution
First we note that X = E0. For each n ∈N, we have
En \ En+1 = {X : n ≤ |f | < n + 1}.
Moreover, the collection {En \ En+1 : n ∈N} ⊂ A consists of measurable disjoint
sets and ∞⋃
n=0
(En \ En+1) = X.
By the integrability of f we have
∞ >
∫
X
|f |dµ =
∞∑
n=0
∫
En\En+1
|f |dµ ≥
∞∑
n=0
nµ(En \ En+1).
Some more calculations for the last summation:
∞∑
n=0
nµ(En \ En+1) =
∞∑
n=0
n[µ(En) − µ(En+1)]
= µ(E1) − µ(E2) + 2[µ(E2) − µ(E3)] + 3[µ(E3) − µ(E4)] + ...
=
∞∑
n=1
µ(En) < ∞.
Since the series ∑∞
n=1 µ(En) converges, lim n→∞ µ(En) = 0 . ■
Problem 68
Let (X, A, µ) be a measure space.
(a) Let {En : n ∈N} be a disjoint collection in A. Let f be an extended real-
valued A-measurable function deﬁned on ⋃
n∈N En. If f is integrable on En for
every n ∈N, does
∫
⋃
n∈N En
f dµ exist?
(b) Let (Fn : n ∈N) be an increasing sequence in A. Let f be an extended real-
valued A-measurable function deﬁned on ⋃
n∈N Fn. Suppose f is integrable on En
for every n ∈ N and moreover limn→∞
∫
Fn
f dµ exists in R. Does
∫
⋃
n∈N Fn
f dµ
exist?
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

83
Solution
(a) NO.
X = [1, ∞), E n = [n, n + 1), n = 1, 2, ..., {En} disjoint.
A = ML, µ L.
X =
⋃
n∈N
En, f (x) = 1 , ∀x ∈ X.
∫
En
f dµ = 1, ∀n ∈N,
∫
⋃
n∈N En
f dµ =
∫
[1,∞)
1dµ = ∞.
(b) NO.
X =R, F n = (−n, n), n = 1, 2, ..., (Fn : n ∈N) increasing
A = ML, µ L.
X =
⋃
n∈N
Fn, f (x) = 1 for x ≥ 0, f (x) = −1 for x < 0
∫
Fn
f dµ =
∫
(−n,0)
(−1)dµ +
∫
[0,n)
1dµ = 0 ⇒ lim
n→∞
∫
Fn
f dµ = 0
∫
⋃
n∈N Fn
f dµ =
∫
R
f dµ =
∫
(−∞,0)
(−1)dµ +
∫
(0,∞)
1dµ does not exist. ■
Problem 69
Let f is a real-valued uniformly continuous function on [0, ∞). Show that if f
is Lebesgue integrable on [0, ∞), then
lim
x→∞
f (x) = 0 .
Solution
Suppose NOT. Then there exists ε > 0 such that for each n ∈N, there is xn > n
such that |f (xn)| ≥ ε. W.L.O.G. we may choose ( xn) such that
xn+1 > x n + 1 for all n ∈N.
Since f is uniformly continuous on [0 , ∞), with the above ε,
∃δ ∈ (0, 1
2 ) : |x − y| < δ ⇒ | f (x) − f (y)| < ε
2 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

84 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
In particular, for x ∈ In = (xn − δ, xn + δ), we have
|f (xn) − f (x)| < ε
2 , ∀n ∈N.
This implies
|f (xn)| − |f (x)| < ε
2 ⇒ | f (x)| > |f (xn)| − ε
2 ≥ ε − ε
2 = ε
2 .
Since xn+1 − xn > 1 and 0 < δ < 1
2 , I n ∩ In+1 = ∅. Moreover, ⋃∞
n=1 In ⊂ [0, ∞).
By assumption, f is integrable on [0 , ∞), so we have
∞ >
∫
[0,∞)
f dµ ≥
∞∑
n=1
∫
In
f dµ >
∞∑
n=1
∫
In
ε
2 dµ = ∞.
This is a contradiction. Thus,
lim
x→∞
f (x) = 0 . ■
Problem 70
Let (X, A, µ) be a measure space and let (fn)n∈N, and f, g be extended real-valued
A-measurable and integrable functions on D ∈ A. Suppose that
1. limn→∞ fn = f a.e. on D.
2. limn→∞
∫
D fndµ =
∫
D f dµ.
3. either fn ≥ g on D for all n ∈N or fn ≤ g on D for all n ∈N.
Show that, for every E ∈ A and E ⊂ D, we have
lim
n→∞
∫
E
fndµ =
∫
E
f dµ.
Solution
(a) First we solve the problem in the case the condition 3. is replaced by fn ≥ 0 on
D for all n ∈N.
Let hn = fn − fnχE for every E ∈ A and E ⊂ D. Then hn ≥ 0 and A-measurable
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

85
and integrable on D. Applying Fatou’s lemma to hn and using assumptions, we get
∫
D
f dµ −
∫
E
f dµ =
∫
D
(f − f χE)dµ ≤ lim inf
n→∞
∫
D
(fn − fnχE)dµ
= lim
n→∞
∫
D
fndµ − lim sup
n→∞
∫
D
fnχEdµ
=
∫
D
f dµ − lim sup
n→∞
∫
E
fndµ.
Since f is integrable on D,
∫
D f dµ < ∞. From the last inequality we obtain,
(∗) lim sup
n→∞
∫
E
fndµ ≤
∫
E
f dµ.
Let kn = fn + fnχE for every E ∈ A and E ⊂ D. Using the same way as in the
previous paragraph, we get
(∗∗)
∫
E
f dµ ≤ lim inf
n→∞
∫
E
fndµ.
From (*) and (**) we get
lim
n→∞
∫
E
fndµ =
∫
E
f dµ. ■
Next we are coming back to the problem. Assume fn ≥ g on D for all n ∈N. Let
ϕn = fn − g. Using the above result for ϕn ≥ 0 we get
lim
n→∞
∫
E
ϕndµ =
∫
E
ϕdµ.
That is
lim
n→∞
∫
E
(fn − g)dµ =
∫
E
(f − g)dµ
lim
n→∞
∫
E
fndµ −
∫
E
gdµ =
∫
E
f dµ −
∫
E
gdµ.
Since g is integrable on E,
∫
E gdµ < ∞. Thus, we have
lim
n→∞
∫
E
fndµ =
∫
E
f dµ. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

86 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
Problem 71 (An extension of the Dominated Convergence Theorem)
Let (X, A, µ) be a measure space and let (fn)n∈N, (gn)n∈N, and f, g be extended
real-valued A-measurable functions on D ∈ A. Suppose that
1. limn→∞ fn = f and limn→∞ gn = g a.e. on D.
2. (gn) and g are all integrable on D and limn→∞
∫
D gndµ =
∫
D gdµ.
3. |fn| ≤ gn on D for every n ∈N.
Prove that f is integrable on D and limn→∞
∫
D fndµ =
∫
D f dµ.
Solution
Consider the sequence ( gn − fn). Since |fn| ≤ gn, and ( fn) and ( gn) are sequences
of measurable functions, the sequence ( gn − fn) consists of non-negative measurable
functions. Using the Fatou’s lemma we have
∫
D
lim inf
n→∞
(gn − fn)dµ ≤ lim inf
n→∞
∫
D
(gn − fn)dµ
∫
D
lim
n→∞
(gn − fn)dµ ≤ lim
n→∞
∫
D
gndµ − lim sup
n→∞
∫
D
fndµ
∫
D
gdµ −
∫
D
f dµ ≤
∫
D
gdµ − lim sup
n→∞
∫
D
fndµ
∫
D
f dµ ≥ lim sup
n→∞
∫
D
fndµ. (∗) (since
∫
D
gdµ < ∞).
Using the same process for the sequence ( gn + fn), we have
∫
D
f dµ ≤ lim inf
n→∞
∫
D
fndµ. (∗∗).
From (*) and (**) we obtain
lim
n→∞
∫
D
fndµ =
∫
D
f dµ.
The fact that f is integrable comes from gn is integrable:
|fn| ≤ gn ⇒
∫
D
fndµ ≤
∫
D
gndµ < ∞
⇒
∫
D
f dµ < ∞. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

87
Problem 72
Given a measure space (X, A, µ). Let (fn)n∈N and f be extended real-valued
A-measurable and integrabe functions on D ∈ A. Suppose that
lim
n→∞
fn = f a.e. on D.
(a) Show that if limn→∞
∫
D |fn|dµ =
∫
D |f |dµ, then limn→∞
∫
D fndµ =
∫
D f dµ.
(b) Show that the converse of (a) is false by constructing a counter example.
Solution
(a) We will use Problem 71 for
gn = 2(|fn| + |gn|) and hn = |fn − f | + |fn| − |f |, n ∈N.
We have
hn → 0 a.e. on D,
gn → 4|f | a.e. on D,
|hn| = hn ≤ 2|fn| ≤ gn,
lim
n→∞
∫
D
gndµ = 2 lim
n→∞
∫
D
|fn|dµ + 2
∫
D
|f |dµ =
∫
D
4|f |dµ.
So all conditions of Problem 71 are satisﬁed. Therefore,
lim
n→∞
∫
D
hndµ =
∫
D
hdµ = 0 ( h = 0).
lim
n→∞
∫
D
|fn − f |dµ + lim
n→∞
∫
D
|fn|dµ −
∫
D
|f |dµ = 0.
Since lim n→∞
∫
D |fn|dµ −
∫
D |f |dµ = 0 by assumption, we have
lim
n→∞
∫
D
|fn − f |dµ = 0.
This implies that
lim
n→∞
⏐⏐⏐⏐
∫
D
fndµ −
∫
D
f dµ
⏐⏐⏐⏐ = 0.
Hence, lim n→∞
∫
D fndµ =
∫
D f dµ.
(b) We will give an example showing that it is not true that
lim
n→∞
∫
D
fndµ =
∫
D
f dµ ⇒ lim
n→∞
∫
D
|fn|dµ =
∫
D
|f |dµ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

88 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
fn(x) =



n if 0 ≤ x < 1
n
0 if 1
n ≤ x ≤ 1 − 1
n
−n if 1 − 1
n < x ≤ 1.
And so
|fn|(x) =
{
n if 0 ≤ x < 1
n or 1 − 1
n < x ≤ 1
0 if 1
n ≤ x ≤ 1 − 1
n .
Then we have
fn → 0 ≡ 0 and
∫
[0,1]
fndµ = 0 → 0 =
∫
[0,1]
0dµ
while ∫
[0,1]
|fn|dµ = 2 → 2 ⁄= 0. ■
Problem 73
Given a measure space (X, A, µ).
(a) Show that an extended real-valued integrable function is ﬁnite a.e. on X.
(b) If (fn)n∈N is a sequence of measurable functions deﬁned on X such that∑
n∈N
∫
X |fn|dµ < ∞, then show that ∑
n∈N fn converges a.e. to an integrable
function f and ∫
X
∑
n∈N
fndµ =
∫
X
f dµ =
∑
n∈N
∫
X
fndµ.
Solution
(a) Let E = {X : |f | = ∞}. We want to show that µ(E) = 0. Assume that
µ(E) > 0. Since f is integrable
∞ >
∫
X
|f |dµ ≥
∫
E
|f |dµ = ∞.
This is a contradiction. Thus, µ(E) = 0.
(b) First we note that ∑N
n=1 |fn| is measurable since fn is measurable for n ∈ N.
Hence,
lim
N →∞
N∑
n=1
|fn| =
∞∑
n=1
|fn|
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

89
is measurable. Recall that (for nonnegative measurable functions)
∫
X
∞∑
n=1
|fn|dµ =
∞∑
n=1
∫
X
|fn|dµ.
By assumption,
∞∑
n=1
∫
X
|fn|dµ < ∞,
hence, ∫
X
∞∑
n=1
|fn|dµ < ∞.
Since ∑∞
n=1 |fn| is integrable on X, by part (a), it is ﬁnite a.e. on X. Deﬁne a
function f as follows:
f (x) =
{∑∞
n=1 fn where ∑∞
n=1 |fn| < ∞
0 otherwise .
So f is everywhere deﬁned and f = lim N →∞
∑N
n=1 fn a.e. Hence, f is measurable
on X. Moreover,
⏐⏐⏐⏐
∫
X
f dµ
⏐⏐⏐⏐ ≤
∫
X
|f |dµ =
∫
X
⏐⏐⏐⏐⏐
∞∑
n=1
fn
⏐⏐⏐⏐⏐ dµ ≤
∫
X
∞∑
n=1
|fn|dµ < ∞.
Thus, f is integrable and hN = ∑N
n=1 fn converges to f a.e. and
|hN | ≤
N∑
n=1
|fn| ≤
∞∑
n=1
|fn|
which is integrable. By the D.C.T. we have
∫
X
f dµ =
∫
X
lim
N →∞
hN dµ = lim
N →∞
∫
X
hN
= lim
N →∞
∫
X
N∑
n=1
fndµ = lim
N →∞
N∑
n=1
∫
X
fndµ
=
∞∑
n=1
∫
X
fndµ. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

90 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
Problem 74
Let f be a real-valued Lebesgue measurable function on [0, ∞) such that
1. f is Lebesgue integrable on every ﬁnite subinterval of [0, ∞).
2. limx→∞ f (x) = c ∈R.
Show that
lim
a→∞
1
a
∫
[0,a]
f dµL = c.
Solution
By assumption 2. we can write
(∗) ∀ε > 0, ∃N : x > N ⇒ | f (x) − c| < ε.
Now, for a > N we have
⏐⏐⏐⏐
1
a
∫
[0,a]
f dµL − c
⏐⏐⏐⏐ =
⏐⏐⏐⏐
1
a
∫
[0,a]
(f − c)dµL
⏐⏐⏐⏐
≤ 1
a
∫
[0,a]
|f − c|dµL
= 1
a
(∫
[0,N ]
|f − c|dµL +
∫
[N,a]
|f − c|dµL
)
.
By (*) we have
x ∈ [N, a] ⇒ | f (x) − c| < ε.
Therefore,
(∗∗)
⏐⏐⏐⏐
1
a
∫
[0,a]
f dµL − c
⏐⏐⏐⏐ ≤ 1
a
∫
[0,N ]
|f − c|dµL + (a − N )
a ε.
It is evident that
lim
a→∞
(a − N )
a ε = ε.
By assumption 1., |f − c| is integrable on [0 , N], so
∫
[0,N ] |f − c|dµL is ﬁnite and does
not depend on a. Hence
lim
a→∞
1
a
∫
[0,N ]
|f − c|dµL = 0.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

91
Thus, we can rewrite (**) as
lim
a→∞
⏐⏐⏐⏐
1
a
∫
[0,a]
f dµL − c
⏐⏐⏐⏐ ≤ ε.
Since ε > 0 is arbitrary, this implies that
lim
a→∞
⏐⏐⏐⏐
1
a
∫
[0,a]
f dµL − c
⏐⏐⏐⏐ = 0. ■
Problem 75
Let f be a non-negative real-valued Lebesgue measurable on R. Show that if∑∞
n=1 f (x + n) is Lebesgue integrable on R, then f = 0 a.e. on R.
Solution
Recall these two facts:
1. If fn ≥ 0 is measurable on D then
∫
D (∑∞
n=1 fn) dµ = ∑∞
n=1
∫
D fndµ.
2. If f is deﬁned and measurable on R then
∫
R f (x + h)dµ =
∫
R f (x)dµ.
From these two facts we have
∫
R
( ∞∑
n=1
f (x + n)
)
dµL =
∞∑
n=1
∫
R
f (x + n)dµL
=
∞∑
n=1
∫
R
f (x)dµL.
Since ∑∞
n=1 f (x + n) is Lebesgue integrable on R,
∫
R
( ∞∑
n=1
f (x + n)
)
dµL < ∞.
Therefore,
(∗)
∞∑
n=1
∫
R
f (x)dµL < ∞.
Since
∫
R f (x)dµL ≥ 0, (*) implies that
∫
R f (x)dµL = 0. Thus, f = 0 a.e. on R. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

92 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
Problem 76
Show that the Lebesgue Dominated Convergence Theorem holds if
a.e. convergence is replaced by convergence in measure.
Solution
We state the theorem:
Given a measure space (X, A, µ). Let (fn : n ∈N) be a sequence of extended real-
valued A-measurable functions on D ∈ A such that |fn| ≤ g on D for every n ∈N
for some integrable non-negative extended real-valued A-measurable function g on
D. If fn
µ
− →f on D, then f is integrable on D and
lim
n→∞
∫
D
fndµ =
∫
D
f dµ.
Proof:
Let ( fnk) be any subsequence of ( fn). Then fnk
µ
− →f since fn
µ
− →f . By Riesz
theorem, there exists a subsequence ( fnkl
) of ( fnk) such that fnkl
→ f a.e. on D.
And we have also |fnkl
| ≤ g on D. By the Lebesgue D.C.T. we have
(∗)
∫
D
f dµ = lim
l→∞
∫
D
fnkl
dµ.
Let an =
∫
D fndµ and a =
∫
D f dµ. Then (*) can be written as
lim
l→∞
ankl
= a.
Hence we can say that any subsequence ( ank) of ( an) has a subsequence ( ankl
)
converging to a. Thus, the original sequence, namely ( an), converges to the same
limit (See Problem 51): lim n→∞ an = a. That is,
lim
n→∞
∫
D
fndµ =
∫
D
f dµ. ■
Problem 77
Given a measure space (X, A, µ). Let (fn)n∈N and f be extended real-valued
measurable and integrable functions on D ∈ A.
Suppose that limn→∞
∫
D |fn − f |dµ = 0. Show that
(a) fn
µ
− →f on D.
(b) limn→∞
∫
D |fn|dµ =
∫
D |f |dµ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

93
Solution
(a) Given any ε > 0, for each n ∈N, let En = {D : |fn − f | ≥ ε}. Then
∫
D
|fn − f |dµ ≥
∫
En
|fn − f |dµ ≥ εµ(En).
Since lim n→∞
∫
D |fn − f |dµ = 0, limn→∞ µ(En) = 0. That is fn
µ
− →f on D.
(b) Since fn and f are integrable
∫
D
(|fn| − |f |)dµ =
∫
D
|fn|dµ −
∫
D
|f |dµ ≤
∫
D
|fn − f |dµ.
By this and the assumption, we get
lim
n→∞
(∫
D
|fn|dµ −
∫
D
|f |dµ
)
≤ lim
n→∞
∫
D
|fn − f |dµ = 0.
This implies
lim
n→∞
∫
D
|fn|dµ =
∫
D
|f |dµ. ■
Problem 78
Given a measure space (X, A, µ). Let (fn)n∈N and f be extended real-valued
measurable and integrable functions on D ∈ A. Assume that fn → f a.e. on D
and limn→∞
∫
D |fn|dµ =
∫
D |f |dµ. Show that
lim
n→∞
∫
D
|fn − f |dµ = 0.
Solution
For each n ∈N, let hn = |fn| + |f | − |fn − f |. Then hn ≥ 0 for all n ∈N.
Since fn → f a.e. on D, h n → 2|f | a.e on D. By Fatou’s lemma,
2
∫
D
|f |dµ ≤ lim inf
n→∞
∫
D
(|fn| + |f |)dµ − lim sup
n→∞
∫
D
|fn − f |dµ
= lim
n→∞
∫
D
|fn|dµ + lim
n→∞
∫
D
|f |dµ − lim sup
n→∞
∫
D
|fn − f |dµ
= 2
∫
D
|f |dµ − lim sup
n→∞
∫
D
|fn − f |dµ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

94 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
Since |f | is integrable, we have
lim sup
n→∞
∫
D
|fn − f |dµ ≤ 0. (i)
Now for each n ∈N, let gn = |fn − f | − (|fn| − |f |). Then hn ≥ 0 for all n ∈N.
Since fn → f a.e. on D, g n → 0 a.e on D. By Fatou’s lemma,
0 = lim
n→∞
∫
D
gndµ ≤ lim inf
n→∞
∫
D
|fn − f |dµ − lim sup
n→∞
∫
D
(|fn| − |f |)dµ
≤ lim inf
n→∞
∫
D
|fn − f |dµ − lim
n→∞
∫
D
|fn|dµ + lim
n→∞
∫
D
|f |dµ)
| {z }
=0
.
Hence
lim inf
n→∞
∫
D
|fn − f |dµ ≥ 0. (ii)
From (i) and ( ii) it follows that
lim
n→∞
∫
D
|fn − f |dµ = 0. ■
Problem 79
Let (R, ML, µL) be the Lebesgue space. Let f be an extended real-valued Lebesgue
measurable function on R. Show that if f is integrable on R then
lim
h→0
∫
R
|f (x + h) − f (x)|dx = 0.
Solution
Since f is integrable,
lim
M →∞
(∫ −M
−∞
|f |dx +
∫ ∞
M
|f |dx
)
= 0 for M ∈R.
Given any ε > 0, we can pick an M > 0 such that
∫ −M
−∞
|f |dx +
∫ ∞
M
|f |dx < ε
4 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

95
Since Cc(R) is dense in L1(R), we can ﬁnd a continuous function ϕ vanishing outside
[−M, M ] such that ∫ M
−M
|f − ϕ|dx < ε
4 .
Then we have
‖f − ϕ‖1 :=
∫
R
|f − ϕ|dx
=
∫ M
−M
|f − ϕ|dx +
∫ −M
−∞
|f |dx +
∫ ∞
M
|f |dx
< ε
4 + ε
4 = ε
2 .
(Recall: ϕ = 0 outside [ −M, M ] ). Now for any h ∈R we have
‖f (x + h) − f (x)‖1 ≤ ‖f (x) − ϕ(x)‖1 + ‖ϕ(x) − ϕ(x + h)‖1 + ‖ϕ(x + h) − f (x + h)‖1.
Because of ϕ ∈ Cc(R) and translation invariance, we have
lim
h→0
‖ϕ(x) − ϕ(x + h)‖1 = 0 and ‖ϕ(x + h) − f (x + h)‖1 = ‖f (x) − ϕ(x)‖1.
It follows that
lim
h→0
‖f (x + h) − f (x)‖1 ≤ ‖ f − ϕ‖1 + lim
h→0
‖ϕ(x) − ϕ(x + h)‖1 + ‖f − ϕ‖1
≤ 2 ε
2 + 0 = ε.
Since ε > 0 is arbitrary, we have
lim
h→0
‖f (x + h) − f (x)‖1 = lim
h→0
∫
R
|f (x + h) − f (x)|dx = 0. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

96 CHAPTER 7. INTEGRATION OF MEASURABLE FUNCTIONS
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 8
Signed Measures and
Radon-Nikodym Theorem
1. Signed measure
Deﬁnition 21 (Signed measure)
A signed measure on a measurable space (X, A) is a function λ : A → [−∞, ∞] such that:
(1) λ(∅) = 0 .
(2) λ assumes at most one of the values ±∞.
(3) λ is countably additive. That is, if {En}n∈N ⊂ A is disjoint, then
λ
( ⋃
n∈N
En
)
=
∑
n∈N
λ(En).
Deﬁnition 22 (Positive, negative, null sets)
Let (X, A, λ) be a signed measure space. A set E ∈ A is said to be positive (negative, null) for the
signed measure λ if
F ∈ A, F ⊂ E =⇒ λ(F ) ≥ 0 ( ≤ 0, = 0).
Proposition 21 (Continuity)
Let (X, A, λ) be a signed measure space.
1. If (En)n∈N ⊂ A is an increasing sequence then
lim
n→∞
λ(En) = lim
n→∞
λ
( ⋃
n∈N
En
)
= λ
(
lim
n→∞
En
)
.
2. If (En)n∈N ⊂ A is an decreasing sequence and λ(E1) < ∞, then
lim
n→∞
λ(En) = lim
n→∞
λ
( ⋂
n∈N
En
)
= λ
(
lim
n→∞
En
)
.
97
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

98 CHAPTER 8. SIGNED MEASURES AND RADON-NIKODYM THEOREM
Proposition 22 (Some more properties)
Let (X, A, λ) be a signed measure space.
1. Every measurable subset of a positive (negative, null) set is a positive (negative, null) set.
2. If E is a positive set and F is a negative set, then E ∩ F is a null set.
3. Union of positive (negative, null) sets is a positive (negative, null) set.
Theorem 10 (Hahn decomposition theorem)
Let (X, A, λ) be a signed measure space. Then there is a positive set A and a negative set B such
that
A ∩ B =∅ and A ∪ B = X.
Moreover, if A′ and B′ are another pair, then A ∆ A′ and B ∆ B′ are null sets.
{A, B} is called a Hahn decomposition of (X, A, λ).
Deﬁnition 23 (Singularity)
Two signed measure λ1 and λ2 on a measurable space (X, A) are said to be mutually singular and
we write λ1⊥λ2 if there exist two set E, F ∈ A such that E ∩ F =∅, E ∪ F = X, E is a null set
for λ1 and F is a null set for λ2.
Deﬁnition 24 (Jordan decomposition)
Given a signed measure space (X, A, λ). If there exist two positive measures µ and ν, at least one
of which is ﬁnite, on the measurable (X, A) such that
µ⊥ν and λ = µ − ν,
then {µ, ν} is called a Jordan decomposition of λ.
Theorem 11 (Jordan decomposition of signed measures)
Given a signed measure space (X, A, λ). A Jordan decomposition for (X, A, λ) exists and unique,
that is, there exist a unique pair {µ, ν} of positive measures on (X, A), at least one of which is
ﬁnite, such that µ⊥ν and λ = µ − ν.
Moreover, with any arbitrary Hahn decomposition {A, B} of (X, A, λ), if we deﬁne two set functions
µ and ν by setting
µ(E) = λ(E ∩ A) and ν(E) = −λ(E ∩ B) for E ∈ A,
then {µ, ν} is a Jordan decomposition for (X, A, λ).
2. Lebesgue decomposition, Radon-Nikodym Theorm
Deﬁnition 25 (Radon-Nikodym derivative)
Let µ be a positive measure and λ be a signed measure on a measurable space (X, A). If there exists
an extended real-valued A-measurable function f on X such that
λ(E) =
∫
E
f dµ for every E ∈ A,
then f is called a Radon-Nikodym derivative of λ with respect to µ, and we write dλ
dµ for it.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

99
Proposition 23 (Uniqueness)
Let µ be a σ-ﬁnite positive measure and λ be a signed measure on a measurable space (X, A). If
two extended real-valued A-measurable functions f and g are Radon-Nikodym derivatives of λ with
respect to µ, then f = g µ -a.e. on X.
Deﬁnition 26 (Absolute continuity)
Let µ be a positive measure and λ be a signed measure on a measurable space (X, A). We say that
λ is absolutely continuous with respect to µ and write λ ≪ µ if
∀E ∈ A), µ (E) = 0 =⇒ λ(E) = 0 .
Deﬁnition 27 (Lebesgue decomposition)
Let µ be a positive measure and λ be a signed measure on a measurable space (X, A). If there exist
two signed measures λa and λs on (X, A) such that
λa ≪ µ, λ s⊥µ and λ = λa + λs,
then we call {λa, λs} a Lebesgue decomposition of λ with respect to µ. We call λa and λs the
absolutely continuous part and the singular part of λ with respect to µ.
Theorem 12 (Existence of Lebesgue decomposition)
Let µ be a σ-ﬁnite positive measure and λ be a σ-ﬁnite signed measure on a measurable space
(X, A). Then there exist two signed measures λa and λs on (X, A) such that
λa ≪ µ, λ s⊥µ, λ = λa + λs and λa is deﬁned by λa(E) =
∫
E
f dµ, ∀E ∈ A,
where f is an extended real-valued measurable function on X.
Theorem 13 (Radon-Nikodym theorem)
Let µ be a σ-ﬁnite positive measure and λ be a σ-ﬁnite signed measure on a measurable space
(X, A). If λ ≪ µ, then the Radon-Nikodym derivative of λ with respect to µ exists, that is, there
exists an extended real-valued measurable function on X such that
λ(E) =
∫
E
f dµ, ∀E ∈ A.
∗ ∗ ∗∗
Problem 80
Given a signed measure space (X, A, λ). Suppose that {µ, ν} is a Jordan de-
composition of λ, and E and F are two measurable subsets of X such that
E ∩ F =∅, E ∪ F = X, E is a null set for ν and F is a null set for ν.Show
that {E, F } is a Hahn decomposition for (X, A, λ).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

100 CHAPTER 8. SIGNED MEASURES AND RADON-NIKODYM THEOREM
Solution
We show that E is a positive set for λ and F is a negative set for λ. Since {µ, ν} is
a Jordan decomposition of λ, we have
λ(E) = µ(E) − ν(E), ∀E ∈ A.
Let E0 ∈ A , E 0 ⊂ E. Since E is a null set for ν, E 0 is also a null set for ν. Thus
ν(E0) = 0. Consequently, λ(E0) = µ(E0) ≥ 0. This shows that E is a positive set
for λ.
Similarly, let F0 ∈ A , F 0 ⊂ E. Since F is a null set for µ, F 0 is also a null set for
µ. Thus µ(F0) = 0. Consequently, λ(F0) = −ν(F0) ≤ 0. This shows that F is a
negative set for λ.
We conclude that {E, F } is a Hahn decomposition for ( X, A, λ). ■
Problem 81
Consider a measure space ([0, 2π], ML ∩ [0, 2π], µL). Deﬁne a signed measure λ
on this space by setting
λ(E) =
∫
E
sin xdµL, for E ∈ ML ∩ [0, 2π].
Let C = [ 4
3 π, 5
3 π]. Let ε > 0 be arbitrary given. Find a measurable set C ′ ⊂ C
such that λ(C ′) ≥ λ(C) and λ(E) > −ε for every measurable subset E of C ′.
Solution
Let X = [0 , 2π], f (x) = sin x. Then f is continuous on X, so f is Lebesgue
(=Riemann) integrable on X. Given ε > 0, let δ = min{ ε
2 , π
3 }. Let C ′ = [ 4
3 π, 4
3 π +δ],
then
C ′ ⊂ C and f (x) = sin x < 0, x ∈ C ′.
We have
λ(C ′) =
∫
C′
sin xdµL ≥
∫
C
sin xdµL = λ(C).
Now for any E ⊂ C ′ and E ∈ M L ∩ [0, 2π], since µ(E) ≤ µ(C ′) and f (x) ≤ 0 on
C ′, we have
λ(E) =
∫
E
sin xdµL ≥
∫
C′
sin xdµL ≥
∫
C′
(−1)dµL = −µ(C ′) = −δ.
By the choice of δ, we have
δ < ε
2 ⇒ − δ > − ε
2 > −ε.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

101
Thus, for any E ∈ M L ∩ [0, 2π] with E ⊂ C ′ we have λ(E) > −ε. ■
Problem 82
Given a signed measure space (X, A, λ).
(a) Show that if E ∈ A and λ(E) > 0, then there exists a subset E0 ⊂ E which
is a positive set for λ with λ(E0) ≥ λ(E).
(b) Show that if E ∈ A and λ(E) < 0, then there exists a subset E0 ⊂ E which
is a negative set for λ with λ(E0) ≤ λ(E).
Solution
(a) If E is a positive set for λ then we’re done (just take E0 = E).
Suppose E is a not positive set for λ. Let {A, B} be a Hahn decomposition of
(X, A, λ). Let E0 = E ∩ A. Since A is a positive set, so E0 is also a positive set (for
E0 ⊂ A). Moreover,
λ(E) = λ(E ∩ A) + λ(E ∩ B) = λ(E0) + λ(E ∩ B).
Since λ(E ∩ B) ≤ 0, 0 < λ(E) ≤ λ(E0). Thus, E0 = E ∩ A is the desired set.
(b) Similar argument. Answer: E0 = E ∩ B. ■
Problem 83
Let µ and ν two positive measures on a measurable space (X, A). Suppose for
every ε > 0, there exists E ∈ A such that µ(E) < ε and ν(Ec) < ε . Show that
µ⊥ν.
Solution
Recall: For positive measures µ and ν
µ⊥ν ⇔ ∃ A ∈ A : µ(A) = 0 and ν(Ac) = 0 .
By hypothesis, for every n ∈N, there exists En ∈ A such that
µ(En) < 1
n2 and ν(Ec
n) < 1
n2 .
Hence, ∑
n∈N
µ(En) ≤
∑
n∈N
1
n2 < ∞ and
∑
n∈N
ν(Ec
n) ≤
∑
n∈N
1
n2 < ∞.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

102 CHAPTER 8. SIGNED MEASURES AND RADON-NIKODYM THEOREM
By Borel-Cantelli’s lemma we get
µ
(
lim sup
n→∞
En
)
= 0 and ν
(
lim sup
n→∞
Ec
n
)
= 0.
Let A = lim supn→∞ En. Then µ(A) = 0. (*)
We claim: Ac = lim inf n→∞ Ec
n. Recall:
lim inf
n→∞
An = {x ∈ X : x ∈ An for all but ﬁnitely many n ∈N}.
For every x ∈ X, for each n ∈N, we have either x ∈ En or x ∈ Ec
n. If x ∈ En for
inﬁnitely many n, then x ∈ lim supn→∞ En and vice versa. Otherwise, x ∈ En for
a ﬁnite numbers of n. But this is equivalent to x ∈ Ec
n for all but ﬁnitely many n.
That is x ∈ lim infn→∞ Ec
n. Hence,
lim sup
n→∞
En ∪ lim inf
n→∞
Ec
n = X.
Now, if x ∈ lim supn→∞ En then x ∈ En for inﬁnitely many n, so x /∈ lim infn→∞ Ec
n.
This shows that
lim sup
n→∞
En ∩ lim inf
n→∞
Ec
n = ∅.
Thus, Ac = lim inf n→∞ Ec
n as required.
Last, we show that ν(Ac) = 0. Since lim inf n→∞ Ec
n ⊂ lim supn→∞ Ec
n and ν (lim supn→∞ Ec
n) =
0 (by the ﬁrst paragraph), we get
ν(lim inf
n→∞
Ec
n) = ν(Ac) = 0 . (∗∗)
From (*) and (**) we obtain µ⊥ν. ■
Problem 84
Consider the Lebesgue measure space (R, ML, µL). Let ν be the counting measure
on ML, that is, ν is deﬁned by setting ν(E) to be equal to the numbers of elements
in E ∈ M L if E is a ﬁnite set and ν(E) = ∞ if E is inﬁnite set.
(a) Show that µL ≪ ν but dµL
dν does not exist.
(b) Show that ν does not have a Lebesgue decomposition with respect to µL.
Solution
(a) Let E ⊂ R with ν(E) = 0. Since ν be the counting measure, E = ∅. Then
µL(E) = µL(∅) = 0. Thus,
E ⊂R, ν (E) = 0 ⇒ µL(E) = 0 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

103
Hence, µL ≪ ν.
Suppose there exists a measurable function f such that
mL(E) =
∫
E
f dν for every E ∈ M L.
Take E = {x}, x ∈R then we have
E ∈ M L, µ L(E) = 0 , and ν(E) = 1 .
This implies that f ≡ 0. Then for every A ∈ M L we have
µL(A) =
∫
A
0dν = 0.
This is impossible.
(b) Assume that ν have a Lebesgue decomposition with respect to µL. Then, for
every E ⊂R and some measurable function f ,
ν = νa + νs, ν a ≪ µL, ν s⊥µL, and νa(E) =
∫
E
f dµL.
Since νs⊥µL, there exists A ∈ M L such that µL(Ac) = 0 and A is a null set for νs.
Pick a ∈ A then νs({a}) = 0. On the other hand,
νa({a}) =
∫
{a}
f dµL and µL({a}) = 0 .
It follows that νa({a}) = 0. Since ν = νa + νs, we get
1 = ν({a}) = νa({a}) + νs({a}) = 0 + 0 = 0 .
This is a contradiction. Thus, ν does not have a Lebesgue decomposition with
respect to µL. ■
Problem 85
Let µ and ν be two positive measures on a measurable space (X, A).
(a) Show that if for every ε > 0 there exists δ > 0 such that ν(E) < ε for every
E ∈ A with µ(E) < δ , then ν ≪ µ.
(b) Show that if ν is a ﬁnite positive measure, then the converse of (a) holds.
Solution
(a) Suppose this statement is true: (*):= for every ε > 0 there exists δ > 0 such
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

104 CHAPTER 8. SIGNED MEASURES AND RADON-NIKODYM THEOREM
that ν(E) < ε for every E ∈ A with µ(E) < δ .
Take E ∈ A with µ(E) = 0. Then
∀ε > 0, ν (E) < ε.
It follows that ν(E) = 0. Hence ν ≪ µ.
(b) Suppose ν is a ﬁnite positive measure and µ is a positive measure such that
ν ≪ µ. We want to show (*) is true. Assume that (*) is false. that is
∃ε > 0 st
[
∀δ > 0, ∃E ∈ A st {µ(E) < δ and ν(E) ≥ ε}
]
.
In particular,
∃ε > 0 st
[
∀n ∈N, ∃En ∈ A st {µ(En) < 1
n2 and ν(En) ≥ ε}
]
Since ∑
n∈N µ(En) ≤ ∑
n∈N
1
n2 < ∞, by Borel-Catelli lemma, we have
µ(lim sup
n→∞
En) = 0 .
Set E = lim sup n→∞ En, then µ(E) = 0. Since ν ≪ µ, ν (E) = 0. Note that
ν(X) < ∞, we have
ν(E) = ν(lim sup
n→∞
En) ≥ lim sup
n→∞
ν(En) ≥ ν(En) ≥ ε.
This is a contradiction. Thus, (*) must be true. ■
Problem 86
Let µ and ν be two positive measures on a measurable space (X, A). Suppose dν
dµ
exists so that ν ≪ µ.
(a) Show that if dν
dµ > 0, µ -a.e. on X, then µ ≪ ν and thus, µ ∼ ν.
(b) Show that if dν
dµ > 0, µ -a.e. on X and if µ and ν are σ-ﬁnite, then dµ
dν exists
and
dµ
dν =
( dν
dµ
)−1
, µ − a.e. and ν − a.e. on X.
Solution
(a) For every E ∈ A, by deﬁnition, we have
ν(E) =
∫
E
dν
dµ dµ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

105
Suppose ν(E) = 0. Since dν
dµ > 0, µ -a.e. on X, we have
∫
E
dν
dµ dµ = 0.
Hence, µ(E) = 0. This implies that µ ≪ ν and so µ ∼ ν (since ν ≪ µ is given).
(b) Suppose dν
dµ > 0, µ -a.e. on X and if µ and ν are σ-ﬁnite. The existence of dµ
dν is
guaranteed by the Radon-Nikodym theorem (since µ ∼ ν by part a). Moreover,
dµ
dν > 0, ν − a.e. on X.
By the chain rule,
dµ
dν . dν
dµ = dµ
dµ = 1, µ − a.e. on X.
dν
dµ . dµ
dν = dν
dν = 1, ν − a.e. on X.
Thus,
dµ
dν =
( dν
dµ
)−1
, µ − a.e. and ν − a.e. on X. ■
Problem 87
Let (X, A, µ) be a measure space. Assume that there exists a measurable function
f : X → (0, ∞) satisfying the condition that µ{x ∈ X : f (x) ≤ n} < ∞ for
every n ∈N.
(a) Show that the existence of such a function f implies that µ is a σ-ﬁnite
measure.
(b) Deﬁne a positive measure ν on A by setting
ν(E) =
∫
E
f dµ for E ∈ A.
Show that ν is a σ-ﬁnite measure.
(c) Show that dµ
dν exists and
dµ
dν = 1
f , µ − a.e. and ν − a.e. on X.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

106 CHAPTER 8. SIGNED MEASURES AND RADON-NIKODYM THEOREM
Solution
(a)By assumption, µ{x ∈ X : f (x) ≤ n} < ∞ for every n ∈N. Since 0 < f < ∞,
so ⋃∞
n=1{X : f ≤ n} = X. Hence µ is a σ-ﬁnite measure.
(b) Let ν(E) =
∫
E f dµ for E ∈ A.
Since f > 0, ν is a positive measure and if µ(E) = 0 then ν(E) = 0. Hence ν ≪ µ.
Conversely, if ν(E) = 0, since f > 0, µ(E) = 0. So µ ≪ ν. Thus, µ ∼ ν. Since µ is
σ-ﬁnite ( by (a)), ν is also σ-ﬁnite.
(c) Since ν is σ-ﬁnite, dµ
dν exists. By part (b), f = dν
dµ . By chain rule,
dµ
dν . dν
dµ = 1, µ − a.e. and ν − a.e. on X.
Thus,
dµ
dν = 1
f , µ − a.e. and ν − a.e. on X. ■
Problem 88
Let µ and ν be σ-ﬁnite positive measures on (X, A). Show that there exist A, B ∈
A such that
A ∩ B =∅, A ∩ B = X, µ ∼ ν on (A, A ∩ A) and µ⊥ν on (B, A ∩ B).
Solution
Deﬁne a σ-ﬁnite measure λ = µ + ν. Then µ ≪ λ and ν ≪ λ. By the Radon-
Nikodym theorem there exist non-negative A-measurable functions f and g such
that for every E ∈ A,
µ(E) =
∫
E
f dλ and ν(E) =
∫
E
gdλ.
Let A = {x ∈ X : f (x)g(x) > 0} and B = Ac. Then µ ∼ ν. Indeed, f > 0 in A.
Thus, if µ(E) = 0, then λ(E) = 0, and therefore, ν(E) = 0. This implies ν ≪ µ.
We can prove µ ≪ ν in the same manner. Hence, µ ∼ ν.
Let C = {x ∈ B : f (x) = 0 }, D = B \ C. For any measurable sets E ⊂ C and
F ⊂ D, µ (E) = ν(F ) = 0. Thus, µ⊥ν on ( B, A ∩ B). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

107
Problem 89
Let µ and ν be σ-ﬁnite positive measures on (X, A). Show that there exists
a non-negative extended real-valued A-measurable function ϕ on X and a set
A0 ∈ A with µ(A0) = 0 such that
ν(E) =
∫
E
ϕdµ + ν(E ∩ A0) for every E ∈ A.
Solution
By the Lebesgue decomposition theorem,
ν = νa + νs, ν a ≪ µ, ν s⊥µ and νa(E) =
∫
E
ϕdµ for any E ∈ A,
where ϕ is a non-negative extended real-valued A-measurable function on X.
Now since νs⊥µ, there exists A0 ∈ A such that
µ(A0) = 0 and νs(Ac
0) = 0 .
Hence [
νa ≪ µ and µ(A0) = 0
]
=⇒ νa(A0) = 0 . (∗)
On the other hand, since νs(E) = νs(E ∩ A0) for every E ∈ A, so we have
ν(E ∩ A0) = νa(E ∩ A0)| {z }
=0 by ( ∗)
+νs(E ∩ A0) = νs(E ∩ A0) = νs(E).
Finally,
ν(E) = νa(E) + νs(E) =
∫
E
ϕdµ + ν(E ∩ A0) for every E ∈ A. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

108 CHAPTER 8. SIGNED MEASURES AND RADON-NIKODYM THEOREM
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 9
Diﬀerentiation and Integration
The measure space in this chapter is the space ( R, ML, µL). Therefore, we write
µ instead of µL for the Lebesgue measure. Also, we say f is integrable (derivable)
instead of f is µL-integrable (derivable).
1. BV functions and absolutely continuous functions
Deﬁnition 28 (Variation of f )
Let [a, b] ⊂R with a < b . A partition of [a, b] is a ﬁnite ordered set P = {a = x0 < x 1 < ... < x n =
b}. For a real-valued function f on [a, b] we deﬁne the variation of f corresponding to a partition
P by
V b
a (f, P) :=
n∑
k=1
|f (xk) − f (xk−1)| ∈ [0, ∞).
We deﬁne the total variation of f on [a, b] by
V b
a (f ) := sup
P
V b
a (f, P) ∈ [0, ∞],
where the supremum is taken over all partitions of [a, b]. We say that f is a function of bounded
variation on [a, b], or simply a BV function, if V b
a (f ) < ∞.
We write BV ([a, b]) for the collection of all BV functions on [a, b].
Theorem 14 (Jordan decomposition of a BV function)
1. A function f is a BV function on [a, b] if and only if there are two real-valued increasing
functions g1 and g2 on [a, b] such that f = g1 − g2 on [a, b].
{g1, g2} is called a Jordan decomposition of f .
2. If a BV function on [a, b] is continuous on [a, b], then g1 and g2 can be chosen to be continuous
on [a, b].
Theorem 15 (Derivability and integrability)
If f is a BV function on [a, b], then f ′ exists a.e. on [a, b] and integrable on [a, b].
109
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

110 CHAPTER 9. DIFFERENTIATION AND INTEGRATION
Deﬁnition 29 (Absolutely continuous functions)
A real-valued function f on [a, b] is said to be absolutely continuous on [a, b] if, given any ε > 0,
there exists a δ > 0 such that
n∑
k=1
|f (bk) − f (ak)| < ε
for every ﬁnite collection {[ak, bk]}1≤k≤n of non-overlapping intervals contained in [a, b] with
n∑
k=1
|bk − ak| < δ.
Theorem 16 (Properties)
If f is an absolutely continuous on [a, b] then
1. f is uniformly continuous on [a, b],
2. f is a BV function on [a, b],
3. f ′ exists a.e. on [a, b],
4. f is integrable on [a, b].
Deﬁnition 30 (Condition (N))
Let f be a real-valued function on [a, b]. We say that f satisﬁes Lusin ’s Condition (N) on [a, b] if
for every E ⊂ [a, b] with µL(E) = 0 , we have µ
(
f (E)
)
= 0.
Theorem 17 (Banach-Zarecki criterion for absolute continuity)
Let f be a real-valued function on [a, b]. Then f is absolutely continuous on [a, b] if and only if it
satisﬁes the following three conditions:
1. f is continuous on [a, b].
2. f is of BV on [a, b].
3. f satisﬁes condition (N) on [a, b].
2. Indeﬁnite integrals and absolutely continuous functions
Deﬁnition 31 (Indeﬁnite integrals)
Let f be a extended real-valued function on [a, b]. Suppose that f is measurable and integrable on
[a, b]. By indeﬁnite integral of f on [a, b] we mean a real-valued function F on [a, b] deﬁned by
F (x) =
∫
[a,x]
f dµ + c, x ∈ [a, b] and c ∈R is a constant .
Theorem 18 (Lebesgue diﬀerentiation theorem)
Let f be a extended real-valued, measurable and integrable function on [a, b]. Let F be an indeﬁnite
integral of f on [a, b]. Then
1. F is absolutely continuous on [a, b],
2. F ′ exists a.e. on [a, b] and F ′ = f a.e. on [a, b],
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

111
Theorem 19 Let f be a real-valued absolutely continuous on [a, b]. Then
∫
[a,x]
f ′dµ = f (x) − f (a), ∀x ∈ [a, b].
Thus, an absolutely continuous function is an indeﬁnite integral of its derivative.
Theorem 20 (A characterization of an absolutely continuous function)
A real-valued function f on [a, b] is absolutely continuous on [a, b] if and only if it satisﬁes the
following conditions:
(i) f ′ exists a.e. on [a, b]
(ii) f ′ is measurable and integrable on [a, b].
(iii)
∫
[a,x] f ′dµ = f (x) − f (a), ∀x ∈ [a, b].
3. Indeﬁnite integrals and BV functions
Theorem 21 (Total variation of F )
Let f be a extended real-valued measurable and integrable function on [a, b]. Let F be an indeﬁnite
integral of f on [a, b] deﬁned by
F (x) =
∫
[a,x]
f dµ + c, x ∈ [a, b].
Then the total variation of F is given by
V b
a (F ) =
∫
[a,b]
|f |dµ.
∗ ∗ ∗∗
Problem 90
Let f ∈ BV ([a, b]). Show that if f ≥ c on [a, b] for some constant c > 0, then
1
f ∈ BV ([a, b]).
Solution
Let P = {a = x0 < x 1 < ... < x n = b} be a partition of [ a, b]. Then
V b
a
( 1
f , P
)
=
n∑
k=1
⏐⏐⏐⏐
1
f (xk) − 1
f (xk−1)
⏐⏐⏐⏐ =
n∑
k=1
|f (xk) − f (xk−1)|
|f (xk)f (xk−1)| .
Since f ≥ c > 0,
|f (xk) − f (xk−1)|
|f (xk)f (xk−1|) ≤ |f (xk) − f (xk−1)|
c2 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

112 CHAPTER 9. DIFFERENTIATION AND INTEGRATION
It follows that
V b
a
( 1
f , P
)
≤ 1
c2
n∑
k=1
|f (xk) − f (xk−1)| = 1
c2 V b
a (f, P) ≤ 1
c2 V b
a (f ).
Since V b
a (f ) < ∞, V b
a
( 1
f
)
< ∞. ■
Problem 91
Let f, g ∈ BV ([a, b]). Show that f g ∈ BV ([a, b]) and
V b
a (f g) ≤ sup
[a,b]
|f |.V b
a (g) + sup
[a,b]
|g|.V b
a (f ).
Solution
Note ﬁrst that f, g ∈ BV ([a, b]) implies that f and g are bounded on [ a, b]. There
are some 0 < M < ∞ and 0 < N < ∞ such that
M = sup
[a,b]
|f | and N = sup
[a,b]
|g|.
For any x, y ∈ [a, b] we have
|f (x)g(x) − f (y)g(y)| ≤ | f (x) − f (y)||g(x)| + |g(x) − g(y)||f (y)|
≤ N |f (x) − f (y)| + M |g(x) − g(y)| (∗).
Now, let P = {a = x0 < x 1 < ... < x n = b} be any partition of [ a, b]. Then we have
V b
a (f g, P) =
n∑
k=1
|f (xk)g(xk) − f (xk−1)g(xk−1)|
≤ M
n∑
k=1
|g(xk) − g(xk−1)| + N
n∑
k=1
|f (xk) − f (xk−1)|
≤ M V b
a (g, P) + N V b
a (f, P).
Since P is arbitrary,
sup
P
V b
a (f g, P) ≤ M sup
P
V b
a (g, P) + N sup
P
V b
a (f, P),
where the supremum is taken over all partitions of [ a, b]. Thus,
V b
a (f g) ≤ sup
[a,b]
|f |.V b
a (g) + sup
[a,b]
|g|.V b
a (f ). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

113
Problem 92
Let f be a real-valued function on [a, b]. Suppose f is continuous on [a, b] and
satisfying the Lipschitz condition, that is, there exists a constant M > 0 such
that
|f (x′) − f (x′′)| ≤ M |x′ − x′′|, ∀x′, x′′ ∈ [a, b].
Show that f ∈ BV ([a, b]) and V b
a (f ) ≤ M (b − a).
Solution
Let P = {a = x0 < x 1 < ... < x n = b} be any partition of [ a, b]. Then
V b
a (f, P) =
n∑
k=1
|f (xk) − f (xk−1)|
≤ M
n∑
k=1
(xk − xk−1)
≤ M (xn − x0) = M (b − a).
This implies that
V b
a (f ) = sup
P
V b
a (f, P) ≤ M (b − a) < ∞. ■
Problem 93
Let f be a real-valued function on [a, b]. Suppose f is continuous on [a, b] and
is diﬀerentiable on (a, b) with |f ′| ≤ M for some constant M > 0. Show that
f ∈ BV ([a, b]) and V b
a (f ) ≤ M (b − a).
Hint:
Show that f satisﬁes the Lipschitz condition.
Problem 94
Let f be a real-valued function on [0, 2
π ] deﬁned by
f (x) =
{
sin 1
x for x ∈ (0, 2
π ]
0 for x = 0.
Show that f /∈ BV ([0, 2
π ]).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

114 CHAPTER 9. DIFFERENTIATION AND INTEGRATION
Solution
Let us choose a particular partition of [0 , 2
π ]:
x1 = 2
π > x 2 = 2
π + 2π > ... > x 2n−1 = 2
π + 2n.2π > x 2n = 0.
Then we have
V
2
π
0 (f, P) = |f (x1) − f (x2)| + |f (x2) − f (x3)| + ... + |f (x2n−1) − f (x2n)|
= 2 + 2 + ... + 2| {z }
2n−1
+1 = (2 n − 1)2 + 1.
Therefore,
sup
P
V
2
π
0 (f, P) = ∞,
where the supremum is taken over all partitions of [0 , 2
π ]. Thus, f is not a BV
function. ■
Problem 95
Let f be a real-valued continuous and BV function on [0, 1]. Show that
lim
n→∞
n∑
i=1
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐
2
= 0.
Solution
Since f is continuous on [0 , 1], which is compact, f is uniformly continuous on [0 , 1].
Hence,
∀ε > 0, ∃N > 0 : |x − y| ≤ 1
N ⇒ | f (x) − f (y)| ≤ ε, ∀x, y ∈ [0, 1].
Partition of [0 , 1]:
x0 = 0 < x 1 = 1
n < x 2 = 2
n < ... < x n = n
n = 1.
For n ≥ N we have
⏐⏐ i
n − i−1
n
⏐⏐ = 1
n ≤ 1
N . Hence,
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐ ≤ ε, i = 1, 2, ...
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

115
Now we can write, for n ≥ N ,
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐
2
=
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐ .
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐
≤ ε
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐ ,
and so
n∑
i=1
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐
2
≤ ε
n∑
i=1
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐ ≤ εV 1
0 (f ).
Since V 1
0 (f ) < ∞, we can conclude that
lim
n→∞
n∑
i=1
⏐⏐⏐⏐f
( i
n
)
− f
( i − 1
n
)⏐⏐⏐⏐
2
= 0. ■
Problem 96
Let (fi : i ∈ N) and f be real-valued functions on an interval [a, b] such that
limi→∞ fi(x) = f (x) for x ∈ [a, b]. Show that
V b
a (f ) ≤ lim inf
i→∞
V b
a (fi).
Solution
Let Pn = {a = x0 < x 1 < ... < x n = b} be a partition of [ a, b]. Then
V b
a (f, Pn) =
n∑
k=1
|f (xk) − f (xk−1)|,
V b
a (fi, Pn) =
n∑
k=1
|fi(xk) − fi(xk−1)| for each i ∈N.
Consider the counting measure space ( N, P(N), ν) where ν is the counting measure.
Let D = {1, 2, ..., n}. Then D ∈ P (N). Deﬁne
gi(k) = |fi(xk) − fi(xk−1)| ≥ 0,
g(k) = |f (xk) − f (xk−1)| for k ∈ D.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

116 CHAPTER 9. DIFFERENTIATION AND INTEGRATION
Since lim i→∞ fi(x) = f (x) for x ∈ [a, b], we have
lim
i→∞
gi(k) = g(k) for every k ∈ D.
By Fatou’s lemma,
∫
D
g(k)dν =
∫
D
lim
i→∞
gi(k)dν ≤ lim inf
i→∞
∫
D
gi(k)dν. (∗)
Since D = ⨆n
k=1{k} (union of disjoint sets), we have
∫
D
g(k)dν =
n∑
k=1
∫
{k}
g(k)dν
=
n∑
k=1
g(k)
=
n∑
k=1
|f (xk) − f (xk−1)|
= V b
a (f, Pn).
Similarly, we get ∫
D
gi(k)dν = V b
a (fi, Pn) for each i ∈N.
With these, we can rewrite (*) as follows:
V b
a (f, Pn) ≤ lim inf
i→∞
V b
a (fi, Pn).
By taking all partitions Pn, we obtain
V b
a (f ) ≤ lim inf
i→∞
V b
a (fi). ■
Problem 97
Let f be a real-valued absolutely continuous function on [a, b]. If f is never zero,
show that 1
f is also absolutely continuous on [a, b].
Solution
The function f is continuous on [ a, b], which is compact, so f has a minimum on it.
Since f is non-zero, there is some m ∈ (0, ∞) such that
min
x∈[a,b]
|f (x)| = m.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

117
Given any ε > 0 there exists δ > 0 such that for any ﬁnite family of non-overlapping
closed intervals {[ai, bi] : i = 1, ..., n} in [ a, b] such that∑n
i=1(bi − ai) < δ we have ∑n
i=1 |f (ai) − f (bi)| < ε. Now,
n∑
i=1
⏐⏐⏐⏐
1
f (ai) − 1
f (bi)
⏐⏐⏐⏐ =
n∑
i=1
|f (ai) − f (bi)|
|f (ai)f (bi)|
≤ 1
m2
n∑
i=1
|f (ai) − f (bi)|
≤ ε
m2 . ■
Problem 98
Let f be a real-valued function on [a, b] satisfying the Lipschitz condition on [a, b].
Show that f is absolutely continuous on [a, b].
Solution
The Lipschitz condition on [ a, b]:
∃K > 0 : ∀x, y ∈ [a, b], |f (x) − f (y)| ≤ K|x − y|.
Given any ε > 0, let δ = ε
K . Let {[ci, di] : i = 1 , ..., n} be a family of non-
overlapping subintervals of [ a, b] with ∑n
i=1(di − ci) < δ , then, by the Lipschitz
condition, we have
n∑
i=1
|f (ck) − f (dk)| ≤
n∑
i=1
K(dk − ck)
≤ K
n∑
i=1
(dk − ck)
< K ε
K = ε.
Thus f is absolutely continuous on [ a, b]. ■
Problem 99
Show that if f is continuous on [a, b] and f ′ exists on (a, b) and satisﬁes
|f ′(x)| ≤ M for x ∈ (a, b) with some M > 0, then f satisﬁes the Lipschitz
condition and thus absolutely continuous on [a, b].
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

118 CHAPTER 9. DIFFERENTIATION AND INTEGRATION
(Hint: Just use the Intermediate Value Theorem.)
Problem 100
Let f be a continuous function on [a, b]. Suppose f ′ exists on (a, b) and satisﬁes
|f ′(x)| ≤ M for x ∈ (a, b) with some M > 0. Show that for every E ⊂ [a, b] we
have
µ∗
L
(
f (E)
)
≤ M µ∗
L(E).
Solution
Recall:
µ∗
L(E) = inf
{ ∞∑
n=1
𝓁(In) : In are open intervals and
∞⋃
n=1
In ⊃ E
}
.
Let E ⊂ [a, b]. Let {In = ( a′
n, b′
n)} be a covering of E, where each ( a′
n, b′
n) ⊂ [a, b].
Then
E ⊂
⋃
n
(a′
n, b′
n) ⇒ f (E) ⊂
⋃
n
f
(
(a′
n, b′
n)
)
.
Since f is continuous, f
(
(a′
n, b′
n)
)
must be an interval. So
f
(
(a′
n, b′
n)
)
=
(
f (an), f(bn)
)
for an, bn ∈ (a′
n, b′
n).
Hence,
f (E) ⊂
⋃
n
(
f (an), f(bn)
)
.
Therefore {
(
f (an), f(bn)
)
} is a covering of f (E). By the Mean Value Theorem,
𝓁
((
f (an), f(bn)
))
= |f (bn) − f (an)|
= |f ′(x)||bn − an|, x ∈ (an, bn)
≤ M |bn − an|.
It follows that
∑
n
𝓁
((
f (an), f(bn)
))
≤ M
∑
n
|bn − an| ≤ M
∑
n
|b′
n − a′
n|
≤ M
∑
n
𝓁
(
(a′
n, b′
n)
)
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

119
Thus,
inf
∑
n
𝓁
((
f (an), f(bn)
))
≤ M inf
∑
n
𝓁
(
(a′
n, b′
n)
)
.
The inﬁmum is taken over coverings of f (E) and E respectively. By deﬁnition (at
the very ﬁrst of the proof) we have
µ∗
L
(
f (E)
)
≤ M µ∗
L(E). ■
Problem 101
Let f be a real-valued function on [a, b] such that f is absolutely continuous on
[a + η, b] for every η ∈ (0, b − a). Show that if f is continuous and of bounded
variation on [a, b], then f is absolutely continuous on [a, b].
Solution
Using the Banach-Zaracki theorem, to show that f is absolutely continuous on [ a, b],
we need to show that f has property (N) on [ a, b]. Suppose E ⊂ [a, b] such that
µL(E) = 0. Given any ε > 0, since f is continuous at a+, there exists δ ∈ (0, b − a)
such that
a ≤ x ≤ a + δ ⇒ | f (x) − f (a)| < ε
2 . (∗)
Let E1 = E ∩ [a, a + δ] and E2 = E \ E1. Then E = E1 ∪ E2 and so f (E) =
f (E1) ∪ f (E2). But E2 ⊂ [a + δ, b) and f is absolutely continuous on [ a + δ, b], so f
has property (N) on this interval. Since E2 ⊂ E, we have µL(E2) = 0. Therefore,
µL(f (E2)) = 0 = µ∗
L(f (E2)).
On the other hand,
x ∈ E1 ⇒ x ∈ [a, a + δ)
⇒ f (a) − ε
2 ≤ f (x) ≤ f (a) + ε
2 by ( ∗)
⇒ f (E1) ⊂ [ f (a) − ε
2 , f (a) + ε
2 ]
⇒ µ∗
L(f (E1)) ≤ ε.
Thus,
µ∗
L(f (E)) ≤ µ∗
L(f (E1)) + µ∗
L(f (E2)) ≤ ε.
Since ε > 0 is arbitrary, µ∗
L(f (E)) = 0 and so µL(f (E)) = 0 . ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

120 CHAPTER 9. DIFFERENTIATION AND INTEGRATION
Problem 102
Let f be a real-valued integrable function on [a, b]. Let
F (x) =
∫
[a,x]
f dµL, x ∈ [a, b].
Show that F is continuous and of bounded variation on [a, b].
Solution
The continuity follows from Theorem 18 (absolute continuity implies continuity).
To show that F is of BV on [ a, b], let a = x0 < x 1 < ... < x n = b be any partition
of [ a, b]. Then
n∑
i=1
|F (xi − xi−1| =
n∑
i=1
⏐⏐⏐⏐
∫
[xi−1,xi]
f dµL
⏐⏐⏐⏐
≤
n∑
i=1
∫
[xi−1,xi]
|f |dµL
=
∫
[a,b]
|f |dµL.
Thus, since |f | is integrable,
V b
a (F ) ≤
∫
[a,b]
|f |dµL < ∞. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 10
Lp Spaces
1. Norms
For 0 < p < ∞ :
‖f ‖p =
(∫
X
|f |pdµ
)1/p
.
For p = ∞ :
‖f ‖∞ = inf
{
M ∈ [0, ∞) : µ{x ∈ X : |f (x)| > M } = 0
}
.
Theorem 22 Let (X, A, µ) be a measure space. Then the linear space Lp(X) is a Banach space
with respect to the norm ‖.‖p for 1 ≤ p < ∞ or the norm ‖.‖∞ for p = ∞.
2. Inequalities for 1 ≤ p < ∞
1. H¨ older’s inequality: If p and q satisfy the condition 1
p + 1
q = 1, then for f ∈ Lp(X), g ∈ Lq(X),
we have ∫
X
|f g|dµ =
(∫
X
|f |pdµ
)1/p (∫
X
|g|qdµ
)1/q
,
or
‖f g‖1 ≤ ‖f ‖p‖g‖q.
In particular,
‖f g‖1 ≤ ‖f ‖2‖g‖2 (Schwarz’s inequality).
2. Minkowski’s inequality: For f, g ∈ Lp(X), we have
‖f + g‖p ≤ ‖f ‖p + ‖g‖p.
3. Convergence
Theorem 23 Let (fn) be a sequence in Lp(X) and f an element in Lp(X) with 1 ≤ p < ∞. If
fn → f in Lp(X), i.e., ‖fn − f ‖p → 0, then
(1) ‖fn‖p → ‖f ‖p,
(2) fn
µ
− →f on X,
(3) There exists a subsequence (fnk ) such that fnk → f a.e. on X.
121
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

122 CHAPTER 10. LP SPACES
Theorem 24 Let (fn) be a sequence in Lp(X) and f an element in Lp(X) with 1 ≤ p < ∞. If
fn → f a.e. on X and ‖fn‖p → ‖f ‖p, then ‖fn − f ‖p → 0.
Theorem 25 Let (fn) be a sequence in Lp(X) and f an element in Lp(X) with 1 ≤ p < ∞. If
fn
µ
− →f on X and ‖fn‖p → ‖f ‖p, then ‖fn − f ‖p → 0.
Theorem 26 Let (fn) be a sequence in Lp(X) and f an element in Lp(X) with 1 ≤ p < ∞. If
‖fn − f ‖∞ → 0, then
(1) ‖fn‖∞ → ‖f ‖∞,
(2) fn → f uniformly on X \ E where E is a null set.
(3) fn
µ
− →f on X.
Problem 103
Let f be a Lebesgue measurable function on [0, 1]. Suppose 0 < f (x) < ∞ for all
x ∈ [0, 1]. Show that
(∫
[0,1]
f dµ
) (∫
[0,1]
1
f dµ
)
≥ 1.
Solution
The functions √f and 1√f are Lebesgue measurable since f is Lebesgue measurable
and 0 < f < ∞. By Schwarz’s inequality, we have
1 =
∫
[0,1]
1dµ =
∫
[0,1]
√
f 1√f dµ ≤
(∫
[0,1]
(√
f
)2
dµ
)1/2 (∫
[0,1]
( 1√f
)2
dµ
)1/2
≤
(∫
[0,1]
f dµ
)1/2 (∫
[0,1]
1
f dµ
)1/2
.
Squaring both sides we get
(∫
[0,1]
f dµ
) (∫
[0,1]
1
f dµ
)
≥ 1. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

123
Problem 104
Let (X, A, µ) be a ﬁnite measure space. Let f ∈ Lp(X) with p ∈ (1, ∞) and q its
conjugate. Show that
∫
X
|f |dµ ≤ µ(X)
1
q
(∫
X
|f |pdµ
) 1
p
.
Hint:
Write
f = f 1X
where 1X is the characteristic function of X, then apply the H¨ older’s inequality.
Problem 105
Let (X, A, µ) be a ﬁnite measure space.
(1) If 1 ≤ p < ∞ show that L∞(X) ⊂ Lp(X).
(2) If 1 ≤ p1 < p 2 < ∞ show that Lp2(X) ⊂ Lp1(X).
Solution
(1) Take any f ∈ L∞(X). Then ‖f ‖∞ < ∞. By deﬁnition, we have |f | ≤ ‖ f ‖∞ a.e.
on X. So we have
∫
X
|f |pdµ ≤
∫
X
‖f ‖p
∞dµ = µ(X)‖f ‖p
∞.
By assumption, µ(X) < ∞. Thus
∫
X |f |pdµ < ∞. That is f ∈ Lp(X).
(2) Consider the case 1 ≤ p1 < p 2 < ∞. Take any f ∈ Lp2(X). Let α := p2
p1
. Then
1 < α < ∞. Let β ∈ (1, ∞) be the conjugate of α, that is, 1
α + 1
β = 1. By the
H¨ older’s inequality, we have
∫
X
|f |p1dµ =
∫
X
(
|f |p2
)1/α
1Xdµ
≤
(∫
X
|f |p2dµ
)1/α (∫
X
|1X|βdµ
)1/β
= ‖f ‖p2/α
p2 µ(X) < ∞,
since ‖f ‖p2 < ∞ and µ(X) < ∞. Thus f ∈ Lp1(X). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

124 CHAPTER 10. LP SPACES
Problem 106 (Extension of H¨ older’s inequality)
Let (X, A, µ) be an arbitrary measure space. Let f1, ..., fn be extended complex-
valued measurable functions on X such that |f1|, ..., |fn| < ∞ a.e. on X. Let
p1, ..., pn be real numbers such that
p1, ..., pn ∈ (1, ∞) and 1
p1
+ ... + 1
pn
= 1.
Prove that
‖f1...fn‖1 ≤ ‖f1‖p1...‖fn‖pn. (∗)
Hint:
Proof by induction. For n = 2 we have already the H¨ older’s inequality.
Assume that ( ∗) holds for n ≥ 2. Let
q =
( 1
p1
+ ... + 1
pn
)−1
.
Then
q, pn+1 ∈ (0, ∞) and 1
q + 1
pn+1
= 1.
Keep going this way.
Problem 107
Let (X, A, µ) be an arbitrary measure space. Let f1, ..., fn be extended complex-
valued measurable functions on X such that |f1|, ..., |fn| < ∞ a.e. on X. Let
p1, ..., pn and r be real numbers such that
p1, ..., pn, r ∈ (1, ∞) and 1
p1
+ ... + 1
pn
= 1
r . (i)
Prove that
‖f1...fn‖r ≤ ‖f1‖p1...‖fn‖pn.
Solution
We can write ( i) as follows:
1
p1/r + ... + 1
pn/r = 1.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

125
From the extension of H¨ older’s inequality (Problem 105) we have
‖‖|f1...fn|r‖‖
1 ≤
‖‖|f1|r‖‖
p1/r...
‖‖|fn|r‖‖
pn/r. (ii)
Now we have ‖‖|f1...fn|r‖‖
1 =
∫
X
|f1...fn|rdµ = ‖f1...fn‖r
r,
and for i = 1, ..., n we have
‖‖|fi|r‖‖
pi/r =
(∫
X
|fi|r pi
r dµ
)r/pi
=
(∫
X
|fi|pidµ
)r/pi
= ‖fi‖r
pi.
By substituting these expressions into ( ii), we have
‖f1...fn‖r
r ≤ ‖f1‖r
p1...‖fn‖r
pn.
Taking the r-th roots both sides of the above inequality we obtain ( i). ■
Problem 108
Let (X, A, µ) be a measure space. Let θ ∈ (0, 1) and let p, q, r ≥ 1 with p, q ≥ r
be related by
1
r = θ
p + 1 − θ
q .
Show that for every extended complex-valued measurable function on X we have
‖f ‖r ≤ ‖f ‖θ
p‖f ‖1−θ
q .
Solution
Recall: (Extension of Holder’s inequality)
1
r = 1
p1
+ ... + 1
pn
⇒ ‖ f1...fn‖r ≤ ‖f ‖p1...‖fn‖pn.
For n = 2 we have 1
r = 1
p + 1
q ⇒ ‖ f g‖r ≤ ‖f ‖p‖g‖q.
Now, we have
1
r = θ
p + 1 − θ
q = 1
p/θ + 1
q/(1 − θ) .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

126 CHAPTER 10. LP SPACES
Applying the above formula we get
‖f ‖r =
‖‖|f |θ.|f |1−θ‖‖ ≤
‖‖|f |θ‖‖
p/θ .
‖‖|f |1−θ‖‖
q/(1−θ) . (∗)
Some more calculations:
‖‖|f |θ‖‖
p/θ =
(∫
X
(
|f |θ)p/θ
)θ/p
=
(∫
X
|f |p
)θ/p
= ‖f ‖θ
p.
And
‖‖|f |1−θ‖‖
q/(1−θ) =
(∫
X
(
|f |1−θ)q/1−θ
)1−θ/q
=
(∫
X
|f |q
)1−θ/q
= ‖f ‖1−θ
q .
Plugging into (*) we obtain
‖f ‖r ≤ ‖f ‖θ
p.‖f ‖1−θ
q . ■
Problem 109
Let (X, A, µ) be a measure space. Let p, q ∈ [1, ∞] be conjugate. Let (fn)n∈N ⊂
Lp(X) and f ∈ Lp(X) and similarly (gn)n∈N ⊂ Lq(X) and g ∈ Lq(X). Show
that
[
lim
n→∞
‖fn − f ‖p = 0 and lim
n→∞
‖gn − g‖q = 0
]
⇒ lim
n→∞
‖fngn − f g‖1 = 0.
Solution
We use H¨ older’s inequality:
‖fngn − f g‖1 =
∫
X
|fngn − f g|dµ
≤
∫
X
(|fngn − fng| + |fng − f g|)dµ
≤
∫
X
|fn||gn − g|dµ +
∫
X
|g||fn − f |dµ
≤ ‖ fn‖p.‖gn − g‖q + ‖g‖q.‖fn − f ‖p. (∗)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

127
By Minkowski’s inequality, we have
‖fn‖p ≤ ‖f ‖p + ‖fn − f ‖p.
Since ‖f ‖p and ‖fn − f ‖p are bounded (why?), ‖fn‖p is bounded for every n ∈N.
From assumptions we deduce that lim n→∞ ‖fn‖p.‖gn − g‖q = 0.
Since ‖g‖q is bounded, from assumptions we get lim n→∞ ‖g‖q.‖fn − f ‖p = 0. There-
fore, from (*) we obtain
lim
n→∞
‖fngn − f g‖1 = 0. ■
Problem 110
Let (X, A, µ) be a measure space and let p ∈ [1, ∞). Let (fn)n∈N ⊂ Lp(X) and
f ∈ Lp(X) be such that limn→∞ ‖fn − f ‖p = 0 . Let (gn)n∈N be a sequence of
complex-valued measurable functions on X such that |gn| ≤ M for every n ∈N
and let g be a complex-valued measurable function on X such that limn→∞ gn = g
a.e. on X. Show that
lim
n→∞
‖fngn − f g‖p = 0.
Solution
We ﬁrst note that |g| ≤ M a.e. on X. Indeed, we have for all n ∈N,
|g| ≤ | gn − g| + |gn|.
Since |gn| ≤ M for every n ∈N and |gn − g| → 0 a.e. on X by assumption. Hence
|g| ≤ M a.e. on X.
Now, by Minkowski’s inequality, we have
‖fngn − f g‖p ≤ ‖ fngn − f gn‖p + ‖f gn − f g‖p
≤ ‖ gn(fn − f )‖p + ‖f (gn − g)‖p (∗)
Some more calculations:
‖gn(fn − f )‖p
p =
∫
X
|gn(fn − f )|pdµ
≤
∫
X
|gn|p.|fn − f |pdµ
≤ M p‖fn − f ‖p
p.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

128 CHAPTER 10. LP SPACES
Since ‖fn − f ‖p → 0 by assumption, we have that ‖gn(fn − f )‖p → 0.
Let hn = f gn − f g for every n ∈N. Then
|hn| ≤ | f |.|gn − g| ≤ | f |(|gn| + |g|) ≤ 2M |f |
|hn|p ≤ 2pM p|f |p < ∞.
Now, |hn|p is bounded and |hn|p ≤ | f |p.|gn − g|p ⇒ | hn|p → 0 (since gn → g a.e.).
By the Dominated Convergence Theorem, we have
0 =
∫
X
lim
n→∞
|hn|pdµ = lim
n→∞
∫
X
|hn|pdµ
= lim
n→∞
∫
X
|f gn − f g|pdµ
= lim
n→∞
‖f (gn − g)‖p
p.
From these results, (*) gives that
lim
n→∞
‖fngn − f g‖p = 0. ■
Problem 111
Let f be an extended real-valued Lebesgue measurable function on [0, 1] such that∫
[0,1] |f |pdµ < ∞ for some p ∈ [1, ∞). Let q ∈ (1, ∞] be the conjugate of p. Let
a ∈ (0, 1]. Show that
lim
a→0
1
a1/q
∫
[0,a]
|f |dµ = 0.
Solution
• p = 1
Since q = ∞, we have to show
lim
a→0
∫ a
0
|f (s)|ds = 0 (Lebesgue integral = Riemann integral) .
This is true since f is integrable so
∫ a
0 |f (s)|ds is continuous with respect to a.
• 1 < p < ∞
Then 1 < q < ∞. We have∫ a
0
|f (s)|ds =
∫ a
0
|f (s)|.1 ds
≤ µ([0, a])1/q
(∫ a
0
|f (s)|ds
)1/p
(Problem 104)
= a1/q
(∫ a
0
|f (s)|ds
)1/p
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

129
Hence,
1
a1/q
∫ a
0
|f (s)|ds ≤
(∫ a
0
|f (s)|ds
)1/p
(∗)
Since |f | is integrable, we have 1 (Problem 66)
∀ε > 0, ∃δ > 0 : µ([0, a]) < δ ⇒
∫
[0,a]
|f |dµ < ε p.
Equivalently,
∀ε > 0, ∃δ > 0 : 0 < a < δ ⇒
(∫ a
0
|f (s)|ds
)1/p
< ε. (∗∗)
From (*) and (**) we obtain
∀ε > 0, ∃δ > 0 : 0 < a < δ ⇒ 1
a1/q
∫ a
0
|f (s)|ds < ε.
That is,
lim
a→0
1
a1/q
∫ a
0
|f (s)|ds = 0. ■
Problem 112
Let (X, A, µ) be a ﬁnite measure space. Let fn, f ∈ L2(X) for all n ∈N such
that limn→∞ fn = f a.e. on X and ‖fn‖2 ≤ M for all n ∈N.
Show that limn→∞ ‖fn − f ‖1 = 0.
Solution
We ﬁrst claim: ‖f ‖2 ≤ M . Indeed, y Fatous’ lemma, we have
‖f ‖2
2 =
∫
X
|f |2dµ ≤ lim inf
n→∞
∫
X
|fn|2dµ ≤ M 2.
Since µ(X) < ∞, we can use Egoroﬀ’s theorem:
∀ε > 0, ∃A ∈ A with µ(A) < ε 2 and fn → f uniformly on X \ A.
Now we can write
‖fn − f ‖1 =
∫
X
|fn − f |dµ =
∫
A
|fn − f |dµ +
∫
X\A
|fn − f |dµ.
1This is called the uniform continuity of the integral with respect to the measure µ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

130 CHAPTER 10. LP SPACES
On X \ A, f n → f uniformly, so for large n, we have
∫
X\A |fn − f |dµ < ε . On A we
have
∫
A
|fn − f |dµ =
∫
X
|fn − f |χA dµ ≤ µ(A)1/2.‖fn − f ‖2
≤ µ(A)1/2(‖fn‖2 + ‖f ‖2)
≤ 2M ε (since µ(A) < ε 2).
Thus, for any ε > 0, for large n, we have
‖fn − f ‖1 ≤ (2M + 1)ε.
This tells us that lim n→∞ ‖fn − f ‖1 = 0. ■
Problem 113
Let (X, A, µ) be a ﬁnite measure space and let p, q ∈ (1, ∞) be conjugates. Let
fn, f ∈ Lp(X) for all n ∈N such that limn→∞ fn = f a.e. on X and ‖fn‖p ≤ M
for all n ∈N. Show that
(a) ‖f ‖p ≤ M .
(b) limn→∞ ‖fn − f ‖p = 0.
(c) limn→∞
∫
X fngdµ =
∫
X f gdµ for every g ∈ Lq(X).
(d) limn→∞
∫
E fndµ =
∫
E f dµ for every E ∈ A.
Hint:
(a) and (b): See Problem 112.
(c) Show ‖fng − f g‖1 ≤ ‖fn − f ‖p‖g‖q. Then use (b).
(d) Write ∫
E
fng =
∫
X
fng1E =
∫
X
fn(g1E).
Then use (c).
Problem 114
Let (X, A, µ) be a measure space. Let f be a real-valued measurable function on
X such that f ∈ L1(X) ∩ L∞(X). Show that f ∈ Lp(X) for every p ∈ [1, ∞].
Hint:
If p = 1 or p = ∞, there is nothing to prove.
Suppose p ∈ (1, ∞). Let f ∈ L1(X) ∩ L∞(X). Write
|f |p = |f |1|f |p−1 ≤ |f |.‖f ‖p−1
∞ .
Integrate over X, then use the fact that ‖f ‖1 and ‖f ‖∞ are ﬁnite.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

131
Problem 115
Let (X, A, µ) be a measure space and let 0 < p 1 < p < p 2 ≤ ∞. Show that
Lp(X) ⊂ Lp1(X) + Lp2(X),
that is, if f ∈ Lp(X) then f = g +h for some g ∈ Lp1(X) and some h ∈ Lp2(X).
Solution
For any f ∈ Lp(X), let D = {X : |f | ≥ 1}. Let g = f 1D and h = f 1Dc. Then
g + h = f 1D + f 1Dc = f (1D + 1Dc
| {z }
=1D∪Dc
) = f (See Problem 37) .
We want to show g ∈ Lp1(X) and h ∈ Lp2(X).
On D we have : 1 ≤ |f |p1 ≤ |f |p ≤ |f |p2. It follows that
∫
X
|g|p1dµ =
∫
D
|f |p1dµ ≤
∫
X
|f |pdµ < ∞ since f ∈ Lp(X).
Hence, g ∈ Lp1(X).
On Dc we have : |f |p1 ≥ |f |p ≥ |f |p2. It follows that
∫
X
|h|p2dµ =
∫
Dc
|f |p2dµ ≤
∫
X
|f |pdµ < ∞.
Hence, h ∈ Lp2(X). This completes the proof. ■
Problem 116
Given a measure space (X, A, µ). For 0 < p < r < q ≤ ∞, show that
Lp(X) ∩ Lq(X) ⊂ Lr(X).
Hint:
Let D = {X : |f | ≥ 1}. On D we have |f |r ≤ |f |q, and on X \ D we have |f |r ≤ |f |p.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

132 CHAPTER 10. LP SPACES
Problem 117
Suppose f ∈ L4([0, 1]), ‖f ‖4 = C ≥ 1 and ‖f ‖2 = 1. Show that
1
C ≤ ‖f ‖4/3 ≤ 1.
Solution
First we note that 4 and 4/3 are conjugate. By assumption and by H¨ older’s inequal-
ity we have
1 = ‖f ‖2
2 =
∫
[0,1]
|f |2dµ =
∫
[0,1]
|f |.|f |dµ
≤ ‖ f ‖4.‖f ‖4/3
≤ C.‖f ‖4/3.
This implies that ‖f ‖4/3 ≥ 1
C . (∗).
By Schwrarz’s inequality we have
‖f ‖4/3
4/3 =
∫
[0,1]
|f |4/3dµ =
∫
[0,1]
|f |.|f |1/3dµ
≤ ‖ f ‖2.‖f ‖1/3
2 = 1 since ‖f ‖2 = 1.
Hence, ‖f ‖4/3 ≤ 1. (∗∗)
From (*) and (**) we obtain
1
C ≤ ‖f ‖4/3 ≤ 1. ■
Problem 118
Let (X, A, µ) be a measure space with µ(X) ∈ (0, ∞). Let f ∈ L∞(X) and let
αn =
∫
X |f |ndµ for n ∈N. Show that
lim
n→∞
αn+1
αn
= ‖f ‖∞.
Solution
We ﬁrst note that if ‖f ‖∞ = 0, the problem does not make sense. Indeed,
‖f ‖∞ = 0 ⇒ f ≡ 0 a.e. on X
⇒ αn = 0, ∀n ∈N.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

133
Suppose that 0 < ‖f ‖∞ < ∞. Then αn > 0, ∀n ∈N. We have
αn+1 =
∫
X
|f |n+1dµ =
∫
X
|f |n|f |dµ
≤ ‖ f ‖∞.
∫
X
|f |ndµ = ‖f ‖∞αn.
This implies that
αn+1
αn
≤ ‖f ‖∞, ∀n ∈N.
⇒ lim sup
n→∞
αn+1
αn
≤ ‖f ‖∞. (∗)
Notice that n+1
n and n + 1 are conjugate. Using again H¨ older’s inequality, we get
αn =
∫
X
|f |n.1 dµ ≤
(∫
X
(|f |n)
n+1
n dµ
) n
n+1
(∫
X
1n+1
) 1
n+1
=
(∫
X
(|f |n+1)dµ
) n
n+1
.µ(X)
1
n+1
= α
n
n+1
n+1.µ(X)
1
n+1 .
With a simple calculation we get
αn+1
αn
≥ α
1
n+1
n+1.µ(X)− 1
n+1 , ∀n ∈N.
Given any ε > 0, let E = {X : |f | > ‖f ‖∞ − ε}, then, by deﬁnition of ‖f ‖∞, we
have µ(E) > 0. Now,
α
1
n+1
n+1 =
(∫
X
(|f |n+1)dµ
) 1
n+1
≥
(∫
E
(|f |n+1)dµ
) 1
n+1
> µ (E)
1
n+1 .(‖f ‖∞ − ε).
It follows that
αn+1
αn
≥ (‖f ‖∞ − ε).
[ µ(E)
µ(X)
] 1
n+1
.
⇒ lim inf
n→∞
αn+1
αn
≥ ‖f ‖∞ − ε, ∀ε > 0
⇒ lim inf
n→∞
αn+1
αn
≥ ‖f ‖∞. (∗∗)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

134 CHAPTER 10. LP SPACES
From (*) and (**) we obtain
lim
n→∞
αn+1
αn
= ‖f ‖∞. ■
Problem 119
Let (X, A, µ) be a measure space and p ∈ [1, ∞).
Let f ∈ Lp(X) and (fn : n ∈ N) ⊂ Lp(X). Suppose limn→∞ ‖fn − f ‖p = 0 .
Show that for every ε > 0, there exists δ > 0 such that for all n ∈N we have
∫
E
|fn|pdµ < ε for every E ∈ A such that µ(E) < δ.
Solution
By assumption we have lim n→∞ ‖fn − f ‖p
p = 0. Equivalently,
∀ε > 0, ∃N ∈N : n ≥ N ⇒ ‖fn − f ‖p
p < ε
2p+1 . (1)
From triangle inequality we have 2
|fn| ≤ | fn − f | + |f |,
|fn|p ≤ (|fn − f | + |f |)p ≤ 2p|fn − f |p + 2p|f |p.
Integrating over E ∈ A and using (1), we get for n ≥ N ,
∫
E
|fn|pdµ ≤ 2p
∫
E
|fn − f |pdµ + 2p
∫
E
|f |pdµ
≤ 2p‖fn − f ‖p
p + 2p
∫
E
|f |pdµ
≤ 2p. ε
2p+1 + 2p
∫
E
|f |pdµ
= ε
2 + 2p
∫
E
|f |pdµ. (2)
2In fact, for a, b ≥ 0 and 1 ≤ p < ∞ we have
(a + b)p ≤ 2p−1(ap + bp).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

135
Since |f |p is integrable, by the uniform absolute continuity of integral (Problem 66)
we have
∃δ0 > 0 : µ(E) < δ 0 ⇒
∫
E
|f |pdµ < ε
2p+1 .
So, for n ≥ N , from (2) we get
∃δ0 > 0 : µ(E) < δ 0 ⇒
∫
E
|fn|pdµ ≤ ε
2 + 2p. ε
2p+1 = ε. (3)
Similarly, all |f1|p, ..., |fN −1|p are integrable, so we have
∃δj > 0 : µ(E) < δ j ⇒
∫
E
|fj|pdµ < ε, j = 1, ..., N − 1. (4)
Let δ = min{δ0, δ1, .., δN −1}. From (3) and (4) we get for every n ∈N,
∃δ > 0 : µ(E) < δ ⇒
∫
E
|fn|pdµ < ε. ■
Problem 120
Let f be a bounded real-valued integrable function on [0, 1]. Suppose∫
[0,1] xnf dµ = 0 for n = 0, 1, 2, .... Show that f = 0 a.e. on [0, 1].
Solution
Fix an arbitrary function ϕ ∈ C[0, 1]. By the Stone-Weierstrass theorem, there is a
sequence ( pn) of polynomials such that ‖ϕ − pn‖∞ → 0 as n → ∞. Then
⏐⏐⏐⏐
∫
[0,1]
f ϕdµ
⏐⏐⏐⏐ =
⏐⏐⏐⏐
∫
[0,1]
f (ϕ − pn + pn)dµ
⏐⏐⏐⏐
≤
∫
[0,1]
|f | | ϕ − pn|dµ +
⏐⏐⏐⏐
∫
[0,1]
f pndµ
⏐⏐⏐⏐
≤ ‖ f ‖1‖ϕ − pn‖∞ +
⏐⏐⏐⏐
∫
[0,1]
f pndµ
⏐⏐⏐⏐
| {z }
=0 by hypothesis
= ‖f ‖1‖ϕ − pn‖∞.
Since ‖f ‖1 < ∞ and ‖ϕ − pn‖∞ → 0, we have
∫
[0,1]
f ϕdµ = 0, ∀ϕ ∈ C[0, 1]. (∗)
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

136 CHAPTER 10. LP SPACES
Now, since C[0, 1] is dense in L1[0, 1], there exists a sequence ( ϕn) ⊂ C[0, 1] such
that ‖ϕn − f ‖1 → 0 as n → ∞. Then
0 ≤
∫
[0,1]
f 2dµ =
⏐⏐⏐⏐
∫
[0,1]
f (f − ϕn + ϕn)dµ
⏐⏐⏐⏐
≤
∫
[0,1]
|f | | f − ϕn|dµ +
⏐⏐⏐
∫
[0,1]
f ϕndµ
| {z }
=0 by (*)
⏐⏐⏐
≤ ‖ f ‖∞‖f − ϕn‖1.
Since ‖f ‖∞ < ∞ and ‖f − ϕn‖1 → 0, we have
∫
[0,1]
f 2dµ = 0.
Thus f = 0 a.e. on [0 , 1]. ■
Problem 121
Let (X, A, µ) be a σ-ﬁnite measure space with µ(X) = ∞.
(a) Show that there exists a disjoint sequence (En : n ∈ N) in A such that⋃
n∈N En = X and µ(En) ∈ [1, ∞) for every n ∈N.
(b) Show that there exists an extended real-valued measurable function f on X
such that f /∈ L1(X) and f ∈ Lp(X) for all p ∈ (1, ∞].
Solution
(a) Since ( X, A, µ) is a σ-ﬁnite measure space, there exists a sequence ( An : n ∈N)
of disjoint sets in A such that
X =
⋃
n∈N
An and µ(An) < ∞, ∀n ∈N.
By the countable additivity and by assumption, we have
µ(X) =
∑
n∈N
µ(An) = ∞.
It follows that
∃k1 ∈N : 1 ≤
k1∑
n=1
µ(An) = µ(A1 ∪ ... ∪ Ak1) < ∞.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

137
Let E1 = A1 ∪ ... ∪ Ak1 then we have
1 ≤ µ(E1) < ∞ and µ(Ak1+1 ∪ Ak1+2 ∪ ...) = µ(X \ E1) = ∞.
Then there exists k2 ≥ k1 + 1 such that
1 ≤ µ(Ak1+1 ∪ ... ∪ Ak2) < ∞.
Let E1 = Ak1+1 ∪ ... ∪ Ak2 then we have
1 ≤ µ(E2) < ∞ and E1 ∩ E1 = ∅.
And continuing this process we are building a sequence ( En : n ∈ N) of disjoint
subsets in A satisfying
⋃
n∈N
En =
⋃
n∈N
An = X and µ(En) ∈ [1, ∞), ∀n ∈N.
(b) Deﬁne a real-valued function f on X = ⋃
n∈N An by
f =
∞∑
n=1
χAn
nµ(An) .
Then
f |A1 = 1
1µ(A1) , ..., f|An = 1
nµ(An) , ...
Hence, ∫
X
f dµ =
∞∑
n=1
∫
An
f dµ =
∞∑
n=1
1
n = ∞.
That is f /∈ L1(X).
We also have
f p|A1 = 1
1pµ(A1)p , ..., fp|An = 1
npµ(An)p , ...(1 < p < ∞)
By integrating
∫
X
f pdµ =
∞∑
n=1
∫
An
f pdµ
=
∞∑
n=1
1
npµ(An)p−1
≤
∞∑
n=1
1
np < ∞. since µ(An)p−1 ≥ 1.
Thus, f ∈ Lp(X). ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

138 CHAPTER 10. LP SPACES
Problem 122
Consider the space Lp([0, 1]) where p ∈ (1, ∞].
(a) Prove that ‖f ‖p is increasing in p for any bounded measurable function f .
(b) Prove that ‖f ‖p → ‖f ‖∞ when p → ∞.
Solution
(a)
• Suppose 1 < p < ∞. We want to show ‖f ‖p ≤ ‖f ‖∞.
By deﬁnition, we have
|f | ≤ ‖ f ‖∞ a.e. on [0 , 1].
Therefore,
|f |p ≤ ‖f ‖p
∞ a.e. on [0 , 1].
⇒
∫
[0,1]
|f |pdµ ≤
∫
[0,1]
‖f ‖p
∞dµ
⇒ ‖f ‖p
p ≤ ‖f ‖p
∞ µ([0, 1])
⇒ ‖f ‖p ≤ ‖f ‖∞.
• Suppose 1 < p 1 < p 2 < ∞. We want to show ‖f ‖p1 ≤ ‖f ‖p2.
Notice that p1
p2
+ p2 − p1
p2
= 1 or 1
p2/p1
+ 1
p2/(p2 − p1) = 1.
By H¨ older’s inequality we have
‖f ‖p1
p1 =
∫
[0,1]
|f |p1dµ =
∫
[0,1]
|f |p1.1.dµ
≤ ‖| f |p1‖p2/p1.‖1‖p2/(p2−p1)
= ‖f ‖p1
p2/p1
. (∗)
Now,
‖f ‖p1
p2/p1
=
(∫
[0,1]
|f |p1. p2
p1 dµ
)p1/p2
=
(∫
[0,1]
|f |p2dµ
)p1. 1
p2
= ‖f ‖p1
p2.
Finally, (*) implies that ‖f ‖p1 ≤ ‖f ‖p2.
In both cases we have
1 < p 1 < p 2 =⇒ ‖f ‖p1 ≤ ‖f ‖p2.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

139
That is ‖f ‖p is increasing in p.
(b) By part (a) we get ‖f ‖p ≤ ‖f ‖∞. Then
lim sup
p→∞
‖f ‖p ≤ ‖f ‖∞. (i)
Given any ε > 0, let E = {X : |f | > ‖f ‖∞ − ε}. Then µ(E) > 0 and
‖f ‖p
p ≥
∫
E
|f |pdµ > (‖f ‖∞ − ε)pµ(E).
⇒ ‖f ‖p ≥ (‖f ‖∞ − ε)µ(E)1/p
⇒ lim inf
p→∞
‖f ‖p ≥ ‖f ‖∞ − ε, ∀ε > 0 (since lim
p→∞
µ(E)1/p = 1).
⇒ lim inf
p→∞
‖f ‖p ≥ ‖f ‖∞. (ii)
From (i) and (ii) we obtain
lim
p→∞
‖f ‖p = ‖f ‖∞. ■
∗ ∗ ∗∗
APPENDIX
The Lp Spaces for 0 < p < 1
Let ( X, A, µ) be a measure space and p ∈ (0, 1). It is easy to check that Lp(X) is a linear space.
Exercise 1. If ‖f ‖p :=
(∫
X |f |pdµ
)1/p
and 0 < p < 1, then ‖.‖p is not a norm on X.
Hint:
Show that ‖.‖p does not satisfy the triangle inequality:
Take X = [0, 1] with the Lebesgue measure on it. Let f = 1[0, 1
2 ) and g = 1[ 1
2 ,1). Then show that
‖f + g‖p = 1.
and that
‖f ‖p = 2 − 1
p and ‖g‖p = 2 − 1
p .
It follows that
‖f + g‖p > ‖f ‖p + ‖g‖p.
Exercise 2. If α, β ∈C and 0 < p < 1, then
|α + β|p ≤ |α|p + |α|p.
Hint:
Consider the real-valued function ϕ(t) = (1 + t)p − 1 − tp, t ∈ [0, ∞). Show that it is strictly
decreasing on [0 , ∞). Then take t = |β|
|α| > 0.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

140 CHAPTER 10. LP SPACES
Exercise 3. For 0 < p < 1, ‖.‖p is not a norm. However
ρp(f, g) :=
∫
X
|f − g|pdµ, f, g ∈ Lp(X)
is a metric on Lp(X).
Proof.
We prove only the triangle inequality. For f, g, h ∈ Lp(X), we have
ρp(f, g) =
∫
X
|f − g|pdµ
=
∫
X
|(f − h) + (h − g)|pdµ
≤
∫
X
(|f − h| + |h − g|)pdµ
≤
∫
X
|f − h|pdµ +
∫
X
|h − g|pdµ (by Exercise 2)
= ρp(f, h) + ρp(h, g). ■
∗ ∗ ∗∗
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 11
Integration on Product Measure
Space
1. Product measure spaces
Deﬁnition 32 (Product measure)
Given n measure spaces (X1, A1, µ1), ..., (Xn, An, µn). Consider the product measurable space(
X1 × ... × Xn, σ(A1 × ... × An)
)
. A measure µ on σ(A1 × ... × An) such that
µ(E) = µ1(A1)...µn(An) for E = A1 × ... × An ∈ A 1 × ... × An
with the convention ∞.0 = 0 is called a product measure of µ1, ..., µn and we write
µ = µ1 × ... × µn.
Theorem 27 (Existence and uniqueness)
For n arbitrary measure spaces (X1, A1, µ1), ..., (Xn, An, µn), a product measure space
(
X1 × ... ×
Xn, σ(A1 × ... × An), µ1 × ... × µn
)
exists. Moreover, if the n measure spaces are all σ-ﬁnite, then
the product measure space is unique.
2. Integration
Deﬁnition 33 (Sections and section functions)
Let
(
X × Y, σ(A × B), µ × ν
)
be the product of two σ-ﬁnite measure spaces (X, A, µ) and (Y, B, ν).
Let E ⊂ X × Y , and f be an extended real-valued function on E.
(a) For x ∈ X, the set E(x, .) := {y ∈ Y : ( x, y) ∈ E} is called the x-section of E.
For y ∈ Y , the set E(., y) := {x ∈ X : ( x, y) ∈ E} is called the y-section of E.
(b) For x ∈ X, the function f (x, .) deﬁned on E(x, .) is called the x-section of f .
For y ∈ Y , the function f (., y) deﬁned on E(., y) is called the y-section of f .
Proposition 24 Let
(
X×Y, σ(A×B), µ×ν
)
be the product of two σ-ﬁnite measure spaces (X, A, µ)
and (Y, B, ν). For every E ∈ σ(A × B ), ν
(
E(x, .)
)
is a A-measurable function of x ∈ X and
µ
(
E(., y)
)
is a B-measurable function of y ∈ Y . Furthermore, we have
(µ × ν)(E) =
∫
X
ν
(
E(x, .)
)
µ(dx) =
∫
Y
µ
(
E(., y)
)
ν(dy).
141
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

142 CHAPTER 11. INTEGRATION ON PRODUCT MEASURE SPACE
Theorem 28 (Tonelli’s Theorem)
Let (X × Y, σ(A × B), µ × ν) be product measure space of two σ-ﬁnite measure spaces. Let f be a
non-negative extended real-valued measurable on X × Y . Then
(a) F 1(x) :=
∫
Y f (x, .)dν is a A-measurable function of x ∈ X.
(b) F 2(y) :=
∫
X f (., y)dµ is a B-measurable function of y ∈ Y .
(c)
∫
X×Y f d(µ × ν) =
∫
X F 1dµ =
∫
Y F 2dν, that is,
∫
X×Y
f d(µ × ν) =
∫
X
[∫
Y
f (x, .)dν
]
dµ =
∫
Y
[∫
X
f (., y)dµ
]
dν.
Theorem 29 (Fubini’s Theorem)
Let (X × Y, σ(A × B), µ × ν) be product measure space of two σ-ﬁnite measure spaces. Let f be a
µ × ν-integrable extended real-valued measurable function on X × Y . Then
(a) The B-measurable function f (x, .) is ν-integrable on Y for µ-a.e. x ∈ X and the A-
measurable function f (., y) is µ-integrable on X for ν-a.e. y ∈ Y .
(b) The function F 1(x) :=
∫
Y f (x, .)dν is deﬁned for µ-a.e. x ∈ X, A-measurable and µ-
integrable on X.
The function F 2(y) :=
∫
X f (., y)dν is deﬁned for ν-a.e. y ∈ X, B-measurable and ν-
integrable on Y .
(c) We have the equalities:
∫
X×Y f d(µ × ν) =
∫
X F 1dµ =
∫
Y F 2dν, that is,
∫
X×Y
f d(µ × ν) =
∫
X
[∫
Y
f (x, .)dν
]
dµ =
∫
Y
[∫
X
f (., y)dµ
]
dν.
∗ ∗ ∗∗
Problem 123
Consider the product measure space
(
R ×R, σ(BR × BR), µL × µL
)
.
Let D = {(x, y) ∈R ×R : x = y}. Show that
D ∈ σ(BR × BR) and (µL × µL)(D) = 0 .
Solution
Let λ = µL × µL. Let D0 = {(x, y) ∈ [0, 1] × [0, 1] : x = y}. For each n ∈Z let
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

143
Dn = {(x, y) ∈ [n, n + 1] × [n, n + 1] : x = y}. Then, by translation invariance of
Lebesgue measure, we have
λ(D0) = λ(Dn), ∀n ∈N.
and D =
⋃
n∈Z
Dn.
To solve the problem, it suﬃces to prove D0 ∈ σ(BR × BR) and λ(D0) = 0.
For each n ∈N, divide [0 , 1] into 2 n equal subintervals as follows:
In,1 =
[
0, 1
2n
]
, In,2 =
[ 1
2n , 2
2n
]
, ..., In,2n =
[ 2n − 1
2n , 1
]
.
Let Sn = ⋃2n
k=1(In,k × In,k), then D0 = lim n→∞ Sn.
Now, for each n ∈N and for k = 1, 2, ..., 2n, I n,k ∈ BR. Therefore,
In,k × In,k ∈ σ(BR × BR) and so Sn ∈ σ(BR × BR).
Hence, D0 ∈ σ(BR × BR).
It is clear that ( Sn) is decreasing (make a picture yourself), so
D0 = lim
n→∞
Sn =
∞⋂
n=1
Sn.
And we have
λ(Sn) =
2n
∑
k=1
λ(In,k × In,k)
=
2n
∑
k=1
1
2n . 1
2n = 2 n. 1
22n = 1
2n .
It follows that
λ(D0) ≤ λ(Sn) = 1
2n , ∀n ∈N.
Thus, λ(D0) = 0 . ■
Problem 124
Consider the product measure space (R ×R, σ(BR × BR), µL × µL). Let f be a
real-valued function of bounded variation on [a, b]. Consider the graph of f :
G = {(x, y) ∈R ×R : y = f (x) for x ∈R}.
Show that G ∈ σ(BR × BR) and (µL × µL)(G) = 0 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

144 CHAPTER 11. INTEGRATION ON PRODUCT MEASURE SPACE
Hint:
Partition of [ a, b]:
P = {a = x0 < x 1 < ... < x n = b}.
Elementary rectangles:
Rn,k = [xk−1, xk] × [mk, Mk], k = 1, ..., n,
where
mk = inf
x∈[xk−1,xk]
f (x) and Mk = sup
x∈[xk−1,xk]
f (x).
Let
Rn =
n⋃
k=1
Rn,k and ‖P ‖ = max
1≤k≤n
(xk − xk−1).
Let λ = µL × µL. Show that
λ(Rn) ≤ ‖P ‖
n∑
k=1
(Mk − mk) ≤ ‖P ‖V b
a (f ),
Problem 125
Let (X, A, µ) and (Y, B, ν) be the measure spaces given
X = Y = [0, 1]
A = B = B[0,1], the σ-algebra of the Borel sets in [0, 1],
µ = µL and ν is the counting measure .
Consider the product measurable space
(
X × Y, σ(A × B )
)
and a subset in it
deﬁned by E = {(x, y) ∈ X × Y : x = y}. Show that
(a) E ∈ σ(A × B),
(b)
∫
X
(∫
Y
χEdν
)
dµ ⁄=
∫
Y
(∫
X
χEdµ
)
dν.
Why is Tonelli’s theorem not applicable?
Solution
(a) For each n ∈N, divide [0 , 1] into 2 n equal subintervals as follows:
In,1 =
[
0, 1
2n
]
, In,2 =
[ 1
2n , 2
2n
]
, ..., In,2n =
[ 2n − 1
2n , 1
]
.
Let Sn = ⋃2n
k=1(In,k × In,k). It is clear that ( Sn) is decreasing, so
E = lim
n→∞
Sn =
∞⋂
n=1
Sn.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

145
Now, for each n ∈N and for k = 1, 2, ..., 2n, I n,k ∈ B [0,1]. Therefore,
In,k × In,k ∈ σ(B[0,1] × B[0,1]) and so Sn ∈ σ(B[0,1] × B[0,1]).
Hence, E ∈ σ(B[0,1] × B[0,1]).
(b) For any x ∈ X, 1E(x, .) = 1{x}(.). Therefore,
∫
Y
1Edν =
∫
[0,1]
1{x}dν = ν{x} = 1.
Hence, ∫
X
(∫
Y
1Edν
)
dµ =
∫
[0,1]
1dµ = 1. (∗)
On the other hand, for every y ∈ Y, 1E(., y) = 1{y}(.). Therefore,
∫
X
1Edµ =
∫
[0,1]
1{y}dµ = µ{y} = 0.
Hence, ∫
Y
(∫
X
1Edµ
)
dν =
∫
[0,1]
0dµ = 0. (∗∗)
Thus, from (*) and (**) we get
∫
X
(∫
Y
1Edν
)
dµ ⁄=
∫
Y
(∫
X
1Edµ
)
dν.
Tonelli’s theorem requires that the two measures must be σ-ﬁnite. Here, the counting
measure ν is not σ-ﬁnite, so Tonelli’s theorem is not applicable. ■
Question: Why the counting measure on [0 , 1] is not σ-ﬁnite?
Problem 126
Suppose g is a Lebesgue measurable real-valued function on [0, 1] such that the
function f (x, y) = 2 g(x) − 3g(y) is Lebesgue integrable over [0, 1] × [0, 1]. Show
that g is Lebesgue integrable over [0, 1].
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

146 CHAPTER 11. INTEGRATION ON PRODUCT MEASURE SPACE
Solution
By Fubini’s theorem we have
∫
[0,1]×[0,1]
f (x, y)d(µL(x) × µL(y)) =
∫ 1
0
∫ 1
0
f (x, y)dxdy
=
∫ 1
0
∫ 1
0
[2g(x) − 3g(y)]dxdy
=
∫ 1
0
∫ 1
0
2g(x)dxdy −
∫ 1
0
∫ 1
0
3g(y)dxdy
= 2
∫ 1
0
g(x)
(∫ 1
0
1.dy
)
dx − 3
∫ 1
0
g(y)
(∫ 1
0
1.dx
)
dy
= 2
∫ 1
0
g(x).1.dx − 3
∫ 1
0
g(y).1.dy
= 2
∫ 1
0
g(x)dx − 3
∫ 1
0
g(y)dy
= −
∫ 1
0
g(x)dx.
Since f (x, y) is Lebesgue integrable over [0 , 1] × [0, 1]:⏐⏐⏐⏐
∫
[0,1]×[0,1]
f (x, y)d(µL(x) × µL(y))
⏐⏐⏐⏐ < ∞.
Therefore, ⏐⏐⏐⏐
∫ 1
0
g(x)dx
⏐⏐⏐⏐ < ∞.
That is g is Lebesgue (Riemann) integrable over [0 , 1]. ■
Problem 127
Let (X, M, µ) be a complete measure space and let f be a non-negative integrable
function on X. Let b(t) = µ{x ∈ X : f (x) ≥ t}. Show that
∫
X
f dµ =
∫ ∞
0
b(t)dt.
Solution
Deﬁne F : [0, ∞) × X →R by
F (t, x) =
{
1 if 0 ≤ t ≤ f (x)
0 if t > f (x).
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

147
If Et = {x ∈ X : f (x) ≥ t}, then F (t, x) = 1Et(x). We have
∫ ∞
0
F (t, x)dt =
∫ f (x)
0
F (t, x)dt +
∫ ∞
f (x)
F (t, x)dt = f (x) + 0 = f (x).
By Fubini’s theorem we have
∫
X
f dµ =
∫
X
(∫ f (x)
0
dt
)
dx
=
∫
X
(∫ ∞
0
F (t, x)dt
)
dx
=
∫ ∞
0
(∫
X
F (t, x)dx
)
dt
=
∫ ∞
0
(∫
X
1Et(x)dx
)
dt
=
∫ ∞
0
b(t)dt. (since µ(Et) = b(t) ) . ■
Problem 128
Consider the function u : [0, 1] × [0, 1] →R deﬁned by
u(x, y) =
{
x2−y2
(x2+y2)2 for (x, y) ⁄= (0, 0),
0 for (x, y) = (0 , 0).
(a) Calculate
∫ 1
0
(∫ 1
0
u(x, y)dy
)
dx and
∫ 1
0
(∫ 1
0
u(x, y)dx
)
dy.
Observation?
(b) Check your observation by using polar coordinates to show that
∫ ∫
D
|u(x, y)|dxdy = ∞,
that is, u is not integrable. Here D is the unit disk.
Answer.
(a) π
4 and − π
4 .
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

148 CHAPTER 11. INTEGRATION ON PRODUCT MEASURE SPACE
Problem 129
Let
I[0, 1], R+ = [0, ∞),
f (u, v) = 1
1 + u2v2 ,
g(x, y, t) = f (x, t)f (y, t), (x, y, t) ∈ I × I ×R+ := J.
(a) Show that g is integrable on J (equipped with Lebesgue measure). Using
Tonelli’s theorem on R+ × I × I show that
A =:
∫
J
gdtdxdy =
∫
R+
( arctan t
t
)2
dt.
(b) Using Tonelli’s theorem on I × I ×R+ show that
A = π
2
∫
I×I
1
x + y dxdy.
(c) Using Tonelli’s theorem again show that A = π ln 2.
Solution
(a) It is clear that g is continuous on R3, so measurable. Using Tonelli’s theorem on
R+ × I × I we have
A =
∫
R+
(∫
I×I
f (x, t)f (y, t)dxdy
)
dt
=
∫
R+
(∫
I
f (x, t)
(∫
I
f (y, t)dy
)
dx
)
dt
=
∫
R+
((∫
I
1
1 + x2t2 dx
) (∫
I
1
1 + y2t2 dy
))
dt
=
∫
R+
(∫
I
1
1 + x2t2 dx
)2
dt
=
∫
R+
( arctan t
t
)2
dt.
Note that for all t ∈R+, 0 < arctan t < π
2 and arctan t ∼ t as t → 0, so
A =
∫
R+
( arctan t
t
)2
dt < ∞.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

149
Thus g is integrable on J.
(b) We ﬁrst decompose g(x, y, t) = f (x, t)f (y, t) into simple elements:
g(x, y, t) = f (x, t)f (y, t) = 1
1 + x2t2 . 1
1 + y2t2
= 1
x2 − y2
[ x2
1 + x2t2 − y2
1 + y2t2
]
.
Using Tonelli’s theorem on I × I ×R+ we have
A =
∫
I×I
(∫
R+
1
x2 − y2
[ x2
1 + x2t2 − y2
1 + y2t2
]
dt
)
dxdy
=
∫
I×I
1
x2 − y2
(∫
R+
[ x
1 + s2 − y
1 + s2
]
ds
)
dxdy
=
∫
I×I
1
x + y
(∫ ∞
0
ds
1 + s2
)
dxdy
= π
2
∫
I×I
1
x + y dxdy.
(c) Using (b) and using Tonelli’s theorem again we get
A = π
2
∫ 1
0
(∫ 1
0
1
x + y dy
)
dx
= π
2
∫ 1
0
[ln(x + 1) − ln x]dx
= π
2 [(x + 1) ln(x + 1) − x ln x]x=1
x=0 = π ln 2. ■
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

150 CHAPTER 11. INTEGRATION ON PRODUCT MEASURE SPACE
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Chapter 12
Some More Real Analysis
Problems
Problem 130
Let (X, M, µ) be a measure space where the measure µ is positive. Consider a
sequence (An)n∈N in M such that
∞∑
n=1
µ(An) < ∞.
Prove that
µ
( ∞⋂
n=1
⋃
k≥n
Ak
)
= 0.
Hint:
Let Bn = ⋃
k≥n Ak. Then ( Bn) is a decreasing sequence in M with
µ(B1) =
∞∑
n=1
µ(An) < ∞.
Problem 131
Let (X, M, µ) be a measure space where the measure µ is positive.
Prove that (X, M, µ) is σ-ﬁnite if and only if there exists a function f ∈ L1(X)
and f (x) > 0, ∀x ∈ X.
151
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

152 CHAPTER 12. SOME MORE REAL ANALYSIS PROBLEMS
Hint:
• Consider the function
f (x) =
∞∑
n=1
1Xn (x)
2n[
µ(Xn) + 1
] .
It is clear that f (x) > 0, ∀x ∈ X. Just show that f is integrable on X.
• Conversely, suppose that there exists f ∈ L1(X) and f (x) > 0, ∀x ∈ X. For every n ∈N set
Xn =
{
x ∈ X : f (x) > 1
n + 1
}
.
Show that ∞⋃
n=1
Xn = X and µ(Xn) ≤ (n + 1)
∫
X
f dµ.
Problem 132
Let (X, M, µ) be a measure space where the measure µ is positive. Let f : X →
R+ be a measurable function such that
∫
X f dµ < ∞.
(a) Let N = {x ∈ X : f (x) = ∞}. Show that N ∈ M and µ(N ) = 0 .
(b) Given any ε > 0, show that there exists α > 0 such that
∫
E
f dµ < ε for any E ∈ M with µ(E) ≤ α.
Hint:
(a) N = f −1({∞}) and {∞} is closed.
For every n ∈N, n 1N ≤ f .
(b) Write
0 ≤
∫
E
f dµ =
∫
E∩N c
f dµ.
For every n ∈N set gn := f 1f >nf 1N c . Show that gn(x) → 0 for all x ∈ X.
Problem 133
Let ε > 0 be arbitrary. Construct an open set Ω ⊂R which is dense in R and
such that µL(Ω) < ε.
Hint:
WriteQ = {x1, x2, ...}. For each n ∈N let
In :=
(
xn − ε
2n+2 , xn + ε
2n+2
)
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

153
Then the In’s are open and Ω := ⋃∞
n=1 In ⊃Q.
Problem 134
Let (X, M, µ) be a measure space. Suppose µ is positive and µ(X) = 1 (so
(X, M, µ) is a probability space). Consider the family
T := {A ∈ M : µ(A) = 0 or µ (A) = 1 }.
Show that T is a σ-algebra.
Hint:
Let ( An)n∈N ⊂ M. Let A = ⋃
n∈N An.
If µ(A) = 0, then A ∈ T .
If µ(An0) = 1 for some n0 ∈N, then
1 = µ(An0 ) ≤ µ(A) ≤ µ(X) = 1 .
Problem 135
For every n ∈N, consider the functions fn and gn deﬁned on R by
fn(x) = nα
(|x| + n)β where α, β ∈R and β > 1
gn(x) = nγe−n|x| where γ ∈R.
(a) Show that fn ∈ Lp(R) and compute ‖fn‖p for 1 ≤ p ≤ ∞.
(b) Show that gn ∈ Lp(R) and compute ‖gn‖p for 1 ≤ p ≤ ∞.
(c) Use (a) and (b) to show that, for 1 ≤ p < q ≤ ∞, the topologies induced on
Lp ∩ Lq by Lp and Lq are not comparable.
Hint:
(a)
• For 1 ≤ p < ∞ we have
‖fn‖p = 2
1
p (βp − 1)− 1
p nα−β+ 1
p .
• For p = ∞ we have
‖fn‖∞ = lim
p→∞
‖fn‖p = nα−β.
(b)
• For p = ∞ we have
‖gn‖∞ = nγ.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

154 CHAPTER 12. SOME MORE REAL ANALYSIS PROBLEMS
• For 1 ≤ p < ∞ we have
‖gn‖p = 2
1
p nγ− 1
p p− 1
p .
(c) If the topologies induced on Lp ∩ Lq by Lp and Lq are comparable, then, for ϕn ∈ Lp ∩ Lq, we
must have
(∗) lim
n→∞
‖ϕn‖p = 0 =⇒ lim
n→∞
‖ϕn‖q = 0.
Find an example which shows that the above assumption is not true. For example:
ϕn = n−γ+ 1
q gn.
Problem 136
(a) Show that any non-empty open set in Rn has strictly positive Lebesgue mea-
sure.
(b) Is the assertion in (a) true for closed sets in Rn?
Hint:
(a) For any ε > 0, consider the open ball in Rn
B2ε(0) =
{
x = (x1, .., xn) : x2
1 + ... + x2
n < 4ε2}
.
For each n ∈R, let In(0) :=
[
− ε√n , ε√
k
)
. Show that
Iε(0) := In(0) × ... × In(0)| {z }
n
⊂ B2ε(0).
(b) No.
Problem 137
(a) Construct an open and unbounded set in R with ﬁnite and strictly positive Lebesgue mea-
sure.
(b) Construct an open, unbounded and connected set in R2 with ﬁnite and strictly positive
Lebesgue measure.
(c) Can we ﬁnd an open, unbounded and connected set in R with ﬁnite and strictly positive
Lebesgue measure?
Hint:
(a) For each k = 0, 1, 2, ... let
Ik =
(
k − 1
2k , k + 1
2k
)
.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

155
Then show that I = ⋃∞
k=0 Ik satisﬁes the question.
(b) For each k = 1, 2, ... let
Bk =
(
− 1
2k , 1
2k
)
× (−k, k).
Then show that B = ⋃∞
k=0 Bk satisﬁes the question.
(c) No. Why?
Problem 138
Given a measure space (X, A, µ). A sequence (fn) of real-valued measurable
functions on a set D ∈ A is said to be a Cauchy sequence in measure if given
any ε > 0, there is an N such that for all n, m ≥ N we have
µ{x : |fn(x) − fm(x)| ≥ ε} < ε.
(a) Show that if fn
µ
− →f on D, then (fn) is a Cauchy sequence in measure on D.
(b) Show that if (fn) is a Cauchy sequence in measure, then there is a function
f to which the sequence (fn) converges in measure.
Hint:
(a) For any ε > 0, there exists N > 0 such that for n, m ≥ N we have
µ{D : |fm − fn| ≥ ε} ≤ µ
{
D : |fm − f | ≥ ε
2
}
+ µ
{
D : |fn − f | ≥ ε
2
}
.
(b) By deﬁnition,
for δ = 1
2 , ∃n1 ∈N : µ
{
D : |fn1+p − fn1 | ≥ 1
2
}
< 1
2 for all p ∈N.
In general,
for δ = 1
2k , ∃nk ∈N, n k > n k−1 : µ
{
D : |fnk+p − fnk | ≥ 1
2k
}
< 1
2k for all p ∈N.
Since nk+1 = nk + p for some p ∈N, so we have
µ
{
D : |fnk+1 − fnk | ≥ 1
2k
}
< 1
2k for k ∈N.
Let gk = fnk . Show that ( gk) converges a.e. on D. Let Dc := {x ∈ D : lim k→∞ gk(x) ∈ R}.
Deﬁne f by f (x) = lim k→∞ gk(x) for x ∈ Dc and f (x) = 0 for x ∈ D \ Dc. Then show that gk
µ
− →f
on D. Finally show that fn
µ
− →f on D.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

156 CHAPTER 12. SOME MORE REAL ANALYSIS PROBLEMS
Problem 139
Check whether the following functions are Lebesgue integrable :
(a) u(x) = 1
x , x ∈ [1, ∞).
(b) v(x) = 1√x , x ∈ (0, 1].
Hint:
(a) u(x) is NOT Lebesgue integrable on [1 , ∞).
∫
[1,∞)
u(x)dµL(x) = lim
n→∞
∫ 1
x 1[1,n)(x)dµL(x) = lim
n→∞
∫ n
1
1
x dx.
(b) v(x) is Lebesgue integrable on (0 , 1].
We can write
v(x) = 1√x , x ∈ (0, 1] = 1√x 1(0,1](x) = sup
n
1√x 1[ 1
n ,1](x).
Use the Monotone Convergence Theorem for the sequence
( 1√x 1[ 1
n ,1]
)
n∈N.
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

Bibliography
[1] Wheeden, L.R.; Zygmund, A. Measure and Integral. Marcel Dekker. New York, 1977.
[2] Folland. G.B. Real Analysis. John Wiley and Sons. New York, 1985.
[3] Rudin. W. Real and Complex Analysis. Third edition. McGraw-Hill, Inc. New York, 1987.
[4] Royden. H.L. Real Analysis. Third edition. Prentice Hall. NJ, 1988.
[5] Rudin. W Functional Analysis. McGraw-Hill, Inc. New York, 1991.
[6] Hunter. J.K.; Nachtergaele. B. Applied Analysis. World Scientiﬁc. NJ, 2001.
[7] Yeh, J. Real Analysis. Theory of measure and integration. Second edition. World Scientiﬁc.
NJ, 2006.
157
www.MATHVN.com - Anh Quang Le, PhD
www.MathVn.com - Math Vietnam

