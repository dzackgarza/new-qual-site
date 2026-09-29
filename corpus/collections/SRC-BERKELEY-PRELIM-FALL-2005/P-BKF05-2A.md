---
schema: qual/card@1
id: P-BKF05-2A
kind: problem
title: Partial fractions for proper complex rational functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained dimension-count argument; injectivity
    is proved by isolating the highest principal-part coefficient at each
    pole after multiplication by the corresponding pole power.
---

::: {.problem}
Let
\[
f(z)=\frac{P(z)}{Q(z)}
\]
be a rational function with complex coefficients and \(\deg P<\deg Q\). Prove that \(f\) is a sum of terms of the form
\[
\frac{a}{(z-b)^k},\qquad a,b\in\mathbb C.
\]
:::

::: {.solution}

If $P=0$, the assertion is immediate from the empty sum, so assume
$P\ne0$. Multiplying numerator and denominator by the same nonzero
constant if necessary, assume that $Q$ is monic. Factor
$$
Q(z)=\prod_{i=1}^r(z-b_i)^{n_i},
$$
where the $b_i$ are distinct and
$$
N\coloneqq\deg Q=\sum_{i=1}^r n_i.
$$

::: pf

::: {.pf-step #Ra-definition}
Let
$$
V=
\left\{
(a_{ij})_{\substack{1\le i\le r\\1\le j\le n_i}}
:a_{ij}\in\CC
\right\}.
$$
For $a=(a_{ij})\in V$, there is a unique polynomial
$R_a\in\CC[z]$ of degree less than $N$ such that
$$
\sum_{i=1}^r\sum_{j=1}^{n_i}
\frac{a_{ij}}{(z-b_i)^j}
=
\frac{R_a(z)}{Q(z)}.
$$

::: pf-proof
Putting the left-hand side over the common denominator $Q$ gives
$$
R_a(z)=
\sum_{i=1}^r\sum_{j=1}^{n_i}
a_{ij}\frac{Q(z)}{(z-b_i)^j}.
$$
Each quotient $Q(z)/(z-b_i)^j$ is a polynomial of degree
$N-j\le N-1$, so $\deg R_a<N$. The numerator with denominator $Q$ is
unique because $Q$ is a nonzero polynomial.
:::

:::

::: {.pf-step #phi-injective}
The linear map
$$
\Phi:V\longrightarrow
\{R\in\CC[z]:\deg R<N\},
\qquad
a\longmapsto R_a,
$$
is injective.

::: pf-proof
Suppose $\Phi(a)=0$. Then, as a rational function,
$$
\sum_{i=1}^r\sum_{j=1}^{n_i}
\frac{a_{ij}}{(z-b_i)^j}=0.
$$
Fix $i$. If some coefficient $a_{ij}$ is nonzero, let $p$ be the
largest $j$ for which $a_{ij}\ne0$. Multiply the displayed identity by
$(z-b_i)^p$ and let $z\to b_i$.

For the terms with index $i$ and $j<p$, the factor
$(z-b_i)^{p-j}$ tends to zero. The term with $j=p$ tends to
$a_{ip}$. For every term whose first index is different from $i$, its
denominator stays nonzero at $b_i$, while $(z-b_i)^p\to0$. Therefore
the limit of the left-hand side is $a_{ip}$, whereas the right-hand
side has limit zero. This contradicts $a_{ip}\ne0$.

Hence every coefficient with first index $i$ is zero. Since $i$ was
arbitrary, all $a_{ij}$ vanish, so $\ker\Phi=0$.
:::

:::

::: {.pf-step #phi-surjective}
The map $\Phi$ is surjective.

::: pf-proof
The domain has dimension
$$
\dim_{\CC}V
=
\sum_{i=1}^r n_i
=
N.
$$
The codomain, with basis $1,z,\ldots,z^{N-1}$, also has dimension
$N$. By step [](#phi-injective){.pf-ref}, $\Phi$ is an injective linear map between
finite-dimensional vector spaces of the same dimension. Therefore it
is surjective.
:::

:::

::: {.pf-step #partial-fraction-coefficients}
There are coefficients $a_{ij}\in\CC$ such that
$$
\frac{P(z)}{Q(z)}
=
\sum_{i=1}^r\sum_{j=1}^{n_i}
\frac{a_{ij}}{(z-b_i)^j}.
$$

::: pf-proof
The hypothesis $\deg P<\deg Q=N$ places $P$ in the codomain of
$\Phi$. By step [](#phi-surjective){.pf-ref}, choose $a\in V$ with $\Phi(a)=P$. The defining
identity from step [](#Ra-definition){.pf-ref} then gives exactly the displayed partial
fraction expansion.
:::

:::

::: {.pf-step #f-sum-of-terms}
Thus $f$ is a sum of terms
$$
\boxed{\frac{a}{(z-b)^k}},
\qquad
a,b\in\CC.
$$

::: pf-proof
Every summand in step [](#partial-fraction-coefficients){.pf-ref} has the required form, with
$b=b_i$ and $k=j$.
:::

:::

::: pf-qed
Step [](#f-sum-of-terms){.pf-ref} is the asserted decomposition.
:::

:::

:::
