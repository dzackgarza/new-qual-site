---
schema: qual/card@1
id: P-BSATZ
kind: problem
title: $\bigl|\frac{f(z)-f(0)}{M^2-\overline{f(0)}f(z)}\bigr|\le\frac{|z|}{MR}$ for
  $|f|\le M$ on $D(0,R)$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Show that if $f: D(0, R) \rightarrow \mathbb{C}$ is holomorphic, with $|f(z)| \leq M$ for some $M>0$, then
\[
\left|\frac{f(z)-f(0)}{M^{2}-\overline{f(0)} f(z)}\right| \leq \frac{|z|}{M R} .
\]
:::

:::{.concept}
The strategy:

- Write the RHS as $a$.
  Note that we need to get rid of the $M^2$ on the LHS, so keep the $M$ around and write $a \da z/R$ so $z = aR$.
- Make the substitution to get
\[
\abs{f(aR) - f(0) \over M^2 - \bar{f(0)} f(aR) } \leq M\inv \abs{a} \\
\implies
\abs{M\qty{ f(aR) - f(0)}  \over M^2 - \bar{f(0)} f(aR) } \leq \abs{a} \\
\abs{ f(aR)/M - f(0)/M  \over 1 - \bar{f(0)} f(aR)/M^2 } \leq \abs{a} 
.\]
  - Recognize the LHS as $\psi_w(g(a))$ for $w\da f(0)/M$ and $g(a) \da f(aR)/M$.

:::

:::{.solution}

> Proof due to Swaroop Hegde!

Fix $R, M$ and make a clever choice: define
\[
F: \DD &\to \CC \\
z &\mapsto {f(Rz) \over M}
.\]
Write $a\da F(0)$ and consider the Blaschke factor
\[
\psi_a(z) \da {a-z \over 1-\bar{a} z} \in \Aut(\DD)
,\]
and define
\[
g: \DD &\to \DD \\
z &\mapsto (\psi_a \circ F)(z)
.\]
Then $g(0) = 0$ and $\abs{g(z)} \leq 1$ for all $z\in \DD$, so by Schwarz we have $\abs{g(z)} \leq \abs{z}$ for all $z\in \DD$.
Thus for all $z\in \DD$,
\[
&\abs{g(z)} \leq z \\ \\
\iff & \abs{\psi_a(F(z)) } \leq \abs{z} \\ \\
\iff & \abs{ {f(Rz) \over M} - a \over 1 - {\bar a f(Rz) \over M}  } \leq \abs{z} \\ \\
\iff & \abs{f(Rz) - f(0) \over 1 - {\bar{f(0)} f(Rz) \over M^2 } } \leq \abs{z} \\ \\
\iff & \abs{f(Rz) - f(0) \over M^2 - \bar{f(0)} f(Rz) } \leq {\abs{z} \over M} \\ \\
\iff & \abs{f(w) - f(0) \over M^2 - \bar{f(0)} f(w) } \leq {\abs{w} \over MR}
,\]
which holds for all $w\in \DD$ by replacing $Rz$ with $w$ (i.e. to show this equality for arbitrary $w\in \DD$, write $w = Rz$ for some $z\in \DD$ and run this chain of inequalities backward).




:::
