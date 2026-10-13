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
Let $a<b$, let $\alpha:[a,b]\to\mathbb R$ be increasing, and let $f:[a,b]\to\mathbb R$ be bounded. Prove that $f \in \mathcal{R}(\alpha)$ on $[a,b]$ if and only if, for any $a<c<b$, $f \in \mathcal{R}(\alpha)$ on $[a,c]$ and on $[c,b]$.
In addition, if either condition holds, then we have that $$\int_a^c fd\alpha + \int_c^b fd\alpha = \int_a^b fd\alpha.$$
:::
::: {.solution}

::: pf

::: {.pf-step #s1}

($\Rightarrow$) If $f \in \mathcal R(\alpha)$ on $[a,b]$ then $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$.

::: pf-proof

Fix $\varepsilon>0$. The Darboux criterion supplies a partition $Q$ of $[a,b]$ with $U(f,Q,\alpha)-L(f,Q,\alpha)<\varepsilon$. Refine $Q$ by inserting $c$ to obtain $P$. Since $\alpha$ is increasing, refinement does not increase the upper-minus-lower sum. The partition $P$ splits at $c$ into $P_1,P_2$, and
\[
0\leq D_\alpha(f,P_1)+D_\alpha(f,P_2)=D_\alpha(f,P)<\varepsilon,
\]
where $D_\alpha(f,Q)=U(f,Q,\alpha)-L(f,Q,\alpha)$. Both summands are nonnegative, so each is less than $\varepsilon$. The Darboux criterion proves integrability on both subintervals.

:::

:::

::: {.pf-step #s2}

($\Leftarrow$) If $f \in \mathcal R(\alpha)$ on $[a,c]$ and on $[c,b]$, then $f \in \mathcal R(\alpha)$ on $[a,b]$.

::: pf-proof

::: pf-step

Given $\eps > 0$, choose partitions $P_1$ of $[a,c]$ and $P_2$ of $[c,b]$ with $U(f,P_1,\alpha) - L(f,P_1,\alpha) < \eps/2$ and $U(f,P_2,\alpha) - L(f,P_2,\alpha) < \eps/2$.

::: pf-proof

Apply the Darboux criterion separately on $[a,c]$ and $[c,b]$.

:::

:::

::: {.pf-step #s2-2}

$P = P_1 \cup P_2$ is a partition of $[a,b]$ with $U(f,P,\alpha) - L(f,P,\alpha) < \eps$.

::: pf-proof

The upper and lower Stieltjes sums are additive under concatenation of partitions at $c$, since their terms are indexed by the subintervals. Hence $D_\alpha(f,P)=D_\alpha(f,P_1)+D_\alpha(f,P_2)<\varepsilon$.

:::

:::

::: pf-qed

Step [](#s2-2){.pf-ref} verifies the Darboux criterion on $[a,b]$.

:::

:::

:::

::: {.pf-step #s3}

Additivity: $\int_a^c f\,d\alpha + \int_c^b f\,d\alpha = \int_a^b f\,d\alpha$.

::: pf-proof

For every pair of tagged partitions $P_1,P_2$ of $[a,c]$ and $[c,b]$, their concatenation $P$ satisfies the exact identity $S_\alpha(f;P)=S_\alpha(f;P_1)+S_\alpha(f;P_2)$. Choose sequences of tagged partitions on both subintervals whose meshes tend to zero. Their concatenations also have mesh tending to zero. By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, all three integrals exist; taking limits in the sum identity proves the formula.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} establish both implications and additivity for every $c\in(a,b)$.

:::

:::

:::
