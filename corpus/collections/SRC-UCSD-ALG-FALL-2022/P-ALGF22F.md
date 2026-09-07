---
schema: qual/card@1
id: P-ALGF22F
kind: problem
title: "Coefficients of monic polynomials with product in the integral closure must lie in it"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 6 of the official UCSD Algebra Qualifying Exam, Fall 2022 source; the integral-closure hypotheses and conclusion agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Replaced placeholder justifications with the complete argument using roots of the monic product, transitivity of integrality, and closure of integral elements under elementary symmetric polynomials.
---

::: problem
Let $A$ be a subring of an integral domain $B$ and let $C$ be the integral closure of $A$ inside $B$.
Let $f$ and $g$ be monic polynomials with coefficients in $B$ such that all of the coefficients of $fg$ lie in $C$.
Prove that the coefficients of $f$ and $g$ belong to $C$.
:::

::: {.solution}
Let $L=\operatorname{Frac}(B)$, and fix an algebraic closure $\overline L$.

<1>1. Over $\overline L$, write
\[
f(x)=\prod_{i=1}^m(x-\alpha_i),
\qquad
g(x)=\prod_{j=1}^n(x-\beta_j).
\]
::: {.proof}
The ring $B$ is an integral domain, so it embeds in its fraction field $L$.
Both $f$ and $g$ may therefore be viewed as monic polynomials in $L[x]$, and they split into linear factors over $\overline L$.
:::

<1>2. Every root of $fg$ in $\overline L$ is integral over $A$.
::: {.proof}
By hypothesis,
\[
fg\in C[x],
\]
and $fg$ is monic because $f$ and $g$ are monic.
Thus any root $\gamma$ of $fg$ satisfies a monic polynomial with coefficients in $C$, namely $fg$ itself.
Hence $\gamma$ is integral over $C$.

By definition of the integral closure, every element of $C$ is integral over $A$.
Thus $C/A$ is an integral extension.
Integrality is transitive, so every element integral over $C$ is integral over $A$.
Therefore every root of $fg$ is integral over $A$.
:::

<1>3. Every $\alpha_i$ and every $\beta_j$ is integral over $A$.
::: {.proof}
By <1>1, each $\alpha_i$ and each $\beta_j$ is a root of
\[
fg=f\,g.
\]
The assertion therefore follows from <1>2.
:::

<1>4. Every coefficient of $f$ and every coefficient of $g$ is integral over $A$.
::: {.proof}
The elements of $\overline L$ integral over $A$ form a subring.
By <1>3, all the roots $\alpha_i$ are integral over $A$.
The coefficients of the monic polynomial
\[
f(x)=\prod_{i=1}^m(x-\alpha_i)
\]
are, up to sign, elementary symmetric polynomials in the $\alpha_i$.
They are therefore sums of products of elements integral over $A$, hence are themselves integral over $A$.

The same argument applied to the roots $\beta_j$ shows that every coefficient of $g$ is integral over $A$.
:::

<1>5. All coefficients of $f$ and $g$ belong to $C$.
::: {.proof}
By hypothesis, the coefficients of $f$ and $g$ lie in $B$.
By <1>4, they are integral over $A$.
But
\[
C=\{b\in B:b\text{ is integral over }A\}.
\]
Hence every coefficient of $f$ and $g$ lies in $C$, as required.
:::
:::
