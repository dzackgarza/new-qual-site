---
schema: qual/card@1
id: P-BKF80-8
kind: problem
title: $GL_2(\mathbb F_2)$ is isomorphic to $S_3$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $G=GL_2(\FF_2)$, the group of invertible $2\times2$ matrices over the field with two elements. Prove that
$$
G\cong S_3.
$$
:::

::: {.solution}
Let
$$
V\coloneqq\FF_2^2\sm\{0\}.
$$
Then $V$ has exactly three elements.

::: pf

::: {.pf-step #rho-injective}
The natural action of $G$ on $V$ defines an injective homomorphism
$$
\rho:G\longrightarrow\operatorname{Sym}(V)\cong S_3.
$$

::: pf-proof
Every element of $G$ is an invertible linear map on $\FF_2^2$, so it sends nonzero vectors to nonzero vectors and therefore permutes $V$. This gives a homomorphism
$$
\rho:G\to\operatorname{Sym}(V).
$$
If $T\in\ker\rho$, then $T$ fixes every nonzero vector. In particular, for the standard basis $e_1,e_2$ one has
$$
Te_1=e_1,
\qquad
Te_2=e_2.
$$
Hence $T=I_2$, so $\ker\rho=\{I_2\}$ and $\rho$ is injective.
:::

:::

::: {.pf-step #g-order-six}
$\abs G=6$.

::: pf-proof
The first column of an invertible $2\times2$ matrix over $\FF_2$ can be any nonzero vector, giving $4-1=3$ choices. Once the first column is chosen, the second column must lie outside its one-dimensional span, which contains two vectors, giving $4-2=2$ choices. Thus
$$
\abs G=(4-1)(4-2)=6.
$$
:::

:::

::: {.pf-step #g-iso-s3}
$G\cong\boxed{S_3}$.

::: pf-proof
By step [](#rho-injective){.pf-ref}, $G$ embeds in $S_3$. Step [](#g-order-six){.pf-ref} gives
$$
\abs G=6=\abs{S_3}.
$$
Therefore the injective homomorphism $\rho:G\to S_3$ is surjective and hence an isomorphism.
:::

:::

::: pf-qed
Step [](#g-iso-s3){.pf-ref} proves the required isomorphism.
:::

:::
:::
