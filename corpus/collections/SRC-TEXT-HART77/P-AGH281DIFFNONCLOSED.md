---
schema: qual/card@1
id: P-AGH281DIFFNONCLOSED
kind: problem
title: Differentials at nonclosed points and regularity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves of Differentials
  - Regular Local Rings
  - Separable Extensions
relations: []
review: draft
---

::: {.problem}
Here we strengthen the results of the text to include information about the sheaf of differentials at a not necessarily closed point of a scheme $X$.

a. Generalize (8.7) as follows. Let $B$ be a local ring containing a field $k$, and assume that the residue field $k(B) = B/\mfm$ of $B$ is a separably generated extension of $k$.
Then the exact sequence of (8.4A),
\[
0 \to \mfm/\mfm^2 \mapsvia{\delta} \Omega_{B/k} \tensor k(B) \to \Omega_{k(B)/k} \to 0
\]
is exact on the left also.
*Hint:* in copying the proof of (8.7), first pass to $B/\mfm^2$, which is a complete local ring, and then use (8.25A) to choose a field of representatives for $B/\mfm^2$.

b. Generalize (8.8) as follows. With $B, k$ as above, assume furthermore that $k$ is perfect and that $B$ is a localization of an algebra of finite type over $k$.
Show that $B$ is a regular local ring if and only if $\Omega_{B/k}$ is free of rank $\dim B + \trdeg k(B)/k$.

c. Strengthen (8.15) as follows. Let $X$ be an irreducible scheme of finite type over a perfect field $k$, and let $\dim X = n$.
For any point $x \in X$, not necessarily closed, show that the local ring $\OO_{x, X}$ is a regular local ring if and only if the stalk $(\Omega_{X/k})_x$ is free of rank $n$.

d. Strengthen (8.16) as follows. If $X$ is a variety over an algebraically closed field $k$, then $U = \ts{x \in X \st \OO_x \text{ is a regular local ring}}$ is an open dense subset of $X$.
:::
