---
schema: qual/card@1
id: P-BKF96-2
kind: problem
title: An upper-semicontinuous function on a compact interval is bounded above
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Used upper semicontinuity with epsilon=1 to obtain a local upper bound
    near each point, then extracted a finite subcover of the compact interval.
---

::: {.problem}
A real-valued function $f$ on a closed bounded interval $[a,b]$ is **upper semicontinuous** if for every $\varepsilon>0$ and $p\in[a,b]$ there exists $\delta>0$ such that
\[
x\in[a,b],\quad |x-p|<\delta
\quad\Longrightarrow\quad
f(x)<f(p)+\varepsilon.
\]
Prove that an upper-semicontinuous function is bounded above on $[a,b]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $p\in[a,b]$, there is an open interval $I_p$ containing
$p$ such that
$$
x\in I_p\cap[a,b]
\quad\Longrightarrow\quad
f(x)<f(p)+1.
$$

::: pf-proof

Apply upper semicontinuity at $p$ with
$$
\varepsilon=1.
$$
It gives $\delta_p>0$ such that
$$
\abs{x-p}<\delta_p
\quad\Longrightarrow\quad
f(x)<f(p)+1
$$
for $x\in[a,b]$. Take
$$
I_p=(p-\delta_p,p+\delta_p).
$$

:::

:::

::: {.pf-step #s2}

There are points
$$
p_1,\ldots,p_m\in[a,b]
$$
such that
$$
[a,b]\subseteq I_{p_1}\cup\cdots\cup I_{p_m}.
$$

::: pf-proof

The intervals $I_p$, for $p\in[a,b]$, form an open cover of the compact
interval $[a,b]$. Compactness gives a finite subcover.

:::

:::

::: {.pf-step #s3}

Define
$$
M\coloneqq
\max_{1\leq j\leq m}\bigl(f(p_j)+1\bigr).
$$
Then
$$
f(x)<M
$$
for every $x\in[a,b]$.

::: pf-proof

Fix $x\in[a,b]$. By step [](#s2){.pf-ref}, choose $j$ such that
$$
x\in I_{p_j}.
$$
Step [](#s1){.pf-ref} gives
$$
f(x)<f(p_j)+1\leq M.
$$

:::

:::

::: {.pf-step #s4}

The function $f$ is bounded above on $[a,b]$.

::: pf-proof

Step [](#s3){.pf-ref} gives the global upper bound $M$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
