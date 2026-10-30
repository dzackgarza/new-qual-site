---
schema: qual/card@1
id: P-UCLARA14F-10
kind: problem
title: Completeness of the Fock space of entire functions
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Integral Formula
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 10 on page 2 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let us introduce a vector space $\mathcal{B}$ defined as follows,
$$
\mathcal{B} = \left\{ u : \CC \to \CC, \ u \text{ is holomorphic and } \iint_{\CC} \abs{u(x+iy)}^2 e^{-(x^2+y^2)}\,dx\,dy < \infty \right\}.
$$
Show that $\mathcal{B}$ becomes a *complete* space when equipped with the norm
$$
\norm{u}^2 = \iint_{\CC} \abs{u(x+iy)}^2 e^{-(x^2+y^2)}\,dx\,dy.
$$
:::

::: {.solution}

Let
$$
d\mu(z)=e^{-\abs{z}^2}\,dA(z),
$$
where $dA=dx\,dy$ is planar Lebesgue measure.

::: pf

::: {.pf-step #s1-1}

The ambient space
$$
L^2(\CC,\mu)
$$
is a Hilbert space, and
$$
\mathcal B\subseteq L^2(\CC,\mu)
$$
is a linear subspace.


::: pf-proof

The measure $\mu$ is positive and $\sigma$-finite; in fact
$$
\mu(\CC)
=
\int_{\CC}e^{-\abs{z}^2}\,dA(z)
=\pi<\infty.
$$
Thus the usual $L^2$ completeness theorem applies. Sums and scalar
multiples of entire functions are entire, so $\mathcal B$ is linear.

:::

:::

::: pf-step

Fix a compact set $K\subset\CC$ and define
$$
K_1
=
\{w\in\CC:\operatorname{dist}(w,K)\le1\}.
$$
Then there exists a constant $c_K>0$ such that
$$
e^{-\abs{w}^2}\ge c_K
\qquad(w\in K_1).
$$


::: pf-proof

The set $K_1$ is compact. The positive continuous function
$$
w\longmapsto e^{-\abs{w}^2}
$$
therefore attains a positive minimum on $K_1$.

:::

:::

::: {.pf-step #s1-3}

If $h$ is entire, then
$$
\boxed{
\sup_{z\in K}\abs{h(z)}
\le
\frac1{\sqrt{\pi c_K}}
\norm{h}_{L^2(\mu)}}.
$$


::: pf-proof

Fix $z\in K$. The closed unit disk centered at $z$ lies in $K_1$. By the
area mean-value formula for holomorphic functions,
$$
h(z)
=
\frac1\pi
\int_{D(z,1)}h(w)\,dA(w).
$$
Hence
$$
\begin{aligned}
\abs{h(z)}
&\le
\frac1\pi
\int_{D(z,1)}\abs{h(w)}\,dA(w)\\
&\le
\frac1\pi
\bigl(\pi\bigr)^{1/2}
\left(
\int_{D(z,1)}\abs{h(w)}^2\,dA(w)
\right)^{1/2}\\
&\le
\frac1{\sqrt\pi}
\left(
\frac1{c_K}
\int_{D(z,1)}
\abs{h(w)}^2e^{-\abs{w}^2}\,dA(w)
\right)^{1/2}\\
&\le
\frac1{\sqrt{\pi c_K}}
\norm{h}_{L^2(\mu)}.
\end{aligned}
$$
The bound is independent of $z\in K$, so taking the supremum gives the
claim.

:::

:::

::: {.pf-step #s1-4}

Every norm-Cauchy sequence $(f_n)$ in $\mathcal B$ is locally
uniformly Cauchy on $\CC$.


::: pf-proof

For any compact $K$ and any $n,m$, step [](#s1-3){.pf-ref} applied to the entire function
$$
h=f_n-f_m
$$
gives
$$
\sup_K\abs{f_n-f_m}
\le
C_K\norm{f_n-f_m}_{L^2(\mu)}.
$$
Since $(f_n)$ is Cauchy in the given norm, the right-hand side tends to zero
as $n,m\to\infty$. Thus $(f_n)$ is uniformly Cauchy on every compact set.

:::

:::

::: {.pf-step #s1-5}

There exists an entire function $g$ such that
$$
f_n\to g
$$
locally uniformly on $\CC$.


::: pf-proof

By step [](#s1-4){.pf-ref}, on each compact disk the sequence is uniformly Cauchy, hence
uniformly convergent to a continuous limit. These local limits agree on
overlaps, producing a function $g$ on $\CC$. The Weierstrass theorem
for locally uniform limits of holomorphic functions shows that $g$ is
entire.

:::

:::

::: pf-step

Since $L^2(\mu)$ is complete, there exists
$$
f\in L^2(\mu)
$$
such that
$$
f_n\to f
$$
in $L^2(\mu)$.


::: pf-proof

This follows from step [](#s1-1){.pf-ref} because $(f_n)$ is norm-Cauchy in the ambient
complete space.

:::

:::

::: {.pf-step #s1-7}

The functions $f$ and $g$ agree $\mu$-almost everywhere.


::: pf-proof

From convergence in $L^2(\mu)$, choose a subsequence
$$
f_{n_j}
$$
that converges pointwise $\mu$-almost everywhere to $f$. On the other hand,
step [](#s1-5){.pf-ref} gives
$$
f_{n_j}(z)\to g(z)
$$
for every $z\in\CC$. Hence
$$
f=g
$$
almost everywhere.

:::

:::

::: {.pf-step #s1-8}

The $L^2(\mu)$ limit belongs to $\mathcal B$.


::: pf-proof

By step [](#s1-7){.pf-ref}, the equivalence class $f$ has the entire representative $g$.
Also
$$
\norm{g}_{L^2(\mu)}
=
\norm{f}_{L^2(\mu)}
<\infty.
$$
Thus $g\in\mathcal B$, and
$$
\norm{f_n-g}_{L^2(\mu)}
=
\norm{f_n-f}_{L^2(\mu)}
\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{\mathcal B\text{ is complete in the stated norm}}.
$$


::: pf-proof

Every Cauchy sequence in $\mathcal B$ converges in the norm to an element of
$\mathcal B$ by steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref}. Hence $\mathcal B$ is a closed
subspace of the Hilbert space $L^2(\mu)$ and is itself complete.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
