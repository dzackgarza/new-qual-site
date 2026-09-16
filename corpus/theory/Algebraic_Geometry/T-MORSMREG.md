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
- State the Jacobian criterion, and prove that smoothness over a field is equivalent to $\Omega_{X/k}$ being locally free of rank $\dim X$.
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
:::

::: {.proof}
1. $\Omega_{X/k}$ is the quotient of $\bigoplus_j \OO_X\, dx_j$ by the relations $df_i = \sum_j (\partial f_i / \partial x_j)\, dx_j$, so $\Omega_{X/k} \otimes \kappa(x)$ is the cokernel of the transpose $J(x)^{\top} \colon k^r \to k^m$, of dimension $m - \operatorname{rank} J(x)$. For a local $k$-algebra with residue field $k$, $d$ induces an isomorphism $\mfm_x/\mfm_x^2 \to \Omega_{X/k} \otimes \kappa(x)$ [@Har10a, Proposition II.8.7].

2. $\OO_{X,x}$ is regular exactly when $\dim_k \mfm_x/\mfm_x^2 = n$.
:::

::: {.theorem title="Smoothness over a field"}
Let $k$ be a field and $X$ a scheme locally of finite type over $k$, of pure dimension $n$. The following are equivalent.

1. $X$ is smooth over $k$.

2. $\Omega_{X/k}$ is locally free of rank $n$.

3. $X$ is covered by open subschemes isomorphic to open subschemes of $\Spec k[x_1, \ldots, x_m]/(f_1, \ldots, f_r)$ whose Jacobian matrix has rank $m - n$ at every point.

4. $X_{\bar{k}} = X \times_k \Spec \bar{k}$ is regular.

If $k$ is perfect, these are also equivalent to: $X$ is regular.
:::

::: {.proof}
1. $\Omega_{X_{\bar k}/\bar k} = \Omega_{X/k} \otimes_k \bar{k}$, and a coherent sheaf is locally free of rank $n$ exactly when its pullback along the faithfully flat $X_{\bar k} \to X$ is, so conditions 2 and 3 can be checked on $X_{\bar k}$, where the Jacobian rank at a point is computed by the same polynomials. By definition, condition 1 is condition 4.

2. Over $\bar{k}$, suppose $X$ is regular. Regular local rings are domains, so $X$ is reduced. By the Jacobian criterion the coherent sheaf $\Omega_{X/\bar k}$ has fibre dimension $n$ at every closed point; fibre dimension is upper semicontinuous and closed points are dense in every closed subset, so it is $n$ everywhere, and a coherent sheaf of constant fibre dimension on a reduced scheme is locally free. This gives condition 2, and condition 3 is the Jacobian criterion at closed points.

3. Over $\bar{k}$, conditions 2 or 3 give fibre dimension $n = \dim \OO_{X,x}$ at every closed point, so every closed point is regular by the Jacobian criterion, and every localization of a regular local ring at a prime is regular, so $X$ is regular.

4. If $k$ is perfect, $\bar{k}/k$ is separable, and $\OO_{X,x}$ is regular if and only if every local ring of $X_{\bar k}$ over $x$ is regular; so $X$ is regular exactly when $X_{\bar k}$ is.
:::

::: {.remark}
Smooth is a property of a *morphism* and regular is a property of a *ring*, and keeping them apart is most of what this question tests.
Smooth is the stronger, base-change-stable notion: it is "regular after every field extension", which is why the two agree exactly when there are no inseparable extensions to spoil it.

The counterexample to the converse over an imperfect field is the one to have ready: $k = \FF_p(t)$ and $X = \Spec k[x]/(x^p - t)$ is the spectrum of a field, hence regular, while $\fiberprod{X}{k}{\kbar} = \Spec \kbar[x]/(x - t^{1/p})^p$ is non-reduced, so $X$ is not smooth over $k$.

A smooth morphism is regular fibrewise, not absolutely: a smooth morphism over a singular base has singular total space, and the fibres are what the definition controls.
:::
