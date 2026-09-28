---
title: The Galois correspondence
order: 10
topics:
- Isomorphism Theorems
- Irreducibility Criteria
---

# The Galois correspondence

## Galois extensions

[[D-5JYEI]]

[[FD-4GFTY]]

[[FT-3WWKN]]

[[FD-YJEDU]]

[[FE-Z4VF2]]

[[PR-QDRB4]]

[[PR-3TYBE]]

## The fundamental theorem

[[T-NLPZY]]

[[FT-GJ6NR]]

[[T-SGY3O]]

[[PR-FM5FN]]

::: {.remark title="Degrees, indices, and normal subgroups"}
Let $L/F$ be a finite Galois extension with $G=\Gal(L/F)$.
The correspondence $K\mapsto\Gal(L/K)$ from intermediate fields to subgroups is inclusion-reversing, and if $K$ corresponds to $H$, then
$$
[L:K] = \size H, \qquad [K:F] = [G:H], \qquad [L:F] = \size G.
$$
The extension $K/F$ is Galois if and only if $H$ is normal in $G$, and then $\Gal(K/F)\cong G/H$.
:::

## Criteria for Galois extensions

::: {.fact title="Criteria"}
**Irreducibility of $f\in\QQ[x]$.**

- Eisenstein's criterion, applied to $f(x)$, to $f(x+a)$ for some $a\in\ZZ$, or to the reversed polynomial $x^nf(1/x)$.

- If $f\in\ZZ[x]$ has leading coefficient not divisible by a prime $p$ and $f\bmod p$ is irreducible over $\FF_p$, then $f$ is irreducible over $\QQ$.

- A polynomial of degree $2$ or $3$ over a field is irreducible if and only if it has no root in the field.

**Separability of $f$.**

- $f$ is separable if and only if $\gcd(f,f')=1$.

- Over a perfect field, every irreducible polynomial is separable.

- An irreducible $f$ is separable if and only if $f' \neq 0$.

**Separability of an extension.**

- The splitting field of a separable polynomial is separable and normal, hence Galois.

- Every algebraic extension of a perfect field is separable; in characteristic $0$ a finite extension is Galois if and only if it is normal.

- A finite extension $L/k$ is separable if and only if its separable degree $[L:k]_s$ equals $[L:k]$, and separable extensions form a distinguished class.

**Normality.**

- A finite extension $L/k$ is normal if and only if $L$ is the splitting field over $k$ of some polynomial.

**Galois.**

- A finite extension is Galois if and only if it is normal and separable, if and only if it is the splitting field of a separable polynomial.

- Every finite extension of finite fields is Galois: $\FF_{p^n}$ is the splitting field of the separable polynomial $x^{p^n}-x$ over every subfield.
:::

## Irreducibility

[[PR-PB6UE]]

::: {.remark}
Over a finite field $\FF_p$, a polynomial of degree $d$ is irreducible if and only if it has no monic irreducible factor of degree at most $d/2$, which can be checked by dividing by each monic irreducible polynomial of degree at most $d/2$.
:::

::: {.example title="Irreducibility modulo $2$"}
$f(x) \da x^4 + x + 1$ is irreducible over $\QQ$.
Modulo $2$, $f(0)=f(1)=1$, so $f$ has no linear factor, and the only monic irreducible quadratic over $\FF_2$ is $x^2+x+1$, which leaves remainder $1$ on dividing $f$; hence $f$ is irreducible over $\FF_2$.
:::

[[T-CF6S3]]

[[FT-2P5VV]]

::: {.remark title="Shifting"}
For $a\in\ZZ$, $g(x)\mapsto g(x+a)$ is a ring automorphism of $\QQ[x]$, so if $f(x+a)$ satisfies Eisenstein's criterion at $p$, then $f$ is irreducible.
For monic $f$ of degree $n\geq2$, in that case $f(x+a)\equiv x^n \pmod p$, so $f \bmod p$ has a repeated root, and $p$ divides $\Delta_f = \Delta_{f(x+a)}$; the primes to test are among the prime divisors of the discriminant.
:::

[[T-AILFB]]
