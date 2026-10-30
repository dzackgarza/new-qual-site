---
schema: qual/card@1
id: P-UCLAB05S-AN6
kind: problem
title: Compactness of a normalized family of Lipschitz functions
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 6 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Consider the set of functions $f:[0,1]\to\RR$ satisfying
$$
\abs{f(x)-f(y)}\leq\abs{x-y}
\qquad\text{and}\qquad
\int_0^1 f(x)\,dx=1.
$$
Show that this is a compact subset of $C([0,1])$.
:::

::: {.solution}

Let $\mathcal F$ denote the displayed family, and equip $C([0,1])$ with the uniform norm
$$
\norm{f}_\infty\coloneqq\sup_{x\in[0,1]}\abs{f(x)}.
$$

::: pf

::: {.pf-step #s1-1}

The family $\mathcal F$ is equicontinuous.


::: pf-proof

Every $f\in\mathcal F$ satisfies
$$
\abs{f(x)-f(y)}\le\abs{x-y}.
$$
Thus, given $\varepsilon>0$, choosing $\delta=\varepsilon$ gives
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}<\varepsilon
$$
simultaneously for every $f\in\mathcal F$.

:::

:::

::: {.pf-step #s1-2}

The family $\mathcal F$ is uniformly bounded; in fact, for every $f\in\mathcal F$ and every $x\in[0,1]$,
$$
\abs{f(x)-1}\le\frac12.
$$


::: pf-proof

Since $\int_0^1f(t)\,dt=1$,
$$
\begin{aligned}
\abs{f(x)-1}
&=\abs{\int_0^1(f(x)-f(t))\,dt}\\
&\le\int_0^1\abs{f(x)-f(t)}\,dt\\
&\le\int_0^1\abs{x-t}\,dt\\
&=\frac{x^2+(1-x)^2}{2}\\
&\le\frac12.
\end{aligned}
$$
Hence $\norm{f}_\infty\le3/2$ for every $f\in\mathcal F$.

:::

:::

::: {.pf-step #s1-3}

The closure of $\mathcal F$ in $C([0,1])$ is compact.


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, the family is equicontinuous and uniformly bounded on the compact interval $[0,1]$. The Arzelà--Ascoli theorem therefore implies that $\mathcal F$ is relatively compact in the uniform topology; equivalently, its closure is compact.

:::

:::

::: {.pf-step #s1-4}

The family $\mathcal F$ is closed in $C([0,1])$.


::: pf-proof

Suppose $f_n\in\mathcal F$ and $f_n\to f$ uniformly. For every $x,y\in[0,1]$,
$$
\abs{f(x)-f(y)}
=\lim_{n\to\infty}\abs{f_n(x)-f_n(y)}
\le\abs{x-y}.
$$
Also,
$$
\abs{\int_0^1 f(x)\,dx-1}
=\abs{\int_0^1(f(x)-f_n(x))\,dx}
\le\norm{f-f_n}_\infty\to0.
$$
Thus $\int_0^1f=1$, so $f\in\mathcal F$.

:::

:::

::: {.pf-step #s1-5}

The set $\mathcal F$ is compact in $C([0,1])$.


::: pf-proof

By step [](#s1-3){.pf-ref}, the closure of $\mathcal F$ is compact, and by step [](#s1-4){.pf-ref} the family equals its closure. Hence $\mathcal F$ itself is compact.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
