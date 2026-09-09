---
schema: qual/card@1
id: P-OVRL2
kind: problem
title: Finite integral domains are fields
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Fields
relations: []
review: draft
---

::: problem
Show that every finite integral domain is a field.
:::

::: {.solution}
Let $R$ be a finite integral domain and let $0\ne a\in R$. Consider multiplication by $a$,
\[
\mu_a:R\to R,\qquad x\mapsto ax.
\]
Because $R$ has no zero divisors, $\mu_a$ is injective. Since $R$ is finite, it is therefore surjective. Hence there exists $b\in R$ with
\[
ab=1.
\]
Thus every nonzero element is invertible, so $R$ is a field.
:::
