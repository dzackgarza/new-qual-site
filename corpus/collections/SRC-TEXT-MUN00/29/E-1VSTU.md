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

Show that these definitions reduce to familiar ones when $J = \ZZ_+$.
:::

::: {.solution}

::: pf

::: pf-step
$\ZZ_+$ is a directed set under the standard ordering $\le$:

::: pf-proof

::: pf-step
The standard relation $\le$ on $\ZZ_+$ is reflexive ($n \le n$) and transitive ($m \le n \land n \le k \implies m \le k$).
:::

::: pf-step
For any two elements $m, n \in \ZZ_+$, choose $k = \max\{m, n\} \in \ZZ_+$. Then $m \le k$ and $n \le k$.
:::

::: pf-step
Therefore $(\ZZ_+, \le)$ is a directed set.
:::

:::

:::

::: pf-step
A net indexed by $\ZZ_+$ is a sequence:

::: pf-proof

::: pf-step
A net in $X$ indexed by $\ZZ_+$ is a function $f: \ZZ_+ \to X$.
:::

::: pf-step
By standard definition, a sequence in $X$ is a function from $\ZZ_+$ into $X$, written as $(x_n)_{n \in \ZZ_+}$ where $x_n = f(n)$.
:::

::: pf-step
Thus nets indexed by $\ZZ_+$ and sequences in $X$ are the exact same objects.
:::

:::

:::

::: pf-step
Net convergence on $\ZZ_+$ is sequence convergence:

::: pf-proof

::: pf-step
Under the net convergence definition with $(J, \preceq) = (\ZZ_+, \le)$, $(x_n) \to x$ if and only if for every neighborhood $U$ of $x$, there exists $N \in \ZZ_+$ such that:
$$N \le n \implies x_n \in U.$$
:::

::: pf-step
Under the classical definition of sequence convergence in a topological space, $(x_n) \to x$ if and only if for every neighborhood $U$ of $x$, there exists an integer $N$ such that $x_n \in U$ for all $n \ge N$.
:::

::: pf-step
These two conditions are logically and syntactically identical.
:::

:::

:::

::: pf-step
Conclusion:
The theory of nets on the directed set $(\ZZ_+, \le)$ reduces directly to the standard theory of sequences. Q.E.D.
:::

:::

:::
