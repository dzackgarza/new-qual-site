---
schema: qual/card@1
id: P-WESTOP09-I2
kind: problem
title: The slotted plane is Hausdorff, separable, nonregular, and not first countable
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Define the *slotted plane* to be $\mathbb R^2$ with the following topology: a set $U$ is open if for every $x\in U$ there are an ordinary open disk $D$ about $x$, an integer $k\ge0$, and straight lines $L_1,\dots,L_k$ through $x$ such that
\[
\{x\}\cup\bigl(D\setminus(L_1\cup\cdots\cup L_k)\bigr)\subseteq U.
\]

1. Prove that these sets form a topology finer than the usual topology on $\mathbb R^2$.
2. Prove that the slotted plane is Hausdorff but not regular.
3. Prove that it is separable but not first countable.
:::
