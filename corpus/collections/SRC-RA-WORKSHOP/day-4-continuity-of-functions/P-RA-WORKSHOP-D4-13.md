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
  target: T-RA-WORKSHOP-D4-3-3
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove Theorem 3.3.
:::

::: {.solution}
Let $K\subseteq\mathbb R^n$ be compact and let $f:K\to\mathbb R^m$ be continuous, as in [[T-RA-WORKSHOP-D4-3-3|Theorem 3.3]]. Equip both Euclidean spaces with their usual norms.

<1>1. If $f$ is not uniformly continuous, there exist $\varepsilon>0$ and sequences $(x_j)$ and $(y_j)$ in $K$ satisfying
\[
\|x_j-y_j\|<1/j,\qquad \|f(x_j)-f(y_j)\|\geq\varepsilon
\quad(j\geq1).
\]

::: {.proof}
The negation of uniform continuity supplies $\varepsilon>0$ such that, for every $\delta>0$, some $x,y\in K$ satisfy $\|x-y\|<\delta$ and $\|f(x)-f(y)\|\geq\varepsilon$. Apply this statement with $\delta=1/j$ for each positive integer $j$.
:::

<1>2. There are indices $j_1<j_2<\cdots$ and $x\in K$ such that $x_{j_k}\to x$ and $y_{j_k}\to x$.

::: {.proof}
Compactness of $K\subseteq\mathbb R^n$ implies sequential compactness, so $(x_j)$ has a subsequence converging to some $x\in K$. By step <1>1 and the triangle inequality,
\[
\|y_{j_k}-x\|\leq\|y_{j_k}-x_{j_k}\|+\|x_{j_k}-x\|
<1/j_k+\|x_{j_k}-x\|\longrightarrow0.
\]
:::

<1>3. The assumption in step <1>1 is impossible.

::: {.proof}
Continuity of $f$ at $x$ and step <1>2 give $f(x_{j_k})\to f(x)$ and $f(y_{j_k})\to f(x)$. Consequently $\|f(x_{j_k})-f(y_{j_k})\|\to0$, contradicting the lower bound $\varepsilon>0$ in step <1>1.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 excludes the negation of uniform continuity, proving the assertion of Theorem 3.3.
:::
:::
