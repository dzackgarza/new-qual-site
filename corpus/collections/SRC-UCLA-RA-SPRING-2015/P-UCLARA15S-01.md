---
schema: qual/card@1
id: P-UCLARA15S-01
kind: problem
title: Partition sums $\sum_k\abs{\int_{k/n}^{(k+1)/n}f}$ converge to $\norm{f}_1$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Riemann Integration
  - Density
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1(\RR)$.
Show that
$$
\lim_{n\to\infty}\sum_{k=-n^2}^{n^2}\abs{\int_{k/n}^{(k+1)/n}f(x)\,dx}=\int_{\RR}\abs{f(x)}\,dx.
$$
:::

::: {.solution}

For $n\ge1$, define
$$
S_n(h)
\coloneqq
\sum_{k=-n^2}^{n^2}
\abs{
\int_{k/n}^{(k+1)/n}h(x)\,dx
}.
$$

::: pf

::: {.pf-step #s1}

For all $f,g\in L^1(\RR)$,
$$
\abs{S_n(f)-S_n(g)}
\le
\norm{f-g}_{L^1}.
$$


::: pf-proof

For each mesh interval
$$
I_{k,n}
=
\left[\frac{k}{n},\frac{k+1}{n}\right],
$$
the reverse triangle inequality gives
$$
\abs{
\abs{\int_{I_{k,n}}f}
-
\abs{\int_{I_{k,n}}g}
}
\le
\abs{
\int_{I_{k,n}}(f-g)
}
\le
\int_{I_{k,n}}\abs{f-g}.
$$
Summing over $-n^2\le k\le n^2$ yields
$$
\abs{S_n(f)-S_n(g)}
\le
\int_{-n}^{n+1/n}\abs{f-g}
\le
\norm{f-g}_1.
$$

:::

:::

::: {.pf-step #s2}

If $g\in C_c(\RR)$, then
$$
S_n(g)
\longrightarrow
\norm{g}_{L^1}.
$$


::: pf-proof

::: {.pf-step #s2-1}

Let $\operatorname{supp}(g)\subset[-R,R]$ and let
$$
\omega_g(\delta)
\coloneqq
\sup\{\abs{g(x)-g(y)}:\abs{x-y}\le\delta\}.
$$
Then
$$
\omega_g(\delta)\longrightarrow0
\qquad
(\delta\downarrow0).
$$


::: pf-proof

A continuous compactly supported function is uniformly continuous on $\RR$. The displayed statement is exactly uniform continuity written in terms of the modulus of continuity.

:::

:::

::: {.pf-step #s2-2}

For every mesh interval $I=I_{k,n}$,
$$
0
\le
\int_I\abs{g(x)}\,dx
-
\abs{\int_I g(x)\,dx}
\le
\frac{2}{n}\omega_g(1/n).
$$


::: pf-proof

The left inequality is the triangle inequality. Fix any $x_I\in I$. Since $\setmeasure{I}=1/n$,
$$
\abs{
\int_I g(x)\,dx
-
\frac1n g(x_I)
}
\le
\frac1n\omega_g(1/n),
$$
while
$$
\abs{
\int_I\abs{g(x)}\,dx
-
\frac1n\abs{g(x_I)}
}
\le
\frac1n\omega_g(1/n).
$$
Using
$$
\abs{\frac1n g(x_I)}
=
\frac1n\abs{g(x_I)}
$$
and combining the two estimates gives the upper bound.

:::

:::

::: {.pf-step #s2-3}

For all sufficiently large $n$,
$$
0
\le
\norm{g}_1-S_n(g)
\le
C_R\,\omega_g(1/n)
$$
for a constant $C_R$ depending only on $R$.


::: pf-proof

For $n>R+1$, the interval
$$
[-n,n+1/n]
$$
contains the support of $g$, so
$$
\norm{g}_1
=
\sum_{k=-n^2}^{n^2}
\int_{I_{k,n}}\abs{g(x)}\,dx.
$$
Only mesh intervals meeting $[-R,R]$ contribute. Their number is at most
$$
2Rn+3.
$$
Applying step [](#s2-2){.pf-ref} on those intervals,
$$
0
\le
\norm{g}_1-S_n(g)
\le
(2Rn+3)\frac{2}{n}\omega_g(1/n).
$$
For $n\ge1$ the coefficient is bounded by a constant $C_R$, giving the claim.

:::

:::

::: pf-qed

Step [](#s2-3){.pf-ref} and step [](#s2-1){.pf-ref} give
$$
\abs{S_n(g)-\norm{g}_1}
\longrightarrow0.
$$
This proves step [](#s2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

For every $f\in L^1(\RR)$,
$$
S_n(f)
\longrightarrow
\norm{f}_{L^1}.
$$


::: pf-proof

Fix $\varepsilon>0$. Since $C_c(\RR)$ is dense in $L^1(\RR)$, choose $g\in C_c(\RR)$ such that
$$
\norm{f-g}_1<\frac{\varepsilon}{3}.
$$
By step [](#s2){.pf-ref}, for all sufficiently large $n$,
$$
\abs{S_n(g)-\norm{g}_1}
<
\frac{\varepsilon}{3}.
$$
Using step [](#s1){.pf-ref} and
$$
\abs{\norm{f}_1-\norm{g}_1}
\le
\norm{f-g}_1,
$$
one obtains
$$
\begin{aligned}
\abs{S_n(f)-\norm{f}_1}
&\le
\abs{S_n(f)-S_n(g)}
+
\abs{S_n(g)-\norm{g}_1}
+
\abs{\norm{g}_1-\norm{f}_1}\\
&<
\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\lim_{n\to\infty}
\sum_{k=-n^2}^{n^2}
\abs{
\int_{k/n}^{(k+1)/n}f(x)\,dx
}
=
\int_{\RR}\abs{f(x)}\,dx
}.
$$


::: pf-proof

This is step [](#s3){.pf-ref} written out using the definition of $S_n$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required limit.

:::

:::

:::
