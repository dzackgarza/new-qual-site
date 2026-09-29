---
schema: qual/card@1
id: P-BKF13-4B
kind: problem
title: Evaluation of $\int_{-\infty}^{\infty} x\sin x/(x^2+1)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2013 solution packet: the
    upper-half-plane contour, residue at z=i, and vanishing semicircle
    contribution give the stated limit.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the residue computation and a direct O(1/N) estimate for the
    semicircular arc before taking imaginary parts.
---

::: {.problem}
Compute

$$
\lim_{N\to\infty}\int_{-N}^{N}\frac{x\sin(x)}{x^2+1}\,dx.
$$
:::

::: {.solution}
For $N>1$, let $C_N$ be the upper semicircle from $N$ to $-N$, oriented
counterclockwise, and set
$$
F(z)\coloneqq\frac{ze^{iz}}{z^2+1}.
$$

::: pf

::: {.pf-step #s1}

The only pole of $F$ in the upper half-plane is $z=i$, and
$$
\Res_{z=i}F(z)=\frac1{2e}.
$$

::: pf-proof

Since $z^2+1=(z-i)(z+i)$, the poles are $i$ and $-i$. Hence
$$
\Res_{z=i}F(z)
=
\lim_{z\to i}\frac{ze^{iz}}{z+i}
=
\frac{ie^{-1}}{2i}
=
\frac1{2e}.
$$

:::

:::

::: {.pf-step #s2}

For every $N>1$,
$$
\int_{-N}^{N}\frac{xe^{ix}}{x^2+1}\,dx
+
\int_{C_N}F(z)\,dz
=
\frac{\pi i}{e}.
$$

::: pf-proof

The contour consisting of the interval $[-N,N]$ followed by $C_N$
encloses only the pole $i$. By the residue theorem and step [](#s1){.pf-ref},
$$
\int_{-N}^{N}\frac{xe^{ix}}{x^2+1}\,dx
+
\int_{C_N}F(z)\,dz
=
2\pi i\Res_{z=i}F(z)
=
\frac{\pi i}{e}.
$$

:::

:::

::: {.pf-step #s3}

The semicircular contribution tends to zero:
$$
\lim_{N\to\infty}\int_{C_N}F(z)\,dz=0.
$$

::: pf-proof

Parametrize $C_N$ by $z=Ne^{i\theta}$ for $0\le\theta\le\pi$. Since
$|e^{iz}|=e^{-N\sin\theta}$ and
$|z^2+1|\ge N^2-1$, we obtain
$$
\left|\int_{C_N}F(z)\,dz\right|
\le
\frac{N^2}{N^2-1}
\int_0^\pi e^{-N\sin\theta}\,d\theta.
$$
For $0\le\theta\le\pi/2$, concavity of $\sin$ gives
$\sin\theta\ge2\theta/\pi$. By symmetry,
$$
\begin{aligned}
\int_0^\pi e^{-N\sin\theta}\,d\theta
&=
2\int_0^{\pi/2}e^{-N\sin\theta}\,d\theta\\
&\le
2\int_0^{\pi/2}e^{-2N\theta/\pi}\,d\theta\\
&=
\frac{\pi}{N}(1-e^{-N})
\le
\frac{\pi}{N}.
\end{aligned}
$$
Therefore
$$
\left|\int_{C_N}F(z)\,dz\right|
\le
\frac{\pi N}{N^2-1}\longrightarrow0.
$$

:::

:::

::: {.pf-step #s4}

Consequently,
$$
\lim_{N\to\infty}
\int_{-N}^{N}\frac{xe^{ix}}{x^2+1}\,dx
=
\frac{\pi i}{e}.
$$

::: pf-proof

Let $N\to\infty$ in the identity from step [](#s2){.pf-ref} and use step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

The requested limit is
$$
\boxed{\frac{\pi}{e}}.
$$

::: pf-proof

For real $x$,
$$
\frac{xe^{ix}}{x^2+1}
=
\frac{x\cos x}{x^2+1}
+
i\frac{x\sin x}{x^2+1}.
$$
Taking imaginary parts in step [](#s4){.pf-ref} therefore gives
$$
\lim_{N\to\infty}
\int_{-N}^{N}\frac{x\sin x}{x^2+1}\,dx
=
\frac{\pi}{e}.
$$

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the required value.

:::

:::

:::
