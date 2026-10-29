---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-13
kind: problem
title: Uniform continuity on compact sets
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Compactness
  - Continuity
relations:
- kind: uses
  target: T-O4UD3
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $K\subseteq\RR^n$ be compact and let $f\colon K\to\RR^m$ be continuous.
Prove that $f$ is uniformly continuous on $K$.
:::

::: {.solution}
Equip $\RR^n$ and $\RR^m$ with their Euclidean norms.

::: pf

::: {.pf-step #s1}

If $f$ is not uniformly continuous, there exist $\varepsilon>0$ and sequences $(x_j)$ and $(y_j)$ in $K$ satisfying
$$
\norm{x_j-y_j}<1/j,\qquad \norm{f(x_j)-f(y_j)}\geq\varepsilon
\quad(j\geq1).
$$

::: pf-proof

The negation of uniform continuity supplies $\varepsilon>0$ such that, for every $\delta>0$, some $x,y\in K$ satisfy $\norm{x-y}<\delta$ and $\norm{f(x)-f(y)}\geq\varepsilon$. Apply this statement with $\delta=1/j$ for each positive integer $j$.

:::

:::

::: {.pf-step #s2}

There are indices $j_1<j_2<\cdots$ and $x\in K$ such that $x_{j_k}\to x$ and $y_{j_k}\to x$.

::: pf-proof

Compactness of $K\subseteq\RR^n$ implies sequential compactness, so $(x_j)$ has a subsequence converging to some $x\in K$. By step [](#s1){.pf-ref} and the triangle inequality,
$$
\norm{y_{j_k}-x}\leq\norm{y_{j_k}-x_{j_k}}+\norm{x_{j_k}-x}
<1/j_k+\norm{x_{j_k}-x}\convergesto{k\to\infty}0.
$$

:::

:::

::: {.pf-step #s3}

The assumption in step [](#s1){.pf-ref} is impossible.

::: pf-proof

Continuity of $f$ at $x$ and step [](#s2){.pf-ref} give $f(x_{j_k})\to f(x)$ and $f(y_{j_k})\to f(x)$. Consequently $\norm{f(x_{j_k})-f(y_{j_k})}\to0$, contradicting the lower bound $\varepsilon>0$ in step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

By step [](#s3){.pf-ref}, $f$ is uniformly continuous on $K$; this is the [[T-O4UD3|Heine--Cantor theorem]] for $K\subseteq\RR^n$.

:::

:::

:::
