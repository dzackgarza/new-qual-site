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
  target: PR-QX0VL
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
Every neighborhood of either origin contains the common generic point, so neighborhoods of the two origins always meet [@Har10a, Example II.4.0.1].

The diagonal $\Delta_{X/k}:X\to X\times_kX$ is not closed.
On the open subset $U\times_kV\cong\Spec k[u,v]$, its image is $V(u-v)\cap D(u)$.
The closure is the whole line $V(u-v)$, which contains $(0_U,0_V)$, a point not on the diagonal.
Thus $X$ is not separated over $k$.
:::

::: {.remark}
The two chart inclusions $\AA_k^1\to X$ agree on the punctured affine line but send the origin to different points.
For comparison, two $S$-morphisms from a reduced $S$-scheme $Z$ to a separated $S$-scheme $Y$ that agree on a dense open subset of $Z$ are equal [@Har10a, Exercise II.4.2], as proved in [[P-AGH242AGREEDENSE]].
The reducedness of the source and separatedness of the target are separate hypotheses ([[PR-QX0VL]]).
Here the source $\AA_k^1$ is reduced, so the conclusion fails only because $X$ is not separated.
The doubled line is also a standard example of a scheme that is not a classical variety, which shows why separatedness is imposed in the scheme-theoretic definition of a variety.
:::

::: {.example title="A nonreduced source and a separated target"}
Put $R=k[t,\varepsilon]/(\varepsilon^2,t\varepsilon)$ and $Z=\Spec R$.
Its underlying space is $\Spec k[t]$, since quotienting by the nilpotent ideal $(\varepsilon)$ does not change the prime spectrum.
Thus $D(t)$ is dense in $Z$.
The two ring homomorphisms
$$
k[z]\rightrightarrows R,\qquad z\longmapsto0,\quad z\longmapsto\varepsilon
$$
define distinct morphisms $Z\to\AA_k^1$: the class of $\varepsilon$ is nonzero, as its image in $R/(t)=k[\varepsilon]/(\varepsilon^2)$ is nonzero.
They agree on $D(t)$ because $t\varepsilon=0$ makes $\varepsilon$ zero after inverting $t$.
The target is affine and therefore separated; the failure of dense-open uniqueness here comes from the nonreduced source, not from the target.
:::

::: {.remark}
The calculation of [[P-AGH274AMPLESEP|invertible sheaves on $X$]] gives $\Pic(X)\cong\ZZ$.
Only the trivial class is globally generated, and no class is ample.
:::
