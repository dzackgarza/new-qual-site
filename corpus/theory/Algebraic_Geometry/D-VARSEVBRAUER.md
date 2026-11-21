---
schema: qual/card@1
id: D-VARSEVBRAUER
kind: definition
title: Severi--Brauer varieties, and the Brauer class of a twisted projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Severi-Brauer Varieties
  - Brauer Group
  - Conics
relations:
- kind: related-to
  target: PR-VGA2L
review: draft
prompts:
- What is a Severi--Brauer variety?
---

::: {.definition title="Severi--Brauer variety"}
Let $k$ be a field with separable closure $k^s$.
A \dfn{Severi--Brauer variety} of dimension $n$ over $k$ is a variety $X$ over $k$ with $X_{k^s} \cong \PP^n_{k^s}$; an arbitrary separable splitting extension may replace $k^s$ in this condition (Jean-Pierre Serre, *Local Fields*, §X.6, which calls a $k$-scheme a Severi--Brauer variety when it becomes $\PP^{n-1}$ over some separable algebraic extension of $k$).
:::

::: {.theorem}
1. Isomorphism classes of Severi--Brauer varieties of dimension $n$ over $k$ are in bijection with $H^1(\Gal(k^s/k), \PGL_{n+1}(k^s))$ and hence with isomorphism classes of central simple $k$-algebras of degree $n+1$, each with a class in $\operatorname{Br}(k)$ (Jean-Pierre Serre, *Local Fields*: the descent argument of §X.6 gives the bijection with $H^1(G, \PGL(n,K))$ for $G=\Gal(K/k)$; §X.5, Proposition 8 states the canonical bijection $A(n,K/k)\to H^1(G,\PGL(n,K))$ between the classes of $k$-algebras becoming $M_n$ over $K$ and those forms; §X.5, Proposition 9 identifies $A(K/k)$ with $H^2(K/k)=\operatorname{Br}(k)$).

2. (Châtelet) $X \cong \PP^n_k$ if and only if $X(k) \neq \emptyset$, if and only if its Brauer class is trivial (Jean-Pierre Serre, *Local Fields*, §X.6, Exercise 1: a Severi--Brauer variety is isomorphic to $\PP^{n-1}_k$ if and only if it has a rational point in $k$).
:::

::: {.example}
The Severi--Brauer varieties of dimension $1$ are the smooth conics (Jean-Pierre Serre, *Local Fields*, §X.6, Example 1).
The conic $x^2 + y^2 + z^2 = 0$ over $\RR$ has no real point, so it is not $\PP^1_\RR$; it corresponds to the Hamilton quaternions (Serre, *Local Fields*, §X.7, example (e)).
If $k$ is finite, or is the function field of a curve over an algebraically closed field, then $\operatorname{Br}(k) = 0$ (Wedderburn, Tsen), so every Severi--Brauer variety over $k$ is a projective space (Serre, *Local Fields*, §X.7, examples (a) and (c)).
:::
