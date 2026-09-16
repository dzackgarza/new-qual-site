---
schema: qual/card@1
id: D-CRVPLSING
kind: definition
title: Node, cusp and tacnode, and the delta invariant that runs the genus formula
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
\[
\delta_p \da \dim_k \qty{ \qty{\nu_* \OO_{\tilde C} / \OO_C}_p } ,
\]
a finite number, and $r_p$ denotes the number of analytic branches of $C$ at $p$.
:::

::: {.definition title="The three that get named"}
Up to analytic isomorphism at the origin:

| name | equation | $r_p$ | $\delta_p$ |
| --- | --- | --- | --- |
| node, $A_1$ | $y^2 = x^2$ | $2$ | $1$ |
| cusp, $A_2$ | $y^2 = x^3$ | $1$ | $1$ |
| tacnode, $A_3$ | $y^2 = x^4$ | $2$ | $2$ |

More generally $A_n : y^2 = x^{n+1}$ has $\delta_p = \floor{(n+1)/2}$, and an ordinary point of multiplicity $r$, meaning $r$ smooth branches with distinct tangents, has $\delta_p = \binom{r}{2}$.
:::

::: {.proposition title="Genus drop"}
\[
p_a(C) - g(\tilde C) = \sum_{p \in \Sing C} \delta_p .
\]
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

::: {.remark title="What the normal forms are actually distinguishing"}
Node and cusp both have $\delta_p = 1$ and are separated by the branch count, not by the genus drop: a nodal and a cuspidal plane cubic both have geometric genus $0$.
The invariant that tells them apart is $r_p$, and it is what the normalisation sees — the node pulls back to two points and the cusp to one.
This is why [[FE-ADOKK]] gets different Picard groups for the two: $\GG_m$ for the node, $\GG_a$ for the cusp.

Node and tacnode both have two branches and are separated by $\delta_p$: the tacnode's branches are tangent, so they agree to second order and cost two.
The rule behind the table is that $\delta_p$ counts conditions, and tangency is one more condition than crossing.

The Milnor number collects both, by $\mu_p = 2\delta_p - r_p + 1$: the node and the cusp have $\mu = 1, 2$ and the tacnode $\mu = 3$, which is the $n$ in $A_n$.
:::

::: {.remark title="Why nodes are the ones that appear"}
A general projection to $\PP^2$ produces nodes and nothing worse, which is the content of [[T-CRVEMBP3]]. Cusps and tacnodes need a coincidence — the centre of projection on a tangent line, or on a line meeting the curve in two tangentially-related points — and those are codimension-one conditions on the centre, so a general centre avoids them.
The practical consequence is that a curve presented as a plane model with a cusp or a tacnode was not obtained by a general projection, and the fact is usually the point of the question.
:::
