---
schema: qual/card@1
id: D-CRVBRILLNOETHER
kind: definition
title: The Brill--Noether number, and Brill--Noether general curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Brill-Noether Theory
  - Linear Systems
  - Curves
relations:
- kind: uses
  target: D-CRVGON
- kind: related-to
  target: D-CRVHYP
review: draft
prompts:
- What is a Brill--Noether curve?
- What is the Brill--Noether theorem?
---

::: {.definition title="Brill--Noether number"}
Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field, and let $r \geq 0$ and $d$ satisfy $g - d + r \geq 0$.
The locus $W^r_d(C) \subseteq \Pic^d(C)$ of line bundles $L$ with $h^0(C, L) \geq r + 1$ is a closed subscheme, cut out locally as a degeneracy locus of a map of vector bundles.
Its expected dimension is the \dfn{Brill--Noether number}
$$\rho(g, r, d) = g - (r+1)(g - d + r).$$
The curve $C$ is \dfn{Brill--Noether general} if for every such $r$ and $d$, $W^r_d(C)$ is empty when $\rho(g,r,d) < 0$ and has dimension $\rho(g,r,d)$ when $\rho(g,r,d) \geq 0$.
:::

::: {.theorem title="Brill--Noether"}
Let $g$, $r$, $d$ be as above.

1. If $\rho(g,r,d) \geq 0$, then every smooth projective curve of genus $g$ has a $g^r_d$, and every component of $W^r_d(C)$ has dimension at least $\rho(g,r,d)$ (Kempf, Kleiman--Laksov).

2. A general curve of genus $g$ is Brill--Noether general (Griffiths--Harris).

3. For a general curve and $\rho(g,r,d) \geq 0$, $W^r_d(C) \setminus W^{r+1}_d(C)$ is smooth of dimension $\rho(g,r,d)$ (Gieseker--Petri).
:::

::: {.example}
A $g^1_d$ has $\rho(g,1,d) = 2d - g - 2$.
So every curve of genus $g$ has a map of degree $\lceil (g+2)/2 \rceil$ to $\PP^1$, and the general curve has no map of smaller degree: its gonality is $\lfloor (g+3)/2 \rfloor$.
For $d = 2$, $\rho = 2 - g$, which is negative for $g \geq 3$; this is why every curve of genus $2$ is hyperelliptic while the general curve of genus $g \geq 3$ is not.
:::
