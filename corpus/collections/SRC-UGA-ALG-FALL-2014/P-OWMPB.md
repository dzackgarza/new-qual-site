---
schema: qual/card@1
id: P-OWMPB
kind: problem
title: A polynomial $g$ with $g(T)=0$ is irreducible iff $k(T)$ is invertible for
  every nonzero $k$ of lower degree
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Irreducibility Criteria
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Let $F$ be a field and $T$ an $n\times n$ matrix with entries in $F$.
Let $I$ be the ideal consisting of all polynomials $f\in F[x]$ such that $f(T) =0$.

Show that the following statements are equivalent about a polynomial $g\in I$:

a. $g$ is irreducible.

b. If $k\in F[x]$ is nonzero and of degree strictly less than $g$, then $k[T]$ is an invertible matrix.
:::

::: {.solution}
Let $m_T$ be the minimal polynomial of $T$. Since
\[
I=\{f\in F[x]:f(T)=0\}=(m_T),
\]
the polynomial $m_T$ divides every element of $I$.

Assume first that $g$ is irreducible. Since $g\in I$, we have $m_T\mid g$.
The minimal polynomial is nonconstant, so irreducibility of $g$ forces
$m_T$ to be an associate of $g$. Let $0\ne k\in F[x]$ with
$\deg k<\deg g$. Then $\gcd(k,g)=1$, hence there exist $a,b\in F[x]$ such
that
\[
a(x)k(x)+b(x)g(x)=1.
\]
Evaluating at $T$ and using $g(T)=0$ gives
\[
a(T)k(T)=I_n.
\]
Since polynomial expressions in $T$ commute, also $k(T)a(T)=I_n$. Thus
$k(T)$ is invertible.

Conversely, assume (b). If $g$ were reducible, write
\[
g=uv
\]
with $u,v$ nonconstant and $\deg u,\deg v<\deg g$. Condition (b) would make
both $u(T)$ and $v(T)$ invertible. But
\[
0=g(T)=u(T)v(T),
\]
which is impossible for a product of invertible matrices. Hence $g$ is
irreducible.

Therefore (a) and (b) are equivalent.
:::
