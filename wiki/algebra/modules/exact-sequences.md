---
title: Exact sequences and tensor products
order: 30
topics:
- Exact Sequences
- Tensor Products
- Homological Algebra
---

# Exact sequences and tensor products

## Exact sequences

[[D-BJYH3]]

[[D-3JJJN]]

[[PR-OODAV]]

::: {.remark title="Sufficient conditions for splitting"}
A short [[D-BJYH3|exact sequence]] $0\to A\xrightarrow{f} B\xrightarrow{g} C\to 0$ of $R$-modules splits, and then $B \cong A\oplus C$, if $C$ is projective or if $A$ is injective.
Every free module is projective, so the sequence splits when $C$ is free.
Over a PID, applied to $0\to M_t\to M\to M/M_t\to 0$ with $M/M_t$ free, this splits off the free part of a finitely generated module $M$.
:::

## Tensor products

::: {.proposition}
For positive integers $m$ and $n$, $\ZZ/m \tensor_\ZZ \ZZ/n \cong \ZZ/\gcd(m,n)$.
In particular $\ZZ/2 \tensor_\ZZ \ZZ/3 = 0$.
:::

::: {.proof}
Tensoring the exact sequence $\ZZ \xrightarrow{n} \ZZ \to \ZZ/n \to 0$ with $\ZZ/m$ gives, by right exactness, the exact sequence $\ZZ/m \xrightarrow{n} \ZZ/m \to \ZZ/n\tensor_\ZZ \ZZ/m \to 0$.
Hence $\ZZ/n\tensor_\ZZ\ZZ/m \cong (\ZZ/m)/n(\ZZ/m) \cong \ZZ/\gcd(m,n)$.
:::

::: {.remark title="Right exactness"}
For every $R$-module $M$, the functor $-\tensor_R M$ is right exact, and it is exact if and only if $M$ is flat.
Multiplication by $2$ on $\ZZ$ is injective, and tensored with $\ZZ/2$ it is the zero map on $\ZZ/2$, which is not injective; the kernel is $\Tor_1^\ZZ(\ZZ/2,\ZZ/2)\cong\ZZ/2$.
:::
