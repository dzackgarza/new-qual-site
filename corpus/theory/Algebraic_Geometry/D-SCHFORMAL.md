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
Let $A$ be a noetherian ring, complete and separated in the $I$-adic topology for an ideal $I$.
The \dfn{formal spectrum} $\operatorname{Spf} A$ is the topological space $\Spec(A/I)$ with the sheaf of topological rings $\varprojlim_{n\ge1}\OO_{\Spec(A/I^n)}$.
A \dfn{locally noetherian formal scheme} is a topologically ringed space locally isomorphic to such formal spectra.
It is a \dfn{noetherian formal scheme} if it is also quasi-compact, equivalently if finitely many of these affine formal opens cover it [@Har77, Chapter II, §9].
Its underlying space is then noetherian: each affine formal open has the topology of a noetherian affine scheme, and a finite union of noetherian open subspaces is noetherian.
:::

::: {.definition title="Completion along a closed subscheme"}
Let $X$ be a Noetherian scheme and $Z \subseteq X$ a closed subscheme with ideal sheaf $\mathcal{I}$.
The \dfn{formal completion} of $X$ along $Z$ is $\hat{X} = (Z, \varprojlim_n \OO_X/\mathcal{I}^n)$, a Noetherian formal scheme with underlying space $Z$.
For $X = \Spec A$ and $Z = V(I)$, $\hat{X} = \operatorname{Spf} \hat{A}$ with $\hat{A} = \varprojlim_n A/I^n$.
:::

::: {.example title="The formal disc"}
The formal completion of $\AA^1_k$ at the origin is
$$
\widehat{\AA^1_{k,0}}
=
\operatorname{Spf} k[[t]],
$$
the \dfn{formal disc}.
Its underlying topological space is the single closed point $(t)$, and its structure sheaf remembers the compatible system of infinitesimal neighbourhoods
$\Spec k[t]/(t^n)$.

The ordinary scheme $\Spec k[[t]]$ is different: it has the closed point $(t)$ and the generic point $(0)$, with open generic subscheme $\Spec k((t))$.
Thus $\Spec k((t))$ is the punctured spectrum of $k[[t]]$, not an open formal subscheme of $\operatorname{Spf}k[[t]]$.
In the category of formal schemes used here, deleting the unique point of the formal disc gives the empty open; a “punctured formal disc” requires an additional generic-fibre or adic framework.
:::
