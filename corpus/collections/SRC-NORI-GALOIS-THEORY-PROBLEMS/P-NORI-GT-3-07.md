---
schema: qual/card@1
id: P-NORI-GT-3-07
kind: problem
title: Roots of cyclotomic polynomials in characteristic $p$
classification:
  areas: [algebra]
  topics:
  - Cyclotomic Polynomials
  - Positive Characteristic
  - Roots of Unity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.7 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
The cyclotomic polynomials $\Phi_{n}(X) \in \ZZ[X]$, defined for all natural numbers $n$, have the property
$$
X^{n} - 1 = \prod_{d \mid n} \Phi_{d}(X).
$$

Let $n = n' p^{k}$ with $p$ not dividing $n'$. Let $F$ be a field of characteristic $p$ such that $\mu_{n'}(F)$ has order $n'$. Show that the roots of $\Phi_{n}(X)$ in $F$ are the primitive $n'$-th roots of unity, each of them occurring with multiplicity $\varphi(p^{k})$.

Here $\varphi$ is Euler's phi function: $\varphi(m)$ is the order of the group of units of the ring $\ZZ/m\ZZ$. Equivalently, $\varphi(m)$ is the cardinality of the set of natural numbers $k \leq m$ such that $\gcd(k, m) = 1$. $\varphi(1) = 1$. If $p$ is a prime, then $\varphi(p^{k}) = p^{k-1}(p-1)$ if $k > 0$.
:::

::: {.solution}

Write
$$
n=mp^k,
\qquad m=n',
\qquad p\nmid m.
$$

::: pf

::: {.pf-step #s1-1}

If $k=0$, then $n=m$ and $\Phi_n=\Phi_m$ has as its roots exactly the primitive $m$-th roots of unity, each with multiplicity $1=\varphi(1)$.


::: pf-proof

Because $p\nmid m$, the derivative of $X^m-1$ is
$$
mX^{m-1}\ne0,
$$
so all $m$-th roots of unity are simple. The defining factorization
$$
X^m-1=\prod_{d\mid m}\Phi_d(X)
$$
then partitions them by exact order; hence the roots of $\Phi_m$ are precisely those of order $m$.

:::

:::

::: {.pf-step #s1-2}

Assume $k>0$. In $\FF_p[X]$ one has
$$
X^{mp^k}-1=(X^m-1)^{p^k}.
$$


::: pf-proof

In characteristic $p$, Frobenius gives
$$
(A-B)^{p^k}=A^{p^k}-B^{p^k}.
$$
Take $A=X^m$ and $B=1$.

:::

:::

::: {.pf-step #s1-3}

Likewise,
$$
X^{mp^{k-1}}-1=(X^m-1)^{p^{k-1}}.
$$


::: pf-proof

Apply the same Frobenius identity with exponent $p^{k-1}$.

:::

:::

::: {.pf-step #s1-4}

Over $\ZZ[X]$, one has
$$
\frac{X^{mp^k}-1}{X^{mp^{k-1}}-1}
=\prod_{d\mid m}\Phi_{dp^k}(X).
$$


::: pf-proof

The cyclotomic factorization of the numerator contains $\Phi_e$ for every divisor $e$ of $mp^k$, while the denominator contains those for divisors of $mp^{k-1}$. The divisors occurring only in the numerator are exactly
$$
e=dp^k
$$
with $d\mid m$. Cancelling the common factors gives the identity.

:::

:::

::: {.pf-step #s1-5}

Reducing step [](#s1-4){.pf-ref} modulo $p$ and using steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} gives
$$
\prod_{d\mid m}\Phi_{dp^k}(X)
=(X^m-1)^{p^k-p^{k-1}}
=(X^m-1)^{\varphi(p^k)}.
$$


::: pf-proof

The quotient of the two powers from steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} is
$$
(X^m-1)^{p^k-p^{k-1}},
$$
and for $k>0$,
$$
p^k-p^{k-1}=p^{k-1}(p-1)=\varphi(p^k).
$$

:::

:::

::: {.pf-step #s1-6}

Since
$$
X^m-1=\prod_{d\mid m}\Phi_d(X),
$$
step [](#s1-5){.pf-ref} becomes
$$
\prod_{d\mid m}\Phi_{dp^k}(X)
=\prod_{d\mid m}\Phi_d(X)^{\varphi(p^k)}
$$
in characteristic $p$.


::: pf-proof

Substitute the cyclotomic factorization of $X^m-1$ into the right side of step [](#s1-5){.pf-ref} and distribute the common exponent over the product.

:::

:::

::: {.pf-step #s1-7}

For distinct divisors $d,e$ of $m$, the polynomials $\Phi_d$ and $\Phi_e$ have disjoint root sets in $F$.


::: pf-proof

Because $p\nmid m$, every $m$-th root of unity is simple. A root of $\Phi_d$ has exact order $d$, while a root of $\Phi_e$ has exact order $e$. A root cannot have two different exact orders.

:::

:::

::: {.pf-step #s1-8}

The roots of $\Phi_{mp^k}$ are exactly the primitive $m$-th roots of unity.


::: pf-proof

In step [](#s1-6){.pf-ref}, the factor indexed by $d=m$ on the right has exactly the primitive $m$-th roots by step [](#s1-1){.pf-ref}. By step [](#s1-7){.pf-ref} these roots occur in no factor indexed by a proper divisor $d<m$. Equality of the two products therefore forces them to occur in the corresponding left factor $\Phi_{mp^k}$ and nowhere else. Conversely, any root of $\Phi_{mp^k}$ contributes to the left product and hence, by step [](#s1-6){.pf-ref}, is an $m$-th root of unity; its placement in the $d=m$ factor forces exact order $m$.

:::

:::

::: {.pf-step #s1-9}

Each primitive $m$-th root occurs in $\Phi_{mp^k}$ with multiplicity
$$
\varphi(p^k).
$$


::: pf-proof

Fix a primitive $m$-th root $\zeta$. On the right side of step [](#s1-6){.pf-ref}, it is a simple root of $\Phi_m$ by $p\nmid m$, hence has total multiplicity $\varphi(p^k)$. By step [](#s1-7){.pf-ref} it occurs in no other right-hand factor. By step [](#s1-8){.pf-ref} it occurs on the left only in $\Phi_{mp^k}$. Equality of the products therefore gives precisely that multiplicity in $\Phi_{mp^k}$.

:::

:::

::: {.pf-step #s1-10}

Thus for every $k\ge0$, the roots in $F$ of
$$
\Phi_{n}(X)=\Phi_{mp^k}(X)
$$
are precisely the primitive $m=n'$-th roots of unity, each occurring with multiplicity
$$
\boxed{\varphi(p^k)}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} proves the case $k=0$. Steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} prove the assertion for $k>0$.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is exactly the required statement.

:::

:::

:::
