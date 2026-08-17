---
schema: qual/card@1
id: P-ALZSD
kind: problem
title: Continuity from above for a finite Borel measure, and $\varepsilon$-$\delta$ absolute continuity
classification:
  areas:
  - real-analysis
  topics:
  - continuity-of-measure
  - measure-theory
  - absolute-continuity
relations: []
review: draft
solved: true
---
Let $\mathcal B$ denote the set of all Borel subsets of $\RR$ and $\mu : \mathcal B \to [0, \infty)$ denote a finite Borel measure on $\RR$.
  
a. 
Prove that if $\{F_k\}$ is a sequence of Borel sets for which $F_k \supseteq  F_{k+1}$ for all $k$, then
\[
\lim _{k \rightarrow \infty} \mu\left(F_{k}\right)=\mu\left(\bigcap_{k=1}^{\infty} F_{k}\right)
\]

b. 
Suppose $\mu$ has the property that $\mu (E) = 0$ for every $E \in \mathcal B$ with Lebesgue measure $m(E) = 0$.
Prove that for every $\epsilon  > 0$ there exists $\delta > 0$ so that if $E \in \mathcal B$ with $m(E) < δ$, then $\mu(E) < ε$.

:::{.concept}
\envlist
- Proof of continuity of measure.
- Using limsup/liminf sets (intersections of unions and vice-versa) and (sub)additivity to bound measures.
  - Control over lower bound: use tails of convergent sums
  - Control over upper bound: use rapidly converging coefficients like $\sum 1/2^n$
- Convergent sums have vanishing tails.
- Intersecting over *more* sets can only lose measure, taking a union over *more* can only gain measure.
- Similarly intersecting over *fewer* sets can only *gain* measure, and taking a union over *fewer* sets can only *lose* measure.
:::


:::{.strategy}
Use a limsup or liminf of sets and continuity of measure.
Note that choosing a limsup vs a liminf is fiddly -- for one choice, you can only get one of the bounds you need, for the other choice you can get both.
:::


:::{.solution}
\envlist

:::{.proof title="of a"}
- Observation: $\mu$ finite means $\mu(E) < \infty$ for all $E \in\mathcal{B}$, which we'll need in several places.
- Prove a more general statement: for any measure $\mu$,
\[
\mu(F_1) < \infty,\, F_k \decreasesto F \implies \lim_{k\to\infty}\mu(F_k) = \mu(F)
,\]
  where $F_k \searrow F$ means $F_1 \supseteq F_2 \supseteq \cdots$ with $\Intersect_{k=1}^\infty F_k = F$.
  - Note that $\mu(F)$ makes sense: each $F_k \in \mathcal{B}$, which is a $\sigma\dash$algebra and closed under countable intersections.

- Take disjoint annuli by setting $E_k \da F_k \sm F_{k+1}$
- Funny step: write
\[
F_1 = F \disjoint \Disjoint_{k=1}^{\infty} E_k
.\]

  - This is because $x\in F_1$ iff $x$ is in every $F_k$, so in $F$, **or**
  - $x\not \in F_1$ but $x\in F_2$, noting incidentally $x\in F_3, F_4,\cdots$, **or**,
  - $x\not\in F_2$ but $x\in F_3$, and so on.

- Now take measures, and note that we get a telescoping sum:
\[
\mu(F_1) 
&= \mu(F) + \sum_{k=1}^\infty \mu(E_k) \\
&= \mu(F) + \lim_{N\to\infty} \sum_{k=1}^N \mu(E_k) \\
&\da \mu(F) + \lim_{N\to\infty} \sum_{k=1}^N \mu(F_k \sm F_{k+1} ) \\
&\da \mu(F) + \lim_{N\to\infty} \sum_{k=1}^N \mu(F_k) - \mu(F_{k+1} ) \hspace{5em}\text{to be justified}\\
&= \mu(F) + \lim_{N\to\infty} 
[
(\mu(F_1) - \mu(F_2)) +  
(\mu(F_2) - \mu(F_3)) +  
\cdots \\ 
& \hspace{8em} + (\mu(F_{N-1}) - \mu(F_N)) +  
(\mu(F_N) - \mu(F_{N+1})) 
] \\ \\
&= \mu(F) + \lim_{N\to\infty} \mu(F_1) - \mu(F_{N+1}) \\
&= \mu(F) + \mu(F_1) - \lim_{N\to\infty} \mu(F_{N+1})
.\]

- Justifying the measure subtraction: the general statement is that for any pair of sets $A\subseteq X$, $\mu(X\sm A) = \mu(X) - \mu(A)$ when $\mu(A) < \infty$:
  \[
  X &= A \disjoint (X\sm A) \\
  \implies \mu(X) &= \mu(A) + \mu(X\sm A) && \text{countable additivity} \\
  \implies \mu(X) -\mu(A) &= \mu(X\sm A) && \text{if } \mu(A) < \infty 
  .\]


- Now use that $\mu(F_1)<\infty$ to justify subtracting it from both sides:
\[
\mu(F_1)
&= \mu(F) + \mu(F_1) - \lim_{N\to\infty} \mu(F_{N+1}) \\
\implies
0
&= \mu(F_1) - \lim_{N\to\infty} \mu(F_{N+1}) \\
\lim_{N\to\infty} \mu(F_{N+1})
&= \mu(F_1) 
.\]

- Now use that $\lim_{N\to\infty}\mu(F_{N+1}) = \lim_{N\to\infty} \mu(F_N)$ to conclude.
:::

:::{.proof title="of b"}
\envlist

- Toward a contradiction, negate the implication: there exists an $\eps>0$ such that for all $\delta$, there exists an $E\in \mathcal{B}$ 
\[
m(E) < \delta && \text{but} \hspace{4em} \mu(E) > \eps 
.\]

  - **Goal**: produce a set $A$ with $m(A)= 0$ **but** $\mu(A)\neq 0$.
- Take a sequence $\delta_n = \alpha(n)$, some function to be determined later, produce sets $E_n$ with
\[
m(E_n) < \delta_n && \text{but} \hspace{4em} \mu(E_n) > \eps \quad \forall n
.\]
- Set 
\[
A_M \da \Intersect_{N=1}^M \Union_{n=N}^\infty E_n \da \Intersect_{N=1}^M F_N
\hspace{4em} 
F_N \da \Union_{n=N}^\infty E_n
.\]
  - Observation: $F_N \supseteq F_{N+1}$ for all $N$, since the right-hand side involves taking a union over *fewer* sets.
  - Notation: define
\[
A_\infty \da \Intersect_{N=1}^\infty \Union_{n=N}^\infty E_n
.\]

- Bounding the Lebesgue measure $m$ from above:
\[
m(A_\infty)
&\da
m\qty{ 
\Intersect_{N=1}^\infty \Union_{n=N}^\infty E_n
} \\
&\leq
m\qty{ 
\Union_{n=N}^\infty E_n
} && \forall N \\
&\leq \sum_{n=N}^\infty m(E_n) && \forall N \quad \text{by countable subadditivity} \\
&\leq \sum_{n=N}^\infty \alpha(n) \\ \\
&\converges{N\to\infty}\too 0
,\]
  where we've used that intersecting over *fewer* sets (i.e. none) can only increase measure in the first bound.
  - We have control over the sequence $\alpha(n)$, so we can choose it to be summable so that the tails converge to zero as rapidly as we'd like.
  - So e.g. for any $\eps_1 >0$, we can choose $\alpha(n) \da \eps_1/2^n$, then
  \[
  \sum_{n=N}^\infty \alpha(n) &\leq \sum_{n=1}^\infty {\eps_1 \over 2^n} = \eps_1 \to 0
  .\]

- Bounding the $\mu$ measure from below:
\[
\mu(A_\infty) 
&\da
\mu\qty{\Intersect_{N=1}^\infty F_N} \\
&= \lim_{N\to\infty} \mu(F_N) && \text{by part (1) }\\
&= \lim_{N\to\infty} \mu\qty{ \Union_{n=N}^\infty E_n } \\
&\geq \lim_{N\to\infty} \mu(E_N ) \\
&\geq \lim_{N\to\infty} \eps \\
&= \eps \\
&>0
,\]
where we've used that taking a union over *fewer* sets can only make the measure smaller.

:::

:::


