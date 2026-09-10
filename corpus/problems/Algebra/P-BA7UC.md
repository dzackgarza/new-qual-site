---
schema: qual/card@1
id: P-BA7UC
kind: problem
title: Definition of a splitting field, and a finite extension of $\FF_q$ as a Galois
  splitting field
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
Let $F$ be a field and let $f(x) \in F[x]$.

1. State the definition of a splitting field of $f(x)$ over $F$.

2. Let $F$ be a finite field with $q$ elements.
   Let $E/F$ be a finite extension of degree $n>0$.
   Exhibit an explicit polynomial $g(x) \in F[x]$ such that $E/F$ is a splitting field of $g$ over $F$.
   Fully justify your answer.

3. Show that the extension in $(b)$ is a Galois extension.
:::


::: {.solution}
<1>1. A splitting field of $f\in F[x]$ is an extension $L/F$ such that $f$ splits into linear factors over $L$ and $L$ is generated over $F$ by the roots of $f$.
::: {.proof}
Equivalently, if $\alpha_1,\ldots,\alpha_r$ are all roots of $f$ in an algebraic closure, then a splitting field is
\[
F(\alpha_1,\ldots,\alpha_r).
\]
The minimality condition rules out adjoining unrelated elements.
:::

<1>2. If $|F|=q$ and $[E:F]=n$, then $|E|=q^n$ and every element of $E$ is a root of
\[
g(x)=x^{q^n}-x\in F[x].
\]
::: {.proof}
The field $E$ is an $n$-dimensional vector space over the $q$-element field $F$, so $|E|=q^n$. For $a\in E^\times$, Lagrange's theorem in the finite group $E^\times$ gives
\[
a^{q^n-1}=1,
\]
so $a^{q^n}=a$. The same equation is trivial for $a=0$.
:::

<1>3. The polynomial $g(x)=x^{q^n}-x$ has exactly the elements of $E$ as its roots, so $E$ is its splitting field over $F$.
::: {.proof}
Its derivative is
\[
g'(x)=q^n x^{q^n-1}-1=-1
\]
in characteristic $p$, where $q$ is a power of $p$. Thus $g$ has no repeated roots. It has degree $q^n$ and, by <1>2, already has $q^n$ distinct roots in $E$. Hence it splits completely over $E$ and has no other roots. Since the set of roots is all of $E$, the field generated over $F$ by the roots is exactly $E$.
:::

<1>4. The extension $E/F$ is Galois.
::: {.proof}
By <1>3, $E$ is the splitting field of $g$. The polynomial $g$ is separable because $g'=-1$. Therefore its splitting field over $F$ is normal and separable, hence Galois.
:::
:::
