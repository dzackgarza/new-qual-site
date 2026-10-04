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
\mathbb R^3\setminus\{0\}.
$$

<1>1. Away from the origin,
$$
\operatorname{div}\vec A=0.
$$

::: {.proof}
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

<1>2. Let $S$ be a sphere whose interior contains the origin. Choose
$\varepsilon>0$ small enough that the centered sphere
$$
S_\varepsilon
=
\{x:\|x\|=\varepsilon\}
$$
lies entirely inside $S$.

::: {.proof}
Because the origin is an interior point of the solid bounded by $S$, some
small Euclidean ball about the origin lies inside it.
:::

<1>3. Let $\Omega_\varepsilon$ be the region inside $S$ but outside
$S_\varepsilon$. Then
$$
\int_{\partial\Omega_\varepsilon}
\vec A\cdot n
\,dS
=0.
$$

::: {.proof}
The field is smooth on $\Omega_\varepsilon$, and by step <1>1 its divergence
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

<1>4. Therefore the outward flux through $S$ equals the outward flux through
$S_\varepsilon$.

::: {.proof}
The boundary of $\Omega_\varepsilon$ consists of the outer sphere $S$ with its
usual outward normal and the inner sphere $S_\varepsilon$ with normal pointing
into the excised ball, which is the negative of the usual outward normal of
$S_\varepsilon$. Thus step <1>3 gives
$$
\Phi(S)-\Phi(S_\varepsilon)=0.
$$
:::

<1>5. On $S_\varepsilon$,
$$
\vec A\cdot n
=
\frac{q}{\varepsilon^2}.
$$

::: {.proof}
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

<1>6. Hence
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

::: {.proof}
Use step <1>5 and the surface area formula for a sphere of radius
$\varepsilon$.
:::

<1>7. Therefore
$$
\boxed{
\Phi(S)=4\pi q.
}
$$

::: {.proof}
Combine steps <1>4 and <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required flux.
:::
:::
