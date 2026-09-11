---
schema: qual/card@1
id: FE-DIVP1E
kind: example
title: Degree-zero divisors on the line and on an elliptic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Picard Group
  - Rational Curves
  - Elliptic Curves
relations:
- kind: uses
  target: PR-Y5S7V
review: draft
prompts:
- Show every degree-zero divisor on $\PP^1$ is principal.
- Is every degree-zero divisor on an elliptic curve principal?
- What is $\Pic(E)$ for $E$ elliptic?
---

::: {.example}
On $\PP^1$, any two points satisfy $[a] \sim [b]$ by $f(z) = (z-a)/(z-b)$.
Degree-zero divisors are sums of such differences, so $\Pic^0(\PP^1) = 0$ and $\Pic(\PP^1) \cong \ZZ$ by degree.
:::

::: {.example}
On an elliptic curve $E$, distinct points $p \neq q$ are never linearly equivalent: $p - q = \div(f)$ would make $f : E \to \PP^1$ a degree-one map, hence an isomorphism, contradicting $g(E) = 1 \neq 0 = g(\PP^1)$.
Instead $\Pic^0(E) \cong E$ by $p \mapsto [p - O]$, so $\Pic(E) \cong E \oplus \ZZ$.
:::

::: {.remark}
The contrast is the whole content: $\Pic^0$ measures how far the curve is from being rational, and it vanishes exactly for $\PP^1$.
A curve is rational precisely when it admits two distinct linearly equivalent points, which is the same as admitting a degree-one map to $\PP^1$.

The degree argument is the one to reproduce: a principal divisor $p - q$ gives a rational function with one simple zero and one simple pole, so the induced map to $\PP^1$ has degree one.
For a non-rational example, $y^2 = x^3 - x$ homogenised to $y^2 z = x^3 - xz^2$ is the standard witness, and the group law on it is exactly the isomorphism $E \cong \Pic^0(E)$.
:::
