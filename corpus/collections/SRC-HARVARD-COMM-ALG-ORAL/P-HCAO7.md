---
schema: qual/card@1
id: P-HCAO7
kind: problem
title: Every finite integral domain is a field
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $R$ be a finite commutative ring with no zero divisors.

Show that $R$ has an identity and that every nonzero element of $R$ has an inverse.
Does the result remain true when $R$ is infinite?
:::

::: solution
Assume $R\ne0$.

<1>1. For every nonzero $a\in R$, multiplication by $a$ is a bijection
\[
m_a:R\to R,
\qquad
x\mapsto ax.
\]
::: proof
If $m_a(x)=m_a(y)$, then
\[
a(x-y)=0.
\]
Since $a\ne0$ and $R$ has no zero divisors, $x-y=0$, so $x=y$. Thus $m_a$ is
injective. Because $R$ is finite, every injective self-map of $R$ is surjective.
:::

<1>2. The ring $R$ has a multiplicative identity.
::: proof
Choose $0\ne a\in R$. By surjectivity of $m_a$, there is $e\in R$ such that
\[
ae=a.
\]
For any $x\in R$,
\[
a(ex-x)=aex-ax=(ae)x-ax=0.
\]
Since $a\ne0$ and there are no zero divisors, $ex=x$. Commutativity gives
$xe=x$ as well, so $e$ is an identity element.
:::

<1>3. Every nonzero element of $R$ is invertible.
::: proof
Let $0\ne x\in R$. By <1>1, multiplication by $x$ is surjective, so there is
$y\in R$ with
\[
xy=e.
\]
Thus $y=x^{-1}$.
:::

<1>4. The conclusion fails for infinite rings.
::: proof
The ring $\mathbb Z$ is infinite, commutative, has an identity, and has no zero
divisors, but for example $2$ is not invertible. Hence an infinite integral
domain need not be a field.
:::
:::
