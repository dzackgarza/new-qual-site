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
$$
f^{-1}:Y\to X
$$
and the composite
$$
g\circ f:X\to Z
$$
are homeomorphisms.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $f$ is a homeomorphism,
$$
f^{-1}:Y\to X
$$
is bijective.


::: pf-proof

The inverse of any bijection is again a bijection.

:::

:::

::: {.pf-step #s1-2}

The map
$$
f^{-1}:Y\to X
$$
is continuous.


::: pf-proof

This is part of the definition of a homeomorphism:
$f$ is a continuous bijection whose inverse is continuous.

:::

:::

::: {.pf-step #s1-3}

The inverse of
$$
f^{-1}
$$
is
$$
f,
$$
which is continuous.


::: pf-proof

By definition,
$$
(f^{-1})^{-1}=f.
$$
Since $f$ is a homeomorphism, it is continuous.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
f^{-1}:Y\to X
\text{ is a homeomorphism}.
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} show that $f^{-1}$ is a continuous bijection with
continuous inverse.

:::

:::

::: {.pf-step #s1-5}

The composite
$$
g\circ f:X\to Z
$$
is bijective.


::: pf-proof

The composition of bijections is a bijection.

:::

:::

::: {.pf-step #s1-6}

The composite
$$
g\circ f
$$
is continuous.


::: pf-proof

Both
$$
f:X\to Y
$$
and
$$
g:Y\to Z
$$
are continuous.
The composition of continuous maps is continuous.

:::

:::

::: {.pf-step #s1-7}

The inverse of the composite is
$$
(g\circ f)^{-1}
=
f^{-1}\circ g^{-1}.
$$


::: pf-proof

Compute
$$
(f^{-1}\circ g^{-1})\circ(g\circ f)
=
f^{-1}\circ(g^{-1}\circ g)\circ f
=
f^{-1}\circ f
=
\operatorname{id}_X,
$$
and similarly
$$
(g\circ f)\circ(f^{-1}\circ g^{-1})
=
\operatorname{id}_Z.
$$

:::

:::

::: {.pf-step #s1-8}

The inverse
$$
f^{-1}\circ g^{-1}
$$
is continuous.


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
f^{-1}
$$
is continuous.
Because $g$ is a homeomorphism,
$$
g^{-1}
$$
is continuous.
Their composition is therefore continuous.

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
g\circ f:X\to Z
\text{ is a homeomorphism}.
}
$$


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-8){.pf-ref} show that $g\circ f$ is a continuous bijection with
continuous inverse.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the inverse statement, and step [](#s1-9){.pf-ref} proves the composition
statement.

:::

:::

:::
