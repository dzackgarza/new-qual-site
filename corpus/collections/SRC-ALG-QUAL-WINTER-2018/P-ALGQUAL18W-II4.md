---
schema: qual/card@1
id: P-ALGQUAL18W-II4
kind: problem
title: A quotient by an ideal with maximal radical is finite-dimensional
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 4 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Independently proved finite-dimensionality by translating the maximal
    radical to a point ideal, choosing powers of each translated coordinate
    that lie in I, and bounding the quotient by the finitely many monomials
    below those exponents. The argument agrees with the worked source
    solution.
---

::: {.problem}
Let $I\triangleleft\mathbb C[x_1,\ldots,x_n]$ be an ideal such that $\sqrt I$ is maximal.
Prove that
\[
\mathbb C[x_1,\ldots,x_n]/I
\]
is finite-dimensional over $\mathbb C$.
:::

::: {.solution}
Put
$$
R=\CC[x_1,\ldots,x_n]
\qquad\text{and}\qquad
\mfm=\sqrt I.
$$

::: pf

::: {.pf-step #s1}

There are $c_1,\ldots,c_n\in\CC$ such that
$$
\mfm=(x_1-c_1,\ldots,x_n-c_n).
$$

::: pf-proof

The ideal $\mfm$ is maximal by hypothesis. Since the ground field $\CC$ is
algebraically closed, the weak Hilbert Nullstellensatz says that every
maximal ideal of $\CC[x_1,\ldots,x_n]$ is the ideal of a point of
$\CC^n$. Hence $\mfm$ has the displayed form.

:::

:::

::: {.pf-step #s2}

For each $i$ there is an integer $e_i\geq1$ such that
$$
(x_i-c_i)^{e_i}\in I.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
x_i-c_i\in\mfm=\sqrt I.
$$
By the definition of the radical, some positive power of $x_i-c_i$ lies in
$I$. Choose one such exponent and call it $e_i$.

:::

:::

::: {.pf-step #s3}

The monomials
$$
\prod_{i=1}^n (x_i-c_i)^{a_i},
\qquad
(a_1,\ldots,a_n)\in\ZZ_{\geq0}^n,
$$
form a $\CC$-basis of $R$.

::: pf-proof

The change of variables
$$
y_i=x_i-c_i
$$
defines a $\CC$-algebra automorphism of $R$. It carries the ordinary monomial
basis
$$
\prod_{i=1}^n x_i^{a_i}
$$
to the displayed family, so that family is again a basis.

:::

:::

::: {.pf-step #s4}

The residue classes of the monomials
$$
\prod_{i=1}^n (x_i-c_i)^{a_i},
\qquad
0\leq a_i<e_i
\quad\text{for every }i,
$$
span $R/I$ over $\CC$.

::: pf-proof

By step [](#s3){.pf-ref} every element of $R$ is a $\CC$-linear combination of translated
monomials. If one such monomial has
$$
a_i\geq e_i
$$
for some $i$, then it is divisible by
$$
(x_i-c_i)^{e_i}\in I
$$
by step [](#s2){.pf-ref}, so its class in $R/I$ is zero. Thus only the displayed
monomials are needed to span the quotient.

:::

:::

::: {.pf-step #s5}

The quotient is finite-dimensional, with
$$
\boxed{
\dim_{\CC}(R/I)
\leq
\prod_{i=1}^n e_i
<
\infty
}.
$$

::: pf-proof

There are exactly
$$
\prod_{i=1}^n e_i
$$
monomials in the spanning family from step [](#s4){.pf-ref}. Hence $R/I$ is spanned by
finitely many vectors and satisfies the displayed dimension bound.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required finite-dimensionality statement.

:::

:::

:::
