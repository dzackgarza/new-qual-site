---
schema: qual/card@1
id: E-YBJTZ
kind: problem
title: The one-point compactification of R is the circle
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 6, printed p. 186, with Theorem 29.1
    on printed p. 183; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.6, PDF p. 22. The line is identified with the
    circle minus one point: t -> (cos 2 pi t, sin 2 pi t) on (-1/2, 1/2) omits (-1,0); the
    circle is then the one-point compactification of the line, unique by Theorem 29.1. The
    aside on this card previously named the omitted point as (1,0) and cited Exercise 29.5
    for uniqueness; both are corrected. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof. The reading found one gap: the earlier prose concluded
    that R and S^1 - {(-1,0)} are homeomorphic from the injectivity and continuity of the restricted
    map alone, which does not give a homeomorphism, since a continuous injection need not be open and
    the codomain here is not compact. The card now exhibits the inverse (x,y) -> arctan(y/(1+x))/pi,
    proves it continuous on the punctured circle and verifies it on both sides, including the
    half-angle identities. The density of the punctured circle in S^1, which the definition of a
    compactification also requires, is now proved rather than asserted. The map and the use of
    Exercise 29.5 are unchanged; the statement was checked against Munkres, Topology (2000), Section
    29 Exercise 6, printed p. 186.
---

::: {.exercise}

Show that the one-point compactification of $\RR$ is homeomorphic with the circle $S^1$.
:::

::: {.solution}

The map and the reduction are **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.6, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the proof that the restriction of $q$ is a *homeomorphism*, and not merely a continuous injection, is supplied here, that solution identifying the two spaces from injectivity alone. The statement was checked against Munkres, *Topology* (2000), §29 Exercise 6, printed p. 186, with the definition of a compactification on printed p. 183, Theorem 27.3 on printed p. 173 and Exercise 29.5 on printed p. 186.

Throughout $S^{1}=\theset{(x,y)\in\RR^{2}\mid x^{2}+y^{2}=1}$ with the subspace topology of $\RR^{2}$, $p\coloneqq(-1,0)$, and
$$
q\colon\RR\longrightarrow S^{1},\qquad q(t)\coloneqq(\cos 2\pi t,\ \sin 2\pi t).
$$

::: pf

::: {.pf-step #q-continuous}

$q$ is continuous and $q(\RR)=S^{1}$.

::: pf-proof

The coordinate functions $t\mapsto\cos 2\pi t$ and $t\mapsto\sin 2\pi t$ are continuous, so $q$ is continuous into $\RR^{2}$ by Theorem 18.4 (printed p. 110); its values satisfy $\cos^{2}2\pi t+\sin^{2}2\pi t=1$, so they lie in $S^{1}$, and $q$ is then continuous as a map into $S^{1}$ by Theorem 18.2(e), printed p. 107. For surjectivity, a point of $S^{1}$ has the form $(\cos\theta,\sin\theta)$ for some $\theta$, and then $q(\theta/2\pi)$ is that point.

:::

:::

::: {.pf-step #restriction}

The restriction of $q$ to $(-1/2,1/2)$ is a homeomorphism of that interval onto $S^{1}-\theset{p}$.

:::: pf-proof

Write $p=(-1,0)$; the three claims below are injectivity, the image, and the continuity of the inverse.

::: {.pf-step #injective}

$q$ is injective on the open interval $(-1/2,1/2)$.

::: pf-proof

Suppose $q(s)=q(t)$ with $s,t\in(-1/2,1/2)$. Then $\cos 2\pi s=\cos 2\pi t$ and $\sin 2\pi s=\sin 2\pi t$, so $2\pi s-2\pi t\in2\pi\ZZ$, that is $s-t\in\ZZ$. But $\abs{s-t}<1$, since both points lie in an interval of length $1$, and the only integer of absolute value less than $1$ is $0$; hence $s=t$.

:::

:::

::: {.pf-step #image}

$q$ carries $(-1/2,1/2)$ onto $S^{1}-\theset{p}$.

::: pf-proof

$q(\pm1/2)=(\cos(\pm\pi),\sin(\pm\pi))=(-1,0)=p$, so no point of $(-1/2,1/2)$ is mapped to $p$; the endpoints are not in the open interval, and by step [](#injective){.pf-ref} no other point is mapped to $p$ either, so the image misses $p$. For the other inclusion, let $(x,y)\in S^{1}$ with $(x,y)\neq p$. Since $x^{2}+y^{2}=1$ and $x\neq-1$, there is a unique $\theta\in(-\pi,\pi)$ with $x=\cos\theta$ and $y=\sin\theta$, namely the principal argument of $(x,y)$; then $t\coloneqq\theta/2\pi$ lies in $(-1/2,1/2)$ and $q(t)=(x,y)$.

:::

:::

::: {.pf-step #inverse}

The map $h\colon S^{1}-\theset{p}\to\RR$, $h(x,y)\coloneqq\frac{1}{\pi}\arctan\dfrac{y}{1+x}$, is continuous and is the two-sided inverse of $q$ restricted to $(-1/2,1/2)$.

::: pf-proof

On $S^{1}$ one has $x\geq-1$ with equality only at $p$, so $1+x>0$ on $S^{1}-\theset{p}$; the quotient $y/(1+x)$ is therefore continuous there, being a quotient of continuous functions with nonvanishing denominator, and $\arctan$ is continuous, so $h$ is continuous.

For $t\in(-1/2,1/2)$ set $x\coloneqq\cos 2\pi t$ and $y\coloneqq\sin 2\pi t$. Then
$$
1+x=1+\cos 2\pi t=2\cos^{2}\pi t,\qquad y=\sin 2\pi t=2\sin\pi t\,\cos\pi t,
$$
so $y/(1+x)=\tan\pi t$ (the denominator is nonzero because $\pi t\in(-\pi/2,\pi/2)$), and $\arctan(\tan\pi t)=\pi t$ because $\pi t$ lies in the range $(-\pi/2,\pi/2)$ of $\arctan$. Hence $h(q(t))=t$.

Conversely let $(x,y)\in S^{1}-\theset{p}$, put $s\coloneqq y/(1+x)$ and $t\coloneqq\arctan s/\pi\in(-1/2,1/2)$. From $x^{2}+y^{2}=1$ one gets $1+s^{2}=1+y^{2}/(1+x)^{2}=\big((1+x)^{2}+y^{2}\big)/(1+x)^{2}=2/(1+x)$, and then
$$
\frac{1-s^{2}}{1+s^{2}}=\frac{(1+x)^{2}-y^{2}}{2(1+x)}=\frac{1+2x+x^{2}-(1-x^{2})}{2(1+x)}=x,\qquad
\frac{2s}{1+s^{2}}=\frac{2y/(1+x)}{2/(1+x)}=y,
$$
which are the identities $\cos 2\theta=(1-\tan^{2}\theta)/(1+\tan^{2}\theta)$ and $\sin 2\theta=2\tan\theta/(1+\tan^{2}\theta)$ at $\theta=\pi t$. So $q(t)=(x,y)$, that is $q(h(x,y))=(x,y)$.

:::

:::

::: pf-step

The restriction of $q$ to $(-1/2,1/2)$ is a homeomorphism of that interval onto $S^{1}-\theset{p}$.

::: pf-proof

It is continuous, being a restriction of the continuous map $q$; it is injective by step [](#injective){.pf-ref} and onto by step [](#image){.pf-ref}; and its inverse is the continuous map $h$ of step [](#inverse){.pf-ref}. A continuous bijection with continuous inverse is a homeomorphism.

:::

:::

::::

:::

::: {.pf-step #s1-compact}

$S^{1}$ is compact Hausdorff.

::: pf-proof

$S^{1}$ is a closed and bounded subset of $\RR^{2}$: it is bounded, being contained in the square $[-1,1]^{2}$, and it is closed, being the preimage of the closed set $\theset{1}$ under the continuous map $(x,y)\mapsto x^{2}+y^{2}$ (Theorem 18.1(3), printed p. 104). So $S^{1}$ is compact by Theorem 27.3 (printed p. 173), and it is Hausdorff as a subspace of the Hausdorff space $\RR^{2}$.

:::

:::

::: {.pf-step #one-point}

$S^{1}$ is the one-point compactification of $S^{1}-\theset{p}$.

:::: pf-proof

By step [](#s1-compact){.pf-ref} the space $S^{1}$ is compact Hausdorff; the two remaining clauses of the definition on printed p. 183 are settled below.

::: {.pf-step #complement}

$S^{1}-\theset{p}$ is a proper subspace of $S^{1}$ and $S^{1}-\big(S^{1}-\theset{p}\big)=\theset{p}$.

::: pf-proof

$p\in S^{1}$ and $p\notin S^{1}-\theset{p}$, while every other point of $S^{1}$ lies in $S^{1}-\theset{p}$; so the difference is the single point $p$ and the subspace is proper.

:::

:::

::: {.pf-step #dense}

The closure of $S^{1}-\theset{p}$ in $S^{1}$ is $S^{1}$.

::: pf-proof

Let $V$ be a subset of $S^{1}$ that is open in $S^{1}$ and contains $p$, say $V=S^{1}\cap U$ with $U$ open in $\RR^{2}$; choose $\varepsilon>0$ with the ball $B(p,\varepsilon)\subset U$. By step [](#q-continuous){.pf-ref} the map $q$ is continuous, so for some $\delta\in(0,1/2)$ the points $q(t)$ with $\abs{t+1/2}<\delta$ lie in $B(p,\varepsilon)$; taking such a $t$ in $(-1/2,1/2)$ one has $q(t)\neq p$ by step [](#image){.pf-ref}, so $V$ meets $S^{1}-\theset{p}$. Hence every neighbourhood in $S^{1}$ of the one point outside $S^{1}-\theset{p}$ meets it, and the closure is $S^{1}$.

:::

:::

::::

:::

::: {.pf-step #line}

$\RR$ is locally compact Hausdorff and is not compact.

::: pf-proof

$\RR$ is Hausdorff, being a metric space. At a point $x$ the closed interval $[x-1,x+1]$ is compact by Theorem 27.3 (printed p. 173), being closed and bounded, and it contains the neighbourhood $(x-1,x+1)$ of $x$; so $\RR$ is locally compact at each of its points. The cover by the intervals $(-n,n)$, $n\in\ZZ_{+}$, is an open cover with no finite subcover, since finitely many of them are contained in $(-N,N)$ for the largest index $N$ occurring; so $\RR$ is not compact.

:::

:::

::: pf-step

Therefore the one-point compactification of $\RR$ is homeomorphic with $S^{1}$.

::: pf-proof

By step [](#line){.pf-ref} the line is a locally compact Hausdorff space that is not compact, so it has a one-point compactification $\RR^{+}$, and by step [](#one-point){.pf-ref} the space $S^{1}$ is the one-point compactification of $S^{1}-\theset{p}$, which is locally compact Hausdorff as the image of $\RR$ under the homeomorphism of step [](#restriction){.pf-ref}. Exercise 29.5 (printed p. 186) says that a homeomorphism of locally compact Hausdorff spaces extends to a homeomorphism of their one-point compactifications; applied to the homeomorphism of step [](#restriction){.pf-ref} it gives $\RR^{+}$ homeomorphic with $S^{1}$.

:::

:::

:::

:::
