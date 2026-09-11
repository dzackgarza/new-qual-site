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
---

::: {.example title="The double point"}
$\Spec k[\varepsilon]/(\varepsilon^2)$ has one point and a two-dimensional ring of functions.
It is the scheme-theoretic intersection of the parabola $y = x^2$ with the line $y = 0$, and it is what distinguishes tangency from transversality: the reduced intersection is a single point either way.

Its $k$-points valued in a $k$-algebra compute tangent vectors: a morphism $\Spec k[\varepsilon]/(\varepsilon^2) \to X$ is a point of $X$ together with an element of $T_p X$.
:::

::: {.example title="Two points that are not the same size"}
$\Spec \ZZ$ has a closed point for each prime and a dense generic point $(0)$.
Its residue fields are $\FF_p$ and $\QQ$, so the "functions" on it take values in different fields at different points.
:::

::: {.example title="A nonreduced multiple structure"}
$\Spec k[x]/(x^2)$ and $\Spec k[x]/(x)$ have the same topological space.
The first is the fibre of $\AA^1 \to \AA^1$, $t \mapsto t^2$, over the branch point, and its length $2$ is what makes the degree of that map constant.
:::

::: {.remark}
The three examples are the three things schemes add: nilpotents record multiplicity, generic points record "generically", and arithmetic rings make the base something other than a field.
Any one of them is a sufficient answer to why the classical language was replaced.
:::
