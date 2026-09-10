---
schema: qual/card@1
id: E-I9R8B
kind: problem
title: The cone on the infinite earring
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
---

::: {.exercise}

Let $X$ be the infinite earring in $\mathbb{R}^2$.
(See Example 1 of §80.) Let $C(X)$ be the subspace of $\mathbb{R}^3$ that is the union of all line segments joining points of $X \times 0$ to the point $p = (0, 0, 1)$.
It is called the cone on $X$.
Show that $C(X)$ is simply connected, but is not locally simply connected at the origin.
:::

::: {.solution}
The cone can be written as
\[
C(X)=(X\times[0,1])/(X\times\{1\}),
\]
with cone point \(p\). The homotopy
\[
H([x,t],s)=[x,(1-s)t+s]
\]
contracts all of \(C(X)\) to \(p\). Hence \(C(X)\) is contractible, in particular simply connected.

Let \(o=(0,0,0)\), the origin in the base \(X\times\{0\}\). We show \(C(X)\) is not locally simply connected at \(o\). Take the neighborhood
\[
U=C(X)-\{p\}.
\]
Since the cone point is closed, \(U\) is open. Radial projection in the cone coordinate gives a deformation retraction
\[
U\simeq X\times\{0\}=X.
\]

Let \(V\subset U\) be any neighborhood of \(o\). Its intersection with the base contains a neighborhood of \(o\) in the infinite earring. Hence, for all sufficiently large \(n\), it contains the entire small circle \(C_n\) of the earring. Let \(\gamma_n\) traverse \(C_n\) once. Then \(\gamma_n\subset V\).

Under the deformation retraction \(U\to X\), the loop \(\gamma_n\) remains the standard loop on \(C_n\). Retraction of the earring \(X\to C_n\), collapsing all other circles to \(o\), sends it to a generator of
\[
\pi_1(C_n,o)\cong\mathbb Z.
\]
Thus \(\gamma_n\) is not nullhomotopic in \(U\). Therefore no neighborhood \(V\subset U\) of \(o\) has all its loops nullhomotopic in \(U\); in particular there is no basis of simply connected neighborhoods at \(o\). Hence \(C(X)\) is not locally simply connected at the origin.
:::
