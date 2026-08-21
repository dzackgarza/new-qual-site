---
schema: qual/card@1
id: P-RA19J5
kind: problem
title: UNL analysis qualifying exam, January 2019, problem 5
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Use the Riemann condition to show that $f\in\mathcal R_\alpha[0,4]$ where $f(x)=e^{2x}$ and
$$\alpha(x)=\begin{cases}
x+1,&0\le x\le2,\\
3x-2,&2<x\le4.
\end{cases}$$
Compute the value of the Riemann--Stieltjes integral
$$\int_0^4 f(x)\,d\alpha.$$
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Use the Riemann condition to show $f(x) = e^{2x} \in \mathcal R_\alpha[0,4]$ with the piecewise-linear $\alpha$, and compute $\int_0^4 f\,d\alpha$.

<1>1. $\alpha(x) = x+1$ on $[0,2]$ and $\alpha(x) = 3x - 2$ on $(2,4]$: continuous, and $\alpha' = 1$ on $(0,2)$, $\alpha' = 3$ on $(2,4)$.
    Proof: differentiate each piece; $\alpha$ is continuous at $2$: $2 + 1 = 3 = 3\cdot2 - 2$.

<1>2. $\int_0^4 f\,d\alpha = \int_0^4 f(x)\alpha'(x)\,dx$ (the reduction theorem for $C^1$ integrators).
    Proof: since $f$ is continuous (hence Riemann integrable) and $\alpha$ is $C^1$ except at the corner $x = 2$, the standard reduction $\int f\,d\alpha = \int f\alpha'$ holds on each interval of smoothness; the corner is a single point and contributes nothing (both $f$ and $\alpha$ are continuous at $2$). More precisely apply the theorem on $[0,2]$ and $[2,4]$ separately and add (additivity of RS integrals).

<1>3. $\int_0^4 e^{2x}\,d\alpha = \int_0^2 e^{2x}\cdot 1\,dx + \int_2^4 e^{2x}\cdot 3\,dx = \left[\frac{e^{2x}}{2}\right]_0^2 + 3\left[\frac{e^{2x}}{2}\right]_2^4 = \frac{e^4 - 1}{2} + \frac{3(e^8 - e^4)}{2} = \frac{3e^8 + 2e^4 - 1}{2}$.
    Proof: <1>2 and elementary integration.

<1>4. Riemann condition verification (the problem asks to "use the Riemann condition"):
    <2>1. The Riemann condition for RS integrability: for every $\varepsilon > 0$ there is a partition $P$ with $U(P, f, \alpha) - L(P, f, \alpha) < \varepsilon$.
    <2>2. $U - L \le \sum_i (M_i - m_i)\Delta\alpha_i$; on each of $[0,2]$ and $[2,4]$ where $\alpha'$ is constant, $\Delta\alpha_i = \alpha'\Delta x_i$, so $U - L = \sum(M_i - m_i)\alpha'\Delta x_i \le \max(1, 3)\sum(M_i - m_i)\Delta x_i$ — and $\sum(M_i - m_i)\Delta x_i \to 0$ by (ordinary) Riemann integrability of $f$ (continuous on a compact interval). Taking $\alpha' \le 3$ and $f$ continuous: $U - L \le 3\sum(M_i - m_i)\Delta x_i \to 0$.
        Proof: since $f$ is continuous on $[0,4]$, it is uniformly continuous, so with a fine enough partition each $(M_i - m_i)$ is small and $\sum(M_i-m_i)\Delta x_i < \varepsilon/3$; hence $U - L < \varepsilon$: the Riemann condition holds.
    <2>3. Q.E.D.
        Proof: <2>2 verifies the Riemann condition, so $f \in \mathcal R_\alpha[0,4]$; <1>3 computes the value.

:::
