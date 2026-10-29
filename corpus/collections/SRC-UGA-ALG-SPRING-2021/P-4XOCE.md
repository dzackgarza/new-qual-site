---
schema: qual/card@1
id: P-4XOCE
kind: problem
title: A normal subgroup of smallest prime order lies in the center
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Normal Subgroups
  - Conjugacy
relations: []
review: draft
---

::: {.problem}
Let $H \normal G$ be a normal subgroup of a finite group $G$, where the order of $H$ is the smallest prime $p$ dividing $\abs{G}$.
Prove that $H$ is contained in the center of $G$.
:::

::: {.strategy}
Show that conjugation by every $g\in G$ acts trivially on $H$, by bounding the image of $G\to\Aut(H)$.
:::

::: {.solution}
::: pf

::: {.pf-step #aut}
Conjugation gives a homomorphism $\varphi\colon G\to\Aut(H)$, and $\abs{\Aut(H)}=p-1$.

::: pf-proof
$H$ is normal, so $g\mapsto(h\mapsto ghg^{-1})$ maps $G$ into $\Aut(H)$, and it is a homomorphism. Since $\abs H=p$ is prime, $H\cong\ZZ/p\ZZ$ and $\Aut(H)\cong(\ZZ/p\ZZ)^\times$ has order $p-1$.
:::

:::

::: {.pf-step #trivial}
$\varphi$ is trivial.

::: pf-proof
$\abs{\im\varphi}$ divides $\abs G$ by the first isomorphism theorem and divides $p-1$ by Lagrange's theorem and step [](#aut){.pf-ref}. A prime divisor $q$ of $\abs{\im\varphi}$ would divide $\abs G$, so $q\geq p$ by minimality of $p$, and would divide $p-1$, so $q<p$. Hence $\abs{\im\varphi}=1$.
:::

:::

::: pf-qed
By step [](#trivial){.pf-ref}, $ghg^{-1}=h$ for all $g\in G$ and $h\in H$, so $H\subseteq Z(G)$.
:::

:::
:::
