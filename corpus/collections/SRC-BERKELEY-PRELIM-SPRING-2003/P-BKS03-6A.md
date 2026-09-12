---
schema: qual/card@1
id: P-BKS03-6A
kind: problem
title: A recurrence limit from $2x_{n+1}-x_n$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Suppose $(x_n)$ is a real sequence such that
\[
2x_{n+1}-x_n\longrightarrow x.
\]
Show that $x_n\to x$.
:::

::: {.solution}
First show that $\{ x _ { n } \}$ is bounded. We know that the sequence $\{ 2 x _ { n + 1 } - x _ { n } \}$ is bounded. Then we can choose M large so that $| x _ { 1 } | \le M$ and $| 2 x _ { n + 1 } - x _ { n } | \leq M$ for all n. We prove by induction that $| x _ { n } | \leq M$ for all n. Indeed, suppose that $| x _ { n } | \leq M$ . Then

$$
| x _ { n + 1 } | = | \frac { x _ { n } + ( 2 x _ { n + 1 } - x _ { n } ) } { 2 } | \leq \frac { 1 } { 2 } ( | x _ { n } | + | 2 x _ { n + 1 } - x _ { n } | ) \leq M
$$

This concludes the induction and shows that $\{ x _ { n } \}$ is bounded.

Now write again

$$
x _ { n + 1 } = { \frac { x _ { n } + ( 2 x _ { n + 1 } - x _ { n } ) } { 2 } }
$$

and take lim sup. We get

$$
\operatorname* { l i m } \operatorname* { s u p } x _ { n } \leq { \frac { \operatorname* { l i m } \operatorname* { s u p } x _ { n } + x } { 2 } }
$$

which gives lim sup $x _ { n } \leq x$ . Similarly we get lim inf $x _ { n } \geq x$ . Together these two inequalities imply that lim $x _ { n } = x$
:::
