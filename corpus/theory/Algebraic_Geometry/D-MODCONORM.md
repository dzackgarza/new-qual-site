---
schema: qual/card@1
id: D-MODCONORM
kind: definition
title: The conormal and normal sheaves, and adjunction
classification:
  areas:
  - algebraic-geometry
  topics:
  - Conormal Sheaf
  - Canonical Sheaf
  - Closed Subschemes
relations:
- kind: uses
  target: D-MODIDEAL
- kind: uses
  target: D-4GCH6
review: draft
prompts:
- What is the conormal sheaf of a closed subscheme?
- State the adjunction formula.
- What is the canonical sheaf of a smooth degree-$d$ plane curve?
---

::: {.definition title="Conormal and normal"}
Let $i:Z\hookrightarrow X$ be a closed immersion of schemes with ideal sheaf $\mci$.
The \dfn{conormal sheaf} is $\mci/\mci^2$, regarded as an $\OO_Z$-module.
Its dual is the \dfn{normal sheaf}
$$
\mcn_{Z/X}\coloneqq\sheafhom_{\OO_Z}(\mci/\mci^2,\OO_Z).
$$
:::

::: {.definition title="Determinant"}
For a locally free sheaf $\mcf$ of finite rank $r$ on a scheme $X$, its \dfn{determinant} is the invertible sheaf $\det\mcf\coloneqq\bigwedge^r\mcf$.
For a smooth variety $X$ over a field $k$, the canonical invertible sheaf is $\omega_X=\det\Omega_{X/k}$ [@Har10a, Chapter II, §8].
:::

::: {.proposition title="Determinants of exact sequences"}
Let $X$ be a scheme and let $0\to\mcf_1\to\cdots\to\mcf_n\to0$ be an exact sequence of locally free sheaves of finite rank.
With exponent $-1$ denoting the dual of an invertible sheaf, there is a canonical isomorphism
$$
\bigotimes_{i=1}^n(\det\mcf_i)^{\otimes(-1)^{i+1}}\cong\OO_X.
$$
For $n=3$ it is $\det\mcf_2\cong\det\mcf_1\otimes\det\mcf_3$.
The short-exact-sequence map is proved in [[P-AGH2516TENSOROPS]], part (d); applying it to the successive image sheaves gives the displayed cancellation for a longer exact sequence [@Har10a, Exercise II.5.16].
:::

::: {.theorem title="Adjunction"}
Let $i:Z\hookrightarrow X$ be a closed immersion of smooth varieties over a field $k$, of dimensions $m$ and $n$, with ideal sheaf $\mci$.
Then the conormal sequence is short exact,
$$
0\longrightarrow\mci/\mci^2\longrightarrow i^*\Omega_{X/k}\longrightarrow\Omega_{Z/k}\longrightarrow0,
$$
and $\mci/\mci^2$ is locally free of rank $n-m$.
Taking determinants gives
$$
\omega_Z\cong i^*\omega_X\otimes_{\OO_Z}\bigwedge^{n-m}\mcn_{Z/X}.
$$
[@Har10a, Theorem II.8.17 and Proposition II.8.20]
:::

::: {.theorem title="Adjunction for a divisor"}
Let $X$ be a smooth variety over a field $k$, and let $i:Z\hookrightarrow X$ be a smooth effective Cartier divisor.
Its ideal sheaf is $\OO_X(-Z)$, and
$$
\omega_Z\cong i^*\bigl(\omega_X\otimes_{\OO_X}\OO_X(Z)\bigr).
$$
[@Har10a, Proposition II.8.20]
:::

::: {.example title="A free conormal module on a nonsmooth subscheme"}
Let $k$ be a field, let $X=\Spec k[x]$, and let $Z$ be the closed subscheme defined by $I=(x^2)$.
Put $B=k[x]/(x^2)$.
The map
$$
B\longrightarrow I/I^2,\qquad a\bmod x^2\longmapsto ax^2\bmod x^4
$$
is an isomorphism: it is surjective, and $ax^2\in(x^4)$ holds exactly when $a\in(x^2)$.
Thus the conormal sheaf is free of rank one on $Z$.
The element $x\bmod x^2$ is nonzero and nilpotent, so $Z$ is not reduced and is not smooth over $k$ [@Har10a, Chapter III, §10].
Consequently local freeness of the conormal sheaf does not imply smoothness of the closed subscheme.
:::

::: {.example title="Canonical sheaf and genus of a smooth plane curve"}
Let $k$ be algebraically closed and let $C\subseteq\PP_k^2$ be a smooth integral plane curve of degree $d\ge1$.
The identities $\omega_{\PP_k^2}\cong\OO(-3)$ and $\OO(C)\cong\OO(d)$ give
$$
\omega_C\cong\OO_C(d-3),\qquad\deg\omega_C=d(d-3).
$$
Since $\deg\OO_C(1)=d$ and $\deg\omega_C=2g(C)-2$, it follows that
$$
g(C)=\frac{(d-1)(d-2)}2.
$$
[@Har10a, Example II.8.20.3 and Chapter IV, §1]
:::
