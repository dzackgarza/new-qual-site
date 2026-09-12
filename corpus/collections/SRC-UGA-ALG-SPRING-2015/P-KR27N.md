---
schema: qual/card@1
id: P-KR27N
kind: problem
title: Galois group of $x^4-5$ over $\QQ$ and over $\QQ(\sqrt{5})$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $f(x) = x^4 - 5 \in \QQ[x]$.

a. Compute the Galois group of $f$ over $\QQ$.

b. Compute the Galois group of $f$ over $\QQ(\sqrt{5})$.
:::

::: solution
Let $\alpha=5^{1/4}>0$. The roots of $x^4-5$ are
\[
\alpha,-\alpha,i\alpha,-i\alpha,
\]
so its splitting field is
\[
E=\mathbb Q(\alpha,i).
\]
Eisenstein's criterion at $5$ shows that $x^4-5$ is irreducible, hence
\[
[\mathbb Q(\alpha):\mathbb Q]=4.
\]
Since $\mathbb Q(\alpha)\subset\mathbb R$, it does not contain $i$, so
\[
[E:\mathbb Q]=8.
\]

Define automorphisms
\[
r(\alpha)=i\alpha,\qquad r(i)=i,
\]
and
\[
s(\alpha)=\alpha,\qquad s(i)=-i.
\]
Then $r$ has order $4$, $s$ has order $2$, and
\[
srs=r^{-1}.
\]
These generate $8$ distinct automorphisms, so
\[
\operatorname{Gal}(E/\mathbb Q)
\cong
\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle,
\]
the dihedral group of order $8$.

Now let $K=\mathbb Q(\sqrt5)=\mathbb Q(\alpha^2)$. Since
\[
r(\alpha^2)=-\alpha^2,
\]
$r$ does not fix $K$, while $r^2$, $s$, and $r^2s$ do. Therefore
\[
\operatorname{Gal}(E/K)=\{1,r^2,s,r^2s\}.
\]
Each nonidentity element in this subgroup has order $2$, so
\[
\operatorname{Gal}(E/\mathbb Q(\sqrt5))\cong C_2\times C_2.
\]
:::
