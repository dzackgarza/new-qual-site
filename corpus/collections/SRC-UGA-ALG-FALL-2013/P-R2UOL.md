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
<1>1. The algebraic closure $\bar F$ has infinite degree over $F$.

::: {.proof}
If $\bar F/F$ were finite, then $\bar F$ would be a finite field of cardinality $q$. Every element $a\in\bar F$ satisfies $a^q=a$. Consequently the polynomial $x^q-x-1$ has no root in $\bar F$, since its value at any $a$ is $-1\neq0$. This contradicts algebraic closedness.
:::

<1>2. The multiplicative order of $2$ in $(\mathbb Z/17\mathbb Z)^\times$ is $8$.

::: {.proof}
The congruence $2^4=16\equiv-1\pmod{17}$ gives $2^8\equiv1\pmod{17}$. The order divides eight but does not divide four, so it equals eight.
:::

<1>3. If $\alpha^{17}=1$ and $\alpha\neq1$, then
\[
\boxed{[F(\alpha):F]=8}.
\]

::: {.proof}
Since $17$ is prime, $\alpha$ has multiplicative order $17$. Write $d=[F(\alpha):F]$. The multiplicative group of $F(\alpha)$ has order $2^d-1$, so $17\mid2^d-1$ and step <1>2 implies $8\mid d$.

Conversely, $2^8\equiv1\pmod{17}$ implies that every root of $x^{17}-1$ belongs to the root set of $x^{2^8}-x$: any such root is nonzero and satisfies $\alpha^{2^8-1}=1$. This root set is the unique subfield $\mathbb F_{2^8}$ of $\bar F$. Hence $\alpha\in\mathbb F_{2^8}$, giving $d\mid8$. Thus $d=8$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1 and <1>3 establish parts (a) and (b), respectively.
:::
:::
