---
schema: qual/card@1
id: P-ALGF06E
kind: problem
title: "Local versus non-local polynomial quotient rings over Q(X) and Q[X,Y]"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 3.1 of the official UCSD Algebra Qualifying Examination, Fall 2006; all three parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified irreducibility of Y^2+X over Q(X), the unique maximal ideal of R_1, two distinct rational-point maximal ideals of R_2, and the nonmaximal prime induced by (Y^2+X).
---

::: {.problem}
Let $X$ and $Y$ be two independent variables.

(a) Prove that the ring $R_1 := \mathbb{Q}(X)[Y]/((Y^2 + X)^3)$ is a local ring.

(b) Prove that the ring $R_2 := \mathbb{Q}[X,Y]/((Y^2 + X)^3)$ is not a local ring by giving examples (with proof) of two distinct maximal ideals in $R_2$.

(c) Give an example of a prime ideal in $R_2$ which is not maximal.
Are there such ideals in $R_1$?
Justify your answers.
:::


::: {.solution}
Write
\[
f:=Y^2+X.
\]

<1>1. The polynomial $f$ is irreducible in $\mathbb Q(X)[Y]$.
::: {.proof}
Because $f$ is quadratic in $Y$, it is reducible over $\mathbb Q(X)$ if and only if it has a root in $\mathbb Q(X)$.
Such a root would give an element $r(X)\in\mathbb Q(X)$ satisfying
\[
r(X)^2=-X.
\]
Let $v_X$ denote the exponent of $X$ in a nonzero rational function: if
\[
r(X)=X^k\frac{a(X)}{b(X)},
\qquad
a(0)b(0)\neq0,
\]
then $v_X(r)=k$.
For every nonzero $r$,
\[
v_X(r^2)=2v_X(r)
\]
is even, whereas
\[
v_X(-X)=1.
\]
Therefore $-X$ is not a square in $\mathbb Q(X)$, so $f$ has no root and is irreducible.
:::

<1>2. The ring
\[
R_1=\mathbb Q(X)[Y]/(f^3)
\]
is local, with unique maximal ideal
\[
\mathfrak m_1=(f)/(f^3).
\]
::: {.proof}
Since $\mathbb Q(X)$ is a field, $\mathbb Q(X)[Y]$ is a principal ideal domain.
By <1>1, the irreducible polynomial $f$ generates a maximal ideal $(f)$.

Maximal ideals of $R_1$ correspond to maximal ideals $M$ of $\mathbb Q(X)[Y]$ containing $(f^3)$.
If $f^3\in M$, then $f\in M$ because every maximal ideal is prime.
Hence
\[
(f)\subseteq M.
\]
Since $(f)$ itself is maximal, this forces
\[
M=(f).
\]
Thus $R_1$ has exactly one maximal ideal, namely $(f)/(f^3)$, and is local.
:::

<1>3. The ring
\[
R_2=\mathbb Q[X,Y]/(f^3)
\]
has at least two distinct maximal ideals.
::: {.proof}
In $\mathbb Q[X,Y]$, consider
\[
\mathfrak m=(X,Y)
\]
and
\[
\mathfrak n=(X+1,Y-1).
\]
Both are maximal because evaluation at $(0,0)$ and $(-1,1)$ gives
\[
\mathbb Q[X,Y]/\mathfrak m\cong\mathbb Q,
\qquad
\mathbb Q[X,Y]/\mathfrak n\cong\mathbb Q.
\]
Moreover,
\[
f(0,0)=0
\]
and
\[
f(-1,1)=1-1=0,
\]
so
\[
f\in\mathfrak m\cap\mathfrak n.
\]
Hence $(f^3)$ is contained in both maximal ideals.
Their images
\[
\overline{\mathfrak m}:=\mathfrak m/(f^3),
\qquad
\overline{\mathfrak n}:=\mathfrak n/(f^3)
\]
are therefore maximal ideals of $R_2$.
They are distinct because, for example,
\[
X\in\mathfrak m
\]
but
\[
X\notin\mathfrak n
\]
as $X(-1,1)=-1\neq0$.
Thus $R_2$ is not local.
:::

<1>4. The ideal
\[
\mathfrak p:=(f)/(f^3)\subset R_2
\]
is prime but not maximal.
::: {.proof}
The quotient by $\mathfrak p$ is
\[
R_2/\mathfrak p
\cong
\mathbb Q[X,Y]/(f).
\]
Since
\[
f=X+Y^2,
\]
substituting $X=-Y^2$ gives an isomorphism
\[
\mathbb Q[X,Y]/(X+Y^2)\cong\mathbb Q[Y].
\]
The ring $\mathbb Q[Y]$ is an integral domain, so $\mathfrak p$ is prime.
It is not a field, so $\mathfrak p$ is not maximal.
:::

<1>5. There are no prime ideals of $R_1$ which are not maximal.
::: {.proof}
Every prime ideal contains every nilpotent element.
In $R_1$, the ideal
\[
\mathfrak m_1=(f)/(f^3)
\]
consists of nilpotent elements modulo $(f^3)$ in the sense that every element of the ideal has a sufficiently high power equal to zero.
Thus every prime ideal of $R_1$ contains $\mathfrak m_1$.
But <1>2 shows that $\mathfrak m_1$ is maximal.
Therefore every prime ideal equals $\mathfrak m_1$, so every prime ideal of $R_1$ is maximal.
:::
:::
