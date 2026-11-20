---
schema: qual/card@1
id: E-SS10.EX-9
kind: problem
title: Sums of two squares from the formula for $r_2(n)$
classification:
  areas:
  - complex-analysis
  topics:
  - Number Theory
  - Theta Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with six steps, each carrying a `pf-proof`; the three parts and the formula used are
    unchanged. Cited by number only: the formula $r_2(n)=4(d_1(n)-d_3(n))$ for the number of
    representations as a sum of two squares, and the multiplicativity of the divisor sum of a
    multiplicative function. Checked: that no representation of an odd prime has a zero
    coordinate or equal absolute values, so the eight sign-and-order variants form one orbit;
    the counts of even and odd $j$ among $0,\dots,a$; and the three factors of the divisor
    product, including the factor $1$ from the power of $2$.
---

::: {.exercise}
Use the formula for $r_2(n)$ to prove the following:

(a) If $n = p$, where $p$ is a prime of the form $4k + 1$, then $r_2(n) = 8$. This implies that $n$ can be written in a unique way as $n = n_1^2 + n_2^2$, except for the signs and reordering of $n_1$ and $n_2$.

(b) If $n = q^a$, where $q$ is prime of the form $4k + 3$ and $a$ is a positive integer, then $r_2(n) > 0$ if and only if $a$ is even.

(c) In general, $n$ can be represented as the sum of two squares if and only if all the primes of the form $4k + 3$ that arise in the prime decomposition of $n$ occur with even exponents.
:::

::: {.solution}

::: pf

::: pf-step

Recall the two-squares formula
$$
r_2(n)=4\bigl(d_1(n)-d_3(n)\bigr), \tag{1}
$$
where $d_j(n)$ is the number of positive divisors of $n$ congruent to $j\pmod 4$.

::: pf-proof

This is the formula the exercise asks to be used: $r_2(n)$ is the number of pairs $(n_1,n_2)$ of integers with $n_1^2+n_2^2=n$, counted with signs and order, and $d_j(n)$ counts the positive divisors of $n$ in the residue class $j$ modulo $4$. For $n\ge1$ both sides are finite, $d_1+d_3$ being the number of odd divisors of $n$.

:::

:::

::: pf-step

(a) If $p\equiv1\pmod4$ is prime, its divisors are $1,p$, both congruent to $1\pmod4$, so $r_2(p)=4(2-0)=8$.

::: pf-proof

The positive divisors of a prime are $1$ and $p$; both are $\equiv1\pmod4$ because $p\equiv1\pmod4$. So $d_1(p)=2$ and $d_3(p)=0$, and (1) gives $8$.

:::

:::

::: pf-step

(a) No representation of such an odd prime has a zero coordinate or two coordinates of equal absolute value, so the eight sign-and-order variants come from one unordered pair of positive absolute values: the representation is unique up to signs and reordering.

::: pf-proof

If $n_1=0$ then $p=n_2^2$ is a square, impossible for a prime. If $\abs{n_1}=\abs{n_2}$ then $p=2n_1^2$ is even, impossible. So both coordinates are nonzero and of different absolute values, and the orbit of a single pair $(n_1,n_2)$ under the eight sign changes and the swap has exactly eight distinct elements: distinct signs and the swap change the ordered pair, and no two of the eight coincide because $\abs{n_1}\ne\abs{n_2}$ and both are nonzero. Since $r_2(p)=8$ counts all ordered signed pairs, they form one orbit, so the unordered pair of absolute values is unique.

:::

:::

::: pf-step

(b) If $q\equiv3\pmod4$ is prime, the divisors of $q^a$ are $1,q,\dots,q^a$ with $q^j\equiv(-1)^j\pmod4$, hence
$$
d_1(q^a)-d_3(q^a)=\begin{cases}1,&a\text{ even},\\0,&a\text{ odd},\end{cases}
$$
and $r_2(q^a)>0$ exactly when $a$ is even.

::: pf-proof

Since $q\equiv3\equiv-1\pmod4$, its $j$-th power is $\equiv(-1)^j$; among $j=0,\dots,a$ the even ones number $\lfloor a/2\rfloor+1$ and the odd ones $\lceil a/2\rceil$, so the difference is $1$ for even $a$ and $0$ for odd $a$. By (1), $r_2(q^a)=4$ for even $a$ and $0$ for odd $a$, and a count of representations is nonnegative, so it is positive exactly for even $a$.

:::

:::

::: pf-step

(c) With $\chi$ the nontrivial character modulo $4$ extended by $\chi(d)=0$ for even $d$, one has $d_1(n)-d_3(n)=\sum_{d\mid n}\chi(d)$, and this divisor sum is multiplicative; writing $n=2^e\prod_ip_i^{\alpha_i}\prod_jq_j^{\beta_j}$ with $p_i\equiv1$ and $q_j\equiv3\pmod4$,
$$
\sum_{d\mid n}\chi(d)=\prod_i(\alpha_i+1)\prod_j\bigl(1-1+\cdots+(-1)^{\beta_j}\bigr),
$$
the second factor being $1$ for even $\beta_j$ and $0$ for odd $\beta_j$.

::: pf-proof

$\chi(d)$ is $1$ on divisors $\equiv1$, $-1$ on divisors $\equiv3$ and $0$ on even divisors, so the sum over divisors is $d_1(n)-d_3(n)$. $\chi$ is completely multiplicative and the divisor sum of a multiplicative function is multiplicative, so the sum over $d\mid n$ is the product of the sums over the prime powers: over $2^e$ the only odd divisors are $1^j$, contributing $1$; over $p_i^{\alpha_i}$ every divisor is $\equiv1\pmod4$, contributing $\alpha_i+1$; over $q_j^{\beta_j}$ the divisors are $q_j^t$ with $\chi(q_j^t)=(-1)^t$, contributing $1-1+1-\cdots+(-1)^{\beta_j}$, which is $1$ for even $\beta_j$ and $0$ for odd.

:::

:::

::: pf-step

(c) By (1), $r_2(n)>0$ exactly when every prime $q\equiv3\pmod4$ occurs in $n$ with even exponent, which is the two-squares criterion.

::: pf-proof

Step 5 writes $d_1(n)-d_3(n)$ as a product of positive integers $\alpha_i+1$ and factors that are $1$ or $0$; the product is positive exactly when no factor vanishes, that is exactly when every $\beta_j$ is even, the primes $2$ and those $\equiv1\pmod4$ being unrestricted. By (1) this is $r_2(n)>0$, and $r_2(n)>0$ means $n$ is a sum of two squares.

:::

:::

:::
:::
