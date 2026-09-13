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
---

::: {.definition}
The **residue field** at $x \in X$ is $\kappa(x) \da \OO_{X,x}/\mfm_x$; for $x = \mfp \in \Spec A$ this is $\Frac(A/\mfp) = A_\mfp/\mfp A_\mfp$.
To **evaluate** $f \in \OO_X(U)$ at $x$ is to take its image under $\OO_X(U) \to \OO_{X,x} \to \kappa(x)$.

A **closed point** is one whose closure is itself, corresponding to a maximal ideal in an affine chart.
A **generic point** of an irreducible closed $Z$ is $\eta$ with $\closure{\ts{\eta}} = Z$.
For $X$ over $k$, a **rational point** is an $x$ with $\kappa(x) = k$.

Write $\tilde x \leadsto x$, "$\tilde x$ **specialises** to $x$", when $x \in \closure{\ts{\tilde x}}$; equivalently $\mfp_{\tilde x} \subseteq \mfp_x$ in an affine chart.
:::

::: {.remark}
The unfamiliar point, and the one an examiner presses on, is that a "function" on a scheme takes values in different fields at different points, so it is not a function on a set in any useful sense.
On $\Spec \ZZ$ the element $5$ evaluates to $0 \in \FF_5$, to $5 \in \FF_7$, and to $5 \in \QQ$ at the generic point.
On a nonreduced scheme a function can be nonzero and vanish at every point: $\eps \in k[\eps]/\eps^2$.
This is why $\OO_X$ is a sheaf of rings imposed on the space rather than extracted from it.

Specialisation orders the points by inclusion of primes, so a scheme carries a partial order of which the classical picture only ever sees the minimal elements.
A DVR is the smallest interesting example: $\Spec R$ is a generic point specialising to one closed point, and a morphism $\Spec R \to X$ is a choice of specialisation together with a valuation, which is exactly the data the valuative criteria for separatedness and properness test.
:::
