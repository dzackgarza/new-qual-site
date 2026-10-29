---
schema: qual/card@1
id: P-C6SRA
kind: problem
title: Examples of vanishing tensors over $\mathbf{Z}$ and $\mathbf{Q}$, torsion-free
  nonfree modules, maximal nonprime ideals, non-Noetherian rings, and non-ideal centers
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Modules
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---
::: {.problem}
For each of the following, either give an example or indicate that none exists.
You do not need to supply proofs.
a. Two non-zero $\mathbf{Z}$-modules $A$ and $B$ such that $A\otimes_{\mathbf{Z}} B=0$.
b. Two non-zero $\mathbf{Q}$-modules $V$ and $W$ such that $V\otimes_{\mathbf{Q}} W=0$.
c. A ring $R$ and a module $M$ over $R$ which is torsion free but is not free.
d. A ring $R$ and an ideal $I$ of $R$ that is maximal but not prime.
e. A ring which is not Noetherian.
f. A ring whose center is not an ideal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (a), take
\[
A=\ZZ/2\ZZ,
\qquad
B=\ZZ/3\ZZ.
\]
Then \(A\otimes_{\ZZ}B=0\).

::: pf-proof

Using \((\ZZ/m)\otimes_{\ZZ}B\cong B/mB\),
\[
(\ZZ/2)\otimes_{\ZZ}(\ZZ/3)
\cong (\ZZ/3)/2(\ZZ/3)=0,
\]
because multiplication by \(2\) is an automorphism of \(\ZZ/3\).

:::

:::

::: {.pf-step #s2}

For part (b), no such nonzero \(\QQ\)-modules exist.

::: pf-proof

A \(\QQ\)-module is a vector space. If \(0\ne v\in V\) and \(0\ne w\in W\), choose linear functionals \(\lambda:V\to\QQ\) and \(\mu:W\to\QQ\) with \(\lambda(v)=\mu(w)=1\). The induced map
\[
\lambda\otimes\mu:V\otimes_{\QQ}W\to\QQ
\]
sends \(v\otimes w\) to \(1\), so \(V\otimes_{\QQ}W\ne0\).

:::

:::

::: {.pf-step #s3}

For part (c), take \(R=\ZZ\) and \(M=\QQ\).

::: pf-proof

The \(\ZZ\)-module \(\QQ\) is torsion-free. It is not free: \(\QQ\) is divisible, whereas a nonzero free abelian group is not divisible.

:::

:::

::: {.pf-step #s4}

For part (d), take
\[
R=M_2(\QQ),
\qquad
I=0.
\]
Then \(I\) is maximal but not prime under the criterion that \(R/I\) be an integral domain.

::: pf-proof

The ring \(M_2(\QQ)\) is simple, so its only two-sided ideals are \(0\) and \(R\); hence \(0\) is maximal. But \(R\) has nonzero zero divisors, for example
\[
E_{11}E_{22}=0,
\]
so \(R/I\cong R\) is not an integral domain.

:::

:::

::: {.pf-step #s5}

For part (e), take
\[
R=k[x_1,x_2,x_3,\dots]
\]
for any field \(k\).

::: pf-proof

The ascending chain
\[
(x_1)\subsetneq(x_1,x_2)\subsetneq(x_1,x_2,x_3)\subsetneq\cdots
\]
does not stabilize, so \(R\) is not Noetherian.

:::

:::

::: {.pf-step #s6}

For part (f), again take \(R=M_2(\QQ)\).

::: pf-proof

Its center is
\[
Z(R)=\{aI_2:a\in\QQ\}.
\]
This is a proper subset of \(R\) but contains the identity matrix. Any two-sided ideal containing \(1\) is all of \(R\), so \(Z(R)\) is not an ideal.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} answer parts (a)--(f), respectively.

:::

:::

:::
