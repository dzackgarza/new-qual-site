---
schema: qual/card@1
id: P-ALGS17F
kind: problem
title: "The algebraic closure of a prime field is infinite-dimensional"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $F$ be a prime field, so that $F$ is either isomorphic to $\mathbb{Q}$ or $\mathbb{F}_p$ for a prime $p$.
Show that the algebraic closure of $F$ is infinite-dimensional over $F$.
:::

::: {.solution}
<1>1. Let $\overline{F}$ be the algebraic closure of $F$.
Proof: setup.

<1>2. For each positive integer $n$, there is an irreducible polynomial of degree $n$ over $F$.
Proof: for $F = \mathbb{Q}$, $x^n - 2$ is irreducible (Eisenstein at $2$); for $F = \mathbb{F}_p$, there is an irreducible polynomial of every degree $n$ (the field $\mathbb{F}_{p^n}$ exists, and its generator over $\mathbb{F}_p$ has degree $n$).

<1>3. Hence for each $n$, there is an element $\alpha_n \in \overline{F}$ with $[F(\alpha_n) : F] = n$.
Proof: <1>2 (a root of an irreducible degree-$n$ polynomial).

<1>4. If $\overline{F}$ were finite-dimensional over $F$, say $[\overline{F} : F] = N < \infty$, then every element of $\overline{F}$ would have degree $\le N$ over $F$.
Proof: the degree of any element is at most the degree of the field extension.

<1>5. But <1>3 gives elements of arbitrarily large degree, contradicting <1>4.
Proof: <1>3 and <1>4.

<1>6. Hence $\overline{F}$ is infinite-dimensional over $F$.
Proof: <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
