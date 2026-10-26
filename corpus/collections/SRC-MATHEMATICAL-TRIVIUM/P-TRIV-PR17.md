---
schema: qual/card@1
id: P-TRIV-PR17
kind: problem
title: Chernoff and Markov tail bounds
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 17, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $\xi$ be a continuous random variable.

(a) Prove that if $\mathbf { E } e ^ { \lambda \xi }$ is finite then

$$
P ( \xi \geqslant x ) \leqslant e ^ { - \lambda x } \mathbf { E } e ^ { \lambda \xi } , \quad \lambda > 0 .\tag{45}
$$

(b) Prove that if $\mathbf { E } | \boldsymbol { \xi } | ^ { m }$ is finite then

$$
P ( | \xi | \geqslant x ) \leqslant x ^ { - m } \mathbf { E } | \xi | ^ { m } , x > 0 , m > 0 .\tag{46}
$$
:::

::: pf

::: pf-step

For $\lambda>0$, the event $\{\xi\geq x\}$ equals
\[
\{e^{\lambda\xi}\geq e^{\lambda x}\}.
\]


::: pf-proof

The exponential function $u\mapsto e^{\lambda u}$ is strictly increasing when $\lambda>0$.

:::

:::

::: pf-step

Markov's inequality applied to the nonnegative random variable $e^{\lambda\xi}$ gives
\[
\boxed{
P(\xi\geq x)
\leq e^{-\lambda x}\mathbf E e^{\lambda\xi}}.
\]


::: pf-proof

For any nonnegative random variable $Y$ and $a>0$,
\[
\mathbf EY\geq\mathbf E[Y\mathbf1_{Y\geq a}]
\geq aP(Y\geq a),
\]
so $P(Y\geq a)\leq\mathbf EY/a$. Take $Y=e^{\lambda\xi}$ and $a=e^{\lambda x}$, using step <1>1. Finiteness of the stated exponential moment makes the bound finite.

:::

:::

::: pf-step

For $m>0$ and $x>0$, the event $\{|\xi|\geq x\}$ equals
\[
\{|\xi|^m\geq x^m\}.
\]


::: pf-proof

The function $u\mapsto u^m$ is increasing on $[0,\infty)$ for every $m>0$.

:::

:::

::: pf-step

Markov's inequality applied to $|\xi|^m$ gives
\[
\boxed{
P(|\xi|\geq x)
\leq x^{-m}\mathbf E|\xi|^m}.
\]


::: pf-proof

Apply the Markov inequality proved in step <1>2 to the nonnegative random variable $Y=|\xi|^m$ with threshold $a=x^m$, and use step <1>3.

:::

:::

::: pf-qed

Step <1>2 proves part (a), and step <1>4 proves part (b). Neither argument requires $\xi$ to have a continuous distribution.

:::

:::
