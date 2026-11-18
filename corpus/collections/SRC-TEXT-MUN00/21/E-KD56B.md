---
schema: qual/card@1
id: E-KD56B
kind: problem
title: First countability of the lower limit topology and the ordered square
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 4, printed p. 134, with the lower
    limit topology of §13 and the ordered square of §16; the stored statement is the printed
    one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.4, PDF p. 24. Explicit countable bases are
    given at every point: half-open intervals of decreasing length in R_l, and in the
    ordered square at the two corners, at points of the interior fibres, and at the two
    kinds of boundary point of a fibre. (tmp/sources/munkres-solutions-positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the four-fold case analysis into numbered steps, one per kind of point, each with the
    two things first countability needs: that the listed sets are open neighbourhoods of the point,
    and that every neighbourhood of the point contains one of them. Supplied the reduction used
    silently in the ordered square: any basis element of the order topology containing an interior
    point contains an open interval around it, after which the estimates on the two endpoints are
    elementary. Checked the endpoint estimates for each case against the dictionary order, including
    the two corner cases where the basis element is an initial or final segment. Not re-read this
    session: the positron0802 page, PDF p. 24.
---

::: {.exercise}

Show that $\RR_\ell$ and the ordered square satisfy the first countability axiom.
(This result does not, of course, imply that they are metrizable.)
:::

::: {.solution}

The countable bases at each kind of point are those of **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.4, PDF p. 24** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the verifications that each family is a basis at its point are written out below.

A space is first countable when each of its points has a countable basis of neighbourhoods: a countable family $\{B_{n}\}$ of neighbourhoods of $x$ such that every neighbourhood of $x$ contains some $B_{n}$.

::: pf

::: {.pf-step #rell}
$\RR_{\ell}$ is first countable.

::: pf-proof
For $x\in\RR_{\ell}$ put $U_{n}=[x,x+1/n)$ for $n\in\ZZ_{+}$. Each $U_{n}$ is a basis element of the lower limit topology, hence open, and contains $x$; the family is countable. Let $V$ be a neighbourhood of $x$. Then $V$ contains a basis element $[a,b)$ with $x\in[a,b)$, so $a\leq x<b$ and $b-x>0$; choose $n$ with $1/n<b-x$, which gives $x+1/n<b$ and hence $U_{n}=[x,x+1/n)\subset[a,b)\subset V$. So $\{U_{n}\}$ is a countable basis at $x$.
:::

:::

::: {.pf-step #square-basis}
In the ordered square $I_{o}^{2}$ every basis element of the order topology containing a point $p$ contains an open interval $(L,U)$ with $L<p<U$.

::: pf-proof
A basis element containing $p$ is either an open interval $(L,U)$ with $L<p<U$, or an initial segment $[\min,U)$ with $p<U$, or a final segment $(L,\max]$ with $L<p$. In the first case take the element itself. In the second, $p\neq\min$ and $(L,U)\coloneqq(\min,U)$ contains $p$; in the third, $(L,U)\coloneqq(L,\max)$ contains $p$. So in every case $p$ lies inside an open interval $(L,U)$ contained in the basis element.
:::

:::

::: {.pf-step #corner-min}
The sets $U_{n}=[0\times0,\,0\times1/n)$ form a countable basis at $0\times0$.

::: pf-proof
Each $U_{n}$ is an initial segment, hence open in the order topology, and contains $0\times0$. Let $V$ be a neighbourhood of $0\times0$ and let $B\subset V$ be a basis element containing it. Since $0\times0$ is the least element, there is no element below it, so $B$ cannot be an open interval with a lower endpoint and must be an initial segment $[\min,U)=\{x\mid x<U\}$; write $U=(c,d)$, so that $0\times0<(c,d)$, that is $c>0$, or $c=0$ and $d>0$. If $c>0$ then $0\times1/n<(c,d)$ for every $n$ and $U_{n}\subset(L,U)$; if $c=0$ choose $n$ with $1/n<d$, then $0\times1/n<(0,d)$. In both cases $U_{n}\subset V$.
:::

:::

::: {.pf-step #corner-max}
The sets $V_{n}=(1\times(1-1/n),\,1\times1]$ form a countable basis at $1\times1$.

::: pf-proof
Each $V_{n}$ is a final segment, hence open, and contains $1\times1$. Let $V$ be a neighbourhood of $1\times1$ and let $B\subset V$ be a basis element containing it. As $1\times1$ is the greatest element, $B$ must be a final segment $(L,\max]$; write $L=(c,d)$ with $(c,d)<1\times1$, that is $c<1$, or $c=1$ and $d<1$. If $c<1$ then $(c,d)<1\times(1-1/n)$ for every $n$, so $V_{n}\subset(L,U)$; if $c=1$ choose $n$ with $1-1/n>d$, then $(1,(1-1/n))>L$. In both cases $V_{n}\subset V$.
:::

:::

::: {.pf-step #interior}
At $a\times b$ with $0<b<1$ the sets $\bigl(a\times(b-\delta/n),\,a\times(b+\delta/n)\bigr)$, with $\delta=\min\{b,1-b\}>0$, form a countable basis.

::: pf-proof
Each is an open interval of the order topology containing $a\times b$, and the family is countable. Let $V$ be a neighbourhood of $a\times b$ containing an open interval $(L,U)$ with $L< a\times b<U$, where $L=(c,d)$ and $U=(e,f)$. From $L<a\times b$: either $c<a$, or $c=a$ and $d<b$. From $a\times b<U$: either $a<e$, or $a=e$ and $b<f$. Choose $n$ with $\delta/n<b-d$ in the case $c=a$ and with $\delta/n<f-b$ in the case $a=e$; then $a\times(b-\delta/n)>L$ in either case ($c<a$ gives it for every $n$) and $a\times(b+\delta/n)<U$. So the listed interval lies inside $(L,U)\subset V$.
:::

:::

::: {.pf-step #bottom}
At $a\times0$ with $a>0$ the sets $\bigl((a-a/n)\times0,\ a\times1/n\bigr)$ form a countable basis.

::: pf-proof
Each is an open interval containing $a\times0$, since $(a-a/n)\times0<a\times0<a\times1/n$. Let $V$ contain $(L,U)$ with $L<a\times0<U$. Write $L=(c,d)$; the inequality $(c,d)<a\times0$ forces $c<a$ (if $c=a$ then $d<0$, impossible), so $c<a$. Write $U=(e,f)$; from $a\times0<U$ either $a<e$, or $a=e$ and $0<f$. Choose $n$ with $a-a/n>c$ and, in the case $e=a$, with $1/n<f$. Then $(a-a/n)\times0>L$ and $a\times1/n<U$ (for $a<e$ this holds for every $n$), so the listed interval lies in $(L,U)\subset V$.
:::

:::

::: {.pf-step #top}
At $a\times1$ with $a<1$ the sets $\bigl(a\times(1-1/n),\ (a+(1-a)/n)\times1\bigr)$ form a countable basis.

::: pf-proof
Each is an open interval containing $a\times1$, since $a\times(1-1/n)<a\times1<(a+(1-a)/n)\times1$. Let $V$ contain $(L,U)$ with $L<a\times1<U$, $L=(c,d)$ and $U=(e,f)$. From $L<a\times1$: either $c<a$, or $c=a$ and $d<1$. From $a\times1<U$ we must have $a<e$, since $a=e$ would force $1<f$. Choose $n$ with $a+(1-a)/n<e$ and, in the case $c=a$, with $1-1/n>d$. Then $a\times(1-1/n)>L$ and $(a+(1-a)/n)\times1<U$, so the listed interval lies in $(L,U)\subset V$.
:::

:::

::: {.pf-step}
$\RR_{\ell}$ and the ordered square are first countable.

::: pf-proof
Step [](#rell){.pf-ref} gives a countable basis at each point of $\RR_{\ell}$, and steps [](#corner-min){.pf-ref}, [](#corner-max){.pf-ref}, [](#interior){.pf-ref}, [](#bottom){.pf-ref} and [](#top){.pf-ref} cover every point $a\times b$ of the ordered square, the cases $b\in(0,1)$, $b=0$ with $a>0$, $b=1$ with $a<1$, and the two corners being exhaustive.
:::

:::

:::

:::
