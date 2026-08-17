---
schema: qual/card@1
id: P-6T7VU
kind: problem
title: Invariant factors of $R/(r)\oplus R/(s)$ over a PID
classification:
  areas:
  - algebra
  topics:
  - structure-theorem
  - modules
  - principal-ideal-domains
relations: []
review: draft
solved: false
---

::: problem
**Lemma:**
If $M$ is a cyclic module over a PID, then $M$ has exactly 1 invariant factor.

**Lemma:**
Let $A$ be a cyclic module, so $A = Ra$. If the order of $A$ is $r$, so $\mathcal O_a = (r)$, then $A \cong R/(r)$.

This means that we can write $A = R/(a)$ and $B = R/(b)$, and $a, b$ are the invariant factors of $A, B$ respectively, and $M\definedas A \oplus B \cong R/(ab)$.

Since $R$ is a PID, there is unique factorization, so we can write
\[
\begin{align*}
r &= \prod_{i=1}^n p_i^{k_i} \\
s &= \prod_{i=1}^n p_i^{\ell_i} \\
\implies rs &= \prod_{i=1}^n p_i^{k_i + \ell_i},
\end{align*}
\]

where we allow some $k_i, \ell_i = 0$ so that we can take the product over the same set of primes.

However, means that the elementary divisors of $M$ are given by the multiset $L \definedas \theset{p_i^{k_i}} \union \theset{p_i^{\ell_i}}$.

The largest invariant factor $d_1$ of $M$ is obtained from the elementary divisors
by 

a. Forming the multiset $L$ of elementary divisors,
b. Selecting the highest power of each prime occurring, say $s_i \definedas p_i^{\max(k_i, \ell_i)}$,
c. Removing $s_i$ from $L$,
d. Then letting $d_1 = \prod s_i$.

However, this process yields $d_1 = \mathrm{lcm}(r, s)$ by construction, since 
$$
d_1 = \prod_{i=1}^n s_i = \prod_{i=1}^n p_i^{\max(k_i, \ell_i)} \definedas \mathrm{lcm}(r_s).
$$

The next largest invariant factor is obtained by performing the same process on the remaining prime powers in $L$.
However, we can note that after obtaining $d_1$, we have $L = \theset{p_i^{\min(k_i, \ell_i)}}$, since **there were only two choices** for each $p_i$ occurring and we chose the copy with the maximal exponent.

But this means when we perform step (b) to obtain $d_2$, **there is now only one choice**, and thus each $s_i = p_i^{\min(k_i, \ell_i)}$ and we have
$$
d_2 = \prod_{i=1}^n s_i = \prod_i p_i^{\min(k_i, \ell_i)} \definedas \gcd(r, s).
$$

> Note: by construction, $d_2 \divides d_1$, since we are choosing from the same prime powers but with smaller exponents.

Since there were only at most two copies of each prime occurring in $L$, where one of them was chosen for $d_1$ and the other was chosen for $d_2$, this exhausts all of the elements in $L$. But this means $M$ has only two invariant divisors,
\[
\begin{align*}
d_1 &= \lcm(r, s) \\
d_2 &= \gcd(r, s)
,\end{align*}
\]

which is what we wanted to show.
$\qed$
:::
