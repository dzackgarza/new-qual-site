---
schema: qual/card@1
id: P-BKF14-5B
kind: problem
title: Zeros minus poles of an elliptic function sum to a Gaussian integer
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
  note: Restored the poles w_b and put the unit-square condition inside math against Fall_2014_Exam.pdf page 16 problem 5B.
---

::: {.problem}
Let $f$ be a doubly-periodic meromorphic function: $f(z + 1) = f(z) = f(z + i)$ for all $z \in \mathbf{C}$. Let $z_a$ be the zeroes of $f$ inside the unit square $0 < \operatorname{Re} z, \operatorname{Im} z < 1$, $w_b$ be its poles inside the square, and $k_a$ and $l_b$ be respective multiplicities. Assuming that $f$ has no zeroes or poles on the boundary of the square, prove that

$$
\sum_a k_a z_a - \sum_b l_b w_b \in \mathbb{Z}[i],
$$

that is, is a Gaussian integer. Hint: Show that the following integral along the boundary of the square is a Gaussian integer:

$$
\frac{1}{2\pi i} \oint z \frac{f'(z)}{f(z)} \, dz.
$$
:::
