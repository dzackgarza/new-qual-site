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
  note: Checked against the repository review-sheet source assets/attachments/ringsandmodules.pdf, Fall 2009 problem 4 block.
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
Then \(M\not\cong N\) as \(\mathbb Z\)-modules, but
\[
\mathbb Q\otimes_{\mathbb Z}M\cong\mathbb Q\otimes_{\mathbb Z}N.
\]
::: {.proof}
The module \(N\) has nonzero \(2\)-torsion whereas \(M\) is torsion-free, so they are not isomorphic. Since \(\mathbb Q\) is a localization of \(\mathbb Z\), tensoring with \(\mathbb Q\) kills finite torsion; explicitly,
\[
\mathbb Q\otimes_{\mathbb Z}\mathbb Z/2\mathbb Z=0.
\]
Hence
\[
\mathbb Q\otimes_{\mathbb Z}N
\cong
\mathbb Q\oplus0
\cong
\mathbb Q
\cong
\mathbb Q\otimes_{\mathbb Z}M.
\]
:::

<1>2. Write the elementary-divisor decomposition of the finitely generated \(\mathbb R[x]\)-module \(M\) as
\[
M\cong \mathbb R[x]^r
\oplus
\bigoplus_j \mathbb R[x]/(p_j(x)^{e_j}),
\]
where each \(p_j\) is monic irreducible over \(\mathbb R\). Then
\[
\mathbb C[x]\otimes_{\mathbb R[x]}M
\cong
\mathbb C[x]^r
\oplus
\bigoplus_j \mathbb C[x]/(p_j(x)^{e_j}).
\]
::: {.proof}
Scalar extension commutes with finite direct sums, and for every \(f\in\mathbb R[x]\),
\[
\mathbb C[x]\otimes_{\mathbb R[x]}\mathbb R[x]/(f)
\cong
\mathbb C[x]/(f).
\]
This gives the displayed decomposition before factoring the \(p_j\)'s further over \(\mathbb C\).
:::

<1>3. More explicitly, real linear elementary divisors remain unchanged, while each irreducible real quadratic splits into a conjugate pair of complex linear elementary divisors.
::: {.proof}
Every monic irreducible polynomial over \(\mathbb R\) is either \(x-a\) with \(a\in\mathbb R\), or
\[
q_z(x)=(x-z)(x-\bar z)
\]
for a nonreal \(z\in\mathbb C\). Thus
\[
\mathbb C[x]/((x-a)^e)
\]
remains a single elementary-divisor block. For a quadratic block,
\[
\mathbb C[x]/(q_z(x)^e)
=
\mathbb C[x]/((x-z)^e(x-\bar z)^e).
\]
The two ideals \(((x-z)^e)\) and \(((x-\bar z)^e)\) are comaximal, so the Chinese remainder theorem gives
\[
\mathbb C[x]/(q_z^e)
\cong
\mathbb C[x]/((x-z)^e)
\oplus
\mathbb C[x]/((x-\bar z)^e).
\]
Therefore complexification preserves the free rank and replaces each real quadratic elementary-divisor block by the two corresponding conjugate complex linear blocks.
:::
:::
