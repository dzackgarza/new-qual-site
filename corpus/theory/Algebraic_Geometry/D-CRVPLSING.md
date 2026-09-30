---
schema: qual/card@1
id: D-CRVPLSING
kind: definition
title: Node, cusp, and tacnode; the delta invariant and the genus formula
classification:
  areas:
  - algebraic-geometry
  topics:
  - Curves
  - Singularities
  - Genus
relations:
- kind: uses
  target: D-G1AEH
- kind: related-to
  target: T-CRVEMBP3
review: draft
prompts:
- Give the local normal forms distinguishing a node, a cusp and a tacnode.
- What is the delta invariant of a plane curve singularity?
- How does the arithmetic genus of a plane curve drop to the geometric genus?
---

::: {.definition title="Delta invariant"}
Let $p$ be a singular point of a curve $C$ with normalisation $\nu : \tilde C \to C$.
Then
$$
\delta_p \definedas \dim_k \qty{ \qty{\nu_* \OO_{\tilde C} / \OO_C}_p } ,
$$
a finite number, and $r_p$ denotes the number of analytic branches of $C$ at $p$.
:::

::: {.definition title="Node, cusp, and tacnode"}
Up to analytic isomorphism at the origin:

| name | equation | $r_p$ | $\delta_p$ |
| --- | --- | --- | --- |
| node, $A_1$ | $y^2 = x^2$ | $2$ | $1$ |
| cusp, $A_2$ | $y^2 = x^3$ | $1$ | $1$ |
| tacnode, $A_3$ | $y^2 = x^4$ | $2$ | $2$ |

A \dfn{node} is a singular point of multiplicity $2$ with two distinct tangent directions.
More generally $A_n : y^2 = x^{n+1}$ has $\delta_p = \floor{(n+1)/2}$, and an ordinary point of multiplicity $r$, meaning $r$ smooth branches with distinct tangents, has $\delta_p = \binom{r}{2}$.
:::

::: {.proposition title="Genus drop"}
$$
p_a(C) - g(\tilde C) = \sum_{p \in \Sing C} \delta_p .
$$
For a plane curve of degree $d$ this reads $g = \binom{d-1}{2} - \sum_p \delta_p$.
:::

::: {.proposition title="The genus formula with multiplicities"}
Let $C \subseteq \PP^2$ be an integral curve of degree $d$.
Resolve its singularities by successively blowing up singular points of the strict transforms, and let $m_i$ run over the multiplicities of all singular points met in this process, including the infinitely near points on the strict transforms.
Then
$$g(\tilde{C}) = \frac{1}{2}(d-1)(d-2) - \frac{1}{2} \sum_i m_i(m_i - 1).$$
If every singular point of $C$ is ordinary, no infinitely near singular points occur, and the sum runs over the singular points of $C$.
:::

::: {.example}
The tacnode $y^2 = x^4$ has multiplicity $2$ at the origin and $\delta = 2$.
One blowup, in the chart $y = x y_1$, gives the strict transform $y_1^2 = x^2$, which is a node at the origin: an infinitely near singular point of multiplicity $2$.
The two points contribute $\frac{1}{2}(2 \cdot 1 + 2 \cdot 1) = 2 = \delta$, while the origin alone would give $1$.
:::

::: {.remark title="Invariants separating the normal forms"}
Node and cusp both have $\delta_p = 1$ and are separated by the branch count: $\nu^{-1}(p)$ has two points for the node and one for the cusp.
A nodal and a cuspidal plane cubic both have geometric genus $0$, and their groups $\Pic^0$ are $\GG_m$ and $\GG_a$ respectively ([[FE-ADOKK]]).

Node and tacnode both have two smooth branches.
For a singular point with branches $B_1,\ldots,B_r$, $\delta_p=\sum_i\delta_p(B_i)+\sum_{i<j}(B_i\cdot B_j)_p$; for two smooth branches this is their intersection multiplicity, which is $1$ for the transverse branches $y=\pm x$ of the node and $2$ for the tangent branches $y=\pm x^2$ of the tacnode.

The Milnor number is $\mu_p = 2\delta_p - r_p + 1$: the node and the cusp have $\mu = 1, 2$ and the tacnode $\mu = 3$, which is the $n$ in $A_n$.
:::

::: {.remark title="Singularities of general projections"}
By [[T-CRVEMBP3]], projection of a smooth curve in $\PP^3$ from a general point is birational onto a plane curve whose only singularities are nodes.
The centres of projection that produce a cusp lie on a tangent line of the curve, and those that produce a tacnode lie on a secant line whose two tangent lines are coplanar; each set has dimension less than $3$, so a general centre avoids them.
:::
