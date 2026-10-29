---
schema: qual/card@1
id: P-BKS78-5
kind: problem
title: Moduli $n$ for which $\ZZ_n[x]/(x^2+x+1)$ is a field
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $I=(x^2+x+1)\subset\ZZ_n[x]$.

1. For which $n$, $1\le n\le10$, is $\ZZ_n[x]/I$ a field?
2. Give the multiplication table for the resulting quotient when $n=2$.
:::

::: {.solution}
Put
$$
q(x)\coloneqq x^2+x+1.
$$

::: pf

::: {.pf-step #prime-necessary}
If $\ZZ_n[x]/(q)$ is a field, then $n$ is prime.

::: pf-proof
Because $q$ is monic of degree $2$, no nonzero constant polynomial belongs to the ideal $(q)$. Indeed, if
$$
c=q(x)h(x)
$$
with $h\neq0$, then the leading coefficient of $qh$ equals the leading coefficient of $h$, so
$$
\deg(qh)=\deg h+2\geq2,
$$
contrary to $c$ being constant. Hence the natural map
$$
\ZZ_n\longrightarrow \ZZ_n[x]/(q)
$$
is injective.

If the quotient is a field, its subring $\ZZ_n$ has no zero divisors. Thus $\ZZ_n$ is an integral domain, which for $n\geq2$ occurs exactly when $n$ is prime. For $n=1$ the quotient is the zero ring, not a field.
:::

:::

::: {.pf-step #quadratic-criterion}
For a prime $p$, the quotient
$$
\FF_p[x]/(q)
$$
is a field exactly when $q$ has no root in $\FF_p$.

::: pf-proof
Over the field $\FF_p$, the quotient by $(q)$ is a field exactly when $q$ is irreducible. Since $q$ has degree $2$, it is reducible exactly when it has a linear factor, equivalently a root in $\FF_p$.
:::

:::

::: {.pf-step #prime-candidates}
For $1\leq n\leq10$, the only possible values from [](#prime-necessary){.pf-ref} are
$$
n=2,3,5,7.
$$

::: pf-proof
These are precisely the primes between $1$ and $10$.
:::

:::

::: {.pf-step #irreducible-cases}
The polynomial $q$ is irreducible over $\FF_2$ and over $\FF_5$.

::: pf-proof
Over $\FF_2$,
$$
q(0)=1,
\qquad
q(1)=1+1+1=1,
$$
so $q$ has no root.

Over $\FF_5$, direct evaluation gives
$$
\begin{array}{c|ccccc}
a&0&1&2&3&4\\
\hline
q(a)&1&3&2&3&1
\end{array}
$$
in $\FF_5$, so again there is no root. [](#quadratic-criterion){.pf-ref} gives irreducibility in both cases.
:::

:::

::: {.pf-step #reducible-cases}
The polynomial $q$ is reducible over $\FF_3$ and over $\FF_7$.

::: pf-proof
In $\FF_3$,
$$
q(1)=1+1+1=0.
$$
In $\FF_7$,
$$
q(2)=4+2+1=0.
$$
Thus $q$ has a root in each field and is reducible by [](#quadratic-criterion){.pf-ref}.
:::

:::

::: pf-step
Therefore, for $1\leq n\leq10$,
$$
\boxed{
\ZZ_n[x]/(x^2+x+1)\text{ is a field exactly for }n=2,5.
}
$$

::: pf-proof
[](#prime-candidates){.pf-ref}, [](#irreducible-cases){.pf-ref}, and [](#reducible-cases){.pf-ref} exhaust the prime candidates, and [](#prime-necessary){.pf-ref} rules out all composite values and $n=1$.
:::

:::

::: {.pf-step #defining-relation}
In the case $n=2$, let
$$
\alpha\coloneqq[x]\in\FF_2[x]/(q).
$$
Then
$$
\alpha^2=\alpha+1.
$$

::: pf-proof
The defining relation is
$$
\alpha^2+\alpha+1=0.
$$
Since the characteristic is $2$, subtraction equals addition, so
$$
\alpha^2=\alpha+1.
$$
:::

:::

::: pf-step
The four elements of the quotient for $n=2$ are
$$
0,\quad1,\quad\alpha,\quad\alpha+1,
$$
and their multiplication table is
$$
\boxed{
\begin{array}{c|cccc}
\cdot&0&1&\alpha&\alpha+1\\
\hline
0&0&0&0&0\\
1&0&1&\alpha&\alpha+1\\
\alpha&0&\alpha&\alpha+1&1\\
\alpha+1&0&\alpha+1&1&\alpha
\end{array}
}.
$$

::: pf-proof
Every residue class has a unique representative of degree at most $1$, so the four listed classes are all elements. [](#defining-relation){.pf-ref} gives
$$
\alpha^2=\alpha+1.
$$
Also
$$
\alpha(\alpha+1)
=
\alpha^2+\alpha
=1,
$$
and
$$
(\alpha+1)^2
=
\alpha^2+2\alpha+1
=
(\alpha+1)+1
=\alpha.
$$
Together with multiplication by $0$ and $1$, these identities give the table.
:::

:::

:::

:::
