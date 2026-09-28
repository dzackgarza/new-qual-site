---
schema: qual/card@1
id: P-JHUMAY10ANA
kind: problem
title: Removable singularity under the bound $|f(z)|\le|z|^{-1/2}$
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
Let $f$ be a holomorphic function on the punctured disk $U = \{z \in \mathbb{C} : 0 < |z| < 1\}$.
Suppose that $|f(z)| \le |z|^{-1/2}$ for all $z \in U$.
Prove that $f$ has a removable singularity at $0$.
:::

::: {.solution}
<1>1. The function $g(z)=zf(z)$ extends holomorphically across $0$ with value $0$.
::: {.proof}
For $0<|z|<1$,
$$
|g(z)|=|z|\,|f(z)|\le |z|^{1/2}.
$$
Thus $g$ is bounded near $0$, so the [[D-BQLJV|Riemann removable singularity theorem]] gives a holomorphic extension $G$ to the unit disk. The displayed estimate also gives
$$
G(0)=\lim_{z\to0}zf(z)=0.
$$
:::

<1>2. Dividing the zero of $G$ by $z$ gives a holomorphic extension of $f$.
::: {.proof}
By [[T-SRY2V|holomorphic implies analytic]], the Taylor series of $G$ at $0$ has the form
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

<1>3. Q.E.D.
::: {.proof}
Step <1>2 constructs the required holomorphic extension, so the singularity at $0$ is removable.
:::
:::
