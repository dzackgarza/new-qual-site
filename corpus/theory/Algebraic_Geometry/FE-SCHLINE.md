---
schema: qual/card@1
id: FE-SCHLINE
kind: example
title: The line with a doubled origin
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Separatedness
  - Gluing
  - Separated Morphisms
  - Reduced Schemes
  - Counterexamples
relations:
- kind: uses
  target: D-SCHGLUE
- kind: uses
  target: P-AGH242AGREEDENSE
review: draft
prompts:
- Give a scheme that is not separated.
- Why is the diagonal used to define separatedness?
- Give an example of a non-separated morphism.
- Give two morphisms agreeing on a dense open that are not equal.
---

::: {.example}
Let $k$ be a field.
Glue $U=\Spec k[t]$ and $V=\Spec k[t]$ along $\Spec k[t,t^{-1}]$ by the identity.
The resulting scheme $X$ has two origins $0_U,0_V$.
Every neighborhood of either origin contains the common generic point, so neighborhoods of the two origins always meet [@Har77, Example II.4.0.1].

The diagonal $\Delta_{X/k}:X\to X\times_kX$ is not closed.
On the open subset $U\times_kV\cong\Spec k[u,v]$, its image is $V(u-v)\cap D(u)$.
The closure is the whole line $V(u-v)$, which contains $(0_U,0_V)$, a point not on the diagonal.
Thus $X$ is not separated over $k$.
:::

::: {.remark}
The two chart inclusions $\AA_k^1\to X$ agree on the punctured affine line but send the origin to different points.
For comparison, two $S$-morphisms from a reduced $S$-scheme $Z$ to a separated $S$-scheme $Y$ that agree on a dense open subset of $Z$ are equal [@Har77, Exercise II.4.2], as proved in [[P-AGH242AGREEDENSE]].
The reducedness of the source and separatedness of the target are separate hypotheses ([[P-AGH242AGREEDENSE|morphisms agreeing on a dense open subset]]).
Here the source $\AA_k^1$ is reduced, so the conclusion fails only because $X$ is not separated.
The doubled line is also a standard example of a scheme that is not a classical variety, which shows why separatedness is imposed in the scheme-theoretic definition of a variety.
:::

::: {.remark}
For the doubled line $X$, the calculation of [[P-AGH274AMPLESEP|invertible sheaves on the doubled line]] gives $\Pic(X)\cong\ZZ$.
Only the trivial class is globally generated, and no class is ample.
:::
