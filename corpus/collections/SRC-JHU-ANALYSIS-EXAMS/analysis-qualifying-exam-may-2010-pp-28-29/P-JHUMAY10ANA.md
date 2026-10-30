---
schema: qual/card@1
id: P-JHUMAY10ANA
kind: problem
title: Removable singularity under the bound $\abs{f(z)}\le\abs{z}^{-1/2}$
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f$ be a holomorphic function on the punctured disk $U = \{z \in \CC : 0 < \abs{z} < 1\}$.
Suppose that $\abs{f(z)} \le \abs{z}^{-1/2}$ for all $z \in U$.
Prove that $f$ has a removable singularity at $0$.
:::

::: {.hint}
Riemann's removable singularity theorem does not apply to $z^{1/2}f(z)$, because $z^{1/2}$ has no single-valued holomorphic branch on a punctured neighbourhood of $0$. Apply it to $zf(z)$.
:::

::: {.solution}

::: pf

::: pf-step

The function $g(z)=zf(z)$ extends holomorphically across $0$ with value $0$.

::: pf-proof

For $0<\abs{z}<1$,
$$
\abs{g(z)}=\abs{z}\,\abs{f(z)}\le \abs{z}^{1/2}.
$$
Thus $g$ is bounded near $0$, so the [[T-ZZJDP|Riemann removable singularity theorem]] gives a holomorphic extension $G$ to the unit disk. The displayed estimate also gives
$$
G(0)=\lim_{z\to0}zf(z)=0.
$$

:::

:::

::: {.pf-step #s2}

Dividing the zero of $G$ by $z$ gives a holomorphic extension of $f$.

::: pf-proof

By [[T-GROTS|holomorphic implies analytic]], the Taylor series of $G$ at $0$ has the form
$$
G(z)=\sum_{n\ge1}a_nz^n
$$
because $G(0)=0$. Hence
$$
F(z)=\sum_{n\ge1}a_nz^{n-1}
$$
is holomorphic near $0$ and satisfies $G(z)=zF(z)$. For $z\ne0$ in the punctured disk,
$$
F(z)=\frac{G(z)}z=f(z).
$$
Thus $F$ extends $f$ holomorphically across $0$.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} constructs the required holomorphic extension, so the singularity at $0$ is removable.

:::

:::

:::
