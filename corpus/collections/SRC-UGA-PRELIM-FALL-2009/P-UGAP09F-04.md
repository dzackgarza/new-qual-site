---
schema: qual/card@1
id: P-UGAP09F-04
kind: problem
title: Define a limit and prove $\sqrt{x}\to1/2$ as $x\to1/4$
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
Give the $\varepsilon$-$\delta$ definition for the existence of
$$
\lim_{x\to x_0}f(x).
$$
Then use the definition to show that
$$
\lim_{x\to1/4}\sqrt{x}=\frac12.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A finite limit $\lim_{x\to x_0}f(x)$ exists if there is an $L\in\RR$ such that for every $\varepsilon>0$ there is a $\delta>0$ for which
$$
0<|x-x_0|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon
$$
for every $x$ in the domain of $f$.


::: pf-proof

This is the $\varepsilon$-$\delta$ definition of the assertion that $f(x)$ tends to the finite real number $L$ as $x$ tends to $x_0$.

:::

:::

::: {.pf-step #s1-2}

For every $x\ge0$,
$$
\left|\sqrt{x}-\frac12\right|
\le 2\left|x-\frac14\right|.
$$


::: pf-proof

Rationalizing gives
$$
\left|\sqrt{x}-\frac12\right|
=\frac{\left|x-\frac14\right|}{\sqrt{x}+\frac12}.
$$
Since $x\ge0$, one has $\sqrt{x}+\frac12\ge\frac12$, and the claimed inequality follows.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{\lim_{x\to1/4}\sqrt{x}=\frac12}.
$$


::: pf-proof

Let $\varepsilon>0$ and choose
$$
\delta\coloneqq\frac{\varepsilon}{2}.
$$
If $x\ge0$ and $0<|x-1/4|<\delta$, then step [](#s1-2){.pf-ref} gives
$$
\left|\sqrt{x}-\frac12\right|
\le2\left|x-\frac14\right|
<2\delta
=\varepsilon.
$$
By the definition in step [](#s1-1){.pf-ref}, the stated limit follows.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition and step [](#s1-3){.pf-ref} proves the requested limit.

:::

:::

:::
