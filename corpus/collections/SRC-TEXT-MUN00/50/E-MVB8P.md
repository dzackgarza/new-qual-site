---
schema: qual/card@1
id: E-MVB8P
kind: problem
title: Sigma-compact Hausdorff spaces of finite dimension
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Recall that $X$ is said to be $\sigma$-compact if there is a countable collection of compact subspaces of $X$ whose interiors cover $X$.

Theorem.
Let $X$ be a $\sigma$-compact Hausdorff space.
If every compact subspace of $X$ has topological dimension at most $m$, then so does $X$.

Let $\mathcal{A}$ be an open cover of $X$.
Find an open cover $\mathcal{B}$ of $X$ refining $\mathcal{A}$ that has order at most $m + 1$, as follows:

(a) Show that $X = \bigcup X_n$, where $X_n$ is compact and $X_n \subset \operatorname{Int} X_{n+1}$ for each $n$.
Let $X_0 = \varnothing$.

(b) Find an open covering $\mathcal{B}_0$ of $X$ refining $\mathcal{A}$ such that for each $n$, each element of $\mathcal{B}_0$ that intersects $X_n$ lies in $X_{n+1}$.

(c) Suppose $n \geq 0$ and $\mathcal{B}_n$ is an open covering of $X$ refining $\mathcal{B}_0$ such that $\mathcal{B}_n$ has order at most $m + 1$ at points of $X_n$.
Choose an open covering $\mathcal{C}$ of $X$ refining $\mathcal{B}_n$ that has order at most $m + 1$ at points of $X_{n+1}$.
Choose $f: \mathcal{C} \to \mathcal{B}_n$ so that $C \subset f(C)$.
For $B \in \mathcal{B}_n$, let $D(B)$ be the union of those $C$ for which $f(C) = B$.
Let $\mathcal{B}_{n+1}$ consist of all sets $B \in \mathcal{B}_n$ for which $B \cap X_{n-1} \neq \varnothing$, along with all sets $D(B)$ for which $B \in \mathcal{B}_n$ and $B \cap X_{n-1} = \varnothing$.
Show that $\mathcal{B}_{n+1}$ is an open covering of $X$ that refines $\mathcal{B}_n$ and has order at most $m + 1$ at points of $X_{n+1}$.

(d) Define $\mathcal{B}$ as follows.
Given a set $B$, it belongs to $\mathcal{B}$ if there is an $N$ such that $B \in \mathcal{B}_n$ for all $n \geq N$.
:::

::: {.solution}
Let \(\mathcal A\) be an open cover of \(X\).

**(a)** By \(\sigma\)-compactness choose compact sets \(K_1,K_2,\dots\) whose interiors cover \(X\). We construct integers
\[
1\le r_1<r_2<\cdots
\]
so that
\[
X_n=K_1\cup\cdots\cup K_{r_n}
\]
satisfies \(X_n\subset\operatorname{Int}X_{n+1}\). Once \(r_n\) is chosen, the compact set \(X_n\) is covered by the family \(\{\operatorname{Int}K_j\}\); a finite subfamily suffices, and taking \(r_{n+1}\) larger than all its indices gives the desired inclusion. Enlarging \(r_1\) if necessary makes the \(X_n\)'s cover \(X\). Put \(X_0=\varnothing\).

**(b)** For each \(x\in X\), let \(r\ge1\) be least such that \(x\in\operatorname{Int}X_r\). Choose \(A_x\in\mathcal A\) with \(x\in A_x\), and choose an open neighborhood
\[
x\in B_x\subset A_x\cap\operatorname{Int}X_r
\]
that is disjoint from \(X_{r-2}\) (with \(X_{-1}=X_0=\varnothing\)). Let \(\mathcal B_0=\{B_x:x\in X\}\). If \(B_x\cap X_n\ne\varnothing\), then \(n\ge r-1\), hence
\[
B_x\subset X_r\subset X_{n+1}.
\]
Thus \(\mathcal B_0\) has the required property and refines \(\mathcal A\).

**(c)** Assume \(\mathcal B_n\) has order at most \(m+1\) at points of \(X_n\). Since \(X_{n+1}\) is compact and has dimension at most \(m\), the restriction of \(\mathcal B_n\) to \(X_{n+1}\) has an open refinement of order at most \(m+1\). Extending these sets to \(X\) and adjoining \(X-X_{n+1}\) if necessary gives an open cover \(\mathcal C\) of \(X\) refining \(\mathcal B_n\) and having order at most \(m+1\) at points of \(X_{n+1}\).

Choose \(f:\mathcal C\to\mathcal B_n\) with \(C\subset f(C)\), and set
\[
D(B)=\bigcup\{C\in\mathcal C:f(C)=B\}.
\]
Each \(D(B)\) is open and contained in \(B\). Define \(\mathcal B_{n+1}\) as in the exercise. It is an open refinement of \(\mathcal B_n\). It covers \(X\): points lying in a retained \(B\) remain covered; otherwise a point lies in some \(C\in\mathcal C\), hence in \(D(f(C))\).

For the order bound, let \(x\in X_{n+1}\). If \(x\in X_n\), every member of \(\mathcal B_{n+1}\) containing \(x\) is contained in a distinct member of \(\mathcal B_n\) containing \(x\), so there are at most \(m+1\). If \(x\in X_{n+1}-X_n\), no retained \(B\) can contain \(x\): a retained \(B\) meets \(X_{n-1}\), hence by the property inherited from \(\mathcal B_0\) it lies in \(X_n\). Thus only sets \(D(B)\) occur at \(x\). Distinct such sets yield distinct elements \(C\in\mathcal C\) through \(x\), so their number is at most \(m+1\). Hence \(\mathcal B_{n+1}\) has order at most \(m+1\) on \(X_{n+1}\).

**(d)** Let \(\mathcal B\) consist of the sets that eventually remain unchanged in all \(\mathcal B_n\). Every such set refines \(\mathcal B_0\), hence \(\mathcal A\). To see that \(\mathcal B\) covers \(X\), take \(x\in X_n\) and choose \(B\in\mathcal B_{n+1}\) containing \(x\). At every later stage this \(B\) meets the corresponding retention set \(X_{k-1}\), so it is retained forever; hence \(B\in\mathcal B\).

Finally fix \(x\in X_n\). Any member of \(\mathcal B\) containing \(x\) must already occur by stage \(n+1\): after that stage, a set containing \(x\) can never be newly created as a \(D(B)\), because its predecessor meets \(X_n\) and is therefore retained. Thus the members of \(\mathcal B\) through \(x\) are among those of \(\mathcal B_{n+1}\) through \(x\), at most \(m+1\) of them. Therefore \(\mathcal B\) has order at most \(m+1\) everywhere.

Hence every open cover of \(X\) has an open refinement of order at most \(m+1\), so \(\dim X\le m\).
:::
