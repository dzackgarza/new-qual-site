---
schema: qual/card@1
id: E-QSNCL
kind: problem
title: No function continuous on $\QQ$ and discontinuous on $\RR\setminus\QQ$
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
No. Let $I \subseteq \RR$ be an open interval and $f\colon I \to \RR$ any function. For $n \geq 1$ let
$$
U_n = \theset{x \in I : \operatorname{diam} f(U) < 1/n \text{ for some open } U \subseteq I \text{ containing } x}.
$$

<1>1. Each $U_n$ is open, and the set of points of continuity of $f$ is $\bigcap_n U_n$.

::: {.proof}
If $U$ witnesses $x \in U_n$, it witnesses $y \in U_n$ for every $y \in U$, so $U \subseteq U_n$. The function $f$ is continuous at $x$ if and only if for every $n$ there is an open $U \ni x$ with $\operatorname{diam} f(U) < 1/n$.
:::

<1>2. $\QQ \cap I$ is not a countable intersection of open subsets of $I$.

::: {.proof}
Suppose $\QQ \cap I = \bigcap_n V_n$ with $V_n$ open. Each $V_n$ contains $\QQ \cap I$, so it is dense in $I$. For $q \in \QQ \cap I$, $I \setminus \theset q$ is open and dense in $I$. Then the countable family $\theset{V_n} \cup \theset{I \setminus \theset q : q \in \QQ \cap I}$ consists of open dense subsets of $I$, and its intersection is $(\QQ \cap I) \setminus \QQ = \emptyset$. This contradicts the Baire category theorem, which applies to $I$ because $I$ is homeomorphic to $\RR$.
:::

<1>3. Q.E.D.

::: {.proof}
By step <1>1 the set of continuity points of $f$ is a countable intersection of open sets, and by step <1>2 the set $\QQ \cap I$ is not.
:::
:::
