---
schema: qual/card@1
id: P-TIE-S15-17
kind: problem
title: Partial fraction expansion of $\pi^2/\sin^2\pi z$
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 17.
---

::: {.problem}
(1) Show that $\dfrac{\pi^{2}}{\sin^{2}\pi z}$ and $g(z) = \sum_{n=-\infty}^{\infty} \dfrac{1}{(z - n)^{2}}$ have the same principal part at each integer point.

(2) Show that $h(z) = \dfrac{\pi^{2}}{\sin^{2}\pi z} - g(z)$ is bounded on $\CC$ and conclude that
$$
\frac{\pi^{2}}{\sin^{2}\pi z} = \sum_{n=-\infty}^{\infty} \frac{1}{(z - n)^{2}}.
$$
:::

::: {.solution}

Define
$$
g(z)
\coloneqq
\sum_{n\in\ZZ}
\frac1{(z-n)^2},
$$
for $z\notin\ZZ$.

::: pf

::: {.pf-step #s1-1}

The series defining $g$ converges absolutely and locally uniformly on $\CC\setminus\ZZ$.


::: pf-proof

Let $K\subset\CC\setminus\ZZ$ be compact. Choose $R>0$ such that
$$
\abs{z}\le R
$$
for every $z\in K$. If $\abs{n}>2R$, then
$$
\abs{z-n}
\ge
\abs{n}-\abs{z}
\ge
\frac{\abs{n}}2.
$$
Hence
$$
\abs{\frac1{(z-n)^2}}
\le
\frac4{n^2}
$$
uniformly on $K$ for all sufficiently large $\abs n$. Since
$$
\sum_{n\ne0}\frac1{n^2}
$$
converges, the Weierstrass $M$-test gives absolute locally uniform convergence.

:::

:::

::: {.pf-step #s1-2}

At every integer $m$, the principal part of $g$ is
$$
\frac1{(z-m)^2}.
$$


::: pf-proof

Split the series as
$$
g(z)
=
\frac1{(z-m)^2}
+
\sum_{n\ne m}
\frac1{(z-n)^2}.
$$
By step [](#s1-1){.pf-ref}, the second sum is holomorphic in a neighborhood of $m$. Hence the only negative-power term in the Laurent expansion at $m$ is
$$
(z-m)^{-2}.
$$

:::

:::

::: {.pf-step #s1-3}

At every integer $m$, the principal part of
$$
\frac{\pi^2}{\sin^2\pi z}
$$
is also
$$
\frac1{(z-m)^2}.
$$


::: pf-proof

Write
$$
z=m+w.
$$
Then
$$
\sin\pi z
=
\sin(\pi m+\pi w)
=
(-1)^m\sin\pi w.
$$
As $w\to0$,
$$
\sin\pi w
=
\pi w+O(w^3).
$$
Therefore
$$
\sin^2\pi z
=
\pi^2w^2\left(1+O(w^2)\right),
$$
and hence
$$
\frac{\pi^2}{\sin^2\pi z}
=
\frac1{w^2}+O(1)
=
\frac1{(z-m)^2}+O(1).
$$
Thus the principal part is exactly $(z-m)^{-2}$.

:::

:::

::: {.pf-step #s1-4}

The function
$$
h(z)
\coloneqq
\frac{\pi^2}{\sin^2\pi z}
-
g(z)
$$
extends to an entire function on $\CC$.


::: pf-proof

Away from the integers, both terms are holomorphic. By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, their principal parts cancel at every integer. Thus each apparent singularity of $h$ at an integer is removable. Filling in those removable singularities gives an entire function.

:::

:::

::: {.pf-step #s1-5}

The function $h$ is $1$-periodic.


::: pf-proof

Since
$$
\sin\pi(z+1)
=
-\sin\pi z,
$$
one has
$$
\frac{\pi^2}{\sin^2\pi(z+1)}
=
\frac{\pi^2}{\sin^2\pi z}.
$$
Also, absolute convergence allows reindexing:
$$
\begin{aligned}
g(z+1)
&=
\sum_{n\in\ZZ}
\frac1{(z+1-n)^2}\\
&=
\sum_{m\in\ZZ}
\frac1{(z-m)^2}
=
g(z),
\end{aligned}
$$
where $m=n-1$. Hence $h(z+1)=h(z)$.

:::

:::

::: {.pf-step #s1-6}

On the strip
$$
S
\coloneqq
\left\{
z=x+iy:
-\frac12\le x\le\frac12
\right\},
$$
one has
$$
g(z)\longrightarrow0
$$
uniformly as $\abs y\to\infty$.


::: pf-proof

For $\abs{x}\le1/2$,
$$
\abs{x-n}
\ge
\abs n-\frac12.
$$
Therefore
$$
\begin{aligned}
\abs{g(x+iy)}
&\le
\sum_{n\in\ZZ}
\frac1{(x-n)^2+y^2}\\
&\le
\frac1{y^2}
+
2
\sum_{n=1}^{\infty}
\frac1{(n-\frac12)^2+y^2}.
\end{aligned}
$$
For $\abs y\ge1$, comparison with the decreasing function
$$
t\longmapsto\frac1{t^2+y^2}
$$
gives
$$
\sum_{n=1}^{\infty}
\frac1{(n-\frac12)^2+y^2}
\le
\frac1{y^2}
+
\int_0^\infty
\frac{dt}{t^2+y^2}
=
\frac1{y^2}
+
\frac{\pi}{2\abs y}.
$$
Thus
$$
\sup_{\abs{x}\le1/2}
\abs{g(x+iy)}
\le
\frac3{y^2}
+
\frac{\pi}{\abs y},
$$
which tends to $0$ as $\abs y\to\infty$.

:::

:::

::: {.pf-step #s1-7}

On the same strip,
$$
\frac{\pi^2}{\sin^2\pi z}
\longrightarrow0
$$
uniformly as $\abs y\to\infty$.


::: pf-proof

For $z=x+iy$,
$$
\abs{\sin\pi z}^2
=
\sin^2\pi x+\sinh^2\pi y.
$$
Hence
$$
\abs{\frac{\pi^2}{\sin^2\pi z}}
\le
\frac{\pi^2}{\sinh^2\pi y},
$$
and the right-hand side tends to $0$ as $\abs y\to\infty$, independently of $x$.

:::

:::

::: {.pf-step #s1-8}

The entire function $h$ is bounded on $\CC$.


::: pf-proof

By steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref}, $h$ is bounded on the parts of the fundamental strip $S$ with sufficiently large $\abs y$. On the remaining compact rectangle
$$
\left\{
-\frac12\le\operatorname{Re}z\le\frac12,
\quad
\abs{\operatorname{Im}z}\le Y
\right\},
$$
the entire function $h$ is bounded by continuity. Hence $h$ is bounded on all of $S$.

By step [](#s1-5){.pf-ref}, every point of $\CC$ is congruent modulo an integer translation to a point of $S$, and $h$ is unchanged by such translation. Therefore $h$ is bounded on $\CC$.

:::

:::

::: {.pf-step #s1-9}

The function $h$ is identically zero.


::: pf-proof

By step [](#s1-8){.pf-ref} and Liouville's theorem, $h$ is constant. Along the imaginary axis,
$$
h(iy)
\longrightarrow0
$$
as $\abs y\to\infty$ by steps [](#s1-6){.pf-ref} and [](#s1-7){.pf-ref}. Hence the constant value must be $0$.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\frac{\pi^2}{\sin^2\pi z}
=
\sum_{n=-\infty}^{\infty}
\frac1{(z-n)^2}
}
$$
for every $z\notin\ZZ$.


::: pf-proof

Step [](#s1-9){.pf-ref} says
$$
h(z)
=
\frac{\pi^2}{\sin^2\pi z}
-
g(z)
\equiv0.
$$
Substituting the definition of $g$ gives the identity.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove part (1), and steps [](#s1-4){.pf-ref} through [](#s1-10){.pf-ref} prove part (2).

:::

:::

:::
