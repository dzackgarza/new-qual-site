---
schema: qual/card@1
id: P-UCTOP290-S4-2
kind: problem
title: Cyclic covers of closed orientable surfaces
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 2 against the checked-in extraction and PDF page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 4, problem 2
    (assets/attachments/UCSD_290_F14_sheet4.pdf, sheet page 1, printed page
    253): the sheet asks for a 5-sheeted cover Sigma_11 -> Sigma_3 and a
    3-sheeted cover Sigma_4 -> Sigma_2 together with their groups of deck
    transformations. The card states exactly this, with the surfaces named in
    the same genus notation, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this sheet in the project, so
    the proof is derived here rather than transcribed. It constructs both
    covers as the regular covers corresponding to kernels of surjections
    pi_1(Sigma_g) -> C_d and identifies the surfaces by Euler characteristic.
---

::: {.problem}
Construct a five-sheeted covering
$$
\Sigma_{11}\longrightarrow\Sigma_3
$$
and a three-sheeted covering
$$
\Sigma_4\longrightarrow\Sigma_2,
$$
where $\Sigma_g$ is the closed orientable surface of genus $g$.
Find the deck transformation group of each covering.
:::

::: {.solution}
Write $\Sigma_g$ for the closed orientable surface of genus $g$, so that $\chi(\Sigma_g)=2-2g$, and $\pi_1(\Sigma_g)=\generators{a_1,b_1,\ldots,a_g,b_g\mid\prod_{i=1}^{g}[a_i,b_i]}$.

::: pf

::: {.pf-step #euler}
The Euler characteristics are consistent: $5\chi(\Sigma_3)=-20=\chi(\Sigma_{11})$ and $3\chi(\Sigma_2)=-6=\chi(\Sigma_4)$.

::: pf-proof
$\chi(\Sigma_3)=2-6=-4$, so $5\chi(\Sigma_3)=-20$, and $\chi(\Sigma_{11})=2-22=-20$. Similarly $\chi(\Sigma_2)=2-4=-2$, so $3\chi(\Sigma_2)=-6$, and $\chi(\Sigma_4)=2-8=-6$.
:::

:::

::: {.pf-step #surjection}
For $g\geq1$ and $d\geq1$ there is a surjective homomorphism $\varphi\colon\pi_1(\Sigma_g)\to C_d$.

::: pf-proof
Define $\varphi$ on the generators by $a_1\mapsto1$ and $b_1,a_2,b_2,\ldots,a_g,b_g\mapsto0$, where $C_d$ is written additively. To see that this is a homomorphism, the only relation is $\prod_i[a_i,b_i]=1$, and its image is the sum of the commutators $[1,0]=0$, $[0,0]=0,\ldots$ in the abelian group $C_d$, which is $0$. So $\varphi$ is well defined, and it is surjective because $a_1\mapsto1$ generates $C_d$.
:::

:::

::: {.pf-step #existence}
For a finite group $G$ and a surjection $\varphi\colon\pi_1(\Sigma_g)\to G$, the covering corresponding to $\ker\varphi$ is connected, has degree $\abs{G}$, is a closed orientable surface, and has deck transformation group $G$.

::: pf-proof
Let $H=\ker\varphi$ and let $q\colon\widetilde\Sigma\to\Sigma_g$ be the covering with $q_*\pi_1(\widetilde\Sigma)=H$. It is connected because $H$ has index $\abs{G}$ and $\varphi$ is onto, so the action on the cosets is transitive; its degree is the index of $H$, namely $\abs{G}$. A covering of a surface is a surface, and a covering of an orientable manifold is orientable, being locally homeomorphic to it with compatible charts; so $\widetilde\Sigma$ is a closed orientable surface. For a regular covering, the deck transformation group is $N(H)/H$, and here $H$ is normal because it is a kernel, so the deck group is $\pi_1(\Sigma_g)/H\cong G$.
:::

:::

::: {.pf-step #five}
Taking $g=3$, $G=C_5$ and the surjection of step [](#surjection){.pf-ref} gives a $5$-sheeted covering $\Sigma_{11}\to\Sigma_3$ with deck group $C_5$.

::: pf-proof
By step [](#existence){.pf-ref} the cover $\widetilde\Sigma$ is a closed orientable surface and the covering has degree $5$, so every point of $\Sigma_3$ has five preimages and, the covering being a local homeomorphism with free deck action, $\chi(\widetilde\Sigma)=5\chi(\Sigma_3)=-20$; for a closed orientable surface $2-2h=-20$ forces $h=11$, so $\widetilde\Sigma=\Sigma_{11}$. Its deck transformation group is $C_5$ by step [](#existence){.pf-ref}.
:::

:::

::: {.pf-step}
Taking $g=2$, $G=C_3$ and the surjection of step [](#surjection){.pf-ref} gives a $3$-sheeted covering $\Sigma_4\to\Sigma_2$ with deck group $C_3$, so the two required coverings exist and their deck transformation groups are $C_5$ and $C_3$.

::: pf-proof
The argument of step [](#five){.pf-ref} applies verbatim with $g=2$ and $\abs{G}=3$: the cover is a closed orientable surface with $\chi=3\chi(\Sigma_2)=-6$, so $2-2h=-6$ gives $h=4$, and the deck group is $C_3$.
:::

:::

:::

:::
