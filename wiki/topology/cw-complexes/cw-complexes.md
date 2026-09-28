---
order: 225
topics:
- CW Complexes
- Cell Complexes
- Simplicial Complexes
- Euler Characteristic
---

# CW and simplicial complexes

The cellular chain complex of a [[D-ZOU5G|CW complex]] $X$ has differentials lowering degree:
$$
C_*(X) = \qty{0 \leftarrow C_0 \xleftarrow{\ \del_1\ } C_1 \xleftarrow{\ \del_2\ } C_2 \leftarrow \cdots }.
$$

[[PR-QJZDT]]

::: {.remark}
For singular chains the corresponding statement is the Eilenberg--Zilber theorem: $C_*(X\cross Y)$ is naturally chain homotopy equivalent to $C_*(X)\tensor_\ZZ C_*(Y)$.

:::

::: {.example}
Let $X= S^a \cross S^b$ with $a,b\geq 1$ and the product of the CW structures $e^0\union e^a$ and $e^0\union e^b$.
Then $p_{S^a}(t) = 1 + t^a$ and $p_{S^b}(t) = 1 + t^b$, so $p_X(t) = 1 + t^a + t^b + t^{a+b}$, and $X$ has one $0$-cell, one $a$-cell, one $b$-cell, and one $(a+b)$-cell.

:::

[[E-GTNVU]]

## CW structures on common spaces

::: {.example title="Spheres"}
For $n\geq 1$, $S^n = e^0 \union e^n$, a $0$-cell and an $n$-cell attached by the constant map $\del D^n\to e^0$.
Another CW structure on $S^n$ has two $k$-cells for each $0\leq k \leq n$, the $k$-skeleton being $S^k$ and the two $k$-cells its hemispheres.

:::

::: {.example title="Real projective space"}
$\RP^n = e^0\union e^1 \union e^2 \union \cdots \union e^n$, one cell in each dimension $0,\ldots,n$, with $e^k$ attached by the double cover $S^{k-1}\to\RP^{k-1}$.

:::

::: {.example title="Complex projective space"}
$\CP^n = e^0\union e^2 \union e^4 \union \cdots \union e^{2n}$, with $e^{2k}$ attached by the quotient map $S^{2k-1}\to\CP^{k-1}$.

:::

::: {.example title="Surfaces"}
A closed surface given by a polygon with edge identifications has one $2$-cell, one $1$-cell for each edge pair, and one $0$-cell for each vertex class.

![Fundamental domains](../../../../assets/assets/Topology/figures/1513064067523.png)

:::

## Simplicial complexes

::: {.remark}
With the vertices labelled by integers, a simplicial complex is determined by its list of simplices, each $n$-simplex being recorded as the set of the $n+1$ labels of its vertices.

:::

::: {.example title="Torus"}
![Torus](../../../../assets/assets/Topology/figures/1513062466927.png)

:::

::: {.example title="Klein bottle and $\RP^2$"}
![Klein Bottle and $\RP^2$](../../../../assets/assets/Topology/figures/1513062526623.png)

:::

::: {.example title="A labelling of the torus that is not a triangulation"}
![Not a Torus](../../../../assets/assets/Topology/figures/1513062599096.png)

In this picture a triangle has two vertices with the same label $1$, so the vertex set $\ts{1,2}$ does not determine a unique triangle, and the picture is not a simplicial complex.

:::

## Cellular homology

::: {.fact title="Computing cellular homology"}
Let $X$ be a CW complex with finitely many cells in each dimension.

1. The cellular chain group $C_n$ is free abelian on the $n$-cells $e^n_\alpha$.

2. The differential is
$$
\del_n(e_{\alpha}^n) = \sum_{\beta} d_{\alpha\beta}\, e_{\beta}^{n-1},
$$
where $d_{\alpha\beta}$ is the degree of the composite $S^{n-1} \to X^{(n-1)} \to X^{(n-1)}/\qty{X^{(n-1)}\sm e^{n-1}_\beta}\cong S^{n-1}$ of the attaching map of $e^n_\alpha$ with the map collapsing the complement of $e^{n-1}_\beta$.
For a smooth map $S^{n-1}\to S^{n-1}$ and a regular value $y$, the degree is the number of points of the preimage of $y$ counted with sign $+1$ where the map preserves orientation and $-1$ where it reverses it.

3. If $X$ has a single $0$-cell, then $\del_1 = 0$.
If $X$ has no $n$-cells, then $H_n(X) = 0$.

4. With bases of cells, $\del_n\colon \ZZ^{m} \to \ZZ^{k}$ is a $k\times m$ integer matrix, and $H_n(X) = \ker\del_n/\im\del_{n+1}$.

5. If the Smith normal form of $\del_{n+1}$ has nonzero diagonal entries $d_1,\ldots,d_r$, and $\ker\del_n$ has rank $s$, then
$$
H_n(X)\cong \ZZ^{s-r}\oplus\bigoplus_{i=1}^r \ZZ/d_i.
$$

:::

::: {.example title="A kernel from reduced row echelon form"}
The integer matrix with reduced row echelon form
$$
\begin{pmatrix}
1&2&0&2\\0&0&1&-1\\0&0&0&0
\end{pmatrix},
$$
viewed as a map $\ZZ^4\to\ZZ^3$ on coordinates $(x_1,x_2,x_3,x_4)$, has kernel given by $x_1=-2x_2-2x_4$ and $x_3=x_4$, with basis
$$
\ker = \gens{(2,-1,0,0),\ (2,0,-1,-1)}.
$$
Its rows span the image of the transpose, $\gens{(1,2,0,2),(0,0,1,-1)}\subseteq\ZZ^4$.

:::

## Constructing a CW complex with prescribed homology

::: {.proposition}
For finitely generated abelian groups $G_1, G_2, \ldots$, there is a connected CW complex $X$ with $H_n(X)\cong G_n$ for all $n\geq 1$.

:::

::: {.proof}
By the structure theorem for finitely generated abelian groups, each $G_n$ is a finite direct sum of copies of $\ZZ$ and $\ZZ/d$.
Attaching an $n$-cell to a point gives $S^n$ with $\tilde H_n = \ZZ$ and no other reduced homology.
Attaching an $(n+1)$-cell to $S^n$ along a map of degree $d$ gives a space with $\tilde H_n = \ZZ/d$ and no other reduced homology.
For good pointed spaces $X_i$, $\tilde H_n(\bigvee_i X_i) \cong \bigoplus_i \tilde H_n(X_i)$, so the wedge of these spaces over all summands of all $G_n$ has the required homology.

:::

## Exercises

[[P-EJKY7]]
