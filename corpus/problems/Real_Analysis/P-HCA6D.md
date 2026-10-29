---
schema: qual/card@1
id: P-HCA6D
kind: problem
title: No function continuous exactly on $\QQ$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Counterexamples
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source uses an interval I that it never introduces; the statement declares I an open interval, as the solution reads it.
---

::: {.exercise}
Let $I \subseteq \RR$ be an open interval.
Can there be a function $f:I\to \RR$ that is continuous on $\QQ$ and discontinuous otherwise?
:::

::: {.solution}
No. Let $f\colon I \to \RR$ be any function.

::: pf

::: {.pf-step #s1}

The set of points of continuity of $f$ is a countable intersection of open sets.

::: pf-proof

Let $U_n$ be the set of $x \in I$ having an open neighborhood $U \subseteq I$ with $\operatorname{diam} f(U) < 1/n$. If $U$ witnesses $x \in U_n$, it witnesses $y \in U_n$ for every $y \in U$, so $U_n$ is open. The function $f$ is continuous at $x$ if and only if $x \in U_n$ for every $n$.

:::

:::

::: {.pf-step #s2}

$\QQ \cap I$ is not a countable intersection of open subsets of $I$.

::: pf-proof

Suppose $\QQ \cap I = \bigcap_n V_n$ with $V_n$ open. Each $V_n$ contains $\QQ \cap I$, so it is dense in $I$, and each $I \setminus \theset q$, $q \in \QQ \cap I$, is open and dense in $I$. This countable family of open dense subsets of $I$ has empty intersection, contradicting the Baire category theorem, which applies to $I$ because $I$ is homeomorphic to $\RR$.

:::

:::

::: pf-qed

If $f$ were continuous exactly at the points of $\QQ \cap I$, step [](#s1){.pf-ref} would make $\QQ \cap I$ a countable intersection of open subsets of $I$, contradicting step [](#s2){.pf-ref}.

:::

:::

:::
