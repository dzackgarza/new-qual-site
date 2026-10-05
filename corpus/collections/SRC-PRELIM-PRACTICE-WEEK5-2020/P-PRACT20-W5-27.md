---
schema: qual/card@1
id: P-PRACT20-W5-27
kind: problem
title: The integral $\int_0^{2\pi}e^{e^{it}}\,dt$
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 27).
---

::: {.problem}
Evaluate $\int_0^{2\pi} e^{e^{it}}\,dt$.
:::

::: {.solution}
<1>1. Under the substitution
\[
z=e^{it},
\]
one has
\[
dz=iz\,dt
\qquad\text{and}\qquad
dt=\frac{dz}{iz}.
\]

::: {.proof}
Differentiate $z=e^{it}$ with respect to $t$. As $t$ runs from $0$ to
$2\pi$, the point $z$ traverses the unit circle once counterclockwise.
:::

<1>2. Therefore
\[
\int_0^{2\pi} e^{e^{it}}\,dt
=
\frac1i
\oint_{|z|=1}\frac{e^z}{z}\,dz.
\]

::: {.proof}
Substitute $z=e^{it}$ and the differential relation from step <1>1.
:::

<1>3. The contour integral satisfies
\[
\oint_{|z|=1}\frac{e^z}{z}\,dz=2\pi i.
\]

::: {.proof}
The integrand has a single simple pole at $0$ inside the unit circle, with
residue
\[
\operatorname{Res}_{z=0}\frac{e^z}{z}=e^0=1.
\]
The residue theorem gives
\[
\oint_{|z|=1}\frac{e^z}{z}\,dz
=2\pi i.
\]
:::

<1>4. Hence
\[
\boxed{\int_0^{2\pi} e^{e^{it}}\,dt=2\pi}.
\]

::: {.proof}
Combine steps <1>2 and <1>3:
\[
\frac1i(2\pi i)=2\pi.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the requested value.
:::
:::
