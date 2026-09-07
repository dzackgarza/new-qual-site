---
schema: qual/card@1
id: P-ALGF14E
kind: problem
title: Nilpotent matrices in $M_n(\mathbb{C})$ and similarity classes in $M_4(\mathbb{C})$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2014; both parts and the characteristic-polynomial hint agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Cayley-Hamilton proof and the classification of nilpotent similarity classes by partitions of 4.
---

::: {.problem}
(i) Suppose $x \in M_n(\mathbb{C})$ is a nilpotent matrix.
Prove that $x^n = 0$.
(Hint: think of the characteristic polynomial.)

(ii) How many similarity classes are there of nilpotent matrices in $M_4(\mathbb{C})$?
:::


::: {.solution}
<1>1. If \(x\in M_n(\mathbb C)\) is nilpotent, then every eigenvalue of \(x\) is zero.
::: {.proof}
Choose \(m\ge1\) such that
\[
x^m=0.
\]
If \(v\neq0\) is an eigenvector with eigenvalue \(\lambda\), then
\[
0=x^mv=\lambda^m v.
\]
Hence \(\lambda^m=0\), so
\[
\lambda=0.
\]
Thus zero is the only eigenvalue of \(x\).
:::

<1>2. The characteristic polynomial of \(x\) is \(t^n\), and therefore \(x^n=0\).
::: {.proof}
Over \(\mathbb C\), the characteristic polynomial splits into linear factors and its roots are exactly the eigenvalues, counted with algebraic multiplicity.
By <1>1 every eigenvalue is zero, so
\[
\chi_x(t)=t^n.
\]
The Cayley-Hamilton theorem gives
\[
\chi_x(x)=0.
\]
Hence
\[
x^n=0.
\]
:::

<1>3. Nilpotent similarity classes in \(M_4(\mathbb C)\) are in bijection with partitions of \(4\).
::: {.proof}
Every nilpotent complex matrix has Jordan canonical form consisting entirely of Jordan blocks
\[
J_r(0).
\]
Two nilpotent matrices are similar if and only if their multisets of Jordan block sizes agree.
Thus a similarity class is determined exactly by a partition of the dimension \(4\).
:::

<1>4. There are exactly five nilpotent similarity classes in \(M_4(\mathbb C)\).
::: {.proof}
The partitions of \(4\) are
\[
4,
\qquad
3+1,
\qquad
2+2,
\qquad
2+1+1,
\qquad
1+1+1+1.
\]
They correspond respectively to the Jordan forms
\[
J_4(0),
\]
\[
J_3(0)\oplus J_1(0),
\]
\[
J_2(0)\oplus J_2(0),
\]
\[
J_2(0)\oplus J_1(0)\oplus J_1(0),
\]
and
\[
0_4.
\]
Therefore there are
\[
5
\]
similarity classes of nilpotent matrices in \(M_4(\mathbb C)\).
:::
:::
