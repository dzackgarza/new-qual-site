---
schema: qual/card@1
id: P-TCB4X
kind: problem
title: Quadratic extensions in characteristic not $2$ are Galois
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that any quadratic extension of a field $F$ with $\ch(F)\neq 2$ is Galois.
:::

::: {.solution}
Let $K/F$ be quadratic and assume $\operatorname{char}F\ne2$. Choose $\alpha\in K\setminus F$. Then $K=F(\alpha)$ and the minimal polynomial of $\alpha$ has degree $2$:
\[
m(x)=x^2+bx+c.
\]
Set
\[
\beta=\alpha+\frac b2.
\]
Then $K=F(\beta)$ and
\[
\beta^2=\frac{b^2-4c}{4}=:d\in F.
\]
Since $\beta\notin F$, $d$ is not a square in $F$, and the minimal polynomial of $\beta$ is
\[
x^2-d.
\]
Its two roots are $\beta$ and $-\beta$, both of which lie in $K$. Thus $K$ is the splitting field of $x^2-d$ over $F$, so $K/F$ is normal.

Because $\operatorname{char}F\ne2$, the two roots $\beta$ and $-\beta$ are distinct; hence the polynomial is separable. Therefore $K/F$ is finite, normal, and separable, so it is Galois.
:::
