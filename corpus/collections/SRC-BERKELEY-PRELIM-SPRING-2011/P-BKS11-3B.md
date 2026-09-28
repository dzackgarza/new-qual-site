---
schema: qual/card@1
id: P-BKS11-3B
kind: problem
title: Infinitely many solutions of $e^z=z$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2011 solution PDF and independently reviewed its change-of-argument sketch.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Replaced the source sketch by a quantitative Rouche argument producing one zero in each of infinitely many disjoint disks.
---

::: {.problem}
Prove that there are infinitely many complex numbers z with $e ^ { z } = z$ . (Hint: consider the behavior of $e ^ { z } - z$ on the boundary of a large square.)
:::

::: {.solution}
Set
$$
F(z)\coloneqq e^z-z.
$$
For each positive integer $n$, write
$$
M_n\coloneqq2\pi n
$$
and
$$
a_n\coloneqq
\log M_n+i\left(M_n+\frac\pi2\right).
$$
Then
$$
e^{a_n}=iM_n.
$$

<1>1. For
$$
r_n\coloneqq\frac{2\log M_n}{M_n},
$$
one has
$$
r_n\longrightarrow0.
$$

::: {.proof}
Apply the limit
$$
\frac{\log t}{t}\longrightarrow0
$$
as $t\to\infty$, applied to $t=M_n$.
:::

<1>2. If $\abs{w}=r_n$, then
$$
F(a_n+w)
=
iM_nw+H_n(w),
$$
where
$$
H_n(w)
\coloneqq
iM_n(e^w-1-w)
-\log M_n
-\frac{\pi i}{2}
-w.
$$

::: {.proof}
Using
$$
e^{a_n}=iM_n
$$
and the definition of $a_n$,
$$
\begin{aligned}
F(a_n+w)
&=
iM_ne^w
-\log M_n
-iM_n
-\frac{\pi i}{2}
-w\\
&=
iM_nw
+
iM_n(e^w-1-w)
-\log M_n
-\frac{\pi i}{2}
-w.
\end{aligned}
$$
:::

<1>3. For every complex number $w$,
$$
\abs{e^w-1-w}
\leq
\frac12e^{\abs{w}}\abs{w}^2.
$$

::: {.proof}
From the exponential series,
$$
e^w-1-w
=
\sum_{k=2}^{\infty}\frac{w^k}{k!}.
$$
Therefore
$$
\begin{aligned}
\abs{e^w-1-w}
&\leq
\sum_{k=2}^{\infty}\frac{\abs{w}^k}{k!}\\
&\leq
\frac{\abs{w}^2}{2}
\sum_{j=0}^{\infty}\frac{\abs{w}^j}{j!}\\
&=
\frac12e^{\abs{w}}\abs{w}^2.
\end{aligned}
$$
:::

<1>4. For all sufficiently large $n$ and every $w$ with
$\abs{w}=r_n$,
$$
\abs{H_n(w)}
<
\abs{iM_nw}.
$$

::: {.proof}
By steps <1>2 and <1>3,
$$
\abs{H_n(w)}
\leq
\frac12M_ne^{r_n}r_n^2
+
\log M_n
+
\frac\pi2
+
r_n.
$$
On the other hand,
$$
\abs{iM_nw}
=
M_nr_n
=
2\log M_n.
$$
Moreover,
$$
\frac{
\frac12M_ne^{r_n}r_n^2
+\frac\pi2+r_n
}{
\log M_n
}
=
\frac{2e^{r_n}\log M_n}{M_n}
+
\frac{\pi}{2\log M_n}
+
\frac{2}{M_n}
\longrightarrow0
$$
by step <1>1. Hence for all sufficiently large $n$,
$$
\frac12M_ne^{r_n}r_n^2
+\frac\pi2+r_n
<
\log M_n.
$$
Substituting this into the first bound gives
$$
\abs{H_n(w)}
<
2\log M_n
=
\abs{iM_nw}.
$$
:::

<1>5. For every sufficiently large $n$, the function $F$ has exactly one
zero in the disk
$$
D_n
\coloneqq
\{z\in\CC:\abs{z-a_n}<r_n\},
$$
counted with multiplicity.

::: {.proof}
On the circle $\abs{w}=r_n$, step <1>4 gives
$$
\abs{H_n(w)}
<
\abs{iM_nw}.
$$
Rouché's theorem therefore shows that
$$
w\longmapsto F(a_n+w)
$$
and
$$
w\longmapsto iM_nw
$$
have the same number of zeros in $\abs{w}<r_n$. The latter has exactly
one zero, at $w=0$, with multiplicity $1$.
:::

<1>6. The disks $D_n$ are pairwise disjoint for all sufficiently large
$n$.

::: {.proof}
The imaginary parts of consecutive centers differ by
$$
\operatorname{Im}(a_{n+1}-a_n)
=
2\pi.
$$
Hence
$$
\abs{a_{n+1}-a_n}
\geq
2\pi.
$$
By step <1>1, one has $r_n<1$ for all sufficiently large $n$. Thus for
large $m\neq n$,
$$
r_m+r_n<2<2\pi\leq\abs{a_m-a_n},
$$
so the corresponding disks are disjoint.
:::

<1>7. The equation
$$
e^z=z
$$
has infinitely many distinct complex solutions.

::: {.proof}
By step <1>5, every sufficiently large $n$ contributes a zero of $F$ in
$D_n$. By step <1>6, those disks are pairwise disjoint, so the resulting
zeros are distinct. Since there are infinitely many such integers $n$,
$F$ has infinitely many zeros.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required conclusion.
:::
:::
