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

## The theorem

[[T-NLPZY]]

[[FT-GJ6NR]]

[[T-SGY3O]]

[[PR-FM5FN]]

::: {.remark title="What corresponds to what"}
The correspondence reverses inclusion and relates degrees to subgroup indices:
\[
[L:K] = \size H, \qquad [K:F] = [G:H], \qquad [L:F] = \size G
\]
for a finite Galois extension $L/F$ and intermediate field $K$, with $G=\Gal(L/F)$ and $H=\Gal(L/K)$.
An intermediate field is normal over the base exactly when its subgroup is normal in $G$, and then the quotient $G/H$ is its Galois group.
Thus normality of an intermediate extension corresponds to normality of its subgroup.
:::

## Showing an extension is Galois

::: {.fact title="The checklist"}
**Irreducibility of $f$:**

- Eisenstein, including after shifting or inverting.

- A primitive polynomial in $\ZZ[x]$ whose reduction modulo a prime $p$ has the same degree and is irreducible is irreducible over $\QQ$ and $\ZZ$.

- A quadratic with no root in the field is irreducible.

**Separability of $f$:**

- Factor and exhibit distinct roots in $\bar k$.

- Over a perfect field, irreducible implies separable.

- For irreducible $f$: separable exactly when $f' \not\equiv 0$.

**Separability of the extension:**

- A splitting field of a separable polynomial is separable and normal, hence Galois.

- Algebraic extensions of perfect fields are separable, so in characteristic zero only normality needs checking.

- Other criteria: $[L:k]_s = [L:k]$, or the permanence properties of separability as a distinguished class.

**Normality:**

- Show $L/k$ is finite and the splitting field of some polynomial.

**Galois:**

- Normal and separable, equivalently the splitting field of a separable polynomial.

- Automatic for a finite extension of finite fields, being the splitting field of $x^{p^n}-x$.
:::

## Irreducibility in practice

[[PR-PB6UE]]

::: {.remark}
Over a finite field, irreducibility can be checked by division by the monic irreducible polynomials of degree at most half the degree of $f$.
:::

::: {.example title="Irreducibility mod $p$"}
$f(x) \da x^4 + x + 1$ is irreducible over $\ZZ[x]$: mod $2$, neither $0$ nor $1$ is a root so there is no linear factor, and dividing by each $a_1x^2+a_2x+a_3$ with $a_i \in \ts{0,1}$ leaves a remainder, so there is no quadratic factor.
:::

[[T-CF6S3]]

[[FT-2P5VV]]

::: {.remark title="Shifting"}
If $a\in\QQ$ and $f(x+a)$ is irreducible over $\QQ$ by Eisenstein's criterion, then $f$ is irreducible: substitution $x\mapsto x+a$ is an automorphism of $\QQ[x]$, with inverse $x\mapsto x-a$.
:::

[[T-AILFB]]
