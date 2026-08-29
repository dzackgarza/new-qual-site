---
schema: qual/card@1
id: P-LFWBF
kind: problem
title: Naturality of the bidual evaluation map
classification:
  areas:
  - algebra
  topics:
  - Dual Spaces
  - Modules
  - Homomorphisms
relations: []
review: draft
---

::: problem
> Note: Let $X\dual \definedas \hom_R(X, R)$ denote the dual.

We have maps

\[
\begin{align*}
\theta_A: A &\to (A\dual)\dual \\
a &\mapsto (\mathrm{ev}_a: f \mapsto f(a) )
\end{align*}
\]

\[
\begin{align*}
\theta_B: B &\to (B\dual)\dual \\
b &\mapsto (\mathrm{ev}_b: g \mapsto g(b) )
\end{align*}
\]

\[
\begin{align*}
f: A &\to B \\
a &\mapsto f(a)
\end{align*}
\]

\[
\begin{align*}
f\dual: B\dual &\to A\dual \\
g &\mapsto g \circ f
\end{align*}
\]

\[
\begin{align*}
f^{\vee\vee}: A^{\vee\vee} &\to B^{\vee\vee} \\
h &\mapsto h \circ f\dual
\end{align*}
\]

We can now check that $f^{\vee\vee} \circ \theta_A = \theta_B \circ f$ as maps from $A$ to $B^{\vee\vee}$.
Letting $a\in A$, and $h\in B^{\vee\vee}$ (so $h: B\dual \to R$), we will show that both maps act on $h$ in the same way.

For notational convenience, write $\phi \actson h \definedas h\circ \phi$.
We then have

\[
\begin{align*}
(f^{\vee\vee} \circ \theta_A)(a) \actson h 
&\definedas f^{\vee\vee}(\theta_A(a)) \actson h \\
&\definedas f^{\vee\vee}(\mathrm{ev}_a)\actson h \\
&=(\mathrm{ev}_a \circ f\dual)\actson h \\
&\definedas h \circ (\mathrm{ev}_a  \circ f) \\
&\definedas h(f(a)) \\
&= \mathrm{ev}_{f(a)}\actson h \\
&\definedas \theta_B(f(a))\actson h \\
&\definedas (\theta_B \circ f)(a)\actson h,
\end{align*}
\]

which shows that these actions agree, and thus the diagram commutes.
:::
