---
schema: qual/card@1
id: P-CASP15F
kind: problem
title: "Sum of zeros minus poles of an elliptic function in a fundamental parallelogram"
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Residue Theorem
  - Periodic Functions
relations: []
review: draft
---

::: problem
Let $f(z)$ be an elliptic function with periods $\omega_1, \omega_2$.
Assume that $f(z)$ has no zeros or poles on $\partial P$, where
$$
P := \{z = s_1 \omega_1 + s_2 \omega_2 \mid 0 < s_1, s_2 < 1\}
$$
and let $a_1, a_2, \ldots, a_m$ denote the zeros and $b_1, b_2, \ldots, b_n$ the poles of $f(z)$ in $P$ (each repeated according to multiplicity).
State and prove a theorem regarding $\sum_{j=1}^m a_j - \sum_{k=1}^n b_k$.
:::

::: solution
Let
\[
\Lambda=\mathbb Z\omega_1+\mathbb Z\omega_2.
\]
Then
\[
\boxed{\sum_{j=1}^m a_j-\sum_{k=1}^n b_k\in\Lambda.}
\]
In particular the sum of the zeros and the sum of the poles are congruent
modulo the period lattice.

First, by the argument principle,
\[
\frac1{2\pi i}\int_{\partial P}\frac{f'(z)}{f(z)}\,dz=m-n.
\]
Opposite sides of $P$ cancel because $f'/f$ is elliptic, so the integral is
$0$ and therefore $m=n$.

Now apply the residue theorem to
\[
z\frac{f'(z)}{f(z)}.
\]
Its residue at a zero is the zero location counted with multiplicity, and at
a pole it is minus the pole location counted with multiplicity. Hence
\[
\sum_j a_j-\sum_k b_k
=\frac1{2\pi i}\int_{\partial P}z\frac{f'(z)}{f(z)}\,dz.
\]

Pair the two sides parallel to $\omega_1$. Translating one side by
$\omega_2$ and using periodicity of $f'/f$ shows that their combined
contribution is
\[
-\omega_2\int_{\gamma_1}\frac{f'}f\,dz.
\]
Similarly the pair parallel to $\omega_2$ contributes
\[
\omega_1\int_{\gamma_2}\frac{f'}f\,dz.
\]
Each integral of $f'/f$ divided by $2\pi i$ is an integer, namely the winding
number of the corresponding closed image curve under $f$. Therefore
\[
\sum_j a_j-\sum_k b_k
=N_1\omega_1+N_2\omega_2
\]
for some $N_1,N_2\in\mathbb Z$, proving the claim.
:::
