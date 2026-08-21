---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W1
kind: problem
title: Products of bounded Riemann-integrable functions
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
([KRD10, 6.4.N]) If $f$ and $g$ are bounded on $[a,b]$ and both are Riemann integrable on $[a,b]$, show that $fg\in\mathcal R$ on $[a,b]$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to squares and sums.
Proof: the identity $fg = \frac14\big((f+g)^2 - (f-g)^2\big)$ reduces the claim to: $\mathcal{R}$ is closed under addition (and scalar multiplication), and $h \in \mathcal{R} \implies h^2 \in \mathcal{R}$.
<1>2. $\mathcal{R}$ is a vector space.
Proof: for $f, g \in \mathcal{R}$ and a partition $P$, the oscillation bound $\mathrm{osc}_{[x_{i-1},x_i]}(f+g) \le \mathrm{osc}_{[x_{i-1},x_i]}(f) + \mathrm{osc}_{[x_{i-1},x_i]}(g)$ gives $U_{f+g}(P) - L_{f+g}(P) \le \big(U_f(P) - L_f(P)\big) + \big(U_g(P) - L_g(P)\big)$, which tends to $0$ along a suitable sequence of partitions; scalar multiples are immediate.
Hence $f+g, cf \in \mathcal{R}$.
<1>3. $h \in \mathcal{R}$ bounded implies $h^2 \in \mathcal{R}$.
Proof: let $|h| \le M$.
For $u, v$ in an interval, $|h(u)^2 - h(v)^2| = |h(u) - h(v)||h(u) + h(v)| \le 2M|h(u) - h(v)|$, so $\mathrm{osc}(h^2) \le 2M\,\mathrm{osc}(h)$ on every subinterval; hence $U_{h^2}(P) - L_{h^2}(P) \le 2M\big(U_h(P) - L_h(P)\big) \to 0$.
So $h^2 \in \mathcal{R}$.
<1>4. Conclude.
Proof: $f+g, f-g \in \mathcal{R}$ (<1>2), so $(f+g)^2, (f-g)^2 \in \mathcal{R}$ (<1>3), and $fg = \frac14[(f+g)^2 - (f-g)^2] \in \mathcal{R}$.
<1>5. Q.E.D.
:::
