---
schema: qual/card@1
id: P-HCAO53
kind: problem
title: An ideal with two prescribed associated primes
classification:
  areas:
  - algebra
  topics:
  - Associated Primes
  - Primary Decomposition
  - Polynomial Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an ideal in $k[x,y,z]$ whose associated primes are $(x,y)$ and $(x,y,z)$.
:::

::: solution
Take
\[
I=(x^2,xy,y^2,xz,yz)=(x,y)^2+z(x,y).
\]
Equivalently,
\[
I=(x,y)\cap(x,y,z)^2.
\]

<1>1. The displayed intersection equals $I$.
::: proof
Both ideals are monomial. A monomial in $(x,y)\cap(x,y,z)^2$ has total degree
at least $2$ and is divisible by $x$ or $y$. The minimal such monomials are
\[
x^2,\ xy,\ y^2,\ xz,\ yz,
\]
which generate $I$.
:::

<1>2. The ideal $(x,y)$ is prime, while $(x,y,z)^2$ is
$(x,y,z)$-primary.
::: proof
The first quotient is $k[z]$, a domain. The second ideal is a power of the
maximal ideal $(x,y,z)$, hence is primary with that radical.
:::

<1>3. The decomposition is irredundant, so
\[
\operatorname{Ass}(k[x,y,z]/I)=\{(x,y),(x,y,z)\}.
\]
::: proof
Neither component contains the other: $z^2\in(x,y,z)^2$ but
$z^2\notin(x,y)$, while $x\in(x,y)$ but $x\notin(x,y,z)^2$. Thus this is a
minimal primary decomposition, and the associated primes are the radicals of
its primary components.
:::
:::
