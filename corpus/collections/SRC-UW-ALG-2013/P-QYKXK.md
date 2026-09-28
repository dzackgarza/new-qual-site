---
schema: qual/card@1
id: P-QYKXK
kind: problem
title: $(5,x^2+2)$ is prime in $\mathbb{Z}[x,y]$ with infinitely many maximal extensions
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Ideals
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
This question concerns the polynomial ring $R=\mathbb Z[x,y]$ and the ideal $I=(5,x^2+2)$ in $R$.

- Prove that $I$ is a prime ideal of $R$ and that $R/I$ is a PID.

- Give an explicit example of a maximal ideal of $R$ which contains $I$.
  (Give a set of generators for such an ideal.)

- Show that there are infinitely many distinct maximal ideals in $R$ which contain $I$.
:::


::: {.solution}
<1>1. There is an isomorphism
\[
R/I\cong \mathbb F_5[x,y]/(x^2+2).
\]
:::

<1>2. The polynomial \(x^2+2\in\mathbb F_5[x]\) is irreducible.
::: {.proof}
The squares in \(\mathbb F_5\) are
\[
0,1,4.
\]
Thus \(-2\equiv3\pmod5\) is not a square, so \(x^2+2\) has no root in \(\mathbb F_5\). Since it has degree \(2\), it is irreducible.
:::

<1>3. Hence
\[
R/I\cong \mathbb F_{25}[y].
\]
In particular, \(I\) is prime and \(R/I\) is a PID.
::: {.proof}
By <1>2,
\[
\mathbb F_5[x]/(x^2+2)
\]
is a field with \(5^2=25\) elements. Therefore
\[
\mathbb F_5[x,y]/(x^2+2)
\cong
\bigl(\mathbb F_5[x]/(x^2+2)\bigr)[y]
\cong \mathbb F_{25}[y].
\]
A polynomial ring in one variable over a field is a PID and an integral domain. Therefore \(R/I\) is a domain, so \(I\) is prime.
:::

<1>4. The ideal
\[
\mathfrak m=(5,x^2+2,y)
\]
is a maximal ideal of \(R\) containing \(I\).
::: {.proof}
We have
\[
R/\mathfrak m
\cong \mathbb F_5[x]/(x^2+2)
\cong \mathbb F_{25},
\]
which is a field. Hence \(\mathfrak m\) is maximal.
:::

<1>5. The ring \(\mathbb F_{25}[y]\) has infinitely many monic irreducible polynomials.
::: {.proof}
Suppose instead that the monic irreducible polynomials were exactly
\[
q_1(y),\dots,q_r(y).
\]
Consider
\[
Q(y)=q_1(y)\cdots q_r(y)+1.
\]
This is a nonconstant polynomial, so it has an irreducible factor \(q(y)\). But no \(q_i\) divides \(Q\), because
\[
Q\equiv1\pmod{q_i}.
\]
Thus \(q\) is a monic irreducible not on the list, a contradiction.
:::

<1>6. There are infinitely many distinct maximal ideals of \(R\) containing \(I\).
::: {.proof}
By the correspondence theorem, maximal ideals of \(R\) containing \(I\) are in bijection with maximal ideals of
\[
R/I\cong\mathbb F_{25}[y].
\]
Since this is a PID, each monic irreducible \(q(y)\in\mathbb F_{25}[y]\) generates a maximal ideal \((q)\), and distinct monic irreducibles give distinct maximal ideals. By <1>5 there are infinitely many of them. Their inverse images under the quotient map \(R\to R/I\) are therefore infinitely many distinct maximal ideals of \(R\) containing \(I\).
:::
