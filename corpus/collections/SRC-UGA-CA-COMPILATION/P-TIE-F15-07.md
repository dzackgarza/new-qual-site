---
schema: qual/card@1
id: P-TIE-F15-07
kind: problem
title: The Gaussian $e^{-\pi x^2}$ is its own Fourier transform for complex frequencies
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 7.
---

::: {.problem}
Prove by justifying all steps that for all $\xi \in \CC$ we have $e ^ { - \pi \xi ^ { 2 } } = \int _ { - \infty } ^ { \infty } e ^ { - \pi x ^ { 2 } } e ^ { 2 \pi i x \xi } d x$

Hint: You may use that fact in Example 1 on p. 42 of the textbook without proof, i.e., you may assume the above is true for real values of $\xi .$
:::

::: {.solution}

Define
$$
F(\xi)
\coloneqq
\int_{-\infty}^{\infty}
e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
$$

::: pf

::: pf-step

For every $\xi\in\CC$, the defining integral for $F(\xi)$ converges absolutely.


::: pf-proof

Write
$$
\xi=u+iv,
\qquad
u,v\in\RR.
$$
Then
$$
\abs{e^{2\pi i x\xi}}
=
e^{-2\pi xv}.
$$
Hence
$$
\begin{aligned}
\abs{
e^{-\pi x^2}e^{2\pi i x\xi}
}
&=
e^{-\pi x^2-2\pi xv}\\
&=
e^{\pi v^2}e^{-\pi(x+v)^2}.
\end{aligned}
$$
The final function is integrable over $\RR$, so the integral converges absolutely.

:::

:::

::: {.pf-step #s1-2}

Let $K\subset\CC$ be compact. There is an integrable function $g_K:\RR\to[0,\infty)$ such that
$$
\abs{
e^{-\pi x^2}e^{2\pi i x\xi}
}
\le
g_K(x)
$$
for every $x\in\RR$ and every $\xi\in K$.


::: pf-proof

Since $K$ is compact, there exists $M>0$ such that
$$
\abs{\operatorname{Im}\xi}\le M
$$
for all $\xi\in K$. Thus
$$
\abs{
e^{-\pi x^2}e^{2\pi i x\xi}
}
\le
e^{-\pi x^2+2\pi M\abs{x}}.
$$
Set
$$
g_K(x)
\coloneqq
e^{-\pi x^2+2\pi M\abs{x}}.
$$
For $\abs{x}\ge4M$,
$$
-\pi x^2+2\pi M\abs{x}
\le
-\frac{\pi}{2}x^2.
$$
Hence $g_K$ is dominated outside a bounded interval by $e^{-\pi x^2/2}$ and is continuous on the remaining bounded interval. Therefore $g_K$ is integrable on $\RR$.

:::

:::

::: {.pf-step #s1-3}

The function $F$ is entire.


::: pf-proof

For $R>0$, define
$$
F_R(\xi)
\coloneqq
\int_{-R}^{R}
e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
$$
For fixed $R$, the integrand is entire in $\xi$, uniformly on compact $\xi$-sets over the finite interval $[-R,R]$, so differentiation under the integral sign gives
$$
F_R'(\xi)
=
\int_{-R}^{R}
2\pi i x
e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
$$
Thus each $F_R$ is entire.

Let $K\subset\CC$ be compact. By step [](#s1-2){.pf-ref},
$$
\sup_{\xi\in K}
\abs{F(\xi)-F_R(\xi)}
\le
\int_{\abs{x}>R}g_K(x)\,dx
\longrightarrow0.
$$
Hence $F_R\to F$ uniformly on every compact subset of $\CC$. By the Weierstrass theorem on locally uniform limits of holomorphic functions, $F$ is entire.

:::

:::

::: {.pf-step #s1-4}

The function
$$
G(\xi)
\coloneqq
e^{-\pi\xi^2}
$$
is entire and satisfies
$$
F(\xi)=G(\xi)
$$
for every real $\xi$.


::: pf-proof

The function $G$ is the exponential of the polynomial $-\pi\xi^2$, so it is entire. The equality
$$
e^{-\pi\xi^2}
=
\int_{-\infty}^{\infty}
e^{-\pi x^2}e^{2\pi i x\xi}\,dx
$$
for real $\xi$ is exactly the real-frequency identity that the problem permits us to assume.

:::

:::

::: {.pf-step #s1-5}

For every $\xi\in\CC$,
$$
\boxed{
e^{-\pi\xi^2}
=
\int_{-\infty}^{\infty}
e^{-\pi x^2}e^{2\pi i x\xi}\,dx.
}
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, the functions $F$ and $G$ are entire and agree on the real axis. The real axis has accumulation points in $\CC$, so the identity theorem implies
$$
F\equiv G
$$
on $\CC$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required identity for every complex frequency $\xi$.

:::

:::

:::
