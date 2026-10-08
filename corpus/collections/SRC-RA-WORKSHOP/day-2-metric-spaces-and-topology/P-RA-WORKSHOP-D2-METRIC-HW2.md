---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-HW2
kind: problem
title: Compactness of the reciprocal-integer set
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(June 2010 #2b) Prove that $\{1/n:n\in\mathbb Z\setminus\{0\}\}\cup\{0\}$ is compact using the above definition.
:::

::: {.solution}
Write $K=\{1/n:n\in\mathbb Z\setminus\{0\}\}\cup\{0\}$ and let $(U_\alpha)_{\alpha\in A}$ be an arbitrary open cover of $K$ in $\mathbb R$.

<1>1. Some member of the cover contains all but finitely many points of $K$.

::: {.proof}
Since $0\in K$, choose $\alpha_0\in A$ with $0\in U_{\alpha_0}$. Openness gives $\varepsilon>0$ such that $(-\varepsilon,\varepsilon)\subseteq U_{\alpha_0}$. Choose an integer $N\geq1$ with $1/N<\varepsilon$. For every integer $n\ne0$ with $|n|\geq N$, one has $|1/n|\leq1/N<\varepsilon$. Hence only the finitely many points $1/n$ with $0<|n|<N$ may lie outside $U_{\alpha_0}$.
:::

<1>2. The cover has a finite subcover.

::: {.proof}
Let $F=\{1/n:n\in\mathbb Z,\ 0<|n|<N\}$. For each $p\in F$, choose $\alpha_p\in A$ with $p\in U_{\alpha_p}$. Since $F$ is finite, the family consisting of $U_{\alpha_0}$ and the $U_{\alpha_p}$ for $p\in F$ is finite. By step <1>1 it covers all of $K$.
:::

<1>3. Q.E.D.

::: {.proof}
The open cover was arbitrary, and step <1>2 supplies a finite subcover. Thus $K$ is compact by the open-cover definition.
:::
:::
