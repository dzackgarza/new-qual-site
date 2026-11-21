---
schema: qual/card@1
id: P-CAFA16D
kind: problem
title: "An analytic function on the disk vanishing on an arc of the boundary is identically zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the reflection step against
    its hypotheses: f is holomorphic on the disc, continuous on the closed disc, and vanishes on an
    open arc of the boundary circle, so it is real-valued on an open circular arc up to which it is
    continuous, which is exactly what the Schwarz reflection principle for a circular arc needs;
    the card's "after a rotation ... a neighborhood of the interval of the real axis" is now the
    statement that a Mobius map carrying the circle to the line reduces it to reflection across an
    interval. The extension is defined on the union of the disc with a neighbourhood of an interior
    arc, which is connected because that neighbourhood meets the disc, so the identity theorem
    applies to give F identically zero, and f = 0 on the closed disc by continuity. The hypothesis
    alpha > 0 is used only to produce an interior point of the arc, and the step says so. Statement
    unchanged; the card says the argument is its own.
---

::: {.problem}
Let $f: \overline{\DD} \to \CC$ be a continuous function which is analytic on $\DD$.
Assume that there exists $0 < \alpha \leq 2\pi$ such that $f(e^{i\theta}) = 0$ for all $\theta \in (0, \alpha)$.
Prove that $f(z) = 0$ for every $z \in \DD$.
:::

::: {.solution}
The zero set of $f$ contains an open arc of the circle, and along that arc $f$ is continuous with real (indeed zero) boundary values, so the Schwarz reflection principle extends $f$ holomorphically across an interior point of the arc. The extension has interior zeros with an accumulation point on the arc, so it vanishes identically on the connected domain it is defined on, and $f\equiv0$ on the disc follows. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #arc}
Pick $0<\theta_0<\alpha$ and $0<\varepsilon$ with $(\theta_0-\varepsilon,\theta_0+\varepsilon)\subset(0,\alpha)$; then $f$ vanishes on the open arc $I=\{e^{i\theta}:\abs{\theta-\theta_0}<\varepsilon\}$.

::: pf-proof
This is the hypothesis $f(e^{i\theta})=0$ for $0<\theta<\alpha$, restricted to a smaller interval inside it. Such an interval exists because $(0,\alpha)$ is open in $\RR$ and nonempty, the hypothesis $\alpha>0$ ensuring it has interior points.
:::

:::


::: {.pf-step #reflect}
There is a connected open set $\Omega\supseteq\DD\cup I$ and a holomorphic $F\colon\Omega\to\CC$ with $F=f$ on $\DD$.

::: pf-proof
$f$ is holomorphic on $\DD$ and continuous on $\overline\DD$, hence continuous on $\DD\cup I$, and $f=0$ on $I$ by step [](#arc){.pf-ref}, so $f$ is real-valued on the open circular arc $I$. The Schwarz reflection principle for a circular arc applies: if $g$ is holomorphic on a region, continuous up to an open arc of a circle bounding a disc inside the region, and real on that arc, then $g$ extends holomorphically across the arc. Concretely, a Möbius transformation carrying the circle to the real line and $\DD$ to the upper half-plane reduces the statement to the classical Schwarz reflection across an interval of $\RR$; composing back gives the extension $F$ on a neighbourhood of $I$ glued to $\DD$. Taking $\Omega$ to be the union of $\DD$ with a small neighbourhood of $I$, we get a connected open set, since $\DD$ is connected and any neighbourhood of an interior point of the arc meets $\DD$.
:::

:::


::: {.pf-step #zero}
$F\equiv0$ on $\Omega$, hence $f\equiv0$ on $\DD$ and on $\overline\DD$.

::: pf-proof
The arc $I$ is contained in $\Omega$ and consists of interior points of $\Omega$ by construction; $F=0$ on $I$ because $F$ agrees with $f$ there. A holomorphic function vanishing on a set with accumulation points inside its domain vanishes identically on the connected component containing it, by the identity theorem; $I$ has accumulation points in $\Omega$ and $\Omega$ is connected, so $F\equiv0$ on $\Omega$. In particular $F\equiv0$ on $\DD$, and $F=f$ there, so $f\equiv0$ on $\DD$ and, $f$ being continuous on $\overline\DD$, on the closed disc as well.
:::

:::


::: {.pf-step #conclusion}
$f(z)=0$ for every $z\in\DD$.

::: pf-proof
Step [](#zero){.pf-ref} gives the assertion. The hypothesis $\alpha>0$ is what supplies an interior point of the arc, and it is used only there.
:::

:::

:::
:::
