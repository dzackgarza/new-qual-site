---
title: Characters
order: 20
topics:
- Character Theory
---

# Characters

Throughout, $G$ is a finite group and representations are finite-dimensional over $\CC$.

[[D-CTAKB]]

::: {.remark title="Characters determine representations"}
The character $\chi_V(g) \da \tr\rho_V(g)$ determines $V$ up to isomorphism: by [[T-PIO2B|Maschke's theorem]] $V$ is a direct sum of irreducible representations, and by [[T-YHH3M|Schur's lemma]] and the orthogonality relations the multiplicity of each irreducible summand is an inner product of characters.

- $\chi_V$ is a class function, since the trace is invariant under conjugation.
- $\chi_V(1) = \dim V$.
- $\chi_{V\oplus W} = \chi_V + \chi_W$ and $\chi_{V\tensor W} = \chi_V\chi_W$.
:::

## Orthogonality

For representations $V$ and $W$,
$$
\inner{\chi_V}{\chi_W} \da {1\over\size G}\sum_{g\in G} \chi_V(g)\overline{\chi_W(g)} = \dim \Hom_G(V,W),
$$
and the irreducible characters form an orthonormal basis of the space of class functions on $G$.
Consequently:

- $V$ is irreducible if and only if $\inner{\chi_V}{\chi_V} = 1$.
- The multiplicity of an irreducible $V_i$ as a summand of $W$ is $\inner{\chi_W}{\chi_{V_i}}$.

## Building a character table

1. The number of irreducible characters equals the number of conjugacy classes, so the character table is square.
2. The degree-one characters are the characters of the abelianization $G/[G,G]$, pulled back to $G$; they include the trivial character, and for $S_n$ the sign character.
3. The degrees $d_i$ of the irreducible characters divide $\size G$ and satisfy $\size G = \sum_i d_i^2$.
4. For an action of $G$ on a finite set $X$, the permutation character is $\chi(g) = \size{\Fix(g)}$; if the action is $2$-transitive, then $\chi-\chi_{\text{triv}}$ is irreducible.
5. The remaining entries are determined by the column orthogonality relations $\sum_i \chi_i(g)\overline{\chi_i(h)} = \size{C_G(g)}$ if $g$ and $h$ are conjugate and $0$ otherwise; for $g=h=1$ this is $\size G = \sum_i d_i^2$.

::: {.remark title="Permutation characters and Burnside's lemma"}
For the permutation character $\chi(g) = \size{\Fix(g)}$ of an action on $X$, Burnside's lemma states that the number of orbits is $\inner{\chi}{\chi_{\text{triv}}}$; see [[algebra/group-actions/the-class-equation|The class equation]].
:::
