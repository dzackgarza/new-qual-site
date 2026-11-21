---
schema: qual/card@1
id: P-BKF09-1B
kind: problem
title: Convergence of the improper integral $\int_1^\infty x^2\cos(x^\beta)\,dx$
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Fall 2009
    solutions, Problem 1B, PDF p. 5, the file named in the collection's provenance), which the
    body now cites; the card previously carried no citation. The case 0 < beta <= 3 is where
    the card adds to the sheet: the sheet asserts that the differences
    $I((2\pi k+\pi/2)^{1/\beta})-I((2\pi k-\pi/2)^{1/\beta})$ do not tend to 0, and the card
    proves it by the substitution $u=x^\beta$, giving $u^{3/\beta-1}\ge1$ and $\int\cos u\,du=2$
    on each half-period, so the difference is at least $2/\beta$ for every $k$. The
    integration by parts is written out with both terms, and the divergence for $\beta\le0$
    is bounded below by $x^2\cos1$. The answer $\beta>3$ is unchanged.
---

::: {.problem}
Find the real values of $\beta$ for which the following limit exists and is finite:
$$
\lim_{R\to\infty}\int_1^R x^2\cos(x^\beta)\,dx.
$$
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Fall 2009 preliminary examination solutions, Problem 1B** (`assets/attachments/f09solutions.pdf`, the file named in this collection's `provenance`): the split into $\beta\le0$, $0<\beta\le3$ and $\beta>3$, the substitution $u=x^\beta$, and the integration by parts are that solution's. The card adds the estimate that shows the oscillations do not cancel when $0<\beta\le3$, which the sheet states without proof.

Throughout $\beta$ is real and
$$
I(R)\coloneqq\int_1^R x^2\cos(x^\beta)\,dx,\qquad R>1 .
$$

::: pf

::: {.pf-step #nonpositive}
For $\beta\le0$ the integral diverges: $I(R)\to+\infty$.

::: pf-proof
For $x\ge1$ and $\beta\le0$ we have $x^\beta\in(0,1]$, so $\cos(x^\beta)\ge\cos 1>0$ and $x^2\cos(x^\beta)\ge x^2\cos 1$. Hence $I(R)\ge\cos 1\cdot(R^3-1)/3\to\infty$.

:::

:::

::: {.pf-step #substitution}
For $\beta>0$, with $u=x^\beta$,
$$
I(R)=\frac1\beta\int_1^{R^\beta}u^{3/\beta-1}\cos u\,du .
$$

::: pf-proof
$u=x^\beta$ is a $C^1$ bijection of $[1,R]$ onto $[1,R^\beta]$ with $du=\beta x^{\beta-1}dx$, so $dx=\beta^{-1}u^{1/\beta-1}du$ and $x^2dx=\beta^{-1}u^{3/\beta-1}du$.

:::

:::

::: {.pf-step #oscillation}
For $0<\beta\le3$ the limit does not exist.

::: pf-proof
For $k\ge1$ put $b_k=(2\pi k-\pi/2)^{1/\beta}$ and $a_k=(2\pi k+\pi/2)^{1/\beta}$, so that $b_k<a_k$ and both tend to $\infty$. By step [](#substitution){.pf-ref},
$$
I(a_k)-I(b_k)=\frac1\beta\int_{2\pi k-\pi/2}^{2\pi k+\pi/2}u^{3/\beta-1}\cos u\,du .
$$
On that interval $\cos u\ge0$ and $\int\cos u\,du=2$; since $3/\beta-1\ge0$ and $u\ge2\pi k-\pi/2\ge3\pi/2>1$ there, $u^{3/\beta-1}\ge1$. Hence $I(a_k)-I(b_k)\ge 2/\beta>0$ for every $k$. A convergent sequence would have $I(a_k)-I(b_k)\to0$, so $I(R)$ does not converge.

:::

:::

::: {.pf-step #large}
For $\beta>3$ the limit exists and is finite.

::: pf-proof
Integrating by parts in step [](#substitution){.pf-ref},
$$
I(R)=\frac1\beta\Bigl[R^{3-\beta}\sin(R^\beta)-\sin 1\Bigr]-\frac{3-\beta}{\beta}\int_1^R x^{2-\beta}\sin(x^\beta)\,dx .
$$
The first bracket tends to $-\sin1$, because $3-\beta<0$ makes $R^{3-\beta}\to0$ and $\sin$ is bounded. The integral converges absolutely, because $\abs{\sin(x^\beta)}\le1$ and $\int_1^\infty x^{2-\beta}dx$ converges when $2-\beta<-1$, that is $\beta>3$. A sum of two convergent terms converges.

:::

:::

::: {.pf-step #conclusion}
The limit exists and is finite exactly for $\beta>3$.

::: pf-proof
Step [](#nonpositive){.pf-ref} disposes of $\beta\le0$, step [](#oscillation){.pf-ref} of $0<\beta\le3$, and step [](#large){.pf-ref} gives convergence for $\beta>3$. The three cases exhaust the real line.

:::

:::

:::
:::
