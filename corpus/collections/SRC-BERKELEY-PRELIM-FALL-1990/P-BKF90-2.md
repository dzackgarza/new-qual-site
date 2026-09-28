---
schema: qual/card@1
id: P-BKF90-2
kind: problem
title: The contour integral $\frac1{2\pi i}\oint_{\abs z=1}\frac{dz}{(z-2)(1+2z)^2(1-3z)^3}$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Avoided differentiating at the double and triple poles by using decay at
    infinity to make the sum of all finite residues zero, leaving only the
    simple residue at z=2 to compute.
---

::: {.problem}
Let $C$ be the positively oriented unit circle.
Evaluate
\[
\frac1{2\pi i}\int_C
\frac{dz}{(z-2)(1+2z)^2(1-3z)^3}.
\]
:::

::: {.solution}
Set
$$
R(z)\coloneqq\frac{1}{(z-2)(1+2z)^2(1-3z)^3}.
$$

<1>1. The poles of $R$ inside $C$ are $-1/2$ and $1/3$, while the only pole outside $C$ is $2$.

::: {.proof}
The denominator vanishes only at
$$
z=2,
\qquad
z=-\frac12,
\qquad
z=\frac13.
$$
The latter two points have modulus less than $1$, while $\abs{2}>1$.
:::

<1>2. The sum of the residues of $R$ at all three finite poles is $0$.

::: {.proof}
As $z\to\infty$,
$$
R(z)=O(z^{-6}).
$$
Hence on the positively oriented circle $\abs{z}=T$,
$$
\abs{\int_{\abs{z}=T}R(z)\,dz}=O(T^{-5})\longrightarrow0.
$$
For every $T>2$, the residue theorem gives
$$
\int_{\abs{z}=T}R(z)\,dz
=
2\pi i\sum_{p\in\{2,-1/2,1/3\}}\operatorname{Res}(R;p).
$$
The residue sum is independent of $T$, so letting $T\to\infty$ shows that it is $0$.
:::

<1>3. The residue at the exterior pole $z=2$ is
$$
\operatorname{Res}(R;2)=-\frac1{3125}.
$$

::: {.proof}
The pole at $2$ is simple, so
$$
\begin{aligned}
\operatorname{Res}(R;2)
&=\frac{1}{(1+2\cdot2)^2(1-3\cdot2)^3}\\
&=\frac{1}{5^2(-5)^3}\\
&=-\frac1{3125}.
\end{aligned}
$$
:::

<1>4. The sum of the residues inside the unit circle is
$$
\frac1{3125}.
$$

::: {.proof}
By steps <1>2 and <1>3,
$$
\operatorname{Res}(R;-1/2)+\operatorname{Res}(R;1/3)
=
-\operatorname{Res}(R;2)
=
\frac1{3125}.
$$
:::

<1>5. The requested integral is
$$
\boxed{\frac1{3125}}.
$$

::: {.proof}
By step <1>1, the residue theorem on $C$ gives
$$
\frac1{2\pi i}\int_C R(z)\,dz
=
\operatorname{Res}(R;-1/2)+\operatorname{Res}(R;1/3).
$$
Step <1>4 evaluates the right-hand side.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the required value.
:::
:::
