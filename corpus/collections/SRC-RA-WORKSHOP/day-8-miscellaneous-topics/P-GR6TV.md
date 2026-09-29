---
schema: qual/card@1
id: P-GR6TV
kind: problem
title: A closed bounded noncompact subset of a metric space
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Metric Spaces
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Find an example of a metric space $X$ and a subset $E \subseteq X$ such that $E$ is closed and bounded but not compact.
:::
::: {.solution}

::: pf

::: pf-step

Example: $X = (0, 1)$ with the usual metric $d(x,y) = |x - y|$, and $E = (0, 1) = X$ itself.

::: pf-proof

explicit space and subset.

:::

:::

::: {.pf-step #s2}

$E$ is closed in $X$.

::: pf-proof

$E = X$ is the whole space, and the whole space is always closed (its complement $\varnothing$ is open).

:::

:::

::: {.pf-step #s3}

$E$ is bounded.

::: pf-proof

$E \subseteq B(x_0, 1)$ for any $x_0 \in X$ (the diameter of $(0,1)$ is $1$; e.g. $E \subseteq B(1/2, 1)$).

:::

:::

::: {.pf-step #s4}

$E$ is not compact.

::: pf-proof

the sequence $x_k = 1/(k+1) \in E$ has no convergent subsequence in $X$: it converges to $0 \notin X$, and any subsequence also converges to $0$, so no subsequence converges to a point of $X$.

(Compactness of metric spaces is equivalent to sequential compactness.)

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} show closed + bounded $\not\Rightarrow$ compact in general metric spaces; compactness needs completeness (or the ambient space must be $\RR^n$). Alternative example: $X = \QQ$, $E = \QQ \cap [0,1]$ (closed and bounded in $\QQ$, not compact).

:::

:::

:::
