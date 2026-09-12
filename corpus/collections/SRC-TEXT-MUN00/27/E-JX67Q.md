---
schema: qual/card@1
id: E-JX67Q
kind: problem
title: The Cantor set
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Let $A_0$ be the closed interval $[0, 1]$ in $\mathbb{R}$.
Let $A_1$ be the set obtained from $A_0$ by deleting its "middle third" $(\tfrac{1}{3}, \tfrac{2}{3})$.
Let $A_2$ be the set obtained from $A_1$ by deleting its "middle thirds" $(\tfrac{1}{9}, \tfrac{2}{9})$ and $(\tfrac{7}{9}, \tfrac{8}{9})$.
In general, define $A_n$ by the equation

$$
A_n = A_{n-1} - \bigcup_{k=0}^{\infty} \left( \frac{1+3k}{3^n}, \frac{2+3k}{3^n} \right).
$$

The intersection

$$
C = \bigcap_{n \in \mathbb{Z}_+} A_n
$$

is called the Cantor set; it is a subspace of $[0, 1]$.

(a) Show that $C$ is totally disconnected.

(b) Show that $C$ is compact.

(c) Show that each set $A_n$ is a union of finitely many disjoint closed intervals of length $1/3^n$; and show that the end points of these intervals lie in $C$.

(d) Show that $C$ has no isolated points.

(e) Conclude that $C$ is uncountable.
:::

::: {.solution}
Write \(C\) for the Cantor set.

(a) Let \(x<y\) be distinct points of \(C\). Choose \(n\) so large that \(3^{-n}<y-x\). The components of \(A_n\) are pairwise disjoint closed intervals of length \(3^{-n}\), so \(x\) and \(y\) cannot lie in the same component interval. Hence some deleted middle-third interval separates them. Therefore \(C\) admits a separation with \(x\) and \(y\) in different sides. Thus no connected subset of \(C\) contains two points, so \(C\) is totally disconnected.

(b) Each \(A_n\) is closed in compact \([0,1]\), hence compact, and
\[
C=\bigcap_{n\ge1}A_n
\]
is closed in \([0,1]\). Therefore \(C\) is compact.

(c) Inductively, \(A_0=[0,1]\). At stage \(n\), each component interval of \(A_{n-1}\), of length \(3^{-(n-1)}\), has its open middle third deleted, leaving two disjoint closed intervals of length \(3^{-n}\). Hence \(A_n\) is the union of \(2^n\) pairwise disjoint closed intervals of length \(3^{-n}\). Endpoints are never deleted at later stages, so every endpoint belongs to every subsequent \(A_m\), hence lies in \(C\).

(d) Fix \(x\in C\) and \(\varepsilon>0\). Choose \(n\) with \(3^{-n}<\varepsilon\), and let \(I_n\) be the component interval of \(A_n\) containing \(x\). One endpoint \(e_n\) of \(I_n\) is distinct from \(x\) unless \(x\) itself is that endpoint; in that case take the other endpoint. By (c), \(e_n\in C\), and
\[
0<|e_n-x|\le 3^{-n}<\varepsilon.
\]
Thus every neighborhood of \(x\) contains another point of \(C\), so \(C\) has no isolated points.

(e) For each binary sequence \(\epsilon=(\epsilon_1,\epsilon_2,\dots)\in\{0,1\}^{\omega}\), choose recursively the left subinterval at stage \(n\) if \(\epsilon_n=0\) and the right subinterval if \(\epsilon_n=1\). This gives nested closed intervals \(I_n(\epsilon)\subset A_n\) with lengths \(3^{-n}\). Their intersection consists of exactly one point \(x_\epsilon\in C\). If \(\epsilon\ne\epsilon'\), at the first differing index the corresponding stage intervals are disjoint, so \(x_\epsilon\ne x_{\epsilon'}\). Hence \(\{0,1\}^{\omega}\) injects into \(C\). Since \(\{0,1\}^{\omega}\) is uncountable, \(C\) is uncountable.
:::
