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

::: pf

::: pf-step

A splitting field of $f\in F[x]$ over $F$ is an extension $L/F$ in which $f$ factors into linear factors and which is generated over $F$ by all the roots of $f$ in $L$.


::: pf-proof

These are the defining properties of a splitting field.

:::

:::

::: pf-step

The polynomial
\[
\boxed{g(x)=x^{q^n}-x\in F[x]}
\]
has as its distinct roots exactly the elements of $E$.


::: pf-proof

As an $n$-dimensional vector space over the field of cardinality $q$, the field $E$ has $q^n$ elements. For each $a\in E^\times$, Lagrange's theorem applied to the finite group $E^\times$ of order $q^n-1$ gives $a^{q^n-1}=1$, hence $a^{q^n}=a$. The equality also holds for $a=0$. Therefore all $q^n$ elements of $E$ are roots of $g$. Since $g$ has degree $q^n$, these are all its roots, each of multiplicity one.

:::

:::

::: pf-step

The extension $E/F$ is a splitting field of $g$.


::: pf-proof

By step <1>2, the polynomial $g$ splits completely over $E$, and its roots comprise every element of $E$. Consequently the subfield of $E$ generated over $F$ by these roots is $E$ itself. Step <1>1 therefore identifies $E$ as a splitting field.

:::

:::

::: pf-step

The extension $E/F$ is Galois.


::: pf-proof

By step <1>2, the polynomial $g$ has no repeated root and is therefore separable. Step <1>3 exhibits $E$ as its splitting field, so $E/F$ is a finite normal and separable extension. Hence $E/F$ is Galois.

:::

:::

::: pf-qed

Step <1>1 answers part (a), steps <1>2 and <1>3 answer part (b), and step <1>4 answers part (c).

:::

:::
