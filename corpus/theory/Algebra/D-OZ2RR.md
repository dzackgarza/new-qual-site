---
schema: qual/card@1
id: D-OZ2RR
kind: definition
title: Normalizer of a subgroup
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
  - Normal Subgroups
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group and $H\leq G$ a [[D-IQ4OX|subgroup]].
The \dfn{normalizer} of $H$ in $G$ is
$$
N_G(H) \coloneqq \theset{g\in G \suchthat gHg^{-1} = H}.
$$
:::

::: {.proposition}
Let $H\leq G$.
Then $N_G(H)$ is a subgroup of $G$ in which $H$ is [[D-EKE4Q|normal]], and every subgroup $M\leq G$ with $H\normal M$ is contained in $N_G(H)$.
Hence
$$
N_G(H) = \bigcup_{M\in S} M, \qquad S \coloneqq \theset{M\leq G\suchthat H \normal M}.
$$
:::

::: {.proof}
If $gHg^{-1}=H$ and $g'Hg'^{-1}=H$, then $(gg')H(gg')^{-1}=H$ and $g^{-1}Hg=H$, so $N_G(H)$ is a subgroup; it contains $H$, and $H$ is normal in it by definition.
If $H\normal M$, then $mHm^{-1}=H$ for every $m\in M$, so $M\subseteq N_G(H)$.
The union of all such $M$ therefore lies in $N_G(H)$ and contains $N_G(H)\in S$.
:::

::: {.remark}
Conjugation defines a homomorphism $N_G(H)\to\Aut(H)$, $g\mapsto(h\mapsto ghg^{-1})$, whose kernel is the [[D-PX64W|centralizer]] $C_G(H)$.
Thus $C_G(H)\subseteq N_G(H)$, and elements of $N_G(H)$ permute the elements of $H$ by conjugation while elements of $C_G(H)$ fix them.
:::
