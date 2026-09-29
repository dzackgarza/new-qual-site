---
schema: qual/card@1
id: P-DEYSQ
kind: problem
title: Riemann-Stieltjes integrability and additivity across a subdivision point
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
---

::: {.problem}
Prove : $f \in \mathcal{R}(\alpha)$ on $[a,b]$ if and only if for any $a <c<b$, $f \in \mathcal{R}(\alpha)$ on $[a,c]$ and on $[c,b]$.
In addition, if either condition holds, then we have that $$\int_a^c fd\alpha + \int_c^b fd\alpha = \int_a^b fd\alpha.$$
:::
::: {.solution}
::: pf

::: {.pf-step #s1}
($\Rightarrow$) If $f \in \mathcal R(\alpha)$ on $[a,b]$ then $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$.

::: pf-proof
given partitions $P_1, P_2$ of $[a,c], [c,b]$, their union $P$ is a partition of $[a,b]$ with $U(f,P,\alpha) - L(f,P,\alpha) = \big(U(f,P_1,\alpha) - L(f,P_1,\alpha)\big) + \big(U(f,P_2,\alpha) - L(f,P_2,\alpha)\big)$ (the $\alpha$-increments on the two subintervals add up to those on $[a,b]$; note $f$ is bounded on $[a,b]$ by integrability).

Since integrability on $[a,b]$ lets $U - L \to 0$ along such partitions, each subinterval's difference tends to $0$, giving integrability on each.
:::

:::

::: {.pf-step #s2}
($\Leftarrow$) If $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$, then $f \in \mathcal R(\alpha)$ on $[a,b]$.

::: pf-proof

::: pf-step
Given $\eps > 0$, choose partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with $U(f,P_1,\alpha) - L(f,P_1,\alpha) < \eps/2$ and $U(f,P_2,\alpha) - L(f,P_2,\alpha) < \eps/2$.

::: pf-proof
integrability on each subinterval.
:::

:::

::: {.pf-step #s2-2}
$P = P_1 \cup P_2$ is a partition of $[a,b]$ with $U(f,P,\alpha) - L(f,P,\alpha) < \eps$.

::: pf-proof
the upper/lower sums split over the two subintervals as in step [](#s1){.pf-ref} (the boundary point $c$ contributes its $\Delta\alpha$ to exactly one of the two sums), so $U - L = (U_1 - L_1) + (U_2 - L_2) < \eps$.
:::

:::

::: pf-qed
Step [](#s2-2){.pf-ref} shows $U - L$ can be made arbitrarily small, i.e. integrability on $[a,b]$ (Cauchy criterion).
:::

:::

:::

::: {.pf-step #s3}
Additivity: $\int_a^c f\,d\alpha + \int_c^b f\,d\alpha = \int_a^b f\,d\alpha$.

::: pf-proof
for the partitions of step [](#s2-2){.pf-ref}, Riemann–Stieltjes sums satisfy $S(P) = S(P_1) + S(P_2)$; taking $P_1, P_2$ with mesh making all three sums converge to the respective integrals gives $\int_a^b = \int_a^c + \int_c^b$ (both sides are limits of the same telescoping sums).
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} establish both directions and the additivity formula.
:::

:::
:::
