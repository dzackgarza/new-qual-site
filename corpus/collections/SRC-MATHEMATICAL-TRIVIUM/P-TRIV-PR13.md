---
schema: qual/card@1
id: P-TRIV-PR13
kind: problem
title: 'Gambler''s ruin: absorption probabilities and mean duration of a random walk'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 13, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains one or more nonprinting control bytes at this source position; they were removed from the authored card as nonsemantic extraction artifacts. The source includes Figure 8 illustrating the random walk; Flash preserves only the image placeholder/caption.
---

::: {.problem}
"Random walk" Let $A$, $B$, $x$ be integers, $A \leqslant x \leqslant B$. Consider the particle that starts moving from the point $x$ at time $t = 0$. At each step $\Delta t = 1$ the particle can move left or right from its recent position with the probabilities $p$ and $q = 1 - p$ correspondingly. If at some step it reaches the points $A$ or $B$, it stays there forever (see example figure below).

The source's Figure 8 illustrates one sample trajectory with $A=-B=5$ and $x=2$; the graphical trajectory is not present in the deterministic extraction.

(a) Assuming that the total number of steps approaches infinity, compute the probabilities $\alpha(x)$, $\beta(x)$ to find the particle at the points $A$ and $B$ correspondingly, as functions of the initial position $x$ of the particle.

(b) Find the mean time $m(x)$ of a random walk of the particle before it hits $A$ or $B$. Assume that $m(x) < \infty$. Check that if $p = q = \frac{1}{2}$ and $A = -B$, then $m(0) = B^2$. Hence the mean time of random walk is given by a square of distance traveled.
:::

::: {.solution}

The particle moves left with probability $p$ and right with probability $q=1-p$. Put $N=B-A$ and $i=x-A$.

::: pf

::: {.pf-step #s1-1}

The probability $\beta(x)$ of eventual absorption at $B$ satisfies
$$
\beta(x)=p\beta(x-1)+q\beta(x+1),
\qquad
\beta(A)=0,
\qquad
\beta(B)=1.
$$


::: pf-proof

Condition on the first step from an interior point. The walk moves to $x-1$ with probability $p$ and to $x+1$ with probability $q$. At the absorbing endpoints the probability of eventual absorption at $B$ is respectively $0$ and $1$.

:::

:::

::: {.pf-step #s1-2}

If $p\ne q$, then
$$
\boxed{
\beta(x)=
\frac{(p/q)^{x-A}-1}{(p/q)^{B-A}-1}},
\qquad
\boxed{\alpha(x)=1-\beta(x)}.
$$


::: pf-proof

The characteristic equation of the recurrence in step [](#s1-1){.pf-ref} is
$$
qr^2-r+p=0,
$$
whose roots are $1$ and $p/q$. Hence
$$
\beta(x)=C+D(p/q)^{x-A}.
$$
The boundary conditions give $C+D=0$ and $C+D(p/q)^N=1$, yielding the formula. Since absorption occurs at one of the two endpoints with probability $1$ on this finite interval, $\alpha=1-\beta$.

:::

:::

::: {.pf-step #s1-3}

If $p=q=1/2$, then
$$
\boxed{\beta(x)=\frac{x-A}{B-A}},
\qquad
\boxed{\alpha(x)=\frac{B-x}{B-A}}.
$$


::: pf-proof

The recurrence becomes $2\beta(x)=\beta(x-1)+\beta(x+1)$, so the second finite difference vanishes and $\beta$ is affine in $x$. The endpoint values determine the displayed linear function; $\alpha=1-\beta$.

:::

:::

::: {.pf-step #s1-4}

The mean absorption time satisfies
$$
m(x)=1+pm(x-1)+qm(x+1),
\qquad
m(A)=m(B)=0.
$$


::: pf-proof

From an interior point, one step is spent immediately and the expected remaining duration is the probability-weighted mean from the new position. At either absorbing endpoint no further steps are required.

:::

:::

::: {.pf-step #s1-5}

If $p\ne q$, then
$$
\boxed{
m(x)=
\frac{x-A}{p-q}
-\frac{B-A}{p-q}
\frac{(p/q)^{x-A}-1}{(p/q)^{B-A}-1}.}
$$


::: pf-proof

A particular solution of step [](#s1-4){.pf-ref} is $(x-A)/(p-q)$, because substituting a linear function $cx$ into
$$
m-pm(x-1)-qm(x+1)=1
$$
gives $c(p-q)=1$. The homogeneous solutions are $1$ and $(p/q)^{x-A}$ as in step [](#s1-2){.pf-ref}. Thus
$$
m(x)=\frac{x-A}{p-q}+C+D(p/q)^{x-A}.
$$
Imposing $m(A)=m(B)=0$ and solving for $C,D$ gives the displayed formula.

:::

:::

::: {.pf-step #s1-6}

If $p=q=1/2$, then
$$
\boxed{m(x)=(x-A)(B-x)}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} becomes
$$
m(x+1)-2m(x)+m(x-1)=-2.
$$
Hence $m$ is a quadratic polynomial with leading coefficient $-1$. The zeros at $A$ and $B$ therefore force $m(x)=(x-A)(B-x)$.

:::

:::

::: {.pf-step #s1-7}

In particular, if $A=-B$, $x=0$, and $p=q=1/2$, then
$$
\boxed{m(0)=B^2}.
$$


::: pf-proof

Substitute $A=-B$ and $x=0$ into step [](#s1-6){.pf-ref}:
$$
m(0)=(0+B)(B-0)=B^2.
$$

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} give the absorption probabilities, and steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref} give the mean absorption time and the requested symmetric check.

:::

:::

:::
