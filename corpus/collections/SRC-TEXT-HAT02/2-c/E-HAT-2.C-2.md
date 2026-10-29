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

::: {.exercise}
Use the Lefschetz fixed point theorem to show that a map $f: S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $x \mapsto -x$.
:::

::: {.solution}
Write $a(x) = -x$ for the antipodal map of $S^n$ and $d = \deg f$.

::: pf

::: {.pf-step #s1}
$\deg(a) = (-1)^{n+1}$.

::: pf-proof

::: pf-step
The antipodal map $a: S^n \to S^n$ is given by $a(x_0, x_1, \dots, x_n) = (-x_0, -x_1, \dots, -x_n)$ on $S^n \subset \RR^{n+1}$.
:::

::: pf-step
The map $a$ is the composition of $n + 1$ coordinate reflections $r_i(x_0, \dots, x_i, \dots, x_n) = (x_0, \dots, -x_i, \dots, x_n)$.
:::

::: pf-step
Each reflection has degree $-1$, so by functoriality of topological degree:
$$\deg(a) = \deg(r_0 \circ r_1 \circ \cdots \circ r_n) = (-1)^{n+1}.$$
:::

:::

:::

::: {.pf-step #lefschetz-number}
For $n \ge 1$, the Lefschetz number of $f$ is $\Lambda(f) = 1 + (-1)^n d$.

::: pf-proof

::: pf-step
The rational homology groups of the $n$-sphere $S^n$ are:
$$H_k(S^n; \QQ) \cong \begin{cases} \QQ & k = 0, n, \\ 0 & 0 < k < n \text{ and } k > n. \end{cases}$$
:::

::: pf-step
For $k = 0$, $S^n$ is non-empty and connected, so $f_*: H_0(S^n; \QQ) \to H_0(S^n; \QQ)$ is the identity, with $\operatorname{tr}(f_*|_{H_0}) = 1$.
:::

::: pf-step
For $k = n$, by definition of topological degree, $f_*: H_n(S^n; \QQ) \to H_n(S^n; \QQ)$ is multiplication by $\deg(f) = d$, so $\operatorname{tr}(f_*|_{H_n}) = d$.
:::

::: pf-step
If $n = 0$, $S^0 = \{-1, 1\}$ has $H_0(S^0; \QQ) \cong \QQ^2$, where a degree $d$ map satisfies $\Lambda(f) = 1 + d$.
:::

::: pf-step
For $n \ge 1$, the Lefschetz number $\Lambda(f)$ is
$$\Lambda(f) = \sum_{k=0}^n (-1)^k \operatorname{tr}(f_*|_{H_k(S^n; \QQ)}) = (-1)^0 (1) + (-1)^n (d) = 1 + (-1)^n d.$$
:::

:::

:::

::: pf-step
If $\deg(f) \neq \deg(a)$, then $f$ has a fixed point.

::: pf-proof

::: pf-step
The sphere $S^n$ is a compact, triangulable CW complex (a compact polyhedron).
:::

::: pf-step
By the Lefschetz Fixed Point Theorem, if $\Lambda(f) \neq 0$, then $f$ must have at least one fixed point (there exists $x \in S^n$ such that $f(x) = x$).
:::

::: pf-step
By step [](#lefschetz-number){.pf-ref}, the Lefschetz number vanishes exactly when
$$\Lambda(f) = 0 \iff 1 + (-1)^n d = 0 \iff (-1)^n d = -1 \iff d = -(-1)^{-n} = (-1)^{n+1}.$$
:::

::: pf-step
By step [](#s1){.pf-ref}, $(-1)^{n+1} = \deg(a)$.
:::

::: pf-step
Therefore, $\Lambda(f) = 0$ if and only if $\deg(f) = \deg(a) = (-1)^{n+1}$.
:::

::: pf-step
If $\deg(f) \neq \deg(a)$, then $\Lambda(f) \neq 0$, so $f$ must have a fixed point.
:::

:::

:::

:::

:::
