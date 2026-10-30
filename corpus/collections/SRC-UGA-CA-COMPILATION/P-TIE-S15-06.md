---
schema: qual/card@1
id: P-TIE-S15-06
kind: problem
title: Laurent series of $\frac1z+\frac{1}{z^2-1}$ in all annuli
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 6.
---

::: {.problem}
Let $f(z) = \dfrac{1}{z} + \dfrac{1}{z^{2} - 1}$. Find all the Laurent series of $f$ and describe the largest annuli in which these series are valid.
:::

::: {.solution}

The singularities of
$$
f(z)
=
\frac1z+\frac1{z^2-1}
$$
are
$$
z=0,\qquad z=1,\qquad z=-1.
$$
Thus the singularity moduli are $0$ and $1$.

::: pf

::: {.pf-step #s1-1}

On the annulus
$$
0<\abs{z}<1,
$$
one has
$$
\boxed{
f(z)
=
\frac1z
-
\sum_{n=0}^{\infty}z^{2n}.
}
$$


::: pf-proof

If $\abs{z}<1$, then $\abs{z^2}<1$, so the geometric series gives
$$
\frac1{1-z^2}
=
\sum_{n=0}^{\infty}z^{2n}.
$$
Hence
$$
\frac1{z^2-1}
=
-\frac1{1-z^2}
=
-\sum_{n=0}^{\infty}z^{2n}.
$$
Adding $1/z$ gives the displayed Laurent series. The term $1/z$ excludes $z=0$, so the domain is
$$
0<\abs{z}<1.
$$

:::

:::

::: {.pf-step #s1-2}

The annulus
$$
0<\abs{z}<1
$$
is maximal for the Laurent series in step [](#s1-1){.pf-ref}.


::: pf-proof

The function has a singularity at $z=0$, so the inner radius cannot be reduced below $0$. The points $z=\pm1$ are singularities with modulus $1$, so the outer radius cannot exceed $1$. Hence the annulus is maximal.

:::

:::

::: {.pf-step #s1-3}

On the annulus
$$
\abs{z}>1,
$$
one has
$$
\boxed{
f(z)
=
\frac1z
+
\sum_{n=0}^{\infty}z^{-2n-2}.
}
$$


::: pf-proof

If $\abs{z}>1$, then $\abs{z^{-2}}<1$. Therefore
$$
\begin{aligned}
\frac1{z^2-1}
&=
\frac{z^{-2}}{1-z^{-2}}\\
&=
z^{-2}
\sum_{n=0}^{\infty}z^{-2n}\\
&=
\sum_{n=0}^{\infty}z^{-2n-2}.
\end{aligned}
$$
Adding $1/z$ gives the displayed Laurent expansion.

:::

:::

::: {.pf-step #s1-4}

The annulus
$$
\abs{z}>1
$$
is maximal for the Laurent series in step [](#s1-3){.pf-ref}.


::: pf-proof

The singularities $z=\pm1$ lie on the circle $\abs{z}=1$, so the inner radius cannot be decreased below $1$. There are no finite singularities with modulus greater than $1$, so the outer radius is infinite. Hence this annulus is maximal.

:::

:::

::: {.pf-step #s1-5}

These are all Laurent expansions of $f$ about $0$ on maximal annuli.


::: pf-proof

A Laurent expansion about $0$ is determined on each connected annular component obtained by removing the singularity circles centered at $0$. The only singularity radii are $0$ and $1$, so the only maximal annuli are exactly those in steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} give both Laurent series and their largest annuli of validity.

:::

:::

:::
