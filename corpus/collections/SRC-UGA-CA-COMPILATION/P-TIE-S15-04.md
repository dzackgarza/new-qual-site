---
schema: qual/card@1
id: P-TIE-S15-04
kind: problem
title: Analytic functions unimodular on the unit circle are finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 4.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the OCR accent on f, cleaned the LaTeX, and moved the Stein cross-reference to a remark, against Spring 2015, question 4, page 11 of Questions_from_Tie.pdf.
---

::: {.problem}
Suppose $f$ is analytic in an open set containing the unit disc $\mathbb{D}$ and $\abs{f(z)} = 1$ when $\abs{z} = 1$. Show that either $f(z) = e^{i\theta}$ for some $\theta \in \mathbb{R}$ or there are finite number of $z_k \in \mathbb{D}$, $k \le n$ and $\theta \in \mathbb{R}$ such that
$$
f(z) = e^{i\theta} \prod_{k=1}^n \frac{z - z_k}{1 - \bar{z}_k z}.
$$
:::

::: {.remark}
The source adds "Also cf. Stein et al, 1.4.7, 3.8.17", a pointer to exercises in Stein and Shakarchi, *Complex Analysis*; the statement does not depend on them.
:::
