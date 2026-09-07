---
schema: qual/card@1
id: P-ALGF11G
kind: problem
title: Tensoring with $R/I$; dimension over $R/I$ for modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 7 of the official UCSD Algebra Qualifying Exam, Fall 2011; both parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the quotient-tensor isomorphism and the exact dimension formula from the PID elementary-divisor decomposition.
---

::: {.problem}
(a) Let $M$ be a (left) module over a commutative ring $R$ and let $I$ be an ideal of $R$.
Prove that
\[
(R/I) \otimes_R M \cong M/IM
\]
(as $R$-modules).

(b) Now let $R$ be a PID and let $I$ be a maximal ideal of $R$.
Suppose that $M$ is a finitely generated $R$-module.
Calculate the dimension of $(R/I) \otimes_R M$ as a vector space over the field $K = R/I$ in terms of the elementary divisors (or invariant factors) of $M$.
:::


::: {.solution}
<1>1. There is a canonical isomorphism
\[
(R/I)\otimes_R M\cong M/IM.
\]
::: {.proof}
Define
\[
\Phi:(R/I)\otimes_RM\longrightarrow M/IM
\]
on pure tensors by
\[
\Phi((r+I)\otimes m)=rm+IM.
\]
This is well defined: changing \(r\) by an element of \(I\) changes \(rm\) by an element of \(IM\), and the formula is \(R\)-balanced because
\[
\Phi(((rs)+I)\otimes m)=rsm+IM
=\Phi((r+I)\otimes sm).
\]
Thus \(\Phi\) is an \(R\)-module homomorphism.

Conversely define
\[
\Psi:M/IM\longrightarrow(R/I)\otimes_RM,
\qquad
\Psi(m+IM)=(1+I)\otimes m.
\]
If \(m-m'\in IM\), write
\[
m-m'=\sum_j i_jm_j
\qquad(i_j\in I).
\]
Then
\[
(1+I)\otimes(m-m')
=\sum_j(1+I)\otimes i_jm_j
=\sum_j(i_j+I)\otimes m_j
=0,
\]
so \(\Psi\) is well defined.
Finally,
\[
\Phi\Psi(m+IM)=m+IM
\]
and
\[
\Psi\Phi((r+I)\otimes m)
=(1+I)\otimes rm
=(r+I)\otimes m.
\]
Thus \(\Phi\) and \(\Psi\) are inverse isomorphisms.
:::

<1>2. Let \(I=(\pi)\) with \(\pi\) irreducible, and write the elementary-divisor decomposition
\[
M\cong R^r\oplus
\bigoplus_{j=1}^t R/(q_j^{e_j}),
\]
where each \(q_j\) is irreducible.
Then
\[
\dim_K((R/I)\otimes_RM)
=r+\#\{j:q_j\text{ is associate to }\pi\}.
\]
::: {.proof}
Since \(I\) is maximal in the PID \(R\),
\[
I=(\pi)
\]
for an irreducible \(\pi\), and
\[
K=R/I.
\]
Tensor product commutes with finite direct sums, so
\[
K\otimes_RM
\cong K^r\oplus
\bigoplus_{j=1}^t K\otimes_R R/(q_j^{e_j}).
\]
The free part contributes dimension \(r\).

For a torsion summand, <1>1 gives
\[
K\otimes_RR/(q_j^{e_j})
\cong
\frac{R/(q_j^{e_j})}{I(R/(q_j^{e_j}))}
\cong
R/(I+(q_j^{e_j})).
\]
If \(q_j\) is associate to \(\pi\), then
\[
I+(q_j^{e_j})=I,
\]
so this quotient is \(K\) and contributes one dimension.
If \(q_j\) is not associate to \(\pi\), then \(\pi\) and \(q_j\) are relatively prime, hence
\[
I+(q_j^{e_j})=R,
\]
so the quotient is zero.
Summing the contributions proves the formula.
:::

<1>3. In invariant-factor form, if
\[
M\cong R^r\oplus\bigoplus_{j=1}^sR/(d_j),
\qquad d_1\mid d_2\mid\cdots\mid d_s,
\]
then
\[
\dim_K((R/I)\otimes_RM)
=r+\#\{j:\pi\mid d_j\}.
\]
::: {.proof}
As above,
\[
K\otimes_RR/(d_j)
\cong R/(I+(d_j)).
\]
This is \(K\) exactly when \(d_j\in I\), equivalently \(\pi\mid d_j\), and is zero otherwise.
Adding the free contribution gives the stated formula.
:::
:::
