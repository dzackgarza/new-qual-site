---
schema: qual/card@1
id: E-SS6.EX-16
kind: problem
title: "Another proof of the analytic continuation of the zeta function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
16. Use the previous exercise to give another proof that $\zeta ( s )$ is continuable in the complex plane with only singularity a simple pole at $s = 1$

[Hint: Write

$$
\zeta (s) = \frac {1}{\Gamma (s)} \int_ {0} ^ {1} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x + \frac {1}{\Gamma (s)} \int_ {1} ^ {\infty} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x.
$$

The second integral defines an entire function, while

$$
\int_ {0} ^ {1} \frac {x ^ {s - 1}}{e ^ {x} - 1} d x = \sum_ {m = 0} ^ {\infty} \frac {B _ {m}}{m ! (s + m - 1)},
$$

where $B _ { m }$ denotes the $m ^ { \mathrm { t h } }$ Bernoulli number defined by

$$
{\frac {x}{e ^ {x} - 1}} = \sum_ {m = 0} ^ {\infty} {\frac {B _ {m}}{m !}} x ^ {m}.
$$

Then $B _ { 0 } = 1$ , and since $z / ( e ^ { z } - 1 )$ is holomorphic for $| z | < 2 \pi$ , we must have lim s $\begin{array} { r } { \operatorname * { l p } _ { m  \infty } | B _ { m } / m ! | ^ { 1 / m } = 1 / 2 \pi . ] } \end{array}$
:::

::: solution
Split
\[
\Gamma(s)\zeta(s)
=\int_0^1\frac{x^{s-1}}{e^x-1}\,dx
+\int_1^\infty\frac{x^{s-1}}{e^x-1}\,dx.
\tag{1}
\]
The second integral defines an entire function of $s$, because on every compact set in the $s$-plane its integrand is dominated by $C x^N e^{-x}$ for large $x$.

Write
\[
h(x)=\frac{x}{e^x-1}=\sum_{m=0}^\infty \frac{B_m}{m!}x^m,
\qquad |x|<2\pi.
\]
Fix $N\ge0$. Then near $0$,
\[
h(x)=\sum_{m=0}^N\frac{B_m}{m!}x^m+x^{N+1}r_N(x),
\]
where $r_N$ is holomorphic near $[0,1]$. Hence
\[
\int_0^1\frac{x^{s-1}}{e^x-1}\,dx
=\int_0^1 x^{s-2}h(x)\,dx
=\sum_{m=0}^N\frac{B_m}{m!(s+m-1)}+H_N(s),
\tag{2}
\]
where $H_N$ is holomorphic for $\Re s>-N$.

Multiplying (1) and (2) by $1/\Gamma(s)$ therefore extends $\zeta(s)$ meromorphically to $\Re s>-N$. Since $N$ is arbitrary, this gives a meromorphic continuation to all of $\mathbb C$.

The possible poles arising from (2) occur at
\[
s=1-m\qquad(m=0,1,2,\ldots).
\]
For $m\ge1$, these are nonpositive integers, and $1/\Gamma(s)$ has a simple zero there, so those poles cancel. At $s=1$, the $m=0$ term is $1/(s-1)$ because $B_0=1$, and $1/\Gamma(1)=1$, so the pole survives and is simple, with residue $1$.

Thus $\zeta$ continues meromorphically to $\mathbb C$ with exactly one singularity, a simple pole at $s=1$.
:::
