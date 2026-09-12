---
schema: qual/card@1
id: E-XUJ8N
kind: problem
title: Finite presentations of free products and pushouts
classification:
  areas:
  - topology
  topics:
  - Seifert-van Kampen Theorem
relations: []
review: draft
---

::: {.exercise}

(a) Show that if $G_1$ and $G_2$ have finite presentations, so does $G_1 * G_2$.

(b) Show that if $\pi_1(U \cap V, x_0)$ is finitely generated and $\pi_1(U, x_0)$ and $\pi_1(V, x_0)$ have finite presentations, then $\pi_1(X, x_0)$ has a finite presentation.
[Hint: If $N'$ is a normal subgroup of $\pi_1(U, x_0) * \pi_1(V, x_0)$ that contains the elements $i_1(g_i)^{-1} i_2(g_i)$ where $g_i$ runs over a set of generators for $\pi_1(U \cap V, x_0)$, then $N'$ contains $i_1(g)^{-1} i_2(g)$ for arbitrary $g$.]
:::

::: {.solution}
(a) Write finite presentations
\[
G_1=\langle A\mid R\rangle,
\qquad
G_2=\langle B\mid S\rangle,
\]
with \(A,B,R,S\) finite. Replacing generators by disjoint copies if necessary, the free product has presentation
\[
G_1*G_2\cong \langle A\sqcup B\mid R\sqcup S\rangle.
\]
Indeed, the quotient of the free group on \(A\sqcup B\) by the normal closure of \(R\sqcup S\) has the universal property of the free product. Hence \(G_1*G_2\) is finitely presented.

(b) Let
\[
H=\pi_1(U\cap V,x_0),\quad
G_U=\pi_1(U,x_0),\quad
G_V=\pi_1(V,x_0),
\]
and let
\[
i_1:H\to G_U,\qquad i_2:H\to G_V
\]
be induced by inclusion. By van Kampen,
\[
\pi_1(X,x_0)\cong (G_U*G_V)/N,
\]
where \(N\) is the normal closure of all elements
\[
i_1(h)^{-1}i_2(h),\qquad h\in H.
\]

Choose a finite generating set \(h_1,\dots,h_r\) for \(H\), and let \(N'\) be the normal closure in \(G_U*G_V\) of the finitely many elements
\[
i_1(h_j)^{-1}i_2(h_j),\qquad 1\le j\le r.
\]
We show \(N'=N\). In the quotient \((G_U*G_V)/N'\), the two homomorphisms \(i_1,i_2:H\to (G_U*G_V)/N'\) agree on the generating set \(h_1,\dots,h_r\), hence agree on all of \(H\). Therefore
\[
i_1(h)^{-1}i_2(h)\in N'
\]
for every \(h\in H\). Thus \(N\subseteq N'\), while \(N'\subseteq N\) is immediate from the definition. Hence \(N=N'\).

By part (a), \(G_U*G_V\) has a finite presentation because both factors do. Quotienting by the normal closure of the finitely many additional relators
\[
i_1(h_j)^{-1}i_2(h_j)
\]
still gives a finite presentation. Therefore \(\pi_1(X,x_0)\) is finitely presented.
:::
