---
schema: qual/card@1
id: P-AZOFF-A04
kind: problem
title: Uniform convergence of $f\circ g_n$ for uniformly continuous $f$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the uniform limit g of g_n and applied the epsilon-delta definition
    of uniform continuity to the uniform bound on |g_n-g|. This proves
    f composed with g_n converges uniformly to f composed with g. The source
    compilation contains no worked solution for this problem.
---

::: {.problem}
Suppose $(g_n)$ is a uniformly convergent sequence of functions from $\RR$ to $\RR$, while $f\colon \RR \to \RR$ is uniformly continuous.
Prove that the sequence $(f \circ g_n)$ of composite functions is also uniformly convergent on $\RR$.
:::

::: {.solution}
Let
$$
g_n\longrightarrow g
$$
uniformly on $\RR$.

::: pf

::: {.pf-step #s1}

For every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\abs{u-v}<\delta
\quad\Longrightarrow\quad
\abs{f(u)-f(v)}<\varepsilon
$$
for all $u,v\in\RR$.

::: pf-proof

This is exactly the uniform continuity of $f$.

:::

:::

::: {.pf-step #s2}

For the $\delta$ from step [](#s1){.pf-ref}, there exists $N$ such that
$$
n\geq N
\quad\Longrightarrow\quad
\abs{g_n(x)-g(x)}<\delta
$$
for every $x\in\RR$.

::: pf-proof

Since $g_n\to g$ uniformly, the definition of uniform convergence applied to
the positive number $\delta$ gives such an $N$.

:::

:::

::: {.pf-step #s3}

For every $n\geq N$ and every $x\in\RR$,
$$
\abs{f(g_n(x))-f(g(x))}<\varepsilon.
$$

::: pf-proof

Fix $n\geq N$ and $x\in\RR$. By step [](#s2){.pf-ref},
$$
\abs{g_n(x)-g(x)}<\delta.
$$
Applying step [](#s1){.pf-ref} with
$$
u=g_n(x),
\qquad
v=g(x)
$$
gives
$$
\abs{f(g_n(x))-f(g(x))}<\varepsilon.
$$
This is the claimed estimate.

:::

:::

::: {.pf-step #s4}

The sequence $(f\circ g_n)$ converges uniformly to $f\circ g$.

::: pf-proof

Step [](#s3){.pf-ref} gives, for every $\varepsilon>0$, an $N$ such that
$$
n\geq N
\quad\Longrightarrow\quad
\abs{(f\circ g_n)(x)-(f\circ g)(x)}
<
\varepsilon
$$
for every $x\in\RR$. This is uniform convergence.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the required uniform convergence.

:::

:::

:::
