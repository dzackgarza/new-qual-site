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
---

::: {.exercise}
Can there be a function $f:I\to \RR$ that is continuous on $\QQ$ and discontinuous otherwise?
:::

::: {.solution}
No. Let $I \subseteq \RR$ be an open interval and $f\colon I \to \RR$ any function.

<1>1. The set of points of continuity of $f$ is a countable intersection of open sets.

::: {.proof}
Let $U_n$ be the set of $x \in I$ having an open neighborhood $U \subseteq I$ with $\operatorname{diam} f(U) < 1/n$. If $U$ witnesses $x \in U_n$, it witnesses $y \in U_n$ for every $y \in U$, so $U_n$ is open. The function $f$ is continuous at $x$ if and only if $x \in U_n$ for every $n$.
:::

<1>2. $\QQ \cap I$ is not a countable intersection of open subsets of $I$.

::: {.proof}
Suppose $\QQ \cap I = \bigcap_n V_n$ with $V_n$ open. Each $V_n$ contains $\QQ \cap I$, so it is dense in $I$, and each $I \setminus \theset q$, $q \in \QQ \cap I$, is open and dense in $I$. This countable family of open dense subsets of $I$ has empty intersection, contradicting the Baire category theorem, which applies to $I$ because $I$ is homeomorphic to $\RR$.
:::

<1>3. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2. See also [[E-QSNCL]].
:::
:::
