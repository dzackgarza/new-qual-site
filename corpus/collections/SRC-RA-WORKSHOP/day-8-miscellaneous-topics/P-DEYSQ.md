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
Let $a<b$, let $\alpha:[a,b]\to\RR$ be increasing, and let $f:[a,b]\to\RR$ be bounded. Prove that $f \in \mathcal{R}(\alpha)$ on $[a,b]$ if and only if, for any $a<c<b$, $f \in \mathcal{R}(\alpha)$ on $[a,c]$ and on $[c,b]$.
In addition, if either condition holds, then we have that $$\int_a^c fd\alpha + \int_c^b fd\alpha = \int_a^b fd\alpha.$$
:::

::: {.solution}

Fix $c\in(a,b)$. For a partition $Q$ of an interval, write $D_\alpha(f,Q)\coloneqq U(f,Q,\alpha)-L(f,Q,\alpha)$. If $P_1$ and $P_2$ are partitions of $[a,c]$ and $[c,b]$, their union $P$ is a partition of $[a,b]$, and the upper and lower sums are additive, $U(f,P,\alpha)=U(f,P_1,\alpha)+U(f,P_2,\alpha)$ and likewise for $L$, because their terms are indexed by the subintervals.

::: pf

::: {.pf-step #s1}

($\Rightarrow$) If $f \in \mathcal R(\alpha)$ on $[a,b]$ then $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$.

::: pf-proof

Fix $\varepsilon>0$. The Darboux criterion supplies a partition $Q$ of $[a,b]$ with $D_\alpha(f,Q)<\varepsilon$. Inserting $c$ into $Q$ gives a refinement $P$. Since $\alpha$ is increasing, refinement does not increase the upper-minus-lower sum. The partition $P$ splits at $c$ into $P_1,P_2$, and
$$
0\leq D_\alpha(f,P_1)+D_\alpha(f,P_2)=D_\alpha(f,P)<\varepsilon.
$$
Both summands are nonnegative, so each is less than $\varepsilon$. The Darboux criterion proves integrability on both subintervals.

:::

:::

::: {.pf-step #s2}

($\Leftarrow$) If $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$, then $f \in \mathcal R(\alpha)$ on $[a,b]$.

::: pf-proof

Given $\varepsilon > 0$, the Darboux criterion on $[a,c]$ and on $[c,b]$ supplies partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with $D_\alpha(f,P_1) < \varepsilon/2$ and $D_\alpha(f,P_2) < \varepsilon/2$. By additivity, $P = P_1 \cup P_2$ satisfies $D_\alpha(f,P)=D_\alpha(f,P_1)+D_\alpha(f,P_2)<\varepsilon$. This is the Darboux criterion on $[a,b]$.

:::

:::

::: pf-step

If either condition holds, $\int_a^c f\,d\alpha + \int_c^b f\,d\alpha = \int_a^b f\,d\alpha$.

::: pf-proof

By step [](#s1){.pf-ref} and step [](#s2){.pf-ref}, all three integrals exist. Given $\varepsilon>0$, choose $P_1,P_2$ as in the proof of step [](#s2){.pf-ref} and let $P=P_1\cup P_2$. Each integral lies between the lower and upper sums of its partition, so both $\int_a^c f\,d\alpha + \int_c^b f\,d\alpha$ and $\int_a^b f\,d\alpha$ lie in the interval
$$
\bigl[L(f,P_1,\alpha)+L(f,P_2,\alpha),\ U(f,P_1,\alpha)+U(f,P_2,\alpha)\bigr]=\bigl[L(f,P,\alpha),\ U(f,P,\alpha)\bigr],
$$
whose length is $D_\alpha(f,P)<\varepsilon$. Since $\varepsilon>0$ is arbitrary, the two quantities are equal.

:::

:::

:::

:::
