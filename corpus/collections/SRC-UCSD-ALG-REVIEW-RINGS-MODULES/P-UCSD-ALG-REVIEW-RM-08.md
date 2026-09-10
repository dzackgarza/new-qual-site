---
schema: qual/card@1
id: P-UCSD-ALG-REVIEW-RM-08
kind: problem
title: Tensoring finitely generated modules with $\mathbb Q$ and extending scalars $\mathbb R[x]\to\mathbb C[x]$
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
(a) Give an example of two finitely generated $\mathbb Z$-modules $M$ and $N$ that are not isomorphic as $\mathbb Z$-modules but satisfy
\[
\mathbb Q\otimes_{\mathbb Z}M\cong \mathbb Q\otimes_{\mathbb Z}N
\]
as $\mathbb Q$-modules.

(b) Let $M$ be a finitely generated $\mathbb R[x]$-module, described using the classification of finitely generated modules over a PID. Give a corresponding description of
\[
\mathbb C[x]\otimes_{\mathbb R[x]}M
\]
as a $\mathbb C[x]$-module.
:::

::: {.solution}
<1>1. For part (a), take
\[
M=\mathbb Z,
\qquad
N=\mathbb Z\oplus\mathbb Z/2\mathbb Z.
\]
Then $M\not\cong N$ as $\mathbb Z$-modules, but
\[
\mathbb Q\otimes_{\mathbb Z}M
\cong
\mathbb Q
\cong
\mathbb Q\otimes_{\mathbb Z}N.
\]
::: {.proof}
The module $N$ has nonzero torsion while $M$ is torsionfree, so they are not isomorphic.
Also
\[
\mathbb Q\otimes_{\mathbb Z}(\mathbb Z/2\mathbb Z)=0,
\]
because $2$ is invertible in $\mathbb Q$. Hence
\[
\mathbb Q\otimes_{\mathbb Z}N
\cong
\mathbb Q\oplus0
\cong\mathbb Q.
\]
:::

<1>2. Write the elementary-divisor decomposition of the finitely generated $\mathbb R[x]$-module $M$ as
\[
M\cong \mathbb R[x]^r
\oplus
\bigoplus_{i=1}^s \mathbb R[x]/(p_i(x)^{e_i}),
\]
where each $p_i$ is monic irreducible in $\mathbb R[x]$ and $e_i\ge1$.
::: {.proof}
The ring $\mathbb R[x]$ is a PID, so this is the elementary-divisor form of the structure theorem for finitely generated modules over a PID.
:::

<1>3. Extension of scalars gives
\[
\mathbb C[x]\otimes_{\mathbb R[x]}M
\cong
\mathbb C[x]^r
\oplus
\bigoplus_{i=1}^s \mathbb C[x]/(p_i(x)^{e_i}).
\]
::: {.proof}
Tensor product commutes with finite direct sums, and
\[
\mathbb C[x]\otimes_{\mathbb R[x]}\mathbb R[x]\cong\mathbb C[x].
\]
For every ideal $(a)\subseteq\mathbb R[x]$, right exactness applied to
\[
\mathbb R[x]\xrightarrow{\cdot a}\mathbb R[x]\to\mathbb R[x]/(a)\to0
\]
gives
\[
\mathbb C[x]\otimes_{\mathbb R[x]}\mathbb R[x]/(a)
\cong
\mathbb C[x]/(a)\mathbb C[x].
\]
Apply this with $a=p_i^{e_i}$.
:::

<1>4. If $p_i(x)=x-a$ with $a\in\mathbb R$, then the corresponding summand remains
\[
\mathbb C[x]/((x-a)^{e_i}).
\]
::: {.proof}
A real linear irreducible remains linear over $\mathbb C$.
:::

<1>5. If $p_i$ is an irreducible quadratic over $\mathbb R$, write
\[
p_i(x)=(x-z_i)(x-\overline z_i),
\qquad z_i\in\mathbb C\setminus\mathbb R.
\]
Then
\[
\mathbb C[x]/(p_i^{e_i})
\cong
\mathbb C[x]/((x-z_i)^{e_i})
\oplus
\mathbb C[x]/((x-\overline z_i)^{e_i}).
\]
::: {.proof}
The two linear factors are distinct, so their powers are coprime. The Chinese remainder theorem gives
\[
\mathbb C[x]/\big((x-z_i)^{e_i}(x-\overline z_i)^{e_i}\big)
\cong
\mathbb C[x]/((x-z_i)^{e_i})
\oplus
\mathbb C[x]/((x-\overline z_i)^{e_i}).
\]
:::

<1>6. Thus scalar extension preserves the free rank, preserves each real-linear primary summand, and splits every real-quadratic primary summand into the two conjugate complex primary summands described in <1>5.
::: {.proof}
Combine <1>3, <1>4, and <1>5. Every monic irreducible polynomial over $\mathbb R$ has degree $1$ or $2$.
:::
:::
