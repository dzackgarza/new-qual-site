---
schema: qual/card@1
id: P-APAS06C
kind: problem
title: Non-abelian group of order $p^3$ from $(\mathbb{Z}/p^2\mathbb{Z})^\times$
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $p$ be a prime number.

(a) Show that the order of $\widehat{1+p}$ in $(\mathbb{Z}/p^2\mathbb{Z})^\times$ is equal to $p$.

(b) Use (a) above to construct a non-abelian group of order $p^3$.

(c) Describe the non-abelian group you have constructed in (b) above via generators and relations.

Note.
As usual, $(\mathbb{Z}/p^2\mathbb{Z})^\times$ denotes the multiplicative group consisting of all the congruence classes $\hat{x}\in\mathbb{Z}/p^2\mathbb{Z}$ such that $\gcd(x,p)=1$.
:::

::: {.solution}
<1>1. The class of $1+p$ has order exactly $p$ in $(\mathbb Z/p^2\mathbb Z)^\times$.
::: {.proof}
For every integer $k\ge 0$, the binomial theorem gives
\[
(1+p)^k
=1+kp+\sum_{j=2}^k \binom{k}{j}p^j
\equiv 1+kp\pmod{p^2}.
\]
In particular,
\[
(1+p)^p\equiv 1+p^2\equiv1\pmod{p^2},
\]
so the order divides $p$.

If $1\le k<p$, then $p^2\nmid kp$, hence
\[
(1+p)^k\equiv1+kp\not\equiv1\pmod{p^2}.
\]
Thus no positive exponent smaller than $p$ gives the identity, and the order is exactly $p$.
:::

<1>2. Let
\[
A=\mathbb Z/p^2\mathbb Z
\]
with its additive group structure, and define
\[
\varphi:A\longrightarrow A,
\qquad
\varphi(x)=(1+p)x.
\]
Then $\varphi$ is an automorphism of order $p$.
::: {.proof}
Since $\gcd(1+p,p)=1$, multiplication by $1+p$ is invertible modulo $p^2$, so $\varphi\in\operatorname{Aut}(A)$.
Moreover
\[
\varphi^k(x)=(1+p)^k x.
\]
Thus the order of $\varphi$ equals the order of the unit $\widehat{1+p}$, which is $p$ by <1>1.
:::

<1>3. Let $B=\langle b\rangle\cong C_p$ and let $B$ act on $A$ by sending the generator $b$ to $\varphi$. Then
\[
G=A\rtimes_\varphi B
\]
has order $p^3$.
::: {.proof}
The homomorphism $B\to\operatorname{Aut}(A)$, $b\mapsto\varphi$, is well-defined because $\varphi^p=1$ by <1>2.
As a set, the semidirect product is $A\times B$, so
\[
|G|=|A||B|=p^2p=p^3.
\]
:::

<1>4. The group $G$ is nonabelian.
::: {.proof}
Let $a$ denote the class of $1$ in the cyclic additive group $A$, viewed as an element of $G$.
By the definition of the semidirect product,
\[
bab^{-1}=a^{\,1+p}.
\]
Since $1+p\not\equiv1\pmod{p^2}$, one has $a^{1+p}\ne a$.
Hence $ba\ne ab$, so $G$ is nonabelian.
:::

<1>5. The group constructed above has the presentation
\[
G\cong
\left\langle a,b\ \middle|\ a^{p^2}=1,\ b^p=1,\ bab^{-1}=a^{1+p}\right\rangle.
\]
::: {.proof}
The subgroup $\langle a\rangle$ is cyclic of order $p^2$, the subgroup $\langle b\rangle$ is cyclic of order $p$, and the conjugation relation records exactly the action $b\mapsto\varphi$ used in <1>3.
Every word can therefore be rewritten, using
\[
ba=a^{1+p}b,
\]
in the form $a^ib^j$ with $0\le i<p^2$ and $0\le j<p$.
Thus the presented group has at most $p^3$ elements, while the semidirect product $G$ of <1>3 satisfies the relations and has exactly $p^3$ elements.
The induced surjection from the presented group onto $G$ is therefore an isomorphism.
:::
:::
