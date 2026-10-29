---
schema: qual/card@1
id: P-WESCA10-II5
kind: problem
title: 'Entire functions and singularities at infinity'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $f$ be entire.

(a) Prove that $f$ has a removable singularity at infinity if and only if $f$ is constant.

(b) Prove that $f$ has a pole at infinity of order $m$ if and only if $f$ is a polynomial of degree $m$.
:::

::: {.solution}

For $w\ne0$, set
\[
g(w)=f(1/w).
\]

::: pf

::: {.pf-step #s1}

The function $f$ has a removable singularity at infinity if and only if
$f$ is constant.


::: pf-proof

::: {.pf-step #s1-1}

If $f$ has a removable singularity at infinity, then $f$ is constant.


::: pf-proof

By definition, $g$ extends holomorphically across $w=0$. Hence $g$ is bounded
on some disk $|w|<\delta$. Therefore $f(z)=g(1/z)$ is bounded for
$|z|>1/\delta$. Since $f$ is continuous on the compact disk
$|z|\le1/\delta$, it is bounded there as well. Thus $f$ is bounded on all of
$\CC$, so Liouville's theorem implies that $f$ is constant.

:::

:::

::: {.pf-step #s1-2}

If $f$ is constant, then $f$ has a removable singularity at infinity.


::: pf-proof

If $f\equiv c$, then $g(w)=c$ for $w\ne0$, and defining $g(0)=c$ gives a
holomorphic extension across $0$. Thus the singularity at infinity is
removable.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove both implications in part (a).

:::

:::

:::

::: {.pf-step #s2}

If $f$ has a pole at infinity of order $m$, then $f$ is a polynomial of
degree $m$.


::: pf-proof

::: {.pf-step #s2-1}

There are constants $C>0$ and $R>0$ such that
\[
|f(z)|\le C|z|^m
\qquad(|z|\ge R).
\]


::: pf-proof

Since $g$ has a pole of order $m$ at $0$, the function
\[
h(w)=w^m g(w)
\]
extends holomorphically across $0$ with $h(0)\ne0$. In particular, $h$ is
bounded on some disk $|w|<\delta$: say $|h(w)|\le C$. For
$|z|>1/\delta$, put $w=1/z$. Then
\[
|f(z)|
=|g(1/z)|
=|z|^m|h(1/z)|
\le C|z|^m.
\]
Taking $R=1/\delta$ gives the claim.

:::

:::

::: {.pf-step #s2-2}

For every integer $n>m$,
\[
f^{(n)}(0)=0.
\]


::: pf-proof

Fix $n>m$. For every $r\ge R$, Cauchy's estimate on the circle $|z|=r$
and step [](#s2-1){.pf-ref} give
\[
|f^{(n)}(0)|
\le \frac{n!}{r^n}\max_{|z|=r}|f(z)|
\le n!C r^{m-n}.
\]
Because $m-n<0$, letting $r\to\infty$ yields $f^{(n)}(0)=0$.

:::

:::

::: {.pf-step #s2-3}

The Taylor series of $f$ is a polynomial of degree exactly $m$.


::: pf-proof

Step [](#s2-2){.pf-ref} shows that all Taylor coefficients of degrees greater than $m$
vanish, so $f$ is a polynomial of degree at most $m$. If its degree were
$d<m$, then
\[
g(w)=f(1/w)
\]
would have a pole of order $d$ at $0$, contradicting the assumption that the
pole order is $m$. Hence $\deg f=m$.

:::

:::

::: pf-qed

Step [](#s2-3){.pf-ref} proves this implication of part (b).

:::

:::

:::

::: {.pf-step #s3}

If $f$ is a polynomial of degree $m$, then $f$ has a pole at infinity
of order $m$.


::: pf-proof

Write
\[
f(z)=a_m z^m+a_{m-1}z^{m-1}+\cdots+a_0,
\qquad a_m\ne0.
\]
Then
\[
g(w)=f(1/w)
=w^{-m}\bigl(a_m+a_{m-1}w+\cdots+a_0w^m\bigr).
\]
The factor in parentheses is holomorphic and nonzero at $w=0$. Therefore
$g$ has a pole of order exactly $m$ at $0$, so $f$ has a pole of order $m$ at
infinity.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), while steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove both directions of
part (b).

:::

:::

:::
