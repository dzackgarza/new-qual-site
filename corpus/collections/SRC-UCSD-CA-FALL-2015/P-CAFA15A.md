---
schema: qual/card@1
id: P-CAFA15A
kind: problem
title: 'Classical complex-analysis theorems: statements and proof sketches'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Pick four of the following results from the course and state them clearly.
Then pick two of those four results and sketch their proofs.

- Cauchy's Theorem

- Cauchy's Integral Formula

- Morera's Theorem

- Liouville's Theorem

- Casorati–Weierstrass

- Open Mapping Theorem

- Residue Theorem

- Argument Principle

- Weierstrass' Theorem

- Hurwitz's Theorem

- Reflection Principle

- Riemann Mapping Theorem
:::

::: {.solution}

The four statements are the standard ones and are quoted as the exercise asks; the two sketches are the card's own write-ups of the usual arguments, and the one theorem the second sketch borrows (Rouché's theorem) is named as borrowed, since it is not among the four stated here.

::: pf

::: {.pf-step #cauchy-formula}
Statement, Cauchy's integral formula. If $f$ is holomorphic on a neighbourhood of the closed disc $\overline{B(a,R)}$, then for every $z\in B(a,R)$
$$
f(z)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{\zeta-z}\,d\zeta,
$$
the circle being traversed positively.

::: pf-proof
Quoted, as asked. The hypothesis is holomorphy on a neighbourhood of the *closed* disc, which is what makes $f$ continuous on the circle and lets the integral be taken; the point $z$ must lie in the open disc, so that $\zeta\mapsto f(\zeta)/(\zeta-z)$ has no singularity on the contour.
:::

:::

::: {.pf-step #morera}
Statement, Morera's theorem. If $f$ is continuous on a domain $\Omega$ and $\int_{\partial T}f(z)\,dz=0$ for every triangle $T$ whose closure lies in $\Omega$, then $f$ is holomorphic on $\Omega$.

::: pf-proof
Quoted, as asked. Continuity is a hypothesis; the triangles range over all closed triangles contained in $\Omega$, each with its positively oriented boundary.
:::

:::

::: {.pf-step #liouville}
Statement, Liouville's theorem. Every bounded entire function is constant.

::: pf-proof
Quoted, as asked. Both hypotheses are needed: entire means holomorphic on all of $\CC$, and bounded means $\abs{f}\le M$ for some finite $M$ on all of $\CC$; $e^{z}$ is entire and unbounded, $1/(1+z^{2})$ is bounded on $\CC$ but not entire.
:::

:::

::: {.pf-step #open-mapping}
Statement, the open mapping theorem. If $f$ is nonconstant and holomorphic on a domain $\Omega$, then $f(\Omega)$ is open.

::: pf-proof
Quoted, as asked. The domain is nonempty, open and connected, and nonconstancy is essential: a constant map has image a single point, which is not open.
:::

:::

::: {.pf-step #sketch-liouville}
Sketch of Liouville's theorem: Cauchy's estimate bounds $f'(a)$ by $M/R$, and $R$ is arbitrary.

::: pf-proof
Let $f$ be entire with $\abs{f}\le M$ on $\CC$, and fix $a\in\CC$. For every $R>0$ the closed disc $\overline{B(a,R)}$ lies in $\CC$ and $f$ is holomorphic on a neighbourhood of it, so step [](#cauchy-formula){.pf-ref} applies on the circle $\abs{\zeta-a}=R$. Differentiating the integral formula with respect to $z$ under the integral sign gives $f'(a)=\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{(\zeta-a)^{2}}d\zeta$, and estimating the integral gives
$$
\abs{f'(a)}=\abs{\frac{1}{2\pi i}\int_{\abs{\zeta-a}=R}\frac{f(\zeta)}{(\zeta-a)^{2}}\,d\zeta}\le\frac{1}{2\pi}\cdot\frac{M}{R^{2}}\cdot2\pi R=\frac{M}{R}.
$$
Since $M$ is fixed and $R$ can be taken arbitrarily large, $\abs{f'(a)}=0$. So $f'$ vanishes identically on the connected set $\CC$, and $f$ is constant.
:::

:::

::: {.pf-step #sketch-open-mapping}
Sketch of the open mapping theorem: the local normal form plus Rouché's theorem about the boundary circle.

::: pf-proof
Let $a\in\Omega$. Since $f$ is nonconstant and holomorphic, $f(z)-f(a)$ has a zero of finite order $m\ge1$ at $a$, so $f(z)-f(a)=(z-a)^{m}g(z)$ with $g$ holomorphic near $a$ and $g(a)\ne0$. Because $g(a)\ne0$, there is $r>0$ with $\overline{B(a,r)}\subset\Omega$ and $g$ zero-free on it; then $f(z)-f(a)$ vanishes on that disc only at $z=a$. On the circle $\abs{z-a}=r$ the continuous function $\abs{f(z)-f(a)}$ therefore attains a minimum $\eta>0$. If $\abs{w-f(a)}<\eta$, then on the boundary circle
$$
\abs{(f(z)-f(a))-(f(z)-w)}=\abs{w-f(a)}<\eta\le\abs{f(z)-f(a)},
$$
so the hypothesis of Rouché's theorem holds with $f(z)-f(a)$ in place of $f$ and $f(a)-w$ in place of $g$. Rouché's theorem — borrowed here, as it is not among the four results stated — gives that $f(z)-w$ has in $B(a,r)$ as many zeros as $f(z)-f(a)$, namely $m\ge1$. So $w=f(z)$ for some $z\in B(a,r)$, that is $B(f(a),\eta)\subset f(B(a,r))\subset f(\Omega)$, and $f(a)$ is an interior point of $f(\Omega)$. As $a$ was arbitrary, $f(\Omega)$ is open.
:::

:::

:::
:::
