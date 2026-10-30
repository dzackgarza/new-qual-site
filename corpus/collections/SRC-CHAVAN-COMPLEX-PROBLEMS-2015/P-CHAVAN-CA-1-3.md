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
\max_{\abs{z}\le1}\abs{f(z)}=\max_{\abs{z}=1}\abs{f(z)}.
$$
:::

::: {.solution}

For $N\ge0$, let
$$
p_N(z)=\sum_{n=0}^N a_nz^n,
$$
and set
$$
K=\{z\in\CC:\abs{z}\le1\},
\qquad
\partial K=\{z\in\CC:\abs{z}=1\}.
$$

::: pf

::: {.pf-step #s1-1}

The function $f$ is continuous on $K$, so $\abs{f}$ attains maxima on both $K$ and $\partial K$.


::: pf-proof

Each partial sum $p_N$ is continuous on $K$, and $p_N\to f$ uniformly on $K$ by hypothesis. A uniform limit of continuous functions is continuous, hence $f$ is continuous on $K$. Since $K$ and $\partial K$ are compact, the extreme value theorem gives maxima of $\abs{f}$ on both sets.

:::

:::

::: {.pf-step #s1-2}

If
$$
\varepsilon_N=\max_{z\in K}\abs{p_N(z)-f(z)},
$$
then $\varepsilon_N\to0$, and for every nonempty subset $E\subseteq K$ on which both maxima exist,
$$
\abs{\max_{z\in E}\abs{p_N(z)}-\max_{z\in E}\abs{f(z)}}\le\varepsilon_N.
$$


::: pf-proof

Uniform convergence is exactly the statement that $\varepsilon_N\to0$. For every $z\in K$, the reverse triangle inequality gives
$$
\abs{\abs{p_N(z)}-\abs{f(z)}}
\le \abs{p_N(z)-f(z)}
\le\varepsilon_N.
$$
Therefore
$$
\abs{p_N(z)}\le \abs{f(z)}+\varepsilon_N
$$
for every $z\in E$, so
$$
\max_E\abs{p_N}\le\max_E\abs{f}+\varepsilon_N.
$$
Interchanging $p_N$ and $f$ gives
$$
\max_E\abs{f}\le\max_E\abs{p_N}+\varepsilon_N.
$$
Combining the two inequalities proves the claim.

:::

:::

::: {.pf-step #s1-3}

For every $N$,
$$
\max_{z\in K}\abs{p_N(z)}=\max_{z\in\partial K}\abs{p_N(z)}.
$$


::: pf-proof

Each $p_N$ is a polynomial. The polynomial maximum-modulus result established in Problems 1.1 and 1.2 therefore applies to $p_N$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\max_{\abs{z}\le1}\abs{f(z)}=\max_{\abs{z}=1}\abs{f(z)}}.
$$


::: pf-proof

Applying step [](#s1-2){.pf-ref} with $E=K$ and with $E=\partial K$ gives
$$
\max_K\abs{p_N}\longrightarrow\max_K\abs{f}
$$
and
$$
\max_{\partial K}\abs{p_N}\longrightarrow\max_{\partial K}\abs{f}.
$$
The two quantities on the left are equal for every $N$ by step [](#s1-3){.pf-ref}. Their limits are therefore equal, which is the displayed identity.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required maximum-modulus equality.

:::

:::

:::
