---
schema: qual/card@1
id: P-TRIV-RA43
kind: problem
title: Flux of the Coulomb field through a sphere
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 43, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that the flux of the vector field $\vec { A } = q \frac { \vec { r } } { r ^ { 3 } } , q = \mathrm { C o n s t }$ , through the sphere containing the origin equals 4πq.
:::

::: {.solution}

Let
$$
\vec A(x)
=
q\frac{x}{\|x\|^3}
$$
on
$$
\RR^3\setminus\{0\}.
$$

::: pf

::: {.pf-step #s1-1}

Away from the origin,
$$
\operatorname{div}\vec A=0.
$$


::: pf-proof

Since
$$
\vec A
=
-q\nabla\left(\frac1r\right),
$$
one has
$$
\operatorname{div}\vec A
=
-q\Delta\left(\frac1r\right).
$$
For $r>0$,
$$
\Delta(1/r)=0.
$$

:::

:::

::: pf-step

Let $S$ be a sphere whose interior contains the origin. Choose
$\varepsilon>0$ small enough that the centered sphere
$$
S_\varepsilon
=
\{x:\|x\|=\varepsilon\}
$$
lies entirely inside $S$.


::: pf-proof

Because the origin is an interior point of the solid bounded by $S$, some
small Euclidean ball about the origin lies inside it.

:::

:::

::: {.pf-step #s1-3}

Let $\Omega_\varepsilon$ be the region inside $S$ but outside
$S_\varepsilon$. Then
$$
\int_{\partial\Omega_\varepsilon}
\vec A\cdot n
\,dS
=0.
$$


::: pf-proof

The field is smooth on $\Omega_\varepsilon$, and by step [](#s1-1){.pf-ref} its divergence
vanishes there. The divergence theorem gives
$$
\int_{\partial\Omega_\varepsilon}
\vec A\cdot n
\,dS
=
\int_{\Omega_\varepsilon}
\operatorname{div}\vec A
\,dV
=0.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore the outward flux through $S$ equals the outward flux through
$S_\varepsilon$.


::: pf-proof

The boundary of $\Omega_\varepsilon$ consists of the outer sphere $S$ with its
usual outward normal and the inner sphere $S_\varepsilon$ with normal pointing
into the excised ball, which is the negative of the usual outward normal of
$S_\varepsilon$. Thus step [](#s1-3){.pf-ref} gives
$$
\Phi(S)-\Phi(S_\varepsilon)=0.
$$

:::

:::

::: {.pf-step #s1-5}

On $S_\varepsilon$,
$$
\vec A\cdot n
=
\frac{q}{\varepsilon^2}.
$$


::: pf-proof

The outward unit normal is
$$
n=\frac{x}{\varepsilon}.
$$
Since $\|x\|=\varepsilon$,
$$
\vec A
=
q\frac{x}{\varepsilon^3}
=
\frac{q}{\varepsilon^2}n.
$$

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\Phi(S_\varepsilon)
=
\frac{q}{\varepsilon^2}
\operatorname{Area}(S_\varepsilon)
=
\frac{q}{\varepsilon^2}
4\pi\varepsilon^2
=
4\pi q.
$$


::: pf-proof

Use step [](#s1-5){.pf-ref} and the surface area formula for a sphere of radius
$\varepsilon$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\Phi(S)=4\pi q.
}
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required flux.

:::

:::

:::
