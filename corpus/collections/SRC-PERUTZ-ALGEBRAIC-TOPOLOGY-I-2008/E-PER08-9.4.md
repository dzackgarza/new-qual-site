---
schema: qual/card@1
id: E-PER08-9.4
kind: problem
title: Perutz Algebraic Topology I Exercise 9.4
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
If $a:A_\ast\to B_\ast$ is a chain map, its mapping cone, denoted $\operatorname{cone}(a)_\ast$, is the complex
\[
\operatorname{cone}(a)_n=A_{n-1}\oplus B_n
\]
with differential
\[
d_{\operatorname{cone}(a)}(x,y)=-d_Ax+a(x)+d_By
\]
(check that this squares to zero).
The point of this construction is to convert questions about chain maps to questions about chain complexes.

(i) Show that the induced map on homology, $a_\ast=H(a):H_\ast(A)\to H_\ast(B)$, is an isomorphism iff $H(\operatorname{cone}(a)_\ast)=0$.

(ii) Construct a short exact sequence
\[
0\longrightarrow B_\ast\longrightarrow \operatorname{cone}(a)_\ast\longrightarrow A_{\ast-1}\longrightarrow 0,
\]
and identify the connecting map in the resulting long exact sequence.

(iii) Show that to give a map of complexes $f=(h,b):\operatorname{cone}(a)_\ast\to C_\ast$ is to give a chain map $b:B_\ast\to C_\ast$ and a chain-homotopy $h$ from $b\circ a$ to the zero map.

(iv) Show that if the map $f$ from (iii) induces an isomorphism on homology then there is a long exact sequence
\[
\cdots\longrightarrow H_n(A)\xrightarrow{a_\ast}H_n(B)\xrightarrow{b_\ast}H_n(C)\longrightarrow H_{n-1}(A)\xrightarrow{a_\ast}H_{n-1}(B)\xrightarrow{b_\ast}H_{n-1}(C)\longrightarrow\cdots.
\]
:::
