---
title: Classify this module
order: 0
topics:
- Modules
- Module Theory
---

# Classify this module

## Principal ideal domains and other rings

Over a principal ideal domain — $\ZZ$, $k[x]$, $k[\![x]\!]$ for a field $k$, and every Euclidean domain — the structure theorem is available and the classification is a computation; over $k[x,y]$, $\ZZ[x]$, or a quotient $k[x,y]/I$ it is not.
For finitely generated modules over $k[x,y]$ the four conditions free, projective, flat, and torsion-free can differ; over a principal ideal domain they coincide.

[[PR-UVUS6]]

## The computation over a PID

Let $R$ be a principal ideal domain and $M$ a finitely generated $R$-module.

### Presentation

Write $M \cong R^n / \im(A)$ for a matrix $A$ over $R$; for an abelian group given by generators and relations, $A$ is the relation matrix.

[[PR-Z3YWJ]]

[[PR-DJZLY]]

### Smith normal form

The Smith normal form of $A$ is computed from its minors, and its diagonal entries are the data the decomposition uses.

[[T-SMTHN]]

### Decomposition

$$
M \cong R^{n-k} \oplus \bigoplus_{i=1}^k R/\generators{a_i}.
$$

The free rank of $M$ is $n-k$, the summands $R/\generators{a_i}$ with $a_i$ a unit are zero, and the nonunit $a_i$ are the invariant factors of $M$.

[[D-SS34F]]

[[D-JQNJQ]]

### Elementary divisors and invariant factors

The conversion between the two lists is a regrouping of one set of prime powers, over the primes dividing the invariant factors.

[[PR-TLPVU]]

## Three instances of the structure theorem

| Ring | Module | Name of the classification |
| --- | --- | --- |
| $\ZZ$ | abelian group | structure theorem for finitely generated abelian groups |
| $k[x]$ | vector space with a linear operator | [[algebra/linear-algebra/rational-canonical-form\|rational canonical form]] |
| $k[x]$, with the characteristic polynomial split over $k$ | vector space with a linear operator | [[algebra/linear-algebra/jordan-canonical-form\|Jordan canonical form]] |

A square matrix $A$ over a field $k$ makes $k^n$ a $k[x]$-module with $x$ acting by $A$, and the invariant factors of this module are the invariant factors of $xI-A$.

## Free, projective, flat, and torsion-free modules

For modules over an integral domain the implications run

$$
\text{free} \implies \text{projective} \implies \text{flat} \implies \text{torsion-free},
$$

and none of them reverses in general; over a principal ideal domain the four conditions coincide for finitely generated modules.

[[PR-RPL4Q]]

[[PR-4K4XZ]]

[[D-FS52P]]

::: {.example title="Separating the conditions"}
\envlist

- $\ZZ/2$ over $\ZZ/6$ is projective and not free: $\ZZ/6\cong\ZZ/2\times\ZZ/3$, so $\ZZ/2$ is a direct summand of a free module, and it has $2<6$ elements.

- $\QQ$ over $\ZZ$ is flat, not projective, and not finitely generated.

- The ideal $\generators{2,x} \subseteq \ZZ[x]$ is torsion-free and not flat. Its localization at $\mathfrak m=\generators{2,x}$ is a finitely generated ideal of the local Noetherian domain $\ZZ[x]_{\mathfrak m}$ that needs two generators, since $\mathfrak m/\mathfrak m^2$ is $2$-dimensional over $\FF_2$; a finitely generated flat module over a local Noetherian ring is free, and a free ideal is principal.
:::

[[FF-QILDV]]

[[PR-ASW5L]]

Hence every nonprincipal ideal of an integral domain is a torsion-free module that is not free.
