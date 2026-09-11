---
schema: qual/card@1
id: P-BKF82-2
kind: problem
title: Reduction modulo the ideal $(7,x-3)$ in $\mathbb Z[x]$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Identified (7,x-3) as the kernel of evaluation at 3 modulo 7 and reduced the given polynomial using powers of 3 modulo 7."
---

::: problem
Let $R=\mathbb Z[x]$ and $I=(7,x-3)$.

(a) Show that for every $r\in R$ there is an integer $0\le\alpha\le6$ such that $r-\alpha\in I$.

(b) Find $\alpha$ for $r=x^{250}+15x^{14}+x^2+5$.
:::

::: solution
Define
$$
\varphi:\mathbb Z[x]\longrightarrow\mathbb F_7,
\qquad
\varphi(r)=r(3)\pmod7.
$$

<1>1. The kernel of $\varphi$ is $I=(7,x-3)$.
::: proof
Certainly
$$
7\in\ker\varphi
$$
and
$$
x-3\in\ker\varphi,
$$
so
$$
I\subseteq\ker\varphi.
$$

Conversely, for any $r\in\mathbb Z[x]$, division by the monic polynomial
$x-3$ gives
$$
r(x)=(x-3)q(x)+r(3)
$$
with $q(x)\in\mathbb Z[x]$. If $r\in\ker\varphi$, then $r(3)$ is divisible
by $7$, so
$$
r(3)=7m
$$
for some $m\in\mathbb Z$. Hence
$$
r=(x-3)q+7m\in I.
$$
Thus
$$
\boxed{\ker\varphi=I.}
$$
:::

<1>2. Every polynomial has a unique residue representative among $0,1,\ldots,6$.
::: proof
For $r\in\mathbb Z[x]$, choose the unique integer
$$
0\le\alpha\le6
$$
such that
$$
\alpha\equiv r(3)\pmod7.
$$
Then
$$
\varphi(r-\alpha)=0,
$$
so by step <1>1,
$$
r-\alpha\in I.
$$
This proves part (a).
:::

<1>3. Compute the residue for the given polynomial.
::: proof
For
$$
r=x^{250}+15x^{14}+x^2+5,
$$
we calculate modulo $7$. Since
$$
3^6\equiv1\pmod7,
$$
and
$$
250\equiv4\pmod6,
$$
we have
$$
3^{250}\equiv3^4\equiv4\pmod7.
$$
Also
$$
15\equiv1\pmod7,
\qquad
14\equiv2\pmod6,
$$
so
$$
15\cdot3^{14}\equiv3^2\equiv2\pmod7.
$$
Finally
$$
3^2\equiv2\pmod7.
$$
Therefore
$$
r(3)
\equiv4+2+2+5
\equiv13
\equiv6\pmod7.
$$
Hence
$$
\boxed{\alpha=6.}
$$
:::
:::
