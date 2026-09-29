---
schema: qual/card@1
id: P-BKS13-8A
kind: problem
title: Rationality of $\log_m n$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2013 solution PDF and independently reviewed the prime-factorization argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked both implications and the coprime-exponent divisibility step.
---

::: {.problem}
Let m and n be integers greater than 1. Prove that $\log _ { m } ( n )$ is rational if and only if $m = l ^ { r }$ and $n = l ^ { s }$ , for some positive integers l, r, and s.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If
$$
m=l^r
\qquad\text{and}\qquad
n=l^s
$$
for positive integers $l,r,s$, then
$$
\log_m n
=
\frac{s}{r}
\in
\QQ.
$$

::: pf-proof

Since $m>1$, one has $l>1$. Then
$$
m^{s/r}
=
(l^r)^{s/r}
=
l^s
=
n.
$$
By the definition of logarithm,
$$
\log_m n=\frac{s}{r}.
$$

:::

:::

::: {.pf-step #s2}

Conversely, suppose
$$
\log_m n
=
\frac{s}{r}
$$
with positive coprime integers $r,s$. Then
$$
m^s=n^r.
$$

::: pf-proof

Exponentiating the defining identity gives
$$
n
=
m^{s/r}.
$$
Raising both sides to the $r$th power yields
$$
n^r=m^s.
$$

:::

:::

::: {.pf-step #s3}

Let
$$
m=\prod_{j=1}^k p_j^{e_j}
\qquad\text{and}\qquad
n=\prod_{j=1}^k p_j^{f_j},
$$
where the $p_j$ are the distinct primes occurring in either factorization
and $e_j,f_j\geq0$. Then
$$
se_j=rf_j
$$
for every $j$.

::: pf-proof

By step [](#s2){.pf-ref},
$$
m^s=n^r.
$$
The exponent of $p_j$ on the left is $se_j$, and on the right it is
$rf_j$. Uniqueness of prime factorization forces equality of these
exponents.

:::

:::

::: {.pf-step #s4}

For every $j$, there is a nonnegative integer $h_j$ such that
$$
e_j=rh_j
\qquad\text{and}\qquad
f_j=sh_j.
$$

::: pf-proof

From
$$
se_j=rf_j
$$
and
$$
\gcd(r,s)=1,
$$
Euclid's lemma gives
$$
r\mid e_j.
$$
Write
$$
e_j=rh_j.
$$
Substitution gives
$$
srh_j=rf_j,
$$
so
$$
f_j=sh_j.
$$

:::

:::

::: {.pf-step #s5}

Define
$$
l
\coloneqq
\prod_{j=1}^k p_j^{h_j}.
$$
Then
$$
\boxed{
m=l^r,
\qquad
n=l^s
}.
$$

::: pf-proof

Using step [](#s4){.pf-ref},
$$
m
=
\prod_jp_j^{rh_j}
=
\left(\prod_jp_j^{h_j}\right)^r
=
l^r,
$$
and similarly
$$
n=l^s.
$$
Because $m>1$, at least one $h_j$ is positive, so $l>1$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves one implication, and steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove the converse.

:::

:::

:::
