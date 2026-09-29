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

::: pf

::: {.pf-step #poles-are-double}
The poles of $F$ are
$$
z_k=\left(k+\frac12\right)i,
\qquad
k\in\ZZ,
$$
and every pole has order $2$.

::: pf-proof
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

:::

::: {.pf-step #two-poles-inside}
Exactly two poles lie inside the unit circle:
$$
\frac{i}{2}
\qquad\text{and}\qquad
-\frac{i}{2}.
$$

::: pf-proof
By step [](#poles-are-double){.pf-ref},
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

:::

::: {.pf-step #residue-at-pole}
At either pole $z_0=\pm i/2$,
$$
\operatorname{Res}_{z=z_0}F(z)
=
-\frac{1}{2\pi}.
$$

::: pf-proof
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

:::

::: {.pf-step #residue-sum}
The sum of the residues inside $\abs{z}=1$ is
$$
-\frac{1}{\pi}.
$$

::: pf-proof
By steps [](#two-poles-inside){.pf-ref} and [](#residue-at-pole){.pf-ref}, there are exactly two enclosed poles and each
contributes $-1/(2\pi)$.
:::

:::

::: {.pf-step #integral-value-boxed}
The contour integral equals
$$
\boxed{-2i}.
$$

::: pf-proof
The contour is counterclockwise and contains no pole on its boundary by
step [](#two-poles-inside){.pf-ref}. Hence the residue theorem and step [](#residue-sum){.pf-ref} give
$$
\int_{\abs{z}=1}F(z)\,dz
=
2\pi i
\left(-\frac1\pi\right)
=
-2i.
$$
:::

:::

::: pf-qed
Step [](#integral-value-boxed){.pf-ref} is the requested value.
:::

:::
:::
