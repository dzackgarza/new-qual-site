---
schema: qual/card@1
id: P-BERK84S-16
kind: problem
title: A real polynomial with a nonreal root
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 16 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the logarithmic-derivative contradiction under the assumption that all roots are real.
---

::: {.problem}
Let $p ( z )$ be a nonconstant polynomial with real coefficients such that for some real number $a , p ( a ) \neq 0$ but $p ^ { \prime } ( a ) = p ^ { \prime \prime } ( a ) = 0$ . Prove that the equation $p ( z ) = 0$ has a nonreal root.
:::


::: {.solution}
Suppose, for contradiction, that every root of $p$ is real. Since $p(a)\neq0$, none of those roots equals $a$.

<1>1. Factor $p$ over $\mathbb R$ as
\[
p(z)=c\prod_{j=1}^s (z-r_j)^{m_j},
\]
where the $r_j$ are distinct real numbers and $m_j\ge1$.
::: {.proof}
This is possible under the supposition that all roots of the nonconstant real polynomial $p$ are real. Because $p(a)\neq0$, one has $a-r_j\neq0$ for every $j$.
:::

<1>2. At every $z$ with $p(z)\neq0$,
\[
\frac{p'(z)}{p(z)}=\sum_{j=1}^s\frac{m_j}{z-r_j}.
\]
::: {.proof}
Differentiate the product in <1>1 and divide by $p(z)$. Equivalently, this is the logarithmic derivative of the factorization.
:::

<1>3. Differentiating the identity in <1>2 gives
\[
\frac{p''(z)}{p(z)}-\left(\frac{p'(z)}{p(z)}\right)^2
=-\sum_{j=1}^s\frac{m_j}{(z-r_j)^2}.
\]
::: {.proof}
The derivative of $p'/p$ is
\[
\left(\frac{p'}p\right)'=\frac{p''}{p}-\left(\frac{p'}p\right)^2,
\]
while termwise differentiation of the right-hand side of <1>2 gives the displayed negative sum.
:::

<1>4. Evaluating at $z=a$ contradicts the hypotheses.
::: {.proof}
Since $p'(a)=0$ and $p(a)\neq0$, <1>2 gives
\[
\sum_{j=1}^s\frac{m_j}{a-r_j}=0.
\]
Using $p'(a)=0$ in <1>3 yields
\[
\frac{p''(a)}{p(a)}
=-\sum_{j=1}^s\frac{m_j}{(a-r_j)^2}.
\]
Every summand on the right is strictly positive before the minus sign, because $m_j>0$ and $a\neq r_j$. Hence
\[
\frac{p''(a)}{p(a)}<0,
\]
so $p''(a)\neq0$. This contradicts the assumption $p''(a)=0$.
:::

Therefore not all roots of $p$ are real. Since every nonconstant polynomial has a complex root and the roots of a real polynomial occur in conjugate pairs, $p(z)=0$ has a nonreal root.
:::
