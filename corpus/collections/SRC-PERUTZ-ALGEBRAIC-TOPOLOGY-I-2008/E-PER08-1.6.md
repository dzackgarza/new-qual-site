---
schema: qual/card@1
id: E-PER08-1.6
kind: problem
title: Free-loop homotopy and basepoint-independent fundamental groups
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.6 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the boundary-square conjugacy calculation, the converse basepoint-slide homotopy, and the fundamental-groupoid proof of basepoint-independent invariance.
---

::: {.problem}
Let $f_0,f_1:(I,\partial I)\to(X,x)$ be loops.

1. Say that $f_0$ and $f_1$ are homotopic through loops if they are joined by a homotopy $f_t$ with $f_t(0)=f_t(1)$, but not necessarily equal to $x$.
   Show that $f_0$ is homotopic to $f_1$ through loops if and only if $[f_0]$ is conjugate to $[f_1]$ in $\pi_1(X,x)$.

2. Show that a homotopy equivalence between path-connected spaces induces an isomorphism on fundamental groups, regardless of the choices of basepoints.
:::

::: {.solution}
We write $a*b$ for path concatenation in the order ``first $a$, then $b$''.

<1>1. A homotopy through loops implies conjugacy in $\pi_1(X,x)$.
::: {.proof}
Let
\[
H:I\times I\to X,
\qquad
H(t,s)=f_t(s),
\]
be a homotopy through loops from $f_0$ to $f_1$. Since each $f_t$ is a loop, the two vertical boundary values agree:
\[
H(t,0)=H(t,1).
\]
Define the basepoint track
\[
\alpha(t)=H(t,0)=H(t,1).
\]
Because $f_0$ and $f_1$ are both based at $x$, $\alpha$ is itself a loop at $x$.

The image under $H$ of the oriented boundary of the square is null-homotopic. Starting at $(0,0)$, that boundary is sent to
\[
\alpha*f_1*\alpha^{-1}*f_0^{-1}.
\]
Hence in $\pi_1(X,x)$,
\[
[\alpha][f_1][\alpha]^{-1}[f_0]^{-1}=1,
\]
so
\[
[f_1]=[\alpha]^{-1}[f_0][\alpha].
\]
Thus $[f_0]$ and $[f_1]$ are conjugate.
:::

<1>2. Conjugacy implies a homotopy through loops.
::: {.proof}
Suppose
\[
[f_1]=[\alpha]^{-1}[f_0][\alpha]
\]
for some loop $\alpha$ at $x$. Then $f_1$ is based-homotopic to the concatenated loop
\[
\alpha^{-1}*f_0*\alpha.
\]
It therefore suffices to freely homotope $f_0$ to this conjugate.

For $t\in I$, let $\alpha_t$ be the initial segment of $\alpha$ from $x$ to $\alpha(t)$,
\[
\alpha_t(u)=\alpha(tu).
\]
The loops
\[
\alpha_t^{-1}*f_0*\alpha_t
\]
are based at the moving point $\alpha(t)$ and vary continuously with $t$ after the usual linear reparametrization of the three concatenated pieces. At $t=0$ the two whiskers are constant, so the loop is a reparametrization of $f_0$; at $t=1$ it is $\alpha^{-1}*f_0*\alpha$. Reparametrizing a path through orientation-preserving linear changes of parameter gives a homotopy rel endpoints, so this family gives a homotopy through loops from $f_0$ to $\alpha^{-1}*f_0*\alpha$.

Composing with the based homotopy from that loop to $f_1$ gives a homotopy through loops from $f_0$ to $f_1$.
:::

Thus two based loops are freely homotopic exactly when their elements of $\pi_1(X,x)$ are conjugate.

<1>3. A homotopy of maps gives a natural change-of-basepoint isomorphism on fundamental groupoids.
::: {.proof}
Let $F_0,F_1:X\to Y$ be homotopic by
\[
K:I\times X\to Y.
\]
For each $z\in X$, the track
\[
\eta_z(t)=K(t,z)
\]
is a path from $F_0(z)$ to $F_1(z)$.

If $\gamma$ is a path from $z$ to $z'$, apply the same boundary-square argument as in <1>1 to the restriction of $K$ to $I\times\gamma$. It gives, in the fundamental groupoid of $Y$,
\[
[F_1\gamma]=[\eta_z]^{-1}[F_0\gamma][\eta_{z'}],
\]
with the evident interpretation according to the chosen concatenation convention. Equivalently, the family $[\eta_z]$ is a natural isomorphism between the functors on fundamental groupoids induced by $F_0$ and $F_1$.
:::

<1>4. A homotopy equivalence induces an isomorphism on fundamental groups at corresponding basepoints.
::: {.proof}
Let
\[
F:X\to Y
\]
be a homotopy equivalence with homotopy inverse
\[
G:Y\to X.
\]
Choose homotopies
\[
GF\simeq\operatorname{id}_X,
\qquad
FG\simeq\operatorname{id}_Y.
\]
By <1>3, these homotopies give natural isomorphisms
\[
\Pi_1(G)\Pi_1(F)\cong\operatorname{id}_{\Pi_1(X)},
\qquad
\Pi_1(F)\Pi_1(G)\cong\operatorname{id}_{\Pi_1(Y)}.
\]
Hence the induced functor
\[
\Pi_1(F):\Pi_1(X)\to\Pi_1(Y)
\]
is an equivalence of groupoids, with quasi-inverse $\Pi_1(G)$.

An equivalence of groupoids is fully faithful: applying the quasi-inverse and then the two natural isomorphisms gives inverse bijections on every morphism set. In particular, for each $x\in X$ it gives an isomorphism of automorphism groups
\[
\operatorname{Aut}_{\Pi_1(X)}(x)
\cong
\operatorname{Aut}_{\Pi_1(Y)}(F(x)).
\]
These automorphism groups are precisely
\[
\pi_1(X,x)
\quad\text{and}\quad
\pi_1(Y,F(x)).
\]
Therefore
\[
F_*:\pi_1(X,x)\xrightarrow{\cong}\pi_1(Y,F(x)).
\]
:::

<1>5. The isomorphism is independent of the chosen basepoints up to the standard basepoint-change isomorphisms.
::: {.proof}
Let $x_0\in X$ and $y_0\in Y$ be arbitrary. Since $Y$ is path-connected, choose a path $\beta$ from $F(x_0)$ to $y_0$. Conjugating loops by $\beta$ gives the standard basepoint-change isomorphism
\[
\beta_\#:\pi_1(Y,F(x_0))\xrightarrow{\cong}\pi_1(Y,y_0).
\]
By <1>4,
\[
F_*:\pi_1(X,x_0)\xrightarrow{\cong}\pi_1(Y,F(x_0)).
\]
Therefore
\[
\beta_\#\circ F_*:\pi_1(X,x_0)\xrightarrow{\cong}\pi_1(Y,y_0)
\]
is an isomorphism.

If a different basepoint in $X$ is chosen, path-connectedness of $X$ gives the analogous basepoint-change isomorphism there as well. Thus a homotopy equivalence between path-connected spaces gives isomorphic fundamental groups for arbitrary choices of basepoints.
:::
:::
