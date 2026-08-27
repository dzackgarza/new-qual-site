---
schema: qual/card@1
id: P-PQG5I
kind: problem
title: Compactness of $\{x\in\ell^2:\sum n|x_n|^2\le 1\}$ and attainment of $\int_0^{2\pi}\bigl|\sum
  x_n e^{in\theta}\bigr|\frac{d\theta}{2\pi}$ on this set
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Compactness
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Let $$A = \left\{x\in\ell^2: \sum_{n\ge1} n|x_n|^2 \le 1\right\}.$$

a. Show that $A$ is compact in the $\ell^2$ topology.

b. Show that the mapping from $A$ to $\mathbb{R}$ defined by $$x \mapsto \int_0^{2\pi} \left|\sum_{n\ge1} x_n e^{in\theta}\right| \frac{d\theta}{2\pi}$$ achieves its maximum on $A$.
:::

:::: {.solution}
<1>1. (a) $A$ is closed in $\ell^2$.
Proof: let $x^{(k)} \to x$ in $\ell^2$ with $x^{(k)} \in A$.
For every $N$, \[\sum_{n=1}^N n|x_n|^2 = \lim_{k\to\infty}\sum_{n=1}^N n|x_n^{(k)}|^2 \le \limsup_{k\to\infty}\sum_{n\ge1} n|x_n^{(k)}|^2 \le 1,\] and letting $N \to \infty$ (monotone convergence) gives $\sum_{n\ge1}n|x_n|^2 \le 1$, so $x \in A$.
<1>2. (a) $A$ is totally bounded.
Proof: fix $\epsilon > 0$ and choose $N$ with $1/(N+1) < \epsilon^2/4$.
For $x \in A$, the tail satisfies \[\sum_{n>N}|x_n|^2 \le \frac{1}{N+1}\sum_{n>N}n|x_n|^2 \le \frac{1}{N+1} < \frac{\epsilon^2}{4},\] so $\left(\sum_{n>N}|x_n|^2\right)^{1/2} < \epsilon/2$.
The head $(x_1,\ldots,x_N)$ ranges over the bounded set $\{u \in \mathbb{R}^N : \sum n u_n^2 \le 1\}$ in $\mathbb{R}^N$, which is compact, hence covered by finitely many $\epsilon/2$-balls.
Lifting those balls to $\ell^2$ (varying only the first $N$ coordinates) gives a finite $\epsilon$-net for $A$.
Since $\ell^2$ is complete, closed + totally bounded $\implies$ compact.
<1>3. (b) The functional $\Phi(x) = \int_0^{2\pi}\left|\sum_{n\ge1}x_ne^{in\theta}\right|\frac{d\theta}{2\pi}$ is continuous on $\ell^2$.
Proof: for $x \in \ell^2$, $g_x(\theta) = \sum_n x_ne^{in\theta}$ is an $L^2$ function on the circle (its Fourier coefficients are $x_n$), and by Parseval $\|g_x\|_{L^2} = \|x\|_{\ell^2}$.
By the reverse triangle inequality followed by Cauchy–Schwarz on the probability space $(\mathbb{T}, d\theta/2\pi)$, \[|\Phi(x) - \Phi(y)| \le \int\big||g_x| - |g_y|\big|\frac{d\theta}{2\pi} \le \int|g_x - g_y|\frac{d\theta}{2\pi} \le \left(\int|g_x - g_y|^2\frac{d\theta}{2\pi}\right)^{1/2} = \|x - y\|_{\ell^2},\] so $\Phi$ is 1-Lipschitz, hence continuous.
<1>4. (b) $\Phi$ attains its maximum on $A$.
Proof: $\Phi$ is continuous and $A$ is compact (<1>1, <1>2); a continuous function on a compact set attains its maximum.
<1>5. Q.E.D.
:::
