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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith Math 8000 packet 8000e.pdf page 1,
    abelian-groups (generators) problem 5: "Assuming the dimension of a Q vector
    space is well defined, use the result of 4, to deduce that Z^s cannot be
    isomorphic to Z^t unless s = t." The card states exactly this, and its
    reference is to the packet's own problem 4, which the neighbouring card
    proves. The proof was checked: precomposition with an isomorphism
    phi: Z^s → Z^t is a Q-linear isomorphism Hom(Z^t,Q) → Hom(Z^s,Q) with
    inverse precomposition by phi^{-1}; problem 4 identifies these with Q^t and
    Q^s; invariance of dimension gives t = s. Complete; no defect.
---

::: {.exercise}
Assuming the dimension of a $\QQ$-vector space is well defined, use [[E-SMI-8000E-GA4]] to deduce that $\ZZ^s$ cannot be isomorphic to $\ZZ^t$ unless $s = t$.
:::

::: {.solution}
Suppose
$$
\phi:\ZZ^s\xrightarrow{\sim}\ZZ^t
$$
is an isomorphism of abelian groups.

::: pf

::: {.pf-step #s1}

Precomposition with $\phi$ gives an isomorphism of $\QQ$-vector spaces on Hom groups.

::: pf-proof

Define
$$
\phi^*:\operatorname{Hom}(\ZZ^t,\QQ)
\longrightarrow
\operatorname{Hom}(\ZZ^s,\QQ)
$$
by
$$
\phi^*(f)=f\circ\phi.
$$
This map is $\QQ$-linear because addition and rational scalar
multiplication of homomorphisms are defined pointwise. Since $\phi$ is an
isomorphism, precomposition with $\phi^{-1}$ is the inverse of $\phi^*$.
Therefore
$$
\operatorname{Hom}(\ZZ^t,\QQ)
\cong
\operatorname{Hom}(\ZZ^s,\QQ)
$$
as $\QQ$-vector spaces.

:::

:::

::: pf-step

$\QQ^t\cong\QQ^s$ as $\QQ$-vector spaces.

::: pf-proof

By [[E-SMI-8000E-GA4]],
$$
\operatorname{Hom}(\ZZ^r,\QQ)\cong\QQ^r
$$
for each finite $r$. Hence step [](#s1){.pf-ref} yields
$$
\QQ^t\cong\QQ^s
$$
as vector spaces over $\QQ$.

:::

:::

::: pf-step

Compare dimensions.

::: pf-proof

Dimension is invariant under vector-space isomorphism, so
$$
t=\dim_{\QQ}\QQ^t
=\dim_{\QQ}\QQ^s
=s.
$$
Thus
$$
\boxed{\ZZ^s\cong\ZZ^t\Longrightarrow s=t.}
$$
Therefore the rank of a finitely generated free abelian group is well defined.

:::

:::

:::

:::
