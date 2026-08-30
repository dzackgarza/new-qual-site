---
title: Exact sequences and tensor products
order: 30
problems:
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

:::{.remark title="Why splitting is the question"}
A short exact sequence $0\to A\to B\to C\to 0$ always says $B$ is built from $A$ and $C$; it says $B \cong A\oplus C$ only when it splits.
Two sufficient conditions do nearly all the work on an exam: $C$ projective, and a retraction of the first map.
Free implies projective, so a sequence ending in a free module always splits, which is the step used to peel the free part off a module over a PID.

:::

## Tensor products

:::{.example title="Computing tensor products"}
$\ZZ/2 \tensor_\ZZ \ZZ/3 = 0$.

The general principle: $\ZZ/m \tensor_\ZZ \ZZ/n \cong \ZZ/\gcd(m,n)$, so coprime orders kill the tensor product entirely.
The computation is a right-exactness argument: tensoring the presentation $\ZZ \xrightarrow{n} \ZZ \to \ZZ/n \to 0$ with $\ZZ/m$ gives $\ZZ/m \xrightarrow{n} \ZZ/m \to \ZZ/n\tensor \ZZ/m \to 0$, and multiplication by $n$ on $\ZZ/m$ is surjective when $\gcd(m,n)=1$.

:::

:::{.remark title="Right exact, not exact"}
Tensoring preserves cokernels and not kernels: $-\tensor M$ is right exact for every $M$, and exact exactly when $M$ is flat.
The failure is measured by $\Tor$, and the standard example is $\ZZ \xrightarrow{2} \ZZ$ tensored with $\ZZ/2$, which is the zero map rather than injective.

:::
