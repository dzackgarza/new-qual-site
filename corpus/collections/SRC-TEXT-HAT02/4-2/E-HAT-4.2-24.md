---
schema: qual/card@1
id: E-HAT-4.2-24
kind: problem
title: "Moore spaces $M(G,1)$ and $H_2(K(G,1))$"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show there is a Moore space $M(G, 1)$ with $\pi_1\bigl(M(G, 1)\bigr) \approx G$ iff $H_2(K(G, 1); \ZZ) = 0$.
In particular, there is no $M(\ZZ^n, 1)$ with fundamental group $\ZZ^n$, free abelian of rank $n$, if $n \geq 2$.
:::

::: {.solution}
Here $G$ is abelian, as in the definition of a Moore space: $H_1(M(G,1))\cong G$ and $\widetilde H_i(M(G,1))=0$ for $i\ne1$.

Suppose first that such a space $M$ has $\pi_1(M)\cong G$. Attach cells of dimensions at least $3$ to kill its higher homotopy groups, obtaining a $K(G,1)$. Exercise 23, applied to $M$, identifies
$$
H_2(K(G,1))\cong H_2(M)/h(\pi_2(M))=0.
$$

Conversely, let $K$ be a CW model for $K(G,1)$ with $H_2(K)=0$, and put $A=K^2$. The inclusion induces an isomorphism $\pi_1(A)\cong G$, and $H_2(A)$ is a subgroup of the free cellular group $C_2(A)$, hence is free abelian. By Exercise 23,
$$
H_2(A)/h(\pi_2(A))\cong H_2(K(G,1))=0.
$$
Choose a basis of $H_2(A)$ and represent each basis element by a map $S^2\to A$. Attach one $3$-cell along each map, and call the result $M$. In its cellular chain complex the new differential $C_3(M)\to C_2(A)$ maps the chosen free basis bijectively onto $H_2(A)=\ker(d_2)$. It is therefore injective, so $H_3(M)=0$, and its image makes $H_2(M)=0$. There are no cells above dimension $3$. Attaching the $3$-cells preserves $\pi_1$ and $H_1$, giving
$$
\pi_1(M)\cong G,\qquad H_1(M)\cong G,\qquad\widetilde H_i(M)=0\quad(i\ne1).
$$
Thus $M$ is the required Moore space.

Finally, $T^n$ is a $K(\ZZ^n,1)$ and
$$
H_2(T^n;\ZZ)\cong\bigwedge^2\ZZ^n\ne0\qquad(n\ge2).
$$
Hence no Moore space $M(\ZZ^n,1)$ has fundamental group $\ZZ^n$ in this range.
:::
