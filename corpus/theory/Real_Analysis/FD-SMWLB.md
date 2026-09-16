---
schema: qual/card@1
id: FD-SMWLB
kind: definition
title: Nowhere dense sets
prompts:
- What does it mean for a set to be nowhere dense?
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Closure
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
A set $A\subseteq X$ is \dfn{nowhere dense} in $X$ if its [[D-ASXW6|closure]] has empty interior, $\qty{\overline{A}}^\circ=\emptyset$; equivalently, $A$ is not [[FD-BA2WU|dense]] in any nonempty open subset of $X$.
:::

::: {.remark}
For $X=\RR$, a set $A$ is nowhere dense if and only if every open interval $I$ contains an open subinterval $S\subseteq I$ with $S\cap A = \emptyset$, that is, $\overline{A}$ contains no open interval.
:::

::: {.example}
In $\RR$, the sets $\theset{1/n \suchthat n\geq 1}$ and $\ZZ$ are nowhere dense: their closures $\theset{0}\cup\theset{1/n\suchthat n\geq 1}$ and $\ZZ$ contain no open interval.
The sets $\QQ$ and $\ZZ\cup\qty{(a, b)\cap \QQ}$ with $a<b$ are not nowhere dense: their closures contain $\RR$ and $[a,b]$ respectively.
:::
