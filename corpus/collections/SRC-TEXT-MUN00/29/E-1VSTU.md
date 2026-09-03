---
schema: qual/card@1
id: E-1VSTU
kind: problem
title: Net convergence generalizes sequence convergence
classification:
  areas:
  - topology
  topics:
  - Nets
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $X$ be a topological space.
A net in $X$ is a function $f$ from a directed set $J$ into $X$.
If $\alpha \in J$, we usually denote $f(\alpha)$ by $x_\alpha$.
We denote the net $f$ itself by the symbol $(x_\alpha)_{\alpha \in J}$, or merely by $(x_\alpha)$ if the index set is understood.

The net $(x_\alpha)$ is said to converge to the point $x$ of $X$ (written $x_\alpha \to x$) if for each neighborhood $U$ of $x$, there exists $\alpha \in J$ such that

$$
\alpha \preceq \beta \implies x_\beta \in U.
$$

Show that these definitions reduce to familiar ones when $J = \mathbb{Z}_+$.
:::

::: solution
**Goal:** Prove that when the directed set $J$ is the set of positive integers $\mathbb{Z}_+$ equipped with the standard ordering $\le$, the definition of a net and net convergence in a topological space $X$ coincides precisely with the classical definition of a sequence and sequence convergence.

<1>1. $\mathbb{Z}_+$ is a directed set under the standard ordering $\le$:
    *Proof:*
    <2>1. The standard relation $\le$ on $\mathbb{Z}_+$ is reflexive ($n \le n$) and transitive ($m \le n \land n \le k \implies m \le k$).
    <2>2. For any two elements $m, n \in \mathbb{Z}_+$, choose $k = \max\{m, n\} \in \mathbb{Z}_+$. Then $m \le k$ and $n \le k$.
    <2>3. Therefore $(\mathbb{Z}_+, \le)$ is a directed set.

<1>2. A net indexed by $\mathbb{Z}_+$ is a sequence:
    *Proof:*
    <2>1. A net in $X$ indexed by $\mathbb{Z}_+$ is a function $f: \mathbb{Z}_+ \to X$.
    <2>2. By standard definition, a sequence in $X$ is a function from $\mathbb{Z}_+$ into $X$, written as $(x_n)_{n \in \mathbb{Z}_+}$ where $x_n = f(n)$.
    <2>3. Thus nets indexed by $\mathbb{Z}_+$ and sequences in $X$ are the exact same objects.

<1>3. Net convergence on $\mathbb{Z}_+$ is sequence convergence:
    *Proof:*
    <2>1. Under the net convergence definition with $(J, \preceq) = (\mathbb{Z}_+, \le)$, $(x_n) \to x$ if and only if for every neighborhood $U$ of $x$, there exists $N \in \mathbb{Z}_+$ such that:
        $$N \le n \implies x_n \in U.$$
    <2>2. Under the classical definition of sequence convergence in a topological space, $(x_n) \to x$ if and only if for every neighborhood $U$ of $x$, there exists an integer $N$ such that $x_n \in U$ for all $n \ge N$.
    <2>3. These two conditions are logically and syntactically identical.

<1>4. Conclusion:
    The theory of nets on the directed set $(\mathbb{Z}_+, \le)$ reduces directly to the standard theory of sequences. Q.E.D.
:::
