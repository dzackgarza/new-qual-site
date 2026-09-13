---
schema: qual/card@1
id: P-AMH-ALG-SG16-22
kind: problem
title: Amherst algebra study guide problem 22
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
(January 2014) A nonzero element $a$ of a ring is said to be nilpotent if there is a positive integer $n\ge 1$ such that $a^n=0$.
(The element $0$ itself is not said to be nilpotent.)
Let $R$ be a commutative ring, and let $I\subseteq R$ be an ideal.
Prove that the following two statements are equivalent.
(a) The quotient ring $R/I$ contains no nilpotents.
(b) For every element $b\in R$ such that $b^m\in I$ for some positive integer $m\ge 1$, we have $b\in I$.
:::

::: {.solution}
Proof.
(=⇒) Given b∈R and m≥ 1 with bm∈I, we have (I +b)m =I +bm =I + 0. SinceI + 0 is the zero element of R/I, it follows that I +b is either nilpotent or zero in R/I. But by assumption (a), I +b is not nilpotent.
Therefore, I +b =I + 0, which means b =b− 0∈I. (⇐=) SupposeI +b∈R/I is a nilpotent.
Then there is some integerm≥ 1 such that (I +b)m =I +0. That is, I +bm = (I +b)m =I + 0, and hence bm =bm− 0∈I. By property (b), we have b∈I. Thus, I +b =I + 0, contradicting the assumption that I +b is nilpotent, and proving that R/I has no nilpotents.
QED
:::
