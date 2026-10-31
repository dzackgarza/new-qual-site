---
schema: qual/card@1
id: P-UWALG05-6
kind: problem
title: Characteristic polynomials of $f(A)$ when $A^p=I$ in characteristic $p$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $F$ be a finite field of characteristic $p$.
Let $A$ be an $n\times n$ matrix over $F$.
Suppose that $A^p$ is the identity matrix.
Show that for every polynomial $f(x)$, the characteristic polynomial of the matrix $f(A)$ is equal to $(t-c)^n$ for some $c$.
:::

::: {.solution}
Everything happens in the finite field $F$ of characteristic $p$; the finiteness is not used beyond that.

::: pf

::: {.pf-step #unipotent}
$A=I+N$ for a nilpotent matrix $N$ with $N^p=0$.

::: pf-proof
Put $N=A-I$. In characteristic $p$ the binomial coefficients $\binom pk$ vanish for $0<k<p$, so the binomial theorem applies to commuting matrices without the middle terms and
$$
N^p=(A-I)^p=A^p-I^p=0,
$$
because $A^p=I$ by hypothesis and $I^p=I$.
:::

:::

::: {.pf-step #f-of-unipotent}
For every $f\in F[x]$ there is $c\in F$ with $f(A)=cI+(\text{a nilpotent matrix})$.

::: pf-proof
Taylor expansion of $f$ about $1$ in the ring $F[x]$ gives $f(x)=f(1)+(x-1)g(x)$ for a polynomial $g$.
Substituting $A$ gives $f(A)=f(1)I+g(A)(A-I)=f(1)I+g(A)N$.
The matrix $g(A)N$ is nilpotent, since it commutes with $N$ and $N^p=0$ implies $(g(A)N)^p=g(A)^pN^p=0$.
:::

:::

::: {.pf-step #characteristic-polynomial}
For every $f\in F[x]$ the characteristic polynomial of $f(A)$ is $(t-c)^n$ with $c=f(1)$.

::: pf-proof
By step [](#f-of-unipotent){.pf-ref} we have $f(A)=cI+M$ with $c=f(1)$ and $M$ nilpotent.
Then
$$
\det\bigl(tI-f(A)\bigr)=\det\bigl((t-c)I-M\bigr)=(t-c)^n,
$$
because a nilpotent matrix $M$ has characteristic polynomial $t^n$: over the algebraic closure of $F$ it is similar to a strictly upper triangular matrix, whose diagonal entries are all zero.
:::

:::

:::

:::
