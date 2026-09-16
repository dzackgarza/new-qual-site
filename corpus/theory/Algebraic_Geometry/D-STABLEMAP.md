---
schema: qual/card@1
id: D-STABLEMAP
kind: definition
title: Stable maps
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stable Maps
  - Moduli of Curves
  - Gromov--Witten Invariants
relations:
- kind: related-to
  target: T-MGSMOOTH
review: draft
prompts:
- What is a stable map?
---

::: {.definition title="Stable map"}
Let $X$ be a projective variety over $\CC$ and $\beta \in H_2(X, \ZZ)$.
A \dfn{stable map} of genus $g$ with $n$ marked points and class $\beta$ is a tuple $(C; p_1, \ldots, p_n; f)$ where $C$ is a connected projective curve of arithmetic genus $g$ with at worst nodes, $p_1, \ldots, p_n$ are distinct smooth points of $C$, and $f \colon C \to X$ is a morphism with $f_*[C] = \beta$, such that the automorphism group of the tuple is finite.
Equivalently, every irreducible component of $C$ of genus $0$ contracted by $f$ contains at least three special points (nodes or marked points), and every contracted component of genus $1$ contains at least one.
:::

::: {.theorem title="Kontsevich"}
Stable maps are parametrized by a proper Deligne--Mumford stack $\overline{\mathcal{M}}_{g,n}(X, \beta)$.
For $X$ a point it is the moduli stack $\overline{\mathcal{M}}_{g,n}$ of stable marked curves.
:::

::: {.remark}
The Gromov--Witten invariants of $X$ are integrals over the virtual fundamental class of $\overline{\mathcal{M}}_{g,n}(X, \beta)$ of pullbacks of cohomology classes along the evaluation maps $f \mapsto f(p_i)$.
For $X = \PP^2$, $g = 0$ and $\beta = d[\text{line}]$ with $n = 3d - 1$ point classes, the invariant is the number $N_d$ of rational plane curves of degree $d$ through $3d - 1$ general points.
:::
