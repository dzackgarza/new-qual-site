---
schema: qual/card@1
id: P-ALGS21E
kind: problem
title: "Higher Ext groups over Z for Z/2Z with coefficients in Z and Q"
classification:
  areas:
  - algebra
  topics:
  - Homological Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
For $i \geq 0$, calculate $\operatorname{Ext}^i_\ZZ(\ZZ/2\ZZ, \ZZ)$ and $\operatorname{Ext}^i_\ZZ(\ZZ/2\ZZ, \QQ)$.
:::

::: {.solution}

::: pf

::: pf-step

Use the free resolution
$$
0\longrightarrow\ZZ\xrightarrow{\cdot2}\ZZ\longrightarrow\ZZ/2\ZZ\longrightarrow0.
$$

::: pf-proof

Multiplication by $2$ is injective on $\ZZ$, and its cokernel is $\ZZ/2\ZZ$. Thus this is a projective resolution of length $1$.

:::

:::

::: {.pf-step #s2}

For any abelian group $M$, applying $\operatorname{Hom}_{\ZZ}(-,M)$ gives the cochain complex
$$
0\longrightarrow M\xrightarrow{\cdot2}M\longrightarrow0.
$$
Hence
$$
\operatorname{Ext}^0_{\ZZ}(\ZZ/2,M)=\ker(2:M\to M),
$$
$$
\operatorname{Ext}^1_{\ZZ}(\ZZ/2,M)=M/2M,
$$
and $\operatorname{Ext}^i=0$ for $i\ge2$.

::: pf-proof

One has $\operatorname{Hom}_{\ZZ}(\ZZ,M)\cong M$, and precomposition with multiplication by $2$ becomes multiplication by $2$ on $M$. The cohomology in degrees $0$ and $1$ is therefore the displayed kernel and cokernel, and there are no higher terms.

:::

:::

::: pf-step

Taking $M=\ZZ$,
$$
\operatorname{Ext}^i_{\ZZ}(\ZZ/2,\ZZ)
\cong
\begin{cases}
0,&i=0,\\
\ZZ/2\ZZ,&i=1,\\
0,&i\ge2.
\end{cases}
$$

::: pf-proof

Multiplication by $2$ on $\ZZ$ is injective, so the degree-zero kernel is zero, and its cokernel is $\ZZ/2\ZZ$. Apply step [](#s2){.pf-ref}.

:::

:::

::: pf-step

Taking $M=\QQ$,
$$
\operatorname{Ext}^i_{\ZZ}(\ZZ/2,\QQ)=0
\qquad\text{for every }i\ge0.
$$

::: pf-proof

Multiplication by $2$ is an automorphism of $\QQ$, so both its kernel and cokernel are zero. Higher Ext groups vanish by step [](#s2){.pf-ref}.

:::

:::

:::

:::
