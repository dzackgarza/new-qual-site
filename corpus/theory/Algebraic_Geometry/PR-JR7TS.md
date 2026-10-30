---
schema: qual/card@1
id: PR-JR7TS
kind: proposition
title: A hypersurface of equation-degree $d$ has degree $d$
slogan: 'For a projective hypersurface, equation degree, Hilbert-polynomial degree, and intersection-theoretic degree all equal $d$.'
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
Let $k$ be a field, let $f \in k[x_0,\ldots,x_n]$ be a nonzero homogeneous irreducible polynomial of degree $d$, and let $X = V(f) \subseteq \PP_k^n$.
Then $\deg X = d$.
:::

::: {.proof}
Put $S=k[x_0,\ldots,x_n]$. Since $S$ is a domain and $f\ne0$, multiplication by $f$ gives a graded exact sequence
$$
0 \to S(-d) \xrightarrow{\; \cdot f \;} S \to S/(f) \to 0 ,
$$
and hence, for $r\gg0$,
$$
P_X(r) = \binom{r+n}{n} - \binom{r-d+n}{n} ,
$$
whose degree is $n-1$ and whose leading coefficient is $d/(n-1)!$. By [[D-L6ERW]], the degree of the $(n-1)$-dimensional projective variety $X$ is $(n-1)!$ times this leading coefficient, hence $\deg X=d$.
:::

::: {.theorem title="Degree of a hypersurface section"}
Let $Y \subseteq \PP^n$ be a projective variety of dimension $\geq 1$ and $H$ a hypersurface not containing $Y$, with $Y \cap H = Z_1 \cup \cdots \cup Z_s$ the irreducible components.
Then
$$
\sum_{j=1}^s i(Y, H; Z_j) \deg Z_j = (\deg Y)(\deg H) ,
$$
where $i(Y, H; Z_j)$ is the intersection multiplicity along $Z_j$.
For distinct plane curves $Y, Z \subseteq \PP^2$ of degrees $d$ and $e$ with no common component, $\sum_{P \in Y \cap Z} i(Y, Z; P) = de$ (Bézout).
[@Har77, Theorem I.7.7]
:::

::: {.remark}
If $n\geq2$, then after base change to an algebraic closure a general line $L\subseteq\PP^n$ meets the hypersurface $X$ in a zero-dimensional scheme of length $d$. This is the intersection-theoretic form of the same equality, since Bézout gives
$$
\deg(X\cap L)=(\deg X)(\deg L)=d.
$$
:::
