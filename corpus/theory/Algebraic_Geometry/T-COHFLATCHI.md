---
schema: qual/card@1
id: T-COHFLATCHI
kind: theorem
title: Flatness is constancy of the Hilbert polynomial
slogan: 'For coherent sheaves on projective space over an integral Noetherian base, flatness is exactly constancy of the fibre Hilbert polynomial.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Families
  - Hilbert Polynomial
  - Euler Characteristic
relations:
- kind: uses
  target: D-COHEULER
review: draft
prompts:
- What does flatness do to the Hilbert polynomial?
- Give a family that is not flat, and say which invariant jumps.
---

::: {.theorem}
Let $T$ be an integral Noetherian scheme and $\mcf$ a coherent sheaf on $\PP^n_T$.
Then $\mcf$ is flat over $T$ exactly when the Hilbert polynomial of $\restrictionof{\mcf}{\PP^n_t}$ is the same for every $t \in T$.
:::

::: {.remark}
For a closed subscheme $X\subseteq\PP_T^n$, apply the theorem to $\mcf=\OO_X$. Flatness of $X\to T$ is then equivalent to constancy of the fibre Hilbert polynomial.

For such a flat projective family, the fibre dimension, degree, arithmetic genus, and Euler characteristic $\chi(\OO_{X_t})$ are determined by the common Hilbert polynomial and are therefore constant. Properties not determined by the Hilbert polynomial may change: irreducibility, reducedness, smoothness, and Picard number need not be constant in a flat family. A flat family of plane conics can specialize from smooth conics to a double line while retaining the polynomial $2m+1$.

If $X$ is a smooth variety and $Z\subseteq X$ is a smooth closed subvariety of codimension $c\geq2$, the blowup $\Bl_ZX\to X$ is not flat: its generic fibre is a point, whereas the fibre over a point of $Z$ is $\PP^{c-1}$. This does not apply to a blowup along an effective Cartier divisor, which is an isomorphism.
:::
