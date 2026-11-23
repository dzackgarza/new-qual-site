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
Let $C$ be a smooth projective curve of genus $g$ over an algebraically closed field, and let $d \geq 1$ and $r \geq 0$ be integers with $g-d+r \geq 0$.
The locus $W^r_d(C) \subseteq \Pic^d(C)$ of line bundles $L$ with $h^0(C, L) \geq r + 1$ is a closed subscheme, cut out locally as a degeneracy locus of a map of vector bundles.
Its expected dimension is the \dfn{Brill--Noether number}
$$\rho(g, r, d) = g - (r+1)(g - d + r).$$
The curve $C$ is \dfn{Brill--Noether general} if for every such $r$ and $d$, $W^r_d(C)$ is empty when $\rho(g,r,d) < 0$ and has dimension $\rho(g,r,d)$ when $\rho(g,r,d) \geq 0$.
:::

::: {.theorem title="Brill--Noether"}
Work over $\CC$. Let $g$ be the genus of a smooth projective curve $C$, let $d$ and $r$ be as in the definition (in particular $d \geq 1$, $r \geq 0$ and $r \geq d-g$), and put $\rho=\rho(g,r,d)$.

1. If $\rho \geq 0$, then $G^r_d(C)$, and hence $W^r_d(C)$, is nonempty. Every component of $G^r_d(C)$ has dimension at least $\rho$; if $r \geq d-g$, every component of $W^r_d(C)$ also has dimension at least $\rho$ (Kempf and Kleiman--Laksov; Arbarello--Cornalba--Griffiths--Harris, *Geometry of Algebraic Curves, Volume I*, Chapter V, Existence Theorem (1.1)).

2. If $C$ is general and $\rho<0$, then $G^r_d(C)$, and hence $W^r_d(C)$, is empty; if $\rho \geq 0$, then $G^r_d(C)$ is reduced of pure dimension $\rho$ (Griffiths--Harris; Arbarello--Cornalba--Griffiths--Harris, *Geometry of Algebraic Curves, Volume I*, Chapter V, Dimension Theorem (1.5)).

3. For a general $C$ the locus $G^r_d(C)$ is smooth of dimension $\rho$ (Arbarello--Cornalba--Griffiths--Harris, *Geometry of Algebraic Curves, Volume I*, Chapter V, Smoothness Theorem (1.6)), which is the hypothesis of Proposition (4.4) of Chapter IV; that proposition and Lemma (3.5) of the same chapter then give that $W^r_d(C)$ is Cohen--Macaulay, reduced and normal of pure dimension $\rho$, that $W^r_d(C)\setminus W^{r+1}_d(C)$ is smooth of dimension $\rho$, and that for $d<g+r$ the singular locus of $W^r_d(C)$ is $W^{r+1}_d(C)$.

4. So a general curve of genus $g$ is Brill--Noether general in the sense of the definition above: $W^r_d(C)$ is empty when $\rho<0$ and of dimension $\rho$ when $\rho \geq 0$, the second reading following from the dimension statement of item 3 and not from the Dimension Theorem alone, which concerns $G^r_d(C)$.
:::

::: {.remark}
The field is $\CC$ in all three statements, and no more general field is claimed.
:::

::: {.example}
A $g^1_d$ has $\rho(g,1,d) = 2d - g - 2$, which is nonnegative exactly when $d\ge\lceil(g+2)/2\rceil=\lfloor(g+3)/2\rfloor$.
So over $\CC$ the existence theorem gives a $g^1_d$ with $d=\lfloor(g+3)/2\rfloor$ on every curve of genus $g$, and after removing the base divisor of that pencil every curve of genus $g$ has a map to $\PP^1$ of degree at most $\lfloor(g+3)/2\rfloor$.
A general curve has no $g^1_d$ for $d$ below that bound, because $\rho(g,1,d)<0$ there and a Brill--Noether general curve has no linear system of negative expected dimension; its gonality is exactly $\lfloor(g+3)/2\rfloor$.
For $d = 2$, $\rho = 2 - g$, which is negative for $g \geq 3$; this is why every curve of genus $2$ is hyperelliptic while the general curve of genus $g \geq 3$ is not.
:::
