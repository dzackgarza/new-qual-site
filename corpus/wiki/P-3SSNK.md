---
schema: qual/card@1
id: P-3SSNK
kind: problem
title: Riemann–Stieltjes integral against a jump at $0$
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
  - Continuity
relations: []
review: draft
solved: true
---

::: problem
(June 2014 1)Define $\alpha \colon [-1,1] \to \mathbb{R}$ by $$\alpha(x) := \begin{cases} -1 & x \in [-1,0] \\ 1 & x \in (0,1]. \end{cases}$$ Let $f \colon [-1,1] \to \mathbb{R}$ be a function that is uniformly bounded on $[-1,1]$ and continuous at $x=0$, but not necessarily continuous for $x \neq 0$.
Prove that $f$ is Riemann-Stieltjes integrable with respect to $\alpha$ over $[-1,1]$ and that $$\int_{-1}^1 f(x)d\alpha(x) = 2f(0).$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $\alpha$ has bounded variation and is constant on each side of its single jump at $0$: $\alpha \equiv -1$ on $[-1,0]$ and $\alpha \equiv 1$ on $(0,1]$, with jump $\alpha(0+) - \alpha(0-) = 2$.
Proof: definition of $\alpha$; the value $\alpha(0)$ is irrelevant to the Stieltjes integral.

<1>2. $f$ is bounded and continuous at $0$; let $|f| \le M$.
Proof: hypothesis.

<1>3. For any partition $P$ with $0$ as a partition point, the Stieltjes sum depends only on the interval containing $0$.
Proof: on intervals where $\alpha$ is constant, the $\alpha$-increment is $0$, so those terms contribute nothing to $\sum f(t_i)\Delta\alpha_i$.

<1>4. Given $\eps > 0$, choose $\delta > 0$ with $|f(x) - f(0)| < \eps$ for $|x - 0| < \delta$ (continuity at $0$); then for any partition containing $0$ whose interval around $0$ has length $< \delta$: <2>1. The upper and lower Stieltjes sums satisfy $U(P) - L(P) \le 2\eps$ (the jump is $2$). Proof: the only contributing interval $[x_j, x_{j+1}] \ni 0$ has $\Delta\alpha = 2$ and oscillation of $f$ on it $\le 2\eps$; every other interval has $\Delta\alpha = 0$.
<2>2. Hence $f$ is Riemann–Stieltjes integrable with respect to $\alpha$.
Proof: the Riemann–Stieltjes criterion: $U(P) - L(P)$ can be made arbitrarily small by refining the partition.

<1>5. $\int_{-1}^1 f\,d\alpha = 2f(0)$.
Proof: for partitions as in <1>4, $\sum f(t_i)\Delta\alpha_i = f(t)(\alpha(0+) - \alpha(0-)) = 2f(t)$ for some $t$ in the interval around $0$, and $|f(t) - f(0)| < \eps$, so the sums converge to $2f(0)$ as the mesh tends to $0$.
:::
