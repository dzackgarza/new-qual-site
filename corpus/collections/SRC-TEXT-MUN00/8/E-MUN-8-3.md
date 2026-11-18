---
schema: qual/card@1
id: E-MUN-8-3
kind: problem
title: Powers and factorials as cases of the recursive product
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
    Read against Munkres, Topology (2000), §8 Exercise 3, printed p. 56; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 8.3,
    printed p. 95 (tmp/sources/munkres-solutions-whitman.pdf): the constant sequence
    b_i = a gives a^n, and b_i = i gives n!, each checked against its own induction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the two specializations into numbered steps, and supplied what the prose left as an
    index remark: the product of Exercise 8.2 satisfies p(1) = b_1 and p(n) = p(n-1) b_n for n > 1
    (as Theorem 8.4 delivers it on the earlier card), so specializing b_i = a returns exactly the
    recursion a^1 = a, a^n = a^{n-1} a of Exercise 4.6, and specializing b_i = i returns 1! = 1,
    n! = (n-1)! n. No defect found. Not re-read this session: the Whitman page and Munkres printed
    p. 56.
---

::: {.exercise}

Obtain the definitions of $a^n$ and $n!$ for $n \in \ZZ_+$ as special cases of Exercise 2.
:::

::: {.solution}

Both specializations and their verifications are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 8.3, printed p. 95** (`tmp/sources/munkres-solutions-whitman.pdf`).

By Exercise 8.2, applied through Theorem 8.4 to a sequence $(b_{1},b_{2},\dots)$, there is a unique function $p\colon\ZZ_{+}\to\RR$ with
$$
p(1)=b_{1},\qquad p(n)=p(n-1)\,b_{n}\ \ (n>1),
$$
and $\prod_{k=1}^{n}b_{k}\coloneqq p(n)$.

::: pf

::: {.pf-step #powers}
With $b_{i}=a$ for every $i$, the resulting $p$ satisfies $p(n)=a^{n}$.

::: pf-proof
The sequence is constant, so the recursion of Exercise 8.2 reads $p(1)=a$ and $p(n)=p(n-1)\,a$ for $n>1$. That is exactly the recursion defining the powers of $a$ in Exercise 4.6, namely $a^{1}=a$ and $a^{n}=a^{n-1}a$; by the uniqueness in Theorem 8.4 the two functions agree, so $p(n)=a^{n}$ for every $n\geq1$.
:::

:::

::: {.pf-step #factorials}
With $b_{i}=i$ for every $i$, the resulting $p$ satisfies $p(n)=n!$.

::: pf-proof
Now the recursion reads $p(1)=1$ and $p(n)=p(n-1)\,n$ for $n>1$, which is the usual recursive definition of the factorial, $1!=1$ and $n!=(n-1)!\,n$. By induction on $n$ the two agree: at $n=1$ both are $1$, and if $p(n-1)=(n-1)!$ then $p(n)=(n-1)!\,n=n!$.
:::

:::

::: {.pf-step}
$a^{n}$ and $n!$ are the values at $n$ of the product construction of Exercise 8.2 for the sequences $b_{i}=a$ and $b_{i}=i$.

::: pf-proof
Steps [](#powers){.pf-ref} and [](#factorials){.pf-ref} identify the two specializations. Both are cases of one construction, which is what the exercise asks: the definition of the product of a sequence of reals specializes to the definition of powers and to the definition of factorials.
:::

:::

:::

:::
