---
schema: qual/card@1
id: P-WVJBX
kind: problem
title: 'A sequence converging to $0$ in $L^2$ has a subsequence converging almost everywhere'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

1. Suppose $\{ f _ { n } \} _ { n = 1 } ^ { \infty } \subset L ^ { 2 } ( \mathbb { R } )$ is a sequence that converges to 0 in the $L ^ { 2 }$ norm; in other words,

$$
| | f _ { n } | | _ { L ^ { 2 } ( \mathbb { R } ) } = \left( \int _ { - \infty } ^ { \infty } | f _ { n } | ^ { 2 } \ d x \right) ^ { \frac { 1 } { 2 } } \to 0 .
$$

Prove that there exists a subsequence $\{ f _ { n _ { k } } \}$ such that $f _ { n _ { k } }  0$ almost everywhere.

::: {.solution}
<1>1. Since $\|f_n\|_{L^2} \to 0$, we can choose a subsequence $\{f_{n_k}\}$ with $\|f_{n_k}\|_{L^2} \le 2^{-k}$.
::: {.proof}
convergence to $0$ lets us pick $n_k$ with $\|f_{n_k}\| \le 2^{-k}$.
:::

<1>2. $\sum_{k=1}^{\infty} \|f_{n_k}\|_{L^2}^2 \le \sum_{k=1}^{\infty} 4^{-k} < \infty$.
::: {.proof}
<1>1.
:::

<1>3. Hence $\sum_{k=1}^{\infty} \int |f_{n_k}|^2\, dx < \infty$.
::: {.proof}
<1>2.
:::

<1>4. By the monotone convergence theorem, $\int \sum_{k=1}^{\infty} |f_{n_k}|^2\, dx = \sum_{k=1}^{\infty} \int |f_{n_k}|^2\, dx < \infty$.
::: {.proof}
interchange sum and integral for nonnegative functions.
:::

<1>5. Hence $\sum_{k=1}^{\infty} |f_{n_k}(x)|^2 < \infty$ for almost every $x$.
::: {.proof}
a function with finite integral is finite almost everywhere.
:::

<1>6. Therefore $|f_{n_k}(x)|^2 \to 0$, i.e. $f_{n_k}(x) \to 0$, for almost every $x$.
::: {.proof}
the terms of a convergent series tend to $0$.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
