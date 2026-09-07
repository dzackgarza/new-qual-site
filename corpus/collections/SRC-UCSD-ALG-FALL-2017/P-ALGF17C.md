---
schema: qual/card@1
id: P-ALGF17C
kind: problem
title: Zorn's lemma; maximal ideals missing a multiplicative set; primeness
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2017; all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the chain-upper-bound argument for Zorn's lemma and the standard maximal-disjoint-ideal proof of primality.
---

::: {.problem}
(a) Carefully state Zorn's Lemma.

(b) Let $R$ be a commutative ring and let $X$ be any multiplicatively closed subset of $R$ which does not contain $0$.
Show that $R$ has an ideal $I$ which is a maximal element of the collection of those ideals $J$ such that $J \cap X = \emptyset$.

(c) If $X$ is not empty then prove that the ideal $I$ as in (b) must be a prime ideal.
:::

::: {.solution}
<1>1. Zorn's Lemma states: if every chain in a nonempty partially ordered set has an upper bound in that partially ordered set, then the partially ordered set has a maximal element.
::: {.proof}
This is the statement of Zorn's Lemma used in the remaining parts.
:::

<1>2. Let
\[
\mathcal P:=\{J\triangleleft R:J\cap X=\varnothing\},
\]
ordered by inclusion. Then $\mathcal P$ is nonempty.
::: {.proof}
Since $0\notin X$, the zero ideal satisfies
\[
(0)\cap X=\varnothing.
\]
Hence
\[
(0)\in\mathcal P.
\]
:::

<1>3. Every chain in $\mathcal P$ has an upper bound in $\mathcal P$.
::: {.proof}
Let $\mathcal C\subseteq\mathcal P$ be a chain and set
\[
J:=\bigcup_{I\in\mathcal C}I.
\]
Because $\mathcal C$ is totally ordered by inclusion, $J$ is an ideal: if $a,b\in J$, then $a\in I_1$ and $b\in I_2$ for some $I_1,I_2\in\mathcal C$; one of these ideals contains the other, so both $a$ and $b$ lie in a common member of the chain and hence $a-b\in J$. Closure under multiplication by elements of $R$ is immediate.

If $J\cap X$ were nonempty, choose
\[
x\in J\cap X.
\]
Then $x\in I$ for some $I\in\mathcal C$, contradicting
\[
I\cap X=\varnothing.
\]
Thus
\[
J\cap X=\varnothing,
\]
so $J\in\mathcal P$. It contains every member of $\mathcal C$, hence is an upper bound.
:::

<1>4. There is an ideal $I$ maximal among the ideals disjoint from $X$.
::: {.proof}
By <1>2, $\mathcal P$ is nonempty, and by <1>3 every chain in $\mathcal P$ has an upper bound in $\mathcal P$.
Zorn's Lemma therefore gives a maximal element
\[
I\in\mathcal P.
\]
Equivalently,
\[
I\cap X=\varnothing
\]
and no strictly larger ideal has empty intersection with $X$.
This proves part (b).
:::

<1>5. If $X\neq\varnothing$, then $I$ is a proper ideal.
::: {.proof}
If $I=R$, then every element of the nonempty set $X$ would lie in $I$, so
\[
I\cap X=X\neq\varnothing,
\]
contrary to the defining property of $I$.
Thus
\[
I\neq R.
\]
:::

<1>6. If $ab\in I$ and $a,b\notin I$, then one obtains an element of $I\cap X$.
::: {.proof}
Assume
\[
ab\in I,
\qquad
a\notin I,
\qquad
b\notin I.
\]
Then the ideals $I+(a)$ and $I+(b)$ strictly contain $I$.
By maximality of $I$ among ideals disjoint from $X$, both larger ideals meet $X$.
Choose
\[
x\in(I+(a))\cap X,
\qquad
y\in(I+(b))\cap X.
\]
Write
\[
x=i+ra,
\qquad
y=j+sb
\]
with $i,j\in I$ and $r,s\in R$.
Since $X$ is multiplicatively closed,
\[
xy\in X.
\]
But
\[
xy=ij+isb+jra+rsab.
\]
Every term on the right lies in $I$: the first three because $i,j\in I$, and the last because $ab\in I$.
Therefore
\[
xy\in I\cap X,
\]
a contradiction.
:::

<1>7. The ideal $I$ is prime.
::: {.proof}
By <1>5, $I$ is proper.
If $ab\in I$, then <1>6 shows that it is impossible for both $a$ and $b$ to lie outside $I$.
Hence
\[
a\in I\quad\text{or}\quad b\in I.
\]
Thus $I$ is prime, proving part (c).
:::
:::
