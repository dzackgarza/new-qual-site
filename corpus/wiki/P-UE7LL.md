---
schema: qual/card@1
id: P-UE7LL
kind: problem
title: "Note that if either $p=1$ or $q=1$, $G$ is a $p\\dash$group, which is \u2026"
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - normal-subgroups
  - classification
relations: []
review: draft
---

Note that if either $p=1$ or $q=1$, $G$ is a $p\dash$group, which is a nontrivial center that is always normal.
So assume $p\neq 1$ and $q\neq 1$.

We want to show that $G$ has a non-trivial normal subgroup.
Noting that $\size G = p^2 q$, we will proceed by showing that either $n_p$ or $n_q$ must be 1.

We immediately note that
\[
\begin{align*}
n_p \equiv 1 \mod p &\quad& n_q \equiv 1 \mod q \\
n_p \divides q &\quad& n_q \divides p^2
,\end{align*}
\]

which forces
$$
n_p \in \theset{1, q}, \quad n_1 \in \theset{1, p, p^2}.
$$

If either $n_p =1$ or $n_q = 1$, we are done, so suppose $n_p \neq 1$ and $n_1 \neq 1$.
This forces $n_p = q$, and we proceed by cases:
