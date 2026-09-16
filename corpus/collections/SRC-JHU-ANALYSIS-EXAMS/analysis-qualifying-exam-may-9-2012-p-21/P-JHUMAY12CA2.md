---
schema: qual/card@1
id: P-JHUMAY12CA2
kind: problem
title: Unique fixed point of a disk map whose boundary values lie in the open disk
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose $f$ is holomorphic on the open unit disc $D(0,1)$ and continuous on $\overline{D(0,1)}$.
Assume $\abs{f(\xi)} < 1$ for $\xi \in \partial D(0,1)$.
Show that there exists a unique point $a \in D(0,1)$ such that $f(a) = a$.
:::

::: {.solution}
<1>1. There is $q<1$ such that $\abs{f(z)}\le q$ for every $z\in D(0,1)$.
::: {.proof}
Since the boundary circle is compact and $f$ is continuous there,
$$
q\coloneqq\max_{\abs{\xi}=1}\abs{f(\xi)}<1.
$$
The [[T-BYNL5|maximum modulus principle]] gives $\abs{f(z)}\le q$ throughout the disk.
:::

<1>2. The function $g(z)=f(z)-z$ has exactly one zero in the unit disk, counted with multiplicity.
::: {.proof}
Choose $r$ with $q<r<1$. On $\abs{z}=r$, step <1>1 gives
$$
\abs{f(z)}\le q<r=\abs{-z}.
$$
The functions $f$ and $-z$ are holomorphic on an open neighborhood of the closed disk $\abs{z}\le r$. Therefore the [[T-CJCKL|Rouché theorem]], applied to
$$
g(z)=(-z)+f(z),
$$
shows that $g$ and $-z$ have the same number of zeros in $\abs{z}<r$, counted with multiplicity. Thus $g$ has exactly one zero there.

If $g(a)=0$ anywhere in the unit disk, then $a=f(a)$, so step <1>1 gives
$$
\abs{a}=\abs{f(a)}\le q<r.
$$
Hence every zero of $g$ in the unit disk already lies in $\abs{z}<r$, and there is exactly one such zero in the whole unit disk.
:::

<1>3. The unique zero of $g$ is the unique fixed point of $f$ in the unit disk.
::: {.proof}
For $a\in D(0,1)$,
$$
g(a)=0
\quad\Longleftrightarrow\quad
f(a)=a.
$$
By step <1>2 there is exactly one such zero, so there is exactly one fixed point.
:::

<1>4. Q.E.D.
::: {.proof}
Step <1>3 proves the required existence and uniqueness.
:::
:::
