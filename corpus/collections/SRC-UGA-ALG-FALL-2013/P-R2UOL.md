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

::: pf

::: {.pf-step #s1-1}

The algebraic closure $\bar F$ has infinite degree over $F$.


::: pf-proof

If $\bar F/F$ were finite, then $\bar F$ would be a finite field of cardinality $q$. Every element $a\in\bar F$ satisfies $a^q=a$. Consequently the polynomial $x^q-x-1$ has no root in $\bar F$, since its value at any $a$ is $-1\neq0$. This contradicts algebraic closedness.

:::

:::

::: {.pf-step #s1-2}

The multiplicative order of $2$ in $(\ZZ/17\ZZ)^\times$ is $8$.


::: pf-proof

The congruence $2^4=16\equiv-1\pmod{17}$ gives $2^8\equiv1\pmod{17}$. The order divides eight but does not divide four, so it equals eight.

:::

:::

::: {.pf-step #s1-3}

If $\alpha^{17}=1$ and $\alpha\neq1$, then
$$
\boxed{[F(\alpha):F]=8}.
$$


::: pf-proof

Since $17$ is prime, $\alpha$ has multiplicative order $17$. Write $d=[F(\alpha):F]$. The multiplicative group of $F(\alpha)$ has order $2^d-1$, so $17\mid2^d-1$ and step [](#s1-2){.pf-ref} implies $8\mid d$.

Conversely, $2^8\equiv1\pmod{17}$ implies that every root of $x^{17}-1$ belongs to the root set of $x^{2^8}-x$: any such root is nonzero and satisfies $\alpha^{2^8-1}=1$. This root set is the unique subfield $\FF_{2^8}$ of $\bar F$. Hence $\alpha\in\FF_{2^8}$, giving $d\mid8$. Thus $d=8$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
