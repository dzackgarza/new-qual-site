---
schema: qual/card@1
id: E-SS3.PR-3
kind: problem
title: Laurent series on an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Chapter 3, §9, problem 3, read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF page 127). This card did not
    exist before: it was found missing by a completeness audit of the collection against the book,
    which located every printed Exercises and Problems item and compared it with the cards on disk.
    The transcription was taken from the OCR text layer and cleaned of OCR errors; the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Proved as the hint directs: the difference of the two Cauchy integrals is expanded by the geometric
    series in $\zeta-z_0$ (inside $C_{r_2}$) and in $z-z_0$ (outside $C_{r_1}$), the two series are
    collected into one Laurent series, absolute convergence on compact subsets of the open annulus
    follows from the two geometric bounds, and the series is unique. The pole case then follows by
    taking $a_n=0$ for $n<-k$. Nothing is left in outline.
---

::: {.exercise}
If $f(z)$ is holomorphic in the deleted neighborhood $\{0<\abs{z-z_0}<r\}$ and has a pole of order $k$ at $z_0$, then we can write
$$
f(z)=\frac{a_{-k}}{(z-z_0)^k}+\cdots+\frac{a_{-1}}{(z-z_0)}+g(z)
$$
where $g$ is holomorphic in the disc $\{\abs{z-z_0}<r\}$. There is a generalization of this expansion that holds even if $z_0$ is an essential singularity. This is a special case of the Laurent series expansion, which is valid in an even more general setting.

Let $f$ be holomorphic in a region containing the annulus $\{z:r_1\le\abs{z-z_0}\le r_2\}$ where $0<r_1<r_2$. Then
$$
f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n
$$
where the series converges absolutely in the interior of the annulus. To prove this, it suffices to write
$$
f(z)=\frac{1}{2\pi i}\int_{C_{r_2}}\frac{f(\zeta)}{\zeta-z}\,d\zeta-\frac{1}{2\pi i}\int_{C_{r_1}}\frac{f(\zeta)}{\zeta-z}\,d\zeta
$$
when $r_1<\abs{z-z_0}<r_2$, and argue as in the proof of Theorem 4.4, Chapter 2. Here $C_{r_1}$ and $C_{r_2}$ are the circles bounding the annulus.
:::

::: {.solution}

Let $0<r_1<r_2$, let $A=\{z:r_1<\abs{z-z_0}<r_2\}$ be the open annulus and $\bar A=\{z:r_1\le\abs{z-z_0}\le r_2\}$, on which $f$ is holomorphic. Fix $z\in A$.

::: pf

::: {.pf-step #s1}

$\displaystyle f(z)=\frac{1}{2\pi i}\int_{C_{r_2}}\frac{f(\zeta)}{\zeta-z}\,d\zeta-\frac{1}{2\pi i}\int_{C_{r_1}}\frac{f(\zeta)}{\zeta-z}\,d\zeta$, the circles being traversed counterclockwise.

::: pf-proof

On the annulus minus a small disc around $z$ the function $\zeta\mapsto f(\zeta)/(\zeta-z)$ is holomorphic; applying Cauchy's theorem to the annulus with the two boundary circles and then the Cauchy integral formula to the inner boundary taken clockwise gives
$$
0=\int_{C_{r_2}}\frac{f(\zeta)}{\zeta-z}d\zeta-\int_{C_{r_1}}\frac{f(\zeta)}{\zeta-z}d\zeta-2\pi if(z),
$$
which is the displayed identity. (Equivalently: the cycle $C_{r_2}-C_{r_1}$ is homologous to a small positively oriented circle about $z$.)

:::

:::

::: {.pf-step #s2}

On $C_{r_2}$ one has $\abs{(z-z_0)/(\zeta-z_0)}\le\varrho<1$, and on $C_{r_1}$ one has $\abs{(\zeta-z_0)/(z-z_0)}\le\varrho'<1$, with $\varrho,\varrho'$ depending only on $z$ and the radii.

::: pf-proof

For $\zeta\in C_{r_2}$, $\abs{\zeta-z_0}=r_2$ and $\abs{z-z_0}<r_2$, so
$$
\Bigl|\frac{z-z_0}{\zeta-z_0}\Bigr|=\frac{\abs{z-z_0}}{r_2}=:\varrho<1 .
$$
For $\zeta\in C_{r_1}$, $\abs{\zeta-z_0}=r_1$ and $\abs{z-z_0}>r_1$, so
$$
\Bigl|\frac{\zeta-z_0}{z-z_0}\Bigr|=\frac{r_1}{\abs{z-z_0}}=:\varrho'<1 .
$$

:::

:::

::: {.pf-step #s3}

The first integral equals $\sum_{n\ge0}a_n(z-z_0)^n$ with $a_n=\frac{1}{2\pi i}\int_{C_{r_2}}\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}d\zeta$, absolutely and uniformly on compact subsets of $A$.

::: pf-proof

For $\zeta\in C_{r_2}$ write $\zeta-z=(\zeta-z_0)-(z-z_0)$, so
$$
\frac{1}{\zeta-z}=\frac{1}{\zeta-z_0}\cdot\frac{1}{1-\frac{z-z_0}{\zeta-z_0}}=\sum_{n\ge0}\frac{(z-z_0)^n}{(\zeta-z_0)^{n+1}},
$$
the geometric series converging uniformly in $\zeta\in C_{r_2}$ by step [](#s2){.pf-ref}. Multiplying by $f(\zeta)$ and integrating termwise (legitimate by that uniform convergence on a compact circle and continuity of $f$) gives the display. For $z$ in a compact $K\subseteq A$ the bound $\varrho\le\varrho_K<1$ is uniform, so the series converges uniformly there.

:::

:::

::: {.pf-step #s4}

The second integral equals $\sum_{n\ge1}b_n(z-z_0)^{-n}$ with $b_n=\frac{1}{2\pi i}\int_{C_{r_1}}f(\zeta)(\zeta-z_0)^{n-1}d\zeta$, and $b_n=-a_{-n}$ with $a_{-n}$ given by the same formula with $C_{r_2}$.

::: pf-proof

For $\zeta\in C_{r_1}$ write $\zeta-z=(\zeta-z_0)-(z-z_0)=-(z-z_0)\bigl(1-\frac{\zeta-z_0}{z-z_0}\bigr)$, so
$$
\frac{1}{\zeta-z}=-\frac{1}{z-z_0}\sum_{n\ge0}\Bigl(\frac{\zeta-z_0}{z-z_0}\Bigr)^{n}=-\sum_{n\ge1}(\zeta-z_0)^{n-1}(z-z_0)^{-n},
$$
uniformly in $\zeta$ by step [](#s2){.pf-ref}. Integrating termwise and inserting the minus sign in front of the second Cauchy integral gives
$$
-\frac{1}{2\pi i}\int_{C_{r_1}}\frac{f(\zeta)}{\zeta-z}d\zeta=\sum_{n\ge1}\Bigl[\frac{1}{2\pi i}\int_{C_{r_1}}f(\zeta)(\zeta-z_0)^{n-1}d\zeta\Bigr](z-z_0)^{-n}.
$$
By Cauchy's theorem applied in the annulus, the integral of the holomorphic function $\zeta\mapsto f(\zeta)(\zeta-z_0)^{n-1}$ over $C_{r_1}$ equals its integral over $C_{r_2}$ (the annulus between them is contained in the region where $f$ is holomorphic, and $n-1\ge0$ keeps the integrand holomorphic at $z_0$). Hence $b_n=a_{-n}$ with
$$
a_{-n}=\frac{1}{2\pi i}\int_{C_{r_2}}\frac{f(\zeta)}{(\zeta-z_0)^{-n+1}}d\zeta,
$$
which is the same formula $a_m=\frac{1}{2\pi i}\int_{C_{r_2}}\frac{f(\zeta)}{(\zeta-z_0)^{m+1}}d\zeta$ at $m=-n$.

:::

:::

::: {.pf-step #s5}

Therefore $f(z)=\sum_{n=-\infty}^{\infty}a_n(z-z_0)^n$ on $A$, the series converging absolutely and uniformly on compact subsets of $A$; and the coefficients are unique.

::: pf-proof

Adding the two displays of steps [](#s3){.pf-ref} and [](#s4){.pf-ref} gives the Laurent expansion with all coefficients computed by the single formula $a_n=\frac{1}{2\pi i}\int_{C_r}\frac{f(\zeta)}{(\zeta-z_0)^{n+1}}d\zeta$ for any $r\in(r_1,r_2)$, since by Cauchy's theorem the integral does not depend on $r$.

For absolute convergence on a compact $K\subseteq A$: the positive part is bounded by a constant times $\sum\varrho_K^n$ and the negative part by a constant times $\sum(\varrho'_K)^n$, both convergent.

For uniqueness: if $\sum c_n(z-z_0)^n=\sum d_n(z-z_0)^n$ on $A$, then multiplying by $(z-z_0)^{-m-1}$ and integrating over $C_r$ with $r_1<r<r_2$ gives $2\pi i(c_m-d_m)=0$ by uniform convergence on the circle.

:::

:::

::: {.pf-step #s6}

The case of a pole at $z_0$ follows.

::: pf-proof

If $f$ is holomorphic on $\{0<\abs{z-z_0}<r\}$ and has a pole of order $k$ there, then $f$ is holomorphic on any annulus $\{r_1\le\abs{z-z_0}\le r_2\}$ with $0<r_1<r_2<r$, so by steps [](#s1){.pf-ref}–[](#s5){.pf-ref} it has a Laurent expansion there. The function $f(z)-\sum_{n=-k}^{-1}a_n(z-z_0)^n$ has a removable singularity at $z_0$ (its Laurent series has no negative powers), so it extends to a holomorphic $g$ on the disc, and $f=\sum_{n=-k}^{-1}a_n(z-z_0)^n+g$ is the displayed decomposition. When $z_0$ is an essential singularity the negative part is infinite, and the general expansion is exactly the series proved above.

:::

:::

:::

:::
