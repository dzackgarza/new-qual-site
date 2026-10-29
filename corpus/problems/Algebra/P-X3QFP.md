---
schema: qual/card@1
id: P-X3QFP
kind: problem
title: Classification of groups of order $12$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Semidirect Products
relations: []
review: draft
---

::: {.problem}
Classify the groups of order $12$ up to isomorphism.
:::

::: {.solution}

Let $G$ have order $12=2^2\cdot3$, and let $n_3$ be the number of Sylow $3$-subgroups. Sylow's theorems give $n_3\equiv1\pmod3$ and $n_3\mid4$, so $n_3\in\{1,4\}$.

::: pf

::: {.pf-step #a4}

If $n_3=4$, then $G\cong A_4$.

::: pf-proof

Let $P_1,\ldots,P_4$ be the Sylow $3$-subgroups. Since $[G:N_G(P_i)]=n_3=4$, we have $N_G(P_i)=P_i$. Conjugation on $\{P_1,\ldots,P_4\}$ gives a homomorphism $G\to S_4$ whose kernel is $\bigcap_i N_G(P_i)=\bigcap_i P_i=1$, since distinct subgroups of order $3$ meet trivially. So $G$ is isomorphic to a subgroup of order $12$ of $S_4$. That subgroup has index $2$, so it is normal and contains the square of every element of $S_4$, in particular every $3$-cycle; the $3$-cycles generate $A_4$, so the subgroup is $A_4$.

:::

:::

::: {.pf-step #sd}

If $n_3=1$, then $G\cong C_3\rtimes_\theta H$ with $H\in\{C_4,V_4\}$ and $\theta:H\to\Aut(C_3)\cong C_2$.

::: pf-proof

The Sylow $3$-subgroup $N\cong C_3$ is normal. A Sylow $2$-subgroup $H$ has order $4$, so $H\cong C_4$ or $V_4$, and $N\cap H=1$ with $\abs{NH}=12$. Hence $G=NH$ is the semidirect product for the conjugation action of $H$ on $N$.

:::

:::

::: {.pf-step #list}

The groups in step [](#sd){.pf-ref} are, up to isomorphism, $C_{12}$, $C_6\times C_2$, $C_3\rtimes C_4$ with a generator of $C_4$ acting by inversion, and $S_3\times C_2\cong D_{12}$.

::: pf-proof

For $H=C_4$, $\theta$ is trivial, giving $C_3\times C_4\cong C_{12}$, or is the unique surjection $C_4\to C_2$, giving $C_3\rtimes C_4$. For $H=V_4$, $\theta$ is trivial, giving $C_3\times V_4\cong C_6\times C_2$, or is a surjection $V_4\to C_2$. The three surjections differ by an automorphism of $V_4$, so they give isomorphic semidirect products. Writing $V_4=\langle a\rangle\times\langle b\rangle$ with $\ker\theta=\langle b\rangle$, this group is $(C_3\rtimes\langle a\rangle)\times\langle b\rangle\cong S_3\times C_2$.

:::

:::

::: pf-step

The groups of order $12$ are exactly $\boxed{C_{12},\ C_6\times C_2,\ C_3\rtimes C_4,\ S_3\times C_2,\ A_4}$, pairwise non-isomorphic.

::: pf-proof

By steps [](#a4){.pf-ref} and [](#list){.pf-ref}, every group of order $12$ is one of these. The group $A_4$ has four Sylow $3$-subgroups and the others have one. Among the others, $C_{12}$ and $C_6\times C_2$ are abelian and are distinguished by having an element of order $12$; $C_3\rtimes C_4$ and $S_3\times C_2$ are nonabelian, with cyclic and noncyclic Sylow $2$-subgroups respectively.

:::

:::

:::

:::
