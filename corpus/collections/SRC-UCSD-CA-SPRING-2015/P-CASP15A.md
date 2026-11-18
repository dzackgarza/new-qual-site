---
schema: qual/card@1
id: P-CASP15A
kind: problem
title: 'Classical complex-analysis theorems: statements and proof sketches'
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy's Theorem
  - Cauchy Integral Formula
  - Morera
  - Liouville's Theorem
  - Casorati-Weierstrass
  - Open Mapping Theorem
  - Maximum Principle
  - Residue Theorem
  - Argument Principle
  - Weierstrass Theorem
  - Hurwitz
  - Reflection Principle
  - Riemann Mapping Theorem
relations: []
review: draft
---

::: {.problem}
Pick four of the following results from the course and state them clearly ($5$ points each).
Then pick two of those four results and sketch their proofs ($10$ points each).

Cauchy's Theorem; Cauchy's integral formula; Morera's Theorem; Liouville's Theorem; Casorati-Weierstrass; Open mapping theorem; Maximum principle; Residue Theorem; Argument Principle; Weierstrass' Theorem; Hurwitz's Theorem; Reflection Principle; Riemann Mapping Theorem.
:::

::: {.solution}

The four statements are the standard ones and are quoted as the exercise asks; the two sketches are the card's own write-ups.

This is a different examination question from the one on [[P-CAFA15A]]: the candidate list here has thirteen entries, adding the maximum principle to the twelve of the Fall 2015 paper, and the four results chosen are different.

::: pf

::: {.pf-step #cauchy}
Statement, Cauchy's theorem. If $G$ is a simply connected domain and $f\in H(G)$, then $\int_{\gamma}f(z)\,dz=0$ for every closed piecewise $C^{1}$ curve $\gamma$ in $G$.

::: pf-proof
Quoted, as asked. Simple connectivity of $G$ is the hypothesis that cannot be dropped — on the punctured plane $\int_{\abs z=1}dz/z=2\pi i\ne0$ — and the curves range over the closed piecewise $C^{1}$ ones, for which the integral is defined.
:::

:::

::: {.pf-step #morera}
Statement, Morera's theorem. If $f$ is continuous on a domain $G$ and $\int_{\partial T}f(z)\,dz=0$ for every triangle $T$ with $\overline T\subset G$, then $f$ is holomorphic on $G$.

::: pf-proof
Quoted, as asked. Continuity is a hypothesis; every triangle whose closure lies in $G$ is required, with its positively oriented boundary.
:::

:::

::: {.pf-step #liouville}
Statement, Liouville's theorem. Every bounded entire function is constant.

::: pf-proof
Quoted, as asked. Both hypotheses are needed: $e^{z}$ is entire and unbounded, $1/(1+z^{2})$ is bounded on $\CC$ and not entire.
:::

:::

::: {.pf-step #riemann}
Statement, the Riemann mapping theorem. Every nonempty simply connected proper domain $G\subsetneq\CC$ is conformally equivalent to the unit disk.

::: pf-proof
Quoted, as asked. "Proper" excludes $G=\CC$, which is simply connected and not conformally equivalent to $\DD$ because a conformal equivalence would be a bounded entire function with bounded inverse.
:::

:::

::: {.pf-step #sketch-morera}
Sketch of Morera's theorem: a primitive on each disc, whose derivative is $f$.

::: pf-proof
Let $D\Subset G$ be a disc and $z_{0}\in D$. Define $F(z)=\int_{[z_{0},z]}f(\zeta)\,d\zeta$ along the segment, which lies in $D$. The hypothesis that the integral over every triangle boundary vanishes gives, by induction on the number of sides, that the integral over every closed polygonal path in $G$ vanishes, so the integral defining $F(z)$ does not depend on the polygonal path from $z_{0}$ to $z$ in $D$. Hence for $z,z+h\in D$
$$
F(z+h)-F(z)=\int_{[z,z+h]}f(\zeta)\,d\zeta,
$$
and by continuity of $f$ at $z$,
$$
\frac{F(z+h)-F(z)}{h}=\frac{1}{h}\int_{[z,z+h]}\big(f(\zeta)-f(z)\big)d\zeta+f(z)\longrightarrow f(z)
$$
as $h\to0$, the integral being bounded by $\sup_{\zeta\in[z,z+h]}\abs{f(\zeta)-f(z)}\to0$. So $F'=f$ on $D$; a holomorphic function has a holomorphic derivative, so $f$ is holomorphic on $D$, and $D$ was an arbitrary disc inside $G$. Every point of $G$ lies in such a disc, so $f\in H(G)$.
:::

:::

::: {.pf-step #sketch-liouville}
Sketch of Liouville's theorem: Cauchy's estimate bounds $f'(a)$ by $M/R$ with $R$ arbitrary.

::: pf-proof
Let $f$ be entire with $\abs f\le M$ on $\CC$ and fix $a\in\CC$. For every $R>0$, differentiating Cauchy's integral formula on the circle $\abs{\zeta-a}=R$ gives
$$
f'(a)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{(\zeta-a)^{2}}\,d\zeta,\qquad\text{so}\qquad \abs{f'(a)}\le\frac{1}{2\pi}\cdot\frac{M}{R^{2}}\cdot2\pi R=\frac{M}{R}.
$$
Letting $R\to\infty$ gives $f'(a)=0$. As $a$ was arbitrary, $f'$ vanishes on the connected set $\CC$, so $f$ is constant.
:::

:::

:::
:::
