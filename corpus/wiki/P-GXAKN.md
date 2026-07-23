---
schema: qual/card@1
id: P-GXAKN
kind: problem
title: "Define"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Define
$$
f(x, y):=\left\{\begin{array}{ll}{\frac{x^{1 / 3}}{(1+x y)^{3 / 2}}} & {\text { if } 0 \leq x \leq y} \\ {0} & {\text { otherwise }}\end{array}\right.
$$

Carefully show that $f \in L^1(\RR^2)$.
:::

:::{.solution}
Note that

\[
\int_{\RR^2}\abs{f} \dmu 
&= \int_0^\infty \int_x^\infty x^{1\over 3}(1+xy)^{-3\over 2} \dy \dx \\
&= \int_0^\infty -2x^{-{ 2\over 3} }(1+xy)^{-{ 1\over 2} }\evalfrom_{y=x}^{y=\infty} \dx \\
&= \int_0^\infty {2\over x^{2\over 3} (1+x^2)^{1\over 2}}\\
&= \int_0^1 {2\over x^{2\over 3} (1+x^2)^{1\over 2}} + \int_1^\infty {2\over x^{2\over 3} (1+x^2)^{1\over 2}} \\
&=
\int_0^1 {2\over x^{2\over 3} } + \int_1^\infty {2\over x^{5\over 3} } \\
&<\infty
,\]
where 

- For the first term: We've entirely neglected the $1+x^2$ factor, since neglecting to divide by a positive number can only make the integrand larger,
- For the second term:
\[
1+x^2\geq 0 \implies {1\over \sqrt{1+x^2}} \leq {1\over \sqrt{x^2}} = {1\over x}
\]

- Both terms converge by the $p\dash$tests.

The use of iterated integration is justified by Tonelli's theorem on $\abs{f} = f$, since $f$ is non-negative and clearly measurable on $\RR^2$, and if any iterated integral is finite then it is equal to $\int \abs{f}$.

:::

