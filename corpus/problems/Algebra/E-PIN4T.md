---
schema: qual/card@1
id: E-PIN4T
kind: problem
title: Degree of a splitting field of a degree-$n$ polynomial divides $n!$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Permutations
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced the incomplete inseparable argument by induction on degree, splitting one proper factor and then the complementary factor over its splitting field.
---

::: {.exercise}
Let $K$ be a field, let $f\in K[x]$ have degree $n\ge1$, and let $F$ be its splitting field. Prove that
\[
[F:K]\mid n!.
\]
In particular, $[F:K]\le n!$.
:::

::: {.solution}
We prove the divisibility by induction on $n=\deg f$.

If $n=1$, the splitting field is $K$.

Suppose first that $f$ is irreducible of degree $n$. Choose a root $\alpha\in F$. Then
\[
[K(\alpha):K]=n.
\]
Over $K(\alpha)$ we can write
\[
f=(x-\alpha)g,
\qquad \deg g=n-1,
\]
and $F$ is the splitting field of $g$ over $K(\alpha)$. By induction,
\[
[F:K(\alpha)]\mid (n-1)!.
\]
Hence
\[
[F:K]=[F:K(\alpha)]\,[K(\alpha):K]\mid (n-1)!\,n=n!.
\]

Now suppose $f$ is reducible. Write
\[
f=gh
\]
with $g,h\in K[x]$ nonconstant, say $\deg g=d$ and $\deg h=n-d$ with $1\le d<n$. Let $L$ be the splitting field of $g$ over $K$. By induction,
\[
[L:K]\mid d!.
\]
Since $g$ already splits over $L$, the splitting field $F$ of $f$ is exactly the splitting field of $h$ over $L$. Applying induction again, now over the base field $L$, gives
\[
[F:L]\mid (n-d)!.
\]
Therefore
\[
[F:K]=[F:L][L:K]\mid d!(n-d)!.
\]
Finally,
\[
\frac{n!}{d!(n-d)!}=\binom nd\in\mathbb Z,
\]
so $d!(n-d)!\mid n!$. Hence
\[
\boxed{[F:K]\mid n!}.
\]
In particular, $[F:K]\le n!$.
:::

