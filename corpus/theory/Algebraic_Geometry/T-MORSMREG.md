---
schema: qual/card@1
id: T-MORSMREG
kind: theorem
title: Smooth over an algebraically closed field equals regular
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Regularity
  - Singularities
relations:
- kind: uses
  target: D-MORSM
review: draft
prompts:
- How is smoothness related to regularity?
- Is a regular scheme smooth?
- State the Jacobian criterion and the criterion for smoothness over a field by differentials.
---

::: {.theorem}
Let $k$ be a field and $X$ a scheme locally of finite type over $k$.
If $X \to \Spec k$ is smooth of relative dimension $n$ then $X$ is regular of dimension $n$.
The converse holds when $k$ is perfect, in particular when $k = \kbar$, and fails otherwise.
:::

::: {.theorem title="Jacobian criterion"}
Let $k$ be an algebraically closed field, $X = V(f_1, \ldots, f_r) \subseteq \AA^m_k$, and $x \in X$ a closed point with $\dim \OO_{X,x} = n$.
Let $J(x) = (\partial f_i / \partial x_j (x))$ be the Jacobian matrix at $x$.

1. $\dim_k \mfm_x / \mfm_x^2 = \dim_k \Omega_{X/k} \otimes \kappa(x) = m - \operatorname{rank} J(x)$.

2. $X$ is regular at $x$ if and only if $\operatorname{rank} J(x) = m - n$.

[@Har10a, Theorem I.5.1, Proposition II.8.7]
:::

::: {.theorem title="Smoothness over a field"}
Let $k$ be a field and $X$ a scheme locally of finite type over $k$, of pure dimension $n$. The following are equivalent.

1. $X$ is smooth over $k$.

2. $\Omega_{X/k}$ is locally free of rank $n$.

3. $X$ is covered by open subschemes isomorphic to open subschemes of $\Spec k[x_1, \ldots, x_m]/(f_1, \ldots, f_r)$ whose Jacobian matrix has rank $m - n$ at every point.

4. $X_{\bar{k}} = X \times_k \Spec \bar{k}$ is regular.

If $k$ is perfect, these are also equivalent to: $X$ is regular.

[@Har10a, Theorem II.8.15, Theorem III.10.2]
:::

::: {.remark}
Smooth is a property of a *morphism* and regular is a property of a *ring*, and keeping them apart is most of what this question tests.
Smooth is the stronger, base-change-stable notion: it is "regular after every field extension", which is why the two agree exactly when there are no inseparable extensions to spoil it.

The counterexample to the converse over an imperfect field is the one to have ready: $k = \FF_p(t)$ and $X = \Spec k[x]/(x^p - t)$ is the spectrum of a field, hence regular, while $\fiberprod{X}{k}{\kbar} = \Spec \kbar[x]/(x - t^{1/p})^p$ is non-reduced, so $X$ is not smooth over $k$.

A smooth morphism is regular fibrewise, not absolutely: a smooth morphism over a singular base has singular total space, and the fibres are what the definition controls.
:::
