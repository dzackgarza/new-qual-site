---
schema: qual/card@1
id: E-MUN-8-4
kind: problem
title: Defining the Fibonacci numbers by recursive definition
classification:
  areas:
  - topology
  topics:
  - Recursive Definition
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §8 Exercise 4, printed p. 56; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.4,
    printed pp. 95-96 (tmp/sources/munkres-solutions-whitman.pdf). His rho is 1 at
    m = 1 and f(m) + f(m-1) for m > 1, with a_0 = 1; the range is Z_+ because the
    Fibonacci numbers are positive.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the recursive definition, which is what Queue D asks for on this card. The three steps are the data Theorem 8.4 needs (with the check that rho lands in A on every nonempty section), the function the theorem produces (with the two branches evaluated), and the identification with the Fibonacci recursion together with its uniqueness, which the prose asserted in one clause and which is now argued by applying the uniqueness clause of Theorem 8.4 to a second solution. Statement re-read against Munkres, Topology (2000), §8 Exercise 4, printed p. 56, and the construction against Dan Whitman's set, Exercise 8.4, printed pp. 95-96. No statement repair.
---

::: {.exercise}

The Fibonacci numbers of number theory are defined recursively by the formula
$$
\lambda_1 = \lambda_2 = 1,
\qquad
\lambda_n = \lambda_{n-1} + \lambda_{n-2} \quad \text{for } n > 2.
$$
Define them rigorously by use of Theorem 8.4.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.4, printed pp. 95--96** (`tmp/sources/munkres-solutions-whitman.pdf`); the function $\rho$ below is his. The statement is Munkres, *Topology*, 2nd ed. (2000), §8 Exercise 4, printed p. 56, and the theorem applied is Theorem 8.4 of that section.

::: pf

::: {.pf-step #data}
With $A=\ZZ_+$ and $a_0=1$, the rule
$$
\rho(f)=\begin{cases}1,&m=1,\\ f(m)+f(m-1),&m>1,\end{cases}
\qquad f:\{1,\dots,m\}\to\ZZ_+ ,
$$
assigns to each function on a nonempty section an element of $\ZZ_+$.

::: pf-proof
A nonempty section of $\ZZ_+$ is a set $\{1,\dots,m\}$ with $m\ge1$. For $m=1$ the value $1$ lies in $\ZZ_+$; for $m>1$ both $f(m)$ and $f(m-1)$ are defined and lie in $\ZZ_+$, and $\ZZ_+$ is closed under addition, so their sum lies in $\ZZ_+$. So $\rho$ is a function defined on the functions from nonempty sections into $A$ with values in $A$, which is the hypothesis Theorem 8.4 requires.
:::

:::

::: {.pf-step #existence}
There is a function $F:\ZZ_+\to\ZZ_+$ with $F(1)=1$ and $F(n)=\rho(F\restriction\{1,\dots,n-1\})$ for $n>1$; explicitly $F(2)=1$ and $F(n)=F(n-1)+F(n-2)$ for $n>2$.

::: pf-proof
Theorem 8.4 applies to the data of step [](#data){.pf-ref} and gives a unique $F:\ZZ_+\to\ZZ_+$ with $F(1)=a_0=1$ and $F(i)=\rho(F\restriction\{1,\dots,i-1\})$ for $i>1$. At $i=2$ the section is $\{1\}$, so $F(2)=\rho(F\restriction\{1\})=1$ by the first branch; at $i>2$ the section is $\{1,\dots,i-1\}$ with $i-1>1$, so $F(i)=\rho(F\restriction\{1,\dots,i-1\})=F(i-1)+F(i-2)$ by the second branch.
:::

:::

::: {.pf-step #fibonacci}
The numbers $\lambda_n=F(n)$ satisfy $\lambda_1=\lambda_2=1$ and $\lambda_n=\lambda_{n-1}+\lambda_{n-2}$ for $n>2$, and they are the only sequence with these properties.

::: pf-proof
The recursion of step [](#existence){.pf-ref} is exactly the three clauses that define the Fibonacci numbers, so $(\lambda_n)$ is such a sequence. For uniqueness, let $(\mu_n)$ be any sequence of positive integers with $\mu_1=\mu_2=1$ and $\mu_n=\mu_{n-1}+\mu_{n-2}$ for $n>2$, and consider the function $G:\ZZ_+\to\ZZ_+$ with $G(n)=\mu_n$. Then $G(1)=1=a_0$ and $G(i)=\mu_{i}=\mu_{i-1}+\mu_{i-2}=G(i-1)+G(i-2)=\rho(G\restriction\{1,\dots,i-1\})$ for $i>2$, while $G(2)=\mu_2=1=\rho(G\restriction\{1\})$; so $G$ is a function with the two properties that step [](#existence){.pf-ref} attributes to $F$, and the uniqueness clause of Theorem 8.4 gives $G=F$, that is $\mu_n=\lambda_n$ for all $n$. This is the rigorous definition the exercise asks for.
:::

:::

:::
:::
