---
schema: qual/card@1
id: P-R2UOL
kind: problem
title: $\overline{\FF}_2/\FF_2$ is infinite, and $[\FF_2(\alpha):\FF_2]=8$ when $\alpha^{17}=1$
  and $\alpha\neq 1$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
  - Roots of Unity
relations: []
review: draft
---

::: {.problem}
Let $F = \FF_2$ and let $\bar F$ denote its algebraic closure.

a. Show that $\bar F$ is not a finite extension of $F$.

b. Suppose that $\alpha \in \bar F$ satisfies $\alpha^{17} = 1$ and $\alpha\neq 1$.
Show that $F(\alpha)/F$ has degree 8.
:::

::: {.solution}
(a) Suppose for contradiction that $\bar F/F$ were finite. Then $\bar F$
would be a finite field, say with $q$ elements. Every $a\in\bar F$ satisfies
$a^q=a$, so for every $a\in\bar F$,
\[
a^q-a-1=-1\ne0.
\]
Thus the polynomial $x^q-x-1\in\bar F[x]$ would have no root in $\bar F$,
contradicting that $\bar F$ is algebraically closed. Hence
\[
[\bar F:F]=\infty.
\]

(b) Since $17$ is prime and $\alpha\ne1$, the element $\alpha$ has
multiplicative order exactly $17$. Put
\[
d=[F(\alpha):F].
\]
Then $F(\alpha)$ is the finite field with $2^d$ elements, so its
multiplicative group has order $2^d-1$. Therefore
\[
17\mid 2^d-1.
\]
Equivalently, $d$ is a positive multiple of the multiplicative order of $2$
modulo $17$. Now
\[
2^4=16\equiv-1\pmod{17},
\]
so $2^8\equiv1\pmod{17}$, while none of $2,2^2,2^4$ is congruent to $1$
modulo $17$. Hence
\[
\operatorname{ord}_{17}(2)=8,
\]
so $8\mid d$.

On the other hand, $17\mid 2^8-1$, so the finite field $\FF_{2^8}$ contains
an element of order $17$. Equivalently, every primitive $17$-th root of unity
over $\FF_2$ has degree dividing $8$. Thus $d\mid8$. Combining the two
divisibilities gives
\[
\boxed{[F(\alpha):F]=8}.
\]
:::
