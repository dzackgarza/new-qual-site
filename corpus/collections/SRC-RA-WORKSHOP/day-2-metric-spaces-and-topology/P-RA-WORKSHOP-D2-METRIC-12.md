---
schema: qual/card@1
id: P-RA-WORKSHOP-D2-METRIC-12
kind: problem
title: Open subsets of $\RR$ are finite or countable unions of disjoint open intervals
classification:
  areas:
  - real-analysis
  topics:
  - Euclidean Spaces
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Prove that every open set $G\subset\RR$ can be written as a finite or countable union of disjoint open intervals $(a_j,b_j)$ with at most one $a_j=-\infty$ and at most one $b_j=\infty$.
:::

::: {.solution}
For each $x\in G$, let $C_x$ denote the connected component of $G$ containing $x$.

::: pf

::: {.pf-step #s1}

Each $C_x$ is an open interval, possibly unbounded.

::: pf-proof

Every connected subset of $\RR$ is an interval. Given $y\in C_x$, openness of $G$ supplies $\varepsilon>0$ such that $I=(y-\varepsilon,y+\varepsilon)\subseteq G$. The union $C_x\cup I$ is connected since the two sets meet at $y$. Maximality of $C_x$ implies $I\subseteq C_x$. Therefore $C_x$ is open, hence is an interval $(a_x,b_x)$ with endpoints in the extended real line.

:::

:::

::: {.pf-step #s2}

The family of distinct components is at most countable.

::: pf-proof

Let $(q_n)_{n\geq1}$ be an enumeration of $\QQ$. For each component $C$, let $n(C)$ be the least $n$ for which $q_n\in C$; this exists by step [](#s1){.pf-ref} and density of $\QQ$. Distinct components are disjoint, so $n(C)=n(D)$ implies $C=D$. Thus $C\mapsto n(C)$ is an injection into $\NN$.

:::

:::

::: {.pf-step #s3}

At most one component is unbounded below, and at most one is unbounded above.

::: pf-proof

Two nonempty intervals unbounded below must intersect: choosing one point in each, any real number smaller than both points lies in both intervals. Since distinct components are disjoint, at most one is unbounded below. The analogous argument with a real number larger than both points proves the assertion for intervals unbounded above.

:::

:::

::: pf-qed

The components partition $G$. By step [](#s1){.pf-ref} they are open intervals, by step [](#s2){.pf-ref} there are finitely or countably many, and step [](#s3){.pf-ref} gives the endpoint restrictions. If $G=\varnothing$, the empty union applies.

:::

:::

:::
