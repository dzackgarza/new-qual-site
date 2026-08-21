---
schema: qual/card@1
id: P-COY2N
kind: problem
title: $\sup_{\|g\|_1\le 1}\|fg\|_1=\|f\|_\infty$ for continuous $f$ on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Norms
  - Lp Spaces
relations: []
review: draft
solved: true
---

::: problem
Let $f: [0, 1] \to \RR$ be continuous.
Show that
\[
\sup \left\{\|f g\|_{1} \suchthat g \in L^{1}[0,1],~~ \|g\|_{1} \leq 1\right\}=\|f\|_{\infty}
\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. For every $g \in L^1[0,1]$ with $\|g\|_1 \le 1$: $\|fg\|_1 \le \|f\|_\infty$.
Proof: $|f(x)g(x)| \le \|f\|_\infty |g(x)|$ a.e., so $\|fg\|_1 \le \|f\|_\infty \|g\|_1 \le \|f\|_\infty$.

<1>2. Hence $\sup_{\|g\|_1 \le 1}\|fg\|_1 \le \|f\|_\infty$.
Proof: <1>1 holds for every admissible $g$.

<1>3. $f$ attains its maximum modulus: there is $x_0 \in [0,1]$ with $|f(x_0)| = \|f\|_\infty$.
Proof: $f$ is continuous on the compact interval $[0,1]$.

<1>4. Given $\eps > 0$, there is an interval $I \subseteq [0,1]$ of positive length on which $|f(x)| \ge \|f\|_\infty - \eps$.
Proof: continuity at $x_0$ (<1>3): choose $\delta$ with $|x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| < \eps$, and let $I$ be a small interval around $x_0$ (intersected with $[0,1]$); then $|f(x)| \ge |f(x_0)| - \eps = \|f\|_\infty - \eps$.

<1>5. $\sup_{\|g\|_1 \le 1}\|fg\|_1 \ge \|f\|_\infty$.
Proof: take $g = \chi_I / m(I)$; then $\|g\|_1 = 1$ and $\|fg\|_1 = \dfrac{1}{m(I)}\int_I |f| \ge \|f\|_\infty - \eps$; letting $\eps \to 0$ gives the claim.

<1>6. Q.E.D. Proof: <1>2 and <1>5 sandwich the sup between $\|f\|_\infty - \eps$ (all $\eps$) and $\|f\|_\infty$, so it equals $\|f\|_\infty$.
:::
