---
title: The Galois correspondence
order: 10
problems:
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

## The theorem

[[T-NLPZY]]

[[FT-GJ6NR]]

[[T-SGY3O]]

[[PR-FM5FN]]

:::{.remark title="What corresponds to what"}
The correspondence is inclusion-reversing, and the three dictionary entries used constantly are
\[
[L:K] = \size H, \qquad [F:K] = [G:H], \qquad [L:F] = \size G
\]
for $L/K/F$ matching $1/H/G$.
An intermediate field is normal over the base exactly when its subgroup is normal in $G$, and then the quotient $G/H$ is its Galois group.
That is the entire content: normality of extensions and normality of subgroups are the same condition read on two sides.

:::

## Showing an extension is Galois

:::{.fact title="The checklist"}
**Irreducibility of $f$:**

- Eisenstein, including after shifting or inverting.
- Irreducible over some $\FF_p[x]$ implies irreducible over $\ZZ[x]$.
- A quadratic with no root in the field is irreducible.

**Separability of $f$:**

- Factor and exhibit distinct roots in $\bar k$.
- Over a perfect field, irreducible implies separable.
- For irreducible $f$: separable exactly when $f' \not\equiv 0$.

**Separability of the extension:**

- A splitting field of a separable polynomial is separable and normal, hence Galois.
- Algebraic extensions of perfect fields are separable, so in characteristic zero only normality needs checking.
- Harder routes: show $[L:k]_s = [L:k]$, or use that separability is a distinguished class.

**Normality:**

- Show $L/k$ is finite and the splitting field of some polynomial.

**Galois:**

- Normal and separable, equivalently the splitting field of a separable polynomial.
- Automatic for a finite extension of finite fields, being the splitting field of $x^{p^n}-x$.

:::

## Irreducibility in practice

[[PR-PB6UE]]

:::{.remark}
Finding a good prime is the hard part, but irreducibility over a small field can be checked exhaustively: enumerate the low-degree polynomials and divide.

:::

:::{.example title="Irreducibility mod $p$"}
$f(x) \da x^4 + x + 1$ is irreducible over $\ZZ[x]$: mod $2$, neither $0$ nor $1$ is a root so there is no linear factor, and dividing by each $a_1x^2+a_2x+a_3$ with $a_i \in \ts{0,1}$ leaves a remainder, so there is no quadratic factor.

:::

[[T-CF6S3]]

[[FT-2P5VV]]

:::{.remark title="Shifting"}
If $f(x+a)$ satisfies Eisenstein for some $p$, then $f$ is irreducible, since $\Delta_{f(x)} = \Delta_{f(x+a)}$ and a working prime divides the discriminant.

:::

[[T-AILFB]]
