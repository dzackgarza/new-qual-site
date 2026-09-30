---
schema: qual/card@1
id: D-VKR54
kind: definition
title: $\Spec A$ as a locally ringed space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Spec
  - Affine Schemes
  - Structure Sheaf
relations:
- kind: uses
  target: D-BIVAU
review: draft
prompts:
- What are the points of $\Spec A$, and what is its topology?
- What is the structure sheaf of $\Spec A$?
- What are the stalks of $\OO_{\Spec A}$?
- Construct a ring $R$ such that $\Spec R$ is $\AA^1_k$ punctured at $0$ and $1$.
- What is the value of $n \in \ZZ$ at a prime $p \in \Spec \ZZ$, and what are the zeros of $60$ as a function on $\Spec \ZZ$?
- Find a ring $R$ and $0 \neq f \in R$ whose value at every point of $\Spec R$ is zero.
- Describe all the prime ideals of $k[x,y]$.
- Show that $\sqrt{I}$ is the intersection of the prime ideals containing $I$.
- If $D(f) = \bigcup_i D(g_i)$, show that $f^n = \sum_i b_i g_i$ for some $n$ and some $b_i \in R$.
- Show that the Zariski topology on $\Spec R$ is not $T_1$ in general.
---

::: {.definition title="The spectrum"}
$\Spec A$ is the set of prime ideals of $A$, with closed sets $V(J) = \theset{\mfp \st \mfp \supseteq J}$.
Its structure sheaf sends $U$ to the functions
$$
\varphi : U \to \coprod_{\mfp \in U} A_\mfp
$$
with $\varphi(\mfp) \in A_\mfp$, locally of the form $f/g$ with $g \notin \mfp$.
:::

::: {.proposition}
$\OO_{\Spec A}(D_f) = A_f$, and in particular $\OO_{\Spec A}(\Spec A) = A$.
The stalk at $\mfp$ is $A_\mfp$, a local ring.
:::

::: {.example}
For a field $k$, the affine line punctured at $0$ and $1$ is the distinguished open set $D_{x(x-1)} \subseteq \AA^1_k = \Spec k[x]$, whose closed complement is $V(x(x-1)) = \{(x), (x-1)\}$.
It is the affine scheme $\Spec R$ with $$R = k[x]_{x(x-1)} = k[x]\left[\frac{1}{x(x-1)}\right].$$
:::

::: {.remark}
For a ring map $\varphi\colon A\to B$ and a prime $\mfq$ of $B$, $\inverseof{\varphi}(\mfq)$ is a prime of $A$, so $\varphi$ induces a continuous map $\Spec B\to\Spec A$.
The preimage of a maximal ideal need not be maximal: for $\ZZ\subseteq\QQ$, the preimage of the maximal ideal $(0)$ of $\QQ$ is the prime $(0)$ of $\ZZ$, which is not maximal.

Morphisms of schemes are morphisms of locally ringed spaces: the induced maps on stalks are local homomorphisms.
With this condition, ring maps $A\to B$ correspond bijectively to morphisms $\Spec B\to\Spec A$ [@Har10a, Proposition II.2.3]; as morphisms of ringed spaces there are more ([[D-AN662]]).
:::
