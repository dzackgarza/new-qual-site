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

By Maschke's theorem, every finite-dimensional complex representation of a finite group is a direct sum of irreducible representations; by Schur's lemma, a homomorphism of representations between irreducible representations is zero or an isomorphism, and over $\CC$ every endomorphism of an irreducible representation is a scalar.

[[D-FHUV5]]

## Maschke's theorem

[[T-PIO2B]]

::: {.remark title="Hypotheses and proof"}
So $k[G]$ is semisimple, and a finite-dimensional complex representation is determined up to isomorphism by the multiplicities of its irreducible summands.

If $\operatorname{char}k = p$ divides $\size G$, the conclusion can fail: the regular representation of $\ZZ/p$ over $\FF_p$ is indecomposable and not irreducible.
If $G$ is infinite, the conclusion can fail: $\ZZ$ acting on $\CC^2$ by $n\mapsto\matt{1}{n}{0}{1}$ has the invariant line $\CC e_1$ and no invariant complement.

For a subrepresentation $W\subseteq V$, choose any linear projection $\pi\colon V\to W$ and set $\pi_G \definedas {1\over\size G}\sum_{g\in G} g\pi \inverseof{g}$.
Then $\pi_G$ is a $G$-equivariant projection onto $W$, and $\ker\pi_G$ is a $G$-invariant complement of $W$; the division by $\size G$ uses the hypothesis on the characteristic.
:::

## Schur's lemma

[[T-YHH3M]]

::: {.remark title="Proof"}
For irreducible representations $V$ and $W$ of $G$, every $G$-equivariant linear map $V\to W$ is zero or an isomorphism, because its kernel and image are subrepresentations.
For $f\in\Endo_G(V)$ with $V$ finite-dimensional over an algebraically closed field, $f$ has an eigenvalue $\lambda$, and $f - \lambda I$ is a $G$-equivariant map with nonzero kernel, hence zero.

For irreducible complex representations, $\dim \Hom_G(V,W)=0$ if $V\not\cong W$ and $\dim \operatorname{End}_G(V)=1$; together with Maschke's theorem, these give the character orthogonality relations and the multiplicity formula.
:::

## Consequences

Let $V_1,\ldots,V_r$ be the irreducible complex representations of $G$ up to isomorphism, with $d_i = \dim V_i$.
Then $\CC[G] \cong \bigoplus_i \operatorname{End}(V_i) \cong \bigoplus_i \Mat_{d_i}(\CC)$, so
$$
\size G = \sum_i d_i^2,
$$
and $r$ equals the number of conjugacy classes of $G$.

::: {.example}
$S_3$ has three conjugacy classes and order $6$; its two degree-one representations are the trivial and sign representations, so $6 = 1 + 1 + d_3^2$ gives $d_3=2$.
:::
