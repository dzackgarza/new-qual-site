---
schema: qual/card@1
id: P-CASP22E
kind: problem
title: "Poles of a meromorphic limit appear in the approximating sequence"
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Normal Families
  - Convergence
relations: []
review: draft
---

::: {.problem}
Let $G \subset \CC$ be an open set, $\{f_n\}$ a sequence in $M(G)$, and $f$ a meromorphic function such that $f_n \to f$ in $M(G)$.
Suppose $a \in G$ is a pole of $f$.
Show that there is a sequence $\{a_n\}$ in $G$ such that $a_n \to a$ and $f_n$ has a pole at $a_n$ for sufficiently large $n$.
:::

::: {.solution}

The argument is the card's own, by a contour test for poles and a diagonal selection; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $G\subset\CC$ be open, $f_{n}\in M(G)$ with $f_{n}\to f$ in $M(G)$, and let $a\in G$ be a pole of $f$; write $m\ge1$ for its order. Convergence in $M(G)$ is uniform convergence with respect to the spherical metric on compact subsets of $G$.

::: pf

::: {.pf-step #contour}
There is $r>0$ with $\overline{B(a,r)}\subset G$ such that $a$ is the only pole of $f$ in $\overline{B(a,r)}$ and $\displaystyle\int_{\abs{z-a}=r}(z-a)^{m-1}f(z)\,dz\ne0$.

::: pf-proof
The poles of the meromorphic function $f$ are isolated, so for small enough $r>0$ the closed disc $\overline{B(a,r)}$ lies in $G$ and meets the pole set only in $a$. On the punctured disc $f$ has the Laurent expansion $f(z)=\sum_{k\ge-m}c_{k}(z-a)^{k}$ with $c_{-m}\ne0$ by the definition of the order of a pole. Multiplying by $(z-a)^{m-1}$ gives $c_{-m}(z-a)^{-1}$ plus terms $(z-a)^{j}$ with $j\ne-1$, and integrating term by term over the circle,
$$
\int_{\abs{z-a}=r}(z-a)^{m-1}f(z)\,dz=2\pi i\,c_{-m}\ne0 .
$$
:::

:::

::: {.pf-step #stability}
For all sufficiently large $n$, $\displaystyle\int_{\abs{z-a}=r}(z-a)^{m-1}f_{n}(z)\,dz\ne0$.

::: pf-proof
The circle $C=\{\abs{z-a}=r\}$ is compact and contains no pole of $f$, so $f$ is finite on $C$ and there is $\delta>0$ with $\chi(f(z),\infty)\ge\delta$ on $C$, where $\chi$ is the spherical metric. Convergence in $M(G)$ is uniform on $C$, so for large $n$ one has $\chi\big(f_{n}(z),f(z)\big)<\delta/2$ for $z\in C$, and then $\chi(f_{n}(z),\infty)\ge\delta/2$: $f_{n}$ has no pole on $C$ and, by a compactness argument on the finitely many coordinate patches, $f_{n}\to f$ uniformly on $C$ in the usual sense. Hence
$$
\int_{C}(z-a)^{m-1}f_{n}(z)\,dz\longrightarrow\int_{C}(z-a)^{m-1}f(z)\,dz\ne0
$$
by step [](#contour){.pf-ref}, so the left-hand integral is nonzero for all large $n$.
:::

:::

::: {.pf-step #pole-in-disc}
Each $f_{n}$ with $\displaystyle\int_{C}(z-a)^{m-1}f_{n}\ne0$ has a pole in $B(a,r)$.

::: pf-proof
Suppose $f_{n}$ has no pole in the open disc $B(a,r)$. Since $m\ge1$, the function $z\mapsto(z-a)^{m-1}f_{n}(z)$ is then holomorphic on a neighbourhood of the closed disc $\overline{B(a,r)}$ — the only possible singularity of $f_{n}$ there being $a$, which is excluded, and the factor $(z-a)^{m-1}$ being holomorphic — so its integral over the boundary circle vanishes by Cauchy's theorem. That contradicts the nonvanishing of step [](#stability){.pf-ref}, so $f_{n}$ has a pole in $B(a,r)$.
:::

:::

::: {.pf-step #diagonal}
There is a sequence $a_{n}\to a$ with $a_{n}$ a pole of $f_{n}$ for all sufficiently large $n$.

::: pf-proof
Let $r_{k}\downarrow0$ with $r_{1}=r$ and $\overline{B(a,r_{k})}\subset G$. By steps [](#stability){.pf-ref} and [](#pole-in-disc){.pf-ref} applied with $r_{k}$ in place of $r$, there is $N_{k}$ such that every $n\ge N_{k}$ has a pole of $f_{n}$ in $B(a,r_{k})$; choose the $N_{k}$ increasing. For $N_{k}\le n<N_{k+1}$ let $a_{n}$ be such a pole, so $a_{n}\in B(a,r_{k})$ and hence $\abs{a_{n}-a}<r_{k}$; for $n<N_{1}$ choose $a_{n}$ arbitrarily. Then $\abs{a_{n}-a}<r_{k}\to0$ as $n\to\infty$, so $a_{n}\to a$, and each $f_{n}$ with $n\ge N_{1}$ has a pole at $a_{n}$ by construction. That is the required sequence.
:::

:::

:::
:::
