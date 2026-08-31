---
schema: qual/card@1
id: P-APAS15E
kind: problem
title: Finite variety implies finite-dimensional quotient; counterexample over a non-algebraically closed field
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $K$ be an algebraically closed field, let $K^n$ be affine $n$-space over $K$, and consider the polynomial ring $K[x_1, \ldots, x_n]$.

(1) Suppose that $I \subseteq K[x_1, \ldots, x_n]$ is an ideal such that $V(I) \subseteq K^n$ is a finite set.
Prove that $K[x_1, \ldots, x_n]/I$ is a finite-dimensional $K$-vector space.

(2) Let $F$ be a field which is not algebraically closed.
Prove that there exists an ideal $I \subseteq F[x, y]$ such that $V(I) = \emptyset$ but $F[x, y]/I$ is an infinite-dimensional $F$-vector space.
:::

::: {.solution}
**Goal.** (1) Finite $V(I)$ forces $K[x_1,\dots,x_n]/I$ finite-dimensional over an algebraically closed $K$. (2) Over a non-algebraically-closed field, $V(I) = \emptyset$ need not force finite-dimensionality.

<1>1. (1) $K[x_1,\dots,x_n]/I$ is finite-dimensional.
<2>1. $V(I)$ finite means $\sqrt I$ is a finite intersection of maximal ideals.
::: {.proof}
by the Nullstellensatz (over algebraically closed $K$), $V(I) = \theset{\mathfrak m_1, \dots, \mathfrak m_r}$ implies $\sqrt I = \mathfrak m_1 \cap \cdots \cap \mathfrak m_r$.
:::
<2>2. Some power of $\sqrt I$ lies in $I$.
::: {.proof}
$\sqrt I$ is finitely generated, so $(\sqrt I)^N \subseteq I$ for some $N$.
:::
<2>3. $K[x_1,\dots,x_n]/\sqrt I$ is finite-dimensional.
::: {.proof}
$\sqrt I = \bigcap_j \mathfrak m_j$ with each $\mathfrak m_j$ maximal, so $K[x_1,\dots,x_n]/\sqrt I \cong \prod_j K[x_1,\dots,x_n]/\mathfrak m_j \cong K^r$ (each quotient is $K$ by the Nullstellensatz).
:::
<2>4. $K[x_1,\dots,x_n]/I$ is finite-dimensional.
::: {.proof}
$I \supseteq (\sqrt I)^N$ gives a surjection $K[x_1,\dots,x_n]/(\sqrt I)^N \surjects K[x_1,\dots,x_n]/I$, and $K[x_1,\dots,x_n]/(\sqrt I)^N$ is finite-dimensional (it is filtered by the finite-dimensional pieces $(\sqrt I)^k/(\sqrt I)^{k+1}$).
:::

<1>2. (2) Counterexample over non-algebraically-closed $F$.
<2>1. Take $I = (x^2 + y^2 + 1) \subseteq \RR[x,y]$ (with $F = \RR$).
::: {.proof}
$x^2 + y^2 + 1$ has no real zero.
:::
<2>2. $V(I) = \emptyset$.
::: {.proof}
$x^2 + y^2 + 1 \ge 1 > 0$ for all real $x, y$.
:::
<2>3. $\RR[x,y]/I$ is infinite-dimensional.
::: {.proof}
$x^2 + y^2 + 1$ is irreducible over $\RR$, so $I$ is prime and $\RR[x,y]/I$ is an integral domain of Krull dimension $1$, hence infinite-dimensional as an $\RR$-vector space.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves (1); <1>2 gives the counterexample for (2).
:::
:::
