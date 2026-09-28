---
schema: qual/card@1
id: P-JHUFA05ANE
kind: problem
title: The keyhole integral of $1/(x^{1/3}(1+x))$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the one-third power and keyhole-contour hint with September 2005 problem 5 in the retained JHU source; separated the hint and removed the page-continuation instruction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked absolute convergence, the two boundary values of the fractional power, the pole residue, both arc estimates and the limiting construction of the keyhole contour."
---

::: {.problem}
5. Use contour integration to evaluate

$$
\int _ { 0 } ^ { + \infty } { \frac { d x } { x ^ { 1 / 3 } ( 1 + x ) } } .
$$
:::

::: {.hint}
Use a keyhole contour around the positive real axis, with
inner radius $\varepsilon$ and outer radius $R$.
:::

::: {.solution}
The value is $\boxed{2\pi/\sqrt3}$.

<1>1. The integral converges absolutely at both endpoints.

::: {.proof}
For $0<x\leq1$, the positive integrand is at most
$x^{-1/3}$, whose integral at zero is finite. For $x\geq1$,
it is at most $x^{-4/3}$, integrable at infinity. Write
$I=\int_0^\infty x^{-1/3}/(1+x)\,dx$.
:::

<1>2. The logarithm branch gives a keyhole residue identity.

::: {.proof}
Use $0<\arg z<2\pi$ and set
$$
F(z)=\frac{\exp(-\operatorname{Log}z/3)}{1+z}.
$$
For fixed $0<\varepsilon<1<R$, first integrate over the
positive boundary of
$\{\varepsilon<|z|<R,\ \delta<\arg z<2\pi-\delta\}$,
where $0<\delta<\pi/2$. The branch is holomorphic near
this contour. Its only enclosed pole is $-1$, simple,
with residue $e^{-i\pi/3}$. The residue theorem gives
the contour integral $2\pi i e^{-i\pi/3}$ [@SS03].

Let $\delta\downarrow0$ with the radii fixed. On each
radial segment the integrand converges uniformly, since
$x$ stays in the compact interval $[\varepsilon,R]$ and
the limiting denominator is nonzero. The upper bank,
traversed outward, contributes $I_{\varepsilon,R}$.
The lower bank has fractional-power value
$e^{-2\pi i/3}x^{-1/3}$ and is traversed inward, so
contributes $-e^{-2\pi i/3}I_{\varepsilon,R}$. The arc
integrals also have limits by boundedness on their fixed
circles. Hence
$$
(1-e^{-2\pi i/3})I_{\varepsilon,R}
+\text{outer arc integral}+\text{inner arc integral}
=2\pi i e^{-i\pi/3}.
$$
:::

<1>3. The arcs disappear and the phase factors determine $I$.

::: {.proof}
The respective arc integrals have moduli bounded by
$$
\frac{2\pi R^{2/3}}{R-1}\longrightarrow0,
\qquad
\frac{2\pi\varepsilon^{2/3}}{1-\varepsilon}\longrightarrow0.
$$
These follow from $|z^{-1/3}|=|z|^{-1/3}$, the arc
lengths, and $|1+z|\geq\bigl||z|-1\bigr|$.
Letting $R\to\infty$ and $\varepsilon\downarrow0$ in
step <1>2 therefore yields
$$
(1-e^{-2\pi i/3})I=2\pi i e^{-i\pi/3}.
$$
Since $1-e^{-2\pi i/3}=2i e^{-i\pi/3}\sin(\pi/3)$,
division gives $I=\pi/\sin(\pi/3)=2\pi/\sqrt3$.
:::
:::
