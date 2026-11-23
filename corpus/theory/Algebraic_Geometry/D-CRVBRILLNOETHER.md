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
Work over $\CC$. Let $g$, $r$, $d$ be as above.

1. If $\rho(g,r,d) \geq 0$, then every smooth projective curve of genus $g$ has a $g^r_d$, and every component of $W^r_d(C)$ has dimension at least $\rho(g,r,d)$ (Kempf, Kleiman--Laksov).

2. A general curve of genus $g$ is Brill--Noether general, so $W^r_d(C)$ is empty when $\rho(g,r,d)<0$ (Griffiths--Harris).

3. For a general curve and $\rho(g,r,d) \geq 0$, $W^r_d(C) \setminus W^{r+1}_d(C)$ is smooth of dimension $\rho(g,r,d)$ (Gieseker--Petri).
:::

::: {.remark}
The three theorems are classical Brill--Noether theory, attributed above by author; no edition of the standard references (Arbarello--Cornalba--Griffiths--Harris, or Griffiths--Harris) is retained in this repository's sources, so they carry no numbered citation here.
The field is $\CC$ in all three, and no more general field is claimed.
:::

::: {.example}
A $g^1_d$ has $\rho(g,1,d) = 2d - g - 2$, which is nonnegative exactly when $d\ge\lceil(g+2)/2\rceil=\lfloor(g+3)/2\rfloor$.
So over $\CC$ the existence theorem gives a $g^1_d$ with $d=\lfloor(g+3)/2\rfloor$ on every curve of genus $g$, and after removing the base divisor of that pencil every curve of genus $g$ has a map to $\PP^1$ of degree at most $\lfloor(g+3)/2\rfloor$.
A general curve has no $g^1_d$ for $d$ below that bound, because $\rho(g,1,d)<0$ there and a Brill--Noether general curve has no linear system of negative expected dimension; its gonality is exactly $\lfloor(g+3)/2\rfloor$.
For $d = 2$, $\rho = 2 - g$, which is negative for $g \geq 3$; this is why every curve of genus $2$ is hyperelliptic while the general curve of genus $g \geq 3$ is not.
:::
