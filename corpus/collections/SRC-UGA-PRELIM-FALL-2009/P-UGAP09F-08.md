---
schema: qual/card@1
id: P-UGAP09F-08
kind: problem
title: Uniform convergence permits passage of the limit through an integral
classification:
  areas: [prelim]
  topics:
  - Uniform Convergence
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f:[0,1]\to\RR$ and $f_n:[0,1]\to\RR$ be continuous functions, and suppose $f_n\to f$ uniformly.

Give the definition of uniform convergence and, using basic properties of integrals and absolute values, show that
$$
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx
=
\int_0^1 f(x)\,dx.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The sequence $(f_n)$ converges uniformly to $f$ on $[0,1]$ if for every $\varepsilon>0$ there is an integer $N$ such that for every $n\ge N$ and every $x\in[0,1]$,
$$
\abs{f_n(x)-f(x)}<\varepsilon.
$$


::: pf-proof

This is the definition of uniform convergence on $[0,1]$: the same index $N$ works simultaneously for every point of the domain.

:::

:::

::: {.pf-step #s1-2}

For every $n$,
$$
\abs{
\int_0^1 f_n(x)\,dx-
\int_0^1 f(x)\,dx
}
\le
\int_0^1 \abs{f_n(x)-f(x)}\,dx.
$$


::: pf-proof

By linearity of the integral and the triangle inequality for integrals,
$$
\begin{aligned}
\abs{
\int_0^1 f_n(x)\,dx-
\int_0^1 f(x)\,dx
}
&=
\abs{\int_0^1 (f_n(x)-f(x))\,dx}\\
&\le
\int_0^1 \abs{f_n(x)-f(x)}\,dx.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

One has
$$
\boxed{
\lim_{n\to\infty}\int_0^1 f_n(x)\,dx
=
\int_0^1 f(x)\,dx.
}
$$


::: pf-proof

Let $\varepsilon>0$. By uniform convergence, choose $N$ as in step [](#s1-1){.pf-ref}. For every $n\ge N$ and every $x\in[0,1]$,
$$
\abs{f_n(x)-f(x)}<\varepsilon.
$$
Therefore step [](#s1-2){.pf-ref} gives
$$
\abs{
\int_0^1 f_n(x)\,dx-
\int_0^1 f(x)\,dx
}
\le
\int_0^1 \abs{f_n(x)-f(x)}\,dx
<
\int_0^1\varepsilon\,dx
=\varepsilon.
$$
This is exactly the definition of convergence of the sequence of integrals to $\int_0^1 f(x)\,dx$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-3){.pf-ref} proves the desired interchange of limit and integral.

:::

:::

:::
