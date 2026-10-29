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
$$
[F:K]\mid n!.
$$
In particular, $[F:K]\le n!$.
:::

::: {.solution}
We argue by strong induction on $n=\deg f$, for all base fields at once. If $n=1$, the splitting field is $K$.
Let $n\ge2$ and assume the claim for every polynomial of degree less than $n$ over every field.

::: pf

::: {.pf-step #irreducible-case}
If $f$ is irreducible, then $[F:K]\mid n!$.

::: pf-proof
Choose a root $\alpha\in F$. Then $[K(\alpha):K]=n$, and over $K(\alpha)$ one has $f=(x-\alpha)g$ with $\deg g=n-1$. The field $F$ is the splitting field of $g$ over $K(\alpha)$, so by induction $[F:K(\alpha)]\mid(n-1)!$. Hence
$$
[F:K]=[F:K(\alpha)]\,[K(\alpha):K]\mid(n-1)!\,n=n!.
$$
:::

:::

::: {.pf-step #reducible-case}
If $f=gh$ with $g,h\in K[x]$ of degrees $d$ and $n-d$, where $1\le d<n$, then $[F:K]\mid n!$.

::: pf-proof
Let $L$ be the splitting field of $g$ over $K$. By induction $[L:K]\mid d!$. Since $g$ splits over $L$, the field $F$ is the splitting field of $h$ over $L$, and induction over the base field $L$ gives $[F:L]\mid(n-d)!$. Hence $[F:K]=[F:L][L:K]$ divides $d!(n-d)!$, which divides $n!$ because $\frac{n!}{d!(n-d)!}=\binom nd\in\ZZ$.
:::

:::

::: pf-step
$\boxed{[F:K]\mid n!}$, and in particular $[F:K]\le n!$.

::: pf-proof
Every $f$ of degree $n\ge2$ is irreducible or a product as in step [](#reducible-case){.pf-ref}; step [](#irreducible-case){.pf-ref} covers the first case.
:::

:::

:::

:::
