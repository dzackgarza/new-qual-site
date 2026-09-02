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

:::: {.solution}
<1>1. Let $\{U_\alpha\}$ be any open cover of $K = \{1/n : n \in \mathbb{Z}\setminus\{0\}\} \cup \{0\}$ in $\mathbb{R}$.
<1>2. One open set covers a neighborhood of $0$ and hence all but finitely many points of $K$.
Proof: $0 \in K$, so some $U_{\alpha_0}$ contains $0$; since $U_{\alpha_0}$ is open, $(-\epsilon, \epsilon) \subseteq U_{\alpha_0}$ for some $\epsilon > 0$.
Choose $N$ with $1/N < \epsilon$; then every point $1/n$ with $|n| \ge N$ lies in $(-\epsilon, \epsilon) \subseteq U_{\alpha_0}$.
<1>3. The finitely many remaining points are covered by finitely many sets of the cover.
Proof: the remaining points $\{\pm 1, \pm 1/2, \ldots, \pm 1/(N-1)\}$ form a finite set; for each such point $p$ choose some $U_{\alpha_p}$ containing $p$.
Together with $U_{\alpha_0}$ this gives a finite subcover.
<1>4. Q.E.D. Proof: every open cover of $K$ has a finite subcover, so $K$ is compact by the definition.
:::
