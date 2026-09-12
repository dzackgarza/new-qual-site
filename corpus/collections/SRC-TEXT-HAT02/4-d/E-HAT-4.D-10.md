---
schema: qual/card@1
id: E-HAT-4.D-10
kind: problem
title: "Eigenvalues of quaternionic matrices"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.D, Exercise 10; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Fill in the details of the following argument to show that every $n \times n$ matrix $A$ with entries in $\mathbb{H}$ has an eigenvalue in $\mathbb{H}$.
For $t \in [0, 1]$ and $\lambda \in S^3 \subset \mathbb{H}$, consider the matrix $t\lambda I + (1-t)A$.
If $A$ has no eigenvalues, this is invertible for all $t$.
Thus the map $S^3 \to GL_n(\mathbb{H})$, $\lambda \mapsto \lambda I$, is nullhomotopic.
But by the preceding problem and Exercise 10(b) in §3.C, this map represents $n$ times a generator of $\pi_3 GL_n(\mathbb{H})$.

::: {.solution}
Assume, for contradiction, that \(A\in M_n(\mathbb H)\) has no (left) eigenvalue. In particular \(A\) is invertible. For
\[
t\in[0,1],\qquad \lambda\in S^3\subset\mathbb H,
\]
set
\[
H(t,\lambda)=t\lambda I+(1-t)A.
\]
If \(0\le t<1\) and \(H(t,\lambda)\) were singular, there would be \(v\ne0\) with
\[
Av=-\frac{t}{1-t}\lambda v,
\]
so \(-\frac{t}{1-t}\lambda\) would be an eigenvalue of \(A\), contrary to hypothesis. For \(t=1\), \(H(1,\lambda)=\lambda I\) is invertible. Thus
\[
H:[0,1]\times S^3\to GL_n(\mathbb H)
\]
is a homotopy from the constant map \(\lambda\mapsto A\) to
\[
\lambda\longmapsto\lambda I.
\]
Hence the latter map would be nullhomotopic.

But \(GL_n(\mathbb H)\) deformation retracts onto \(Sp(n)\), and the preceding exercise homotopes \(\lambda I=\operatorname{diag}(\lambda,\ldots,\lambda)\) to
\[
\operatorname{diag}(\lambda^n,1,\ldots,1).
\]
By Exercise 10(b) of §3.C, the power map \(S^3\to S^3\), \(\lambda\mapsto\lambda^n\), represents \(n\) times a generator of \(\pi_3(S^3)\). The inclusion \(Sp(1)\hookrightarrow Sp(n)\) induces an isomorphism on \(\pi_3\), so \(\lambda\mapsto\lambda I\) represents
\[
n\ne0\in\pi_3(GL_n(\mathbb H))\cong\mathbb Z.
\]
This contradicts nullhomotopy. Therefore every quaternionic matrix has an eigenvalue:
\[
\boxed{\exists\lambda\in\mathbb H,\ v\ne0\text{ with }Av=\lambda v.}
\]
:::
