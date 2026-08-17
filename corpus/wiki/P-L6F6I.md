---
schema: qual/card@1
id: P-L6F6I
kind: problem
title: "Describe all possible covering maps between $S^2, T^2, K$"
classification:
  areas:
  - topology
  topics:
  - covering-spaces
  - surfaces
  - fundamental-group
relations: []
review: draft
solved: true
---
Describe all possible covering maps between $S^2, T^2, K$

:::{.solution}

\envlist
:::{.concept}
\envlist

1. $\tilde X \surjects X$ induces $\pi_1(\tilde X) \injects \pi_1(X)$
2. $\chi(\tilde X) = n \chi (X)$
3. $\pi_n(X) = [S^n, X]$
4. $Y \to X$ with $\pi_1(Y) = 0$ and $\tilde X \homotopic \pt \implies$ every $Y\mapsvia{f} X$ is nullhomotopic.
5. $\pi_*(T^2) = [\ZZ \ast \ZZ, 0\rightarrow]$
6. $\pi_*(K) = [\ZZ \semidirect_{\ZZ_2} \ZZ, 0\rightarrow]$
7. Universal covers are homeomorphic.
8. $\pi_{\geq 2}(\tilde X) \cong \pi_{\geq 2}(X)$

:::

Spaces

- $S^2 \surjects T^2$
- $S^2 \surjects K$
- $K \surjects S^2$
- $T^2 \surjects S^2$
	- All covered by the fact that 
  $$
    \ZZ = \pi_2(S^2) \neq \pi_2(X) = 0
    $$ 
    for $X = T^2, K$.
- $K \surjects T^2$
	- Doesn't cover, would induce $\pi_1(K) \injects \pi_1(T^2) \implies \ZZ\semidirect \ZZ \injects \ZZ^2$ but this would be a non-abelian subgroup of an abelian group.
- $T^2 \surjects K$
  - ?

:::{.remark}
Not complete!
:::

:::
