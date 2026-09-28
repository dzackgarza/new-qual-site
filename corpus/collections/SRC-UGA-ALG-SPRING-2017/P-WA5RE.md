---
schema: qual/card@1
id: P-WA5RE
kind: problem
title: Splitting fields, and finite extensions of finite fields as Galois splitting
  fields
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Finite Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $F$ be a field and let $f(x) \in F[x]$.

a. Define what a splitting field of $f(x)$ over $F$ is.

b. Let $F$ now be a finite field with $q$ elements.
Let $E/F$ be a finite extension of degree $n>0$.
Exhibit an explicit polynomial $g(x) \in F[x]$ such that $E/F$ is a splitting field of $g(x)$ over $F$.
Fully justify your answer.

c. Show that the extension $E/F$ in (b) is a Galois extension.
:::

::: {.solution}
A splitting field of $f\in F[x]$ is an extension $L/F$ in which $f$ factors completely into linear factors and which is generated over $F$ by the roots of $f$.

Now let $|F|=q$ and $[E:F]=n$. Then $E$ has $q^n$ elements. Every $a\in E$ satisfies $a^{q^n}=a$, so every element of $E$ is a root of
\[
g(x)=x^{q^n}-x\in F[x].
\]
Conversely this polynomial has degree $q^n$ and already has the $q^n$ distinct elements of $E$ as roots. They are distinct because
\[
g'(x)=q^n x^{q^n-1}-1=-1
\]
in characteristic $p$, where $q$ is a power of $p$. Hence $E$ is exactly the splitting field of $g$ over $F$.

The polynomial $g$ is separable by the derivative computation. A splitting field of a separable polynomial is normal and separable, hence Galois. Therefore $E/F$ is Galois.
:::
