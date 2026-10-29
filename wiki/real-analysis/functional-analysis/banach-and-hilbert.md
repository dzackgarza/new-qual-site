---
title: Banach and Hilbert spaces
order: 10
topics:
- Hilbert Spaces
- Norms
---

# Banach and Hilbert spaces

Recall that a [[D-BG455|Banach space]] is a normed space that is complete in its norm, and a [[D-7QQUO|Hilbert space]] is an inner product space that is complete in the norm $\norm x\coloneqq\inner xx^{1/2}$; every Hilbert space is a Banach space.
In a Hilbert space $H$, closed subspaces have orthogonal complements and orthogonal projections.

[[PR-L35O7]]

[[T-5BFVS]]

[[PR-KTZZ5]]

[[T-5AALA]]

[[T-LDCZB]]

[[T-J3AN3]]

::: {.proposition title="Parallelogram law"}
A norm on a vector space is induced by an inner product if and only if it satisfies $\norm{x+y}^2+\norm{x-y}^2 = 2\norm x^2+2\norm y^2$ for all $x, y$.

:::

::: {.example title="$L^p$ is a Hilbert space only for $p=2$"}
Let $E,F$ be disjoint measurable sets with $0<\mu(E),\mu(F)<\infty$, and let $f\coloneqq\chi_E/\norm{\chi_E}_p$ and $g\coloneqq\chi_F/\norm{\chi_F}_p$.
For $1\leq p<\infty$, $\norm{f\pm g}_p = 2^{1/p}$, so the parallelogram law reads $2\cdot2^{2/p} = 4$, which holds only for $p=2$.
For $p=\infty$, $\norm{f\pm g}_\infty=1$ and the law reads $2=4$.
So $L^p(\mu)$ is not a Hilbert space for $p\neq2$ on such a measure space.

:::
