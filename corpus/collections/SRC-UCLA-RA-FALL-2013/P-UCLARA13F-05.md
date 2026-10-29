---
schema: qual/card@1
id: P-UCLARA13F-05
kind: problem
title: '$L^1$-bounded holomorphic functions on the disk form a normal family'
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Let $(f_n)$ be holomorphic functions on $\DD$ satisfying
$$
\int_{\DD}|f_n(z)|\,d\lambda(z)\le1
$$
for every $n$.
Show that some subsequence converges uniformly on every compact subset of $\DD$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Fix $0<r<R<1$. For every $z$ with $|z|\leq r$, the disk
$$
D(z,R-r)
$$
is contained in $\DD$.


::: pf-proof

If $|w-z|<R-r$, then
$$
|w|\leq|z|+|w-z|<r+(R-r)=R<1.
$$

:::

:::

::: {.pf-step #s1-2}

Since $|f_n|$ is subharmonic, the sub-mean inequality gives
$$
|f_n(z)|
\leq\frac1{\pi(R-r)^2}
\int_{D(z,R-r)}|f_n(w)|\,d\lambda(w).
$$


::: pf-proof

The modulus of a holomorphic function is subharmonic. Apply its mean-value inequality over the disk from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Therefore, uniformly in $n$,
$$
\sup_{|z|\leq r}|f_n(z)|
\leq\frac1{\pi(R-r)^2}.
$$


::: pf-proof

The integral over the smaller disk in step [](#s1-2){.pf-ref} is at most
$$
\int_{\DD}|f_n(w)|\,d\lambda(w)\leq1
$$
by hypothesis.

:::

:::

::: pf-step

Thus the family $\{f_n\}$ is locally uniformly bounded on $\DD$.


::: pf-proof

Every compact $K\subset\DD$ is contained in some closed disk $\{|z|\leq r\}$ with $r<1$. Choose $R$ with $r<R<1$ and apply step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Fix $0<r<R<1$. Cauchy's estimate gives a constant $C_{r,R}$ independent of $n$ such that
$$
\sup_{|z|\leq r}|f_n'(z)|\leq C_{r,R}.
$$


::: pf-proof

Choose $r<R_1<R<1$. Step [](#s1-3){.pf-ref} gives a uniform bound $M$ for $|f_n|$ on $|z|\leq R_1$. For $|z|\leq r$, the circle of radius $R_1-r$ about $z$ lies in $|w|<R_1$. Cauchy's derivative estimate gives
$$
|f_n'(z)|\leq \frac{M}{R_1-r},
$$
which is independent of $n$.

:::

:::

::: {.pf-step #s1-6}

On every closed disk $\{|z|\leq r\}$, the sequence $(f_n)$ is uniformly bounded and equicontinuous.


::: pf-proof

Uniform boundedness is step [](#s1-3){.pf-ref}. The derivative bound in step [](#s1-5){.pf-ref} and the line-segment integral formula give
$$
|f_n(z)-f_n(w)|\leq C_{r,R}|z-w|
$$
for points in a slightly smaller convex disk, yielding equicontinuity.

:::

:::

::: pf-step

For each integer $k\geq2$, let
$$
K_k=\{z:|z|\leq1-1/k\}.
$$
By Arzela--Ascoli, every subsequence of $(f_n)$ has a further subsequence converging uniformly on $K_k$.


::: pf-proof

Each $K_k$ is compact. Step [](#s1-6){.pf-ref} gives uniform boundedness and equicontinuity there, so Arzela--Ascoli gives a uniformly convergent subsequence on $K_k$.

:::

:::

::: {.pf-step #s1-8}

A diagonal extraction produces a single subsequence $(f_{n_j})$ converging uniformly on every $K_k$.


::: pf-proof

Choose a subsequence converging on $K_2$; from it choose one converging on $K_3$; continue. Taking the diagonal subsequence ensures that for each fixed $k$, all sufficiently late terms lie in the subsequence selected at stage $k$, and therefore converge uniformly on $K_k$.

:::

:::

::: {.pf-step #s1-9}

Hence $(f_{n_j})$ converges uniformly on every compact subset of $\DD$.


::: pf-proof

Every compact subset of $\DD$ lies in some $K_k$, and step [](#s1-8){.pf-ref} gives uniform convergence there.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required conclusion.

:::

:::

:::
