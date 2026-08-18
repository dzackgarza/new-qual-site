---
schema: qual/card@1
id: P-TNOTE
kind: problem
title: "Spring 2021, 1"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - measure-theory
  - borel-cantelli
relations: []
review: draft
solved: true
---
:::{.problem title="Spring 2021, 1"}
Let \( (X, \mathcal{M},\mu)  \) be a measure space and let $E_n \in \mathcal{M}$ be a measurable set for $n\geq 1$.
Let $f_n \da \chi_{E_n}$ be the indicator function of the set $E_n$ and show that 

a. $f_n \converges{n\to\infty}\to 1$ uniformly \( \iff \) there exists $N\in \NN$ such that $E_n = X$ for all $n\geq N$.

b. $f_n(x) \converges{n\to\infty}\to 1$ for almost every $x$ \( \iff \) 
\[
\mu \qty{ \Intersect_{n \geq 0} \Union_{k \geq n} (X \sm E_k) } = 0
.\]
:::

:::{.solution}
**Part a**:

$\implies$:

- Suppose $\chi_{E_n}\to 1$ uniformly, we want to produce an $N$ such that $n\geq N \implies x\in E_n$ for all $x\in X$.
- Take $\eps \da 1/2$. 
  By uniform convergence, for $N$ large enough,
  \[
& \forall n\geq N \quad \abs{\chi_{E_n}(x) - 1} < 1/2 && \forall x\in X\\
&\iff
\forall n\geq N \quad \chi_{E_n}(x) = 1 && \forall x\in X \\
&\iff 
\forall n\geq N \quad x\in E_n && \forall x\in X
&\iff 
\forall n\geq N \quad E_n = X
,\]
where we've used that $E_n \subseteq X$ by definition and this shows $X \subseteq E_n$.
So this $N$ suffices.

$\impliedby$:

- Let $\eps > 0$ be arbitrary.
- Choose $N$ such that $n\geq N \implies X = E_n$.
  Then
\[
&\forall n\geq N \quad x\in E_n && \forall x\in X \\
&\forall n\geq N \quad \chi_{E_n}(x) = 1 && \forall x\in X \\
&\forall n\geq N \quad \abs{\chi_{E_n}(x) - 1} = 0 < \eps && \forall x\in X 
,\]
so $\chi_{E_n} \to 1$ uniformly.

**Part b**:

- Define
\[
S &\da \ts{x\in X \st \chi_{E_k}(x) \to 1}\\
&\da \ts{x\in X \st \forall \eps,\, \exists N\, \text{ s.t. } \abs{\chi_{E_k}(x) - 1 } < \eps ,\forall k\geq N}\\
L &\da \Intersect_{n\geq 0} \Union_{k\geq n} \qty{X\sm E_k}
,\]
so $S$ is the set where $f_n\to f$ and $X\sm S$ is the exceptional set where $f_n\not\to f$ doesn't converge pointwise.

- **Claim**: $L = X\sm S$, so if $x\in S \iff x\in X\sm L$.
- Proof of claim:
Suppose there exists an $N$ such that the first line below is true.
Then for a fixed $x$, there are equivalent statements:
\[
&\qquad x \in S \\
&\iff \exists N \text{ s.t. } \forall \eps>0,\quad \abs{\chi_{E_k}(x) - 1 } < \eps && \forall k\geq N \\ 
&\iff 
\exists N \text{ s.t. } 
\abs{\chi_{E_k}(x) - 1 } = 0 && \forall k\geq N \\ 
&\iff 
\exists N \text{ s.t. } 
\chi_{E_k}(x) = 1 && \forall k\geq N \\
&\iff 
\exists N \text{ s.t. } 
x\in E_k && \forall k\geq N \\
&\iff 
\exists N \text{ s.t. } 
x\not\in X\sm E_k &&\forall k\geq N \\
&\iff 
\exists N \text{ s.t. } 
x\not\in \Union_{k\geq N} X\sm E_k  \\
&{\color{blue} \iff} 
x\not\in \Intersect_{n\geq 0}\Union_{k\geq n} X\sm E_k \\
&\iff x\not\in L \\
&\iff x\in X\sm L
.\]

- Proving the iff:
  $f_n\to f$ almost everywhere $\iff \mu(X\sm S) = 0 \iff \mu(L) = 0$.

:::

