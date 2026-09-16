---
schema: qual/card@1
id: FE-O12TX
kind: example
title: The schemes that the classical picture cannot hold
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Nilpotents
  - Generic Points
relations:
- kind: uses
  target: PR-6TCSJ
review: draft
prompts:
- Give a scheme that is not a variety, and say what it records.
- Show that a regular function on an affine scheme is not determined by its values at points.
---

::: {.example title="The double point"}
$\Spec k[\varepsilon]/(\varepsilon^2)$ has one point and a two-dimensional ring of functions.
It is the scheme-theoretic intersection of the parabola $y = x^2$ with the line $y = 0$, and it is what distinguishes tangency from transversality: the reduced intersection is a single point either way.

The function $\varepsilon$ is nonzero, but its value at the unique point, its image in the residue field $k[\varepsilon]/(\varepsilon) = k$, is $0$; so $\varepsilon$ and $0$ are different functions with the same values at every point.

Its $k$-points valued in a $k$-algebra compute tangent vectors: a morphism $\Spec k[\varepsilon]/(\varepsilon^2) \to X$ is a point of $X$ together with an element of $T_p X$.
:::

::: {.example title="Two points that are not the same size"}
$\Spec \ZZ$ has a closed point for each prime and a dense generic point $(0)$.
Its residue fields are $\FF_p$ and $\QQ$, so the "functions" on it take values in different fields at different points.
:::

::: {.example title="Values of a regular function on $D(6) \subseteq \Spec \ZZ$"}
The distinguished open set $D(6) \subseteq \Spec \ZZ$ consists of the generic point $(0)$ and the points $(p)$ for primes $p \neq 2, 3$, and $\OO_{\Spec \ZZ}(D(6)) \cong \ZZ[1/6]$.
So $\varphi = 5/6$ is a regular function on $D(6)$, and its value at a point is its image in the residue field there.

- At $(0)$, the value is $5/6 \in \QQ = \kappa((0))$.

- At $(p)$ with $p \neq 2, 3$, the value is $\bar{5} \cdot \bar{6}^{-1} \in \FF_p = \kappa((p))$.
  Hence $\varphi$ vanishes at $(5)$, and $\varphi((11)) = \bar{5} \cdot \bar{2} = \bar{10} \in \FF_{11}$, since $\bar{6} \cdot \bar{2} = \bar{1}$ in $\FF_{11}$.
:::

::: {.example title="A nonreduced multiple structure"}
$\Spec k[x]/(x^2)$ and $\Spec k[x]/(x)$ have the same topological space.
The first is the fibre of $\AA^1 \to \AA^1$, $t \mapsto t^2$, over the branch point, and its length $2$ is what makes the degree of that map constant.
:::

::: {.remark}
The three examples are the three things schemes add: nilpotents record multiplicity, generic points record "generically", and arithmetic rings make the base something other than a field.
Any one of them is a sufficient answer to why the classical language was replaced.
:::
