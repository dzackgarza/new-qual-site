---
schema: qual/card@1
id: P-3YESG
kind: problem
title: "State the standard Schwarz reflection principle involving\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - schwarz-reflection
  - fractional-linear-transformations
  - maximum-modulus-principle
relations: []
review: draft
---

::: problem
State the standard Schwarz reflection principle involving reflection across the real axis.

Give a linear fractional transformation $T$ mapping $\DD$ to $\HH$.
Let $g(z) = \bar z$, and show
\[  
(T^{-1} \circ g \circ T)(z) = 1/\bar z
.\]

Suppose that $f$ is holomorphic on $\DD$, continuous on $\bar \DD$, and real on $S^1$.
Show that $f$ must be constant.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) State the Schwarz reflection principle across the real axis; (2) give a Möbius map $T: \DD \to \HH$ and verify $T^{-1}\circ g \circ T = 1/\bar z$ for $g(z) = \bar z$; (3) show $f$ holomorphic on $\DD$, continuous on $\bar\DD$, real on $S^1$, must be constant.

<1>1. Statement of the Schwarz reflection principle (real axis).
    Proof: Let $\Omega \subseteq \HH$ be a domain whose boundary contains an open interval $I$ of the real axis, and let $f$ be holomorphic on $\Omega$, continuous on $\Omega \cup I$, with $\Im f(z) \to 0$ as $z \to I$ (equivalently $f$ real on $I$). Then $f$ extends holomorphically across $I$ to $\Omega \cup I \cup \overline\Omega$ by $f(\bar z) = \overline{f(z)}$.

<1>2. Give $T: \DD \to \HH$.
    Proof: $T(z) = i\frac{1 + z}{1 - z}$ maps the unit disk onto the upper half-plane (the Cayley transform): $z \in \DD$ iff $\Im T(z) > 0$. Its inverse is $T^{-1}(w) = \frac{w - i}{w + i}$.

<1>3. Verify $T^{-1} \circ g \circ T = 1/\bar z$ with $g(z) = \bar z$.
    Proof: Compute: $g(T(z)) = \overline{T(z)} = \overline{i\frac{1+z}{1-z}} = -i\frac{1+\bar z}{1 - \bar z}$. Then $T^{-1}(\overline{T(z)}) = \frac{\overline{T(z)} - i}{\overline{T(z)} + i} = \frac{-i\frac{1+\bar z}{1-\bar z} - i}{-i\frac{1+\bar z}{1-\bar z} + i} = \frac{-i(1+\bar z) - i(1 - \bar z)}{-i(1+\bar z) + i(1-\bar z)} = \frac{-2i}{-2i\bar z} = \frac{1}{\bar z}$.

<1>4. Setup for (3): $F = f \circ T^{-1}$ is holomorphic on $\HH$, continuous on $\bar\HH$, and real on $\RR$; extend by reflection to an entire function.
    Proof: $T^{-1}$ maps $\HH$ onto $\DD$ and $\RR$ onto $S^1 \setminus \{1\}$; since $f$ is real on $S^1$, $F$ is real on $\RR$ (minus possibly one point, removable). By the reflection principle (<1>1), $F$ extends holomorphically to all of $\CC$ via $F(\bar w) = \overline{F(w)}$, and the extension is bounded on the compact... rather: $f$ is bounded on the compact $\bar\DD$ (continuous), so $F$ is bounded on $\bar\HH$; the reflected extension is bounded on the lower half-plane too, hence $F$ is a bounded entire function. By Liouville, $F$ is constant.

<1>5. Q.E.D.
    Proof: <1>4: $F$ constant ⟹ $f$ constant. All three parts done: <1>1 states the principle, <1>2–<1>3 handle the Cayley transform computation, <1>4–<1>5 prove constancy.

:::
