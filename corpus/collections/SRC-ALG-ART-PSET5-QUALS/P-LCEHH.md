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
and $E=L^{H_1}$, $K=L^{H_2}$.

::: pf

::: {.pf-step #s1}
$E=\QQ(\sqrt2)$ and $K=\QQ(\sqrt[4]{2})$.

::: pf-proof
Since $\sigma^2(\sqrt[4]{2})=-\sqrt[4]{2}$, the element $\sqrt2=(\sqrt[4]{2})^2$ is fixed by $\sigma^2$ and $\tau$, and $\sqrt[4]{2}$ is fixed by $\tau$. The Galois correspondence gives $[E:\QQ]=[D_4:H_1]=2$ and $[K:\QQ]=[D_4:H_2]=4$, which are the degrees of $\QQ(\sqrt2)$ and $\QQ(\sqrt[4]{2})$.
:::

:::

::: {.pf-step #s2}
$E/F$ and $K/E$ are normal.

::: pf-proof
By the Galois correspondence, $E/F$ is normal if and only if $H_1\trianglelefteq D_4$, and $K/E$ is normal if and only if $H_2\trianglelefteq H_1$. Both subgroups have index $2$ in the larger group, so both are normal.
:::

:::

::: {.pf-step #s3}
$K/F$ is not normal.

::: pf-proof
By the Galois correspondence, $K/F$ is normal if and only if $H_2\trianglelefteq D_4$. But $\sigma\tau\sigma^{-1}=\tau\sigma^{-2}=\tau\sigma^2\notin H_2$. Equivalently, $x^4-2$ has the root $\sqrt[4]{2}$ in $K\subseteq\RR$ but not the root $i\sqrt[4]{2}$.
:::

:::

::: pf-qed
By steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}, the tower $\QQ\subseteq\QQ(\sqrt2)\subseteq\QQ(\sqrt[4]{2})\subseteq\QQ(\sqrt[4]{2},i)$ has the required properties.
:::

:::

:::
