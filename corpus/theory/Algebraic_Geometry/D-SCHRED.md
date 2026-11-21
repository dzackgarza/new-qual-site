---
schema: qual/card@1
id: D-SCHRED
kind: definition
title: The reduced induced structure on a closed subset
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subschemes
  - Reduced Schemes
  - Ideal Sheaves
relations:
- kind: uses
  target: D-SCHSUB
- kind: related-to
  target: PR-6TCSJ
review: draft
prompts:
- What is the reduced induced scheme structure on a closed subset?
- In what sense is it canonical?
---

::: {.definition}
Let $Z \subseteq \abs{X}$ be closed.
For $X = \Spec A$ take $\mfa \coloneqq \Intersect_{\mfp \in Z} \mfp$, a radical ideal, and give $Z$ the structure $\Spec(A/\mfa)$.
These agree on overlaps, so they glue to a closed subscheme structure on $Z$ for any $X$: the \dfn{reduced induced structure} $Z^\red$.
:::

::: {.proposition}
$Z^\red$ is the unique reduced closed subscheme of $X$ with underlying space $Z$, and it is the smallest closed subscheme with that space: every closed subscheme supported on $Z$ contains $Z^\red$ as a closed subscheme.
Every morphism $T\to X$ from a reduced scheme $T$ whose image lies in $Z$ factors uniquely through $Z^\red$.
:::

::: {.proof}
All three claims are local on $X$, so take $X=\Spec A$ and $Z=V(\mfa)$.
By [@Har77, Corollary II.5.10] the closed subschemes of $\Spec A$ are the $\Spec(A/\mfb)$, one for each ideal $\mfb$, and the underlying space of $\Spec(A/\mfb)$ is $V(\mfb)$.
Such a subscheme is reduced exactly when $\mfb$ is radical, since the nilradical of $A/\mfb$ is $\sqrt{\mfb}$.

**Uniqueness.**
Let $\Spec(A/\mfb)$ be reduced with $V(\mfb)=V(\mfa)$.
Then $\mfb$ is radical and the primes containing $\mfb$ are exactly the primes containing $\mfa$, because a prime contains an ideal precisely when it contains its radical; hence
$$
\mfb=\bigcap_{\mfp\supseteq\mfb}\mfp=\bigcap_{\mfp\supseteq\mfa}\mfp=\sqrt{\mfa}=\mfa
$$
[[E-AMD-HWVXZVE4]], and the reduced closed subscheme with space $Z$ is $\Spec(A/\mfa)$.

**Smallest.**
If $V(\mfb)=V(\mfa)$ then $\sqrt{\mfb}=\sqrt{\mfa}=\mfa$ by the same formula, so $\mfa\supseteq\mfb$ and $A/\mfa$ is a quotient of $A/\mfb$; the corresponding closed immersion $\Spec(A/\mfa)\injects\Spec(A/\mfb)$ exhibits $Z^\red$ as a closed subscheme of every closed subscheme with space $Z$.

**Factorization.**
Let $T$ be reduced and $f\colon T\to\Spec A$ with $f(T)\subseteq V(\mfa)$, and let $\Spec B\subseteq T$ be an affine open, on which $f$ is given by a ring map $\varphi\colon A\to B$.
For a prime $\mfp\subseteq B$ the point $f(\mfp)=\varphi^{-1}(\mfp)$ lies in $V(\mfa)$, so $\varphi(\mfa)\subseteq\mfp$; as this holds for every prime of $B$, the ideal $\varphi(\mfa)$ lies in the nilradical of $B$, which is $0$ because $B$ is reduced.
Hence $\mfa\subseteq\ker\varphi$ and $\varphi$ factors through $A\to A/\mfa$, which gives $f$ a factorization through $Z^\red$ on each affine open; the factorizations agree on overlaps, and on an affine open the factorization is the ring map $A/\mfa\to B$ determined by $\varphi$, so it is unique.
:::

::: {.remark}
Taking $Z = \abs{X}$ gives the reduction $X^\red \to X$, a homeomorphism that is an isomorphism if and only if $X$ is reduced.
For an ideal $\mfa\subseteq A$, $\bigcap_{\mfp\supseteq\mfa}\mfp=\sqrt{\mfa}$, so the reduced induced structure on $V(\mfa)\subseteq\Spec A$ is $\Spec(A/\sqrt{\mfa})$.
:::
