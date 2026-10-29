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
Prove that $\{1/n:n\in\ZZ\setminus\{0\}\}\cup\{0\}$ is compact using the open-cover definition: every open cover has a finite subcover.
:::

::: {.solution}
Write $K=\{1/n:n\in\ZZ\setminus\{0\}\}\cup\{0\}$ and let $(U_\alpha)_{\alpha\in A}$ be an arbitrary open cover of $K$ in $\RR$.

::: pf

::: {.pf-step #s1}

Some member of the cover contains all but finitely many points of $K$.

::: pf-proof

Since $0\in K$, choose $\alpha_0\in A$ with $0\in U_{\alpha_0}$. Openness gives $\varepsilon>0$ such that $(-\varepsilon,\varepsilon)\subseteq U_{\alpha_0}$. Choose an integer $N\geq1$ with $1/N<\varepsilon$. For every integer $n\ne0$ with $\abs{n}\geq N$, one has $\abs{1/n}\leq1/N<\varepsilon$. Hence only the finitely many points $1/n$ with $0<\abs{n}<N$ may lie outside $U_{\alpha_0}$.

:::

:::

::: {.pf-step #s2}

The cover has a finite subcover.

::: pf-proof

Let $F=\{1/n:n\in\ZZ,\ 0<\abs{n}<N\}$. For each $p\in F$, choose $\alpha_p\in A$ with $p\in U_{\alpha_p}$. Since $F$ is finite, the family consisting of $U_{\alpha_0}$ and the $U_{\alpha_p}$ for $p\in F$ is finite. By step [](#s1){.pf-ref} it covers all of $K$.

:::

:::

::: pf-qed

The open cover was arbitrary, and step [](#s2){.pf-ref} supplies a finite subcover. Thus $K$ is compact by the open-cover definition.

:::

:::

:::
