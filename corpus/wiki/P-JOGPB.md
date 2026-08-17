---
schema: qual/card@1
id: P-JOGPB
kind: problem
title: "Assume $f$ is continuous in the region: $0 < \\abs{z-a} \\leq R,\\quad 0 \\leq \\Arg(z-a) \\leq \\beta_0 \\qquad \\beta_0\\in (0, 2\\pi]$"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - laurent-series
  - poles
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Assume $f$ is continuous in the region:
\[
0 < \abs{z-a} \leq R,\quad 0 \leq \Arg(z-a) \leq \beta_0 \qquad \beta_0\in (0, 2\pi]
.\]

and the following limit exists:
\[
\lim_{z\to a}(z-a)f(z) = A
.\]
Show that
$$\lim_{r \rightarrow 0} \int_{\gamma_r} f(z) dz  = i A \beta_0 \; , \; \;$$
where
\[
\gamma_r : = \{ z \; | \; z = a + r e^{it}, \; 0 \leq  t \leq \beta_0 \}.
.\]
:::

:::{.problem title="Alternative version"}
Let $f$ be a continuous function in the region
$$
D=\{z \suchthat  \abs{z}>R, 0\leq \arg z\leq \theta\}\quad\text{where}\quad 1\leq \theta \leq 2\pi
.$$ 
If there exists $k$ such that
$\displaystyle{\lim_{z\to\infty} zf(z)=k}$ for $z$ in the region $D$.
Show that 
$$
\lim_{R'\to\infty} \int_{L} f(z) dz=i\theta k
,$$ 
where $L$ is the part of the circle $|z|=R'$ which lies in the region $D$.

:::

:::{.solution}
Without loss of generality take $a=0$.
Since $zf(z) \to A$ as $z\to 0$, $z=0$ is a simple pole of $f$ and we can write $f(z) = c_{-1}z\inv + c_0 + c_1z + \cdots$.
Then
\[
\int_{\gamma_r} f(z)\dz 
&= \int_{\gamma_r} \sum_{k\geq -1} c_k z^k \dz \\
&= \sum_{k\geq -1} c_k \int_{\gamma_r} z^k \dz \\
&= c_{-1}\int_{\gamma_r}{1\over z}\dz \\
&= c_{-1}\int_{0}^{\beta_0} {1\over re^{i t}} ire^{it} \dt \qquad z= re^{it}, \dz = ire^{it} \dt \\
&= i c_{-1}\int_{0}^{\beta_0} \dt \\
&= i c_{-1}\beta_0
.\]
Now use that
\[
zf(z) = c_{-1} + c_0z + \cdots \convergesto{z\to 0} c_{-1} = A
,\]
so the integral is $iA\beta_0$.
:::
