---
schema: qual/card@1
id: P-MMAQ-S7C4CCIUTP
kind: problem
title: Cauchy's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Theorem
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the two Green-theorem applications it turns on. The solution's statement of
    Cauchy's theorem required only that the interior of $\gamma$ lie in $\Omega$, and that
    hypothesis is not enough to make the theorem meaningful, because $\Omega$ is open:
    $\Omega=\theset{\abs z<1}$ with $\gamma=\theset{\abs z=1}$ satisfies it while $\gamma$ misses
    $\Omega$ entirely, so $f$ need not be defined on $\gamma$ and $u,v\in C^1(\overline{D})$, which
    the Green step needs, does not follow. The hypothesis now reads
    $\gamma\subseteq\Omega$ and $\operatorname{Int}(\gamma)\subseteq\Omega$, i.e.
    $\overline{\operatorname{Int}(\gamma)}\subseteq\Omega$ for a Jordan curve, and the step that
    applies Green's theorem says where the clause is used. The two applications and both
    Cauchy--Riemann cancellations were re-derived and are unchanged. Not checked in this pass:
    anything outside this solution.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Use Green theorem or otherwise to prove the Cauchy theorem.
:::

::: {.solution}

The argument is the card's own: $f\,dz$ is split into its real and imaginary line integrals and Green's theorem is applied to each, with the Cauchy--Riemann equations making both double integrals vanish, and no source transcribed. The collection records no retained paper --- its `provenance:` list is empty and its `source_kind` is `university-exam` --- so no printed page is cited here, and none is implied.
### Statement of Cauchy's theorem for $C^1$ functions

Let $\Omega \subset \CC$ be a simply connected domain.
Let $f: \Omega \to \CC$ be a holomorphic function whose derivative $f'$ is continuous ($f \in C^1(\Omega)$). Let $\gamma$ be a piecewise smooth, positively oriented simple closed curve with $\gamma \subseteq \Omega$ and $\text{Int}(\gamma) \subseteq \Omega$, that is, with $\overline{\text{Int}(\gamma)} \subseteq \Omega$.
Then: $$\oint_\gamma f(z) \, dz = 0.$$

* * *

### Proof via Green's theorem

::: pf

::: pf-step

**Decompose the complex contour integral into real line integrals.**

::: pf-proof

::: pf-step

Write $f(z) = u(x, y) + i v(x, y)$ where $z = x + iy$, and $dz = dx + i dy$.

::: pf-proof

Decomposition of complex functions and differentials into real and imaginary parts.

:::

:::

::: pf-step

The product $f(z) \, dz$ expands as: $$f(z) \, dz = (u + iv)(dx + i dy) = (u \, dx - v \, dy) + i (v \, dx + u \, dy).$$

::: pf-proof

Algebraic expansion of complex multiplication ($i^2 = -1$).

:::

:::

::: {.pf-step #s1-3}

Integrating along $\gamma$: $$\oint_\gamma f(z) \, dz = \oint_\gamma (u \, dx - v \, dy) + i \oint_\gamma (v \, dx + u \, dy).$$

::: pf-proof

Linearity of integration.

:::

:::

:::

:::

::: pf-step

**Recall Green's Theorem on the bounded region $D = \text{Int}(\gamma)$.**

::: pf-proof

::: pf-step

Let $D \subset \RR^2$ be the bounded region enclosed by $\gamma = \partial D$.
If $P, Q: \overline{D} \to \RR$ are $C^1$, then: $$\oint_\gamma (P \, dx + Q \, dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA.$$

::: pf-proof

Statement of Green's Theorem for planar regions.

:::

:::

::: pf-step

Since $f'$ is continuous, the partial derivatives $u_x, u_y, v_x, v_y$ exist and are continuous on $\overline{D}$, so Green's Theorem is applicable.

::: pf-proof

Continuity of $f'$ implies $u, v \in C^1(\overline{D})$. Here is where the hypothesis $\gamma \subseteq \Omega$ is used: $\overline{D} = \overline{\text{Int}(\gamma)} = \text{Int}(\gamma) \cup \gamma \subseteq \Omega$, so $f$ is defined and $C^1$ on a neighbourhood of $\overline{D}$. Under the weaker hypothesis $\text{Int}(\gamma) \subseteq \Omega$ alone the values of $f$ on $\gamma$, and with them the integral the theorem is about, need not exist.

:::

:::

:::

:::

::: {.pf-step #s3}

**Evaluate the real part $\oint_\gamma (u \, dx - v \, dy)$.**

::: pf-proof

::: pf-step

Set $P = u$ and $Q = -v$.

::: pf-proof

Identification of components.

:::

:::

::: {.pf-step #s3-2}

By Green's Theorem: $$\oint_\gamma (u \, dx - v \, dy) = \iint_D \left( \frac{\partial(-v)}{\partial x} - \frac{\partial u}{\partial y} \right) dA = -\iint_D \left( \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y} \right) dA.$$

::: pf-proof

Applying Green's Theorem to $P = u, Q = -v$.

:::

:::

::: {.pf-step #s3-3}

By the Cauchy-Riemann equations for the holomorphic function $f$, $u_y = -v_x \iff v_x + u_y = 0$.

::: pf-proof

Cauchy-Riemann equations hold everywhere in $\Omega \supset \overline{D}$.

:::

:::

::: pf-step

Therefore: $$\oint_\gamma (u \, dx - v \, dy) = -\iint_D 0 \, dA = 0.$$

::: pf-proof

Substitution of step [](#s3-3){.pf-ref} into step [](#s3-2){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s4}

**Evaluate the imaginary part $\oint_\gamma (v \, dx + u \, dy)$.**

::: pf-proof

::: pf-step

Set $P = v$ and $Q = u$.

::: pf-proof

Identification of components.

:::

:::

::: {.pf-step #s4-2}

By Green's Theorem: $$\oint_\gamma (v \, dx + u \, dy) = \iint_D \left( \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \right) dA.$$

::: pf-proof

Applying Green's Theorem to $P = v, Q = u$.

:::

:::

::: {.pf-step #s4-3}

By the Cauchy-Riemann equations for $f$, $u_x = v_y \iff u_x - v_y = 0$.

::: pf-proof

Cauchy-Riemann equations.

:::

:::

::: pf-step

Therefore: $$\oint_\gamma (v \, dx + u \, dy) = \iint_D 0 \, dA = 0.$$

::: pf-proof

Substitution of step [](#s4-3){.pf-ref} into step [](#s4-2){.pf-ref}.

:::

:::

:::

:::

::: pf-step

**Conclusion: $\oint_\gamma f(z) \, dz = 0$.**

::: pf-proof

::: pf-step

Combining the real and imaginary parts from steps [](#s3){.pf-ref} and [](#s4){.pf-ref}: $$\oint_\gamma f(z) \, dz = 0 + i(0) = 0.$$

::: pf-proof

Follows from step [](#s1-3){.pf-ref}.

:::

:::

:::

:::

:::

:::
