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

::: pf-step

For part (a), take
\[
A=\mathbb Z/2\mathbb Z,
\qquad
B=\mathbb Z/3\mathbb Z.
\]
Then \(A\otimes_{\mathbb Z}B=0\).

::: pf-proof

Using \((\mathbb Z/m)\otimes_{\mathbb Z}B\cong B/mB\),
\[
(\mathbb Z/2)\otimes_{\mathbb Z}(\mathbb Z/3)
\cong (\mathbb Z/3)/2(\mathbb Z/3)=0,
\]
because multiplication by \(2\) is an automorphism of \(\mathbb Z/3\).

:::

:::

::: pf-step

For part (b), no such nonzero \(\mathbb Q\)-modules exist.

::: pf-proof

A \(\mathbb Q\)-module is a vector space. If \(0\ne v\in V\) and \(0\ne w\in W\), choose linear functionals \(\lambda:V\to\mathbb Q\) and \(\mu:W\to\mathbb Q\) with \(\lambda(v)=\mu(w)=1\). The induced map
\[
\lambda\otimes\mu:V\otimes_{\mathbb Q}W\to\mathbb Q
\]
sends \(v\otimes w\) to \(1\), so \(V\otimes_{\mathbb Q}W\ne0\).

:::

:::

::: pf-step

For part (c), take \(R=\mathbb Z\) and \(M=\mathbb Q\).

::: pf-proof

The \(\mathbb Z\)-module \(\mathbb Q\) is torsion-free. It is not free: \(\mathbb Q\) is divisible, whereas a nonzero free abelian group is not divisible.

:::

:::

::: pf-step

For part (d), no example exists in a ring with identity; without identity, take
\[
R=2\mathbb Z,
\qquad
I=4\mathbb Z.
\]

::: pf-proof

In a ring with identity, a maximal two-sided ideal \(I\) is prime: if \(a,b\notin I\) and \(aRb\subseteq I\), then \(R=I+RaR\) and \(R=I+RbR\), so \(R=R\cdot R\subseteq I+RaR\,RbR\subseteq I+R(aRb)R\subseteq I\), a contradiction. In \(R=2\mathbb Z\), the ideal \(4\mathbb Z\) has index \(2\), so no ideal lies strictly between it and \(R\), and it is maximal. It is not prime, since \(2\cdot2=4\in I\) while \(2\notin I\).

:::

:::

::: pf-step

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

::: pf-step

For part (f), again take \(R=M_2(\mathbb Q)\).

::: pf-proof

Its center is
\[
Z(R)=\{aI_2:a\in\mathbb Q\}.
\]
This is a proper subset of \(R\) but contains the identity matrix. Any two-sided ideal containing \(1\) is all of \(R\), so \(Z(R)\) is not an ideal.

:::

:::

:::

:::
