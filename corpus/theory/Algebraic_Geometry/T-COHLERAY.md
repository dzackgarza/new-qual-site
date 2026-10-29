---
schema: qual/card@1
id: T-COHLERAY
kind: theorem
title: The Leray spectral sequence
slogan: 'Compute cohomology upstairs by taking higher direct images first; if they vanish above degree zero, cohomology descends to the base.'
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
$$
E_2^{p,q} = H^p\qty{Y, R^q f_* \mcf} \Longrightarrow H^{p+q}(X, \mcf) .
$$
:::

::: {.remark}
The spectral sequence is the Grothendieck spectral sequence for
$$
\Gamma(X,-)=\Gamma(Y,-)\circ f_*.
$$

If $R^q f_* \mcf = 0$ for all $q>0$, the sequence collapses to the edge and $H^i(X,\mcf) \cong H^i(Y, f_*\mcf)$ for all $i$.
This holds, for example, when $f$ is an affine morphism of schemes and $\mcf$ is quasicoherent.
In low degrees one obtains the five-term exact sequence
$$
0 \to H^1(Y, f_* \mcf)
\to H^1(X, \mcf)
\to H^0(Y, R^1 f_* \mcf)
\to H^2(Y, f_*\mcf)
\to H^2(X,\mcf).
$$
:::
