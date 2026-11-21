---
schema: qual/card@1
id: P-BKS03-9A
kind: problem
title: The ring $\ZZ+3i\ZZ$ is not a UFD
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let
$$
R=\{a+3bi:a,b\in\ZZ\}.
$$
Prove that $R$ is a subring of $\CC$, an integral domain, and not a unique factorization domain.
:::

::: {.solution}

The argument is the card's own: $R$ is a subring of $\CC$ by direct computation, and $10$ has two essentially different factorisations into irreducibles.

::: pf

::: {.pf-step #subring}

$R=\{a+3bi:a,b\in\ZZ\}$ is a subring of $\CC$, hence an integral domain.

::: pf-proof

$R$ is closed under subtraction, since $(a+3bi)-(c+3di)=(a-c)+3(b-d)i$ with integer parts, and contains $1$. It is closed under multiplication: $(a+3bi)(c+3di)=(ac-9bd)+3(ad+bc)i$, again with integer parts. A subring of a field is an integral domain because a subring of a commutative ring without zero divisors has no zero divisors and is commutative.

:::

:::

::: {.pf-step #norm}

The norm $N(a+3bi)=a^{2}+9b^{2}$ is a positive integer, multiplicative, and $N(z)<9$ forces $z\in\ZZ$.

::: pf-proof

$N(z)=\abs{z}^{2}=z\bar z$, so $N(zw)=\abs{zw}^{2}=\abs{z}^{2}\abs{w}^{2}=N(z)N(w)$, and $N(z)=0$ only for $z=0$. If $a^{2}+9b^{2}<9$ then $b=0$, so $z=a\in\ZZ$; then $N(a)=a^{2}$, and $N(z)=1$ exactly for $z=\pm1$.

:::

:::

::: {.pf-step #irreducible}

$2$, $5$, $1+3i$ and $1-3i$ are irreducible in $R$, and no two are associates.

::: pf-proof

$N(2)=4$ and $N(5)=25$, and $N(1\pm3i)=1+9=10$. If $2=zw$ with neither factor a unit, then $4=N(z)N(w)$ with both norms $\ge2$ and $<4$, so one of them would be $2$ or $3$; but $a^{2}+9b^{2}\in\{2,3\}$ has no integer solution, so no element of $R$ has norm $2$ or $3$, and $2$ is irreducible. A nontrivial factorisation of $5$ would need a factor of norm $5$, likewise impossible, and a nontrivial factorisation of $1+3i$ a factor of norm $2$ or $5$, also impossible. Units are exactly the elements of norm $1$, namely $\pm1$, so two elements are associates only if they have equal norm; the norms $4,25,10$ show that $2$ is associate to neither of $5,1+3i,1-3i$, and $\pm(1+3i)\ne\pm(1-3i)$.

:::

:::

::: {.pf-step #twofactorisations}

$10=2\cdot5=(1+3i)(1-3i)$ gives two essentially distinct factorisations.

::: pf-proof

$2\cdot5=10$ and $(1+3i)(1-3i)=1-9i^{2}=10$, and all four factors lie in $R$ and are irreducible by step [](#irreducible){.pf-ref}. The two factorisations have the same number of factors but no factor of the first is associate to a factor of the second.

:::

:::

::: {.pf-step #notufd}

$R$ is not a unique factorisation domain.

::: pf-proof

Suppose $R$ were a UFD. In a UFD an irreducible element is prime, so the irreducible $2$, dividing $10=(1+3i)(1-3i)$, would divide one factor: $1+3i=2w$ or $1-3i=2w$ with $w\in R$. But then $w=(1\pm3i)/2=\frac12\pm\frac32 i$ has non-integer parts, so $w\notin R$. Hence $R$ has an element with two essentially distinct factorisations into irreducibles:
$$
\boxed{R\ \text{is an integral domain that is not a UFD:}\ 10=2\cdot5=(1+3i)(1-3i).}
$$

:::

:::

:::

:::
