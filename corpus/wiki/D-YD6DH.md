---
schema: qual/card@1
id: D-YD6DH
kind: definition
title: "The Fundamental Group"
classification:
  areas:
  - topology
  topics:
  - fundamental-group
  - homotopy
relations: []
review: draft
---
:::{.definition title="The Fundamental Group"}
Given a pointed space $(X,x_{0})$, we define the fundamental group $\pi_{1}(X)$ as follows:

- Take the set 
\[
L \da \theset{\alpha: S^1\into X \mid \alpha(0) = \alpha(1) = x_{0}}
.\]

- Define an equivalence relation $\alpha \sim \beta$ iff  $\alpha \homotopic \beta$ in $X$, so there exists a homotopy 

\[
H: &S^1 \cross I  \to X \\ 
&
\begin{cases}
H(s, 0) = \alpha(s)\\
H(s, 1) = \beta(s) ,
\end{cases}
\]
- Check that this relation is 

  - Symmetric:
    Follows from considering $H(s, 1-t)$.

  - Reflexive:
    Take $H(s, t) = \alpha (s)$ for all $t$.

  - Transitive:
    Follows from reparameterizing.

- Define $L/\sim$, which contains elements like $[\alpha]$ and $[\id_{x_{0}}]$, the equivalence classes of loops after quotienting by this relation.

- Define a product structure: for $[\alpha], [\beta] \in L/\sim$, define $[\alpha][\beta] = [\alpha \cdot \beta]$, where we just need to define a product structure on actual loops. 
  Do this by reparameterizing:
\[
(\alpha \cdot \beta )(s) \da 
\begin{cases}
\alpha (2s) &  s \in [0, 1/2]
\\
\beta (2s-1) & 
s \in [1/2, 1]
.
\end{cases}
\]
- Check that this map is:

  - Continuous: by the pasting lemma and assumed continuity of $f, g$.

  - Well-defined: ?

- Check that this is actually a group

  - Identity element: 
    The constant loop $\id_{x_0}: I\to X$ where $\id_{x_0}(t) = x_0$ for all $t$.

  - Inverses: 
    The reverse loop $\bar \alpha(t) \da \alpha(1-t)$.

  - Closure:
    Follows from the fact that start/end points match after composing loops, and reparameterizing.

  - Associativity:
    Follows from reparameterizing.

:::
