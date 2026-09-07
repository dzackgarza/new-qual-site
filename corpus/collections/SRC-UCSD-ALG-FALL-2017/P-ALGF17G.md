---
schema: qual/card@1
id: P-ALGF17G
kind: problem
title: Algebraic elements over $K$ in $L$ when $M \cap A = K$; degree bounds
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 7 of the official UCSD Algebra Qualifying Exam, Fall 2017; all three parts and the characteristic-zero hypothesis agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified descent of minimal-polynomial coefficients through M cap A = K, the primitive-element degree comparison, and the finite-subextension argument bounding A/K.
---

::: {.problem}
Let $L/M/K$ be field extensions with $[L : M] < \infty$.
Let $A$ be the subfield of $L$ consisting of all elements of $L$ that are algebraic over $K$.
Suppose that $M \cap A = K$.

(a) If $\alpha \in A$ and $f(x) \in M[x]$ is the minimal polynomial of $\alpha$ over $M$ then show that $f(x) \in K[x]$.

(b) Now suppose, for the rest of this question, that the characteristic is zero.
If $K \subset B \subset A$ is an intermediary field and $[B : K] < \infty$ then show that
\[
[B : K] \leq [L : M].
\]

(c) Prove that $[A : K] \leq [L : M]$.
:::

::: {.solution}
<1>1. If $\alpha\in A$ and $f(x)\in M[x]$ is its minimal polynomial over $M$, then every coefficient of $f$ is algebraic over $K$.
::: {.proof}
Let
\[
g(x)\in K[x]
\]
be the minimal polynomial of $\alpha$ over $K$.
Since $K\subseteq M$, the polynomial $f$ divides $g$ in $M[x]$.
Fix an algebraic closure containing a splitting field of $g$.
All roots of $g$ are algebraic over $K$.
Because $f$ is monic and divides $g$, its roots, counted with multiplicity, form a submultiset of the roots of $g$.
The coefficients of $f$ are elementary symmetric polynomials in those roots.
Hence every coefficient of $f$ is algebraic over $K$.
:::

<1>2. The minimal polynomial $f(x)$ from part (a) belongs to $K[x]$.
::: {.proof}
By definition,
\[
f(x)\in M[x].
\]
By <1>1, every coefficient of $f$ is algebraic over $K$.
Since the coefficients lie in $M\subseteq L$, they therefore belong to the subfield $A$ of elements of $L$ algebraic over $K$.
Thus every coefficient lies in
\[
M\cap A=K.
\]
Hence
\[
f(x)\in K[x].
\]
This proves part (a).
:::

<1>3. In characteristic zero, if $K\subseteq B\subseteq A$ and $[B:K]<\infty$, then there is an element $\alpha\in B$ with
\[
B=K(\alpha).
\]
::: {.proof}
A finite extension in characteristic zero is separable.
The primitive element theorem therefore applies to $B/K$, giving
\[
B=K(\alpha)
\]
for some $\alpha\in B$.
:::

<1>4. For the element $\alpha$ from <1>3, its minimal polynomial over $M$ is the same as its minimal polynomial over $K$.
::: {.proof}
Let
\[
g(x)\in K[x]
\]
be the minimal polynomial of $\alpha$ over $K$, and let
\[
f(x)\in M[x]
\]
be the minimal polynomial over $M$.
Since $\alpha\in B\subseteq A$, part (a), proved in <1>2, gives
\[
f(x)\in K[x].
\]
Also $f$ divides $g$ in $M[x]$ and both are monic.
Now $g$ is irreducible in $K[x]$, while $f\in K[x]$ is a nonconstant divisor of $g$.
Therefore
\[
f=g.
\]
Consequently
\[
[M(\alpha):M]
=\deg f
=\deg g
=[K(\alpha):K]
=[B:K].
\]
:::

<1>5. Every finite intermediate field $B$ as in part (b) satisfies
\[
[B:K]\le[L:M].
\]
::: {.proof}
By <1>3 and <1>4,
\[
[B:K]=[M(\alpha):M].
\]
Since
\[
\alpha\in B\subseteq A\subseteq L,
\]
and $M\subseteq L$, one has
\[
M(\alpha)\subseteq L.
\]
The tower law therefore gives
\[
[M(\alpha):M]\le[L:M].
\]
Hence
\[
[B:K]\le[L:M].
\]
This proves part (b).
:::

<1>6. The whole algebraic extension $A/K$ satisfies
\[
[A:K]\le[L:M].
\]
::: {.proof}
Set
\[
d:=[L:M].
\]
Suppose, toward a contradiction, that
\[
[A:K]>d.
\]
Then there exist $d+1$ elements
\[
\alpha_1,\ldots,\alpha_{d+1}\in A
\]
which are linearly independent over $K$.
Because every $\alpha_i$ is algebraic over $K$, the field
\[
B:=K(\alpha_1,\ldots,\alpha_{d+1})
\]
is a finite extension of $K$ contained in $A$.
Its $K$-dimension is at least $d+1$, since it contains the $d+1$ linearly independent elements above.
Thus
\[
[B:K]\ge d+1,
\]
contradicting part (b), which gives
\[
[B:K]\le d.
\]
Therefore
\[
[A:K]\le d=[L:M].
\]
This proves part (c).
:::
:::
