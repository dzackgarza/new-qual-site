---
schema: qual/card@1
id: P-BDFPC
kind: problem
title: Riemann–Stieltjes integral against a jump, and vanishing of $g$ against $x^{3k+2}$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Stone-Weierstrass
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 6 of the preserved UNL May 2016 qualifying-exam source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: "Corrected the Stieltjes partition argument: because alpha(0)=-1 and alpha(x)=1 for x>0, the nonzero increment is on the interval beginning at 0."
---

::: {.problem}
1. Suppose $f:[-1,1]\to\RR$ is bounded and continuous at $0$. Let
$$
\alpha(x)=
\begin{cases}
-1,&x\in[-1,0],\\
1,&x\in(0,1].
\end{cases}
$$
Prove that $f\in\mathcal R(\alpha)[-1,1]$ and
$$
\int_{-1}^1 f\,d\alpha=2f(0).
$$

2. Let $g:[0,1]\to\RR$ be continuous and suppose
$$
\int_0^1 g(x)x^{3k+2}\,dx=0
\qquad(k=0,1,2,\ldots).
$$
Prove that $g\equiv0$.
:::

::: {.solution}

::: pf

::: pf-step

(1) $f\in\mathcal R(\alpha)[-1,1]$ and $\boxed{\int_{-1}^1 f\,d\alpha=2f(0)}$.

::: pf-proof

The integrator $\alpha$ is nondecreasing, constant on $[-1,0]$ and on $(0,1]$, with $\alpha(0)=-1$ and $\alpha(x)=1$ for $x>0$.

Fix $\varepsilon>0$. By continuity of $f$ at $0$, choose $r\in(0,1)$ with $\abs{f(x)-f(0)}<\varepsilon/4$ for $0\le x\le r$. Let $P$ be any partition containing the points $-1<0<r<1$. Every increment of $\alpha$ over a subinterval of $P$ vanishes except the one over $[0,r]$, which is $\alpha(r)-\alpha(0)=2$. If $M$ and $m$ are the supremum and infimum of $f$ on $[0,r]$, then $M-m<\varepsilon/2$, so
$$
U(f,P,\alpha)-L(f,P,\alpha)=2(M-m)<\varepsilon.
$$
Thus $f\in\mathcal R(\alpha)[-1,1]$. Moreover $2m\le \int_{-1}^1f\,d\alpha\le2M$ and $f(0)-\varepsilon/4\le m\le M\le f(0)+\varepsilon/4$, so $\abs{\int_{-1}^1 f\,d\alpha-2f(0)}\le\varepsilon/2$ for every $\varepsilon>0$.

:::

:::

::: pf-step

(2) $\boxed{g\equiv0}$.

::: pf-proof

::: {.pf-step #moments}

$\int_0^1 g(x)x^2p(x^3)\,dx=0$ for every polynomial $p$.

::: pf-proof

$x^2p(x^3)$ is a finite linear combination of the functions $x^{3k+2}$, $k\ge0$, so this follows from the hypothesis by linearity.

:::

:::

::: pf-step

$\int_0^1 x^2 g(x)^2\,dx=0$, and therefore $g\equiv0$.

::: pf-proof

Let $h(t)\coloneqq g(t^{1/3})$ for $t\in[0,1]$. Then $h$ is continuous, so by the Weierstrass approximation theorem there are polynomials $p_n$ with $p_n\to h$ uniformly on $[0,1]$. Substituting $t=x^3$ gives $p_n(x^3)\to g(x)$ uniformly on $[0,1]$. Since $x^2g(x)$ is bounded, step [](#moments){.pf-ref} gives
$$
0=\lim_{n\to\infty}\int_0^1 g(x)x^2p_n(x^3)\,dx=\int_0^1x^2g(x)^2\,dx.
$$
The integrand is continuous and nonnegative, so it vanishes identically. Thus $g(x)=0$ for every $x\in(0,1]$, and continuity gives $g(0)=0$.

:::

:::

:::

:::

:::

:::
