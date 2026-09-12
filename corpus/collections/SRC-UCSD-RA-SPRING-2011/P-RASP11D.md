---
schema: qual/card@1
id: P-RASP11D
kind: problem
title: "Closedness of L^p balls and embeddings in L^1"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Spring 2011 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $(X, \mathcal{M}, \mu)$ be a finite measure space.

(a) (10 pts) Let $1 \leq p \leq \infty$.
Show that for fixed $M > 0$ the ball $\{f : \|f\|_{L^p(d\mu)} \leq M\}$ is closed in $L^1(d\mu)$.

(b) (10 pts) Show that the whole of $L^p(d\mu)$ is closed in $L^1(d\mu)$ iff there exists $C > 0$ such that $\|f\|_{L^p(d\mu)} \leq C\|f\|_{L^1(d\mu)}$ for all $f \in L^p(d\mu)$.

(c) (10 pts) Now let $1 < p \leq \infty$.
Show that the assumptions of part (b) above hold iff both $L^p(d\mu)$ and $L^1(d\mu)$ are finite dimensional.

Hint: Show that if $(X, \mathcal{M}, \mu)$ is any measure space where there exists $0 < c, C < \infty$ such that $c \leq \mu(E) \leq C$ for every set $E \in \mathcal{M}$ of nonzero measure, then $L^1(d\mu)$ is finite dimensional.
:::

::: solution
<1>1. Prove that every closed $L^p$ ball is closed in $L^1$.
::: proof
Let $f_n\to f$ in $L^1$ and suppose $\|f_n\|_p\le M$ for every $n$. Passing to a subsequence, still denoted $f_n$, we may assume
\[
f_n(x)\to f(x)
\]
for almost every $x$.

If $1\le p<\infty$, Fatou's lemma gives
\[
\int_X|f|^p\,d\mu
\le \liminf_{n\to\infty}\int_X|f_n|^p\,d\mu
\le M^p.
\]
Hence $f\in L^p$ and $\|f\|_p\le M$.

If $p=\infty$, after discarding one null set we have
\[
|f_n(x)|\le M
\]
for every $n$ and almost every $x$. Taking the pointwise limit gives $|f(x)|\le M$ a.e., so $\|f\|_\infty\le M$.

Thus the radius-$M$ $L^p$ ball is closed in $L^1$.
:::

<1>2. Prove part (b).
::: proof
Assume first that
\[
\|f\|_p\le C\|f\|_1
\qquad(f\in L^p).
\]
If $(f_n)\subset L^p$ and $f_n\to f$ in $L^1$, then
\[
\|f_n-f_m\|_p\le C\|f_n-f_m\|_1,
\]
so $(f_n)$ is Cauchy in $L^p$. Since $L^p$ is complete, $f_n\to g$ in $L^p$ for some $g\in L^p$. Because $\mu(X)<\infty$, the standard finite-measure embedding $L^p\hookrightarrow L^1$ is continuous, so $f_n\to g$ also in $L^1$. Uniqueness of the $L^1$ limit gives $f=g$ a.e. Thus $f\in L^p$, and $L^p$ is closed in $L^1$.

Conversely, suppose $L^p$ is closed in $L^1$. Then $L^p$, equipped with the $L^1$ norm, is a Banach space. The identity map
\[
I:(L^p,\|\cdot\|_p)\longrightarrow(L^p,\|\cdot\|_1)
\]
is continuous because $\mu(X)<\infty$, and it is bijective. By the bounded inverse theorem, its inverse is continuous. Hence there exists $C>0$ such that
\[
\boxed{\|f\|_p\le C\|f\|_1\qquad(f\in L^p).}
\]
:::

<1>3. The norm inequality forces a uniform lower bound on nonzero set measures.
::: proof
Assume $1<p<\infty$ and the inequality from Step 2. Apply it to $f=\mathbf1_E$ for a measurable set $E$ with $\mu(E)>0$:
\[
\mu(E)^{1/p}\le C\mu(E).
\]
Therefore
\[
\mu(E)\ge C^{-p/(p-1)}.
\]
If $p=\infty$, the same argument gives
\[
1=\|\mathbf1_E\|_\infty\le C\mu(E),
\]
so $\mu(E)\ge C^{-1}$. Thus in every case there is $c>0$ such that
\[
\mu(E)>0\quad\Longrightarrow\quad \mu(E)\ge c.
\]
Of course also $\mu(E)\le\mu(X)<\infty$.
:::

<1>4. A finite measure space with that lower bound has finite-dimensional $L^1$.
::: proof
There cannot be more than
\[
N:=\left\lfloor\frac{\mu(X)}c\right\rfloor
\]
pairwise disjoint measurable sets of positive measure.

Starting from $X$, repeatedly split any positive-measure set which is not an atom into two disjoint positive-measure measurable subsets. Each split increases the number of pairwise disjoint positive-measure pieces, so after at most $N-1$ splits the process must stop. We obtain finitely many atoms
\[
A_1,\dots,A_m
\]
whose union agrees with $X$ up to a null set.

Every measurable function is almost everywhere constant on each atom: for a real measurable $u$ on an atom $A$, each sublevel set $A\cap\{u<q\}$ has either zero measure or full measure in $A$, and a countable rational-threshold argument determines a single essential value. Applying this to real and imaginary parts gives the complex case.

Hence every $L^1$ function has the form
\[
\sum_{j=1}^m a_j\mathbf1_{A_j}
\]
almost everywhere. Therefore
\[
\dim L^1\le m<\infty.
\]
The same description shows $L^p=L^1$ as vector spaces and $L^p$ is finite dimensional as well.
:::

<1>5. Finish the equivalence in part (c).
::: proof
Steps 3 and 4 show that the assumptions in part (b) imply that both $L^p$ and $L^1$ are finite dimensional.

Conversely, suppose both are finite dimensional. Since bounded measurable simple functions lie in $L^p$ and are dense in $L^1$ on a finite measure space, $L^p$ is dense in $L^1$. A finite-dimensional subspace is closed, so density forces
\[
L^p=L^1
\]
as vector spaces. Any two norms on a finite-dimensional vector space are equivalent; hence there exists $C>0$ with
\[
\|f\|_p\le C\|f\|_1.
\]
By part (b), this is equivalent to $L^p$ being closed in $L^1$.
:::
:::
