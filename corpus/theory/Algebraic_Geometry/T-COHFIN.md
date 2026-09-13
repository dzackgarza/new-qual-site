---
schema: qual/card@1
id: T-COHFIN
kind: theorem
title: Finiteness of cohomology for coherent sheaves on a projective scheme
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Coherent Sheaves
  - Projective Schemes
relations:
- kind: uses
  target: T-IJW1K
- kind: uses
  target: PR-COHLES
review: draft
prompts:
- Why is $H^i(X, \mcf)$ finite dimensional?
- Which hypothesis in Serre finiteness fails first?
---

::: {.theorem}
Let $A$ be Noetherian, $X$ projective over $A$, and $\mcf \in \Coh(X)$.
Then each $H^i(X, \mcf)$ is a finitely generated $A\dash$module.
Over a field, every $h^i(X,\mcf)$ is finite and vanishes for $i > \dim X$.
:::

::: {.remark title="Proof shape"}
Reduce to $X = \PP^n_A$ by pushing forward along the closed immersion, which changes no cohomology.
Any coherent $\mcf$ on $\PP^n$ sits in $0 \to \mcr \to \mce \to \mcf \to 0$ with $\mce$ a finite sum of twists $\OO(-d_i)$, and $\mcr$ is again coherent.
The twists have finitely generated cohomology by the explicit computation, and descending induction on $i$ from Grothendieck vanishing runs the long exact sequence down.
:::

::: {.remark title="Hypotheses"}
Properness is what fails first and it fails already in degree $0$: on $X = \AA^1_k$, $H^0(X,\OO) = k[x]$ is infinite dimensional.
So finiteness is a statement about proper schemes, not about nice sheaves, and the correct general form is for $f: X \to \Spec A$ proper with $\mcf$ coherent.

Coherence is the second hypothesis, and it fails on quasicoherent sheaves for the same reason: $\bigoplus_{d \geq 0} \OO(d)$ on $\PP^n$ has infinite dimensional $H^0$.

The practical payoff is that $h^0, h^1, \ldots$ are *numbers*, so $\chi$ exists and Riemann--Roch can be a statement about integers.
:::
