---
schema: qual/card@1
id: P-UCLARA11S-01
kind: problem
title: Weak $L^2$ convergence implies uniform convergence of primitives
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
(a) Define what it means to say that $f_n\to f$ weakly in $L^2([0,1])$.

(b) Suppose $f_n\in L^2([0,1])$ converge weakly to $f\in L^2([0,1])$, and define
$$
F_n(x)=\int_0^x f_n(t)\,dt,
\qquad
F(x)=\int_0^x f(t)\,dt.
$$
Show that $F_n,F\in C([0,1])$ and that $F_n\to F$ uniformly on $[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The statement
$$
f_n\rightharpoonup f
\quad\text{in }L^2([0,1])
$$
means that for every $g\in L^2([0,1])$,
$$
\int_0^1 f_n(t)g(t)\,dt
\longrightarrow
\int_0^1 f(t)g(t)\,dt.
$$


::: pf-proof

This is the definition of weak convergence in the Hilbert space $L^2([0,1])$, identifying its continuous dual with itself via the inner product.

:::

:::

::: pf-step

There is a constant $M<\infty$ such that
$$
\|f_n\|_2\le M
\qquad
(n\ge1).
$$


::: pf-proof

Every weakly convergent sequence in a Banach space is norm bounded. Apply this standard consequence of the uniform boundedness principle to $(f_n)$.

:::

:::

::: {.pf-step #s1-3}

The functions $F_n$ and $F$ are continuous on $[0,1]$, and $(F_n)$ is equicontinuous.


::: pf-proof

For $0\le x<y\le1$, Cauchy--Schwarz gives
$$
\begin{aligned}
|F_n(y)-F_n(x)|
&=
\left|
\int_x^y f_n(t)\,dt
\right|\\
&\le
\left(
\int_x^y|f_n(t)|^2\,dt
\right)^{1/2}
|y-x|^{1/2}\\
&\le
M|y-x|^{1/2}.
\end{aligned}
$$
The bound is independent of $n$, so $(F_n)$ is equicontinuous. The same estimate with $f$ in place of $f_n$ gives continuity of $F$.

:::

:::

::: {.pf-step #s1-4}

The family $(F_n)$ is uniformly bounded on $[0,1]$.


::: pf-proof

For every $x\in[0,1]$,
$$
|F_n(x)|
\le
\int_0^x|f_n(t)|\,dt
\le
\|f_n\|_2 x^{1/2}
\le
M.
$$

:::

:::

::: {.pf-step #s1-5}

For every fixed $x\in[0,1]$,
$$
F_n(x)\longrightarrow F(x).
$$


::: pf-proof

The characteristic function
$$
\mathbf 1_{[0,x]}
$$
belongs to $L^2([0,1])$. Weak convergence therefore gives
$$
\begin{aligned}
F_n(x)
&=
\int_0^1
f_n(t)\mathbf 1_{[0,x]}(t)\,dt\\
&\longrightarrow
\int_0^1
f(t)\mathbf 1_{[0,x]}(t)\,dt\\
&=
F(x).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

One has
$$
\boxed{
F_n\longrightarrow F
\text{ uniformly on }[0,1].
}
$$


::: pf-proof

Suppose uniform convergence failed. Then there would exist $\varepsilon>0$ and a subsequence $(F_{n_k})$ such that
$$
\|F_{n_k}-F\|_\infty\ge\varepsilon
\qquad
(k\ge1).
$$

By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, the subsequence is uniformly bounded and equicontinuous. Arzelà--Ascoli therefore gives a further subsequence converging uniformly on $[0,1]$ to some continuous function $G$.

But step [](#s1-5){.pf-ref} gives pointwise convergence of the full sequence to $F$, so the same further subsequence converges pointwise to $F$. Hence
$$
G=F.
$$
Thus the further subsequence converges uniformly to $F$, contradicting
$$
\|F_{n_k}-F\|_\infty\ge\varepsilon.
$$
Therefore the full sequence converges uniformly.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), while steps [](#s1-3){.pf-ref} and [](#s1-6){.pf-ref} prove part (b).

:::

:::

:::
