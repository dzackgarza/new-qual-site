---
schema: qual/card@1
id: P-LARQ9
kind: problem
title: A commutative ring with no proper nonzero ideals is a field
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the no-proper-ideal hypothesis and field conclusion with Lerman practice problem 9."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked that every nonzero principal ideal is nonzero, hence all of R, yielding a multiplicative inverse for each nonzero element."
---

::: problem
Let $R$ be a nonzero commutative ring with identity.
Suppose its only ideals are $(0)$ and $R$.
Prove that $R$ is a field.
:::

::: solution
<1>1. Every nonzero element generates the unit ideal.
::: proof
Let $a\in R$ with $a\ne0$. The principal ideal $(a)$ contains $a$, so $(a)\ne(0)$. By hypothesis, the only ideals are $(0)$ and $R$. Therefore
$$
(a)=R.
$$
In particular $1\in(a)$.
:::

<1>2. Every nonzero element is invertible.
::: proof
Since $1\in(a)$, there exists $b\in R$ such that
$$
ba=1.
$$
Because $R$ is commutative, also $ab=1$. Thus every nonzero $a\in R$ has a multiplicative inverse. Since $R$ is nonzero and has an identity, this is exactly the definition of a field.
:::
:::
