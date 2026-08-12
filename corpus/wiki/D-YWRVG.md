---
schema: qual/card@1
id: D-YWRVG
kind: definition
title: "Essential supremum and infimum, essentially bounded"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.definition title="Essential supremum and infimum, essentially bounded"}
An **essential lower bound** $b$ on a function $f$ is any real number such that $S_{b} \da \ts{x\st f(x) < b } = f\inv(-\infty, b)$ has measure zero.
The **essential infimum** is the supremum of all essential lower bounds, i.e. $\ess\inf f \da \sup_{b} \ts{b\st \mu S_b = 0}$.
This is the greatest lower bound almost everywhere.

Similarly an **essential upper bound** $c$ is any number such that $S^c \da f\inv(c, \infty)$ has measure zero, and the **essential supremum** is $\ess\sup f \da \inf_{c} \ts{c\st \mu S^c = 0}$, which is the least upper bound almost everywhere.

A function is **essentially bounded** if $\norm{f}_\infty \da \ess\sup f < \infty$.
These are functions which are bounded almost everywhere.
:::
