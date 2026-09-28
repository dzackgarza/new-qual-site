---
schema: qual/card@1
id: P-BKS17-6B
kind: problem
title: Low-rank approximation of the matrix $f(t_is_j)$ for analytic $f$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 17 problem 6B.
---

::: {.problem}
Let $D$ be the unit disk in the complex plane $\mathbb{C}$, $f : D \to \mathbb{C}$ an analytic function with

$$
|f^{(k)}(0)| \leq M
$$

for all $k \geq 0$, and let $t_p \in D$, $s_p \in D$ for $1 \leq p \leq n$. For each $n \geq 1$ define $A_{ij} = f(t_i s_j)$ for $1 \leq i, j \leq n$. For each $r \geq 1$ find an $n \times n$ matrix $B$ with rank $\leq r$ and

$$
|A_{ij} - B_{ij}| \leq \frac{2M}{r!}
$$

for $1 \leq i, j \leq n$.
:::
