---
schema: qual/card@1
id: T-BERTINI
kind: theorem
title: Bertini's theorem
classification:
  areas:
  - algebraic-geometry
  topics:
  - Bertini Theorem
  - Hyperplane Sections
  - Linear Systems
relations:
- kind: uses
  target: D-DIVLINSYS
review: draft
prompts:
- What is Bertini's theorem?
---

::: {.theorem title="Bertini's theorem for hyperplane sections"}
Let $X \subseteq \PP^n$ be a smooth projective variety over an algebraically closed field $k$ of any characteristic.
The hyperplanes $H \subseteq \PP^n$ with $H \not\supseteq X$ and $H \cap X$ smooth form a dense open subset of $(\PP^n)^\dual$.
If $X$ is irreducible of dimension at least $2$, then $H \cap X$ is moreover connected, hence irreducible, for $H$ in that open set.
:::

::: {.theorem title="Bertini's theorem for linear systems"}
Let $X$ be a smooth variety over an algebraically closed field of characteristic zero and let $\mathfrak{d}$ be a linear system on $X$.
Then a general member of $\mathfrak{d}$ is smooth away from the base locus of $\mathfrak{d}$.
:::

::: {.example}
The second statement fails in characteristic $p$.
On $\AA^2$ the pencil spanned by $x^p$ and $y^p$ has base locus the origin, and every member $a x^p + b y^p = (a^{1/p} x + b^{1/p} y)^p$ is a nonreduced line, singular at each of its points.
:::
