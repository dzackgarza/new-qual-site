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
The \dfn{residue field} at $x \in X$ is $\kappa(x) \coloneqq \OO_{X,x}/\mfm_x$; for $x = \mfp \in \Spec A$ this is $\Frac(A/\mfp) \cong A_\mfp/\mfp A_\mfp$.
To \dfn{evaluate} $f \in \OO_X(U)$ at $x$ is to take its image under $\OO_X(U) \to \OO_{X,x} \to \kappa(x)$.

A \dfn{closed point} is a point whose closure is itself. On $\Spec A$, the closed points are exactly the maximal ideals of $A$.
A \dfn{generic point} of an irreducible closed subset $Z$ is a point $\eta\in Z$ with $\closure{\theset{\eta}} = Z$.
For a $k$-scheme $X$, a \dfn{rational point} over $k$ is a point $x\in X$ for which the structure map $k\to\kappa(x)$ is an isomorphism.

Write $\tilde x \leadsto x$, "$\tilde x$ \dfn{specialises} to $x$", when $x \in \closure{\theset{\tilde x}}$; equivalently $\mfp_{\tilde x} \subseteq \mfp_x$ when both points lie in an affine open $\Spec A$.
:::

::: {.definition title="General points and general fibres"}
Let $X$ be an irreducible scheme.
A property holds at a \dfn{general point} of $X$ if there is a dense open $U \subseteq X$ such that it holds at every point of $U$.
For a morphism $f \colon X \to Y$ with $Y$ irreducible, a property holds for the \dfn{general fibre} of $f$ if there is a dense open $V \subseteq Y$ such that the fibre $X_y$ has it for every $y \in V$.
:::

::: {.example}
General and generic are different notions.
The generic point is one actual point $\eta$, whereas saying that a property holds at a general point means that it holds at every point of some dense open subset.
Consequently a general-point property always holds at $\eta$.
The converse can fail: on $\AA^1_k=\Spec k[t]$ over an algebraically closed field, the property
$$
\operatorname{trdeg}_k\kappa(x)=1
$$
holds at the generic point $\eta$, where $\kappa(\eta)=k(t)$, but not at any closed point, so it does not hold on any dense open subset.
Conversely, "$\kappa(x)=k$" holds at every closed point but is not a general-point property, because every nonempty open subset contains $\eta$.
For the family $V(xy - t) \to \AA^1_t$, each fibre $xy=c$ with $c\neq0$ is a smooth affine curve isomorphic to $\GG_m$, while the generic fibre is the curve $xy=t$ over the field $k(t)$.
:::

::: {.remark}
A section of the structure sheaf evaluates in the residue field $\kappa(x)$, which can vary with $x$; so a section is not in general a function from $\abs X$ to one fixed field.
On $\Spec \ZZ$ the element $5$ evaluates to $0 \in \FF_5$, to $5 \in \FF_7$, and to $5 \in \QQ$ at the generic point.
On a nonreduced scheme a function can be nonzero and vanish at every point: $\eps \in k[\eps]/\eps^2$.

Specialisation orders the points by inclusion of primes. For a variety over an algebraically closed field, its classical closed points are the maximal elements of this order.
If $R$ is a DVR with fraction field $K$ and residue field $\kappa$, then the generic point of $\Spec R$ has residue field $K$ and specialises to its unique closed point, whose residue field is $\kappa$. The valuative criteria for separatedness and properness quantify over diagrams containing morphisms $\Spec K\to X$ and $\Spec R\to Y$ and ask for uniqueness or existence of a lift $\Spec R\to X$.
:::
