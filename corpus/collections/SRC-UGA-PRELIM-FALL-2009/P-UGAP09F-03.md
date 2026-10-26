---
schema: qual/card@1
id: P-UGAP09F-03
kind: problem
title: Prove a weighted finite geometric-sum formula by induction
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Fix $x\in\mathbb R$. Using mathematical induction, show that if $x\ne1$, then for every $n\ge1$,
\[
x+2x^2+3x^3+\cdots+nx^n
=
\frac{nx^{n+2}-(n+1)x^{n+1}+x}{(x-1)^2}.
\]
:::

Fix $x\in\RR$ with $x\ne1$, and let $S_n\coloneqq\sum_{k=1}^n kx^k$.

::: pf

::: pf-step

The claimed identity holds for $n=1$.


::: pf-proof

For $n=1$, the left-hand side is $S_1=x$, while
$$
\frac{x^3-2x^2+x}{(x-1)^2}
=\frac{x(x-1)^2}{(x-1)^2}=x.
$$

:::

:::

::: pf-step

If the claimed identity holds for some $n\ge1$, then it holds for $n+1$.


::: pf-proof

By the induction hypothesis,
$$
\begin{aligned}
S_{n+1}
&=S_n+(n+1)x^{n+1}\\
&=\frac{nx^{n+2}-(n+1)x^{n+1}+x}{(x-1)^2}+(n+1)x^{n+1}\\
&=\frac{nx^{n+2}-(n+1)x^{n+1}+x+(n+1)x^{n+1}(x-1)^2}{(x-1)^2}\\
&=\frac{(n+1)x^{n+3}-(n+2)x^{n+2}+x}{(x-1)^2}.
\end{aligned}
$$
This is exactly the stated formula with $n$ replaced by $n+1$.

:::

:::

::: pf-step

For every integer $n\ge1$,
$$
\boxed{x+2x^2+\cdots+nx^n
=\frac{nx^{n+2}-(n+1)x^{n+1}+x}{(x-1)^2}.}
$$


::: pf-proof

Step <1>1 is the base case and step <1>2 is the induction step, so the result follows by mathematical induction.

:::

:::

::: pf-qed

Step <1>3 is the required identity.

:::

:::
