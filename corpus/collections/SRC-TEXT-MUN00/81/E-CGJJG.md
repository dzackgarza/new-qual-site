---
schema: qual/card@1
id: E-CGJJG
kind: problem
title: Order-two group actions on the torus
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
---

::: {.exercise}

(a) Find a group $G$ of homeomorphisms of the torus $T$ having order 2 such that $T/G$ is homeomorphic to the torus.

(b) Find a group $G$ of homeomorphisms of $T$ having order 2 such that $T/G$ is homeomorphic to the Klein bottle.
:::

::: {.solution}
Write the torus as \(T=\mathbb R^2/\mathbb Z^2\), with coordinates \([x,y]\).

(a) Let
\[
\tau[x,y]=[x+1/2,y].
\]
Then \(\tau^2=1\) and \(\tau\) has no fixed points. The quotient identifies the first coordinate modulo \(1/2\), so
\[
T/\langle\tau\rangle\cong (\mathbb R/(\tfrac12\mathbb Z))\times(\mathbb R/\mathbb Z)\cong T.
\]
Thus \(G=\{1,\tau\}\) has order \(2\) and torus quotient.

(b) Let
\[
\sigma[x,y]=[x+1/2,-y].
\]
Again \(\sigma^2=1\), and it is fixed-point-free because a fixed point would require \(x+1/2\equiv x\pmod1\). A fundamental domain is the strip \(0\le x\le1/2\). Its vertical sides are identified by
\[
(0,y)\sim(1/2,-y),
\]
while \(y\) is periodic modulo \(1\). This is precisely the standard square model of the Klein bottle. Hence
\[
T/\langle\sigma\rangle\cong K.
\]
:::
