---
schema: qual/card@1
id: P-UCLARA15S-01
kind: problem
title: Partition sums $\sum_k\bigl|\int_{k/n}^{(k+1)/n}f\bigr|$ converge to $\|f\|_1$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f\in L^1(\RR)$.
Show that
\[
\lim_{n\to\infty}\sum_{k=-n^2}^{n^2}\left|\int_{k/n}^{(k+1)/n}f(x)\,dx\right|=\int_{\RR}|f(x)|\,dx.
\]
:::

::: {.solution}

For $n\ge1$, define
\[
S_n(h)
\coloneqq
\sum_{k=-n^2}^{n^2}
\left|
\int_{k/n}^{(k+1)/n}h(x)\,dx
\right|.
\]

::: pf

::: {.pf-step #s1}

For all $f,g\in L^1(\RR)$,
\[
|S_n(f)-S_n(g)|
\le
\|f-g\|_{L^1}.
\]


::: pf-proof

For each mesh interval
\[
I_{k,n}
=
\left[\frac{k}{n},\frac{k+1}{n}\right],
\]
the reverse triangle inequality gives
\[
\left|
\left|\int_{I_{k,n}}f\right|
-
\left|\int_{I_{k,n}}g\right|
\right|
\le
\left|
\int_{I_{k,n}}(f-g)
\right|
\le
\int_{I_{k,n}}|f-g|.
\]
Summing over $-n^2\le k\le n^2$ yields
\[
|S_n(f)-S_n(g)|
\le
\int_{-n}^{n+1/n}|f-g|
\le
\|f-g\|_1.
\]

:::

:::

::: {.pf-step #s2}

If $g\in C_c(\RR)$, then
\[
S_n(g)
\longrightarrow
\|g\|_{L^1}.
\]


::: pf-proof

::: {.pf-step #s2-1}

Let $\operatorname{supp}(g)\subset[-R,R]$ and let
\[
\omega_g(\delta)
\coloneqq
\sup\{|g(x)-g(y)|:|x-y|\le\delta\}.
\]
Then
\[
\omega_g(\delta)\longrightarrow0
\qquad
(\delta\downarrow0).
\]


::: pf-proof

A continuous compactly supported function is uniformly continuous on $\RR$. The displayed statement is exactly uniform continuity written in terms of the modulus of continuity.

:::

:::

::: {.pf-step #s2-2}

For every mesh interval $I=I_{k,n}$,
\[
0
\le
\int_I|g(x)|\,dx
-
\left|\int_I g(x)\,dx\right|
\le
\frac{2}{n}\omega_g(1/n).
\]


::: pf-proof

The left inequality is the triangle inequality. Fix any $x_I\in I$. Since $|I|=1/n$,
\[
\left|
\int_I g(x)\,dx
-
\frac1n g(x_I)
\right|
\le
\frac1n\omega_g(1/n),
\]
while
\[
\left|
\int_I|g(x)|\,dx
-
\frac1n|g(x_I)|
\right|
\le
\frac1n\omega_g(1/n).
\]
Using
\[
\left|\frac1n g(x_I)\right|
=
\frac1n|g(x_I)|
\]
and combining the two estimates gives the upper bound.

:::

:::

::: {.pf-step #s2-3}

For all sufficiently large $n$,
\[
0
\le
\|g\|_1-S_n(g)
\le
C_R\,\omega_g(1/n)
\]
for a constant $C_R$ depending only on $R$.


::: pf-proof

For $n>R+1$, the interval
\[
[-n,n+1/n]
\]
contains the support of $g$, so
\[
\|g\|_1
=
\sum_{k=-n^2}^{n^2}
\int_{I_{k,n}}|g(x)|\,dx.
\]
Only mesh intervals meeting $[-R,R]$ contribute. Their number is at most
\[
2Rn+3.
\]
Applying step [](#s2-2){.pf-ref} on those intervals,
\[
0
\le
\|g\|_1-S_n(g)
\le
(2Rn+3)\frac{2}{n}\omega_g(1/n).
\]
For $n\ge1$ the coefficient is bounded by a constant $C_R$, giving the claim.

:::

:::

::: pf-qed

Step [](#s2-3){.pf-ref} and step [](#s2-1){.pf-ref} give
\[
|S_n(g)-\|g\|_1|
\longrightarrow0.
\]
This proves step [](#s2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

For every $f\in L^1(\RR)$,
\[
S_n(f)
\longrightarrow
\|f\|_{L^1}.
\]


::: pf-proof

Fix $\varepsilon>0$. Since $C_c(\RR)$ is dense in $L^1(\RR)$, choose $g\in C_c(\RR)$ such that
\[
\|f-g\|_1<\frac{\varepsilon}{3}.
\]
By step [](#s2){.pf-ref}, for all sufficiently large $n$,
\[
|S_n(g)-\|g\|_1|
<
\frac{\varepsilon}{3}.
\]
Using step [](#s1){.pf-ref} and
\[
|\|f\|_1-\|g\|_1|
\le
\|f-g\|_1,
\]
one obtains
\[
\begin{aligned}
|S_n(f)-\|f\|_1|
&\le
|S_n(f)-S_n(g)|
+
|S_n(g)-\|g\|_1|
+
|\|g\|_1-\|f\|_1|\\
&<
\varepsilon.
\end{aligned}
\]

:::

:::

::: {.pf-step #s4}

Therefore
\[
\boxed{
\lim_{n\to\infty}
\sum_{k=-n^2}^{n^2}
\left|
\int_{k/n}^{(k+1)/n}f(x)\,dx
\right|
=
\int_{\RR}|f(x)|\,dx
}.
\]


::: pf-proof

This is step [](#s3){.pf-ref} written out using the definition of $S_n$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required limit.

:::

:::

:::
