---
schema: qual/card@1
id: P-UCLAB17F-12
kind: problem
title: Arzela-Ascoli theorem on a compact metric space
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $X$ be compact metric and let $\mathcal F\subset C(X)$ be nonempty. Prove that $\mathcal F$ is compact in the supremum norm if and only if it is closed, bounded, and equicontinuous. Give precise definitions of all terms used.
:::

::: {.solution}

Write
$$
\|f\|_\infty
=
\sup_{x\in X}|f(x)|
$$
for the supremum norm on $C(X)$.
Because $X$ is compact and $f$ is continuous, this supremum is finite.

The meanings of the terms are:

- $\mathcal F$ is **closed** if every uniform limit in $C(X)$ of a sequence from $\mathcal F$ belongs to $\mathcal F$.
- $\mathcal F$ is **bounded** if there is $M<\infty$ such that
  $$
  \|f\|_\infty\le M
  $$
  for every $f\in\mathcal F$.
- $\mathcal F$ is **equicontinuous** if for every $x\in X$ and every $\varepsilon>0$ there exists $\delta>0$ such that
  $$
  d(x,y)<\delta
  $$
  implies
  $$
  |f(x)-f(y)|<\varepsilon
  $$
  for every $f\in\mathcal F$.
- $\mathcal F$ is **compact in the supremum norm** if it is compact as a metric space for
  $$
  d_\infty(f,g)=\|f-g\|_\infty.
  $$

::: pf

::: {.pf-step #s1-1}

Suppose $\mathcal F$ is compact in the supremum norm.
Then $\mathcal F$ is closed.


::: pf-proof

The metric space $C(X)$ with $d_\infty$ is Hausdorff.
Every compact subset of a Hausdorff space is closed.
Hence $\mathcal F$ is closed.

:::

:::

::: {.pf-step #s1-2}

If $\mathcal F$ is compact, then it is bounded.


::: pf-proof

Every compact metric space is bounded.
Thus there exist
$$
f_0\in\mathcal F
$$
and
$$
R<\infty
$$
such that
$$
\|f-f_0\|_\infty\le R
$$
for all $f\in\mathcal F$.
Then
$$
\|f\|_\infty
\le
\|f-f_0\|_\infty+\|f_0\|_\infty
\le
R+\|f_0\|_\infty.
$$
So $\mathcal F$ is bounded.

:::

:::

::: {.pf-step #s1-3}

If $\mathcal F$ is compact, then it is equicontinuous.


::: pf-proof

Suppose not.
Then there exist
$$
x_0\in X
$$
and
$$
\varepsilon_0>0
$$
such that for every positive integer $n$ there are
$$
f_n\in\mathcal F
$$
and
$$
y_n\in X
$$
with
$$
d(x_0,y_n)<\frac1n
$$
but
$$
|f_n(x_0)-f_n(y_n)|
\ge
\varepsilon_0.
$$

Compactness of $\mathcal F$ gives a subsequence
$$
f_{n_k}
$$
converging uniformly to some
$$
f\in\mathcal F.
$$
Also
$$
y_{n_k}\to x_0.
$$
Since $f$ is continuous,
$$
f(y_{n_k})\to f(x_0).
$$
Therefore
$$
\begin{aligned}
|f_{n_k}(x_0)-f_{n_k}(y_{n_k})|
&\le
|f_{n_k}(x_0)-f(x_0)|\\
&\quad+
|f(x_0)-f(y_{n_k})|\\
&\quad+
|f(y_{n_k})-f_{n_k}(y_{n_k})|.
\end{aligned}
$$
The first and third terms tend to zero by uniform convergence, and the middle term tends to zero by continuity of $f$.
Thus the left side tends to zero, contradicting its lower bound $\varepsilon_0$.
Hence $\mathcal F$ is equicontinuous.

:::

:::

::: {.pf-step #s1-4}

Thus compactness implies closedness, boundedness, and equicontinuity.


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Assume conversely that $\mathcal F$ is closed, bounded, and equicontinuous.
Then the equicontinuity is uniform in the following sense:
for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
d(x,y)<\delta
$$
implies
$$
|f(x)-f(y)|<\varepsilon
$$
for every
$$
f\in\mathcal F
$$
and every
$$
x,y\in X.
$$


::: pf-proof

Fix $\varepsilon>0$.
For each $x\in X$, equicontinuity gives $\eta_x>0$ such that
$$
d(x,y)<\eta_x
$$
implies
$$
|f(x)-f(y)|<\frac{\varepsilon}{2}
$$
for every $f\in\mathcal F$.
Set
$$
r_x=\frac{\eta_x}{2}.
$$
The balls
$$
B(x,r_x)
$$
cover $X$.
By compactness, choose a finite subcover
$$
B(x_1,r_{x_1}),\ldots,B(x_N,r_{x_N}).
$$
Let
$$
\delta
=
\min_{1\le j\le N}r_{x_j}
>
0.
$$

Suppose
$$
d(x,y)<\delta.
$$
Choose $j$ such that
$$
x\in B(x_j,r_{x_j}).
$$
Then
$$
d(x_j,x)<r_{x_j}
$$
and
$$
d(x_j,y)
\le
d(x_j,x)+d(x,y)
<
r_{x_j}+\delta
\le
2r_{x_j}
=
\eta_{x_j}.
$$
Thus for every $f\in\mathcal F$,
$$
|f(x)-f(x_j)|<\frac{\varepsilon}{2}
$$
and
$$
|f(y)-f(x_j)|<\frac{\varepsilon}{2}.
$$
Hence
$$
|f(x)-f(y)|<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-6}

The compact metric space $X$ has a countable dense subset.


::: pf-proof

For each positive integer $m$, compactness gives a finite
$$
\frac1m
\text{-net }
D_m\subseteq X.
$$
That is, every point of $X$ lies within distance $1/m$ of some point of $D_m$.
Then
$$
D=\bigcup_{m=1}^{\infty}D_m
$$
is countable.
It is dense because for every $x\in X$ and every radius $r>0$, choosing $m$ with
$$
\frac1m<r
$$
gives a point of $D_m$ inside $B(x,r)$.

:::

:::

::: {.pf-step #s1-7}

Let
$$
D=\{x_1,x_2,\ldots\}
$$
be a countable dense subset of $X$.
For any sequence
$$
(f_n)\subseteq\mathcal F,
$$
there exists a subsequence that converges at every point $x_j\in D$.


::: pf-proof

Because $\mathcal F$ is bounded, there exists $M$ such that
$$
|f(x)|\le M
$$
for all
$$
f\in\mathcal F
$$
and all
$$
x\in X.
$$
Thus
$$
(f_n(x_1))
$$
is a bounded sequence of real numbers.
Choose a convergent subsequence.

From that subsequence, choose a further subsequence whose values at $x_2$ converge.
Continue inductively.

Take the diagonal subsequence.
For each fixed $j$, its tail lies inside the $j$th selected subsequence, so its values at $x_j$ converge.

:::

:::

::: {.pf-step #s1-8}

The subsequence from step [](#s1-7){.pf-ref} is uniformly Cauchy.


::: pf-proof

Let
$$
(g_n)
$$
denote that subsequence.
Fix $\varepsilon>0$.
By step [](#s1-5){.pf-ref}, choose $\delta>0$ such that
$$
d(x,y)<\delta
$$
implies
$$
|f(x)-f(y)|<\frac{\varepsilon}{3}
$$
for every $f\in\mathcal F$.

Because $D$ is dense and $X$ is compact, choose finitely many points
$$
x_{j_1},\ldots,x_{j_r}\in D
$$
whose $\delta$-balls cover $X$.

For each $\ell$, the scalar sequence
$$
g_n(x_{j_\ell})
$$
converges, hence is Cauchy.
Since there are finitely many such points, choose $N$ such that for
$$
m,n\ge N
$$
and every $\ell$,
$$
|g_m(x_{j_\ell})-g_n(x_{j_\ell})|
<
\frac{\varepsilon}{3}.
$$

Now fix $x\in X$ and choose $\ell$ with
$$
d(x,x_{j_\ell})<\delta.
$$
Then
$$
\begin{aligned}
|g_m(x)-g_n(x)|
&\le
|g_m(x)-g_m(x_{j_\ell})|\\
&\quad+
|g_m(x_{j_\ell})-g_n(x_{j_\ell})|\\
&\quad+
|g_n(x_{j_\ell})-g_n(x)|\\
&<
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}
+
\frac{\varepsilon}{3}\\
&=
\varepsilon.
\end{aligned}
$$
Thus
$$
\|g_m-g_n\|_\infty<\varepsilon
$$
for all $m,n\ge N$.

:::

:::

::: {.pf-step #s1-9}

The space
$$
C(X)
$$
is complete in the supremum norm.


::: pf-proof

Let $(h_n)$ be uniformly Cauchy.
For each $x\in X$, the scalar sequence
$$
h_n(x)
$$
is Cauchy in $\RR$, hence converges.
Define
$$
h(x)=\lim_{n\to\infty}h_n(x).
$$

Given $\varepsilon>0$, choose $N$ such that
$$
\|h_m-h_n\|_\infty<\varepsilon
$$
for $m,n\ge N$.
Fix $n\ge N$ and let $m\to\infty$ pointwise.
Then
$$
|h(x)-h_n(x)|
\le
\varepsilon
$$
for every $x$, so
$$
\|h-h_n\|_\infty\le\varepsilon.
$$
Thus $h_n\to h$ uniformly.
A uniform limit of continuous functions is continuous, so
$$
h\in C(X).
$$
Therefore $C(X)$ is complete.

:::

:::

::: {.pf-step #s1-10}

The uniformly Cauchy subsequence from step [](#s1-8){.pf-ref} converges uniformly to some
$$
g\in C(X).
$$


::: pf-proof

Apply completeness of $C(X)$ from step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The limit $g$ belongs to $\mathcal F$.


::: pf-proof

Every term of the subsequence lies in $\mathcal F$, and the convergence is in the supremum norm.
Since $\mathcal F$ is closed, its uniform limit belongs to $\mathcal F$.

:::

:::

::: {.pf-step #s1-12}

Every sequence in $\mathcal F$ has a uniformly convergent subsequence whose limit belongs to $\mathcal F$.


::: pf-proof

Start with an arbitrary sequence in $\mathcal F$.
Step [](#s1-7){.pf-ref} gives a diagonally convergent subsequence, steps [](#s1-8){.pf-ref} through [](#s1-10){.pf-ref} show that this subsequence converges uniformly, and step [](#s1-11){.pf-ref} puts the limit in $\mathcal F$.

:::

:::

::: {.pf-step #s1-13}

Hence $\mathcal F$ is compact in the supremum norm.


::: pf-proof

In metric spaces, compactness is equivalent to sequential compactness.
Step [](#s1-12){.pf-ref} proves sequential compactness of $\mathcal F$.
Therefore $\mathcal F$ is compact.

:::

:::

::: {.pf-step #s1-14}

Therefore
$$
\boxed{
\mathcal F\text{ is compact in }\|\cdot\|_\infty
\iff
\mathcal F\text{ is closed, bounded, and equicontinuous}.
}
$$


::: pf-proof

Step [](#s1-4){.pf-ref} proves the forward implication, and steps [](#s1-5){.pf-ref} through [](#s1-13){.pf-ref} prove the reverse implication.

:::

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the stated Arzelà--Ascoli theorem, with all terms defined at the start of the solution.

:::

:::

:::
