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

::: pf

::: {.pf-step #s1-1}

Under the substitution
$$
z=e^{it},
$$
one has
$$
dz=iz\,dt
\qquad\text{and}\qquad
dt=\frac{dz}{iz}.
$$


::: pf-proof

Differentiate $z=e^{it}$ with respect to $t$. As $t$ runs from $0$ to
$2\pi$, the point $z$ traverses the unit circle once counterclockwise.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\int_0^{2\pi} e^{e^{it}}\,dt
=
\frac1i
\oint_{\abs{z}=1}\frac{e^z}{z}\,dz.
$$


::: pf-proof

Substitute $z=e^{it}$ and the differential relation from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The contour integral satisfies
$$
\oint_{\abs{z}=1}\frac{e^z}{z}\,dz=2\pi i.
$$


::: pf-proof

The integrand has a single simple pole at $0$ inside the unit circle, with
residue
$$
\operatorname{Res}_{z=0}\frac{e^z}{z}=e^0=1.
$$
The residue theorem gives
$$
\oint_{\abs{z}=1}\frac{e^z}{z}\,dz
=2\pi i.
$$

:::

:::

::: {.pf-step #s1-4}

Hence
$$
\boxed{\int_0^{2\pi} e^{e^{it}}\,dt=2\pi}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}:
$$
\frac1i(2\pi i)=2\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the requested value.

:::

:::

:::
