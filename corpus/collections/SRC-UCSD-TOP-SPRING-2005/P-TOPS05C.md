---
schema: qual/card@1
id: P-TOPS05C
kind: problem
title: "Cohomology and homology of RP^2 x RP^3 and Bockstein action"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cohomology
  - Bockstein
  - Projective Spaces
relations: []
review: draft
---

::: {.problem}
(a) Compute the integral and mod $2$ cohomology and homology of $\mathbb{RP}^2 \times \mathbb{RP}^3$.
Is $\mathbb{RP}^2 \times \mathbb{RP}^3$ orientable?

(b) Determine the action of the Bockstein
$$
\beta_1 : H^*(\mathbb{RP}^2 \times \mathbb{RP}^3; \mathbb{Z}_2) \to H^{*+1}(\mathbb{RP}^2 \times \mathbb{RP}^3; \mathbb{Z}_2).
$$
:::

::: {.solution}
<1>1. The integral homology of the two factors is
$$H_*(\mathbb{RP}^2)=\bigl(\mathbb Z,\mathbb Z/2,0\bigr),\qquad
H_*(\mathbb{RP}^3)=\bigl(\mathbb Z,\mathbb Z/2,0,\mathbb Z\bigr).$$
::: {.proof}
This is the standard cellular homology computation for real projective spaces.
:::

<1>2. The integral Künneth theorem gives
$$\boxed{H_k(\mathbb{RP}^2\times\mathbb{RP}^3;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
(\mathbb Z/2)^2,&k=1,\\
\mathbb Z/2,&k=2,\\
\mathbb Z\oplus\mathbb Z/2,&k=3,\\
\mathbb Z/2,&k=4,\\
0,&k=5.
\end{cases}}$$
::: {.proof}
The tensor term $H_1(\mathbb{RP}^2)\otimes H_1(\mathbb{RP}^3)$ contributes $\mathbb Z/2$ in degree $2$; the Tor term $\operatorname{Tor}(\mathbb Z/2,\mathbb Z/2)$ contributes $\mathbb Z/2$ in degree $3$; and $H_1(\mathbb{RP}^2)\otimes H_3(\mathbb{RP}^3)$ contributes $\mathbb Z/2$ in degree $4$.
:::

<1>3. By the integral cohomology universal coefficient theorem,
$$\boxed{H^k(\mathbb{RP}^2\times\mathbb{RP}^3;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
0,&k=1,\\
(\mathbb Z/2)^2,&k=2,\\
\mathbb Z\oplus\mathbb Z/2,&k=3,\\
\mathbb Z/2,&k=4,\\
\mathbb Z/2,&k=5.
\end{cases}}$$
::: {.proof}
Use $0\to\operatorname{Ext}(H_{k-1},\mathbb Z)\to H^k\to\operatorname{Hom}(H_k,\mathbb Z)\to0$ and $\operatorname{Ext}(\mathbb Z/2,\mathbb Z)\cong\mathbb Z/2$.
:::

<1>4. With $\mathbb F_2$ coefficients,
$$H^*(\mathbb{RP}^2\times\mathbb{RP}^3;\mathbb F_2)
\cong \mathbb F_2[x,y]/(x^3,y^4),\qquad |x|=|y|=1,$$
and the mod-$2$ homology dimensions in degrees $0,\dots,5$ are
$$\boxed{1,2,3,3,2,1}.$$
::: {.proof}
For $\mathbb{RP}^m$, mod-$2$ cohomology is $\mathbb F_2[t]/(t^{m+1})$. The field-coefficient Künneth theorem gives the tensor-product ring and the stated Betti numbers.
:::

<1>5. The product is nonorientable.
::: {.proof}
Its top integral homology $H_5$ vanishes by <1>2. Equivalently, the product of a nonorientable manifold with any connected manifold is nonorientable.
:::

<1>6. For the Bockstein associated to
$$0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0,$$
one has
$$\beta_1(x)=x^2,\qquad \beta_1(y)=y^2,$$
and, for every monomial,
$$\boxed{\beta_1(x^iy^j)=(i\bmod2)x^{i+1}y^j+(j\bmod2)x^iy^{j+1}},$$
with terms beyond $x^2$ or $y^3$ understood to vanish.
::: {.proof}
This mod-$2$ Bockstein is $Sq^1$. On the degree-one generator of $H^*(\mathbb{RP}^m;\mathbb F_2)$, $Sq^1(t)=t^2$, and the Cartan formula gives $Sq^1(x^iy^j)=Sq^1(x^i)y^j+x^iSq^1(y^j)$ with $Sq^1(t^r)=r t^{r+1}$ mod $2$.
:::
:::
