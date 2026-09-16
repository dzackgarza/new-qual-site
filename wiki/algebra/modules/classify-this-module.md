---
title: Classify this module
order: 0
topics:
- Modules
- Module Theory
---

# Classify this module

## Principal ideal domains and other rings

Over a [[D-HTIL5|principal ideal domain]] $R$ -- for example $\ZZ$, $k[x]$ and $k[[x]]$ for a field $k$, and every Euclidean domain -- the structure theorem classifies finitely generated $R$-modules: each is the direct sum of a free module and a torsion module, and the torsion module is determined up to isomorphism by its invariant factors.

Over a ring that is not a PID, such as $k[x,y]$, $\ZZ[x]$, or a quotient $k[x,y]/I$, the structure theorem does not apply.
For finitely generated modules over such a ring, the properties of being [[D-LIEMF|free]], [[D-RHJMK|projective]], flat, and [[D-ZJJ7G|torsion-free]] can differ; over a PID they coincide.

## The computation over a PID

Let $R$ be a PID and $M$ a finitely generated $R$-module.

1. **Presentation.**
   Write $M \cong R^n / \im(A)$ for a matrix $A$ over $R$.
   For an abelian group given by generators and relations, $A$ is the relation matrix.

2. **Smith normal form.**
   The Smith normal form of $A$ has diagonal entries $a_1 \divides a_2 \divides \cdots \divides a_k$, with $a_i = d_i/d_{i-1}$, where $d_0=1$ and $d_i$ is a greatest common divisor of the $i\times i$ minors of $A$.
   See [[algebra/linear-algebra/smith-normal-form|Smith normal form]].

3. **Decomposition.**
   $$
   M \cong R^{n-k} \oplus \bigoplus_{i=1}^k R/\gens{a_i}.
   $$
   The free rank of $M$ is $n-k$, and the summands $R/\gens{a_i}$ with $a_i$ a unit are zero; the nonunit $a_i$ are the invariant factors of $M$.

4. **Elementary divisors and invariant factors.**
   The elementary divisors are the prime-power factors of the invariant factors.
   Conversely, the largest invariant factor is the product, over the primes $p$, of the largest elementary divisor that is a power of $p$; removing those elementary divisors and repeating gives the next invariant factor.

## Three instances of the structure theorem

| Ring | Module | Name of the classification |
| --- | --- | --- |
| $\ZZ$ | abelian group | structure theorem for finitely generated abelian groups |
| $k[x]$ | vector space with a linear operator | [[algebra/linear-algebra/rational-canonical-form\|rational canonical form]] |
| $k[x]$, with the characteristic polynomial split over $k$ | vector space with a linear operator | [[algebra/linear-algebra/jordan-canonical-form\|Jordan canonical form]] |

A square matrix $A$ over a field $k$ makes $k^n$ a $k[x]$-module with $x$ acting by $A$, and the invariant factors of this module are the invariant factors of $xI-A$.

## Free, projective, flat, and torsion-free modules

For modules over an integral domain,
$$
\text{free} \implies \text{projective} \implies \text{flat} \implies \text{torsion-free},
$$
and none of the implications reverses in general.
For finitely generated modules over a PID, the four conditions coincide.

::: {.example title="Separating the conditions"}
\envlist

- $\ZZ/2$ over $\ZZ/6$ is projective and not free: $\ZZ/6\cong\ZZ/2\times\ZZ/3$, so $\ZZ/2$ is a direct summand of a free module, and it has $2<6$ elements.
- $\QQ$ over $\ZZ$ is flat, not projective, and not finitely generated.
- The ideal $\gens{2,x} \subseteq \ZZ[x]$ is torsion-free and not free.
:::

## Free ideals

A nonzero ideal $I$ of an integral domain $R$ is free as an $R$-module if and only if it is principal ([[PR-ASW5L]]).
For distinct nonzero $m_1,m_2\in I$, the relation $m_2\cdot m_1 - m_1\cdot m_2 = 0$ has nonzero coefficients, so a basis of $I$ has one element.
In particular, every nonprincipal ideal of an integral domain is a torsion-free module that is not free.
