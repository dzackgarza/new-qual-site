---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-10
kind: problem
title: Prove Theorem 5.3
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Riemann Integrability
relations:
- kind: uses
  target: T-RA-WORKSHOP-D6-5-3
review: draft
solved: true
---

::: {.problem title="?"}
(Essentially June 2013 #7) Prove Theorem 5.3.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Set up: $\alpha$ increasing, $\alpha' \in \mathcal{R}$ on $[a,b]$, $f$ bounded.
Proof: since $\alpha' \in \mathcal{R}$, $\alpha'$ is bounded, so $\alpha$ is Lipschitz (by the fundamental theorem of calculus for Riemann integrals, $\alpha(x) = \alpha(a) + \int_a^x \alpha'(t)\,dt$). In particular $\alpha$ is continuous and of bounded variation.
We prove the two implications.
<1>2. (⟹) If $f \in \mathcal{R}(\alpha)$ then $f\alpha' \in \mathcal{R}$ and $\int f\,d\alpha = \int f\alpha'$.
Proof: let $M = \sup|f|$.
For any partition $P = \{x_0 < \cdots < x_n\}$ and any choice of tags $t_i \in [x_{i-1}, x_i]$, write $m_i' = \inf_{[x_{i-1},x_i]}\alpha'$ and $M_i' = \sup_{[x_{i-1},x_i]}\alpha'$.
Since $\Delta\alpha_i = \int_{x_{i-1}}^{x_i}\alpha'$ (fundamental theorem for monotone functions) and $\int_{x_{i-1}}^{x_i}\alpha' \in [m_i'\Delta x_i,\ M_i'\Delta x_i]$, we have $|\Delta\alpha_i - \alpha'(t_i)\Delta x_i| \le (M_i' - m_i')\Delta x_i$.
Hence the Stieltjes sum and the Riemann sum of $f\alpha'$ with the same tags differ by \[\left|\sum_i f(t_i)\Delta\alpha_i - \sum_i f(t_i)\alpha'(t_i)\Delta x_i\right| \le M\sum_i (M_i' - m_i')\Delta x_i = M\big(U(\alpha',P) - L(\alpha',P)\big).\] Since $f \in \mathcal{R}(\alpha)$, Stieltjes sums converge to $\int f\,d\alpha$ along partitions with mesh $\to 0$; since $\alpha' \in \mathcal{R}$, $U(\alpha',P) - L(\alpha',P) \to 0$ along the same refinement.
So the Riemann sums $\sum f(t_i)\alpha'(t_i)\Delta x_i$ also converge, to $\int f\,d\alpha$.
Riemann sums converging to a common limit along partitions with mesh $\to 0$ is exactly Riemann integrability, so $f\alpha' \in \mathcal{R}$ and $\int f\alpha' = \int f\,d\alpha$.
<1>3. (⟸) If $f\alpha' \in \mathcal{R}$ then $f \in \mathcal{R}(\alpha)$ with the same value.
Proof: the same inequality of <1>2 shows that along any partition sequence with mesh $\to 0$, the Stieltjes sums $\sum f(t_i)\Delta\alpha_i$ are within $M\big(U(\alpha',P) - L(\alpha',P)\big) \to 0$ of the convergent Riemann sums of $f\alpha'$; hence the Stieltjes sums converge, to $\int_a^b f\alpha'$.
So $f \in \mathcal{R}(\alpha)$ and $\int f\,d\alpha = \int_a^b f\alpha'$.
<1>4. Q.E.D. Proof: both directions established: $f \in \mathcal{R}(\alpha)$ iff $f\alpha' \in \mathcal{R}$, and in that case the integrals agree.
:::
