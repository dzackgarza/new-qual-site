---
schema: qual/card@1
id: D-FAIJX
kind: definition
title: Mayer--Vietoris sequence
prompts:
- Write the Mayer-Vietoris long exact sequence for $X = A \cup B$.
classification:
  areas:
  - topology
  topics:
  - Mayer-Vietoris
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $A, B\subseteq X$ subspaces with $X = A^\circ\cup B^\circ$.
Let $i\colon A\cap B\hookrightarrow A$, $j\colon A\cap B\hookrightarrow B$, $k\colon A\hookrightarrow X$, and $l\colon B\hookrightarrow X$ be the inclusions, and let $H_n$ denote [[D-6BUWA|singular homology]] with integer coefficients.
Define
$$
\Phi\colon H_n(A\cap B)\to H_n(A)\oplus H_n(B),\quad \Phi(x) = (i_*x, -j_*x),
\qquad
\Psi\colon H_n(A)\oplus H_n(B)\to H_n(X),\quad \Psi(a, b) = k_*a + l_*b,
$$
and $\del\colon H_n(X)\to H_{n-1}(A\cap B)$ as follows: every $\alpha\in H_n(X)$ is represented by a cycle $z = x + y$ with $x$ an $n$-chain in $A$ and $y$ an $n$-chain in $B$, and $\del\alpha\coloneqq[\del x]$.
The \dfn{Mayer--Vietoris sequence} of $(A, B)$ is
$$
\cdots\to H_n(A\cap B)\xrightarrow{\Phi} H_n(A)\oplus H_n(B)\xrightarrow{\Psi} H_n(X)\xrightarrow{\del} H_{n-1}(A\cap B)\to\cdots\to H_0(X)\to 0.
$$
:::

::: {.theorem}
In the situation of the definition, $\del$ is well defined and the Mayer--Vietoris sequence is exact [@Hat02].
:::

::: {.remark}
Let $C_n(A+B)\subseteq C_n(X)$ be the subgroup of sums of an $n$-chain in $A$ and an $n$-chain in $B$.
Since $X = A^\circ\cup B^\circ$, the inclusion $C_\bullet(A+B)\hookrightarrow C_\bullet(X)$ induces isomorphisms on homology.
The Mayer--Vietoris sequence is the long exact homology sequence of the short exact sequence of chain complexes
$$
0\to C_n(A\cap B)\xrightarrow{x\mapsto(x, -x)} C_n(A)\oplus C_n(B)\xrightarrow{(x, y)\mapsto x+y} C_n(A+B)\to 0,
$$
and $\del$ is its connecting homomorphism; since $\del z = 0$, the chain $\del x = -\del y$ lies in $A\cap B$ and is a cycle there.
:::

::: {.remark}
When $A\cap B\neq\emptyset$ there is an exact sequence of the same form in reduced homology, and there is an exact sequence for singular cohomology with the arrows reversed.
:::
