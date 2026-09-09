---
schema: qual/card@1
id: P-MMAQ-WV7QEYSPXM
kind: problem
title: $H\rtimes_{\varphi_1}K\cong H\rtimes_{\varphi_2}K$ when $K$ is cyclic and $\varphi_1(K)$,
  $\varphi_2(K)$ are conjugate
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Restored the source's omitted hypothesis that both actions are injective when K is infinite; checked against Dummit--Foote 5.5.6 as independently reproduced in University of Utah Math 6320 Exercise 4.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Assume that $K$ is a cyclic group, $H$ is an arbitrary group, and $\varphi_1$
and $\varphi_2$ are homomorphisms from $K$ into $\Aut(H)$ such that
$\varphi_1(K)$ and $\varphi_2(K)$ are conjugate subgroups
of $\Aut(H)$.
If $K$ is infinite, assume in addition that $\varphi_1$ and $\varphi_2$ are
injective.

Prove by constructing an explicit isomorphism that
$H\rtimes_{\varphi_1}K\cong H\rtimes_{\varphi_2} K$.

> Suppose $\sigma_{\varphi_1}(K)\sigma\inv=\varphi_2(K)$
> so that for some $a\in\mathbb Z$ we have $\sigma\varphi_1(k)\sigma\inv
> =\varphi_2(k)^a$for all$k\in K$. Show that the map$\psi:H
> \rtimes_{\varphi_1}K\rightarrow H\rtimes_{\varphi_2}K$
> defined by $\psi((h,k))=(\sigma(h),k^a)$ is a homomorphism.
> Show $\psi$ is bijective by construcing a 2-sided inverse.
:::

::: solution
Write $K=\langle k\rangle$. Choose $\sigma\in\Aut(H)$ such that
\[
\sigma\varphi_1(K)\sigma^{-1}=\varphi_2(K).
\]
Then $\sigma\varphi_1(k)\sigma^{-1}$ is a generator of the cyclic group
$\varphi_2(K)$, so for some $a\in\ZZ$,
\[
\sigma\varphi_1(k)\sigma^{-1}=\varphi_2(k)^a.
\]

<1>1. There is an automorphism $\alpha:K\to K$, $\alpha(k)=k^b$, such that
\[
\sigma\varphi_1(x)\sigma^{-1}=\varphi_2(\alpha(x))
\qquad(x\in K).
\]
::: proof
If $K$ is infinite, the injectivity of $\varphi_1$ and $\varphi_2$ makes both
images infinite cyclic. Since $\varphi_2(k)^a$ generates $\varphi_2(K)$, we
must have $a=\pm1$. Take $b=a$.

Now suppose $|K|=n<\infty$, and let $m=|\varphi_2(K)|$. Conjugacy of the two
images gives $|\varphi_1(K)|=m$. Since a cyclic group has a unique subgroup of
each order, the kernels $\ker\varphi_1$ and $\ker\varphi_2$ are equal, of order
$n/m$. Thus $\varphi_2(k)^a$ generates $\varphi_2(K)$, so $\gcd(a,m)=1$.

We claim that $a$ may be replaced by an integer $b\equiv a\pmod m$ with
$\gcd(b,n)=1$. For every prime $p\mid n$ with $p\nmid m$, choose a residue
$t_p\pmod p$ for which $a+mt_p\not\equiv0\pmod p$; such a residue exists
because multiplication by $m$ is invertible modulo $p$. By the Chinese
remainder theorem choose $t$ realizing all these residues and put $b=a+mt$.
If $p\mid m$, then $p\nmid a$ and hence $p\nmid b$; if $p\mid n$ but
$p\nmid m$, the choice of $t$ gives $p\nmid b$. Therefore $\gcd(b,n)=1$.

Hence $k\mapsto k^b$ is an automorphism $\alpha$ of $K$. Since
$b\equiv a\pmod m$, we have $\varphi_2(k)^b=\varphi_2(k)^a$, and therefore
the displayed intertwining identity holds on the generator $k$, hence on all
of $K$.
:::

<1>2. The map
\[
\Psi:H\rtimes_{\varphi_1}K\longrightarrow H\rtimes_{\varphi_2}K,
\qquad
\Psi(h,x)=(\sigma(h),\alpha(x)),
\]
is an isomorphism.
::: proof
For $(h,x),(h',x')\in H\rtimes_{\varphi_1}K$,
\[
(h,x)(h',x')=(h\varphi_1(x)(h'),xx').
\]
Using the intertwining identity from <1>1,
\[
\begin{aligned}
\Psi((h,x)(h',x'))
&=(\sigma(h\varphi_1(x)(h')),\alpha(xx'))\\
&=(\sigma(h)\,\varphi_2(\alpha(x))(\sigma(h')),\alpha(x)\alpha(x'))\\
&=\Psi(h,x)\Psi(h',x').
\end{aligned}
\]
Thus $\Psi$ is a homomorphism. Since both $\sigma$ and $\alpha$ are
automorphisms, $\Psi$ is bijective. Explicitly, if
$\alpha^{-1}(k)=k^c$, then
\[
\Psi^{-1}(h,x)=(\sigma^{-1}(h),\alpha^{-1}(x))
\]
is its two-sided inverse.
:::
:::
