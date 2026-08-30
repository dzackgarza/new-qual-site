---
title: Characters
order: 20
problems:
  topics:
  - Character Theory
---

# Characters

[[D-CTAKB]]

:::{.remark title="Why a trace is enough"}
The character $\chi_V(g) \da \tr\rho_V(g)$ forgets almost everything about $\rho_V$ and still determines it up to isomorphism, because Maschke makes a representation a list of multiplicities and Schur makes those multiplicities inner products of characters.

Three properties that make it computable:

- $\chi_V$ is a class function, since trace is conjugation invariant.
- $\chi_V(1) = \dim V$.
- $\chi_{V\oplus W} = \chi_V + \chi_W$ and $\chi_{V\tensor W} = \chi_V\chi_W$.

:::

## Orthogonality

\[
\inner{\chi_V}{\chi_W} \da {1\over\size G}\sum_{g\in G} \chi_V(g)\overline{\chi_W(g)} = \dim \Hom_G(V,W)
,\]
so the irreducible characters are an orthonormal basis for the class functions.
Two consequences do all the work:

- $V$ is irreducible exactly when $\inner{\chi_V}{\chi_V} = 1$.
- The multiplicity of $V_i$ in $W$ is $\inner{\chi_W}{\chi_{V_i}}$.

The second is the entire technique: decompose a representation by computing inner products of its character against the table.

## Building a character table

1. Count conjugacy classes; that is the number of irreducibles, so the table is square.
2. Write down the trivial character, and any obvious ones: the sign character for $S_n$, and the characters of $G/[G,G]$, which are the degree-one ones.
3. Use $\size G = \sum d_i^2$ to pin the remaining degrees.
4. Get one more row from the permutation representation: for $G$ acting on a set $X$, $\chi(g) = \size{\Fix(g)}$, and subtracting the trivial character usually leaves an irreducible.
5. Fill the rest by column orthogonality, which for the identity column is again $\size G = \sum d_i^2$.

:::{.remark title="Where the permutation character comes from"}
$\chi(g) = \size{\Fix(g)}$ is exactly the quantity Burnside's lemma averages, so the number of orbits is $\inner{\chi}{\chi_{\text{triv}}}$.
The character theory and the [[algebra/group-actions/the-class-equation|counting arguments]] are the same computation, which is worth noticing because a problem may be stated in either language.

:::
