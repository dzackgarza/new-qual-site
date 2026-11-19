---
schema: qual/card@1
id: P-DE22H
kind: problem
title: Elementary divisors and invariant factors of a given $\QQ[x]$-module
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Canonical Forms
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    The collection's provenance is the examination paper alone,
    assets/attachments/Algebra_Spring_2016.docx, so no retained solution set covers the problem and the
    argument is the card's own. Checked the statement against the paper's wording as the card records
    it, and re-checked both answers by hand: the elementary divisors are the six primary factors
    x-1, (x-1)^3, x+2, (x^2+1)^2, (x^2+1)^3, (x^2+1)^5, and right-aligning the exponents of x^2+1
    (2,3,5), x-1 (1,3) and x+2 (1) gives the three invariant factors (x^2+1)^2,
    (x-1)(x^2+1)^3 and (x-1)^3(x+2)(x^2+1)^5, whose product a^4 b q^10 equals the product of the four
    annihilators. Both parts as printed are answered.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the prose solution into a Lamport proof. The prose asserted the Chinese remainder
    splitting and the alignment rule; the card now proves the coprimality that licenses the splitting
    (the three irreducibles are distinct), states the alignment as an explicit exponent table with one
    column per irreducible, and closes by verifying both conditions of the invariant-factor form:
    d1 | d2 | d3 and d1 d2 d3 equal to the product of the original annihilators. The two answers are
    unchanged.
---

::: {.problem}
Let $D = \QQ[x]$ and let $M$ be a $\QQ[x]\dash$module such that
$$
M \cong \frac{\QQ[x]}{(x-1)^{3}} \oplus \frac{\QQ[x]}{\left(x^{2}+1\right)^{3}} \oplus \frac{\QQ[x]}{(x-1)\left(x^{2}+1\right)^{5}} \oplus \frac{\QQ[x]}{(x+2)\left(x^{2}+1\right)^{2}}
.$$

Determine the elementary divisors and invariant factors of $M$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers the problem; the argument is the card's own. Write $D=\QQ[x]$, $a=x-1$, $b=x+2$ and $q=x^{2}+1$; the four summands of $M$ are $D/a^{3}$, $D/q^{3}$, $D/(aq^{5})$ and $D/(bq^{2})$.

::: pf

::: {.pf-step #coprime}
$a$, $b$ and $q$ are pairwise coprime in $\QQ[x]$.

::: pf-proof
Three distinct monic irreducible polynomials in a principal ideal domain are pairwise coprime: $a=x-1$ and $b=x+2$ are linear, hence irreducible, and are distinct; $x-1$ and $x+2$ do not divide $q=x^{2}+1$, since $q(1)=2\ne0$ and $q(-2)=5\ne0$; and $q$ has no root in $\QQ$, so it is irreducible of degree $2$ over the field $\QQ$.
:::

:::

::: {.pf-step #split}
$D/(aq^{5})\cong D/(a)\oplus D/(q^{5})$ and $D/(bq^{2})\cong D/(b)\oplus D/(q^{2})$.

::: pf-proof
For coprime $u,v$ the Chinese remainder theorem for the principal ideal domain $\QQ[x]$ gives $D/(uv)\cong D/(u)\oplus D/(v)$, the map being $f\bmod uv\mapsto(f\bmod u,f\bmod v)$. Step [](#coprime){.pf-ref} supplies the coprimality of $a$ with $q^{5}$ and of $b$ with $q^{2}$.
:::

:::

::: {.pf-step #elementary}
The elementary divisors of $M$ are $a^{3}$, $a$, $q^{5}$, $q^{3}$, $q^{2}$, $b$, that is $(x-1)^{3}$, $x-1$, $(x^{2}+1)^{5}$, $(x^{2}+1)^{3}$, $(x^{2}+1)^{2}$, $x+2$.

::: pf-proof
The elementary divisors of a module are those of its primary summands. The summands $D/a^{3}$ and $D/q^{3}$ are already primary, contributing $a^{3}$ and $q^{3}$. By step [](#split){.pf-ref} the third summand is $D/a\oplus D/q^{5}$, contributing $a$ and $q^{5}$, and the fourth is $D/b\oplus D/q^{2}$, contributing $b$ and $q^{2}$. Collecting gives the six listed primary factors, one for each summand of $M$ in the structure theorem.
:::

:::

::: {.pf-step #align}
The invariant factors are $d_{1}=q^{2}$, $d_{2}=aq^{3}$, $d_{3}=a^{3}bq^{5}$.

::: pf-proof
For each irreducible, list the exponents occurring among the elementary divisors: for $q$ they are $2,3,5$; for $a$ they are $1,3$; for $b$ it is $1$. The number of invariant factors is the largest of these counts, namely $3$, and the invariant factors are obtained by aligning each list to the right, so that $d_{3}$ takes the largest exponent of every irreducible, $d_{2}$ the next, and $d_{1}$ the next, with a missing exponent contributing the factor $1$:
$$d_{1}=q^{2},\qquad d_{2}=aq^{3},\qquad d_{3}=a^{3}bq^{5}.$$
:::

:::

::: {.pf-step #check}
$d_{1}\mid d_{2}\mid d_{3}$ and $d_{1}d_{2}d_{3}$ is the product of the four annihilators.

::: pf-proof
Dividing, $d_{2}/d_{1}=aq$ and $d_{3}/d_{2}=a^{2}bq^{2}$, both polynomials, so $d_{1}\mid d_{2}\mid d_{3}$. The product is $q^{2}\cdot aq^{3}\cdot a^{3}bq^{5}=a^{4}bq^{10}$, and the product of the annihilators of the four summands is $a^{3}\cdot q^{3}\cdot aq^{5}\cdot bq^{2}=a^{4}bq^{10}$. Agreement of products with the divisibility chain is the check that the invariant-factor module $\bigoplus_{i}D/d_{i}$ is $M$.
:::

:::

::: {.pf-step #answer}
The elementary divisors are $\boxed{(x-1)^{3},\ (x-1),\ (x^{2}+1)^{5},\ (x^{2}+1)^{3},\ (x^{2}+1)^{2},\ (x+2)}$ and the invariant factors are
$$\boxed{\begin{aligned}d_{1}&=(x^{2}+1)^{2},\\ d_{2}&=(x-1)(x^{2}+1)^{3},\\ d_{3}&=(x-1)^{3}(x+2)(x^{2}+1)^{5}.\end{aligned}}$$

::: pf-proof
The list of elementary divisors is step [](#elementary){.pf-ref}, and substituting $a=x-1$, $b=x+2$, $q=x^{2}+1$ into step [](#align){.pf-ref} gives the three invariant factors, which step [](#check){.pf-ref} verifies are in the required divisibility chain with the correct product. These are the two answers the problem asks for.
:::

:::

:::
:::
