---
schema: qual/card@1
id: P-UCLARA14F-04
kind: problem
title: Cosine series with $\sum(1+n^2)|c_n|^2<\infty$ form an algebra
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
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 4 on page 1 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Given $f \in L^2([0,\pi])$, we say that $f \in \mathcal{G}$ if $f$ admits a representation of the form
\[
f(x) = \sum_{n=0}^{\infty} c_n \cos(nx) \quad \text{with} \quad \sum_{n=0}^{\infty} (1+n^2)|c_n|^2 < \infty.
\]
Show that if $f \in \mathcal{G}$ and $g \in \mathcal{G}$ then $fg \in \mathcal{G}$.
:::

::: {.solution}

Let
\[
f(x)=\sum_{n=0}^\infty c_n\cos(nx),
\qquad
g(x)=\sum_{n=0}^\infty d_n\cos(nx),
\]
with
\[
\sum_{n\ge0}(1+n^2)|c_n|^2<\infty,
\qquad
\sum_{n\ge0}(1+n^2)|d_n|^2<\infty.
\]

::: pf

::: {.pf-step #s1-1}

The coefficient sequences $(c_n)$ and $(d_n)$ belong to $\ell^1$.


::: pf-proof

By Cauchy--Schwarz,
\[
\sum_{n=0}^\infty |c_n|
\le
\left(
\sum_{n=0}^\infty(1+n^2)|c_n|^2
\right)^{1/2}
\left(
\sum_{n=0}^\infty\frac1{1+n^2}
\right)^{1/2}
<\infty.
\]
The same argument applies to $(d_n)$.

:::

:::

::: pf-step

The cosine series for $f$ and $g$ converge absolutely and uniformly
on $\RR$.


::: pf-proof

Since
\[
|\cos(nx)|\le1,
\]
step [](#s1-1){.pf-ref} and the Weierstrass $M$-test give absolute and uniform convergence.
Thus the series define continuous even $2\pi$-periodic representatives of
$f$ and $g$.

:::

:::

::: {.pf-step #s1-3}

Define bilateral sequences $(a_k)_{k\in\ZZ}$ and
$(b_k)_{k\in\ZZ}$ by
\[
a_0=c_0,
\qquad
a_k=a_{-k}=\frac{c_k}{2}\quad(k\ge1),
\]
and
\[
b_0=d_0,
\qquad
b_k=b_{-k}=\frac{d_k}{2}\quad(k\ge1).
\]
Then
\[
f(x)=\sum_{k\in\ZZ}a_ke^{ikx},
\qquad
g(x)=\sum_{k\in\ZZ}b_ke^{ikx},
\]
with absolute and uniform convergence.


::: pf-proof

Use
\[
\cos(kx)=\frac{e^{ikx}+e^{-ikx}}2.
\]
The bilateral series are absolutely summable because step [](#s1-1){.pf-ref} gives
$a,b\in\ell^1(\ZZ)$.

:::

:::

::: {.pf-step #s1-4}

The weighted sequences
\[
A_k=(1+k^2)^{1/2}|a_k|,
\qquad
B_k=(1+k^2)^{1/2}|b_k|
\]
belong to $\ell^2(\ZZ)$.


::: pf-proof

By the definitions in step [](#s1-3){.pf-ref},
\[
\sum_{k\in\ZZ}(1+k^2)|a_k|^2
=
|c_0|^2
+
\frac12\sum_{k=1}^\infty(1+k^2)|c_k|^2
<\infty.
\]
The same calculation applies to $b$.

:::

:::

::: {.pf-step #s1-5}

The product has the absolutely convergent Fourier expansion
\[
f(x)g(x)
=
\sum_{n\in\ZZ}e_n e^{inx},
\qquad
e_n=(a*b)_n
=
\sum_{k\in\ZZ}a_kb_{n-k}.
\]


::: pf-proof

The two Fourier series in step [](#s1-3){.pf-ref} are absolutely convergent. Their Cauchy
product is therefore absolutely convergent and equals the pointwise product.
The coefficient at frequency $n$ is exactly the convolution shown above.

:::

:::

::: {.pf-step #s1-6}

There is an absolute constant $C$ such that for all integers $n,k$,
\[
(1+n^2)^{1/2}
\le
C\left(
(1+k^2)^{1/2}
+
(1+(n-k)^2)^{1/2}
\right).
\]


::: pf-proof

Since
\[
|n|
\le
|k|+|n-k|,
\]
one has
\[
(1+n^2)^{1/2}
\le
1+|n|
\le
(1+|k|)+(1+|n-k|).
\]
Also
\[
1+|j|
\le
\sqrt2\,(1+j^2)^{1/2}.
\]
Thus the inequality holds, for example with $C=\sqrt2$.

:::

:::

::: {.pf-step #s1-7}

The weighted product coefficients satisfy
\[
\left\|
\bigl((1+n^2)^{1/2}e_n\bigr)_{n\in\ZZ}
\right\|_{\ell^2}
<\infty.
\]


::: pf-proof

By steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref},
\[
\begin{aligned}
(1+n^2)^{1/2}|e_n|
&\le
C\sum_k
\left(
(1+k^2)^{1/2}|a_k||b_{n-k}|
\right.\\
&\hspace{4em}\left.
+
|a_k|(1+(n-k)^2)^{1/2}|b_{n-k}|
\right).
\end{aligned}
\]
Hence, pointwise in $n$,
\[
(1+n^2)^{1/2}|e_n|
\le
C\bigl((A*|b|)_n+(|a|*B)_n\bigr).
\]
Young's convolution inequality
\[
\ell^2*\ell^1\longrightarrow\ell^2
\]
therefore gives
\[
\begin{aligned}
\left\|(1+n^2)^{1/2}e_n\right\|_{\ell^2}
&\le
C\left(
\|A\|_2\|b\|_1
+
\|a\|_1\|B\|_2
\right)
<\infty,
\end{aligned}
\]
using steps [](#s1-1){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The sequence $(e_n)$ is even:
\[
e_{-n}=e_n.
\]


::: pf-proof

The sequences $a$ and $b$ are even by construction. Therefore
\[
\begin{aligned}
e_{-n}
&=
\sum_k a_kb_{-n-k}\\
&=
\sum_j a_{-j}b_{n-j}
\qquad(j=-k)\\
&=
\sum_j a_jb_{n-j}
=e_n.
\end{aligned}
\]

:::

:::

::: {.pf-step #s1-9}

Hence $fg$ has a cosine expansion
\[
fg(x)
=
\sum_{n=0}^\infty r_n\cos(nx)
\]
with
\[
\sum_{n=0}^\infty(1+n^2)|r_n|^2<\infty.
\]


::: pf-proof

By step [](#s1-8){.pf-ref},
\[
\sum_{n\in\ZZ}e_ne^{inx}
=
e_0
+
\sum_{n=1}^\infty
e_n(e^{inx}+e^{-inx})
=
e_0
+
\sum_{n=1}^\infty 2e_n\cos(nx).
\]
Set
\[
r_0=e_0,
\qquad
r_n=2e_n\quad(n\ge1).
\]
Step [](#s1-7){.pf-ref} gives
\[
\sum_{n\ge0}(1+n^2)|r_n|^2<\infty
\]
up to the harmless factor $4$ for $n\ge1$.

:::

:::

::: {.pf-step #s1-10}

Therefore
\[
\boxed{f,g\in\mathcal G\Longrightarrow fg\in\mathcal G}.
\]


::: pf-proof

Step [](#s1-9){.pf-ref} is exactly the defining condition for $fg\in\mathcal G$.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
