---
schema: qual/card@1
id: P-AGFS15-02
kind: problem
title: Morphisms of affine varieties and coordinate-ring maps
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained Algebraic Geometry FS 15 exam-guidelines PDF dated August 12, 2015.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified both coordinate-ring implications and the affine-line and affine-plane automorphism claims by explicit algebra and counterexamples.
---

::: {.problem}
Let $f:X\to Y$ be a morphism of affine varieties and let $f^\sharp:A(Y)\to A(X)$ be the induced homomorphism of coordinate rings.
Determine whether each statement is true or false.

1. $f$ is surjective if and only if $f^\sharp$ is injective.

2. $f$ is injective if and only if $f^\sharp$ is surjective.

3. If $f:\mathbb A^1\to\mathbb A^1$ is an isomorphism, then $f$ is affine linear: $f(x)=ax+b$ for some $a,b\in k$.

4. If $f:\mathbb A^2\to\mathbb A^2$ is an isomorphism, then $f$ is affine linear: $f(x)=Ax+b$ for some $A\in\operatorname{Mat}_{2,2}(k)$ and $b\in k^2$.
:::


::: {.solution}
The truth values are
\[
\boxed{\text{False},\ \text{False},\ \text{True},\ \text{False}}.
\]

<1>1. Statement 1 is false.
::: {.proof}
If \(f:X\to Y\) is surjective and \(g\in A(Y)\) satisfies \(f^\sharp(g)=g\circ f=0\), then \(g\) vanishes at every point of \(Y\), hence \(g=0\). Thus surjectivity of \(f\) does imply injectivity of \(f^\sharp\).

The converse fails. Take the open immersion
\[
j:\mathbb G_m\hookrightarrow\mathbb A^1.
\]
On coordinate rings,
\[
j^\sharp:k[t]\longrightarrow k[t,t^{-1}]
\]
is the natural inclusion, so it is injective, but \(j\) is not surjective because \(0\notin\mathbb G_m\).
:::

<1>2. Statement 2 is false.
::: {.proof}
If \(f^\sharp:A(Y)\to A(X)\) is surjective, then \(f\) is a closed immersion onto the closed subvariety cut out by \(\ker f^\sharp\); in particular, \(f\) is injective.

Again the converse fails for
\[
j:\mathbb G_m\hookrightarrow\mathbb A^1.
\]
The map \(j\) is injective, but
\[
j^\sharp:k[t]\longrightarrow k[t,t^{-1}]
\]
is not surjective because \(t^{-1}\) is not in its image.
:::

<1>3. Statement 3 is true.
::: {.proof}
An isomorphism \(f:\mathbb A^1\to\mathbb A^1\) induces a \(k\)-algebra automorphism
\[
f^\sharp:k[t]\longrightarrow k[t].
\]
Write \(f^\sharp(t)=p(t)\). If \(q(t)\) is the image of \(t\) under the inverse automorphism, then
\[
q(p(t))=t.
\]
Therefore
\[
1=\deg(q\circ p)=\deg q\,\deg p,
\]
so \(\deg p=1\). Hence
\[
p(t)=at+b
\]
with \(a\ne0\), and therefore \(f(x)=ax+b\).
:::

<1>4. Statement 4 is false.
::: {.proof}
Consider
\[
F:\mathbb A^2\longrightarrow\mathbb A^2,
\qquad
F(x,y)=(x,y+x^2).
\]
It has polynomial inverse
\[
F^{-1}(u,v)=(u,v-u^2),
\]
so \(F\) is an isomorphism. But \(F\) is not affine linear because its second coordinate contains the quadratic term \(x^2\).
:::
:::
