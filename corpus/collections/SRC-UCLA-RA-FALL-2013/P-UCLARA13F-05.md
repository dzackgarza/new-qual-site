---
schema: qual/card@1
id: P-UCLARA13F-05
kind: problem
title: L1-bounded holomorphic functions form a normal family
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
Let $(f_n)$ be holomorphic functions on $\mathbb D$ satisfying
\[
\int_{\mathbb D}|f_n(z)|\,d\lambda(z)\le1
\]
for every $n$.
Show that some subsequence converges uniformly on every compact subset of $\mathbb D$.
:::

::: {.solution}
<1>1. Fix $0<r<R<1$. For every $z$ with $|z|\leq r$, the disk
\[
D(z,R-r)
\]
is contained in $\mathbb D$.

::: {.proof}
If $|w-z|<R-r$, then
\[
|w|\leq|z|+|w-z|<r+(R-r)=R<1.
\]
:::

<1>2. Since $|f_n|$ is subharmonic, the sub-mean inequality gives
\[
|f_n(z)|
\leq\frac1{\pi(R-r)^2}
\int_{D(z,R-r)}|f_n(w)|\,d\lambda(w).
\]

::: {.proof}
The modulus of a holomorphic function is subharmonic. Apply its mean-value inequality over the disk from step <1>1.
:::

<1>3. Therefore, uniformly in $n$,
\[
\sup_{|z|\leq r}|f_n(z)|
\leq\frac1{\pi(R-r)^2}.
\]

::: {.proof}
The integral over the smaller disk in step <1>2 is at most
\[
\int_{\mathbb D}|f_n(w)|\,d\lambda(w)\leq1
\]
by hypothesis.
:::

<1>4. Thus the family $\{f_n\}$ is locally uniformly bounded on $\mathbb D$.

::: {.proof}
Every compact $K\subset\mathbb D$ is contained in some closed disk $\{|z|\leq r\}$ with $r<1$. Choose $R$ with $r<R<1$ and apply step <1>3.
:::

<1>5. Fix $0<r<R<1$. Cauchy's estimate gives a constant $C_{r,R}$ independent of $n$ such that
\[
\sup_{|z|\leq r}|f_n'(z)|\leq C_{r,R}.
\]

::: {.proof}
Choose $r<R_1<R<1$. Step <1>3 gives a uniform bound $M$ for $|f_n|$ on $|z|\leq R_1$. For $|z|\leq r$, the circle of radius $R_1-r$ about $z$ lies in $|w|<R_1$. Cauchy's derivative estimate gives
\[
|f_n'(z)|\leq \frac{M}{R_1-r},
\]
which is independent of $n$.
:::

<1>6. On every closed disk $\{|z|\leq r\}$, the sequence $(f_n)$ is uniformly bounded and equicontinuous.

::: {.proof}
Uniform boundedness is step <1>3. The derivative bound in step <1>5 and the line-segment integral formula give
\[
|f_n(z)-f_n(w)|\leq C_{r,R}|z-w|
\]
for points in a slightly smaller convex disk, yielding equicontinuity.
:::

<1>7. For each integer $k\geq2$, let
\[
K_k=\{z:|z|\leq1-1/k\}.
\]
By Arzela--Ascoli, every subsequence of $(f_n)$ has a further subsequence converging uniformly on $K_k$.

::: {.proof}
Each $K_k$ is compact. Step <1>6 gives uniform boundedness and equicontinuity there, so Arzela--Ascoli gives a uniformly convergent subsequence on $K_k$.
:::

<1>8. A diagonal extraction produces a single subsequence $(f_{n_j})$ converging uniformly on every $K_k$.

::: {.proof}
Choose a subsequence converging on $K_2$; from it choose one converging on $K_3$; continue. Taking the diagonal subsequence ensures that for each fixed $k$, all sufficiently late terms lie in the subsequence selected at stage $k$, and therefore converge uniformly on $K_k$.
:::

<1>9. Hence $(f_{n_j})$ converges uniformly on every compact subset of $\mathbb D$.

::: {.proof}
Every compact subset of $\mathbb D$ lies in some $K_k$, and step <1>8 gives uniform convergence there.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required conclusion.
:::
:::
