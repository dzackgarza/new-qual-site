---
schema: qual/card@1
id: P-HFGO11
kind: problem
title: Degree of the algebraic closure of the rationals
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Determine $[\overline{\mathbb Q}:\mathbb Q]$.
:::

::: {.solution}
<1>1. $[\overline{\QQ} : \QQ] = \infty$.
Proof: $\overline{\QQ}$ is an infinite extension of $\QQ$.

<1>2. Justification: for every $n \ge 1$, the polynomial $x^n - 2$ is irreducible over $\QQ$ (Eisenstein at $2$), so $\QQ(\sqrt[n]{2})$ has degree $n$ over $\QQ$.
Proof: Eisenstein's criterion.

<1>3. Hence $\overline{\QQ}$ contains subfields of arbitrarily large degree over $\QQ$.
Proof: $\QQ(\sqrt[n]{2}) \subseteq \overline{\QQ}$ for all $n$.

<1>4. Therefore $[\overline{\QQ} : \QQ]$ is infinite.
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
