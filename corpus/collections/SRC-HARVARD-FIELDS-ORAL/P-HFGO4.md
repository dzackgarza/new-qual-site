---
schema: qual/card@1
id: P-HFGO4
kind: problem
title: Bound the degree of a normal closure of a quartic extension
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
Let $E/F$ be a separable, nonnormal extension of degree $4$.
Let $K/F$ be its normal closure.
Bound $[K:F]$.
:::

::: solution
One has
\[
[K:F]\le 24.
\]
More precisely, because $E/F$ is not normal,
\[
[K:F]\in\{8,12,24\}.
\]

<1>1. The Galois group $G=\operatorname{Gal}(K/F)$ embeds as a transitive
subgroup of $S_4$.
::: proof
Because $E/F$ is finite separable of degree $4$, the primitive element theorem
gives $E=F(\alpha)$ for some $\alpha$ whose minimal polynomial over $F$ has four
distinct roots. The normal closure $K$ is the splitting field of this polynomial.

Every element of $G$ permutes the four roots, and the action is faithful because
the roots generate $K$. Thus
\[
G\hookrightarrow S_4.
\]
The action is transitive because the minimal polynomial of $\alpha$ is
irreducible over $F$.
:::

<1>2. Hence $[K:F]=|G|$ divides $24$ and is divisible by $4$.
::: proof
Since $K/F$ is Galois,
\[
[K:F]=|G|.
\]
By <1>1, $|G|$ divides $|S_4|=24$. Transitivity on four points implies by the
orbit-stabilizer theorem that $4$ divides $|G|$.
:::

<1>3. The value $[K:F]=4$ is impossible because $E/F$ is nonnormal.
::: proof
We have $E\subseteq K$ and $[E:F]=4$. If $[K:F]=4$, then $E=K$. But $K/F$ is
normal by construction, contradicting the hypothesis that $E/F$ is nonnormal.
:::

<1>4. Therefore
\[
[K:F]\in\{8,12,24\},
\]
and in particular $[K:F]\le24$.
::: proof
The positive divisors of $24$ that are multiples of $4$ are $4,8,12,24$;
exclude $4$ by <1>3.
:::
:::
