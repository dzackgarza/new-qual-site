---
schema: qual/card@1
id: P-BERK86S-20
kind: problem
title: The contour integral $\int_{|z|=1}(e^{2\pi z}+1)^{-2}\,dz$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Located the two double poles z=plus/minus i/2 inside the unit circle,
    computed residue -1/(2 pi) at each from the local exponential
    expansion, and applied the residue theorem.
---

::: {.problem}
Evaluate the counterclockwise contour integral
\[
\int_{|z|=1}\frac{dz}{(e^{2\pi z}+1)^2}.
\]
:::

::: {.solution}
Let
$$
F(z)\coloneqq\frac{1}{(e^{2\pi z}+1)^2}.
$$

<1>1. The poles of $F$ are
$$
z_k=\left(k+\frac12\right)i,
\qquad
k\in\ZZ,
$$
and every pole has order $2$.

::: {.proof}
The denominator vanishes exactly when
$$
e^{2\pi z}=-1.
$$
Since
$$
e^w=-1
$$
exactly for
$$
w=(2k+1)\pi i,
\qquad
k\in\ZZ,
$$
the zeros of $e^{2\pi z}+1$ are precisely the displayed points.
Moreover,
$$
\frac{d}{dz}(e^{2\pi z}+1)
=
2\pi e^{2\pi z}
=
-2\pi
$$
at every such point, so those zeros are simple. Squaring the denominator
therefore makes them double poles of $F$.
:::

<1>2. Exactly two poles lie inside the unit circle:
$$
\frac{i}{2}
\qquad\text{and}\qquad
-\frac{i}{2}.
$$

::: {.proof}
By step <1>1,
$$
\abs{z_k}
=
\abs{k+\frac12}.
$$
The inequality
$$
\abs{k+\frac12}<1
$$
holds exactly for $k=0$ and $k=-1$. No pole lies on
$\abs{z}=1$.
:::

<1>3. At either pole $z_0=\pm i/2$,
$$
\operatorname{Res}_{z=z_0}F(z)
=
-\frac{1}{2\pi}.
$$

::: {.proof}
Put $w=z-z_0$. Since $e^{2\pi z_0}=-1$,
$$
e^{2\pi z}+1
=
1-e^{2\pi w}.
$$
As $w\to0$,
$$
e^{2\pi w}-1
=
2\pi w\left(1+\pi w+O(w^2)\right).
$$
Therefore
$$
\begin{aligned}
F(z)
&=
\frac{1}{
4\pi^2w^2
\left(1+\pi w+O(w^2)\right)^2
}\\
&=
\frac{1}{4\pi^2w^2}
\left(1-2\pi w+O(w^2)\right)\\
&=
\frac{1}{4\pi^2w^2}
-\frac{1}{2\pi w}
+O(1).
\end{aligned}
$$
Thus the coefficient of $(z-z_0)^{-1}=w^{-1}$ is
$-1/(2\pi)$.
:::

<1>4. The sum of the residues inside $\abs{z}=1$ is
$$
-\frac{1}{\pi}.
$$

::: {.proof}
By steps <1>2 and <1>3, there are exactly two enclosed poles and each
contributes $-1/(2\pi)$.
:::

<1>5. The contour integral equals
$$
\boxed{-2i}.
$$

::: {.proof}
The contour is counterclockwise and contains no pole on its boundary by
step <1>2. Hence the residue theorem and step <1>4 give
$$
\int_{\abs{z}=1}F(z)\,dz
=
2\pi i
\left(-\frac1\pi\right)
=
-2i.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the requested value.
:::
:::
