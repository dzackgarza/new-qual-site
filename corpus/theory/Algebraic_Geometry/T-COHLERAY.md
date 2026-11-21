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
It is stated here as the cited theorem it is, not as a proved one: Hartshorne gives no numbered form of it and refers instead to Godement, *Théorie des faisceaux*, II.4.17.1, which is not retained in `tmp/sources` and has no key in `vocabularies/references.yaml`, so no statement number was read and nothing about the construction of the sequence is checked here.

Two consequences are the book's exercises, with the hypotheses it gives them.
If $R^q f_* \mcf = 0$ for all $q>0$, the sequence collapses to the edge and $H^i(X,\mcf) \cong H^i(Y, f_*\mcf)$ for all $i$ [@Har77, Exercise III.8.1], the case the book itself calls degenerate.
This holds in particular when $f$ is an affine morphism of schemes, $X$ is Noetherian and $\mcf$ is quasicoherent [@Har77, Exercise III.8.2].
No retained solution set covers either exercise: the Egbert set carries III.8.3, III.8.5 and III.8.6 and not these, and no other retained set reaches them. So both are recorded as the book's exercises, and the argument for them is not transcribed here.

In low degrees one obtains the five-term exact sequence
$$
0 \to H^1(Y, f_* \mcf)
\to H^1(X, \mcf)
\to H^0(Y, R^1 f_* \mcf)
\to H^2(Y, f_*\mcf)
\to H^2(X,\mcf).
$$
:::
