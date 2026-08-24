---
schema: qual/card@1
id: P-RAF20E
kind: problem
title: "A measure dominated by the L^2 norm has Holder-continuous density"
classification:
  areas:
  - real-analysis
  topics:
  - Radon-Nikodym Theorem
  - Holder Continuity
  - Borel Measures
relations: []
review: draft
---

::: problem
Let $\mu$ be a (positive) Borel measure on $[0, 1]$ and denote by $m$ the Lebesgue measure.
Assume
$$
\left|\int_{[0,1]} f \, d\mu\right| \leq \left(\int_{[0,1]} |f|^2 \, dm\right)^{1/2} \quad \forall f \in C^1([0, 1]).
$$

Prove the following:

(1) $\mu \ll m$;

(2) If $u = d\mu/dm \in L^1(m)$ is the Radon–Nikodym derivative of $\mu$ with respect to $m$, then
$$
|u(x) - u(y)| \leq |x - y|^{1/2} \quad \text{for a.e. } x, y \in [0, 1].
$$
:::
