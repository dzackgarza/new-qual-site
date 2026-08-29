---
schema: qual/card@1
id: E-HAT-4.1-1
kind: exercise
title: "Alternative sum of maps and abelian $\\pi_n$"
classification:
  areas:
  - topology
topics:
  - Higher Homotopy Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

Suppose a sum $f +' g$ of maps $f, g: (I^n, \partial I^n) \to (X, x_0)$ is defined using a coordinate of $I^n$ other than the first coordinate as in the usual sum $f + g$.
Verify the formula $(f + g) +' (h + k) = (f +' h) + (g +' k)$, and deduce that $f +' k \simeq f + k$ so the two sums agree on $\pi_n(X, x_0)$, and also that $g +' h \simeq h + g$ so the addition is abelian.

::: solution
**Theorem.**  
For $n\ge1$, any coordinate choice for the concatenation sum on
$\pi_n(X,x_0)$ is equivalent and gives an abelian group law.

*Proof.*

1. Let $q_1: (I^n,\partial I^n)\to (I^n\vee I^n,\*)$ be the standard pinch map collapsing
   $\{(x_1,\dots,x_n):x_1=1/2\}$ to the wedge point, so $f+g=(f\vee g)\circ q_1$.
2. Let $q_j$ be the analogous pinch map using coordinate $x_j$; then
   $f +' g=(f\vee g)\circ q_j$.
3. The coordinate permutation $\sigma:(I^n,\partial I^n)\to(I^n,\partial I^n)$ that sends
   $x_1\leftrightarrow x_j$ and is identity on the boundary is homotopic rel $\partial I^n$
   to the identity.
   Therefore $q_j\simeq q_1\circ \sigma$ rel boundary.
4. Hence
   \[
   f +' g \simeq (f\vee g)\circ q_1\circ \sigma.
   \]
   Since $\sigma$ is homotopic to $\mathrm{id}$, this gives $f +' g \simeq f+g$.
5. Expanding the definitions gives
   \[
   (f + g) +' (h + k)=((f\vee g)+(h\vee k))\circ q_j \simeq
   (f +' h)+(g +' k).
   \]
6. Taking $h=k$ and swapping coordinates gives $f +' k \simeq f+k$, so the operations are the same in $\pi_n$.
7. Swapping the order of the two summands in $q_j$ gives a homotopy to the sum with reversed order, so $g +' h \simeq h + g$.

Thus the addition is independent of coordinate choice and is abelian. ∎
:::
