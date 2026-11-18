---
schema: qual/card@1
id: P-F05BN
kind: problem
title: Binomial theorem and $(x+y)^p \equiv x^p+y^p \pmod{p}$
classification:
  areas:
  - prelim
  topics:
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(a) State the binomial theorem.

(b) Prove that if $p$ is a prime number, then $(x+y)^p \equiv x^p + y^p \pmod p$.
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper (`assets/attachments/grad_prelim_Fall05.pdf`) and no solutions sheet accompanies it, so the statement and the argument below are the card's own. Part (a) asks for the statement of the binomial theorem and is answered by recording it; part (b) turns on the divisibility of the intermediate binomial coefficients, which is where primality is used, and the card's closing step says so.

Throughout, $\binom nk$ is the binomial coefficient, $p$ is a prime, and a congruence of polynomials is read coefficientwise, that is in $(\ZZ/p\ZZ)[x,y]$.

::: pf

::: {.pf-step #statement}
(a) For every nonnegative integer $n$ and all $x,y$,
$$
(x+y)^{n}=\sum_{k=0}^{n}\binom nk x^{n-k}y^{k},
$$
where $\binom nk=\frac{n!}{k!\,(n-k)!}$ for $0\leq k\leq n$.

::: pf-proof
This is the binomial theorem, which the exercise asks to state; no proof is required for part (a). Its expansion for $n=0$ and $n=1$ reads $(x+y)^{0}=1$ and $(x+y)^{1}=x+y$, matching the formula, and the general case follows by induction on $n$ from Pascal's rule $\binom{n+1}{k}=\binom nk+\binom{n}{k-1}$.
:::

:::

::: {.pf-step #divisibility}
For $1\leq k\leq p-1$ the integer $\binom pk$ is divisible by $p$.

::: pf-proof
From $\binom pk=\frac{p!}{k!\,(p-k)!}$ we get the identity of integers
$$
p\cdot(p-1)!=\binom pk\cdot k!\,(p-k)!.
$$
Since $1\leq k\leq p-1$ and $1\leq p-k\leq p-1$, both $k!$ and $(p-k)!$ are products of integers each smaller than the prime $p$, so $p$ divides neither factorial and hence does not divide their product $k!\,(p-k)!$. By Euclid's lemma, $p$ prime and $p\mid p\cdot(p-1)!$ with $p\nmid k!(p-k)!$ force $p\mid\binom pk$.
:::

:::

::: {.pf-step #freshman}
(b) $(x+y)^{p}\equiv x^{p}+y^{p}\pmod p$.

::: pf-proof
By step [](#statement){.pf-ref} with $n=p$,
$$
(x+y)^{p}=\sum_{k=0}^{p}\binom pk x^{p-k}y^{k}=x^{p}+\sum_{k=1}^{p-1}\binom pk x^{p-k}y^{k}+y^{p},
$$
the terms $k=0$ and $k=p$ being $x^{p}$ and $y^{p}$ because $\binom p0=\binom pp=1$. By step [](#divisibility){.pf-ref} each coefficient $\binom pk$ with $1\leq k\leq p-1$ is $0$ in $\ZZ/p\ZZ$, so the whole sum reduces to $x^{p}+y^{p}$ modulo $p$.
:::

:::

::: pf-step
Therefore $(x+y)^{p}\equiv x^{p}+y^{p}\pmod p$ for all integers $x,y$, and primality is exactly what the proof uses.

::: pf-proof
An identity in $(\ZZ/p\ZZ)[x,y]$ gives, on substituting the classes of integers $x,y$ and evaluating, the congruence $\equiv$ of integers modulo $p$, which is the assertion of (b). The single place where $p$ being prime enters is step [](#divisibility){.pf-ref}; for composite $n$ the statement fails, as $n=4$ shows, where $\binom42=6\not\equiv0\pmod4$.
:::

:::

:::

:::
