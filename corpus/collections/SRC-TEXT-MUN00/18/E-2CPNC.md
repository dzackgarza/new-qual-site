---
schema: qual/card@1
id: E-2CPNC
kind: problem
title: Pasting over a locally finite closed cover
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $\ts{A_\alpha}$ be a collection of subsets of $X$; let $X = \bigcup_\alpha A_\alpha$.
Let $f: X \to Y$; suppose that $f \mid A_\alpha$ is continuous for each $\alpha$.

(a) Show that if the collection $\ts{A_\alpha}$ is finite and each set $A_\alpha$ is closed, then $f$ is continuous.

(b) Find an example where the collection $\ts{A_\alpha}$ is countable and each $A_\alpha$ is closed, but $f$ is not continuous.

(c) An indexed family of sets $\ts{A_\alpha}$ is said to be locally finite if each point $x$ of $X$ has a neighborhood that intersects $A_\alpha$ for only finitely many values of $\alpha$.
Show that if the family $\ts{A_\alpha}$ is locally finite and each $A_\alpha$ is closed, then $f$ is continuous.
:::

::: {.solution}
For a closed set $C\subseteq Y$ put $F_\alpha=(f|_{A_\alpha})^{-1}(C)=f^{-1}(C)\cap A_\alpha$, so that $f^{-1}(C)=\bigcup_\alpha F_\alpha$ because the $A_\alpha$ cover $X$.

<1>1. If $A_\alpha$ is closed in $X$, then $F_\alpha$ is closed in $X$ and $F_\alpha\subseteq A_\alpha$.

::: {.proof}
Since $f|_{A_\alpha}$ is continuous, $F_\alpha$ is closed in the subspace $A_\alpha$, and a closed subset of a closed subspace is closed in $X$.
:::

<1>2. (a) If the $A_\alpha$ are finitely many closed sets, $f$ is continuous.

::: {.proof}
By step <1>1, $f^{-1}(C)$ is a finite union of closed sets for every closed $C\subseteq Y$.
:::

<1>3. (b) For the closed sets $A_0=(-\infty,0]$ and $A_n=[\frac1n,\infty)$, $n\in\mathbb Z_+$, covering $\mathbb R$, the function $f\colon\mathbb R\to\mathbb R$ with $f(x)=0$ for $x\le0$ and $f(x)=1$ for $x>0$ is continuous on each $A_n$ but not continuous.

::: {.proof}
The sets cover $\mathbb R$, since every $x>0$ exceeds some $\frac1n$.
The restriction of $f$ to $A_0$ is constant $0$ and to each $A_n$, $n\ge1$, is constant $1$.
The set $f^{-1}(\{0\})=(-\infty,0]$ is closed, but $f^{-1}(\{1\})=(0,\infty)$ is not closed, although $\{1\}$ is closed.
:::

<1>4. The union of a locally finite family $\{F_\alpha\}$ of closed sets is closed.

::: {.proof}
Let $F=\bigcup_\alpha F_\alpha$ and $x\in\overline F$.
Choose an open $U\ni x$ meeting only $F_{\alpha_1},\ldots,F_{\alpha_k}$.
Then $U\cap F\subseteq F_{\alpha_1}\cup\cdots\cup F_{\alpha_k}$, and $x\in\overline{U\cap F}$ because $U$ is an open neighborhood of $x$.
Hence $x\in\overline{F_{\alpha_1}\cup\cdots\cup F_{\alpha_k}}=F_{\alpha_1}\cup\cdots\cup F_{\alpha_k}\subseteq F$.
:::

<1>5. (c) If $\{A_\alpha\}$ is locally finite and each $A_\alpha$ is closed, $f$ is continuous.

::: {.proof}
By step <1>1, each $F_\alpha$ is closed and $F_\alpha\subseteq A_\alpha$, so $\{F_\alpha\}$ is locally finite.
By step <1>4, $f^{-1}(C)=\bigcup_\alpha F_\alpha$ is closed for every closed $C\subseteq Y$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2, <1>3, and <1>5 answer (a), (b), and (c).
:::
:::
