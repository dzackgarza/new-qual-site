---
schema: qual/card@1
id: P-BKS03-6A
kind: problem
title: If $2x_{n+1}-x_n\to x$, then $x_n\to x$
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

::: {.problem}
Suppose $(x_n)$ is a real sequence such that
\[
2x_{n+1}-x_n\longrightarrow x.
\]
Show that $x_n\to x$.
:::

::: {.solution}
First show that $\{x_n\}$ is bounded.
We know that the sequence $\{2x_{n+1}-x_n\}$ is bounded.
Then we can choose $M$ large so that $\abs{x_1}\leq M$ and $\abs{2x_{n+1}-x_n}\leq M$ for all $n$. We prove by induction that $\abs{x_n}\leq M$ for all $n$. Indeed, suppose that $\abs{x_n}\leq M$. Then

$$
\abs{x_{n+1}}=\abs{\frac{x_n+(2x_{n+1}-x_n)}{2}}\leq\frac12\bigl(\abs{x_n}+\abs{2x_{n+1}-x_n}\bigr)\leq M.
$$

This concludes the induction and shows that $\{x_n\}$ is bounded.

Now write again

$$
x_{n+1}=\frac{x_n+(2x_{n+1}-x_n)}{2}
$$

and take $\limsup$.
We get

$$
\limsup x_n\leq\frac{\limsup x_n+x}{2},
$$

which gives $\limsup x_n\leq x$. Similarly we get $\liminf x_n\geq x$. Together these two inequalities imply that $\lim x_n=x$.
:::
