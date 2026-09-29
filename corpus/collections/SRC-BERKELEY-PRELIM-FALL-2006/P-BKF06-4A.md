---
schema: qual/card@1
id: P-BKF06-4A
kind: problem
title: Finite integral domains are fields
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 4A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained multiplication-map argument. Since the
    problem already assumes a unital ring, the proof directly uses
    surjectivity to obtain an inverse for each nonzero element.
---

::: {.problem}
Let $R$ be a finite commutative ring without zero divisors and containing at least one element other than $0$.
As usual, rings are associative with $1$.
Prove that $R$ is a field.
:::

::: {.solution}

::: pf

::: {.pf-step #ma-injective}
For every nonzero $a\in R$, the map
$$
m_a:R\longrightarrow R,
\qquad
m_a(x)=ax,
$$
is injective.

::: pf-proof
Suppose
$$
m_a(x)=m_a(y).
$$
Then
$$
a(x-y)=0.
$$
Since $a\ne0$ and $R$ has no zero divisors, one must have
$x-y=0$. Thus $x=y$, so $m_a$ is injective.
:::

:::

::: {.pf-step #ab-equals-one}
For every nonzero $a\in R$, there exists $b\in R$ such that
$$
ab=1.
$$

::: pf-proof
The set $R$ is finite, so the injective self-map $m_a$ from step
[](#ma-injective){.pf-ref} is surjective. In particular, $1\in R$ lies in its image.
Hence there is $b\in R$ with
$$
m_a(b)=ab=1.
$$
:::

:::

::: {.pf-step #nonzero-invertible}
Every nonzero element of $R$ is invertible.

::: pf-proof
Let $a\in R$ be nonzero. Step [](#ab-equals-one){.pf-ref} gives $b\in R$ with $ab=1$.
Because $R$ is commutative,
$$
ba=ab=1.
$$
Thus $b$ is a two-sided inverse of $a$.
:::

:::

::: {.pf-step #R-is-field}
Therefore $R$ is a field.

::: pf-proof
The ring $R$ is commutative with identity by hypothesis, and step
[](#nonzero-invertible){.pf-ref} shows that every nonzero element has a multiplicative inverse.
This is precisely the definition of a field.
:::

:::

::: pf-qed
Step [](#R-is-field){.pf-ref} proves the required conclusion.
:::

:::

:::
