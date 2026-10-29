---
schema: qual/card@1
id: P-UCLAB17S-11
kind: problem
title: Pointwise convergence of a subsequence of primitives
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let $f_n:[0,1]\to\RR$ be continuous and satisfy
$$
|f_n(x)|\le 1+\frac{n}{1+n^2x^2}.
$$
Define $F_n(x)=\int_0^x f_n(t)\,dt$. Show that there is a subsequence $n_k\to\infty$ such that $F_{n_k}(x)$ converges for every $x\in[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every
$$
n
$$
and
$$
x\in[0,1],
$$
one has
$$
|F_n(x)|
\le
1+\frac{\pi}{2}.
$$


::: pf-proof

By hypothesis,
$$
|f_n(t)|
\le
1+\frac{n}{1+n^2t^2}.
$$
Therefore
$$
\begin{aligned}
|F_n(x)|
&\le
\int_0^x|f_n(t)|\,dt\\
&\le
\int_0^1
\left(
1+\frac{n}{1+n^2t^2}
\right)dt\\
&=
1
+
\int_0^n
\frac{du}{1+u^2}\\
&=
1+\arctan n\\
&\le
1+\frac{\pi}{2}.
\end{aligned}
$$
The substitution is
$$
u=nt.
$$

:::

:::

::: {.pf-step #s1-2}

Fix a positive integer $m$ and consider the interval
$$
K_m=\left[\frac1m,1\right].
$$
For every $n$ and every $t\in K_m$,
$$
\frac{n}{1+n^2t^2}
\le
\frac m2.
$$


::: pf-proof

For every positive real number $u$,
$$
1+u^2\ge2u.
$$
Set
$$
u=nt.
$$
Then
$$
\frac{n}{1+n^2t^2}
\le
\frac{n}{2nt}
=
\frac1{2t}.
$$
Since
$$
t\ge\frac1m,
$$
one has
$$
\frac1{2t}\le\frac m2.
$$

:::

:::

::: {.pf-step #s1-3}

On $K_m$, the family $(F_n)$ is equi-Lipschitz:
$$
\boxed{
|F_n(x)-F_n(y)|
\le
\left(1+\frac m2\right)|x-y|.
}
$$


::: pf-proof

For
$$
x,y\in K_m,
$$
assume without loss of generality that
$$
x<y.
$$
Then
$$
\begin{aligned}
|F_n(y)-F_n(x)|
&=
\left|
\int_x^y f_n(t)\,dt
\right|\\
&\le
\int_x^y
|f_n(t)|\,dt.
\end{aligned}
$$
By the hypothesis and step [](#s1-2){.pf-ref},
$$
|f_n(t)|
\le
1+\frac m2
$$
on $K_m$.
Thus
$$
|F_n(y)-F_n(x)|
\le
\left(1+\frac m2\right)(y-x).
$$

:::

:::

::: {.pf-step #s1-4}

For each fixed $m$, every sequence $(F_n)$ has a subsequence converging uniformly on
$$
K_m.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the family is uniformly bounded on $K_m$.
By step [](#s1-3){.pf-ref}, it is equicontinuous there.
The interval $K_m$ is compact.
Apply the Arzelà--Ascoli theorem.

:::

:::

::: pf-step

Choose a subsequence
$$
(F_{n^{(1)}_k})
$$
that converges uniformly on
$$
K_1=[1,1].
$$
From it choose a subsequence
$$
(F_{n^{(2)}_k})
$$
that converges uniformly on
$$
K_2.
$$
Continue inductively so that the stage-$m$ subsequence converges uniformly on $K_m$.


::: pf-proof

At each stage, apply step [](#s1-4){.pf-ref} to the subsequence obtained at the previous stage.
Because
$$
K_m\subseteq K_{m+1},
$$
the process enlarges the interval on which convergence is ensured while retaining convergence on earlier intervals.

:::

:::

::: {.pf-step #s1-6}

Define the diagonal subsequence
$$
\boxed{
n_k=n^{(k)}_k.
}
$$
Then for every fixed $m$,
$$
F_{n_k}
$$
converges uniformly on $K_m$ as
$$
k\to\infty.
$$


::: pf-proof

For
$$
k\ge m,
$$
the stage-$k$ subsequence is nested inside the stage-$m$ subsequence.
Thus the tail of the diagonal subsequence is a subsequence of the sequence that converges uniformly on $K_m$.
Every subsequence of a uniformly convergent sequence converges uniformly to the same limit on that set.

:::

:::

::: {.pf-step #s1-7}

For every
$$
x\in(0,1],
$$
the scalar sequence
$$
F_{n_k}(x)
$$
converges.


::: pf-proof

Choose
$$
m
$$
so large that
$$
\frac1m\le x.
$$
Then
$$
x\in K_m.
$$
By step [](#s1-6){.pf-ref},
$$
F_{n_k}
$$
converges uniformly on $K_m$, hence in particular pointwise at $x$.

:::

:::

::: {.pf-step #s1-8}

At the remaining point,
$$
x=0,
$$
one has
$$
F_n(0)=0
$$
for every $n$.


::: pf-proof

By definition,
$$
F_n(0)
=
\int_0^0f_n(t)\,dt
=0.
$$
Thus the sequence converges at $0$ as well.

:::

:::

::: {.pf-step #s1-9}

Therefore there exists a subsequence
$$
\boxed{n_k\to\infty}
$$
such that
$$
\boxed{
F_{n_k}(x)
\text{ converges for every }x\in[0,1].
}
$$


::: pf-proof

Step [](#s1-7){.pf-ref} handles every positive $x$, and step [](#s1-8){.pf-ref} handles $x=0$.
The indices $n_k$ form a subsequence of the positive integers and may be chosen strictly increasing at each extraction stage.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
