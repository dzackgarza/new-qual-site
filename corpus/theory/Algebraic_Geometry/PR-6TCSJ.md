---
schema: qual/card@1
id: PR-6TCSJ
kind: proposition
title: Ring-theoretic criteria for affine schemes
slogan: 'For $X=\Spec A$, reducedness, irreducibility, integrality, connectedness, Noetherianity, and the one-point property have ring-theoretic criteria in $A$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Integral Schemes
  - Noetherian Schemes
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- When is $\Spec A$ reduced, irreducible, integral?
- What is the generic point of an irreducible scheme?
---

::: {.proposition}
For a ring $A$:

| $\Spec A$ | $A$ |
| --- | --- |
| reduced | no nonzero nilpotents |
| irreducible | the nilradical is prime |
| integral | a domain |
| connected | no nontrivial idempotents |
| Noetherian | Noetherian |
| underlying space has one point | $A_{\mathrm{red}}$ is a field |

More generally, a scheme $X$ is integral if and only if it is reduced and irreducible [@Har10a, Proposition II.3.1].
If $A$ is Noetherian, the last row is also equivalent to $A$ being a local Artinian ring.

An irreducible scheme has a unique [[D-SCHPTS|generic point]] $\eta$. For $\Spec A$ integral, $\eta=(0)$ and $\kappa(\eta)\cong\Frac(A)$.
:::

::: {.remark}
The affine integral criterion follows from the first two rows: if $A$ is reduced, then its nilradical is $(0)$, and irreducibility says this ideal is prime.

For an integral scheme $X$ with generic point $\eta$, its function field is the residue field $\kappa(\eta)$.
:::
