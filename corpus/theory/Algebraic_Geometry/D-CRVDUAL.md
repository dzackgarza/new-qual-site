---
schema: qual/card@1
id: D-CRVDUAL
kind: definition
title: The dual curve, and the Plücker formula for its degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Dual Curves
  - Singularities
relations:
- kind: uses
  target: D-CRVPLSING
review: draft
prompts:
- What is the dual curve?
---

::: {.definition title="Dual curve"}
Let $C \subseteq \PP^2$ be an irreducible plane curve over an algebraically closed field of characteristic $0$ that is not a line.
The \dfn{dual curve} $C^\vee \subseteq (\PP^2)^\vee$ is the closure of the set of tangent lines $T_p C$ at the smooth points $p$ of $C$; the map $p\mapsto T_pC$ is a morphism of $C$ to this dual curve [@Har77, Exercise I.7.3, Exercise IV.2.3].
Its degree is the \dfn{class} of $C$: the number of tangent lines to $C$ through a general point of $\PP^2$.
:::

::: {.theorem}
1. (Biduality) $(C^\vee)^\vee = C$.

2. (Plücker) If $C$ has degree $d$ and its only singularities are $\delta$ nodes and $\kappa$ ordinary cusps, then
$$\deg C^\vee = d(d-1) - 2\delta - 3\kappa.$$

The smooth case is [@Har77, Exercise IV.2.3(e)]: the morphism of part (a) sends $P$ to $T_PC\cap L$ for a line $L$ not tangent to $C$, and its degree is $d(d-1)$, so a smooth plane curve of degree $d\geq2$ has class $d(d-1)$.
The correspondence between the singularities of $C^\vee$ and the multiple tangents and inflections of $C$ is parts (b) and (c) of the same exercise: an ordinary node of $C^\vee$ is a bitangent of $C$ and an ordinary cusp an inflection, which is what the corrections $2\delta$ and $3\kappa$ count.
The formula with $\delta$ and $\kappa$ is not printed in Hartshorne; it follows from Hurwitz's theorem in IV.2 applied to $p\mapsto T_pC$ from the normalization of $C$, and no retained source prints it as a numbered statement, so it is recorded as stated and not as cited.
:::

::: {.example}
The dual of a smooth conic is a smooth conic.
The dual of a smooth plane cubic has degree $6$; its $9$ cusps correspond to the $9$ flexes of the cubic, and it has no nodes because a smooth cubic has no bitangents.
Its geometric genus is $\binom{5}{2} - 9 = 1$, equal to the genus of the cubic, since the Gauss map $C\to C^\vee$ is birational.
:::
