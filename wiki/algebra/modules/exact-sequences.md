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

Over a principal ideal domain the sequence $0\to M_t\to M\to M/M_t\to0$ splits, because the quotient is free and a sequence with free last term splits on the right.

[[P-J5GIE]]

## Tensor products

The tensor product of two cyclic groups is cyclic of the order of the greatest common divisor, so it vanishes exactly when the orders are coprime.

[[T-TENSR]]

[[P-I2MBC]]

[[D-B5X33]]

## Exactness of the tensor functor

The functor $-\tensor_R M$ is right exact for every $M$, and it is exact on injections exactly when $M$ is flat.

[[D-FS52P]]

[[PR-KX7L7]]

::: {.remark title="The failure in $\ZZ$-modules"}
Multiplication by $2$ on $\ZZ$ is injective, and tensored with $\ZZ/2$ it is the zero map on $\ZZ/2$, which is not injective; the kernel is the first Tor group $\Tor_1^\ZZ(\ZZ/2,\ZZ/2)\cong\ZZ/2$, which is what the derived functor measures.
:::
