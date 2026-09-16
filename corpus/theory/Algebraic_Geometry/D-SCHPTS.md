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
The **residue field** at $x \in X$ is $\kappa(x) \da \OO_{X,x}/\mfm_x$; for $x = \mfp \in \Spec A$ this is $\Frac(A/\mfp) = A_\mfp/\mfp A_\mfp$.
To **evaluate** $f \in \OO_X(U)$ at $x$ is to take its image under $\OO_X(U) \to \OO_{X,x} \to \kappa(x)$.

A **closed point** is one whose closure is itself, corresponding to a maximal ideal in an affine chart.
A **generic point** of an irreducible closed $Z$ is $\eta$ with $\closure{\ts{\eta}} = Z$.
For $X$ over $k$, a **rational point** is an $x$ with $\kappa(x) = k$.

Write $\tilde x \leadsto x$, "$\tilde x$ **specialises** to $x$", when $x \in \closure{\ts{\tilde x}}$; equivalently $\mfp_{\tilde x} \subseteq \mfp_x$ in an affine chart.
:::

::: {.definition title="General points and general fibres"}
Let $X$ be an irreducible scheme.
A property holds at a \dfn{general point} of $X$ if there is a dense open $U \subseteq X$ such that it holds at every point of $U$.
For a morphism $f \colon X \to Y$ with $Y$ irreducible, a property holds for the \dfn{general fibre} of $f$ if there is a dense open $V \subseteq Y$ such that the fibre $X_y$ has it for every $y \in V$.
:::

::: {.example}
General and generic differ.
On $\AA^1_k = \Spec k[t]$ over an algebraically closed field $k$, the property "$\kappa(x) = k$" holds at a general point, since it holds at every closed point and the closed points form the dense open set $\AA^1_k \setminus \{\eta\}$, but it fails at the generic point $\eta$, where $\kappa(\eta) = k(t)$.
For the family $V(xy - t) \to \AA^1_t$, the general fibre is a smooth conic $xy = c$ with $c \neq 0$, while the generic fibre is the curve $xy = t$ over the field $k(t)$.
:::

::: {.remark}
The unfamiliar point, and the one an examiner presses on, is that a "function" on a scheme takes values in different fields at different points, so it is not a function on a set in any useful sense.
On $\Spec \ZZ$ the element $5$ evaluates to $0 \in \FF_5$, to $5 \in \FF_7$, and to $5 \in \QQ$ at the generic point.
On a nonreduced scheme a function can be nonzero and vanish at every point: $\eps \in k[\eps]/\eps^2$.
This is why $\OO_X$ is a sheaf of rings imposed on the space rather than extracted from it.

Specialisation orders the points by inclusion of primes, so a scheme carries a partial order of which the classical picture only ever sees the minimal elements.
A DVR is the smallest interesting example: $\Spec R$ is a generic point specialising to one closed point, and a morphism $\Spec R \to X$ is a choice of specialisation together with a valuation, which is exactly the data the valuative criteria for separatedness and properness test.
:::
