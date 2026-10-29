---
schema: qual/card@1
id: FE-SRFCUBIC
kind: example
title: The cubic surface and its $27$ lines
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surface
  - Blowups
  - Rational Surfaces
relations:
- kind: uses
  target: FE-SRFBLOW
- kind: uses
  target: T-SRFADJ
review: draft
prompts:
- Why does a smooth cubic surface contain 27 lines?
- Describe the cubic surface as a blowup.
- What is the canonical divisor of a cubic surface?
---

::: {.example}
A smooth cubic surface $S \subseteq \PP^3$ is the blowup of $\PP^2$ at $6$ points in general position, embedded by the anticanonical system $\abs{-K_S} = \abs{3H - \sum_{i=1}^{6} E_i}$.
So $\Pic S = \ZZ^7$ with basis $H, E_1, \dots, E_6$, and $K_S^2 = 9 - 6 = 3 = \deg S$.
:::

::: {.proposition title="The 27 lines"}
A line on $S$ is a class $L$ with $L^2 = -1$ and $L \cdot K_S = -1$, and there are exactly $27$:

- the $6$ exceptional curves $E_i$;

- the $15$ strict transforms $H - E_i - E_j$ of the lines through two of the points;

- the $6$ strict transforms $2H - \sum_{j \neq i} E_j$ of the conics through five of the points.
:::

::: {.remark}
The count $6+15+6=27$ is a computation in $\Pic(S)$: a line has $L\cdot(-K_S)=\deg L=1$ because $-K_S$ is the hyperplane class, and adjunction
$-2=L^2+L\cdot K_S$ then gives $L^2=-1$, and enumerating the effective classes with these intersection numbers gives exactly the three families above.

A line on $S$ is a $(-1)$-curve, so each of the $27$ can be contracted; different choices of six pairwise disjoint lines realise $S$ as a blowup of $\PP^2$ in different ways, and the symmetry group of the configuration of $27$ lines is the Weyl group $W(E_6)$, of order $51840$.

That $S$ is anticanonically embedded is what makes it a del Pezzo surface of degree $3$; the same analysis with $9 - d$ blown-up points gives the del Pezzo surfaces of each degree, and the line counts $27$, $16$, $10$ follow the same way.
:::
