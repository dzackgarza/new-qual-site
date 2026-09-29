---
schema: qual/card@1
id: P-RIW3S
kind: problem
title: Based maps $S^1\to X$ are freely homotopic iff they are conjugate in $\pi_1(X,x_0)$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Conjugacy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement verbatim against problem 3 of the official UGA Spring 2015 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the incomplete argument with the square-boundary conjugacy calculation and a constructive free-homotopy converse.
---

::: {.problem}
Let $S^1$ denote the unit circle in $C$, $X$ be any topological space, $x_0 \in X$, and $$\gamma_0, \gamma_1 : S^1 \to X$$ be two continuous maps such that $\gamma_0 (1) = \gamma_1 (1) = x_0$.

Prove that $\gamma_0$ is homotopic to $\gamma_1$ if and only if the elements represented by $\gamma_0$ and $\gamma_1$ in $\pi_1 (X, x_0 )$ are conjugate.
:::

::: {.solution}
Identify $S^1$ with $I/(0\sim1)$ and use the same symbols $\gamma_0,\gamma_1$ for the corresponding loops $I\to X$.

::: pf

::: {.pf-step #s1}

Suppose first that $\gamma_0$ and $\gamma_1$ are freely homotopic.
If
\[
H:S^1\times I\to X
\]
is a free homotopy from $\gamma_0$ to $\gamma_1$, then the track of the basepoint,
\[
\alpha(t)=H(1,t),
\]
is a loop at $x_0$.

::: pf-proof

Because $H(-,0)=\gamma_0$ and $H(-,1)=\gamma_1$,
\[
\alpha(0)=\gamma_0(1)=x_0
\qquad\text{and}\qquad
\alpha(1)=\gamma_1(1)=x_0.
\]
Thus $\alpha$ is indeed a loop based at $x_0$.

:::

:::

::: {.pf-step #s2}

The based homotopy classes satisfy
\[
[\gamma_0]=[\alpha][\gamma_1][\alpha]^{-1}
\qquad\text{in }\pi_1(X,x_0).
\]

::: pf-proof

Let
\[
q:I\to S^1=I/(0\sim1)
\]
be the quotient map and set
\[
\widetilde H(s,t)=H(q(s),t).
\]
Then
\[
\widetilde H(0,t)=\widetilde H(1,t)=\alpha(t),
\]
while the bottom and top edges of the square are $\gamma_0$ and $\gamma_1$.

Traverse $\partial(I\times I)$ starting at $(0,0)$ along the bottom edge, then the right edge, then the top edge backwards, and finally the left edge backwards.
Its image under $\widetilde H$ represents
\[
[\gamma_0][\alpha][\gamma_1]^{-1}[\alpha]^{-1}.
\]
This boundary loop is null-homotopic because $\widetilde H$ extends it over the whole square.
Hence
\[
[\gamma_0][\alpha][\gamma_1]^{-1}[\alpha]^{-1}=1,
\]
and therefore
\[
[\gamma_0]=[\alpha][\gamma_1][\alpha]^{-1}.
\]
Thus freely homotopic based loops represent conjugate elements.

:::

:::

::: {.pf-step #s3}

Conversely, suppose that $[\gamma_0]$ and $[\gamma_1]$ are conjugate.
Choose a loop $\alpha$ at $x_0$ such that
\[
[\gamma_0]=[\alpha][\gamma_1][\alpha]^{-1}.
\]
Then $\gamma_0$ is homotopic relative to the basepoint to the loop
\[
\alpha*\gamma_1*\alpha^{-1}.
\]

::: pf-proof

The displayed equality is precisely equality of the two based-loop classes in $\pi_1(X,x_0)$.
By the definition of the fundamental group, representatives of the same class are homotopic through loops that keep the basepoint fixed.

:::

:::

::: {.pf-step #s4}

For any two loops $a,b$ based at the same point, the loops $a*b$ and $b*a$ are freely homotopic.

::: pf-proof

Let
\[
L=a*b:S^1\to X
\]
using the standard parameterization in which $a$ occupies the first half of the circle and $b$ the second half.
For $0\le t\le1$, let $R_t:S^1\to S^1$ be rotation through angle $\pi t$.
Then
\[
K(z,t)=L(R_t(z))
\]
is a free homotopy.
At $t=0$ it is $a*b$, while at $t=1$ the half-turn interchanges the two half-circle parameter intervals, so it is $b*a$.

:::

:::

::: {.pf-step #s5}

The conjugate loop $\alpha*\gamma_1*\alpha^{-1}$ is freely homotopic to $\gamma_1$.

::: pf-proof

Up to the standard based reparameterization associating concatenations,
\[
\alpha*\gamma_1*\alpha^{-1}
\simeq
\alpha*(\gamma_1*\alpha^{-1}).
\]
Apply step [](#s4){.pf-ref} with
\[
a=\alpha,
\qquad
b=\gamma_1*\alpha^{-1}.
\]
This gives a free homotopy
\[
\alpha*(\gamma_1*\alpha^{-1})
\simeq_{\mathrm{free}}
(\gamma_1*\alpha^{-1})*\alpha.
\]
The loop on the right is based-homotopic, by associativity of concatenation, to
\[
\gamma_1*(\alpha^{-1}*\alpha).
\]
The loop $\alpha^{-1}*\alpha$ is null-homotopic relative to the basepoint, so this is based-homotopic to $\gamma_1$.
Every based homotopy is in particular a free homotopy, proving the claim.

:::

:::

::: pf-step

Therefore $\gamma_0$ and $\gamma_1$ are freely homotopic if and only if their classes in $\pi_1(X,x_0)$ are conjugate.

::: pf-proof

The forward implication is steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.
For the converse, step [](#s3){.pf-ref} gives a based homotopy from $\gamma_0$ to $\alpha*\gamma_1*\alpha^{-1}$, and step [](#s5){.pf-ref} gives a free homotopy from that conjugate loop to $\gamma_1$.
Concatenating the two homotopies gives a free homotopy from $\gamma_0$ to $\gamma_1$.

:::

:::

:::

:::

- Claim: $\gamma_1$ and $T\ast \gamma_2 \ast \inverseof{T}$ are homotopic rel $x_0$, making $\gamma_1, \gamma_2$ conjugate in $\pi_1$.

  - Idea: for each fixed $s$, follow $T$ for the first third, $\gamma_2$ for the middle third, $\inverseof{T}$ for the last third.

  ![figures/2020-02-04-20:23.png](../../assets/figures/2020-02-04-20%3A23.png)

$\impliedby$:

- Suppose $[\gamma_1] = [h] [\gamma_2] \inverseof{[h]}$ in $\pi_1(X; x_0)$.
  The claim is that $\gamma_1 \homotopic h\gamma_2 \inverseof{h}$ are freely homotopic.

- Since these are equal in $\pi_1$, we get a square interpolating $\gamma_1$ and $h\gamma_2 \inverseof{h}$ with constant sides $\id_{x_0}$.

- For free homotopies, the sides don't have to be constant, to merge $h$ and $\inverseof{h}$ into the sides to get a free homotopy from $f$ to $g$:

![image_2021-06-04-00-44-45.png](../../assets/Topology/figures/image_2021-06-04-00-44-45.png)
