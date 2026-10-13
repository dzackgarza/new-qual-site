---
schema: qual/card@1
id: P-KSRING17-052
kind: problem
title: Ideals maximal with respect to missing a multiplicative set are prime, and the nilradical
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 52 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a non-zero commutative ring with 1.

(a) Let S be a multiplicative subset of R not containing 0 and let P be maximal in the set of ideals of R not intersecting S. Show that P is a prime ideal.

(b) Show that the set of nilpotent elements of R is the intersection of all prime ideals.
:::

::: {.solution}
<1>1. In part (a), the ideal $P$ is proper.

::: {.proof}
Since $S$ is multiplicative,
$$
1\in S.
$$
The hypothesis
$$
P\cap S=\varnothing
$$
therefore implies
$$
1\notin P.
$$
Hence
$$
P\ne R.
$$
:::

<1>2. Suppose
$$
ab\in P
$$
with
$$
a\notin P.
$$
Then
$$
P+(a)
$$
meets $S$.

::: {.proof}
Because
$$
a\notin P,
$$
one has
$$
P\subsetneq P+(a).
$$
If
$$
(P+(a))\cap S=\varnothing,
$$
then $P+(a)$ would be an ideal disjoint from $S$ properly containing $P$, contradicting maximality of $P$. Therefore
$$
(P+(a))\cap S\ne\varnothing.
$$
:::

<1>3. If also
$$
b\notin P,
$$
then
$$
P+(b)
$$
meets $S$.

::: {.proof}
The proof is identical to step <1>2, with $b$ in place of $a$.
:::

<1>4. Under the assumptions
$$
ab\in P,
\qquad
a\notin P,
\qquad
b\notin P,
$$
choose
$$
s\in(P+(a))\cap S,
\qquad
t\in(P+(b))\cap S.
$$
Then
$$
st\in P.
$$

::: {.proof}
Write
$$
s=p+ra,
\qquad
t=q+ub
$$
with
$$
p,q\in P,
\qquad
r,u\in R.
$$
Then
$$
\begin{aligned}
st
&=
(p+ra)(q+ub)\\
&=
pq+pub+raq+ruab.
\end{aligned}
$$
The first three terms lie in $P$ because $p,q\in P$, and the last term lies in $P$ because
$$
ab\in P.
$$
Thus
$$
st\in P.
$$
:::

<1>5. The assumptions in step <1>4 are impossible.

::: {.proof}
Since
$$
s,t\in S
$$
and $S$ is multiplicatively closed,
$$
st\in S.
$$
Step <1>4 gives
$$
st\in P.
$$
Hence
$$
st\in P\cap S,
$$
contradicting
$$
P\cap S=\varnothing.
$$
:::

<1>6. Therefore
$$
\boxed{P\text{ is prime}.}
$$

::: {.proof}
Step <1>1 shows that $P$ is proper. If
$$
ab\in P,
$$
step <1>5 shows that it is impossible for both $a$ and $b$ to lie outside $P$. Hence
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
Thus $P$ is prime.
:::

<1>7. Let
$$
\mathcal N
\coloneqq
\{x\in R:x^n=0\text{ for some }n\ge1\}
$$
be the set of nilpotent elements.
Every prime ideal contains $\mathcal N$.

::: {.proof}
Let
$$
\mathfrak p
$$
be prime and let
$$
x\in\mathcal N.
$$
Choose
$$
n\ge1
$$
with
$$
x^n=0.
$$
Then
$$
x^n\in\mathfrak p.
$$
If
$$
n=1,
$$
then immediately
$$
x\in\mathfrak p.
$$
For
$$
n>1,
$$
write
$$
x^n=x\cdot x^{n-1}.
$$
Primality gives
$$
x\in\mathfrak p
\quad\text{or}\quad
x^{n-1}\in\mathfrak p.
$$
If the second alternative occurs, repeat. After finitely many steps one obtains
$$
x\in\mathfrak p.
$$
Thus
$$
\mathcal N\subseteq\mathfrak p
$$
for every prime ideal $\mathfrak p$.
:::

<1>8. Consequently,
$$
\mathcal N
\subseteq
\bigcap_{\mathfrak p\text{ prime}}\mathfrak p.
$$

::: {.proof}
This is exactly step <1>7 after intersecting over all prime ideals.
:::

<1>9. Let
$$
x\in R
$$
be non-nilpotent, and define
$$
S_x
\coloneqq
\{1,x,x^2,x^3,\ldots\}.
$$
Then
$$
0\notin S_x.
$$

::: {.proof}
If
$$
0\in S_x,
$$
then
$$
x^n=0
$$
for some
$$
n\ge0.
$$
Since
$$
1\ne0,
$$
one must have
$$
n\ge1,
$$
which would make $x$ nilpotent. This contradicts the choice of $x$.
:::

<1>10. There exists an ideal
$$
P
$$
maximal among ideals disjoint from
$$
S_x.
$$

::: {.proof}
Let
$$
\mathcal P_x
\coloneqq
\{
I\trianglelefteq R:
I\cap S_x=\varnothing
\},
$$
ordered by inclusion.

The zero ideal lies in $\mathcal P_x$ by step <1>9, so the poset is nonempty.

Let
$$
\mathcal C
\subseteq
\mathcal P_x
$$
be a chain and set
$$
U
\coloneqq
\bigcup_{I\in\mathcal C}I.
$$
As in the standard Zorn argument, total ordering of the chain implies that $U$ is an ideal.

If
$$
U\cap S_x\ne\varnothing,
$$
choose
$$
s\in U\cap S_x.
$$
Then $s$ lies in some
$$
I\in\mathcal C,
$$
contradicting
$$
I\cap S_x=\varnothing.
$$
Thus
$$
U\in\mathcal P_x,
$$
and it is an upper bound for the chain.

By Zorn's lemma, $\mathcal P_x$ has a maximal element $P$.
:::

<1>11. The ideal $P$ from step <1>10 is prime.

::: {.proof}
The multiplicative set
$$
S_x
$$
does not contain $0$ by step <1>9, and $P$ is maximal among ideals disjoint from $S_x$. Therefore part (a), proved in step <1>6, applies and gives
$$
P\text{ prime}.
$$
:::

<1>12. The prime ideal $P$ from step <1>11 does not contain $x$.

::: {.proof}
One has
$$
x\in S_x.
$$
But
$$
P\cap S_x=\varnothing.
$$
Therefore
$$
x\notin P.
$$
:::

<1>13. Hence every non-nilpotent element is omitted by some prime ideal.

::: {.proof}
Given any non-nilpotent
$$
x\in R,
$$
steps <1>9--<1>12 construct a prime ideal $P$ with
$$
x\notin P.
$$
:::

<1>14. Therefore
$$
\bigcap_{\mathfrak p\text{ prime}}\mathfrak p
\subseteq
\mathcal N.
$$

::: {.proof}
Suppose
$$
x\notin\mathcal N.
$$
By step <1>13, there exists a prime ideal $\mathfrak p$ such that
$$
x\notin\mathfrak p.
$$
Hence
$$
x\notin
\bigcap_{\mathfrak p\text{ prime}}\mathfrak p.
$$
Taking the contrapositive yields the claimed containment.
:::

<1>15. Consequently,
$$
\boxed{
\mathcal N
=
\bigcap_{\mathfrak p\text{ prime}}\mathfrak p.
}
$$

::: {.proof}
Step <1>8 gives one inclusion and step <1>14 gives the reverse inclusion.
:::

<1>16. Q.E.D.

::: {.proof}
Step <1>6 proves part (a), and step <1>15 proves part (b).
:::
:::
