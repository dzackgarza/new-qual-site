---
schema: qual/card@1
id: P-JRI2M
kind: problem
title: Definition of a splitting field; a finite extension of a finite field as a splitting field, and that the extension is Galois
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $F$ be a field and let $f(x)\in F[x]$.

1. Define a splitting field of $f(x)$ over $F$.
2. Let $F$ be a finite field with $q$ elements and let $E/F$ be a finite extension of degree $n>0$. Exhibit an explicit polynomial $g(x)\in F[x]$ whose splitting field over $F$ is $E$.
3. Show that $E/F$ is Galois.
:::

::: {.solution}
<1>1. A splitting field of $f$ over $F$ is a field extension $L/F$ such that $f$ splits into linear factors over $L$ and $L$ is generated over $F$ by the roots of $f$.

<1>2. Since $|F|=q$ and $[E:F]=n$, the field $E$ has $q^n$ elements. Take
\[
g(x)=x^{q^n}-x\in F[x].
\]
Then $E$ is the splitting field of $g$ over $F$.
::: {.proof}
Every $a\in E$ satisfies
\[
a^{q^n}=a,
\]
so every element of $E$ is a root of $g$. The derivative is
\[
g'(x)=q^n x^{q^n-1}-1=-1,
\]
so $g$ has no repeated roots. Since its degree is $q^n$ and $E$ already supplies $q^n$ distinct roots, its roots are exactly the elements of $E$. Therefore $g$ splits over $E$ and its roots generate $E$ over $F$.
:::

<1>3. The extension $E/F$ is Galois.
::: {.proof}
By <1>2, $E$ is the splitting field over $F$ of the separable polynomial $x^{q^n}-x$. A splitting field of a separable polynomial is normal and separable, hence Galois.

Equivalently,
\[
\Gal(E/F)=\langle x\mapsto x^q\rangle\cong C_n.
\]
:::
:::
