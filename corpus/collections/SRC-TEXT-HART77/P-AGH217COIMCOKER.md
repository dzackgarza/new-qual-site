---
schema: qual/card@1
id: P-AGH217COIMCOKER
kind: problem
title: The image and cokernel of a sheaf morphism as quotient sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Quotient Sheaves
  - Cokernels
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise II.1.7 together with the preceding definitions of kernel, image, cokernel, quotient sheaf, and exactness in Hartshorne II.1. The proof applies the short exact quotient result of II.1.6 to the kernel and image subsheaves and verifies the canonical identifications stalkwise.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $\varphi: \mcf \to \mcg$ be a morphism of sheaves.

(a) Show that $\im \varphi \cong \mcf / \ker \varphi$.

(b) Show that $\coker \varphi \cong \mcg / \im \varphi$.
:::

::: {.solution}

::: pf

::: {.pf-step #varphi-factors-through-quotient}
The morphism $\varphi:\mcf\to\mcg$ factors canonically as
$$
\mcf\xrightarrow{q}\mcf/\ker\varphi
\xrightarrow{\bar\varphi}\im\varphi
\hookrightarrow\mcg.
$$

::: pf-proof
The kernel subsheaf $\ker\varphi\subseteq\mcf$ is annihilated by $\varphi$.
By the universal property of the quotient sheaf, $\varphi$ therefore induces a unique morphism
$$
\bar\varphi:\mcf/\ker\varphi\longrightarrow\mcg.
$$
Its image is exactly the image sheaf $\im\varphi$, so it factors uniquely through the inclusion
$$
\im\varphi\hookrightarrow\mcg.
$$
This gives the displayed factorization.
:::

:::

::: {.pf-step #quotient-iso-image}
The induced morphism
$$
\boxed{\mcf/\ker\varphi\xrightarrow{\sim}\im\varphi}
$$
is an isomorphism.

::: pf-proof
At a point $x\in X$, the stalk of the quotient is
$$
(\mcf/\ker\varphi)_x
\cong
\mcf_x/\ker(\varphi_x)
$$
by [[P-AGH216QUOTSEQ|Exercise II.1.6]].
The stalk of the image sheaf is the ordinary image of the stalk map,
$$
(\im\varphi)_x=\im(\varphi_x).
$$
The stalk map induced by $\bar\varphi$ is therefore the ordinary first-isomorphism-theorem map
$$
\mcf_x/\ker(\varphi_x)
\xrightarrow{\sim}
\im(\varphi_x).
$$
Hence $\bar\varphi$ is an isomorphism on every stalk and therefore an isomorphism of sheaves.
This proves part (a).
:::

:::

::: {.pf-step #cokernel-is-cokernel-of-image-inclusion}
By definition, the cokernel sheaf of $\varphi$ is the cokernel of the inclusion
$$
\im\varphi\hookrightarrow\mcg.
$$

::: pf-proof
The cokernel of a morphism of sheaves is obtained by sheafifying the presheaf cokernel.
Since the morphism
$$
\im\varphi\hookrightarrow\mcg
$$
is injective, its cokernel is precisely the quotient sheaf of $\mcg$ by the subsheaf $\im\varphi$.
The original map $\varphi$ and the inclusion of its image have the same cokernel, because the map $\mcf\to\mcg$ factors through $\im\varphi$ and has image exactly that subsheaf.
:::

:::

::: {.pf-step #cokernel-iso-quotient}
There is a canonical isomorphism
$$
\boxed{\coker\varphi\cong\mcg/\im\varphi}.
$$

::: pf-proof
By step [](#cokernel-is-cokernel-of-image-inclusion){.pf-ref}, the cokernel fits into the short exact sequence
$$
\im\varphi\longrightarrow\mcg\longrightarrow\coker\varphi\longrightarrow0.
$$
Apply [[P-AGH216QUOTSEQ|Exercise II.1.6]] to the subsheaf $\im\varphi\subseteq\mcg$.
It identifies the terminal sheaf canonically with the quotient
$$
\mcg/\im\varphi.
$$
This proves part (b).
:::

:::

::: pf-qed
Steps [](#varphi-factors-through-quotient){.pf-ref} and [](#quotient-iso-image){.pf-ref} prove part (a), and steps [](#cokernel-is-cokernel-of-image-inclusion){.pf-ref} and [](#cokernel-iso-quotient){.pf-ref} prove part (b).
:::

:::

:::
