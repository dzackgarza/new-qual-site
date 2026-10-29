---
schema: qual/card@1
id: P-UCSD-ALG-REVIEW-RM-08
kind: problem
title: Tensoring finitely generated modules with $\QQ$ and extending scalars $\RR[x]\to\CC[x]$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Tensor Products
  - Modules over PIDs
relations:
- kind: variant-of
  target: P-ALGF07D
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
(a) Give an example of two finitely generated $\ZZ$-modules $M$ and $N$ that are not isomorphic as $\ZZ$-modules but satisfy
$$
\QQ\otimes_{\ZZ}M\cong \QQ\otimes_{\ZZ}N
$$
as $\QQ$-modules.

(b) Let $M$ be a finitely generated $\RR[x]$-module, described using the classification of finitely generated modules over a PID. Give a corresponding description of
$$
\CC[x]\otimes_{\RR[x]}M
$$
as a $\CC[x]$-module.
:::

::: {.solution}

::: pf

::: pf-step

For part (a), take
$$
M=\ZZ,
\qquad
N=\ZZ\oplus\ZZ/2\ZZ.
$$
Then $M\not\cong N$ as $\ZZ$-modules, but
$$
\QQ\otimes_{\ZZ}M
\cong
\QQ
\cong
\QQ\otimes_{\ZZ}N.
$$

::: pf-proof

The module $N$ has nonzero torsion while $M$ is torsionfree, so they are not isomorphic.
Also
$$
\QQ\otimes_{\ZZ}(\ZZ/2\ZZ)=0,
$$
because $2$ is invertible in $\QQ$. Hence
$$
\QQ\otimes_{\ZZ}N
\cong
\QQ\oplus0
\cong\QQ.
$$

:::

:::

::: pf-step

Write the elementary-divisor decomposition of the finitely generated $\RR[x]$-module $M$ as
$$
M\cong \RR[x]^r
\oplus
\bigoplus_{i=1}^s \RR[x]/(p_i(x)^{e_i}),
$$
where each $p_i$ is monic irreducible in $\RR[x]$ and $e_i\ge1$.

::: pf-proof

The ring $\RR[x]$ is a PID, so this is the elementary-divisor form of the structure theorem for finitely generated modules over a PID.

:::

:::

::: {.pf-step #s3}

Extension of scalars gives
$$
\CC[x]\otimes_{\RR[x]}M
\cong
\CC[x]^r
\oplus
\bigoplus_{i=1}^s \CC[x]/(p_i(x)^{e_i}).
$$

::: pf-proof

Tensor product commutes with finite direct sums, and
$$
\CC[x]\otimes_{\RR[x]}\RR[x]\cong\CC[x].
$$
For every ideal $(a)\subseteq\RR[x]$, right exactness applied to
$$
\RR[x]\xrightarrow{\cdot a}\RR[x]\to\RR[x]/(a)\to0
$$
gives
$$
\CC[x]\otimes_{\RR[x]}\RR[x]/(a)
\cong
\CC[x]/(a)\CC[x].
$$
Apply this with $a=p_i^{e_i}$.

:::

:::

::: {.pf-step #s4}

If $p_i(x)=x-a$ with $a\in\RR$, then the corresponding summand remains
$$
\CC[x]/((x-a)^{e_i}).
$$

::: pf-proof

A real linear irreducible remains linear over $\CC$.

:::

:::

::: {.pf-step #s5}

If $p_i$ is an irreducible quadratic over $\RR$, write
$$
p_i(x)=(x-z_i)(x-\overline z_i),
\qquad z_i\in\CC\setminus\RR.
$$
Then
$$
\CC[x]/(p_i^{e_i})
\cong
\CC[x]/((x-z_i)^{e_i})
\oplus
\CC[x]/((x-\overline z_i)^{e_i}).
$$

::: pf-proof

The two linear factors are distinct, so their powers are coprime. The Chinese remainder theorem gives
$$
\CC[x]/\big((x-z_i)^{e_i}(x-\overline z_i)^{e_i}\big)
\cong
\CC[x]/((x-z_i)^{e_i})
\oplus
\CC[x]/((x-\overline z_i)^{e_i}).
$$

:::

:::

::: pf-step

Thus scalar extension preserves the free rank, preserves each real-linear primary summand, and splits every real-quadratic primary summand into the two conjugate complex primary summands described in step [](#s5){.pf-ref}.

::: pf-proof

Combine steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref}. Every monic irreducible polynomial over $\RR$ has degree $1$ or $2$.

:::

:::

:::

:::
