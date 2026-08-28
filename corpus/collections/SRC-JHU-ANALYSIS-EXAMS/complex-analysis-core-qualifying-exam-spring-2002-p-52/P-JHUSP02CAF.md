---
schema: qual/card@1
id: P-JHUSP02CAF
kind: problem
title: "Mobius transformations carry lines and circles to lines and circles"
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
Show that a Möbius transformation maps a straight line or circle onto a straight line or circle.
:::

::: solution
**Goal:** Prove that every Möbius transformation $T(z) = \frac{az+b}{cz+d}$ with $ad - bc \neq 0$ maps generalized circles (lines and circles) in the extended complex plane $\widehat{\mathbb{C}}$ to generalized circles.

<1>1. Equation of a generalized circle in $\mathbb{C}$:
    A curve $\Gamma \subset \mathbb{C}$ is a straight line or circle if and only if it satisfies the equation:
    $$A |z|^2 + B z + \overline{B} \overline{z} + C = 0$$
    where $A, C \in \mathbb{R}$, $B \in \mathbb{C}$, and $|B|^2 - AC > 0$.
    *Proof:*
    <2>1. If $A = 0$, the equation is $B z + \overline{B} \overline{z} + C = 0$, which in Cartesian coordinates $z = x + iy, B = u + iv$ expands to $2(ux - vy) + C = 0$, the standard equation of a straight line (since $|B|^2 > 0 \implies (u, v) \neq (0, 0)$).
    <2>2. If $A \neq 0$, dividing by $A$ and completing the square yields $|z + \frac{\overline{B}}{A}|^2 = \frac{|B|^2 - AC}{A^2}$, which is a circle with center $-\frac{\overline{B}}{A}$ and radius $R = \frac{\sqrt{|B|^2 - AC}}{|A|} > 0$.

<1>2. Factorization into elementary transformations:
    Every Möbius transformation is a composition of transformations of the following three types:
    1. Translations: $T(z) = z + z_0$ for $z_0 \in \mathbb{C}$.
    2. Homotheties (dilations and rotations): $T(z) = \alpha z$ for $\alpha \in \mathbb{C}^\times$.
    3. Inversion: $T(z) = \frac{1}{z}$.
    *Proof:*
    <2>1. If $c = 0$, then $T(z) = \frac{a}{d} z + \frac{b}{d}$, which is a homothety followed by a translation.
    <2>2. If $c \neq 0$, algebraic decomposition gives:
        $$T(z) = \frac{az+b}{cz+d} = \frac{a}{c} + \frac{bc - ad}{c^2} \cdot \frac{1}{z + \frac{d}{c}}.$$
        This is the composition of translation $z \mapsto z + \frac{d}{c}$, inversion $w \mapsto \frac{1}{w}$, homothety $u \mapsto \frac{bc - ad}{c^2} u$, and translation $v \mapsto v + \frac{a}{c}$.

<1>3. Invariance under elementary transformations:
    Each elementary transformation maps generalized circles to generalized circles.
    *Proof:*
    <2>1. Translation $w = z + z_0 \implies z = w - z_0$:
        Substituting into the general equation gives:
        $$A |w - z_0|^2 + B(w - z_0) + \overline{B}(\overline{w} - \overline{z_0}) + C = 0$$
        $$A |w|^2 + (B - A\overline{z_0}) w + \overline{(B - A\overline{z_0})} \overline{w} + (A|z_0|^2 - B z_0 - \overline{B}\overline{z_0} + C) = 0,$$
        which has the form of a generalized circle with $A' = A \in \mathbb{R}$.
    <2>2. Homothety $w = \alpha z \implies z = \frac{w}{\alpha}$ with $\alpha \neq 0$:
        Substituting into the general equation gives:
        $$A \left|\frac{w}{\alpha}\right|^2 + B \frac{w}{\alpha} + \overline{B} \frac{\overline{w}}{\overline{\alpha}} + C = 0 \iff \frac{A}{|\alpha|^2} |w|^2 + \frac{B}{\alpha} w + \overline{\left(\frac{B}{\alpha}\right)} \overline{w} + C = 0,$$
        which is a generalized circle with $A' = \frac{A}{|\alpha|^2} \in \mathbb{R}$.
    <2>3. Inversion $w = \frac{1}{z} \implies z = \frac{1}{w}$:
        For $w \neq 0$, multiplying the equation by $|w|^2$ gives:
        $$A \left|\frac{1}{w}\right|^2 + B \frac{1}{w} + \overline{B} \frac{1}{\overline{w}} + C = 0 \iff A + B \overline{w} + \overline{B} w + C |w|^2 = 0 \iff C |w|^2 + \overline{B} w + B \overline{w} + A = 0.$$
        This is a generalized circle with $A' = C \in \mathbb{R}$, $B' = \overline{B} \in \mathbb{C}$, and $C' = A \in \mathbb{R}$, with $|B'|^2 - A'C' = |B|^2 - AC > 0$.

<1>4. Conclusion:
    Since any Möbius transformation is a composition of elementary transformations (<1>2), and each elementary transformation preserves the family of generalized circles (<1>3), every Möbius transformation maps straight lines and circles onto straight lines and circles. Q.E.D.
:::
