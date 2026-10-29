---
schema: qual/card@1
id: P-UCLARA16S-08
kind: problem
title: Normal families of holomorphic self-maps of the upper half-plane
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $\CC_+=\{z\in\CC:\operatorname{Im}z>0\}$ and let $f_n:\CC_+\to\CC_+$ be a sequence of holomorphic functions. Show that unless $|f_n|\to\infty$ uniformly on compact subsets of $\CC_+$, there exists a subsequence converging uniformly on compact subsets of $\CC_+$.
:::

::: {.solution}

Let
\[
\Phi(w)
\coloneqq
\frac{w-i}{w+i},
\qquad
\Phi^{-1}(\zeta)
=
i\frac{1+\zeta}{1-\zeta}.
\]
Then $\Phi$ is a biholomorphism from $\CC_+$ onto the unit disk $\DD$.

::: pf

::: {.pf-step #s1-1}

Since $|f_n|$ does not tend to infinity uniformly on compact subsets, there exist a compact set $K\subset\CC_+$, a constant $M>0$, a subsequence $(f_{n_j})$, and points $z_j\in K$ such that
\[
|f_{n_j}(z_j)|\le M
\qquad
(j\ge1).
\]


::: pf-proof

Failure of uniform divergence on compact subsets means that for some compact $K\subset\CC_+$ there is a number $M>0$ such that, for infinitely many indices $n$, the inequality
\[
|f_n(z)|>M
\qquad
(z\in K)
\]
fails. Select those indices as $n_j$ and choose $z_j\in K$ at which it fails.

:::

:::

::: pf-step

After passing to a further subsequence, the functions
\[
g_j
\coloneqq
\Phi\circ f_{n_j}:\CC_+\to\DD
\]
converge uniformly on compact subsets of $\CC_+$ to a holomorphic function $g:\CC_+\to\overline{\DD}$, and the points $z_j$ converge to some $z_\infty\in K$.


::: pf-proof

The family $(g_j)$ is uniformly bounded by $1$, so Montel's theorem gives a locally uniformly convergent subsequence. Relabel it as $(g_j)$. Since $K$ is compact, the associated sequence $(z_j)$ has a convergent subsequence; pass to it as well and write its limit as $z_\infty\in K$. Local uniform limits of holomorphic functions are holomorphic.

:::

:::

::: {.pf-step #s1-3}

The limit function $g$ is not identically equal to $1$.


::: pf-proof

For every $w\in\CC_+$,
\[
1-\Phi(w)
=
\frac{2i}{w+i},
\]
so
\[
|1-\Phi(w)|
=
\frac{2}{|w+i|}.
\]
By step [](#s1-1){.pf-ref},
\[
|1-g_j(z_j)|
=
\frac{2}{|f_{n_j}(z_j)+i|}
\ge
\frac{2}{M+1}.
\]
Because $z_j\to z_\infty$ and $g_j\to g$ locally uniformly, one has
\[
g_j(z_j)\longrightarrow g(z_\infty).
\]
Hence
\[
|1-g(z_\infty)|
\ge
\frac{2}{M+1}>0.
\]
Thus $g(z_\infty)\ne1$, so $g$ is not the constant function $1$.

:::

:::

::: {.pf-step #s1-4}

The function $g$ never takes the value $1$ on $\CC_+$.


::: pf-proof

The limit satisfies $|g|\le1$. If $g(z_0)=1$ at some interior point, then $|g|$ attains its maximum value $1$ at $z_0$. The maximum-modulus principle would force $g\equiv1$, contradicting step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The subsequence $(f_{n_j})$ converges uniformly on compact subsets of $\CC_+$.


::: pf-proof

Let $L\subset\CC_+$ be compact. By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, the continuous function $1-g$ has no zeros on $L$. Hence
\[
\delta
\coloneqq
\min_{z\in L}|1-g(z)|>0.
\]
For all sufficiently large $j$, local uniform convergence gives
\[
|1-g_j(z)|
\ge
\frac{\delta}{2}
\qquad
(z\in L).
\]
Since
\[
f_{n_j}
=
\Phi^{-1}(g_j)
=
i\frac{1+g_j}{1-g_j},
\]
and the rational function
\[
\zeta\longmapsto i\frac{1+\zeta}{1-\zeta}
\]
is uniformly continuous on a neighborhood of the compact set $g(L)$ that stays a positive distance from $1$, the convergence $g_j\to g$ on $L$ implies
\[
f_{n_j}
\longrightarrow
i\frac{1+g}{1-g}
\]
uniformly on $L$. Since $L$ was arbitrary, the convergence is uniform on compact subsets of $\CC_+$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required locally uniformly convergent subsequence.

:::

:::

:::
