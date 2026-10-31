---
schema: qual/card@1
id: P-TAMURAS15-10
kind: problem
title: Extending an equivalent norm from a subspace of a normed space
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Dual Spaces
  - Norms
relations: []
review: draft
---

::: {.problem}
Let $(X,\norm{\cdot})$ be a normed vector space with a subspace $Y$, and let $\norm{\cdot}_1$ be another norm on $Y$ that satisfies
$$
\frac1K\norm{y}_1\le\norm{y}\le K\norm{y}_1,\qquad y\in Y,
$$
where $K>1$ is a fixed constant.
Define $S$ to be the set of linear functionals $\phi:X\to\RR$ satisfying
$$
\abs{\phi(y)}\le\norm{y}_1\quad (y\in Y)
\qquad\text{and}\qquad
\abs{\phi(x)}\le K\norm{x}\quad (x\in X).
$$
Prove the following statements:

(i) $\norm{x}_2\coloneqq\sup\{\abs{\phi(x)}:\phi\in S\}$ defines a norm on $X$.

(ii) For $y\in Y$, $\norm{y}_1=\norm{y}_2$.

(iii) The norms $\norm{\cdot}$ and $\norm{\cdot}_2$ are equivalent on $X$.
:::
