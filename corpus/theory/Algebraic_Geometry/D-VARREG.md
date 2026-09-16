---
schema: qual/card@1
id: D-VARREG
kind: definition
title: The sheaf of regular functions on a variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Regular Functions
  - Function Field
  - Local Rings
relations:
- kind: uses
  target: PR-7OT2Z
- kind: related-to
  target: D-VKR54
review: draft
prompts:
- What is $\OO_X$ for an affine variety?
- What is $k[V]$, what is $A(V)$, and what is $k(V)$?
- What are the sections of $\OO_X$ over a distinguished open set?
- Show that the regular functions on a variety form a sheaf of rings.
- What is a rational map? A birational map?
---

::: {.definition title="Regular functions"}
Let $X$ be a variety and $U \subseteq X$ open.
A function $\phi: U \to k$ is \dfn{regular} if for every $p \in U$ there is an open $U_p \ni p$ and polynomials $f, g$ with $g$ nowhere zero on $U_p$ and $\restrictionof{\phi}{U_p} = f/g$.
These form a sheaf of rings $\OO_X$, with restriction of functions: regularity is a local condition, and a function that is zero on each set of an open cover is zero.
The stalk $\OO_{X,p}$ is the **local ring at $p$**, with maximal ideal $\mfm_p$ the regular functions vanishing at $p$, and the stalk at the generic point is the **function field** $k(X)$.
:::

::: {.proposition title="What the sections are, affinely"}
For $X$ affine with coordinate ring $A(X) = k[X] = k[x_1,\ldots,x_n]/I(X)$ and $D(f) \da X \sm V(f)$,
\[
\OO_X(D(f)) = A(X)\invert{f}, \qquad \OO_X(X) = A(X), \qquad \OO_{X,p} = A(X)_{\mfm_p}, \qquad k(X) = \operatorname{Frac} A(X) .
\]
:::

::: {.proposition title="Sections as an intersection in the function field"}
Let $X$ be a variety.
For every nonempty open $U \subseteq X$, restriction identifies $\OO_X(U)$ with a subring of $k(X)$, and if $U = \bigcup_i U_i$ with each $U_i$ nonempty and open, then
\[
\OO_X(U) = \bigcap_i \OO_X(U_i) \quad \text{inside } k(X) .
\]
In particular, for an ideal $\mfa \neq 0$ of $k[x_1,\ldots,x_n]$, the open set $\AA^n \sm V(\mfa) = \bigcup_{0 \neq f \in \mfa} D(f)$ has
\[
\OO_{\AA^n}(\AA^n \sm V(\mfa)) = \bigcap_{0 \neq f \in \mfa} k[x_1,\ldots,x_n]\invert{f} \subseteq k(x_1,\ldots,x_n) .
\]
[@Har10a, §I.3]
:::

::: {.definition title="Rational and birational maps"}
A \dfn{rational map} $\varphi \colon X \dashrightarrow Y$ of varieties is an equivalence class of pairs $(U, \varphi_U)$ with $U \subseteq X$ nonempty open and $\varphi_U \colon U \to Y$ a morphism, where $(U, \varphi_U) \sim (V, \varphi_V)$ if $\varphi_U$ and $\varphi_V$ agree on $U \cap V$.
It is **dominant** if some, hence every, $\varphi_U$ has dense image.
A \dfn{birational map} is a rational map with a rational inverse, and $X$ and $Y$ are **birational** if one exists.
:::

::: {.proposition title="Rational maps and function fields"}
Over an algebraically closed field $k$, sending $X$ to $k(X)$ gives an arrow-reversing equivalence between varieties with dominant rational maps and finitely generated field extensions of $k$ with $k$-homomorphisms.
In particular $X$ and $Y$ are birational if and only if $k(X) \cong k(Y)$ over $k$.
[@Har10a]
:::

::: {.remark}
The condition is *locally* a quotient, not globally one, and the gap between those two is the whole content: on $\PP^n$ every function is locally a ratio of forms of equal degree and there are no nonconstant global ones, and the standard affine example is $X = V(xw - yz) \subseteq \AA^4$, where $x/y = z/w$ is regular on a union of two opens but is not a single quotient on it.

The definition is stated so that it transports verbatim to $\Spec A$ — replace $k$ by $\coprod_{\mfp} A_\mfp$ and "polynomial" by "element of $A$" — which is the point of stating it this way rather than as "restrictions of polynomials".
An examiner asking for $\OO_X$ on a variety is usually setting up that comparison.
:::
