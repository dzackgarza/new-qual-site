---
schema: qual/card@1
id: E-OI7VN
kind: problem
title: The logarithmic spiral and the knotted x-axis as retracts
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
---

::: {.exercise}

(a) Show that the logarithmic spiral

$$
C = \theset{0 \times 0} \cup \theset{e^t \cos t \times e^t \sin t \mid t \in \RR}
$$

is a retract of $\RR^2$.
Can you define a specific retraction $r: \RR^2 \to C$?

(b) Show that the "knotted x-axis" $K$ pictured in Figure 35.2 of the text is a retract of $\RR^3$.
:::

::: {.solution}
(a) For $z=(x,y)\ne0$, let
$$
\rho=\sqrt{x^2+y^2}.
$$
Define
$$
r(x,y)=\rho\bigl(\cos(\log\rho),\sin(\log\rho)\bigr),
$$
and set $r(0,0)=(0,0)$. The image lies in the logarithmic spiral $C$: if $t=\log\rho$, then $ho=e^t$. The map is continuous away from the origin, and at the origin
$$
\|r(x,y)\|=\rho\to0,
$$
so it is continuous there as well. If $(x,y)=e^t(\cos t,\sin t)\in C\setminus\{0\}$, then $ho=e^t$ and $\log\rho=t$, hence $r(x,y)=(x,y)$. Thus $r$ is a retraction of $\RR^2$ onto $C$.

(b) The knotted $x$-axis $K$ in Figure 35.2 is a closed subspace of $\RR^3$ homeomorphic to $\RR$. Let
$$
h:K\to\RR
$$
be a homeomorphism. Since $\RR^3$ is normal and $K$ is closed, the Tietze theorem extends $h$ to a continuous function
$$
H:\RR^3\to\RR.
$$
Then
$$
r=h^{-1}\circ H:\RR^3\to K
$$
is continuous and, for $k\in K$, satisfies $r(k)=h^{-1}(h(k))=k$. Hence $K$ is a retract of $\RR^3$.
:::
