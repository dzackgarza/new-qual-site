---
schema: qual/card@1
id: P-UCLARA14F-09
kind: problem
title: Locally uniform limits of injective holomorphic functions
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
  note: Retranscribed the font-garbled statement in LaTeX from Problem 9 on page 2 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\Omega \subset \mathbb{C}$ be open and connected. Suppose $(f_n)$ is a sequence of injective holomorphic functions defined on $\Omega$, such that $f_n \to f$ locally uniformly in $\Omega$. Show that if $f$ is not constant, then $f$ is also injective in $\Omega$.
:::

::: {.solution}
<1>1. The locally uniform limit $f$ is holomorphic on $\Omega$.

::: {.proof}
The Weierstrass theorem on locally uniform limits of holomorphic functions
implies that a locally uniform limit of holomorphic functions is holomorphic.
:::

<1>2. Suppose, toward a contradiction, that $f$ is not injective. Then there
exist distinct points
\[
a,b\in\Omega
\]
such that
\[
f(a)=f(b).
\]

::: {.proof}
This is exactly the negation of injectivity.
:::

<1>3. Define
\[
g_n(z)=f_n(z)-f_n(a)
\]
and
\[
g(z)=f(z)-f(a).
\]
Then
\[
g_n\to g
\]
locally uniformly on $\Omega$.

::: {.proof}
Since $f_n\to f$ locally uniformly, in particular
\[
f_n(a)\to f(a).
\]
Hence on every compact set $K\subset\Omega$,
\[
\sup_{z\in K}|g_n(z)-g(z)|
\le
\sup_{z\in K}|f_n(z)-f(z)|
+
|f_n(a)-f(a)|
\longrightarrow0.
\]
:::

<1>4. For each $n$, the only zero of $g_n$ in $\Omega$ is $a$.

::: {.proof}
One has
\[
g_n(z)=0
\quad\Longleftrightarrow\quad
f_n(z)=f_n(a).
\]
Since $f_n$ is injective, this occurs exactly when
\[
z=a.
\]
:::

<1>5. The zero of $g$ at $b$ is isolated.

::: {.proof}
By step <1>2,
\[
g(b)=f(b)-f(a)=0.
\]
If $g$ were identically zero on $\Omega$, then
\[
f\equiv f(a),
\]
contradicting the hypothesis that $f$ is nonconstant. Since $\Omega$ is
connected and $g$ is holomorphic by step <1>1, the identity theorem implies
that the zeros of $g$ are isolated.
:::

<1>6. Choose $r>0$ such that
\[
\overline{D(b,r)}\subset\Omega,
\qquad
a\notin\overline{D(b,r)},
\]
and $g$ has no zeros on
\[
|z-b|=r.
\]

::: {.proof}
The points $a$ and $b$ are distinct, $\Omega$ is open, and the zero at $b$ is
isolated by step <1>5. Hence a sufficiently small radius has all three
properties.
:::

<1>7. For all sufficiently large $n$, the function $g_n$ has at least one
zero in $D(b,r)$.

::: {.proof}
Since $g$ has no zeros on the compact circle
\[
|z-b|=r,
\]
there is
\[
m
=
\min_{|z-b|=r}|g(z)|
>0.
\]
By step <1>3,
\[
g_n\to g
\]
uniformly on that circle. Thus for all sufficiently large $n$,
\[
|g_n(z)-g(z)|<m\le|g(z)|
\qquad(|z-b|=r).
\]
Rouché's theorem implies that $g_n$ and $g$ have the same number of zeros in
$D(b,r)$, counted with multiplicity. Since $g$ has the zero $b$ there,
$g_n$ has at least one zero there as well.
:::

<1>8. This contradicts injectivity of $f_n$.

::: {.proof}
By step <1>6,
\[
a\notin D(b,r).
\]
But step <1>4 says that $a$ is the only zero of $g_n$ anywhere in $\Omega$,
while step <1>7 gives a zero of $g_n$ inside $D(b,r)$. Contradiction.
:::

<1>9. Therefore
\[
\boxed{f\text{ is injective on }\Omega}.
\]

::: {.proof}
The assumption of noninjectivity in step <1>2 leads to the contradiction in
step <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required conclusion.
:::
:::
