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
| underlying space has one point | $A_{\mathrm{red}}$ is a field |

If $A$ is Noetherian then $\Spec A$ is a Noetherian space; the converse fails, so Noetherianness is a one-way row and is not in the table.

More generally, a scheme $X$ is integral if and only if it is reduced and irreducible [@Har77, Proposition II.3.1].
If $A$ is Noetherian, the last row is also equivalent to $A$ being a local Artinian ring.

An irreducible scheme has a unique [[D-SCHPTS|generic point]] $\eta$. For $\Spec A$ integral, $\eta=(0)$ and $\kappa(\eta)\cong\Frac(A)$.
:::

::: {.proof}
**The table.** $\Spec A$ is reduced exactly when no nonzero element of $A$ is nilpotent, since the nilradical of $A$ is the intersection of its primes and a scheme is reduced exactly when all of its local rings are. Writing $N$ for the nilradical: $\Spec A$ is irreducible exactly when $N$ is prime, because $V(f)\cup V(g)=V(fg)$ makes $X=V(f)\cup V(g)$ a covering by closed sets, and $V(h)=X$ exactly when $h$ is nilpotent; conversely two proper closed subsets $V(I),V(J)$ with union $X$ give $f\in I\sm N$ and $g\in J\sm N$ with $fg\in N$. The integral row is the conjunction of the first two. For the connected row, an idempotent $e$ gives the clopen partition $X=V(e)\sqcup V(1-e)$, and a clopen partition gives the idempotent that is $1$ on one part and $0$ on the other. Finally $\Spec A$ is a single point exactly when $A$ has exactly one prime, and then $A_{\mathrm{red}}$ is a domain of dimension $0$, that is a field.

**Noetherianness, one way only.** Closed subsets of $\Spec A$ are the $V(I)$, so the ascending chain condition for closed subsets is the ascending chain condition for radical ideals, which a Noetherian $A$ satisfies; hence $\Spec A$ is a Noetherian space if $A$ is Noetherian.

The converse fails. Let $k$ be a field and
$$
A \coloneqq k[x_1,x_2,\ldots]/(x_i^2 : i\geq1).
$$
Every $x_i$ is nilpotent, so the nilradical is $\mfm=(x_1,x_2,\ldots)$ and every prime of $A$ contains $\mfm$; as $A/\mfm\cong k$, the ideal $\mfm$ is the only prime and $\Spec A$ is a one-point space, which is Noetherian. But $\mfm/\mfm^2$ has the images of the $x_i$ as a $k$-basis, so it is infinite dimensional, while for a finitely generated ideal $I$ the quotient $I/I^2$ is spanned by the images of a generating set; hence $\mfm$ is not finitely generated and $A$ is not Noetherian.
:::

::: {.remark}
The affine integral criterion follows from the first two rows: if $A$ is reduced, then its nilradical is $(0)$, and irreducibility says this ideal is prime.

For an integral scheme $X$ with generic point $\eta$, its function field is the residue field $\kappa(\eta)$.
:::
