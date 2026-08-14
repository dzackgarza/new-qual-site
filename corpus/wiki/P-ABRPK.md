---
schema: qual/card@1
id: P-ABRPK
kind: problem
title: "Suppose $f:\\DD\\to\\DD$ is analytic and admits a continuous extension $\\tilde f: \\bar \\DD \\to \\bar \\DD$ such\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - blaschke-factors
  - schwarz-reflection
  - maximum-modulus-principle
  - zeros
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $f:\DD\to\DD$ is analytic and admits a continuous extension $\tilde f: \bar \DD \to \bar \DD$ such that $\abs{z} = 1 \implies \abs{f(z)} = 1$.

a.
Prove that $f$ is a rational function.

b.
Suppose that $z=0$ is the unique zero of $f$.
Show that
\[  
\exists n\in \NN, \lambda \in S^1 \qtext{ such that }f(z) = \lambda z^n
.\]

c.
Suppose that $a_1, \cdots, a_n \in \DD$ are the zeros of $f$ and prove that
\[  
\exists \lambda \in S^1 \qtext{such that} f(z) = \lambda \prod_{j=1}^n {z - a_j \over 1 - \bar{a_j} z}
.\]

:::

:::{.solution}
**Part 1**:
use the reflection principle to define
\[
F(z) \da 
\begin{cases}
f(z) & \abs{z} \leq 1 
\\
{1\over \bar{f\qty{1/\bar{z}}} } & \abs{z} \geq 1
\end{cases}
.\]

Now $F:\CP^1\to \CP^1$ is holomorphic and all such functions are rational.
As a consequence, $f$ is rational.

**Part 2**:
As in the proof of Schwarz, define $g(z) \da {f(z)\over z^n}$ where $n = \ord_{f}(0)$.
Then $g$ is holomorphic on $\DD$ since the singularity at $z=0$ is removable.
On $\abs{z} = r<1$,
\[
\abs{g(z)} = { \abs{f(z)} \over \abs{z} } = {\abs{f(z)} \over r} \leq {1\over r} \convergesto{r\to 1^-} 1
,\]
using that $\abs{f} \leq 1$ on $\DD$.
By the MMP, $\abs{g} \leq 1$ on all of $\DD$.
Note that $\abs{g} = 1$ when $\abs{z}=1$, so $\abs{1/g}\leq 1$ in $\DD$ by the MMP, forcing $\abs{g} = 1$.
Unwinding this, $\abs{f} = \abs{z}^n$, go $f(z) = \lambda z^n$ for some $\abs{\lambda} = 1$.

**Part 3**:
Define $\Psi(z) \da \prod_{k\leq n} \psi_{a_k}(z)$ where $\psi_a(z) \da {a-z\over 1-\bar a z}$.
Set $g(z) \da {f(z) \over \Psi(z)}$, then by the same argument as above, $\abs{g} \leq 1$ and $\abs{g} = 1$ on $\abs{z} = 1$.
Then $g$ has no zeros, since they've all been divided out, and no poles since $f$ is holomorphic on $\DD$, so $1/g$ is holomorphic on $\DD$.
Since $\abs{1/g} = 1$ on $S^1$, this forces $g$ to be constant.
Equality in the Schwarz lemma implies $g(z) = \lambda z$ is a rotation, and unwinding this yields $f(z) = \lambda \Psi(z)$.
:::
