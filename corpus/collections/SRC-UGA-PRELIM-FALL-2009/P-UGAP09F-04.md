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
\[
\lim_{x\to x_0}f(x).
\]
Then use the definition to show that
\[
\lim_{x\to1/4}\sqrt{x}=\frac12.
\]
:::

::: {.solution}
<1>1. A finite limit $\lim_{x\to x_0}f(x)$ exists if there is an $L\in\RR$ such that for every $\varepsilon>0$ there is a $\delta>0$ for which
$$
0<|x-x_0|<\delta
\quad\Longrightarrow\quad
|f(x)-L|<\varepsilon
$$
for every $x$ in the domain of $f$.

::: {.proof}
This is the $\varepsilon$-$\delta$ definition of the assertion that $f(x)$ tends to the finite real number $L$ as $x$ tends to $x_0$.
:::

<1>2. For every $x\ge0$,
$$
\left|\sqrt{x}-\frac12\right|
\le 2\left|x-\frac14\right|.
$$

::: {.proof}
Rationalizing gives
$$
\left|\sqrt{x}-\frac12\right|
=\frac{\left|x-\frac14\right|}{\sqrt{x}+\frac12}.
$$
Since $x\ge0$, one has $\sqrt{x}+\frac12\ge\frac12$, and the claimed inequality follows.
:::

<1>3. One has
$$
\boxed{\lim_{x\to1/4}\sqrt{x}=\frac12}.
$$

::: {.proof}
Let $\varepsilon>0$ and choose
$$
\delta\coloneqq\frac{\varepsilon}{2}.
$$
If $x\ge0$ and $0<|x-1/4|<\delta$, then step <1>2 gives
$$
\left|\sqrt{x}-\frac12\right|
\le2\left|x-\frac14\right|
<2\delta
=\varepsilon.
$$
By the definition in step <1>1, the stated limit follows.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 gives the requested definition and step <1>3 proves the requested limit.
:::
:::
