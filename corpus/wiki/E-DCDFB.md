---
schema: qual/card@1
id: E-DCDFB
kind: exercise
title: "Fixed point convergence"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Fixed point convergence"}
Suppose $f:\DD\to \DD$ with $f(a) = a$ a fixed point where $\abs{f'(a)} < 1$.
Show that for any initial point $z_0$, the sequence $z_k \da f(z_{k-1})$ converges to $a$.

#complex/exercise/completed

:::

:::{.solution}
First suppose $a=0$ -- then Schwarz applies, and since $\abs{f'(a)} < 1$ is strict, $f$ is *not* a rotation.

:::{.claim}
For any choice of $z_0\in \DD$, there is an $r$ with $0< \abs{z_0} < r < 1$ and a constant $C<1$ such that $\abs{f(z)} \leq C\abs{z}$ for $\abs{z} < r$.
:::

With such an $r$ and $C<1$ in hand,

\[
\abs{z_k} = \abs{f(z_{k-1})} \leq C\abs{z_{k-1}} = C\abs{f(z_{k-2})} \leq C^2 \abs{z_{k-2}} \cdots \implies \abs{z_k} \leq C^k\abs{z_0} \convergesto{k\to\infty}0
,\]
which proves the $a=0$ case.

:::{.proof title="That $f$ is a contraction"}
The claim is that for any given $r$, the constant $C\da M/r$ works, where $M\da \max_{\abs{z} = r} \abs{f(z)}>0$.
The scaled Schwarz lemma gives $\abs{f(z)}\leq {M\over r}\abs{z} = C\abs{z}$, and $\abs{C} \leq 1$ since $\abs{M} \leq r$, which follows because $\abs{f(z)}\leq \abs{z}$ on $\DD$ itself.
:::

For $a\neq 0$, take a Blaschke factor $\psi_a(z)$ and consider $F \da \psi_a\inv \circ f\circ \psi_a$.
The claim is that this reduces to the case $a=0$.

Note $F(0) = 0$, so $0$ is a fixed point of $F$.
Moreover, a clever calculation shows
\[
F'(0) 
&= (\psi_a\inv)'(f(\psi_a(0))) \cdot f'(\psi_a(0)) \cdot \psi_a'(0) \\ \\
&= (\psi_a\inv)'(f( a )) \cdot f'(a ) \cdot \psi_a'(0) \\ \\
&= (\psi_a\inv)'(a) \cdot f'(a ) \cdot \psi_a'(0) \qquad \text{since } f(a) = a \\ \\
&= (\psi_a)'(a) \cdot \psi_a'(0) \cdot f'(a) \qquad \text{since } \psi_a\inv = \psi_a \\ \\
&= (\psi_a)'( \psi_a(0) ) \cdot \psi_a'(0) \cdot f'(a) \\ \\
&= (\psi_a \circ \psi_a)'(0) \cdot f'(a) \\
&= 1 \cdot f'(a)
,\]
so $\abs{F'(0)} = \abs{f'(a)} < 1$.
Now setting $w_k \da \psi_a(z_n)$ and writing $f = \psi_a \circ F \circ \psi_a\inv$, by continuity we have 
\[
f(z_k) = \psi_a(F(w_k)) \convergesto{k\to\infty} \psi_a(0) = a
.\]
:::
