---
title: Classify this module
order: 0
problems:
  topics:
  - Modules
  - Module Theory
---

# Classify this module

A classification question is answerable exactly when the ring is a PID, and then it is one computation.
Over anything else the question is different, and the first job is noticing which case you are in.

## Is the ring a PID?

**Yes** -- $\ZZ$, $k[x]$, $k[[x]]$, any Euclidean domain, any local PID.
Then the structure theorem applies and the classification is complete: every finitely generated module is a free part plus a torsion part, and the torsion part is determined by its invariant factors.

**No** -- $k[x,y]$, $\ZZ[x]$, $k[x,y]/I$, any ring with a non-principal ideal.
Then there is no classification, and the question being asked is something else: is this module free, projective, flat, torsion-free, or finitely generated?
Those are the properties that separate over a general ring and coincide over a PID.

## Over a PID: the computation

1. **Present the module.**
   Write $M \cong R^n / \im(A)$ for a matrix $A$ over $R$.
   For an abelian group given by generators and relations, $A$ is the relation matrix.

2. **Take the Smith normal form of $A$.**
   The invariant factors $a_1 \divides a_2 \divides \cdots \divides a_k$ appear on the diagonal, and are computed as $a_i = d_i/d_{i-1}$ with $d_i$ the gcd of the $i\times i$ minors.
   See [[algebra/linear-algebra/smith-normal-form|Smith normal form]].

3. **Read off the decomposition.**
   \[
   M \cong R^{n-k} \oplus \bigoplus_{i=1}^k R/\gens{a_i}
   .\]
   The free rank is $n-k$, and the units among the $a_i$ contribute nothing.

4. **Convert between the two forms if asked.**
   Invariant factors are the divisibility chain; elementary divisors are the prime powers.
   Going from elementary divisors to invariant factors: take the largest prime power for each prime to build $a_k$, the next largest to build $a_{k-1}$, and so on.

## The three instances of the same theorem

| Ring | Module | The theorem is called |
| --- | --- | --- |
| $\ZZ$ | abelian group | the structure theorem for finitely generated abelian groups |
| $k[x]$ | vector space with an operator | [[algebra/linear-algebra/rational-canonical-form\|rational canonical form]] |
| $k[x]$, $\chi$ split | the same | [[algebra/linear-algebra/jordan-canonical-form\|Jordan canonical form]] |

Recognizing which one a problem is asking is usually the difficulty.
A question about a matrix over $\QQ$ and a question about an abelian group of order $360$ are the same computation over different rings.

## Over a general ring: which property is being asked

For modules over an integral domain:
\[
\text{free} \implies \text{projective} \implies \text{flat} \implies \text{torsion-free}
,\]
and none of the arrows reverses in general.
For finitely generated modules over a PID, all four conditions coincide. The separating examples below relax either the domain/PID hypothesis or finite generation.

The standard separating examples:

- $\ZZ/2$ over $\ZZ/6$: projective, not free.
- $\QQ$ over $\ZZ$: flat, not projective, and not finitely generated.
- An ideal of a non-PID, such as $\gens{2,x} \subseteq \ZZ[x]$: torsion-free, not free.

## The one-line test for an ideal

An ideal $I \subseteq R$ over an integral domain is free as a module exactly when it is principal.
The reason is that any two elements of $I$ are dependent: $m_1m_2 - m_2m_1 = 0$ is a nontrivial relation by commutativity, so a basis has at most one element.

Thus freeness of an ideal reduces to principality in the ring; non-principal ideals are the standard source of torsion-free, non-free modules.
