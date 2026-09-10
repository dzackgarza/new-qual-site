---
schema: qual/card@1
id: E-RX3N7
kind: problem
title: Galois group and intermediate fields of $\QQ(\sqrt{2+\sqrt{2}})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
12. For $u=\sqrt{2+\sqrt2}$, determine the Galois group of $\QQ(u)/\QQ$ and all intermediate fields.
:::

::: {.solution}
Set
\[
L=\QQ(u),
\qquad
u=\sqrt{2+\sqrt2}.
\]

<1>1. The minimal polynomial of $u$ over $\QQ$ is
\[
f(x)=x^4-4x^2+2,
\]
and $[L:\QQ]=4$.
::: {.proof}
From
\[
u^2=2+\sqrt2
\]
we obtain
\[
(u^2-2)^2=2,
\]
so $f(u)=0$. Also
\[
\sqrt2=u^2-2\in L,
\]
so $\QQ(\sqrt2)\subseteq L$.

Let $E=\QQ(\sqrt2)$. If $u\in E$, then $2+\sqrt2$ would be a square in $E$. But
\[
N_{E/\QQ}(2+\sqrt2)=(2+\sqrt2)(2-\sqrt2)=2,
\]
which is not a square in $\QQ$, whereas the norm of a square in $E$ is a square in $\QQ$. Hence $u\notin E$, so
\[
[L:E]=2.
\]
Since $[E:\QQ]=2$, one gets $[L:\QQ]=4$. Therefore the degree-$4$ polynomial $f$ is the minimal polynomial of $u$.
:::

<1>2. The polynomial $f$ splits in $L$.
::: {.proof}
Put
\[
v=\sqrt{2-\sqrt2}.
\]
Then
\[
uv=\sqrt{(2+\sqrt2)(2-\sqrt2)}=\sqrt2,
\]
so
\[
v=\frac{\sqrt2}{u}\in L.
\]
The four roots of $f$ are
\[
\pm u,\qquad \pm v,
\]
all of which lie in $L$. Thus $L/\QQ$ is the splitting field of the separable polynomial $f$, hence is Galois.
:::

<1>3. The Galois group is cyclic of order $4$.
::: {.proof}
Define $\sigma\in\Gal(L/\QQ)$ by
\[
\sigma(u)=v.
\]
Since
\[
\sqrt2=u^2-2,
\]
we have
\[
\sigma(\sqrt2)=v^2-2=-\sqrt2.
\]
Using $v=\sqrt2/u$,
\[
\sigma(v)=\frac{\sigma(\sqrt2)}{\sigma(u)}
=\frac{-\sqrt2}{v}
=-u.
\]
Therefore
\[
u\xmapsto{\sigma}v\xmapsto{\sigma}-u\xmapsto{\sigma}-v\xmapsto{\sigma}u.
\]
Thus $\sigma$ has order $4$. Since $|\Gal(L/\QQ)|=[L:\QQ]=4$, it follows that
\[
\Gal(L/\QQ)=\langle\sigma\rangle\cong C_4.
\]
:::

<1>4. The only proper nontrivial intermediate field is
\[
\QQ(\sqrt2).
\]
::: {.proof}
A cyclic group of order $4$ has a unique subgroup of order $2$, namely $\langle\sigma^2\rangle$. By the Galois correspondence, $L/\QQ$ therefore has a unique intermediate field of degree $2$ over $\QQ$.

Now $\sigma^2(u)=-u$, so
\[
\sigma^2(\sqrt2)=\sigma^2(u^2-2)=u^2-2=\sqrt2.
\]
Hence $\QQ(\sqrt2)$ is fixed by $\langle\sigma^2\rangle$. Since it has degree $2$ over $\QQ$, it is exactly the corresponding fixed field.
:::

<1>5. Hence the full intermediate-field lattice is
\[
\QQ\subsetneq\QQ(\sqrt2)\subsetneq L=\QQ(\sqrt{2+\sqrt2}).
\]
::: {.proof}
This is <1>4 together with the bottom and top fields.
:::
:::
