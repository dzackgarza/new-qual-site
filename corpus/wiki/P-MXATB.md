---
schema: qual/card@1
id: P-MXATB
kind: problem
title: "Let $\\tau \\definedas (t_1, t_2)$ denote the transposition and $\\sigma = (s_1, s_2 \\cdots, s_p)$ denote the $p\\dash$cycle, and let $S = \\generators{\\sigma, \\tau}$."
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

Let $\tau \definedas (t_1, t_2)$ denote the transposition and $\sigma = (s_1, s_2 \cdots, s_p)$ denote the $p\dash$cycle, and let $S = \generators{\sigma, \tau}$.
We would like to show that $S = S_p$, and since $S \subseteq S_p$ is clear, we just need to show that $S_p \subseteq S$.

We first note that because $p$ is prime, $\sigma^k$ is a $p\dash$cycle for every $1\leq k \leq p$, and $\generators{\sigma} = \generators{\sigma^k}$ for any such $k$.

Then note that $t_1=s_i$ for some $i$ and $t_2=s_j$ for some $j$, so we can take $k=j-i$ to get a cycle $\sigma^k$ that sends $t_1$ to $t_2$.
So without loss of generality, we can replace $\sigma$ with
$$
\sigma = (t_1, t_2, \cdots )
$$

But now, we can relabel all of the elements of $S_p$ simultaneously (i.e. replace $\generators{\sigma, \tau}$ with another subgroup in the same conjugacy class) in such a way that $t_1$ becomes 1 and $t_2$ becomes 2. We can then assume wlog that
$$
\tau = (1,2),\quad \sigma=(1,2,\cdots,p)
$$

We can then get all adjacent transpositions: noting that
\[
\begin{align*}
\sigma\inv \tau \sigma &= (2, 3) \\
\sigma^{-2} \tau \sigma^2 &= (3, 4) \\
&\cdots \\
\sigma^{-k} \tau \sigma^k &= (k+1 \mod p,~~k+2\mod p) \quad \forall 1\leq k \leq p
,\end{align*}
\]

where we use the fact that for any $\gamma\in S_p$, we have $\gamma\tau\gamma = (\gamma(1),~\gamma(2))$.

But this also gives us all transpositions of the form $(1, j)$ for each $2\leq j \leq p$:
\[
\begin{align*}
(2, 3)\inv(1, 2)(2, 3) &= (1, 3) \\
(3, 4)\inv (1, 3) (3, 4) &= (1, 4) \\
&\cdots \\
(j-1, j)\inv (1, j-1) (j-1, j) &= (1,j) \quad \forall 1\leq j \leq p
.\end{align*}
\]

Thus we have $J \definedas \generators{\{(1, j) \mid 2\leq j \leq p\}} \subseteq S$.

But now if $\gamma = (g_1, g_2, \cdots, g_k) \in S_p$ is an arbitrary cycle, we can write
$$
\gamma = (g_1, g_2, \cdots, g_k) = (1, g_1)( 1, g_2), \cdots (1, g_k),
$$

so $\gamma \in J$.
Then writing any arbitrary permutation as a product of disjoint cycles, we find that $S_p \subseteq J \subseteq S$, and so $S_p \subseteq S$ as desired.
$\qed$
