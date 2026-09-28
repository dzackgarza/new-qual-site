---
schema: qual/card@1
id: P-HCAX24
kind: problem
title: The modular group and its action on the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Modular Group
relations: []
review: draft
---

::: {.problem}
Define the modular group and describe its action on the upper half-plane.
:::

::: {.solution}
<1>1. The modular group is
$$
\boxed{PSL_2(\mathbb Z)=SL_2(\mathbb Z)/\{\pm I\}}.
$$
::: {.proof}
Thus an element is represented by a matrix
$$
\gamma=
\begin{pmatrix}a&b\\ c&d\end{pmatrix},
\qquad a,b,c,d\in\mathbb Z,
\quad ad-bc=1,
$$
with a matrix identified with its negative.
:::

<1>2. The modular group acts on $\mathbb H$ by Möbius transformations.
::: {.proof}
For
$$
\mathbb H=\{z\in\mathbb C:\operatorname{Im}z>0\},
$$
define
$$
\gamma\cdot z=\frac{az+b}{cz+d}.
$$
Replacing $\gamma$ by $-\gamma$ does not change this fraction, so the formula is well-defined on $PSL_2(\mathbb Z)$. Moreover,
$$
\operatorname{Im}(\gamma\cdot z)
=\frac{\operatorname{Im}z}{|cz+d|^2}>0,
$$
so every group element preserves $\mathbb H$. Matrix multiplication corresponds to composition of the associated Möbius transformations, hence this is a group action.
:::

<1>3. Q.E.D.
::: {.proof}
Steps <1>1--<1>2 give the requested definition and action.
:::
:::
