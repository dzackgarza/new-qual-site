---
schema: qual/card@1
id: P-UCLARA16F-03
kind: problem
title: Weak-star lower semicontinuity and minimizers of the Coulomb energy
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
If $X$ is a compact metric space, denote by $P(X)$ the set of positive Borel measures $\mu$ on $X$ with $\mu(X)=1$.

(a) Let $\phi:X\to[0,\infty]$ be a lower-semicontinuous function on a compact metric space $X$.
Show that if $\mu$ and $\mu_n$, for $n\in\NN$, are in $P(X)$ and $\mu_n\to\mu$ with respect to the weak-star topology on $P(X)$, then
\[
\int \phi\,d\mu\le \liminf_{n\to\infty}\int \phi\,d\mu_n.
\]

(b) Let $K\subset\RR^d$ be compact.
For $\mu\in P(K)$ define
\[
E(\mu)=\int_K\int_K\frac{1}{|x-y|}\,d\mu(x)\,d\mu(y).
\]
Here $|z|$ denotes the Euclidean norm of $z\in\RR^d$.
Show that $E:P(K)\to[0,\infty]$ attains its minimum on $P(K)$ (which could possibly be $\infty$).
:::

::: {.solution}

## Part (a)

Let
\[
\phi:X\to[0,\infty]
\]
be lower semicontinuous.

For each integer \(m\ge1\), define
\[
\boxed{
\phi_m(x)
=
\min\left\{
m,\
\inf_{y\in X}
\bigl(
\phi(y)+m\,d(x,y)
\bigr)
\right\}.}
\]

::: pf

::: {.pf-step #s1-1}

For every \(m\),
\[
\boxed{0\le \phi_m\le m}.
\]


::: pf-proof

The function \(\phi\) is nonnegative, and the distance term is nonnegative, so the infimum is nonnegative. The outer minimum bounds \(\phi_m\) by \(m\).

:::

:::

::: {.pf-step #s1-2}

For every \(x\in X\),
\[
\boxed{\phi_m(x)\le\phi(x)}.
\]


::: pf-proof

In the infimum defining \(\phi_m(x)\), choose \(y=x\). Then
\[
\inf_y
\bigl(
\phi(y)+m d(x,y)
\bigr)
\le
\phi(x).
\]
Taking the minimum with \(m\) preserves the inequality.

:::

:::

::: {.pf-step #s1-3}

The function \(\phi_m\) is \(m\)-Lipschitz and hence continuous.


::: pf-proof

Set
\[
g_m(x)
=
\inf_{y\in X}
\bigl(
\phi(y)+m d(x,y)
\bigr).
\]
For \(x,x'\in X\), the triangle inequality gives
\[
d(x,y)
\le
d(x,x')+d(x',y),
\]
so
\[
\phi(y)+m d(x,y)
\le
m d(x,x')
+
\phi(y)+m d(x',y).
\]
Taking infima in \(y\),
\[
g_m(x)
\le
m d(x,x')+g_m(x').
\]
Interchanging \(x,x'\) yields
\[
|g_m(x)-g_m(x')|
\le
m d(x,x').
\]
The map
\[
t\mapsto\min\{m,t\}
\]
is \(1\)-Lipschitz, so
\[
\phi_m=\min\{m,g_m\}
\]
is also \(m\)-Lipschitz.

:::

:::

::: {.pf-step #s1-4}

The sequence \((\phi_m)\) is pointwise nondecreasing.


::: pf-proof

If \(m_2\ge m_1\), then for every \(y\),
\[
\phi(y)+m_2 d(x,y)
\ge
\phi(y)+m_1 d(x,y).
\]
Hence
\[
g_{m_2}(x)\ge g_{m_1}(x),
\]
and also
\[
m_2\ge m_1.
\]
Therefore
\[
\min\{m_2,g_{m_2}(x)\}
\ge
\min\{m_1,g_{m_1}(x)\}.
\]

:::

:::

::: {.pf-step #s1-5}

If \(\phi(x)<\infty\), then
\[
\boxed{\phi_m(x)\to\phi(x)}.
\]


::: pf-proof

By step [](#s1-2){.pf-ref},
\[
\phi_m(x)\le\phi(x),
\]
and by step [](#s1-4){.pf-ref} the limit
\[
L=\lim_m\phi_m(x)
\]
exists with \(L\le\phi(x)\).

Suppose
\[
L<\phi(x).
\]
Choose \(\varepsilon>0\) such that
\[
L+2\varepsilon<\phi(x).
\]
For arbitrarily large \(m\), choose \(y_m\in X\) with
\[
\phi(y_m)+m d(x,y_m)
<
\phi_m(x)+\varepsilon
\le
L+\varepsilon.
\]
Since \(\phi(y_m)\ge0\),
\[
d(x,y_m)
\le
\frac{L+\varepsilon}{m}
\to0.
\]
Thus \(y_m\to x\). Lower semicontinuity gives
\[
\phi(x)
\le
\liminf_m\phi(y_m)
\le
L+\varepsilon,
\]
contradicting
\[
L+2\varepsilon<\phi(x).
\]
Hence \(L=\phi(x)\).

:::

:::

::: {.pf-step #s1-6}

If \(\phi(x)=+\infty\), then
\[
\boxed{\phi_m(x)\to+\infty}.
\]


::: pf-proof

Suppose instead that \(\phi_m(x)\) remains bounded along some sequence \(m_j\to\infty\):
\[
\phi_{m_j}(x)\le M.
\]
For \(m_j>M+1\), the outer minimum cannot be attained at \(m_j\), so choose \(y_j\) such that
\[
\phi(y_j)+m_jd(x,y_j)
\le
M+1.
\]
Then
\[
d(x,y_j)
\le
\frac{M+1}{m_j}
\to0,
\]
so \(y_j\to x\). Also
\[
\phi(y_j)\le M+1.
\]
Lower semicontinuity would imply
\[
\phi(x)
\le
\liminf_j\phi(y_j)
\le
M+1,
\]
contradicting \(\phi(x)=+\infty\).

:::

:::

::: {.pf-step #s1-7}

Therefore
\[
\boxed{\phi_m\uparrow\phi}
\]
pointwise on \(X\).


::: pf-proof

Monotonicity is step [](#s1-4){.pf-ref}, and pointwise convergence is steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

For each fixed \(m\),
\[
\boxed{
\int_X\phi_m\,d\mu_n
\longrightarrow
\int_X\phi_m\,d\mu}.
\]


::: pf-proof

The function \(\phi_m\) is bounded and continuous by steps [](#s1-1){.pf-ref} and [](#s1-3){.pf-ref}. Weak-star convergence of probability measures is exactly convergence against continuous functions.

:::

:::

::: {.pf-step #s1-9}

Since
\[
\phi_m\le\phi,
\]
one has
\[
\int_X\phi_m\,d\mu_n
\le
\int_X\phi\,d\mu_n.
\]


::: pf-proof

Integrate the pointwise inequality from step [](#s1-2){.pf-ref} against the positive measure \(\mu_n\).

:::

:::

::: {.pf-step #s1-10}

Hence
\[
\boxed{
\int_X\phi_m\,d\mu
\le
\liminf_{n\to\infty}
\int_X\phi\,d\mu_n}.
\]


::: pf-proof

Take \(n\to\infty\) in step [](#s1-9){.pf-ref} and use step [](#s1-8){.pf-ref} on the left.

:::

:::

::: {.pf-step #s1-11}

By monotone convergence,
\[
\boxed{
\int_X\phi\,d\mu
=
\lim_{m\to\infty}
\int_X\phi_m\,d\mu}.
\]


::: pf-proof

Use step [](#s1-7){.pf-ref} and the monotone convergence theorem.

:::

:::

::: {.pf-step #s1-12}

Therefore
\[
\boxed{
\int_X\phi\,d\mu
\le
\liminf_{n\to\infty}
\int_X\phi\,d\mu_n}.
\]


::: pf-proof

The right-hand side of step [](#s1-10){.pf-ref} is independent of \(m\). Let \(m\to\infty\) and use step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

The space \(P(K)\) is compact in the weak-star topology.


::: pf-proof

Identify finite signed Borel measures on \(K\) with the dual \(C(K)^*\) by the Riesz representation theorem. Probability measures lie in the weak-star compact unit ball of \(C(K)^*\) by Banach--Alaoglu.

They form a weak-star closed subset: positivity is preserved under weak-star limits because
\[
\int g\,d\mu\ge0
\]
for every continuous \(g\ge0\), and total mass is preserved because
\[
\mu(K)=\int1\,d\mu.
\]
Therefore \(P(K)\) is weak-star compact.

:::

:::

::: {.pf-step #s1-14}

The function
\[
\kappa:K\times K\to[0,\infty]
\]
is lower semicontinuous.


::: pf-proof

Off the diagonal it is continuous. If
\[
(x_n,y_n)\to(x,x)
\]
on the diagonal, then
\[
|x_n-y_n|\to0,
\]
so
\[
\kappa(x_n,y_n)\to+\infty.
\]
Thus the lower-semicontinuity inequality also holds on the diagonal.

:::

:::

::: {.pf-step #s1-15}

If
\[
\mu_n\overset{*}{\rightharpoonup}\mu
\]
in \(P(K)\), then
\[
\boxed{
\mu_n\otimes\mu_n
\overset{*}{\rightharpoonup}
\mu\otimes\mu}
\]
in \(P(K\times K)\).


::: pf-proof

First consider a product function
\[
G(x,y)=a(x)b(y)
\]
with \(a,b\in C(K)\). Then
\[
\int_{K\times K}G\,d(\mu_n\otimes\mu_n)
=
\left(
\int_K a\,d\mu_n
\right)
\left(
\int_K b\,d\mu_n
\right),
\]
which converges to
\[
\left(
\int_K a\,d\mu
\right)
\left(
\int_K b\,d\mu
\right)
=
\int_{K\times K}G\,d(\mu\otimes\mu).
\]

Finite linear combinations of product functions form a subalgebra of \(C(K\times K)\) that contains the constants and separates points. By Stone--Weierstrass, they are uniformly dense in \(C(K\times K)\).

Since all the product measures have total mass \(1\), uniform approximation transfers convergence from the dense algebra to every continuous \(G\in C(K\times K)\). Hence the product measures converge weak-star.

:::

:::

::: pf-step

The energy can be written as
\[
\boxed{
E(\mu)
=
\int_{K\times K}
\kappa(x,y)\,
d(\mu\otimes\mu)(x,y)}.
\]


::: pf-proof

This is exactly the iterated-integral definition of \(E\), interpreted by Tonelli's theorem for the nonnegative kernel.

:::

:::

::: {.pf-step #s1-17}

The functional \(E\) is weak-star lower semicontinuous on \(P(K)\).


::: pf-proof

Let
\[
\mu_n\overset{*}{\rightharpoonup}\mu.
\]
By step [](#s1-15){.pf-ref},
\[
\mu_n\otimes\mu_n
\overset{*}{\rightharpoonup}
\mu\otimes\mu.
\]
Apply part (a), step [](#s1-12){.pf-ref}, on the compact metric space \(K\times K\) with the nonnegative lower-semicontinuous function \(\kappa\) from step [](#s1-14){.pf-ref}:
\[
E(\mu)
\le
\liminf_{n\to\infty}E(\mu_n).
\]

:::

:::

::: {.pf-step #s1-18}

Choose a minimizing sequence
\[
(\mu_n)\subseteq P(K)
\]
such that
\[
\boxed{
E(\mu_n)\to m}.
\]


::: pf-proof

If \(m<\infty\), choose \(\mu_n\) with
\[
E(\mu_n)<m+\frac1n.
\]
If \(m=\infty\), every probability measure has infinite energy, so any sequence may be chosen.

:::

:::

::: pf-step

By compactness of \(P(K)\), after passing to a subsequence,
\[
\boxed{
\mu_n\overset{*}{\rightharpoonup}\mu}
\]
for some \(\mu\in P(K)\).


::: pf-proof

Apply step [](#s1-13){.pf-ref}.

:::

:::

::: {.pf-step #s1-20}

Lower semicontinuity gives
\[
E(\mu)
\le
\liminf_{n\to\infty}E(\mu_n)
=
m.
\]


::: pf-proof

Use step [](#s1-17){.pf-ref} and the minimizing property from step [](#s1-18){.pf-ref}.

:::

:::

::: {.pf-step #s1-21}

By definition of the infimum,
\[
m\le E(\mu).
\]


::: pf-proof

The measure \(\mu\) belongs to \(P(K)\).

:::

:::

::: {.pf-step #s1-22}

Therefore
\[
\boxed{E(\mu)=m}.
\]


::: pf-proof

Combine steps [](#s1-20){.pf-ref} through [](#s1-21){.pf-ref}.

:::

:::

::: {.pf-step #s1-23}

Hence \(E\) attains its minimum on \(P(K)\), possibly with value \(+\infty\).


::: pf-proof

Step [](#s1-22){.pf-ref} constructs a minimizer.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} proves part (a), and step [](#s1-23){.pf-ref} proves part (b).

:::

:::

:::
