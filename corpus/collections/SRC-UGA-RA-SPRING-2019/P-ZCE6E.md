---
schema: qual/card@1
id: P-ZCE6E
kind: problem
title: The subgraph of a nonnegative function is measurable if and only if the function
  is, and $m(\mathcal{A})=\int_{\RR^n}f=\int_0^\infty m(\{f\ge t\})\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
---

Let $f$ be a non-negative function on $\RR^n$ and $\mathcal A = \{(x, t) ∈ \RR^n \times \RR : 0 ≤ t ≤ f (x)\}$.

Prove the validity of the following two statements:

a. $f$ is a Lebesgue measurable function on $\RR^n \iff  \mathcal A$ is a Lebesgue measurable subset of $\RR^{n+1}$

b. If $f$ is a Lebesgue measurable function on $\RR^n$, then
\[
m(\mathcal{A})=\int _{\RR^{n}} f(x) d x=\int_{0}^{\infty} m\left(\left\{x \in \RR^{n}: f(x) \geq t\right\}\right) dt
\]

:::{.concept}
\envlist
- See Stein and Shakarchi p.82 corollary 3.3.
- Tonelli
- Important trick! $\ts{(x, t) \st 0\leq t \leq f(x)} = \ts{ f(x) \geq t} \intersect \ts{ t\geq 0 }$
:::

:::{.solution}
\envlist


:::{.proof title="a, $\implies$"}
$\implies$:

- Suppose $f:\RR^n\to \RR$ is a measurable function.
- Rewrite $A$:
\[
A 
&= \ts{ (x, t) \in \RR^d \cross \RR \st 0\leq t \leq f(x) } \\
&= \ts{ (x, t) \in \RR^d \cross \RR \st 0 \leq t < \infty } 
\intersect \ts{ (x, t) \in \RR^d\cross \RR \st t\leq f(x) } \\
&= \qty{ \RR^d \cross [0, \infty) } 
\intersect \ts{ (x, t) \in \RR^d\cross \RR \st f(x) -t \geq 0  } \\
&\da \qty{ \RR^d \cross [0, \infty) } \intersect H\inv\qty{[0, \infty)}
,\]
where we define
\[
H: \RR^d \cross \RR &\to \RR \\
(x, t) &\mapsto f(x) - t
.\]
  - Note: this is "clearly" measurable!

- If we can show both sets are measurable, we're done, since $\sigma\dash$algebras are closed under countable intersections.
- The first set is measurable since it is a Borel set in $\RR^{d+1}$.
- For the same reason, it suffices to show $H$ is a measurable function.
- Define cylinder functions
\[
F: \RR^d \cross \RR &\to \RR \\
(x, t) &\mapsto f(x)
\]
and
\[
G: \RR^d \cross \RR &\to \RR \\
(x, t) &\mapsto t
\]
  - $F$ is a cylinder of $f$, and since $f$ is measurable by assumption, $F$ is measurable.
  - $G$ is a cylinder on the identity for $\RR$, which is measurable, so $G$ is measurable.


- Define 
\[
H: \RR^d &\to \RR \\
(x, t) &\mapsto F(x, t) - G(x, t) \da f(x) - t
,\]
  which are linear combinations of measurable functions and thus measurable.


:::

:::{.proof title="a, $\impliedby$"}
$\impliedby$:

- Suppose $\mca$ is a measurable set.
- A corollary of Tonelli applied to $\chi_X$: if $E$ is measurable, then for a.e. $t$ the following slice is measurable:
\[
\mca_t \da \ts{ x \in \RR^d \st (x,t) \in \mca  }
&= \ts{x\in \RR^d \st f(x) \geq t \geq 0} \\
&= f\inv\qty{[t, \infty)}
.\]
  - But maybe this isn't enough, because we need $f\inv\qty{[\alpha, \infty)}$ for *all* $\alpha$
- But the other slice is also measurable for a.e. $x$:
\[
\mca_x 
&\da \ts{ t\in \RR \st (x, t) \in \mca } \\
&= \ts{ t\in \RR \st 0 \leq t \leq f(x) } \\
&= \ts{ t\in \RR \st t\in [0, f(x)]  } \\
&= [0, f(x)]
.\]

- Moreover the function $x\mapsto m(\mca_x)$ is a measurable function of $x$
- Now note $m(\mca_x) = f(x) - 0 = f(x)$, so $f$ must be measurable.

:::

:::{.proof title="of b"}
\envlist
- Writing down what the slices are
\[
\mathcal{A} &= \theset{(x, t) \in \RR^n\cross \RR \suchthat 0 \leq t \leq f(x)} 
\\
\mathcal{A}_t &= \theset{x
\in \RR^n \suchthat t\leq f(x) }
.\]

- Then
\[
\int_{\RR^n} f(x) ~dx 
&= \int_{\RR^n} \int_0^{f(x)} 1 ~dt~dx \\
&= \int_{\RR^n} \int_{0}^\infty \chi_\mathcal{A} ~dt~dx \\
&\overset{F.T.}= \int_{0}^\infty \int_{\RR^n} \chi_\mathcal{A} ~dx~dt\\
&= \int_0^\infty m(\mathcal{A}_t) ~dt
,\]
  where we just use that $\int \int \chi_\mathcal{A} = m(\mathcal{A})$

- By Tonelli, all of these integrals are equal. 
  - This is justified because $f$ was assumed measurable on $\RR^n$, thus by (a) $\mathcal{A}$ is a measurable set and thus $\chi_A$ is a measurable function on $\RR^n\cross \RR$.


:::

:::

