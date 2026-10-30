---
schema: qual/card@1
id: P-TATE85-PI-09
kind: problem
title: Maximal ideals of $C(E)$ for a compact Hausdorff space $E$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
(9) Let $E$ be a compact Hausdorff topological space. Let $A$ be the ring of all continuous real valued functions on $E$. For each $x \in E$, let $M(x)$ be the maximal ideal of $A$ consisting of the functions $f \in A$ such that $f(x) = 0$ (i.e., $M(x)$ is the kernel of the homomorphism $f \rightsquigarrow f(x)$). Prove that the map $x \rightsquigarrow M(x)$ is a *homeomorphism* of $E$ *onto* the maximal ideal spectrum of $A$. (You may use the well-known lemma which states that, given two disjoint closed subsets of $E$ (in particular two distinct points of $E$), there exists a continuous real valued function on $E$ taking the value $0$ on one of the sets and the value $1$ on the other - if you don’t like too much abstraction, take $E$ to be the closed interval $[0, 1]$ on the real line.) (Hint: the only hard part is to show that every maximal ideal $\mathcal{M}$ of $A$ is of the form $M(x)$ for some $x \in E$. To do this, suppose the contrary. Then for every $x \in E$ there exists a function $f_{x} \in \mathcal{M}$, but with $f_{x}(x) \neq 0$. Show that if you replace $f_{x}$ by $g_{x} f_{x}$ with a suitable $g_{x}$, you can assume $f_{x} \in \mathcal{M}$, and $f_{x}(y) = 1$ for all $y$ in some neighborhood $U_{x}$ of $x$. Now these $U_{x}$ cover $E$, so already a finite number $U_{x_{1}}, U_{x_{2}}, \ldots, U_{x_{n}}$ cover $E$ etc.).
:::

::: {.solution}

Let
$$
A=C(E,\RR),
\qquad
M(x)=\{f\in A:f(x)=0\}.
$$
Give $\operatorname{MaxSpec}(A)$ the Zariski topology.

::: pf

::: {.pf-step #s1-1}

For each $x\in E$, the ideal $M(x)$ is maximal.


::: pf-proof

Evaluation at $x$ is a surjective ring homomorphism
$$
\operatorname{ev}_x:A\to\RR,
\qquad
f\mapsto f(x),
$$
with kernel $M(x)$. Hence
$$
A/M(x)\cong\RR
$$
is a field, so $M(x)$ is maximal.

:::

:::

::: {.pf-step #s1-2}

Every maximal ideal $M\subset A$ has a common zero in $E$.


::: pf-proof

Suppose not. Then for every $x\in E$ there exists
$$
f_x\in M
$$
with $f_x(x)\ne0$. By continuity, there is an open neighborhood $U_x$ of $x$ on which $f_x$ is nowhere zero.

Compactness of $E$ gives finitely many points $x_1,\ldots,x_n$ with
$$
E=U_{x_1}\cup\cdots\cup U_{x_n}.
$$
Set
$$
h=f_{x_1}^2+\cdots+f_{x_n}^2.
$$
Since $M$ is an ideal, $h\in M$. At every point of $E$, at least one summand is strictly positive, so
$$
h(y)>0
\qquad
\text{for all }y\in E.
$$
Therefore $1/h$ is a continuous real-valued function on $E$, so $h$ is a unit of $A$. A proper ideal cannot contain a unit, contradicting the maximality of $M$.

:::

:::

::: {.pf-step #s1-3}

Every maximal ideal of $A$ is $M(x)$ for some $x\in E$.


::: pf-proof

By step [](#s1-2){.pf-ref}, choose $x\in E$ such that
$$
f(x)=0
\qquad
\text{for all }f\in M.
$$
Then
$$
M\subseteq M(x).
$$
Both ideals are maximal by hypothesis and step [](#s1-1){.pf-ref}, so
$$
M=M(x).
$$

:::

:::

::: {.pf-step #s1-4}

The point $x$ in step [](#s1-3){.pf-ref} is unique.


::: pf-proof

If $x\ne y$, the separation lemma supplied in the problem gives a continuous function $f:E\to\RR$ with
$$
f(x)=0,
\qquad
f(y)=1.
$$
Thus
$$
f\in M(x)
\qquad\text{but}\qquad
f\notin M(y),
$$
so $M(x)\ne M(y)$.

:::

:::

::: {.pf-step #s1-5}

The map
$$
\Phi:E\to\operatorname{MaxSpec}(A),
\qquad
x\mapsto M(x),
$$
is a continuous bijection.


::: pf-proof

Bijectivity follows from steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

For any ideal $I\subseteq A$, the Zariski-closed subset
$$
V(I)=\{\mathfrak m\in\operatorname{MaxSpec}(A):I\subseteq\mathfrak m\}
$$
has inverse image
$$
\Phi^{-1}(V(I))
=
\{x\in E:f(x)=0\text{ for every }f\in I\}
=
\bigcap_{f\in I}f^{-1}(0),
$$
which is closed in $E$. Hence $\Phi$ is continuous.

:::

:::

::: {.pf-step #s1-6}

The map $\Phi$ is closed.


::: pf-proof

Let $F\subseteq E$ be closed, and define
$$
I(F)=\{f\in A:f\restrict_F=0\}.
$$
For $x\in F$, every function in $I(F)$ vanishes at $x$, so
$$
\Phi(x)=M(x)\in V(I(F)).
$$
Thus
$$
\Phi(F)\subseteq V(I(F)).
$$

Conversely, let $x\notin F$. Since $F$ and $\{x\}$ are disjoint closed subsets, the separation lemma gives $f\in A$ such that
$$
f\restrict_F=0,
\qquad
f(x)=1.
$$
Then $f\in I(F)$ but $f\notin M(x)$, so
$$
M(x)\notin V(I(F)).
$$
Using the surjectivity of $\Phi$, this proves
$$
\Phi(F)=V(I(F)),
$$
which is closed in $\operatorname{MaxSpec}(A)$.

:::

:::

::: {.pf-step #s1-7}

The map $\Phi$ is a homeomorphism.


::: pf-proof

By step [](#s1-5){.pf-ref}, $\Phi$ is a continuous bijection, and by step [](#s1-6){.pf-ref} it is closed. Therefore its inverse is continuous, so $\Phi$ is a homeomorphism.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves the asserted identification of $E$ with the maximal ideal spectrum of $C(E,\RR)$.

:::

:::

:::
