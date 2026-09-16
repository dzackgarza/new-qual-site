---
schema: qual/card@1
id: E-SS8.EX-1
kind: problem
title: "A holomorphic mapping  is a local bijection on U if for every  there exists an o"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
1. A holomorphic mapping $f : U \to V$ is a local bijection on U if for every $z \in U$ there exists an open disc $D \subset U$ centered at z, so that $f : D \to f ( D )$ is a bijection.

Prove that a holomorphic map $f : U \to V$ is a local bijection on U if and only if $f ^ { \prime } ( z ) \neq 0$ for all $z \in U$

[Hint: Use Rouch´e’s theorem as in the proof of Proposition 1.1.]
:::

::: {.solution}
Suppose first that $f'(z_0)\ne0$. Write
\[
f(z)-f(z_0)=(z-z_0)g(z),
\]
where $g$ is holomorphic near $z_0$ and $g(z_0)=f'(z_0)\ne0$. Choose a small closed disc $\overline D$ centered at $z_0$ on which $g$ has no zeros and $f(z)\ne f(z_0)$ on $\partial D$. Let
\[
m=\min_{\partial D}|f(z)-f(z_0)|>0.
\]
For $w$ with $|w-f(z_0)|<m$, Rouché's theorem shows that
\[
f(z)-w
\]
has the same number of zeros in $D$ as $f(z)-f(z_0)$, namely one, counted with multiplicity. Hence every such $w$ has a unique preimage in $D$. After shrinking $D$ if necessary, $f(D)$ is open and $f:D\to f(D)$ is bijective. Thus $f$ is a local bijection at $z_0$.

Conversely, suppose $f$ is locally injective at $z_0$. If $f'(z_0)=0$, then for some $m\ge2$,
\[
f(z)-f(z_0)=(z-z_0)^m g(z),\qquad g(z_0)\ne0.
\]
On a sufficiently small disc, $g$ has a holomorphic $m$th root $h$ with $h(z_0)\ne0$. Then
\[
f(z)-f(z_0)=\bigl((z-z_0)h(z)\bigr)^m.
\]
The map $\phi(z)=(z-z_0)h(z)$ has $\phi'(z_0)=h(z_0)\ne0$, so it maps a neighborhood of $z_0$ biholomorphically onto a neighborhood of $0$. But $w\mapsto w^m$ is not injective on any neighborhood of $0$ when $m\ge2$. Hence $f$ cannot be locally injective, a contradiction. Therefore $f'(z_0)\ne0$.

Since $z_0$ was arbitrary, $f$ is a local bijection on $U$ exactly when $f'$ never vanishes.
:::
