---
schema: qual/card@1
id: P-JHUFA10RA4
kind: problem
title: 'Translation operator on $L^2$ has no real eigenvalues'
classification:
  areas:
  - real-analysis
  topics:
  - Operator Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against the Fall 2010 JHU Analysis Qualifying Exam in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked Fall 2010 problem 4 on PDF page 26 and compared both complete cards. P-JHUMAY11ANL is the same translation-eigenvector problem, not a May 2011 appearance, and is merged into this card."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Read both proofs and retained their isometry and periodic-integral argument, including the zero-vector alternative and the null-set justification for integer translates."
---

::: {.problem}
Define $U : L^2(\RR) \to L^2(\RR)$ by

$$Uf(x) = f(x - 1).$$

Show that if $f \in L^2$ satisfies $Uf = \lambda f$, for some $\lambda \in \RR$ (i.e., $f$ is an eigenvector of $U$) then $f$ must be the zero element, i.e., $f = 0$ almost everywhere.
:::

::: {.solution}

::: pf

::: pf-step
A nonzero solution would have $\abs{\lambda}=1$.

::: pf-proof
Suppose
$$
Uf=\lambda f,
\qquad\text{that is,}\qquad
f(x-1)=\lambda f(x)
\quad\text{a.e.}
$$
The change of variable $y=x-1$ gives
$\norm{Uf}_2^2=\int_{\RR}\abs{f(x-1)}^2\,dx=\norm{f}_2^2$.
Thus $U$ is an isometry on $L^2(\RR)$, so
$$
\norm{f}_2=\norm{Uf}_2=\abs{\lambda}\,\norm{f}_2.
$$
Thus either $f=0$ in $L^2$, in which case there is nothing to prove, or else
$$
\abs{\lambda}=1.
$$
Since $\lambda\in\RR$, a nonzero eigenvector could therefore occur only for $\lambda=1$ or $\lambda=-1$.
:::

:::

::: pf-step
Either remaining value forces the squared modulus to have infinite integral unless $f=0$.

::: pf-proof
In either case,
$$
\abs{f(x-1)}=\abs{f(x)}
\quad\text{a.e.},
$$
so $\abs{f}^2$ is $1$-periodic almost everywhere. Let
$$
a:=\int_0^1 \abs{f(x)}^2\,dx.
$$
For each integer $k$, iteration of the almost-everywhere
periodicity gives $\abs{f(x+k)}^2=\abs{f(x)}^2$ almost everywhere;
only finitely many translates of the exceptional null
set are needed for that $k$. Translation invariance therefore gives
$$
\int_k^{k+1}\abs{f(x)}^2\,dx=a.
$$
Hence
$$
\norm{f}_2^2
=\sum_{k\in\ZZ}\int_k^{k+1}\abs{f(x)}^2\,dx
=\sum_{k\in\ZZ}a.
$$
Because $f\in L^2(\RR)$, this sum is finite. Therefore $a=0$, and consequently $f=0$ almost everywhere on every interval $[k,k+1]$. Thus
$$
f=0\qquad\text{a.e. on }\RR.
$$
:::

:::

:::
:::
