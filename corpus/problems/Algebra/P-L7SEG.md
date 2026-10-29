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

::: {.problem}
Let $\phi:G_1\to G_2$ be a group homomorphism and let $H_2\le G_2$. Put
$$
H_1=\phi^{-1}(H_2).
$$

(a) Show that $\phi(G_1)\le G_2$ and $H_1\le G_1$.

(b) Show that $\ker\phi\trianglelefteq G_1$.

(c) Prove
$$
xH_1=yH_1
\iff
\phi(x)H_2=\phi(y)H_2.
$$

(d) Show that $\phi$ is injective iff $\ker\phi=\{e\}$.

(e) Prove the first isomorphism theorem
$$
G_1/\ker\phi\cong\im\phi.
$$
:::

::: {.solution}

::: pf

::: pf-step
(a) $\phi(G_1)\le G_2$ and $H_1\le G_1$.

::: pf-proof
Both sets contain the identity. If $a=\phi(x)$ and $b=\phi(y)$, then $ab^{-1}=\phi(xy^{-1})\in\phi(G_1)$. If $x,y\in H_1$, then $\phi(xy^{-1})=\phi(x)\phi(y)^{-1}\in H_2$, so $xy^{-1}\in H_1$.
:::

:::

::: pf-step
(b) $\ker\phi\trianglelefteq G_1$.

::: pf-proof
For $k\in\ker\phi$ and $g\in G_1$, $\phi(gkg^{-1})=\phi(g)\,e\,\phi(g)^{-1}=e$.
:::

:::

::: {.pf-step #cosets}
(c) $xH_1=yH_1\iff\phi(x)H_2=\phi(y)H_2$.

::: pf-proof
$xH_1=yH_1\iff y^{-1}x\in H_1\iff\phi(y)^{-1}\phi(x)\in H_2\iff\phi(x)H_2=\phi(y)H_2$.
:::

:::

::: pf-step
(d) $\phi$ is injective if and only if $\ker\phi=\{e\}$.

::: pf-proof
If $\phi$ is injective, then $\phi(g)=e=\phi(e)$ implies $g=e$. Conversely, if $\ker\phi=\{e\}$ and $\phi(x)=\phi(y)$, then $\phi(y^{-1}x)=e$, so $y^{-1}x=e$ and $x=y$.
:::

:::

::: pf-step
(e) $G_1/\ker\phi\cong\im\phi$.

::: pf-proof
Define $\bar\phi:G_1/\ker\phi\to\im\phi$ by $\bar\phi(g\ker\phi)=\phi(g)$. Taking $H_2=\{e\}$ in step [](#cosets){.pf-ref}, so that $H_1=\ker\phi$, shows that $\bar\phi$ is well defined and injective. It is a homomorphism because $\phi$ is, and surjective by construction.
:::

:::

:::

:::
