---
schema: qual/card@1
id: PR-VGA2L
kind: proposition
title: Curves of genus $0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Rational Curves
  - Conics
relations:
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- What can you say about curves of genus $0$?
- Is every genus-zero curve isomorphic to $\PP^1$?
---

::: {.proposition}
Let $C$ be a smooth projective curve of genus $0$ over a field $k$.

- If $C$ has a $k$-rational point, then $C \cong \PP^1_k$.

- In general $C$ embeds as a smooth conic in $\PP^2_k$ by the anticanonical system $\abs{-K}$, which has degree $2$ and $\ell(-K) = 3$.

- Over $k = \bar{k}$, and over any finite field, the first case always holds.
:::

::: {.remark}
Riemann--Roch does the work.
With $g = 0$ and $\deg D = 1$, $\ell(D) = 2$ and $\ell(K - D) = 0$ since $\deg(K-D) = -3 < 0$, so a degree-one divisor gives a degree-one map to $\PP^1$, which is an isomorphism.
A $k$-point is exactly such a divisor, and that is where the rationality hypothesis enters.

Without a rational point the anticanonical divisor still has degree $2$ and $\ell = 3$, giving the conic.
The conic $x^2 + y^2 + z^2 = 0$ over $\RR$ is the standard curve of genus zero that is not $\PP^1$.

Over a finite field the second case cannot occur: a smooth conic over $\FF_q$ always has a rational point by the Chevalley--Warning theorem, so every genus-zero curve there is $\PP^1$.
That is the answer to the follow-up, and it is a counting statement, not a geometric one.
:::
