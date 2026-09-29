---
schema: qual/card@1
id: P-BKS15-8A
kind: problem
title: Factorization of $11x^5-11x^4+14x^2-21x+7$ over $\QQ$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the root x=1, the resulting quartic factor, and Eisenstein's criterion at 7.
---

::: {.problem}
Factor
$$
11x^5-11x^4+14x^2-21x+7
$$
into irreducible polynomials in $\QQ[x]$.
:::

::: {.solution}
Let
$$
f(x)
\coloneqq
11x^5-11x^4+14x^2-21x+7.
$$

::: pf

::: pf-step

The polynomial $x-1$ divides $f(x)$, and
$$
f(x)=(x-1)(11x^4+14x-7).
$$

::: pf-proof

One has
$$
f(1)
=
11-11+14-21+7
=
0,
$$
so the factor theorem gives the factor $x-1$. Direct multiplication gives
$$
\begin{aligned}
(x-1)(11x^4+14x-7)
&=
11x^5-11x^4+14x^2-21x+7\\
&=
f(x).
\end{aligned}
$$

:::

:::

::: {.pf-step #s2}

The quartic
$$
11x^4+14x-7
$$
is irreducible in $\QQ[x]$.

::: pf-proof

Apply Eisenstein's criterion with the prime $7$. The prime $7$ does not divide the leading coefficient $11$; it divides each remaining coefficient
$$
0,\qquad 0,\qquad 14,\qquad -7;
$$
and $7^2$ does not divide the constant coefficient $-7$. Hence the quartic is irreducible over $\QQ$.

:::

:::

::: {.pf-step #s3}

Therefore the factorization into irreducibles in $\QQ[x]$ is
$$
\boxed{
11x^5-11x^4+14x^2-21x+7
=
(x-1)(11x^4+14x-7)
}.
$$

::: pf-proof

The factor $x-1$ is irreducible because it has degree $1$, and step [](#s2){.pf-ref} proves that the quartic factor is irreducible.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the requested factorization.

:::

:::

:::
