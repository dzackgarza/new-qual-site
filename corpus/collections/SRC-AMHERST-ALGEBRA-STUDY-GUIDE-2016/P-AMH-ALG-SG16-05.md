---
schema: qual/card@1
id: P-AMH-ALG-SG16-05
kind: problem
title: Amherst algebra study guide problem 5
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(January 2011) Suppose that $H\subseteq G$ is a subgroup with the property that for every $x,y\in G$, we have $xyx^{-1}y^{-1}\in H$. Prove that $H$ is a normal subgroup of $G$.
:::

::: {.solution}
Proof.
Assume g∈G and h∈H. By the given property of H, we have ghg−1h−1∈H. Since H is closed under multiplication, ghg−1 =ghg−1(h−1h) = (ghg−1h−1)h∈H as desired.
QED
:::
