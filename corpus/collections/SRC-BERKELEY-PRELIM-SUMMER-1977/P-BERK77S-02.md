---
schema: qual/card@1
id: P-BERK77S-02
kind: problem
title: A continuous function holomorphic off the real axis is entire
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used Morera's theorem. For an arbitrary triangle, split it along the
    real axis. Cauchy's theorem on truncations a positive distance from the
    seam and continuity as the truncation tends to the seam show that each
    half has zero boundary integral; the seam integrals cancel, so every
    triangular contour integral of f vanishes.
---

::: {.problem}
Let $f$ be continuous on $\mathbb C$ and analytic on
\[
\{z\in\mathbb C:\operatorname{Im}z\ne0\}.
\]
Prove that $f$ is analytic on all of $\mathbb C$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $P$ be a polygon contained in the closed upper half-plane whose
interior lies in the open upper half-plane. Then
$$
\int_{\partial P}f(z)\,dz=0.
$$

::: pf-proof

For $\varepsilon>0$, truncate $P$ by the horizontal line
$\operatorname{Im}z=\varepsilon$:
$$
P_\varepsilon
=
P\cap\{z:\operatorname{Im}z\geq\varepsilon\}.
$$
For all sufficiently small $\varepsilon$, $P_\varepsilon$ is a polygon
whose closure lies in the open upper half-plane. Since $f$ is holomorphic
there, Cauchy's theorem gives
$$
\int_{\partial P_\varepsilon}f(z)\,dz=0.
$$

As $\varepsilon\downarrow0$, the finitely many vertices and line segments
of $\partial P_\varepsilon$ converge to those of $\partial P$. The function
$f$ is uniformly continuous on a compact neighborhood of $P$, so the
integral over each moving segment converges to the integral over the
corresponding limiting segment. Therefore
$$
\int_{\partial P}f(z)\,dz
=
\lim_{\varepsilon\downarrow0}
\int_{\partial P_\varepsilon}f(z)\,dz
=
0.
$$

:::

:::

::: {.pf-step #s2}

The analogous statement holds for a polygon contained in the closed
lower half-plane whose interior lies in the open lower half-plane.

::: pf-proof

The proof of step [](#s1){.pf-ref} applies verbatim after truncating by
$\operatorname{Im}z=-\varepsilon$, because $f$ is holomorphic throughout
the open lower half-plane and continuous on the real axis.

:::

:::

::: {.pf-step #s3}

For every triangle $\Delta\subset\CC$,
$$
\int_{\partial\Delta}f(z)\,dz=0.
$$

::: pf-proof

If the interior of $\Delta$ lies entirely in one open half-plane, this is
Cauchy's theorem. Otherwise the real axis cuts $\Delta$ into an upper
polygon $\Delta_+$ and a lower polygon $\Delta_-$, allowing one of them to
be degenerate. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give
$$
\int_{\partial\Delta_+}f(z)\,dz=0,
\qquad
\int_{\partial\Delta_-}f(z)\,dz=0.
$$
When these two equations are added, every segment lying on the real axis
occurs once in each orientation and cancels. The remaining oriented edges
are exactly $\partial\Delta$. Hence
$$
\int_{\partial\Delta}f(z)\,dz=0.
$$

:::

:::

::: {.pf-step #s4}

The function $f$ is analytic on $\CC$.

::: pf-proof

The function $f$ is continuous on $\CC$ by hypothesis, and step [](#s3){.pf-ref} shows
that its integral around every triangle is zero. Morera's theorem therefore
implies that $f$ is holomorphic on all of $\CC$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
