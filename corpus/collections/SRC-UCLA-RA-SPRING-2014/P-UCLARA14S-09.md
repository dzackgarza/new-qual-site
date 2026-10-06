---
schema: qual/card@1
id: P-UCLARA14S-09
kind: problem
title: Hurwitz theorem for zero-free holomorphic functions
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $\Omega\subset\mathbb C$ be connected and open, and let $f_n,f:\Omega\to\mathbb C$ be holomorphic.
Suppose $f_n\to f$ uniformly on compact subsets of $\Omega$.
Prove that if $f_n(z)\ne0$ for every $z\in\Omega$ and every $n$, then either $f\equiv0$ or $f(z)\ne0$ for every $z\in\Omega$.
:::

::: {.solution}
<1>1. Suppose that
\[
f\not\equiv0.
\]
Then every zero of $f$ in $\Omega$ is isolated.

::: {.proof}
This is the identity theorem for holomorphic functions on the connected domain $\Omega$: a nonzero holomorphic function cannot have a set of zeros with an accumulation point in $\Omega$.
:::

<1>2. If $f(z_0)=0$ for some $z_0\in\Omega$, then there exists $r>0$ such that
\[
\overline{B(z_0,r)}\subset\Omega,
\]
$z_0$ is the only zero of $f$ in that closed disk, and
\[
\delta
\coloneqq
\min_{|z-z_0|=r}|f(z)|
>
0.
\]

::: {.proof}
By step <1>1, the zero $z_0$ is isolated. Choose $r>0$ small enough that the closed disk is contained in $\Omega$ and contains no zero of $f$ other than $z_0$. Then $f$ is nonzero on the boundary circle. Since the circle is compact and $|f|$ is continuous, its positive minimum there exists and is strictly positive.
:::

<1>3. For all sufficiently large $n$,
\[
|f_n(z)-f(z)|
<
|f(z)|
\qquad
(|z-z_0|=r).
\]

::: {.proof}
The boundary circle
\[
\{z:|z-z_0|=r\}
\]
is compact. By local uniform convergence,
\[
\sup_{|z-z_0|=r}|f_n(z)-f(z)|
\longrightarrow0.
\]
Choose $n$ large enough that this supremum is less than the number $\delta$ from step <1>2. Since
\[
|f(z)|\ge\delta
\]
on the circle, the required strict inequality follows.
:::

<1>4. For all sufficiently large $n$, the function $f_n$ has at least one zero in $B(z_0,r)$.

::: {.proof}
By step <1>3, Rouché's theorem applied on the circle $|z-z_0|=r$ shows that $f_n$ and $f$ have the same number of zeros inside the circle, counted with multiplicity. The function $f$ has at least the zero $z_0$ there, so that number is positive. Hence $f_n$ must also have a zero in the disk.
:::

<1>5. If $f\not\equiv0$, then
\[
f(z)\ne0
\qquad
(z\in\Omega).
\]

::: {.proof}
If $f$ had a zero $z_0$, step <1>4 would force sufficiently large $f_n$ to have a zero in $\Omega$. This contradicts the hypothesis that every $f_n$ is zero-free.
:::

<1>6. Therefore
\[
\boxed{
f\equiv0
\quad\text{or}\quad
f(z)\ne0\text{ for every }z\in\Omega.
}
\]

::: {.proof}
If $f$ is identically zero, the first alternative holds. Otherwise step <1>5 gives the second alternative.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is exactly the desired conclusion.
:::
:::
