---
schema: qual/card@1
id: P-BKF13-1B
kind: problem
title: Convergence of $\sum n^a(\log n)^b$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 1B in the retained Fall 2013 Berkeley prelim exam
    and independently reviewed the retained solution packet F13_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both comparison regimes away from a=-1 and the logarithmic
    integral-test boundary at a=-1.
---

::: {.problem}
For which pairs of real numbers $(a,b)$ does the series $\sum_{n=3}^{\infty}n^a(\log n)^b$ converge?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $c>0$ and $\varepsilon>0$,
$$
(\log n)^c=o(n^\varepsilon).
$$

::: pf-proof

Taking logarithms, it is enough to show
$$
c\log\log n-\varepsilon\log n\longrightarrow-\infty.
$$
But
$$
\frac{\log\log n}{\log n}\longrightarrow0,
$$
since with $u=\log n$ this is $\log u/u\to0$, for example by
l'Hospital's rule. Hence the negative term
$-\varepsilon\log n$ dominates.

:::

:::

::: {.pf-step #s2}

If $a<-1$, then the series converges for every real $b$.

::: pf-proof

If $b\le0$, then $(\log n)^b\le1$ for $n\ge3$, so
$$
n^a(\log n)^b\le n^a,
$$
and $\sum n^a$ converges because $a<-1$.

If $b>0$, choose $\varepsilon>0$ with
$$
a+\varepsilon<-1.
$$
By step [](#s1){.pf-ref}, for all sufficiently large $n$,
$$
(\log n)^b\le n^\varepsilon.
$$
Hence
$$
n^a(\log n)^b
\le n^{a+\varepsilon},
$$
and the comparison series converges.

:::

:::

::: {.pf-step #s3}

If $a>-1$, then the series diverges for every real $b$.

::: pf-proof

If $b\ge0$, then $(\log n)^b\ge1$ for $n\ge3$, so
$$
n^a(\log n)^b\ge n^a.
$$
The series $\sum n^a$ diverges because $a>-1$.

If $b<0$, choose $\varepsilon>0$ with
$$
a-\varepsilon>-1.
$$
Applying step [](#s1){.pf-ref} with $c=-b>0$ gives, for all sufficiently large
$n$,
$$
(\log n)^{-b}\le n^\varepsilon.
$$
Taking reciprocals,
$$
(\log n)^b\ge n^{-\varepsilon},
$$
and therefore
$$
n^a(\log n)^b
\ge n^{a-\varepsilon}.
$$
The series on the right diverges.

:::

:::

::: {.pf-step #s4}

If $a=-1$, then the series converges exactly when $b<-1$.

::: pf-proof

Consider
$$
f(x)=\frac{(\log x)^b}{x}.
$$
For all sufficiently large $x$ this function is positive and
decreasing, because
$$
f'(x)
=
x^{-2}(\log x)^{b-1}(b-\log x).
$$
Thus the integral test applies. With $u=\log x$,
$$
\int_3^\infty\frac{(\log x)^b}{x}\,dx
=
\int_{\log3}^\infty u^b\,du,
$$
which converges exactly when $b<-1$.

:::

:::

::: {.pf-step #s5}

Therefore the convergence region is
$$
\boxed{
\{(a,b)\in\RR^2:a<-1\}
\;\cup\;
\{(-1,b):b<-1\}.
}
$$

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} cover the three mutually exclusive cases
$a<-1$, $a=-1$, and $a>-1$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the complete classification.

:::

:::

:::
