---
schema: qual/card@1
id: P-HFGO15
kind: problem
title: Root bounds over division rings
classification:
  areas: [algebra]
  topics: [Ring Theory]
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
Must a polynomial of degree $n$ over a division ring have at most $n$ roots in every extending division ring?
Prove the claim or give a counterexample.
:::

::: solution
No. The quaternion division ring gives a degree-$2$ polynomial with infinitely
many roots.

Let
\[
\mathbb H=\{a+bi+cj+dk:a,b,c,d\in\mathbb R\}
\]
be the Hamilton quaternions, with
\[
i^2=j^2=k^2=ijk=-1.
\]
Consider
\[
f(x)=x^2+1\in\mathbb R[x]\subseteq\mathbb H[x].
\]

<1>1. Every unit purely imaginary quaternion is a root of $f$.
::: proof
Let
\[
q=bi+cj+dk
\]
with
\[
b^2+c^2+d^2=1.
\]
Using $ij=-ji$, $jk=-kj$, and $ki=-ik$, the mixed terms cancel in $q^2$:
\[
q^2
=b^2i^2+c^2j^2+d^2k^2
=-(b^2+c^2+d^2)
=-1.
\]
Hence
\[
f(q)=q^2+1=0.
\]
:::

<1>2. The polynomial $f$ has infinitely many roots in the division ring
$\mathbb H$.
::: proof
The triples $(b,c,d)$ with $b^2+c^2+d^2=1$ form the unit sphere in
$\mathbb R^3$, so <1>1 supplies infinitely many distinct roots.
:::

Thus the usual degree bound for roots over fields fails for polynomials over
division rings.
:::
