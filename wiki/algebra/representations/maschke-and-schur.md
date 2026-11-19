---
title: Maschke and Schur
order: 10
topics:
- Representation Theory
- Group Rings
- Convolution
- Function Spaces
---

# Maschke and Schur

The two theorems make the category of finite-dimensional representations of a finite group over $\CC$ semisimple: every representation splits into irreducibles, and between non-isomorphic irreducibles there are no maps other than zero.

[[D-FHUV5]]

## Maschke's theorem

[[T-PIO2B]]

Both hypotheses are needed, and each has its standard failure.

::: {.example title="Two failures of semisimplicity"}
If $\operatorname{char}k = p$ divides $\size G$, the conclusion can fail: the regular representation of $\ZZ/p$ over $\FF_p$ is indecomposable and not irreducible.

If $G$ is infinite, the conclusion can fail: $\ZZ$ acting on $\CC^2$ by $n\mapsto\matt{1}{n}{0}{1}$ has the invariant line $\CC e_1$ and no invariant complement.
:::

## Schur's lemma

[[T-YHH3M]]

For irreducible complex representations the consequence is a dimension count: $\dim\Hom_G(V,W)=0$ when $V\not\cong W$ and $\dim\Endo_G(V)=1$.

[[P-2JVYE]]

## Consequences

The group algebra is the product of the endomorphism algebras of the irreducible representations, which gives the degree and class-number counts.

[[P-UIXFV]]

[[P-ZVXTG]]

[[P-MD6VX]]

::: {.example}
$S_3$ has three conjugacy classes and order $6$; its two degree-one representations are the trivial and sign representations, so $6 = 1 + 1 + d_3^2$ gives $d_3=2$.
:::
