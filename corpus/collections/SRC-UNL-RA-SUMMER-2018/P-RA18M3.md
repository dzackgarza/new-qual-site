---
schema: qual/card@1
id: P-RA18M3
kind: problem
title: Riemann-Stieltjes integration against a step integrator on $[-2,2]$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 3 of the preserved UNL May 31, 2018 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced the mesh-limit discussion by the correct refinement criterion for a discontinuous Riemann--Stieltjes integrator.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Corrected and restructured. The card concluded f in R(alpha) with integral equal to 9, which
    is false. Since alpha is constant on [-1,0] and on (0,1], every Riemann-Stieltjes sum on
    [-1,1] collapses to the single term 3 f(tau) where tau is the tag on the subinterval
    containing 0; that term is -3 for a tag to the left and 9 for a tag to the right, so the
    sums do not converge and the integral does not exist. The card's earlier reasoning evidently
    kept the tags to the right of 0 without noticing that the same partition admits tags on the
    other side. The answer is now 'not integrable', the question's own alternative; the
    statement is unchanged. Not claimed: a retained solution set; the collection's provenance is
    the course, and the argument is the card's own.
---

::: {.problem}
Define $f,\alpha\in\mathcal B([-2,2])$ by
$$
f(x):=\begin{cases}
-1,&x\in[-2,0),\\
3,&x\in[0,2],
\end{cases}
\qquad
\alpha(x):=\begin{cases}
-2,&x\in[-2,0],\\
1,&x\in(0,2].
\end{cases}
$$
Determine whether $f$ is Riemann--Stieltjes integrable with respect to $\alpha$ over $[-1,1]$.
If it is, evaluate $$\int_{-1}^{1}f(x)\,d\alpha(x).$$
:::

:::: {.solution}
Throughout $f, \alpha \in \mathcal{B}([-2,2])$ are as in the problem, and both are considered on $[-1,1]$; a Riemann--Stieltjes sum for a partition $P = \theset{x_{0} < \cdots < x_{n}}$ with tags $\tau_{i} \in [x_{i-1}, x_{i}]$ is $S(P, \tau) \coloneqq \sum_{i}f(\tau_{i})\bigl(\alpha(x_{i}) - \alpha(x_{i-1})\bigr)$, and $f \in \mathcal{R}(\alpha)$ means these sums converge as the mesh tends to $0$. The collection's `provenance` is the UNL summer 2018 analysis course, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #jump}
On $[-1,1]$ the function $\alpha$ equals $-2$ on $[-1,0]$ and $1$ on $(0,1]$, so for every partition $P$ exactly one increment is nonzero: $\alpha(x_{i}) - \alpha(x_{i-1}) = 3$ for the unique $i$ with $x_{i-1} \le 0 < x_{i}$, and $0$ for every other $i$.

::: pf-proof
$\alpha$ is constant on each of the two intervals $[-1,0]$ and $(0,1]$, so an increment vanishes unless the subinterval $[x_{i-1}, x_{i}]$ meets both, which happens exactly when $x_{i-1} \le 0 < x_{i}$; that index is unique because the $x_{i}$ increase. For it, $\alpha(x_{i}) - \alpha(x_{i-1}) = 1 - (-2) = 3$, using $x_{i-1} \le 0$ and $x_{i} > 0$.

:::

:::

::: {.pf-step #sums}
Every Riemann--Stieltjes sum on $[-1,1]$ has the form $3f(\tau)$ with $\tau \in [x_{i-1}, x_{i}]$ the tag on the subinterval containing $0$; in particular it equals $-3$ when $\tau < 0$ and $9$ when $\tau \ge 0$.

::: pf-proof
By step [](#jump){.pf-ref} all terms of $S(P,\tau)$ vanish except the one indexed by the subinterval meeting both sides of $0$, and that term is $f(\tau)\cdot 3$. Since $f = -1$ on $[-1,0)$ and $f = 3$ on $[0,1]$, the value is $-3$ for a tag to the left of $0$ and $9$ for a tag at or to the right of $0$.

:::

:::

::: pf-step
$f \notin \mathcal{R}(\alpha)$ on $[-1,1]$: the Riemann--Stieltjes integral does not exist, so there is no value to evaluate.

::: pf-proof
Fix a partition as in step [](#jump){.pf-ref} and tag its distinguished subinterval first at a point $\tau^{-} < 0$ and then at a point $\tau^{+} \ge 0$; both are legitimate choices of tag for the same partition, and by step [](#sums){.pf-ref} the corresponding sums differ by $9 - (-3) = 12$. The Cauchy criterion for convergence of Riemann--Stieltjes sums therefore fails: there is $\varepsilon = 6 > 0$ such that no partition has all its sums within $\varepsilon$ of one another, while any limit would force the sums to become arbitrarily close. Hence $f \notin \mathcal{R}(\alpha)$. The failure is exactly the common discontinuity of $f$ and $\alpha$ at $0$, which is the obstruction in the Riemann--Stieltjes integrability criterion.

:::

:::

:::
:::
