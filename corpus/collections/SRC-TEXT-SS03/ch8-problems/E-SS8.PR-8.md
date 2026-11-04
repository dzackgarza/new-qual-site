---
schema: qual/card@1
id: E-SS8.PR-8
kind: problem
title: Bieberbach bound for real Taylor coefficients
classification:
  areas:
  - complex-analysis
  topics:
  - Univalent Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 8, §3, problem 8, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(f); nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    All six parts. (a) Fourier coefficient of the odd function $v$; (b) induction;
    (c) $f(\bar z)=\overline{f(z)}$ and the sign of the imaginary part near $0$; (d) from the power
    series; (e) the estimate $\abs{a_n}r^n\le nr$ from (a) with $a_1=1$, which gives
    $\abs{a_n}\le n/r^{n-1}\to n$; (f) the Koebe function is univalent because
    $z/(1-z)^2=\frac14\bigl(\frac{1+z}{1-z}\bigr)^2-\frac14$ and squaring is injective on the right
    half-plane. Nothing is left in outline.
---

::: {.exercise}
Let $f$ be injective and holomorphic on the unit disc, with $f(0)=0$ and $f'(0)=1$. Write $f(z)=z+a_2z^2+a_3z^3+\cdots$. This problem proves $\abs{a_n}\leq n$ under the additional assumption that every $a_n$ is real.

(a) For $z=re^{i\theta}$ with $0<r<1$, let $v(r,\theta)=\Im f(re^{i\theta})$. Show that
$$
a_nr^n=\frac2\pi\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta.
$$

(b) Show that $\abs{\sin(n\theta)}\leq n\sin\theta$ for $0\leq\theta\leq\pi$ and $n\geq1$.

(c) Use $a_n\in\RR$ to show that $f(\DD)$ is symmetric about the real axis and that $f$ maps the upper half-disc into either the upper or lower part of $f(\DD)$.

(d) Show that $v(r,\theta)=r\sin\theta[1+O(r)]$ for small $r$. Deduce that $v(r,\theta)\sin\theta\geq0$ for all $0<r<1$ and $0\leq\theta\leq\pi$.

(e) Prove that $\abs{a_nr^n}\leq nr$, then let $r\to1$.

(f) Check that $f(z)=z/(1-z)^2$ meets the hypotheses and has $a_n=n$ for every $n$.
:::

::: {.solution}

Let $f(z)=z+a_2z^2+a_3z^3+\cdots$ be injective and holomorphic on $\DD$ with $f(0)=0$, $f'(0)=1$, and suppose every $a_n\in\RR$. For $0<r<1$ and $z=re^{i\theta}$ put $v(r,\theta)=\operatorname{Im}f(re^{i\theta})$.

::: pf

::: {.pf-step #s1}

Part (a): $a_nr^n=\dfrac2\pi\displaystyle\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta$ for $n\ge1$.

::: pf-proof

Since the $a_k$ are real, $f(re^{i\theta})=\sum_k a_kr^k(\cos k\theta+i\sin k\theta)$ with $a_1=1$, so $v(r,\theta)=\sum_{k\ge1}a_kr^k\sin k\theta$, uniformly convergent in $\theta$. Hence
$$
\frac2\pi\int_0^\pi v(r,\theta)\sin(n\theta)\,d\theta=\sum_{k\ge1}a_kr^k\cdot\frac2\pi\int_0^\pi\sin(k\theta)\sin(n\theta)\,d\theta=a_nr^n,
$$
because $\frac2\pi\int_0^\pi\sin(k\theta)\sin(n\theta)d\theta=\delta_{kn}$.

:::

:::

::: {.pf-step #s2}

Part (b): $\abs{\sin(n\theta)}\le n\sin\theta$ for $0\le\theta\le\pi$ and $n\ge1$.

::: pf-proof

For $n=1$ it is an equality. If it holds for $n-1$, then
$$
\abs{\sin(n\theta)}=\abs{\sin((n-1)\theta)\cos\theta+\cos((n-1)\theta)\sin\theta}\le(n-1)\sin\theta\abs{\cos\theta}+\abs{\cos((n-1)\theta)}\sin\theta\le n\sin\theta
$$
on $[0,\pi]$, where $\sin\theta\ge0$.

:::

:::

::: {.pf-step #s3}

Part (c): $f(\DD)$ is symmetric about the real axis, and $v(r,\theta)>0$ for $0<\theta<\pi$.

::: pf-proof

Since the coefficients are real, $f(\bar z)=\overline{f(z)}$, so $f(\DD)$ is invariant under conjugation, i.e. symmetric about $\RR$.

Since $f$ is injective with $f(0)=0$ and $f'(0)=1$, one has $f(z)=z(1+O(z))$, so for small $z$ in the upper half-disc, $\operatorname{Im}f(z)>0$. The upper half-disc $\DD^+$ is connected, and the set where $\operatorname{Im}f\ne0$ is $\DD^+\setminus f^{-1}(\RR)$; by continuity and connectedness, $\operatorname{Im}f>0$ on all of $\DD^+$. Also $f$ does not vanish on $\DD^+$ (injectivity and $f(0)=0$). Hence $v(r,\theta)>0$ for $0<\theta<\pi$.

:::

:::

::: {.pf-step #s4}

Part (d): $v(r,\theta)=r\sin\theta\,(1+O(r))$ as $r\to0$, uniformly in $\theta$; consequently $v(r,\theta)\sin\theta\ge0$ for $0<r<1$ and $0\le\theta\le\pi$.

::: pf-proof

From the power series, $\abs{v(r,\theta)-r\sin\theta}\le\sum_{k\ge2}\abs{a_k}r^k\le Cr^2$ with $C=\sum_{k\ge2}\abs{a_k}$, which is finite because $f$ is holomorphic on a neighbourhood of $\overline\DD$; this is uniform in $\theta$. So $v(r,\theta)=r\sin\theta(1+O(r))$ with the $O(r)$ uniform in $\theta$.

By step [](#s3){.pf-ref}, $v>0$ on $(0,\pi)$, and $\sin\theta\ge0$ on $[0,\pi]$; hence $v\sin\theta\ge0$.

:::

:::

::: {.pf-step #s5}

Part (e): $\abs{a_n}r^n\le nr$ for $0<r<1$, hence $\abs{a_n}\le n$.

::: pf-proof

By step [](#s1){.pf-ref}, steps [](#s2){.pf-ref} and [](#s4){.pf-ref},
$$
\abs{a_n}r^n=\Bigl|\frac2\pi\int_0^\pi v\sin(n\theta)\,d\theta\Bigr|\le\frac2\pi\int_0^\pi\abs{v}\abs{\sin(n\theta)}\,d\theta\le\frac{2n}{\pi}\int_0^\pi v\sin\theta\,d\theta .
$$
By step [](#s1){.pf-ref} with $n=1$ and $a_1=1$, the last integral equals $\frac\pi2\cdot r$. Hence $\abs{a_n}r^n\le nr$, that is $\abs{a_n}\le n/r^{n-1}$ for every $0<r<1$. Letting $r\to1$ gives $\abs{a_n}\le n$.

:::

:::

::: {.pf-step #s6}

Part (f): $f(z)=\dfrac{z}{(1-z)^2}$ satisfies the hypotheses, with $a_n=n$ for every $n$.

::: pf-proof

The expansion $\frac{z}{(1-z)^2}=\sum_{n\ge1}nz^n$ holds for $\abs z<1$, so $f(0)=0$, $f'(0)=1$ and $a_n=n\in\RR$.

For injectivity, write
$$
f(z)=\frac{z}{(1-z)^2}=\frac14\Bigl(\frac{1+z}{1-z}\Bigr)^2-\frac14 .
$$
The map $z\mapsto\frac{1+z}{1-z}$ is a biholomorphism of $\DD$ onto the right half-plane $\{\Re w>0\}$, and squaring is injective there: if $w_1^2=w_2^2$ with $\Re w_j>0$, then $w_1=\pm w_2$, and the sign must be positive because both have positive real part. Hence $f$ is injective on $\DD$.

:::

:::

:::

:::
