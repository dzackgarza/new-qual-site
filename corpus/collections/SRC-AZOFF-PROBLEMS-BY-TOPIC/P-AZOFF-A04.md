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
Suppose $\left( g _ { n } \right)$ is a uniformly convergent sequence of functions from R to R, while $f : \mathbb { R } \to \mathbb { R }$ is uniformly continuous.
Prove that the sequence $\left( f \circ g _ { n } \right)$ of composite functions is also uniformly convergent on R.
:::

::: {.solution}
Let
$$
g_n\longrightarrow g
$$
uniformly on $\RR$.

<1>1. For every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\abs{u-v}<\delta
\quad\Longrightarrow\quad
\abs{f(u)-f(v)}<\varepsilon
$$
for all $u,v\in\RR$.

::: {.proof}
This is exactly the uniform continuity of $f$.
:::

<1>2. For the $\delta$ from step <1>1, there exists $N$ such that
$$
n\geq N
\quad\Longrightarrow\quad
\abs{g_n(x)-g(x)}<\delta
$$
for every $x\in\RR$.

::: {.proof}
Since $g_n\to g$ uniformly, the definition of uniform convergence applied to
the positive number $\delta$ gives such an $N$.
:::

<1>3. For every $n\geq N$ and every $x\in\RR$,
$$
\abs{f(g_n(x))-f(g(x))}<\varepsilon.
$$

::: {.proof}
Fix $n\geq N$ and $x\in\RR$. By step <1>2,
$$
\abs{g_n(x)-g(x)}<\delta.
$$
Applying step <1>1 with
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

<1>4. The sequence $(f\circ g_n)$ converges uniformly to $f\circ g$.

::: {.proof}
Step <1>3 gives, for every $\varepsilon>0$, an $N$ such that
$$
n\geq N
\quad\Longrightarrow\quad
\abs{(f\circ g_n)(x)-(f\circ g)(x)}
<
\varepsilon
$$
for every $x\in\RR$. This is uniform convergence.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the required uniform convergence.
:::
:::
