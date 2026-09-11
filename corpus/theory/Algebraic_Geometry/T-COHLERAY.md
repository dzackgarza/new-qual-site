---
schema: qual/card@1
id: T-COHLERAY
kind: theorem
title: The Leray spectral sequence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Spectral Sequences
  - Higher Direct Images
  - Cohomology
relations:
- kind: uses
  target: D-COHRIF
review: draft
prompts:
- State the Leray spectral sequence.
- When does it degenerate, and what do you get?
---

::: {.theorem}
For $f: X \to Y$ and $\mcf$ a sheaf of abelian groups on $X$,
\[
E_2^{p,q} = H^p\qty{Y, R^q f_* \mcf} \Longrightarrow H^{p+q}(X, \mcf) .
\]
:::

::: {.remark}
It is the derived-functor form of $\globsec{X;\wait} = \globsec{Y;\wait} \circ f_*$, and the only thing usually needed from it is what happens when it degenerates.

If $R^{q>0} f_* \mcf = 0$, the sequence collapses to the edge and $H^i(X,\mcf) \cong H^i(Y, f_*\mcf)$ for all $i$; that is the affine-morphism case above.
In low degrees, with no vanishing at all, one always gets the exact sequence
\[
0 \to H^1(Y, f_* \mcf) \to H^1(X, \mcf) \to H^0(Y, R^1 f_* \mcf) \to H^2(Y, f_*\mcf) ,
\]
which is the form most often actually used: a class on $X$ is either pulled back from the base or detected fibrewise.
:::
