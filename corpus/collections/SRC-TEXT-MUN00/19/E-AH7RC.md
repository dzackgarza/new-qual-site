---
schema: qual/card@1
id: E-AH7RC
kind: problem
title: Convergence in products via coordinate convergence
classification:
  areas:
  - topology
  topics:
  - Convergence
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Let $\mathbf{x}_1, \mathbf{x}_2, \ldots$ be a sequence of the points of the product space $\prod X_\alpha$.
Show that this sequence converges to the point $\mathbf{x}$ if and only if the sequence $\pi_\alpha(\mathbf{x}_1), \pi_\alpha(\mathbf{x}_2), \ldots$ converges to $\pi_\alpha(\mathbf{x})$ for each $\alpha$.
Is this fact true if one uses the box topology instead of the product topology?
:::

::: {.solution}
**Goal.** Characterize convergence in a product space, and decide the box-topology analogue.

<1>1. In the product topology, $\mathbf x_n \to \mathbf x$ iff $\pi_\alpha(\mathbf x_n) \to \pi_\alpha(\mathbf x)$ for every $\alpha$.
<2>1. ($\Rightarrow$) Each projection $\pi_\alpha$ is continuous.
::: {.proof}
the product topology is the coarsest making all projections continuous.
:::
<2>2. Hence $\pi_\alpha(\mathbf x_n) \to \pi_\alpha(\mathbf x)$.
::: {.proof}
continuous maps preserve convergence.
:::
<2>3. ($\Leftarrow$) Suppose each coordinate converges. A basic neighborhood of $\mathbf x$ is $\prod_\alpha U_\alpha$ with $U_\alpha = X_\alpha$ for all but finitely many $\alpha$.
::: {.proof}
this is the definition of the product topology basis.
:::
<2>4. For each of the finitely many nontrivial $U_\alpha$, there is $N_\alpha$ with $\pi_\alpha(\mathbf x_n) \in U_\alpha$ for $n \ge N_\alpha$.
::: {.proof}
coordinate convergence.
:::
<2>5. Taking $N = \max_\alpha N_\alpha$, $\mathbf x_n$ lies in the basic neighborhood for all $n \ge N$.
::: {.proof}
the maximum is over finitely many indices.
:::
<2>6. Hence $\mathbf x_n \to \mathbf x$.
::: {.proof}
every basic neighborhood eventually contains the sequence.
:::

<1>2. The box topology analogue fails.
<2>1. In the box topology, basic neighborhoods are $\prod_\alpha U_\alpha$ with each $U_\alpha$ open (no finiteness restriction).
::: {.proof}
definition of the box topology.
:::
<2>2. Counterexample: $X = \RR^\NN$ with the box topology, $\mathbf x_n = (1/n, 1/n, 1/n, \dots)$.
::: {.proof}
each coordinate converges to $0$, but the sequence does not converge to $\mathbf 0$.
:::
<2>3. The sequence does not converge to $\mathbf 0$ in the box topology.
::: {.proof}
the box neighborhood $\prod_{k} (-1/k, 1/k)$ contains no $\mathbf x_n$ (since the $n$-th coordinate of $\mathbf x_n$ is $1/n$, which is not in $(-1/n, 1/n)$ for the $n$-th factor when $n$ is large enough relative to the neighborhood's $n$-th interval).
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves the product-topology statement; <1>2 shows it fails for the box topology.
:::
:::
