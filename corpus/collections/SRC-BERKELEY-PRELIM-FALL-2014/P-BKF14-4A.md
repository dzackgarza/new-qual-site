---
schema: qual/card@1
id: P-BKF14-4A
kind: problem
title: A power series convergent on the disk and at $1$ whose sum is discontinuous at $1$
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
    Independently checked the retained Fall 2014 solution packet and its use
    of rays with argument pi/3^k, on which the tail terms are negative real.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked absolute convergence in the open disk, convergence at z=1, and
    the divergence to minus infinity of the real part along each selected
    ray as the radius tends to one.
---

::: {.problem}
Let $D$ be the set consisting of the open unit disk together with the point $1$. Show that the power series

$$
\sum _ { n > 0 } z ^ { 3 ^ { n } } / n - z ^ { 2 \times 3 ^ { n } } / n
$$

converges at all points of $D$. By examining points with argument of the form $\pi/3^k$, show that the function it converges to is not continuous.
:::

::: {.solution}
Write
$$
F(z)\coloneqq
\sum_{n=1}^{\infty}
\frac{z^{3^n}-z^{2\cdot3^n}}{n}
$$
whenever the series converges.

::: pf

::: {.pf-step #s1}

The series converges absolutely for every $z$ with $|z|<1$.

::: pf-proof

Let $r=|z|<1$. Then
$$
\left|
\frac{z^{3^n}-z^{2\cdot3^n}}{n}
\right|
\le
\frac{r^{3^n}+r^{2\cdot3^n}}{n}
\le
2r^{3^n}.
$$
Since $3^n\ge n$ and $0\le r<1$,
$$
r^{3^n}\le r^n.
$$
Thus the series is dominated by the convergent geometric series
$2\sum_{n\ge1}r^n$.

:::

:::

::: {.pf-step #s2}

The series converges at $z=1$, and
$$
F(1)=0.
$$

::: pf-proof

At $z=1$, every summand is
$$
\frac{1^{3^n}-1^{2\cdot3^n}}n=0.
$$
Hence the series converges and has sum $0$.

:::

:::

::: {.pf-step #s3}

Fix $k\ge1$ and put
$$
\theta_k\coloneqq\frac{\pi}{3^k}.
$$
For $0<r<1$ and every $n\ge k$,
$$
\frac{(re^{i\theta_k})^{3^n}
-(re^{i\theta_k})^{2\cdot3^n}}{n}
=
-\frac{r^{3^n}+r^{2\cdot3^n}}n.
$$

::: pf-proof

For $n\ge k$, the integer $3^{n-k}$ is odd. Therefore
$$
e^{i3^n\theta_k}
=
e^{i\pi3^{n-k}}
=
-1,
$$
whereas
$$
e^{i2\cdot3^n\theta_k}
=
e^{i2\pi3^{n-k}}
=
1.
$$
Substitution gives the displayed identity.

:::

:::

::: {.pf-step #s4}

For each fixed $k$,
$$
\Re F(re^{i\theta_k})\longrightarrow-\infty
\qquad\text{as }r\uparrow1.
$$

::: pf-proof

Split the series into the first $k-1$ terms and the tail. The real part
of the finite initial sum has absolute value at most
$$
C_k\coloneqq2\sum_{n=1}^{k-1}\frac1n
$$
for every $0<r<1$. By step [](#s3){.pf-ref}, the tail is real and equals
$$
-\sum_{n=k}^{\infty}
\frac{r^{3^n}+r^{2\cdot3^n}}n.
$$
For every $L\ge k$,
$$
\sum_{n=k}^{\infty}
\frac{r^{3^n}+r^{2\cdot3^n}}n
\ge
\sum_{n=k}^{L}
\frac{r^{3^n}+r^{2\cdot3^n}}n.
$$
As $r\uparrow1$, the right-hand side tends to
$2\sum_{n=k}^{L}1/n$. Since these finite harmonic sums are arbitrarily
large when $L$ is large, the tail tends to $-\infty$. The bounded
initial sum does not change this conclusion.

:::

:::

::: {.pf-step #s5}

The function $F$ is unbounded in every neighborhood of $1$ in
$D$.

::: pf-proof

Let $\delta>0$ and $M>0$. Since
$e^{i\theta_k}\to1$, choose $k$ so large that
$$
|e^{i\theta_k}-1|<\frac{\delta}{2}.
$$
By step [](#s4){.pf-ref}, choose $r<1$ sufficiently close to $1$ that
$$
1-r<\frac{\delta}{2}
\qquad\text{and}\qquad
\Re F(re^{i\theta_k})<-M.
$$
Then $z=re^{i\theta_k}$ lies in the open unit disk and
$$
|z-1|
\le
|z-e^{i\theta_k}|+|e^{i\theta_k}-1|
<
\delta.
$$
Also $|F(z)|\ge|\Re F(z)|>M$. Thus values of $F$ are arbitrarily large
in modulus in every neighborhood of $1$.

:::

:::

::: {.pf-step #s6}

The function $F:D\to\CC$ is not continuous at $1$.

::: pf-proof

By step [](#s2){.pf-ref}, $F(1)=0$. Step [](#s5){.pf-ref} shows that $F$ is not even bounded in
any neighborhood of $1$, so it cannot be continuous there.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove convergence at every point of $D$, while step
[](#s6){.pf-ref} proves the required discontinuity.

:::

:::

:::
