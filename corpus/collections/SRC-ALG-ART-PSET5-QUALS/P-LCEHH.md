---
schema: qual/card@1
id: P-LCEHH
kind: problem
title: A tower of extensions with Galois group $D_4$ in which normality is not transitive
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Normal Subgroups
  - Field Extensions
relations: []
review: draft
---

::: {.problem}

Give an example of a tower of field extensions $F \subseteq E \subseteq K \subseteq L$, with $L/F$ Galois and $\mathrm{Gal}(L/F) \cong D_4$ (the dihedral group of order 8), such that $E/F$ is normal, $K/E$ is normal, but $K/F$ is not normal (i.e. exhibit a failure of transitivity of normality).
:::

::: {.solution}
Let $F=\QQ$ and $L=\QQ(\sqrt[4]{2},i)$, the splitting field of $x^4-2$ over $\QQ$. Then $\operatorname{Gal}(L/\QQ)\cong D_4=\langle \sigma,\tau \mid \sigma^4=\tau^2=e,\ \tau\sigma\tau^{-1}=\sigma^{-1}\rangle$, where
$$
\sigma(\sqrt[4]{2})=i\sqrt[4]{2},\quad \sigma(i)=i,
\qquad
\tau(\sqrt[4]{2})=\sqrt[4]{2},\quad \tau(i)=-i.
$$
Put
$$
H_1=\langle\sigma^2,\tau\rangle=\{e,\tau,\sigma^2,\tau\sigma^2\},
\qquad
H_2=\langle\tau\rangle=\{e,\tau\}\le H_1,
$$
and $E=L^{H_1}$, $K=L^{H_2}$. Since $\sigma^2(\sqrt[4]{2})=-\sqrt[4]{2}$, the element $\sqrt2=(\sqrt[4]{2})^2$ is fixed by $\sigma^2$ and $\tau$, and $\sqrt[4]{2}$ is fixed by $\tau$; comparing degrees gives
$$
E=\QQ(\sqrt2),
\qquad
K=\QQ(\sqrt[4]{2}).
$$
By the Galois correspondence, $E/F$ is normal if and only if $H_1\trianglelefteq D_4$, $K/E$ is normal if and only if $H_2\trianglelefteq H_1$, and $K/F$ is normal if and only if $H_2\trianglelefteq D_4$.

- $[D_4:H_1]=2$, so $H_1\trianglelefteq D_4$ and $E/F$ is normal.

- $[H_1:H_2]=2$, so $H_2\trianglelefteq H_1$ and $K/E$ is normal.

- $\sigma\tau\sigma^{-1}=\sigma^2\tau\notin H_2$, so $H_2\not\trianglelefteq D_4$ and $K/F$ is not normal: $x^4-2$ has the root $\sqrt[4]{2}$ in $K\subseteq\RR$ but not the root $i\sqrt[4]{2}$.

The tower $\QQ\subseteq\QQ(\sqrt2)\subseteq\QQ(\sqrt[4]{2})\subseteq\QQ(\sqrt[4]{2},i)$ therefore has the required properties.
$\blacksquare$
:::
