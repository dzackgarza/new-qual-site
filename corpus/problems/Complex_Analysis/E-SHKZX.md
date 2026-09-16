---
schema: qual/card@1
id: E-SHKZX
kind: problem
title: If poles accumulate at $a$, then every $w\in\mathbb{C}$ is a sequential limit
  of $f$, versus Casorati–Weierstrass
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Poles
  - Singularities
  - Identity Theorem
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic in $\Omega: 0<|z-a|<r$ except at a
sequence of poles $a_n \in \Omega$ with
$\lim_{n \rightarrow \infty} a_n = a$. Show that for any
$w \in \mathbb C$, there exists a sequence $z_n \in \Omega$ such
that $\lim_{n \rightarrow \infty} f(z_n) = w$.

Explain the similarity and difference between the above assertion and the Weierstrass-Casorati theorem.

:::

::: {.solution}
We prove the stronger conclusion that the sequence can be chosen with
$z_n\to a$.

Fix $w\in\CC$. Suppose this stronger conclusion fails. Then there are
$\varepsilon>0$ and $\delta>0$ such that
\[
|f(z)-w|\ge\varepsilon
\]
whenever $0<|z-a|<\delta$ and $z$ is not one of the poles of $f$.
Indeed, otherwise for every $n$ one could choose $z_n$ with
$0<|z_n-a|<1/n$ and $|f(z_n)-w|<1/n$.

On the punctured disk, away from the poles, define
\[
G(z)={1\over f(z)-w}.
\]
Then $|G(z)|\le\varepsilon^{-1}$. At each pole $a_k$ of $f$ lying in this
disk, $G(z)\to0$ as $z\to a_k$, so $a_k$ is a removable singularity of $G$
and the extension satisfies $G(a_k)=0$. After filling in all such points,
$G$ is holomorphic and bounded on $0<|z-a|<\delta$. Hence $a$ is also a
removable singularity of $G$.

Because $a_k\to a$ and $G(a_k)=0$, continuity of the extension gives
$G(a)=0$. Thus the zeros $a_k$ of the extended holomorphic function $G$
accumulate at the interior point $a$. The identity theorem gives $G\equiv0$
on the disk. This is impossible, since at every ordinary point where $f$ is
finite one has $G=1/(f-w)\ne0$.

Therefore for every $w\in\CC$ there exists a sequence $z_n\to a$ with
$f(z_n)\to w$.

This resembles Casorati--Weierstrass because every finite complex value is a
limit value arbitrarily near $a$. The difference is that Casorati--Weierstrass
concerns an isolated essential singularity, whereas here $a$ is not an isolated
singularity at all: poles of $f$ accumulate at $a$.

:::
