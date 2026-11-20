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

Semisimplicity makes the character a complete invariant: a complex representation of a finite group is determined by its irreducible constituents.

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

::: {.fact title="Schur's lemma in dimension form"}
For irreducible complex representations, $\dim\Hom_G(V,W)=0$ when $V\not\cong W$ and $\dim\Endo_G(V)=1$: a $G$-map between irreducibles is either zero or an isomorphism, and a $G$-endomorphism of an irreducible is a scalar by [[T-YHH3M|Schur's lemma]].
:::

[[P-2JVYE]]

## Consequences

[[T-ZOTWN]]

Over $\CC$ each division ring in that decomposition is $\CC$, so the group algebra of a finite group is a product of full matrix algebras, and the degree and class-number counts below are the dimensional bookkeeping of that decomposition.

[[P-UIXFV]]

[[P-ZVXTG]]

[[P-MD6VX]]

::: {.example}
$S_3$ has three conjugacy classes and order $6$; its two degree-one representations are the trivial and sign representations, so $6 = 1 + 1 + d_3^2$ gives $d_3=2$.
:::
