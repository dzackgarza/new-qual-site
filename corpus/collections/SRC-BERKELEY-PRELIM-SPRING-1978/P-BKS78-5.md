---
schema: qual/card@1
id: P-BKS78-5
kind: problem
title: Moduli $n$ for which $\mathbb Z_n[x]/(x^2+x+1)$ is a field
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $I=(x^2+x+1)\subset\mathbb Z_n[x]$.

1. For which $n$, $1\le n\le10$, is $\mathbb Z_n[x]/I$ a field?
2. Give the multiplication table for the resulting quotient when $n=2$.
:::

::: {.solution}
Put
$$
q(x)\coloneqq x^2+x+1.
$$

<1>1. If $\mathbb Z_n[x]/(q)$ is a field, then $n$ is prime.

::: {.proof}
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
\mathbb Z_n\longrightarrow \mathbb Z_n[x]/(q)
$$
is injective.

If the quotient is a field, its subring $\mathbb Z_n$ has no zero divisors. Thus $\mathbb Z_n$ is an integral domain, which for $n\geq2$ occurs exactly when $n$ is prime. For $n=1$ the quotient is the zero ring, not a field.
:::

<1>2. For a prime $p$, the quotient
$$
\mathbb F_p[x]/(q)
$$
is a field exactly when $q$ has no root in $\mathbb F_p$.

::: {.proof}
Over the field $\mathbb F_p$, the quotient by $(q)$ is a field exactly when $q$ is irreducible. Since $q$ has degree $2$, it is reducible exactly when it has a linear factor, equivalently a root in $\mathbb F_p$.
:::

<1>3. For $1\leq n\leq10$, the only possible values from step <1>1 are
$$
n=2,3,5,7.
$$

::: {.proof}
These are precisely the primes between $1$ and $10$.
:::

<1>4. The polynomial $q$ is irreducible over $\mathbb F_2$ and over $\mathbb F_5$.

::: {.proof}
Over $\mathbb F_2$,
$$
q(0)=1,
\qquad
q(1)=1+1+1=1,
$$
so $q$ has no root.

Over $\mathbb F_5$, direct evaluation gives
$$
\begin{array}{c|ccccc}
a&0&1&2&3&4\\
\hline
q(a)&1&3&2&3&1
\end{array}
$$
in $\mathbb F_5$, so again there is no root. Step <1>2 gives irreducibility in both cases.
:::

<1>5. The polynomial $q$ is reducible over $\mathbb F_3$ and over $\mathbb F_7$.

::: {.proof}
In $\mathbb F_3$,
$$
q(1)=1+1+1=0.
$$
In $\mathbb F_7$,
$$
q(2)=4+2+1=0.
$$
Thus $q$ has a root in each field and is reducible by step <1>2.
:::

<1>6. Therefore, for $1\leq n\leq10$,
$$
\boxed{
\mathbb Z_n[x]/(x^2+x+1)\text{ is a field exactly for }n=2,5.
}
$$

::: {.proof}
Steps <1>3--<1>5 exhaust the prime candidates, and step <1>1 rules out all composite values and $n=1$.
:::

<1>7. In the case $n=2$, let
$$
\alpha\coloneqq[x]\in\mathbb F_2[x]/(q).
$$
Then
$$
\alpha^2=\alpha+1.
$$

::: {.proof}
The defining relation is
$$
\alpha^2+\alpha+1=0.
$$
Since the characteristic is $2$, subtraction equals addition, so
$$
\alpha^2=\alpha+1.
$$
:::

<1>8. The four elements of the quotient for $n=2$ are
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

::: {.proof}
Every residue class has a unique representative of degree at most $1$, so the four listed classes are all elements. Step <1>7 gives
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

<1>9. Q.E.D.

::: {.proof}
Step <1>6 answers part 1, and step <1>8 answers part 2.
:::
:::
