---
schema: qual/card@1
id: D-KC4BS
kind: definition
title: Moore space
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $G$ be an abelian group and $n\geq 1$.
A \dfn{Moore space} $M(G, n)$ is a [[D-ZOU5G|CW complex]] $X$ with
$$
\tilde H_i(X;\ZZ)\cong
\begin{cases}
G & i = n, \\
0 & i\neq n.
\end{cases}
$$
:::

::: {.proposition}
For every abelian group $G$ and $n\geq 1$ a Moore space $M(G, n)$ exists.
Choose a free resolution $0\to F_1\mapsvia{\varphi} F_0\to G\to 0$ with a basis $(a_\alpha)_{\alpha}$ of the free abelian group $F_0$ and a basis $(b_\beta)_{\beta}$ of the free abelian group $F_1$; such a resolution exists because every subgroup of a free abelian group is free.
Let $X^n\coloneqq\bigvee_\alpha S^n_\alpha$ be a [[D-IGUUS|wedge]] of $n$-spheres, one for each $a_\alpha$, and identify $H_n(X^n;\ZZ)$ with $F_0$ by sending the class of $S^n_\alpha$ to $a_\alpha$.
For each $\beta$, attach an $(n+1)$-cell $e^{n+1}_\beta$ along a map $f_\beta\colon S^n\to X^n$ with $(f_\beta)_*[S^n] = \varphi(b_\beta)$, which exists because the Hurewicz map $\pi_n(X^n)\to H_n(X^n;\ZZ)$ is surjective; composed with the collapse $X^n\to S^n_\alpha$, the map $f_\beta$ has degree equal to the $a_\alpha$-coordinate of $\varphi(b_\beta)$.
The resulting CW complex $X$ has cellular chain complex $0\to F_1\mapsvia{\varphi}F_0\to 0$ in degrees $n+1$ and $n$, so $\tilde H_n(X;\ZZ)\cong\coker\varphi\cong G$ and $\tilde H_{n+1}(X;\ZZ)\cong\ker\varphi = 0$ [@Hat02].
:::

::: {.example}
The sphere $S^n$ is an $M(\ZZ, n)$.
For $m\geq 2$, the space $S^n\cup_m e^{n+1}$ obtained by attaching an $(n+1)$-cell to $S^n$ along a map $S^n\to S^n$ of degree $m$ is an $M(\ZZ/m, n)$.
:::

::: {.concept}
See [@Hat02].
:::
