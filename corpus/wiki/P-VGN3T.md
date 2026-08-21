---
schema: qual/card@1
id: P-VGN3T
kind: problem
title: '$\ZZ[\sqrt{-5}]$ is not a PID: units $\pm 1$, and $3$ irreducible but not
  prime'
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Integral Domains
  - Principal Ideal Domains
relations: []
review: draft
solved: true
---

For a ring $R$, let $U(R)$ denote the multiplicative group of units in $R$. Recall that in an integral domain $R$, $r \in R$ is called *irreducible* if $r$ is not a unit in R, and the only divisors of $r$ have the form $ru$ with $u$ a unit in $R$. 

We call a non-zero, non-unit $r \in R$ *prime* in $R$ if $r \divides ab \implies r \divides a$ or $r \divides b$. 
Consider the ring $R = \{a + b \sqrt{-5}\suchthat a, b \in Z\}$.

a.
Prove $R$ is an integral domain.

b.
Show $U(R) = \{\pm1\}$.

c.
Show $3, 2 + \sqrt{-5}$, and $2 - \sqrt{-5}$ are irreducible in $R$.

d.
Show 3 is not prime in $R$.

e.
Conclude $R$ is not a PID.


:::{.concept}
\envlist

- Integral domain: $ab=0 \implies a\neq 0 \text{ or } b\neq 0$.
- Prime: $p \divides ab \implies p\divides a$ or $b$.
- Reducible: $a = xy$ where $x, y$ are proper divisors.
- Irreducible implies prime in a UFD.
:::

:::{.solution}
\envlist

- $R$ is an integral domain:
  - Let $\alpha = a + b\sqrt{-5}$ and $\beta = c + d \sqrt{-5}$ and set $\bar \alpha, \bar \beta$ be their conjugates.
  - Then
  \[
  0 = \alpha \beta = \alpha\bar\alpha \beta\bar\beta = (a^2-5b^2)(c^2-5d^2) \in \ZZ
  ,\]
  so one factor is zero.
  - If $a^2 = 5b^2$ then $a = \sqrt{5} b \not\in \ZZ$ unless $a=b=0$.
    Otherwise, the same argument forces $c=d=0$.

- The units are $\pm 1$:
  - Use that $u\in R\units \implies N(u) = \pm 1$, and $N(\alpha) = \alpha \bar\alpha = (a+b\sqrt{-5})(a-b\sqrt{-5}) = a^2 + 5b^2 = 1$
    forces $b=0$ and $a=\pm 1$.

- Irreducible elements:
  - $2, 3$ are irreducible because if (say) $3=xy$ then $N(x)N(y) = N(3) = 9$, and if neither $x,y$ are units then $N(x) = N(y) = 3$.
    But $N(a + b\sqrt{-5}) = a^2 + 5b^2$ and $a^2 + 5b^2 = 3$ has no solutions.
    The same argument works for $2$.
  - $2\pm \sqrt{-5}$ are irreducible because $N(2 + \sqrt{-5}) = 2^2 + 5(1) = 9$, and in fact $N(2 - \sqrt{-5}) = 2^2 + 5(-1)^2 = 9$.
    By the same argument as above, this forces irreducibility.

- $3$ is not prime: 
  - We can write $6 = (3)(2) = (1 + \sqrt{-5})(1 - \sqrt{-5})$, so if we assume $3$ is prime we get $3\divides (1 \pm \sqrt{-5})$.
  - But writing $(1\pm \sqrt{-5}) = 3r$ for some $r\in R$ yields 
  \[
  (1 \pm \sqrt{-5}) = 3(a + b\sqrt{-5}) \implies 3a=1, 3b = \pm 1
  .\]
  These have no solutions $a, b\in \ZZ$. $\contradiction$

- $R$ is not a PID:
  - Use that irreducibles are prime in a UFD, which is not true here. 

:::

