---
schema: qual/card@1
id: P-JHUFA10RA2
kind: problem
title: Convolution of characteristic functions is continuous
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

Let $E, F \subset \mathbb{R}$ be two Lebesgue-measurable subsets of $\mathbb{R}$, each of finite measure, and let $\chi_E$ and $\chi_F$ denote their respective characteristic functions.

(a) Prove that the convolution $\chi_E * \chi_F$ defined by

$$\chi_E * \chi_F(x) = \int_{\mathbb{R}} \chi_E(y) \chi_F(x - y) \, dy$$

is a continuous function of $x$.

(b) Show that as $n \to \infty$

$$n \big(\chi_E * \chi_{[0, 1/n]}\big) \longrightarrow \chi_E$$

pointwise almost everywhere.
