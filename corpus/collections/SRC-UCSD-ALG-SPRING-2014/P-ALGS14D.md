---
schema: qual/card@1
id: P-ALGS14D
kind: problem
title: Artinian domains are fields; primes equal maximals in Artinian rings
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $A$ be a unital commutative ring which is Artinian, i.e. if $\mathfrak{a}_1 \supseteq \mathfrak{a}_2 \supseteq \cdots$ is a chain of ideals of $A$, then $\mathfrak{a}_{k_0} = \mathfrak{a}_{k_0+1} = \cdots$ for some $k_0$.

(a) Show that, if $A$ is an integral domain, then $A$ is a field.
(Hint: Consider $\langle x \rangle \supseteq \langle x^2 \rangle \supseteq \cdots$.)

(b) Prove that $\mathfrak{p} \subset A$ is a prime ideal if and only if $\mathfrak{p}$ is a maximal ideal.
:::

::: {.solution}
<1>1. Part (a): let $0\ne x\in A$.
Since $A$ is Artinian, the descending chain
\[
(x)\supseteq(x^2)\supseteq(x^3)\supseteq\cdots
\]
stabilizes.
Hence for some $n\ge1$,
\[
(x^n)=(x^{n+1}).
\]
::: {.proof}
This is the descending chain condition on ideals.
:::

<1>2. From $(x^n)=(x^{n+1})$ there exists $a\in A$ such that
\[
x^n=ax^{n+1}.
\]
Since $A$ is a domain and $x\ne0$, cancellation gives $1=ax$.
Thus every nonzero element of $A$ is invertible, so $A$ is a field.
::: {.proof}
We have $x^n(1-ax)=0$.
Since $x^n\ne0$ in a domain, $1-ax=0$.
:::

<1>3. Part (b): every maximal ideal of a commutative unital ring is prime.
::: {.proof}
If $\mathfrak m$ is maximal, then $A/\mathfrak m$ is a field, hence an integral domain; therefore $\mathfrak m$ is prime.
:::

<1>4. Conversely, let $\mathfrak p$ be prime.
Then $A/\mathfrak p$ is an integral domain, and it is Artinian because quotients of Artinian rings are Artinian.
By part (a), $A/\mathfrak p$ is a field.
Hence $\mathfrak p$ is maximal.
::: {.proof}
Ideals of $A/\mathfrak p$ correspond to ideals of $A$ containing $\mathfrak p$, so descending chains in the quotient stabilize.
The remaining implication is the standard maximal-ideal criterion.
:::
:::
