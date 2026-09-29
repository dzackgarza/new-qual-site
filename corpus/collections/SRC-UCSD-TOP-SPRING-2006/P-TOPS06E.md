---
schema: qual/card@1
id: P-TOPS06E
kind: problem
title: "Mod 2 cohomology ring of RP^n with RP^k collapsed to a point"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
  - Projective Spaces
  - Quotient Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
Let $X(n, k) = \mathbb{RP}^n / \mathbb{RP}^k$ denote the quotient space of $\mathbb{RP}^n$ obtained by identifying $\mathbb{RP}^k$ to a point for $0 < k < n$.
Calculate the mod $2$ cohomology ring of $X(2k+2, k)$.
:::

::: {.solution}
Write $N=2k+2$, let $q:\RP^N\to X(N,k)=\RP^N/\RP^k$, and use coefficients $\mathbf F_2$ throughout.

::: pf

::: pf-step

The mod-$2$ cohomology of $\RP^N$ is
$$
H^*(\RP^N;\mathbf F_2)=\mathbf F_2[x]/(x^{N+1}),\qquad |x|=1.
$$

::: pf-proof

This is the standard cellular computation of the cohomology ring of real projective space.

:::

:::

::: pf-step

For every $i>0$, the quotient identifies
$$
\widetilde H^i(X(N,k);\mathbf F_2)\cong H^i(\RP^N,\RP^k;\mathbf F_2),
$$
and under $q^*$ its image in $H^i(\RP^N;\mathbf F_2)$ is the kernel of restriction to $\RP^k$.

::: pf-proof

For a CW pair $(Y,A)$, reduced cohomology of $Y/A$ is naturally relative cohomology $H^*(Y,A)$. In the long exact sequence of $(\RP^N,\RP^k)$, the map to absolute cohomology has image equal to the kernel of restriction to $\RP^k$.

:::

:::

::: pf-step

Hence $q^*$ is injective, is an isomorphism in degree $0$, and in positive degrees has image
$$
(x^{k+1})=\operatorname{span}_{\mathbf F_2}\{x^{k+1},x^{k+2},\dots,x^N\}.
$$
Thus, as a unital graded ring,
$$
H^*(X(N,k);\mathbf F_2)\cong \mathbf F_2\cdot1\ \oplus\ (x^{k+1})
$$
with multiplication inherited from $\mathbf F_2[x]/(x^{N+1})$ on the positive-degree ideal.

::: pf-proof

The restriction $H^i(\RP^N)\to H^i(\RP^k)$ sends $x^i$ to $x^i$. It is an isomorphism for $0\le i\le k$ and the target vanishes for $i>k$. The relative long exact sequence therefore gives no positive-degree classes below $k+1$ and one class $x^i$ in each degree $k+1\le i\le N$. Since $X(N,k)$ is connected, $H^0(X(N,k))=\mathbf F_2$, and $q^*$ sends its unit to the unit.

:::

:::

::: {.pf-step #s4}

For $N=2k+2$, the only nonzero product of two positive-degree classes is
$$
(x^{k+1})^2=x^{2k+2}.
$$

::: pf-proof

A product $x^i x^j=x^{i+j}$ with $i,j\ge k+1$ can be nonzero only if $i+j\le2k+2$. This forces $i=j=k+1$.

:::

:::

::: pf-step

Equivalently, if $a$ denotes the class of degree $k+1$ and $y_i$ the class of degree $i$ for $k+2\le i\le2k+1$, then
$$
\boxed{
H^*(X(2k+2,k);\mathbf F_2)
\cong
\mathbf F_2[a,y_{k+2},\ldots,y_{2k+1}]
/\bigl(a^3,\ a y_i,\ y_i y_j\bigr),
}
$$
where $|a|=k+1$, $|y_i|=i$, and $a^2$ is the nonzero top class in degree $2k+2$.

::: pf-proof

The presentation has basis $1,a,y_{k+2},\dots,y_{2k+1},a^2$, exactly one basis class in degrees $0,k+1,k+2,\dots,2k+2$, and step [](#s4){.pf-ref} gives precisely the stated multiplication relations.

:::

:::

:::

:::
