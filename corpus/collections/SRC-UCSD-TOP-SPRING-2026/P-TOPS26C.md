---
schema: qual/card@1
id: P-TOPS26C
kind: problem
title: Finite-index subgroups of finitely generated groups are finitely generated
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.problem}
Show that if $G$ is a finitely generated group and $H$ is a subgroup of finite index then $H$ is finitely generated.
:::

::: {.solution}

::: pf

::: pf-step
Let $G=\langle S\rangle$ with $S$ finite, and choose a finite set $T$ of representatives for the right cosets $H\backslash G$.

::: pf-proof
The set $T$ is finite because $[G:H]<\infty$.
:::

:::

::: {.pf-step #schreier-generators-definition}
For $t\in T$ and $s\in S\cup S^{-1}$, let $\overline{ts}\in T$ represent the coset $Hts$ and set
$$h_{t,s}=ts\overline{ts}^{-1}\in H.$$

::: pf-proof
By definition $ts$ and $\overline{ts}$ lie in the same right $H$-coset, so their quotient lies in $H$.
:::

:::

::: pf-step
The finite set of all $h_{t,s}$ generates $H$.

::: pf-proof
This is the Schreier rewriting argument: for a word $s_1\cdots s_k\in H$, insert successive coset representatives between letters. The word telescopes into a product of the corresponding $h_{t,s}$, and the final representative is the identity coset because the word lies in $H$.
:::

:::

::: pf-step
Thus every finite-index subgroup of a finitely generated group is finitely generated.

::: pf-proof
There are only $|T|\cdot2|S|$ possible Schreier generators in step [](#schreier-generators-definition){.pf-ref}.
:::

:::

:::

:::
