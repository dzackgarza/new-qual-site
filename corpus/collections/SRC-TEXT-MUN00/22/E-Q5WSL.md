---
schema: qual/card@1
id: E-Q5WSL
kind: problem
title: Examples of topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Show that the following are topological groups:

(a) $(\mathbb{Z}, +)$

(b) $(\mathbb{R}, +)$

(c) $(\mathbb{R}_+, \cdot)$

(d) $(S^1, \cdot)$, where we take $S^1$ to be the space of all complex numbers $z$ for which $\abs{z} = 1$.

(e) The general linear group $\mathrm{GL}(n)$, under the operation of matrix multiplication.
($\mathrm{GL}(n)$ is the set of all nonsingular $n$ by $n$ matrices, topologized by considering it as a subset of euclidean space of dimension $n^2$ in the obvious way.)
:::

::: {.solution}
Each of the five spaces is a subspace of some $\RR^k$, hence $T_1$, and each is a group under the stated operation; it remains to show that multiplication and inversion are continuous.

<1>1. (a) $(\ZZ,+)$ is a topological group.

::: {.proof}
The subspace topology on $\ZZ\subseteq\RR$ is discrete, so $\ZZ\times\ZZ$ is discrete and every map out of $\ZZ$ or $\ZZ\times\ZZ$ is continuous.
:::

<1>2. (b), (c) $(\RR,+)$ and $(\RR_+,\cdot)$ are topological groups.

::: {.proof}
Addition, negation, multiplication, and $x\mapsto1/x$ on $(0,\infty)$ are continuous by [[E-YTG4V]].
:::

<1>3. (d) $(S^1,\cdot)$ is a topological group.

::: {.proof}
Complex multiplication $(z,w)\mapsto zw$ and conjugation $z\mapsto\bar z$ are continuous on $\CC=\RR^2$, being polynomial in the real coordinates, and on $S^1$ the inverse is $z^{-1}=\bar z$; restrictions to $S^1$ are continuous.
:::

<1>4. (e) $\mathrm{GL}(n)$ is a topological group.

::: {.proof}
Each entry of $AB$ is a polynomial in the entries of $A$ and $B$, so multiplication is continuous.
By Cramer's rule each entry of $A^{-1}$ is a polynomial in the entries of $A$ divided by $\det A\ne0$, so inversion is continuous on $\mathrm{GL}(n)$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 through <1>4 treat (a) through (e).
:::
:::
