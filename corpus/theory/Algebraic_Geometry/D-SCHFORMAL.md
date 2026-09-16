---
schema: qual/card@1
id: D-SCHFORMAL
kind: definition
title: Formal schemes, and the formal disc
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Schemes
  - Completion
  - Power Series
relations:
- kind: uses
  target: D-VKR54
review: draft
prompts:
- What is a formal scheme?
- What is the analogue of the open unit disc? Of the punctured disc?
---

::: {.definition title="Formal scheme"}
Let $A$ be a Noetherian ring, complete in the $I$-adic topology for an ideal $I$.
The \dfn{formal spectrum} $\operatorname{Spf} A$ is the topological space $\Spec A/I$ with the sheaf of topological rings $\varprojlim_n \OO_{\Spec A/I^n}$.
A \dfn{Noetherian formal scheme} is a topologically ringed space locally isomorphic to some $\operatorname{Spf} A$.
:::

::: {.definition title="Completion along a closed subscheme"}
Let $X$ be a Noetherian scheme and $Z \subseteq X$ a closed subscheme with ideal sheaf $\mathcal{I}$.
The \dfn{formal completion} of $X$ along $Z$ is $\hat{X} = (Z, \varprojlim_n \OO_X/\mathcal{I}^n)$, a Noetherian formal scheme with underlying space $Z$.
For $X = \Spec A$ and $Z = V(I)$, $\hat{X} = \operatorname{Spf} \hat{A}$ with $\hat{A} = \varprojlim_n A/I^n$.
:::

::: {.example title="The formal disc"}
$\Spec k[[t]]$ has two points: the closed point $(t)$ and the generic point $(0)$, whose residue field is $k((t))$.
It plays the role of a small disc $\mathbb{D}$ around $0$ in the $t$-line, and its open subscheme $\Spec k((t))$, the generic point, plays the role of the punctured disc $\mathbb{D} \setminus \{0\}$.
The formal completion of $\AA^1_k$ at the origin is $\operatorname{Spf} k[[t]]$, whose underlying space is the single point $0$ and which remembers every infinitesimal neighbourhood $\Spec k[t]/(t^n)$.
:::
