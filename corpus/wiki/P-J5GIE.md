---
schema: qual/card@1
id: P-J5GIE
kind: problem
title: "Let $R$ be a ring with unity."
classification:
  areas:
  - algebra
  topics:
  - free-modules
  - torsion
  - exact-sequences
relations: []
review: draft
---
Let $R$ be a ring with unity.

a.
Give a definition for a free module over $R$.

b.
Define what it means for an $R\dash$module to be torsion free.

c.
Prove that if $F$ is a free module, then any short exact sequence of $R\dash$modules of the following form splits:
\[
0 \to N \to M \to F \to 0
.\]

d.
Let $R$ be a PID. 
Show that any finitely generated $R\dash$module $M$ can be expressed as a direct sum of a torsion module and a free module.
  
> You may assume that a finitely generated torsionfree module over a PID is free.

:::{.solution}
Let $R$ be a ring with 1.

:::{.proof title="of a"}
An $R\dash$module $M$ is **free** if any of the following conditions hold:

- $M$ admits an $R\dash$linearly independent spanning set $\theset{\vector b_\alpha}$, so $$m\in M \implies m = \sum_\alpha r_\alpha \vector b_\alpha$$ and $$\sum_\alpha r_\alpha \vector b_\alpha = 0_M \implies r_\alpha = 0_R$$ for all $\alpha$.
- $M$ admits a decomposition $M \cong \bigoplus_{\alpha} R$ as a direct sum of $R\dash$submodules.
- There is a nonempty set $X$ an monomorphism $X\injects M$ of sets such that for every $R\dash$module $N$, every set map $X\to N$ lifts to a unique $R\dash$module morphism $M\to N$, so the following diagram commutes:

\begin{tikzcd}
M \ar[rd, dotted, "\exists ! \tilde f"] & \\
X \ar[u, hook] \ar[r, "f"] & N
\end{tikzcd}

Equivalently,
\[
\Hom_\Set(X, \Forget(N)) \mapsvia{\sim} \Hom_{\rmod}(M, N)
.\]


:::

:::{.proof title="of b"}
\envlist

- Define the annihilator:
\[
\Ann(m) \definedas \theset{r\in R \suchthat r\cdot m = 0_M} \normal R
.\]
  - Note that $mR \cong R/\Ann(m)$.
- Define the torsion submodule:
\[
M_t \definedas \theset{m\in M \suchthat \Ann(m) \neq 0} \leq M
\]
- $M$ is **torsionfree** iff $M_t = 0$ is the trivial submodule.

:::

:::{.proof title="of c"}
\envlist

- Let the following be an SES where $F$ is a free $R\dash$module:
\[
0 \to N \to M \mapsvia{\pi} F \to 0
.\]

- Since $F$ is free, there is a generating set $X = \theset{x_\alpha}$ and a map $\iota:X\injects F$ satisfying the 3rd property from (a).
  - If we construct any map $f: X\to M$, the universal property modules will give a lift $\tilde f: F\to M$

- Identify $X$ with $\iota(X) \subseteq F$. 
- For every $x\in X$, the preimage $\pi\inv(x)$ is nonempty by surjectivity.
  So arbitrarily pick any preimage.
- $\theset{\iota(x_\alpha)} \subseteq F$ and $\pi$ is surjective, so choose fibers $\theset{y_\alpha} \subseteq M$ such that $\pi(y_\alpha) = \iota(x_\alpha)$ and define
\[
f: X&\to M \\
x_\alpha &\mapsto y_\alpha
.\]
- The universal property yields $h: F\to M$:

\begin{tikzcd}
& & & X=\theset{x_\alpha} \ar[dd, hook, "\iota"]\ar[ddl, "f"'] &  \\ \\
0 \ar[r]& N \ar[r] & M\ar[r, "\pi"'] & \ar[l, bend right, dotted ,"\exists ! h"'] F \ar[r] & 0
\end{tikzcd}

- It remains to check that it's a section.
  - Write $f= \sum r_i x_i$, then since both maps are $R\dash$module morphism, by $R\dash$linearity we can write
  \[
  (\pi \circ h)(f) 
  &= (\pi \circ h)\qty{ \sum r_i x_i } \\
  &= \sum r_i (\pi \circ h)(x_i)
  ,\]
  but since $h(x_i) \in \pi\inv(x_i)$, we have $(\pi \circ h)(x_i) = x_i$.
  So this recovers $f$.


:::

:::{.proof title="of c, shorter proof"}
\envlist

- Free implies projective

  - Universal property of **projective** objects: for every epimorphism $\pi:M\surjects N$ and every $f:P\to N$ there exists a unique lift $\tilde f: P\to M$:

  \begin{tikzcd}
  & P\ar[d, "f"] \ar[dl, dotted, "\exists ! \tilde f"'] \\
  M \ar[r, "\pi"] & N
  \end{tikzcd}

  - Construct $\phi$ in the following diagram using the same method as above (surjectivity to pick elements in preimage):

\begin{tikzcd}
	&& X \\
	\\
	&& F \\
	\\
	M && N && 0
	\arrow["\iota", hook, from=1-3, to=3-3]
	\arrow["f", from=3-3, to=5-3]
	\arrow["\pi"', two heads, from=5-1, to=5-3]
	\arrow[from=5-3, to=5-5]
	\arrow["{\exists \tilde \phi}"', dashed, from=3-3, to=5-1]
	\arrow["\phi"', curve={height=24pt}, from=1-3, to=5-1]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNSxbMCw0LCJNIl0sWzIsNCwiTiJdLFs0LDQsIjAiXSxbMiwyLCJGIl0sWzIsMCwiWCJdLFs0LDMsIlxcaW90YSIsMCx7InN0eWxlIjp7InRhaWwiOnsibmFtZSI6Imhvb2siLCJzaWRlIjoidG9wIn19fV0sWzMsMSwiZiJdLFswLDEsIlxccGkiLDIseyJzdHlsZSI6eyJoZWFkIjp7Im5hbWUiOiJlcGkifX19XSxbMSwyXSxbMywwLCJcXGV4aXN0cyBcXHRpbGRlIFxccGhpIiwyLHsic3R5bGUiOnsiYm9keSI6eyJuYW1lIjoiZGFzaGVkIn19fV0sWzQsMCwiXFxwaGkiLDIseyJjdXJ2ZSI6NH1dXQ==)



- Now take the identity map, then commutativity is equivalent to being a section.

\begin{tikzcd}
 & & & F\ar[d, "\one_F"]\ar[dl, "\exists ! h"'] & \\
0 \ar[r] & N\ar[r] & M\ar[r] & F \ar[r] & 0
\end{tikzcd}

:::

:::{.proof title="of d"}
\envlist

There is a SES

\begin{tikzcd}
0 \ar[r] & M_t \ar[r] & M \ar[r] & M/M_t \ar[r] & 0
\end{tikzcd}


:::{.claim}
$M/M_t$ is a free \(R\dash\)module, so this sequence splits and
$M\cong M_t \oplus {M\over M_t}$, where $M_t$ is a torsion $R\dash$module.

> Note that by the hint, since $R$ is a PID, it suffices to show that $M/M_t$ is torsionfree.

:::

- Let $m+M_t \in M/M_t$ be arbitrary.
  Suppose this is a torsion element, the claim is that it must be the trivial coset.
  This will follow if $m\in M_t$
- Since this is torsion, there exists $r\in R$ such that
\[
M_t = r(m + M_t) \da (rm) + M_t \implies rm\in M_t
.\]
- Then $rm$ is torsion in $M$, so there exists some $s\in R$ such $s(rm) = 0_M$.
- Then $(sr)m = 0_M$ which forces $m\in M_t$

:::





:::
