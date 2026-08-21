---
schema: qual/card@1
id: P-GT5L7
kind: problem
title: $\ZZ^{*2}$ has subgroups isomorphic to $\ZZ^{*n}$ for every $n$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Groups
  - Fundamental Group
relations: []
review: draft
solved: true
---

Show that $\ZZ^{\ast 2}$ has subgroups isomorphic to $\ZZ^{\ast n}$ for every $n$.

::: {.solution}

\envlist
::: {.concept}
\envlist

1. $\pi_1(\bigvee^k S^1) = \ZZ^{\ast k}$

2. $\tilde X \surjects X \implies \pi_1(\tilde X) \injects \pi_1(X)$

3. Every subgroup $G \leq \pi_1(X)$ corresponds to a covering space $X_G \surjects X$

4. $A \subseteq B \implies F(A) \leq F(B)$ for free groups.
:::

It is easier to prove the stronger claim that $\ZZ^\NN \leq \ZZ^{\ast 2}$ (i.e. the free group on countably many generators) and use fact 4 above.
Just take the covering space $\tilde X \surjects S^1 \vee S^1$ defined via the gluing map $\RR \union_{\ZZ} S^1$ which attaches a circle to each integer point, taking 0 as the base point.
Then let $a$ denote a translation and $b$ denote traversing a circle, so we have $\pi_1(\tilde X) = \left<\union_{n\in\ZZ}a^nba^{-n}\right>$ which is a free group on countably many generators.
Since $\tilde X$ is a covering space, $\pi_1(\tilde X) \injects \pi_1(S^1 \vee S^1) = \ZZ^{\ast 2}$.
By 4, we can restrict this to $n$ generators for any $n$ to get a subgroup, and $A\leq B \leq C \implies A \leq C$ as groups.
:::
