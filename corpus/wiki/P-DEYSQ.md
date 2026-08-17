---
schema: qual/card@1
id: P-DEYSQ
kind: problem
title: "Prove : $f \\in \\mathcal{R}(\\alpha)$ on $[a,b]$ if and"
classification:
  areas:
  - real-analysis
  topics:
  - riemann-integrability
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Prove : $f \in \mathcal{R}(\alpha)$ on $[a,b]$ if and only if for any $a <c<b$, $f \in \mathcal{R}(\alpha)$ on $[a,c]$ and on $[c,b]$.
In addition, if either condition holds, then we have that $$\int_a^c fd\alpha + \int_c^b fd\alpha = \int_a^b fd\alpha.$$
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. ($\Rightarrow$) If $f \in \mathcal R(\alpha)$ on $[a,b]$ then $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$.
Proof: given partitions $P_1, P_2$ of $[a,c], [c,b]$, their union $P$ is a partition of $[a,b]$ with $U(f,P,\alpha) - L(f,P,\alpha) = \big(U(f,P_1,\alpha) - L(f,P_1,\alpha)\big) + \big(U(f,P_2,\alpha) - L(f,P_2,\alpha)\big)$ (the $\alpha$-increments on the two subintervals add up to those on $[a,b]$; note $f$ is bounded on $[a,b]$ by integrability).
Since integrability on $[a,b]$ lets $U - L \to 0$ along such partitions, each subinterval's difference tends to $0$, giving integrability on each.

<1>2. ($\Leftarrow$) If $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$, then $f \in \mathcal R(\alpha)$ on $[a,b]$.
<2>1. Given $\eps > 0$, choose partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with $U(f,P_1,\alpha) - L(f,P_1,\alpha) < \eps/2$ and $U(f,P_2,\alpha) - L(f,P_2,\alpha) < \eps/2$.
Proof: integrability on each subinterval.
<2>2. $P = P_1 \cup P_2$ is a partition of $[a,b]$ with $U(f,P,\alpha) - L(f,P,\alpha) < \eps$.
Proof: the upper/lower sums split over the two subintervals as in <1>1 (the boundary point $c$ contributes its $\Delta\alpha$ to exactly one of the two sums), so $U - L = (U_1 - L_1) + (U_2 - L_2) < \eps$.
<2>3. Q.E.D. Proof: <2>2 shows $U - L$ can be made arbitrarily small, i.e. integrability on $[a,b]$ (Cauchy criterion).

<1>3. Additivity: $\int_a^c f\,d\alpha + \int_c^b f\,d\alpha = \int_a^b f\,d\alpha$.
Proof: for the partitions of <2>2, Riemann–Stieltjes sums satisfy $S(P) = S(P_1) + S(P_2)$; taking $P_1, P_2$ with mesh making all three sums converge to the respective integrals gives $\int_a^b = \int_a^c + \int_c^b$ (both sides are limits of the same telescoping sums).

<1>4. Q.E.D. Proof: <1>1, <1>2, <1>3 establish both directions and the additivity formula.
:::
