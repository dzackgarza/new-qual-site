---
schema: qual/card@1
id: E-OI7VN
kind: problem
title: The logarithmic spiral and the knotted x-axis as retracts
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Moller, "Solutions to exercises
    in Munkres", file S35.pdf, Exercise 35.7, page 2 of the file
    (tmp/sources/munkres-solutions-poulsen-S35.pdf, Internet Archive snapshot 20220130234235),
    checked against Munkres, Topology (2000), Section 35 Exercise 7, printed p. 224, Theorem 35.1 and
    Exercise 35.6. Its (a) gives the explicit retraction of the plane onto the logarithmic spiral --
    in polar form, send the point of modulus rho to the spiral point of parameter log rho, and fix
    the origin -- and the card writes the same map in Cartesian coordinates; its (b) is the
    Tietze-plus-absolute-retract argument, since the knotted x-axis is a closed subspace of R^3
    homeomorphic to the line. What was corrected: Moller writes of (b) "I can't find an explicit
    retraction R^3 -> K, though", which is honest but leaves the reader to check that the composite
    h^{-1} . H is a retraction; the card writes the composite and verifies it fixes K pointwise.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both parts into numbered steps. Supplied for (a): that r takes values in the spiral
    (r(x,y) is the spiral point of parameter log rho), its continuity off the origin as a composite,
    and continuity at the origin through |r(x,y)| = rho -> 0, followed by the fixed-point computation
    on the spiral. Supplied for (b): that the knotted x-axis is closed and homeomorphic to R, that
    R^3 is normal so that Tietze applies to a real-valued function on a closed subspace, and that
    h^{-1} o H is continuous and fixes K. The mathematics is the earlier reading's; no defect found.
---

::: {.exercise}

(a) Show that the logarithmic spiral

$$
C = \theset{0 \times 0} \cup \theset{e^t \cos t \times e^t \sin t \mid t \in \RR}
$$

is a retract of $\RR^2$.
Can you define a specific retraction $r: \RR^2 \to C$?

(b) Show that the "knotted x-axis" $K$ pictured in Figure 35.2 of the text is a retract of $\RR^3$.
:::

::: {.solution}

Both parts are those of **Jesper Michael Moller, "Solutions to exercises in Munkres", S35 Exercise 35.7, page 2 of that file** (`tmp/sources/munkres-solutions-poulsen-S35.pdf`), with the composite in (b) written out. The statement was checked against Munkres, *Topology* (2000), §35 Exercise 7, printed p. 224.

::: pf

::: {.pf-step #spiral}
$C=\{0\}\cup\{e^{t}(\cos t,\sin t)\mid t\in\RR\}$ is a subset of $\RR^{2}$ containing the origin.

::: pf-proof
The curve $t\mapsto e^{t}(\cos t,\sin t)$ is continuous with values in $\RR^{2}$, and the origin is adjoined explicitly.
:::

:::

::: {.pf-step #r-defined}
The rule $r(x,y)=\rho\bigl(\cos(\log\rho),\sin(\log\rho)\bigr)$ for $\rho=\sqrt{x^{2}+y^{2}}\neq0$, with $r(0,0)=(0,0)$, defines a map $\RR^{2}\to C$.

::: pf-proof
For $(x,y)\neq0$ we have $\rho>0$, so $\log\rho\in\RR$ and $r(x,y)=e^{\log\rho}\bigl(\cos\log\rho,\sin\log\rho\bigr)$ is the point of the spiral with parameter $t=\log\rho$; and $r(0,0)=0\in C$.
:::

:::

::: {.pf-step #r-continuous}
$r$ is continuous.

::: pf-proof
Off the origin $r$ is a composite of the continuous maps $(x,y)\mapsto\rho$, $\log$, and $t\mapsto(\cos t,\sin t)$. At the origin, $\norm{r(x,y)}=\rho\to0$ as $(x,y)\to0$, and $r(0,0)=0$, so $r$ is continuous there too.
:::

:::

::: {.pf-step #r-fixes}
$r$ fixes every point of $C$, so $r$ is a retraction of $\RR^{2}$ onto $C$.

::: pf-proof
Let $(x,y)=e^{t}(\cos t,\sin t)$ with $(x,y)\neq0$. Then $\rho=e^{t}\sqrt{\cos^{2}t+\sin^{2}t}=e^{t}$, hence $\log\rho=t$ and $r(x,y)=e^{t}(\cos t,\sin t)=(x,y)$; and $r(0,0)=(0,0)$. A continuous map of $\RR^{2}$ onto $C$ fixing $C$ pointwise is a retraction onto $C$.
:::

:::

::: {.pf-step #k-closed}
The knotted $x$-axis $K$ of Figure 35.2 is a closed subspace of $\RR^{3}$ homeomorphic to $\RR$.

::: pf-proof
$K$ is a properly embedded copy of $\RR$ in $\RR^{3}$, as the figure depicts, so it is homeomorphic to $\RR$. A properly embedded subspace is closed: if $(k_{n})$ is a sequence in $K$ converging in $\RR^{3}$, its image is bounded, so the representing parameters are bounded, and a bounded sequence in $\RR$ has a subsequential limit whose image is the same point, which therefore lies in $K$.
:::

:::

::: {.pf-step #tietze}
There is a continuous $H\colon\RR^{3}\to\RR$ with $\restrictionof{H}{K}=h$.

::: pf-proof
$\RR^{3}$ is metrizable, hence normal, and $K$ is closed by step [](#k-closed){.pf-ref}. By the Tietze extension theorem a continuous real-valued function on a closed subspace of a normal space extends continuously to the whole space; apply it to $h\colon K\to\RR$.
:::

:::

::: {.pf-step #retraction}
$r=h^{-1}\circ H$ is a retraction of $\RR^{3}$ onto $K$.

::: pf-proof
$h^{-1}$ is continuous because $h$ is a homeomorphism onto $K$, and $H$ is continuous by step [](#tietze){.pf-ref}; so $r$ is continuous with values in $K$. For $k\in K$ we have $H(k)=h(k)$, hence $r(k)=h^{-1}(h(k))=k$.
:::

:::

:::

:::
