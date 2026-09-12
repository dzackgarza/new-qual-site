---
schema: qual/card@1
id: P-HFGO25
kind: problem
title: 'Galois group of $x^8+1$'
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Determine the Galois group of $x^8+1$ over $\mathbb Q$.
:::

::: solution
The polynomial is the cyclotomic polynomial
\[
x^8+1=\Phi_{16}(x).
\]
Hence its splitting field is $\mathbb Q(\zeta_{16})$, where $\zeta_{16}$ is a
primitive sixteenth root of unity.

<1>1. Every automorphism of $\mathbb Q(\zeta_{16})/\mathbb Q$ is determined by
\[
\zeta_{16}\longmapsto \zeta_{16}^a
\]
for a unique $a\in(\mathbb Z/16\mathbb Z)^\times$.
::: proof
The conjugates of $\zeta_{16}$ over $\mathbb Q$ are precisely the primitive
sixteenth roots $\zeta_{16}^a$ with $\gcd(a,16)=1$. Conversely, each such choice
extends to a $\mathbb Q$-automorphism of the cyclotomic field.
:::

<1>2. Therefore
\[
\operatorname{Gal}(x^8+1/\mathbb Q)
\cong (\mathbb Z/16\mathbb Z)^\times.
\]
::: proof
Composition of automorphisms corresponds to multiplication of exponents modulo
$16$.
:::

<1>3. The unit group modulo $16$ is isomorphic to $C_2\times C_4$.
::: proof
It has order $\varphi(16)=8$. The element $-1$ has order $2$, while $3$ has
order $4$ modulo $16$ because
\[
3^2\equiv9\not\equiv1\pmod{16},
\qquad
3^4\equiv1\pmod{16}.
\]
Moreover $-1\notin\langle3\rangle=\{1,3,9,11\}$, so
\[
(\mathbb Z/16\mathbb Z)^\times
=\langle-1\rangle\times\langle3\rangle
\cong C_2\times C_4.
\]
:::
:::
