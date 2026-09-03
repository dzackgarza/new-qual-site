---
schema: qual/card@1
id: E-HAT-2.C-2
kind: problem
title: 'Lefschetz fixed point theorem: map $S^n \to S^n$ has fixed point unless degree equals antipodal degree'
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
Use the Lefschetz fixed point theorem to show that a map $f: S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $x \mapsto -x$.
:::

::: solution
**Goal:** Prove via the Lefschetz Fixed Point Theorem that any continuous map $f: S^n \to S^n$ has a fixed point whenever $\deg(f) \neq \deg(a)$, where $a(x) = -x$ is the antipodal map.

<1>1. Degree and Lefschetz number of the antipodal map:
    *Proof:*
    <2>1. The antipodal map $a: S^n \to S^n$ is given by $a(x_0, x_1, \dots, x_n) = (-x_0, -x_1, \dots, -x_n)$ on $S^n \subset \mathbb{R}^{n+1}$.
    <2>2. The map $a$ is the composition of $n + 1$ coordinate reflections $r_i(x_0, \dots, x_i, \dots, x_n) = (x_0, \dots, -x_i, \dots, x_n)$.
    <2>3. Each reflection has degree $-1$, so by functoriality of topological degree:
    $$\deg(a) = \deg(r_0 \circ r_1 \circ \cdots \circ r_n) = (-1)^{n+1}.$$

<1>2. Lefschetz number of an arbitrary continuous map $f: S^n \to S^n$:
    *Proof:*
    <2>1. The rational homology groups of the $n$-sphere $S^n$ are:
    $$H_k(S^n; \mathbb{Q}) \cong \begin{cases} \mathbb{Q} & k = 0, n, \\ 0 & 0 < k < n \text{ and } k > n. \end{cases}$$
    <2>2. For $k = 0$, $S^n$ is non-empty and connected, so $f_*: H_0(S^n; \mathbb{Q}) \to H_0(S^n; \mathbb{Q})$ is the identity, with $\operatorname{tr}(f_*|_{H_0}) = 1$.
    <2>3. For $k = n$, by definition of topological degree, $f_*: H_n(S^n; \mathbb{Q}) \to H_n(S^n; \mathbb{Q})$ is multiplication by $\deg(f) = d$, so $\operatorname{tr}(f_*|_{H_n}) = d$.
    <2>4. If $n = 0$, $S^0 = \{-1, 1\}$ has $H_0(S^0; \mathbb{Q}) \cong \mathbb{Q}^2$, where a degree $d$ map satisfies $\Lambda(f) = 1 + d$.
    <2>5. For $n \ge 1$, the Lefschetz number $\Lambda(f)$ is
    $$\Lambda(f) = \sum_{k=0}^n (-1)^k \operatorname{tr}(f_*|_{H_k(S^n; \mathbb{Q})}) = (-1)^0 (1) + (-1)^n (d) = 1 + (-1)^n d.$$

<1>3. Fixed point existence via the Lefschetz Fixed Point Theorem:
    *Proof:*
    <2>1. The sphere $S^n$ is a compact, triangulable CW complex (a compact polyhedron).
    <2>2. By the Lefschetz Fixed Point Theorem, if $\Lambda(f) \neq 0$, then $f$ must have at least one fixed point (there exists $x \in S^n$ such that $f(x) = x$).
    <2>3. Solve for when the Lefschetz number vanishes:
    $$\Lambda(f) = 0 \iff 1 + (-1)^n d = 0 \iff (-1)^n d = -1 \iff d = -(-1)^{-n} = (-1)^{n+1}.$$
    <2>4. By <1>1, $(-1)^{n+1} = \deg(a)$.
    <2>5. Therefore, $\Lambda(f) = 0$ if and only if $\deg(f) = \deg(a) = (-1)^{n+1}$.
    <2>6. If $\deg(f) \neq \deg(a)$, then $\Lambda(f) \neq 0$, so $f$ must have a fixed point.

<1>4. Conclusion:
    *Proof:*
    Every continuous map $f: S^n \to S^n$ has a fixed point unless $\deg(f) = (-1)^{n+1} = \deg(\text{antipodal})$.
:::
