---
schema: qual/card@1
id: P-CASP06A
kind: problem
title: "Analytic hull properties: distance to boundary and containment in convex hull"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $\Omega$ be an open subset of $\mathbb{C}$.
For a compact subset $K$ of $\Omega$, define the hull $$\hat{K} = \{z \in \Omega : |f(z)| \leq \sup_{w \in K} |f(w)|, \text{ for every } f \in \mathcal{O}(\Omega)\}.$$ Let $\hat{K}_c$ be the convex hull of $K$, namely the smallest convex subset of $\mathbb{C}$ containing $K$.
Show that

(a) $d(K, \mathbb{C} \setminus \Omega) = d(\hat{K}, \mathbb{C} \setminus \Omega)$;

(b) $\hat{K} \subset \hat{K}_c$.
:::

::: {.solution}
Because $K\subset\widehat K$, one direction in (a) is immediate:
\[
d(\widehat K,\mathbb C\setminus\Omega)
\le d(K,\mathbb C\setminus\Omega).
\]
For the reverse inequality, fix $a\in\mathbb C\setminus\Omega$. The function
\[
f_a(z)=\frac1{z-a}
\]
is holomorphic on $\Omega$. Hence for every $z\in\widehat K$,
\[
\frac1{|z-a|}
\le \sup_{w\in K}\frac1{|w-a|}
=\frac1{d(a,K)}.
\]
Thus $|z-a|\ge d(a,K)$. Taking the infimum first over
$z\in\widehat K$ and then over $a\notin\Omega$ gives
\[
d(\widehat K,\mathbb C\setminus\Omega)
\ge d(K,\mathbb C\setminus\Omega),
\]
proving (a).

For (b), suppose $z_0\notin\widehat K_c$. By planar convex separation there
are $\theta\in\mathbb R$ and $c\in\mathbb R$ such that
\[
\operatorname{Re}(e^{-i\theta}z_0)>c
\ge \sup_{w\in K}\operatorname{Re}(e^{-i\theta}w).
\]
For $n\ge1$ set
\[
F_n(z)=\exp(ne^{-i\theta}z).
\]
Then
\[
|F_n(z_0)|
>\sup_{w\in K}|F_n(w)|.
\]
Since $F_n\in\mathcal O(\Omega)$, this shows $z_0\notin\widehat K$. Therefore
\[
\widehat K\subset\widehat K_c.
\]
:::
