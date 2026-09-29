---
schema: qual/card@1
id: P-AZOFF-C01
kind: problem
title: Conformal map of the unit disk onto the upper half-plane
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Conformal mapping, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Used the Cayley transform i(1+z)/(1-z). Its imaginary part on the unit
    disk is (1-|z|^2)/|1-z|^2>0, its inverse (w-i)/(w+i) maps the upper
    half-plane back into the disk, and its derivative never vanishes there.
    The source compilation contains no worked solution for this problem.
---

::: {.problem}
Find a conformal map of the unit disk onto the upper half plane.
:::

::: {.solution}
Let
$$
\DD=\{z\in\CC:\abs z<1\},
\qquad
\mathcal H=\{w\in\CC:\operatorname{Im}w>0\},
$$
and define
$$
T(z)=i\frac{1+z}{1-z}.
$$

::: pf

::: {.pf-step #s1}

The map $T$ is holomorphic on $\DD$ and
$$
T(\DD)\subseteq\mathcal H.
$$

::: pf-proof

The only pole of $T$ is at $z=1$, which does not lie in $\DD$, so $T$ is
holomorphic on $\DD$.

For $z\in\DD$,
$$
\begin{aligned}
\operatorname{Im}T(z)
&=
\operatorname{Re}\frac{1+z}{1-z}\\
&=
\operatorname{Re}
\frac{(1+z)(1-\bar z)}{\abs{1-z}^2}\\
&=
\frac{1-\abs z^2}{\abs{1-z}^2}\\
&>
0.
\end{aligned}
$$
Thus $T(z)\in\mathcal H$.

:::

:::

::: {.pf-step #s2}

For every $w\in\mathcal H$, the equation $w=T(z)$ has the unique
solution
$$
z=\frac{w-i}{w+i},
$$
and this solution belongs to $\DD$.

::: pf-proof

Solving
$$
w=i\frac{1+z}{1-z}
$$
for $z$ gives the displayed formula. Since $w\in\mathcal H$, one has
$w\neq-i$, so the denominator is nonzero.

Write
$$
w=u+iv,
\qquad
v>0.
$$
Then
$$
\begin{aligned}
\abs{w+i}^2-\abs{w-i}^2
&=
\bigl(u^2+(v+1)^2\bigr)
-
\bigl(u^2+(v-1)^2\bigr)\\
&=
4v\\
&>
0.
\end{aligned}
$$
Hence
$$
\abs{\frac{w-i}{w+i}}<1,
$$
so $z\in\DD$. The algebraic solution is unique.

:::

:::

::: {.pf-step #s3}

The derivative of $T$ is nowhere zero on $\DD$.

::: pf-proof

Direct differentiation gives
$$
T'(z)=\frac{2i}{(1-z)^2}.
$$
Since $1\notin\DD$, this derivative is nonzero at every point of $\DD$.

:::

:::

::: {.pf-step #s4}

A conformal bijection of the unit disk onto the upper half-plane is
$$
\boxed{
T(z)=i\frac{1+z}{1-z}
}.
$$

::: pf-proof

Step [](#s1){.pf-ref} shows that $T$ maps $\DD$ into $\mathcal H$. Step [](#s2){.pf-ref} gives an
inverse defined on all of $\mathcal H$, so $T$ is bijective onto
$\mathcal H$. Step [](#s3){.pf-ref} shows that its derivative never vanishes. Hence $T$
is conformal.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives the requested map.

:::

:::

:::
