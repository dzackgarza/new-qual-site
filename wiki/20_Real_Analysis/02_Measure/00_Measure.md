---
order: 20
---

# Measure Theory

:::{.fact}
Some useful tricks:

- \[
\mu(A\sm B) = \mu(A) - \mu(B)
\quad \text{if } \mu(B) < \infty
.\]
- When in doubt, write $f = f-f_n + f_n$ and use the triangle inequality.
- Measurable sets are well-approximated by opens:
\[
G\in \mcm \implies \forall \eps, \exists G = G(\eps) \text{ such that }\,\, m(G) \leq m(E) + \eps
.\]

- Borels are $F_\sigma$ or $G_\delta$ up to null sets, i.e. if $E$ is Borel, there are measure zero sets $N$ such that
\[
E = F_\sigma \disjoint N && E \disjoint N = G_\delta
.\]

:::

[[D-QYLPH]]

[[PR-A4J4G]]

[[T-7LQ7X]]

[[PR-KKJ6O]]

:::{.proof title="sketches"}
Idea: break into disjoint annuli!

- From below: break into disjoint annuli $A_{2} = E_{2}\setminus E_{1}$, 

  - Apply countable disjoint additivity to $E = \disjoint A_{i}$.
- From above: funny step, use $E_{1} = (\disjoint E_{j}\setminus E_{j+1}) \disjoint (\intersect E_{j})$.
  - Taking measures yields a telescoping sum, and use countable additivity, then finiteness to subtract.

  ![image_2021-05-28-23-29-31.png](../../../../assets/assets/figures/image_2021-05-28-23-29-31.png)

:::

:::{.proof title="of continuity of measure from below, detailed"}
For any measure $\mu$,
\[
\mu(F_1) < \infty,\, F_k \decreasesto F \implies \lim_{k\to\infty}\mu(F_k) = \mu(F)
,\]
  where $F_k \searrow F$ means $F_1 \supseteq F_2 \supseteq \cdots$ with $\intersect_{k=1}^\infty F_k = F$.
  - Note that $\mu(F)$ makes sense: each $F_k \in \mathcal{B}$, which is a $\sigma\dash$algebra and closed under countable intersections.

- Take disjoint annuli by setting $E_k \da F_k \sm F_{k+1}$
- Funny step: write
\[
F_1 = F \disjoint \Disjoint_{k=1}^{\infty} E_k
.\]

  - This is because $x\in F_1$ iff $x$ is in every $F_k$, so in $F$, **or**
  - $x\not \in F_1$ but $x\in F_2$, noting incidentally $x\in F_3, F_4,\cdots$, **or**,
  - $x\not\in F_2$ but $x\in F_3$ and thus $F_4, F_4,\cdots$, and so on.

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

# Outer Measure

[[PR-LF7SW]]

[[D-UYOGE]]

# Measures on $\RR^d$

[[PR-I4YON]]

[[PR-DXWWU]]

:::{.proof title="of translation/dilation invariance"}
\envlist

- This is obvious for cubes: 
  - For translation, if $Q_i \covers E$ then $Q_i + k \covers E + k$.
    One can then show $m_*(E + k) \leq \sum \abs{Q_i + k} = \sum \abs{Q_i}\leq m_*(E) + \eps$ for all $\eps$, and get the reverse inequality by writing $E = (E+y)-y$.
  - For dilation, use that $m_*(t(A\disjoint B)) = tm_*(A\disjoint B)$, which is useful because we cover with disjoint cubes.
    Then use that $tQ_i \covers tE$ to get $tm_*(E) \leq t\sum \abs{Q_i} = \sum \abs{tQ_i} \leq m_*(tE) + \eps$ and similarly reverse to get equality.

:::

[[T-KZNWM]]

:::{.proof title="Constructing a non-measurable set"}
\envlist

- Use AOC to choose one representative from every coset of $\RR/\QQ$ on $[0, 1)$, which is countable, and assemble them into a set $N$
- Enumerate the rationals in $[0, 1]$ as $q_{j}$, and define $N_{j} = N + q_{j}$. These intersect trivially.
- Define $M \da \disjoint N_{j}$, then $[0, 1) \subseteq  M \subseteq [-1, 2)$, so the measure must be between 1 and 3.
- By translation invariance, $m(N_{j}) = m(N)$, and disjoint additivity forces $m(M) = 0$, a contradiction.

:::

[[PR-NULVE]]

:::{.proof title="That limsups/infs are measurable"}
Measurable sets form a sigma algebra, and these are expressed as countable unions/intersections of measurable sets.

:::

[[T-YMPTF]]

[[T-OTR5M]]

:::{.proof title="of Borel-Cantelli"}
\envlist

- If $E = \limsup_{j} E_{j}$ with $\sum m(E_{j}) < \infty$ then $m(E) = 0$.
- If $E_{j}$ are measurable, then $\limsup_{j} E_{j}$ is measurable.
- If $\sum_{j} m(E_{j}) < \infty$, then $\sum_{j=N}^\infty m(E_{j}) \converges{N\to\infty}\to 0$ as the tail of a convergent sequence.
- $E = \limsup_{j} E_{j} = \intersect_{k=1}^\infty \union_{j=k}^\infty E_{j} \implies E \subseteq \union_{j=k}^\infty$ for all $k$
- $E \subset \union_{j=k}^\infty \implies m(E) \leq \sum_{j=k}^\infty m(E_{j}) \converges{k\to\infty}\to 0$.

:::

[[PR-I44DD]]

[[PR-552IH]]

:::{.proof title="Convolution"}
Take the cone on $f$ to get $F(x, y) = f(x)$, then compose $F$ with the linear transformation $T = [1, -1; 1, 0]$.

:::

[[D-BXAUS]]

[[PR-UHWNM]]

[[PR-Z5VSQ]]

:::{.proof title="Homeomorphisms need not preserve measurability"}
Let $C\subseteq[0,1]$ be the middle-thirds Cantor set, so $C$ is compact with $m(C)=0$, and let $c\colon[0,1]\to[0,1]$ be the Cantor–Lebesgue function (constant on each complementary interval of $C$, $c(0)=0$, $c(1)=1$).
The map $g(x)\da x+c(x)$ is continuous and strictly increasing (each increment of $x$ is at least the increment of $x$), hence a homeomorphism $[0,1]\to[0,2]$.

On each complementary interval of $C$, $c$ is constant, so $g$ translates that interval.
Thus $m(g([0,1]\setminus C)) = m([0,1]\setminus C) = 1$, and therefore $m(g(C)) = 2-1 = 1$.
In particular $g(C)$ has positive measure, so it contains a non-Lebesgue-measurable subset $A$ (Vitali).
Set $B\da g^{-1}(A)$.
Then $B\subseteq C$, so $m_*(B)=0$ and $B$ is Lebesgue measurable, while $g(B)=A$ is not.
The homeomorphism $g$ therefore sends a measurable set to a non-measurable set.

:::

