---
schema: qual/card@1
id: P-HFGO27
kind: problem
title: Finite fields of the same order are isomorphic
classification:
  areas: [algebra]
  topics: [Finite Fields]
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
Prove that any two finite fields of the same order are isomorphic.
:::

::: solution
Let $K$ and $L$ be finite fields with
\[
|K|=|L|=q.
\]
Then $q=p^n$ for the same prime $p$, and both fields contain the same prime
field $\mathbb F_p$ up to the unique isomorphism fixing $1$.

<1>1. Every element of a field with $q$ elements is a root of
\[
f(T)=T^q-T\in\mathbb F_p[T].
\]
::: proof
For $a=0$ this is immediate. If $a\ne0$, the multiplicative group of the field
has order $q-1$, so Lagrange's theorem gives $a^{q-1}=1$, hence $a^q=a$.
:::

<1>2. The polynomial $f(T)=T^q-T$ has exactly the $q$ elements of the field as
its roots.
::: proof
By <1>1 all $q$ elements are roots. Since $f$ has degree $q$, it has no further
roots in any extension once these $q$ distinct roots are present. Distinctness
also follows from
\[
f'(T)=qT^{q-1}-1=-1
\]
in characteristic $p$, so $f$ is separable.
:::

<1>3. Both $K$ and $L$ are splitting fields of $T^q-T$ over $\mathbb F_p$.
::: proof
By <1>2 the polynomial splits completely in each field and its roots generate
the whole field because its root set is the entire underlying set.
:::

<1>4. Therefore $K\cong L$.
::: proof
Splitting fields of a fixed polynomial over a fixed base field are unique up to
base-field isomorphism. Applying this to $T^q-T$ over $\mathbb F_p$ and using
<1>3 yields an $\mathbb F_p$-isomorphism $K\to L$.
:::
:::
