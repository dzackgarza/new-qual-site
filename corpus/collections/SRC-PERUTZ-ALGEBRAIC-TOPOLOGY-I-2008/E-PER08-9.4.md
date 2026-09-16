---
schema: qual/card@1
id: E-PER08-9.4
kind: problem
title: Mapping cones of chain maps
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
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

::: {.solution}
Write
\[
\operatorname{cone}(a)_n=A_{n-1}\oplus B_n,
\qquad
D(x,y)=(-d_Ax,\,a(x)+d_By).
\]

<1>1. $D^2=0$.
::: {.proof}
Using that $a$ is a chain map,
\[
D^2(x,y)=\bigl(d_A^2x,\,-a(d_Ax)+d_Ba(x)+d_B^2y\bigr)=(0,0).
\]
:::

<1>2. There is a short exact sequence and its connecting map is $a_*$.
::: {.proof}
Define
\[
0\to B_*\xrightarrow{i}\operatorname{cone}(a)_*\xrightarrow{q}A_{*-1}\to0,
\quad i(y)=(0,y),\quad q(x,y)=x,
\]
where the shifted complex $A_{*-1}$ carries differential $-d_A$.
This is degreewise split exact.
If $x\in A_{n-1}$ is a cycle, lift it to $(x,0)$; its cone boundary is $(0,a(x))$.
Hence the connecting map sends $[x]$ to $[a(x)]$, i.e. it is $a_*$.
:::

<1>3. $a_*$ is an isomorphism iff the cone is acyclic.
::: {.proof}
The long exact sequence is
\[
\cdots\to H_n(B)\to H_n(\operatorname{cone}(a))\to H_{n-1}(A)\xrightarrow{a_*}H_{n-1}(B)\to\cdots.
\]
If all cone homology groups vanish, exactness makes every $a_*$ bijective.
Conversely, if every $a_*$ is an isomorphism, exactness forces every cone homology group to vanish.
:::

<1>4. Maps from the cone are chain maps plus null-homotopies.
::: {.proof}
A degree-zero map $f:\operatorname{cone}(a)\to C$ has the form
\[
f(x,y)=h(x)+b(y),
\]
with $b:B_n\to C_n$ and $h:A_{n-1}\to C_n$.
The identity $df=fD$ is equivalent to
\[
d_Cb=bd_B,
\qquad
d_Ch+h\,d_A=ba.
\]
Thus $b$ is a chain map and $h$ is a chain homotopy from $ba$ to zero (up to the conventional direction of the homotopy equation), and conversely these equations make $f$ a chain map.
:::

<1>5. A quasi-isomorphism $f:\operatorname{cone}(a)\to C$ gives the asserted exact sequence.
::: {.proof}
Replace $H_n(\operatorname{cone}(a))$ in the long exact sequence of <1>3 by $H_n(C)$ through the isomorphism $f_*$.
Under $f=(h,b)$, the map $H_n(B)\to H_n(C)$ is $b_*$.
This yields exactly
\[
\cdots\to H_n(A)\xrightarrow{a_*}H_n(B)\xrightarrow{b_*}H_n(C)\to H_{n-1}(A)\to\cdots.
\]
:::
:::
