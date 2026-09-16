---
schema: qual/card@1
id: E-SMI-8000E-GA5
kind: problem
title: Rank of a free abelian group is well defined
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the rank-invariance request with the local 8000e extraction, generators exercise 5 and its reference to exercise 4."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Applied Hom(-,Q) to a hypothetical group isomorphism and used exercise 4 to compare finite-dimensional Q-vector-space dimensions."
---

::: {.exercise}
Assuming the dimension of a $\QQ$-vector space is well defined, use [[E-SMI-8000E-GA4]] to deduce that $\ZZ^s$ cannot be isomorphic to $\ZZ^t$ unless $s = t$.
:::


::: {.solution}
Suppose
$$
\phi:\mathbb Z^s\xrightarrow{\sim}\mathbb Z^t
$$
is an isomorphism of abelian groups.

<1>1. Precomposition with $\phi$ gives an isomorphism of $\mathbb Q$-vector spaces on Hom groups.
::: {.proof}
Define
$$
\phi^*:\operatorname{Hom}(\mathbb Z^t,\mathbb Q)
\longrightarrow
\operatorname{Hom}(\mathbb Z^s,\mathbb Q)
$$
by
$$
\phi^*(f)=f\circ\phi.
$$
This map is $\mathbb Q$-linear because addition and rational scalar
multiplication of homomorphisms are defined pointwise. Since $\phi$ is an
isomorphism, precomposition with $\phi^{-1}$ is the inverse of $\phi^*$.
Therefore
$$
\operatorname{Hom}(\mathbb Z^t,\mathbb Q)
\cong
\operatorname{Hom}(\mathbb Z^s,\mathbb Q)
$$
as $\mathbb Q$-vector spaces.
:::

<1>2. Exercise 4 identifies these Hom spaces with $\mathbb Q^t$ and $\mathbb Q^s$.
::: {.proof}
By [[E-SMI-8000E-GA4]],
$$
\operatorname{Hom}(\mathbb Z^r,\mathbb Q)\cong\mathbb Q^r
$$
for each finite $r$. Hence step <1>1 yields
$$
\mathbb Q^t\cong\mathbb Q^s
$$
as vector spaces over $\mathbb Q$.
:::

<1>3. Compare dimensions.
::: {.proof}
Dimension is invariant under vector-space isomorphism, so
$$
t=\dim_{\mathbb Q}\mathbb Q^t
=\dim_{\mathbb Q}\mathbb Q^s
=s.
$$
Thus
$$
\boxed{\mathbb Z^s\cong\mathbb Z^t\Longrightarrow s=t.}
$$
Therefore the rank of a finitely generated free abelian group is well defined.
:::
:::
