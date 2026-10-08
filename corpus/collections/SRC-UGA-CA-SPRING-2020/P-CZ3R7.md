---
schema: qual/card@1
id: P-CZ3R7
kind: problem
title: $|z-z_1|/|z-z_2|=c$ is a circle
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.problem}
\envlist

a. Prove that if $c>0$,
\[
\abs{w_1} = c\abs{w_2} \implies \abs{w_1 - c^2 w_2} = c\abs{w_1 - w_2}
.\]

b. Prove that if $c>0$ and $c\neq 1$, with $z_1\neq z_2$, then the following equation represents a circle:
\[
\abs{z-z_1 \over z-z_2} = c
.\]
Find its center and radius.

> Hint: use part (a)

:::

::: {.solution}
<1>1. If $|w_1|=c|w_2|$ with $c>0$, then $|w_1-c^2w_2|=c|w_1-w_2|$.

::: {.proof}
Expanding the squared moduli gives
\[
\begin{aligned}
|w_1-c^2w_2|^2
&=|w_1|^2+c^4|w_2|^2-2c^2\operatorname{Re}(w_1\overline{w_2})\\
&=c^2(|w_1|^2+|w_2|^2-2\operatorname{Re}(w_1\overline{w_2}))\\
&=c^2|w_1-w_2|^2.
\end{aligned}
\]
Both sides of the asserted identity are nonnegative; taking square roots proves it.
:::

<1>2. For $c>0$, $c\neq1$, and $z_1\neq z_2$, the locus in part (b) is the circle with center and radius
\[
\boxed{\quad a=\frac{z_1-c^2z_2}{1-c^2},
\qquad r=\frac{c|z_1-z_2|}{|1-c^2|}.\quad}
\]

::: {.proof}
For $z\neq z_2$, the given equation is equivalent to $|z-z_1|=c|z-z_2|$. Apply step <1>1 with $w_1=z-z_1$ and $w_2=z-z_2$ to obtain
\[
|(1-c^2)z-(z_1-c^2z_2)|=c|z_1-z_2|.
\]
Since $1-c^2\neq0$, this is $|z-a|=r$ with the displayed $a,r$. Moreover, $r>0$, and $|z_2-a|=|z_1-z_2|/|1-c^2|\neq r$ because $c\neq1$. Thus the circle excludes $z_2$, where the original quotient is undefined, and the equivalence holds in both directions.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>1 proves part (a), and step <1>2 proves part (b).
:::
:::
