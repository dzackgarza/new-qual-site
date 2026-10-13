---
schema: qual/card@1
id: T-COHFF
kind: theorem
title: The theorem on formal functions
slogan: 'For a proper morphism, all infinitesimal thickenings of a fibre recover the completed stalk of its higher direct image.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Higher Direct Images
  - Proper Morphisms
relations:
- kind: uses
  target: D-COHRIF
review: draft
prompts:
- State the theorem on formal functions.
- Deduce Zariski's connectedness theorem.
---

::: {.theorem}
Let $f\colon X\to Y$ be proper with $Y$ Noetherian, let $\mcf$ be coherent on $X$, and fix $y\in Y$.
Put
$$
A\coloneqq\OO_{Y,y},\qquad \mfm\coloneqq\mfm_y,
$$
let
$$
X_A\coloneqq X\times_Y\Spec A,
$$
and let $\mcf_A$ be the pullback of $\mcf$ to $X_A$. For $n\geq1$, define
$$
X_n\coloneqq X_A\times_{\Spec A}\Spec(A/\mfm^n),
\qquad
\mcf_n\coloneqq\mcf_A/\mfm^n\mcf_A.
$$
Then there is a natural isomorphism of $\widehat A$-modules
$$
\widehat{(R^if_*\mcf)_y}
\xrightarrow{\sim}
\varprojlim_n H^i(X_n,\mcf_n).
$$
:::

::: {.corollary title="Zariski connectedness"}
Let $f\colon X\to Y$ be proper with $Y$ Noetherian and suppose
$$
f_*\OO_X\cong\OO_Y.
$$
Then every fibre of $f$ is connected.
:::

::: {.proof}
Fix $y\in Y$ and use the notation of the theorem with $\mcf=\OO_X$ and $i=0$. The hypothesis gives
$$
\widehat{(f_*\OO_X)_y}\cong\widehat A,
$$
so formal functions yields
$$
\widehat A\cong\varprojlim_n H^0(X_n,\OO_{X_n}).
$$
If the fibre $X_1=X_y$ were disconnected, its ring of global sections would contain a nontrivial idempotent. Idempotents lift uniquely across nilpotent thickenings, so this idempotent would lift compatibly to every $H^0(X_n,\OO_{X_n})$ and hence to a nontrivial idempotent of the inverse limit. But the complete local ring $\widehat A$ has no nontrivial idempotents. Therefore $X_y$ is connected.
:::

::: {.remark}
For a proper birational morphism $f\colon X\to Y$ with $Y$ normal and $f_*\OO_X=\OO_Y$, the corollary gives connected fibres. This is the connectedness conclusion used in the normal-target form of Zariski's main theorem.
:::
