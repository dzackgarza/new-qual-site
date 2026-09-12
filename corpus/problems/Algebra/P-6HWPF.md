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

::: problem
Can we solve general quadratic equations by radicals?
And what about cubics and so on?
Why can't you solve 5th degree equations by radicals?
:::


::: {.solution}
We work over a field of characteristic $0$, such as $\QQ$.

<1>1. General quadratic equations are solvable by radicals.
::: {.proof}
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

<1>2. General cubic and quartic equations are also solvable by radicals.
::: {.proof}
Cardano's formula solves the general cubic by radicals, and Ferrari's method reduces the general quartic to a resolvent cubic and then to radicals. Equivalently from Galois theory, the generic Galois groups are $S_3$ and $S_4$, both solvable groups.
:::

<1>3. A polynomial is solvable by radicals if and only if its Galois group is solvable.
::: {.proof}
This is the fundamental Galois-theoretic criterion for solvability by radicals in characteristic $0$. A radical tower yields a Galois closure with a normal series having abelian cyclic factors, so its Galois group is solvable. Conversely, if the Galois group is solvable, adjoining the necessary roots of unity and using the cyclic factors in a solvable series realizes the splitting field inside a tower of radical extensions.
:::

<1>4. The symmetric group $S_n$ is not solvable for $n\ge5$.
::: {.proof}
For $n\ge5$, the alternating group $A_n$ is a nonabelian simple normal subgroup of $S_n$. If $S_n$ were solvable, then its subgroup $A_n$ would be solvable. But a nontrivial simple solvable group must be cyclic of prime order: the last nontrivial term of its derived series would be a nontrivial proper normal subgroup unless the group were abelian, and a simple abelian group is cyclic of prime order. Since $A_n$ is nonabelian simple, it is not solvable. Hence neither is $S_n$.
:::

<1>5. Therefore there is no formula by radicals for the general polynomial of degree $n\ge5$.
::: {.proof}
The general degree-$n$ polynomial has Galois group $S_n$. By <1>4 this group is nonsolvable for $n\ge5$, and by <1>3 a polynomial with nonsolvable Galois group cannot be solved by radicals. This is the Abel--Ruffini theorem.
:::

<1>6. This does not mean that every quintic is unsolvable by radicals.
::: {.proof}
The criterion in <1>3 depends on the Galois group of the particular polynomial. For example,
\[
x^5-2=0
\]
has roots obtainable by adjoining a fifth root of $2$ and fifth roots of unity, so it is solvable by radicals. Abel--Ruffini says only that no radical formula works for the general quintic, and that there exist specific quintics with nonsolvable Galois group.
:::
:::
