---
schema: qual/card@1
id: P-6HWPF
kind: problem
title: Solvability of polynomials by radicals
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Solvable Groups
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Can we solve general quadratic equations by radicals?
And what about cubics and so on?
Why can't you solve 5th degree equations by radicals?
:::

::: {.solution}
We work over a field of characteristic $0$, such as $\QQ$.

::: pf

::: pf-step

General quadratic equations are solvable by radicals.

::: pf-proof

For
\[
ax^2+bx+c=0,\qquad a\ne0,
\]
the roots are
\[
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
\]
Thus they are obtained from the coefficients using field operations and a square root.

:::

:::

::: pf-step

General cubic and quartic equations are also solvable by radicals.

::: pf-proof

Cardano's formula solves the general cubic by radicals, and Ferrari's method reduces the general quartic to a resolvent cubic and then to radicals. Equivalently from Galois theory, the generic Galois groups are $S_3$ and $S_4$, both solvable groups.

:::

:::

::: {.pf-step #s3}

A polynomial is solvable by radicals if and only if its Galois group is solvable.

::: pf-proof

This is Galois's criterion for solvability by radicals in characteristic $0$. A radical tower yields a Galois closure with a normal series having abelian cyclic factors, so its Galois group is solvable. Conversely, if the Galois group is solvable, adjoining the necessary roots of unity and using the cyclic factors in a solvable series realizes the splitting field inside a tower of radical extensions.

:::

:::

::: {.pf-step #s4}

The symmetric group $S_n$ is not solvable for $n\ge5$.

::: pf-proof

For $n\ge5$, the alternating group $A_n$ is a nonabelian simple normal subgroup of $S_n$. If $S_n$ were solvable, then its subgroup $A_n$ would be solvable. But a nontrivial simple solvable group must be cyclic of prime order: the last nontrivial term of its derived series would be a nontrivial proper normal subgroup unless the group were abelian, and a simple abelian group is cyclic of prime order. Since $A_n$ is nonabelian simple, it is not solvable. Hence neither is $S_n$.

:::

:::

::: pf-step

Therefore there is no formula by radicals for the general polynomial of degree $n\ge5$.

::: pf-proof

The general degree-$n$ polynomial has Galois group $S_n$. By step [](#s4){.pf-ref} this group is nonsolvable for $n\ge5$, and by step [](#s3){.pf-ref} a polynomial with nonsolvable Galois group cannot be solved by radicals. This is the Abel--Ruffini theorem.

:::

:::

::: pf-step

Some quintics are solvable by radicals.

::: pf-proof

The criterion in step [](#s3){.pf-ref} depends on the Galois group of the particular polynomial. For example,
\[
x^5-2=0
\]
has roots obtainable by adjoining a fifth root of $2$ and fifth roots of unity, so it is solvable by radicals. Abel--Ruffini says only that no radical formula works for the general quintic, and that there exist specific quintics with nonsolvable Galois group.

:::

:::

:::

:::
