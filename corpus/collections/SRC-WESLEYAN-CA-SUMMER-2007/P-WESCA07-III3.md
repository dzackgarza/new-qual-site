---
schema: qual/card@1
id: P-WESCA07-III3
kind: problem
title: "Does $v=u^2$ force an analytic function to be constant?"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section III, problem 3 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $f=u+iv$ be analytic on an open set $U\subseteq\mathbb C$ and suppose
\[
v=u^2.
\]
Can one conclude that $f$ is constant on $U$?

If yes, prove it.
If not, give a counterexample and modify the statement so that the corresponding constant-function conclusion is true, then prove the modified statement.
:::

::: {.solution}
<1>1. As stated, one cannot conclude that $f$ is constant on $U$.

::: {.proof}
The obstruction is that an open set need not be connected.
:::

<1>2. A counterexample is obtained by taking
$$
U=D(-2,1/4)\cup D(2,1/4)
$$
and defining
$$
f(z)=
\begin{cases}
0,&z\in D(-2,1/4),\\
1+i,&z\in D(2,1/4).
\end{cases}
$$

::: {.proof}
The two disks are disjoint, so $f$ is holomorphic on the open set $U$: it is constant on each connected component. On the first component,
$$
u=0,
\qquad
v=0=u^2.
$$
On the second component,
$$
u=1,
\qquad
v=1=u^2.
$$
Thus the relation $v=u^2$ holds everywhere on $U$, but $f$ takes two different values and is not constant on $U$.
:::

<1>3. The corrected statement is: if $U$ is a domain, meaning that $U$ is open and connected, then every analytic function $f=u+iv$ on $U$ satisfying
$$
v=u^2
$$
is constant.

::: {.proof}
The added connectedness hypothesis rules out the counterexample from step <1>2 and permits use of the Open Mapping Theorem.
:::

<1>4. Under the corrected hypothesis, $f(U)$ is contained in the parabola
$$
P=\{x+ix^2:x\in\RR\}.
$$

::: {.proof}
If $f(z)=u(z)+iv(z)$ and $v(z)=u(z)^2$, then
$$
f(z)=u(z)+i\,u(z)^2\in P
$$
for every $z\in U$.
:::

<1>5. The set $P$ has empty interior in $\CC$.

::: {.proof}
The set $P$ is the graph in $\RR^2\cong\CC$ of the real-valued function $y=x^2$. No open disk in the plane can be contained in a one-dimensional graph, so $P$ contains no nonempty open subset of $\CC$.
:::

<1>6. Under the corrected hypothesis, $f$ is constant on $U$.

::: {.proof}
Suppose $f$ were nonconstant. Since $U$ is a domain and $f$ is holomorphic, the Open Mapping Theorem would imply that $f(U)$ is open in $\CC$. But step <1>4 gives
$$
f(U)\subseteq P,
$$
while step <1>5 says that $P$ contains no nonempty open set. This is a contradiction. Therefore $f$ is constant.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 disproves the original statement, and step <1>6 proves the corrected connected-domain statement.
:::
:::
