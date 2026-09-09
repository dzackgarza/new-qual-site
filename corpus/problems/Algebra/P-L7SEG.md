---
schema: qual/card@1
id: P-L7SEG
kind: problem
title: Image, kernel, cosets, and the first isomorphism theorem
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Normal Subgroups
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $\phi:G_1\to G_2$ be a group homomorphism and let $H_2\le G_2$. Put
\[
H_1=\phi^{-1}(H_2).
\]

1. Show that $\phi(G_1)\le G_2$ and $H_1\le G_1$.
2. Show that $\ker\phi\trianglelefteq G_1$.
3. Prove
   \[
   xH_1=yH_1
   \iff
   \phi(x)H_2=\phi(y)H_2.
   \]
4. Show that $\phi$ is injective iff $\ker\phi=\{e\}$.
5. Prove the first isomorphism theorem
   \[
   G_1/\ker\phi\cong\operatorname{im}\phi.
   \]
:::

::: {.solution}
<1>1. Images and preimages are subgroups.
::: {.proof}
If $a=\phi(x)$ and $b=\phi(y)$ lie in $\phi(G_1)$, then
\[
ab^{-1}=\phi(xy^{-1})\in\phi(G_1),
\]
so the image is a subgroup.

If $x,y\in H_1$, then $\phi(x),\phi(y)\in H_2$, hence
\[
\phi(xy^{-1})=\phi(x)\phi(y)^{-1}\in H_2.
\]
Thus $xy^{-1}\in H_1$.
:::

<1>2. The kernel is normal.
::: {.proof}
If $k\in\ker\phi$ and $g\in G_1$, then
\[
\phi(gkg^{-1})=\phi(g)e\phi(g)^{-1}=e,
\]
so $gkg^{-1}\in\ker\phi$.
:::

<1>3. The coset criterion holds.
::: {.proof}
We have
\[
xH_1=yH_1
\iff y^{-1}x\in H_1
\iff \phi(y)^{-1}\phi(x)\in H_2
\iff \phi(x)H_2=\phi(y)H_2.
\]
:::

<1>4. Injectivity is equivalent to trivial kernel.
::: {.proof}
If $\phi$ is injective, then $\phi(g)=e$ implies $g=e$. Conversely, if $\ker\phi=\{e\}$ and $\phi(x)=\phi(y)$, then
\[
\phi(y^{-1}x)=e,
\]
so $y^{-1}x=e$ and $x=y$.
:::

<1>5. First isomorphism theorem.
::: {.proof}
Define
\[
\bar\phi:G_1/\ker\phi\to\operatorname{im}\phi,
\qquad
\bar\phi(g\ker\phi)=\phi(g).
\]
This is well defined because two cosets are equal exactly when their quotient lies in the kernel. It is a surjective homomorphism by construction, and its kernel is trivial by <1>4. Hence it is an isomorphism.
:::
:::
