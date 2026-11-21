---
schema: qual/card@1
id: P-CAF13A
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
Choose 4 of the following theorems, and write out their statements carefully and completely.
From among these, choose 2, and sketch their proofs.

- The Open Mapping Theorem

- Rouché's Theorem

- Runge's Theorem

- The Riemann Mapping Theorem

- The Poisson Integral Formula

- Morera's Theorem

- The Argument Principle

- The Great Picard Theorem

- The Monodromy Theorem

- The Schwarz Reflection Principle
:::

::: {.solution}

The four statements are the standard ones and are quoted as the exercise asks; the two sketches are the card's own write-ups of the standard arguments, and the Rouché step used inside the first is stated among the four, so the sketch does not invoke anything unproved beyond it.

::: pf

::: {.pf-step #open-mapping}
Statement, Open Mapping Theorem. If $G\subset\CC$ is a domain and $f:G\to\CC$ is holomorphic and nonconstant, then $f(G)$ is open.

::: pf-proof
Quoted, as asked. The hypotheses are exactly that $G$ is nonempty, open and connected and that $f$ is holomorphic there and not constant; the conclusion is that for each $z_{0}\in G$ some disc about $f(z_{0})$ lies in $f(G)$. Constancy is essential: a constant map has image a single point, which is not open.
:::

:::

::: {.pf-step #rouche}
Statement, Rouché's Theorem. Let $\gamma$ be a positively oriented simple closed contour whose interior and boundary lie in a domain on which $f$ and $g$ are holomorphic, and suppose $\abs{g(z)}<\abs{f(z)}$ for $z\in\gamma$. Then $f$ and $f+g$ have the same number of zeros inside $\gamma$, counted with multiplicity.

::: pf-proof
Quoted, as asked. The point of the strict inequality on the contour is that $f$ has no zero there, so both zero counts are finite and defined; the conclusion counts multiplicities, and the interior is taken with the positive orientation.
:::

:::

::: {.pf-step #morera}
Statement, Morera's Theorem. Let $G$ be a domain and $f:G\to\CC$ continuous. If $\int_{\partial T}f(z)\,dz=0$ for every triangle $T$ whose closure lies in $G$, then $f$ is holomorphic on $G$.

::: pf-proof
Quoted, as asked. Continuity of $f$ is a hypothesis and not a consequence of the integral condition alone in the absence of local boundedness; the triangles range over all closed triangles contained in $G$, and $\partial T$ carries the positive orientation.
:::

:::

::: {.pf-step #argument-principle}
Statement, Argument Principle. Let $f$ be meromorphic on a neighbourhood of the closure of a bounded domain bounded by a positively oriented contour $\gamma$, with no zeros and no poles on $\gamma$. Then
$$
\frac{1}{2\pi i}\int_{\gamma}\frac{f'(z)}{f(z)}\,dz=N-P,
$$
where $N$ and $P$ are the numbers of zeros and of poles inside $\gamma$, counted with multiplicity.

::: pf-proof
Quoted, as asked. The hypothesis that $\gamma$ is a contour bounding a bounded domain, that $f$ is meromorphic on a neighbourhood of its closure, and that no zero or pole lies on $\gamma$ is what makes $f'/f$ holomorphic on a neighbourhood of $\gamma$ and the integral finite; multiplicities are counted, a zero of order $m$ contributing $m$ and a pole of order $m$ contributing $-m$.
:::

:::

::: {.pf-step #sketch-open-mapping}
Sketch of the Open Mapping Theorem: every point of $G$ has an image containing a disc, by Rouché's theorem.

::: pf-proof
Fix $z_{0}\in G$. Since $f$ is nonconstant and holomorphic, $f(z)-f(z_{0})$ has a zero of finite order $m\ge1$ at $z_{0}$, so near $z_{0}$
$$
f(z)-f(z_{0})=(z-z_{0})^{m}h(z),\qquad h(z_{0})\ne0 .
$$
Choose $r>0$ with $\overline{B(z_{0},r)}\subset G$ and $f(z)\ne f(z_{0})$ for $\abs{z-z_{0}}=r$; such $r$ exists because the zeros of $f-f(z_{0})$ are isolated and $G$ is open. The continuous function $\abs{f(z)-f(z_{0})}$ attains a minimum $\delta>0$ on the compact circle $\abs{z-z_{0}}=r$. Let $\abs{w-f(z_{0})}<\delta$. On that circle,
$$
\abs{(f(z)-w)-\big(f(z)-f(z_{0})\big)}=\abs{w-f(z_{0})}<\delta\le\abs{f(z)-f(z_{0})},
$$
so the hypothesis of step [](#rouche){.pf-ref} holds on the circle with $f$ replaced by $f-f(z_{0})$ and $g$ replaced by $f(z_{0})-w$. Rouché's theorem therefore gives that $f-w$ has inside the circle as many zeros as $f-f(z_{0})$, namely $m\ge1$; so $w=f(z)$ for some $z$ with $\abs{z-z_{0}}<r$, and $B(f(z_{0}),\delta)\subset f(G)$. As $z_{0}$ was arbitrary, $f(G)$ is open.
:::

:::

::: {.pf-step #sketch-morera}
Sketch of Morera's Theorem: the triangle condition gives a primitive in a disc, and the primitive is holomorphic with derivative $f$.

::: pf-proof
Let $D\Subset G$ be an open disc and fix $z_{*}\in D$. Define
$$
F(z)=\int_{[z_{*},z]}f(\zeta)\,d\zeta
$$
on the segment $[z_{*},z]\subset D$, which lies in $G$. The hypothesis that the integral over the boundary of every triangle in $G$ vanishes implies, by induction on the number of pieces, that the integral of $f$ over the boundary of every closed polygon in $D$ vanishes; writing the difference of a polygonal path from $z_{*}$ to $z$ and the straight segment as a sum of such polygon boundaries, the integral defining $F(z)$ does not depend on the path. Hence for $z,z+h\in D$ with the segment between them in $D$,
$$
F(z+h)-F(z)=\int_{[z,z+h]}f(\zeta)\,d\zeta,
$$
and by continuity of $f$ at $z$, writing $f(\zeta)=f(z)+\big(f(\zeta)-f(z)\big)$,
$$
\frac{F(z+h)-F(z)}{h}=f(z)+\frac{1}{h}\int_{[z,z+h]}\big(f(\zeta)-f(z)\big)d\zeta=f(z)+o(1)
$$
as $h\to0$, because the integrand is bounded by $\sup_{\zeta\in[z,z+h]}\abs{f(\zeta)-f(z)}$, which tends to $0$. So $F'=f$ on $D$ and $F$ is holomorphic there; a holomorphic function has a holomorphic derivative, so $f=F'$ is holomorphic on $D$. Every point of $G$ lies in such a disc $D\Subset G$, so $f$ is holomorphic on $G$.
:::

:::

:::
:::
