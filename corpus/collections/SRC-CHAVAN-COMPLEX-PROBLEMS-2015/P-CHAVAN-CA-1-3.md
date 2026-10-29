---
schema: qual/card@1
id: P-CHAVAN-CA-1-3
kind: problem
title: Maximum modulus for a uniformly convergent power series on the closed disk
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let
$$
f(z)=\sum_{n=0}^{\infty}a_nz^n
$$
converge uniformly on the closed unit disk.
Show that
$$
\max_{|z|\le1}|f(z)|=\max_{|z|=1}|f(z)|.
$$
:::

::: {.solution}

For $N\ge0$, let
$$
p_N(z)=\sum_{n=0}^N a_nz^n,
$$
and set
$$
K=\{z\in\CC:|z|\le1\},
\qquad
\partial K=\{z\in\CC:|z|=1\}.
$$

::: pf

::: {.pf-step #s1-1}

The function $f$ is continuous on $K$, so $|f|$ attains maxima on both $K$ and $\partial K$.


::: pf-proof

Each partial sum $p_N$ is continuous on $K$, and $p_N\to f$ uniformly on $K$ by hypothesis. A uniform limit of continuous functions is continuous, hence $f$ is continuous on $K$. Since $K$ and $\partial K$ are compact, the extreme value theorem gives maxima of $|f|$ on both sets.

:::

:::

::: {.pf-step #s1-2}

If
$$
\varepsilon_N=\max_{z\in K}|p_N(z)-f(z)|,
$$
then $\varepsilon_N\to0$, and for every nonempty subset $E\subseteq K$ on which both maxima exist,
$$
\left|\max_{z\in E}|p_N(z)|-\max_{z\in E}|f(z)|\right|\le\varepsilon_N.
$$


::: pf-proof

Uniform convergence is exactly the statement that $\varepsilon_N\to0$. For every $z\in K$, the reverse triangle inequality gives
$$
\bigl||p_N(z)|-|f(z)|\bigr|
\le |p_N(z)-f(z)|
\le\varepsilon_N.
$$
Therefore
$$
|p_N(z)|\le |f(z)|+\varepsilon_N
$$
for every $z\in E$, so
$$
\max_E|p_N|\le\max_E|f|+\varepsilon_N.
$$
Interchanging $p_N$ and $f$ gives
$$
\max_E|f|\le\max_E|p_N|+\varepsilon_N.
$$
Combining the two inequalities proves the claim.

:::

:::

::: {.pf-step #s1-3}

For every $N$,
$$
\max_{z\in K}|p_N(z)|=\max_{z\in\partial K}|p_N(z)|.
$$


::: pf-proof

Each $p_N$ is a polynomial. The polynomial maximum-modulus result established in Problems 1.1 and 1.2 therefore applies to $p_N$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\max_{|z|\le1}|f(z)|=\max_{|z|=1}|f(z)|}.
$$


::: pf-proof

Applying step [](#s1-2){.pf-ref} with $E=K$ and with $E=\partial K$ gives
$$
\max_K|p_N|\longrightarrow\max_K|f|
$$
and
$$
\max_{\partial K}|p_N|\longrightarrow\max_{\partial K}|f|.
$$
The two quantities on the left are equal for every $N$ by step [](#s1-3){.pf-ref}. Their limits are therefore equal, which is the displayed identity.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required maximum-modulus equality.

:::

:::

:::
