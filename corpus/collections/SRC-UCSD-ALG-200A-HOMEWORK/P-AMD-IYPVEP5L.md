---
schema: qual/card@1
id: P-AMD-IYPVEP5L
kind: problem
title: Hall subgroups under intersection with a normal subgroup and passage to the quotient
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Subgroups
  - Normal Subgroups
relations: []
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 2, Exercise 5. The source
    defines Hall subgroups by coprimality of subgroup order and index, then asks
    for preservation under intersection with a normal subgroup and passage to
    the quotient.
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Replaced two invalid steps in the prior draft. It treated HN/H as a quotient
    group although H need not be normal in HN, and it checked coprimality of
    |H|/|H cap N| rather than the order |H cap N| required for H cap N to be
    Hall in N. The corrected proof uses the index identity
    [HN:H]=[N:H cap N] and the valid isomorphism HN/N ~= H/(H cap N).
review: draft
---

::: {.problem}
Let $G$ be finite.
Recall that a subgroup $H\le G$ is a **Hall subgroup** if
\[
\gcd(|H|,[G:H])=1.
\]
Let $H$ be a Hall subgroup of $G$, and let $N\normal G$.

Show that $H\cap N$ is a Hall subgroup of $N$ and that $HN/N$ is a Hall subgroup of $G/N$.
:::

::: {.solution}
Set
\[
d=[G:H].
\]
Since $H$ is Hall in $G$,
\[
\gcd(|H|,d)=1.
\]

::: pf

::: {.pf-step #s1}

The index $[N:H\cap N]$ divides $d$.

::: pf-proof

Because $N\normal G$, the product $HN$ is a subgroup of $G$.
For finite subgroups,
\[
|HN|=\frac{|H||N|}{|H\cap N|}.
\]
Therefore
\[
[HN:H]
=\frac{|HN|}{|H|}
=\frac{|N|}{|H\cap N|}
=[N:H\cap N].
\]
The index tower $H\le HN\le G$ gives
\[
d=[G:H]=[G:HN][HN:H].
\]
Hence
\[
[N:H\cap N]=[HN:H]\mid d.
\]

:::

:::

::: pf-step

The subgroup $H\cap N$ is a Hall subgroup of $N$.

::: pf-proof

Since $H\cap N\le H$, Lagrange's theorem gives
\[
|H\cap N|\mid |H|.
\]
By step [](#s1){.pf-ref},
\[
[N:H\cap N]\mid d.
\]
Any common divisor of $|H\cap N|$ and $[N:H\cap N]$ therefore divides both $|H|$ and $d$.
Since $\gcd(|H|,d)=1$,
\[
\gcd(|H\cap N|,[N:H\cap N])=1.
\]
Thus $H\cap N$ is Hall in $N$.

:::

:::

::: {.pf-step #s3}

The order of $HN/N$ divides $|H|$.

::: pf-proof

The second isomorphism theorem gives the valid quotient isomorphism
\[
HN/N\cong H/(H\cap N).
\]
Hence
\[
|HN/N|=[H:H\cap N]=\frac{|H|}{|H\cap N|},
\]
which divides $|H|$.

:::

:::

::: {.pf-step #s4}

The index $[G/N:HN/N]$ divides $d$.

::: pf-proof

The correspondence of cosets under the quotient by $N$ gives
\[
[G/N:HN/N]=[G:HN].
\]
From the index tower used in step [](#s1){.pf-ref},
\[
d=[G:HN][HN:H],
\]
so $[G:HN]\mid d$.
Therefore
\[
[G/N:HN/N]\mid d.
\]

:::

:::

::: pf-step

The subgroup $HN/N$ is a Hall subgroup of $G/N$.

::: pf-proof

By step [](#s3){.pf-ref}, $|HN/N|$ divides $|H|$, and by step [](#s4){.pf-ref} its index in $G/N$ divides $d$.
Since $\gcd(|H|,d)=1$, these two divisors are coprime:
\[
\gcd\bigl(|HN/N|,[G/N:HN/N]\bigr)=1.
\]
Thus $HN/N$ is Hall in $G/N$.

:::

:::

:::

:::
