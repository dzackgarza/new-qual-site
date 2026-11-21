---
schema: qual/card@1
id: P-AMH-ALG-SG16-01
kind: problem
title: Intersections of subgroups are subgroups
classification:
  areas:
  - algebra
  topics:
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained document `assets/attachments/Study_Guide_for_Algebra.pdf`: the statement is item 1 of the Subgroups section, dated January 2012, of the Amherst study guide, and its printed words are
    the card's. The item and the file are now named in the solution's opening sentence. Not
    checked in this pass: the argument, which the edit does not touch.
---

::: {.problem}
Let $G$ be a group, and let $H,K\subseteq G$ be subgroups of $G$.
Prove the following standard theorem about subgroups: that $H\cap K$ is a subgroup of $G$.
:::

::: {.solution}
This is item 1 of the Subgroups section, dated January 2012, of the Amherst study guide, retained in this repository as `assets/attachments/Study_Guide_for_Algebra.pdf`; the statement below is its wording.

::: pf

::: {.pf-step #s1-1}
The intersection $H\cap K$ is nonempty.

::: pf-proof
Since $H$ and $K$ are subgroups of $G$, both contain the identity $e$. Hence
$$
e\in H\cap K.
$$
:::

:::

::: {.pf-step #s1-2}
The intersection is closed under the subgroup test.

::: pf-proof
Let
$$
a,b\in H\cap K.
$$
Then $a,b\in H$ and $a,b\in K$. Because $H$ and $K$ are subgroups,
$$
ab^{-1}\in H
\qquad\text{and}\qquad
ab^{-1}\in K.
$$
Therefore
$$
ab^{-1}\in H\cap K.
$$
:::

:::

::: pf-step
Therefore
$$
\boxed{H\cap K\le G}.
$$

::: pf-proof
By step [](#s1-1){.pf-ref}, $H\cap K$ is nonempty, and by step [](#s1-2){.pf-ref} it is closed under $ab^{-1}$. The subgroup test therefore shows that $H\cap K$ is a subgroup of $G$.
:::

:::

:::

:::
