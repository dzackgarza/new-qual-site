---
schema: qual/card@1
id: E-Q5WSL
kind: exercise
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
<1>1. A topological group is a group $G$ with a topology such that the multiplication $G \times G \to G$ and inversion $G \to G$ are continuous.
::: {.proof}
definition.
:::

<1>2. (a) $(\ZZ, +)$ is a topological group.
::: {.proof}
$\ZZ$ has the discrete topology, so addition and negation are automatically continuous.
:::

<1>3. (b) $(\RR, +)$ is a topological group.
::: {.proof}
addition $(x,y) \mapsto x+y$ and negation $x \mapsto -x$ are continuous functions on $\RR$.
:::

<1>4. (c) $(\RR_+, \cdot)$ is a topological group.
::: {.proof}
multiplication $(x,y) \mapsto xy$ and inversion $x \mapsto 1/x$ are continuous on $\RR_+ = (0, \infty)$.
:::

<1>5. (d) $(S^1, \cdot)$ is a topological group.
::: {.proof}
$S^1 = \{z : |z| = 1\}$ is a subgroup of $\CC^\times$; multiplication $(z,w) \mapsto zw$ and inversion $z \mapsto 1/z = \bar z$ are continuous (restrictions of continuous maps on $\CC$).
:::

<1>6. (e) $\mathrm{GL}(n)$ is a topological group.
<2>1. Matrix multiplication $(A, B) \mapsto AB$ is continuous.
::: {.proof}
each entry of $AB$ is a polynomial in the entries of $A$ and $B$, hence continuous.
:::
<2>2. Inversion $A \mapsto A^{-1}$ is continuous.
::: {.proof}
by Cramer's rule, the entries of $A^{-1}$ are rational functions of the entries of $A$ with denominator $\det A \neq 0$, hence continuous on $\mathrm{GL}(n)$.
:::
<2>3. Hence $\mathrm{GL}(n)$ is a topological group.
::: {.proof}
<2>1 and <2>2.
:::

<1>7. Q.E.D.
::: {.proof}
<1>2–<1>6.
:::
:::
