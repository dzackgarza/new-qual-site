---
schema: qual/card@1
id: D-SCHPTS
kind: definition
title: Closed, rational and generic points; specialisation
classification:
  areas:
  - algebraic-geometry
  topics:
  - Generic Points
  - Residue Fields
  - Specialisation
relations:
- kind: uses
  target: PR-6TCSJ
review: draft
prompts:
- What is the residue field at a point, and what does it mean to evaluate a function there?
- What is a rational point? A closed point? A generic point?
- What is specialisation?
- What is the difference between a general point and the generic point?
---

::: {.definition}
The \dfn{residue field} at $x \in X$ is $\kappa(x) \definedas \OO_{X,x}/\mfm_x$; for $x = \mfp \in \Spec A$ this is $\Frac(A/\mfp) = A_\mfp/\mfp A_\mfp$.
To \dfn{evaluate} $f \in \OO_X(U)$ at $x$ is to take its image under $\OO_X(U) \to \OO_{X,x} \to \kappa(x)$.

A \dfn{closed point} is one whose closure is itself, corresponding to a maximal ideal in an affine chart.
A \dfn{generic point} of an irreducible closed $Z$ is $\eta$ with $\closure{\theset{\eta}} = Z$.
For $X$ over $k$, a \dfn{rational point} is an $x$ with $\kappa(x) = k$.

Write $\tilde x \leadsto x$, "$\tilde x$ \dfn{specialises} to $x$", when $x \in \closure{\theset{\tilde x}}$; equivalently $\mfp_{\tilde x} \subseteq \mfp_x$ in an affine chart.
:::

::: {.definition title="General points and general fibres"}
Let $X$ be an irreducible scheme.
A property holds at a \dfn{general point} of $X$ if there is a dense open $U \subseteq X$ such that it holds at every point of $U$.
For a morphism $f \colon X \to Y$ with $Y$ irreducible, a property holds for the \dfn{general fibre} of $f$ if there is a dense open $V \subseteq Y$ such that the fibre $X_y$ has it for every $y \in V$.
:::

::: {.example}
Every nonempty open subset of an irreducible scheme contains its generic point.
On $\AA^1_k = \Spec k[t]$ over an algebraically closed field $k$, the property "$\kappa(x) = k$" holds at every closed point and fails at the generic point $\eta$, where $\kappa(\eta) = k(t)$; the set of closed points is dense but not open.
For the family $V(xy - t) \to \AA^1_t$, the general fibre is a smooth conic $xy = c$ with $c \neq 0$, while the generic fibre is the curve $xy = t$ over the field $k(t)$.
:::

::: {.remark}
A section of the structure sheaf evaluates in the residue field $\kappa(x)$, which can vary with $x$; so a section is not in general a function from $\abs X$ to one fixed field.
On $\Spec \ZZ$ the element $5$ evaluates to $0 \in \FF_5$, to $5 \in \FF_7$, and to $5 \in \QQ$ at the generic point.
On a nonreduced scheme a nonzero section can vanish at every point: $\eps \in k[\eps]/\eps^2$.
So a section of $\OO_X$ is not determined by its values at the points of $X$.

Specialisation is a partial order on the points of a scheme; on $\Spec A$ it is inclusion of primes.
For a variety over an algebraically closed field, the points of the classical variety are the closed points of the associated scheme.
For a discrete valuation ring $R$ with fraction field $K$, $\Spec R$ consists of a generic point specialising to a closed point, and the valuative criteria ([[D-8XX95]]) test lifts of morphisms $\Spec K\to X$ to $\Spec R$.
:::
