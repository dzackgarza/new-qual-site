---
title: Continuity
order: 30
topics:
- Continuity
- Uniform Continuity
- Fixed Points
---

# Continuity

::: {.proposition}
For $f\colon I\to\RR$ on an interval $I$:
$$
f \text{ differentiable with bounded } f' \implies f \text{ Lipschitz} \implies f \text{ absolutely continuous} \implies f \text{ uniformly continuous} \implies f \text{ continuous}.
$$

:::

::: {.proof}
If $\abs{f'}\leq C$, the mean value theorem gives $\abs{f(x)-f(y)}\leq C\abs{x-y}$.
If $f$ is $C$-Lipschitz and $\sum_i\abs{b_i-a_i}<\varepsilon/C$ for disjoint intervals $(a_i,b_i)$, the triangle inequality gives $\sum_i\abs{f(b_i)-f(a_i)}<\varepsilon$.
Absolute continuity applied to a single interval is uniform continuity, and uniform continuity implies continuity by definition.

:::

## Discontinuity sets

[[L-75UZY]]

::: {.proof}
Let $(r_n)_{n\geq1}$ enumerate $\QQ$, and let $f(r_n) \coloneqq \frac 1 n$ and $f(x)\coloneqq0$ for $x\notin\QQ$.
For every $x_0$ and $N$, some neighborhood of $x_0$ omits $r_1,\ldots,r_N$ (other than possibly $x_0$ itself), so $\lim_{x\to x_0}f(x) = 0$.
Hence $f$ is continuous exactly where $f(x_0)=0$, that is, on $\RR\setminus\QQ$.

:::

[[PR-F5V7D]]

[[FF-AVBFU]] [[FF-5EBCJ]]

::: {.proof}
The discontinuity set $D_f = \bigcup_{k\geq1}\theset{\omega_f\geq 1/k}$ is an $F_\sigma$ set, since $f$ is continuous at $x$ if and only if $\omega_f(x) = 0$ and each $\theset{\omega_f\geq1/k}$ is closed.
If $D_f = \RR\setminus\QQ$, then $\RR\setminus\QQ = \bigcup_k F_k$ with $F_k$ closed; each $F_k$ contains no rational, so has empty interior, and $\QQ = \bigcup_{q\in\QQ}\theset q$ together with the $F_k$ writes $\RR$ as a countable union of closed sets with empty interior, contradicting the Baire category theorem.

:::

## Uniform continuity

::: {.remark}
A function $f\colon\RR\to\RR$ is uniformly continuous if and only if $\norm{f(\wait+y)-f}_\infty \to 0$ as $y \to 0$.

:::

[[PR-SX6NO]]

[[T-O4UD3]]

::: {.proof}
Let $\varepsilon>0$.
For each $x\in X$ choose $\delta_x>0$ with $d_Y(f(x),f(y))<\varepsilon/2$ whenever $d(x,y)<\delta_x$.
The balls $B_{\delta_x/2}(x)$ cover $X$; choose a finite subcover by balls centered at $x_1,\ldots,x_m$ and let $\delta\coloneqq\min_i\delta_{x_i}/2$.
If $d(x,y)<\delta$, then $d(x,x_i)<\delta_{x_i}/2$ for some $i$, and $d(y,x_i)<\delta+\delta_{x_i}/2\leq\delta_{x_i}$, so $d_Y(f(x),f(y))\leq d_Y(f(x),f(x_i))+d_Y(f(x_i),f(y))<\varepsilon$.

:::

## Equicontinuity

[[D-2CCDB]]

[[FD-TGBYP]] [[FD-XVMEE]]

[[FF-63IWC]]

[[FF-XZGIY]]
