---
schema: qual/card@1
id: PR-JR7TS
kind: proposition
title: A hypersurface of equation-degree $d$ has degree $d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Hilbert Polynomial
  - Hypersurfaces
relations:
- kind: uses
  target: D-L6ERW
review: draft
prompts:
- Show that a hypersurface cut out by a degree-$d$ equation has degree $d$.
---

::: {.proposition}
Let $f \in k[x_0,\ldots,x_n]$ be homogeneous, irreducible, of degree $d$, and let $X = V(f) \subseteq \PP^n$.
Then $\deg X = d$.
:::

::: {.remark}
The proof is the exact sequence
\[
0 \to S(-d) \xrightarrow{\; \cdot f \;} S \to S/(f) \to 0 ,
\]
which is exact because $S$ is a domain and $f \neq 0$, so multiplication by $f$ is injective.
Taking dimensions in degree $r$,
\[
P_X(r) = \binom{r+n}{n} - \binom{r-d+n}{n} ,
\]
a polynomial of degree $n-1$ whose leading coefficient is $d/(n-1)!$.

The statement is the compatibility of two definitions of degree that look unrelated: the degree of the defining equation, and the normalised leading term of the Hilbert polynomial.
The geometric count — the number of points in which $X$ meets a general line — agrees with both, and that is Bezout in the first nontrivial case.
:::
