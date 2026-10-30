---
schema: qual/card@1
id: P-CASP22B
kind: problem
title: "Schwarz lemma for polynomial preimages: zeros, bounds, and equality cases"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Polynomials
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $p(z)$ be a nonconstant polynomial.
Let $G \subset \CC$ be a component of the set $\{z : \abs{p(z)} < 1\}$.

(a) Show that $p$ has at least one zero in $G$.

(b) Let $f$ be analytic in $G$ with $\abs{f} \leq 1$.
Assume that $f$ has a zero at every zero of $p$ such that the order of vanishing of $f$ is at least that of $p$.
Show that $\abs{f(z)} \leq \abs{p(z)}$ and if $z = a$ is a zero of $p$ of order $k$, then $\abs{f^{(k)}(a)} \leq \abs{p^{(k)}(a)}$.

(c) If either $\abs{f(a)} = \abs{p(a)}$ for some $z = a$ that is not a zero of $p$ or if $\abs{f^{(k)}(a)} = \abs{p^{(k)}(a)}$ for some $z = a$ that is a zero of $p$ of order $k$, then $f(z) = cp(z)$ for some constant $c$.
:::

::: {.solution}
Every component $G$ of $\{\abs{p}<1\}$ is bounded, because $\abs{p(z)}\to\infty$
as $\abs{z}\to\infty$, and every boundary point of $G$ satisfies $\abs{p}=1$.

(a) Suppose $p$ had no zero in $G$. Then $1/p$ would be holomorphic on $G$
and continuous up to its boundary, with
$$
\abs{\frac1p}=1
$$
on $\partial G$, but $\abs{1/p}>1$ in $G$. This contradicts the maximum modulus
principle. Hence $p$ has at least one zero in $G$.

(b) By the assumed zero multiplicities, the quotient
$$
q=\frac fp
$$
extends holomorphically across every zero of $p$ in $G$. On $\partial G$,
$$
\abs{q}=\frac{\abs{f}}{\abs{p}}\le1.
$$
The maximum modulus principle therefore gives $\abs{q}\le1$ in $G$, so
$$
\abs{f(z)}\le\abs{p(z)}.
$$
If $a$ is a zero of $p$ of order $k$, write
$$
p(z)=(z-a)^kP(z),\qquad f(z)=(z-a)^kF(z).
$$
Then $q(a)=F(a)/P(a)$ and
$$
\abs{q(a)}
=\abs{\frac{f^{(k)}(a)}{p^{(k)}(a)}}
\le1,
$$
which proves the derivative inequality.

(c) Either asserted equality says that $\abs{q}$ attains its maximum value $1$ at
an interior point of $G$. Hence the maximum modulus principle forces
$q\equiv c$ with $\abs{c}=1$. Therefore
$$
\boxed{f=cp.}
$$
:::
