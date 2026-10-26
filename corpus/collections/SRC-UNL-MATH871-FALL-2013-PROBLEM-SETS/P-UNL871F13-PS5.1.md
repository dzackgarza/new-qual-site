---
schema: qual/card@1
id: P-UNL871F13-PS5.1
kind: problem
title: Inverses and compositions of homeomorphisms are homeomorphisms
classification:
  areas: [topology]
  topics: [Homeomorphisms]
relations: []
review: draft
---

::: {.problem}
Let $f:X\to Y$ and $g:Y\to Z$ be homeomorphisms.
Prove that the inverse map
\[
f^{-1}:Y\to X
\]
and the composite
\[
g\circ f:X\to Z
\]
are homeomorphisms.
:::

::: pf

::: pf-step

Since $f$ is a homeomorphism,
\[
f^{-1}:Y\to X
\]
is bijective.


::: pf-proof

The inverse of any bijection is again a bijection.

:::

:::

::: pf-step

The map
\[
f^{-1}:Y\to X
\]
is continuous.


::: pf-proof

This is part of the definition of a homeomorphism:
$f$ is a continuous bijection whose inverse is continuous.

:::

:::

::: pf-step

The inverse of
\[
f^{-1}
\]
is
\[
f,
\]
which is continuous.


::: pf-proof

By definition,
\[
(f^{-1})^{-1}=f.
\]
Since $f$ is a homeomorphism, it is continuous.

:::

:::

::: pf-step

Therefore
\[
\boxed{
f^{-1}:Y\to X
\text{ is a homeomorphism}.
}
\]


::: pf-proof

Steps <1>1--<1>3 show that $f^{-1}$ is a continuous bijection with
continuous inverse.

:::

:::

::: pf-step

The composite
\[
g\circ f:X\to Z
\]
is bijective.


::: pf-proof

The composition of bijections is a bijection.

:::

:::

::: pf-step

The composite
\[
g\circ f
\]
is continuous.


::: pf-proof

Both
\[
f:X\to Y
\]
and
\[
g:Y\to Z
\]
are continuous.
The composition of continuous maps is continuous.

:::

:::

::: pf-step

The inverse of the composite is
\[
(g\circ f)^{-1}
=
f^{-1}\circ g^{-1}.
\]


::: pf-proof

Compute
\[
(f^{-1}\circ g^{-1})\circ(g\circ f)
=
f^{-1}\circ(g^{-1}\circ g)\circ f
=
f^{-1}\circ f
=
\operatorname{id}_X,
\]
and similarly
\[
(g\circ f)\circ(f^{-1}\circ g^{-1})
=
\operatorname{id}_Z.
\]

:::

:::

::: pf-step

The inverse
\[
f^{-1}\circ g^{-1}
\]
is continuous.


::: pf-proof

By step <1>4,
\[
f^{-1}
\]
is continuous.
Because $g$ is a homeomorphism,
\[
g^{-1}
\]
is continuous.
Their composition is therefore continuous.

:::

:::

::: pf-step

Therefore
\[
\boxed{
g\circ f:X\to Z
\text{ is a homeomorphism}.
}
\]


::: pf-proof

Steps <1>5--<1>8 show that $g\circ f$ is a continuous bijection with
continuous inverse.

:::

:::

::: pf-qed

Step <1>4 proves the inverse statement, and step <1>9 proves the composition
statement.

:::

:::
