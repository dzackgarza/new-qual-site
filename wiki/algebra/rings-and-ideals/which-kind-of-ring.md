---
title: Which kind of ring is this?
order: 0
topics:
- Rings
- Commutative Algebra
---

# Which kind of ring is this?

The inclusions below relate fields, Euclidean domains, PIDs, UFDs, and integral domains. Counterexamples show that each inclusion is strict.

## The tower

\[
\text{field} \subset \text{Euclidean domain} \subset \text{PID} \subset \text{UFD} \subset \text{integral domain} \subset \text{ring}
\]

[[PR-LLBRB]]

:::{.remark title="Why each inclusion holds"}
\envlist

- **Field $\implies$ Euclidean:** to write $x = qy+r$, take $q = y\inv x$ and $r=0$.

- **Euclidean $\implies$ PID:** to divide is to contain, and the algorithm terminates on a gcd.
  Alternatively take $a\in I$ of minimal degree; if $I \neq Ra$, pick $b\in I$ not divisible by $a$ and write $b = aq+r$ with $d(r) < d(a)$, so $r = b-aq \in I$ contradicts minimality.

- **PID $\implies$ UFD:** existence because PIDs are Noetherian, so a proper factorization $a = a_1b_1$ gives a proper containment $\gens a \subsetneq \gens{a_1}$ that must stabilize, producing an irreducible factor; uniqueness by dividing two prime factorizations against each other.

:::

## The counterexamples, one per step

:::{.example title="Each inclusion is strict"}
\envlist

- **Euclidean, not a field:** $k[x]$ for $k$ a field.
  It is a PID hence a UFD, but $x$ is not invertible.

- **PID, not Euclidean:** $\ZZ\left[\frac{1 + \sqrt{-19}}{2}\right]$.

- **UFD, not a PID:** $\ZZ[x]$.
  $\ZZ$ is a UFD so $\ZZ[x]$ is, but $\gens{2,x} = \ts{\sum r_ix^i \st r_0 \in 2\ZZ}$ is not principal: a constant generator forces every coefficient even and misses $x$, and a generator of degree at least one misses $2$.

- **Domain, not a UFD:** $\ZZ[\sqrt{-5}]$, where $(2+\sqrt{-5})(2-\sqrt{-5}) = 9 = 3\cdot 3$ with all factors irreducible by a norm computation.

- **Ring, not a domain:** $\ZZ/4$, where $[2]^2 = [0]$.

:::

:::{.example}
A polynomial ring over a PID need not be a PID: $\gens{2,x}\normal \ZZ[x]$ again.

:::

## Reading a quotient

For a commutative ring with identity, primality and maximality of $I$ have quotient-ring characterizations:

[[PR-76BDN]]

:::{.remark title="The two correspondences"}
\[
I \text{ maximal} \iff R/I \text{ is a field}, \qquad I \text{ prime} \iff R/I \text{ is a domain}
.\]
Since fields are domains, maximal implies prime, giving $\mspec R \subseteq \spec R$:
\[
I \text{ maximal } \iff R/I \in \Field {\color{blue} \implies } R/I \in \mathsf{IntDomain} \iff I \text{ prime}
.\]

:::

For a field $k$, $(f)$ is maximal in $k[x]$ exactly when $k[x]/(f)$ is a field, equivalently when $f$ is irreducible.

## Transporting properties

[[PR-GEHJF]]

[[E-XH2QU]]

:::{.fact}
If $\mfm$ is maximal and $x\in R\sm\mfm$ then $\mfm + Rx = R = \gens 1$.
This is the standard way a maximality hypothesis gets used: it turns "not in $\mfm$" into "generates everything together with $\mfm$".

:::

## Gorenstein rings

[[D-DU4UQ]]

:::{.example title="Finite-dimensional graded Gorenstein criterion"}
Let $R=R_0\oplus\cdots\oplus R_n$ be a finite-dimensional commutative nonnegatively graded $k$-algebra with $R_0=k$ and $R_n\ne0$. Then $R$ is Gorenstein exactly when $\dim_k R_n=1$ and multiplication gives a perfect pairing $R_i\tensor_k R_{n-i}\to R_n$ for every $i$.

:::
