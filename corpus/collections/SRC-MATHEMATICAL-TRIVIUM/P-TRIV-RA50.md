---
schema: qual/card@1
id: P-TRIV-RA50
kind: problem
title: Fourier transform of the indicator of a ball in $\RR^3$
classification:
  areas: [real-analysis]
  topics:
  - Fourier Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 50, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate the Fourier image $\tilde{f}(\vec{k})$ of the function $f(\vec{r}) = \begin{cases} f_0, & r \leqslant r_0, \\ 0, & r > r_0 \end{cases}$ in $\RR^3$.
:::

::: {.remark}
Use the three-dimensional Fourier convention from Problem 49:
$$
\widetilde f(\vec k)
=
\frac1{(2\pi)^3}
\int_{\RR^3}
f(\vec r)e^{-i\vec k\cdot\vec r}
\,d^3r.
$$
:::

::: {.solution}

Put
$$
k=\norm{\vec k}.
$$

::: pf

::: pf-step

By rotational symmetry, choose spherical coordinates whose polar axis is
parallel to $\vec k$.


::: pf-proof

The function $f$ depends only on $r=\norm{\vec r}$, and Lebesgue measure is rotation
invariant. Thus rotating the coordinate system does not change the integral.
In the chosen coordinates,
$$
\vec k\cdot\vec r
=
kr\cos\theta.
$$

:::

:::

::: {.pf-step #s1-2}

The Fourier transform is
$$
\widetilde f(\vec k)
=
\frac{f_0}{(2\pi)^3}
\int_0^{r_0}r^2\,dr
\int_0^{2\pi}d\varphi
\int_0^\pi
e^{-ikr\cos\theta}
\sin\theta
\,d\theta.
$$


::: pf-proof

Inside the ball $r\leq r_0$, the function equals the constant $f_0$; outside
it vanishes. The spherical volume element is
$$
r^2\sin\theta\,dr\,d\theta\,d\varphi.
$$

:::

:::

::: {.pf-step #s1-3}

The angular integrals give
$$
\int_0^{2\pi}d\varphi
\int_0^\pi
e^{-ikr\cos\theta}
\sin\theta\,d\theta
=
4\pi\frac{\sin(kr)}{kr}.
$$


::: pf-proof

The $\varphi$-integral contributes $2\pi$. For the polar integral, set
$$
u=\cos\theta.
$$
Then
$$
\int_0^\pi
e^{-ikr\cos\theta}\sin\theta\,d\theta
=
\int_{-1}^{1}e^{-ikru}\,du
=
\frac{2\sin(kr)}{kr}.
$$

:::

:::

::: {.pf-step #s1-4}

For $k>0$,
$$
\widetilde f(\vec k)
=
\frac{4\pi f_0}{(2\pi)^3k}
\int_0^{r_0}
r\sin(kr)
\,dr.
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref} and cancel one factor of $r$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\int_0^{r_0}
r\sin(kr)
\,dr
=
-\frac{r_0\cos(kr_0)}{k}
+
\frac{\sin(kr_0)}{k^2}.
$$


::: pf-proof

Integration by parts gives
$$
\int r\sin(kr)\,dr
=
-\frac{r\cos(kr)}k
+
\frac{\sin(kr)}{k^2}.
$$
The lower endpoint contributes zero.

:::

:::

::: {.pf-step #s1-6}

Hence, for $k>0$,
$$
\boxed{
\widetilde f(\vec k)
=
\frac{f_0}{2\pi^2}
\frac{
\sin(kr_0)-kr_0\cos(kr_0)
}{k^3}.
}
$$


::: pf-proof

Substitute step [](#s1-5){.pf-ref} into step [](#s1-4){.pf-ref} and use
$$
\frac{4\pi}{(2\pi)^3}
=
\frac1{2\pi^2}.
$$

:::

:::

::: {.pf-step #s1-7}

At $k=0$,
$$
\boxed{
\widetilde f(0)
=
\frac{f_0r_0^3}{6\pi^2}.
}
$$


::: pf-proof

Directly,
$$
\widetilde f(0)
=
\frac1{(2\pi)^3}
f_0\operatorname{Vol}(B_{r_0}^3)
=
\frac1{8\pi^3}
f_0\frac{4\pi r_0^3}{3}
=
\frac{f_0r_0^3}{6\pi^2}.
$$
Equivalently, the expression in step [](#s1-6){.pf-ref} has the same limit because
$$
\sin z-z\cos z
=
\frac{z^3}{3}+O(z^5).
$$

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref} give the Fourier image for all $\vec k\in\RR^3$.

:::

:::

:::
