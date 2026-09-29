---
schema: qual/card@1
id: P-AGH47LOCRINGISO
kind: problem
title: Isomorphic local rings at points give isomorphic open neighborhoods
classification:
  areas:
  - algebraic-geometry
  topics:
  - Local Rings
  - Birational Geometry
  - Varieties
relations:
- kind: uses
  target: P-AGH33LOCALRINGS
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with Hartshorne I.4.7. Independent published solutions use the same local-to-open principle: after choosing affine neighborhoods, the local-ring isomorphism is represented by morphisms in both directions and becomes an isomorphism after shrinking.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the construction from finitely many coordinate generators and the final simultaneous shrinking against two independent solution sources. The proof explicitly verifies that the resulting neighborhood isomorphism carries P to Q.'
---

::: {.problem}
Let $X$ and $Y$ be two varieties.
Suppose there are points $P \in X$ and $Q \in Y$ such that the local rings $\mco_{P, X}$ and $\mco_{Q, Y}$ are isomorphic as $k$-algebras.
Show that there are open sets $P \in U \subseteq X$ and $Q \in V \subseteq Y$ and an isomorphism of $U$ with $V$ carrying $P$ to $Q$.
:::

::: {.solution}
Fix a $k$-algebra isomorphism
$$
\alpha:\mco_{P,X}\xrightarrow{\sim}\mco_{Q,Y}
$$
and write $\beta=\alpha^{-1}$.

::: pf

::: {.pf-step #s1}

After replacing $X$ and $Y$ by affine open neighborhoods of $P$ and $Q$, the map $\alpha$ is induced by a morphism
$$
f:V_0\to X
$$
from an open neighborhood $V_0\subseteq Y$ of $Q$.

::: pf-proof

Choose affine embeddings
$$
X\subseteq\AA^r,
\qquad
Y\subseteq\AA^s,
$$
and let $x_1,\ldots,x_r$ be the coordinate functions on $X$.
For each $i$, the germ
$$
\alpha(x_i)\in\mco_{Q,Y}
$$
has a regular representative $g_i$ on some open neighborhood $V_i$ of $Q$.
On the common neighborhood
$$
V'=V_1\cap\cdots\cap V_r
$$
the tuple
$$
(g_1,\ldots,g_r):V'\to\AA^r
$$
is a morphism.

Let $F_1,\ldots,F_m$ generate the ideal $I(X)$.
For each $j$, the germ of
$$
F_j(g_1,\ldots,g_r)
$$
at $Q$ equals
$$
\alpha(F_j(x_1,\ldots,x_r))=0.
$$
Hence, after shrinking $V'$ around $Q$, all these finitely many functions vanish identically.
The tuple therefore lands in $X$ and defines a morphism
$$
f:V_0\to X.
$$
For every global coordinate function $x_i$ on $X$, the germ at $Q$ of $x_i\circ f$ is $\alpha(x_i)$ by construction.

:::

:::

::: {.pf-step #s2}

The morphism $f$ sends $Q$ to $P$.

::: pf-proof

An isomorphism of local rings sends the unique maximal ideal to the unique maximal ideal, so
$$
\alpha(\mathfrak m_{P,X})=\mathfrak m_{Q,Y}.
$$
For every coordinate function $x_i$,
$$
x_i-x_i(P)\in\mathfrak m_{P,X}.
$$
Therefore the germ
$$
g_i-x_i(P)=\alpha(x_i-x_i(P))
$$
lies in $\mathfrak m_{Q,Y}$ and vanishes at $Q$.
Thus
$$
g_i(Q)=x_i(P)
$$
for all $i$, which means $f(Q)=P$.

Now the induced local homomorphism
$$
f_Q^*: \mco_{P,X}\longrightarrow\mco_{Q,Y}
$$
is defined.
It agrees with $\alpha$ on the image of $A(X)$.
Every element of $\mco_{P,X}=A(X)_{\mathfrak m_P}$ is a fraction $a/s$ with $s\notin\mathfrak m_P$, and both maps send it to the quotient of their values on $a$ and $s$.
Hence
$$
f_Q^*=\alpha.
$$

:::

:::

::: {.pf-step #s3}

Applying the same construction to $\beta$ gives an open neighborhood $U_0\subseteq X$ of $P$ and a morphism
$$
g:U_0\to Y
$$
with
$$
g(P)=Q,
\qquad
g_P^*=\beta.
$$

::: pf-proof

Repeat steps [](#s1){.pf-ref} and [](#s2){.pf-ref} with $X,P,\alpha$ and $Y,Q,\beta$ interchanged.

:::

:::

::: {.pf-step #s4}

After shrinking around $P$ and $Q$, the compositions $f\circ g$ and $g\circ f$ are identity morphisms.

::: pf-proof

The composition $f\circ g$ is defined on the open neighborhood
$$
U_c=U_0\cap g^{-1}(V_0)
$$
of $P$, and $g\circ f$ is defined on the open neighborhood
$$
V_c=V_0\cap f^{-1}(U_0)
$$
of $Q$.

On the local ring at $P$,
$$
(f\circ g)_P^*
=g_P^*\circ f_Q^*
=\beta\circ\alpha
=\operatorname{id}_{\mco_{P,X}}.
$$
Choose affine coordinate generators $x_1,\ldots,x_r$ for $X$.
For each $i$, the two regular functions
$$
x_i\circ f\circ g
\qquad\text{and}\qquad
x_i
$$
have the same germ at $P$.
After intersecting finitely many neighborhoods, they agree on one open neighborhood $U_1\subseteq U_c$ of $P$.
Since the coordinate functions determine a map into the affine variety $X$, this gives
$$
f\circ g=\operatorname{id}_{U_1}.
$$

The same argument at $Q$, using
$$
(g\circ f)_Q^*
=f_Q^*\circ g_P^*
=\alpha\circ\beta
=\operatorname{id}_{\mco_{Q,Y}},
$$
gives an open neighborhood $V_1\subseteq V_c$ of $Q$ on which
$$
g\circ f=\operatorname{id}_{V_1}.
$$

:::

:::

::: {.pf-step #s5}

There are open neighborhoods $P\in U\subseteq X$ and $Q\in V\subseteq Y$ such that
$$
g:U\xrightarrow{\sim}V
$$
is an isomorphism carrying $P$ to $Q$.

::: pf-proof

Set
$$
U=U_1\cap g^{-1}(V_1)
$$
and
$$
V=V_1\cap f^{-1}(U).
$$
Both are open neighborhoods of $P$ and $Q$, respectively.

If $x\in U$, then $g(x)\in V_1$ and
$$
f(g(x))=x\in U,
$$
so $g(x)\in V$.
Thus $g(U)\subseteq V$.

Conversely, if $y\in V$, then $f(y)\in U$ and, because $y\in V_1$,
$$
g(f(y))=y.
$$
Hence $y\in g(U)$.
Therefore $g(U)=V$.

On $U$ and $V$, the identities from step [](#s4){.pf-ref} show
$$
f\circ g=\operatorname{id}_U,
\qquad
g\circ f=\operatorname{id}_V.
$$
So $g:U\to V$ is an isomorphism with inverse $f|_V$.
Step [](#s3){.pf-ref} gives $g(P)=Q$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is precisely the required neighborhood isomorphism.

:::

:::

:::
