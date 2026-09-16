---
schema: qual/card@1
id: E-SS8.EX-18
kind: problem
title: "The conformal map of the disk extends to the boundary (Caratheodory)"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Restored the closures in the boundary-extension statement, matching Stein--Shakarchi Theorem 4.2 and Exercise 18.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
18. Suppose that $\Omega$ is a simply connected domain that is bounded by a piecewisesmooth closed curve $\gamma$ (in the terminology of Chapter 1). Then any conformal map $F$ of D to Ω extends to a continuous bijection of $\overline{\mathbb D}$ to $\overline{\Omega}$. The proof is simply a generalization of the argument used in Theorem 4.2.
:::

::: {.solution}
The proof of Theorem 4.2 for polygonal regions uses only two geometric facts about the target boundary: the region is bounded, and for every boundary point $w_0$ there is $r_0>0$ such that for $0<r<r_0$ the intersection
\[
\Omega\cap \{w:|w-w_0|=r\}
\]
is a single arc. We verify that a piecewise-smooth Jordan boundary has the same local property, and then the proof of Theorem 4.2 applies verbatim.

Let $w_0=\gamma(t_0)$. At a smooth point, $\gamma'(t_0)\ne0$ and
\[
\gamma(t)=w_0+\gamma'(t_0)(t-t_0)+o(|t-t_0|).
\]
After a rotation and translation, the curve is therefore locally the graph of a continuous function over its tangent line, with the two sides of the Jordan curve lying on opposite sides. Hence every sufficiently small circle centered at $w_0$ meets $\gamma$ in exactly two nearby points, and its intersection with $\Omega$ is the single open arc between them. At a corner the same conclusion follows from the two one-sided nonzero tangent vectors. Since the boundary is piecewise smooth and simple, this gives the required local-arc property at every boundary point.

Now repeat the proof of Theorem 4.2. For $\zeta_0\in\partial\mathbb D$, let $C_r$ be the circle centered at $\zeta_0$ of radius $r$. If $z_r,z_r'\in C_r\cap\mathbb D$ are joined by the arc of $C_r\cap\mathbb D$, then Cauchy--Schwarz gives
\[
|F(z_r)-F(z_r')|^2
\le 2\pi r\int_{C_r\cap\mathbb D}|F'(z)|^2\,|dz|.
\]
If the left side were bounded below by a positive constant for every sufficiently small $r$, integration in $dr/r$ would give an infinite lower bound, while
\[
\iint_{\mathbb D}|F'(z)|^2\,dx\,dy
=\operatorname{Area}(\Omega)<\infty,
\]
a contradiction. Thus there is a sequence $r_n\downarrow0$ along which the oscillation of $F$ on the relevant circular arc tends to zero.

Suppose now that $F(z)$ had two different cluster values $w,w'\in\partial\Omega$ as $z\to\zeta_0$. Choose disjoint small discs around $w,w'$. By the local-arc property of $\Omega$, each disc meets $\Omega$ in a connected arc-like neighborhood, so one can join the corresponding subsequences of image points to $w$ and $w'$ by curves lying in those disjoint neighborhoods. Pulling these curves back by $F^{-1}$ produces two curves in $\mathbb D$ approaching $\zeta_0$. Every sufficiently small $C_r$ meets both curves, at points $z_r,z_r'$, but their images stay a fixed positive distance apart. This contradicts the preceding oscillation estimate along the sequence $r_n$. Therefore
\[
\lim_{z\to\zeta_0,\,z\in\mathbb D}F(z)
\]
exists for every $\zeta_0\in\partial\mathbb D$.

Define the boundary values by these limits. The same sequential argument used in Theorem 4.2 shows that the extension
\[
\overline F:\overline{\mathbb D}\to\overline\Omega
\]
is continuous.

Apply the identical argument to the conformal inverse $G=F^{-1}:\Omega\to\mathbb D$. The local-arc property just verified for $\Omega$ replaces the polygonal boundary property used in Theorem 4.2, while the unit circle has the corresponding property automatically. Hence $G$ extends continuously to
\[
\overline G:\overline\Omega\to\overline{\mathbb D}.
\]
For $z\in\partial\mathbb D$, choose $z_n\in\mathbb D$ with $z_n\to z$. Since $G(F(z_n))=z_n$, continuity gives
\[
\overline G(\overline F(z))=z.
\]
Similarly $\overline F(\overline G(w))=w$ for $w\in\partial\Omega$. Thus the two extensions are inverse homeomorphisms. In particular, $F$ extends to a continuous bijection
\[
\boxed{\overline{\mathbb D}\xrightarrow{\sim}\overline\Omega}.
\]
:::
