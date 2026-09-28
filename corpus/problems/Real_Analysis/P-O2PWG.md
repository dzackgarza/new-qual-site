---
schema: qual/card@1
id: P-O2PWG
kind: problem
title: Compact sets are closed and bounded, complete totally bounded sets are compact,
  and $\dist(K,F)>0$
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
  - Completeness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Show that every compact set is closed and bounded.

- Show that if a subset of a metric space is complete and totally bounded, then it is compact.

- Show that if $K$ is compact and $F$ is closed with $K, F$ disjoint then $\dist(K, F) > 0$.
:::
::: {.solution}
Work in a metric space $(X, d)$.

<1>1. A compact $K \subseteq X$ is closed and bounded.

::: {.proof}
For $x \notin K$ and $y \in K$, the balls $U_y = B(y, d(x,y)/3)$ and $V_y = B(x, d(x,y)/3)$ are disjoint. Finitely many $U_{y_1}, \ldots, U_{y_n}$ cover $K$, and $\bigcap_i V_{y_i}$ is an open ball about $x$ disjoint from $K$, so $X \setminus K$ is open. For boundedness, fix $x_0$; finitely many of the balls $B(x_0, n)$ cover $K$, so $K \subseteq B(x_0, N)$ for some $N$. See [[E-FFARP]].
:::

<1>2. A complete and totally bounded $E \subseteq X$ is compact.

::: {.proof}
Given a sequence in $E$, cover $E$ by finitely many balls of radius $1$, pass to a subsequence in one of them, then cover by finitely many balls of radius $1/2$ and pass to a further subsequence, and so on. The diagonal subsequence has its $m$th and later terms in one ball of radius $1/m$, so it is Cauchy, and it converges in $E$ because $E$ is complete. So $E$ is sequentially compact, which for metric spaces is equivalent to compactness. See [[E-4CL6A]].
:::

<1>3. If $K$ is compact, $F$ is closed, and $K \cap F = \emptyset$, then $\dist(K, F) > 0$.

::: {.proof}
$x \mapsto \dist(x, F)$ satisfies $|\dist(x, F) - \dist(y, F)| \le d(x, y)$, so it is continuous and attains its minimum on $K$ at some $k_0$, assuming $K$ and $F$ nonempty. If $\dist(k_0, F) = 0$, then $k_0 \in \overline F = F$, contradicting $K \cap F = \emptyset$. See [[E-SA3HI]].
:::
:::
