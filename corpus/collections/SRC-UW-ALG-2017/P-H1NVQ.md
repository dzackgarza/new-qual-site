---
schema: qual/card@1
id: P-H1NVQ
kind: problem
title: $M_2(\FF_4)\otimes_{\FF_2}M_2(\FF_4)$ as a product of matrix rings over division rings
classification:
  areas:
  - algebra
  topics:
  - Rings
  - Tensor Products
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2017`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Answered: the tensor is $\cong M_4(\FF_4)\times M_4(\FF_4)$. Uses
    $M_n(R)\otimes_SM_m(R)\cong M_{nm}(R\otimes_SR)$ and
    $\FF_4\otimes_{\FF_2}\FF_4\cong\FF_4\times\FF_4$ from the factorisation
    $X^2+X+1=(X-\alpha)(X-\alpha^2)$ over $\FF_4$ and the Chinese remainder theorem; the
    $\FF_2$-dimension check $64=32+32$ confirms no factor is missing. Nothing is left in outline.
---

::: {.problem}
If $q$ is a power of a prime let $\FF_q$ denote the field with $q$ elements.
Given an explicit description of $M_2(\FF_4)\otimes_{\FF_2}M_2(\FF_4)$ as a direct product of matrix rings over division rings.
:::

::: {.solution}

Let $A=M_2(\FF_4)$, regarded as an $\FF_4$-algebra and hence as an $\FF_2$-algebra of dimension $8$. We describe $A\otimes_{\FF_2}A$.

::: pf

::: {.pf-step #s1}

$\FF_4\otimes_{\FF_2}\FF_4\cong\FF_4\times\FF_4$ as $\FF_2$-algebras.

::: pf-proof

Write $\FF_4=\FF_2[\alpha]$ with $\alpha^2+\alpha+1=0$. Then
$$
\FF_4\otimes_{\FF_2}\FF_4\cong\FF_4[X]/(X^2+X+1).
$$
Over $\FF_4$ the polynomial factors as
$$
X^2+X+1=(X-\alpha)(X-\alpha^2),
$$
because $\alpha^2+\alpha+1=0$ gives $\alpha^2=\alpha+1$, and the two roots $\alpha,\alpha^2$ are distinct since $\alpha\notin\FF_2$; indeed the sum of the factors' roots is $\alpha+\alpha^2=1$ and their product is $\alpha^3=1$, matching the coefficients. The two factors are coprime, so by the Chinese remainder theorem
$$
\FF_4[X]/(X^2+X+1)\cong\FF_4[X]/(X-\alpha)\times\FF_4[X]/(X-\alpha^2)\cong\FF_4\times\FF_4 .
$$

:::

:::

::: {.pf-step #s2}

For $S$-algebras $R,R'$ there is an isomorphism $M_n(R)\otimes_SM_m(R')\cong M_{nm}(R\otimes_SR')$.

::: pf-proof

Let $e_{ij}$ and $f_{kl}$ be the matrix units. The elements $e_{ij}\otimes f_{kl}$ form an $R\otimes_SR'$-basis of $M_n(R)\otimes_SM_m(R')$ and multiply by
$$
(e_{ij}\otimes f_{kl})(e_{i'j'}\otimes f_{k'l'})=\delta_{ji'}\delta_{lk'}\,e_{ij'}\otimes f_{kl'},
$$
which is the multiplication rule of the matrix units $E_{(ik),(j'l')}$ of $M_{nm}(R\otimes_SR')$ under the identification of the index set $\{1,\dots,n\}\times\{1,\dots,m\}$ with $\{1,\dots,nm\}$. Since both sides are free of the same rank over $R\otimes_SR'$ and the multplication tables agree, the assignment $e_{ij}\otimes f_{kl}\mapsto E_{(ik),(jl)}$ extends to an algebra isomorphism.

:::

:::

::: {.pf-step #s3}

$M_2(\FF_4)\otimes_{\FF_2}M_2(\FF_4)\cong M_4(\FF_4)\times M_4(\FF_4)$, a direct product of two matrix rings over the division ring $\FF_4$.

::: pf-proof

By step [](#s2){.pf-ref} with $n=m=2$, $S=\FF_2$ and $R=R'=\FF_4$,
$$
M_2(\FF_4)\otimes_{\FF_2}M_2(\FF_4)\cong M_4\bigl(\FF_4\otimes_{\FF_2}\FF_4\bigr)\cong M_4(\FF_4\times\FF_4)\cong M_4(\FF_4)\times M_4(\FF_4),
$$
where step [](#s1){.pf-ref} was used for the middle isomorphism, and the last isomorphism is the standard $M_4(R\times R')\cong M_4(R)\times M_4(R')$.

:::

:::

::: {.pf-step #s4}

The description is complete: no further factor occurs, and $\FF_4$ is a division ring.

::: pf-proof

Dimensions over $\FF_2$: the left side has $\FF_2$-dimension $8\cdot8=64$; the right side has $2\cdot\dim_{\FF_2}M_4(\FF_4)=2\cdot 4^2\cdot 2=64$. So the two sides have the same dimension and the isomorphism of step [](#s3){.pf-ref} accounts for the whole algebra.

By the Wedderburn--Artin description, a semisimple finite-dimensional algebra is a product of matrix rings over division rings; here the two factors are $M_4(\FF_4)$, with $\FF_4$ a field and hence a division ring, so this is the asserted product decomposition.

:::

:::

:::

:::
