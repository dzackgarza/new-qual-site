---
schema: qual/card@1
id: P-PQG5I
kind: problem
title: Compactness of $\{x\in\ell^2:\sum n|x_n|^2\le 1\}$ and attainment of $\int_0^{2\pi}\bigl|\sum
  x_n e^{in\theta}\bigr|\frac{d\theta}{2\pi}$ on this set
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Compactness
  - Hilbert Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked against problem 9 of the UCLA Analysis Qualifying Exam, Spring 2010, from the collection provenance PDF; the UCLA solution compilation leaves this problem without a supplied solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Retained the finite-head/uniform-tail compactness argument, with the head correctly treated in complex finite-dimensional space. Defined the trigonometric series in part (b) as its L2 limit under the Fourier isometry, then proved the objective is 1-Lipschitz from l2 to R by L1-L2 comparison.
---

::: {.problem}
Let $$A = \left\{x\in\ell^2: \sum_{n\ge1} n|x_n|^2 \le 1\right\}.$$

a. Show that $A$ is compact in the $\ell^2$ topology.

b. Show that the mapping from $A$ to $\mathbb{R}$ defined by $$x \mapsto \int_0^{2\pi} \left|\sum_{n\ge1} x_n e^{in\theta}\right| \frac{d\theta}{2\pi}$$ achieves its maximum on $A$.
:::

::: {.solution}
<1>1. The set $A$ is closed in $\ell^2$.
::: {.proof}
Let $x^{(k)}\in A$ and suppose
\[
x^{(k)}\longrightarrow x
\qquad\text{in }\ell^2.
\]
For every fixed coordinate $n$,
\[
|x_n^{(k)}-x_n|\le\|x^{(k)}-x\|_{\ell^2},
\]
so $x_n^{(k)}\to x_n$.
Hence for every $N$,
\[
\sum_{n=1}^N n|x_n|^2
=
\lim_{k\to\infty}
\sum_{n=1}^N n|x_n^{(k)}|^2
\le1.
\]
Letting $N\to\infty$ and using monotone convergence of the nonnegative partial sums gives
\[
\sum_{n=1}^{\infty}n|x_n|^2\le1.
\]
Thus $x\in A$.
:::

<1>2. The tails of elements of $A$ are uniformly small:
\[
\sup_{x\in A}
\sum_{n>N}|x_n|^2
\le\frac1{N+1}.
\]
::: {.proof}
For every $x\in A$,
\[
\begin{aligned}
\sum_{n>N}|x_n|^2
&\le
\frac1{N+1}
\sum_{n>N}n|x_n|^2\\
&\le\frac1{N+1}.
\end{aligned}
\]
:::

<1>3. The set $A$ is totally bounded in $\ell^2$.
::: {.proof}
Fix $\varepsilon>0$.
Choose $N$ so large that
\[
\frac1{N+1}<\frac{\varepsilon^2}{4}.
\]
By <1>2, every $x\in A$ has tail norm
\[
\left(\sum_{n>N}|x_n|^2\right)^{1/2}<\frac\varepsilon2.
\]

The first $N$ coordinates of $x\in A$ lie in the finite-dimensional ellipsoid
\[
B_N=
\left\{(z_1,\ldots,z_N)\in\mathbb C^N:
\sum_{n=1}^N n|z_n|^2\le1
\right\}.
\]
This set is closed and bounded in the finite-dimensional normed space $\mathbb C^N$, hence compact.
Therefore it has a finite $\varepsilon/2$-net
\[
v^{(1)},\ldots,v^{(M)}.
\]
Embed each $v^{(j)}$ in $\ell^2$ by adjoining zero coordinates after $N$.
For any $x\in A$, choose $j$ so that its first $N$ coordinates are within $\varepsilon/2$ of $v^{(j)}$.
Then
\[
\begin{aligned}
\|x-v^{(j)}\|_{\ell^2}^2
&=
\sum_{n=1}^N|x_n-v_n^{(j)}|^2
+
\sum_{n>N}|x_n|^2\\
&<\frac{\varepsilon^2}{4}+rac{\varepsilon^2}{4}
<\varepsilon^2.
\end{aligned}
\]
Thus the finitely many embedded vectors form an $\varepsilon$-net for $A$.
:::

<1>4. The set $A$ is compact in $\ell^2$.
::: {.proof}
The Hilbert space $\ell^2$ is complete.
By <1>1, its closed subset $A$ is complete, and by <1>3, $A$ is totally bounded.
A complete totally bounded metric space is compact.
This proves part (a).
:::

For $x=(x_n)\in\ell^2$, let
\[
g_{x,N}(\theta)=\sum_{n=1}^N x_ne^{in\theta}.
\]
Equip the circle with normalized measure $d\theta/(2\pi)$.

<1>5. The sequence $g_{x,N}$ converges in $L^2(\mathbb T)$ to a function $g_x$, and
\[
\|g_x-g_y\|_{L^2}=\|x-y\|_{\ell^2}.
\]
::: {.proof}
The functions $e^{in\theta}$, $n\ge1$, are orthonormal in $L^2(\mathbb T,d\theta/(2\pi))$.
Hence for $M>N$,
\[
\|g_{x,M}-g_{x,N}\|_{L^2}^2
=
\sum_{n=N+1}^M|x_n|^2.
\]
Since $x\in\ell^2$, the right-hand side tends to zero as $M,N\to\infty$.
Thus $g_{x,N}$ is Cauchy in the complete space $L^2(\mathbb T)$ and has a limit $g_x$.
Applying the same orthogonality identity to the coefficient sequence $x-y$ and passing to the limit gives
\[
\|g_x-g_y\|_{L^2}^2
=
\sum_{n=1}^{\infty}|x_n-y_n|^2.
\]
:::

<1>6. The functional in part (b), interpreted as
\[
\Phi(x)=\int_0^{2\pi}|g_x(\theta)|\,\frac{d\theta}{2\pi},
\]
is well-defined and satisfies
\[
|\Phi(x)-\Phi(y)|\le\|x-y\|_{\ell^2}.
\]
::: {.proof}
Because the circle has normalized measure $1$, Cauchy--Schwarz gives
\[
\|h\|_{L^1}\le\|h\|_{L^2}
\]
for every $h\in L^2(\mathbb T)$.
In particular $g_x\in L^1$, so $\Phi(x)$ is finite.
Moreover, the reverse triangle inequality gives
\[
\bigl||g_x|-|g_y|\bigr|\le|g_x-g_y|.
\]
Therefore, using <1>5,
\[
\begin{aligned}
|\Phi(x)-\Phi(y)|
&\le
\int_0^{2\pi}|g_x-g_y|\,\frac{d\theta}{2\pi}\\
&\le\|g_x-g_y\|_{L^2}\\
&=\|x-y\|_{\ell^2}.
\end{aligned}
\]
Thus $\Phi$ is $1$-Lipschitz, hence continuous.
:::

<1>7. The functional $\Phi$ attains its maximum on $A$.
::: {.proof}
By <1>4, $A$ is compact, and by <1>6, $\Phi:A\to\mathbb R$ is continuous.
The extreme-value theorem therefore gives an element $x_\ast\in A$ such that
\[
\Phi(x_\ast)=\max_{x\in A}\Phi(x).
\]
This proves part (b).
:::
:::
