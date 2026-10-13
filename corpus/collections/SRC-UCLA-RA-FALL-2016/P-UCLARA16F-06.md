---
schema: qual/card@1
id: P-UCLARA16F-06
kind: problem
title: Weakly convergent sequences in $\ell^1$ converge in norm
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
Consider the Banach space $\ell^1$ consisting of all sequences $u=\{x_i\}$ in $\mathbb R$ with
\[
\lVert u\rVert_1=\sum_{i=1}^{\infty}|x_i|<\infty,
\]
and the Banach space $\ell^\infty$ consisting of all sequences $v=\{y_i\}$ in $\mathbb R$ with
\[
\lVert v\rVert_\infty=\sup_{i\in\mathbb N}|y_i|<\infty.
\]
There is a well-defined dual pairing between $\ell^1$ and $\ell^\infty$ given by
\[
\langle u,v\rangle=\sum_{i=1}^{\infty}x_i y_i.
\]
With this dual pairing, $\ell^\infty=(\ell^1)^*$ is the dual space of $\ell^1$.

(a) Show that there exists no sequence $\{u_n\}$ in $\ell^1$ such that (i) $\lVert u_n\rVert_1\ge1$ for all $n\in\mathbb N$ and (ii) $\langle u_n,v\rangle\to0$ for each $v\in\ell^\infty$.

(b) Show that every weakly convergent sequence $\{u_n\}$ in $\ell^1$ converges in the norm topology of $\ell^1$.
:::

::: {.solution}
## Part (a)

Suppose, toward a contradiction, that
\[
u_n=(x_i^{(n)})_{i\ge1}\in\ell^1
\]
satisfies
\[
\|u_n\|_1\ge1
\]
for every \(n\), and
\[
\langle u_n,v\rangle\to0
\]
for every \(v\in\ell^\infty\).

<1>1. For every fixed coordinate \(i\),
\[
\boxed{x_i^{(n)}\to0}.
\]

::: {.proof}
Let \(e^{(i)}\in\ell^\infty\) be the coordinate vector
\[
e^{(i)}_j=
\begin{cases}
1,&j=i,\\
0,&j\ne i.
\end{cases}
\]
Then
\[
\langle u_n,e^{(i)}\rangle
=
x_i^{(n)}.
\]
The assumed weak convergence to \(0\) gives the result.
:::

Fix
\[
\varepsilon=\frac18.
\]

We inductively construct:
- integers
\[
0=N_0<N_1<N_2<\cdots,
\]
- a subsequence
\[
u_{n_1},u_{n_2},\dots,
\]
such that
\[
\boxed{
\sum_{i\le N_{k-1}}
|x_i^{(n_k)}|
<
\varepsilon}
\]
and
\[
\boxed{
\sum_{i>N_k}
|x_i^{(n_k)}|
<
\varepsilon}
\]
for every \(k\).

<1>2. Choose any \(n_1\), and then choose \(N_1\) so large that
\[
\sum_{i>N_1}|x_i^{(n_1)}|<\varepsilon.
\]

::: {.proof}
The vector \(u_{n_1}\) belongs to \(\ell^1\), so its tails tend to zero.
:::

<1>3. Suppose \(N_{k-1}\) and \(n_{k-1}\) have been chosen. Then one can choose \(n_k>n_{k-1}\) such that
\[
\sum_{i\le N_{k-1}}
|x_i^{(n_k)}|
<
\varepsilon.
\]

::: {.proof}
For each fixed
\[
1\le i\le N_{k-1},
\]
step <1>1 gives
\[
x_i^{(n)}\to0.
\]
Since there are only finitely many such coordinates, their absolute-value sum tends to \(0\). Hence it is eventually \(<\varepsilon\).
:::

<1>4. After choosing \(n_k\), choose \(N_k>N_{k-1}\) such that
\[
\sum_{i>N_k}
|x_i^{(n_k)}|
<
\varepsilon.
\]

::: {.proof}
Again use that \(u_{n_k}\in\ell^1\).
:::

<1>5. Thus the required subsequence and block endpoints exist.

::: {.proof}
Steps <1>2--<1>4 give the induction.
:::

Define the \(k\)-th block
\[
I_k
=
\{N_{k-1}+1,\dots,N_k\}.
\]

<1>6. The \(\ell^1\)-mass of \(u_{n_k}\) outside \(I_k\) satisfies
\[
\boxed{
\sum_{i\notin I_k}
|x_i^{(n_k)}|
<
2\varepsilon}.
\]

::: {.proof}
The coordinates outside \(I_k\) split into
\[
i\le N_{k-1}
\]
and
\[
i>N_k.
\]
Each contribution is \(<\varepsilon\) by construction.
:::

<1>7. Therefore
\[
\boxed{
\sum_{i\in I_k}
|x_i^{(n_k)}|
>
1-2\varepsilon}.
\]

::: {.proof}
Since
\[
\|u_{n_k}\|_1
=
\sum_{i\in I_k}|x_i^{(n_k)}|
+
\sum_{i\notin I_k}|x_i^{(n_k)}|
\ge1,
\]
apply step <1>6.
:::

Define \(v=(v_i)\) by
\[
v_i
=
\operatorname{sgn}(x_i^{(n_k)})
\]
when \(i\in I_k\), with \(\operatorname{sgn}(0)=0\).

<1>8. The vector \(v\) belongs to \(\ell^\infty\) and
\[
\boxed{\|v\|_\infty\le1}.
\]

::: {.proof}
The blocks \(I_k\) are disjoint and cover a subset of \(\mathbb N\), so the definition is unambiguous. Every coordinate satisfies
\[
|v_i|\le1.
\]
Set \(v_i=0\) on coordinates not belonging to any block.
:::

<1>9. On the block \(I_k\),
\[
\sum_{i\in I_k}
x_i^{(n_k)}v_i
=
\sum_{i\in I_k}
|x_i^{(n_k)}|.
\]

::: {.proof}
By definition,
\[
v_i=\operatorname{sgn}(x_i^{(n_k)})
\]
on \(I_k\).
:::

<1>10. The contribution from outside \(I_k\) satisfies
\[
\left|
\sum_{i\notin I_k}
x_i^{(n_k)}v_i
\right|
<
2\varepsilon.
\]

::: {.proof}
Since \(|v_i|\le1\),
\[
\left|
\sum_{i\notin I_k}
x_i^{(n_k)}v_i
\right|
\le
\sum_{i\notin I_k}
|x_i^{(n_k)}|
<
2\varepsilon
\]
by step <1>6.
:::

<1>11. Hence
\[
\langle u_{n_k},v\rangle
>
1-4\varepsilon.
\]

::: {.proof}
Using steps <1>7, <1>9, and <1>10,
\[
\begin{aligned}
\langle u_{n_k},v\rangle
&=
\sum_{i\in I_k}
x_i^{(n_k)}v_i
+
\sum_{i\notin I_k}
x_i^{(n_k)}v_i\\
&\ge
\sum_{i\in I_k}
|x_i^{(n_k)}|
-
\left|
\sum_{i\notin I_k}
x_i^{(n_k)}v_i
\right|\\
&>
(1-2\varepsilon)-2\varepsilon\\
&=
1-4\varepsilon.
\end{aligned}
\]
:::

<1>12. Since \(\varepsilon=1/8\),
\[
\boxed{
\langle u_{n_k},v\rangle>\frac12}
\]
for every \(k\).

::: {.proof}
\[
1-4\varepsilon
=
1-\frac12
=
\frac12.
\]
:::

<1>13. This contradicts the assumption that
\[
\langle u_n,v\rangle\to0
\]
for every \(v\in\ell^\infty\).

::: {.proof}
The fixed vector \(v\in\ell^\infty\) from step <1>8 has pairings along the subsequence bounded below by \(1/2\), by step <1>12.
:::

<1>14. Therefore no sequence satisfying conditions (i) and (ii) exists.

::: {.proof}
The assumption of its existence led to the contradiction in step <1>13.
:::

## Part (b)

Let
\[
u_n\rightharpoonup u
\]
weakly in \(\ell^1\).

<1>15. Define
\[
w_n=u_n-u.
\]
Then
\[
\boxed{
w_n\rightharpoonup0}.
\]

::: {.proof}
For every \(v\in\ell^\infty\),
\[
\langle w_n,v\rangle
=
\langle u_n,v\rangle-\langle u,v\rangle
\to0.
\]
:::

<1>16. Suppose, toward a contradiction, that
\[
\|w_n\|_1\not\to0.
\]

::: {.proof}
This is the negation of norm convergence.
:::

<1>17. Then there exist
\[
\delta>0
\]
and a subsequence \((w_{n_k})\) such that
\[
\boxed{
\|w_{n_k}\|_1\ge\delta}
\]
for every \(k\).

::: {.proof}
Failure of convergence to \(0\) gives an \(\varepsilon\)-subsequence bounded away from \(0\).
:::

<1>18. Define
\[
\boxed{
z_k=\frac1\delta w_{n_k}}.
\]

::: {.proof}
Since \(\delta>0\), this is well defined.
:::

<1>19. Then
\[
\boxed{
\|z_k\|_1\ge1}
\]
for every \(k\).

::: {.proof}
By step <1>17,
\[
\|z_k\|_1
=
\frac1\delta
\|w_{n_k}\|_1
\ge1.
\]
:::

<1>20. Also
\[
\boxed{
z_k\rightharpoonup0}.
\]

::: {.proof}
For every \(v\in\ell^\infty\),
\[
\langle z_k,v\rangle
=
\frac1\delta
\langle w_{n_k},v\rangle
\to0
\]
by step <1>15.
:::

<1>21. Steps <1>19--<1>20 contradict part (a).

::: {.proof}
Part (a), step <1>14, says no weakly null sequence in \(\ell^1\) can have all norms at least \(1\).
:::

<1>22. Therefore
\[
\boxed{
\|u_n-u\|_1\to0}.
\]

::: {.proof}
The assumption in step <1>16 is impossible, and
\[
\|u_n-u\|_1=\|w_n\|_1.
\]
:::

<1>23. Thus every weakly convergent sequence in \(\ell^1\) converges in norm.

::: {.proof}
This is step <1>22.
:::

<1>24. Q.E.D.

::: {.proof}
Step <1>14 proves part (a), and step <1>23 proves part (b).
:::
:::
