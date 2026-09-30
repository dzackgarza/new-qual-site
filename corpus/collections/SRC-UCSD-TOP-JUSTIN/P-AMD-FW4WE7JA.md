---
schema: qual/card@1
id: P-AMD-FW4WE7JA
kind: problem
title: Nonsurjective maps into $S^n$ are nullhomotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Show that any non-surjective map $f: X \rightarrow S^n$ is homotopic to the constant map.
:::

::: {.solution}
**Goal:** Let $X$ be an arbitrary topological space, and let $f \colon X \to S^n$ be a continuous map ($n \ge 1$). Prove that if $f$ is not surjective, then $f$ is nullhomotopic (homotopic to a constant map).

::: pf

::: pf-step
Pick a point omitted by $f$.

::: pf-proof

::: pf-step
Since $f$ is not surjective, there exists a point $p \in S^n$ such that $p \notin f(X)$, so $f(X) \subseteq S^n \setminus \{p\}$.
:::

::: pf-step
Without loss of generality, by rotating $S^n$ if necessary, let $p = -N = (0, \dots, 0, -1)$ (the south pole), and let $N = (0, \dots, 0, 1)$ (the north pole).
:::

::: pf-qed
Since $f$ is not surjective, $f(X) \neq S^n$, so some point $p$ is omitted; a rotation of $S^n$ carries $p$ to the south pole without changing the homotopy class of $f$.
:::

:::

:::

::: pf-step
Show that the punctured sphere $S^n \setminus \{p\}$ is contractible.

::: pf-proof

::: pf-step
Stereographic projection from the pole $p$ gives a homeomorphism $\phi \colon S^n \setminus \{p\} \to \mathbb{R}^n$.
:::

::: pf-step
Euclidean space $\mathbb{R}^n$ is convex, hence contractible to the origin $0 \in \mathbb{R}^n$ via the straight-line homotopy $h(y, t) = (1-t)y$.
:::

::: pf-step
Pulling back via $\phi$, define $H_0 \colon (S^n \setminus \{p\}) \times [0, 1] \to S^n \setminus \{p\}$ by $H_0(z, t) = \phi^{-1}((1-t)\phi(z))$.
:::

::: pf-step
$H_0(z, 0) = z = \operatorname{id}_{S^n \setminus \{p\}}(z)$, and $H_0(z, 1) = \phi^{-1}(0) = N$ (constant map to the antipodal pole $N$).
:::

::: pf-step
$H_0$ is continuous because $\phi$, $\phi^{-1}$, and scalar multiplication are continuous.
:::

::: pf-qed
The map $H_0$ is a homotopy from the identity on $S^n \setminus \{p\}$ to the constant map at $N$, so $S^n \setminus \{p\}$ is contractible to the point $N$.
:::

:::

:::

::: {.pf-step #s3}
Construct the nullhomotopy for $f$.

::: pf-proof

::: pf-step
Define $H \colon X \times [0, 1] \to S^n$ by $H(x, t) = H_0(f(x), t)$.
:::

::: pf-step
Equivalently, using normalized straight-line geodesics in $\mathbb{R}^{n+1}$: Since $f(x) \neq -N$ for all $x \in X$, $(1-t)f(x) + t N \neq 0$ for all $t \in [0, 1]$, so $$H(x, t) = \frac{(1-t)f(x) + t N}{\|(1-t)f(x) + t N\|}$$ is well-defined, continuous, and lands in $S^n$.
:::

::: {.pf-step #s3-3}
Check endpoints:

- $H(x, 0) = \frac{f(x)}{\|f(x)\|} = f(x)$,

- $H(x, 1) = \frac{N}{\|N\|} = N = c_N(x)$.

:::

::: pf-step
Thus $H$ is a homotopy between $f$ and the constant map $c_N \colon X \to S^n$.

::: pf-proof
The endpoint computations in step [](#s3-3){.pf-ref} show $H(\cdot, 0) = f$ and $H(\cdot, 1) = c_N$, and $H$ is continuous, so $H$ is a homotopy from $f$ to the constant map.
:::

:::

:::

:::

::: pf-qed
Step [](#s3){.pf-ref} proves that $f$ is homotopic to the constant map $c_N$.
:::

:::
:::
