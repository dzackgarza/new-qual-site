---
schema: qual/card@1
id: P-ALGF13D
kind: problem
title: Injectivity of direct sums; projectivity after base change
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
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2013; both parts agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified injectivity of finite direct sums by the extension property and projectivity after scalar extension via split free summands.
---

::: {.problem}
Let $A$ be a commutative ring.
Let $P$ and $Q$ be $A$-modules.

(a) Prove that $P \oplus Q$ is an injective $A$-module if and only if both $P$ and $Q$ are injective $A$-modules.

(b) Let $A \subseteq B$, where $B$ is another commutative ring and $A$ is a unital subring of $B$.
Prove that if $P$ is a projective $A$-module, then $P \otimes_A B$ is a projective $B$-module.
:::

::: {.solution}
<1>1. If \(P\oplus Q\) is injective, then both \(P\) and \(Q\) are injective.
::: {.proof}
We prove the assertion for \(P\); the argument for \(Q\) is identical.
Let
\[
N\hookrightarrow M
\]
be an inclusion of \(A\)-modules and let
\[
f:N\to P
\]
be an \(A\)-linear map.
Compose with the canonical inclusion
\[
\iota_P:P\hookrightarrow P\oplus Q
\]
to obtain
\[
\iota_Pf:N\to P\oplus Q.
\]
Since \(P\oplus Q\) is injective, there is an extension
\[
F:M\to P\oplus Q
\]
whose restriction to \(N\) is \(\iota_Pf\).
Let
\[
\pi_P:P\oplus Q\to P
\]
be projection onto the first summand.
Then
\[
\pi_PF:M\to P
\]
extends \(f\), because on \(N\)
\[
\pi_PF|_N=\pi_P\iota_Pf=f.
\]
Thus \(P\) satisfies the extension property and is injective.
:::

<1>2. If \(P\) and \(Q\) are injective, then \(P\oplus Q\) is injective.
::: {.proof}
Let \(N\hookrightarrow M\) be an inclusion and let
\[
f:N\to P\oplus Q
\]
be \(A\)-linear.
Write
\[
f=(f_P,f_Q)
\]
with
\[
f_P:N\to P,
\qquad
f_Q:N\to Q.
\]
By injectivity of \(P\) and \(Q\), extend these maps to
\[
F_P:M\to P,
\qquad
F_Q:M\to Q.
\]
Then
\[
F=(F_P,F_Q):M\to P\oplus Q
\]
extends \(f\).
Hence \(P\oplus Q\) is injective.
:::

<1>3. Therefore \(P\oplus Q\) is injective if and only if both summands are injective.
::: {.proof}
The forward implication is <1>1 and the reverse implication is <1>2.
:::

<1>4. If \(P\) is projective over \(A\), then \(P\otimes_A B\) is projective over \(B\).
::: {.proof}
Because \(P\) is projective, there exists an \(A\)-module \(Q\) and a free \(A\)-module \(F\) such that
\[
P\oplus Q\cong F.
\]
Tensor this split decomposition with \(B\) over \(A\).
Since tensor product commutes with direct sums,
\[
(P\otimes_A B)\oplus(Q\otimes_A B)
\cong
F\otimes_A B.
\]
If
\[
F\cong\bigoplus_{j\in J}A,
\]
then
\[
F\otimes_A B
\cong
\bigoplus_{j\in J}(A\otimes_A B)
\cong
\bigoplus_{j\in J}B,
\]
which is a free \(B\)-module.
Therefore \(P\otimes_A B\) is a direct summand of a free \(B\)-module, hence is projective as a \(B\)-module.
:::
:::
