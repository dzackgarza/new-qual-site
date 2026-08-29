---
schema: qual/card@1
id: P-AMD-IYPVEP5L
kind: problem
title: 'Given: $H\leq G, N \normal G, H \in \text{Hall}(G)$'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Subgroups
  - Normal Subgroups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Given: $H\leq G, N \normal G, H \in \text{Hall}(G)$

Show: $$H\cap N \in \text{Hall}(N) \text{ and } \frac{HN}{N} \in \text{Hall}\left(\frac{G}{N}\right)$$
:::

::: solution
Write $|G|=|H|\,[G\!:\!H]$, with $\gcd(|H|,[G\!:\!H])=1$.

First, by the Second Isomorphism Theorem,
\[
\frac{HN}{H}\cong \frac{N}{H\cap N}.
\]
So
\[
\left|\frac{HN}{H}\right|=\frac{|N|}{|H\cap N|}=[N:H\cap N].
\]

Now
\[
\gcd\!\left(\frac{|H|}{|H\cap N|},\,[N:H\cap N]\right)=1.
\]
Indeed, if a prime $p$ divided both, then $p\mid |H|$ and $p\mid [N:H\cap N]$
implies $p\mid [G:H]=[G:HN]\,[N:H\cap N]$, so $p$ divides both
$|H|$ and $[G:H]$, a contradiction.
Hence $H\cap N$ is a Hall subgroup of $N$.

For the quotient, by the Second Isomorphism Theorem again,
\[
\frac{HN}{N}\cong \frac{H}{H\cap N},\qquad |HN/N|=\frac{|H|}{|H\cap N|}.
\]
Also
\[
[G/N:HN/N]=[G:HN].
\]
From the same divisibility argument with $\gcd(|H|,[G:H])=1$ and
$[G:HN]\mid [G:H]$, we get
\[
\gcd(|HN/N|,[G/N:HN/N])=1,
\]
so $HN/N$ is Hall in $G/N$.
:::
