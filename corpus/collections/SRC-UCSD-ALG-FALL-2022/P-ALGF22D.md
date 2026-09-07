---
schema: qual/card@1
id: P-ALGF22D
kind: problem
title: "Galois group of an irreducible cubic with exactly one real root is S_3"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2022 source; the irreducibility and one-real-root hypotheses agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified transitivity from irreducibility and used complex conjugation to exhibit a transposition, forcing the transitive subgroup of S3 to be all of S3.
---

::: problem
Let $K$ be the splitting field over $\mathbb{Q}$ of an irreducible polynomial $f(x) \in \mathbb{Q}[x]$ of degree 3. Suppose that $f$ has exactly one real root.
Prove that $\operatorname{Gal}(K/\mathbb{Q})$ is isomorphic to the symmetric group $S_3$.
:::

::: {.solution}
Let
\[
G=\operatorname{Gal}(K/\mathbb Q).
\]

<1>1. The group $G$ acts transitively on the three roots of $f$.
::: {.proof}
Because $f$ is irreducible over $\mathbb Q$ and $K$ is its splitting field, any two roots of $f$ are conjugate over $\mathbb Q$.
Equivalently, for any two roots $\alpha$ and $\beta$, there is a $\mathbb Q$-embedding
\[
\mathbb Q(\alpha)\hookrightarrow K
\]
sending $\alpha$ to $\beta$.
Since $K/\mathbb Q$ is normal, this embedding extends to an automorphism of $K$.
Thus $G$ acts transitively on the roots.
:::

<1>2. Via its action on the roots, $G$ embeds as a transitive subgroup of $S_3$.
::: {.proof}
An automorphism of the splitting field is determined by its action on the roots of $f$, since those roots generate $K$.
Hence the permutation representation
\[
G\longrightarrow S_3
\]
is injective.
By <1>1, its image is transitive.
:::

<1>3. Complex conjugation restricts to an element of $G$ acting as a transposition on the roots.
::: {.proof}
The coefficients of $f$ are rational, hence real.
Therefore complex conjugation preserves the set of roots and preserves the splitting field $K$.
It fixes $\mathbb Q$, so its restriction to $K$ lies in $G$.

By hypothesis, $f$ has exactly one real root.
The other two roots are nonreal and, because the coefficients are real, are complex conjugates of one another.
Thus complex conjugation fixes the unique real root and swaps the two nonreal roots.
Its permutation on the three roots is therefore a transposition.
:::

<1>4. One has
\[
G\cong S_3.
\]
::: {.proof}
The transitive subgroups of $S_3$ are $A_3\cong C_3$ and $S_3$ itself.
By <1>3, the image of $G$ contains a transposition, which does not lie in $A_3$.
Hence the image cannot be $A_3$.
Therefore it is all of $S_3$.
:::
:::
