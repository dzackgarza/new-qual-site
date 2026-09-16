---
schema: qual/card@1
id: PR-DIVZEROPOLE
kind: proposition
title: Zeros and poles of a rational function
classification:
  areas:
  - algebraic-geometry
  topics:
  - Divisors
  - Discrete Valuation Rings
  - Normal Schemes
relations:
- kind: uses
  target: D-5PQ5W
- kind: uses
  target: D-QJ5M9
review: draft
prompts:
- Why does a rational function on an integral Noetherian scheme have only finitely many zeros and poles?
- Why is a rational function with no poles on a normal Noetherian scheme regular?
---

Let $X$ be an integral Noetherian scheme with function field $K$.
For a prime divisor $Y \subseteq X$ with generic point $\eta_Y$ such that $\OO_{X, \eta_Y}$ is a discrete valuation ring with valuation $v_Y$, a function $t \in K^\times$ has a \dfn{zero} along $Y$ if $v_Y(t) > 0$ and a \dfn{pole} along $Y$ if $v_Y(t) < 0$.

::: {.proposition}
1. A Noetherian topological space has finitely many irreducible components [@Har10a, Proposition I.1.5].

2. For $t \in K^\times$, there are only finitely many codimension-one points $y \in X$ with $t \notin \OO_{X,y}^\times$.

3. If $X$ is regular in codimension one, then $\div t = \sum_Y v_Y(t)\, Y$ is a finite sum, hence a Weil divisor [@Har10a, Lemma II.6.1].

4. If $X$ is normal, then $t \in K$ has no poles if and only if $t \in \OO_X(X)$; on an affine open $\Spec A$ this is $A = \bigcap_{\operatorname{ht} \mathfrak{p} = 1} A_{\mathfrak{p}}$ for a Noetherian normal domain $A$ [@Har10a, Proposition II.6.3A].
:::
