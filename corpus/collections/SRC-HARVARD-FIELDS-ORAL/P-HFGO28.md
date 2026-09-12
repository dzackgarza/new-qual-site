---
schema: qual/card@1
id: P-HFGO28
kind: problem
title: Order of a finite Galois group
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
Let $F/k$ be a Galois extension of degree $n$.
Determine the order of $\operatorname{Gal}(F/k)$.
:::

::: solution
One has
\[
|\operatorname{Gal}(F/k)|=n.
\]

<1>1. A finite separable extension of degree $n$ has exactly $n$ distinct
$k$-embeddings into an algebraic closure of $k$.
::: proof
This is the standard embedding theorem for finite separable extensions. Since
$F/k$ is Galois, it is separable.
:::

<1>2. Every $k$-embedding $F\hookrightarrow\overline{k}$ has image equal to
$F$.
::: proof
Because $F/k$ is Galois, it is normal. Normality means that every irreducible
polynomial over $k$ having one root in $F$ splits completely in $F$; equivalently,
every $k$-embedding of $F$ into an algebraic closure maps $F$ onto itself.
:::

<1>3. Hence the $n$ embeddings in <1>1 are exactly the $k$-automorphisms of
$F$.
::: proof
By <1>2 each embedding is an automorphism of $F$ over $k$, and every element of
$\operatorname{Gal}(F/k)$ is such an embedding. Therefore
\[
|\operatorname{Gal}(F/k)|=[F:k]=n.
\]
:::
:::
