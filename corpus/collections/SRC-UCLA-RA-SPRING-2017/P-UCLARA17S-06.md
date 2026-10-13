---
schema: qual/card@1
id: P-UCLARA17S-06
kind: problem
title: Swiss cheese sets have positive area
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let
\[
\mathbb D=\{z\in\mathbb C:|z|<1\}
\]
be the open unit disk and let $\overline{\mathbb D}$ be the closed unit disk. Let $\{p_n\}$ be distinct points in $\mathbb D$, and let $r_n>0$ be such that the disks
\[
D_n=\{z:|z-p_n|\le r_n\}
\]
satisfy (i) $D_n\subset\mathbb D$; (ii) $D_n\cap D_m=\varnothing$ if $n\ne m$; and (iii) $\sum_n r_n<\infty$. Prove that
\[
X=\overline{\mathbb D}\setminus\bigcup_n D_n
\]
has positive area.

Hint: for $-1<x<1$ consider $\#\{n:D_n\cap\{\operatorname{Re}z=x\}\ne\varnothing\}$.
:::

::: {.solution}
For $-1<x<1$, let
$$
N(x)\coloneqq
\#\{n:D_n\cap\{\operatorname{Re}z=x\}\ne\varnothing\}.
$$

<1>1. The function $N$ is integrable on $(-1,1)$ and
$$
\int_{-1}^1N(x)\,dx=2\sum_{n=1}^{\infty}r_n<\infty.
$$

::: {.proof}
Write $p_n=a_n+ib_n$. The vertical line $\operatorname{Re}z=x$ meets $D_n$ exactly when
$$
|x-a_n|\le r_n.
$$
Hence
$$
N(x)=\sum_{n=1}^{\infty}\mathbf 1_{[a_n-r_n,a_n+r_n]}(x).
$$
The summands are nonnegative, so Tonelli's theorem gives
$$
\begin{aligned}
\int_{-1}^1N(x)\,dx
&=\sum_{n=1}^{\infty}
\int_{-1}^1\mathbf 1_{[a_n-r_n,a_n+r_n]}(x)\,dx\\
&=\sum_{n=1}^{\infty}2r_n.
\end{aligned}
$$
Here $[a_n-r_n,a_n+r_n]\subset(-1,1)$ because the closed disk $D_n$ is contained in the open unit disk $\mathbb D$.
:::

<1>2. For almost every $x\in(-1,1)$, only finitely many disks $D_n$ meet the vertical line $\operatorname{Re}z=x$.

::: {.proof}
By step <1>1, the nonnegative function $N$ has finite integral. Therefore $N(x)<\infty$ for almost every $x$.
:::

<1>3. If $N(x)<\infty$, then the vertical section
$$
X_x\coloneqq\{y\in\RR:x+iy\in X\}
$$
has positive one-dimensional Lebesgue measure.

::: {.proof}
The section of the closed unit disk on the line $\operatorname{Re}z=x$ is the interval
$$
I_x=
\left[-\sqrt{1-x^2},\sqrt{1-x^2}\right].
$$
Only the finitely many disks counted by $N(x)$ remove points from this interval. Each such section $D_n\cap\{\operatorname{Re}z=x\}$ is a compact interval, and because $D_n\subset\mathbb D$, it is contained in the interior of $I_x$.

The union of finitely many such sections is therefore a compact subset of the open interval
$$
\left(-\sqrt{1-x^2},\sqrt{1-x^2}\right).
$$
Consequently it stays a positive distance from both endpoints of $I_x$. Its complement in $I_x$, which is exactly $X_x$, therefore contains a nondegenerate interval and has positive length.
:::

<1>4. The set $X$ has positive area.

::: {.proof}
Let
$$
m(x)\coloneqq |X_x|.
$$
By Fubini--Tonelli applied to the indicator function of the measurable set $X$,
$$
|X|=\int_{-1}^1m(x)\,dx.
$$
By steps <1>2 and <1>3, one has $m(x)>0$ for almost every $x\in(-1,1)$. Since $m$ is nonnegative and positive on a set of positive measure,
$$
\boxed{|X|>0}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
